# Idea Discovery Report

**Direction**: 大语言模型在风电光伏预测的应用
**Date**: 2026-04-15
**Pipeline**: research-lit -> idea-creator -> novelty-check -> research-review
**Mode**: non-destructive literature-driven run

## Executive Summary

截至 2026 年 4 月，`LLM/VLM 用于风电和光伏预测` 已经从“可不可行”的早期探索，进入到“多模态、少样本、概率预测、跨场站迁移、调度耦合”的第二阶段。直接做“把 Time-LLM 或通用 LLM 接到功率序列上，证明误差下降一点”的论文，已经很难成为强选题。

在仍然坚持“风电/光伏预测”这个主线的前提下，最值得做的不是最朴素的点预测，而是以下三种更有发表空间的方向：

**首选方向**: 面向多场站小样本迁移的 `图结构 + 检索增强事件提示 + 概率预测` 风光 LLM 框架。  
它兼顾了风电的时空相关性、光伏的天气事件敏感性，以及 LLM 真正擅长的文本/事件条件建模。

## Literature Landscape

### 1. 近期代表性文献

| 类别 | 代表工作 | 日期 | 说明 | 启示 |
|---|---|---:|---|---|
| LLM4TS 起点 | *Time-LLM: Time Series Forecasting by Reprogramming Large Language Models* | 2023 | 用重编程把时序喂给 LLM | 奠定“时序转语言接口”路线 |
| 风电预测 | *BERT4ST: Fine-tuning pre-trained large language model for wind power forecasting* | 2024 | 预训练语言模型做风电时空预测 | 风电方向已不再空白 |
| 光伏预测 | *A Novel Distributed PV Power Forecasting Approach Based on Time-LLM* | 2025 | Time-LLM 用于分布式光伏预测 | 光伏方向已被 Time-LLM 占位 |
| 风电预测 | *PowerMistral: A data-efficient wind power forecasting framework leveraging pre-trained large language models* | 2026 | 小样本风电预测 | few-shot 已成为热点 |
| 风电预测 | *Modality Alignment-Driven large language model for wind farm power forecasting* | 2026 | 模态对齐式风电预测 | “数值序列与语言空间对齐”已很活跃 |
| 风电预测 + 调度 | *PEFT-based large language model for wind power forecasting and risk-tunable energy scheduling in microgrids* | 2026 | 风电预测与调度联动 | 预测正在向下游决策延伸 |
| 光伏预测 | *Ultra-short-term photovoltaic power prediction based on reprogrammed large language models* | 2026 | 超短期光伏 LLM 预测 | 单纯超短期预测也有人做了 |
| 光伏概率预测 | *Probabilistic prediction of photovoltaic power: A multi-task learning and large language model-based approach* | 2026 | 概率预测 + 多任务 | 概率预测不再新鲜，但仍可做强 |
| 多模态光伏 | *PV-VLM: A Multimodal Vision-Language Approach Incorporating Sky Images for Intra-Hour Photovoltaic Power Forecasting* | 2025 | 天空图像 + 时序 | 光伏强烈走向多模态 |
| 多模态光伏 | *Solar-VLM: Multimodal Vision-Language Models for Augmented Solar Power Forecasting* | 2026 | 卫星/图像/文本/时序联合 | 多模态光伏已进入 VLM 时代 |

### 2. 赛道判断

- `单变量或普通多变量点预测`：拥挤
- `Time-LLM 式重编程直接套到风电/光伏`：拥挤
- `few-shot / cross-site transfer`：仍有空间，但需要更强任务定义
- `概率预测`：有空间，但必须和事件级不确定性或校准性结合
- `光伏多模态 VLM`：有空间，但需要和已有 Solar-VLM / PV-VLM 拉开差异
- `风电图结构 + LLM`：有空间，尤其是多场站、跨区域、超图/图先验

### 3. 文献给出的清晰结论

- LLM 在风电/光伏预测上并非天然占优，只有当任务涉及 `小样本迁移、多模态输入、事件文本条件、概率推断` 时，优势才更可能显现。
- 如果只比较 `MAE / RMSE`，强 TS foundation model 和 Transformer 基线往往更有竞争力。
- 如果能把 `天气事件解释、极端场景鲁棒性、跨场站泛化、概率校准` 做进去，LLM/VLM 的价值会更容易成立。

