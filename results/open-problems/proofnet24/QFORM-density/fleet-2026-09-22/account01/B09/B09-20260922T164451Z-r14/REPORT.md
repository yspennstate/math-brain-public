# account01/B09 — grouped rank-two Schur smoothing after a physical square pivot

Run `B09-20260922T164451Z-r14`  
Programme `QFORM-DENSITY-3EIG-20260922`; final owner control observed before publication: revision `2026-09-22.8`  
Assignment: `Bilinear block mechanism`  
Outcome: **ESSENTIAL_STEP_APPLIED / FULL_TARGET_OPEN**  
Execution context: `WITHOUT_VERIFIED_BRAIN`

## 1. Target and fresh correction

The full target remains OPEN: for independent real coordinates with probability densities at most one and every real symmetric `A` with at least three eigenvalues of modulus at least one, prove one dimension-independent finite `C` such that

`P{X^T A X in I} <= C |I|`

for every interval `I`, or produce a target-valid counterexample. Continuity is tracked separately.

Fresh revision `2026-09-22.8` proposed a conditional three-dimensional spectral-projection cap as an open completion step. I do **not** use it: account03/B10 has now refuted that intermediate statement in `QFORM-CONDITIONAL-3D-PROJECTION-CAP-FALSE-v1` (`math-open-problems@947a09fdafd7ee8f60562076674ff20689632e21`). For iid uniforms, a conditional projected density blows up at the edge. This does not refute QFORM or rank-three coarea; it means product aggregation must occur before taking that conditional `L^infinity` supremum.

The mechanism below instead keeps disjoint original-coordinate banks and pays an exact grouped rank-two Schur quotient before any reciprocal tiny physical minor.

## 2. Source-pinned inputs actually used

### Assigned partner account02/B09

Latest complete partner report:

- repository/commit: `yspennstate/math-open-problems@77d71ed8bbd7f8a3fd40958e54b5bf658163c27a`;
- path: `proofnet24/QFORM-density/fleet-2026-09-22/account02/B09/20260922T160923Z-account02-B09-QFORM-r4/REPORT.md`;
- theorem: `QFORM-PIVOT-OFFDIAG-STABLERANK-v1`.

For a genuine physical pivot `a=A_kk!=0`, with scalar Schur complement `S`, `s=||S||_op`, and `S^o=S-diag(S)`, if

`||S^o||_F^2 >= 24 s^2`,

then

`||p_Q||_infinity <= 11.876 / sqrt(|a| s)`.                         (2.1)

The same report applies the completed spectral-window/heavy-coordinate reduction: either `||p_Q||_infinity<35.27`, or some physical coordinate has `max(|a|,||b||_2)>=1/312`. If the latter coordinate is diagonal-dominant, `|a|>=||b||_2`, then `|a|>=1/312` and `s>=c_S:=2/(3+sqrt(5))`; hence (2.1) gives `<340` whenever the stable-rank hypothesis fires.

I use (2.1) below as the high-stable-rank half of the B09 conditional proof, rather than merely citing it.

The same partner report supplies the source-valid correction `QFORM-ONE-HEAVY-ROW-SAME-SQUARE-ABSORPTION-FALSE-v1`: `U^2+X^2+2UX=(U+X)^2` for independent unit-density uniforms has an unbounded square-root density. Thus one heavy row plus the **same** square is insufficient with arbitrary same-bank curvature. The new theorem below explicitly requires a second nondegenerate grouped curvature, or in the sharper hyperbolic corollary two genuinely independent residual banks.

### New account03/B01 half-Riesz input

I also apply the newly completed `QFORM-RANK2-TRANSLATION-HALFRIESZ-v1`:

- `yspennstate/math-open-problems@76fd4f9ccae2e422498fec6d4156bfd64775c8e4`;
- `proofnet24/QFORM-density/fleet-2026-09-22/account03/B01/account03-B01-20260922T163129Z-r15/REPORT.md`.

For an exact rank-two real quadratic form `R=Z^T H Z` in independent cap-one physical coordinates, with nonzero eigenvalue product `Delta`, it proves the translation-uniform estimate

`sup_t E |R-t|^(-1/2) <= C_* Delta^(-1/4)`.                    (2.2)

Using the Livshyts--Paouris--Pivovarov one-dimensional projection bound `sqrt(2)` in the heavy-row part of that proof, one may take `C_*=32` (the diffuse constant in the same proof is smaller). I only need universality; the numerical value is recorded to make the resulting endpoint explicit.

## 3. A sharp product half-Riesz lemma

### Lemma 3.1 — `QFORM-PRODUCT-HALFRIESZ-v1`

Let `U,V` be independent real random variables with probability densities bounded by `M,N`, respectively. Then for every `c!=0` and every `t`,

