# Venue 评审表（Reviewer 评分用）

只用这四个会：**CVPR / NeurIPS / ICRA / RSS**。

## 先定会，再打分（两种情况）

1. **论文已中**：直接用它中的那个会（或同级别 venue 套最近的一个）打分——还原"它当年是怎么被评上的"。
2. **没中 / preprint / 不确定**：先判断"这篇最适合投哪个会"，挑一个，再按那个会的评审表打分。判断依据 = 论文品类（CV / ML 理论 / 机器人系统）+ 有没有真机 + 贡献类型。

不同 venue 评审表不同、评判轴不同，同一篇换 venue 分数差很大——**选错 venue = 评判轴错**。所以第一步一定是"这篇该用哪个会的尺子量"，定了再量。

通用原则：每个 strength/weakness 都要落到「缺了哪个实验 / 哪个对比 / 哪个定义」。分数给完写一句"换成另一个 venue 会怎样"，让用户看到 venue 敏感性。

---

## CVPR（CV 顶会，也适用 ICCV / ECCV）

**评审表字段**：Paper Summary / Strengths / Weaknesses / Rating / Confidence / (Reproducibility)

**Rating 量表**（代表性，逐年微调）：
- 6 Strong Accept / 5 Accept / 4 Weak Accept / 3 Borderline / 2 Weak Reject / 1 Reject

**Confidence**：1（外行）– 5（很确定）

**评判重心**：
- 视觉/方法 novelty——是不是又一个 incremental tweak
- 和 SOTA 的对比是否充分、公平
- ablation 是否到位（CVPR 极看重 ablation）
- 定量结果是否扎实，可视化是否当定量证据滥用
- 可复现性（代码/数据）

**容易死在**：novelty 不够、SOTA 比较不公平、ablation 缺失。

---

## NeurIPS（ML 顶会，也适用 ICML / ICLR 精神）

**评审表字段**：Summary / Strengths & Weaknesses / Questions / Limitations / Soundness / Presentation / Contribution / Overall / Confidence

**四维 + 总分**：
- Soundness 1–4 / Presentation 1–4 / Contribution 1–4
- Overall 1–10：10 award-level，8 strong accept，6 weak accept，5 borderline accept，4 borderline reject，3 reject，1 trivial/wrong
- Confidence 1–5

**Strengths & Weaknesses 拆四面**：Originality / Quality / Clarity / Significance

**评判重心**：
- 原创性与理论贡献（理论根基是否严谨，假设是否成立）
- 实验是否支撑 claim，limitation 是否诚实披露（NeurIPS 专设 Limitations 字段，不写会扣分）
- 对社区的 significance

**容易死在**：理论与实现有缝且不诚实、limitation 回避、贡献增量小。**对"问题转化 + 理论包装"类工作相对友好。**

---

## ICRA（IEEE 机器人顶会，也适用 IROS / RA-L）

**评审表字段**：Overall Rating / Novelty / Technical Soundness / Relevance to Robotics / Clarity / (Video attachment) / Reproducibility

**Overall**：通常 definitely accept / accept / weak accept / weak reject / reject / definitely reject

**评判重心**：
- 与机器人的相关性和实际意义（纯仿真 trick 要论证落地价值）
- **真机/硬件实验**——有没有真机，real-world 是 demo 级还是正经评测
- technical soundness + 系统完整性
- 是否附 video（机器人社区很看重）

**容易死在**：没真机或真机只是几个 episode 的 demo、与机器人实际问题脱节、过度仿真。

---

## RSS（Robotics: Science and Systems，单轨极挑剔）

**评审表字段**：Summary / Significance / Novelty / Technical Soundness / Experimental Validation / Clarity / Overall

**评判重心**（比 ICRA 更狠）：
- **完整系统 + 严谨性**——RSS 偏爱端到端可用的系统和扎实的科学验证
- 长期贡献 / lasting significance，不收 incremental
- 真机验证近乎硬门槛，实验严谨性要求高
- reproducibility

**容易死在**：仿真为主、增量贡献、系统不完整、实验不够严谨。**对小修小补和纯仿真最不友好。**

---

## 输出格式（定会后照此写）

```markdown
## Reviewer 评分 · <VENUE>（日期）

**选会理由**：这篇<已中 XXX / 最适合投 VENUE>，因为<品类 + 真机 + 贡献类型>，所以用 VENUE 的尺子量。

**Summary**：一句话说清这篇做了什么。

**Strengths**
1. ...（落到具体贡献）

**Weaknesses**（按致命度排序）
1. ...（缺了哪个实验/对比/定义 + 为什么致命）

**Scores**
- <按该 venue 的字段逐项给分，如 Soundness x/4, Overall x/10, Confidence x/5>

**Recommendation**：accept / borderline / reject + 一句理由。

**换 venue 会怎样**：投 <另一个 venue> 会因 <某条> 加分/直接出局。
```
