#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Build the full parallel EPUB (lectures 1–22) plus four-language glossaries."""
from __future__ import annotations

import hashlib
import html
import os
import re
import uuid
import zipfile
from datetime import datetime, timezone

VAULT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
LECTURE_DIR = os.path.join(VAULT, 'Hundred Dharmas')
GLOSS = os.path.join(VAULT, 'Glossary')
OUT_EPUB = os.path.join(LECTURE_DIR, '100 Dharmas.epub')
OLD_VOL1 = os.path.join(LECTURE_DIR, '100 Dharmas Volume 1.epub')

FILES = [f'Hundred Dharmas NO.{i}.md' for i in range(1, 23)]
LANG_LABEL = {'zh': 'Chinese', 'en': 'English', 'fr': 'Français', 'vi': 'Tiếng Việt'}
FOLDER = {'zh': 'Chinese', 'en': 'English', 'fr': 'Français', 'vi': 'TiếngViệt'}
FOLDER_TO_LANG = {v: k for k, v in FOLDER.items()}

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
    11: ('第十一講', 'Lecture Eleven', 'Onzième conférence', 'Bài giảng thứ mười một'),
    12: ('第十二講', 'Lecture Twelve', 'Douzième conférence', 'Bài giảng thứ mười hai'),
    13: ('第十三講', 'Lecture Thirteen', 'Treizième conférence', 'Bài giảng thứ mười ba'),
    14: ('第十四講', 'Lecture Fourteen', 'Quatorzième conférence', 'Bài giảng thứ mười bốn'),
    15: ('第十五講', 'Lecture Fifteen', 'Quinzième conférence', 'Bài giảng thứ mười lăm'),
    16: ('第十六講', 'Lecture Sixteen', 'Seizième conférence', 'Bài giảng thứ mười sáu'),
    17: ('第十七講', 'Lecture Seventeen', 'Dix-septième conférence', 'Bài giảng thứ mười bảy'),
    18: ('第十八講', 'Lecture Eighteen', 'Dix-huitième conférence', 'Bài giảng thứ mười tám'),
    19: ('第十九講', 'Lecture Nineteen', 'Dix-neuvième conférence', 'Bài giảng thứ mười chín'),
    20: ('第二十講', 'Lecture Twenty', 'Vingtième conférence', 'Bài giảng thứ hai mươi'),
    21: ('第二十一講', 'Lecture Twenty-one', 'Vingt-et-unième conférence', 'Bài giảng thứ hai mươi mốt'),
    22: ('第二十二講', 'Lecture Twenty-two', 'Vingt-deuxième conférence', 'Bài giảng thứ hai mươi hai'),
}

GLOSS_APPEND = [
    ('zh', '名相表 · 中文',
     '講記正文出現的佛學名相，依中文排序。釋義取詞典首句。'),
    ('en', 'Glossary · English',
     'Buddhist terms appearing in the lectures, sorted in English. Definitions are the first sentence of the glossary entry.'),
    ('fr', 'Glossaire · Français',
     'Termes bouddhiques figurant dans les conférences, classés en français. Définitions : première phrase de la notice.'),
    ('vi', 'Bảng thuật ngữ · Tiếng Việt',
     'Thuật ngữ Phật học xuất hiện trong các bài giảng, xếp theo tiếng Việt. Định nghĩa lấy câu đầu của mục từ.'),
]

WIKI_RE = re.compile(r'\[\[Glossary/([^\]|]+)\|([^\]]+)\]\]')
SEC_RE = re.compile(
    r'\*\*§(\d+)\*\*\s*\n'
    r'\*\*中文\*\*\s*\n(.*?)'
    r'\n\*\*English\*\*\s*\n(.*?)'
    r'\n\*\*Français\*\*\s*\n(.*?)'
    r'\n\*\*Tiếng Việt\*\*\s*\n(.*?)'
    r'(?=\n---|\n\*\*§|\Z)',
    re.S,
)


def note_id(rel: str) -> str:
    """Apple Books only follows ASCII fragment ids; CJK/accents in href=#… silently fail."""
    return 'n-' + hashlib.sha1(rel.encode('utf-8')).hexdigest()[:16]


def strip_wiki(text: str) -> str:
    return WIKI_RE.sub(lambda m: m.group(2), text)


def extract_note(rel_path: str) -> tuple[str, str]:
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


def first_sentence(defn: str, limit: int = 220) -> str:
    if not defn:
        return ''
    parts = re.split(r'(?<=[。．！？.!?])\s+', defn, maxsplit=1)
    s = parts[0].strip()
    if len(s) > limit:
        s = s[:limit].rstrip() + '…'
    return s