## Ranked Ideas

### Idea 1: 面向多场站小样本迁移的图结构事件增强概率风光预测 - RECOMMENDED

- **核心假设**: 风电/光伏预测真正难的不是常规时段平均误差，而是小样本站点、跨区域迁移和极端天气时段。LLM 的价值不是替代主干时序模型，而是把天气事件、场站说明和历史异常模式转成条件知识，提升迁移与不确定性建模。
- **方法轮廓**:
  - 数值主干使用 TS foundation model 或强 Transformer 作为 backbone。
  - 用图结构编码多场站空间关系、气象邻近性、地理相似性。
  - 用 LLM 将天气公告、NWP 摘要、事件标签、生成功率变化描述转为事件提示嵌入。
  - 输出不仅是点预测，还包括分位数或预测区间。
- **最小实验**:
  - 风电和光伏各选一个多场站数据集。
  - 比较 `TS backbone only`、`TS + graph`、`TS + text events`、`TS + graph + LLM events`。
  - 重点评价 cross-site few-shot、extreme-weather slices、CRPS/PICP/PINAW。
- **预期结果**:
  - 在常规整体误差上小幅提升，在小样本迁移与极端天气切片上明显提升。
- **Novelty**: 8.7/10
- **Feasibility**: 中等偏高
- **Risk**: 需要可靠的事件文本来源，且不能让 LLM 只变成“昂贵 embedding 工具”
- **Contribution type**: 方法 + 任务设定 + 评测协议

### Idea 2: 多模态 VLM 驱动的光伏天气事件解释型预测 - BACKUP

- **核心假设**: 光伏预测的关键增量来自“看懂云层演化和天气事件”，而不是单纯换更大的时序模型。
- **方法轮廓**:
  - 输入包含天空图像、卫星图、NWP、功率历史。
  - VLM/LLM 生成中间天气事件描述，例如“快速移动厚云带”“午后局地对流增强”。
  - 预测器同时优化功率误差和事件解释一致性。
- **最小实验**:
  - 对比 `time-series only`、`image + series`、`image + series + text event reasoning`。
  - 报告超短期与短期两种预测跨度。
- **Novelty**: 8.2/10
- **Feasibility**: 中等
- **Risk**: 与 2025 年 `PV-VLM` 和 2026 年 `Solar-VLM` 距离较近，必须强调“解释型中间表示”而不是普通多模态融合
- **Contribution type**: 多模态预测 + 解释性建模

### Idea 3: 风光统一的跨任务提示学习与分解式预测框架 - BACKUP

- **核心假设**: 风电和光伏虽然物理机理不同，但在预测任务上共享“趋势、周期、突变、天气扰动”四类结构。LLM 擅长处理统一提示模板，可以用来做跨任务、跨 horizon 的统一预测器。
- **方法轮廓**:
  - 将风电与光伏任务统一写成 promptable forecasting task。
  - 通过 decomposition + prompt retrieval + shared adapters 共享知识。
  - 支持 day-ahead、intra-day、ultra-short-term 多 horizon。
- **最小实验**:
  - 单独训练 vs 联合训练。
  - 测试跨任务迁移：风电数据辅助光伏，光伏数据辅助风电。
- **Novelty**: 7.8/10
- **Feasibility**: 高
- **Risk**: 容易被质疑为“多任务工程整合”，需要证明 shared prompting 真的有效
- **Contribution type**: 统一框架 + 迁移学习

### Idea 4: 面向风电预测的超图结构 LLM 对齐模型 - BACKUP

- **核心假设**: 风电多场站预测比光伏更依赖空间相关性、地形相似性、风场耦合与时空传播模式，因此“图/超图 + LLM 对齐”比普通序列重编程更有希望出新结果。
- **方法轮廓**:
  - 用超图建模站点组关系而非简单 pairwise graph。
  - 用 LLM 编码场站描述、地理环境文本、历史异常摘要。
  - 对齐超图表示和语言条件表示，辅助多步风电预测。
- **最小实验**:
  - 与 `BERT4ST`、`PowerMistral`、标准 GNN-Transformer 比较。
