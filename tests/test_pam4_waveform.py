import numpy as np

from optical_systems.transceiver.pam4 import generate_pam4_waveform

def test_pam4_waveform():
    symbols = np.array([-3, -1, 1, 3])

    t, waveform = generate_pam4_waveform(
        symbols,
        symbol_rate = 50e9,
        sps = 8,
    )

    # Four symbols, eight samples each
    assert len(waveform) == 32
    assert len(t) == 32

    # Verify rectangular pulse shaping
    np.testing.assert_array_equal(
        waveform,
        np.repeat(symbols,8)
    )

    # Sampling interval = 2.5 ps
    dt = 1/(50e9*8)
    np.testing.assert_allclose(np.diff(t), dt)
