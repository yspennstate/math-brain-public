SIGNED IN - working on the quadratic-form bounded-density conjecture (universal constant), account account01, slot B18, 2026-09-23T21:20:23Z.
attacking: low-hub equal-spectrum residual geometry: replace finite source rays by one exact rank-two ORIGINAL-coordinate source bank, using Livshyts--Paouris--Pivovarov and the completed account02/B18 scalar/dependent-pair receiver at a physical anchored-minor inequality.

# account01/B18 r39 — rank-two source-bank aggregate minor transfer

Programme: `QFORM-DENSITY-3EIG-20260922`.
Run: `20260923T212023Z-account01-B18-qform-auto11-r39`.
Status: **PROVED SUPPORTING TARGET-LEVEL SHARPENING / DESIGNATED PARTNER APPLIED / FULL QFORM OPEN**.
Execution: `WITHOUT_VERIFIED_BRAIN`.
Continuity: obtained separately from an already-completed grouped theorem on the same branch; the account02/B18 receiver by itself is used only for the sharper essential bound.

## 1. Fresh scope and correction boundary

The owner target is unchanged: independent real original coordinates with arbitrary probability densities bounded by one, and an arbitrary real symmetric matrix having at least three eigenvalues of modulus at least one. No moments, iid assumption, symmetry, centering, bounded support, connected support, log-concavity, Gaussianity, or smoothness is assumed.

The full conjecture remains OPEN. This run does not use arbitrary-joint rank-three coarea, a conditional projection-density cap as independence, post-rotation independence, law-uniform pointwise quadratic-phase decay, a fixed good physical minor, deletion of a small nonzero term, or an arbitrary-remainder near-zero continuation.

The fresh correction `QFORM-NEARZERO-ARBITRARY-REMAINDER-EXTENSION-FALSE-v1` at math-open-problems commit `b3a997d0819eccceb313da22e1e04c0dd92c6b42` is preserved: a small nonzero hub core cannot be replaced by zero while allowing an arbitrary environment remainder. The theorem below uses an EXACT zero physical pivot and conditions only ORIGINAL outside coordinates, so the retained quadratic block is exact and the outside variables create affine terms only.

## 2. Primary literature theorem and exact hypothesis match

The external anti-concentration theorem used positively is:

G. Livshyts, G. Paouris, P. Pivovarov,
*On sharp bounds for marginal densities of product measures*,
Israel J. Math. 216 (2016), 877--889; arXiv:1507.07949, Theorem 1.1.

Its relevant statement is: if

`f(x)=prod_i f_i(x_i)`

is a genuine product probability density and every one-dimensional factor satisfies `||f_i||_infinity<=1`, then every `k`-dimensional orthogonal marginal has density bounded by `2^(k/2)`.

No moment, iid, support, log-concavity, centering, symmetry, or smoothness condition is imposed. The theorem gives a marginal/joint-density cap, not independence after rotation.

A consequence used below is the following full-row-rank linear-map version. If `B` is a real `2 x m` matrix of rank two and `X in R^m` has independent cap-one coordinates, let

`G=B B^T`.

Then

`boxed: ||p_(B X)||_infinity <= 2 / sqrt(det G).`                    (2.1)

Indeed `G^(-1/2)B` has orthonormal rows, so LPP applies to `G^(-1/2) B X`; scaling back multiplies the density cap by `1/sqrt(det G)`.

I also checked the focused quadratic-form literature again. Standard quadratic-form concentration theorems such as Hanson--Wright/Bernstein variants assume moment/subgaussian conditions and do not match the owner's rough cap-one class. The older Bentkus--Goetze--Zaitsev approximation theory assumes iid normalized sums and finite moments. None is an exact replacement for the present quantifiers. This is only a hypothesis comparison, not a novelty claim.

## 3. Completed designated-partner theorem actually applied

The analytic receiver is the completed account02/B18 theorem

`QFORM-CAPPED-SCALAR-DEPENDENT-PAIR-v1`,

source:

- math-open-problems commit `ba2e2fbc9d22196f83c4ae35080e7f3d23a55fa1`;
- `proofnet24/QFORM-density/fleet-2026-09-22/account02/B18/20260923T013147Z-bf13c29b/REPORT.md`.

It states: let `S` be a scalar with density cap `K`, genuinely independent of a possibly dependent pair `(C,D)` whose joint density has cap `M`. If the symmetric quadratic matrix in `(S,C,D)` has zero `S^2` pivot and determinant `Delta!=0`, then arbitrary affine terms are harmless (after deterministic translation) and