`boxed: E |t-cUV|^(-1/2) <= 8 sqrt(MN) / sqrt(|c|).`          (3.1)

The constant `8` is attained at `t=0`, `M=N=1` by centered unit-length uniforms.

**Proof.** For every probability density `g<=N` and every `z`, decreasing rearrangement gives

`int |v-z|^(-1/2) g(v) dv <= 2 sqrt(2N)`.                     (3.2)

Indeed the maximizer is density `N` on the interval of length `1/N` centered at `z`, and its integral is exactly `2 sqrt(2N)`. Conditioning on `U=u` gives, for `u!=0`,

`E[|t-cuV|^(-1/2)|U=u] <= 2 sqrt(2N) |cu|^(-1/2)`.          (3.3)

Since `U` is absolutely continuous, `P(U=0)=0`, and another application of (3.2) at zero gives

`E|U|^(-1/2) <= 2 sqrt(2M)`.                                 (3.4)

Multiplying (3.3)-(3.4) proves (3.1). For `U,V` uniform on `[-1/2,1/2]`, `E|UV|^(-1/2)=(2sqrt(2))^2=8`. QED.

This is the exact integrability threshold missing from the partner's same-square counterexample: one product factor gives a logarithmic density singularity, but its **half-Riesz potential** is uniformly finite once both factors come from independent physical banks.

## 4. Three-bank square-hyperbolic smoothing

### Theorem 4.1 — `QFORM-THREEBANK-SQUARE-HYPERBOLIC-v1`

Let `X` be a real random variable with density at most one. Let `F,G,W` be mutually independent sigma-fields, also independent of `X`. Let `U=U(F)`, `V=V(G)` have densities bounded by `M,N`. Let `m=m(F,G,W)` and `H=H(W)` be arbitrary measurable functions. For nonzero `a,c`, put

`T = a (X+m)^2 + c U V + H`.                                  (4.1)

Then `T` has an essentially bounded density and

`boxed: ||p_T||_infinity <= 8 sqrt(MN) / sqrt(|ac|).`         (4.2)

Consequently `P(T in I)` is at most the right side of (4.2) times `|I|` for every interval `I`.

**Proof.** Condition on `F,G,W`. Translation of the cap-one density of `X` does not change its cap. The pushforward under `x -> a(x+m)^2` has density bounded pointwise by

`|a|^(-1/2) |y|^(-1/2)`                                      (4.3)

on the appropriate half-line. Hence for almost every `t`,

`p_T(t) <= |a|^(-1/2) E |t-cUV-H|^(-1/2)`.                  (4.4)

Condition on `W`; `H` is then a scalar translation, while `U,V` remain independent with the same density caps. Lemma 3.1, uniformly in that translation, turns (4.4) into (4.2). QED.

No compact support, moments, log-concavity, sign restriction, or post-rotation independence is used. The square center may depend arbitrarily on **all three residual banks**. This is precisely why physical square completion can coexist with arbitrary pivot couplings.

Continuity is **not** claimed from this argument; it proves an essentially bounded density and a direct `O(|I|)` small-ball estimate.

## 5. Main grouped-coordinate theorem with arbitrary extra Schur spectrum

The preceding hyperbolic theorem is sharpest when the grouped residual is purely off-diagonal. A more flexible endpoint follows by applying the new account03/B01 rank-two half-Riesz theorem to a grouped quotient.

### Theorem 5.1 — `QFORM-PIVOT-GROUPED-RANK2-HALFRIESZ-v1`

Fix an original physical coordinate `k` with `a=A_kk!=0`, and let

`S=A_{-k,-k}-A_{-k,k}A_{k,-k}/a`                              (5.1)

be its scalar Schur complement. Suppose the residual coordinates admit a disjoint physical partition `P | T | W` and nonzero vectors `u in R^P`, `v in R^T` such that, for some real numbers `alpha,beta,gamma`, vectors `r,s` on `W`, and arbitrary symmetric `S_W`,

`S_PP = alpha u u^T`,
`S_TT = gamma v v^T`,
`S_PT = beta u v^T`,
`S_PW = u r^T`,
`S_TW = v s^T`,
`S_WW = S_W`.                                                   (5.2)

Let

`H_2=[[alpha,beta],[beta,gamma]]`

and assume `det H_2 !=0`. Define the invariant grouped rank-two curvature

`Delta_grp := |det H_2| ||u||_2^2 ||v||_2^2`.                  (5.3)

Then every allowed product input law satisfies

`boxed: ||p_Q||_infinity <= sqrt(2) C_* |a|^(-1/2) Delta_grp^(-1/4).` (5.4)

With `C_*=32`, the explicit constant is `32sqrt(2)`.

**Proof.** Complete the genuine physical square:

