SIGNED IN - working on the quadratic-form bounded-density conjecture (universal constant), account 03, slot B15, 2026-09-23T00:28:19Z.
attacking: target-level continuity closure and the exact positive-heat formulation of the sole remaining universal-height problem.

# account03/B15 r22 — independent target-level regularity closure

**Programme:** `QFORM-DENSITY-3EIG-20260922`  
**Assignment:** Absolute continuity and regularity  
**Run:** `20260923T002819Z-account03-B15-qform-r22`  
**Status:** `ESSENTIAL_STEP_APPLIED / TARGET_C0_REGULARITY_REVIEW_PASS / UNIVERSAL_HEIGHT_OPEN`  
**Execution:** `WITHOUT_VERIFIED_BRAIN`  

## 1. Result

The universal constant conjecture is still **OPEN**. This report independently checks and assembles the qualitative regularity implication that had remained separated from the height problem.

### Theorem — fixed-matrix target regularity

Let `X=(X_1,...,X_n)` have independent real coordinates with probability densities `0<=f_i<=1`, and let `A` be a fixed real symmetric matrix.

1. If `A!=0`, then `Q=X^TAX` is absolutely continuous.
2. If `rank(A)>=3`, then `Q` has an individually bounded density with a representative

   `p_Q in C_0(R)`.

The `L^infinity` constant in item 2 may depend on the physical-coordinate geometry of `A`. No moment, compact-support, connected-support, log-concavity, centering, continuity of the input densities, or post-rotation independence is assumed.

Since the owner target has at least three eigenvalues with modulus at least one, every target instance has rank at least three. Consequently the requested **continuous-density conclusion is qualitatively closed at target scope**: every admissible instance already has a bounded `C_0` density. The only remaining full-target question is whether the heights of these continuous densities admit one matrix-, dimension-, and law-independent finite bound.

Equivalently, if the universal conjecture is false, failure cannot occur through one target instance having no density, an unbounded density, or a discontinuous density. It must occur through a sequence of admissible instances whose finite continuous-density maxima tend to infinity.

The proof below independently checks the two physical-coordinate branches in the completed account02/B15 regularity theorem and the earlier account03/B15 nonzero-diagonal theorem.

## 2. Source premises and corrections

Fresh control at startup was `yspennstate/math-research-brain@1b1c3533f0a9ae4bab631e0ad4d5c4ccd76d2ead`, OWNER CONTROL revision `2026-09-22.15`. The full QFORM conjecture is still open in the live state.

Completed regularity sources checked:

- account02/B15 fixed-matrix theorem, repository state containing
  `proofnet24/QFORM-density/fleet-2026-09-22/account02/B15/20260922T200544Z-account02-B15-qform-r11/REPORT.md`;
- account03/B15 nonzero-diagonal proof
  `yspennstate/math-open-problems@d73760eb784a86c356c64f05dd92f84655618f02`, path
  `proofnet24/QFORM-density/fleet-2026-09-22/account03/B15/20260922T153101Z-account03-B15-r12/REPORT.md`;
- designated partner account04/B15 heat theorem
  `yspennstate/math-open-problems@ad7e5daa036cc8330b1432285ad40fec611d37dd`, path
  `proofnet24/QFORM-density/fleet-2026-09-22/account04/B15/20260922T211430Z-account04-B15-heat-regularity-r4/REPORT.md`.

The live corrections were enforced. In particular, this proof does **not** use the false arbitrary-joint rank-three coarea inequality, positive moments of worst conditional projection caps, law-uniform pointwise van-der-Corput decay, independence after spectral rotation, a dimension-free fiber supremum, or a uniformly good physical minor.

## 3. Absolute continuity for every nonzero quadratic form

This first implication is considerably weaker than bounded density and does not need product structure.

Let

`q(x)=x^T A x`, so `grad q(x)=2Ax`.

Let `N subset R` have one-dimensional Lebesgue measure zero. For integers `m>=1`, define

`E_m={x: |x|<=m, |grad q(x)|>=1/m}`.

The coarea formula gives

`int_{E_m cap q^{-1}(N)} |grad q(x)| dx
 = int_N H^{n-1}(E_m cap q^{-1}(t)) dt =0`.

On `E_m`, `|grad q|>=1/m`, so `Leb_n(E_m cap q^{-1}(N))=0`. The complement of `union_m E_m` outside the critical set is empty, and the critical set is

`{grad q=0}=ker A`.

If `A!=0`, `ker A` is a proper linear subspace and is Lebesgue-null. Hence `q^{-1}(N)` is Lebesgue-null. Every absolutely continuous input law, in particular the product law here, therefore pushes forward to an absolutely continuous law.

