# Literature Review

**Topic**: 大语言模型在新能源领域的应用  
**Date**: 2026-04-15  
**Scope**: 50 篇左右文献的结构化分析  
**Purpose**: 支撑 `idea-discovery` 的文献调研阶段，为后续选题、related work 和实验设计提供依据

## Executive Summary

这 50 篇文献可以分成五类：

1. `综合综述 / 领域总览`
2. `时间序列基础模型（TSFM）`
3. `LLM4TS 方法论文`
4. `新能源直接应用论文`
5. `强基线 / 评测与反思论文`

从这 50 篇文献得到的结论非常清楚：

- `LLM 直接做风电/光伏预测` 已经不是空白方向，而是一个快速升温且开始拥挤的赛道。
- 2024-2026 年主流创新集中在：`时序重编程`、`prompt 化预测`、`多模态融合`、`少样本迁移`、`概率预测`。
- 新能源论文的真正增量，正从“再换一个 backbone 做预测”转向“预测 + 解释 + 调度/运维决策支持”。
- 对你当前项目最有价值的不是再做一个纯预测器，而是把 LLM 放到 `风光场站群协同调度、消纳分析、故障诊断、规程问答、日志归因` 这些更贴业务闭环的位置。

## Selection Strategy

本报告纳入的 50 篇论文，分为两类：

- `直接相关文献`: LLM/GenAI 在风电、光伏、调度、能源系统中的直接应用
- `支撑文献`: TS foundation model、LLM4TS、benchmark、批判性分析等，为方法设计和实验对比提供基础

时间范围以 `2022-2026` 为主，重点关注 `2024-2026`。

## Category Distribution

| 类别 | 数量 | 作用 |
|---|---:|---|
| 综合综述 / 领域全景 | 10 | 帮助建立研究脉络、判断饱和度 |
| TS 基础模型 / 预训练 | 14 | 提供大模型时序基线与迁移路径 |
| LLM4TS 核心方法 | 13 | 代表“语言模型做时序”的主流路线 |
| 新能源直接应用 | 8 | 判断在风电/光伏/调度中的实际进展 |
| 强基线 / 评测 / 反思 | 5 | 保证实验设计不过度乐观 |

## Core Paper Table

