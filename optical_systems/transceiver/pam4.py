import numpy as np
from optic.comm.modulation import modulateGray

def generate_pam4_symbols(n_symbols: int, seed: int = 42):
    """
    Generate random bits and Gray-mapped PAM4 symbols
    """
    if not isinstance(n_symbols, int) or isinstance(n_symbols, bool) or n_symbols<=0:
        raise ValueError("n_symbols must be a positive integer")

    # PAM4 carries 2 bits per symbol
    n_bits = n_symbols * 2

    # Reproducible random bit sequence
    rng = np.random.default_rng(seed)
    bits = rng.integers(0,2,size = n_bits)

    # Gray mapping using OptiCommPy
    symbols = modulateGray(bits, 4, "pam")

    return bits, symbols

def generate_pam4_waveform(
        symbols: np.ndarray,
        symbol_rate: float = 50e9,
        sps: int = 8,

):
    """
    Generate an ideal rectangular PAM4 waveform

    Parameters:
    -------
    symbols: np.ndarray
        PAM4 symbol sequence.

    symbol_rate: float
        Symbol rate in baud.

    sps: int
        Samples per symbol.

    Returns:
    --------
    t: np.ndarray
        Time axis in seconds.

    waveform: np.ndarray
        Oversampled PAM4 amplitudes.
    """
    if symbol_rate <=0:
        raise ValueError("symbol_rate must be positive")
    if isinstance(sps,bool) or not isinstance(sps, (int, np.integer)) or sps < 1:
        raise ValueError("sps must be positive integer")

    # Ideal rectangular pulse shaping
    waveform = np.repeat(symbols, sps)

    # Sampling frequency and time axis
    fs = symbol_rate * sps
    t = np.arange(len(waveform))/fs

    return t, waveform
