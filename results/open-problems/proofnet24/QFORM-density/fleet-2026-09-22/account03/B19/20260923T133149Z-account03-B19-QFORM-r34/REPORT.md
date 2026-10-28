SIGNED IN - working on the quadratic-form bounded-density conjecture (universal constant), account 03, slot B19, 2026-09-23T13:31:49Z.
attacking: QFORM-N3-TINYTAU-STAR4-PAYMENT-v1 by forcing third exterior volume from the rank-two STAR4 branch unless the hub and leaf cross block collapse into a quantitatively aligned two-channel core.

# account03/B19 r34 — STAR4 third-volume augmentation or aligned rank-two core

**Programme:** `QFORM-DENSITY-3EIG-20260922`  
**Assignment:** Universal proof assembly  
**Execution:** `WITHOUT_VERIFIED_BRAIN`  
**Status:** `ESSENTIAL_STEP_APPLIED / GLOBAL STAR4 RANK2 BRANCH NARROWED / FULL TARGET OPEN`.

The unrestricted QFORM theorem is **not** claimed. The global continuity statement is also still open. The new structural theorem below is deterministic and therefore covers arbitrary signs, arbitrary bounded-density laws, all same-side quadratic curvature, all affine terms, and arbitrary extra spectrum. The only density conclusion newly paid here is an explicit existing whole-law third-volume branch, where continuity is proved by the cited Fourier theorem.

No Gaussian, log-concave, moment, support, connected-support, iid, diagonal-basis, post-rotation-independence, pointwise van-der-Corput, arbitrary-joint coarea, or perturbative tail-deletion premise is used.

## 1. Source-pinned inputs actually applied

### 1.1 Current global STAR4 frontier

The newest completed global B19 synthesis used here is account02/B19 auto11:

- `yspennstate/math-open-problems@b0628a95c0c4630d063fe8c5649416c804dbceea`
- `proofnet24/QFORM-density/fleet-2026-09-22/account02/B19/20260923T130709Z-account02-B19-QFORM-auto11/REPORT.md`.

It fixes

`tau=2^-20`,

and, after paying the spectral-window and fifth-volume exits, forces every unpaid `N3(tau)` state into a literal original-coordinate packet with one hub `h` and disjoint leaf banks `J,K` satisfying

`||u||_2^2=sum_(j in J) A_hj^2 > beta`,
`||v||_2^2=sum_(k in K) A_hk^2 > beta`,                         (1.1)

where

`u=A[J,h]`, `v=A[K,h]`,

`beta=(1/12800-tau-2tau^2)/2
     =0.000038585661932302174...`,                              (1.2)

and with physical leaf cross block

`N=A[J,K]`,

`||N||_F^2 > E0=(1-tau)^2/4`,                                  (1.3)

whose first four singular directions carry more than `63/64` of its Frobenius energy. Its exact dichotomy says either

`s_2(N)>s_1(N)/16`,                                             (1.4)

which implies

`s_1(N)s_2(N)>rho_*:=63(1-tau)^2/16384
                     =0.003845207509588222...`,                 (1.5)

or the leaf cross block is in the relative rank-one tube

`(sum_(r>=2)s_r(N)^2)^(1/2)<=s_1(N)/6`.                         (1.6)

This run attacks the first branch (1.4)-(1.5) without deleting the tail of `N`.

### 1.2 Whole-law third-volume receiver

I use the completed volume-stability theorem cited in account03/B09 r32 from

- `yspennstate/math-open-problems@c2414ef633b9d4b7f04a83e1aeefbe713ed82bba`
- `proofnet24/QFORM-density/interactive/20260923T002323Z-volume-stability/REPORT.md`.

For an **actual original-coordinate cross matrix** `M`, put

`E3(M)=e_3(M^T M)`.

Normalize the squared physical `3x3` minors of `M` to a probability measure. If the maximum row marginal is at most `q/2`, `1<=q<3/2`, then the full quadratic form, retaining arbitrary same-bank quadratic terms, outside couplings and affine terms, has a continuous `C_0` density satisfying

`||p_Q||_infinity
 <= [3e/((3-2q)sqrt(q))] E3(M)^(-1/6).`                         (1.7)

