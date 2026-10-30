# fleet01/B10 QFORM r18 — heavy null coloop: singular Witt closure and a quantitative nonsingular bridge

**Programme:** QFORM-DENSITY-3EIG-20260922  
**Assignment:** rank-three coupled case  
**Outcome:** `ESSENTIAL_STEP_APPLIED / PROVED_SUPPORTING_THEOREMS / FULL_TARGET_OPEN`  
**Execution:** `WITHOUT_VERIFIED_BRAIN`

## 1. Exact scope and conditional end-to-end map

Let

`A = U M U^T`, `U^T U = I_3`,

with `M=M^T` invertible and `sigma_min(M)>=1`. The physical inputs are independent and have probability densities `0<=f_j<=1`.

This report attacks an exact-null physical row. The clean endpoint is a **null coloop**: one physical row `u_i` satisfies

`||u_i||=1`, `u_i^T M u_i=0`.

Then Parseval forces every other spectral row into the orthogonal plane `u_i^perp`. There are two possibilities.

1. Some residual row has leverage `>1/2`. The completed partner result fleet02/B10 r15, `QFORM-NULL-ROW-NESTED-HEAVY-CLOSURE-v1`, gives a uniformly large physical scalar pivot or a uniformly indefinite physical pair; existing scalar-pivot / pair-log estimates pay that branch.
2. Every residual row has leverage `<=1/2`. The residual two-dimensional product projection has an integrable Fourier transform with a dimension-free `L^1` norm. This report proves:
   - if the residual spectral quadratic block is singular, the full quadratic density is bounded **continuously** by `3 e^(2/3) |det M|^(-1/3)`;
   - if that block is nonsingular with determinant `D`, then the full density is continuous and

     `||p_Q||_infinity <= C_* D^(-1/8) |det M|^(-1/4)`,

     `C_* < 11.748`.

Thus the only unpaid null-coloop subbranch is the punctured near-singular strip `0<D<<1` in the residual-diffuse state. Importantly, the exact endpoint `D=0` is already uniformly paid; the remaining problem is a stability/averaging issue, not a geometric rank loss.

No post-rotation independence is used.

## 2. Normal form and residual product Fourier bound

Write the unit null row as `r`. Since

`sum_j u_j u_j^T=I_3`

and `u_i=r`,

`sum_{j!=i} (u_j dot r)^2 = r^T(I-r r^T)r=0`.

Hence every `u_j`, `j!=i`, lies in `r^perp`, and those rows form a Parseval frame of that two-plane.

Choose an orthonormal basis `(r,e_1,e_2)` with `M r = s e_1`, `s=||Mr||>=1`. Then

`M = [[0,s,0],[s,d,g],[0,g,f]]`,

and

`det M = -s^2 f`.

Also `(M^{-1})_{33}=1/f`; since `||M^{-1}||<=1`, `|f|>=1`.

Let `W` be the `(n-1) x 2` matrix of residual rows in the `(e_1,e_2)` basis and put

`Y=(Y_1,Y_2)=W^T X_{-i}`.

In the diffuse branch every residual leverage `h_j=||w_j||^2<=1/2`. The completed geometric Brascamp--Lieb / Hausdorff--Young estimate gives, for the joint density `g_Y`,

`||hat g_Y||_1 <= (2 pi)^2 B(W) <= (2 pi)^2 e`.     (2.1)

The quadratic is exactly

`Q = 2 s X_i Y_1 + dY_1^2 + 2gY_1Y_2 + fY_2^2`.     (2.2)

The original physical scalar `X_i` remains genuinely independent of `Y`; no independence is asserted between `Y_1,Y_2`.

## 3. Singular residual block: exact Witt closure

Let

`C=[[d,g],[g,f]]`

be the residual spectral block. Assume `det C=0`. Since `M` is invertible, `C` has rank one. Rotate only inside the residual spectral plane, which preserves every residual row leverage and (2.1), so that

`C = [[0,0],[0,lambda]]`.

In this basis the cross vector from the null direction is `(a,b)`, and

`Q = 2X_i(aY_1+bY_2)+lambda Y_2^2`.     (3.1)

