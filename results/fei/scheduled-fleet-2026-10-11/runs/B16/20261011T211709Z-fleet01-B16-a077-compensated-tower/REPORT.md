# B16 / A077 — compensated sparse-defect tower

**Run:** `20261011T211709Z-fleet01-B16-a077-compensated-tower`  
**Primary packet:** A077 (Sparse-defect towers)  
**Attempt:** `A077-B09-SPARSE-CODE-1`  
**Claim version:** `B16-A077-COMPENSATED-TOWER-v1`  
**Gap:** `G-BIASED-TAX` (helper obstruction only)  
**Status:** PROVED pending independent review. Full FEI remains OPEN.

## Result

The repaired B09 biased two-bit gate was converted into a genuinely
multiscale family.  At scale `k`, let `epsilon=2^-k` and use the Boolean gate
`g(X,Y)=(-1)^(XY)` under iid Bernoulli(`epsilon`) inputs.  If `J_k` is the
B09 restriction gain, `M_k=H(S_X|S_Y)`, and `I_core=2r` is the full biased
spectral influence, where `r=4 epsilon^2(1-epsilon)`, then

```
J_k >= r (k-log2(e)),
M_k <= r epsilon (4k+2log2(e)),
J_k/(I_core+M_k) -> infinity.
```

Taking `N_k=2^(2k)` disjoint copies at every scale makes the accumulated
tax-free core payment quadratic while its credited influence is linear and
its conditional spectral term is bounded:

```
sum N_k J_k = Theta(K^2),
sum N_k I_core = Theta(K),
sum N_k M_k = O(1).
```

This rigorously refutes every fixed-constant biased helper
`J <= C(I_core+M)` at this scope.  It does **not** refute FEI.

## Uniform Boolean compensation

Encode each biased bit as the AND of `k` distinct fair physical bits.  The
resulting scale-`k` gate

```
f_k(U,V)=(-1)^(AND(U) AND(V))
```

is an actual Boolean function on the uniform `2k`-cube (the one-point
defect).  Its encoder has label entropy `L_k=log2(2^k-1)` and mean Fourier
degree `D_k=k 2^(k-1)/(2^k-1)`.  The exact transported ledger is

```
J_code = J_k,
M_code = M_k + r L_k,
I(f_k) = 2r D_k = k 2^(2-2k).
```

Thus the omitted label entropy and physical influence are both of order
`rk` and remove the divergence.  For the full tower

```
F_K = product_{k=3}^K product_{j=1}^{2^(2k)} f_{k,j},
```

all coordinates are disjoint, so there is no cross-scale interference and
entropy/influence add exactly.  Writing `S_K=sum_{k=3}^K k`,

```
I(F_K)=4 S_K,
H(F_K)=16 S_K+O(K),
H(F_K)/I(F_K) -> 4.
```

The construction therefore gives a complete compensated tower calculation:
the biased local surrogate diverges, while the actual uniform Boolean FEI
ratio approaches the already known point-defect value 4.

## Scope and obstruction checks

- **Boolean realizability:** explicit truth-table/circuit at every scale.
- **All added influence:** the AND-encoder mean degree is included exactly.
- **Cross-scale interference:** absent because every copy uses disjoint
  physical coordinates; additivity is proved from tensor product spectra.
- **Rare logarithms:** retained through the exact binary entropies.
- **Weighted-versus-uniform guard:** the divergent ratio is explicitly
  product-biased.  The uniform encoded family has `H/I -> 4`.
- **Near tensors / activation:** the tower is an exact disjoint tensor and
  so cannot hide overlap or activation reuse.
- **Addressing/selectors:** no selector or address label is present; the
  relevant missing label is the nonempty-subset label of the AND encoder.

## Evidence

- `SPARSE_DEFECT_TOWERS.tex`: analytic construction and proof.
- `MULTISCALE_COST_LEDGER.json`: exact one-scale and tower formulas.
- `verify_sparse_tower.py`, `CHECK.out`: 80-digit formula audit and finite
  sample ledger.  Computation supports but does not replace the analytic
  all-`k` proof.

## Sources pinned

- B16 contract blob `319bbb049c631c103a842cf9a530c7be91a319d0`.
- Obstruction registry blob `dd482025647aed25166b46cc217a7ed77dcaa767`.
- Repaired B09 interval report: open-problems commit
  `a1ff93577685acd461b154b04e0c1aa0c65645c8`, report blob
  `2674d84116f7454c45b37fdd4991f78d65eaf31c`.
- Campaign baseline inspected at open-problems head
  `87f7c6267e56e7a0eb5b8dfd572a6eaaecae6907`.

## Remaining obligation and next action

This does not produce an unbounded uniform `H/I` sequence.  The exact open
question is whether a uniform Boolean construction with genuinely correlated
auxiliaries can avoid both the `rL_k` label charge and the `rD_k` physical
influence without merely hiding an arbitrary tensor factor.  Route this
package to A079 and A080; independent reviewers are A092 and A088.
