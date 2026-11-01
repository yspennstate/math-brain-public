SIGNED IN - working on the quadratic-form bounded-density conjecture (universal constant), account fleet01, slot B09, 2026-09-24T10:47:16Z.
attacking: the indefinite-pair macroscopic-crossing endpoint: force a genuine Schur third resource before any reciprocal scalar pivot, and convert it either to direct logarithmic-pair smoothing or to anchored overlap-two compound mass.

# fleet01/B09 r35 — indefinite physical pair forces Schur third-resource currency

Programme: `QFORM-DENSITY-3EIG-20260922`  
Role: bilinear block mechanism / analytic derivation and exact structural identities  
Status: **ESSENTIAL_STEP_APPLIED / NEW SUPPORTING THEOREM / PARTNER RESULT APPLIED / FULL QFORM OPEN**  
Execution label: **WITHOUT_VERIFIED_BRAIN**

The unrestricted conjecture remains OPEN. Continuity for the unrestricted target remains OPEN. The result below is a pair-local structural/density compiler; it does not prove that a uniformly conditioned indefinite physical pair must exist.

## 1. Fresh premises and corrections consumed


The proof does **not** use law-uniform pointwise van-der-Corput decay, arbitrary-joint coarea, post-rotation independence, a bounded conditional spectral-density supremum, or the false implication that a single cross minor alone proves bounded density. It also respects the latest designated-partner obstruction `QFORM-SCALARPIVOT-RANK2-CURRENCY-FORCING-FALSE-DENSE-MIXEDFRAME-v1`: no scalar pivot is selected before the two-coordinate Schur resource is aggregated.

Analytic dependency used exactly at Section 3: `QFORM-PHYSICAL-PAIR-LOG-ENVELOPE-v1` / `QFORM-PAIR-LOG-SMALLBALL-SMOOTHING-v1`, source

`yspennstate/math-open-problems@f7f0fedb2d93b46824f96cac1164af6f8a55626f`

`proofnet24/QFORM-density/interactive/20260922T180015Z-pair-log/PAIR_LOG_THEOREM.md`.

Its general statement is: for an invertible indefinite ORIGINAL-coordinate pair `B`, with

`D=|det B|`, `kappa=sigma_min(B)`,

if after completing that pair the remainder `R` satisfies

`sup_t P(|R-t|<rho) <= H sqrt(rho)`,

then

`||p_Q||_infinity <= 4 sqrt(2H) (D*kappa)^(-1/4)`.

Essential boundedness is proved there; continuity is not claimed.

## 2. Exact Schur setup

Fix a literal ORIGINAL-coordinate pair `H={h1,h2}` and write the full symmetric matrix in physical coordinates as

`A = [[B,M],[M^T,C]]`,

where `B=A[H,H]` is `2 x 2`, `M=A[H,L]`, and `L=H^c`.

Assume throughout Sections 2--6 that `B` is invertible. Define the exact Schur remainder

`S = C - M^T B^(-1) M`.                                      (2.1)

For `i,j in L`, let

`N_H(i,j) = det A[H union {i}, H union {j}]`,                  (2.2)

where the first set indexes rows and the second columns. The block determinant identity gives

`boxed: N_H(i,j) = det(B) S_ij.`                               (2.3)

Thus every entry of the Schur remainder is literally an anchored physical third-compound minor divided by `det B`.

## 3. Direct density payment from one Schur diagonal

### Theorem 3.1 — `QFORM-INDEFINITE-PAIR-SCHUR-DIAGONAL-v1`

Assume `B` is indefinite and invertible. If for some literal `i in L`

`|S_ii| >= sigma > 0`,                                        (3.1)

then the FULL ambient quadratic form, with every other coefficient and affine term arbitrary, has an essentially bounded density satisfying

`boxed:
 ||p_(X^T A X)||_infinity
 <= 8 * 2^(1/4) * (D*kappa*sigma)^(-1/4).`                     (3.2)

Consequently every interval `I` obeys

