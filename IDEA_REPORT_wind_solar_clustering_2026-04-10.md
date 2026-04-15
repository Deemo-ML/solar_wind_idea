# Idea Discovery Report

**Direction**: 风光出力聚类方法
**Date**: 2026-04-10
**Pipeline**: research-lit -> idea-creator -> novelty-check -> research-review -> research-refine-pipeline
**Non-destructive run**: 本次结果写入新文件，不覆盖现有 `IDEA_REPORT.md` 与既有 `refine-logs/`

## Executive Summary

围绕“风光出力聚类方法”，现有研究已经覆盖了典型场景提取、K-means/模糊聚类、图聚类、动态聚类、以及服务于超短期预测的站群聚类。单纯再做一个“更好的聚类指标”已经比较拥挤，尤其是只按曲线形状或均值相似性分群时，论文很容易退化成常规方法改进。

最值得推进的方向，是把聚类目标从“压缩数据”或“提升预测精度”推进到“保留调度与风险含义”。推荐题目因此不是普通风光场景聚类，而是**面向调度代价与极端风险保持的风光多视角风险约束协同聚类方法**：同时约束输出形态、爬坡/尾部事件、源荷失配和跨区域相关结构，让聚类结果直接服务于典型场景构造、备用评估和区域协同调度。

## Literature Landscape

### Representative papers

| Paper | Venue | What it adds | Gap left for us |
|---|---|---|---|
| *Wind and Photovoltaic Power Time Series Data Aggregation Method Based on an Ensemble Clustering and Markov Chain* | CSEE JPES, 2021 | 风光时序数据聚合，强调场景压缩与状态转移保持。 | 更偏“降维/仿真加速”，没有把聚类目标直接绑定到调度风险或代价。 |
| *Photovoltaic Solar Power Prediction Using iPSO-Based Data Clustering and AdaLSTM Network* | Energies, 2024 | 以聚类提升光伏预测鲁棒性。 | 是典型“聚类+预测器”路线，对联合风光与系统侧价值覆盖有限。 |
| *Weather Condition Clustering for Improvement of Photovoltaic Power Plant Generation Forecasting Accuracy* | Algorithms, 2024 | 通过天气条件聚类改善光伏预测。 | 聚类围绕天气标签与预测任务，不是面向电网运行的风光联合聚类。 |
| *A K-means cluster division of regional photovoltaic power stations considering the consistency of photovoltaic output* | Energy Reports, 2024 | 按区域光伏输出一致性进行站群划分。 | 主要是光伏单能源与静态一致性，缺少风光联合、极端事件与下游任务约束。 |
| *Ultra-Short-Term Photovoltaic Cluster Power Prediction Based on Photovoltaic Cluster Dynamic Clustering and Spatiotemporal Heterogeneous Dynamic Graph Modeling* | Electronics, 2025 | 动态聚类 + 时空图模型，服务于光伏簇功率预测。 | 任务仍是预测；“什么样的聚类最能保留调度意义”仍未回答。 |
| *Enhancing representative photovoltaic scenario extraction for multiple power stations with a shared-weight and adaptively fused graph clustering method* | Applied Energy, 2026 | 多站光伏代表场景图聚类，强调相关结构与鲁棒性。 | 仍主要针对光伏代表场景提取，缺少风光联合、多任务评价与极端风险保持。 |
| *A novel cluster partition method of hydro-wind-photovoltaic stations considering electrical-hydraulic connection and power output stability* | Electric Power Systems Research, 2026 | 在多能源站群中用网络/社区检测做分区。 | 更偏站群分区与连接关系，不是“对风光输出进行风险保持聚类”的通用方法。 |
| *Clustering of renewable energy assets to optimize resource allocation and operational strategies* | Journal of Intelligent Information Systems, 2025 | 按历史功率、气象与功率曲线对资产聚类。 | 资产管理导向明显，但没有系统性比较聚类结果对场景生成与调度指标的影响。 |

## Extended Literature List