`Q=a(X_k+a^(-1)b^T Y)^2+Y^T S Y`.                             (5.5)

Write `U=u^T Y_P`, `V=v^T Y_T`. Conditional on `Y_W`, (5.2) makes the Schur residual

`[U,V] H_2 [U,V]^T + 2 U r^T Y_W + 2 V s^T Y_W + Y_W^T S_W Y_W`. (5.6)

Because `H_2` is invertible, the two linear terms in (5.6) are removed by a translation of `(U,V)` depending on `Y_W`, plus a scalar translation. The physical banks `P,T,W` are disjoint, so before that translation `U,V` are independent. The one-dimensional product-projection theorem gives

`||p_U||_infinity <= sqrt(2)/||u||_2`,
`||p_V||_infinity <= sqrt(2)/||v||_2`.                         (5.7)

Put `M=sqrt(2)/||u||`, `N=sqrt(2)/||v||` and rescale `U'=MU`, `V'=NV`; their densities are at most one and remain independent. The quadratic matrix in `(U',V')` is

`diag(M^(-1),N^(-1)) H_2 diag(M^(-1),N^(-1))`,

whose determinant magnitude is `|det H_2|/(M^2N^2)`. Apply the source-pinned account03/B01 theorem (2.2), uniformly over the `Y_W`-dependent translation, to get

`sup_t E[|Y^TSY-t|^(-1/2) | Y_W]
 <= C_* (MN)^(1/2) |det H_2|^(-1/4)
 <= sqrt(2) C_* Delta_grp^(-1/4)`.                              (5.8)

Finally the cap-one physical-square pushforward in (5.5) gives

`p_Q(t) <= |a|^(-1/2) E|Y^TSY-t|^(-1/2)`,                    (5.9)

so (5.4) follows after averaging `Y_W`. QED.

**Why this is not merely the rank-three theorem again.** `S_W` is completely arbitrary and may contain arbitrarily many additional eigenvalues of either sign. Moreover the completed-square center in (5.5) may depend on `W`, so this is not an independent convolution with a rank-three form. The theorem pays a rank-two grouped quotient while retaining arbitrary extra Schur spectrum in a separate physical bank.

## 6. Sharper isolated hyperbolic corollary

Suppose in Theorem 5.1

`S_PP=0`, `S_TT=0`, `S_PW=S_TW=0`,

and `S_PT` has rank one with its unique nonzero singular value `sigma>0`; `S_WW` remains arbitrary. Choosing unit singular vectors gives

`Y^T S Y = 2 sigma U V + Y_W^T S_WW Y_W`,

with independent `U,V` whose densities are each at most `sqrt(2)`. Theorem 4.1 therefore yields the much sharper endpoint

`boxed: ||p_Q||_infinity <= 8 / sqrt(|a| sigma).`              (6.1)

This is a genuine **low-stable-rank** companion to the assigned partner's high-stable-rank theorem. In the pure rank-one bipartite Schur case, `||S^o||_F^2/||S||_op^2=2`, far below the partner threshold `24`; (6.1) covers exactly a branch that (2.1) cannot see.

The partner's same-square counterexample is not contradicted: there `det H_2=0` after the attempted grouping, equivalently the second independent grouped curvature is absent.

## 7. Mandatory stress family: singleton plus two banks

For

`A_m=[1] direct_sum J_m/m direct_sum (-J_m/m)`,

whose nonzero spectrum is `{1,1,-1}`, pivot the singleton coordinate. The Schur complement is

`S=J_m/m direct_sum (-J_m/m)`.

Take the positive and negative banks as `P,T`, with unit vectors `u=v=m^(-1/2)(1,...,1)`, `H_2=diag(1,-1)`, and `W` empty. Then

`Delta_grp=1`.                                                   (7.1)

Theorem 5.1 gives the dimension-free bound

`||p_Q||_infinity <= sqrt(2) C_* <= 32sqrt(2)`.                (7.2)

This family is a mandatory correction control because every fixed local principal block or one physical rank-two packet deteriorates with `m`. The grouped theorem pays it **before** any reciprocal local minor is selected.

Earlier B09 aggregation gives a better numerical constant on this exact family; (7.2) is valuable because it exhibits the low-dimensional grouped quotient mechanism that survives arbitrary bank size and extends to arbitrary independent `S_W` as in Theorem 5.1.

## 8. Exact-rank-three zero-diagonal Schur diagnostic

This subsection is a mechanism check, not a claim of new scope: the new account03/B01 theorem already pays all exact-rank-three nonzero-pivot residual orientations.

If `rank A=3`, `a=A_kk!=0`, and the rank-two Schur complement `S` has zero physical diagonal, then its nonzero eigenvalues are `lambda,-lambda`. Write