`boxed:
 P{X^T A X in I}
 <= 8 * 2^(1/4) * (D*kappa*sigma)^(-1/4) |I|.`                 (3.3)

Continuity is not asserted by this route.

### Proof

Write the original independent pair variables as `x=(X_h1,X_h2)` and the complementary variables as `z=X_L`. Including arbitrary affine terms, completing the fixed pair gives exactly

`Q = (x + B^(-1)(Mz+q))^T B (x + B^(-1)(Mz+q)) + R(z)`,       (3.4)

where the quadratic part of `R` is `S`.

Fix all complementary coordinates except `z_i`. Then

`R(z) = S_ii z_i^2 + beta z_i + gamma`                         (3.5)

for deterministic `beta,gamma` under that conditioning. Completing the scalar square shows that, for every center `t` and `rho>0`, the set

`{|S_ii z_i^2 + beta z_i + gamma - t| < rho}`

has total Lebesgue length at most

`2 sqrt(2 rho / |S_ii|)`.

Indeed after translation/scaling it is `{ |y^2-a|<epsilon }`; if `a<=epsilon` its length is at most `2sqrt(2epsilon)`, and if `a>epsilon` the two symmetric intervals have total length `2(sqrt(a+epsilon)-sqrt(a-epsilon))`, maximized at `a=epsilon`.

Because the physical input density of `z_i` is at most one and is independent of the other original coordinates,

`sup_t P(|R-t|<rho) <= 2 sqrt(2) sigma^(-1/2) sqrt(rho).`       (3.6)

Thus the pair-log theorem applies with

`H = 2 sqrt(2) sigma^(-1/2)`.

Substitution into `4 sqrt(2H)(D*kappa)^(-1/4)` gives

`4 sqrt(4sqrt(2)) (D*kappa)^(-1/4) sigma^(-1/4)
 = 8*2^(1/4)(D*kappa*sigma)^(-1/4)`,

which is (3.2). No coordinate rotation of the random inputs occurs. QED.

## 4. Spectral forcing: the Schur remainder has operator norm at least one

### Theorem 4.1 — `QFORM-PAIR-SCHUR-SPECTRAL-FORCING-v1`

For **any** invertible physical pair `B` (definite or indefinite), if

`s_3(A) >= 1`,                                                  (4.1)

then its Schur remainder (2.1) satisfies

`boxed: ||S||_op >= 1.`                                        (4.2)

### Proof

Define

`A_0 = [[B,M],[M^T,M^T B^(-1) M]]`.                            (4.3)

It factors as

`A_0 = F B F^T`,
`F = [[I_2],[M^T B^(-1)]],`                                    (4.4)

so `rank(A_0)<=2`. Moreover

`A-A_0 = [[0,0],[0,S]]`,                                       (4.5)

hence `||A-A_0||_op=||S||_op`. By the Eckart--Young characterization of the third singular value,

`s_3(A) = inf_(rank R<=2) ||A-R||_op <= ||A-A_0||_op`,

which proves (4.2). QED.

This exact rank-two approximation is the key point: the third spectral resource cannot disappear when an invertible physical pair is completed. It must survive quantitatively in `S`.

## 5. If the Schur diagonal is small, a disjoint physical mixed-minor bank is large

### Theorem 5.1 — `QFORM-SCHUR-DIAGONAL-OR-CROSSCUT-v1`

Assume `||S||_op>=1`. Fix `0<=eta<1`. Then at least one of the following holds:

1. **literal Schur square:** `max_i |S_ii| >= eta`;
2. **disjoint Schur crossing:** there is a literal partition `L=I disjoint_union J` such that

`boxed: ||S[I,J]||_op >= (1-eta)/2.`                            (5.1)

Consequently, in branch 2,

`boxed:
 sum_(i in I, j in J) |N_H(i,j)|^2
 >= D^2 (1-eta)^2 / 4.`                                        (5.2)

### Proof

