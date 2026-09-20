# 40-Dimensional MDM Market Geometry Reproducibility Capsule

This capsule implements the executable 40-dimensional Metadynamical Mathematics (MDM) market geometry framework. It tests whether market state transitions are deterministically driven by the metric-coupled gradient ($\mathbf{q}_t = G_t^{-1}\mathbf{d}_t$) and whether the 13 conscious/agent-state dimensions carry independent predictive signal.

## Architecture
- **State Vector ($\mathbf{c}_t$):** 40-D space partitioned into 13 behavioral/conscious components and 27 structural components.
- **Metric Tensor ($G_t$):** Dynamically evolving $40 \times 40$ matrix governed by terminally constrained metric flow.
- **Protocol:** Train $\rightarrow$ Freeze $\rightarrow$ Out-of-Sample (OOS). No parameter tuning occurs during the OOS evaluation phase.

## Quick Start
1. Ensure Docker is installed.
2. Build and run the capsule container:
   ```bash
   docker build -t mdm-geometry-capsule .
   docker run --rm -v $(pwd)/results:/app/results mdm-geometry-capsule
3 ​Check the generated logs and artifacts in the results/ directory.
---
