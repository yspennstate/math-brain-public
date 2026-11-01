SIGNED IN - working on the quadratic-form bounded-density conjecture (universal constant), account fleet02, slot B15, 2026-09-23T23:05:34Z.
attacking: the nonzero leaf-leaf block left by the grouped determinant receiver; isolate the exact bad-fibre obstruction, then retain a collective rank-one Schur bank through the logarithmic pair receiver and recheck rough ruled transport without using continuity for height.

# fleet02/B15 — collective Schur repair and a full-target obstruction to worst-fibre grouped closure

Programme: `QFORM-DENSITY-3EIG-20260922`  
Run: `20260923T230534Z-fleet02-B15-qform-auto11`  
Role: absolute continuity and regularity; complementary constructions/source-valid counterexamples  
Status: `SUPPORTING_LEMMA_PROVED / ROUTE_OBSTRUCTION_PROVED / ROUGH_RULED_BRIDGE_RECHECKED / FULL_QFORM_OPEN`  
Execution: `WITHOUT_VERIFIED_BRAIN`.

## 1. First unpaid implication

The unrestricted owner theorem remains OPEN:

\[
\sup_{\substack{n\ge3,\ s_3(A)\ge1\\ X_i\ \mathrm{independent},\ 0\le f_i\le1}}
\|p_{X^TAX}\|_\infty<\infty.
\]

The previous fleet02/B15 grouped theorem paid every physical block

\[
\begin{pmatrix}C&M\\M^T&0\end{pmatrix},\qquad M\in GL_d,
\]

by conditioning the pivot variables and using the leaf variables as a purely affine receiver. The first local question was whether this can be extended with a constant depending only on `M` when the leaf block is nonzero.

This run proves that such an extension is **false already for `d=2`**: with `det M=1`, the isolated four-coordinate grouped form can have a logarithmically unbounded density. The same construction sits inside a literal full-target matrix whose complete output is uniformly bounded because a delocalized third square is retained. Thus the correct unpaid implication is sharper:

> combine a nonzero leaf-leaf/hyperbolic grouped core with the collective Schur/third resource **before** taking a worst conditional supremum or paying one physical Schur entry.

A rank-one Schur remainder is paid below with a dimension-free aggregate coefficient. The remaining analytic gap is the genuinely higher-rank/dense Schur remainder (or a structural exit to a volume/hub/grouped receiver), especially when every physical Schur coefficient is tiny.

## 2. Latest designated partner actually applied

The latest compatible fleet03/B15 result is

`yspennstate/math-open-problems@2f36eb6204ac8598eaf63faed15f9fa7fddffd0c`

at

`proofnet24/QFORM-density/fleet-2026-09-22/fleet03/B15/20260923T222614Z-fleet03-B15-qform-auto27/REPORT.md`.

Let two ORIGINAL coordinates form an invertible indefinite principal block `D`, write

\[
A=\begin{pmatrix}D&B\\B^T&C\end{pmatrix},\qquad
S=C-B^TD^{-1}B,
\]

and put

\[
\Delta=|\det D|,\qquad \kappa=\sigma_{\min}(D).
\]

Its completed theorem gives, for arbitrary rough cap-one product inputs,

\[
\boxed{\
\|p_{X^TAX}\|_\infty
\le 2^{13/4}\bigl(\Delta\kappa\,\eta(S)\bigr)^{-1/4},
\ }
\tag{2.1}
\]

where `eta(S)` is one nonzero physical Schur coefficient. The proof uses the completed physical-pair logarithmic envelope at

`math-open-problems@f7f0fedb2d93b46824f96cac1164af6f8a55626f`,

whose general form is the following. If, after completing the pair,

\[
Q=(U+m(Z))^TD(U+m(Z))+R(Z)
\]

and

\[
\sup_t\Pr(|R-t|<\rho)\le H\sqrt\rho\qquad(\rho>0),
\tag{2.2}
\]

then

\[
\boxed{\
\|p_Q\|_\infty
\le4\sqrt{2H}\,(\Delta\kappa)^{-1/4}.
\ }
\tag{2.3}
\]

The pair theorem is proved by retaining the logarithmic hyperbolic singularity and averaging it against (2.2); it never asserts independence after diagonalizing `D`.