`boxed:
 ||p_Q||_infinity
 <= 3 (2 M K)^(2/3) |Delta|^(-1/3).`                               (3.1)

The pair coordinates need not be independent.

The newest account02/B18 theorem, `QFORM-NULLHUB-DIFFUSE-PRIVATE-BANK-v1` at commit `529be48498963ede3243fd4a2b00a0104442fc05`, remains compatible with this run and gives a different Fourier/Brascamp--Lieb payment when a private two-frame is coordinate-diffuse. I do not duplicate that theorem here.

## 4. General source-bank theorem

### `QFORM-ZEROPIVOT-RANK2-SOURCE-BANK-MINOR-MASS-v1`

Let `S` be one ORIGINAL coordinate with density cap at most one. Let `X_K=(X_j)_(j in K)` be a disjoint bank of ORIGINAL coordinates, independent of `S`, each with density cap at most one. Suppose that, after conditioning all other ORIGINAL coordinates, the retained polynomial factors through

`Z = B X_K in R^2`,                                                 (4.1)

where `B` is `2 x |K|` of full row rank, and its quadratic part in `(S,Z_1,Z_2)` is a symmetric invertible matrix `H` with

`H_11=0`.                                                           (4.2)

Arbitrary deterministic affine terms in `(S,Z)` are allowed. Put

`G=B B^T`                                                           (4.3)

and define the invariant currency

`Xi := det(G) |det(H)|`.                                            (4.4)

Then

`boxed:
 ||p_Q||_infinity
 <= 3*4^(2/3) Xi^(-1/3).`                                          (4.5)

The estimate is uniform in every outside conditioning value, hence also holds for the unconditional ambient quadratic form.

### Proof

By (2.1), the pair `Z` has joint density cap

`M <= 2 / sqrt(det G)`.                                             (4.6)

The scalar `S` is an original coordinate disjoint from the bank, hence is genuinely independent of the whole pair `Z` and has `K<=1`.

Because `H` is invertible, any affine term can be removed by a deterministic translation of the three retained variables. Such translations do not mix the scalar with the pair and preserve all density caps and the independence statement. Apply account02/B18 (3.1):

`||p_Q||_infinity
 <= 3 [4/sqrt(det G)]^(2/3) |det H|^(-1/3)
 = 3*4^(2/3) [det(G)|det(H)|]^(-1/3).`

This is (4.5). QED.

### Coordinate invariance

If the pair coordinates are replaced by `Z'=T Z`, then

`det G'=(det T)^2 det G`

while the quadratic matrix transforms with

`det H'=(det T)^(-2) det H`.

Thus `Xi` is basis-independent. It is a genuine physical currency, not an artefact of a chosen pair basis.

## 5. Physical anchored-minor identity

The preceding theorem has a particularly useful physical form. Let the retained physical principal block be indexed by `{0} union K`, with `0` the original scalar/hub. Write its exact rank-three factorization

`A_I = C^T H C`,                                                    (5.1)

where

`C = [[1,0,...,0],
      [0,      ],
      [0,  B   ]]`

maps `(X_0,X_K)` to `(S,Z_1,Z_2)`. Thus `A_00=H_11=0` and the bank has exact source rank two.

For every pair `i<j` in `K`, Cauchy--Binet gives

`det A_{0ij}
 = det(H) det([e_1,c_i,c_j])^2.`                                   (5.2)

All these nonzero minors have the same sign, namely the sign of `det H`. Summing their absolute values and applying two-dimensional Cauchy--Binet to `B` yields

`sum_(i<j in K) |det A_{0ij}|
 = |det H| sum_(i<j) det(B_{ij})^2
 = |det H| det(B B^T)
 = Xi.`                                                             (5.3)

Therefore Theorem (4.5) can be written entirely in physical coordinates:

`boxed:
 ||p_Q||_infinity
 <= 3*4^(2/3)
    [ sum_(i<j in K) |det A_{0ij}| ]^(-1/3).`                        (5.4)

This is an aggregate-before-reciprocal statement. It may remain constant-scale even when every individual anchored `3 x 3` minor is tiny.

### Spectral/exterior form

Equivalently, in an exact-rank-three representation

`A_I=R M R^T`, `M` invertible,

let the hub row be `a` and assume the bank rows span a two-plane. Put

`S_K=sum_(j in K) r_j r_j^T`.

Then

`sum_(i<j in K) |det A_{0ij}|
 = |det M| a^T adj(S_K) a
 = |det M| sum_(i<j in K) det[a,r_i,r_j]^2.`                        (5.5)

If `a=sqrt(lambda) v` with `|v|=1`, this is