| No. | Paper | Venue / Year | Category | Core idea | Relevance to our topic | Link |
|---|---|---|---|---|---|---|
| 1 | *Wind and Photovoltaic Power Time Series Data Aggregation Method Based on an Ensemble Clustering and Markov Chain* | CSEE JPES, 2021 | 风光联合聚类 / 场景压缩 | 用集成聚类与 Markov 链做风光时序聚合与状态保持 | 是风光联合出力聚类的直接基础文献，可作为经典 baseline | https://www.sciopen.com/article/10.17775/CSEEJPES.2020.03700 |
| 2 | *Modelling of wind and photovoltaic power output considering dynamic spatio-temporal correlation* | Applied Energy, 2023 | 风光联合相关建模 | 建模风光出力的动态时空相关性 | 虽非纯聚类，但支撑“为何需要联合建模而非单变量聚类” | https://www.sciencedirect.com/science/article/abs/pii/S0306261923013120 |
| 3 | *Short-term correlated probabilistic interval forecasting of wind-photovoltaic power based on improved ISODATA similar-day clustering and the IDBO-BiLSTM-copula method* | Electric Power Systems Research, 2026 | 风光联合 / 相似日聚类 | 用改进 ISODATA 相似日聚类支撑风光联合概率预测 | 很适合作为“相似日聚类”路线的直接相关文献 | https://www.sciencedirect.com/science/article/abs/pii/S0378779626003081 |
| 4 | *A Multi-Task Learning and GCN-Transformer-Based Forecasting Method for Day-Ahead Power of Wind-Solar Clusters* | Electronics, 2026 | 风光簇 / 预测前聚类 | 面向 wind-solar clusters 的日前功率预测 | 可支撑“风光簇”概念与联合建模背景 | https://www.mdpi.com/2079-9292/15/2/462 |
| 5 | *Enhancing representative photovoltaic scenario extraction for multiple power stations with a shared-weight and adaptively fused graph clustering method* | Applied Energy, 2026 | 图聚类 / 代表场景提取 | 用共享权重和自适应融合图聚类提取多站光伏代表场景 | 是“图聚类 + 典型场景”方向的强相关对照文献 | https://www.sciencedirect.com/science/article/pii/S0306261925020215 |
| 6 | *A K-means cluster division of regional photovoltaic power stations considering the consistency of photovoltaic output* | Sustainable Energy, Grids and Networks, 2024 | 站群划分 / K-means | 基于输出一致性对区域光伏站群进行聚类划分 | 可作为“区域电站分区聚类”基线参考 | https://www.sciencedirect.com/science/article/pii/S2352467724003035 |
| 7 | *Ultra-Short-Term Photovoltaic Cluster Power Prediction Based on Photovoltaic Cluster Dynamic Clustering and Spatiotemporal Heterogeneous Dynamic Graph Modeling* | Electronics, 2025 | 动态聚类 / 图建模 | 以动态聚类和异构动态图建模做光伏簇预测 | 非常适合支撑“静态聚类 vs 动态聚类”讨论 | https://www.mdpi.com/2079-9292/14/18/3641 |
| 8 | *Ultra-short-term prediction of photovoltaic cluster power based on spatiotemporal convergence effect and spatiotemporal dynamic graph attention network* | Renewable Energy, 2025 | 光伏簇 / 动态图 | 利用时空收敛效应和动态图注意力网络建模光伏簇 | 是动态聚类/簇级预测方向的重要补充 | https://www.sciencedirect.com/science/article/pii/S0960148125015071 |
| 9 | *A novel cluster partition method of hydro-wind-photovoltaic stations considering electrical-hydraulic connection and power output stability* | Electric Power Systems Research, 2026 | 多能互补站群分区 | 结合电-水连接与功率稳定性做多能站群分区 | 对“考虑物理约束与稳定性”的聚类设计很有启发 | https://www.sciencedirect.com/science/article/abs/pii/S0378779625012805 |
| 10 | *Enhancing stochastic optimization of wind-PV-storage systems: A scenario reconstruction approach with source-load matching and temporal characteristics* | Applied Energy, 2026 | 场景重构 / 源荷匹配 | 将源荷匹配与时间特征纳入风光储场景重构 | 很适合作为“聚类结果要服务系统任务”的支撑文献 | https://www.sciencedirect.com/science/article/pii/S0306261926003193 |
| 11 | *A Short-Term Power Prediction Method for Photovoltaics Based on Similar Day Clustering and Spatio-Temporal Feature Extraction* | Electronics, 2024 | 相似日聚类 / 光伏预测 | 通过相似日聚类与时空特征提取提升短期预测 | 适合补充“聚类作为预测前置模块”的路线 | https://www.mdpi.com/2079-9292/13/17/3536 |
| 12 | *Photovoltaic Power Prediction Based on Similar Day Clustering Combined with CNN-GRU* | Sustainability, 2025 | 相似日聚类 / 深度预测 | 将相似日聚类与 CNN-GRU 结合进行光伏预测 | 可作为相似日聚类常见实现范式参考 | https://www.mdpi.com/2071-1050/17/16/7383 |
| 13 | *Ultra-short-term photovoltaic power prediction based on similar day clustering and temporal convolutional network with bidirectional long short-term memory model* | Applied Energy, 2024 | 相似日聚类 / 光伏预测 | 用相似日聚类和 TCN-BiLSTM 进行超短期预测 | 可作为高质量期刊中的相似日路线代表 | https://www.sciencedirect.com/science/article/pii/S0306261924014685 |
| 14 | *Weather Condition Clustering for Improvement of Photovoltaic Power Plant Generation Forecasting Accuracy* | Algorithms, 2024 | 天气型聚类 | 基于天气条件聚类提升光伏预测精度 | 对你若做“天气型驱动聚类”很有帮助 | https://www.mdpi.com/1999-4893/17/9/419 |
| 15 | *Photovoltaic Solar Power Prediction Using iPSO-Based Data Clustering and AdaLSTM Network* | Energies, 2024 | 数据聚类 / 光伏预测 | 用 iPSO 聚类 + AdaLSTM 做功率预测 | 属于“聚类 + 预测器”标准路线，可作对照 | https://www.mdpi.com/1996-1073/17/7/1624 |
| 16 | *Power prediction of a wind farm cluster based on spatiotemporal correlations* | Applied Energy, 2021 | 风场簇 / 时空相关 | 通过时空相关性进行风场簇功率预测 | 可补齐“风电簇”方向 related work | https://www.sciencedirect.com/science/article/pii/S0306261921009466 |
| 17 | *Short-Term Wind Power Prediction for Wind Farm Clusters Based on SFFS Feature Selection and BLSTM Deep Learning* | Energies, 2021 | 风场簇 / 预测 | 用特征选择和 BLSTM 进行风场簇预测 | 适合作为风场簇预测侧对照文献 | https://www.mdpi.com/1996-1073/14/7/1894 |
| 18 | *Day-ahead wind farm cluster power prediction based on trend categorization and spatial information integration model* | Applied Energy, 2025 | 趋势分类 / 风场簇 | 按趋势分类并融合空间信息进行风场簇预测 | 可借鉴“先分类/分群再预测”的框架 | https://www.sciencedirect.com/science/article/abs/pii/S0306261925003101 |
| 19 | *A centralized power prediction method for large-scale wind power clusters based on dynamic graph neural network* | Energy, 2024 | 大规模风电簇 / 动态图 | 用动态图神经网络做大规模风电簇集中预测 | 为动态图和簇级建模提供补充证据 | https://www.sciencedirect.com/science/article/abs/pii/S0360544224029852 |
| 20 | *A new hybrid model for power forecasting of a wind farm using spatial-temporal correlations* | Renewable Energy, 2022 | 风电 / 聚类混合模型 | 结合时空相关和聚类思想进行风电功率预测 | 可补充较早的时空相关聚类思路 | https://www.sciencedirect.com/science/article/pii/S0960148122012101 |