I apply (2.3), rather than only citing it, in the next section.

## 3. Collective rank-one Schur repair

### Theorem 3.1 — `QFORM-B15-COLLECTIVE-RANK1-SCHUR-REPAIR-v1`

Assume the full form is homogeneous, the selected ORIGINAL physical pair `D` is invertible and indefinite, and its Schur complement has rank one:

\[
S=\sigma rr^T,\qquad \|r\|_2=1,\qquad \sigma\ne0.
\]

Then for arbitrary independent input coordinates with density caps one,

\[
\boxed{\
\|p_{X^TAX}\|_\infty
\le 8\sqrt2\,
(\Delta\kappa|\sigma|)^{-1/4}.
\ }
\tag{3.1}
\]

The same conclusion holds when the affine term left in the Schur remainder lies in `Range(S)`; the owner target itself is homogeneous, so no affine condition is needed there.

### Proof

Complete the physical pair in the ORIGINAL coordinates. Because the full target is homogeneous,

\[
Q=(U+D^{-1}BZ)^TD(U+D^{-1}BZ)+\sigma\langle r,Z\rangle^2.
\tag{3.2}
\]

Put

\[
T=\langle r,Z\rangle.
\]

The coordinates of `Z` remain independent; we do **not** claim that any rotated vector of coordinates is independent. We use only the one-dimensional marginal theorem for a projection of a product measure: the same Ball/Rogozin/Livshyts--Paouris--Pivovarov projection input that gives the two-dimensional cap `2` in the ruled theorem gives

\[
\|p_T\|_\infty\le\sqrt2
\tag{3.3}
\]

for every unit `r`.

For any `a in R` and `rho>0`, the set

\[
\{t:\ |\sigma t^2-a|<\rho\}
\]

has Lebesgue length at most

\[
2\sqrt{2\rho/|\sigma|}.
\]

Indeed this is the elementary sharp square-preimage bound used in the physical-entry theorem. Multiplying by (3.3),

\[
\boxed{\
\sup_a\Pr(|\sigma T^2-a|<\rho)
\le4\sqrt{\rho/|\sigma|}.
\ }
\tag{3.4}
\]

Thus (2.2) holds with

\[
H=4|\sigma|^{-1/2}.
\]

Substitution in the completed logarithmic-pair compiler (2.3) gives

\[
4\sqrt{8|\sigma|^{-1/2}}(\Delta\kappa)^{-1/4}
=8\sqrt2(\Delta\kappa|\sigma|)^{-1/4},
\]

which is (3.1). QED.

### Why this is genuinely different from (2.1)

The partner theorem pays one physical coefficient `eta(S)` and therefore can deteriorate on a delocalized rank-one bank. Theorem 3.1 pays the **nonzero Schur eigenvalue** after aggregating the whole original-coordinate bank into one scalar projection. No post-rotation independence is used; only the marginal density of that one projection is invoked.

For a fixed rank-three target branch, the height (3.1) is proved first. Only afterwards may the completed same-constant regularity compiler be invoked to obtain a canonical `C_0` representative.

## 4. A delocalized full-target family

For `m>=1`, use original coordinates

\[
(P_1,P_2,L_1,L_2,W_1,\ldots,W_m)
\]

and set

\[
Y_m={1\over\sqrt m}\sum_{j=1}^m W_j,
\]

\[
\boxed{\
Q_m=(P_1+L_1)^2-(P_2-L_2)^2+Y_m^2.
\ }
\tag{4.1}
\]

Its symmetric matrix is

\[
A_m=
\begin{pmatrix}
1&0&1&0&0\\
0&-1&0&1&0\\
1&0&1&0&0\\
0&1&0&-1&0\\
0&0&0&0&J_m/m
\end{pmatrix},
\tag{4.2}
\]

where the last row/column denotes the `m x m` bank block. The first positive pair has eigenvalues `2,0`, the negative pair has eigenvalues `-2,0`, and `J_m/m` has eigenvalues `1,0,...,0`. Hence

\[
\boxed{\operatorname{spec}(A_m)=\{2,-2,1,0,\ldots,0\}.}
\tag{4.3}
\]

So every `A_m` is literally in the owner target, uniformly in `m`.

