import numpy as np
import json
from src.simulator import MDMMarketSimulator

def main():
    print("=== MDM Market Geometry Reproducibility Capsule ===")
    
    # 1. Initialize Simulator
    sim = MDMMarketSimulator(dt=0.01, kappa=0.1, alpha=0.05, beta=0.01)
    
    # 2. TRAINING PHASE: Fit parameters on historical training partition
    print("\n[Phase 1] Executing training and parameter calibration...")
    training_data = np.random.normal(0, 0.1, (100, 40)) # Placeholder for historical stream
    
    # [Calibration logic goes here]
    
    # 3. FREEZE PHASE: Lock parameters and metric configuration
    print("[Phase 2] Freezing capsule parameters...")
    frozen_config = {
        "kappa": sim.kappa,
        "alpha": sim.alpha,
        "beta": sim.beta,
        "timestamp": "2026-09-20"
    }
    with open("results/frozen_parameters.json", "w") as f:
        json.dump(frozen_config, f, indent=4)
        
    # 4. OUT-OF-SAMPLE (OOS) TESTING PHASE
    print("[Phase 3] Running Out-of-Sample evaluation stream...")
    sim.set_state(training_data[-1])
    
    oos_results = []
    for t in range(50):
        noise = np.random.normal(0, 0.01, 40)
        metrics = sim.step(eta=noise)
        
        oos_results.append({
            "step": t,
            "objective_F": float(metrics["F"]),
            "gradient_norm": float(metrics["gradient_norm"]),
            "min_eigenvalue": float(metrics["eigenvalues"].min())
        })
        
    with open("results/oos_eigenvalue_spectrum.csv", "w") as f:
        f.write("step,objective_F,gradient_norm,min_eigenvalue\n")
        for res in oos_results:
            f.write(f"{res['step']},{res['objective_F']},{res['gradient_norm']},{res['min_eigenvalue']}\n")
            
    print("\nCapsule execution complete. Artifacts saved to /results.")

if __name__ == "__main__":
    main()
