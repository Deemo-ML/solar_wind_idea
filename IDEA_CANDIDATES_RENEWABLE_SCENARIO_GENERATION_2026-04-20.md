# Research Idea Shortlist

**Direction**: Generative-model-based renewable energy scenario generation for wind/PV curves

**Generated**: 2026-04-20

**Workflow stage**: `idea-discovery -> idea-creator`

**Basis**:
- Literature survey in [LITERATURE_RENEWABLE_SCENARIO_GENERATION_GEN_MODELS_2026-04-20.md](d:\learn\project\solar_wind\LITERATURE_RENEWABLE_SCENARIO_GENERATION_GEN_MODELS_2026-04-20.md)
- Quick novelty checks against recent work up to 2026-04-20
- Constraint: prioritize ideas that are new enough to matter, but still testable on moderate compute

## Landscape Summary

The field has already moved from generic `GAN`-based renewable scenario generation into more controlled and structured methods. Representative work includes `controllable GAN`, `StyleGAN`, `cross-modal GAN`, `conditional latent diffusion`, `multi-resolution diffusion`, and `pattern-guided diffusion`. By 2025-2026, the most active line is clearly `diffusion`, with several papers already addressing multi-scale structure, controllability, extreme patterns, and few-shot / zero-shot pattern generation.

The `LLM` story is newer. As of 2026-04-20, I found direct evidence that natural-language-guided power-system scenario generation has started to appear, but it is still sparse and mostly broader than "wind/PV curve generation". This means "just add an LLM" is no longer novel enough, but there is still room if the task is made sharper: editing instead of from-scratch generation, compositional constraints, cross-site adaptation, retrieval over rare historical regimes, or downstream decision awareness.

The easiest ideas to kill are:
- plain `conditional diffusion for wind/PV scenario generation`
- plain `few-shot renewable scenario generation`
- plain `graph-based multi-site generator`
- plain `interpretable controllable latent space`

Those are already too close to recent literature.

## Recommended Ideas

### Idea 1: Instruction-Based Renewable Scenario Editing

- **One-line summary**: Turn renewable scenario generation from "generate from scratch" into "edit an existing wind/PV curve using natural-language or template instructions while preserving untouched properties".
- **Core hypothesis**: In practice, operators and researchers often want controlled edits such as "make the morning ramp steeper", "shift the PV peak later by 30 minutes", or "inject a Dunkelflaute-like low-output window". Editing a real scenario should be easier to control, easier to evaluate, and more useful than unconstrained generation.
- **Minimum viable experiment**:
  - Build synthetic edit pairs from real wind/PV curves using pattern labels or algorithmic transformations.
  - Train a diffusion-based or latent editor on public wind/PV datasets.
  - Compare against from-scratch controllable generation and general time-series editing baselines adapted to energy data.
  - Evaluate edit success, preservation score, distribution realism, and downstream scheduling sensitivity.
- **Expected contribution type**: new task + new method + benchmark/evaluation protocol
- **Closest work**:
  - `Instruction-based Time Series Editing` (2025)
  - `Towards Editing Time Series` (NeurIPS 2024)
  - `An LLM-Enabled Frequency-Aware Flow Diffusion Model for Natural-Language-Guided Power System Scenario Generation` (2026)
- **Why it survives filtering**: the general time-series editing task exists, but I did not find a direct renewable-energy-specific scenario editing paper. This is differentiated from generic language-guided generation because it focuses on controllable counterfactual edits on existing curves.
- **Novelty**: 8.8/10
- **Feasibility**: medium
- **Risk**: medium
- **Estimated effort**: weeks
- **Likely reviewer objection**: "This is adaptation of time-series editing to energy."
- **Counter**: the key is to make it energy-native: ramp edits, curtailment-aware edits, rare-event injection, operational preservation metrics, and dispatch-level usefulness.

### Idea 2: Metadata-Aware Cold-Start Scenario Generator for Unseen Wind/PV Sites

