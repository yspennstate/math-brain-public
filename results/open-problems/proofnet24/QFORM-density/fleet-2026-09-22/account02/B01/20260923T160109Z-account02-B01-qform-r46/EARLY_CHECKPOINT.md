# account02/B01 r46 — early checkpoint

Programme: `QFORM-DENSITY-3EIG-20260922`. Full conjecture OPEN.

Attack: the newest account03/B01 report leaves the nonzero near-singular physical-pair determinant as the first unpaid continuation of its exact-singular random-slope theorem. Do not perturb the exact-null half-Riesz proof: account03/B01 gives an explicit divergence example for that continuation.

Let a physical pair have

`B=[[a,b],[b,c]]`, `a!=0`, `D=|det B|>0`, `kappa=sigma_min(B)`.

After scalar completion of the first coordinate write

`delta=c-b^2/a`, `ell=v-(b/a)u`, `M=C-a^{-1}u u^T`.

The exact full pair-Schur remainder matrix is

`S=M-delta^{-1} ell ell^T`.

The newest partner's exact overlap-two identity immediately rewrites as

`W2(B)=a^2 sum_(k!=l)(delta M_kl-ell_k ell_l)^2
      =a^2 delta^2 sum_(k!=l)S_kl^2
      =D^2 F_off(S)`.

Thus the obstruction example in which the completed remainder is an exact square has `F_off(S)=W2=0`; positive W2 is exactly off-diagonal curvature surviving the *second* Schur completion.

Now apply the proved account02/B01 global sub-half-Riesz theorem to the exact Schur remainder random variable `R(Z)=Z^T S Z+affine`:

`H_beta(R)<=C_beta F_off(S)^(-beta/2)
          =C_beta D^beta W2^(-beta/2)`, `0<beta<1/2`.

Combining this with the proved logarithmic density envelope for an invertible indefinite physical pair gives, for every `r>0`,

`p_Q(t)<=2sqrt(2)/r
 +D^(-1/2)(H_beta/beta)(2r^2/kappa)^beta`.

This is already a rigorous new near-singular interpolation mechanism. Optimizing `r` will give the full theorem in `REPORT.md`; at `beta=1/4` the expected scale is

`||p_Q||inf <= 22.385 D^(-1/6) kappa^(-1/6) W2^(-1/12)`.

The remaining endpoint debt is now sharply localized: remove the residual `kappa` loss (or route tiny-kappa states elsewhere) while retaining product structure. The false law-uniform scalar pointwise Fresnel estimate is not used.
