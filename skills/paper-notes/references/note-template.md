# 笔记模板

Use this template for the single work note that grows from pre to companion to post. Keep the stable handoff sections even when later modules are abbreviated.

## Contents

- [Frontmatter and identity](#frontmatter-and-identity)
- [Module 1: Motivation Map](#module-1--大框架--motivation-map)
- [Stable evidence handoff](#stable-evidence-handoff)
- [Module 2: Guided Q&A](#module-2--导读问答题--我的回答)
- [Module 3: Personal judgment](#module-3--我的感悟)
- [Module 3.5: Cross-paper positioning](#module-35--横向定位--联想)
- [Module 4: Reviewer score](#module-4--reviewer-评分venue-四选一)
- [Stage rules](#取用与生命周期规则)

## Frontmatter and identity

```markdown
---
type: paper-note
producer: paper-notes
schema_version: 1
paper_id: "arxiv:YYMM.NNNNN"
reading_stage: pre
status: drafting
review_status: ai-draft
owner: ai
source: ai-draft
tags: [论文阅读, <方向>, <简称>]
related:
  - "[[相关笔记]]"
zotero_key: <key>
arxiv: <id>
doi: <doi>
venue: <已中或拟投的会>
created: YYYY-MM-DD
archive_note: ""
---

# 阅读笔记：<论文简称>

## 论文身份
- 标题 / 作者（标出一作、通讯）/ 机构 / venue / arXiv / DOI
- 性质：新架构 / 新方法 / 数据-centric / 训练范式 / 推理优化 / 综述
- 论文版本、项目页、代码与是否开源

## 一句话定位
> 解决什么问题，哪个细分方向，最强 take-home 是什么。

## 核心逻辑链（problem → method → validation）
| 环节 | 内容 | 证据（图/表/公式编号）|
|---|---|---|
| 问题 | | |
| 方法 | | |
| 验证 | | |

- Pipeline 几步？哪步自己创新、哪步借用？
```

## Module 1 · 大框架 / Motivation Map

```markdown
## 模块 1 · 大框架 / Motivation Map

> 这一节是“我能从这篇学到什么”，全是往上拿的东西，不挑毛病。

- **Motivation**：作者为什么做这件事？前人卡在哪、这篇补了哪个洞？
- **突出点**：一两个能复述给同学的记忆点。
- **创新点**：分开写问题转化、新损失、新架构、新数据视角和借用的现成件。
- **方法学习点**：值得迁移到以后研究的设计技巧。
- **Exp 学习点**：值得复用的 benchmark、对照、ablation 或定量验证设计。
```

## Stable evidence handoff

Keep these headings stable so `paper-reading-intake` can consume the post note without copying raw Q&A.

```markdown
## 关键结果与证据锚点

| Claim / Result | Value or finding | Evidence anchor | Verification state |
|---|---|---|---|
| | | Fig./Table/Section/Appendix | 已核对 / 待核对 |

## 机制辨析

### <X 是什么，不是什么>
- 容易误解的说法：
- 订正后的机制：
- 证据锚点：
- 仍不确定的地方：
```

## Module 2 · 导读问答（题 + 我的回答）

```markdown
## 模块 2 · 导读问答（题 + 我的回答）

> A 区自测 + B 区互动。保留轻量订正状态，不保存冗长批改全过程。

### A 区 · 自测问答
1. **问题** —— *我的回答*：……<br>
   *状态*：已订正 / 方向对但需补全 / 仍待确认<br>
   *锚点*：公式、图、表或章节

### B 区 · 互动点
- 隐藏假设、缺失 ablation、最近邻区别、真算法与 pipeline 装饰。
- 用户 insight 经订正和补上下文后再写入。
```

## Module 3 · 我的感悟

```markdown
## 模块 3 · 我的感悟

- 品类纠偏：对手是否在同一 league，评判轴是否正确。
- Sharp insight：比表面性能更关键的判断。
- 核心贡献判断：相对读前预判确认了什么、修正了什么。
- 对研究的用处：可复用的框架、测量法或对照系。
- 导师追问预备：迁移性、scale、复用价值和证据边界。
```

## Module 3.5 · 横向定位 + 联想

```markdown
## 模块 3.5 · 横向定位 + 联想

### 定位层 · 钉坐标
| 论文 | 问题 niche | 方法家族 + 核心假设 | 最强证据 | 主要局限 | 独特价值 |
|---|---|---|---|---|---|
| 本篇 | | | | | |
| [[最近邻A]] | | | | | |
| [[最近邻B]] | | | | | |

- 关系：互补 / 重叠 / 矛盾。

### 联想层 · 生发
- 缝合：A 的 X + B 的 Y 能否组成新方法？
- 矛盾即机会：哪对假设或结论冲突可能形成研究缺口？
- 趋势线：子方向往哪里走，下一步缺什么？
- 对我 idea 的弹药：baseline、测量法、反驳靶子。
- 错位发现：大家默认了什么，这篇又隐含了什么不同假设？
```

## Module 4 · Reviewer 评分（venue 四选一）

```markdown
## 模块 4 · Reviewer 评分 · <VENUE>

**选会理由**：<已中或最适合投该 venue 的原因>。

**Summary**：一句话说清做了什么。

**Strengths**
1. ...

**Weaknesses**
1. ...（缺哪个实验、对比或定义，以及为什么重要）

**Scores**
- <按 venue-scoring.md 的字段逐项给分>

**Recommendation**：accept / borderline / reject + 一句理由。

**换 venue 会怎样**：投另一个 venue 会因什么加分或出局。
```

## TODO / 待确认

```markdown
## TODO / 待确认
- [ ] 没读懂或没查证的细节，标清 appendix / figure / table
- [ ] 下一步可调研的方向
- [ ] intake 前仍需核对的数字或版本变化
```

## 取用与生命周期规则

- **pre**：填 identity、one-line position、logic chain、Motivation Map 和 TODO。设 `reading_stage: pre`, `status: drafting`。
- **companion**：加入 guided Q&A、关键结果锚点和机制订正。设 `reading_stage: companion`, `status: drafting`。
- **post**：补个人判断、横向定位、reviewer score 和 unresolved evidence。结构完成后设 `reading_stage: post`, `status: complete`。
- 只有用户明确复核结论后，才把 `review_status` 从 `ai-draft` 改成 `user-reviewed`。
- 同一篇从 pre 长到 post，不开新文件。
- post 后仍留在 workspace-local Obsidian；正式归档由 `paper-reading-intake` 另行生成。
- intake 完成后，在允许编辑时填 `archive_note`，但不要移动或删除工作笔记。
