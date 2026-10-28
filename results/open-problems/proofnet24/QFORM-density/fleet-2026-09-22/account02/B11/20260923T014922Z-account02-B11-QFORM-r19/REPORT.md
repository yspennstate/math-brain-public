SIGNED IN - working on the quadratic-form bounded-density conjecture (universal constant), account account02, slot B11, 2026-09-23T01:49:22Z.
attacking: the small-positive-D0 three-null-ray near-coloop chamber; test whether the exact null-Schur translation may be paid by conditioning the hub, and close the resulting two-sheet bank family without that loss.

# QFORM B11 r19 — near-coloop conditioning loses the rank-three smoothing

## Status and first unpaid implication

**ESSENTIAL_STEP_APPLIED / SOURCE-VALID COUNTEREXAMPLE TO A PROOF MECHANISM / PROVED SUPPORTING FAMILY / FULL QFORM OPEN.**

The first unpaid implication is now sharper:

`QFORM-FIVE-NEAR-RAY-AVERAGED-HUB-COMPILER-v1` — in the small-positive-`D0` zero-diagonal exact-rank-three chamber isolated by account01/B11 r13, retain at least one near-coloop null hub in the density integral and average it jointly with the transverse square/tangent bank.  A proof may not replace that average by `sup_x ||p_{Q|X_i=x}||_inf`: the theorem below gives a target-valid three-ray family for which the full law is uniformly bounded while that conditional supremum diverges logarithmically as `D0 -> 0`.  The compiler must still tolerate within-bank dependence and the light angular mass, or route to a completed pair/ridge/volume exit.

The full arbitrary-dimensional conjecture, arbitrary additional spectrum, and continuity remain OPEN.

## 1. Exact three-ray family with fixed target spectrum and arbitrarily small physical pairs

Let

\[
 A_0=\begin{pmatrix}0&-1&-1\\-1&0&-1\\-1&-1&0\end{pmatrix},
\]

whose eigenvalues are `1,1,-2`.  Fix `m>=1` and `0<epsilon<=1/2`.  Let `S=S_{m,epsilon}` be the `(2+2m) x 3` isometry with rows

* `sqrt(1-epsilon) e_1`, `sqrt(epsilon)e_1`;
* `m^{-1/2}e_2` repeated on a bank `B` of `m` original coordinates;
* `m^{-1/2}e_3` repeated on a disjoint bank `C` of `m` original coordinates.

Thus `S^T S=I_3`.  Define

\[
 A_{m,\epsilon}=S A_0S^T. \tag{1.1}
\]

Because `S` is an isometry, the nonzero spectrum is exactly

\[
\boxed{\{1,1,-2\}}. \tag{1.2}
\]

Every physical diagonal is zero.  The range leverage scores are

\[
1-\epsilon,\quad \epsilon,\quad 1/m,\ldots,1/m. \tag{1.3}
\]

In particular coordinate `0` is a null near-coloop of leverage `1-epsilon`.  The only nonzero physical pairs are

\[
 A_{0j}=-\sqrt{1-\epsilon}/\sqrt m,\quad
 A_{1j}=-\sqrt\epsilon/\sqrt m \qquad (j\in B\cup C),
\]

and

\[
 A_{jk}=-1/m \qquad (j\in B,k\in C). \tag{1.4}
\]

Hence

\[
\boxed{\max_{i\ne j}|A_{ij}|\le m^{-1/2}.} \tag{1.5}
\]

For every prescribed local-pair scale `eta>0`, taking `m>=eta^{-2}` therefore makes every physical pair smaller than `eta` while retaining the three target eigenvalues.

This is exactly a three-projective-null-ray frame.  Under the ordered disjoint-basis convention of the preceding B11 `D0` theorem, the Pluecker weights give

\[
\boxed{D_0=2\epsilon(1-\epsilon)(1-1/m)^2.} \tag{1.6}
\]

Indeed a nonzero basis chooses one coordinate from each of the three ray banks; two such bases are disjoint iff they choose different members of the split first ray and different members in each size-`m` bank.  Thus `D0 -> 0` precisely as the first-ray coordinate becomes a coloop.

For independent original inputs define the three disjoint-bank linear forms

\[
Y=m^{-1/2}\sum_{j\in B}X_j,\qquad
W=m^{-1/2}\sum_{k\in C}X_k,
\]
\[
Z_\epsilon=\sqrt{1-\epsilon}\,X_0+\sqrt\epsilon\,X_1. \tag{1.7}
\]

Then the physical form is exactly

\[
\boxed{Q_{m,\epsilon}=-2\{Z_\epsilon(Y+W)+YW\}.} \tag{1.8}
\]

