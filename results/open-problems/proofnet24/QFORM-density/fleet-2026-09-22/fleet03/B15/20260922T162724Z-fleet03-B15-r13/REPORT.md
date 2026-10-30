# QFORM B15 — full rough-input continuity from physical zero-diagonal blocks

**Programme:** `QFORM-DENSITY-3EIG-20260922`, owner revision `2026-09-22.5`  
**Worker:** `fleet03/B15`  
**Run:** `20260922T162724Z-fleet03-B15-r13`  
**Classification:** `ESSENTIAL_STEP_APPLIED / TARGET-LEVEL-CONTINUITY-CANDIDATE / UNIVERSAL-CONSTANT-OPEN`  
**Execution:** `WITHOUT_VERIFIED_BRAIN`

## 1. Result and exact scope

Let `X=(X_1,...,X_n)` have independent real coordinates with probability densities `0<=f_i<=1`, and let `A` be a real symmetric matrix of rank at least three. Then the law of

`Q=X^T A X`

has a density with a **continuous representative vanishing at infinity**:

`p_Q in C_0(R)`.

Moreover the proof gives a finite `L^infinity` bound for each fixed matrix `A`. The bound is **matrix dependent**. Therefore this report settles the separately requested rough-input continuity implication, subject to independent review, but it does **not** prove the owner's universal dimension- and matrix-independent constant. Under the owner's hypothesis of at least three eigenvalues with absolute value at least one, `rank(A)>=3`, so the theorem applies.

The nonzero-physical-diagonal case was proved in the preceding B15 run at

- `yspennstate/math-open-problems@d73760eb784a86c356c64f05dd92f84655618f02`,
- `proofnet24/QFORM-density/fleet-2026-09-22/fleet03/B15/20260922T153101Z-fleet03-B15-r12/REPORT.md`.

The first unpaid implication was therefore the exceptional class `diag(A)=0`. This report proves that class. No rotation of the independent input vector is used.

## 2. Partner mathematics actually applied

The assigned partner `fleet04/B15` proved at

- `yspennstate/math-open-problems@07672b7beb8f867c7a7b973aa3157a42ae506460`,
- `proofnet24/QFORM-density/fleet-2026-09-22/fleet04/B15/20260922T152333Z-b15-qform-continuous-envelope-r3/REPORT.md`

that the optimal universal height constants over the full target class, over target outputs in `C_0`, and over compactly supported smooth cap-one marginals are exactly equal:

`C_all=C_C0=C_sm`, including the value `+infinity`.

Its quantitative approximation statement says that for every rough target output density `p` and every `eta>0`, there is a smooth cap-one target instance with output `p_eta in C_0` such that

`||p_eta||_infinity >= ||p||_infinity-eta`.

I apply that completed result to the zero-diagonal branch proved below: for every such rough output,

`||p||_infinity <= C_sm + eta`,

hence, letting `eta downarrow 0`,

`boxed( ||p||_infinity <= C_sm ).`

Thus after the present continuity closure, the central universal-height problem may be attacked entirely on smooth marginal inputs without leaving a hidden discontinuous rough-output branch. This does not assert that `C_sm<infinity`; that remains the main conjecture.

## 3. A product-density lemma with the correct logarithmic singularity

Let `U,V` be independent real variables with probability densities `f,g` satisfying `0<=f,g<=1`. Then `S=UV` is absolutely continuous and for `s!=0` has density

`k(s)=int_R f(u) g(s/u) du/|u|`.

For `0<|s|<=1`, split the integral into `|u|<=|s|`, `|s|<|u|<=1`, and `|u|>1`.

On the first set, substitute `v=s/u`. Since `|v|>=1`,

`int_{|u|<=|s|} ... <= int_{|v|>=1} g(v) dv/|v| <=1`.

On the middle set use only `f,g<=1`:

`int_{|s|<|u|<=1} ... <= 2 log(1/|s|)`.

On the last set,

`int_{|u|>1} ... <= int f(u)du/|u| <=1`.

Hence

`k(s)<=2+2 log(1/|s|)` for `0<|s|<=1`.

For `|s|>1`, split at `sqrt(|s|)`. On the small side substitute `v=s/u`; on the large side use `1/|u|<=|s|^{-1/2}`. This gives

`k(s)<=2 |s|^{-1/2}<=2`.

Therefore, uniformly over all cap-one input densities and all translations of them,

`boxed( k(s)<=2+2 log_+(1/|s|),  s!=0. )`  (3.1)

The density is continuous on `R\{0}`. For example on `s>0`, set

`F_+(r)=e^r f(e^r)`, `G_+(r)=e^r g(e^r)`

and similarly for the negative halves. These are `L^1(R)`, and `s k(s)` is a finite sum of ordinary `L^1*L^1` convolutions evaluated at `log s`. Such convolutions lie in `C_0`; the same argument handles `s<0`.

This is exactly the singularity needed below: logarithmic, not the nonintegrable reciprocal bound produced by naive one-fiber conditioning.

## 4. Triangle block: arbitrary affine terms are continuously regularized

Consider three independent cap-one variables `X,Y,Z` and the affine quadratic

