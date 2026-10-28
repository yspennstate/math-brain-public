SIGNED IN - working on the quadratic-form bounded-density conjecture (universal constant), account account02, slot B16, 2026-09-22T22:31:25Z.
attacking: two-bank Pluecker disjointness—turn projected volume mass into a genuine original-coordinate product partition, then test the high-leverage obstruction.

# account02/B16 auto12 — disjoint Pluecker mass gives two full product banks

Status: `NEW SUPPORTING THEOREM + EXACT HIGH-LEVERAGE OBSTRUCTION / FULL QFORM OPEN`.
Execution: `WITHOUT_VERIFIED_BRAIN`.


The full target remains: independent real `X_i` with densities at most one, symmetric `A` with at least three eigenvalues of magnitude at least one, prove a universal bound on the density of `X^T A X` or exhibit a valid counterexample. The result below closes a substantial exact-rank-three branch but does not cover every exact-rank-three frame and does not by itself treat arbitrary additional spectrum.

## 1. Completed designated-partner theorem actually used

I use account03/B16 run `20260922T215409Z-account03-B16-QFORM-r18`, canonical report

`yspennstate/math-open-problems@a8103979d7666d4087a23134adf547ab0232c653:proofnet24/QFORM-density/fleet-2026-09-22/account03/B16/20260922T215409Z-account03-B16-QFORM-r18/REPORT.md`.

Its `QFORM-TWO-BANK-CROSSBLOCK-L2-v1` theorem states, in the zero-residual-cross-block specialization, the following. Let

`A=U Lambda U^T`,  `U^T U=I_3`,  `Lambda=diag(lambda_1,lambda_2,lambda_3)`,

with each `|lambda_j|>=1`. For a partition of the ORIGINAL coordinates `[n]=I disjoint_union J`, put

`G_I=U_I^T U_I`,  `G_J=U_J^T U_J`.

If both Gram matrices are positive definite, then the full quadratic form has a bounded continuous density and

`||p_Q||_infinity <= 3 e |det Lambda|^(-1/3) [det G_I det G_J]^(-1/6)`.   (1.1)

The proof is product-safe: the two independent objects are the disjoint original-coordinate groups `X_I,X_J`; projected spectral coordinates inside a bank are never declared independent. The theorem follows by unconditional bounded-density projection estimates followed by an exact joint L2 Fresnel/Plancherel cross operator.

## 2. Pluecker notation and two exact identities

Let `r_i in R^3` denote row `i` of `U`, and write the physical leverage

`ell_i=||r_i||_2^2`.

Since `U^T U=I_3`,

`sum_i ell_i=3`.                                                     (2.1)

For every three-element coordinate set `S`, define its Pluecker volume weight

`w_S=det(U_S)^2 >=0`.                                                (2.2)

Cauchy--Binet gives

`sum_{|S|=3} w_S=det(U^T U)=1`.                                     (2.3)

For every coordinate subset `I`, another Cauchy--Binet application gives the exact partial-volume identity

`det G_I = sum_{S subset I, |S|=3} w_S`.                            (2.4)

There is also an exact one-point marginal identity

`sum_{S: i in S} w_S = ell_i`.                                      (2.5)

For completeness, define

`F(x_1,...,x_n)=det(sum_j x_j r_j r_j^T)`.

Cauchy--Binet expands `F=sum_S w_S prod_{j in S}x_j`. At `x_j=1`, the matrix inside the determinant is `I_3`, so Jacobi's formula gives

`partial_i F(1)=tr(r_i r_i^T)=ell_i`.

Differentiating the Cauchy--Binet expansion gives the left side of (2.5).

Thus the Pluecker weights form a probability distribution on physical triples whose one-coordinate inclusion probabilities are exactly the leverages.

## 3. New theorem — QFORM-DISJOINT-PLUECKER-TWO-BANK-v1

Define the disjoint-pair Pluecker mass

`D_disj := sum_{S,T: |S|=|T|=3, S cap T=emptyset} w_S w_T`.          (3.1)

If `D_disj>0`, then

`||p_Q||_infinity <= 6 e |det Lambda|^(-1/3) D_disj^(-1/6)`.         (3.2)

In particular the density is continuous on this branch.

### Proof

Choose a random partition `[n]=I disjoint_union J` by independently sending each original coordinate to `I` or `J` with probability `1/2`. By (2.4),

`det G_I det G_J
 = sum_{S,T} w_S w_T 1_{S subset I}1_{T subset J}`.              (3.3)

If `S cap T` is nonempty the indicator product vanishes identically. If `S,T` are disjoint triples, the six prescribed coordinates must be sent to specified opposite sides, an event of probability exactly `2^(-6)=1/64`. Therefore

`E_I[det G_I det G_J] = D_disj/64`.                                 (3.4)

Hence some deterministic original-coordinate partition satisfies

`det G_I det G_J >= D_disj/64`.                                     (3.5)

