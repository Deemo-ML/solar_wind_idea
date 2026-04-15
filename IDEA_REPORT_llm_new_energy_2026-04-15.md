# Idea Discovery Report

**Direction**: 大语言模型在新能源领域的应用
**Date**: 2026-04-15
**Pipeline**: research-lit -> idea-creator -> novelty-check -> research-review
**Mode**: non-destructive literature-driven run

## Executive Summary

2025-2026 年，“LLM 直接用于风电/光伏功率预测”已经快速拥挤：风电、光伏、概率预测、零样本/小样本预测、跨场站泛化、多模态天空图像融合等方向都已出现代表性工作。继续做“把通用 LLM 接到数值时序上做预测”的论文，创新门槛已经明显抬高。

更值得投入的方向，是让 LLM 从“预测器”转向“新能源业务协同层”：把设备文档、调度规则、告警日志、SCADA 摘要、气象说明、专家经验和优化器结果连接起来，做面向调度与运维的可解释决策助手。基于当前文献密度、差异化空间和你现有风光研究背景，最推荐的方向是：

**面向风光场站群协同调度与消纳的检索增强、规则约束 LLM Copilot。**

## Literature Landscape

### 1. 近期文献图谱

| 类别 | 代表工作 | 时间 | 说明 | 对我们意味着什么 |
|---|---|---:|---|---|
| 综合综述 | *Large Language Models Meet Energy Systems: Opportunities, Challenges, and Future Perspectives* | 2026 | 系统梳理 LLM 在能源系统中的 13 类角色与 5 类增强技术 | 说明该方向已从“点状尝试”进入“系统梳理”阶段 |
| 综合综述 | *Generative AI and LLM applications in renewable energy and smart grids* | 2026 | 汇总 106 篇研究，覆盖 forecasting、operation、reliability、market 等 7 类任务 | 表明“新能源+LLM”已经成体系，选题必须更聚焦 |
| 风电预测 | *PowerMistral: A data-efficient wind power forecasting framework leveraging pre-trained large language models* | 2026 | 小样本风电预测 | 预测赛道已卷到 few-shot |
| 风电预测 | *Modality Alignment-Driven large language model for wind farm power forecasting* | 2026 | 做模态对齐以缓解数值时序与文本空间不匹配 | “数值序列如何喂给 LLM”已是显学 |
| 风电预测 + 调度 | *PEFT-based large language model for wind power forecasting and risk-tunable energy scheduling in microgrids* | 2026 | 预测与微网调度联动 | 已有人把预测结果向调度场景延伸 |
| 光伏预测 | *Ultra-short-term photovoltaic power prediction based on reprogrammed large language models* | 2026 | 超短期光伏预测 | 说明光伏预测也已有 LLM 专项工作 |
| 光伏概率预测 | *Probabilistic prediction of photovoltaic power: A multi-task learning and large language model-based approach* | 2026 | 周尺度概率预测 | 纯“LLM+预测”很难再靠任务定义取胜 |
| 调度助手 | *A large language model for advanced power dispatch* | 2025 | 面向电力调度任务构建领域 LLM 与 ElecBench 评测 | “新能源+LLM”往调度助手演进是明确趋势 |
| 多模态新能源预测 | *Solar-VLM: Multimodal Vision-Language Models for Augmented Solar Power Forecasting* | 2026 | 卫星/图像/时序融合 | 多模态新能源预测开始形成新分支 |

### 2. 关键结论

- `LLM 直接做数值预测` 已不再稀缺，尤其风电/光伏短期预测方向文献增长很快。
- 目前真正相对稀缺的是 `LLM + 检索增强 + 规则/知识约束 + 实际业务闭环`。
- 新能源场景最自然的落点不是让 LLM 替代数值模型，而是让它成为 `解释层、协同层、交互层、知识组织层`。
- 如果论文只证明 “LLM 比 Transformer 预测更准”，很容易被质疑为换底座、拼调参、缺少行业增量。
- 如果论文能证明 `LLM 帮助做更快、更稳、更可解释的运维/调度决策`，新意和应用价值会同时更强。

### 3. 仍然存在的结构性空白

- 缺少面向 `风光场站群协同调度/消纳` 的 LLM 专用任务定义与公开 benchmark。
- 缺少把 `电网运行规程、并网规则、设备手册、场站日志、历史处置单` 统一纳入的检索增强框架。
- 缺少证明 `LLM 输出在安全边界内可控` 的规则约束与评测协议。
- 缺少 “LLM 负责解释与决策草案，优化器/规则引擎负责约束校验” 的新能源闭环框架。