| ID | 类别 | 文献 | 年份 | 核心贡献 | 对新能源研究的价值 |
|---|---|---|---:|---|---|
| 1 | 综述 | Foundation Models for Time Series: A Survey | 2025 | 系统梳理时序基础模型 | 适合搭建大模型时序背景 |
| 2 | 综述 | A Survey of Time Series Foundation Models: Generalizing Time Series Representation with Large Language Model | 2024 | 连接 TSFM 与 LLM4TS | 适合解释“为什么会出现 LLM4TS” |
| 3 | 综述 | Large Language Models for Time Series: A Survey | 2024 | 专门综述 LLM 做时序 | 适合作为 related work 入口 |
| 4 | 综述 | Large Language Models for Time Series Analysis | 2025 | 更新版 LLM4TS 综述 | 适合补充最新方法图谱 |
| 5 | 方法分析 | Time Series Forecasting with LLMs: Understanding and Enhancing Model Capabilities | 2024 | 分析 LLM 在时序中的有效条件 | 很适合判断风光任务是否真适合 LLM |
| 6 | 综述 | Deep Learning for Time Series Forecasting: A Survey | 2025 | 非 LLM 时序预测总览 | 用于构建传统基线框架 |
| 7 | 能源综述 | Foundation Models for Clean Energy Forecasting: A Comprehensive Review | 2026 | 清洁能源预测基础模型综述 | 是新能源大模型的重要综述 |
| 8 | 风电综述 | A survey on wind power forecasting with machine learning approaches | 2024 | 风电预测综述 | 帮助把 LLM 工作放回风电大背景 |
| 9 | 多模态综述 | Multi-modal Time Series Analysis: A Tutorial and Survey | 2025 | 多模态时序总览 | 对光伏图像+时序、多源风电很关键 |
| 10 | 基准 | Towards the Next Generation of Time Series Forecasting Benchmarks | 2026 | 重新讨论时序 benchmark | 适合设计更可信的实验 |
| 11 | TSFM | Chronos: Learning the Language of Time Series | 2024 | token 化时序预训练 | 零样本/少样本新能源预测强基线 |
| 12 | TSFM | A decoder-only foundation model for time-series forecasting | 2024 | TimesFM | 必须纳入的通用强基线 |
| 13 | TSFM | Unified Training of Universal Time Series Forecasting Transformers | 2024 | Moirai | 适合多频率、多变量建模 |
| 14 | TSFM | Time-MoE: Billion-Scale Time Series Foundation Models with Mixture of Experts | 2024 | MoE 扩展时序基础模型 | 说明时序模型在 scale up |
| 15 | TSFM | MOMENT: A Family of Open Time-series Foundation Models | 2024 | 开源时序模型家族 | 复现和迁移价值高 |
| 16 | TSFM | Lag-Llama: Towards Foundation Models for Probabilistic Time Series Forecasting | 2023 | 概率时序大模型 | 对新能源不确定性建模很有用 |
| 17 | TSFM | DAM: Towards A Foundation Model for Time Series Forecasting | 2024 | 灵活预测跨度的基础模型 | 对混合时间尺度任务有参考性 |
| 18 | TSFM | Sundial: A Family of Highly Capable Time Series Foundation Models | 2025 | 新一代时序基础模型 | 可作更新基线 |
| 19 | TSFM | Toto: Time Series Optimized Transformer for Observability | 2024 | 面向可观测工业时序 | 贴近能源工业数据特性 |
| 20 | TSFM | Timer: Generative Pre-trained Transformers Are Large Time Series Models | 2024 | 生成式时序预训练 | 可借鉴自回归生成思路 |
| 21 | TSFM | TimeFound: A Foundation Model for Time Series Forecasting | 2025 | 多分辨率时序建模 | 对长短期风光预测有启发 |
| 22 | 预训练 | Large Pre-trained time series models for cross-domain Time series analysis tasks | 2023 | 跨域时序预训练 | 对跨区域场站迁移有帮助 |
| 23 | 跨模态 TS | VisionTS: Visual Masked Autoencoders Are Free-Lunch Zero-Shot Time Series Forecasters | 2024 | 视觉预训练迁移到时序 | 对图像+时序建模思路有启发 |
| 24 | 预训练 | TimeSiam: A Pre-Training Framework for Siamese Time-Series Modeling | 2024 | Siamese 预训练 | 对小样本新能源场景有帮助 |
| 25 | LLM4TS | One Fits All: Power General Time Series Analysis by Pretrained LM | 2023 | 早期预训练语言模型做时序 | LLM4TS 起点文献 |
| 26 | LLM4TS | Time-LLM: Time Series Forecasting by Reprogramming Large Language Models | 2023 | 时序重编程 | 最关键的代表作之一 |
| 27 | LLM4TS | TEMPO: Prompt-based Generative Pre-trained Transformer for Time Series Forecasting | 2023 | 分解 + prompt 路线 | 对风光周期/趋势建模有参考 |
| 28 | LLM4TS | LLM4TS: Aligning Pre-Trained LLMs as Data-Efficient Time Series Forecasters | 2023 | 对齐式数据高效预测 | 适合小样本场站迁移 |
| 29 | LLM4TS | TEST: Text Prototype Aligned Embedding to Activate LLM's Ability for Time Series | 2023 | 文本原型对齐 | 对结构化提示设计很有价值 |
| 30 | LLM4TS | Large Language Models Are Zero-Shot Time Series Forecasters | 2023 | 零样本时序预测 | 有助于建立上限/下限认知 |
| 31 | LLM4TS | AutoTimes: Autoregressive Time Series Forecasters via Large Language Models | 2024 | 自回归式 LLM 预测 | 多步滚动预测值得参考 |
| 32 | LLM4TS | PromptCast: A New Prompt-based Learning Paradigm for Time Series Forecasting | 2022 | prompt 化时序预测早期工作 | 适合讲清楚方法演进 |
| 33 | LLM4TS | GPT4MTS: Prompt-based Large Language Model for Multimodal Time-series Forecasting | 2024 | 多模态时序 prompt-LM | 对多源新能源输入很重要 |
| 34 | LLM4TS | LangTime: A Language-Guided Unified Model for Time Series Forecasting with Proximal Policy Optimization | 2025 | 语言引导 + PPO | 代表较新的强化式调优思路 |
| 35 | LLM4TS | Multi-scale hypergraph meets LLMs: Aligning large language models for time series analysis | 2026 | 图结构 + LLM 对齐 | 对多站点风电/光伏很有启发 |
| 36 | LLM4TS | Forecasting Time Series with LLMs via Patch-Based Prompting and Decomposition | 2025 | patch prompt + 分解 | 适合多尺度风光波动 |
| 37 | LLM4TS | Taming Pre-trained LLMs for Generalised Time Series Forecasting via Cross-modal Knowledge Distillation | 2024 | 跨模态知识蒸馏 | 适合多源异构数据融合 |
| 38 | 反思 | Are Language Models Actually Useful for Time Series Forecasting? | 2024 | 批判性分析 LLM4TS | 防止选题过度乐观 |
| 39 | 强基线 | A Time Series is Worth 64 Words: Long-term Forecasting with Transformers | 2022 | PatchTST | 必须纳入强基线 |
| 40 | 强基线 | iTransformer: Inverted Transformers Are Effective for Time Series Forecasting | 2023 | iTransformer | 多变量新能源预测常见强基线 |
| 41 | 强基线 | TimeMixer: Decomposable Multiscale Mixing for Time Series Forecasting | 2024 | 多尺度混合模型 | 非常适合风光多尺度波动 |
| 42 | 能源基线 | CT-PatchTST: Channel-Time Patch Time-Series Transformer for Long-Term Renewable Energy Forecasting | 2025 | 面向新能源预测的 PatchTST 改进 | 与风光任务直接相关 |
| 43 | 强基线 | Crossformer: Transformer Utilizing Cross-Dimension Dependency for Multivariate Time Series Forecasting | 2023 | 跨变量依赖建模 | 对多气象量、多站点任务有帮助 |
| 44 | 强基线 | N-BEATS: Neural basis expansion analysis for interpretable time series forecasting | 2019 | 可解释时序深度基线 | 可作非 Transformer 对照 |
| 45 | 光伏应用 | A Novel Distributed PV Power Forecasting Approach Based on Time-LLM | 2025 | Time-LLM 用于分布式光伏预测 | 直接说明光伏预测赛道已被占位 |
| 46 | 光伏应用 | Solar-VLM: Multimodal Vision-Language Models for Augmented Solar Power Forecasting | 2026 | 卫星图像 + 文本 + 时序 + 多站点 | 多模态光伏方向代表作 |
| 47 | 光伏应用 | PV-VLM: A Multimodal Vision-Language Approach Incorporating Sky Images for Intra-Hour Photovoltaic Power Forecasting | 2025 | 天空图像 + 时序的光伏预测 | 适合超短期场景 |
| 48 | 光伏应用 | Short-Term Photovoltaic Power Forecasting Using PV Data and Sky Images in an Auto Cross Modal Correlation Attention Multimodal Framework | 2024 | 光伏图像融合工程路线 | 作为多模态非 LLM 对照很有价值 |
| 49 | 风电应用 | BERT4ST: Fine-tuning pre-trained large language model for wind power forecasting | 2024 | 预训练语言模型做风电时空预测 | 是风电方向关键应用文献 |
| 50 | 风电应用 | M2WLLM: Multi-Modal Multi-Task Ultra-Short-term Wind Power Prediction Algorithm Based on Large Language Model | 2025 | 多模态多任务风电 LLM | 适合参考风电 LLM 设计 |

