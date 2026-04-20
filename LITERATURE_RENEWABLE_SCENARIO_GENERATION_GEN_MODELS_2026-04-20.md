# 基于生成模型的可再生能源场景生成文献清单

更新日期：2026-04-20

主题范围：风电 / 光伏 / 联合可再生能源出力场景生成，重点覆盖 `GAN / VAE / IMLE / Normalizing Flow / Diffusion / LLM`

说明：
- 这份清单按 `idea-discovery` 工作流的 Phase 1 文献调研来整理，目标是先把研究版图铺开。
- 我优先保留“直接做场景生成”的论文；少量“LLM/文本条件时间序列生成”相邻工作单独放在最后，便于后续构思新 idea。
- 部分条目是 2025-2026 年的 very recent 论文或预印本；以下日期均以 2026-04-20 可检索到的信息为准。

## 一页结论

1. 这条线已经从早期 `GAN` 主导，逐步演进到 `controllable GAN -> conditional latent diffusion -> text/natural-language-guided generation`。
2. 直接面向风电/光伏场景生成的主线文献里，2024 以后最活跃的是 `diffusion`。
3. 真正把 `LLM` 用到“可再生能源场景生成”的论文还很少。截至 2026-04-20，我检到的更像是两条支线：
   - `LLM -> 语义条件/自然语言条件 -> 场景生成`
   - `LLM -> 通用时间序列合成`
4. 如果后面要做新 idea，最自然的切口不是“再做一个普通 diffusion”，而是：
   - `自然语言可控场景生成`
   - `极端事件 / rare pattern / zero-shot pattern generation`
   - `风光联合、多站点、多模态条件`
   - `few-shot / cold-start 新场站场景生成`

## 1. 综述与入口论文

| 年份 | 论文 | 方法/定位 | 备注 | 链接 |
|---|---|---|---|---|
| 2023 | A Review of Solar Power Scenario Generation Methods with Focus on Weather Classifications, Temporal Horizons, and Deep Generative Models | 综述 | 很适合当入口文献；系统梳理了 solar scenario generation 与 deep generative models | https://doi.org/10.3390/en16155600 |
| 2026 | Large language models in renewable energy systems: A comprehensive review of forecasting, control, policy, and fault diagnosis | LLM+能源系统综述 | 不是专门讲 scenario generation，但能帮助判断 LLM 在能源领域的位置 | https://doi.org/10.1016/j.nxener.2026.100586 |

## 2. 经典生成模型主线：GAN / VAE / IMLE / Flow

