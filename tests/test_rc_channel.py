import numpy as np
from optical_systems.transceiver.channel import rc_lowpass

def test_rc_channel_3db_bandwidth():
    fs = 400e9
    f3db = 25e9

    # Sinusoidal excitation at nominal 3-dB frequency
    t = np.arange(4096) / fs
    x = np.sin(2*np.pi*f3db*t)

    y = rc_lowpass(x, fs, f3db)

    # Discard filter sratup transient
    x_steady = x[512:]
    y_steady = y[512:]

    gain = np.std(y_steady) / np.std(x_steady)
    gain_db = 20 *np.log10(gain)

    # Independent frequency-domain reference: -3.0103 dB
    assert np.isclose(gain_db, -3.0103, atol=0.15)

def test_rc_channel_dc_gain():
    fs = 400e9
    f3db = 25e9

    x = np.full(1000, -1.0)
    y = rc_lowpass(x, fs, f3db)

    # A low-pass RC channel must perserve DC amplitude
    np.testing.assert_allclose(y,x,atol=1e-12)


def test_rc_step_response_matches_analytic_solution():
    fs = 400e9
    f3db = 25e9

    x = np.concatenate([
        np.zeros(40),
        np.ones(80),
    ])

    y = rc_lowpass(x,fs,f3db)

    # Analytical solution of the continuous-time PC ODE
    t = np.arange(1,11)/fs
    expected = 1-np.exp(-2 * np.pi * f3db *t)

    np.testing.assert_allclose(
        y[40:50],
        expected,
        atol = 1e-12,
    )
