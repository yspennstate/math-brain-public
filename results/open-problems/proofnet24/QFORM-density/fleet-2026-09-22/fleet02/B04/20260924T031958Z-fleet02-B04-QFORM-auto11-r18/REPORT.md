SIGNED IN - working on the quadratic-form bounded-density conjecture (universal constant), account fleet02, slot B04, 2026-09-24T03:19:58Z.
attacking: high-leverage residual carrier/deletion dichotomy: exact two-carrier entropy balancing, then same-matrix higher-compound and ridge comparison.

# fleet02/B04 r18 — exact two-carrier volume balance

Programme: `QFORM-DENSITY-3EIG-20260922`.
Status: **NEW SUPPORTING THEOREM / GLOBAL PHYSICAL-WEIGHT OPTIMIZATION / PINNED THEOREM D APPLIED / DESIGNATED PARTNER r47 APPLIED / FULL QFORM OPEN**.
Execution context: `WITHOUT_VERIFIED_BRAIN`.

The unrestricted theorem is not proved here. The result advances the live high-leverage carrier/deletion branch without using moments, support assumptions, log-concavity, a diagonal-basis reduction, post-rotation independence, arbitrary-joint coarea, or pointwise quadratic-phase decay.

## 1. Fresh source pins and first unpaid implication

Fresh owner control remained revision `2026-09-22.15`, QFORM-only, with no applicable stop. The live corrections were re-read immediately before publication.

Pinned source required by the owner:

`yspennstate/math-open-problems@e5f71d79eff325201dd0274053d20268ce65b837`

under

`proofnet24/QFORM-density/interactive/20260922T211500Z-decoupling-brascamp-lieb/`

with `RESULTS.md`, `FOURIER_ROUTE_REPORT.md`, and `COUNTEREXAMPLE_SEARCH.md` all read at that commit. The exact input used below is Theorem D and its arbitrary-weight remark: for a literal original-coordinate cross block `M=A[I,J]`, any probability weight `w_ST` on supported physical `3x3` minors whose I-side row marginals are at most `1/2` gives

`||p_Q||inf <= 6 sqrt(e) G(w)^(-1/6)`,                          (1.1)

where

`G(w)=exp(sum w_ST log det(M_ST)^2 + H(w))`.                    (1.2)

The J-side has no marginal gate. The D' extension permits an I-side cap `h<3/4`, with multiplier

`6 sqrt(e) (2h)^(-1/2)(3-4h)^(-1)`.                            (1.3)

The freshest compatible designated partner is fleet03/B04 r47,

`yspennstate/math-open-problems@24476f8abf801b3e862fd227748790459d731340`,

`proofnet24/QFORM-density/fleet-2026-09-22/fleet03/B04/20260924T024757Z-fleet03-B04-QFORM-auto11-r47/REPORT.md`.

Its completed `QFORM-HIGHER-COMPOUND-DOWNSHIFT-v1` gives, on the same literal cross block,

`||p_Q||inf <= C_* c_m^(-1/6) E_m(M)^(-1/(2m))`,               (1.4)

where `C_*=8.4530212255281768747...` and `c_m=(m!)^(3/m)/6`. In particular

`||p_Q||inf <= 7.659094523616393... E4(M)^(-1/8)`.              (1.5)

The first unpaid implication entering this run was

`QFORM-HIGHLEVERAGE-RESIDUAL-TO-CARRIER-DELETION-DICHOTOMY-v1`:

when the natural E3 law is concentrated on heavy physical carriers, either rebalance at bounded determinant-entropy cost, or show small deletion currency forces a paid anchored/hub/higher-compound endpoint.

## 2. Exact two-carrier balance theorem

Let

`z_S = sum_{|T|=3} det(M_ST)^2`                                 (2.1)

for physical row triples `S`. Fix two distinguished physical rows `i,j`, and aggregate the squared-minor mass into the four faces

`W_ab = sum_{S: 1{i in S}=a, 1{j in S}=b} z_S`, `a,b in {0,1}`. (2.2)

Assume all four displayed masses are positive.

### Theorem — `QFORM-TWO-CARRIER-GEOMETRIC-BALANCE-v1`

Among all supported physical minor laws whose two carrier marginals are **exactly** `1/2`, the largest determinant-entropy currency is

`boxed: G_ij = 2( sqrt(W_00 W_11) + sqrt(W_10 W_01) ).`         (2.3)

