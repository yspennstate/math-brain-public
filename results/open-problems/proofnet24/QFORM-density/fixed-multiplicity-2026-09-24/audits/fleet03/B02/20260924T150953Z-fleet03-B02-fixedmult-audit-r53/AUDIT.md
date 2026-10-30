SIGNED IN - working on the quadratic-form bounded-density conjecture (universal constant), account fleet03, slot B02, 2026-09-24T15:09:53Z.
attacking: independent audit of the new nine-eigenvalue grouped-Fourier proof, the fresh two-anchor L2 relay, and the first unresolved multiplicity-eight implication.

# fleet03/B02 r53 audit

Objective: `QFORM-FIXED-MULTIPLICITY-AUDIT-20260924` (fresh control supersedes the older per-slot-only Fourier brief while preserving the full three-eigenvalue target).

Pinned baseline manuscript: `yspennstate/math-open-problems@7c0d6e60946b19423e6400a12d34b473cf0591e2`, path `proofnet24/QFORM-density/fixed-multiplicity-2026-09-24/manuscript.tex`, blob `183ccd294763214e6a707e8d4749ff9a8cf7006d`.

New dependencies checked in this run:

- fleet03/B04 threshold-nine grouped-Fourier candidate, `proofnet24/QFORM-density/fixed-multiplicity-2026-09-24/improvements/fleet03/B04/20260924T121940Z-fleet03-B04-fixedmult-audit-r1/REPORT.md`, blob `054facef834d29927713c5d42a1f09a541c5644b`;
- fleet01/B02 independent threshold-nine reconstruction, `proofnet24/QFORM-density/fixed-multiplicity-2026-09-24/improvements/fleet01/B02/20260924T142019Z-fleet01-B02-fixedmult-audit-r13/IMPROVEMENT.md`, blob `fc3761b698b94a0332492b4ca5bf767c1ae9ddf3`;
- fleet03/B16 two-anchor joint-L2 relay, `proofnet24/QFORM-density/fixed-multiplicity-2026-09-24/improvements/fleet03/B16/20260924T145240Z-fleet03-B16-FIXEDMULT-r48/TWOANCHOR_L2_RELAY.md`, blob `d13baa0b2fefc6cd9ea50cb38b156dc81c87f87d`;
- fleet03/B15 exterior spectral inheritance, `proofnet24/QFORM-density/fixed-multiplicity-2026-09-24/improvements/fleet03/B15/20260924T145303Z-fleet03-B15-fixedmult-r15/REPORT.md`, blob `0ba9e3c5d8f38783dee9bc0658390f025f06dd37`;
- designated historical fleet04/B02 zero-diagonal physical-triple theorem, canonical report commit `0b11995430ce407a8852ac3bc5651491f2ee64f7`.

Execution/memory status: `WITHOUT_VERIFIED_BRAIN`. Repository retrieval/writeback is real; no authenticated native learned-memory receiver use was observed.

## 1. Verdict on the nine-eigenvalue grouped-Fourier proof

**PASS.** I independently checked the new analytic compiler and the threshold-nine case split. In particular, the argument does not rotate random coordinates and does not require a conditional density cap after a rotated projection.

For disjoint original-coordinate banks `H,I,J`, with a `k`-dimensional hub variable `W`, residual physical crossing rows `c_i`, order-`ell` exterior volume

`Z_ell = sum_{|T|=ell} det(C_T C_T^T)`,

subset weights `w_T`, marginals `alpha_i<=1/2`, and `d=k+ell`, the checked estimate is

`|phi_Q(t)| <= min(1, K_{k,ell}|t|^{-d/2})`,

where

`K_{k,ell}=M_H^(1/2) pi^(d/2) 2^(ell/4) e^((k+2ell)/4)
            (ell^ell/ell!)^(1/4) S^(-1/2) Z_ell^(-1/4)`.

The proof uses: (i) an exact `L2` Plancherel norm in the literal hub-frequency variable, (ii) the product-projection density bound for the difference variables, (iii) the baseline scalar Fourier-power bound at exponents `1/alpha_i>=2`, and (iv) the entropy inequality

`H(w)+sum_i alpha_i log alpha_i <= ell log ell-log(ell!)`.

The promotion branches are exact Gram-Schmidt identities, not reciprocal-minor selections. The resulting marginal-free receivers are

`||p_Q||_infinity <= C3 E_3(M)^(-1/6)`,

`C3=3 sqrt(2) e (9/2)^(1/6)=14.818337662843...`,

with a continuous `C0` density, and

`sup_a E|Q-a|^(-1/2) <= C2 E_2(M)^(-1/8)`,

`C2=8 sqrt(e) 2^(-1/8)=12.095072570796...`.

The second statement is a half-potential theorem only. It is not silently promoted to an order-two density theorem.

