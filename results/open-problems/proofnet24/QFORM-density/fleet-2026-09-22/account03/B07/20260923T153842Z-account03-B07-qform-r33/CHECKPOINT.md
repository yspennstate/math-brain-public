SIGNED IN - working on the quadratic-form bounded-density conjecture (universal constant), account 03, slot B07, 2026-09-23T15:38:42Z.
attacking: the r32 four-bank cancellation survivor — prove that small aggregate cross-rectangle minor mass forces the ENTIRE selected physical four-bank core, not merely its four blocks separately, into a quantitative rank-one low-tail tube.

# Early substantive checkpoint — bank-cycle cancellation implies global low tail

Run: `20260923T153842Z-account03-B07-qform-r33`.
Programme: `QFORM-DENSITY-3EIG-20260922`.
Full QFORM remains open.

Let

```
K = [ A  B ]
    [ C  D ]
```

with physical original-coordinate banks, and set

`alpha=||A||F`, `beta=||B||F`, `gamma=||C||F`, `delta=||D||F`,

`Omega=sum_{i,k,j,l}(A_ij D_kl-B_il C_kj)^2`.

The r32 identity is

`Omega=(alpha delta)^2+(beta gamma)^2-2T`,

`T=<A^T B,C^T D>F=<A C^T,B D^T>F`.

Suppose `Omega<eps^2 alpha^2 delta^2`, `0<eps<1`, and `alpha delta>0`. Then

`|beta gamma-alpha delta|<eps alpha delta`, hence `beta gamma>(1-eps)alpha delta`, and

`T/(alpha beta gamma delta) >= 1-eta`,

`eta=eps^2/[2(1-eps)]`.

Therefore each of the four shared-side correlations is at least `1-eta`:

`||A^T B||F >=(1-eta) alpha beta`,
`||C^T D||F >=(1-eta) gamma delta`,
`||A C^T||F >=(1-eta) alpha gamma`,
`||B D^T||F >=(1-eta) beta delta`.

For same-row matrices `U,V`, if `||U^T V||F >=(1-eta)||U||F||V||F`, writing

`tau=1-(1-eta)^2=2eta-eta^2`,

one has

`E2([U V]) <= tau (||U||F^2+||V||F^2)^2`.

Reason: `||U||op >=(1-eta)||U||F` and likewise for `V`, so each internal second-compound mass is at most `tau||U||F^4`, respectively `tau||V||F^4`; the mixed-column minor mass is exactly `||U||F^2||V||F^2-||U^T V||F^2 <=tau||U||F^2||V||F^2`.

Apply this horizontally and vertically. The exact minor partition is

`E2(K)=E2([A B])+E2([C D])+E2([A;C])+E2([B;D])`
`      -E2(A)-E2(B)-E2(C)-E2(D)+Omega`.

With `S=||K||F^2=alpha^2+beta^2+gamma^2+delta^2`, the four pair-square terms sum to at most `2S^2`, while `Omega<eps^2 S^2/4`. Hence

`E2(K) < Delta(eps) S^2`,

`Delta(eps)=2(2eta-eta^2)+eps^2/4`.

If `Delta(eps)<1/4`, and `R=sum_{j>=2}s_j(K)^2`, then

`R/S <= theta(eps):=[1-sqrt(1-4Delta(eps))]/2`.

Indeed `E2(K)>=s1(K)^2 R=(S-R)R`; the alternative `R>S/2` would itself imply `E2(K)>=S^2/4`.

At `eps=1/64`,

`eta=1/8064`,
`Delta=36223/65028096=0.0005570361463451121...`,
`theta=0.0005573467817802658...`,

so

`dist_F(K,rank<=1) <0.023608194 ||K||F`,

and

`(sum_{j>=2}s_j(K)^2)^(1/2)/s1(K) <0.023614775`.

This is a genuine physical low-tail alternative: no individual coordinate minor is selected or inverted.

Next step in this run: propagate the actual r31/partner scales through this dichotomy, check constants deterministically, and record exactly what analytic receiver is still missing.
