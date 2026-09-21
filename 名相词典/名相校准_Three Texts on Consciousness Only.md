---
type: 校准表
source: "Three Texts on Consciousness Only, tr. Francis H. Cook, BDK English Tripitaka 60-I/II/III (Numata, 1999)"
scope: 成唯识论 / 唯识三十颂 / 唯识二十论
status: 已执行
tags:
  - 名相
  - 校准
---

# 名相校准表：对照 Cook《Three Texts on Consciousness Only》

底本为 BDK 英译大藏经 60-I/II/III，Francis H. Cook 译《成唯识论》《唯识三十颂》《唯识二十论》，共 474 页。
以下「权威」一栏均为该书正文中实际出现的措辞，附出现次数，供核查。

> **底本覆盖范围**：纯唯识学名相。四念处、净土、禅宗公案、天台、人物传记等**不在此书范围内**，这些条目无法据此校准。

## 执行结果

全面对齐已完成，三处同步：

| 项目 | 数量 |
|---|---|
| 英文词条改名 | 89 / 271 |
| 跨语链接更新 | 947 |
| 英文释义与正文用语统一 | 626 |
| 库内 English 链接 / 死链 | 3113 / **0** |
| EPUB 重建 | 658 段，XML 错误 0，内部断链 0 |

旧名一律写入各条 `aliases`，Obsidian 搜索与历史链接仍可命中。
执行脚本：`_build/authority/cook_map.py`、`apply_cook.py`、`apply_cook2.py`。

### 刻意偏离 Cook 之处

| 条目 | 保留 | 理由 |
|---|---|---|
| 大乘 / 小乘 | Great Vehicle / Lesser Vehicle | 正文体例为「义译 + 首现附梵文」，已作 Great Vehicle (*Mahāyāna*)；改用 Mahayana / Hinayana 会成「Mahayana (Mahāyāna)」重复，且 Hinayana 带贬义 |
| 善业、不善业、善根 | wholesome karma 等 | 属 善业 范畴，非「善心所」，Cook 的 good 只对应后者 |
| 念佛、正念 | mindfulness | 非别境之「念」；别境「念」已改为 memory |
| 禅定 | meditative concentration | 独立词条，与别境「定」(samādhi) 分立 |
| 果报 | karmic result | 让位给「异熟 = retribution」，避免两条同名 |

---

## 一、我们译错或不够准（建议改）

| 中文 | 我们现用 | 权威译法 | 说明 |
|---|---|---|---|
| 因缘（四缘之一） | causes and conditions | **condition as cause**（20） | 我们把四缘中的「因缘」译成了泛指的「因与缘」，失去了它作为四缘之一的专名。 |
| 想 | perception (conception) | **conceptualization**（多处） | perception 在唯识语境中通常对应「现量／了别」，用于「想」易与 pratyakṣa 混淆。 |
| 念 | mindfulness (recollection) | **memory**（45） | 别境五法之「念」是记持曾习境，非四念处之 mindfulness。 |
| 覆 / 谄 | concealment / **dissimulation** | 覆 = **dissimulation**，谄 = **hypocrisy** | 我们把 dissimulation 用在了「谄」，权威用在「覆」，同词异指，易生混淆。 |
| 惛沉 | *（词典缺条目）* | **torpor** | 大随烦恼之一，我们词典漏收。 |
| 习气 | *（词典缺条目）* | **habit energy**（36） | 与「种子」相对的关键概念，我们漏收。 |
| 心不相应行法 | *（词典缺条目）* | **forces not associated with mind** | 五位之一，我们漏收。 |

---

## 二、我们与权威不同，但两者皆可（取舍看体例）

### 基础范畴

| 中文 | 我们现用 | 权威译法（次数） |
|---|---|---|
| 心所 | mental factors | mental activities（267） |
| 烦恼 | affliction | passions（353） |
| 根本烦恼 | root afflictions | fundamental passions（6） |
| 随烦恼 | secondary afflictions | secondary passions（67） |
| 遍行 | universally active | universal（mental activities） |
| 别境 | object-specific | those with specific objects |
| 不定 | indeterminate | nondetermined / indeterminate（86） |
| 有漏 | contaminated (with outflows) | **impure**（158） |
| 无漏 | uncontaminated (without outflows) | **pure**（460） |
| 异熟 | maturation (ripened result) | **retribution**（174） |
| 现行 | present activity | activity（152） |

### 八识与四分