## Structured Analysis

### A. 综合综述告诉了我们什么

`1, 2, 3, 4, 6, 7, 8, 9, 10` 这些综述和基准类文献共同说明：

- 研究重心已经从“单一模型刷指标”转向“可迁移、可扩展、可多模态、可零样本”的时序基础模型。
- 新能源是 foundation model 很自然的应用场景，因为它具有强时序性、跨场站迁移需求和高不确定性。
- 但专门落到新能源时，评价指标不能只看 `MAE/RMSE`，还要看极端天气鲁棒性、概率校准、跨场站泛化、下游调度可用性。
- 2026 年的能源综述已经把 LLM 在能源系统中的角色归纳得很完整，这意味着新的论文必须有更清晰的任务锚点。

### B. TS 基础模型的启示

`11-24` 说明了一个重要事实：

- 即使完全不用语言模型，TS foundation model 也已经足够强。
- 如果你的新能源论文宣称 “引入 LLM 后更好”，那至少应该对比 `Chronos / TimesFM / Moirai / MOMENT / Sundial` 这类强基线，而不能只和普通 LSTM、Informer 比。
- 这些模型对新能源场景最有价值的地方，不仅是精度，而是：
  - 零样本/少样本预测
  - 跨场站迁移
  - 概率预测
  - 多时间尺度建模