## Ranked Ideas

### Idea 1: 面向风光场站群协同调度与消纳的检索增强规则约束 LLM Copilot - RECOMMENDED

- **核心假设**: 在高比例新能源场景中，真正缺的不是又一个预测模型，而是能够把预测结果、限电规则、设备状态、气象扰动、场站告警和调度经验统一起来的“协同决策助手”。
- **方法轮廓**:
  - 用 RAG 接入场站运行规程、并网规范、调度日志、故障处置单、设备说明书。
  - 将风电/光伏预测结果、负荷/电价、告警摘要、场站状态编码为结构化上下文。
  - 用规则约束模块对 LLM 的建议做安全校验，例如越限动作、并网约束、爬坡约束、储能功率边界。
  - 输出内容不是“直接控制”，而是 `调度建议 + 原因链条 + 风险说明 + 候选动作排序`。
- **最小实验**:
  - 构建一个 `新能源调度问答/决策` 数据集，任务包含限电原因分析、弃风弃光缓解建议、故障联动处置、跨场站协同建议。
  - 对比 `纯 LLM`、`RAG-LLM`、`RAG + 规则校验`、`小模型分类器/检索基线`。
  - 评价 factuality、rule compliance、actionability、latency、expert preference。
- **预期结果**:
  - RAG + 规则约束能显著减少幻觉和违规建议。
  - 在复杂新能源事件分析上优于纯检索和纯生成。
- **Novelty**: 8.9/10
- **Feasibility**: 中等偏高。需要整理文档、日志和规则，但不一定需要大规模 GPU 训练。
- **Risk**: 主要风险在于高质量案例数据集构建成本较高。
- **Contribution type**: 系统框架 + 数据集/benchmark + 安全评测协议
- **Why this is the top idea**: 它避开了最拥挤的“LLM 做预测”赛道，同时又能充分利用新能源领域的真实痛点。

### Idea 2: 面向风光场站故障诊断与运维处置的多源知识增强 LLM Agent - BACKUP

- **核心假设**: 新能源运维中最难的不是单点告警识别，而是把告警、波形、SCADA 摘要、维护手册和历史工单串成一条可执行处置路径。
- **方法轮廓**:
  - 将告警码、时序片段统计特征、检修记录、设备手册、巡检文本统一成可检索知识库。
  - LLM 完成根因归纳、处置建议生成、证据引用、工单草拟。
  - 引入“必须引用证据”的 grounded generation。
- **最小实验**:
  - 在逆变器、箱变、风机偏航/变桨、通讯异常等常见故障上做 case benchmark。
  - 比较人工规则库、BM25 检索、RAG-LLM、RAG-LLM + 工具调用。
- **Novelty**: 8.4/10
- **Feasibility**: 高。尤其适合企业/实验室有历史工单和手册时。
- **Risk**: 如果没有真实运维文本，论文容易退化成 demo。
- **Contribution type**: 应用系统 + grounded diagnosis benchmark

### Idea 3: 多模态 VLM/LLM 驱动的低样本光伏预测与天气事件解释 - BACKUP

- **核心假设**: 光伏预测的下一波增量不在“再换一个时序 backbone”，而在于把天空图像、卫星云图、气象文本、数值预报和功率曲线统一建模，并显式生成天气事件解释。
- **方法轮廓**:
  - 用视觉编码器提取天空图像/卫星图。
  - 用 LLM/VLM 对天气演化生成可解释事件描述。
  - 与数值时序 backbone 联合训练，目标同时包含预测误差和解释一致性。
- **最小实验**:
  - 比较时序-only、图像+时序、多模态+文本解释。
  - 强调低样本场站迁移与极端天气鲁棒性。
- **Novelty**: 7.9/10
- **Feasibility**: 中等。数据和工程都较重。
- **Risk**: 与近期 Solar-VLM、PV-VLM 一类工作距离较近，必须在“解释”和“低样本迁移”上拉开差异。

### Idea 4: 面向新能源调度问答与事件推理的领域 Benchmark 与 Safety Evaluation - BACKUP

- **核心假设**: 目前新能源领域缺的不是更多“案例展示”，而是一个可重复、可比较、可度量安全性的评测基准。
- **方法轮廓**:
  - 设计任务集：异常天气解释、限电原因归因、并网约束问答、故障处置排序、跨场站协同建议。
  - 设置 factuality、rule compliance、hallucination rate、unsafe-action rate、citation correctness 等指标。
