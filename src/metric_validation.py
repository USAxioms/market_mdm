import numpy as np

def enforce_metric_invariants(G, min_eigenval=1e-4):
    """
    Enforces symmetry and positive-definiteness on candidate metric G.
    Returns the corrected metric and its eigenvalue spectrum.
    """
    # 1. Symmetry check & projection
    G_sym = 0.5 * (G + G.T)
    
    # 2. Spectral decomposition
    evals, evecs = np.linalg.eigh(G_sym)
    
    # 3. Non-degeneracy / positive-definiteness enforcement
    evals_clipped = np.maximum(evals, min_eigenval)
    G_valid = evecs @ np.diag(evals_clipped) @ evecs.T
    
    return G_valid, evals_clipped, evecs

def diagnose_geometric_collapse(evals, threshold=1e-3):
    """
    Diagnoses whether the manifold is experiencing dimensional compression 
    (e.g., during a crash or liquidity freeze where eigenvalues collapse).
    """
    collapsed_dimensions = np.sum(evals < threshold)
    is_collapsing = collapsed_dimensions > 0
    return {
        "is_collapsing": is_collapsing,
        "collapsed_count": int(collapsed_dimensions),
        "min_eigenvalue": float(evals.min())
    }