No spectral coordinates have been declared independent: `Z_epsilon`, `Y`, and `W` are independent only because they use three disjoint sets of ORIGINAL independent coordinates.

Negating `A_{m,epsilon}` gives the dual `(1,2)` signature with spectrum `{-1,-1,2}` and all conclusions below unchanged after reflecting the output variable.

## 2. Apply the exact Claude ruled theorem to the one-sheet side

Required source package:

`yspennstate/math-open-problems@e5f71d79eff325201dd0274053d20268ce65b837`, `COUNTEREXAMPLE_SEARCH.md`, Theorem C.

That theorem gives, for an exact rank-three `(2,1)` form with spectral coefficients `lambda_1,lambda_2,-mu`, the dimension-free ruled-level-set bound on the one-sheet side `s>=0`.

Here `lambda_1=lambda_2=1`, `mu=2`, so the theorem gives the actual inequality

\[
\begin{aligned}
p_{Q_{m,\epsilon}}(s)
&\le {1\over\sqrt2}\int_0^{2\pi}
 {d\theta\over\sqrt{\sin^2\theta+\cos^2\theta+1/2}}\\
&=\boxed{{2\pi\over\sqrt3}}<3.628,
\qquad s\ge0. \tag{2.1}
\end{aligned}
\]

uniformly in `m,epsilon` and in all cap-one product input laws.  This is a direct application of the requested completed Claude result, not a bibliography citation.

The theorem does not cover `s<0`, the two-sheet side.  The next section pays that side for this family by keeping the original product-bank structure.

## 3. Uniform global bound, hence a two-sheet bound, from the completed partner kernel

Put

\[
U=Y+W,\qquad V=Y-W. \tag{3.1}
\]

Then

\[
YW={U^2-V^2\over4}
\]

and therefore

\[
\boxed{Q_{m,\epsilon}=-2Z_\epsilon U-\frac12U^2+\frac12V^2.} \tag{3.2}
\]

The current source package uses Rogozin/Ball product-projection bounds; in particular a normalized one-dimensional linear form of cap-one independent variables has a universal density cap `sqrt(2)`.  Thus

\[
\|p_Y\|_\infty,\|p_W\|_\infty\le\sqrt2. \tag{3.3}
\]

Because the two banks are independent, `(Y,W)` has product density.  The linear map `(Y,W)->(V,U)` has determinant `2`, hence

\[
\boxed{\|p_{V,U}\|_\infty\le1.} \tag{3.4}
\]

Also, since `epsilon<=1/2`, convolution with the scaled `X_1` law gives

\[
\boxed{\|p_{Z_\epsilon}\|_\infty\le (1-\epsilon)^{-1/2}\le\sqrt2.} \tag{3.5}
\]

Moreover `Z_epsilon` is independent of the pair `(V,U)` by the original-coordinate bank partition.

Latest completed named partner used:

`account03/B11`, run `20260923T011215Z-account03-B11-QFORM-r21`, canonical publication commit `807a3ba81ef862c342668396a129851fb694cf06`, `REPORT.md` Theorem 3.1 / displayed kernel (3.1).  It records the dependence-safe canonical estimate

\[
\|p_{2\alpha ZW+\beta V^2+2\gamma VW+\delta W^2}\|_\infty
\le
3\,2^{2/3}(LM)^{2/3}|\alpha|^{-2/3}|\beta|^{-1/3} \tag{3.6}
\]

when `Z` is independent of the pair, `||p_Z||inf<=L`, and the pair joint density is at most `M`.

Apply (3.6) to (3.2) with

\[
\alpha=-1,\quad \beta=1/2,\quad \gamma=0,\quad \delta=-1/2,
\quad L=\sqrt2,\quad M=1.
\]

Then

\[
\boxed{
\|p_{Q_{m,\epsilon}}\|_\infty
\le3\,2^{4/3}
=7.559526299\ldots
} \tag{3.7}
\]

for every `m>=1`, every `0<epsilon<=1/2`, and every original product input law with one-dimensional density caps at most one.

Thus the genuinely rotated `(2,1)` family has a uniform bound on the previously uncovered two-sheet side `s<0` as well as on the one-sheet side.  For the negated `(1,2)` family the same global bound holds, while (2.1) transfers to its majority-sign one-sheet side by output reflection.

### Where the rank-two logarithm went