- **Novelty**: 8.1/10
- **Feasibility**: 高
- **Risk**: 偏 benchmark/资源论文，方法贡献较弱。
- **Contribution type**: 数据集 + 评测基准

## Eliminated Ideas

| Idea | Reason eliminated |
|---|---|
| 直接把通用 LLM 用于风电/光伏短期预测 | 2025-2026 年文献已明显拥挤，容易被质疑只是换 backbone |
| 做一个“新能源大模型综述” | 已有 2026 年系统综述，除非做中文产业报告，否则学术增量不足 |
| 让 LLM 直接输出新能源实时控制动作 | 安全风险过高，且论文评审会强烈质疑可控性与合规性 |
| 只做“文档问答机器人” | 工程价值有，但学术贡献偏弱，缺少硬评测与方法创新 |

## Deep Novelty Check for the Top Idea

当前文献已经证明两件事：

1. `LLM/大时序模型` 用于风电、光伏预测是可行的。
2. `领域 LLM` 用于电力调度问答与辅助决策也是可行的。

但两者之间仍有明显空白：**针对新能源高渗透场景，把预测、告警、规则、日志、设备知识和调度建议真正闭环起来的“安全可控协同 Copilot”还没有形成成熟范式。**

因此，Top idea 的新颖性必须建立在下面三个点同时成立：

- 不是泛电网问答，而是明确聚焦 `风光场站群协同调度/消纳`；
- 不是纯生成，而是 `检索增强 + 规则约束 + 可追溯证据`；
- 不是 demo，而是有一套 `安全性与行动可用性评测协议`。

如果缺少这三点中的任意一点，论文就容易退化成“电力版聊天机器人”。

## Critical Review of the Top Idea

### Strengths

- 避开了最拥挤的 LLM 数值预测赛道。
- 与新能源行业真实需求高度一致，应用说服力强。
- 可与现有预测模型、优化器、规则库自然拼接，利于做系统论文。
- 即使模型本体不大，也能靠任务设计、数据构建和安全评测形成贡献。

### Main Weaknesses

- 如果没有真实运行日志或规程文档，容易停留在概念层。
- 需要非常明确地区分“建议生成”和“自动控制”，否则会被安全性质疑。
- 若评测只用通用 NLP 指标，论文会显得不够电力/新能源。

### Internal Reviewer Score

- **Before refinement**: 8.3/10
- **After scope control**: 9.0/10

## Refined Proposal Sketch

**题目草案**:
`A Retrieval-Augmented and Rule-Constrained LLM Copilot for Renewable Plant Cluster Dispatch Assistance`

**问题锚点**:
在高比例风光并网条件下，调度和运维人员面对的信息源高度异构，现有方法难以把预测、规程、告警、设备知识和历史经验统一成可追溯、可约束、可执行的建议。

**方法主张**:
让 LLM 负责跨模态知识整合与解释生成，让规则引擎/校验器负责安全边界，让优化器负责候选动作验证，形成“生成 - 校验 - 反馈”的新能源协同 Copilot。

**最小可发表版本**:
- 一个新能源事件决策 benchmark
- 一个 RAG + rule-checking baseline system
- 一组围绕 factuality / compliance / actionability 的评测

## Next Steps

- [ ] 明确聚焦场景：`场站运维` 还是 `场站群调度`
- [ ] 盘点可用数据：规程、告警、工单、场站说明书、历史调度记录
- [ ] 先做 50-100 个高质量案例的小型 benchmark
- [ ] 搭第一版 `RAG + rules + citation` 原型
- [ ] 再决定是否扩展到 agent/tool-use 或多模态输入

## Source Links

- Applied Energy 2026 review: https://doi.org/10.1016/j.apenergy.2025.127076
- Artificial Intelligence Review 2026 systematic review: https://link.springer.com/article/10.1007/s10462-026-11545-2
- Scientific Reports 2025 GAIA dispatch LLM: https://www.nature.com/articles/s41598-025-91940-x
- Applied Energy 2026 PowerMistral: https://www.sciencedirect.com/science/article/pii/S0306261926002771
- Chinese Journal of Mechanical Engineering 2026 wind forecasting with modality alignment: https://www.sciencedirect.com/science/article/pii/S1000934526000076
- Renewable Energy 2026 PEFT + scheduling: https://www.sciencedirect.com/science/article/pii/S0960148126001229
- IJEPES 2026 PV forecasting with reprogrammed LLM: https://www.sciencedirect.com/science/article/pii/S0142061526000840
- Renewable Energy 2026 probabilistic PV forecasting: https://www.sciencedirect.com/science/article/pii/S0960148125016684
