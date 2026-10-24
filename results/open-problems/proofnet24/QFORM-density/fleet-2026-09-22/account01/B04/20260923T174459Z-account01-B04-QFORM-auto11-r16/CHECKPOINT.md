SIGNED IN - working on the quadratic-form bounded-density conjecture (universal constant), account account01, slot B04, 2026-09-23T17:44:59Z.
attacking: fractionalize the grouped projected-crossing Fourier lemma so a one-hub/two-volume packet survives row marginals above 1/2, then apply it to a genuinely rotated higher-rank indefinite form.

# Early checkpoint — fractional grouped projected crossing

Full QFORM remains OPEN. This checkpoint records the essential new calculation before publication refresh.

Let the grouped-crossing setup be as in `NEW_PROJECTED_CROSSING.md`: k hub projection dimensions, an ell-volume projected crossing matrix C, hub-to-column matrix B of row rank k and singular-value product S, and canonical ell-volume weights

w_T = det(C_T C_T^T)/Z_ell,   Z_ell=e_ell(CC^T),

with row marginals alpha_i and

E(w)=exp((H(w)+sum_i alpha_i log alpha_i)/2).

For q>=1 assume alpha_i<=q/2. In the decoupled L2 estimate put

I_t=E[kappa(BD) prod_i |psi_i(2t<a_i,D>)|].

The new step is to use finite-measure Jensen before weighted Holder:

I_t^q <= m^(q-1) E[kappa(BD) prod_i |psi_i|^q],

m=E kappa(BD) <= 2^(k/2)/S.

Weighted Holder with the canonical ell-subset weights uses exponents q/alpha_i>=2. The sharp scalar Fourier integral gives

int |psi_i(2ty)|^(q/alpha_i)dy <= (2pi/|t|) sqrt(alpha_i/q).

Combining the joint product-projection determinant bound and the canonical determinant entropy identity yields

I_t <= [2^(k/2+ell/(2q)) (2pi)^(ell/q)]
       /[S q^(ell/(2q)) Z_ell^(1/(2q)) |t|^(ell/q)]
       * E(w)^(1/q).                                             (A)

With the hub Plancherel factor,

|phi_Q(t)|^2 <= M_H (pi/|t|)^k I_t.

Put D_q=kq+ell. If D_q>2q, then Fourier inversion gives the explicit fractional grouped-crossing certificate

||p_Q||_infinity <= [D_q/(D_q-2q)]
  * 2^((kq+3ell)/(2D_q)) q^(-ell/(2D_q))
  * M_H^(q/D_q) S^(-q/D_q) Z_ell^(-1/(2D_q)) E(w)^(1/D_q).      (B)

The same calculation gives phi_Q in L1, hence a continuous C0 density. At q=1, entropy subadditivity E(w)<=exp(ell/2) recovers exactly the current grouped-crossing theorem. For k=1, ell=2 the integrability condition is q<2, so every non-coloop two-volume law (alpha_*<1) is accessible by taking max(1,2alpha_*)<=q<2; the old q=1 gate alpha_*<=1/2 is no longer structural.

A symmetric rank-three projected-crossing stress packet is already identified: hub row w=(1,1,1,0) and three light rows
(1,-1,-1,1), (-1,1,-1,1), (-1,-1,1,1).
After projecting away w, C has squared singular values 4,4,3, so Z_2=40 and all natural row marginals are 2/3. Thus the old q=1 projected-crossing gate fails, while q=4/3 in (B) applies. Exact constants and the full ambient spectral check will be written in REPORT.md.

Sources being extended, not silently assumed as full QFORM closure:
- yspennstate/math-open-problems@4f92aeb74083c6f95cb314a11fed1b812eacef9a, `NEW_PROJECTED_CROSSING.md`;
- current control math-research-brain@72038b4bc2ab4c369014cff17eeb8efc17973188;
- current Claude continuation math-open-problems@c4c23b784395630c094ba299a50712209921d1ae (its open SP statement is NOT used as a premise).

Status: supporting analytic theorem in progress; independent review pending; WITHOUT_VERIFIED_BRAIN.