| 中文 | 我们现用 | 权威译法（次数） |
|---|---|---|
| 阿赖耶识 | storehouse-consciousness | store consciousness（69）／fundamental consciousness（12） |
| 末那识 | manas-consciousness | manas（184）／thought（158） |
| 眼识 | eye-consciousness | visual consciousness（44） |
| 耳识 | ear-consciousness | auditory consciousness（3） |
| 相分 | image portion | image part／seen part（42） |
| 见分 | perceiving portion | seeing part（54） |
| 自证分 | self-aware portion | self-authenticating part |
| 证自证分 | re-aware portion | the part that authenticates self-authentication |

### 三性、二障、四缘

| 中文 | 我们现用 | 权威译法（次数） |
|---|---|---|
| 遍计所执性 | imagined nature | imagined nature（21）✓ 一致 |
| 依他起性 | other-dependent nature | nature dependent on other（60） |
| 圆成实性 | perfectly accomplished nature | perfected nature（26） |
| 烦恼障 | hindrance of afflictions | obstacle of the passions（24） |
| 所知障 | hindrance to the knowable | obstacle to the knowable |
| 增上缘 | predominant condition | dominant condition（35） |
| 所缘缘 | object-as-condition | condition as perceptual object |
| 等无间缘 | immediate-antecedent condition | immediately antecedent condition（35） |

### 心所别名

| 中文 | 我们现用 | 权威译法 |
|---|---|---|
| 定 | concentration | samādhi（160） |
| 慧 | wisdom (discernment) | discernment（108） |
| 贪 / 无贪 | greed / non-greed | craving / noncraving |
| 惭 / 愧 | shame / embarrassment | conscience / sense of shame |
| 无惭 / 无愧 | shamelessness / non-embarrassment | lack of conscience / shamelessness |
| 慢 | conceit (pride) | pride |
| 精进 | diligence (vigor) | vigor |
| 轻安 | pliancy (ease) | serenity（22） |
| 不放逸 | carefulness (non-laxity) | vigilance（20） |
| 行舍 | equanimity | indifference（48） |
| 不害 | non-harming | harmlessness |
| 恨 | resentment | hostility |
| 恼 | spite (vexation) | vexation |
| 悭 | stinginess | avarice（8） |
| 诳 | deception | deceit |
| 憍 | haughtiness | vanity |
| 掉举 | restlessness | agitation（30） |
| 不信 | lack of faith | unbelief |
| 懈怠 | laziness | indolence |
| 放逸 | laxity (heedlessness) | negligence |
| 不正知 | non-introspection | incorrect knowing |
| 寻 / 伺 | initial inquiry / sustained scrutiny | applied and sustained thought (vitarka-vicāra) |

---

## 三、已经一致（无需改动）

contact（触）、feeling（受）、volition（思）、desire（欲）、attention（作意）、faith（信）、
hatred（瞋）、delusion（痴）、doubt（疑）、envy（嫉）、harmfulness（害）、
forgetfulness（失念）、distraction（散乱）、anger（忿）、regret（悔）、
seeds（种子）、perfuming（熏习）、unconditioned dharmas（无为法）、
true suchness（真如）、nirvāṇa（涅槃）、four conditions（四缘）、three natures（三性）、
attachment to a self（我执）、attachment to dharmas（法执）、mental consciousness（意识）

---

## 四、此底本无法校准的条目

以下类别在《Three Texts》中完全不出现，需另寻依据（如 PTS、BDK 其他分册、《佛光大辞典》英译）：

- **四念处相关**：观身不净、观受是苦、观心无常、观法无我（全书 "mindfulness" 仅 1 处，且非此义）
- **净土**：极乐世界、信愿持名、弥陀
- **禅宗**：百丈禅师、野狐禅、不落因果／不昧因果
- **天台、人物、地名、经论题名**：天台宗、玄奘、窥基、蕅益、迦湿弥罗国等

### 关于「观身不净」（已改）

- 原译 *contemplating the body as impure*。
- 问题不在 impure 本身不对，而在**与本底本冲突**：Cook 全书以 impure 专指「有漏」（sāsrava），158 处皆然。
- 四念处之「不净」是 *aśubha*，指身体的可厌、不美好，非「有漏／染污」。
- 已改为 **contemplating the body as unattractive (*aśubha*)**，与「有漏 = impure」区隔。
- 同段其余三念处（观受是苦、观心无常、观法无我）措辞无冲突，保留原译。

---

## 五、底本使用注意

该 PDF 为扫描 OCR（CVISION PdfCompressor），**英文正文可靠，梵文变音符号几乎全部识别错误**
（如 anātman→andtman、ālaya→älava、vijñāna→vijñcza、saṃvṛti-satya→scnnurti-satva）。
因此本表只采其**英文术语**，梵文仍以我们原有条目为准。
