SIGNED IN - working on the quadratic-form bounded-density conjecture (universal constant), account fleet01, slot B15, 2026-09-23T17:10:51Z.
attacking: an original-coordinate proof of qualitative absolute continuity, an exact dyadic criterion separating bounded density from continuous density, and a soft-bank regularity decomposition using the completed fleet02/B15 ruled-sheet theorem.

# QFORM fleet01/B15 — dyadic regularity ladder, no uniform continuity modulus, and soft-bank C^{1,1} budget

**Programme:** QFORM-DENSITY-3EIG-20260922  
**Role:** B15 — absolute continuity and regularity  
**Status:** `NEW_TARGET_LEVEL_REGULARITY_LEMMA / NO_UNIFORM_CONTINUITY_MODULUS / SOFT_BANK_C11 / FULL_QFORM_OPEN`  
**Execution context:** `WITHOUT_VERIFIED_BRAIN`

The full owner target remains OPEN. Nothing below is presented as a proof of the universal density conjecture.

The main new points are:

1. qualitative absolute continuity has a short proof entirely in the original independent coordinates, avoiding even a qualitative reliance on a rotated/coarea representation;
2. bounded density and continuous density admit an exact **dyadic triangular-desmoothing characterization**: boundedness of the dyadic ladder is exactly `L^infinity`, while the Cauchy property of that ladder is exactly existence of a `C_0` representative;
3. applying the completed fleet02/B15 high-frequency family yields a target-valid theorem that **no source-uniform modulus of continuity can hold**, even for fixed `A=I_3`, smooth compact cap-one sources, common compact output support, and output height at most `1/2`;
4. applying fleet02/B15's completed ruled-majority theorem gives an exact high-majority/low-majority decomposition in which the high-majority part has not just a height cap but explicit box-Lipschitz and tent-`C^{1,1}` budgets. Any excess tent curvature is forced into the original-product minority/two-sheet residual.

These points sharpen the separation requested in B15: continuity is genuinely stronger than the central height estimate, and in fact no *uniform quantitative continuity modulus* is compatible with the full target class.

## 1. Sources and live corrections used

Fresh control was resolved from `yspennstate/math-research-brain/main` under the current QFORM continuation. The full conjecture is still marked OPEN. The following live corrections are preserved throughout:

- no uniform pointwise quadratic Fourier decay;
- no independence after spectral rotation;
- no projection/X-ray-only estimate for the minority/two-sheet side;
- no arbitrary-joint rank-three coarea cap;
- no conditional-density-supremum shortcut;
- no assertion that one uniformly conditioned physical principal minor must exist.

The designated completed partner source actually used is fleet02/B15:

`yspennstate/math-open-problems@46c33d97490f78f8c3de0435f63d573958d81180`

`proofnet24/QFORM-density/fleet-2026-09-22/fleet02/B15/20260923T130525Z-fleet02-B15-qform-auto11/REPORT.md`.

Two proved ingredients from that report are used below:

- the ruled majority/one-sheet submeasure theorem for an invertible indefinite **original-coordinate** physical triple;
- the verified fixed-`A=I_3` phase-aligned family of smooth compact cap-one sources with output height at most `1/2` and a large prescribed high-frequency Fourier coefficient.

The latter is used at an actual inequality in Section 4, and the former at actual inequalities in Section 5.

## 2. Qualitative absolute continuity: an original-coordinate proof

The qualitative assertion is much weaker than the owner target.

### Theorem 2.1

Let `X_1,...,X_n` be independent real random variables, each with a Lebesgue density. Let `A=A^T` be any nonzero real symmetric matrix. Then

\[
Q=X^TAX
\]

is absolutely continuous with respect to Lebesgue measure on `R`.

No density cap, eigenvalue lower bound, rank-three assumption, bounded support, smoothness, or continuity hypothesis is needed.

### Proof

The proof stays in the physical coordinates.

#### Case 1: some diagonal coefficient is nonzero

Suppose `A_ii != 0`. Condition on all coordinates except `X_i`. For every fixed outside vector,

\[
Q=aX_i^2+bX_i+c,
\qquad a=A_{ii}\ne0.
\tag{2.1}
\]