The theorem may of course be applied after transposing the physical cross cut, so a corresponding column-marginal gate is equally legitimate.

### 1.3 Designated partner account04/B19

The completed designated-partner theorem is

- `QFORM-NULL-COLOOP-ADAPTIVE-HY-STABILITY-v1`
- `yspennstate/math-open-problems@5b5cea245bb2f9f6e85e0efb7f9bc28183fc5f1a`
- `proofnet24/QFORM-density/fleet-2026-09-22/account04/B19/20260922T222052Z-account04-B19-QFORM-r2/REPORT.md`.

In its residual-diffuse **exact-null-coloop** scope it proves, for `0<D_res<=1`,

`||p_Q||_infinity <34 sqrt(log(e/D_res)).`                      (1.8)

The newer account04/B19 r3 counterexample is also consumed as a correction: generic `L^3 + sqrt-small-ball` information does not imply `L^infinity`. No such interpolation is attempted below.

## 2. Exact third-volume update identity

The first essential missing inequality in the STAR4 rank-two branch is whether the two strong hub stars in (1.1) supply a genuinely third transverse direction to the rank-two leaf cross packet (1.5), or merely lie inside its two dominant singular channels.

Let

`N = sum_r s_r p_r q_r^T`                                       (2.1)

be a singular-value decomposition, with `s_1>=s_2>=...>=0`. Fix one choice of top-two singular subspaces

`L_2=span{p_1,p_2} subset R^J`,
`R_2=span{q_1,q_2} subset R^K`.                                 (2.2)

Define the two actual augmented physical cross cuts

`M_L=A[J,K union {h}]=[N,u]`,
`M_R=A[J union {h},K]=[N;v^T]`.                                 (2.3)

No random variable is rotated in (2.1)-(2.3); the SVD is only deterministic matrix bookkeeping.

### Lemma 2.1 — `QFORM-STAR4-THIRDVOLUME-AUGMENTATION-v1`

For every real matrix `N` and every vectors `u,v` of compatible dimensions,

`E3(M_L)
 >= E3(N)+(s_1s_2)^2 ||P_(L_2^perp)u||_2^2`,                   (2.4)

`E3(M_R)
 >= E3(N)+(s_1s_2)^2 ||P_(R_2^perp)v||_2^2`.                   (2.5)

If `N` has rank exactly two, equality holds after dropping `E3(N)=0` in the corresponding augmentation formula.

#### Proof

Put `C=NN^T`, with eigenvalues `lambda_r=s_r^2`. Since

`M_L M_L^T=C+uu^T`,                                            (2.6)

the rank-one update of the third elementary symmetric polynomial is

`e_3(C+uu^T)
 =e_3(C)+u^T T_2(C)u`,                                         (2.7)

where the second Newton transform is

`T_2(C)=e_2(C)I-e_1(C)C+C^2`.                                  (2.8)

In an eigenbasis of `C`, the eigenvalue of `T_2(C)` in direction `p_m` is

`sum_(a<b; a,b != m) lambda_a lambda_b`.                        (2.9)

For every `m>=3`, the sum (2.9) contains the term `lambda_1 lambda_2=s_1^2s_2^2`, while all terms are nonnegative. Hence

`u^T T_2(C)u
 >=s_1^2s_2^2 ||P_(L_2^perp)u||_2^2`,                       (2.10)

which proves (2.4). Apply the identical argument to `N^T N+vv^T=M_R^T M_R` for (2.5).

When `rank N=2`, (2.9) vanishes for `m=1,2` and equals `s_1^2s_2^2` on the kernel, so (2.10) is an equality. QED.

This is the exact aggregate-before-minor inequality needed here: no single physical `3x3` minor is selected and no reciprocal local determinant is paid.

## 3. Quantitative STAR4 compiler

Set

`delta_0 := sqrt(beta)/4
          =0.0015529339557009132...`,                           (3.1)

and

`eta_3 := (rho_* delta_0)^2
         =3.56570603332105e-11.`                                (3.2)

### Theorem 3.1 — `QFORM-STAR4-E3-ESCAPE-OR-ALIGNED-RANK2-v1`

Every STAR4 state in the quantitative rank-two branch (1.4) satisfies at least one of the following.

**(A) Third-volume escape.** One of the actual physical cross cuts `M_L,M_R` obeys

