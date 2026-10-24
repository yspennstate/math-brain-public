SIGNED IN - working on the quadratic-form bounded-density conjecture (universal constant), account account01, slot B12, 2026-09-24T08:17:37Z.
attacking: one-sided spectral-cone shielding on an original-coordinate bank, then adaptive canonical-angle rank spending for remaining signed packets.

# account01/B12 — one-sided spectral-cone shield and hybrid packet compiler

Programme: `QFORM-DENSITY-3EIG-20260922`  
Assignment: Additional eigenvalue control  
Run: `20260924T081737Z-account01-B12-QFORM-auto11`  
Status: **NEW SUPPORTING STABILITY THEOREM / FULL QFORM OPEN**  
Brain status: `WITHOUT_VERIFIED_BRAIN`

## 1. Scope and corrections respected

The full target remains open: for arbitrary independent cap-one input densities and arbitrary real symmetric `A` with at least three eigenvalues of modulus at least one, prove a universal `L^infinity` density bound, or give a valid counterexample. No moment, support, log-concavity, Gaussian, iid, diagonal-basis, or post-rotation independence assumption is used here.

This run uses only deterministic coefficient-matrix inequalities until the final completed receiver. It does **not** treat `X^T E X` for a spectral remainder `E` as independent noise or as a uniformly small random variable. The live corrections concerning false pointwise oscillatory decay, dimension-losing fiber suprema, and loss of independence after rotation remain in force.

The designated partner result actually used below is:

- `QFORM-ADAPTIVE-MULTIPACKET-ANGLE-BUDGET-v1`, account02/B12;
- source: `yspennstate/math-open-problems@3e7c3dea777f9cfbae2d6311372daf447bd01ef0`;
- path: `proofnet24/QFORM-density/fleet-2026-09-22/account02/B12/20260924T075526Z-account02-B12-r11/REPORT.md`.

For a full-column carrier `M_0` and arbitrary successive packets `N_r`, if `q_r` canonical-resonant directions are spent at stage `r`, then

` s_(m-Q)(M_0+sum_r N_r) >= s_m(M_0) prod_r eta_r, `

with `Q=sum q_r` and `eta_r=sqrt(1-(c_(q_r+1)^(r))^2)`. Packet norms and signs do not enter.

The same source records the completed five-square-mode receiver: if an ORIGINAL-coordinate bank `H` of size `m` satisfies

` s_5(A P_H) >= h>0, `

then

` ||p_(X^T A X)||_infinity <= sqrt(24*pi*m+K_3^2)/h, `

where `K_3=3*2^(4/3)*exp(1/3)`. This is an essential-supremum statement. I do not claim unrestricted continuity from this branch.

## 2. Main theorem: one-sided spectral-cone shield

Let `H` be a set of `m` ORIGINAL coordinates and let `P_H:R^m->R^n` be the coordinate embedding. Fix a sign `sigma in {+1,-1}`.

Let `A_0` be symmetric and assume the physical principal block has a sign-definite floor

` sigma A_0[H,H] >= g I_m `                                      (2.1)

in quadratic-form order, for some `g>0`.

Let `E` be an arbitrary symmetric spectral addition. Relative to `sigma`, write its spectral decomposition as

` E = sigma P - sigma N_hi - sigma N_lo, `                     (2.2)

where `P,N_hi,N_lo` are positive semidefinite, with no restriction at all on `P` or `N_hi`, and

` 0 <= N_lo <= h I_n. `                                         (2.3)

Thus every added eigenvalue whose sign agrees with the protected sign is placed in `P`, regardless of magnitude; opposite-sign added eigenvalues of magnitude at most `h` are placed in `N_lo`; the remaining opposite-sign eigenvalues are placed in `N_hi`.

Let `T` be any further symmetric remainder satisfying only the local same-bank condition

` ||T[H,H]||_op <= delta. `                                     (2.4)

All cross blocks and the outside-outside block of `T` may be arbitrarily large.

Set

` A_b = A_0 + E + T `                                           (2.5)

and define the projected opposite-sign footprint rank

` q = rank( N_hi[H,H] ). `                                      (2.6)

### Theorem 2.1 — `QFORM-ONE-SIDED-SPECTRAL-CONE-SHIELD-v1`

If

` g_0 := g-h-delta >0, `                                       (2.7)

then

` boxed: s_(m-q)( A_b P_H ) >= g_0. `                           (2.8)

Equivalently, there is an `(m-q)`-dimensional subspace `F` of the ORIGINAL-coordinate domain `R^H` on which

` ||A_b P_H x|| >= g_0 ||x||. `                                (2.9)

The result is symmetric under `A -> -A` and therefore treats either protected sign.

### Proof

