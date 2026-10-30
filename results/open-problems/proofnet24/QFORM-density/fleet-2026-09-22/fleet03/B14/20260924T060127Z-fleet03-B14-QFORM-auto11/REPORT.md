SIGNED IN - working on the quadratic-form bounded-density conjecture (universal constant), account fleet03, slot B14, 2026-09-24T06:01:27Z.
attacking: translation-uniform localization by quantile gauge fixing, with arbitrary affine leakage retained and no moment/support/fragment cost.

# fleet03/B14 — exact quantile-gauge localization

Run: `20260924T060127Z-fleet03-B14-QFORM-auto11`  
Programme: `QFORM-DENSITY-3EIG-20260922`  
Owner control at pre-publication refresh: revision `2026-09-22.15`; full QFORM remains OPEN.  
Execution: `WITHOUT_VERIFIED_BRAIN`.

## 1. Result

Fix once and for all any `p in (0,1)`. For a real probability law `mu`, write

`q_p(mu)=inf{x: mu((−infinity,x])>=p}`

for its lower `p`-quantile. It is finite and translation-equivariant:

`q_p(mu shifted by a)=q_p(mu)+a`.

For a probability measure `nu` on the output line define the interval-height functional

`H(nu)=sup_I nu(I)/|I|`,

where the supremum runs over bounded nonempty open intervals. If `nu` has density `r`, then `H(nu)=||r||_(infinity,ess)`.

Let `C_full` be the supremum of `H(law(X^T A X))` over the exact owner target: all dimensions, all independent real coordinates with probability densities bounded by one, and all real symmetric `A` with `s_3(A)>=1`.

Let `C_reg,aff(p)` be the corresponding supremum of

`H(law(Y^T A Y+b^T Y+c))`

over all dimensions subject to

1. every marginal density of `Y` belongs to `C_c^infinity`, is a probability density, and is bounded by one;
2. every coordinate is in the fixed translation gauge `q_p(Y_i)=0`;
3. `A=A^T` satisfies the strict spectral margin `s_3(A)>1`;
4. `b` and `c` are completely arbitrary deterministic affine coefficients.

### Theorem (`QFORM-QUANTILE-GAUGE-ZERO-LOSS-LOCALIZATION-v1`)

For every fixed `p in (0,1)`,

`boxed: C_reg,aff(p)=C_full,`

including the value `+infinity`.

Thus the universal density-height problem loses **no constant at all** if arbitrary physical translations are gauge-fixed by one quantile in every original coordinate, provided arbitrary affine terms are retained. Simultaneously one may work with smooth compact input laws and a strict spectral margin. No moments, common support centre, common support diameter, connected support, or finite fragment count are introduced.

For `p=1/2`, every original coordinate may therefore be median-centred at zero in the analytic core, with all translation information carried only by deterministic affine coefficients.

This is a translation localization statement, not a claim that centred laws are extremisers for the homogeneous problem. Dropping the affine term after centring would be invalid.

## 2. First direction: every rough homogeneous instance enters the quantile gauge

Take an arbitrary exact-target instance `(X,A)`. Put

`m_i=q_p(law(X_i))`, `m=(m_1,...,m_n)`, `Z=X-m`.

Then the coordinates of `Z` remain independent, retain the same density caps, and satisfy

`q_p(Z_i)=0`.

Exactly,

`X^T A X = Z^T A Z + b^T Z + c`,

where

`b=2Am`, `c=m^T A m`.                                               (2.1)

No expectation or moment appears. The numbers `m_i` can be arbitrarily large and can lie in arbitrarily large gaps of fragmented supports.

We next regularise without changing the limiting output height.

For each coordinate, use the cap-preserving tail-mass compactification from this slot's earlier theorem `QFORM-EXACT-CONSTANT-COMPACT-AFFINE-LOCALIZATION-v1`, pinned at

`yspennstate/math-open-problems@a0917bc3d1bea79d37bf8e5e043ec673d3084517`,

`proofnet24/QFORM-density/fleet-2026-09-22/fleet03/B14/20260923T213400Z-fleet03-B14-QFORM-auto11/REPORT.md`.

It produces compactly supported probability densities `g_i^(k)<=1` with

`||g_i^(k)-f_(Z_i)||_1 ->0`,                                        (2.2)