- **Novelty**: 8.1/10
- **Feasibility**: 中等
- **Risk**: 风电专属，泛化到光伏较弱
- **Contribution type**: 结构建模方法

## Eliminated Ideas

| Idea | Reason eliminated |
|---|---|
| 直接复现 Time-LLM 做风电或光伏点预测 | 赛道已拥挤，创新性不足 |
| 只做一个“LLM 比 PatchTST 更准”的实验论文 | 容易被质疑基线不充分或收益不稳定 |
| 只做单场站光伏短期预测 | 过于局部，难体现 LLM 的真正价值 |
| 只做文本提示，不引入事件、多模态或迁移问题 | 很难回答“为什么需要语言模型” |

## Deep Novelty Check for the Top Idea

Top idea 的新颖性依赖于下面三个点同时成立：

1. **不是普通点预测**，而是明确聚焦 `small-sample cross-site transfer + probabilistic forecasting`。
2. **不是纯数值主干套 LLM**，而是用 LLM/VLM 提供 `事件条件知识`。
3. **不是平均误差主导**，而是强调 `极端天气切片、概率校准、迁移鲁棒性`。

如果只做到其中一部分，比如只有图结构没有事件增强，或只有概率预测没有迁移评测，那么论文会更像已有工作的组合，而不是新的方向。

## Critical Review of the Top Idea

### Strengths

- 仍然留在“风电/光伏预测”这个明确主线内。
- 比纯点预测更能体现 LLM 的文本条件建模能力。
- 可同时对接风电和光伏，适合做统一论文。
- 审稿时更容易解释为什么不用普通 TS backbone 就够了。

### Main Weaknesses

- 如果事件文本来源太弱，方法可能退化为“额外加了一个 noisy modality”。
- 若实验只看平均 RMSE，贡献会被严重低估。
- 实现上需要同时兼顾图结构、语言条件和概率输出，复杂度偏高。

### Internal Reviewer Score

- **Before refinement**: 8.0/10
- **After scope control**: 8.9/10

## Refined Proposal Sketch

**题目草案**:  
`Event-Enhanced Graph-Conditioned LLM for Few-Shot Probabilistic Wind and PV Forecasting`

**问题锚点**:  
现有 LLM 风光预测研究大多聚焦单任务点预测，缺少对小样本迁移、极端天气鲁棒性和概率校准的统一建模，因此尚未充分体现语言模型在新能源预测中的独特价值。

**方法主张**:  
用强时序 backbone 负责数值建模，用图结构负责场站关系建模，用 LLM/VLM 负责天气事件与场站语义条件建模，三者联合提升跨站点小样本风光概率预测。

**最小可发表版本**:

- 一个多场站风电数据集 + 一个多场站光伏数据集
- 一套事件文本构造方式：NWP 摘要、天气标签或自动生成天气描述
- 一组针对 few-shot transfer 和 probabilistic calibration 的核心实验

## Next Steps

- [ ] 先定主攻对象：`风电为主` 还是 `风光统一`
- [ ] 选可复现实验数据集，并确认是否有天气文本或图像模态
- [ ] 确定强基线：`TimesFM / Chronos / PatchTST / iTransformer / Time-LLM`
- [ ] 先做一个“事件文本是否有增益”的小型消融
- [ ] 若事件文本有效，再加图结构和概率头

## Source Links

- Time-LLM: https://arxiv.org/abs/2310.01728
- BERT4ST: https://www.sciencedirect.com/science/article/pii/S0196890424002723
- PowerMistral: https://www.sciencedirect.com/science/article/pii/S0306261926002771
- Modality Alignment-Driven LLM for wind farm forecasting: https://www.sciencedirect.com/science/article/pii/S1000934526000076
- PEFT-based LLM for wind forecasting and scheduling: https://www.sciencedirect.com/science/article/pii/S0960148126001229
- Distributed PV forecasting based on Time-LLM: https://arxiv.org/abs/2503.06216
- Ultra-short-term PV prediction based on reprogrammed LLMs: https://www.sciencedirect.com/science/article/pii/S0142061526000840
- Probabilistic PV prediction with MTL + LLM: https://www.sciencedirect.com/science/article/pii/S0960148125016684
- PV-VLM: https://arxiv.org/abs/2504.13624
- Solar-VLM: https://arxiv.org/abs/2604.04145