Because `N_hi[H,H]` is positive semidefinite of rank `q`, its kernel

` F = ker N_hi[H,H] `                                          (2.10)

has dimension at least `m-q`. For every `x in F`, positivity implies

` x^T N_hi[H,H] x=0. `                                         (2.11)

Using (2.1)-(2.4),

` sigma x^T A_b[H,H] x
 = sigma x^T A_0[H,H]x
   +x^T P[H,H]x
   -x^T N_hi[H,H]x
   -x^T N_lo[H,H]x
   +sigma x^T T[H,H]x
 >= (g-h-delta)||x||^2
 = g_0||x||^2. `                                                (2.12)

Now `P_H` is an isometry, and by Cauchy-Schwarz,

` ||A_b P_Hx|| ||x||
 >= | <P_Hx, A_bP_Hx> |
 = |x^T A_b[H,H]x|
 >= g_0||x||^2. `                                               (2.13)

Hence (2.9). The singular-value max-min principle on the particular subspace `F` gives (2.8). QED.

### What the theorem buys

1. **All same-sign added eigenvalues are free.** Their number, orientation and magnitude do not enter; they contribute the PSD term `P[H,H]` in the favorable direction.
2. **All small opposite-sign eigenvalues cost one scalar threshold.** Regardless of their number, `N_lo<=hI` costs only `h`.
3. **All large opposite-sign eigenvalues cost only projected footprint dimension.** Their magnitudes do not enter; the cost is `q=rank N_hi[H,H]`, which can be much smaller than their total count.
4. **Arbitrary outside curvature is free at this stage.** Only `T[H,H]` is charged. Cross and outside blocks can be unbounded because the proof uses the physical Rayleigh quotient and then lower-bounds the full carrier norm.

This is stronger than ordinary operator-norm perturbation whenever the same-sign spectrum is huge or the opposite-sign high spectrum has low physical footprint rank.

## 3. Spectral-threshold corollary

For a single arbitrary symmetric addition

` E=sum_j lambda_j u_j u_j^T, `                                (3.1)

fix `sigma` and a threshold `h>0`. Define

` P=sum_(sigma lambda_j>0) |lambda_j|u_ju_j^T, `
` N_lo=sum_(sigma lambda_j<0, |lambda_j|<=h)|lambda_j|u_ju_j^T, `
` N_hi=sum_(sigma lambda_j<0, |lambda_j|>h)|lambda_j|u_ju_j^T. ` (3.2)

Because these come from one orthonormal spectral decomposition,

` ||N_lo||_op<=h. `                                            (3.3)

Therefore Theorem 2.1 applies with

` q=rank(P_H^T N_hi P_H)
    =rank(N_hi[H,H]). `                                        (3.4)

So an arbitrary spectrum has a rigorous high/low compiler: all large and small eigenvalues of the protected sign are free; every opposite-sign eigenvalue below threshold is paid collectively by `h`; all larger opposite-sign eigenvalues are paid only through the dimension of their projection onto the selected original-coordinate bank.

No commutation between `A_0` and `E` is assumed.

## 4. Hybrid with the completed account02/B12 adaptive theorem

The preceding sign shield can be used as a **baseline generator** for the partner's arbitrary-packet theorem.

Let `V_0:R^(m-q)->R^m` be an isometry onto an `(m-q)`-dimensional subspace of `F` from Theorem 2.1, and put

` M_0=A_b P_H V_0. `                                           (4.1)

Then

` s_(m-q)(M_0)>=g_0. `                                         (4.2)

Now add completely arbitrary symmetric packets `S_1,...,S_R` and set

` N_r=S_r P_H V_0 `                                            (4.3)

at the first stage, followed by the partner's adaptive surviving right-domain compressions. If that theorem spends `q_r` canonical-resonant directions at stage `r`, with factors `eta_r`, and

` Q=sum_r q_r < m-q, `                                         (4.4)

then the partner theorem gives the actual final-matrix inequality

` boxed:
 s_(m-q-Q)( (A_b+sum_r S_r)P_H )
 >= g_0 prod_r eta_r. `                                        (4.5)

The point is that the two mechanisms pay different currencies:

- Theorem 2.1 pays opposite-sign **spectral footprint rank** and a low-spectrum threshold, while making same-sign spectrum free.
- account02/B12 then pays only **canonical-resonant directions** of the remaining arbitrary packets.

Neither step uses packet norm or treats a quadratic remainder probabilistically.

## 5. Actual application of the partner theorem

Take an ORIGINAL-coordinate bank `H` of size `m=7`. Let

` A_0[H,H] >= 2 I_7. `                                         (5.1)

Allow the following simultaneously:

