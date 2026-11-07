import numpy as np
from scipy.signal import lfilter, lfilter_zi

def rc_lowpass(x: np.ndarray, fs: float, f3db: float) -> np.ndarray:
    """
    First-order RC channel using exact zero-order-hold (ZOH) discretization.
    """
    x = np.asarray(x, dtype = float)
    
    if x.ndim != 1 or x.size ==0:
        raise ValueError("x must be a nonempty 1-D array")
    if not (0< f3db <fs/2):
        raise ValueError("Require 0 < f3db< fs/2")

    a = np.exp(-2*np.pi*f3db/fs)

    b = [1-a]
    denominator = [1, -a]

    # Initialize at steady state to avoid artificial startup transients.
    zi =lfilter_zi(b, denominator) * x[0]

    y, _ = lfilter(b, denominator, x, zi= zi) # Output array after the filter

    return y