## 风电光伏聚类相关文献整理

| Paper | Venue | What it adds | Gap left for us |
|---|---|---|---|
| *Wind and Photovoltaic Power Time Series Data Aggregation Method Based on Ensemble Clustering and Markov Chain* | CSEE JPES, 2022 | 对风光时序进行场景切分，采用集成聚类进行典型场景压缩，并利用 Markov 链保持状态转移特性，适合用于风光时序聚合与场景压缩。 | 更偏向时序压缩和仿真提速，没有直接将聚类目标与调度成本、弃风弃光风险或系统运行价值绑定。 |
| *面向可靠性评估的两阶段聚类风-光-荷典型场景生成方法* | 电工电能新技术, 2021 | 将风、光、荷联合纳入两阶段聚类框架，服务于可靠性评估，是风光荷联合典型场景提取的代表性工作。 | 重点仍在典型场景选取，对极端波动保持、调度鲁棒性保持和多任务评价涉及不足。 |
| *Long-term Scenario Generation of Renewable Energy Generation Using Attention-Based Conditional GANs* | Energy Conversion and Economics, 2024 | 面向相关风电与光伏输出的长期场景生成，可作为风光聚类前的场景生成基线或对照方法。 | 更偏向生成模型，不是直接研究聚类目标如何设计，也未突出调度风险保持。 |
| *A WGAN-GP-Based Scenarios Generation Method for Wind and Solar Power Complementary Study* | Energies, 2023 | 基于 WGAN-GP 生成风光互补场景，并结合 k-means 进行场景约简，强调风光互补性分析。 | 重点在风光互补与场景生成，聚类本身较基础，未系统讨论聚类结果对电网运行的价值。 |
| *A High Dimensional Uncertain Scenario Generating Method for Wind Power and Photovoltaic Considering Spatiotemporal Correlation* | Energy, 2025 | 针对多风光站高维场景，结合聚类降维与时空相关建模，兼顾多站点间时空耦合。 | 更偏向高维场景生成服务，尚未回答“怎样的聚类最能保留调度意义”这一核心问题。 |
| *Wind–Photovoltaic–Hydropower Joint Output Model Study Based on Probability Distribution and Correlation Analysis* | Energies, 2025 | 建立风光水联合输出模型，并利用 k-means 提取典型联合场景，适合多能互补研究。 | 聚类部分方法较基础，更多作为后续多能系统分析输入，而非独立聚类方法研究。 |
| *A Scenario Generation Method for Wind/PV Power Outputs and Load Sequences Preserving Extreme Scenario Characteristics* | IET Renewable Power Generation, 2026 | 面向风电、光伏和负荷联合场景生成，强调保留极端场景特征，对极端风险研究很有借鉴价值。 | 更偏场景生成而非严格意义上的聚类方法，但“保极值、保极端”的思想很值得引入聚类目标设计。 |
| *A K-means Cluster Division of Regional Photovoltaic Power Stations Considering the Consistency of Photovoltaic Output* | Sustainable Energy, Grids and Networks, 2024 | 按区域光伏站输出一致性进行站群划分，综合考虑时间、空间及站点特征，适合区域站群聚类研究。 | 主要针对光伏单能源与静态一致性分析，缺乏风光联合和系统侧价值刻画。 |
| *Photovoltaic Solar Power Prediction Using iPSO-Based Data Clustering and AdaLSTM Network* | Energies, 2024 | 采用“聚类 + 预测器”的思路，通过工况聚类提升光伏预测鲁棒性。 | 聚类主要服务于预测，未涉及风光联合聚类及其在调度、规划中的作用。 |
| *Weather Condition Clustering for Improvement of Photovoltaic Power Plant Generation Forecasting Accuracy* | Algorithms, 2024 | 通过天气条件聚类改善光伏出力预测精度，适合借鉴“天气型先验分层”的思路。 | 聚类围绕天气标签和预测任务展开，不是面向电网运行或风光联合场景的聚类方法。 |
| *Ultra-Short-Term Photovoltaic Cluster Power Prediction Based on Photovoltaic Cluster Dynamic Clustering and Spatiotemporal Heterogeneous Dynamic Graph Modeling* | Electronics, 2025 | 引入动态聚类识别光伏簇之间的平滑互补关系，并结合时空动态图模型进行预测。 | 动态聚类思想较强，但核心任务仍是预测，没有系统说明聚类如何保留调度价值。 |
| *Extraction of Representative Scenarios for Photovoltaic Power With Shared Weight Graph Clustering* | IEEE Transactions on Smart Grid, 2024 | 将图聚类方法引入光伏代表场景提取，能够更好保留相关结构和典型模式。 | 研究对象仍是光伏单能源，对风光联合场景和多下游任务约束覆盖不足。 |
| *A Novel Clustering Method for Extracting Representative Photovoltaic Scenarios Considering Power, Energy, and Variability* | IEEE Transactions on Power Systems, 2025 | 同时考虑功率、能量和波动性三个维度设计聚类目标，是多指标聚类的典型代表。 | 方法设计很值得借鉴，但仍局限于光伏单能源，没有扩展到风光联合。 |
| *Enhancing Representative Photovoltaic Scenario Extraction for Multiple Power Stations with a Shared-Weight and Adaptively Fused Graph Clustering Method* | Applied Energy, 2026 | 在共享权重图聚类基础上加入自适应融合，强调多站点相关结构、鲁棒性和抗噪性。 | 仍主要针对多站光伏代表场景提取，尚未扩展到风光联合、多任务评价与极端风险保持。 |
| *Distributed Photovoltaic Generation Aggregation Approach Considering Distribution Network Topology* | Energies, 2024 | 在聚类特征中引入配电网拓扑、电压敏感度和功率曲线，体现了“聚类服务电网任务”的思路。 | 对象主要是分布式光伏聚合，不是面向风光联合出力场景的通用聚类框架。 |
| *Clustering of Renewable Energy Assets to Optimize Resource Allocation and Operational Strategies* | Journal of Intelligent Information Systems, 2025 | 基于历史功率、气象与功率曲线特征对风机与光伏逆变器等资产进行聚类，偏资产运维视角。 | 更偏资产管理和运维优化，没有系统分析聚类结果对场景生成、调度指标的影响。 |
| *A Clustering-Based Scenario Generation Framework for Power Market Simulation with Wind Integration* | Journal of Renewable and Sustainable Energy, 2020 | 基于风场间相关性先分簇，再进行场景生成，适合用于市场仿真中的风电场景压缩。 | 只针对风电，缺乏光伏及多能源联合建模，也未关注调度风险保持。 |
| *Finding Representative Wind Power Scenarios and their Probabilities for Stochastic Models* | ISAP, 2011 | 通过聚类从大量风电场景中提取代表场景及其概率，是早期经典代表场景方法。 | 方法较早、相对基础，不适合直接处理当前多站风光高维时空相关问题。 |
| *A Clustering-Based Wind Power Scenario Reduction Technique* | PSCC, 2011 | 使用聚类从大规模风电场景中筛选少量代表性场景，为后续场景削减研究奠定基础。 | 主要适用于单一风电场景削减，难以直接适配风光联合和高维复杂场景。 |
| *Short-Term Wind Power Forecasting Based on Clustering Pre-Calculated CFD Method* | Energies, 2018 | 在复杂地形风场中通过风机聚类提升预测建模效率，体现设备级聚类思想。 | 更偏设备级或风机级预测，不是面向风光出力联合场景聚类的方法。 |
| *Wind Power Forecasting Method of Large-Scale Wind Turbine Clusters Based on DBSCAN Clustering and an Enhanced Hunter-Prey Optimization Algorithm* | Energy Conversion and Management, 2024 | 在大规模风机簇中引入 DBSCAN 聚类，再结合优化算法与预测模型，是风电“密度聚类 + 预测”路线代表。 | 依旧以预测为主要目标，缺少面向调度、规划和风险保持的分析。 |
| *Wind Farm Cluster Power Prediction Based on Graph Deviation Attention Network with Learnable Graph Structure and Dynamic Error Correction* | Energy, 2024 | 面向风场簇的图结构建模与簇级预测，体现“风场簇 + 图模型”的研究思路。 | 对风场簇预测有参考价值，但没有扩展到风光联合聚类与场景保持。 |
| *Representative Days for Expansion Decisions in Power Systems* | Energies, 2020 | 在代表日选择中强调保留负荷和可再生出力的极值，对风光典型日聚类很有方法启发。 | 不是专门的风光聚类论文，但对“聚类不能只保平均，还要保极端”这一点很有价值。 |
| *Improvement of Representative Days Selection in Power System Planning by Incorporating the Extreme Days of the Net Load* | Applied Energy, 2020 | 在代表日聚类中显式加入极端净负荷日，提高对系统极端运行状态的保真能力。 | 更偏规划中的代表日选择，不是专门的风光联合出力聚类。 |