This proves only density existence. Rank one and rank two examples show that absolute continuity by itself does not imply boundedness or continuity.

## 4. Smooth compact product inputs: a common C0 endpoint

Suppose first that every marginal is in `C_c^infinity`. The product density is `F in C_c^infinity(R^n)`. Orthogonally diagonalize `A` and integrate the null directions. If `r=rank(A)>=3`, the non-null spectral variables have a compactly supported smooth joint density `a in C_c^infinity(R^r)`, and

`phi_Q(t)=int exp(i t y^T Lambda y) a(y)dy`.

Fourier inversion of the smooth amplitude, followed by the exact regulated Fresnel integral, gives for `|t|>=1`

`|phi_Q(t)| <= C(A,a) |t|^{-r/2}`.

Because `r>=3`, the right side is integrable at infinity, while `|phi_Q|<=1` near zero. Thus `phi_Q in L^1(R)`. Fourier inversion gives a bounded continuous density; the Riemann-Lebesgue theorem gives vanishing at infinity:

`p_Q in C_0(R)`.

This step does not claim that rotated coordinates are independent; their whole smooth joint amplitude is retained.

Every cap-one one-dimensional probability density has cap-preserving smooth compact approximants in `L^1`: truncate, move the missing mass to a disjoint cap-one bump, then mollify with a positive unit-mass mollifier. It therefore remains to show enough fixed-matrix stability, or a direct rough theorem, to pass this endpoint to arbitrary rough marginals.

## 5. Nonzero physical diagonal: direct rough C0 theorem

Assume `rank(A)>=3` and `A_jj!=0` for some original coordinate `j`. A completed finite-dimensional principal-block extension theorem supplies an invertible physical principal block `B` of size `d=3` or `4` containing that pivot. Condition on every coordinate outside this block. The conditional polynomial in the block variables is

`T(Y)=Y^T B Y+2 ell^T Y+c`.

Because `B` is invertible, translating each original block coordinate by the corresponding component of `B^{-1}ell` removes the affine term. Such deterministic coordinate translations preserve independence and every density cap. Thus all conditioner values reduce to the same homogeneous matrix `B`, up to output translation.

After permuting within the block, write

`B=[[C,a],[a^T,b]]`, `b!=0`,

and put

`S=C-aa^T/b`, `R(U)=U^T S U`, `M(U)=a^T U/b`.

Then

`Y^T B Y = R(U)+b(Z+M(U))^2`.

Because `B` is invertible, `S` is invertible. In dimensions `d=3,4`, the residual `R` has a probability density `p_R in L^3`; the completed binary-indefinite/definite and ternary finite-block estimates give a finite matrix-dependent bound

`||p_R||_3=M_3(S)<infinity`.

### Coupled pivot, `a!=0`

The map

`Psi(u)=(R(u),M(u))=(u^TSu,(a/b)^Tu)`

has differential rows `2Su` and `a/b`. Its rank drops only on the one-dimensional subspace

`S^{-1} span(a/b)`,

which is null in dimensions two and three. Coarea therefore shows that `(R,M)` has a joint density `H(r,m)`.

Convolving the `M` coordinate with the independent pivot variable `Z` gives a joint density

`K(r,z)=int H(r,m) f_Z(z-m)dm`.

For a.e. `r`, `K(r,.) in C_0(R)` because it is an `L^1*L^1` convolution, and the cap `f_Z<=1` yields the exact envelope

`0<=K(r,z)<=int H(r,m)dm=p_R(r)`.

For `T=R+bV^2`, `V=Z+M`, the square change of variables gives

`p_T(t) <= |b|^{-1/2} int_{sign(b)(t-r)>0} p_R(r)|t-r|^{-1/2}dr`.

Split at distance `L`. Holder with exponents `3` and `3/2` gives the near contribution

`<=4^(2/3)||p_R||_3 L^(1/6)`,

and the far contribution is `<=L^{-1/2}`. Choosing

`L=1/(4||p_R||_3^(3/2))`

gives

`||p_T||_infinity <=4 |b|^{-1/2} ||p_R||_3^(3/4)<infinity`.

Continuity follows from dominated convergence away from the moving square-root endpoint and the same `L^3` estimate on a shrinking endpoint interval. Vanishing at infinity follows by splitting at fixed `L`, using local `L^3` tail decay of `p_R^3`, and then taking `L` large. Hence `p_T in C_0`.

### Uncoupled pivot, `a=0`

Then `R` and `bZ^2` are independent. The completed finite-dimensional residual estimate and ordinary convolution regularity give a bounded `C_0` density. In the four-variable branch, for example,

`||p_R||_infinity <= (2*pi+3*sqrt(3))/sigma_min(S)`,