- **One-line summary**: Generate realistic scenarios for a new site with little or no local history by conditioning on site metadata, geography, climatology, and coarse weather/NWP signals.
- **Core hypothesis**: Existing few-shot renewable scenario generation mainly addresses data scarcity within an already-seen distribution. A stronger and more useful setting is unseen-site generation, where the model must transfer across plants using metadata and environmental context.
- **Minimum viable experiment**:
  - Use multiple wind/PV plants with leave-one-site-out evaluation.
  - Condition the generator on static metadata such as location, elevation, installed capacity, orientation, rough climate zone, and coarse NWP.
  - Compare against few-shot CGAN and generic conditional diffusion baselines.
- **Expected contribution type**: new method + cross-site generalization study
- **Closest work**:
  - `Combined methodology of statistical knowledge and adversarial learning for few-shot renewable scenario generation` (2026)
  - `Controllable renewable energy scenario generation based on pattern-guided diffusion models` (2025)
  - cross-site forecasting/domain-adaptation work in PV forecasting
- **Why it survives filtering**: few-shot renewable scenario generation now exists, but the cross-site "cold-start plant" setup still appears underexplored on the scenario-generation side.
- **Novelty**: 8.1/10
- **Feasibility**: medium
- **Risk**: medium
- **Estimated effort**: weeks
- **Likely reviewer objection**: "This is just domain adaptation."
- **Counter**: frame it as `scenario generation for unseen sites`, not plain forecasting transfer, and evaluate diversity, realism, and decision quality under domain shift.

### Idea 3: Retrieval-Augmented Rare-Regime Scenario Generation

- **One-line summary**: Use a retrieval module to pull similar rare historical regimes before generation, so the model can better synthesize extreme and low-frequency patterns.
- **Core hypothesis**: Pattern-guided diffusion and few-shot methods help, but rare-event generation is still bottlenecked by weak memory of long-tail examples. Retrieval over historical regime libraries should improve faithfulness for extreme ramps, prolonged low-output windows, and compound wind-solar scarcity.
- **Minimum viable experiment**:
  - Build a regime memory bank from historical wind/PV segments and meteorological conditions.
  - Retrieve top-k analog events for a target condition before generation.
  - Compare generation quality on tail subsets only.
- **Expected contribution type**: method + empirical finding on long-tail scenario quality
- **Closest work**:
  - `TS-RAG` (2025) and `TimeRAF` (2024) on retrieval-augmented time-series forecasting
  - `RAG4CTS` (2026) on covariate time series
  - `pattern-guided diffusion` (2025) on renewable scenario generation
- **Why it survives filtering**: I found retrieval-augmented time-series forecasting papers, but not a direct renewable scenario generator that retrieves rare historical regimes as generation memory.
- **Novelty**: 8.3/10
- **Feasibility**: medium
- **Risk**: medium
- **Estimated effort**: weeks
- **Likely reviewer objection**: "Retrieval is already common."
- **Counter**: the novelty is not generic RAG; it is regime-aware retrieval for tail-event scenario generation with renewable-specific extreme metrics.

### Idea 4: Decision-Focused Renewable Scenario Generator

- **One-line summary**: Train the generator not only for fidelity to history, but also for usefulness to downstream unit commitment, dispatch, reserve sizing, or curtailment analysis.
- **Core hypothesis**: A scenario set can look statistically realistic yet still miss the cases that matter most for downstream decisions. End-to-end or surrogate-based decision-focused training should improve operational value even if raw generative metrics change only modestly.
- **Minimum viable experiment**:
  - Wrap a simplified dispatch or reserve-sizing surrogate around the generator.
  - Train with a joint objective: realism + controllability + downstream decision loss.
  - Compare against standard diffusion/GAN methods on both generative and operational metrics.
- **Expected contribution type**: method + evaluation reframing
- **Closest work**:
  - scenario generation papers that report dispatch value
  - `Surrogate-based risk-aware scenario screening` (2026)
  - `Diffusion-DFL: Decision-focused Diffusion Models for Stochastic Optimization` (2026)
- **Why it survives filtering**: there is growing work on decision-focused diffusion and risk-aware scenario screening, but I did not find a clear end-to-end renewable scenario generator optimized for downstream operational utility.
- **Novelty**: 7.9/10
- **Feasibility**: medium-high
- **Risk**: medium-high
- **Estimated effort**: weeks to months
- **Likely reviewer objection**: "Improvements may come from the surrogate, not the generator."
- **Counter**: include ablations separating surrogate quality from generator quality and report both distributional and decision metrics.