The full determinant is

`det M = -a^2 lambda`,

so `a!=0`, `lambda!=0`.

### Theorem 3.1 — `QFORM-NULL-COLOOP-SINGULAR-WITT-v1`

Under the assumptions above,

`|phi_Q(t)| <= min(1, e pi^(3/2) |det M|^(-1/2) |t|^(-3/2))`,     (3.2)

and therefore `Q` has a bounded continuous density vanishing at infinity with

`||p_Q||_infinity <= 3 e^(2/3) |det M|^(-1/3) <= 3e^(2/3) < 5.844`.     (3.3)

### Proof

Fourier-invert the residual projected density using (2.1):

`g_Y(y)=(2pi)^(-2) int hat g_Y(xi) exp(i xi dot y) dxi`.

For fixed `t!=0` and residual frequency `(xi,eta)`, the kernel is

`K_t(xi,eta)=int f_i(x) int_R2 exp(i[t(2x(ay+bz)+lambda z^2)+xi y+eta z]) dy dz dx`.

Integrate `y` first. It produces

`2pi delta(2tax+xi)`.

The `x`-integration therefore contributes at most

`pi/(|ta|)`

because `f_i<=1`. The remaining `z` Fresnel integral has modulus

`sqrt(pi/(|t lambda|))`.

Hence

`|K_t(xi,eta)| <= pi^(3/2)|a|^(-1)|lambda|^(-1/2)|t|^(-3/2)`

` = pi^(3/2)|det M|^(-1/2)|t|^(-3/2)`.     (3.4)

Using (2.1) in the Fourier inversion gives (3.2). If `K=e pi^(3/2)|det M|^(-1/2)`, then

`int_R min(1,K|t|^(-3/2)) dt = 6 K^(2/3)`.

Fourier inversion yields

`||p_Q||_infinity <= (2pi)^(-1) 6K^(2/3)=3e^(2/3)|det M|^(-1/3)`.

Because `phi_Q in L^1`, the density has a continuous representative vanishing at infinity. QED.

This proof is joint in the hyperbolic and square directions. It does not invoke the false law-uniform one-dimensional pointwise van-der-Corput estimate.

## 4. Nonsingular residual block: an integrated-L3 bridge

Assume now

`D=|det C|>0`.

For a residual frequency `xi=(xi_1,xi_2)`, perform the exact two-dimensional Fresnel integral in (2.2). One obtains

`|K_t(xi)| = pi |t|^(-1) D^(-1/2) |q_{b(xi)}(t)|`,     (4.1)

where

`q_b(t)=int_R f_i(x) exp(-i alpha t x^2-i b x) dx`,

and

`|alpha| = s^2 |f|/D = |det M|/D`.     (4.2)

The linear modulation `b` depends on `xi` but is independent of `t`.

The scalar quadratic transform has a modulation-uniform `L^3` estimate. Indeed, after `w=x^2`,

`q_b(t)=int_0^infinity H_b(w)e^{-i alpha t w}dw`,

`H_b(w)=[f_i(sqrt w)e^{-ib sqrt w}+f_i(-sqrt w)e^{ib sqrt w}]/(2 sqrt w)`.

As in the standard square-transform estimate,

`int |H_b|^(3/2) <= E|X_i|^(-1/2) <= 5`;

the last inequality follows by integrating `|x|^(-1/2)` on `|x|<1` using `f_i<=1` and using total mass one outside. Hausdorff--Young therefore gives uniformly in `b`

`||q_b||_{L^3(dt)} <= (2pi)^(1/3) 5^(2/3) |alpha|^(-1/3)`.     (4.3)

For every `T>0`, Holder with exponents `3` and `3/2` yields

`int_{|t|>T} |t|^(-1)|q_b(t)|dt`

` <= 4^(2/3) T^(-1/3)(2pi)^(1/3)5^(2/3)|alpha|^(-1/3)`.     (4.4)

Insert (4.1)--(4.4), integrate `|hat g_Y|` using (2.1), and use `|phi_Q|<=1` on `|t|<=T`. Thus

