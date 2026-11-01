# r34 clarification — zero selected pivot is already the near-null branch

This addendum narrows one sentence in Section 5 of `REPORT.md` and does not change Theorems 2.1, 3.1 or Corollary 4.1.

In the designated fleet04/B13 diffuse exact-rank-two endpoint, choose `k` with `|d_k|>=1` as in the partner theorem. The normalized scalar-Schur frame `W` and its leave-one-out disjointness parameter `delta_k` are invoked only when the genuine physical pivot

`a=A_kk`

is nonzero. If `a=0`, the partner's near-null alternative

`|A_kk|<=sqrt(1536 e^2) rho^(-2)`

already holds identically, and no Schur-DPP construction is required.

Thus the precise simultaneous conclusion is:

- if `A_kk=0`, the near-null branch is already reached;
- if `A_kk!=0`, then the normalized Schur frame exists, `max_i tilde c_i<=1/2`, hence

  `delta_k>=1/512`,

  while the partner slab inequality gives

  `|A_kk det Lambda|<=1536 e^2 rho^(-4)`.

Accordingly, for every **nonzero** selected physical pivot in the diffuse chamber, the disjoint pair-volume cannot collapse. The only remaining high-ratio exits are the partner's near-null pivot or near-rank-one carrier degeneracies. No assertion is made that `delta_k` is defined at an exact zero pivot.