## 可以进一步提炼出的研究空白

| 方向 | 当前已有工作 | 仍然存在的不足 |
|---|---|---|
| 风光联合聚类 | 已有部分工作开始对风光联合场景进行生成或典型场景提取。 | 高质量文献中仍以单一能源（尤其光伏）为主，真正面向风光联合聚类的方法还不够多。 |
| 聚类目标设计 | 已开始考虑功率、能量、波动性、相关性等多维特征。 | 很少直接把聚类目标和调度成本、弃风弃光、可靠性风险等系统指标绑定。 |
| 极端场景保持 | 有些代表日、场景生成工作已经关注极值和极端日。 | 极端爬坡、长时低出力、连续阴天弱风等关键运行风险保持仍不足。 |
| 动态与时空相关 | 部分工作已经引入动态图、图聚类、时空相关建模。 | 缺少统一框架来同时保持时间连续性、空间相关性和系统运行价值。 |
| 下游任务闭环评价 | 多数工作在预测、场景生成或站群划分上已有验证。 | 缺乏“同一聚类结果在预测、调度、规划、可靠性多个任务上的统一评价体系”。 |

### Landscape conclusions

- 现有风光聚类工作大致分成三条线：`典型场景压缩`、`预测前分群`、`站群/资产分区`。
- 2025-2026 年的新工作开始更多使用图聚类、动态聚类、多站相关建模，说明“只做 K-means”已不够新。
- 但多数方法仍以“聚类内部紧致、外部分离、预测误差降低、场景数减少”为目标。
- 真正缺的不是再造一个距离，而是回答：**聚类以后，是否仍然保留了系统最关心的风险小时、爬坡事件、源荷失配与调度代价结构？**
- 因此，新论文最有希望的切口是：把聚类的“评价函数”从统计相似性改成“统计相似性 + 系统任务保持性”。