Using the baseline no-pivot interpolation proposition at order three gives the already-reported implication `s_9(A)>=1 -> bounded density`; the scalar and pair pivot branches close by Schur inheritance. I found no new mathematical gap in this threshold-nine proof.

## 2. Audit of the fresh two-anchor relay

The fleet03/B16 theorem `QFORM-TWOANCHOR-JOINT-L2-RELAY-v1` also **passes**.

If two literal independent original coordinates `X=(X1,X2)` are independent of `(L,R)`, the joint law of `(L,R)` has density `h in L2(R^3)`, and

`Q=X^T B X+2X dot L+R`,

then, with `kappa_X=(||f1||_2^2||f2||_2^2)^(1/2)`,

`||p_Q||_infinity <= 3*2^(-2/3) (kappa_X ||h||_2)^(2/3)`

and `p_Q in C0`.

The key exact identity is

`||A_t||_2^2 = pi^2 kappa_X^2/t^2`,

where `A_t(l)` is the two-anchor oscillatory transform in the *linear-frequency* variable `l`. The self-quadratic matrix `B` disappears from this Plancherel norm because its phase has modulus one. A second Plancherel identity gives

`int ||g_t||_2^2 dt = 2pi ||h||_2^2`.

The frequency split is therefore a genuine integrated-Fourier argument and not a pointwise van-der-Corput assertion.

Minor notation correction: in B16 Proposition 5.1, if `J^2=int ||a_t||_2^2 dt`, the direct split gives

`||p_Q||_infinity <= 1/pi + J/sqrt(2)`.

After using `J=sqrt(2pi)||h||_2`, this becomes the correctly stated joint-density form

`||p_Q||_infinity <= 1/pi + sqrt(pi)||h||_2`.

Thus the displayed joint-density conclusion is correct; only the symbol `J` is relabelled ambiguously in the prose around (5.2).

The B15/B16 spectral reductions also pass: for a terminal physical pair `H`, if

`A=[[B,C],[C^T,D]]`, `rank C=2`, and `K=ker C`,

then the subspace `{0_H} direct_sum K` has codimension four and on it `A` is exactly `D|_K`. Therefore

`s_j(D|_K) >= s_{j+4}(A)`,

so `s_8(A)>=1` forces `s_4(D|_K)>=1`. This is stronger than merely `s_4(D)>=1` and remains uniform as `B->0`.

**Multiplicity eight remains open.** Neither B15 nor B16 claims otherwise; the missing step is a product-source-valid joint `L2` estimate for `(CY,R(Y))` in the strong-cross terminal collar.

## 3. New exact parameter optimization: nine directions imply height <640

The published threshold-nine candidate can be sharpened substantially without changing its mechanism. Normalize `K=s=1` and choose

`eta=1/16`,

`beta=sqrt(eta+eta^2)=sqrt(17)/16`,

`q3=(15-2sqrt(17))/144`, `kappa3=q3^2`,

`q2=(15-sqrt(17))/64`, `kappa2=q2^2`.

### Parametric no-pivot volume lemma

If there is no `eta`-pivot, then

`|a_ii|<eta`, `|a_ij|<beta` for `i!=j`.

Suppose the order-`k` volume is below `kappa_k^k`. The baseline telescoping argument gives a seed order `r<k` with

`V_{r+1}/V_r < kappa_k`.

The completion has

`||E||_F < (r+1) q_k`, `rank R<=3r`, `rank R_LL<=r`.

With `m=4k-3` and `s_m(A)>=1`, rank perturbation forces at least `r+1` diagonal entries of `D` in `L` of modulus at least `1-||E||`. On the corresponding `(r+1)`-set `H`,

`|R_ii| > 1-(r+1)q_k-eta`,

`|R_ij| < beta+(r+1)q_k`.

Strict diagonal dominance follows whenever

`r beta + (r+1)^2 q_k + eta <= 1`.

For `(k,r)=(3,2)` the chosen `q3` makes this an equality:

`2 beta+9q3+eta=1`.

For `(k,r)=(2,1)` the chosen `q2` makes

`beta+4q2+eta=1`.

All smaller `r` are easier, and `r=0` is excluded by `||A||<=eta+q_k<1`. Hence

`no eta-pivot and s_9(A)>=1 -> V_3(A)>=kappa3^3`,

`no eta-pivot and s_5(A)>=1 -> V_2(A)>=kappa2^2`.

A fair physical cut therefore gives

`E_3(M)^(-1/6) <= 2/q3`,

and the grouped receiver gives

`||p_Q||_infinity <= 2 C3/q3 = 631.894393747... <640`.

For the residual no-pivot `s_5` half-potential branch,

