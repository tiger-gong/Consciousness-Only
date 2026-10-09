# Graph: one language at a time / 图谱：按语种看

Each lecture file carries four language chains, and glossary notes cross-link at the bottom. The **global graph** therefore looks like a four-color tangle. That is expected, not a bug. Filter with the search box at the top left of Graph view: keep one language (and the lectures, if you want).

Open Graph view from the left ribbon, or `⌘G` if you have set the shortcut.

讲记每个文件里同时挂了中英法越四条链，词条末尾又互相「其他语言」对链，所以**全局图谱**会变成一团四色毛线。这不是坏了，是四语同页造成的。要看清，用图谱左上角的**搜索框**做过滤。

## Start here (Chinese terms + lectures) / 先试这一条

Paste the whole line into the graph search box and press Enter:

```
-path:Glossary/English -path:Glossary/Français -path:Glossary/TiếngViệt
```

English, French, and Vietnamese notes hide. What remains: Chinese notes, the twenty-two lectures, and the Readers Guide.

本库已把这条设成图谱的默认搜索。若你改过搜索框，再贴一次即可。

## Four subgraphs / 四种子图（复制即用）

**Terms only** (sparse: notes rarely link sideways):

```
path:Glossary/Chinese
```

```
path:Glossary/English
```

```
path:Glossary/Français
```

```
path:Glossary/TiếngViệt
```

**That language + lectures** (shows which lecture uses which term):

```
-path:Glossary/English -path:Glossary/Français -path:Glossary/TiếngViệt
```

```
-path:Glossary/Chinese -path:Glossary/Français -path:Glossary/TiếngViệt
```

```
-path:Glossary/Chinese -path:Glossary/English -path:Glossary/TiếngViệt
```

```
-path:Glossary/Chinese -path:Glossary/English -path:Glossary/Français
```

Clear the search box to return to the full four-language graph.

## Colors / 颜色

Local graph settings color folders: Chinese / English / Français / TiếngViệt. After a filter you mostly see one color.

## Local graph / 局部图谱

Open one note → right-click **Open local graph**. Depth 1 or 2. That shows only what this term touches.

## Why not four separate vaults / 为什么不拆成四个库

Lectures keep all four languages **on the same page**. Obsidian’s graph uses one node per file, so one lecture fans out in four languages. Filtering is the way to read the map without splitting the book.