The optimal category probabilities are

`q_00=q_11 = sqrt(W_00 W_11) / [2(K0+K1)]`,                    (2.4)

`q_10=q_01 = sqrt(W_10 W_01) / [2(K0+K1)]`,                    (2.5)

where `K0=sqrt(W_00 W_11)` and `K1=sqrt(W_10 W_01)`. Conditional on a category, the optimal law is the canonical squared-minor law inside that category.

Consequently, if the resulting non-carrier row marginals are also at most `1/2`, the pinned Theorem D gives

`boxed: ||p_Q||inf <= 6 sqrt(e) G_ij^(-1/6).`                  (2.6)

### Proof

First optimize the column choice at fixed row triple. If `p_S` is the row-triple law, the conditional Gibbs/log-sum identity shows that choosing

`w(T|S)=det(M_ST)^2/z_S`

maximizes (1.2), and reduces it exactly to

`log G = H(p) + sum_S p_S log z_S`.                             (2.7)

Now coarsen by the four carrier faces. At fixed face probabilities `q_ab`, the same log-sum identity says the optimum inside each face is proportional to `z_S`, reducing (2.7) further to

`F(q)=H(q)+sum_ab q_ab log W_ab`.                               (2.8)

Both carrier marginals equal `1/2` iff

`q_10+q_11=q_01+q_11=1/2`.                                    (2.9)

Together with normalization this forces

`q_00=q_11=r`, `q_10=q_01=1/2-r`.                              (2.10)

Strict concavity makes the optimum unique. Differentiating (2.8) in `r` gives

`log[W_00 W_11/(W_10 W_01)] + 2 log[(1/2-r)/r]=0`,             (2.11)

which is exactly (2.4)-(2.5). Substitution into (2.8) cancels the entropy terms and gives

`F_max=log[2(K0+K1)]`.                                         (2.12)

This proves (2.3). No individual minor is inverted; only aggregated physical squared-minor faces enter.

Equation (2.3) is the two-carrier analogue of the preceding one-carrier geometric currency `2 sqrt(W_0 W_1)`. In particular, two individually near-unit natural marginals are not by themselves a hard obstruction: what matters is whether the complementary face products collapse.

## 3. A dense rank-four physical family

Let `H_8` be the Sylvester Hadamard matrix and let

`U = H_8[:,0:4]/sqrt(8)`,                                      (3.1)

so `U^T U=I_4` and every light physical row has four squared coordinates `1/8`.

Take the exact orthogonal Householder matrix

`V=(1/15) [[14,-2,-3,-4],[-2,11,-6,-8],[-3,-6,6,-12],[-4,-8,-12,-1]]`. (3.2)

Indeed its integer numerator times its transpose is `225 I_4`.

For `L>=1`, stack

`R_L = [ L e_1 ; L e_2 ; U ]`                                  (3.3)

as a `10x4` row matrix and define the literal physical cross block

`M_L = R_L V^T`.                                                (3.4)

This is a deterministic coefficient construction; the random coordinates are never rotated. Every one of the forty physical coefficients of `M_L` is nonzero. For the light rows this is checked exactly by multiplying the four Hadamard sign patterns by the integer numerator in (3.2); the smallest resulting nonzero integer magnitude is one.

Since

`R_L^T R_L = diag(L^2+1,L^2+1,1,1)`,                           (3.5)

the singular values of `M_L` are

`sqrt(L^2+1), sqrt(L^2+1), 1, 1`.                              (3.6)

Define the symmetric `14x14` pure-cross target matrix

`A_L = [[0_10,M_L],[M_L^T,0_4]]`.                              (3.7)

Its nonzero spectrum is

`{ +/-sqrt(L^2+1) (twice), +/-1 (twice) }`.                    (3.8)

Thus it is genuinely non-diagonal and indefinite in the original product coordinates and has eight eigenvalues of modulus at least one.

## 4. Exact face masses and globally optimized Theorem-D law

Use the first two rows of `R_L` as the carriers. Cauchy-Binet on the light Parseval frame gives exactly

`W_00 = e_3(I_4)=4`,                                           (4.1)

`W_10=W_01 = L^2 e_2(I_3)=3L^2`,                              (4.2)

`W_11 = L^4 e_1(I_2)=2L^4`.                                   (4.3)

Hence

