# Idea Discovery Report

**Direction**: 大语言模型用于光伏风电典型曲线生成
**Date**: 2026-04-15
**Pipeline**: research-lit -> idea-creator -> novelty-check -> research-review
**Mode**: non-destructive literature-driven run
**Interpretation**: 这里的“典型曲线生成”按 `representative curves / representative days / prototype profiles / typical scenario library` 理解

## Executive Summary

截至 2026 年 4 月，风电/光伏“典型曲线”这条线的主流仍然是 `聚类提取 / 代表日选择 / 场景约简 / 图聚类场景抽取`，而不是 LLM 直接生成。另一方面，`LLM + 通用时序生成` 与 `diffusion + 可控场景生成` 都已经开始成熟。两条线之间的交叉空白非常明确：

**当前几乎没有人系统研究：如何让 LLM 参与“典型曲线”的语义定义、原型生成、模式解释与库构造。**

因此，最值得做的方向不是让 LLM 直接自回归输出风光功率序列，而是：

**让 LLM 作为“典型模式编排器/原型生成器”，在聚类提取和扩散生成之间插入一个语义层，生成可解释、可控、可调用的风光典型曲线库。**

这比“纯典型日聚类”更新，也比“纯风光曲线生成”更贴近你现有项目。

## Literature Landscape

### 1. 两条已经成熟的文献线

#### A. 典型曲线/代表场景提取

这一支已经相当成熟，核心方法是聚类和代表日选择：

- *Wind and Photovoltaic Power Time Series Data Aggregation Method Based on Ensemble Clustering and Markov Chain* (CSEE JPES, 2021)
- *面向可靠性评估的两阶段聚类风-光-荷典型场景生成方法* (电工电能新技术, 2021)
- *Representative Days for Expansion Decisions in Power Systems* (Energies, 2020)
- *Improvement of Representative Days Selection in Power System Planning by Incorporating the Extreme Days of the Net Load* (Applied Energy, 2020)
- *Extraction of Representative Scenarios for Photovoltaic Power With Shared Weight Graph Clustering* (IEEE Transactions on Smart Grid, 2024)
- *A Novel Clustering Method for Extracting Representative Photovoltaic Scenarios Considering Power, Energy, and Variability* (IEEE Transactions on Power Systems, 2025)
- *Enhancing representative photovoltaic scenario extraction for multiple power stations with a shared-weight and adaptively fused graph clustering method* (Applied Energy, 2026)

#### B. 曲线/场景生成

这一支的强方法主要是 GAN 和 diffusion，而不是 LLM：

- *Conditional Style-Based Generative Adversarial Networks for Renewable Scenario Generation* (IEEE TPWRS, 2023)
- *Short-Term Wind Power Scenario Generation Based on Conditional Latent Diffusion Models* (IEEE TSTE, 2024)
- *Controllable renewable energy scenario generation based on pattern-guided diffusion models* (Applied Energy, 2025)
- *A Novel Renewable Energy Scenario Generation Method Based on Multi-Resolution Denoising Diffusion Probabilistic Models* (Energies, 2025)
- *Wind power scenario generation via multi-scale condition adaptive diffusion model* (Electric Power Systems Research, 2026)

#### C. LLM 做通用时序合成

- *Synthetic Time Series Generation for Decision Intelligence Using Large Language Models* (Mathematics, 2024)
- *Forging Time Series with Language: A Large Language Model Approach to Synthetic Data Generation* (NeurIPS 2025)

### 2. 这三条线还没有真正合并

现有文献说明了三个事实：

- 典型曲线提取已经很成熟，但大多仍是“从真实样本里选”。
- 曲线生成已经可以很强，但通常缺少“什么算典型”的语义层。
- LLM 已经能参与通用时序生成，但在风光典型曲线这个任务上几乎还没有成型范式。

所以真正的机会点不在：

- 再做一个 `K-means / DTW / 图聚类` 变体
- 再做一个 `diffusion 生成器`
- 再让 `LLM 直接输出数值曲线`

真正的机会点在于：

- `让 LLM 先定义、组织和编排典型模式`
- `再让聚类或 diffusion 去落地具体曲线`

### 3. 典型曲线任务与普通生成任务的不同

典型曲线生成不是“生成尽可能多的合理曲线”，而是“生成少量、高代表性、可解释、可复用的原型曲线”。它更强调：

- 代表性
- 覆盖性
- 可解释性
- 极端模式保留
- 库级去冗余

这恰好给了 LLM 一个天然位置：它更适合负责 `模式命名、模式组织、原型描述、模式检索与约束生成`，而不是直接承担全部数值建模。

## Ranked Ideas

