#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Merge lectures 1–10 into continuous § numbering and build
   100 Dharmas Volume 1.epub with tap-to-popup glossary notes.
"""
from __future__ import annotations

import html
import os
import re
import uuid
import zipfile
from datetime import datetime, timezone

VAULT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
LECTURE_DIR = os.path.join(VAULT, 'Hundred Dharmas')
GLOSS = os.path.join(VAULT, '名相词典')
OUT_EPUB = os.path.join(LECTURE_DIR, '100 Dharmas Volume 1.epub')
MAP_JSON = os.path.join(VAULT, '_build', 'volume1_para_map.json')

FILES = [f'Hundred Dharmas NO.{i}.md' for i in range(1, 11)]
LANG_MARK = {
    '**中文**': 'zh',
    '**English**': 'en',
    '**Français**': 'fr',
    '**Tiếng Việt**': 'vi',
}
LANG_LABEL = {'zh': '中文', 'en': 'English', 'fr': 'Français', 'vi': 'Tiếng Việt'}
LECTURE_TITLES = {
    1: ('第一講', 'Lecture One', 'Première conférence', 'Bài giảng thứ nhất'),
    2: ('第二講', 'Lecture Two', 'Deuxième conférence', 'Bài giảng thứ hai'),
    3: ('第三講', 'Lecture Three', 'Troisième conférence', 'Bài giảng thứ ba'),
    4: ('第四講', 'Lecture Four', 'Quatrième conférence', 'Bài giảng thứ tư'),
    5: ('第五講', 'Lecture Five', 'Cinquième conférence', 'Bài giảng thứ năm'),
    6: ('第六講', 'Lecture Six', 'Sixième conférence', 'Bài giảng thứ sáu'),
    7: ('第七講', 'Lecture Seven', 'Septième conférence', 'Bài giảng thứ bảy'),
    8: ('第八講', 'Lecture Eight', 'Huitième conférence', 'Bài giảng thứ tám'),
    9: ('第九講', 'Lecture Nine', 'Neuvième conférence', 'Bài giảng thứ chín'),
    10: ('第十講', 'Lecture Ten', 'Dixième conférence', 'Bài giảng thứ mười'),
}

WIKI_RE = re.compile(r'\[\[名相词典/([^\]|]+)\|([^\]]+)\]\]')
SEC_RE = re.compile(
    r'\*\*§(\d+)\*\*\s*\n'
    r'\*\*中文\*\*\s*\n(.*?)'
    r'\n\*\*English\*\*\s*\n(.*?)'
    r'\n\*\*Français\*\*\s*\n(.*?)'
    r'\n\*\*Tiếng Việt\*\*\s*\n(.*?)'
    r'(?=\n---|\n\*\*§|\Z)',
    re.S,
)
ILLEGAL = re.compile(r'[\\/:*?"<>|#^\[\]]')


def slug(s: str) -> str:
    s = s.strip().replace(' ', '-').replace('/', '-')
    s = re.sub(r'[^0-9A-Za-z\u00C0-\u024F\u1E00-\u1EFF\u4e00-\u9fff\-]+', '', s)
    return s[:96] or 'x'


def strip_wiki(text: str) -> str:
    return WIKI_RE.sub(lambda m: m.group(2), text)


def extract_note(rel_path: str) -> tuple[str, str]:
    """Return (sanskrit, definition) from a glossary markdown file."""
    fp = os.path.join(GLOSS, rel_path + '.md')
    if not os.path.isfile(fp):
        return '', ''
    raw = open(fp, encoding='utf-8').read()
    skt = ''
    msk = re.search(r'^sanskrit:\s*(.+)$', raw, re.M)
    if msk:
        skt = msk.group(1).strip()
    if not skt:
        msk2 = re.search(r'\*\*梵[^*]*\*\*[：:]\s*\*?([^*\n]+)\*?', raw)
        if msk2:
            skt = msk2.group(1).strip()
    body = re.sub(r'^---\n.*?\n---\n', '', raw, count=1, flags=re.S)
    m = re.search(
        r'^##\s+(释义|Explanation|Explication|Giải thích).*?\n(.*?)(?=^## |\Z)',
        body, re.S | re.M,
    )
    if not m:
        return skt, ''
    defn = strip_wiki(m.group(2)).strip()
    defn = re.sub(r'\*\*([^*]+)\*\*', r'\1', defn)
    defn = re.sub(r'\*([^*]+)\*', r'\1', defn)
    defn = re.sub(r'\n{3,}', '\n\n', defn).strip()
    return skt, defn


NOTE_CACHE: dict[str, tuple[str, str]] = {}


def note_for(rel_path: str) -> tuple[str, str]:
    if rel_path not in NOTE_CACHE:
        NOTE_CACHE[rel_path] = extract_note(rel_path)
    return NOTE_CACHE[rel_path]


def parse_lecture(path: str) -> list[dict]:
    text = open(path, encoding='utf-8').read()
    blocks = []
    for m in SEC_RE.finditer(text):
        blocks.append({
            'old': int(m.group(1)),
            'zh': m.group(2).strip(),
            'en': m.group(3).strip(),
            'fr': m.group(4).strip(),
            'vi': m.group(5).strip(),
        })
    return blocks


def renumber_markdown(path: str, start: int) -> tuple[int, int]:
    """Rewrite **§N** lines in order with global numbers starting at `start`.
    Returns (start, last) inclusive.
    """
    lines = open(path, encoding='utf-8').read().split('\n')
    n = start
    out = []
    count = 0
    for ln in lines:
        if re.fullmatch(r'\*\*§\d+\*\*', ln.strip()):
            out.append(f'**§{n}**')
            n += 1
            count += 1
        else:
            out.append(ln)
    text = '\n'.join(out)
    for a, b in (
        ('各语种共用同一段落编号 §N',
         '全书 Volume 1 连续编号 §N（四种译文共用）'),
        ('每讲内共用同一段落编号 §N',
         '全书 Volume 1 连续编号 §N'),
        ('每講內共用同一段落編號 §N',
         '全書 Volume 1 連續編號 §N'),
        ('每段均标有编号 §N，四种译文共用同一编号',
         '段落编号与《100 Dharmas Volume 1》全书连续编号一致（§1 起），四种译文共用同一编号'),
        ('Each paragraph carries a number (§N) shared by all four translations.',
         'Each paragraph carries a number (§N) shared by all four translations and continuous across Volume 1.'),
        ('Chaque paragraphe porte un numéro (§N) commun aux quatre traductions.',
         'Chaque paragraphe porte un numéro (§N) commun aux quatre traductions et continu tout au long du Volume 1.'),
        ('Mỗi đoạn đều mang một số hiệu (§N) dùng chung cho cả bốn bản dịch',
         'Mỗi đoạn đều mang một số hiệu (§N) dùng chung cho cả bốn bản dịch, liên tục xuyên suốt Volume 1'),
    ):
        text = text.replace(a, b)
    open(path, 'w', encoding='utf-8').write(text)
    last = start + count - 1 if count else start - 1
    return start, last


CSS = """@charset "UTF-8";
@namespace epub "http://www.idpf.org/2007/ops";
html { font-size: 100%; }
body {
  margin: 0.9em 1.1em 2em;
  line-height: 1.62;
  font-family: "Source Han Serif SC", "Noto Serif CJK SC", "Songti SC",
               "Palatino Linotype", Palatino, serif;
  color: #1a1a1a;
}
h1 { font-size: 1.45em; text-align: center; margin: 1.4em 0 0.4em; font-weight: 600; }
h2 { font-size: 1.15em; margin: 1.6em 0 0.6em; font-weight: 600; }
.title-page { text-align: center; margin-top: 18vh; }
.title-page h1 { font-size: 2em; letter-spacing: 0.06em; margin-bottom: 0.2em; }
.title-page .vol { font-size: 1.15em; letter-spacing: 0.18em; color: #5a4632; margin: 0.4em 0 1.4em; }
.title-page .sub { font-size: 1.05em; margin: 0.3em 0; }
.title-page .meta { margin-top: 2.2em; font-size: 0.95em; color: #444; line-height: 1.8; }
.nav a { text-decoration: none; color: #3a2a1a; }
.nav li { margin: 0.35em 0; }
.entry {
  margin: 0 0 1.35em;
  padding: 0 0 1.05em;
  border-bottom: 1px solid #d9d0c4;
}
.pn {
  font-weight: 700;
  letter-spacing: 0.04em;
  margin: 0 0 0.45em;
  color: #5a4632;
}
.block { margin: 0.25em 0 0.7em; }
.lbl {
  display: block;
  font-size: 0.72em;
  font-weight: 700;
  letter-spacing: 0.1em;
  text-transform: uppercase;
  color: #7a6a58;
  margin: 0 0 0.15em;
}
.zh, .en, .fr, .vi { text-align: justify; }
a.term {
  color: inherit;
  text-decoration: none;
  border-bottom: 1px dotted #8b5e34;
  -webkit-text-fill-color: inherit;
}
a.term:active, a.term:hover { background: #f3eadc; }
aside[epub|type~="footnote"] {
  margin: 0.7em 0 1em;
  padding: 0.55em 0.7em;
  background: #f7f1e7;
  border-left: 3px solid #8b5e34;
}
.notes { margin-top: 2.2em; padding-top: 0.6em; border-top: 2px solid #c4b49a; }
.notes h2 { text-align: left; }
aside.note {
  margin: 0.7em 0 1em;
  padding: 0.55em 0.7em;
  background: #f7f1e7;
  border-left: 3px solid #8b5e34;
}
aside.note .nt { font-weight: 700; }
aside.note .sk { font-style: italic; color: #555; }
.toc-range { color: #666; font-size: 0.9em; }
"""

COVER_SVG = """<?xml version="1.0" encoding="UTF-8"?>
<svg xmlns="http://www.w3.org/2000/svg" width="1600" height="2560" viewBox="0 0 1600 2560">
  <rect width="1600" height="2560" fill="#2c241c"/>
  <rect x="70" y="70" width="1460" height="2420" fill="none" stroke="#c4b49a" stroke-width="3"/>
  <rect x="100" y="100" width="1400" height="2360" fill="none" stroke="#c4b49a" stroke-width="1"/>
  <text x="800" y="780" text-anchor="middle" fill="#f3eadc"
        font-family="Georgia, Times, serif" font-size="72" letter-spacing="8">100 DHARMAS</text>
  <text x="800" y="900" text-anchor="middle" fill="#c4b49a"
        font-family="Georgia, Times, serif" font-size="42" letter-spacing="14">VOLUME 1</text>
  <line x1="520" y1="980" x2="1080" y2="980" stroke="#c4b49a" stroke-width="1"/>
  <text x="800" y="1120" text-anchor="middle" fill="#f3eadc"
        font-family="Songti SC, STSong, serif" font-size="48">大乘百法明門論 · 直解</text>
  <text x="800" y="1220" text-anchor="middle" fill="#c4b49a"
        font-family="Georgia, Times, serif" font-size="28">Lectures 1–10  ·  第一講至第十講</text>
  <text x="800" y="2100" text-anchor="middle" fill="#c4b49a"
        font-family="Georgia, Times, serif" font-size="26">Vasubandhu  ·  Master Ǒuyì  ·  Master Jingjie</text>
  <text x="800" y="2180" text-anchor="middle" fill="#a09078"
        font-family="Georgia, Times, serif" font-size="22">Chinese · English · Français · Tiếng Việt</text>
</svg>
"""


def xhtml_wrap(title: str, body: str, lang: str = 'zh') -> str:
    return (
        '<?xml version="1.0" encoding="UTF-8"?>\n'
        '<!DOCTYPE html>\n'
        '<html xmlns="http://www.w3.org/1999/xhtml" '
        'xmlns:epub="http://www.idpf.org/2007/ops" xml:lang="%s" lang="%s">\n'
        '<head><meta charset="utf-8"/>'
        '<title>%s</title>'
        '<link rel="stylesheet" type="text/css" href="style.css"/>'
        '</head>\n<body>\n%s\n</body>\n</html>\n'
    ) % (lang, lang, html.escape(title), body)


def text_to_html_paras(text: str) -> str:
    parts = []
    for chunk in text.split('\n'):
        if chunk.strip() == '':
            parts.append('<br/>')
        else:
            parts.append(html.escape(chunk))
    # keep original newlines as <br/>
    inner = '<br/>\n'.join(p if p != '<br/>' else '' for p in parts)
    inner = re.sub(r'(<br/>\n){2,}', '</p><p>', inner)
    inner = inner.replace('<br/>\n', '<br/>\n')
    return '<p>' + inner + '</p>'


def link_terms(text: str, lang: str, used: dict) -> str:
    """Escape text and wrap wiki terms as EPUB noterefs. `used` maps id -> (display, skt, def, lang)."""
    out = []
    last = 0
    for m in WIKI_RE.finditer(text):
        out.append(html.escape(text[last:m.start()]))
        rel, display = m.group(1), m.group(2)
        skt, defn = note_for(rel)
        nid = 'n-' + slug(rel)
        if nid not in used:
            used[nid] = (display, skt, defn, rel)
        title_attr = html.escape((defn or display)[:180].replace('\n', ' '), quote=True)
        out.append(
            f'<a class="term" epub:type="noteref" role="doc-noteref" '
            f'href="#{html.escape(nid)}" title="{title_attr}">'
            f'{html.escape(display)}</a>'
        )
        last = m.end()
    out.append(html.escape(text[last:]))
    # newlines
    s = ''.join(out).replace('\n', '<br/>\n')
    return '<p>' + s + '</p>'


def notes_html(used: dict) -> str:
    if not used:
        return ''
    chunks = ['<section class="notes" epub:type="footnotes">',
              '<h2>Notes · 注釋 · Notes · Chú thích</h2>']
    for nid, (display, skt, defn, rel) in used.items():
        body = html.escape(defn) if defn else html.escape(display)
        body = body.replace('\n', '<br/>\n')
        sk = f' <span class="sk">({html.escape(skt)})</span>' if skt else ''
        chunks.append(
            f'<aside class="note" id="{html.escape(nid)}" epub:type="footnote" role="doc-footnote">'
            f'<p><span class="nt">{html.escape(display)}</span>{sk}</p>'
            f'<p>{body}</p></aside>'
        )
    chunks.append('</section>')
    return '\n'.join(chunks)


def build_lecture_xhtml(num: int, blocks: list[dict]) -> tuple[str, str, str]:
    zh_t, en_t, fr_t, vi_t = LECTURE_TITLES[num]
    first, last = blocks[0]['global'], blocks[-1]['global']
    title = f'{en_t}  ·  {zh_t}'
    used: dict = {}
    parts = [
        f'<h1 id="lec{num}">{html.escape(title)}</h1>',
        f'<p class="toc-range">§{first} – §{last}</p>',
    ]
    for b in blocks:
        parts.append(f'<article class="entry" id="p{b["global"]}">')
        parts.append(f'<div class="pn">§{b["global"]}</div>')
        for lang in ('zh', 'en', 'fr', 'vi'):
            parts.append('<div class="block">')
            parts.append(f'<span class="lbl">{LANG_LABEL[lang]}</span>')
            parts.append(f'<div class="{lang}">{link_terms(b[lang], lang, used)}</div>')
            parts.append('</div>')
        parts.append('</article>')
    parts.append(notes_html(used))
    return title, xhtml_wrap(title, '\n'.join(parts)), f'§{first}–§{last}'


def build_epub(lectures: list[tuple[int, list[dict]]]) -> None:
    uid = 'urn:uuid:' + str(uuid.uuid4())
    now = datetime.now(timezone.utc).strftime('%Y-%m-%dT%H:%M:%SZ')

    title_body = """
<div class="title-page">
  <h1>100 Dharmas</h1>
  <p class="vol">VOLUME 1</p>
  <p class="sub">大乘百法明門論 · 直解</p>
  <p class="sub">The Treatise on the Illumination of the Hundred Dharmas</p>
  <p class="meta">天親菩薩造 · 蕅益大師注 · 淨界法師講述<br/>
  Vasubandhu · Master Ǒuyì · Master Jingjie<br/><br/>
  Lectures 1–10 · 第一講至第十講<br/>
  Chinese · English · Français · Tiếng Việt<br/><br/>
  Paragraphs numbered continuously as §1–§{last}<br/><br/>
  Dotted terms are glossary notes — tap or click to read the explanation.<br/>
  虚线名相可点按弹出释义。</p>
</div>
""".format(last=lectures[-1][1][-1]['global'])

    nav_items = []
    spine = []
    manifest = [
        '<item id="css" href="style.css" media-type="text/css"/>',
        '<item id="nav" href="nav.xhtml" media-type="application/xhtml+xml" properties="nav"/>',
        '<item id="title" href="title.xhtml" media-type="application/xhtml+xml"/>',
        '<item id="cover-svg" href="cover.svg" media-type="image/svg+xml" properties="cover-image"/>',
        '<item id="cover-page" href="cover.xhtml" media-type="application/xhtml+xml"/>',
        '<item id="ncx" href="toc.ncx" media-type="application/x-dtbncx+xml"/>',
    ]
    files = {
        'OEBPS/style.css': CSS,
        'OEBPS/cover.svg': COVER_SVG,
        'OEBPS/title.xhtml': xhtml_wrap('100 Dharmas Volume 1', title_body, 'en'),
        'OEBPS/cover.xhtml': xhtml_wrap('Cover', '''
<div class="title-page" style="margin-top:8vh">
  <p><img src="cover.svg" alt="100 Dharmas Volume 1" style="width:70%; max-width:280px;"/></p>
</div>''', 'en'),
    }

    ncx_nav = []
    play = 1
    for num, blocks in lectures:
        title, xh, rng = build_lecture_xhtml(num, blocks)
        href = f'lecture-{num:02d}.xhtml'
        files[f'OEBPS/{href}'] = xh
        eid = f'lec{num}'
        manifest.append(
            f'<item id="{eid}" href="{href}" media-type="application/xhtml+xml"/>'
        )
        spine.append(f'<itemref idref="{eid}"/>')
        zh_t, en_t, fr_t, vi_t = LECTURE_TITLES[num]
        label = f'{en_t} / {zh_t} ({rng})'
        nav_items.append(f'<li><a href="{href}">{html.escape(label)}</a></li>')
        play += 1
        ncx_nav.append(
            f'<navPoint id="nav{num}" playOrder="{play}">'
            f'<navLabel><text>{html.escape(label)}</text></navLabel>'
            f'<content src="OEBPS/{href}"/></navPoint>'
        )

    nav = xhtml_wrap('Contents', '''
<h1>Contents · 目錄</h1>
<nav epub:type="toc" class="nav">
<ol>
<li><a href="title.xhtml">Title page</a></li>
%s
</ol>
</nav>
<p class="toc-range">All paragraphs are numbered continuously across this volume (§1 onward).</p>
''' % '\n'.join(nav_items), 'en')
    files['OEBPS/nav.xhtml'] = nav

    ncx = f'''<?xml version="1.0" encoding="UTF-8"?>
<ncx xmlns="http://www.daisy.org/z3986/2005/ncx/" version="2005-1">
  <head>
    <meta name="dtb:uid" content="{uid}"/>
    <meta name="dtb:depth" content="1"/>
    <meta name="dtb:totalPageCount" content="0"/>
    <meta name="dtb:maxPageNumber" content="0"/>
  </head>
  <docTitle><text>100 Dharmas Volume 1</text></docTitle>
  <navMap>
    <navPoint id="nav0" playOrder="1">
      <navLabel><text>Title</text></navLabel>
      <content src="OEBPS/title.xhtml"/>
    </navPoint>
    {''.join(ncx_nav)}
  </navMap>
</ncx>
'''
    files['OEBPS/toc.ncx'] = ncx  # ncx content src is relative to ncx file location if in OEBPS
    # Fix NCX: file is OEBPS/toc.ncx so src should be title.xhtml not OEBPS/title.xhtml
    ncx = ncx.replace('src="OEBPS/', 'src="')
    files['OEBPS/toc.ncx'] = ncx

    opf = f'''<?xml version="1.0" encoding="UTF-8"?>
<package xmlns="http://www.idpf.org/2007/opf" unique-identifier="BookId" version="3.0" xml:lang="en">
  <metadata xmlns:dc="http://purl.org/dc/elements/1.1/">
    <dc:identifier id="BookId">{uid}</dc:identifier>
    <dc:title>100 Dharmas Volume 1</dc:title>
    <dc:creator>Vasubandhu</dc:creator>
    <dc:creator>Master Ǒuyì</dc:creator>
    <dc:creator>Master Jingjie</dc:creator>
    <dc:language>zh</dc:language>
    <dc:language>en</dc:language>
    <dc:language>fr</dc:language>
    <dc:language>vi</dc:language>
    <dc:publisher>Hundred Dharmas parallel edition</dc:publisher>
    <dc:date>{now[:10]}</dc:date>
    <dc:description>Five-language parallel edition of Master Jingjie's lectures on the Treatise on the Hundred Dharmas, Volume 1 (Lectures 1–10). Tap a dotted term to see its glossary note.</dc:description>
    <meta property="dcterms:modified">{now}</meta>
    <meta name="cover" content="cover-svg"/>
  </metadata>
  <manifest>
    {chr(10).join('    ' + x for x in manifest)}
  </manifest>
  <spine toc="ncx">
    <itemref idref="cover-page"/>
    <itemref idref="title"/>
    <itemref idref="nav"/>
    {chr(10).join('    ' + x for x in spine)}
  </spine>
  <guide>
    <reference type="cover" title="Cover" href="cover.xhtml"/>
    <reference type="toc" title="Contents" href="nav.xhtml"/>
  </guide>
</package>
'''
    files['OEBPS/content.opf'] = opf
    files['META-INF/container.xml'] = '''<?xml version="1.0" encoding="UTF-8"?>
<container version="1.0" xmlns="urn:oasis:names:tc:opendocument:xmlns:container">
  <rootfiles>
    <rootfile full-path="OEBPS/content.opf" media-type="application/oebps-package+xml"/>
  </rootfiles>
</container>
'''

    os.makedirs(os.path.dirname(OUT_EPUB), exist_ok=True)
    if os.path.exists(OUT_EPUB):
        os.remove(OUT_EPUB)
    with zipfile.ZipFile(OUT_EPUB, 'w') as z:
        z.writestr('mimetype', 'application/epub+zip', compress_type=zipfile.ZIP_STORED)
        for name, content in files.items():
            z.writestr(name, content.encode('utf-8'), compress_type=zipfile.ZIP_DEFLATED)


def main():
    import json
    mapping = []
    lectures = []
    global_n = 1
    print('--- renumber markdown ---')
    for i, fn in enumerate(FILES, 1):
        path = os.path.join(LECTURE_DIR, fn)
        blocks = parse_lecture(path)
        if not blocks:
            raise SystemExit(f'no paragraphs parsed: {fn}')
        start, last = renumber_markdown(path, global_n)
        # re-parse after rewrite so texts stay, numbers update
        blocks2 = parse_lecture(path)
        if len(blocks2) != len(blocks):
            raise SystemExit(f'parse count changed after renumber: {fn} {len(blocks)} -> {len(blocks2)}')
        for b in blocks2:
            b['global'] = b['old']  # now old IS the global number
            mapping.append({'lecture': i, 'global': b['global']})
        lectures.append((i, blocks2))
        print(f'{fn}: {len(blocks2)} paras  §{start}–§{last}')
        global_n = last + 1
    json.dump({'files': FILES, 'total': global_n - 1, 'map': mapping},
              open(MAP_JSON, 'w', encoding='utf-8'), ensure_ascii=False, indent=1)
    print('--- build epub ---')
    build_epub(lectures)
    print('wrote', OUT_EPUB, 'bytes', os.path.getsize(OUT_EPUB))
    print('paragraphs', global_n - 1, 'glossary files cached', len(NOTE_CACHE))


if __name__ == '__main__':
    main()
