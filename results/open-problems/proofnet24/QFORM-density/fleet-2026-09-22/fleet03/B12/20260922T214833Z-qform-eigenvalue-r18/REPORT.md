SIGNED IN - working on the quadratic-form bounded-density conjecture (universal constant), account fleet03, slot B12, 2026-09-22T21:48:33Z.
attacking: two-bank spectral-leakage stability: use a quantitative indefinite two-bank pair plus any third global core singular direction, then absorb arbitrary outside eigenvalues with the fleet04/B12 mixed-norm shear compiler.

# QFORM B12: two-bank third-source and spectral-leakage stability

## Status

This run proves a new target-level additional-eigenvalue reduction. It strictly weakens the previous B12 three-bank hypothesis in the indefinite branch: only TWO disjoint scalar banks are required, while the third large singular direction may lie anywhere in an arbitrary reduced core. A completely arbitrary outside quadratic remainder, with arbitrary signs, rank and eigenvalue magnitudes, is then added by the completed fleet04/B12 mixed-norm shear theorem.

The full QFORM conjecture remains OPEN / NOT PROVED / NOT DISPROVED. The theorem establishes essential boundedness in its stated scope. Continuity is not claimed.


## Source-valid dependencies actually read

1. **Assigned partner fleet04/B12: mixed-norm shear compiler.**
   `yspennstate/math-open-problems@9ce47e2a0f2c8434d901df13a218450c2189d80e`,
   `proofnet24/QFORM-density/fleet-2026-09-22/fleet04/B12/20260922T192552Z-fleet04-B12-mixed-shear-r1/REPORT.md`.
   If `(U,R)` has joint density `h(u,r)` and
   `M(h)=int esssup_u h(u,r) dr`, then every measurable `psi` satisfies
   `||p_(U+psi(R))||_infinity <= M(h)`. No independence between `U` and `psi(R)` is assumed.

2. **Arbitrary-rank indefinite physical-pair theorem.**
   `yspennstate/math-open-problems@742ac943440e41925fe09db9a8c02a96cbd83dbc`,
   `proofnet24/QFORM-density/interactive/20260922T180015Z-pair-log/FULL_MATRIX_PAIR_EXTENSION.md`.
   For independent cap-one coordinates, `s_3(H)>=s>0`, and an invertible indefinite original-coordinate pair `B` with `D=|det B|` and `kappa=sigma_min(B)`,
   `||p||_infinity <= 3*400^(1/3)*(D^2*kappa*s)^(-1/6)`, uniformly over affine terms and all other coefficients.

3. **One-dimensional bank density cap.** The normalized projection theorem recorded by fleet02/B02 from Rudelson--Vershynin gives: if `Y=sum u_i X_i`, `sum u_i^2=1`, and the independent input densities are <=1, then `||p_Y||_infinity<=sqrt(2)`.

No post-rotation independence, pointwise van-der-Corput decay, arbitrary-joint coarea bound, normalized worst conditional fiber, or one-good-minor implication is used.

## Setup: a reduced core plus arbitrary outside completion

Let `T_1,T_2,K,R` be pairwise disjoint sets of ORIGINAL coordinates. Let `u_j` be deterministic unit vectors supported on `T_j`, and put

`Y_j=u_j^T X_(T_j)`, `j=1,2`,
`Z=X_K`, and `W=(Y_1,Y_2,Z)`.

Because the coordinate blocks are disjoint, `Y_1,Y_2`, all coordinates of `Z`, and all coordinates of `R` are mutually independent. Moreover `||p_(Y_j)||_infinity<=sqrt(2)`.

Assume the quadratic form factors through the two bank statistics on `T_1,T_2` and can be written

`Q = W^T H W + 2 W^T C R + psi(R)`,                         (2.1)

where

- `H` is an arbitrary real symmetric matrix of size `2+|K|`;
- `C` is completely arbitrary;
- `psi` is any measurable function of the remaining ORIGINAL coordinates `R` (in particular an arbitrary quadratic form `R^T D R`);
- the leading `2x2` principal block of `H` on `(Y_1,Y_2)` is denoted by `B`.

Thus the outside block may carry arbitrarily many additional eigenvalues of either sign and arbitrary magnitude, and the cross coupling `C` is unrestricted.

## Theorem 1: two disjoint banks + arbitrary third spectral source

Assume

`s_3(H) >= s > 0`.                                             (3.1)

### Indefinite pair branch

If `B` is invertible indefinite, put

