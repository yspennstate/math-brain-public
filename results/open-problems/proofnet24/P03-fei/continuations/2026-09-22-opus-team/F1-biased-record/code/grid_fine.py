"""Grid with extra refinement near 1/2: step 2^-13 on [0.44, 0.5] (mirrored), otherwise as ro_gamma.Grid."""
import numpy as np
from ro_gamma import Grid


class GridFine(Grid):
    def __init__(self, M=24, K=40, lo=0.44, step=2.0 ** -13):
        mid = np.arange(64, 1024 + 1) / 2048.0
        fine = np.arange(int(np.ceil(lo / step)), int(0.5 / step) + 1) * step
        tail = 2.0 ** (-(5 + np.arange(1, (K - 5) * M + 1) / M))
        self.M, self.K = M, K
        self.ps = np.unique(np.concatenate([mid, fine, tail]))[::-1]
        self.xs = np.log2(1 / self.ps)
        self.xs[0] = 1.0; self.xs[-1] = float(K)
        self.all_p = np.unique(np.concatenate([self.ps, 1 - self.ps]))
        self.Lall = np.log2(1 / self.all_p)