`T=2aXY+2bXZ+2cYZ+2rX+2sY+2uZ+d`,

where `a b c !=0`. Define

`X'=X+(c/a)Z+s/a`,
`Y'=Y+(b/a)Z+r/a`.

For each fixed `Z=z`, `X'` and `Y'` remain independent and their translated densities are still bounded by one. Direct expansion gives

`T=2a X'Y' + h(Z)`,

where

`h(z)=gamma z^2+beta z+d_0`,
`gamma=-2bc/a !=0`.

By (3.1), conditional on `Z=z`, the density `g_z` of `2aX'Y'` obeys

`g_z(w) <= |a|^{-1}[1+log_+(2|a|/|w|)]`                 (4.1)

for `w!=0`, uniformly in all affine shifts.

Consequently a version of the density of `T` is

`p_T(t)=int f_Z(z) g_z(t-h(z)) dz`.

### 4.1 Uniform height bound

For every `delta>0` and every real `t`, completing the square in `h` gives the one-dimensional quadratic sublevel estimate

`Leb{z: |t-h(z)|<delta} <= 2 sqrt(2 delta/|gamma|)`.       (4.2)

Indeed after translation and division by `|gamma|` this is the elementary bound

`Leb{w: |w^2-v|<epsilon} <=2 sqrt(2 epsilon)`.

Let `K=2|a|` and

`A_0=2 sqrt(2K/|gamma|)=2 sqrt(2)*|a|/sqrt(|bc|)`.

Layer cake and `f_Z<=1`, `int f_Z=1`, imply

`int f_Z(z) log_+(K/|t-h(z)|) dz`
` <= int_0^infinity min(1,A_0 e^{-q/2}) dq`
` = Psi(A_0)`,

where

`Psi(A)=2A` for `0<A<=1`,
`Psi(A)=2+2 log A` for `A>=1`.

Therefore

`boxed( ||p_T||_infinity <= M_tri(a,b,c):=|a|^{-1}[1+Psi(2 sqrt(2)|a|/sqrt(|bc|))] < infinity. )`   (4.3)

No continuity of `f_X,f_Y,f_Z` is used.

### 4.2 Continuity

Let `t_m->t`. For almost every `z`, `t-h(z)!=0`; the exceptional equation has at most two solutions. By Section 3, `g_z` is continuous away from zero, so

`g_z(t_m-h(z))->g_z(t-h(z))`

for almost every `z`.

The logarithmic envelopes are uniformly integrable. More precisely, with

`Y_tau(z)=log_+(K/|tau-h(z)|)`,

(4.2) gives for every `tau` and `q>=0`

`int f_Z 1_{Y_tau>q} <= min(1,A_0 e^{-q/2})`.

Hence the tails of `Y_tau` tend to zero uniformly in `tau`; explicitly for large `R`,

`sup_tau int_{Y_tau>R} Y_tau f_Z dz <= A_0(R+2)e^{-R/2}->0`.

Together with (4.1), Vitali's theorem gives

`int f_Z |g_z(t_m-h(z))-g_z(t-h(z))| dz ->0`.

Thus `p_T` is continuous.

The same estimates also show `p_T(t)->0` as `|t|->infinity`: first restrict `Z` to a compact set carrying all but `epsilon` of its probability; on that compact set `|t-h(z)|->infinity` uniformly and the `2/sqrt(|s|)` part of Section 3 tends uniformly to zero. On the complement use the same layer-cake estimate with total mass `epsilon`; its contribution is `O(epsilon(1+log(1/epsilon)))`. Therefore

`boxed( p_T in C_0(R). )`                                                   (4.4)

## 5. Four-variable bipartite block

Let `U=(U_1,U_2)` and `V=(V_1,V_2)` have four independent cap-one coordinate densities. Let `C` be an invertible real `2x2` matrix. Consider

`T=2 U^T C V +2r^T U+2s^T V+d`.

Componentwise translations

`U'=U+C^{-T}s`, `V'=V+C^{-1}r`

preserve independence and the cap, and reduce the problem, up to an output translation, to `2U'^T C V'`. Thus suppress the primes.

Fix `u!=0` and put

`c(u)=2 C^T u=(c_1(u),c_2(u))`.

For almost every `u`, both coefficients are nonzero. Conditional on `U=u`, the density `h_u` of `c_1V_1+c_2V_2` is a convolution of two scaled `L^1` densities, hence `h_u in C_0(R)`, and Young's inequality gives

`||h_u||_infinity <= 1/max(|c_1(u)|,|c_2(u)|)`.

If `sigma=sigma_min(C)`, then

`max_j |c_j(u)| >= ||c(u)||_2/sqrt(2) >= sqrt(2) sigma |u|`,

so

`||h_u||_infinity <= 1/(sqrt(2) sigma |u|)`.                (5.1)

The joint density `F(u)=f_1(u_1)f_2(u_2)` satisfies `0<=F<=1` and `int F=1`. A layer-cake calculation gives the sharp elementary bound