### Source links

- https://www.sciopen.com/article/10.17775/CSEEJPES.2020.03700
- https://www.mdpi.com/1996-1073/17/7/1624
- https://www.mdpi.com/1999-4893/17/9/419
- https://www.sciencedirect.com/science/article/pii/S2352467724003035
- https://www.mdpi.com/2079-9292/14/18/3641
- https://www.sciencedirect.com/science/article/pii/S0306261925020215
- https://www.sciencedirect.com/science/article/abs/pii/S0378779625012805
- https://link.springer.com/article/10.1007/s10844-024-00914-4

## Ranked Ideas

### Idea 1: 面向调度代价与极端风险保持的风光多视角风险约束协同聚类 - RECOMMENDED

- **核心问题**: 现有风光聚类大多只保留“平均形状相似”，却会丢掉真正影响系统运行的低出力连续段、联合爬坡、残余负荷尖峰和跨区协同关系。
- **方法直觉**: 把每个风光样本日/样本周表示为四个视角：`归一化出力曲线`、`爬坡与波动特征`、`源荷失配/残余负荷特征`、`跨区域相关/互补特征`，再做多视角协同聚类；聚类目标不仅最小化簇内距离，还最小化下游调度指标失真。
- **最小实验**: 用省级或站级小时风电、光伏、负荷数据构造样本日；对比 K-means、DTW-k-medoids、ECMC、现有图聚类和本方法。评价包括场景压缩误差、概率潮流误差、CVaR 保持、爬坡分布保持、备用需求误差、简化调度成本 gap。
- **预期结果**: 在相同簇数下，本方法对极端低风低光事件、残余负荷尾部和调度成本的保持优于纯统计聚类。
- **Novelty**: 8.8/10。聚类本身不新，但“多视角 + 风险约束 + 下游调度保持”这个组合仍有明显空间。
- **Feasibility**: 中等。主要难点在评价体系设计，不必先上很重的优化器。
- **Risk**: 中等。若下游指标提升不明显，容易被质疑为损失函数工程。
- **Contribution type**: 方法 + 评测框架。
- **Pilot result**: SKIPPED。当前工作区无可直接运行的风光小时级数据集。
- **Reviewer's likely objection**: “你只是给聚类目标多加了几个权重，是否真有方法论贡献？”
- **为什么值得做**: 它把论文从“聚类算法改良”抬升到“面向电力系统任务的聚类原则设计”。