### 4.1 Uniform full output bound for arbitrary owner inputs

Let all original coordinates be arbitrary independent variables with densities at most one. Put

\[
U=P_1+L_1,\qquad V=P_2-L_2.
\]

Because convolution with a probability density cannot raise `L^infinity`,

\[
\|p_U\|_\infty\le1,
\qquad
\|p_V\|_\infty\le1.
\tag{4.4}
\]

The scalar `Y_m` is a unit-vector projection of the independent `W` bank, hence

\[
\|p_{Y_m}\|_\infty\le\sqrt2.
\tag{4.5}
\]

The three variables `U,V,Y_m` are independent because they depend on disjoint original coordinate banks.

If a scalar variable `T` has density cap `K`, then for `s>0`

\[
p_{T^2}(s)
={p_T(\sqrt s)+p_T(-\sqrt s)\over2\sqrt s}
\le {K\over\sqrt s}.
\tag{4.6}
\]

Therefore, using (4.4)--(4.5), the same-sign sum satisfies

\[
\begin{aligned}
p_{U^2+Y_m^2}(t)
&\le \sqrt2\int_0^t {ds\over\sqrt{s(t-s)}}\\
&=\pi\sqrt2,
\qquad t>0.
\end{aligned}
\tag{4.7}
\]

Finally `-V^2` is an independent probability law, so convolution cannot raise the essential supremum:

\[
\boxed{\
\|p_{Q_m}\|_\infty\le\pi\sqrt2
\qquad\text{for every }m\text{ and every admissible product law.}
\ }
\tag{4.8}
\]

This is a complete universal-in-`m` target-chamber theorem. It uses no moment, support, log-concavity, smoothness or post-rotation independence assumption.

### 4.2 Required `e5f71d79...` source applied at a real inequality

The owner-pinned source

`math-open-problems@e5f71d79eff325201dd0274053d20268ce65b837`

was reread in all three requested files `RESULTS.md`, `FOURIER_ROUTE_REPORT.md`, and `COUNTEREXAMPLE_SEARCH.md`. Its completed Theorem A says that for three independent cap-one variables and a three-dimensional quadratic form whose three eigenvalue magnitudes are at least `sigma`,

\[
\|p_Q\|_\infty\le {6\sqrt\pi\over\sigma}.
\tag{4.9}
\]

Apply it to the actual family (4.1). By (4.5), define

\[
Z=\sqrt2\,Y_m.
\]

Then

\[
\|p_Z\|_\infty
={1\over\sqrt2}\|p_{Y_m}(\cdot/\sqrt2)\|_\infty\le1.
\]

The variables `U,V,Z` are independent cap-one variables and

\[
Q_m=U^2-V^2+{1\over2}Z^2.
\]

Thus the three coefficient magnitudes are `1,1,1/2`, so Theorem A with `sigma=1/2` gives the genuine owner-valid estimate

\[
\boxed{\
\|p_{Q_m}\|_\infty\le12\sqrt\pi.
\ }
\tag{4.10}
\]

Equation (4.8) improves that constant, but (4.10) is an independent direct application of a completed result from the required source. No independence is inferred from a spectral rotation: `U,V,Z` are explicitly built from disjoint original-coordinate banks.

### 4.3 Continuity is added only after height

The matrix `A_m` has rank three. Fleet04/B15's completed same-constant compiler at

`math-open-problems@7b2b0f54db9acbd23a5f69f715178ab666e22d8e`

states that, for a fixed rank-at-least-three target/product instance, an already-proved interval domination

\[
\Pr(Q\in I)\le M|I|
\]

upgrades to its canonical `C_0(R)` representative with the same height `M`. Apply it **after** (4.8):

\[
\boxed{\
p_{Q_m}\in C_0(\mathbb R),\qquad
\|p_{Q_m}\|_\infty\le\pi\sqrt2.
\ }
\tag{4.11}
\]

Continuity did not pay a single part of the height estimate.

## 5. Exact obstruction: arbitrary leaf curvature destroys the isolated grouped receiver

Now specialize only the first four input laws:

\[
P_1,P_2,L_1,L_2\stackrel{\rm iid}{\sim}{\rm Unif}[-1/2,1/2].
\]

Then

\[
U=P_1+L_1,\qquad V=P_2-L_2
\]

