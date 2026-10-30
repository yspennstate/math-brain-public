# fleet01/B08 r20 — spectral-gated localized/diffuse split with a dense low-spectrum tail

Programme: `QFORM-DENSITY-3EIG-20260922`  
Run: `20260922T234017Z-fleet01-B08-qform-r20`  
Status: **PROVED SUPPORTING THEOREM; FULL QFORM REMAINS OPEN**  
Execution memory: `WITHOUT_VERIFIED_BRAIN`.

## 1. Exact target and scope

The owner target is the following unrestricted statement: for every dimension, every product law with independent real coordinates having densities at most one, and every real symmetric matrix with at least three eigenvalues of modulus at least one, prove a universal `L^infinity` density bound for `Q=X^T A X`, or give a valid counterexample. No moment, support, log-concavity, Gaussianity, or eigen-coordinate independence assumption is available.

This report proves a new **spectrally invariant localized/diffuse split** for the important case in which the actual spectral window `|A|>=1/96` has rank exactly three. The diffuse side is completely paid, including an arbitrary dense low-spectrum tail. The complementary side is reduced to a quantitatively localized high-spectral direction on at most 95 physical coordinates. This does **not** solve the localized/hybrid side and therefore does not solve full QFORM.

The proof deliberately uses the *actual spectral projection* of `A`, rather than an arbitrarily chosen rank-three component, so cancellation by an untracked remainder cannot fake the three large directions.

## 2. Dependencies and corrections consumed

### Newest Claude package actually applied

Source:

`yspennstate/math-open-problems@e5f71d79eff325201dd0274053d20268ce65b837`

`proofnet24/QFORM-density/interactive/20260922T211500Z-decoupling-brascamp-lieb/FOURIER_ROUTE_REPORT.md`

Section 5.1 proves the localized/diffuse frame identity: after removing coordinates of leverage larger than a threshold, either the surviving frame Gram has a quantitative lower bound, or some unit vector in the selected spectral subspace has most of its mass on the removed coordinates. I use that structural identity below, but replace its exact diagonal-plus-rank-three analytic payment by a perturbatively stable source-coordinate theorem, so that a dense low spectral tail is allowed.

The same source's Theorems D/D'/D5 were checked for compatibility but are not used to transfer row marginals across the low-spectrum perturbation: the owner continuation explicitly warns that singular-value stability alone does not preserve a volume-marginal gate.

`COUNTEREXAMPLE_SEARCH.md` in the same source was also read. Its ruled one-sheet theorem is orthogonal to the present branch; it does not cover arbitrary extra low-spectrum curvature or the convex/two-sheet side.

### Designated partner result actually applied

Partner: fleet02/B08.

Canonical source:

`yspennstate/math-open-problems@c1c6ffe8c742cbba7611b5a3f1d73cf71019f47b`


In the notation needed here, write

`A = R Lambda R^T + C`, `R^T R = I_3`, `s_min(Lambda)>=1`.

Condition original coordinates `H`, put `T=H^c`,

`M=R_T^T R_T`, `eta=||R_H^T R_H||`, `W=R_T M^{-1/2}`.

If on `T`

`C[T,T]=C0+E`,

where `C0` is block diagonal, set

`mu=max_G ||W_G^T W_G||`, `tau=||E||`,

`alpha=(1-sqrt(3mu))/2`, `rho=alpha(1-eta)-tau`.

If `mu<1/3`, `rho>0`, and

`(sqrt(mu/alpha)+sqrt(6) tau/rho)^2 <= 1/2`,                 (P)

then every admissible product input has a **continuous density vanishing at infinity** and

`||p_Q||_infinity <= 9 sqrt(3e)/(2 rho)`.                  (PB)

I apply this theorem below with an actual spectral remainder, `C0=0`, singleton physical blocks, and obtain a numerical universal bound `<99` in the diffuse branch.

### Live corrections respected

The argument does not use uniform pointwise quadratic-phase decay, independence after spectral rotation, arbitrary-joint coarea, worst fiber suprema, conditional projection-density moments, a single well-conditioned physical minor, or a universal rank-three physical cross cut. No moment estimate is used. The low spectral tail is not called a small random-variable perturbation; it is paid inside the partner's physical-coordinate ridge theorem.

## 3. New theorem

### Theorem `QFORM-SPECTRAL-GATED-96-HYBRID-SPLIT-v1`

Let `A` be real symmetric and suppose that at least three eigenvalues of `A` have modulus at least one. Assume in addition that the **actual spectral projection**

`P = 1_{ {|A| >= 1/96} }`