A nonconstant real quadratic sends an absolutely continuous one-dimensional law to an absolutely continuous law. One way to see this is to split `R` at the unique critical point of the quadratic. On each open side the polynomial is `C^1` and strictly monotone; the inverse is locally absolutely continuous, and the single critical point itself has zero input mass. Equivalently, the one-dimensional area formula shows that the preimage of a null set is null away from the unique zero of the derivative.

Thus every conditional output law in (2.1) is absolutely continuous. A mixture of absolutely continuous measures is absolutely continuous, proving the claim in this case.

#### Case 2: every diagonal coefficient is zero

Now suppose `A_ii=0` for every `i`. Since `A` is nonzero, choose `i != j` with

\[
A_{ij}\ne0.
\tag{2.2}
\]

Condition on `X_{-i}`. Then

\[
Q=B X_i+C,
\qquad
B=2\sum_{k\ne i}A_{ik}X_k.
\tag{2.3}
\]

Write

\[
B=2A_{ij}X_j+W,
\tag{2.4}
\]

where `W` depends only on coordinates other than `i,j`. Independence gives `X_j independent W`. Since `2A_ij X_j` has an absolutely continuous law, convolution with the arbitrary law of `W` is again absolutely continuous. Hence

\[
\Pr(B=0)=0.
\tag{2.5}
\]

For almost every outside realization, therefore, the conditional map in (2.3) is a nonconstant affine map of `X_i`; its pushforward is absolutely continuous. Averaging again proves absolute continuity of `Q`.

This proves Theorem 2.1. `square`

### Remark 2.2

This proof is deliberately more source-faithful than a spectral-coordinate proof. It uses independence only in the original coordinates, never rotates the source, and makes no quantitative density claim. Thus it does not touch the live arbitrary-joint coarea-cap correction.

## 3. Exact dyadic regularity ladder

The central B15 distinction can be expressed in one exact one-dimensional lemma.

For a finite positive Borel measure `mu` on `R`, define

\[
K_r(x)=\frac{(r-|x|)_+}{r^2},
\qquad
H_r[\mu](y)=(K_r*\mu)(y),
\tag{3.1}
\]

so `K_r` is the normalized triangular probability kernel on `[-r,r]`. Let

\[
r_k=2^{-k},\qquad k=0,1,2,\dots.
\tag{3.2}
\]

Also set

\[
D_\infty(\mu)
=
\inf\{M\ge0:\mu(E)\le M|E|\text{ for every Borel }E\},
\tag{3.3}
\]

allowing `+infinity`.

### Theorem 3.1 — bounded density is boundedness of the dyadic ladder

For every finite positive measure `mu`,

\[
\boxed{
D_\infty(\mu)
=
\sup_{k\ge0}\|H_{r_k}[\mu]\|_\infty.
}
\tag{3.4}
\]

In particular, the right side is finite if and only if `mu=p dx` for some `p in L^infinity`, and then it equals `||p||_infinity`.

#### Proof

If `mu=p dx` and `||p||_infinity=M`, Young's inequality gives

\[
\|K_r*p\|_\infty\le M
\quad\text{for every }r>0.
\tag{3.5}
\]

At every Lebesgue point of `p`,

\[
K_{r_k}*p(y)\longrightarrow p(y),
\tag{3.6}
\]

so the supremum over `k` is at least the essential supremum of `p`. This proves equality when `D_infinity(mu)<infinity`.

Conversely, suppose

\[
\sup_k\|H_{r_k}[\mu]\|_\infty\le M.
\tag{3.7}
\]

The absolutely continuous measures

\[
H_{r_k}[\mu](y)\,dy
\]

converge weakly to `mu`, because `(K_{r_k})` is an approximate identity. For every nonnegative `phi in C_c(R)`,

\[
\int \phi\,d\mu
=
\lim_{k\to\infty}
\int \phi(y)H_{r_k}[\mu](y)\,dy
\le
M\int\phi(y)\,dy.
\tag{3.8}
\]

Therefore `mu<=M dx`, which proves (3.4). `square`

### Theorem 3.2 — continuous density is the Cauchy property of the same ladder

For every finite positive Borel measure `mu`,