Suppose branch 1 fails. Choose a unit eigenvector `v` of `S` with eigenvalue `lambda` satisfying `|lambda|=||S||_op>=1`. Put

`d = sum_i S_ii v_i^2`, so `|d|<eta`.                          (5.3)

Randomly assign each coordinate independently to `I` or `J` with probability `1/2`. Let

`Z(I,J)=v_I^T S[I,J] v_J`.                                     (5.4)

Every unordered off-diagonal pair is cut with probability `1/2`, and contributes the same scalar regardless of orientation, hence

`E Z = (lambda-d)/4`.                                           (5.5)

Therefore some literal partition satisfies

`|Z| >= |lambda-d|/4 >= (1-eta)/4`.                            (5.6)

Since `||v_I||_2^2+||v_J||_2^2=1`,

`||v_I||_2 ||v_J||_2 <= 1/2`.                                  (5.7)

Thus

`||S[I,J]||_op >= |Z|/(||v_I|| ||v_J||) >= (1-eta)/2`,

proving (5.1). By (2.3), the anchored mixed-minor bank is exactly `det(B) S[I,J]`; Frobenius norm dominates operator norm, so

`sum |N_H(i,j)|^2 = D^2 ||S[I,J]||_F^2
 >= D^2 ||S[I,J]||_op^2
 >= D^2(1-eta)^2/4`.

QED.

No single good minor is selected. The entire disjoint bank is aggregated before any reciprocal payment.

## 6. Main target-level compiler for an indefinite physical pair

### Theorem 6.1 — `QFORM-INDEFINITE-PAIR-SCHUR-EXIT-v1`

Assume the owner target `s_3(A)>=1` and let `B` be any invertible **indefinite** literal physical pair, with

`D=|det B|`, `kappa=sigma_min(B)`.

Then, taking `eta=1/2`, at least one of the following holds:

**(A) direct density payment**

`boxed:
 ||p_Q||_infinity <= 8 sqrt(2) (D*kappa)^(-1/4),`               (6.1)

with the same coefficient in `P{Q in I}<=C|I|`;

or

**(B) anchored overlap-two currency**: some literal partition `L=I disjoint_union J` satisfies

`boxed:
 sum_(i in I,j in J)
 |det A[H union {i}, H union {j}]|^2
 >= D^2/16.`                                                    (6.2)

The density conclusion in (A) is essential boundedness; continuity is not separately proved.

### Proof

Theorem 4.1 gives `||S||op>=1`. Apply Theorem 5.1 with `eta=1/2`. If a Schur diagonal has magnitude at least `1/2`, Theorem 3.1 gives

`8*2^(1/4)(D*kappa/2)^(-1/4)=8sqrt(2)(D*kappa)^(-1/4)`.

Otherwise (5.2) gives (6.2). QED.

### Quantitative near-singular trichotomy

For every `epsilon in (0,1]`, the same pair satisfies at least one of:

`boxed:
(A_epsilon) ||p_Q||_infinity <= 8sqrt(2) epsilon^(-3/4);`       (6.3)

`boxed:
(B_epsilon) kappa < epsilon;`                                  (6.4)

or

`boxed:
(C_epsilon) sum_(i in I,j in J)|N_H(i,j)|^2
             >= epsilon^4/16`                                  (6.5)

for some disjoint literal partition.

Indeed, if `kappa>=epsilon`, then for the two singular values `s1>=kappa` of `B`,

`D*kappa = s1*kappa^2 >= kappa^3 >= epsilon^3`,                 (6.6)

so branch (A) of Theorem 6.1 implies (6.3). In branch (B),

`D=s1*kappa >= kappa^2 >= epsilon^2`,

and hence `D^2/16>=epsilon^4/16`.

This is the practical endpoint needed after the preceding triangle-crossing work: a well-conditioned indefinite physical pair cannot leave an unspecified third resource. It either pays the density immediately or forces a macroscopic **anchored overlap-two third-compound bank**. The only third alternative is a quantitatively near-singular pair, precisely the chamber where the existing singular-pair mechanisms are designed to operate.

