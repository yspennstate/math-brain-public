SIGNED IN - working on the quadratic-form bounded-density conjecture (universal constant), account fleet03, slot B16, 2026-09-22T20:23:47Z.
attacking: replace the false projection-height/coarea interface by an original-coordinate determinant-scaled three-coordinate theorem using scalar-pivot half-Riesz and indefinite-pair smoothing.

# fleet03/B16 — determinant-scaled physical triple theorem

Run: `20260922T202347Z-fleet03-B16-QFORM-r15`  
Programme: `QFORM-DENSITY-3EIG-20260922`  
Assignment: Projection-product interaction.  
Execution: `WITHOUT_VERIFIED_BRAIN`.  
Status: `PROVED SUPPORTING THEOREM / AMBIENT PHYSICAL-TRIPLE BRANCH / FULL QFORM OPEN`.

## 1. Target and correction-aware scope

The full target remains open: for every dimension, every independent real input with one-dimensional density at most one, and every symmetric real matrix with at least three eigenvalues of modulus at least one, prove one universal finite bound on the density of `X^T A X`, or give a counterexample.

This run does **not** use the false arbitrary-joint rank-three coarea estimate, any positive moment of a conditional projection-density height, receiver-only fiber suprema, law-uniform pointwise van der Corput decay, or independence after rotation. It works in the original independent coordinates throughout.

The new result is stronger than the earlier localized theorem in one precise sense: a physical `3 x 3` block is paid at its **determinant scale**, without requiring each of its three eigenvalues separately to be bounded below. It is still only a supporting branch because the bare three-large-global-eigenvalue hypothesis does not force one physical triple with determinant bounded below by a universal constant.

## 2. Source-valid inputs

### 2.1 Rank-two affine half-Riesz estimate

From

`yspennstate/math-open-problems@e542b1a6ef471b329e4e88a6553e1aacb45acc1a`

`proofnet24/QFORM-density/interactive/20260922T161801Z-rank-two-fusion/REPORT.md`,

for every invertible symmetric rank-two quadratic form `Y^T S Y + beta^T Y + c` in independent cap-one coordinates,

`sup_t E |Y^T S Y + beta^T Y + c - t|^(-1/2)
 <= 16 sqrt(30) |det S|^(-1/4)`                                           (2.1)

when the affine vector lies in the range of the rank-two frame. In dimension two with frame `I_2`, this includes **every** affine vector. The general arbitrary-ambient-affine constant `128` is therefore unnecessary in the two-coordinate application below.

### 2.2 Indefinite physical-pair logarithmic smoothing

From

`yspennstate/math-open-problems@f7f0fedb2d93b46824f96cac1164af6f8a55626f`

`proofnet24/QFORM-density/interactive/20260922T180015Z-pair-log/PAIR_LOG_THEOREM.md`,

an invertible indefinite original-coordinate pair `P`, with

`D=|det P|`, `kappa=sigma_min(P)`,

admits the logarithmic pair envelope. If the scalar remainder obeys

`sup_t P(|R-t|<rho) <= H sqrt(rho)`,

then

`||p_Q||_infinity <= 4 sqrt(2H) (D kappa)^(-1/4)`.                       (2.2)

For a one-dimensional quadratic-affine remainder `lambda Z^2+beta Z+c`, independent cap-one input gives

`H=10/sqrt(|lambda|)`,

and hence

`||p_Q||_infinity <= 8 sqrt(5) (D kappa |lambda|)^(-1/4)`.              (2.3)

This use does not require a lower bound on every eigenvalue of the full `3 x 3` block; (2.3) follows directly from the general pair envelope plus the one-dimensional small-ball lemma.

### 2.3 Designated partner fleet04/B16

The completed partner report

`yspennstate/math-open-problems@0f2d6290352a984c4e4ae0b024f8c27c7a2bb473`

`proofnet24/QFORM-density/fleet-2026-09-22/fleet04/B16/20260922T191443Z-fleet04-B16-QFORM-r3/REPORT.md`

proves that in the two-diffuse-block cube family, for the conditional spectral projection height `M_m`,

`E M_m = m`,

and more generally every positive moment either diverges with `m` or is infinite already at fixed `m` at exponent at least two. Applying this to the candidate receiver-only bridge

`||p_Q||_infinity <= C E M_m`                                           (2.4)