\[
\boxed{
\mu=p\,dx\text{ for some }p\in C_0(\mathbb R)
\iff
\bigl(H_{r_k}[\mu]\bigr)_{k\ge0}
\text{ is Cauchy in }L^\infty(\mathbb R).
}
\tag{3.9}
\]

If the condition holds, the uniform limit is exactly the `C_0` density `p`.

#### Proof

If `p in C_0`, uniform continuity of `p` and the approximate-identity property imply

\[
\|K_r*p-p\|_\infty\to0,
\tag{3.10}
\]

so the dyadic sequence is uniformly Cauchy.

Conversely, every `H_{r_k}[mu]` lies in `C_0(R)`: continuity follows from uniform continuity of the compactly supported continuous kernel `K_{r_k}`, and vanishing at infinity follows from finiteness of `mu`. If the sequence is Cauchy in sup norm, it has a uniform limit `p in C_0(R)`. On the other hand,

\[
H_{r_k}[\mu](y)\,dy\Rightarrow\mu.
\tag{3.11}
\]

Uniform convergence implies local `L^1` convergence to `p`, hence the same weak limit is `p dx`. Therefore `mu=p dx`. `square`

### Corollary 3.3 — quantitative Dini compiler

Let

\[
\eta_k
=
\|H_{r_{k+1}}[\mu]-H_{r_k}[\mu]\|_\infty.
\tag{3.12}
\]

If

\[
\sum_{k=0}^\infty\eta_k<\infty,
\tag{3.13}
\]

then `mu=p dx` with `p in C_0`, and

\[
\boxed{
\|p-H_{r_m}[\mu]\|_\infty
\le
\sum_{k=m}^\infty\eta_k.
}
\tag{3.14}
\]

This is only a sufficient quantitative criterion; the exact qualitative criterion is the Cauchy condition (3.9).

### 3.1 The distinction is strict

The probability measure with density

\[
p=\mathbf 1_{[0,1]}
\tag{3.15}
\]

has `D_infinity=1`, so Theorem 3.1 gives a uniformly bounded dyadic ladder. It has no continuous representative. Correspondingly, its dyadic ladder is not uniformly Cauchy. Indeed for any `r<=1/2`, at `y=r/2` the left endpoint at zero is the only relevant boundary and

\[
(K_r*p)(r/2)=\frac78,
\qquad
(K_{r/2}*p)(r/2)=1,
\tag{3.16}
\]

so

\[
\boxed{
\|K_r*p-K_{r/2}*p\|_\infty\ge\frac18.
}
\tag{3.17}
\]

Thus bounded density alone does not imply continuous density, even at the one-dimensional measure-theory level.

### 3.2 Target interpretation

For a QFORM output law `mu_Q`, Theorem 3.1 says the central height assertion is exactly boundedness of one dyadic desmoothing ladder. By the spectral scaling `A -> A/r`, the global owner supremum can equivalently be represented at one fixed tent scale, as established in the previous B15 run.

Theorem 3.2 identifies the *additional* requirement for raw continuity: the same ladder must be uniformly Cauchy. The universal height conjecture asks for the first property, not the second.

## 4. Partner-derived theorem: there is no uniform continuity modulus in the target class

This is the strongest regularity separation of the run.

The completed fleet02/B15 report verifies a fixed-matrix, target-valid family with the following properties. There are numbers `s_m -> infinity`, smooth compactly supported cap-one one-dimensional densities `f_m`, three iid coordinates with density `f_m`, and the fixed matrix

\[
A=I_3,
\tag{4.1}
\]

such that the output density `p_m` of

\[
Q_m=X_{m,1}^2+X_{m,2}^2+X_{m,3}^2
\tag{4.2}
\]

satisfies

\[
p_m\in C_c^\infty((3,300)),
\qquad
\|p_m\|_\infty\le\frac12,
\tag{4.3}
\]

and

\[
\boxed{
|\widehat p_m(s_m)|\ge\frac{27}{64}.
}
\tag{4.4}
\]

This lies inside the exact owner class: `I_3` has exactly three eigenvalues of modulus one.

### Theorem 4.1 — no target-uniform approximate-identity modulus

Let `K_r` be the normalized tent kernel (3.1), and set

\[
r_m=\frac{\pi}{s_m}.
\tag{4.5}
\]

Then