Both determinants are then positive, so the completed account03/B16 theorem (1.1) applies. Substitution gives

`||p_Q||_infinity
 <=3e |det Lambda|^(-1/3)(D_disj/64)^(-1/6)
 =6e |det Lambda|^(-1/3)D_disj^(-1/6)`,

which is (3.2). No conditioning or independence in rotated coordinates occurs. QED.

## 4. Leverage-only corollary and a concrete universal branch

Let `S,T` be independent Pluecker-random triples with law `P(S)=w_S`. By (2.5),

`P(i in S)=ell_i`.

Therefore the union bound gives

`P(S cap T nonempty)
 <= sum_i P(i in S, i in T)
 = sum_i ell_i^2`.                                                   (4.1)

Thus

`D_disj >= 1-sum_i ell_i^2`.                                        (4.2)

Consequently, whenever `sum_i ell_i^2 <=1-sigma` for some `sigma>0`,

`||p_Q||_infinity <=6e sigma^(-1/6)`.                               (4.3)

Here I used `|det Lambda|>=1`.

A particularly simple source-valid branch follows from a maximum-leverage hypothesis. Since (2.1) gives `sum ell_i=3`,

`sum_i ell_i^2 <= (max_i ell_i) sum_i ell_i =3 max_i ell_i`.        (4.4)

Hence if

`max_i ell_i <=1/6`,                                                 (4.5)

then `D_disj>=1/2` and

`||p_Q||_infinity <=6 e 2^(1/6)
 =18.307009134325725...`.                                            (4.6)

This is an exact-rank-three universal bounded-continuous-density theorem obtained by genuine original-coordinate product separation. It is stronger in leverage range than the earlier `max ell_i<=1/12` exact-rank-three diffuse branch quoted in the current state, although it is only an exact-rank-three statement and its constant is not optimized.

## 5. Exact obstruction: disjoint full spectral banks can vanish completely

The new theorem also exposes its exact failure mode. Consider the valid exact-rank-three family

`A_m = [1] direct_sum (J_m/m) direct_sum (-J_m/m)`.                  (5.1)

Its nonzero spectrum is exactly `{1,1,-1}`. Take the rank-three frame whose rows are

- one singleton row `e_1`,
- `m` rows `e_2/sqrt(m)`,
- `m` rows `e_3/sqrt(m)`.

Every nonzero Pluecker triple must contain the singleton coordinate, one coordinate from the positive diffuse bank, and one coordinate from the negative diffuse bank. Hence any two nonzero Pluecker triples intersect in the singleton coordinate. Therefore

`D_disj=0`.                                                         (5.2)

Equivalently, for every original-coordinate partition `I,J`, at least one of `det G_I,det G_J` is zero: two disjoint original-coordinate groups can never each carry the full three-dimensional spectral projection.

This is stronger than merely observing that the leverage bound (4.5) fails. Here

`sum_i ell_i^2 =1+2/m`,                                             (5.3)

and the exact disjoint-pair volume mass is zero.

Nevertheless this is not a QFORM counterexample. The same family is uniformly paid after source-bank grouping: the preceding account02/B16 theorem `QFORM-FINITE-LINE-BANK-COMPRESSION-v1` compresses its three collinear original-coordinate banks before paying any physical determinant and gives a dimension-free bound. Thus the failure in (5.2) is a structural obstruction specifically to the strategy “find two disjoint full three-dimensional spectral banks, then apply the two-bank Fresnel theorem.”

## 6. What has changed in the proof frontier

The partner theorem turns any quantitatively nondegenerate pair of full spectral banks into a bounded continuous density. The present result supplies a deterministic way to manufacture such banks from Pluecker geometry whenever `D_disj` is positive at a controlled scale, and in particular closes every exact-rank-three frame with maximum leverage at most `1/6`.

The singleton-plus-two-diffuse-banks family shows this cannot be the entire structural reduction. The remaining exact-rank-three obligation is now sharply localized to frames whose Pluecker measure has a strong common-coordinate/intersection structure. In that regime one must exploit the common high-leverage physical coordinates as scalar/pair pivots and aggregate the remaining one- or two-dimensional original-coordinate banks before reciprocal determinant payment. For arbitrary higher-rank `A`, the complementary spectral quadratic form additionally creates a residual cross block; account03/B16's full `r>0` theorem shows that a quantitatively transverse residual cross space can help rather than hurt through the augmented determinant. The missing synthesis is therefore:

`QFORM-PLUECKER-INTERSECTION-OR-AUGMENTED-BANK-v1`:
from three singular/eigenvalue directions of size at least one, either obtain controlled disjoint Pluecker mass and use (3.2), or convert the common-coordinate intersection structure (and, in higher rank, residual cross singular directions) into an existing source-valid scalar/pair/grouped-bank branch.

No claim is made here that this dichotomy has already been proved. Full QFORM remains OPEN.