`sup_a E|R-a|^(-1/2)
 <= C2 sqrt(2) q2^(-1/2)
 =41.4916788501...`.

### Pivot constants at eta=1/16

The exact coefficient in the baseline quarter-power concentration proof is bounded by

`Cq <= (8/3)(pi e^3/2)^(1/8) =4.10529289509... <5`.

This follows from the recurrence `Gamma(3/8)=(8/3)Gamma(11/8)` and Holder

`Gamma(11/8)<=Gamma(3/2)^(3/4)=(sqrt(pi)/2)^(3/4)`.

Thus the logarithmic potential obeys

`Llog <= 4+4 log Cq < 4+4 log 5 < 21/2`.

Retaining the sharper singular-kernel bound

`J(d)<=8+2sqrt(2) log_+(1/|d|)`

gives, at a scalar `eta`-pivot and with two surviving unit spectral directions,

`H_trunc < eta^(-1/2)[8+2sqrt(2)(21/2)] <152`,

hence the full half-potential is `<153`.

A definite pair pivot has full half-potential `<52`. An indefinite pair pivot with `D>=eta=1/16` has

`H_trunc <= D^(-1/2)[32+4log(16sqrt D)] <152`,

again full half-potential `<153`.

Now start from `s_9(A)>=1`:

- no pivot: density `<631.895` by the order-three grouped Fourier receiver;
- scalar pivot: its Schur complement retains at least eight unit singular directions. If it has a pivot, its full half-potential is `<153`; if not, it has `s_5>=1` and the order-two route gives `<42`. The outer square profile contributes `eta^(-1/2)=4`, hence density `<612`;
- definite pair pivot: density `<4pi<13`;
- indefinite pair pivot: the Schur complement retains at least seven unit directions and the hyperbolic/log estimate is `<72`.

Therefore the normalized theorem is

`boxed: s_9(A)>=1 -> ||p_Q||_infinity <640.`

Scaling `Y=KX` and `A` by `s` gives the general statement

`boxed: s_9(A)>=s -> ||p_Q||_infinity <=640 K^2/s.`

The no-pivot branch has a continuous `C0` density because its characteristic function is in `L1`; the theorem as a whole claims only an essentially bounded density.

## 4. New compatible-cut joint-L2 theorem for the multiplicity-eight endpoint

This is the main new B02 Fourier lemma of the run.

Let the outside product vector be split into literal original-coordinate banks `Y=(Y_I,Y_J)`. Write

`C=(C_I,C_J)`, with `C_J` a rank-two `2 x |J|` matrix, and write the outside quadratic polynomial as

`R(Y)=F(Y_I)+2Y_I^T M Y_J+G(Y_J)`.

Put

`Gamma=sqrt(det(C_J C_J^T))>0`,

`K_J=ker C_J`.

Assume the restricted physical crossing map obeys

`s_2(M|_{K_J}) >= sigma >0`.

Then the joint law of

`Z=(CY,R(Y)) in R^3`

has an `L2` density `h` satisfying

`boxed: ||h||_2^2 <= e^2 sqrt(pi)/(Gamma sigma)`,

or equivalently

`boxed: ||h||_2 <= e pi^(1/4) (Gamma sigma)^(-1/2).`

### Proof

Let

`Phi(xi,t)=E exp(i xi dot CY + it R(Y))`.

Cauchy--Schwarz in the literal bank `Y_I` gives

`|Phi(xi,t)|^2 <= E_{Y_I}|E_{Y_J} exp(i xi dot C_JY_J + it[G(Y_J)+2Y_I^T M Y_J])|^2`.

Expand the square with an independent `Y'_J` and put `U=Y_J-Y'_J`. The coordinates of `U` are independent and have densities bounded by one. The `F(Y_I)` and `C_IY_I` phases have disappeared only because of this legitimate Cauchy--Schwarz step; no rotated independence is used.

For fixed `U=u`, the remaining dependence on `Y_I` is the scalar linear form `2(Mu) dot Y_I`. The baseline product-projection theorem bounds its density by

`sqrt(e)/(2||Mu||)`.

Use Gaussian Fourier regularization in `t`; its integral is therefore at most

`pi sqrt(e)/||Mu||`, uniformly in every shift coming from `G(Y_J)-G(Y'_J)`.

It remains to control the two linear constraints generated by `xi`. Let `v1,v2` be orthonormal right singular vectors of `M|_{K_J}` with singular values `s1,s2>=sigma`, and let `w1,w2` be the corresponding orthonormal left singular vectors. Put `V u=(v1 dot u,v2 dot u)`. Because the `v_j` lie in `ker C_J`, the four-row map

`u -> (C_Ju,Vu)`

has Gram determinant `Gamma^2`. Hence the product-projection theorem gives its density `rho(c,z)` the cap

`rho(c,z) <= e^2/Gamma`,