`|det M| lambda det( (P_(v^perp) S_K P_(v^perp))|_(v^perp) )`,      (5.6)

which is exactly the grouped determinant currency appearing in the earlier account03/B18 rank1+rank2 theorem.

## 6. Prior solution / no novelty claim / continuity tracked separately

An exact qualitative solution of this same rank-one-bank plus rank-two-bank branch already exists in account03/B18 r21,

`QFORM-NULL-RANK1-PLUS-RANK2-GROUPED-v1`,

`proofnet24/QFORM-density/fleet-2026-09-22/account03/B18/20260923T021509Z-account03-B18-QFORM-r21/REPORT.md`.

That theorem uses LPP and an affine zero-pivot receiver to prove a **continuous** density with

`||p_Q||_infinity <= 12 Xi^(-1/3).`                                 (6.1)

Thus I do **not** claim novelty for the qualitative branch. The new contribution here is:

1. applying the completed account02/B18 receiver at the singleton-original-coordinate endpoint, improving the essential-density constant from `12` to

`3*4^(2/3)=7.559526299369239...`;                                  (6.2)

2. identifying the exact physical currency with the total anchored principal-minor mass (5.3);
3. applying that sharper physical theorem to the newest low-hub equal-spectrum source geometry in Section 7.

Continuity is tracked separately as requested: account03/B18 r21 supplies a continuous `C_0` representative on the same branch. Combining that existence with the sharper essential bound (5.4), continuity forces the continuous representative itself to obey the sharper bound pointwise: if it exceeded the essential bound at one point, it would exceed it on an interval of positive measure.

## 7. Actual application to the low-hub equal-spectrum target family

Use the completed account02/B18 low-hub family from commit

`c99a85972a70c210b19dd41128300ad55a9b8cb4`,

and the finite-ray normalization from account01/B18 r38. Its physical matrix has exactly the three nonzero eigenvalues

`{-1,1,1}`                                                          (7.1)

for every `0<eta<1/64`.

The normalized residual frame is

`W H`, `W^T W=I_3`,                                                  (7.2)

where

`r=(x,y,-eta)`, `||r||^2=1-eta^6`,
`H=(I-r r^T)^(1/2)`,
`H r=eta^3 r`, `det H=eta^3`,                                      (7.3)

and the deterministic active-coordinate change `T` has

`det T=c=sqrt(1-eta^2)`.                                            (7.4)

The distinguished original coordinate is an exact zero-diagonal hub with active row `rT`.

Now let `K` be ANY literal ORIGINAL-coordinate residual bank such that its raw `W`-rows span exactly a two-dimensional plane `E`. No ray decomposition inside `K` is required: the bank may contain arbitrarily many noncollinear rows in that plane.

Let

`G_K = sum_(j in K) w_j w_j^T`                                     (7.5)

and define its anchored exterior-volume currency

`kappa_K := r^T adj(G_K) r
         = sum_(i<j in K) det[r,w_i,w_j]^2.`                        (7.6)

Because `rank G_K=2`, `kappa_K>0` exactly when `r` is transverse to the bank plane.

Choose an orthonormal basis `u_1,u_2` of `E`. The bank contribution to the spectral variable depends only on the two aggregate coordinates generated by `u_1,u_2`; hence Section 4 applies after conditioning every original coordinate outside the hub and `K`.

The same exact determinant cancellation used in r38 is

`det[r;u_1 H;u_2 H]=det[r;u_1;u_2]`.                               (7.7)

Indeed

`det[rH;u_1H;u_2H]=det(H)det[r;u_1;u_2]=eta^3 det[r;u_1;u_2]`,

while `rH=eta^3 r`, so the factor `eta^3` cancels.

After the active transform `T`, the retained three-variable quadratic determinant is

`|Delta| = c^2 det[r;u_1,u_2]^2`.                                  (7.8)

Let `G_E` be the `2 x 2` coefficient Gram of the bank aggregates in the basis `(u_1,u_2)`. Then

`det(G_E) det[r;u_1,u_2]^2 = kappa_K`.                              (7.9)

Substituting (7.8)--(7.9) into Theorem 4 gives the explicit whole-line target-valid inequality

`boxed:
 ||p_Q||_infinity
 <= 3*4^(2/3)
    [ (1-eta^2) kappa_K ]^(-1/3).`                                 (7.10)

By Section 6 the density has a continuous `C_0` representative on this branch.

### Constant-scale exit

If

`kappa_K >= 1/64`,                                                   (7.11)

then for every `0<eta<1/64`,

`||p_Q||_infinity
 <=3*4^(2/3)
   [64/(1-1/4096)]^(1/3)
 =30.2405663814... <30.241.`                                       (7.12)