### Idea 2: 面向季节转换与天气型切换的风光动态聚类图

- **核心问题**: 静态聚类默认全年共享同一相似关系，但风光出力在季节与天气型切换时常常重构相关网络。
- **方法直觉**: 用天气型/季节隐状态驱动动态图聚类，让“谁和谁属于同一簇”可以随月份或天气机制变化。
- **最小实验**: 比较静态聚类与动态聚类在四季、寒潮、连续阴天、低风速期上的代表性保持能力。
- **Novelty**: 8.1/10。
- **Risk**: 中高。若数据规模有限，动态图容易显得过重。
- **为什么是备选**: 新颖度不错，但更依赖天气再分析数据和状态切换设计。

### Idea 3: 面向跨区域协同调度的风光双层聚类与走廊选择

- **核心问题**: 现有聚类通常只聚“时序”或只聚“站点”，没有同时回答“哪些地区应归为一类”和“哪些典型日最代表这些地区的协同关系”。
- **方法直觉**: 上层做区域/场站协同聚类，下层做簇内代表日提取，形成可直接输入区域调度或输电规划的双层聚类结果。
- **最小实验**: 在省际或站群级数据上比较双层聚类与单层典型日方法对跨区潮流、弃电与备用配置的解释能力。
- **Novelty**: 7.9/10。
- **Risk**: 中等。
- **为什么是备选**: 更偏应用框架，投稿时可能被认为方法深度略弱。