using only tail mass and no tail moment. Convolve `g_i^(k)` with a compactly supported smooth probability mollifier of scale tending to zero. The resulting `h_i^(k)` are in `C_c^infinity`, have mass one, satisfy `0<=h_i^(k)<=1`, and still converge in `L1` to the law of `Z_i`.

Let `W_i^(k)` have density `h_i^(k)`, independently, and put

`a_i^(k)=q_p(law(W_i^(k)))`, `Y_i^(k)=W_i^(k)-a_i^(k)`.              (2.3)

Then every `Y_i^(k)` is smooth, compactly supported, cap-one, independent, and has lower `p`-quantile exactly zero. The recentering amounts `a_i^(k)` need not converge and need not be bounded; this is harmless because they are absorbed algebraically rather than estimated.

Choose any `eta_k downarrow0` and put

`A_k=(1+eta_k)A`,                                                    (2.4)

so `s_3(A_k)>1`. Define the polynomial on the uncentred approximation

`F_k(w)=w^T A_k w+b^T w+c`.

Writing `w=y+a^(k)` gives the exact identity

`F_k(y+a^(k))
 = y^T A_k y + b_k^T y+c_k`,                                        (2.5)

with

`b_k=2A_k a^(k)+b`,
`c_k=(a^(k))^T A_k a^(k)+b^T a^(k)+c`.                              (2.6)

Hence `F_k(W^(k))` is a member of the regular quantile-gauge affine class.

The product laws of `W^(k)` converge in total variation to that of `Z`. For the same varying polynomial,

`d_TV(law(F_k(W^(k))),law(F_k(Z)))
 <= d_TV(law(W^(k)),law(Z)) ->0`.                                   (2.7)

For every sample value of `Z`,

`F_k(Z) -> Z^T A Z+b^T Z+c = X^T A X`                              (2.8)

almost surely, because `A_k->A`; again no moment is needed. Combining (2.7) and (2.8) gives weak convergence

`law(F_k(W^(k))) => law(X^T A X)`.                                  (2.9)

For each bounded open interval `I`, Portmanteau yields

`P{X^T A X in I}
 <= liminf_k P{F_k(W^(k)) in I}`.                                   (2.10)

Therefore

`H(law(X^T A X))
 <= liminf_k H(law(F_k(W^(k))))
 <= C_reg,aff(p)`.                                                   (2.11)

Taking the supremum over all rough target instances gives

`C_full <= C_reg,aff(p)`.                                           (2.12)

This direction is where arbitrary shifts, distant fragments and unbounded supports are removed. The constant is exactly preserved.

## 3. Reverse direction: affine quantile-gauge instances homogenise back into the original target

Take any member of the regular quantile-gauge affine class,

`Q=Y^T A Y+b^T Y+c`, `s_3(A)>1`.                                   (3.1)

The scalar `c` only translates the output, so ignore it. If `b=0`, (3.1) is already an original homogeneous target instance.

Assume `b!=0`. Let `U~Unif[0,1]` be independent and let

`V_T=T+U`.                                                           (3.2)

For sufficiently large `T`, define

`B_T=[[A, b/(2T)], [b^T/(2T), 0]]`.                                (3.3)

The perturbation from `diag(A,0)` has operator norm `||b||_2/(2T)`. Since `s_3(A)>1`, for all sufficiently large `T` Weyl's inequality leaves the same three signed eigenvalues outside `[-1,1]`. Thus `B_T` satisfies the original three-large-eigenvalue target.

The homogeneous quadratic form of the independent cap-one vector `(Y,V_T)` is

`Q_T=(Y,V_T)^T B_T (Y,V_T)
    =Y^T A Y+(V_T/T)b^T Y`.                                        (3.4)

Under the natural coupling,

`V_T/T=1+U/T ->1`,

so

`Q_T -> Y^T A Y+b^T Y` almost surely.                               (3.5)

Again no moment is used. Portmanteau gives, for every bounded open interval `I`,

`P{Q in I} <= liminf_T P{Q_T in I}`.                               (3.6)

Consequently

`H(law(Q)) <= liminf_T H(law(Q_T)) <= C_full`.                      (3.7)

Taking the supremum gives