This is independent of the number of original coordinates in the bank.

## 8. Relation to r38 and exact gain

The preceding account01/B18 r38 theorem paid the same low-hub family when the residual `W`-rows lie in at most four one-dimensional source rays, with bound `<13.738`. That argument extracts two independent ray-bank aggregates.

The new theorem is complementary rather than a replacement: it pays a **single arbitrarily large exact rank-two source bank** directly, without decomposing it into rays and without paying the number of directions in the bank. The two coordinates of the bank aggregate may be dependent; only their LPP joint-density cap is used.

Thus the source-complexity obstruction is sharpened. The low-hub family is now paid whenever a constant amount of anchored exterior volume is carried either

- by finitely many rank-one source rays (r38), or
- inside one literal rank-two original-coordinate source bank (this run).

What remains is the genuinely source-entangled situation in which substantial anchored exterior volume is carried only through rank-three source banks or through cross-bank interactions that cannot be reduced to a retained `1+2` original-product packet without conditioning on rotated variables.

## 9. Why the new correction does not invalidate this proof

The fresh near-zero arbitrary-remainder counterexample factors a small nonzero two-hub core against an adversarial same-bank remainder and produces a logarithmic product singularity. Here:

- the scalar pivot is **exactly zero**, not merely small;
- the retained pair is an actual linear image of one literal product bank;
- the scalar is a disjoint original coordinate and is genuinely independent of the whole pair;
- every omitted original coordinate is conditioned, so it creates affine terms only;
- the retained quadratic determinant is nonzero and is spent explicitly through (3.1).

No small coefficient is deleted and no arbitrary residual quadratic function is treated as independent noise.

## 10. Literature audit conclusion and remaining implication

The primary LPP theorem matches the product-source assumptions exactly and supplies the pair cap needed by the account02/B18 receiver. I found no exact published theorem in the focused search that directly states the owner's unrestricted arbitrary-dimension, arbitrary-non-iid cap-one quadratic-form density theorem. Existing classical quadratic-form concentration/approximation results impose materially stronger distributional hypotheses. This search miss is not used as evidence of novelty.

The full QFORM conjecture remains **OPEN / NOT PROVED / NOT DISPROVED**.

The next structural implication is now precise: in the low-hub equal-spectrum stress geometry, prove that every residual source configuration either contains a literal rank-two bank with `kappa_K>=c>0`, reduces to a bounded-number rank-one ray decomposition, or enters another already-paid ridge/private-cross/grouped-source packet. A generic exact rank-three source bank is not covered by (7.10), and an approximately rank-two bank cannot be replaced by an exact one by deleting its small third direction under the rough-law corrections.

## 11. Exact checks performed

1. Algebraic check of the aggregate-minor identity: for random numerical `2 x m` matrices `B` and random invertible symmetric `H` with `H_11=0`, direct construction `A=C^T H C` gave

`sum_(i<j)|det A_{0ij}| = |det H| det(BB^T)`

to floating-point precision in repeated trials.

2. Exterior check: for random rank-two `W` banks and random `r`, direct computation gave

`r^T adj(W^T W) r = sum_(i<j) det[r,w_i,w_j]^2`

to floating-point precision.

3. Constant in (7.12):

`3*4^(2/3)*(64/(1-1/4096))^(1/3)
 =30.24056638137171...`.

The identities themselves are proved exactly above; the numerical checks are regression checks only.

## 12. Source pins

- LPP primary source: arXiv:1507.07949; Israel J. Math. 216 (2016), 877--889, Theorem 1.1.
- Designated partner account02/B18 receiver: `math-open-problems@ba2e2fbc9d22196f83c4ae35080e7f3d23a55fa1`.
- Newest account02/B18 private-bank theorem: `math-open-problems@529be48498963ede3243fd4a2b00a0104442fc05`.
- Existing qualitative rank1+rank2 grouped solution/continuity: account03/B18 r21, `proofnet24/QFORM-density/fleet-2026-09-22/account03/B18/20260923T021509Z-account03-B18-QFORM-r21/REPORT.md`.
- Low-hub equal-spectrum source family: `math-open-problems@c99a85972a70c210b19dd41128300ad55a9b8cb4`.
- Prior finite-ray closure: `math-open-problems@35fc7bb8691555a8cfdd3aefc06da310ed19e175`.
- Fresh near-zero correction: `math-open-problems@b3a997d0819eccceb313da22e1e04c0dd92c6b42`.

No email/push, new task, cross-account authentication, paid/remote call, public release, repository visibility change, permission expansion, or scheduler-state change was made.