| 年份 | 论文 | 方法 | 任务/对象 | 备注 | 链接 |
|---|---|---|---|---|---|
| 2018 | Model-Free Renewable Scenario Generation Using Generative Adversarial Networks | GAN | 风电+光伏联合场景生成 | 早期代表作，很多后续论文都会引用 | https://doi.org/10.1109/TPWRS.2018.2794541 |
| 2018 | Conditional Variational Automatic Encoder Method for Stochastic Scenario Generation of Wind Power and Photovoltaic System | CVAE | 风电+光伏 | 中文期刊方向，较早把 VAE 用到风光随机场景生成 | https://eurekamag.com/research/104/691/104691184.php |
| 2022 | CWM-CGAN Method for Renewable Energy Scenario Generation Based on Weather Label Multi-Factor Definition | CGAN | 光伏/可再生场景生成 | 明确把天气标签作为条件信息 | https://doi.org/10.3390/pr10030470 |
| 2022 | Data-driven scenario generation of renewable energy production based on controllable generative adversarial networks with interpretability | Controllable GAN | 风电+光伏联合 | 可控、可解释 latent manifold，是很关键的一篇 | https://doi.org/10.1016/j.apenergy.2021.118387 |
| 2022 | Scenario Generations for Renewable Energy Sources and Loads Based on Implicit Maximum Likelihood Estimations | IMLE | 可再生能源与负荷曲线 | 非 GAN 路线的重要代表，常被拿来和 GAN/VAE 比 | https://doi.org/10.35833/MPCE.2022.000108 |
| 2022 | Normalizing flow-based day-ahead wind power scenario generation for profitable and reliable delivery commitments by wind farm operators | Normalizing Flow | 风电 day-ahead 场景生成 | `flow` 路线代表作，结合 forecast information | https://doi.org/10.1016/j.compchemeng.2022.107923 |
| 2023 | Two-stage scheduling of integrated energy systems based on a two-step DCGAN-based scenario prediction approach | DCGAN | 综合能源系统场景预测/调度 | 更偏应用，但 DCGAN 场景生成部分可当 baseline 参考 | https://doi.org/10.3389/fenrg.2022.1012367 |
| 2023 | Conditional Style-Based Generative Adversarial Networks for Renewable Scenario Generation | StyleGAN / conditional GAN | 可再生能源场景生成 | Style-based 路线，直接对标更强的可控性与时空动态刻画 | https://doi.org/10.1109/TPWRS.2022.3170992 |
| 2024 | Short-Term Output Scenario Generation of Renewable Energy Using Transformer-Wasserstein Generative Adversarial Nets-Gradient Penalty | Transformer-WGAN-GP | 可再生能源短期出力场景生成 | Transformer + WGAN-GP，偏工程化 | https://doi.org/10.3390/su162410936 |
| 2024 | A Cross-Modal Generative Adversarial Network for Scenarios Generation of Renewable Energy | Cross-modal GAN | 光伏/风电场景生成 | 强调多模态观测与 spatial-temporal transformer | https://doi.org/10.1109/TPWRS.2023.3277698 |
| 2024 | Generation method of wind power and photovoltaic output scenarios based on LHS-GRU | LHS + GRU | 风电+光伏场景生成 | 严格说不属于深生成模型主流，但常见于对比实验 | https://doi.org/10.1016/j.segan.2024.101602 |
| 2025 | Wind Power Scenario Generation Based on the Generalized Dynamic Factor Model and Generative Adversarial Network | GDFM + GAN | 多风场长期风电场景生成 | 更强调 spatial/frequency correlation | https://doi.org/10.1109/TPWRS.2025.3615610 |
| 2025 | Wind-Photovoltaic Power Generation Scenario Generation Based on VAE-DCGAN | VAE-DCGAN | 风电+光伏 | 近期会议论文，可作为轻量 hybrid baseline | https://doi.org/10.1109/ICOECAI67333.2025.11335780 |
| 2026 | Two-stage scenario generation of hydro-wind-solar complementary system based on improved variational autoencoder and generative adversarial networks model | Improved VAE + GAN | 水-风-光联合场景生成 | 把场景生成扩展到 hydro-wind-solar complementary system | https://doi.org/10.1016/j.renene.2026.125358 |
| 2026 | A solar radiation data generation method for solar energy utilization scenarios: BIPV generation forecasting as a case study | UAGAN / gray-box GAN | 太阳辐照生成 | 不直接生成功率，而是生成辐照场景，物理含义更强 | https://doi.org/10.1016/j.renene.2025.124772 |

## 3. 近两年的主战场：Diffusion 系列

| 年份 | 论文 | 方法 | 任务/对象 | 备注 | 链接 |
|---|---|---|---|---|---|
| 2024 | Short-Term Wind Power Scenario Generation Based on Conditional Latent Diffusion Models | Conditional Latent Diffusion | 风电短期场景生成 | 这条线里非常关键的一篇，值得优先细读 | https://doi.org/10.1109/TSTE.2023.3327497 |
| 2025 | Generative probabilistic forecasting of wind power: A Denoising-Diffusion-based nonstationary signal modeling approach | Diffusion + nonstationary modeling | 风电概率预测/场景生成邻近任务 | 更偏 probabilistic forecasting，但方法可迁移到 scenario generation | https://doi.org/10.1016/j.energy.2025.134576 |
| 2025 | A Novel Renewable Energy Scenario Generation Method Based on Multi-Resolution Denoising Diffusion Probabilistic Models | Multi-resolution DDPM | 风电+光伏联合场景生成 | 多尺度分解 + cascaded diffusion | https://doi.org/10.3390/en18143781 |
| 2025 | Controllable renewable energy scenario generation based on pattern-guided diffusion models | Pattern-guided latent diffusion | 风电+光伏联合、可控场景生成 | few-shot / zero-shot pattern generation 很有启发性 | https://doi.org/10.1016/j.apenergy.2025.126446 |
| 2025 | An Improved Renewable Energy Scenario Generation Method Based on Cross-Attention Latent Diffusion Models with Controllability | Cross-attention latent diffusion | 风电+光伏联合、可控场景生成 | SSRN 预印本，强调 richer conditional information | https://papers.ssrn.com/sol3/papers.cfm?abstract_id=5527538 |
| 2026 | Wind power scenario generation via multi-scale condition adaptive diffusion model | Multi-scale condition adaptive diffusion | 风电场景生成 | 最新 diffusion 代表作之一，重点强化复杂气象条件建模 | https://doi.org/10.1016/j.epsr.2026.112753 |