`E3(M)>=eta_3`.                                                  (3.3)

**(B) Aligned absolute rank-two core.** Simultaneously

`E3(N)<eta_3`,                                                   (3.4)

`s_3(N)<delta_0`,                                                (3.5)

`||P_(L_2)u||_2^2 >15 beta/16
                    =0.000036174058061533286...`,               (3.6)

`||P_(R_2)v||_2^2 >15 beta/16`,                                 (3.7)

while of course the strong two-channel cross currency remains

`s_1(N)s_2(N)>rho_*`.                                           (3.8)

In particular the hub retains more than `15/16` of each guaranteed star energy inside the dominant two left/right singular channels, and every third singular value is **absolutely** below `delta_0`; no tail is deleted.

#### Proof

If `E3(N)>=eta_3`, alternative (A) follows because `E3(M_L),E3(M_R)>=E3(N)` by Lemma 2.1.

Assume now `E3(N)<eta_3`. If

`||P_(L_2^perp)u||>=delta_0`,                                  (3.9)

then (1.5), (2.4) give

`E3(M_L)
 >=rho_*^2 delta_0^2=eta_3`,                                   (3.10)

so (A) holds. The same argument with `v` and (2.5) handles the right side.

The only remaining possibility is

`||P_(L_2^perp)u||<delta_0`,
`||P_(R_2^perp)v||<delta_0`.                                   (3.11)

Because `delta_0^2=beta/16` and `||u||^2,||v||^2>beta` by (1.1), Pythagoras gives (3.6)-(3.7).

Finally `E3(N)` contains the nonnegative monomial

`s_1^2s_2^2s_3^2`.

Thus (1.5), (3.4) imply

`rho_*^2 s_3^2
 < eta_3=rho_*^2 delta_0^2`,                                  (3.12)

and hence (3.5). QED.

### Interpretation

The global STAR4 rank-two problem is no longer an undifferentiated `s_2>s_1/16` packet. Either a true third exterior direction exists at the universal scale `eta_3`, or the entire obstruction is forced into a two-channel geometry in which **both** literal hub stars live almost completely inside the same two singular channels and the third singular value of the leaf cross block is below `1.553e-3` in absolute scale.

This is stronger than merely saying `N` is relatively close to rank two: `s_1` may be arbitrarily large, while (3.5) is an absolute bound.

## 4. Pay the diffuse part of the third-volume escape

Take alternative (A), and let `M` denote an augmented cut satisfying (3.3). Let the normalized physical `3x3`-volume row marginals of `M` be `alpha_i` and column marginals be `gamma_j`.

### Corollary 4.1 — `QFORM-STAR4-E3-DIFFUSE-PAYMENT-v1`

If either

`max_i alpha_i <=5/8`                                          (4.1)

or

`max_j gamma_j <=5/8`,                                         (4.2)

then the complete quadratic form has a continuous `C_0` density and

`boxed: ||p_Q||_infinity <805.`                                 (4.3)

If the corresponding marginal maximum is in fact at most `1/2`, the sharper bound is

`boxed: ||p_Q||_infinity <450.`                                 (4.4)

#### Proof

For (4.1), apply (1.7) with `q=5/4`, so `q/2=5/8`. Its constant is

`3e/((3-5/2)sqrt(5/4))
 =14.587831081048433...`.                                      (4.5)

Using `E3(M)>=eta_3`,

`||p_Q||_infinity
 <=14.587831081048433 eta_3^(-1/6)
 =804.0810056354978... <805.`                                  (4.6)

For (4.2), transpose the physical cut and apply the same theorem. At marginal threshold `1/2`, use `q=1`, whose constant is `3e`; this gives

`3e eta_3^(-1/6)=449.4949470043412...<450.`                     (4.7)

The cited theorem gives continuity. QED.

No same-side curvature or extra spectrum has been removed in this payment; the augmented matrices in (2.3) are literal cross blocks of the original full matrix.

## 5. If the third-volume escape is concentrated, it has a two-sided physical core

The failure of Corollary 4.1 is itself quantitative rather than a generic `high leverage` label.

### Lemma 5.1 — `QFORM-STAR4-E3-CONCENTRATED-ROWCOL-CORE-v1`

