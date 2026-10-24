# B07 / A034 — anchored-tail phase completion

**Status:** restricted theorem proved; independent review pending; full FEI open.

The preceding A034 theorem paid conditional Fourier entropy with averaged
Rényi-half complexity. That was effective on AND fibers but overcharged
rare one-point defects by a constant while their influence vanished.

This run replaces each positive conditional fiber `q` by the better of:

1. its full Rényi-half entropy; and
2. an anchored decomposition around a maximum atom,
   `h2(epsilon)+epsilon H_{1/2}(tail)`.

Both quantities upper-bound `H(q)`, so their minimum does as well. Inserting
this fiberwise bound into the exact spectral chain rule gives

`H(f) <= (2/ln2) I_Y(f)+2(d-1)-E Gamma_d+A_at(f)`.

This strictly strengthens `B07-A034-RENYI-FIBER-v1`.

For the genuine Boolean point defect `q_k`, the residual Fourier tail is
uniform. The anchored expression therefore equals Shannon entropy exactly,
and an all-`k` calculation proves `A_at(q_k)<=4 I(q_k)`. This neutralizes
the campaign's fixed-Rényi point-defect obstruction without weakening the
AND-family gain.

The condition does not admit repeated arbitrary tensor cores under a fixed
cap: `A_at` is at least conditional Shannon entropy, which increases by
`m H(g)` after inserting `m` fresh copies of a non-character factor `g`.
No FEI inequality is used in that exclusion.

Exact command:

`python3 verify_point_defect.py`

The checker verifies the exact point-defect spectrum, influence, rare-tail
mass, and rational margins for `k=1,...,64`. The all-dimensional entropy
bound is proved analytically in the theorem file.

Source pins:

- source plan head: `094528da1b7b399fa834d82c2bae15df4338d56d`;
- B07 compact contract blob: `2402180c94777484a0f41d5f13a9e01059107569`;
- predecessor claim: `B07-A034-RENYI-FIBER-v1`, delivered at open-problems
  commit `c7f4db2eb2566b5c3ba9228a9b1ac6357603c566` and Brain commit
  `9868e4a4e882d936c520921c6d4cf815c8b297b8`.

The remaining universal obstruction is unchanged in kind but narrower:
prove an influence payment or decomposition for the anchored-tail cost on
a growing Boolean class. Full FEI remains open.