## Eliminated Ideas

| Idea | Reason eliminated |
|---|---|
| 单纯提出一个新的风光聚类距离或指标 | 太容易落入“又一个相似度”的拥挤赛道。 |
| 只做光伏簇或只做风电簇的预测前分群 | 文献已经很多，且与“风光联合出力”主题不够一致。 |
| 先做超复杂 GNN 再用其隐向量聚类 | 容易把论文重心转成预测模型，聚类贡献反而被淹没。 |
| 纯场景压缩论文，不接系统侧任务 | 新意不足，尤其面对 2025-2026 年图聚类场景提取论文时竞争力偏弱。 |

## Deep Novelty Check for the Top Idea

已有工作已经证明：

- 风光时序可以通过集成聚类、Markov 链等方式做代表场景压缩；
- 光伏多站相关性可以通过图聚类更好建模；
- 动态聚类可服务于站群超短期预测；
- 站群分区可以引入物理连接与输出稳定性。

因此，**Top idea 的新意不能落在“用了图聚类”或“用了多特征”本身**。它保持新颖的前提是：

- 明确把目标定义为 `risk-preserving clustering` 或 `dispatch-aware clustering`；
- 证明聚类后保留的不是一般统计量，而是 `CVaR / ramp / residual-load / reserve-demand / dispatch-cost gap`；
- 给出统一评测协议，显示现有方法在风险小时上的失真，而新方法显著更稳。

如果最终只做“多特征加权聚类 + 常规轮廓系数对比”，那就不够新。

## Critical Review of the Top Idea

### Strengths

- 方向贴合新型电力系统场景，能把聚类从数据预处理提升为调度工具。
- 与现有图聚类/动态聚类工作形成差异，不必正面拼谁的预测误差更低。
- 可以先做轻量下游验证，再决定是否扩展到概率潮流或 UC/ED。

### Main weaknesses

- 论文成败高度依赖“下游保持指标”定义得是否漂亮且可信。
- 如果没有负荷数据或简化调度器，容易被质疑“调度导向只是口号”。
- 多视角设计过多会让方法显得堆料，需要有一个非常清晰的主线。

### Internal reviewer score

- **Before refinement**: 8.2/10
- **After refinement**: 9.0/10

## Refined Proposal

- Proposal: `refine-logs-wind-solar-clustering-20260410/FINAL_PROPOSAL.md`
- Experiment plan: `refine-logs-wind-solar-clustering-20260410/EXPERIMENT_PLAN.md`
- Tracker: `refine-logs-wind-solar-clustering-20260410/EXPERIMENT_TRACKER.md`

## Next Steps

- [ ] 明确研究对象：省级区域聚类、站群聚类，还是样本日聚类
- [ ] 确定下游保持目标：`CVaR`、`ramp`、`residual load`、`reserve demand` 至少选 2-3 个
- [ ] 准备小时级风电、光伏、负荷数据，并定义训练/验证年份
- [ ] 先复现 `K-means / DTW-k-medoids / ECMC / graph clustering` 作为基线
- [ ] 用小规模调度代理模型验证“同样簇数下是否更保真”
