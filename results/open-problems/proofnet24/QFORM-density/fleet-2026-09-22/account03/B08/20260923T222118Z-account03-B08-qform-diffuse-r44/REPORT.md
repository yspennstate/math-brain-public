SIGNED IN - working on the quadratic-form bounded-density conjecture (universal constant), account account03, slot B08, 2026-09-23T22:21:18Z.
attacking: the exact-Schur-match/zero-tail third-curvature endpoint by extracting a product-safe same-bank projected crossing, then forcing that crossing quantitatively for a diffuse rank-one residual without paying the near-singular hub pair.

# account03/B08 r44 — diffuse rank-one third curvature survives exact common-plane Schur match

Programme: `QFORM-DENSITY-3EIG-20260922`  
Run: `20260923T222118Z-account03-B08-qform-diffuse-r44`  
Assignment: diffuse eigenvector case  
Status: **NEW SUPPORTING THEOREMS / TARGET-VALID EXACT-MATCH FAMILY PAID / FULL QFORM OPEN**  
Execution: `WITHOUT_VERIFIED_BRAIN`  
Continuity: **proved on the new projected-crossing branches; global target continuity remains OPEN.**

The unrestricted conjecture is not proved or disproved here. All random coordinates below are ORIGINAL independent coordinates with one-dimensional probability densities bounded by one. No moment, support, connectedness, Gaussian, log-concavity, post-rotation independence, arbitrary-joint coarea, pointwise quadratic-phase decay, or one-good-minor assumption is used.

## 1. Fresh source boundary

The final prepublication owner refresh is

`yspennstate/math-research-brain@49901dcc9030ec296df489a19fd7be41e21c09a7`,

with OWNER CONTROL revision `2026-09-22.15`, QFORM as the sole research target, and the full theorem still OPEN. The live `CORRECTION_INBOX.json` at the same source was reread. In particular, this proof does not condition on rotated eigen-coordinates and does not infer a density bound from a bounded projection density alone.

The analytic engine actually used is the independently reviewed grouped projected-crossing theorem

`yspennstate/math-open-problems@829192412f2a2d84e72b4bed91115fc5fab68401`,
`proofnet24/QFORM-density/interactive/20260923T164118Z-full-proof-paper/NEW_PROJECTED_CROSSING.md`.

For `k=2`, `ell=1`, its formula `(GC)` says the following. Let two original hub variables couple through a rank-two arm `M_J` to a selected physical light set `J`; let

`S = s_1(M_J)s_2(M_J) = sqrt(det(M_J M_J^T))`.

Project the residual `I-J` crossing off `row(M_J)` and call the resulting matrix `C`. Put `F=||C||_F`. If `F>0` and every physical row satisfies

`||C_i||^2 <= F^2/2`,                                             (1.1)

then the full quadratic-affine form, with arbitrary hub self-curvature, arbitrary `I-I` and `J-J` curvature, every diagonal and every affine term retained, has

`||p_Q||_infinity <= C0 (S F)^(-1/3),`                           (1.2)

where

`C0 = 3*2^(5/6) = 5.345392308842036...`.                         (1.3)

Its characteristic-function majorant is integrable (`|t|^{-3/2}`), so this branch has a continuous density in `C_0(R)`.

Two completed neighbour results explain why the present endpoint is the right one to attack.

* `account01/B19`, `math-open-problems@80415fc95c0b84bf12c30711f83f22c04bb4900a`, proves a uniform receiver for every **nonzero** common-plane Schur mismatch, including rank-one degeneration. The exact zero-mismatch surface remains.
* `account02/B08`, `math-open-problems@fc3b9a4f04112672734f037b19358256b50c0a08`, constructs a target-valid exact-match stress family in that remaining surface: the hub pair may be arbitrarily ill-conditioned, both arm areas equal one, the post-pair cross block is exactly zero, and the missing third curvature is a diffuse same-bank square.

The designated partner result consumed below is

`account04/B08`, `math-open-problems@a5e66e2944c89857a41d5e18c283d53a4307be76`,
`proofnet24/QFORM-density/fleet-2026-09-22/account04/B08/20260923T212412Z-account04-B08-QFORM-r2/REPORT.md`.

## 2. First essential implication: common-plane curvature cancels under a physical projection

Partition ORIGINAL coordinates into two hubs `H={h_1,h_2}` and two disjoint light banks `J_1,J_2`. Write the hub arms as