### Idea 1: LLM 引导的原型条件典型曲线生成框架 - RECOMMENDED

- **核心假设**: 传统典型曲线提取只能“从历史里挑几条最像的”，但无法显式表达“这条曲线代表的到底是什么模式”。LLM 可以把聚类结果、天气特征、统计摘要转化成模式原型描述，再由条件生成器输出更平滑、更典型、更可解释的风光原型曲线。
- **方法轮廓**:
  - 第一步：用聚类/图聚类从历史风光曲线中得到若干候选簇。
  - 第二步：把每个簇的统计摘要输入 LLM，例如：
    - 峰值时刻
    - ramp 强度
    - 波动性
    - 连续低发时长
    - 风光互补程度
    - 对应天气标签
  - 第三步：LLM 输出“原型模式描述”和 prototype prompt，例如：
    - `晴天型高峰单峰光伏曲线`
    - `午后云扰动双峰光伏曲线`
    - `夜间强风-清晨回落型风电曲线`
    - `风光联合低发保守型曲线`
  - 第四步：条件生成器根据 prototype prompt + 簇统计约束生成典型曲线，而不是直接复制真实某一天。
- **最小实验**:
  - 对比 `代表日直接选取`、`簇中心曲线`、`纯条件 diffusion`、`LLM 原型条件生成`。
  - 指标包括 representative coverage、shape fidelity、extreme-pattern preservation、prototype distinctness、human interpretability。
- **预期结果**:
  - 生成的典型曲线在覆盖性和可解释性上优于直接抽样代表日。
  - 在同样数量的典型曲线下，更能覆盖不同天气/风险模式。
- **Novelty**: 9.1/10
- **Feasibility**: 中等偏高
- **Risk**: 若 LLM 只是把簇标签换个名字，贡献会变弱
- **Contribution type**: 原型生成框架 + 典型曲线库构造方法 + 评测协议

### Idea 2: 面向极端模式保留的 LLM 语义增强代表日生成 - BACKUP

- **核心假设**: 传统代表日选择容易保平均、丢极端。LLM 可以通过识别“极端天气/极端出力语义”，帮助把稀有但关键的曲线模式纳入典型曲线库。
- **方法轮廓**:
  - 先自动识别低发、急剧 ramp、异常双峰、联合低发等模式。
  - 将这些模式转换为语义标签。
  - 代表日选择时加入语义覆盖约束，保证每类极端模式至少有原型曲线。
- **最小实验**:
  - 比较普通代表日选择与语义约束代表日生成对 extreme cases 的覆盖。
- **Novelty**: 8.5/10
- **Feasibility**: 高
- **Risk**: 偏“选择增强”而非真正生成，方法力度略弱
- **Contribution type**: 典型库构造 + 语义覆盖约束

### Idea 3: 面向风光联合典型曲线库的文本条件场景压缩器 - BACKUP

- **核心假设**: 风电与光伏联合典型曲线的关键不是单曲线形状，而是联合关系。LLM 可以作为压缩器，把联合模式表示成文本化原型，然后生成少量联合典型曲线对。
- **方法轮廓**:
  - 输入风电、光伏联合曲线及其互补性统计。
  - LLM 生成联合原型描述，如：
    - `光伏中午高峰明显，风电夜间支撑`
    - `全天风弱 + 光伏午后受云抑制`
  - 由联合生成器输出成对的风电/光伏典型曲线。
- **最小实验**:
  - 评价联合分布保持、互补性保持、源荷失配保持。
- **Novelty**: 8.7/10
- **Feasibility**: 中等
- **Risk**: 需要更强的联合评测，不然容易退化成两个单变量问题拼接
- **Contribution type**: 联合原型库 + 典型场景压缩

### Idea 4: LLM 作为典型曲线库的解释器与检索接口 - BACKUP

- **核心假设**: 即使典型曲线库本身由聚类或 diffusion 构建，LLM 仍可作为“解释器 + 检索器”，使库能被按自然语言调用。
- **方法轮廓**:
  - 给每条典型曲线自动生成说明文本。
  - 支持用查询语句检索典型曲线，例如：
    - `找一个夏季晴天但午后云扰动的光伏典型曲线`
    - `找一个夜间大风、清晨快速回落的风电典型曲线`
  - 可与规划、调度或仿真软件联动。
- **最小实验**:
  - 评估 text-to-curve retrieval 精度和使用者偏好。
- **Novelty**: 7.8/10
- **Feasibility**: 高
- **Risk**: 更像系统增强，方法创新偏弱
- **Contribution type**: 人机交互 + 库管理

## Eliminated Ideas