## 4. LLM / 文本条件 / 自然语言控制：目前还很新

| 年份 | 论文 | 方法 | 与本课题的关系 | 链接 |
|---|---|---|---|---|
| 2024 | Synthetic Time Series Generation for Decision Intelligence Using Large Language Models | LLM synthetic time series | 通用时间序列生成，不是能源专用，但能借鉴 tokenization / fine-tuning 方案 | https://doi.org/10.3390/math12162494 |
| 2025 | Large Language Model for Power System Scenario Generation Considering Weather Condition | LLM + prompt engineering + CoT | 直接碰到“电力系统场景生成”，但更像离散系统级 scenario construction，不是高保真曲线生成 | https://doi.org/10.1109/PESGM52009.2025.11225627 |
| 2025 | Forging Time Series with Language: A Large Language Model Approach to Synthetic Data Generation | LLM synthetic multivariate time series | 通用多变量时间序列生成强相关，适合作为方法迁移参考 | https://arxiv.org/abs/2505.17103 |
| 2025 | Text-Conditioned Diffusion-Based Synthetic Data Generation for Turbine Engine Sensor Analysis and RUL Estimation | Text-conditioned diffusion | 不是能源场景生成，但很接近“文本条件时间序列生成”范式 | https://doi.org/10.3390/machines13050374 |
| 2026 | An LLM-Enabled Frequency-Aware Flow Diffusion Model for Natural-Language-Guided Power System Scenario Generation | LLM + flow diffusion | 截至 2026-04-20，我检到的最接近“自然语言驱动风光场景生成”的论文之一 | https://arxiv.org/abs/2602.19522 |

## 5. 建议优先精读的 12 篇

如果你的目标是后面做“生成模型的可再生能源场景生成”研究，我建议先按这个顺序读：

1. A Review of Solar Power Scenario Generation Methods with Focus on Weather Classifications, Temporal Horizons, and Deep Generative Models
2. Model-Free Renewable Scenario Generation Using Generative Adversarial Networks
3. Data-driven scenario generation of renewable energy production based on controllable generative adversarial networks with interpretability
4. Conditional Style-Based Generative Adversarial Networks for Renewable Scenario Generation
5. Scenario Generations for Renewable Energy Sources and Loads Based on Implicit Maximum Likelihood Estimations
6. Normalizing flow-based day-ahead wind power scenario generation for profitable and reliable delivery commitments by wind farm operators
7. Short-Term Wind Power Scenario Generation Based on Conditional Latent Diffusion Models
8. A Novel Renewable Energy Scenario Generation Method Based on Multi-Resolution Denoising Diffusion Probabilistic Models
9. Controllable renewable energy scenario generation based on pattern-guided diffusion models
10. Wind power scenario generation via multi-scale condition adaptive diffusion model
11. Large Language Model for Power System Scenario Generation Considering Weather Condition
12. An LLM-Enabled Frequency-Aware Flow Diffusion Model for Natural-Language-Guided Power System Scenario Generation

## 6. 基于这批文献，我对选题空间的判断

### 已经比较拥挤的点

- 普通 `GAN` 做风电/光伏场景生成
- 只把天气/NWP 当成数值条件的 conditional generator
- 普通 `latent diffusion` 做单站点或短时风电场景生成

### 还比较有机会的点

- 自然语言或结构化文本条件下的风光曲线生成
- 联合风电、光伏、多站点、多区域的统一生成器
- rare pattern / extreme event / Dunkelflaute 类稀有模式生成
- 少样本新场站适配、跨区域迁移、cold-start scenario generation
- 生成模型与物理先验、NWP、场站元数据联合建模

### 一个比较自然的研究命题

`Language-Conditioned Renewable Scenario Generator`

核心思路：
- 用 LLM 把“场景需求”从自然语言或模板语言映射成语义条件
- 用 latent diffusion / flow matching 负责高保真曲线生成
- 条件里不仅包括天气/NWP，还包括场景模式标签、季节、时段、极端事件描述、站点属性
- 评估不只看 distribution fidelity，还看 controllability、extreme-event recall、跨站点泛化和 few-shot adaptation

## 7. 我下一步建议

如果继续按 `idea-discovery` 走，下一步可以直接做两件事：

1. 把上面这批文献再细分成 `必须下载精读 / 略读 / 只做 related work` 三层。
2. 基于这些文献，输出 8-12 个可投稿的新 idea，并先做 novelty filtering。