`M_1 = A[H,J_1]`, `M_2 = A[H,J_2]`,

and suppose the light-light matrix has the exact common-plane representation

`A_LL = M^T R M + diag(S_1,S_2)`,                                (2.1)

where `M=[M_1 M_2]`, `R=R^T` is any `2 x 2` real matrix, and `S_1,S_2` are arbitrary symmetric same-bank matrices. In the r45 exact Schur-match endpoint one has `R=B^{-1}`, but no inverse of the hub block is used below.

Choose an actual physical subset `K subset J_1` such that

`M_K := M_1[:,K]`

has row rank two. Let

`I = (J_1\K) union J_2`

and let `P_K` be the orthogonal projection in `R^K` onto `row(M_K)`. Then

`A_LL[I,K]
 = [ M_1[:,J_1\K]^T R M_K + S_1[J_1\K,K] ;
     M_2^T R M_K ].`                                             (2.2)

Every row of both common-plane terms belongs to `row(M_K)`. Therefore

`boxed:
 A_LL[I,K](I-P_K)
 = [ S_1[J_1\K,K](I-P_K) ; 0 ].`                                (2.3)

This is the crucial exact cancellation. It does not complete or invert the hub pair, and it does not rotate any random coordinate.

Define the two currencies

`A_K := sqrt(det(M_K M_K^T)),`                                   (2.4)

`F_K := ||S_1[J_1\K,K](I-P_K)||_F.`                             (2.5)

For each physical row `i in J_1\K`, put

`alpha_i := ||(S_1[J_1\K,K](I-P_K))_{i,*}||^2 / F_K^2`          (2.6)

when `F_K>0`.

### Theorem 2.1 — `QFORM-COMMONPLANE-SAMEBANK-PROJECTED-RECEIVER-v1`

Under (2.1), if for some physical `K`

`A_K>0`, `F_K>0`, and `max_i alpha_i <=1/2`,                     (2.7)

then for every independent cap-one product input

`boxed:
 ||p_Q||_infinity
 <= 3*2^(5/6) (A_K F_K)^(-1/3).`                                (2.8)

Moreover `p_Q` is continuous and vanishes at infinity.

#### Proof

Apply the reviewed grouped projected-crossing theorem with the two literal coordinates in `H` as the two hubs, selected light set `J=K`, and `I` as above. The two hub coordinates have joint density at most one. Equation (2.3) identifies the theorem's projected crossing exactly, so its first-volume is

`Z_1=F_K^2`.

Its arm singular-product is `A_K`. The `ell=1` marginal condition is precisely (2.7). Formula `(GC)` with `k=2`, `ell=1`, `d=3`, `M_H<=1` gives (2.8). The corresponding characteristic-function estimate is integrable, hence Fourier inversion gives a continuous `C_0` density. QED.

### Localized/aligned meaning of failure

The theorem makes the failure certificates physical and quantitative.

* If a row marginal exceeds `1/2`, then an actual coordinate `i in J_1\K` satisfies

  `||C_{i,*}|| > F_K/sqrt(2)`,                                   (2.9)

  a localized third-curvature witness.
* If `F_K` is small relative to the raw crossing `S_1[J_1\K,K]`, that raw crossing lies close in Frobenius norm to the two-dimensional carrier `row(M_K)`: it is an aligned certificate, not an unexplained Fourier failure.
* If `A_K` is small, the selected physical hub arm has lost two-dimensional area.

Thus (2.8) complements rather than duplicates localized-coordinate conditioning.

## 3. Rank-one third curvature: a random physical cut forces the currencies simultaneously

The first essential missing structural implication can be proved completely when the same-bank residual is rank one and its eigenvector is diffuse and genuinely transverse to the hub arm.

Assume

`S_1 = lambda q q^T`, `||q||_2=1`, `lambda !=0`,                 (3.1)

and let `M=M_1` have row rank two. Define

`S_M := sqrt(det(MM^T)) = s_1(M)s_2(M)>0`,                       (3.2)

`mu := max_j q_j^2`,                                             (3.3)

`tau := ||(I-P_M)q||_2`,                                        (3.4)

where `P_M` projects onto `row(M)` in the full bank. Assume `tau>0`.

Let

`W = [ M ; q^T ]`, a `3 x |J_1|` matrix.                          (3.5)

By the Gram Schur-complement identity,

`det(WW^T) = det(MM^T) tau^2 = S_M^2 tau^2.`                    (3.6)