| Idea | Reason eliminated |
|---|---|
| 让 LLM 直接自回归输出典型风光曲线 | 长程一致性、物理合理性和“典型性”都难保证 |
| 只做传统典型日聚类加一个 LLM 描述器 | 容易被认为只是后处理包装 |
| 只做 unconditional 典型曲线生成 | 无法体现“典型模式库”的可控和可解释特性 |
| 仅针对单场站单变量做典型曲线 | 太窄，不足以支撑“典型库”论文故事 |

## Deep Novelty Check for the Top Idea

已有工作已经分别证明：

1. 聚类和代表日方法可以提取典型场景；
2. diffusion 可以生成可控的新能源曲线；
3. LLM 可以处理通用时序合成任务。

但还没有形成这样一个完整链条：

`聚类/统计摘要 -> LLM 原型语义生成 -> 条件生成器落地典型曲线 -> 形成可解释典型曲线库`

因此，Top idea 的新颖性成立，前提是必须同时做到：

- 不是简单“选一条最接近簇中心的真实曲线”，而是生成更典型的 prototype curve；
- 不是简单“给簇起名字”，而是让语义原型真正参与生成约束；
- 评测的不只是生成逼真度，还包括 `代表性、可解释性、模式去冗余、极端模式覆盖`。

如果缺少这些，论文就会退化成“聚类 + caption”。

## Critical Review of the Top Idea

### Strengths

- 和你现有的风光聚类方向天然衔接，不需要完全换题。
- LLM 的使用位置合理，避免了“硬让 LLM 直接输出数值曲线”的不自然设定。
- 典型曲线库是一个很好的论文对象，既可做方法，也可做应用。
- 容易扩展到风光联合、极端模式保留和调度场景调用。

### Main Weaknesses

- “典型性”定义必须非常清楚，否则容易陷入主观解释。
- 需要设计一套新评测，不然无法体现生成原型优于直接抽样代表日。
- 如果生成器太强而 LLM 作用太弱，会被问“去掉 LLM 是否一样成立”。

### Internal Reviewer Score

- **Before refinement**: 8.4/10
- **After scope control**: 9.0/10

## Refined Proposal Sketch

**题目草案**:  
`LLM-Guided Prototype Generation for Representative Wind and Photovoltaic Curve Libraries`

**问题锚点**:  
现有风光典型曲线方法大多依赖聚类后直接选择代表日或簇中心，能够压缩数据，但难以得到同时具备代表性、可解释性、极端模式覆盖和可调用性的原型曲线库。

**方法主张**:  
先从历史风光曲线中提取候选模式，再由 LLM 将统计模式升华为“语义原型”，最后由条件生成器生成符合原型约束的典型风光曲线，从而构建可解释的 representative curve library。

**最小可发表版本**:

- 一个光伏或风电典型曲线库任务
- 一套 prototype prompt 设计方法
- 一个 `cluster summary -> LLM prototype -> conditional generator` 原型
- 一组关于代表性、解释性和极端模式覆盖的实验

## Next Steps

- [ ] 先定 `光伏`、`风电` 还是 `联合风光`
- [ ] 先定典型曲线对象：`代表日` 还是 `日内原型曲线`
- [ ] 用现有聚类结果先做一版 cluster summary 模板
- [ ] 验证 LLM 生成的原型标签是否能稳定区分模式
- [ ] 若原型语义稳定，再接条件生成器生成 prototype curves

## Source Links

- *Wind and Photovoltaic Power Time Series Data Aggregation Method Based on Ensemble Clustering and Markov Chain*: https://www.sciopen.com/article/10.17775/CSEEJPES.2020.03700
- *Enhancing representative photovoltaic scenario extraction for multiple power stations with a shared-weight and adaptively fused graph clustering method*: https://www.sciencedirect.com/science/article/pii/S0306261925020215
- *A Novel Clustering Method for Extracting Representative Photovoltaic Scenarios Considering Power, Energy, and Variability*: https://doi.org/10.1109/TPWRS.2024.3481691
- *Conditional Style-Based Generative Adversarial Networks for Renewable Scenario Generation*: https://doi.org/10.1109/TPWRS.2022.3170992
- *Short-Term Wind Power Scenario Generation Based on Conditional Latent Diffusion Models*: https://ieeexplore.ieee.org/document/10296015/
- *Controllable renewable energy scenario generation based on pattern-guided diffusion models*: https://doi.org/10.1016/j.apenergy.2025.126446
- *Synthetic Time Series Generation for Decision Intelligence Using Large Language Models*: https://www.mdpi.com/2227-7390/12/16/2494
- *Forging Time Series with Language: A Large Language Model Approach to Synthetic Data Generation*: https://openreview.net/forum?id=A2pmvkqOgp