\[
\boxed{
\liminf_{m\to\infty}
\|K_{r_m}*p_m-p_m\|_\infty
\ge
\frac{27}{64\cdot297}
\left(1-\frac4{\pi^2}\right)
>8.44\times10^{-4}.
}
\tag{4.6}
\]

In particular there is **no** function `omega(r)->0` such that

\[
\|K_r*p_Q-p_Q\|_\infty\le\omega(r)
\tag{4.7}
\]

holds for every smooth target-valid output in this fixed-`A=I_3` subclass, even after imposing the common height bound `||p_Q||_infinity<=1/2` and the common compact output support `[3,300]`.

#### Proof

The Fourier multiplier of `K_r` is

\[
\widehat K_r(\xi)
=
\left(\frac{\sin(r\xi/2)}{r\xi/2}\right)^2.
\tag{4.8}
\]

At the choice (4.5),

\[
\widehat K_{r_m}(s_m)=\frac4{\pi^2}.
\tag{4.9}
\]

Therefore, using (4.4),

\[
\begin{aligned}
\|(K_{r_m}*p_m-p_m)\|_1
&\ge
\left|\widehat{K_{r_m}*p_m-p_m}(s_m)\right|\\
&=
\left(1-\frac4{\pi^2}\right)|\widehat p_m(s_m)|\\
&\ge
\frac{27}{64}\left(1-\frac4{\pi^2}\right).
\end{aligned}
\tag{4.10}
\]

The difference is supported in an interval of length at most

\[
297+2r_m.
\tag{4.11}
\]

Hence

\[
\|K_{r_m}*p_m-p_m\|_\infty
\ge
\frac{27}{64(297+2r_m)}
\left(1-\frac4{\pi^2}\right).
\tag{4.12}
\]

Since `r_m ->0`, (4.6) follows. `square`

### Corollary 4.2 — no common modulus of continuity

There is no modulus `omega(delta)->0` for which all densities in the family satisfy

\[
|p_m(x+h)-p_m(x)|\le\omega(|h|)
\quad\text{for all }x,h,m.
\tag{4.13}
\]

Indeed such a modulus, replaced by its nondecreasing envelope if needed, would imply

\[
\|K_r*p_m-p_m\|_\infty
\le
\omega(r),
\tag{4.14}
\]

contradicting (4.6) along `r=r_m`.

Thus even if one proves that every individual target output has a continuous density, the owner hypotheses cannot yield source-uniform equicontinuity.

### Corollary 4.3 — every positive Hölder seminorm is non-uniform

Fix `0<alpha<=1`. If `[p]_{C^{0,alpha}}` denotes the usual global Hölder seminorm, then

\[
\|K_r*p-p\|_\infty
\le
\frac{2}{(\alpha+1)(\alpha+2)}
[p]_{C^{0,\alpha}}r^\alpha.
\tag{4.15}
\]

Combining (4.12) and (4.15) gives

\[
[p_m]_{C^{0,\alpha}}
\ge
\frac{27}{64(297+2\pi/s_m)}
\left(1-\frac4{\pi^2}\right)
\frac{(\alpha+1)(\alpha+2)}{2}
\left(\frac{s_m}{\pi}\right)^\alpha.
\tag{4.16}
\]

Therefore

\[
\boxed{
\liminf_{m\to\infty}
\frac{[p_m]_{C^{0,\alpha}}}{s_m^\alpha}
\ge
\frac{27}{64\cdot297}
\left(1-\frac4{\pi^2}\right)
\frac{(\alpha+1)(\alpha+2)}{2\pi^\alpha}
>0.
}
\tag{4.17}
\]

So no target-uniform Hölder bound of any positive order can accompany the desired universal `L^infinity` height theorem. This is not a counterexample to qualitative continuity: every `p_m` here is smooth.

### Relation to fleet02/B15's weak-limit obstruction

The partner report also proves that weakly converging cap-one sources in this family can have output laws converging uniformly on **unnormalized** interval masses while normalized shrinking-window profiles and output densities fail to converge. Theorem 4.1 is a complementary consequence: even within the smooth class itself, the desmoothing modulus of the individual output densities cannot be uniform over the target class.

## 5. Applying the completed ruled-majority theorem to an actual regularity inequality