Choose a random physical subset `K` by retaining each coordinate independently with probability

`p=3/4`.                                                         (3.7)

Write

`D_K=det(W_K W_K^T)`, `r_K=||q_{K^c}||_2^2`.                    (3.8)

Cauchy-Binet and independence of the Bernoulli cut give the exact expectation

`E[D_K r_K]
 = p^3(1-p) sum_{|T|=3} det(W_T)^2
     (1-sum_{j in T}q_j^2).`                                    (3.9)

Indeed, after expanding `D_K`, a term indexed by a triple `T` and an outside coordinate `j` survives exactly when `T subset K` and `j notin K`, an event of probability `p^3(1-p)`.

Since every triple carries at most `3mu` of the `q` mass,

`E[D_K r_K]
 >= c (1-3mu) det(WW^T),`                                       (3.10)

with the optimal Bernoulli constant

`c=p^3(1-p)=27/256.`                                             (3.11)

Hence some physical cut `K` satisfies

`D_K r_K >= c(1-3mu) S_M^2 tau^2.`                              (3.12)

The right side is positive. Therefore `W_K` has rank three, in particular `M_K` has rank two. Also

`W_KW_K^T <= WW^T`

in Loewner order, so determinant monotonicity gives `D_K<=det(WW^T)`. Combining with (3.12),

`r_K >= c(1-3mu).`                                               (3.13)

For this cut, the Gram Schur complement inside `K` yields

`D_K
 = det(M_KM_K^T) ||(I-P_K)q_K||_2^2
 = A_K^2 ||(I-P_K)q_K||_2^2.`                                   (3.14)

On the other hand (3.1) gives exactly

`F_K
 = |lambda| ||q_{K^c}||_2 ||(I-P_K)q_K||_2.`                    (3.15)

Consequently

`(A_KF_K)^2
 = lambda^2 D_K r_K
 >= lambda^2 c(1-3mu) S_M^2 tau^2`,                             (3.16)

or

`boxed:
 A_KF_K
 >= |lambda| S_M tau sqrt(c(1-3mu)).`                           (3.17)

Finally the projected rank-one crossing has row marginal

`alpha_i=q_i^2/r_K` for `i in K^c`.                              (3.18)

Thus (3.13) implies `alpha_i<=1/2` provided

`2mu <= c(1-3mu)`,                                               (3.19)

namely

`boxed: mu <= c/(2+3c)=27/593=0.0455311973... .}`                (3.20)

We have therefore proved:

### Theorem 3.1 — `QFORM-DIFFUSE-RANK1-THIRDCURVATURE-v1`

In the common-plane form (2.1), suppose one same-bank residual is `lambda q q^T` and the corresponding two-row hub arm `M` has area `S_M>0`. If

`mu=max_j q_j^2 <=27/593`,                                       (3.21)

and

`tau=dist(q,row(M))>0`,                                         (3.22)

then the full output has a continuous `C_0` density and

`boxed:
 ||p_Q||_infinity
 <= 2^(13/6) sqrt(3)
    (|lambda| S_M tau)^(-1/3)
    (1-3mu)^(-1/6).`                                             (3.23)

Numerically the leading constant before the last factor is

`2^(13/6)sqrt(3)=7.77664518895866... .`                          (3.24)

#### Proof

Use the cut furnished by (3.12). Equations (3.17)-(3.20) verify all hypotheses of Theorem 2.1. Since

`3*2^(5/6)c^(-1/6)=2^(13/6)sqrt(3)`,                            (3.25)

(2.8) becomes (3.23). QED.

This theorem is the desired diffuse/localized complement: if `mu` is not small there is a localized physical coordinate; if `tau` is small, the third eigenvector is aligned with the two-dimensional hub arm; otherwise the whole diffuse branch is paid without any hub inverse and without any moment assumption.

## 4. Actual inequality in the live r45 exact-match descendant

The inherited r45 common-plane state has, on each arm,

`S_M = s_1(M)s_2(M)
 > s_* L^2`,

where

`s_* = 1/(64 sqrt(896)) = 0.0005219946131102039... .`            (4.1)

Consider its exact pair-Schur-match/zero-crossing subbranch in which the retained third Schur curvature on one bank is rank one,

`S_1=lambda q q^T`,                                              (4.2)

with `|lambda|>=L`. (In the exact rank-one Schur-residual case the completed Schur spectral-retention theorem supplies this scale, after swapping the two banks if necessary.)

