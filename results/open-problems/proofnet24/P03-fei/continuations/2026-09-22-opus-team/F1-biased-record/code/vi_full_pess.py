"""vi_full with PESSIMISTIC pricing of every g-move input: V(q) is replaced by the larger of the two neighbouring node
values (times q/q_node scaling through G = V/p), removing the downward bias of chord interpolation in concave regions.
AND/OR moves keep the standard operator.  Usage: python vi_full_pess.py C tag"""
import sys, os
import numpy as np
import vi_full as VF
from ro_gamma import Grid


def gamma_pess(grid, G, q):
    q = np.asarray(q, dtype=float)
    small = np.minimum(q, 1 - q)
    x = np.log2(1 / np.maximum(small, 1e-300))
    xs = grid.xs
    j = np.clip(np.searchsorted(xs, x) - 1, 0, len(xs) - 2)
    Gq = np.maximum(G[j], G[j + 1])
    out = small * Gq
    beyond = x > grid.K
    if beyond.any():
        out[beyond] = grid.gamma_at(G, q[beyond])
    at = np.isclose(x, xs[j]) | np.isclose(x, xs[j + 1])
    out[at] = grid.gamma_at(G, q[at])          # exact nodes are priced at their own value
    return out


C = float(sys.argv[1]); tag = sys.argv[2]
_orig_run = VF.run
# patch: wrap Grid.gamma_at used for g-moves by monkeypatching the lambda inside run through a subclass
class PessGrid(Grid):
    def gamma_at_pess(self, G, q):
        return gamma_pess(self, G, q)
VF.Grid = PessGrid
src = open(VF.__file__).read()
src = src.replace("gam_fn = lambda q: grid.gamma_at(G, q)", "gam_fn = lambda q: grid.gamma_at_pess(G, q)")
src = src.replace('if __name__ == "__main__":', 'if False:')
ns = {"__name__": "vf_pess", "__file__": VF.__file__}
exec(compile(src, VF.__file__, "exec"), ns)
ns["Grid"] = PessGrid
G, grid = ns["run"](C, list(ns["FAMILIES"]), 64, [0.0], 0.3, 0.7, tag)
for q in (0.5, 0.4995, 0.499, 0.495, 0.49, 0.485, 0.48, 0.45):
    print("  V(%.4f) - C = %+.6e" % (q, grid.gamma_at(G, np.array([q]))[0] - C))
