# Deterministic counterexample to LLS Lemma 2.14 on the boxes B_N it is applied to:
# the maximal configuration (all heights 2d-1) is recurrent on every finite K, and its
# second wave from the centre contains every neighbour of the centre once the box has side >= 5.
import itertools
from waves_enum import make_box, is_recurrent, waves
for dims in [(5,5),(7,7),(5,5,5),(7,7,7)]:
    sites, idx, nbrs, deg, o = make_box(dims)
    eta=[deg-1]*len(sites)
    assert is_recurrent(eta,nbrs,deg)
    W,topp=waves(eta,nbrs,deg,o)
    N0=set(nbrs[o])
    print(f"dims={dims}: number of waves N={len(W)}; |W_k|={[len(w) for w in W]}; "
          f"waves containing ALL nbrs of o: k={[k+1 for k,w in enumerate(W) if N0<=w]}; "
          f"waves containing SOME nbr: k={[k+1 for k,w in enumerate(W) if w&N0]}")