We now use the other completed fleet02/B15 result.

Let `S` be an invertible indefinite original-coordinate physical triple and write

\[
B_S=A_{S,S},
\qquad
\kappa_S=\sigma_{\min}(B_S).
\tag{5.1}
\]

Let `G_S` denote the conditional majority/one-sheet event defined in the original coordinates after conditioning on the outside variables. The completed partner theorem gives the output submeasure

\[
\mu_S^+(E)
=
\Pr(Q\in E,G_S)
\tag{5.2}
\]

the domination

\[
\boxed{
\mu_S^+(E)\le C_S|E|,
\qquad
C_S\le\frac{\pi\sqrt2}{\kappa_S}.
}
\tag{5.3}
\]

This remains valid for arbitrary cap-one rough product inputs and arbitrary outside quadratic terms/cross-couplings under the partner hypotheses. No rotation of the source is performed.

### 5.1 Soft bank decomposition

Take a finite bank `T` of such triples and nonnegative weights `a_S`. Put

\[
R(X)=\sum_{S\in\mathcal T}a_S\mathbf 1_{G_S}(X).
\tag{5.4}
\]

For `delta>0`, split the full output law exactly as

\[
\mu_Q=\alpha_\delta+\beta_\delta,
\tag{5.5}
\]

where

\[
\alpha_\delta(E)
=
\Pr(Q\in E,R\ge\delta),
\qquad
\beta_\delta(E)
=
\Pr(Q\in E,R<\delta).
\tag{5.6}
\]

On `{R>=delta}` we have `1<=R/delta`, so for every Borel set `E`,

\[
\begin{aligned}
\alpha_\delta(E)
&\le
\frac1\delta
\mathbb E[\mathbf 1_{\{Q\in E\}}R]\\
&=
\frac1\delta
\sum_{S\in\mathcal T}a_S\mu_S^+(E)\\
&\le
D_\delta |E|,
\end{aligned}
\tag{5.7}
\]

where

\[
\boxed{
D_\delta
=
\frac1\delta
\sum_{S\in\mathcal T}a_SC_S.
}
\tag{5.8}
\]

Thus the high-majority part has an actual density `p_alpha` satisfying

\[
\boxed{
\|p_{\alpha_\delta}\|_\infty\le D_\delta.
}
\tag{5.9}
\]

This is stronger than a scalar height decomposition because it gives a genuine measure splitting with a bounded-density component.

### 5.2 Box-profile Lipschitz budget

For a positive measure `nu`, define the normalized width-`2r` box profile

\[
B_r^\nu(y)
=
\frac{\nu([y-r,y+r])}{2r}.
\tag{5.10}
\]

If `nu=p dx` with `||p||_infinity<=D`, then the symmetric difference of two shifted width-`2r` intervals has length

\[
2\min\{|h|,2r\}.
\tag{5.11}
\]

Hence

\[
\boxed{
|B_r^{\alpha_\delta}(y+h)-B_r^{\alpha_\delta}(y)|
\le
D_\delta\min\left\{\frac{|h|}{r},2\right\}.
}
\tag{5.12}
\]

More sharply, since `mu_Q=alpha_delta+beta_delta`,

\[
\boxed{
|B_r^{\mu_Q}(y+h)-B_r^{\mu_Q}(y)|
\le
D_\delta\min\left\{\frac{|h|}{r},2\right\}
+
\frac{\beta_\delta(I_{y+h,r}\triangle I_{y,r})}{2r},
}
\tag{5.13}
\]

where `I_{y,r}=[y-r,y+r]`. Thus every box-profile oscillation beyond the paid Lipschitz budget is localized to the minority residual **near the moving window edges**, not merely to its total mass.

### 5.3 Tent-profile C^{1,1} budget

Let

\[
H_r^\nu=K_r*\nu
\tag{5.14}
\]

with `K_r` from (3.1). If `nu=p dx` and `||p||_infinity<=D`, then

\[
(H_r^\nu)''(y)
=
\frac{p(y+r)-2p(y)+p(y-r)}{r^2}
\tag{5.15}
\]

for almost every `y`. Equivalently, `(H_r^nu)'` is globally Lipschitz with