while the marginal density of `C_JU` is at most `e/Gamma`.

For general `u`, decompose it orthogonally as

`u=k+C_J^T(C_JC_J^T)^(-1)c`, `c=C_Ju`, `k in K_J`.

Project `Mu` onto `span(w1,w2)`. There is a fixed `2 x 2` matrix `A0` such that

`(w1 dot Mu,w2 dot Mu)=diag(s1,s2) z + A0 c`.

Consequently

`||Mu|| >= sigma |z+a(c)|`

for a deterministic shift `a(c)`. For every fixed `c`, the subdensity `z -> rho(c,z)` has cap `e^2/Gamma` and mass at most `e/Gamma`. The elementary two-dimensional layer-cake inequality

`r<=A, int r<=m -> int r(z)/|z-a| dz <=2 sqrt(pi A m)`

therefore gives uniformly in `c`

`int rho(c,z)/||Mu|| dz
 <= 2 sqrt(pi) e^(3/2)/(Gamma sigma)`.

Gaussian regularization in `xi` averages this bound over `c`, so letting the regularizer vanish yields

`int_{R^3}|Phi(xi,t)|^2 dxi dt
 <= 8 pi^(7/2) e^2/(Gamma sigma)`.

By three-dimensional Plancherel/weak `L2` compactness, the law of `Z` has an `L2` density and

`||h||_2^2 <= (2pi)^(-3) * 8 pi^(7/2)e^2/(Gamma sigma)
            = e^2 sqrt(pi)/(Gamma sigma)`.

This proves the claim. Every regularization bound is uniform; no value of a rough density on a null fiber is selected.

### Actual two-anchor consequence

Combine this with the audited B16 relay. If the terminal physical pair `H` has outside statistic `(CY,R(Y))` and one can find a literal outside cut `I,J` with the two quantitative conditions above, then

`boxed:
 ||p_Q||_infinity
 <= 3*2^(-2/3) e^(2/3) pi^(1/6)
    (Gamma sigma)^(-1/3).`

Numerically the prefactor before `(Gamma sigma)^(-1/3)` is `4.45474201106...`. The density is continuous and vanishes at infinity. Crucially, there is no factor involving the weak two-anchor self determinant `det B`.

Thus the remaining multiplicity-eight problem is narrowed to a deterministic/product-compatible physicalization question: from the terminal facts `det(CC^T)>=g_*` and `s_4(D|ker C)>=1`, force one literal cut for which both `Gamma` and `s_2(D_{I,J}|ker C_J)` are bounded below, or find a different receiver for the complementary geometry.

## 5. Designated fleet04/B02 result applied at an actual inequality

The completed fleet04/B02 theorem gives, whenever a nonsingular physical `3 x 3` principal block `B0` has a zero diagonal entry,

`int |phi_Q(t)|^2 dt <= 6pi 2^(2/3)|det B0|^(-1/3)`.

On the overlap with the new threshold-nine theorem, Plancherel gives

`||p_Q||_2 <= sqrt(3) 2^(1/3)|det B0|^(-1/6)`.

Interpolating this actual partner inequality with `||p_Q||_infinity<=640` yields

`boxed:
 ||p_Q||_4
 <= sqrt(640) * 3^(1/4) * 2^(1/6)
    |det B0|^(-1/12).`

This partner theorem is used only on its exact stated scope; no zero diagonal is inferred from the nine-eigenvalue hypothesis.

## 6. Status and next obligation

- Baseline 17-eigenvalue manuscript: no new fatal gap found; prior independent audit remains valid.
- Nine-eigenvalue grouped-Fourier theorem: **PASS in this independent audit**.
- New constant sharpening: **PROVED CANDIDATE**, `s_9(A)>=s -> ||p_Q||_infinity<=640 K^2/s`; needs an independent end-to-end review before release.
- B16 two-anchor relay: **PASS**; one local notation clarification recorded above.
- New compatible-cut joint-L2 theorem: **PROVED CANDIDATE**; it converts a compatible physical cut into the exact joint `L2` resource needed by the relay.
- Multiplicity eight: **OPEN**. The first remaining implication is now a physicalization theorem coupling the strong `C` projection with two transverse crossing singular directions, or an alternate receiver for the failure of such a cut.
- Full unrestricted three-eigenvalue conjecture: **OPEN / NOT PROVED / NOT DISPROVED**.

No Gaussian, log-concavity, moment, compact-support, connected-support, diagonal-basis, post-rotation independence, arbitrary-joint coarea, or pointwise rough quadratic-phase decay assumption is used.

MODEL: GPT-5.6 Sol. THINKING LEVEL: UNKNOWN/not exposed; maximum supported was requested. Reasoning-token and provider thinking-time counters were not exposed.