has rank exactly three. Let `R` be any `n x 3` orthonormal matrix spanning `Ran P`; because `P` is spectral we may choose its columns to be eigenvectors and write

`A = R Lambda R^T + C`,

where the three diagonal entries of `Lambda` are the three eigenvalues in the window. Put the invariant leverage scores

`ell_i=P_ii=||r_i||_2^2`,

where `r_i` is row `i` of `R`, and define the physical heavy set

`H={i: ell_i>1/32}`, `L=H^c`,

and

`M=R_L^T R_L`.

Then one of the following two alternatives holds.

**Diffuse alternative.** If

`lambda_min(M)>=1/2`,

then for every independent input with coordinate densities `0<=f_i<=1`, the law of `Q=X^TAX` has a **continuous `C_0` density** and

`||p_Q||_infinity < (864/25) sqrt(3e) < 99`.              (3.1)

**Localized/hybrid alternative.** If

`lambda_min(M)<1/2`,

then there is a unit vector `v in Ran P` such that

`sum_{i in H} |v_i|^2 > 1/2`,                             (3.2)

while

`|H|<=95`.                                                (3.3)

In particular some physical coordinate in `H` satisfies

`|v_i|^2>1/190`.                                          (3.4)

Thus, under this explicit spectral gate, failure of the paid diffuse branch forces a genuine bounded-cardinality hybrid core. No statement is made here that this localized core alone is sufficient for a density bound; that is the remaining implication.

## 4. Proof

### 4.1 The spectral decomposition is honest

Since `rank P=3` and the target assumption supplies at least three eigenvalues of modulus at least one, the three eigenvalues in `Ran P` all have modulus at least one. Hence

`s_min(Lambda)>=1`.

The spectral residual

`C=A-R Lambda R^T`

acts on the orthogonal complement of `Ran P`, and by definition of the window

`||C||_op < 1/96`.                                       (4.1)

This is the key source-valid spectral gate. There is no arbitrary rank-three component whose eigenvalues could be cancelled by an uncontrolled remainder.

Also

`sum_i ell_i=tr P=3`.                                    (4.2)

Since every index of `H` has `ell_i>1/32`, (4.2) gives

`|H|/32 < 3`, hence `|H|<96`, proving (3.3).

### 4.2 The structural localized/diffuse split

Because `R^TR=I_3`,

`M=R_L^T R_L=I_3-R_H^T R_H`.                             (4.3)

Write

`beta=lambda_min(M)`.

If `beta<1/2`, choose a unit vector `u in R^3` attaining the minimum Rayleigh quotient. Set `v=Ru`. Then `||v||=1`, `v in Ran P`, and

`||v_L||^2=u^T M u=beta<1/2`.

Therefore

`||v_H||^2=1-beta>1/2`,

which is (3.2). Since `|H|<=95`, at least one coordinate carries more than `(1/2)/95=1/190` squared mass, proving (3.4).

This is precisely the invariant form of the newest-source localized/diffuse identity; no eigenbasis ambiguity remains because `P`, the leverage scores, and the heavy set are invariant under rotations inside repeated eigenspaces.

It remains to pay the case

`beta>=1/2`.                                              (4.4)

### 4.3 Whiten the surviving physical frame

Condition on the original physical coordinates `X_H`. This keeps the coordinates indexed by `L` independent with the same cap-one marginal densities; all couplings to `H` become affine terms, which the partner theorem permits.

For the partner theorem take `T=L` and

`W=R_L M^{-1/2}`.

Then `W^T W=I_3`. For a surviving physical coordinate `i in L`,

`||w_i||^2 = r_i M^{-1} r_i^T
            <= ||r_i||^2 / beta
            = ell_i/beta
            <= (1/32)/(1/2)
            = 1/16`.                                     (4.5)

Choose singleton blocks in the partner theorem and put

`C0=0`, `E=C[L,L]`.

The zero matrix is block diagonal on those blocks. Compression cannot increase operator norm, so (4.1) gives

`tau=||E||_op <1/96`.                                    (4.6)

Thus the partner block-mass parameter obeys

`mu<=1/16`.                                              (4.7)

Moreover, by (4.3),

`1-eta=1-||R_H^T R_H||_op=lambda_min(M)=beta>=1/2`.       (4.8)

### 4.4 Verify the partner's quantitative gate

The partner defines

`alpha=(1-sqrt(3mu))/2`.

Using (4.7),

`alpha >= (1-sqrt(3/16))/2 = (4-sqrt(3))/8`.

For a completely rational lower estimate, `sqrt(3)<7/4`, so

`alpha>9/32`.                                            (4.9)