\[
\boxed{
\operatorname{Lip}((H_r^\nu)')
\le
\frac{4D}{r^2}.
}
\tag{5.16}
\]

Applying this to `alpha_delta` gives

\[
\boxed{
|H_r^{\alpha_\delta}(y+h)-2H_r^{\alpha_\delta}(y)+H_r^{\alpha_\delta}(y-h)|
\le
\frac{4D_\delta h^2}{r^2}.
}
\tag{5.17}
\]

Since `H_r^{beta_delta}>=0`, (5.17) gives the one-sided residual forcing inequality

\[
\boxed{
H_r^{\beta_\delta}(y)
\ge
\left[
H_r^{\mu_Q}(y)
-
\frac{H_r^{\mu_Q}(y-h)+H_r^{\mu_Q}(y+h)}2
-
\frac{2D_\delta h^2}{r^2}
\right]_+.
}
\tag{5.18}
\]

Thus any local concavity of the full tent trace sharper than the high-majority `C^{1,1}` budget must be carried quantitatively by the low-majority/minority-two-sheet residual.

This is the completed partner theorem applied to an actual new inequality, rather than merely cited as a qualitative input.

### 5.4 Aggregate-before-inversion specialization

Choose

\[
a_S
=
\frac{\kappa_S}{\sum_{T\in\mathcal T}\kappa_T}.
\tag{5.19}
\]

Then (5.3) gives

\[
\sum_Sa_SC_S
\le
\frac{\pi\sqrt2\,N}{\sum_S\kappa_S},
\tag{5.20}
\]

where `N=|T|`. If

\[
\frac1N\sum_S\kappa_S
\ge
c\,s_3(A),
\tag{5.21}
\]

then

\[
\boxed{
s_3(A)D_\delta
\le
\frac{\pi\sqrt2}{c\delta}.
}
\tag{5.22}
\]

At unit scale this yields the explicit target-normalized regularity estimates

\[
\boxed{
s_3(A)
|B_1^{\alpha_\delta}(y+h)-B_1^{\alpha_\delta}(y)|
\le
\frac{\pi\sqrt2}{c\delta}\min\{|h|,2\},
}
\tag{5.23}
\]

and

\[
\boxed{
s_3(A)\operatorname{Lip}((H_1^{\alpha_\delta})')
\le
\frac{4\pi\sqrt2}{c\delta}.
}
\tag{5.24}
\]

The residual forcing becomes

\[
\boxed{
s_3(A)H_1^{\beta_\delta}(y)
\ge
\left[
 s_3(A)\left(
H_1^{\mu_Q}(y)
-
\frac{H_1^{\mu_Q}(y-h)+H_1^{\mu_Q}(y+h)}2
\right)
-
\frac{2\pi\sqrt2}{c\delta}h^2
\right]_+.
}
\tag{5.25}
\]

This is an aggregate-before-inversion regularity certificate. A bank need not contain one uniformly conditioned block, and it need not cover every sample point by a majority sheet. The paid component is whichever part of the source sees total weighted majority coverage at least `delta`; the rest remains explicitly visible as `beta_delta`.

## 6. What is proved, what is not, and the next unpaid implication

### 6.1 Precise hierarchy

For the owner class:

1. **Absolute continuity:** proved qualitatively, and in fact under much weaker hypotheses, by Theorem 2.1.
2. **Bounded density:** the central unresolved theorem. By Theorem 3.1 it is exactly uniform boundedness of a shrinking dyadic triangular ladder; by spectral homogeneity the global target supremum is equivalently a one-fixed-scale problem.
3. **Continuous density:** strictly stronger. By Theorem 3.2 it is exactly the uniform-Cauchy property of the same dyadic ladder. The canonical full continuous-representative claim remains OPEN; this report does not promote it.
4. **Uniform quantitative continuity:** false. Theorem 4.1 and Corollaries 4.2-4.3 show that even in the smooth fixed-`I_3` subclass with a common height cap, there is no target-uniform modulus of continuity or positive Hölder seminorm bound.

Thus the desired universal `L^infinity` theorem should be proved as a height/small-ball theorem. Any later qualitative continuity proof must be logically separate, and no argument may expect a universal modulus of continuity as a free by-product.

### 6.2 First unpaid B15 implication

The partner ruled-majority theorem plus Section 5 pays the entire high-weighted-majority component in both height and regularity. The remaining local obstruction is

\[
\beta_\delta
=
(Q)_\#\bigl(\mathbf 1_{\{R<\delta\}}\,\Pr_X\bigr),
\tag{6.1}
\]

where almost all cost-efficient original-coordinate indefinite triples are simultaneously on their minority/two-sheet sides.

For the universal height problem it remains enough to bound, at one fixed scale,

\[
\boxed{
\sup_{\rm target}\sup_y
s_3(A)\,H_1^{\beta_\delta}(y)<\infty
}
\tag{6.2}
\]

for a bank with a nondegenerate average-conditioning certificate, or to show that failure of such a bank falls into an already-paid product-preserving ridge/volume/grouped-coordinate branch.

For regularity, (5.13) and (5.25) say more: all excess box oscillation or tent concavity beyond the explicit majority budget is localized to that same residual. A future bridge can therefore attack the residual geometrically without using continuity of the full output as a premise.

### 6.3 Why the forbidden shortcuts do not enter

- **No pointwise Fourier decay:** Fourier is used only in Section 4 to turn the partner's *counterexample family* into a no-uniform-modulus theorem. No Fourier decay estimate is asserted.
- **No rotated independence:** Theorem 2.1 conditions on physical coordinates. Section 5 uses partner events and blocks in original coordinates.
- **No projection-only shortcut:** the minority residual is retained explicitly and is not estimated through an X-ray bound.
- **No arbitrary-joint coarea cap:** no quantitative joint-density coarea inequality is used.
- **No good-minor shortcut:** (5.19)-(5.22) average conditioning before inversion; one uniformly conditioned minor is not assumed.

## 7. Compact reusable statements

The following are safe to reuse in later assembly.

### B15-A — physical-coordinate absolute continuity

If independent `X_i` have densities and `A=A^T !=0`, then `X^TAX` is absolutely continuous. No cap or rank hypothesis is needed.

### B15-B — dyadic regularity ladder

For `K_r(x)=(r-|x|)_+/r^2`,

\[
D_\infty(\mu)=\sup_{k\ge0}\|K_{2^{-k}}*\mu\|_\infty,
\]

and `mu` has a `C_0` density iff `(K_{2^{-k}}*mu)_k` is Cauchy in `L^infinity`.

### B15-C — no universal continuity modulus

Inside the exact target, already for `A=I_3` and smooth compact cap-one iid sources whose output densities satisfy `||p||_infinity<=1/2`, there is no common modulus `omega(r)->0` for either

\[
\|K_r*p-p\|_\infty
\]

or pointwise continuity. In fact the family above obeys the explicit lower bound (4.6), and all positive Hölder seminorms are unbounded as in (4.17).

### B15-D — soft ruled-bank regularity compiler

If completed physical-sheet submeasures obey `mu_S^+<=C_S dx`, then for `R=sum a_S 1_{G_S}` and threshold `delta`, the high-majority pushforward `alpha_delta` satisfies

\[
\|p_{\alpha_\delta}\|_\infty
\le
D_\delta
=\delta^{-1}\sum_Sa_SC_S,
\]

its box profiles satisfy (5.12), its tent profiles satisfy the `C^{1,1}` estimate (5.17), and the minority residual obeys the forcing inequalities (5.13) and (5.18).

With fleet02/B15's `C_S<=pi sqrt(2)/kappa_S` and weights proportional to `kappa_S`, average conditioning `(1/N)sum kappa_S>=c s_3(A)` gives the target-normalized constants (5.22)-(5.25).

## 8. Status

**Full QFORM:** OPEN / NOT PROVED.  
**Absolute continuity under target hypotheses:** PROVED, with substantially weaker assumptions.  
**Universal bounded-density constant:** OPEN.  
**Continuous-representative implication under the full target:** not promoted; remains separate/open in the canonical claim ledger.  
**Universal modulus of continuity or positive Hölder regularity:** FALSE, by the target-valid partner family and Section 4.

No email, notification, schedule, cadence, enabled/quiet state, task identity, cross-account authentication, permission, paid/remote-call, or public-release state was changed.
