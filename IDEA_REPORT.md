# Idea Discovery Report

**Direction**: Study regional complementarity based on wind and photovoltaic output characteristics
**Date**: 2026-04-08
**Pipeline**: research-lit -> idea-creator -> novelty-check -> research-review -> research-refine-pipeline

## Executive Summary

The literature is already rich in static complementarity maps, new indices, climate-impact studies, and storage-benefit analysis. Another paper centered on an average complementarity index is unlikely to stand out.

The strongest direction is to move from "average complementarity" to "risk-hour complementarity": identify which province pairs actually reduce compound low-generation and high-load risk, then convert that into actionable pair and corridor ranking. The recommended idea is therefore a tail-aware regional complementarity graph for inter-provincial wind-PV coordination in China.

## Literature Landscape

### Representative papers

| Paper | Venue | What it adds | Gap left for us |
|---|---|---|---|
| "Evaluating complementarity: A review of metrics and their implications for hybrid renewable energy systems" | Renewable and Sustainable Energy Reviews, 2026 | No single metric is sufficient; complementarity assessment should be purpose-driven. | A new index alone is weak unless tied to a real planning decision. |
| "Evaluating wind and solar complementarity in China: Considering climate change and source-load matching dynamics" | Energy, 2024 | China-wide multi-timescale complementarity under source-load matching. | Strong map, but limited guidance on which province pairings matter most. |
| "Assessing wind and solar energy complementarity using novel metrics based on residual load profiles" | Energy, 2025 | Moves complementarity toward residual-load relevance. | Still mostly a metric story, not a pair-selection framework. |
| "Techno-economic benefits and energy storage gains of wind-solar complementary power generation: A provincial analysis in China" | Energy Conversion and Management, 2026 | Shows storage and interconnection benefits of complementarity. | Does not identify which region-to-region links create the most value. |
| "Renewable energy quality trilemma and coincident wind and solar droughts" | Communications Earth and Environment, 2024 | Shows coincident droughts can undermine geographic diversification. | Drought characterization is strong, but pairwise planning guidance is still missing. |
| "Standardized Benchmark of Historical Compound Wind and Solar Energy Droughts Across the Continental United States" | Renewable Energy, 2024 | Demonstrates compound wind-solar droughts aligned with high load are especially severe. | Strong event perspective, but not a China pair-ranking method. |

### Landscape conclusions

- The field has largely moved past plain Pearson-style correlation maps.
- China-specific studies already establish broad regional patterns; novelty must come from decision relevance.
- Event-centric reliability views are emerging, especially around droughts and residual load.
- The remaining gap is operational: which region helps which other region during the hardest hours?

### Source links

- https://www.sciencedirect.com/science/article/pii/S1364032125010950
- https://www.sciencedirect.com/science/article/pii/S0360544224032614
- https://www.sciencedirect.com/science/article/pii/S0360544225037491
- https://www.sciencedirect.com/science/article/abs/pii/S0196890425014530
- https://www.nature.com/articles/s43247-024-01850-5
- https://www.pnnl.gov/publications/standardized-benchmark-historical-compound-wind-and-solar-energy-droughts-across

## Ranked Ideas

### Idea 1: Tail-Aware Regional Complementarity Graph for Wind-PV Coordination in China - RECOMMENDED

- **Hypothesis**: Annual complementarity overestimates practical value; true complementarity is whether region j reduces region i's residual-load tail risk during compound low-generation and high-load hours.
- **Minimum experiment**: Build hourly province-level wind, PV, and load series for 2016-2024. Compare pair rankings from Pearson, Kendall, DCI, residual-load metrics, and the proposed metric on out-of-sample CVaR, drought hours, and ramp burden.
- **Expected outcome**: Only a subset of west-north to central-east pairings will remain strong once the evaluation focuses on stress hours.
- **Novelty**: 8.6/10. Closest work already studies source-load matching, residual load, and droughts, but not directed pair ranking tied to corridor choice.
- **Feasibility**: Moderate. Mostly CPU and data engineering.
- **Risk**: Medium.
- **Contribution type**: Method + empirical planning diagnostic.
- **Pilot result**: SKIPPED. No local dataset exists in this workspace yet.
- **Reviewer's likely objection**: "This is just another metric paper unless you prove it selects better region pairs than existing baselines."
- **Why we should do this**: It turns complementarity into a decision object rather than a descriptive map.

### Idea 2: Regime-Switching Complementarity Under Extreme Weather

- **Hypothesis**: Region pairs that look complementary annually may fail under heat waves, cold surges, or persistent cloudy-windless periods.
- **Minimum experiment**: Partition hours by weather regime and compare annual rankings with regime-specific rankings.
- **Novelty**: 7.7/10.
- **Risk**: Medium to high.
- **Why it is backup**: Good appendix or second paper, but less sharp than Idea 1.

### Idea 3: Complementarity-to-Flexibility Exchange Rate

- **Hypothesis**: Complementarity can be quantified as a region-pair-specific substitute for storage power, storage energy, or balancing reserve.
- **Minimum experiment**: Estimate how much flexibility is offset when moving from low to high complementarity pairings.
- **Novelty**: 7.2/10.
- **Risk**: Medium.
- **Why it is backup**: Close to recent storage-benefit papers, so the novelty bar is higher.

## Eliminated Ideas

| Idea | Reason eliminated |
|---|---|
| A new single complementarity index based only on wind and PV output curves | Too crowded; recent review and 2026 China index work already occupy this lane. |
| A China-wide annual complementarity atlas | Too descriptive without a decisive systems claim. |
| A mega-model combining climate scenarios, storage, transmission, and market dispatch | Too broad for one paper and too easy to lose the core story. |

## Deep Novelty Check for the Top Idea

Closest prior work already covers source-load matching, residual-load metrics, techno-economic benefits, and drought coincidence. The top idea stays novel only if it is framed as a **directed, event-aware province-pair ranking method** with measurable planning value. It is not novel enough if it stops at a renamed index or a national heatmap.

## Critical Review of the Top Idea

### Strengths

- Timely and aligned with the literature shift toward risk-aware planning.
- Compact enough to execute without a full system simulator.
- Naturally produces pair, corridor, and portfolio guidance.

### Main weaknesses

- It can still be mistaken for "another metric paper."
- Province-level load quality is the main empirical bottleneck.
- If results only confirm obvious west-to-east balancing, the novelty weakens.

### Internal reviewer score

- **Before refinement**: 8.4/10
- **After refinement**: 9.1/10

## Refined Proposal

- Proposal: `refine-logs/FINAL_PROPOSAL.md`
- Experiment plan: `refine-logs/EXPERIMENT_PLAN.md`
- Tracker: `refine-logs/EXPERIMENT_TRACKER.md`

## Next Steps

- [ ] Build the province-level hourly dataset
- [ ] Reproduce baseline metrics
- [ ] Implement the directed tail-aware graph
- [ ] Validate top-k pair selection on a held-out year