If the square term `V^2/2` is deleted from (3.2), the core is a product-type saddle in `Z_epsilon` and `U`, and centered uniform laws give the usual logarithmic singularity.  The partner inequality does not pretend that product density is bounded.  It uses the genuinely third quadratic direction `V^2/2`: the product singularity contributes a reciprocal scale, while the independent transverse square supplies the half-order smoothing which makes the final reciprocal potential integrable.

This is exactly the rank-three mechanism required by the assignment.

## 4. Apply account03/B11 r21 null-Schur ruling and obtain a counterexample to sup-conditioning

The same named partner r21 proves an exact null-Schur translation.  For a zero physical pivot

\[
 A=\begin{pmatrix}0&a^T\\a&B\end{pmatrix},
\]

if `Bv=a` and `v^TBv=0`, then

\[
Q(\xi,Y)=(Y+v\xi)^TB(Y+v\xi), \tag{4.1}
\]

so a translation-uniform residual theorem may be applied after conditioning on the ORIGINAL variable `xi`.

For the present family the null-kernel relation is explicit.  The two coordinates on the first projective ray are collinear in `S`, and

\[
 d=\left(1,-\sqrt{(1-\epsilon)/\epsilon},0,\ldots,0\right)
\]

lies in `ker(A_{m,epsilon})`.  Consequently the partner translation vector is supported only on coordinate `1` and has

\[
\boxed{\|v\|^2={1-\epsilon\over\epsilon},} \tag{4.2}
\]

exactly matching its general formula `c/(1-c)` for leverage `c=1-epsilon`.

Indeed, conditioning `X_0=x` simply replaces

\[
X_1\mapsto X_1+\sqrt{(1-\epsilon)/\epsilon}\,x \tag{4.3}
\]

inside the residual principal form.  This is a legitimate product-preserving translation.

The issue is that taking a **supremum** over that conditional residual law destroys the uniform rank-three smoothing.

Choose now the source-valid input law in which every original coordinate is `Uniform[-1/2,1/2]`.  At the single legitimate conditional slice `X_0=0`, the residual form is

\[
R_{m,\epsilon}=-2\{\sqrt\epsilon X_1(Y+W)+YW\}. \tag{4.4}
\]

As `epsilon->0` this tends to the pure opposite-sign rank-two product `-2YW`.

### Exact lower bound on the conditional density

Let `f_m` be the density of

\[
Y=m^{-1/2}\sum_{j=1}^m U_j,
\qquad U_j\stackrel{iid}{\sim}\mathrm{Unif}[-1/2,1/2].
\]

Put

\[
\delta_m={1\over8\sqrt m},\qquad
c_m=\sqrt m\,(4m)^{-(m-1)}. \tag{4.5}
\]

For `|y|<=delta_m`, restrict the first `m-1` summands to

\[
[-1/(8m),1/(8m)].
\]

Their sum has absolute value below `1/8`; because `|sqrt(m)y|<=1/8`, the last summand required to hit `sqrt(m)y` then lies inside `[-1/4,1/4]`.  Hence

\[
\boxed{f_m(y)\ge c_m\quad (|y|\le\delta_m).} \tag{4.6}
\]

The same lower bound holds for the independent bank `W`.

Condition (4.4) further on `(Y,W)=(y,w)`.  As a function of `X_1`, the derivative has magnitude

\[
2\sqrt\epsilon |y+w|,
\]

and the root at output zero is

\[
 x_*=-{yw\over\sqrt\epsilon(y+w)}. \tag{4.7}
\]

Assume

\[
0<\epsilon\le {1\over1024m}. \tag{4.8}
\]

On the rectangle

\[
0<y\le\sqrt\epsilon/4,
\qquad
2\sqrt\epsilon\le w\le\delta_m/2, \tag{4.9}
\]

we have `|x_*|<=1/2`, both bank densities are at least `c_m`, and `y+w<=9w/8`.  Therefore the exact conditional-density formula gives

\[
\begin{aligned}
p_{R_{m,\epsilon}}(0)
&\ge c_m^2
\int_0^{\sqrt\epsilon/4}\int_{2\sqrt\epsilon}^{\delta_m/2}
 {dw\,dy\over2\sqrt\epsilon(y+w)}\\
&\ge
\boxed{
{c_m^2\over9}\log {1\over32\sqrt{m\epsilon}}
}. \tag{4.10}
\end{aligned}
\]

For each fixed `m`, this diverges to infinity as `epsilon->0`.

At the endpoint `epsilon=0`, the slice is exactly

\[
R_{m,0}=-2YW, \tag{4.11}
\]

and (4.6) gives the genuine logarithmic rank-two singularity directly from the product-density formula.

Combining (1.6) and (4.10), this is precisely a logarithmic loss as the small-positive disjoint-basis mass `D0` tends to zero.