Suppose `E3(M)>=eta_3`, but both the row and column normalized third-volume measures have maximum marginal greater than `5/8`. Then there exist one physical row `i` and one physical column `k` such that the total squared `3x3` determinant mass of minors containing **both** `i` and `k` is strictly larger than

`E3(M)/4 >= eta_3/4
          =8.914265083302626e-12.`                              (5.1)

#### Proof

Let `(R,C)` be a random row-triple/column-triple pair sampled with probability proportional to `det M[R,C]^2`. Choose `i,k` with

`P(i in R)>5/8`, `P(k in C)>5/8`.                               (5.2)

The union bound in reverse gives

`P(i in R and k in C)
 >=P(i in R)+P(k in C)-1 >1/4`.                                 (5.3)

Multiplying by the normalizing total `E3(M)` proves (5.1). QED.

Thus the unpaid part of the E3 escape is a literal two-sided physical row/column concentration carrying a fixed amount of third determinant mass. This is a substantially smaller finite-core-style target than arbitrary STAR4.

## 6. Compact conditional end-to-end assembly after this run

The strongest current source-pinned assembly is now:

1. The owner geometric synthesis used by account02/B19 reduces the full target to one fixed strict no-pivot class; account02/B19 takes `tau=2^-20`.
2. The completed `1/16` spectral-window receiver pays the low-leverage branch by `<217.085` with continuous density.
3. Every remaining state yields a literal balanced hub and leaf cut. The unrestricted fifth-volume theorem pays the diffuse five-direction leaf cross branch by `<198.634`, continuously.
4. Every survivor is STAR4. Account02/B19 splits STAR4 into a quantitative rank-two branch (1.4)-(1.5) and a relative rank-one tube (1.6).
5. This run splits the quantitative rank-two branch into:
   - a third-volume escape;
   - or the aligned absolute-rank-two core (3.4)-(3.8).
6. The volume-diffuse part of the third-volume escape is now paid by `<805` (or `<450` at the sharper `1/2` marginal gate), continuously.
7. Its only unpaid third-volume subbranch is the two-sided concentrated physical row/column core (5.1).
8. Separately, the STAR4 relative-rank-one tube remains unpaid.

Therefore a full proof along the present global route would follow once the following **three explicit residues** are paid without deleting their retained curvature/tails:

`QFORM-STAR4-ALIGNED-2CHANNEL-CORE-v1`,

`QFORM-STAR4-E3-CONCENTRATED-ROWCOL-CORE-v1`,

and the pre-existing

`QFORM-STAR4-RELATIVE-RANK1-TUBE-PAYMENT-v1`.

The first is now numerically rigid: it has two hub-star projections each exceeding `15 beta/16`, cross product `s_1s_2>rho_*`, and `s_3<delta_0`.

## 7. Designated partner account04/B19 applied to an actual inequality

Apply (1.8) exactly in its proved residual-diffuse exact-null-coloop scope. On the concrete interval

`e^-8 <= D_res <=1`,                                            (7.1)

we have

`log(e/D_res)<=9`.                                               (7.2)

Therefore

`boxed: ||p_Q||_infinity <34*3=102.`                             (7.3)

The partner source separately pays `D_res=0` and `D_res>=1`. This is an equation-level application of the designated partner result. I do **not** infer any near-coloop extension from it, and I do not use the partner's refuted generic-interpolation route.

## 8. Continuity and final status

- Corollary 4.1: bounded **continuous** `C_0` density.
- Partner exact-null-coloop range (7.1): continuous density in the partner theorem's scope.
- The new deterministic compiler itself: no density regularity assertion; it only routes coefficient geometry.
- Full target: `OPEN / NOT PROVED / NOT DISPROVED`.
- Full-target continuity: `OPEN`.
- Two independent end-to-end reviews of a full proof do not exist.

The next mathematical attack should start from the aligned two-channel core before trying another generic Fourier estimate: retain the two-dimensional product-projection provenance of `J` and `K`, the literal independent hub coordinate, and the absolute `s_3<delta_0` tail certificate. If that route fails, the concentrated E3 core in Lemma 5.1 is the second target; its heavy row and heavy column should be spent directly rather than converted to a reciprocal single minor.