### Idea 5: Disentangled Weather-vs-Curtailment Renewable Generator

- **One-line summary**: Learn separate latent factors for weather-driven variability and non-weather distortions such as curtailment, outages, or operating constraints, then generate or edit them independently.
- **Core hypothesis**: Observed renewable power curves are not pure weather traces. They mix meteorological resource, asset behavior, curtailment, control actions, and missing-data artifacts. A disentangled generator could create cleaner scenarios and more meaningful counterfactuals.
- **Minimum viable experiment**:
  - Use paired signals where possible: power, NWP, irradiance/wind speed, and curtailment proxies.
  - Learn a factorized latent representation with weather and non-weather factors.
  - Evaluate whether the model can keep weather fixed while varying curtailment-like effects, and vice versa.
- **Expected contribution type**: new method + interpretability/diagnostic contribution
- **Closest work**:
  - interpretable controllable GAN / VAEGAN papers in renewable scenario generation
  - causal representation and disentanglement work in PV forecasting/domain adaptation
- **Why it survives filtering**: interpretability exists, but the specific split between weather resource and operational distortion appears much less explored for scenario generation.
- **Novelty**: 8.0/10
- **Feasibility**: medium-high
- **Risk**: high
- **Estimated effort**: months
- **Likely reviewer objection**: "True disentanglement is hard to verify."
- **Counter**: treat this as a targeted factorization problem with proxy labels and intervention tests, not as unconstrained unsupervised disentanglement.

### Idea 6: Compositional Language-and-Constraint Generator for Joint Wind-PV Multi-Site Scenarios

- **One-line summary**: Support structured prompts such as "three-day winter event, low PV midday, strong evening wind recovery in coastal sites, moderate inland correlation" and generate multi-site wind/PV scenarios satisfying these compositional constraints.
- **Core hypothesis**: Current controllable methods usually rely on latent codes, weather labels, or single text descriptions. A compositional interface could make the generator much more useful for planning studies and stress testing, especially for multi-site and joint wind-PV conditions.
- **Minimum viable experiment**:
  - Define a controlled scenario grammar rather than open free text.
  - Train a generator on prompt-to-scenario pairs produced from automatically labeled historical data.
  - Evaluate compositional generalization on held-out combinations.
- **Expected contribution type**: new task + controllability benchmark + method
- **Closest work**:
  - `LFFD` natural-language-guided power system scenario generation (2026)
  - controllable renewable scenario generation with interpretable features or pattern-guided diffusion
  - high-dimensional hydro-wind-PV scenario generation papers
- **Why it survives filtering**: pure natural-language-guided generation is already emerging, so the novelty here must come from compositionality, multi-site coupling, and joint wind-PV control rather than "LLM + diffusion" alone.
- **Novelty**: 7.7/10
- **Feasibility**: medium
- **Risk**: medium-high
- **Estimated effort**: weeks
- **Likely reviewer objection**: "This is too close to recent natural-language-guided work."
- **Counter**: keep the scope tight: multi-site joint wind-PV, compositional prompts, and explicit constraint satisfaction metrics.

## Backup Ideas

### Idea 7: Fast Renewable Scenario Sampling via Distilled Diffusion / Rectified Flow

- **Status**: backup
- **Reason**: useful engineering contribution, but less differentiated scientifically unless paired with a harder task such as online what-if analysis or dispatch-in-the-loop generation.

### Idea 8: Weather-Field-to-Power Cross-Modal Generator

- **Status**: backup
- **Reason**: cross-modal renewable scenario generation already exists, so this would need a much stronger angle such as satellite/cloud imagery plus site metadata plus uncertainty editing.

## Eliminated Ideas