and convolution with the independent square density does not increase this height.

All constants depend only on the selected fixed block `B`, not on the conditioned outside coordinates or affine terms. Therefore averaging the conditional densities over the outside variables preserves continuity and vanishing at infinity by dominated convergence. Thus

`rank(A)>=3` and `some A_jj!=0` imply `p_Q in C_0 cap L^infinity`.

## 6. Zero physical diagonal: exhaustive graph proof

Assume now

`diag(A)=0`, `rank(A)>=3`.

Let the support graph have vertices the original coordinates and an edge `ij` whenever `A_ij!=0`.

### 6.1 Triangle branch

Suppose vertices `x,y,z` form a triangle. After conditioning on all other original coordinates, the conditional polynomial is

`2axy+2bxz+2cyz+ell_1 x+ell_2 y+ell_3 z+d`, `abc!=0`.

For fixed `z`, coordinate translations in `x,y` rewrite this as

`2aUV+H(z)`,

where `H` is a one-dimensional quadratic whose quadratic coefficient is `-2bc/a`, hence nonzero.

The needed rough stability follows from a product-density envelope. If `0<=h<=1` has mass `delta` and `0<=g<=1` is a probability density, the density `k` of the product sublaw satisfies, for `s!=0`,

`k(s)<=Phi_delta(s):=4 log(1+(1/2)sqrt(delta/|s|))`.       (6.1)

A direct split of `int h(u)g(s/u)du/|u|` at `|u|=r`, followed by the bathtub principle on each side and the choice `r=sqrt(delta |s|)`, proves (6.1).

If a real random variable `W` obeys the quadratic small-ball estimate

`P(|W|<=rho)<=min(1,L sqrt(rho))`,

then integrating (6.1) against `W` gives

`E Phi_delta(W) <= Omega(L sqrt(delta))`,                 (6.2)

where

`Omega(a)=2a log(1+2/a)+4 log(1+a/2)`,

and `Omega(a)->0` as `a->0`. For the nonconstant quadratic `(t-H(Z))/(2a)` with a cap-one `Z`, the elementary quadratic preimage bound gives exactly such an `L sqrt(rho)` estimate, with finite `L` depending on `a,b,c` but not on the input law or affine terms.

Therefore changing one of the three triangle marginals by `L^1` distance `delta` changes the output density in `L^infinity` by a modulus tending to zero. Taking `delta=1` in the same estimate gives a finite conditional core height `M_T`. Changing any outside marginal costs at most `M_T` times its `L^1` distance, because after conditioning outside the triangle the affine coefficients may change but the same conditional core bound applies.

Approximate every marginal by smooth compact cap-one densities. Telescoping the three core marginals with (6.2) and all outside marginals with the linear `M_T` estimate shows that the smooth output densities converge uniformly. Since each smooth output lies in `C_0` and `C_0` is closed in the sup norm, the rough output lies in `C_0` and is bounded.

### 6.2 Triangle-free branch

Suppose the support graph is triangle-free. Pick any nonzero edge `{i,j}`, with `a=A_ij`. Its `2x2` principal block

`P=[[0,a],[a,0]]`

is invertible. The Schur complement on the remaining coordinates has rank `rank(A)-2>=1`. Its diagonal entries are

`S_kk=-2 A_ki A_kj/a=0`,

because triangle-freeness prevents both factors from being nonzero. A nonzero symmetric zero-diagonal matrix has a nonzero off-diagonal entry `S_kl`. Hence the physical principal four-block on `{i,j,k,l}` is invertible.

A triangle-free graph on these four vertices is bipartite. Invertibility excludes a `1+3` bipartition, so after permutation the block has the form

`B=[[0,C],[C^T,0]]`, `C in GL_2(R)`.

Conditioning outside this block adds affine terms. Since `C` is invertible, translations of the two original-coordinate pairs remove those affine terms while preserving product structure. The core is

`2U^T C V`,

with `U,V` independent pairs of original coordinates.

For fixed `u`, the density of the linear form `2u^TCV` is at most

`1/(sqrt(2)||C^T u||) <= 1/(sqrt(2) sigma_min(C)|u|)`.

If `0<=F<=1` is a planar subdensity of mass `delta`, the planar bathtub bound is

`int F(u)/|u| du <=2 sqrt(pi delta)`.

Thus changing one block marginal by `L^1` distance `delta` changes the output density by at most

`||p_f-p_g||_infinity <= sqrt(2*pi*delta)/sigma_min(C)`.       (6.3)

At `delta=1`, the same argument gives the affine-uniform conditional core height

`M_B=sqrt(2*pi)/sigma_min(C)`.