def parse_lecture(path: str) -> list[dict]:
    text = open(path, encoding='utf-8').read()
    blocks = []
    for m in SEC_RE.finditer(text):
        blocks.append({
            'global': int(m.group(1)),
            'zh': m.group(2).strip(),
            'en': m.group(3).strip(),
            'fr': m.group(4).strip(),
            'vi': m.group(5).strip(),
        })
    return blocks


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
.gloss { margin: 0.8em 0 0; }
.gloss dt {
  font-weight: 700;
  margin: 0.95em 0 0.15em;
  color: #3a2a1a;
}
.gloss dd { margin: 0 0 0.2em; text-align: justify; color: #333; }
.gloss .sk { font-weight: 400; font-style: italic; color: #666; }
"""

COVER_SVG = """<?xml version="1.0" encoding="UTF-8"?>
<svg xmlns="http://www.w3.org/2000/svg" width="1600" height="2560" viewBox="0 0 1600 2560">
  <rect width="1600" height="2560" fill="#2c241c"/>
  <rect x="70" y="70" width="1460" height="2420" fill="none" stroke="#c4b49a" stroke-width="3"/>
  <rect x="100" y="100" width="1400" height="2360" fill="none" stroke="#c4b49a" stroke-width="1"/>
  <text x="800" y="780" text-anchor="middle" fill="#f3eadc"
        font-family="Georgia, Times, serif" font-size="72" letter-spacing="8">100 DHARMAS</text>
  <line x1="520" y1="880" x2="1080" y2="880" stroke="#c4b49a" stroke-width="1"/>
  <text x="800" y="1040" text-anchor="middle" fill="#f3eadc"
        font-family="Songti SC, STSong, serif" font-size="48">大乘百法明門論 · 直解</text>
  <text x="800" y="1140" text-anchor="middle" fill="#c4b49a"
        font-family="Georgia, Times, serif" font-size="28">Lectures 1–22  ·  第一講至第二十二講</text>
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


def link_terms(text: str, used: dict, collected: dict) -> str:
    out = []
    last = 0
    for m in WIKI_RE.finditer(text):
        out.append(html.escape(text[last:m.start()]))
        rel, display = m.group(1), m.group(2)
        folder, _, title = rel.partition('/')
        lang = FOLDER_TO_LANG.get(folder)
        if lang:
            collected[lang].add((rel, display))
        skt, defn = note_for(rel)
        nid = note_id(rel)
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


def build_lecture_xhtml(num: int, blocks: list[dict], collected: dict) -> tuple[str, str, str]:
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
            parts.append(f'<div class="{lang}">{link_terms(b[lang], used, collected)}</div>')
            parts.append('</div>')
        parts.append('</article>')
    parts.append(notes_html(used))
    return title, xhtml_wrap(title, '\n'.join(parts)), f'§{first}–§{last}'


def sort_key(lang: str, display: str) -> tuple:
    if lang == 'zh':
        return (display,)
    return (display.casefold(), display)


def build_glossary_xhtml(lang: str, title: str, blurb: str, items: set[tuple[str, str]]) -> str:
    rows = []
    seen = set()
    for rel, display in items:
        if rel in seen:
            continue
        seen.add(rel)
        skt, defn = note_for(rel)
        rows.append((display, skt, first_sentence(defn), rel))
    rows.sort(key=lambda r: sort_key(lang, r[0]))
    parts = [
        f'<h1>{html.escape(title)}</h1>',
        f'<p class="toc-range">{html.escape(blurb)} {len(rows)} entries.</p>',
        '<dl class="gloss">',
    ]
    for display, skt, brief, _rel in rows:
        sk = f' <span class="sk">({html.escape(skt)})</span>' if skt else ''
        parts.append(f'<dt>{html.escape(display)}{sk}</dt>')
        parts.append(f'<dd>{html.escape(brief) if brief else "—"}</dd>')
    parts.append('</dl>')
    return xhtml_wrap(title, '\n'.join(parts), lang)


def build_epub(lectures: list[tuple[int, list[dict]]]) -> None:
    uid = 'urn:uuid:' + str(uuid.uuid4())
    now = datetime.now(timezone.utc).strftime('%Y-%m-%dT%H:%M:%SZ')
    last_n = lectures[-1][1][-1]['global']
    collected = {k: set() for k in FOLDER}

    title_body = f"""
<div class="title-page">
  <h1>100 Dharmas</h1>
  <p class="sub">大乘百法明門論 · 直解</p>
  <p class="sub">The Treatise on the Illumination of the Hundred Dharmas</p>
  <p class="meta">天親菩薩造 · 蕅益大師注 · 淨界法師講述<br/>
  Vasubandhu · Master Ǒuyì · Master Jingjie<br/><br/>
  Lectures 1–22 · 第一講至第二十二講<br/>
  Chinese · English · Français · Tiếng Việt<br/><br/>
  Paragraphs numbered continuously as §1–§{last_n}<br/><br/>
  Dotted terms are glossary notes — tap or click to read the explanation.<br/>
  虛線名相可點按彈出釋義。<br/>
  Glossaries in Chinese, English, French, and Vietnamese follow the lectures.</p>
</div>
"""

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
        'OEBPS/title.xhtml': xhtml_wrap('100 Dharmas', title_body, 'en'),
        'OEBPS/cover.xhtml': xhtml_wrap('Cover', '''
<div class="title-page" style="margin-top:8vh">
  <p><img src="cover.svg" alt="100 Dharmas" style="width:70%; max-width:280px;"/></p>
</div>''', 'en'),
    }

    ncx_nav = []
    play = 1
    for num, blocks in lectures:
        title, xh, rng = build_lecture_xhtml(num, blocks, collected)
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
            f'<content src="{href}"/></navPoint>'
        )

    gloss_nav = []
    for lang, gtitle, blurb in GLOSS_APPEND:
        href = f'glossary-{lang}.xhtml'
        files[f'OEBPS/{href}'] = build_glossary_xhtml(lang, gtitle, blurb, collected[lang])
        eid = f'gloss-{lang}'
        manifest.append(
            f'<item id="{eid}" href="{href}" media-type="application/xhtml+xml"/>'
        )
        spine.append(f'<itemref idref="{eid}"/>')
        gloss_nav.append(f'<li><a href="{href}">{html.escape(gtitle)}</a></li>')
        play += 1
        ncx_nav.append(
            f'<navPoint id="navg-{lang}" playOrder="{play}">'
            f'<navLabel><text>{html.escape(gtitle)}</text></navLabel>'
            f'<content src="{href}"/></navPoint>'
        )

    nav = xhtml_wrap('Contents', '''
<h1>Contents · 目錄</h1>
<nav epub:type="toc" class="nav">
<ol>
<li><a href="title.xhtml">Title page</a></li>
%s
<li>Glossaries · 名相表
<ol>
%s
</ol>
</li>
</ol>
</nav>
<p class="toc-range">All paragraphs are numbered continuously (§1 onward). Glossaries follow the lectures, in Chinese → English → Français → Tiếng Việt.</p>
''' % ('\n'.join(nav_items), '\n'.join(gloss_nav)), 'en')
    files['OEBPS/nav.xhtml'] = nav

    ncx = f'''<?xml version="1.0" encoding="UTF-8"?>
<ncx xmlns="http://www.daisy.org/z3986/2005/ncx/" version="2005-1">
  <head>
    <meta name="dtb:uid" content="{uid}"/>
    <meta name="dtb:depth" content="2"/>
    <meta name="dtb:totalPageCount" content="0"/>
    <meta name="dtb:maxPageNumber" content="0"/>
  </head>
  <docTitle><text>100 Dharmas</text></docTitle>
  <navMap>
    <navPoint id="nav0" playOrder="1">
      <navLabel><text>Title</text></navLabel>
      <content src="title.xhtml"/>
    </navPoint>
    {''.join(ncx_nav)}
  </navMap>
</ncx>
'''
    files['OEBPS/toc.ncx'] = ncx

    opf = f'''<?xml version="1.0" encoding="UTF-8"?>
<package xmlns="http://www.idpf.org/2007/opf" unique-identifier="BookId" version="3.0" xml:lang="en">
  <metadata xmlns:dc="http://purl.org/dc/elements/1.1/">
    <dc:identifier id="BookId">{uid}</dc:identifier>
    <dc:title>100 Dharmas</dc:title>
    <dc:creator>Vasubandhu</dc:creator>
    <dc:creator>Master Ǒuyì</dc:creator>
    <dc:creator>Master Jingjie</dc:creator>
    <dc:language>zh</dc:language>
    <dc:language>en</dc:language>
    <dc:language>fr</dc:language>
    <dc:language>vi</dc:language>
    <dc:publisher>Hundred Dharmas parallel edition</dc:publisher>
    <dc:date>{now[:10]}</dc:date>
    <dc:description>Four-language parallel edition of Master Jingjie's lectures on the Treatise on the Hundred Dharmas (Lectures 1–22), with glossaries in Chinese, English, French, and Vietnamese.</dc:description>
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

    for lang, _t, _b in GLOSS_APPEND:
        print(f'  glossary {lang}: {len(collected[lang])} terms')


def main() -> None:
    lectures = []
    print('--- parse lectures 1–22 (no renumber) ---')
    for i, fn in enumerate(FILES, 1):
        path = os.path.join(LECTURE_DIR, fn)
        blocks = parse_lecture(path)
        if not blocks:
            raise SystemExit(f'no paragraphs parsed: {fn}')
        first, last = blocks[0]['global'], blocks[-1]['global']
        lectures.append((i, blocks))
        print(f'{fn}: {len(blocks)} paras  §{first}–§{last}')
    print('--- build epub ---')
    build_epub(lectures)
    print('wrote', OUT_EPUB, 'bytes', os.path.getsize(OUT_EPUB))
    if os.path.isfile(OLD_VOL1):
        os.remove(OLD_VOL1)
        print('deleted', OLD_VOL1)
    print('glossary files cached', len(NOTE_CACHE))


if __name__ == '__main__':
    main()