| Idea | Reason eliminated |
|---|---|
| Plain conditional diffusion for wind/PV scenario generation | Too close to 2024-2026 mainline papers |
| Plain few-shot renewable scenario generation | Direct recent paper already exists in 2026 |
| Plain graph-based multi-site generator | Dynamic spatiotemporal graph GAN and graph diffusion style work already exist |
| Plain interpretable controllable latent space | Strong overlap with controllable GAN and improved VAEGAN papers |
| Generic "LLM + renewable scenario generation" | No longer sharp enough after 2025-2026 language-guided papers |

## Ranking

1. **Instruction-Based Renewable Scenario Editing**
   - Best balance of novelty, clarity, and practical usefulness
   - Strong chance to become both a method paper and a benchmark/task paper

2. **Metadata-Aware Cold-Start Scenario Generator**
   - Operationally meaningful problem
   - More differentiated than another generic controllable diffusion paper

3. **Retrieval-Augmented Rare-Regime Scenario Generation**
   - Good if you want a stronger long-tail/extreme-event story
   - Especially attractive if you care about Dunkelflaute or stress scenarios

4. **Decision-Focused Renewable Scenario Generator**
   - High value if you want tighter connection to optimization and system operation
   - More ambitious and somewhat harder to execute cleanly

5. **Disentangled Weather-vs-Curtailment Generator**
   - Interesting and potentially impactful, but validation is harder

6. **Compositional Language-and-Constraint Generator**
   - Still promising, but must be scoped carefully to avoid overlap with recent natural-language-guided work

## Suggested Execution Order

If we continue the pipeline, I recommend:

1. Start with **Idea 1** as the primary direction.
2. Keep **Idea 2** as the practical backup.
3. Keep **Idea 3** as the extreme-event / long-tail backup.

## Immediate Next Steps

- Build a deeper novelty note for the top 3 ideas only.
- Turn the top idea into a concrete method thesis and experiment plan.
- Decide datasets, baselines, metrics, and what counts as a publishable positive or negative result.

## Sources Used For Quick Novelty Filtering

- Model-Free Renewable Scenario Generation Using Generative Adversarial Networks: https://doi.org/10.1109/TPWRS.2018.2794541
- Data-driven scenario generation of renewable energy production based on controllable generative adversarial networks with interpretability: https://doi.org/10.1016/j.apenergy.2021.118387
- Conditional Style-Based Generative Adversarial Networks for Renewable Scenario Generation: https://doi.org/10.1109/TPWRS.2022.3170992
- A Cross-Modal Generative Adversarial Network for Scenarios Generation of Renewable Energy: https://doi.org/10.1109/TPWRS.2023.3277698
- Short-Term Wind Power Scenario Generation Based on Conditional Latent Diffusion Models: https://doi.org/10.1109/TSTE.2023.3327497
- A novel scenario generation method of renewable energy using improved VAEGAN with controllable interpretable features: https://doi.org/10.1016/j.apenergy.2024.122905
- Controllable renewable energy scenario generation based on pattern-guided diffusion models: https://doi.org/10.1016/j.apenergy.2025.126446
- Combined methodology of statistical knowledge and adversarial learning for few-shot renewable scenario generation: https://doi.org/10.1016/j.ijepes.2026.111758
- Wind power scenario generation via multi-scale condition adaptive diffusion model: https://doi.org/10.1016/j.epsr.2026.112753
- An LLM-Enabled Frequency-Aware Flow Diffusion Model for Natural-Language-Guided Power System Scenario Generation: https://arxiv.org/abs/2602.19522
- Towards Editing Time Series: https://proceedings.neurips.cc/paper_files/paper/2024/hash/423d0909791493b7c10916fd328c2913-Abstract-Conference.html
- Instruction-based Time Series Editing: https://arxiv.org/abs/2508.01504
- TS-RAG: Retrieval-Augmented Generation based Time Series Foundation Models are Stronger Zero-Shot Forecaster: https://arxiv.org/abs/2503.07649
- TimeRAF: Retrieval-Augmented Foundation model for Zero-shot Time Series Forecasting: https://arxiv.org/abs/2412.20810
- Retrieval-Augmented Generation with Covariate Time Series: https://arxiv.org/abs/2603.04951
- Diffusion-DFL: Decision-focused Diffusion Models for Stochastic Optimization: https://arxiv.org/abs/2510.11590