`S=lambda(uu^T-vv^T)`

with orthonormal `u,v`. `diag S=0` implies `u_i^2=v_i^2`. Thus, after writing `v_i=epsilon_i u_i`, `epsilon_i in {+1,-1}` on the support, orthogonality implies

`sum_{epsilon_i=+1}u_i^2=sum_{epsilon_i=-1}u_i^2=1/2`.          (8.1)

The same-sign blocks of `S` vanish, while the opposite-sign block is

`S_PT=2lambda u_P u_T^T`,

whose unique nonzero singular value is `|lambda|`. Hence (6.1) gives

`||p_Q||_infinity <= 8/sqrt(|a lambda|)`.                     (8.2)

For `A=R Lambda_3 R^T`, let `ell_k=||R_{k,*}||^2`. Schur/Cauchy--Binet gives exactly

`lambda^2 = |det Lambda_3| ell_k / |a|`.                       (8.3)

Therefore

`||p_Q||_infinity <= 8 (|a| |det Lambda_3| ell_k)^(-1/4)`.    (8.4)

Under the exact target spectral condition `|lambda_j(Lambda_3)|>=1`, `|det Lambda_3| ell_k >= |a|`, so if `|a|>=1/312`, (8.4) yields

`||p_Q||_infinity <= 8 sqrt(312) <141.31`.                    (8.5)

This confirms quantitatively that the grouped hyperbolic endpoint handles a canonical low-stable-rank/null-diagonal branch and respects all signs and repeated spectra.

## 9. An elementary definite physical-pair gate

For later routing, one simple gate is worth recording. If an original physical pair `I={i,j}` has a positive- or negative-definite `2x2` principal block `H=A[I,I]`, then, conditioning on all other coordinates and completing the two-dimensional square,

`boxed: ||p_Q||_infinity <= pi / sqrt(|det H|).`               (9.1)

Indeed the conditional input density on the selected pair is at most one and the Lebesgue area of a quadratic annulus of width `h` is at most `pi h/sqrt(|det H|)`. This remains valid with arbitrary outside couplings and spectrum.

At a scalar pivot, `det H=a S_jj`. Hence a same-sign Schur diagonal produces

`||p_Q||_infinity <= pi / sqrt(|a S_jj|)`.                    (9.2)

This is only a routing gate, not a full reduction.

## 10. Conditional end-to-end argument and remaining implication

The B09 proof skeleton after this run is:

1. Use the completed spectral-window theorem: either `||p_Q||_infinity<35.27`, or obtain a physical heavy coordinate with `max(|a|,||b||)>=1/312`.
2. If a chosen heavy coordinate is diagonal-dominant and its Schur complement satisfies `||S^o||_F^2>=24||S||_op^2`, apply the **assigned partner** theorem (2.1). Since `|a|>=1/312` and `||S||_op>=2/(3+sqrt(5))`, this gives

   `||p_Q||_infinity <339.42<340`.                              (10.1)

3. On low-stable-rank residuals, do not select one tiny minor. If a nondegenerate grouped rank-two quotient of the form (5.2) exists at scale `Delta_grp`, Theorem 5.1 gives the direct `O(|I|)` bound while retaining arbitrary extra `S_W` spectrum. In the isolated hyperbolic rank-one-cross case, (6.1) is sharper.
4. The singleton-plus-two-banks obstruction is paid by step 3 with `Delta_grp=1` for every bank size.
5. A same-sign scalar Schur diagonal can instead fire the elementary definite-pair gate (9.2).

The first unpaid implication is now

> **`QFORM-LOWSTABLERANK-GROUPED-EXTRACTION-v1` (OPEN).** Starting from a matrix left by steps 1--2, prove that a low-off-diagonal-stable-rank Schur complement either contains a quantitatively nondegenerate product-preserving grouped rank-two quotient of the form (5.2), fires an existing definite/ridge/diffuse gate, or reduces to a separately controlled near-null physical-pivot configuration. The extraction must retain arbitrary additional spectrum and must not condition on a complementary spectral coordinate and demand a uniform conditional projection cap, which is now refuted.

The genuinely off-diagonal-heavy / zero-near-zero pivot case remains part of this residual. The full QFORM conjecture is therefore **not solved** by this report.

## 11. Continuity and integrity status

Theorems 4.1, 5.1, 6.1 and 9.1 prove existence of an essentially bounded density through linear interval estimates / square disintegration. They do **not** establish a continuous representative. No pointwise law-uniform Fresnel decay, post-rotation independence, conditional projection cap, bounded support, moment, Gaussian, log-concavity, or connected-support assumption is used.

The numerical checker stored beside this report only verifies algebraic constants and the zero-diagonal rank-two classification on finite examples; it is diagnostic, not proof.