`E3(M_L)=2(L^2+1)(L^2+2)`,                                    (4.4)

while each natural carrier marginal is

`[3L^2+2L^4]/[2(L^2+1)(L^2+2)]`,                              (4.5)

which tends to one.

At the Theorem-D cap `1/2`, (2.3) gives the exact global carrier-balanced currency

`boxed: G_D(L)=2(3+2sqrt(2))L^2=2(1+sqrt(2))^2 L^2.`           (4.6)

The category probabilities are

`q_00=q_11=3sqrt(2)-4=0.242640687119...`,                      (4.7)

`q_10=q_01=9/2-3sqrt(2)=0.257359312881...`.                    (4.8)

There is no hidden light-row obstruction. Under the canonical conditional laws the eight light rows have category-wise marginals

`3/8` in face `00`, `1/4` in faces `10` and `01`, and `1/8` in face `11`. (4.9)

Therefore every light row has final marginal exactly

`(3/8)q_00+(1/4)(q_10+q_01)+(1/8)q_11 = 1/4`.                 (4.10)

So (4.6) is the global optimum over **all supported physical 3x3-minor weights** with the pinned D row cap, not a symmetric ansatz.

## 5. Global optimization across the whole proved D/D' window at L=64

The D' extension allows a common cap `h` in `[1/2,3/4)`. On this family, for every such `h`, the unconstrained natural carrier marginal exceeds `3/4` once `L^2>(3+sqrt(33))/2`; hence both carrier caps are active. The conditional Gibbs optimizer is still feasible for all eight light rows: because the expected number of light rows is `3-2h` and the light frame is symmetric, each light marginal is

`(3-2h)/8 < h`.                                                (5.1)

Let

`v_L(h)=log G_h(L)`                                             (5.2)

be the exactly optimized determinant-entropy value after imposing both carrier marginals `h`. The map `v_L` is concave in `h`: it is the value function of a concave entropy-plus-linear objective under affine marginal constraints.

At `h=1/2`, the dual multiplier for either carrier is

`lambda = log( W_10 q_00/(W_00 q_10) )
        = log(L^2/sqrt(2))`,                                   (5.3)

so by the envelope theorem

`v_L'(1/2)=2 lambda = 4 log L - log 2`.                         (5.4)

For the exact D' coefficient

`B_L(h)=6sqrt(e)(2h)^(-1/2)(3-4h)^(-1) exp[-v_L(h)/6]`,        (5.5)

we obtain

`[d/dh log B_L(h)]_{h=1/2}
 = 3 -(2/3)log L +(1/6)log 2`.                                 (5.6)

Because `-v_L/6` is convex and the two explicit logarithmic prefactors in (5.5) are convex, `log B_L(h)` is convex. Therefore `h=1/2` is the **global** D/D' minimizer whenever

`L <= exp(9/2) 2^(1/4)=107.0490130147...`.                     (5.7)

Choose the concrete stress value `L=64`. Then the endpoint derivative is

`0.342935807853543...>0`,                                      (5.8)

so the global optimum over every supported physical weight and every proved D/D' exponent is exactly (4.6), namely

`G_D(64)=47746.475005920789...`.                               (5.9)

Applying the completed pinned e5 Theorem D to the actual target form gives

`boxed:
 ||p_{X^T A_64 X}||inf
 <=6sqrt(e)[2(1+sqrt(2))^2 64^2]^(-1/6)
 =1.642384882794337... .`                                      (5.10)

This is an actual inequality for every independent cap-one product input law.

## 6. Fresh designated partner r47 applied on the identical matrix

The same block has exact fourth volume

`E4(M_64)=det(M_64^T M_64)=(64^2+1)^2=16785409`.               (6.1)

Therefore fleet03/B04 r47 applies directly and gives

`boxed:
 ||p_{X^T A_64 X}||inf
 <=7.659094523616393... (16785409)^(-1/8)
 =0.957328390112904... .`                                      (6.2)

The partner theorem is genuinely a different mechanism: no carrier rebalance is required because fourth-compound currency downshifts to the marginal-free E3 receiver. On this same matrix the underlying direct marginal-free E3 theorem from the partner lineage is even sharper because

`E3(M_64)=33579012`,                                           (6.3)

and yields

`8.453021225528176... E3^(-1/6)=0.470616670745077...`.         (6.4)