### C. LLM4TS 的主流技术路线

`25-37` 大致形成了四条主线：

- `Reprogramming`：把数值序列改写成 LLM 可接受的 token/input
- `Prompting`：用文本描述、原型、模板来引导预测
- `Alignment`：让时序表示空间与语言空间对齐
- `Distillation / Hybrid`：把多模态、图结构、蒸馏等机制与 LLM 结合

这些方法对新能源的意义是：

- 风电/光伏预测并不是天然适合语言模型，必须解决“数值序列如何进入语言模型”这个根问题。
- 当样本稀缺、迁移需求强、多模态输入多时，LLM 路线才更可能体现优势。
- 如果数据充足、任务单一、评价只看点预测误差，传统 TSFM/Transformer 往往更有性价比。

### D. 新能源直接应用文献说明了什么

`45-50` 加上 `A large language model for advanced power dispatch`、`PowerMistral`、`PEFT-based large language model for wind power forecasting and risk-tunable energy scheduling in microgrids`、`Ultra-short-term photovoltaic power prediction based on reprogrammed large language models`、`Probabilistic prediction of photovoltaic power: A multi-task learning and large language model-based approach` 这些近期工作说明：

- 风电和光伏预测方向已经从“试试看能不能用 LLM”进入到“few-shot、概率、多模态、调度耦合”的第二阶段。
- 光伏方向明显在往 `vision-language + time series` 融合发展。
- 风电方向则更强调 `多场站时空关联`、`小样本迁移`、`风险敏感调度`。
- 调度方向开始从简单问答走向 benchmark 化和真实任务化，这比纯预测更有新意。

### E. 批判性论文给出的边界

`38` 的价值很大，它提醒我们：

- 不是所有时序任务都适合 LLM。
- 很多 LLM4TS 的收益来自训练规模、复杂输入编码和更大模型容量，而不一定来自语言能力本身。
- 因此在新能源论文里，必须明确回答：`我们为什么需要语言模型，而不是更强的时序模型？`

## Year-by-Year Trend

| 年份 | 趋势 |
|---|---|
| 2022 | prompt 化时序预测开始出现，仍属探索期 |
| 2023 | LLM4TS 爆发，Time-LLM、LLM4TS、TEST、零样本预测等奠基性工作出现 |
| 2024 | 进入结构化发展期，开始出现批判性分析、跨模态蒸馏、风电直接应用 |
| 2025 | 多模态、PPO、patch prompting、新能源专门应用增多 |
| 2026 | 能源系统总览、系统综述、调度助手、多模态光伏、few-shot 风电等明显成熟 |

## What Has Become Crowded

- `直接把 LLM 接到风电/光伏序列上做点预测`
- `只用 prompt 或重编程证明预测误差略降`
- `只和旧基线比较，不和 TS foundation model 比`
- `没有解释为什么必须用语言模型`

