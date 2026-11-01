"""Exact check that G7 violates the gate inequality for the CERTIFIED arity-2 potential Gamma_hat = h24k40 + 0.01 p(1-p)
(the potential of the theorem H <= 6.4573 I): D_{Gamma_hat}(G7; p) < 0 at p = (1/2, 1/2, 7/24, 1/2, 1/2, 2/7, 5/17)."""
import sys, os
from fractions import Fraction as Fr
HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)
import exact_gate as X
MINTERMS = [(1, 3), (0, 4), (2, 3, 4), (0, 1, 5), (1, 4, 6), (2, 4, 6), (1, 5, 6)]
table = [-1 if any(all((x >> i) & 1 for i in m) for m in MINTERMS) else 1 for x in range(128)]
H = Fr(1, 2)
ps = [H, H, Fr(7, 24), H, H, Fr(2, 7), Fr(5, 17)]
out = X.check(table, ps, os.path.join(HERE, "..", "..", "inputs", "cert_vi_h24k40.npz"), c=Fr(1, 100))
print("certified: D_{h24k40 + 0.01 p(1-p)}(G7) < 0 :", out["D"][1] < 0)
