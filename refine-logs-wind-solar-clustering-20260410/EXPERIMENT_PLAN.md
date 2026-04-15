# Experiment Plan

**Project**: 风光出力聚类方法
**Top idea**: 面向调度代价与极端风险保持的风光多视角风险约束协同聚类
**Date**: 2026-04-10

## Claim 1

传统风光聚类方法在相同压缩率下，无法稳定保留极端低出力、强爬坡和源荷失配结构。

### Evidence needed

- 聚类前后 `tail hours` 覆盖率差异
- 聚类前后 `ramp distribution` 距离
- 聚类前后 `residual-load CVaR` 误差

### Baselines

- K-means
- K-medoids / DTW-k-medoids
- ECMC 类时序聚合基线
- 代表性图聚类基线

## Claim 2

多视角风险约束协同聚类，比纯统计相似性聚类更适合作为下游调度/规划的代表场景输入。

### Evidence needed

- 简化调度成本 gap
- 备用需求估计误差
- 概率潮流或净负荷分布保持误差

## Datasets

### Minimum viable dataset

- 小时级风电出力
- 小时级光伏出力
- 小时级负荷
- 时间跨度建议至少 2-3 年

### Optional extensions

- 天气再分析变量
- 省际输电约束
- 多区域标签

## Feature Blocks

1. 形状特征
2. 波动与爬坡特征
3. 尾部风险特征
4. 源荷失配特征
5. 跨区域相关/互补特征

## Experiment Blocks

### Block A: 数据与基线复现

- 清洗并标准化风电、光伏、负荷时间序列
- 划分样本日
- 复现 K-means、DTW-k-medoids、ECMC、图聚类

### Block B: 评价协议建立

- 定义重构方式
- 定义压缩率与簇数范围
- 实现 tail-risk、ramp、CVaR、备用需求误差指标

### Block C: 主方法实现

- 实现多视角特征融合
- 实现风险约束协同聚类目标
- 做消融：去掉 risk term / 去掉 task term / 去掉 cross-region term

### Block D: 下游验证

- 轻量简化调度器或代理成本函数
- 比较各聚类结果输入下的成本 gap
- 分析极端样本恢复能力

## Ablations

- 仅形状视角
- 形状 + 爬坡
- 形状 + 爬坡 + 源荷失配
- 完整模型
- 静态版本 vs 动态版本

## Run Order

1. 数据检查与样本日构造
2. 基线聚类复现
3. 指标实现与 sanity check
4. 主方法最简版本
5. 风险项消融
6. 调度代理验证

## Success Criteria

- 在至少 2 个风险指标上显著优于 K-means / DTW-k-medoids
- 在相同簇数下获得更小的调度代理误差
- 结论对不同年份切分基本稳定

## Failure Conditions

- 相比简单基线无显著收益
- 收益仅来自更大模型复杂度，解释性不足
- 没有负荷或下游任务数据，无法支撑“调度导向”主张