这些方向不是不能做，而是投稿时会很容易被审稿人问倒。

## What Still Looks Open

### 1. LLM + 新能源调度 / 运维协同

这是目前最值得做的方向之一。原因是：

- 真实系统里信息源是文本、规程、日志、时序、图像、优化结果混合的。
- LLM 的强项在于知识整合、解释生成、交互式决策支持。
- 这里的对手不只是预测模型，而是人工经验和复杂的信息整合流程。

### 2. 规则约束 / 检索增强 / 可追溯输出

新能源是高风险场景，LLM 不能只会生成，还必须：

- 可引用依据
- 可被规则校验
- 可与优化器、数据库、告警系统联动

### 3. 多模态事件级分析

尤其是光伏：

- 卫星图
- 天空图像
- 气象文本
- 功率曲线
- 告警日志

如果论文能把这些信息用于“天气事件解释 + 预测 + 风险提示”，会比单纯点预测更有新意。

### 4. Benchmark / Evaluation Protocol

新能源领域目前仍缺少像 `ElecBench` 那样专门面向风光调度、消纳、故障处置的标准评测。

## Most Relevant Papers for Your Direction

如果你的重点是“LLM 在新能源领域”，而不仅仅是“LLM 做时序预测”，最值得优先精读的是这 10 篇：

1. *Large Language Models Meet Energy Systems: Opportunities, Challenges, and Future Perspectives* (2026)
2. *Generative AI and LLM applications in renewable energy and smart grids* (2026)
3. *A large language model for advanced power dispatch* (2025)
4. *Foundation models for clean energy forecasting: A comprehensive review* (2026)
5. *Time Series Forecasting with LLMs: Understanding and Enhancing Model Capabilities* (2024)
6. *Are Language Models Actually Useful for Time Series Forecasting?* (2024)
7. *Time-LLM: Time Series Forecasting by Reprogramming Large Language Models* (2023)
8. *PowerMistral: A data-efficient wind power forecasting framework leveraging pre-trained large language models* (2026)
9. *Solar-VLM: Multimodal Vision-Language Models for Augmented Solar Power Forecasting* (2026)
10. *BERT4ST: Fine-tuning pre-trained large language model for wind power forecasting* (2024)

## Recommendation for Idea Discovery

基于这 50 篇文献，最推荐的选题收敛方式是：

### 推荐主线

`LLM 不直接替代风光预测器，而是作为风光场站群协同调度 / 运维 / 规程问答 / 异常分析的知识协同层`

### 推荐论文形态

- `系统论文`: RAG + 规则约束 + 调度/运维 benchmark
- `多模态论文`: 图像 + 时序 + 文本 + 事件解释
- `benchmark 论文`: 新能源调度/运维 LLM 评测基准

### 不太推荐作为主线的方向

- 单纯再做一个 `LLM 风电预测`
- 单纯再做一个 `LLM 光伏预测`
- 只做“问答机器人”，没有安全约束和硬评测

## Bottom Line

50 篇文献的分析支持一个很强的结论：

**大语言模型在新能源领域最有前景的位置，不是单独做一个更大的预测器，而是作为“新能源知识整合与决策协同中枢”。**

如果你要从这里继续往下推进，最合理的下一步是二选一：

1. 把这 50 篇文献进一步压缩成 `related work + gap + problem statement`
2. 直接基于它们生成一版 `FINAL_PROPOSAL + EXPERIMENT_PLAN`

## Source Links

- Applied Energy 2026 review: https://www.sciencedirect.com/science/article/pii/S0306261925018069
- Artificial Intelligence Review 2026 systematic review: https://link.springer.com/article/10.1007/s10462-026-11545-2
- Scientific Reports 2025 dispatch LLM: https://www.nature.com/articles/s41598-025-91940-x
- Foundation models for clean energy forecasting review: https://www.sciencedirect.com/science/article/pii/S1364032125011256
- BERT4ST: https://www.sciencedirect.com/science/article/pii/S0196890424002723
- Core 50-paper seed list in workspace: `IDEA_REPORT_LLM`