`int_{R^2} F(u)/|u| du`
` = int_0^infinity int F(u) 1_{|u|<1/q} du dq`
` <= int_0^infinity min(1,pi/q^2)dq`
` =2 sqrt(pi)`.                                               (5.2)

Integrating (5.1),

`boxed( ||p_T||_infinity <= sqrt(2pi)/sigma_min(C). )`        (5.3)

For `t_m->t`, `h_u(t_m)->h_u(t)` for almost every `u`; the right side of (5.1) is integrable against `F` by (5.2). Dominated convergence proves continuity. The same argument as `|t|->infinity`, using `h_u in C_0`, proves vanishing at infinity. Thus

`boxed( p_T in C_0(R). )`                                     (5.4)

Again this is uniform over every affine term and over all cap-one marginal densities; only the fixed block `C` enters the height constant.

## 6. Structural lemma for every zero-diagonal symmetric matrix of rank at least three

Let `A` be symmetric, `diag(A)=0`, and `rank(A)>=3`.

### Case 1: a triangle exists

If there are distinct indices `i,j,k` with

`A_ij A_ik A_jk !=0`,

then the corresponding `3x3` principal block is

`[[0,a,b],[a,0,c],[b,c,0]]`

with determinant `2abc!=0`. Conditioning on every coordinate outside this block introduces only affine terms in the three retained variables. Section 4 applies with a bound depending only on `a,b,c`, not on the conditioned values. Hence the unconditional output is a mixture of `C_0` conditional densities uniformly bounded by `M_tri`. Dominated convergence yields

`p_Q in C_0`, `||p_Q||_infinity<=M_tri`.

### Case 2: no triangle exists

Choose any nonzero edge, relabelled `(1,2)`, and write `a=A_12!=0`. The `2x2` principal pivot

`B=[[0,a],[a,0]]`

is invertible. Let `S` be the Schur complement on the remaining coordinates. Since

`rank(A)=rank(B)+rank(S)`

and `rank(A)>=3`, `S!=0`.

For every remaining index `k`,

`S_kk = -2 A_1k A_2k/a =0`,

because otherwise `(1,2,k)` would be a triangle. Thus `S` is a nonzero symmetric zero-diagonal matrix, so some off-diagonal entry `S_kl` is nonzero.

The principal `4x4` block on `{1,2,k,l}` has Schur complement, relative to `B`,

`[[0,S_kl],[S_kl,0]]`,

which is invertible. Hence this physical `4x4` principal block is invertible.

Its support graph is triangle-free on four vertices, therefore bipartite. Invertibility rules out a `1+3` bipartition (such a bipartite adjacency matrix has rank at most two), so after a permutation the block has the form

`[[0,C],[C^T,0]]`

with an invertible `2x2` cross matrix `C`.

Conditioning on every coordinate outside this block again creates only affine terms. Section 5 applies uniformly in those terms, giving

`p_Q in C_0`,
`||p_Q||_infinity <= sqrt(2pi)/sigma_min(C) < infinity`.

This proves the zero-diagonal case completely.

## 7. Combined target-level regularity theorem

Combine Section 6 with the previous B15 physical-diagonal theorem.

> **Theorem (rough-product quadratic regularity, rank at least three).**  
> For every `n`, every independent real `X_i` with probability densities `0<=f_i<=1`, and every real symmetric `A` with `rank(A)>=3`, the law of `X^TAX` has a density `p_Q in C_0(R)`. For each fixed `A`, `||p_Q||_infinity<infinity`, with an explicit matrix-dependent bound obtained from a physical `3x3` or `4x4` block. No input-density continuity, moment, compact-support, connected-support, Gaussian, log-concavity, or eigenbasis-independence assumption is made.

For the owner's exact three-large-eigenvalue target this proves:

1. absolute continuity;
2. essential boundedness for every fixed instance;
3. existence of a continuous representative (indeed `C_0`).

What remains open is the decisive uniformity:

`sup_{n,A,(f_i)} ||p_{X^TAX}||_infinity < infinity`

under the three-large-eigenvalue normalization. The block constants above can deteriorate as physical minors become small, so they do not establish a universal `C`.

## 8. First next implication

The regularity question is no longer the obstruction if this proof survives independent review. The central unpaid step is to replace the selected-block constants

`M_tri(a,b,c)` and `sqrt(2pi)/sigma_min(C)`

by a dimension- and matrix-independent aggregate payment using the spectral hypothesis that at least three eigenvalues have magnitude at least one. The live correction inbox already rules out doing this through a single uniformly good physical minor. The next route must average/aggregate many physical blocks or use a global product-measure inequality before paying reciprocal minor costs.

## 9. Verification notes

The key algebraic identity in Section 4 was checked symbolically during this run:

`q-2a(x+c z/a+s/a)(y+b z/a+r/a)`

is exactly a quadratic polynomial in `z` with leading coefficient `-2bc/a`.

The constants in (4.2), the layer-cake integral `Psi`, and (5.2) are exact elementary integrals. No Monte Carlo or numerical histogram is used.

**Status:** continuity/instancewise boundedness candidate proved at worker scope; universal QFORM constant OPEN; independent end-to-end review still required before fleet-level claim consolidation.