Again smooth cap-one approximation plus marginal telescoping gives uniform convergence of `C_0` output densities to the rough output density. Hence the zero-diagonal triangle-free branch also has a bounded `C_0` density.

The triangle and triangle-free cases exhaust `diag(A)=0`. Combining them with Section 5 proves the fixed-matrix theorem.

## 7. Exact application of designated partner account04/B15

The designated partner account04/B15 proved the Gaussian heat-height identity. For any finite positive law `mu`, with

`gamma_epsilon(u)=exp(-u^2/(2epsilon^2))/(sqrt(2*pi)epsilon)`, 

one has

`sup_{epsilon>0,y} (mu*gamma_epsilon)(y)=||p_mu||_infinity`,

with value `+infinity` when no bounded density exists. If `p_mu in C_0`, Gaussian smoothing converges uniformly to `p_mu`, and the heat maxima increase to the attained maximum of `p_mu` as `epsilon downarrow0`.

Apply this completed partner theorem to the target-level regularity theorem just proved. For every **individual** admissible QFORM instance,

`0 < sup_{epsilon>0,y} E gamma_epsilon(Q-y)
   = ||p_Q||_infinity
   = max_y p_Q(y) < infinity`.                                      (7.1)

Moreover, if

`M_Q(epsilon)=sup_y E gamma_epsilon(Q-y)`,

then `M_Q(epsilon)` is nondecreasing as `epsilon downarrow0` and

`lim_{epsilon downarrow0} M_Q(epsilon)=max_y p_Q(y)`.                 (7.2)

This is an actual inequality/identity application of the assigned partner result, not only a citation.

Consequently the full universal-height conjecture is exactly equivalent to

`boxed{ sup_target sup_{epsilon>0,y} E gamma_epsilon(X^TAX-y) < infinity. }`   (7.3)

There is no hidden singular-output branch left behind by this positive regularization: every target output is already a continuous bounded density. What remains is **uniformity across instances**.

The partner small-ball consequence also reads

`P(|Q-y|<=r) <= sqrt(2*pi*e) r E gamma_r(Q-y)`.

Thus any successful universal positive-heat estimate immediately yields the desired linear small-ball inequality and hence the universal density bound.

## 8. A useful separation: continuity is closed, uniform positive regularity is false

The target-level `C_0` theorem should not be overinterpreted. A newer account02/B15 construction, already with the fixed matrix `A=I_3` and strictly positive analytic Schwartz cap-one marginals, has uniformly bounded output heights but no target-uniform positive Besov/Sobolev/BV bound and no common `L^1` translation modulus. Its high-frequency output oscillation survives at scales tending to zero.

Therefore the correct ledger is:

- absolute continuity: qualitatively proved already for every nonzero `A`;
- bounded `C_0` density: qualitatively proved for every fixed `rank(A)>=3` product instance;
- a common modulus of continuity / positive Sobolev or Besov norm: false at target scope;
- one universal `L^infinity` height constant: still open.

This sharply separates the owner's stronger continuity request from the central conjecture. The remaining proof should attack the positive heat/tent or equivalent small-ball functional **directly**, before replacing the product geometry by a worst conditional density, reciprocal small minor, or uniform output-regularity seminorm.

## 9. Consequence for counterexample search

Because every target instance has a finite continuous maximum, a valid disproof of the universal constant must now be a sequence

`(n_k,A_k,{f_{i,k}})`

with at least three `|lambda(A_k)|>=1` such that

`max_y p_{Q_k}(y) -> infinity`.

Equivalently by (7.1), there must be centers `y_k` and heat scales `epsilon_k` such that

`E gamma_{epsilon_k}(Q_k-y_k) -> infinity`.

A single rough-density hard edge, jump discontinuity, atom, or infinite fixed-instance spike cannot occur in the target class and therefore cannot be the obstruction.

## 10. Full-target status and next implication

The full universal QFORM theorem is **not proved** here. The live exact-rank-three one-sheet theorem from the preceding B15 run pays the majority-sign side by `pi sqrt(2)`, while the minority-sign two-sheet side and the higher-rank aggregate geometry remain substantive universal-height problems. The latest weighted curved-fiber theorem converts the exact-rank-three two-sheet side into a cone-restricted weighted-cover problem, but its cover cost is not known to be universally bounded and can lose in diffuse frames; the diffuse rank-three Fourier-Brascamp-Lieb theorem is complementary.

The first unpaid universal implication is therefore a hybrid estimate which bounds the positive heat/tent functional uniformly across the heavy/intermediate/diffuse geometries **before** paying a local reciprocal-minor or worst-fiber cost. Continuity itself no longer needs to be proved again.

No scheduler, task state, notification, email/Drive, workflow, paid-model/API/Codex, permission, or public-release action is part of this result.