makes its right side `C m`, while the same exact-rank-three family has a known dimension-uniform output-density bound. Thus (2.4) is quantitatively non-uniform and cannot be the needed projection-to-curvature interface. The proof below deliberately replaces that failed conditional-height payment by original-coordinate scalar/pair smoothing.

## 3. Main theorem

### Theorem — `QFORM-PHYSICAL-TRIPLE-DETERMINANT-v1`

Let `X_1,X_2,X_3` be independent real random variables with probability densities bounded by one. Let `B` be any invertible real symmetric `3 x 3` matrix, let `ell in R^3`, and let `c in R`. Then

`Q_B = X^T B X + ell^T X + c`

has an essentially bounded density and

`boxed( ||p_(Q_B)||_infinity <= 16 sqrt(30) 2^(1/4) |det B|^(-1/3) )`    (3.1)

In particular,

`16 sqrt(30) 2^(1/4) = 104.216889989... < 105`.                        (3.2)

No sign assumption on `B` is imposed.

### Ambient corollary

Let `A` be any real symmetric `n x n` matrix and let `S` be any three original coordinates such that the physical principal block `B=A[S,S]` is invertible. For independent cap-one input coordinates,

`boxed( ||p_(X^T A X)||_infinity <= 16 sqrt(30) 2^(1/4)
                                         |det A[S,S]|^(-1/3) )`.       (3.3)

All additional eigenvalues, all outside quadratic coefficients, and all couplings between `S` and its complement are arbitrary.

Essential boundedness is proved. Continuity is **not** proved by this argument.

## 4. Proof of the three-variable theorem

Write

`Delta=|det B| > 0`, `s=Delta^(1/3)`.

Use the physical-coordinate representation

`B = [[a,b,c1],[b,d,e],[c1,e,f]]`.

We split according to the physical diagonal entries. The constants are chosen so the two branches overlap with room to spare.

### Case A: a physical scalar pivot has size at least `s/2`

Assume, after permuting coordinates if necessary,

`|a| >= s/2`.                                                          (4.1)

Complete the square only in the original coordinate `X_1`. Conditional on `(X_2,X_3)`, the shifted variable

`V = X_1 + m(X_2,X_3)`

still has density at most one. The form becomes

`Q_B = a V^2 + R(X_2,X_3)`,                                            (4.2)

where `R` is a quadratic-affine form with Hessian equal to the `2 x 2` Schur complement

`S_2 = B[{2,3},{2,3}] - a^(-1) (b,c1)^T (b,c1)`.                       (4.3)

Since `B` is invertible and `a!=0`, `S_2` is invertible and

`det S_2 = det B / a`.                                                  (4.4)

For every fixed value of the residual variables, the pushforward of a cap-one density by `aV^2` obeys

`p_(aV^2 | X_2,X_3)(u) <= |a|^(-1/2) |u|^(-1/2)`                       (4.5)

on the appropriate half-line. Therefore, for almost every target `t`,

`p_(Q_B)(t)
 <= |a|^(-1/2) E |R-t|^(-1/2)`.                                       (4.6)

Apply (2.1) to the two independent coordinates `(X_2,X_3)`. Because the rank-two frame is `I_2`, its arbitrary affine term lies in the frame range. Using (4.4),

`||p_(Q_B)||_infinity
 <= 16 sqrt(30) |a|^(-1/2) |det S_2|^(-1/4)`
` = 16 sqrt(30) |a|^(-1/4) Delta^(-1/4)`
` <= 16 sqrt(30) 2^(1/4) Delta^(-1/3)`.                                (4.7)

This proves (3.1) in Case A.

### Case B: all three scalar pivots are smaller than `s/2`

Assume

`|a|,|d|,|f| < s/2`.                                                    (4.8)

I first claim that at least one off-diagonal entry has magnitude at least `9s/16`. If instead

`|b|,|c1|,|e| < 9s/16`,                                                (4.9)

then the exact determinant expansion

`det B = a d f + 2 b c1 e - a e^2 - d c1^2 - f b^2`                   (4.10)

gives

`|det B|
 < [1/8 + 2(9/16)^3 + 3(1/2)(9/16)^2] s^3`
` = (1957/2048) s^3`
` < s^3 = Delta`,                                                      (4.11)

contradicting the definition of `s`. Hence, after a permutation,

`|b| >= 9s/16`.                                                        (4.12)

Consider the original-coordinate physical pair

`P=[[a,b],[b,d]]`.