The point of (6.2) is that the **fresh r47 completed result** is positively applied at its stated hypothesis, not merely cited.

## 7. Direct ridge gate on the same physical matrix

Let `g=gamma^2`, `D=L^2+1+g`. The ridge operator on the ten-row side has carrier diagonal

`k_c=L^2/D`                                                     (7.1)

and identical light-row diagonal

`k_l=(1/4)[1/D+1/(1+g)]`.                                      (7.2)

Its trace is

`theta=2(L^2+1)/D + 2/(1+g)`.                                  (7.3)

For `L>=1`, `k_c` is the maximal physical leverage. Since every ridge certificate requires `q>=2k_c`, the strict integrability gate `theta>2q` forces

`theta>4k_c`.                                                   (7.4)

A direct simplification gives

`theta-4k_c
 = 2[2-g(L^2-2)]/[D(1+g)]`,                                   (7.5)

so any admissible ridge scale must lie in the very narrow window

`boxed: g < 2/(L^2-2).`                                        (7.6)

At `L=64`, take the explicit valid choice

`g=64^(-4)=5.960464477539063e-8`,                              (7.7)

`q=2k_c=1.999511837901103...`.                                 (7.8)

Then

`theta=3.999999880761621...>2q`,                               (7.9)

so the completed determinant-retaining ridge theorem applies. Its exact first bound

`e/[sqrt(2q)gamma] * theta/(theta-2q) * D_gamma^(-1/(2theta))`  (7.10)

with

`D_gamma=det(I+M M^T/g)`                                       (7.11)

gives

`boxed: ||p_{X^T A_64 X}||inf <=696.177256048086... .`         (7.12)

No claim of global ridge optimality is made. Equation (7.6) is the useful comparison: the two heavy physical rows force any direct ridge certificate into an almost-critical `q≈2`, `theta≈4` window, whereas the volume law can rebalance the carriers and the higher-compound receiver avoids the leverage gate entirely.

Thus on one and the same physical matrix we have the certified hierarchy

`0.470617  direct marginal-free E3`
`< 0.957329  fresh partner r47 E4-downshift`
`< 1.642385  globally optimized pinned D/D' physical weights`
`<< 696.1773 displayed valid direct ridge certificate`.        (7.13)

## 8. Structural consequence and next unpaid implication

The new theorem sharpens the live carrier/deletion branch. One heavy carrier is paid when its anchored/deletion product is large; now two simultaneous heavy carriers are paid whenever

`sqrt(W_00 W_11)+sqrt(W_10 W_01)`                               (8.1)

is target-scale and the induced non-carrier marginals pass the cap. In the explicit family both natural carrier marginals are `0.999633938...`, yet exact entropy balancing costs only the aggregate geometric-face currency (4.6).

Moreover, partner r47 removes any configuration where a target-scale `E4` is already present on the same physical block. Therefore the genuinely unpaid collision regime is narrower:

`QFORM-MULTICARRIER-FACE-COLLAPSE-OR-OVERLAP-RECEIVER-v1`:

> From the surviving high-leverage/small-`s3` zero-anchor C1 residual, find a literal original-coordinate crossing for which either (i) one- or two-carrier E3 face products are target-scale and the exact entropy balance pays them, or (ii) `E4` is target-scale and r47 pays it, or else prove that simultaneous collapse of the complementary E3 faces and E4 forces a completed rank-two star, fixed-pair/hyperbolic, square-bank, grouped-hub, or overlap `C2/C3` receiver. The implication must aggregate before reciprocals, preserve original-coordinate product provenance, and never discard a nonzero rough quadratic tail as a small random perturbation.

This is strictly earlier than the density endpoint: the analytic E3/E4 receivers are paid; the remaining problem is the product-preserving structural routing from the bare three-large-eigenvalue hypothesis.

## 9. Deterministic audit

The committed checker verifies the exact Householder orthogonality and absence of zero physical cross coefficients, the face masses, `E3`, `E4`, the optimal category law and light marginals, the D' endpoint derivative, all displayed constants, and the ridge gate at `g=64^-4`. Marker:

`QFORM_B04_R18_TWO_CARRIER_BALANCE_CHECK_PASS`.

Full QFORM status remains **OPEN**. The bounded-density statements above are universal over the admissible input laws for the displayed matrix/family; continuity is only asserted where supplied by the invoked Fourier receiver and is not promoted to the unrestricted conjecture.