are independent with triangular density

\[
g(u)=(1-|u|)_+,\qquad |u|<1.
\]

For `H=U^2`, the density is

\[
h(s)={1-\sqrt s\over\sqrt s}\,\mathbf1_{(0,1)}(s).
\tag{5.1}
\]

Let

\[
R=U^2-V^2.
\]

For `0<t<1`,

\[
p_R(t)=\int_0^{1-t}h(s+t)h(s)\,ds.
\tag{5.2}
\]

For `0<t<1/8`, restrict the integral to `s in [t,1/4]`. On this interval,

\[
h(s)\ge{1\over2\sqrt s},
\]

and because `s+t<=2s<=1/2`,

\[
h(s+t)\ge{1\over4\sqrt{s+t}}.
\]

Hence

\[
\begin{aligned}
p_R(t)
&\ge {1\over8}\int_t^{1/4}{ds\over\sqrt{s(s+t)}}\\
&\ge {1\over8\sqrt2}\int_t^{1/4}{ds\over s}\\
&={1\over8\sqrt2}\log {1\over4t}.
\end{aligned}
\tag{5.3}
\]

Therefore

\[
\boxed{\|p_R\|_\infty=\infty.}
\tag{5.4}
\]

In the pivot/leaf order

\[
P=(P_1,P_2),\qquad L=(L_1,L_2),
\]

the four-coordinate matrix is

\[
\begin{pmatrix}
C&M\\M^T&D_L
\end{pmatrix},
\qquad
C=D_L=\operatorname{diag}(1,-1),
\qquad M=I_2.
\tag{5.5}
\]

Thus

\[
|\det M|=1
\]

while the output density is unbounded. Consequently:

\[
\boxed{\
\text{there is no finite bound depending only on }|\det M|
\text{ for }\begin{pmatrix}C&M\\M^T&D_L\end{pmatrix}
\text{ when }D_L\text{ is arbitrary.}
\ }
\tag{5.6}
\]

This is the exact obstruction to extending the previous grouped theorem by simply allowing a free leaf-leaf quadratic block.

### Worst-fibre failure inside the full target

For the full `Q_m`, conditioning on the whole `W` bank fixes `Y_m^2` and leaves only a translate of `R`. Therefore every such conditional law has an unbounded density:

\[
\boxed{\
\|p_{Q_m\mid W=w}\|_\infty=\infty
\quad\text{for every }w,
\ }
\tag{5.7}
\]

whereas the unconditional law satisfies (4.8). Hence

\[
\|p_{Q_m}\|_\infty
\le \sup_w\|p_{Q_m\mid W=w}\|_\infty
\]

is formally true but analytically useless: its right-hand side is infinite while the left-hand side is at most `pi sqrt(2)`. The third smoothing resource must be kept **inside** the receiver.

This is a source-valid obstruction to a proof interface, not a counterexample to QFORM.

## 6. Why the latest partner's physical-entry theorem is nonuniform here

Select the original physical pair `(P_1,P_2)`. Its block is

\[
D_0=\operatorname{diag}(1,-1),
\qquad \Delta=1,\quad\kappa=1.
\]

On the remaining coordinates `(L_1,L_2,W)`, the Schur complement is

\[
S_m=0_2\oplus J_m/m.
\tag{6.1}
\]

Its only nonzero eigenvalue is `1`, but every nonzero physical coefficient has magnitude `1/m`. Hence the partner certificate is

\[
\eta(S_m)=1/m,
\]

and (2.1) yields only

\[
\boxed{\
\|p_{Q_m}\|_\infty
\le2^{13/4}m^{1/4}.
\ }
\tag{6.2}
\]

The theorem is correct; the deterioration is structural. Applying Theorem 3.1 instead uses the collective rank-one eigenvalue `sigma=1` and gives

\[
\boxed{\
\|p_{Q_m}\|_\infty\le8\sqrt2
\ }
\tag{6.3}
\]

uniformly in `m`. The direct same-sign bank argument further improves this family to (4.8).

Thus the example separates three interfaces quantitatively:

1. one physical Schur entry: cost `m^(1/4)`;
2. aggregate rank-one Schur projection: uniform cost `8 sqrt(2)`;
3. retain the whole same-sign bank before convolution: uniform cost `pi sqrt(2)`.