## 7. Relation to the latest fleet02/B09 obstruction

The fresh fleet02/B09 handoff `20260924T104241Z-fleet02-B09-QFORM-auto11` proves that a scalar-pivot-first currency `|a|^2 Delta_2` can vanish throughout a target-valid dense mixed-frame family even though a pre-pivot mixed-frame theorem pays uniformly.

Theorem 6.1 does not contradict or reuse that false scalar-pivot implication. It starts with an **invertible 2x2 physical pair as a whole**, forms its exact rank-two Schur approximation, and invokes `s_3(A)>=1` only after the rank-two part has been removed. The residual resource is therefore an operator-level Schur quantity, and (5.2) aggregates its complete anchored mixed-minor bank before inversion.

This suggests the next bridge should be pair-first rather than scalar-pivot-first in the indefinite crossing branch.

## 8. Required designated-partner result applied to an actual inequality

I applied the completed fleet02/B09 theorem `QFORM-ZERO-HUBPAIR-ARBITRARY-REMAINDER-v1`, canonical source commit

`yspennstate/math-open-problems@03ec6ccf1de2e2544e850cbda25d460aacae6a1b`.

Let `m>=8`, let `c,d,w1,w2 in R^m` be orthonormal flat Walsh vectors, and let all physical inputs be independent with densities bounded by one. Define

`Q_* = 2 U <c,Y> + 2 V <d,Y>
       + <w1,Y>^2 - 3 <w2,Y>^2.`                               (8.1)

The two literal hub coordinates `(U,V)` have zero physical core. Their full complementary coupling rows are `c,d`, so

`Delta = ||c||^2||d||^2-<c,d>^2 = 1`.                         (8.2)

The partner theorem therefore gives the **continuous** density bound

`boxed: ||p_(Q_*)||_infinity <= 2sqrt(2) < 2.829`,             (8.3)

and directly

`boxed: P{Q_* in I} <= 2sqrt(2)|I|`.                           (8.4)

The compressed deterministic spectrum is

`{1,-1,1,-1,1,-3}`,                                            (8.5)

so this is an actual owner-target instance (indeed six eigenvalues have modulus at least one). The arbitrary same-bank remainder allowed by the partner theorem is genuinely used here through both positive and negative dense Walsh squares.

## 9. Deterministic checks

A 100-instance random algebra check with invertible indefinite `2x2` pair `B`, random `M`, and random symmetric `C` verified:

- `rank(A_0)<=2` in every instance;
- `s_3(A)<=||S||op` in every instance to floating precision;
- the exact bordered-minor identity `N_H(i,j)=det(B)S_ij` with maximum absolute numerical error `1.07e-14`.

A separate brute-force check on 100 random normalized symmetric `6x6` Schur matrices verified the cut inequality (5.1); the smallest observed slack `max_cut ||S_IJ||op-(1-eta)/2` was positive (`0.287...`) in that finite sample. These are regression checks only, not proof.

Constants:

`8*2^(1/4)=9.513656920021768...`,
`8sqrt(2)=11.313708498984761...`.

No Monte Carlo output-density histogram is used.

## 10. Remaining implication

The full conjecture remains OPEN. The next B09 step is

`QFORM-INDEFINITE-PAIR-OMEGA2-AGGREGATE-OR-NEARSINGULAR-EXIT-v1`:

> starting from the parametric trichotomy (6.3)--(6.5), compile the forced anchored overlap-two bank into an existing whole-bank bilinear receiver without selecting a tiny minor; in the `kappa<epsilon` branch, pass quantitatively to the established singular-pair/rank-one-cross or promoted-hub mechanisms while retaining arbitrary cross rank and same-bank curvature.

The new theorem removes the prior ambiguity about where the third spectral resource lives after an invertible indefinite pair is chosen. It does **not** yet prove that one of the existing receivers pays every forced overlap-two bank, and it does not prove a uniformly good physical pair exists under the bare spectral hypothesis.
