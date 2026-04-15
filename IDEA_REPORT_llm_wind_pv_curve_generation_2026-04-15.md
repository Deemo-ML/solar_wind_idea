# Idea Discovery Report

**Direction**: 大语言模型如何用于光伏风电曲线生成
**Date**: 2026-04-15
**Pipeline**: research-lit -> idea-creator -> novelty-check -> research-review
**Mode**: non-destructive literature-driven run
**Interpretation**: 这里的“曲线生成”按 `风电/光伏功率轨迹生成、场景生成、合成曲线生成` 理解

## Executive Summary

截至 2026 年 4 月，风电/光伏曲线生成这条线的主流方法并不是 LLM，而是 `GAN / VAE / normalizing flow / diffusion`。最近两年的文献清楚地表明：在新能源场景生成里，真正有效的是 `条件扩散`、`可控生成`、`极端事件模式建模`、`多模态/跨模态条件融合`。而 LLM 在“纯数值轨迹直接生成”上的代表性工作还很少，更多停留在通用时序合成数据生成。

这意味着一个很重要的判断：

**如果直接让 LLM 单独生成风光功率曲线，风险较高；如果让 LLM 负责编排语义条件、天气事件和场景控制，再让 diffusion/latent generator 负责落地到数值曲线，反而是更自然、也更有新意的方向。**

因此，这次最推荐的方向不是“LLM 直接替代场景生成器”，而是：

**面向极端天气与可控场景的 `LLM 条件编排 + Latent Diffusion 曲线生成` 风光轨迹生成框架。**

## Literature Landscape

### 1. 相关文献分成两支

#### A. 新能源场景/曲线生成主流文献

这些论文说明新能源曲线生成已经有比较成熟的非 LLM 路线：

- *Conditional Style-Based Generative Adversarial Networks for Renewable Scenario Generation* (IEEE Transactions on Power Systems, 2023)
- *Short-Term Wind Power Scenario Generation Based on Conditional Latent Diffusion Models* (IEEE Transactions on Sustainable Energy, 2024)
- *A Cross-Modal Generative Adversarial Network for Scenarios Generation of Renewable Energy* (IEEE Transactions on Power Systems, 2024)
- *A Novel Renewable Energy Scenario Generation Method Based on Multi-Resolution Denoising Diffusion Probabilistic Models* (Energies, 2025)
- *Controllable renewable energy scenario generation based on pattern-guided diffusion models* (Applied Energy, 2025)
- *Generative probabilistic forecasting of wind power: A Denoising-Diffusion-based nonstationary signal modeling approach* (Energy, 2025)
- *Wind power scenario generation via multi-scale condition adaptive diffusion model* (Electric Power Systems Research, 2026)

#### B. LLM/语言模型做通用时序生成

这些论文说明 “LLM 生成时序” 这件事正在形成，但还没有深度吃透新能源：

- *Synthetic Time Series Generation for Decision Intelligence Using Large Language Models* (Mathematics, 2024)
- *Forging Time Series with Language: A Large Language Model Approach to Synthetic Data Generation* (NeurIPS 2025)

### 2. 当前最重要的结构性事实

- 在新能源曲线生成里，`diffusion` 正在成为最强主流。
- 在通用时序合成里，`LLM 直接生成 multivariate time series` 开始出现代表作。
- 但在“`LLM + 风电/光伏曲线生成`”这个交叉点上，直接命中的代表性论文仍然很少。
- 因此，真正可做的不是简单复刻通用时序 LLM 生成，而是把 LLM 的优势放在：
  - `语义条件`
  - `事件编排`
  - `可控生成`
  - `跨模态条件融合`
  - `生成后解释与筛选`

### 3. 文献给出的直接启示

- `风光曲线生成` 的难点不是只拟合边际分布，而是要同时保留：
  - 日内形状
  - 爬坡与突变
  - 风光互补/同跌
  - 极端事件模式
  - 空间相关性
- 这些约束非常像“高层语义 + 低层数值落地”的两层任务。
- LLM 更适合高层语义控制，不适合直接承担全部数值生成责任。

## Ranked Ideas

### Idea 1: 面向极端天气与可控模式的 LLM 条件编排 + Latent Diffusion 风光曲线生成 - RECOMMENDED

- **核心假设**: 风光曲线生成真正缺少的不是又一个 unconditional generator，而是能够用自然语言或结构化事件描述，控制生成“什么样的曲线”的生成器。LLM 最适合把天气事件、场景标签、调度需求、风险描述转成高层条件；latent diffusion 最适合把这些条件落成真实功率曲线。
- **方法轮廓**:
  - 用 LLM 接收输入条件，例如：
    - `连续阴云 + 午后骤降`
    - `夜间强风 + 清晨 ramp-up`
    - `Dunkelflaute-like wind-solar joint low output`
    - `高温晴天但午后云团扰动`
  - 将这些文本条件或结构化标签映射为 scenario prompt embedding。
  - 用 latent diffusion / conditional diffusion 根据 prompt + 历史上下文 + NWP 条件生成未来风光曲线。
  - 支持 controllable generation：控制 ramp、峰值时刻、持续低发时长、风光互补程度。