## 5. Decisive obstruction and relation to the latest five-near-ray theorem

The full family satisfies the uniform arbitrary-law estimate (3.7), but for centered uniform laws

\[
\sup_x\|p_{Q_{m,\epsilon}\mid X_0=x}\|_\infty
\ge p_{R_{m,\epsilon}}(0)
\longrightarrow\infty. \tag{5.1}
\]

Therefore

\[
\boxed{
\text{the near-coloop null hub cannot be removed by a sup-conditional compiler uniformly in }D_0.
} \tag{5.2}
\]

This does **not** contradict account03/B11 r21.  Its null-Schur theorem is correct: it states that any already-uniform translation-stable residual bound lifts.  The present family proves that such a residual bound cannot itself remain universal in the near-coloop limit, even though the unconditioned full form remains uniformly bounded.  The lost information is the averaging over the null hub.

This also interfaces directly with the fresh account01/B11 r13 structural theorem (`math-open-problems@42a6318c46518baa413d08d31a0b18fbda582860`): small `D0` concentrates a zero-diagonal exact-rank-three frame near at most five null rays.  The present family lies in an exact **three-ray** subcase, has `D0~2epsilon`, and may simultaneously have every physical pair arbitrarily small by choosing large `m`.  Hence a future five-near-ray tangent-bank compiler cannot simply condition away a dominant ray and appeal to a translation-uniform residual theorem; it has to preserve a hub average or replace it with another genuinely aggregated payment.

The construction also blocks the fallback claim that failure of sup-conditioning must expose a constant physical pair: by (1.5), the entire pair matrix can be made arbitrarily small entrywise while (3.7) stays dimension-free.

## 6. Conditional end-to-end proof map and the new first debt

For the zero-diagonal exact-rank-three indefinite branch, the current source map now reads:

1. If `D0` is quantitatively positive and the guaranteed cross cut is diffuse, the completed volume route pays it (preceding B11 plus current volume-stability package).
2. At `D0=0`, the completed finite-null-ray bank theorem pays the exact endpoint.
3. For small positive `D0`, account01/B11 r13 concentrates all but small mass near at most five null rays and gives an exact principal/tangent/opposite-null decomposition inside each bank.
4. The present theorem proves that even an exact three-ray near-coloop subcase can have a uniformly bounded full law while every sup-conditioned residual theorem at the dominant ray loses `log(1/D0)`.  Thus hub averaging is an **essential**, not cosmetic, part of the missing compiler.
5. In the explicit three-ray split-bank model, preserving that average and the transverse square gives the global bound `3*2^(4/3)`, while the Claude ruling independently gives `2pi/sqrt(3)` on the one-sheet side.

So the first genuine unpaid implication is `QFORM-FIVE-NEAR-RAY-AVERAGED-HUB-COMPILER-v1` stated at the start.  A plausible route is a mixed Fresnel/three-arm estimate that keeps one original null bank as a coefficient variable and the tangent/opposite-null aggregates of the other banks on the smoothing side, instead of replacing the coefficient variable by a worst conditional slice.  Arbitrary self-curvature and within-bank dependence must remain present; the live corrections forbid perturbatively deleting the light angular residue merely because its coefficients are small.

## 7. Sources and correction status


Sources actually used at equations:

* `yspennstate/math-open-problems@e5f71d79eff325201dd0274053d20268ce65b837`, `COUNTEREXAMPLE_SEARCH.md`, Theorem C -> equation (2.1).
* Same source package, `RESULTS.md`, Rogozin/Ball product-projection input -> equation (3.3).
* `yspennstate/math-open-problems@807a3ba81ef862c342668396a129851fb694cf06`, account03/B11 r21 -> canonical saddle-plus-square estimate (3.6) and null-Schur translation (4.1)-(4.3).
* `yspennstate/math-open-problems@42a6318c46518baa413d08d31a0b18fbda582860`, account01/B11 r13 -> five-near-ray current structural interface used in Section 5.
* Predecessor B11 disjoint-basis/cut theorem: `yspennstate/math-open-problems@e47740cfec219112c826613bec5785af4b96cf3` -> definition and current role of `D0`.

No post-rotation independence, hidden support/moment/log-concavity assumption, arbitrary-joint coarea estimate, conditional-cap-as-independence step, finite census closure, fixed-local-minor assertion, or perturbative deletion is used.

Continuity is not claimed here.  The result is an essential-density theorem for the explicit family plus a rigorous counterexample to a proposed reduction mechanism.  Full QFORM remains OPEN / NOT PROVED / NOT DISPROVED.