`||phi_Q||_1 <= 2T + A T^(-1/3)`,     (4.5)

where

`A = e pi 4^(2/3)(2pi)^(1/3)5^(2/3) D^(-1/6)|det M|^(-1/3)`.     (4.6)

Optimizing at `T=(A/6)^(3/4)` gives

`||p_Q||_infinity <= C_* D^(-1/8)|det M|^(-1/4)`,     (4.7)

with

`C_*=(2pi)^(-1)(4/3)6^(1/4)[e pi 4^(2/3)(2pi)^(1/3)5^(2/3)]^(3/4)`

` < 11.748`.     (4.8)

Again `phi_Q in L^1`, so the density is continuous and vanishes at infinity.

For example, if `D>=1/16`, then under `|det M|>=1`,

`||p_Q||_infinity < 11.748*16^(1/8) <16.614`.     (4.9)

## 5. Actual application of fleet02/B10 r15

Completed partner result consumed:

`fleet02/B10 r15`, `QFORM-NULL-ROW-NESTED-HEAVY-CLOSURE-v1`, canonical mathematics
`yspennstate/math-open-problems@b539c58ee7c0f4c09fe8a061b14a48ba279ae4`.

For a null row of leverage `c=1` and `sigma_min(M)>=1`, if a residual row has leverage `>1/2`, r15 gives

`|A_jj|>=3/8`

or

`|A_ij|>1/32`.

In the first alternative that same row has physical leverage `>1/2`; the completed rank-three scalar-pivot bound

`128[c_j |A_jj| |det M|]^(-1/4)`

gives

`||p_Q||_infinity <=128(16/3)^(1/4)<195`.     (5.1)

In the second alternative with `|A_jj|<3/8`, r15 supplies the physical-pair singular-value lower bound `sigma_min(B)>=1/416`, while `|det B|=A_ij^2>1/1024`. The completed pair-log estimate therefore gives

`||p_Q||_infinity <8sqrt(5)(1/(1024*416))^(-1/4)<458`.     (5.2)

Thus **every residual-heavy null-coloop state is paid**. Combining this with Sections 3--4, a null coloop can remain unpaid only when all residual physical rows have leverage `<=1/2` and the residual spectral determinant lies in the punctured strip

`0<|det C|<1/16`     (5.3)

(or, more generally, tends to zero without a uniform lower bound).

## 6. First essential missing implication

The exact singular point `det C=0` is now easier than the nearby nonsingular problem. The next target is therefore

`QFORM-NULL-COLOOP-SCHUR-STABILITY-v1`:

> In the residual-diffuse null-coloop normal form (2.2), prove a density bound uniform as `det C ->0` through nonzero values.

The calculation above isolates the analytical debt. After the two-dimensional Fresnel step, the only loss is the weighted scalar transform integral

`J_b(R)=int_{|u|>R} |int f_i(x)e^{-iu x^2-i b x}dx| du/|u|`.

The `L^3` estimate gives `J_b(R)=O(R^(-1/3))`; an `O(R^(-1/2))` estimate uniform in `b` would exactly cancel the `D^(-1/2)` Fresnel prefactor and close (5.3). Such an endpoint estimate is **not assumed here**; phase-fragmented inputs make pointwise decay unavailable, so any repair must be genuinely integrated or must keep the residual product projection coupled before the scalar supremum.

The full exact-rank-three theorem is therefore still OPEN. The full owner conjecture, including additional spectrum, is also OPEN.

## 7. Corrections respected

This report does not use:

- uniform pointwise one-dimensional quadratic-phase decay;
- independence after spectral rotation;
- arbitrary-joint rank-three coarea;
- a positive conditional projection-density moment;
- naive fiber-sup integration;
- a uniformly good physical minor assumption.

The only rotation is within the two-dimensional spectral residual plane; product independence is always kept in the original physical coordinates, and the residual projection is handled through its product-origin Fourier estimate.

## 8. Continuity

Unlike several earlier B10 branches, both new branches in Sections 3 and 4 prove `phi_Q in L^1`. Hence they establish a bounded **continuous** density vanishing at infinity, not merely an essentially bounded density.
