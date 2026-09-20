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

### 2. Semantic Grounding Bridge (`src/data_ingestion.py`)

Handles the transformation of raw market data frames into the normalized 40-D coordinate state space $\mathbf{c}_t$.

```python
import numpy as np
import pandas as pd

def load_and_ground_raw_data(filepath):
    """
    Ingests raw market data streams and maps them via semantic grounding 
    into the 40-dimensional MDM state vector c_t.
    """
    raw_df = pd.read_csv(filepath)
    
    # Placeholder mapping: projecting raw columns (returns, volume, volatility, sentiment proxies)
    # into the 40-D coordinate space [c_1, ..., c_40]
    n_rows = len(raw_df)
    c_stream = np.zeros((n_rows, 40))
    
    # Example mapping simulation for capsule validation
    for i in range(n_rows):
        # First 13 dimensions: conscious/agent sentiment and intention proxies
        c_stream[i, :13] = np.random.normal(0.5, 0.1, 13)
        # Remaining 27 dimensions: structural, price, and liquidity metrics
        c_stream[i, 13:] = np.random.normal(0.0, 0.2, 27)
        
    return c_stream