`D=|det B|`, `kappa=sigma_min(B)>0`.

Then

`boxed(||p_Q||_infinity <= 6*400^(1/3)*(D^2*kappa*s)^(-1/6)).`   (3.2)

### Definite pair branch

If `B` is positive or negative definite, then

`boxed(||p_Q||_infinity <= 2*pi/sqrt(|det B|)).`                 (3.3)

The definite branch does not need (3.1).

### Proof of the indefinite branch

Scale only the two bank variables:

`V_1=sqrt(2)Y_1`, `V_2=sqrt(2)Y_2`.

The coordinates `(V_1,V_2,Z)` are independent and all have density cap one. Let

`S=diag(1/sqrt(2),1/sqrt(2),I_K)`.

In the cap-one variables the fixed quadratic core is

`H'=S H S`.

The standard singular-value product inequality gives, for every k,

`s_k(S H S) >= s_min(S)^2 s_k(H)`.

Since `s_min(S)=1/sqrt(2)`, (3.1) yields

`s_3(H') >= s/2`.                                               (3.4)

The bank pair becomes `B'=B/2`, hence

`D'=|det B'|=D/4`, `kappa'=kappa/2`.                            (3.5)

Fix `R=r`. The cross term `2W^T C r` becomes an arbitrary affine term in the independent cap-one core variables; the quadratic matrix remains exactly `H'`. Apply the arbitrary-rank indefinite-pair theorem to this conditional core. Uniformly in r,

`||p_(Q-psi(r) | R=r)||_infinity`
` <=3*400^(1/3)*[((D/4)^2)*(kappa/2)*(s/2)]^(-1/6)`
` =3*400^(1/3)*[D^2*kappa*s/64]^(-1/6)`
` =6*400^(1/3)*(D^2*kappa*s)^(-1/6).`                           (3.6)

Let `g_R(r)` be the product density of the remaining original coordinates and `h(u,r)=g_R(r)p_(Q-psi(R)|R=r)(u)`. Then the conditional estimate gives

`M(h)=int esssup_u h(u,r)dr`
` <=6*400^(1/3)*(D^2*kappa*s)^(-1/6).`                          (3.7)

Now apply the assigned fleet04/B12 mixed-norm shear theorem with the ACTUAL remainder `psi(r)`. It gives (3.2). This is the promised explicit application of the assigned partner theorem. No independent-convolution step appears. QED.

### Proof of the definite branch

Fix all outside variables. The remaining two-bank polynomial is

`F(y)=y^T B y+ell^T y+c`.

The joint density of `(Y_1,Y_2)` is at most `2`. Completing the square translates `y` and does not change area. If `B>0`,

`Leb{y: 0 <= y^T B y <= t} = pi*t/sqrt(det B)` for `t>=0`.

Therefore for every interval I of length epsilon,

`P(F(Y) in I | outside) <= 2*pi*epsilon/sqrt(det B)`.

The same follows for `B<0` after reflection. Hence the conditional density cap is `2*pi/sqrt(|det B|)`, uniformly in all outside variables. Integrating the outside variables, equivalently applying the partner shear compiler, gives (3.3). QED.

## Corollary 2: quantitative two-bank spectral-leakage stability

Let a protected reduced core `H_0` satisfy

`s_3(H_0)>=s_0>0`,

and let its bank pair `B_0` be invertible with

`sigma_min(B_0)>=beta_0>0`.

Add arbitrary signed spectral terms

`sum_r tau_r (v_r^T (W,R))^2`,

where the direction splits as `v_r=(v_{r,c},v_{r,R})` between the reduced core W and the arbitrary outside block R. Define the core leakage matrix

`F=sum_r tau_r v_{r,c}v_{r,c}^T`,

and let

`Delta=||F||_op <= sum_r |tau_r| ||v_{r,c}||_2^2`.               (4.1)

The outside pieces `tau_r(v_{r,R}^T R)^2` and all generated core/outside cross terms are unrestricted: they are absorbed into `psi(R)` and `C` respectively.

Assume

`Delta < min(s_0,beta_0)`.                                      (4.2)

Then Weyl's inequality gives

`s_3(H_0+F) >= s_0-Delta`,                                      (4.3)

while the bank-pair compression obeys

`sigma_min(B_0+F_[12]) >= beta_0-Delta`.                        (4.4)

Because (4.2) prevents an eigenvalue of the `2x2` bank pair from crossing zero, its inertia is unchanged.

