# Experiment Tracker

**Project**: 风光出力聚类方法
**Created**: 2026-04-10

## Status

- [x] 选题完成
- [x] 初步文献地形梳理完成
- [x] Top idea 确定
- [x] Proposal 初稿完成
- [x] Experiment plan 初稿完成
- [ ] 数据源确定
- [ ] 基线实现
- [ ] 主方法实现
- [ ] 消融实验
- [ ] 下游验证

## Immediate TODO

- [ ] 确定数据口径：省级还是站级
- [ ] 确定样本对象：样本日、样本周或站点-日
- [ ] 确定最小评价集：`CVaR`、`ramp`、`residual load`
- [ ] 建立 3 个最小基线

## Notes

- 当前工作区没有可直接用于 pilot 的现成数据，因此本轮为 paper-idea 与 experiment-design 级别输出。
- 如果后续进入实现，建议优先先做“样本日级别静态版本”，不要一开始就上动态图或复杂深度模型。