- **最小实验**:
  - 选一个风电场景集和一个光伏场景集。
  - 构造文本/标签条件：天气事件、功率模式、极端场景类型。
  - 对比 `conditional diffusion`、`prompt-conditioned diffusion`、`LLM prompt + diffusion`。
  - 指标包括 distribution fidelity、ramp fidelity、extreme-event recall、scenario controllability。
- **预期结果**:
  - 平均统计指标不一定大幅领先，但在“按指定模式生成”与“极端场景覆盖”上明显更强。
- **Novelty**: 9.0/10
- **Feasibility**: 中等
- **Risk**: 需要设计高质量的场景文本/标签体系，否则 LLM 条件会流于表面
- **Contribution type**: 方法 + controllable generation task + 评测协议

### Idea 2: 面向多场站联合风光曲线生成的跨模态 LLM 场景编译器 - BACKUP

- **核心假设**: 多场站风光曲线生成最难的是空间相关性与天气共因，而这些信息往往同时存在于 NWP、站点元数据、天气摘要、区域描述中。LLM 可以充当“场景编译器”，把这些异构输入压缩成统一的条件表示，再交给生成器。
- **方法轮廓**:
  - 输入：站点位置、地形描述、天气摘要、NWP 数值、历史曲线。
  - LLM 将它们编译为统一的 scene token 或 condition code。
  - 扩散模型生成多场站联合曲线。
- **最小实验**:
  - 测试空间相关性保持、联合分布质量、跨区域泛化。
- **Novelty**: 8.6/10
- **Feasibility**: 中等偏低
- **Risk**: 多场站联合生成评测更复杂，数据要求高
- **Contribution type**: 跨模态联合生成

### Idea 3: 面向数据增强的少样本风光曲线合成器 - BACKUP

- **核心假设**: 对新建场站、小样本站点或极端天气稀缺区域，训练预测器和调度模型时最大的瓶颈是数据少。LLM 可以借鉴通用时序合成框架，把少量真实风光曲线编码成“语言化表示”，再生成统计上相似、下游可用的合成样本。
- **方法轮廓**:
  - 参考 `SDForger` 一类工作，将风光时间序列压缩成可文本化 embedding。
  - 微调小型 autoregressive LLM 做 synthetic curve generation。
  - 用下游预测/调度任务检验 utility。
- **最小实验**:
  - few-shot setting 下训练预测模型，比较是否因合成数据而改进。
- **Novelty**: 7.9/10
- **Feasibility**: 高
- **Risk**: 容易被质疑只是“通用时序合成框架迁移到新能源”
- **Contribution type**: 数据增强 + 合成数据评测

### Idea 4: LLM 作为风光曲线生成的评审器与约束对齐器 - BACKUP

- **核心假设**: 生成模型最大的痛点不一定是“生成不出来”，而是“生成了但不合理”。LLM 不一定非要做生成器本体，也可以做后验评审器：检查生成曲线是否符合物理/气象/运行逻辑，并反馈给主生成器。
- **方法轮廓**:
  - 主生成器仍为 diffusion/GAN。
  - LLM 根据曲线摘要、天气条件、场景目标生成 critique，判断：
    - 是否出现不合理夜间光伏输出
    - 是否出现与天气条件不符的波动
    - 是否遗漏联合低发事件
  - 用 critique-guided reranking 或 rejection sampling 优化样本质量。
- **Novelty**: 8.0/10
- **Feasibility**: 高
- **Risk**: 容易被看成 pipeline trick，需要设计很强的约束评测
- **Contribution type**: 生成后校验/对齐

## Eliminated Ideas

| Idea | Reason eliminated |
|---|---|
| 让通用 LLM 直接按 token 自回归输出长风光功率曲线 | 数值稳定性、长程一致性和物理合理性风险很高 |
| 只把现有通用时序合成 LLM 迁移到新能源 | 学术上容易显得是直接应用，创新不足 |
| 只做 unconditional 风光曲线生成 | 可控性弱，难体现 LLM 的价值 |
| 只做单场站单变量曲线合成 | 太窄，无法体现空间相关、极端事件和场景语义 |

## Deep Novelty Check for the Top Idea

现有文献已经说明两件事：

