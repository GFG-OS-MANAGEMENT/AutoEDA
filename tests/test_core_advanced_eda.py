"""
tests/test_core_advanced_eda.py
-------------------------------
Unit tests for core EDA algorithms:
  - autoeda.core.normalization (minmax, standard, robust, maxabs)
  - autoeda.core.transformation (log, boxcox, yeojohnson, binning)
  - autoeda.core.pca (covariance, eigendecomposition, loadings, projections)
  - autoeda.core.distribution (skewness, kurtosis, normality tests, Q-Q coords)
  - autoeda.core.collinearity (R-squared, VIF, condition number)
"""

import pytest

from autoeda.core.normalization import compute_minmax_scale, compute_standard_scale
from autoeda.core.transformation import compute_log_transform, compute_boxcox_transform
from autoeda.core.pca import compute_pca
from autoeda.core.distribution import compute_skewness_kurtosis, compute_shapiro_wilk
from autoeda.core.collinearity import compute_r_squared


# ---------------------------------------------------------------------------
# Normalization unit tests
# ---------------------------------------------------------------------------

@pytest.mark.skip(reason="Implement compute_minmax_scale in autoeda/core/normalization.py to pass.")
def test_compute_minmax_scale_range():
    data = [10.0, 20.0, 30.0, 40.0, 50.0]
    scaled, params = compute_minmax_scale(data, feature_range=(0.0, 1.0))
    assert scaled[0] == 0.0
    assert scaled[-1] == 1.0
    assert params.min_val == 10.0
    assert params.max_val == 50.0


@pytest.mark.skip(reason="Implement compute_standard_scale in autoeda/core/normalization.py to pass.")
def test_compute_standard_scale():
    data = [10.0, 20.0, 30.0, 40.0, 50.0]
    scaled, params = compute_standard_scale(data)
    # Mean of standard scaled data should be ~0.0
    valid_scaled = [x for x in scaled if x is not None]
    assert abs(sum(valid_scaled) / len(valid_scaled)) < 1e-6


# ---------------------------------------------------------------------------
# Transformation unit tests
# ---------------------------------------------------------------------------

@pytest.mark.skip(reason="Implement compute_log_transform in autoeda/core/transformation.py to pass.")
def test_compute_log_transform():
    data = [0.0, 1.0, 2.0, 10.0]
    transformed, params = compute_log_transform(data, plus_one=True)
    assert transformed[0] == 0.0  # ln(0 + 1) == 0


# ---------------------------------------------------------------------------
# PCA unit tests
# ---------------------------------------------------------------------------

@pytest.mark.skip(reason="Implement compute_pca in autoeda/core/pca.py to pass.")
def test_pca_variance_sum():
    # Sum of explained variance ratios should equal 1.0
    pass


# ---------------------------------------------------------------------------
# Normality & distribution unit tests
# ---------------------------------------------------------------------------

@pytest.mark.skip(reason="Implement compute_skewness_kurtosis in autoeda/core/distribution.py to pass.")
def test_symmetric_distribution_skewness():
    symmetric_data = [1.0, 2.0, 3.0, 4.0, 5.0]
    skew, kurt = compute_skewness_kurtosis(symmetric_data)
    assert abs(skew) < 1e-5


# ---------------------------------------------------------------------------
# Collinearity unit tests
# ---------------------------------------------------------------------------

@pytest.mark.skip(reason="Implement compute_r_squared in autoeda/core/collinearity.py to pass.")
def test_perfect_collinearity_r_squared():
    pass