- `P>=0` completely arbitrary, with any rank, orientation and arbitrarily large eigenvalues;
- `N_hi>=0` completely arbitrary in magnitude and global rank, subject only to

  `rank N_hi[H,H] <=1`;                                       (5.2)

- `0<=N_lo<=1/8 I` of arbitrary rank;
- an arbitrary symmetric `T` satisfying only

  `||T[H,H]||_op<=1/8`;                                       (5.3)

  all its cross and outside blocks may be arbitrarily large.

Define

` A_b=A_0+P-N_hi-N_lo+T. `                                    (5.4)

Theorem 2.1, with `sigma=+1`, `g=2`, `h=delta=1/8`, gives a six-dimensional ORIGINAL-coordinate subspace `F subset R^H` such that

` boxed: s_6(A_bP_H V_0)>= 2-1/8-1/8 = 7/4. `                (5.5)

Now add one more completely arbitrary signed rank-one spectral mode

` S=tau u u^T,    tau in R, `                                  (5.6)

with no bound on `|tau|` and no restriction on the orientation of `u`.

On the six-dimensional baseline domain,

` N_1=SP_HV_0 `                                                (5.7)

has rank at most one. Hence its canonical correlations with `Ran(A_bP_HV_0)` satisfy

` c_2=0. `                                                      (5.8)

Apply the **completed account02/B12 adaptive theorem** with `q_1=1`. Its factor is

` eta_1=sqrt(1-c_2^2)=1. `                                     (5.9)

Therefore

` boxed:
 s_5((A_b+S)P_H)
 >= s_5((A_b+S)P_HV_0)
 >= 7/4. `                                                      (5.10)

This is an equation-level use of the designated partner result. The last rank-one eigenvalue may be arbitrarily positive or arbitrarily negative and may be tuned exactly to a destructive resonance in its one affected direction; the other five carrier modes retain the full `7/4` floor.

Because `A=A_b+S` is symmetric,

` lambda_5((A^2)[H,H])=s_5(AP_H)^2 >= (7/4)^2. `              (5.11)

Using the completed five-square receiver quoted in the partner report with `m=7` and `h=7/4`,

` ||p_(X^TAX)||_infinity
 <= (4/7) sqrt(168*pi+9*2^(8/3)*exp(2/3))
 = 14.445886393291724... . `                                   (5.12)

Also

` s_5(A)>=s_5(AP_H)>=7/4>1, `                                  (5.13)

so every matrix in this family genuinely satisfies the owner's target hypothesis of at least three eigenvalues of modulus at least one.

The family includes simultaneously:

- arbitrarily many arbitrarily large positive eigenvalues through `P`;
- arbitrarily many arbitrarily large negative eigenvalues through `N_hi`, provided their aggregate `H`-footprint has rank at most one;
- arbitrarily many small negative eigenvalues through `N_lo`;
- arbitrary huge cross/outside curvature through `T` while its `H x H` compression is small;
- one additional arbitrarily large eigenvalue of either sign and arbitrary orientation through `S`.

Thus the theorem genuinely controls both smaller and larger added eigenvalues of either sign without any convolution argument.

## 6. Why this does not solve the full conjecture

The unpaid structural implication is now explicit. From the bare assumption `s_3(A)>=1`, we do **not** know that there exists an ORIGINAL-coordinate bank `H` with a sign-definite principal core of dimension at least five after paying the projected footprint rank of the opposite-sign high spectrum. The live correction set already shows that several naive principal-minor and fixed cross-rank dichotomies fail.

A promising next step is therefore a sign-sensitive bank dichotomy:

> either some ORIGINAL-coordinate bank has a quantitative one-sided Rayleigh floor and the opposite-sign high spectrum has low projected footprint rank (so Theorem 2.1 plus the adaptive partner compiler closes that branch), or every bank has large opposite-sign footprint, which should force a two-sided crossing / grouped-bank / Schur / physical-pair certificate.

That implication is not proved here.

## 7. Continuity status

This run proves an essentially bounded density only through the cited five-square receiver. It does **not** establish a continuous density representative for the full family, and it certainly does not establish continuity for the unrestricted conjecture.

## 8. Source pins

Control repository: `yspennstate/math-research-brain`, branch `main`; startup control head observed at `664bfdb0433fbf565f817d7fafa439fb39dd9e6b`, later refreshed before publication. OWNER CONTROL revision remained `2026-09-22.15`; programme revision remained `2026-09-22.5`.

Partner mathematics applied: `yspennstate/math-open-problems@3e7c3dea777f9cfbae2d6311372daf447bd01ef0`, path `proofnet24/QFORM-density/fleet-2026-09-22/account02/B12/20260924T075526Z-account02-B12-r11/REPORT.md`.

Full target status: **OPEN / NOT PROVED / NOT DISPROVED**.
