import numpy as np
from optic.comm.modulation import modulateGray
from optical_systems.transceiver.pam4 import generate_pam4_symbols


def test_pam4_gray_mapping():
    # All four PAM4 symbols, ordered by amplitude
    bits = np.array([0,0,0,1,1,1,1,0])

    # Expected Gray-coded PAM4 amplitudes
    expected = np.array([-3,-1,1,3])

    symbols = modulateGray(bits, 4, "pam")

    np.testing.assert_array_equal(symbols, expected)
    assert len(symbols) == len(bits) // 2

def test_pam4_symbol_generator():
    bits1, symbols1 = generate_pam4_symbols(1000, seed=42)
    bits2, symbols2 = generate_pam4_symbols(1000, seed = 42)

    # 1000 PAM4 symbols should contain 2000 bits
    assert len(bits1) == 2000
    assert len(symbols1) == 1000

    # Verify constellation levels
    assert np.all(np.isin(symbols1, [-3,-1,1,3]))

    # Same seed should reproduce identical sequences
    np.testing.assert_array_equal(bits1, bits2)
    np.testing.assert_array_equal(symbols1, symbols2)
