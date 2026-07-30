# Consciousness Only

Multilingual study materials for Yogācāra / *Consciousness-Only* (*vijñaptimātra*), centered on Master Jingjie’s lectures on the *Hundred Dharmas Treatise* (*大乘百法明门论*).

## Contents

| Path | Description |
|------|-------------|
| `Hundred Dharmas/` | Lecture notes (ZH / EN / FR / VI parallel) |
| `名相词典/` | Glossary notes in Chinese, English, French, Vietnamese |
| `_build/` | Scripts and data to regenerate glossary notes |

## Collaboration

- **Read**: public repository — anyone may browse and clone.
- **Write**: work on your own branch (or a fork), then open a pull request to `main`.
- Please do not push large copyrighted binaries (PDF / EPUB / DOC) into this repo.

## Regenerating the glossary

```bash
cd _build
python3 gen_notes.py
```

Requires Python 3 and the pipeline files in `_build/` (`master.json`, `defs_i18n.json`, etc.).

## License / attribution

Lecture content follows Master Jingjie’s *直解*; glossary definitions draw on standard Yogācāra name lists. Contributors retain credit for their translations and edits.