1. 新能源曲线生成里，`conditional diffusion / controllable generation` 已经是强基线。
2. 通用时序领域里，`LLM 直接做 synthetic time series generation` 已经开始成立。

但这两条线还没有在风光场景里充分合并。真正的空白在于：

- 用 `自然语言/结构化事件` 控制风光曲线的生成；
- 不只是生成像真的曲线，而是生成 `指定模式` 的曲线；
- 让生成结果可被解释成“为什么会长成这样”的场景。

因此，Top idea 的新颖性成立，前提是必须同时满足：

- 生成任务是 `controllable` 而不是普通 unconditional sampling；
- LLM 负责的是 `高层语义场景控制` 而不是仅仅做 embedding；
- 评测不仅看分布接近度，还看 `模式可控性、极端事件召回、物理合理性`。

## Critical Review of the Top Idea

### Strengths

- 非常契合 LLM 的优势：文本条件、语义编排、事件描述。
- 不和当前最强的 diffusion 主流正面冲突，而是把 LLM 放在更合适的位置。
- 可自然扩展到天气文本、专家规则、调度目标等多种条件。
- 比“LLM 直接输出数值曲线”更容易说服审稿人。

### Main Weaknesses

- 如果文本条件只是人工标签改写，审稿人可能会质疑“LLM 必要性”。
- 需要构造一套可信的场景语义体系，否则 controllability 难以评测。
- 如果没有真实极端事件数据，论文可能更多展示生成灵活性而非业务价值。

### Internal Reviewer Score

- **Before refinement**: 8.2/10
- **After scope control**: 9.1/10

## Refined Proposal Sketch

**题目草案**:  
`Language-Conditioned Latent Diffusion for Controllable Wind and Photovoltaic Curve Generation`

**问题锚点**:  
现有风光曲线生成方法虽然可以学习历史分布，但对“生成什么类型的曲线”控制能力有限，特别是在极端天气、联合低发和少样本异常模式场景下，难以生成既可控又合理的功率轨迹。

**方法主张**:  
用 LLM 把天气事件、场景意图和风险模式转成高层条件表示，再用 latent diffusion 将这些条件落地为风电/光伏功率曲线，从而实现可解释、可控的风光轨迹生成。

**最小可发表版本**:

- 一个风电或光伏日内曲线生成任务
- 一套文本/标签条件体系
- 一个 `LLM prompt encoder + latent diffusion` 原型
- 一组关于 controllability、fidelity、extreme-pattern coverage 的实验

## Next Steps

- [ ] 先定是 `风电`、`光伏`，还是 `联合风光`
- [ ] 先做文本条件设计：天气事件、曲线模式、运行场景三选一为主
- [ ] 选生成 backbone：`conditional latent diffusion` 优先
- [ ] 先做一组 controllable generation 小实验，验证文本条件是否真的能改变曲线形状
- [ ] 若有效，再加入多场站空间相关或极端场景 few-shot 扩展

## Source Links

- *Synthetic Time Series Generation for Decision Intelligence Using Large Language Models* (Mathematics, 2024): https://www.mdpi.com/2227-7390/12/16/2494
- *Forging Time Series with Language: A Large Language Model Approach to Synthetic Data Generation* (NeurIPS 2025): https://openreview.net/forum?id=A2pmvkqOgp
- *Conditional Style-Based Generative Adversarial Networks for Renewable Scenario Generation* (IEEE TPWRS, 2023): https://doi.org/10.1109/TPWRS.2022.3170992
- *Short-Term Wind Power Scenario Generation Based on Conditional Latent Diffusion Models* (IEEE TSTE, 2024): https://ieeexplore.ieee.org/document/10296015/
- *A Cross-Modal Generative Adversarial Network for Scenarios Generation of Renewable Energy* (IEEE TPWRS, 2024): https://ieeexplore.ieee.org/document/10129080/
- *Controllable renewable energy scenario generation based on pattern-guided diffusion models* (Applied Energy, 2025): https://doi.org/10.1016/j.apenergy.2025.126446
- *A Novel Renewable Energy Scenario Generation Method Based on Multi-Resolution Denoising Diffusion Probabilistic Models* (Energies, 2025): https://www.mdpi.com/1996-1073/18/14/3781
- *Generative probabilistic forecasting of wind power: A Denoising-Diffusion-based nonstationary signal modeling approach* (Energy, 2025): https://doi.org/10.1016/j.energy.2025.134576
- *Wind power scenario generation via multi-scale condition adaptive diffusion model* (Electric Power Systems Research, 2026): https://doi.org/10.1016/j.epsr.2026.112753
- *Text-Conditioned Diffusion-Based Synthetic Data Generation for Turbine Engine Sensor Analysis and RUL Estimation* (Machines, 2025): https://www.mdpi.com/2075-1702/13/5/374