If

`max_j q_j^2 <=1/48`,                                            (4.3)

and

`dist(q,row(M))>=1/2`,                                           (4.4)

then Theorem 3.1 gives the fully numerical target-scale estimate

`boxed: ||p_Q||_infinity <123.01/L,`                             (4.5)

and `p_Q in C_0(R)`.

The calculation is

`2^(13/6)sqrt(3)
 * s_*^(-1/3)
 * (1/2)^(-1/3)
 * (1-3/48)^(-1/6)
 =123.003762689... .`                                            (4.6)

Thus an arbitrarily ill-conditioned physical hub pair is harmless on this genuinely diffuse/transverse rank-one third-curvature branch. The surviving rank-one states have a concrete certificate: either a coordinate carries more than `1/48` of the third eigenvector, or that eigenvector lies within distance `1/2` of the hub-arm row plane.

## 5. The account02/B08 exact-match stress family is paid uniformly

Now apply the mechanism to the explicit target-valid family from

`account02/B08@fc3b9a4f04112672734f037b19358256b50c0a08`.

Let `m=2^d`, choose three distinct normalized Sylvester characters `r_a,r_b,q in R^m`, put

`M=[r_a^T;r_b^T]`, `MM^T=I_2`, `Mq=0`,                          (5.1)

choose

`B=diag(epsilon,-epsilon)`,                                      (5.2)

and define the two-bank matrix exactly as in that source. Its nonzero spectrum is

`{Lambda,-Lambda,1}`, `Lambda=epsilon+2/epsilon`,                (5.3)

its pair-Schur crossing is exactly zero, its two arm areas are one, and its remaining Schur curvature is

`diag(q q^T,0)`.                                                 (5.4)

For `epsilon<1/64` and sufficiently large `m`, the source shows every physical `2 x 2` principal block lies below the `L/64` pair gate; this is therefore a real near-singular exact-match stress state, not an algebraic toy.

For `m>=8`, choose a nonzero Sylvester character `chi_h` whose index is distinct from the three pairwise differences among the indices of `r_a,r_b,q`, and take the physical half-set

`K={x: chi_h(x)=1}`.                                             (5.5)

Character orthogonality on this half-set gives exactly

`M_KM_K^T=(1/2)I_2`,                                             (5.6)

`q_K perpendicular row(M_K)`,                                   (5.7)

`||q_K||^2=||q_{K^c}||^2=1/2`.                                  (5.8)

Hence

`A_K=1/2`, `F_K=1/2`,                                           (5.9)

and every projected row marginal is

`alpha_i=2/m <=1/4`.                                             (5.10)

Theorem 2.1 therefore gives, for **every** `epsilon>0`, every admissible independent cap-one product law, and every `m=2^d>=8`,

`boxed:
 ||p_Q||_infinity <= 6 sqrt(2) <8.486,`                          (5.11)

with `p_Q in C_0(R)`.

After multiplying the whole matrix by a target scale `L`,

`boxed: ||p_Q||_infinity <= 6 sqrt(2)/L.`                        (5.12)

This is stronger for this family than paying the near-singular hub pair: the constant does not depend on `epsilon` at all. It directly answers the stress mechanism identified by account02/B08.

## 6. A useful arbitrary-residual router

The preceding random-cut theorem was rank one only, but the analytic receiver Theorem 2.1 is not. A simple deterministic observation records what remains for an arbitrary same-bank `S_1`.

Suppose

`||S_1||_op >= L`,                                               (6.1)

and

`max_i |(S_1)_{ii}| <= delta L`, `0<=delta<1`.                   (6.2)

Let `D=diag(S_1)` and `O=S_1-D`. Then

`||O||_F >= ||O||_op >= (1-delta)L`.                             (6.3)

For a Bernoulli half-cut `K`,

`E ||S_1[K^c,K]||_F^2
 = (1/4)||O||_F^2`.                                              (6.4)

Thus some physical cut satisfies

`boxed:
 ||S_1[K^c,K]||_F >= (1-delta)L/2.`                              (6.5)

Separately, Cauchy-Binet for the two-row arm gives

`E det(M_KM_K^T)=(1/4)det(MM^T)`.                               (6.6)

