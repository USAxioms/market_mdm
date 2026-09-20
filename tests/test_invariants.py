import numpy as np
import pytest
from src.metric_validation import enforce_metric_invariants, diagnose_geometric_collapse
from src.mdm_operators import MDMOperatorManager

def test_metric_symmetry_and_positive_definiteness():
    # Create a corrupted, non-symmetric, semi-negative matrix
    bad_G = np.eye(40)
    bad_G[0, 1] = 5.0
    bad_G[1, 0] = -5.0 # Asymmetric
    bad_G[5, 5] = -2.0 # Negative eigenvalue seed
    
    valid_G, evals, _ = enforce_metric_invariants(bad_G)
    
    # Assertions
    assert np.allclose(valid_G, valid_G.T), "Metric failed symmetry check."
    assert np.all(evals >= 0), "Metric contains negative eigenvalues."

def test_mdm_partition_dimensions():
    manager = MDMOperatorManager(total_dim=40, conscious_dim=13)
    dummy_state = np.ones(40)
    c_13, c_27 = manager.partition_state(dummy_state)
    
    assert len(c_13) == 13
    assert len(c_27) == 27
    assert len(c_13) + len(c_27) == 40