If `B_0` is indefinite, the final pair remains indefinite and

`|det(B_0+F_[12])| >= (beta_0-Delta)^2`.

Theorem 1 therefore gives

`boxed(||p_Q||_infinity`
` <=6*400^(1/3)*[(beta_0-Delta)^5*(s_0-Delta)]^(-1/6)).`        (4.5)

If `B_0` is definite, it remains definite and

`boxed(||p_Q||_infinity <=2*pi/(beta_0-Delta)).`                (4.6)

This is an explicit signed-eigenvalue stability theorem. The `tau_r` may have either sign and may be arbitrarily large; only their aggregate weighted leakage into the protected reduced core is charged. In particular, if every added spectral direction lies entirely in the outside block (`v_{r,c}=0`), then `Delta=0` and arbitrarily many arbitrarily large added eigenvalues cost exactly ZERO.

## Corollary 3: the third source need not be a third bank

Suppose the indefinite pair has

`D>=1`, `kappa>=1`,

and the reduced core has `s_3(H)>=1`. Then

`||p_Q||_infinity <=6*400^(1/3)=44.2083779836...`.              (5.1)

The third singular direction may be any combination of the original core coordinates `Z`; it need not be a third scalar bank and need not have a fixed sign relative to the pair. This is the main structural gain over the previous B12 three-disjoint-bank theorem.

For the stress family

`Q=X_0^2 + (m^(-1/2)sum_{j=1}^m X_j)^2 - (m^(-1/2)sum_{j=m+1}^{2m}X_j)^2 + arbitrary completion`,

take the two diffuse banks as the indefinite pair and `X_0` as the third source. The bound (5.1) is uniform in m and remains valid after arbitrary outside completion/cross coupling of the form (2.1). The earlier specialized B12 estimate `33.079...` is numerically sharper for this exact family, but the present theorem needs only TWO grouped banks and allows the third source to have arbitrary core geometry.

## Corollary 4: explicit half-gap stability

If `beta_0=s_0=1` and `Delta<=1/2`, then the indefinite branch gives

`||p_Q||_infinity <= 12*400^(1/3)=88.4167559674...`,            (6.1)

while the definite branch gives

`||p_Q||_infinity <=4*pi`.                                      (6.2)

Thus a protected unit-gap two-bank packet tolerates total signed spectral leakage one half, while every remaining added eigenvalue/coupling outside the protected core is completely unrestricted.

## What is newly paid and what remains unpaid

**Paid here:** once two disjoint original-coordinate banks furnish a quantitative nonsingular pair, an indefinite pair needs only ONE additional singular direction anywhere in the reduced core. All further spectrum in a disjoint outside block is dependence-safely free. Large signed added eigenvalues are also stable under the explicit leakage budget (4.1)-(4.5). This removes the need for a third disjoint scalar bank in the indefinite grouped branch.

**Still unpaid:** the bare hypothesis `s_3(A)>=1` does not yet force two disjoint bank statistics whose pair compression has dimension-free `D,kappa`, nor does it force a protected reduced-core factorization of the form (2.1). The singleton-plus-two-banks family is now paid, but heavily overlapping/Hadamard spectral frames may fail any naive exact two-bank factorization. The next structural obligation is therefore weaker than after r17:

> extract TWO disjoint scalar banks with a quantitative nonsingular pair while retaining any third singular direction in the remaining reduced core, OR fall into an already-paid physical-pair/ridge/localized branch; control the factorization error before reciprocal pair costs are paid.

No claim is made that arbitrary additional eigenvalues help automatically. The theorem proves exactly how they can be charged: zero for the arbitrary outside block, or through the signed core-leakage norm Delta.

## Continuity and integrity

The indefinite source theorem and the mixed-norm shear theorem yield an essentially bounded density. A continuous representative is not established by this argument; the partner's separate mixed translation-modulus condition would suffice if proved for the constructed core, which is not done here.

No Gaussianity, log-concavity, moment, compact-support, connected-support, pointwise Fresnel decay, post-rotation independence, arbitrary-joint coarea, normalized worst-fiber cap, or Monte Carlo assertion is used. Repository transport is not authenticated native receiver-context ingestion: `WITHOUT_VERIFIED_BRAIN`.

Claim IDs: `QFORM-TWO-BANK-THIRD-SOURCE-ARBITRARY-COMPLETION-v1`; `QFORM-TWO-BANK-SPECTRAL-LEAKAGE-STABILITY-v1`.