The unresolved issue is **simultaneous** selection after projection: one still has to force a cut carrying both macroscopic arm area and a macroscopic component of (6.5) transverse to `row(M_K)`. If the transverse component is macroscopic and row-diffuse, Theorem 2.1 pays it; if a row marginal is heavy, one obtains an actual localized coordinate; if the transverse component is small, (6.5) is quantitatively aligned into a two-dimensional physical arm carrier. This is a substantially sharper endpoint than “arbitrary third curvature remains.”

## 7. Required designated-partner application

The newest completed designated partner `account04/B08` theorem is `QFORM-PHYSICAL-DELETION-CHILD-WINDOW-v1` at

`math-open-problems@a5e66e2944c89857a41d5e18c283d53a4307be76`.

Apply it to the same current ambient matrix after deleting one ORIGINAL coordinate. If the physical child matrix `C_h` has at least three eigenvalues of modulus at least

`m=L/64`,                                                        (7.1)

and its high-window projection obeys

`max_j (P_{C_h}(m/64))_{jj}
 =max_j(P_{C_h}(L/4096))_{jj} <=1/32`,                           (7.2)

then the partner theorem gives the actual inequality

`boxed:
 ||p_Q||_infinity
 <64/m
 =4096/L,`                                                       (7.3)

and the output density is continuous `C_0`.

Thus a diffuse three-child spectral window is independently paid. Failure of this partner branch supplies either a child with fewer than three `L/64` modes or an actual coordinate with child high-window leverage `>1/32`. This is complementary to Theorems 2.1 and 3.1, which spend transverse same-bank crossing volume rather than a three-child spectral window.

For reference, the older account04/B08 anisotropic direct-sum theorem remains valid at

`math-open-problems@abbec61f52e1f4b4d367fd67e73e4d2501ac9c74`,

with `<7.251/L`; it is not generalized beyond its proved scope here.

## 8. Deterministic checks

`CHECKS.py` and `CHECKS.txt` are in this run directory. They verify:

1. the exact constant identities
   `c=27/256`, `mu_gate=27/593`, and
   `3*2^(5/6)c^(-1/6)=2^(13/6)sqrt(3)`;
2. 500 seeded common-plane matrices satisfy the projection identity (2.3), with maximum floating error
   `1.8610113450279187e-14`;
3. 30 small random frames, enumerating every Bernoulli cut, satisfy the exact expectation identity (3.9), with maximum floating error
   `1.5543122344752192e-15`;
4. the Sylvester cuts for `m=8,16,32` give `A_K=F_K=1/2` and row marginals `2/m`.

The checker terminates `QFORM_B08_R44_CHECK_PASS`. These are regression checks only; Sections 2-7 are analytic proofs.

## 9. What is and is not solved

### Proved in this run

* `QFORM-COMMONPLANE-SAMEBANK-PROJECTED-RECEIVER-v1`: exact product-safe cancellation of arbitrary common-plane curvature under the physical projected-crossing receiver, yielding (2.8) with continuity.
* `QFORM-DIFFUSE-RANK1-THIRDCURVATURE-v1`: a random physical cut forces simultaneous arm area and transverse rank-one residual currency for every `mu<=27/593`, yielding (3.23) with continuity.
* Actual inherited-r45 inequality `<123.01/L` in the rank-one residual branch `mu<=1/48`, `tau>=1/2`.
* The exact-match Hadamard stress family is paid uniformly by `6sqrt(2)/L`, independent of its arbitrarily ill-conditioned hub pair.
* The newest account04/B08 child-window theorem is applied at the actual branch inequality `<4096/L`.

### Not proved

The unrestricted QFORM conjecture remains **OPEN**. The new theorem does not show that a general exact-match Schur residual contains a rank-one self block, nor does it force simultaneous arm area and transverse projected volume for an arbitrary high-rank self block. It also does not pay the rank-one branch when the third vector is strongly aligned with the two-row hub arm, and it does not by itself handle every singular hub geometry.

The next precise B08 implication is

`QFORM-EXACTMATCH-HIGHRANK-SIMULTANEOUS-CUT-OR-ALIGNMENT-COMPILER-v1`:

> In the exact common-plane Schur-match/zero-tail state, use the third spectral scale to force either (i) one physical cut with macroscopic two-arm area and diffuse transverse projected same-bank crossing, paid by Theorem 2.1; (ii) an actual localized row/eigenvector witness; or (iii) a quantitatively aligned low-dimensional carrier that an existing grouped-hub theorem can consume, without discarding any small nonzero curvature.

Global continuity remains OPEN, although every new branch proved here has a continuous `C_0` density.
