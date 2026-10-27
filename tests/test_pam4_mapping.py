import numpy as np
from optic.comm.modulation import modulateGray


def test_pam4_gray_mapping():
    # All four PAM4 symbols, ordered by amplitude
    bits = np.array([0,0,0,1,1,1,1,0])

    # Expected Gray-coded PAM4 amplitudes
    expected = np.array([-3,-1,1,3])

    symbols = modulateGray(bits, 4, "pam")

    np.testing.assert_array_equal(symbols, expected)
    assert len(symbols) == len(bits) // 2