Therefore, using (4.6), (4.8), and (4.9),

`rho=alpha(1-eta)-tau
     > (9/32)(1/2)-1/96
     = 25/192 >0`.                                       (4.10)

Next,

`sqrt(mu/alpha)
 < sqrt((1/16)/(9/32))
 = sqrt(2)/3
 < 1/2`,                                                 (4.11)

where the final strict inequality follows from `sqrt(2)<3/2`.

Also, from (4.6) and (4.10),

`tau/rho < (1/96)/(25/192)=2/25`.

Since `sqrt(6)<5/2`,

`sqrt(6) tau/rho <1/5`.                                 (4.12)

Combining (4.11)-(4.12),

`sqrt(mu/alpha)+sqrt(6)tau/rho < 1/2+1/5=7/10`,

and hence

`(sqrt(mu/alpha)+sqrt(6)tau/rho)^2 <49/100<1/2`.         (4.13)

Thus every hypothesis of fleet02/B08's completed theorem is satisfied.

### 4.5 Density and continuity

The partner conclusion (PB) and (4.10) yield

`||p_Q||_infinity
 < 9 sqrt(3e) / (2*(25/192))
 = (864/25) sqrt(3e)
 = 98.6919209293... <99`.                                (4.14)

The same theorem gives a continuous representative vanishing at infinity. Its estimate is uniform in the values of the conditioned coordinates `X_H`; averaging over `X_H` therefore returns the stated conclusion for the original `Q`.

This completes the proof of the theorem.

## 5. Strict enlargement over the earlier raw-leverage spectral-window branch

The point of the new split is that it permits genuinely heavy rows provided no high-spectral direction is mostly trapped in them.

Here is an exact family. Construct an `89 x 3` Parseval frame `R` with rows

- one row `(1/2,0,0)`;
- 24 rows `(1/sqrt(32),0,0)`;
- 32 rows `(0,1/sqrt(32),0)`;
- 32 rows `(0,0,1/sqrt(32))`.

Then `R^TR=I_3`. Put

`Lambda=diag(1,1,-1)`,

`C=(1/192)(I-RR^T)`,

`A=R Lambda R^T+C`.

The spectrum is exactly `1,1,-1` on `Ran R` and `1/192` on its orthogonal complement, so

`rank 1_{|A|>=1/96}=3`.

The maximum high-window leverage is `1/4`, so earlier certificates requiring a raw maximum leverage at most `1/7` (or `1/22`) do not apply. Under the present split, however, the heavy set is just the first coordinate and

`M=diag(3/4,1,1)`,

so the diffuse branch applies.

One can insert the actual values into the partner theorem rather than the worst-case estimates above. The whitened maximum leverage is `mu=1/24`, `tau=1/192`,

`alpha=(1-sqrt(1/8))/2`,

`rho=(3/4)alpha-1/192`,

and the gate left-hand side is `0.1704227630...<1/2`. The resulting density bound is

`||p_Q||_infinity <54.174`.

This family is full rank and contains a nonzero low-spectrum tail; the improvement is therefore not merely an exact-rank-three restatement.

## 6. What this does and does not close

The new theorem pays the following source-valid branch:

`rank 1_{|A|>=1/96}=3` **and** after removing physical coordinates with high-window leverage above `1/32`, every direction of the actual high spectral subspace retains at least half of its squared mass.

It leaves exactly the complementary hybrid packet:

`QFORM-SPECTRAL96-LOCALIZED-HYBRID-v1`:

there is a unit `v` in the actual three-dimensional high spectral subspace with more than half of its mass on at most 95 original coordinates, while an arbitrary dense residual of operator norm below `1/96` remains present. The localized set is bounded in cardinality, but its same-side quadratic block can be indefinite and nearly singular, and the dense tail cannot be discarded by a characteristic-function perturbation argument without moment assumptions.

The next mathematical step should therefore combine one of the bounded-coordinate pivot/pair/hub mechanisms with the still-spread orthogonal high-spectral directions **while retaining the dense tail in a product-preserving ridge or grouped determinant payment**. A single good physical minor is not forced, and the current correction inbox rules out several shortcuts through worst conditional density caps or arbitrary-joint coarea.

## 7. Status

- Full QFORM theorem: **OPEN**.
- Full target continuity: **OPEN**.
- New diffuse spectral-gated branch: **PROVED**, continuous `C_0` density, constant `<99`.
- New structural complement: **PROVED**, >1/2 high-spectral mass on at most 95 physical coordinates.
- No counterexample to QFORM is claimed.
- No independence after spectral rotation is used.
- No moment/support regularity is used.