The lesson is not that the physical-entry theorem is wrong; it is that **aggregation must precede reciprocal physical-entry payment** in delocalized Schur banks.

## 7. Independent audit of the ruled/rough-input bridge

The required `e5f71d79...` source proves, for an exact rank-three signature `(+,+,-)` form

\[
q(y)=\lambda_1y_1^2+\lambda_2y_2^2-\mu y_3^2,
\qquad \lambda_1,\lambda_2,\mu\ge1,
\]

on the one-sheet side `s>=0`,

\[
\boxed{\
p_+(s)\le C_+(\lambda_1,\lambda_2,\mu)
=(\lambda_1\lambda_2\mu)^{-1/2}
\int_0^{2\pi}
{d\theta\over
\sqrt{\sin^2\theta/\lambda_1+
\cos^2\theta/\lambda_2+1/\mu}}
\le\pi\sqrt2.
\ }
\tag{7.1}
\]

I rechecked both delicate geometric factors.

After spectral scaling to

\[
q_0(z)=z_1^2+z_2^2-z_3^2,
\]

the ruling

\[
F(\theta,t)=\sqrt s\,e_\theta+t(e_\theta^\perp+e_3)
\]

satisfies

\[
F_\theta\times F_t={1\over2}\nabla q_0(F),
\]

so

\[
{d\sigma\over|\nabla q_0|}={1\over2}\,d\theta\,dt.
\tag{7.2}
\]

Undoing the spectral scaling, the ruling direction is

\[
v_\theta=
\left(-{\sin\theta\over\sqrt{\lambda_1}},
{\cos\theta\over\sqrt{\lambda_2}},
{1\over\sqrt\mu}\right).
\tag{7.3}
\]

The parameter `t` is **not arclength**. Therefore

\[
\int \rho(y_0+t v_\theta)\,dt
={1\over|v_\theta|}\int_{\mathrm{line}}\rho\,d\ell.
\tag{7.4}
\]

The line integral is a value of a two-dimensional orthogonal projection density of the original product law, bounded by `2`. This factor `2` cancels the coarea `1/2` in (7.2), giving exactly (7.1). No independence of spectral coordinates is asserted.

### Rough inputs: interval transport, not pointwise trace

Now let the three active ORIGINAL marginals be arbitrary measurable cap-one densities `f_i`. Mollify only them:

\[
f_{i,\eta}=f_i*\rho_\eta.
\]

Then

\[
0\le f_{i,\eta}\le1,
\qquad
\|f_{i,\eta}-f_i\|_1\to0,
\]

and for their product laws

\[
\left\|
\prod_i f_{i,\eta}-\prod_i f_i
\right\|_1
\le\sum_i\|f_{i,\eta}-f_i\|_1\to0.
\tag{7.5}
\]

Suppose this physical triple sits inside a larger form and condition on every outside original coordinate `W=w`. Since the physical `3x3` block is invertible, square completion gives

\[
Q_w(x)=
(x+B^{-1}d(w))^TB(x+B^{-1}d(w))+c(w).
\tag{7.6}
\]

This is a translation in the ORIGINAL independent coordinates. Translation preserves the cap and leaves the `L^1` error in (7.5) unchanged. For each fixed `w`, deterministic quadratic pushforward and restriction to the majority event

\[
\{Q_w\ge c(w)\}
\]

contract total variation. Hence the smooth majority-side submeasures converge in total variation to the rough majority submeasure, uniformly in `w` with error bounded by the left side of (7.5).

The smooth ruled theorem gives, for every interval `I`,

\[
\nu_{w,\eta,+}(I)\le C_+(B)|I|.
\]

Taking `eta->0` in total variation and then averaging the untouched outside law yields

\[
\boxed{\
\Pr\{Q\in I,\ Q\ge c(W)\}
\le C_+(B)|I|.
\ }
\tag{7.7}
\]

This is essential boundedness of a positive submeasure. It does **not** assert continuity of that rough submeasure's density. The cone vertex creates no atom: the zero set of the nonzero quadratic polynomial has Lebesgue measure zero under an absolutely continuous product input.