`C_reg,aff(p) <= C_full`.                                           (3.8)

Together with (2.12), this proves the theorem.

The far auxiliary coordinate is not required to satisfy the quantile gauge; it is used only in the reverse comparison to an unrestricted original target instance. This is why the theorem is an equality of the two optimal constants, rather than an invalid assertion that the homogeneous problem may simply be median-centred and the affine term discarded.

## 4. A reusable proof interface

The theorem gives a safe translation-normal form for any future analytic estimate:

- choose one fixed `p` (for example `p=1/2`);
- translate each original marginal until its lower `p`-quantile is zero;
- retain the full deterministic affine term created by that translation;
- prove a uniform bound on the smooth compact strict-margin affine class;
- do not pay any norm of the translation vector, any moment, any support radius, any gap length or any fragment count.

Any constant proved uniformly on that class transfers to the exact original owner target unchanged.

A search of the visible QFORM corpus for `median centering affine homogenization` and `quantile gauge p-quantile centered affine` returned no matching theorem. The nearest sources are this slot's earlier affine-homogenization theorem above and fleet03/B15's normalized regular extremal-envelope theorem. Those sources remove affine terms and roughness at the level of the full supremum, but they do not state the fixed-quantile translation gauge (2.3)-(2.6).

## 5. Designated partner fleet04/B14 applied to an actual inequality

Use the completed fleet04/B14 r10 theorem at

`yspennstate/math-open-problems@deb713bc8e6df3f7e0ac5398e8cccbf00d1e7513`,

`proofnet24/QFORM-density/fleet-2026-09-22/fleet04/B14/20260924T001624Z-fleet04-B14-scaled-schur-localization-r10/REPORT.md`.

It proves: if some original-coordinate `3x3` principal block `B` is invertible and

`sigma=min_j |lambda_j(B)|>0`,

then for every cap-one product law and arbitrary outside curvature/couplings,

`||p_(X^T A X)||_(infinity,ess) <= 6 sqrt(pi)/sigma`.                (5.1)

Apply the quantile gauge to an arbitrary translated, fragmented, unbounded input. Put `m_i=q_p(X_i)` and `Z=X-m`. Then

`X^T A X=Z^T A Z+2(Am)^T Z+m^TAm`.                                 (5.2)

Conditioning on all coordinates outside the partner's physical triple leaves exactly the same principal block `B`; all terms generated by (5.2) are affine on the triple and the partner theorem is uniform in those affine coefficients. Hence the actual inequality is

`boxed:
 sup_(all deterministic coordinate translations)
 ||p_((X+t)^T A (X+t))||_(infinity,ess)
 <= 6 sqrt(pi)/sigma.`                                              (5.3)

There is no dependence on `t`, tails, fragment locations or moments.

For the concrete target block

`B_*=I_3-(2/3) 11^T`,                                               (5.4)

one has `spec(B_*)={1,1,-1}` and `sigma=1`. Therefore every ambient extension

`A=[[B_*,C],[C^T,D]]`,                                              (5.5)

with completely arbitrary `C,D`, obeys for every admissible product law and every deterministic translation vector `t`

`boxed:
 ||p_((X+t)^T A (X+t))||_(infinity,ess)
 <=6 sqrt(pi)=10.634723105433096... .`                              (5.6)

This is a literal three-large-eigenvalue chamber by interlacing and a literal use of the completed designated partner result.

## 6. What is and is not solved

**Proved in this run:** exact zero-loss fixed-quantile translation gauge for the full universal density-height constant; simultaneous smooth compact strict-margin reduction with arbitrary affine terms; equation-level fleet04/B14 application with a translation-uniform numerical bound.

**Not proved:** the unrestricted universal constant is finite. The hard step remains the matrix/product-geometry estimate on the regular affine core as local pivots/minors approach zero. The quantile gauge removes absolute location only; it gives no uniform support diameter, no moment and no finite fragment count.

**Continuity:** this theorem is an interval-height/essential-density localization theorem. It does not infer continuity by taking limits. The fleet has separate fixed-matrix `C_0` regularity work, but the current owner `CLAIMS.json` still records full-target continuity as open, so no stronger status is claimed here.

FULL QFORM: **OPEN / NOT PROVED / NOT DISPROVED**.