Its determinant is strictly negative:

`det P = ad-b^2
 < s^2/4 - 81s^2/256
 = -17s^2/256 <0`,                                                     (4.13)

so `P` is invertible indefinite. Compare it to `P_0=[[0,b],[b,0]]`. The diagonal perturbation has operator norm `<s/2`; singular-value perturbation gives

`kappa:=sigma_min(P)
 >= |b|-max(|a|,|d|)
 > 9s/16-s/2
 = s/16`.                                                             (4.14)

Complete this physical pair. Because the whole matrix `B` is `3 x 3`, the Schur remainder is a single quadratic-affine variable

`R=lambda X_3^2+beta X_3+gamma`,                                      (4.15)

and the block determinant identity gives

`|det P| |lambda| = |det B| = Delta`.                                 (4.16)

Apply (2.3). With `D=|det P|`, (4.14)-(4.16) yield

`||p_(Q_B)||_infinity
 <= 8 sqrt(5) (kappa Delta)^(-1/4)`
 < 8 sqrt(5) 16^(1/4) Delta^(-1/3)`
 = 16 sqrt(5) Delta^(-1/3)`.                                          (4.17)

Since `16 sqrt(5) < 16 sqrt(30) 2^(1/4)`, Case B is cheaper than Case A. This proves (3.1). QED.

## 5. Proof of the ambient corollary

Condition on every original coordinate outside the selected triple `S`. The three coordinates in `S` remain independent and retain their density caps. Every outside-outside term becomes a scalar constant and every cross term becomes an affine term in the selected three coordinates. The quadratic Hessian on those selected coordinates remains exactly `B=A[S,S]`.

The three-variable theorem therefore gives (3.3) uniformly in the conditioning. Averaging the conditional densities preserves the same essential-supremum bound. No spectral-coordinate independence is asserted. QED.

## 6. Exact-rank-three Pluecker interpretation

For an exact-rank-three matrix

`A=R Lambda R^T`, `R^T R=I_3`,

and a physical triple `S`,

`det A[S,S] = det(Lambda) det(R_S)^2`.                                 (6.1)

Thus the theorem gives

`||p_Q||_infinity
 <= 16 sqrt(30) 2^(1/4)
    ( |det Lambda| det(R_S)^2 )^(-1/3)`                                (6.2)

whenever that Pluecker atom is nonzero. Cauchy-Binet gives

`sum_{|S|=3} det(R_S)^2 = 1`.                                         (6.3)

This makes the remaining structural debt explicit: selecting one triple and paying its reciprocal cube root can still lose dimension when the Pluecker mass is diffuse. The next universal step must aggregate the determinant bank **before** reciprocal payment, or combine it with a diffuse/ridge certificate. A simple positive conditional-projection-height moment cannot perform that aggregation by the designated partner obstruction in Section 2.3.

## 7. What changed relative to the previous B16 mechanism

The previous B16 run closed the exact-rank-three nested-heavy branch by a leverage/pair dichotomy. This run changes the mechanism to a determinant-scaled local theorem that:

1. applies to **any** nonsingular physical triple, all signatures;
2. allows arbitrary affine translations generated by outside conditioning;
3. remains valid for an ambient matrix of arbitrary rank and arbitrary additional spectrum;
4. avoids all receiver-only conditional projection-height moments; and
5. replaces separate lower bounds on the three local eigenvalues by one scale-correct determinant payment.

It does **not** turn a diffuse determinant bank into one large physical determinant. Hence it is supporting progress, not a full proof.

## 8. Status and next implication

New claim: `QFORM-PHYSICAL-TRIPLE-DETERMINANT-v1` — **PROVED conditional on the explicitly pinned, completed rank-two half-Riesz and physical-pair logarithmic lemmas, whose exact scopes were re-read before use.**

Full QFORM conjecture: **OPEN / NOT PROVED / NOT DISPROVED**.  
Continuous density: **NOT PROVED by this run**.

First unpaid target-level implication: derive a dimension-free **aggregate-before-inversion** inequality which converts the three-large-global-eigenvalue hypothesis into either (i) a determinant-bank average compatible with (3.3), (ii) a diffuse/ridge product certificate, or (iii) a quantitative physical pair certificate, without taking positive moments of conditional projection heights. The exact-rank-three Pluecker identity (6.3) is the natural algebraic starting point; arbitrary additional spectrum must then be retained rather than discarded.