Thus the ruled/rough-input bridge is sound at interval/total-variation level. Continuity is neither needed nor used to pass the height.

## 8. Absolute continuity, essential boundedness and continuity remain distinct

### 8.1 Qualitative absolute continuity

For any nonzero symmetric `A`, the joint product law has an absolutely continuous density `F`. Let

\[
q(x)=x^TAx.
\]

For a Lebesgue-null set `N subset R`, apply local coarea on balls and then monotone convergence:

\[
\int_{q^{-1}(N)}F(x)|\nabla q(x)|\,dx=0.
\]

Here

\[
\nabla q(x)=2Ax
\]

vanishes only on the proper linear subspace `ker A`, which has Lebesgue measure zero. Hence

\[
\Pr(q(X)\in N)=0.
\]

So every nonconstant quadratic pushforward under an absolutely continuous joint law is absolutely continuous. This qualitative statement has no universal height content.

### 8.2 Essential boundedness

The height estimates in this report are paid directly by small-ball/logarithmic averaging or by convolution:

- collective rank-one Schur: (3.1);
- delocalized target family: (4.8);
- ruled majority submeasure: (7.7).

No continuity statement is used to derive any of them.

### 8.3 Continuous representative

Only after a full target instance has a paid interval bound do I invoke the completed fixed-matrix rank-at-least-three theorem/same-constant compiler. For the family `A_m`, this produces (4.11) with no height loss. It does not provide any class-wide modulus of continuity, and it does not solve the universal-height problem by itself.

## 9. Exact remaining gap

The isolated extension

\[
\begin{pmatrix}C&M\\M^T&0\end{pmatrix}
\longrightarrow
\begin{pmatrix}C&M\\M^T&D_L\end{pmatrix}
\]

with a bound depending only on `M` is now ruled out by (5.6). A worst-fibre treatment of the third resource is also ruled out by (5.7).

The productive next B15 implication is therefore:

\[
\boxed{\
\text{pay the logarithmic two-sheet/grouped core jointly with a collective Schur resource,}
\text{ before taking any reciprocal physical-entry or fibre supremum.}
\ }
\]

Rank-one homogeneous Schur remainders are paid by Theorem 3.1. The next genuinely uncovered local case is a higher-rank or sign-indefinite Schur remainder whose physical coefficients all vanish with dimension, with no single rank-one projection already isolated. A valid proof must either obtain a dimension-free aggregate small-ball/log-potential estimate from the original product law or route the matrix into a completed projected-crossing/volume/hub receiver. The live `QFORM-TWOSHEET-XRAY-ONLY-FALSE` correction still forbids substituting a generic X-ray norm for this product-provenance-sensitive step.

Globally, the bare spectral hypothesis still does not guarantee a uniformly conditioned physical pair or triple, so structural aggregation remains essential.

## 10. Source and integrity ledger


Required owner-pinned source read in full scope:

- `math-open-problems@e5f71d79eff325201dd0274053d20268ce65b837`;
- `proofnet24/QFORM-density/interactive/20260922T211500Z-decoupling-brascamp-lieb/RESULTS.md`;
- `FOURIER_ROUTE_REPORT.md`;
- `COUNTEREXAMPLE_SEARCH.md`.

Latest designated partner actually applied:

- fleet03/B15, `math-open-problems@2f36eb6204ac8598eaf63faed15f9fa7fddffd0c`, run `20260923T222614Z-fleet03-B15-qform-auto27`;
- underlying pair-log compiler `math-open-problems@f7f0fedb2d93b46824f96cac1164af6f8a55626f`;
- same-constant rough/C0 compiler checked at fleet04/B15 `math-open-problems@7b2b0f54db9acbd23a5f69f715178ab666e22d8e`.

Live corrections retained include: no arbitrary-joint coarea height theorem, no post-rotation independence, no universal pointwise quadratic-phase decay, no uniform good single physical minor, no generic two-sheet X-ray closure, and the corrected translation-uniform nonzero-square affine estimate.

No moment, bounded-support, log-concavity, identical-law, Gaussian-mixture, or continuity hypothesis was introduced. No numerical experiment is used as proof. Repository access was authenticated, but no authenticated native learned-memory receiver ingestion/use was observed, so execution remains `WITHOUT_VERIFIED_BRAIN`.
