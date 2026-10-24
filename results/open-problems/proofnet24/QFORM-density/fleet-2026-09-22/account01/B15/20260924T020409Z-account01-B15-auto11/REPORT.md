SIGNED IN - working on the quadratic-form bounded-density conjecture (universal constant), account account01, slot B15, 2026-09-24T02:04:09Z.
attacking: target-level regularity at the borderline between bounded density and continuity, and a rough-law stability/compactness principle strong enough to use account02/B15's completed semidefinite-Schur receiver at an actual inequality.

# account01/B15 — same-height independent-smoothing compiler and the sharp rank-two-to-rank-three regularity transition

Programme: `QFORM-DENSITY-3EIG-20260922`, revision `2026-09-22.5`.  
Run: `20260924T020409Z-account01-B15-auto11`.  
Status: `NEW_SAME_HEIGHT_C0_COMPILER / SHARP_REGULARITY_TRANSITION / PARTNER_APPLIED / FULL_QFORM_OPEN`.  
Execution: `WITHOUT_VERIFIED_BRAIN`.

The unrestricted owner target remains OPEN:

\[
\sup_{\substack{n\ge3,\ s_3(A)\ge1\\ X_i\text{ independent},\ 0\le f_i\le1}}
\|p_{X^TAX}\|_\infty<\infty.
\]

This report isolates a target-level regularity mechanism that is exact in constant and uses only genuine independence of disjoint ORIGINAL-coordinate blocks. It also computes an explicit target-valid example showing that the passage from a bounded but discontinuous rank-two semidefinite output to rank three can create exactly a square-root boundary cusp: continuity is gained, but Lipschitz (and every Hölder exponent greater than `1/2`) can still fail.

## 1. Sources, partner result, and correction boundary

Fresh owner controls and the live QFORM state were reread before this run. The full conjecture is still `OPEN`. The live corrections are preserved: no law-uniform pointwise quadratic Fourier decay, no independence after spectral rotation, no arbitrary-joint three-dimensional coarea height theorem, no projection-only/two-sheet X-ray closure, and no conditional cap shortcut.

The designated partner result used below is the completed account02/B15 report

`yspennstate/math-open-problems@1353b3eb430da4be2e43bdc37e5de9ab1a1d5d4e`,

`proofnet24/QFORM-density/fleet-2026-09-22/account02/B15/20260924T011547Z-account02-B15-qform-auto11/REPORT.md`.

Its rank-two semidefinite projection theorem is:

> If `S` is a semidefinite rank-two symmetric matrix on an ORIGINAL-coordinate product bank, with nonzero eigenvalue magnitudes `sigma_1,sigma_2`, then for `R=Z^T S Z`,
> \[
> \boxed{\|p_R\|_\infty\le {2\pi\over\sqrt{|\sigma_1\sigma_2|}}.}
> \tag{1.1}
> \]
> The proof uses the two-dimensional orthogonal-projection density cap `<=2`; it does not assert independence of the projected spectral coordinates.

The same source shows that, when this semidefinite rank-two remainder is coupled to an indefinite physical pair, a more complicated pair-logarithmic compiler gives a valid full-output estimate. Here I identify the important simpler endpoint when the two blocks are genuinely independent in the original coordinates.

## 2. Absolute continuity remains qualitatively much easier than boundedness

For completeness, the exact qualitative baseline is:

### Lemma 2.1 — nonzero quadratic pushforwards are absolutely continuous

Let `W` have an absolutely continuous law on `R^d` and let `B` be a nonzero real symmetric matrix. Then

\[
H=W^T B W
\]

has an absolutely continuous law.

One proof is coarea. The critical set of `q(w)=w^T B w` is `ker B`, a proper linear subspace and therefore Lebesgue-null. If `N subset R` is Lebesgue-null, the coarea formula gives

\[
\int_{q^{-1}(N)}|\nabla q(w)|\,dw=0.
\]

Away from `ker B`, `|\nabla q|=2|Bw|>0`; hence `q^{-1}(N)` is null. Since `W` has a density, `P(H in N)=0`.

For product inputs one can equivalently condition on one ORIGINAL coordinate. No cap-one hypothesis and no rank-three hypothesis are needed for this qualitative statement. It supplies no universal `L^infinity` bound.

## 3. Same-height independent-smoothing compiler

The following is the main regularity lemma of this run.

### Theorem 3.1 — `QFORM-B15-INDEPENDENT-SMOOTHING-C0-SAME-HEIGHT-v1`

Let `R` and `H` be independent real random variables. Assume

1. `R` has a probability density `f in L^1 cap L^infinity` with
   \[
   \|f\|_\infty\le K;
   \]
2. `H` is absolutely continuous, with probability density `g in L^1`.

Then `T=R+H` has a density

\[
p_T=f*g
\]

satisfying

\[
\boxed{p_T\in C_0(R),\qquad \|p_T\|_\infty\le K.}
\tag{3.1}
\]

Thus an independent absolutely continuous smoothing block upgrades bounded density to continuous density with **zero loss in the already-paid height constant**.

More quantitatively, for every translation `h in R`,

\[
\boxed{
\|p_T(\cdot+h)-p_T\|_\infty
\le K\,\|g(\cdot+h)-g\|_1.
}
\tag{3.2}
\]

Since translations are continuous in `L^1`, the right side tends to zero as `h->0`.

### Proof

Young's inequality gives immediately

\[
\|f*g\|_\infty\le\|f\|_\infty\|g\|_1\le K.
\]

Using commutativity of convolution,

\[
\tau_h(f*g)-f*g=f*(\tau_hg-g),
\]

so another Young inequality gives (3.2). Hence `p_T` has a uniformly continuous representative.

Also `p_T in L^1` with integral one. A uniformly continuous `L^1` function vanishes at infinity: otherwise some `epsilon>0` and a sequence `|x_j|->infinity` would satisfy `|p_T(x_j)|>=epsilon`; uniform continuity would then produce disjoint intervals on which `|p_T|>=epsilon/2`, contradicting integrability. Therefore `p_T in C_0`. QED.

### Important scope point

This theorem does **not** manufacture independence by diagonalizing a matrix. It applies only when the two summands depend on disjoint ORIGINAL-coordinate blocks (or are otherwise genuinely independent). This is exactly why it is safe under the live `QFORM-NO-INDEPENDENCE-AFTER-ROTATION` correction.

## 4. Product-preserving block-diagonal target theorem

The partner's semidefinite rank-two result combines with Theorem 3.1 to give a useful exact QFORM chamber.

### Theorem 4.1 — `QFORM-B15-SEMI2-BLOCK-C0-v1`

Split the independent original coordinates into two disjoint nonempty banks `Z` and `W`, and let

\[
A=S\oplus B,
\]

where

- `S` is semidefinite of rank exactly two on the `Z` bank, with nonzero eigenvalue magnitudes `sigma_1,sigma_2`;
- `B != 0` is an arbitrary symmetric matrix on the disjoint `W` bank.

Then, for arbitrary cap-one product marginals,

\[
Q=Z^T S Z+W^T B W
\]

has a density satisfying

\[
\boxed{
 p_Q\in C_0(R),\qquad
 \|p_Q\|_\infty
 \le {2\pi\over\sqrt{|\sigma_1\sigma_2|}}.
}
\tag{4.1}
\]

If `|sigma_1|,|sigma_2|>=1`, then simply

\[
\boxed{\|p_Q\|_\infty\le2\pi.}
\tag{4.2}
\]

If the `B` block supplies a third eigenvalue of modulus at least one, (4.2) is a genuine full-target result.

### Proof

By the completed account02/B15 theorem, the semidefinite rank-two output

\[
R=Z^TSZ
\]

has density bounded by the right side of (4.1). Since `B!=0` and the `W` bank has an absolutely continuous product law, Lemma 2.1 gives a probability density for

\[
H=W^T B W.
\]

The two outputs are independent because they use disjoint ORIGINAL-coordinate banks. Theorem 3.1 gives (4.1) with the identical height constant. QED.

This is a precise separation of the two tasks: the height is paid entirely by the rank-two semidefinite block, while the independent nonconstant block is used only to upgrade the representative to `C_0`.

## 5. Partner theorem applied to an actual target inequality

Let `Z=(Z_1,...,Z_m)` be an arbitrary cap-one product bank and let `r,s in R^m` be orthonormal. Let `X,Y` be two further independent cap-one variables, independent of `Z`. Put

\[
R=(r\cdot Z)^2+(s\cdot Z)^2,
\qquad
H=2XY,
\qquad
Q=H+R.
\tag{5.1}
\]

The coefficient matrix has nonzero spectrum

\[
\{1,-1,1,1\},
\]

so this is an owner-target family for every `m` and every orientation of the diffuse plane `span{r,s}`.

The partner theorem (1.1), with `sigma_1=sigma_2=1`, gives the actual inequality

\[
\boxed{\|p_R\|_\infty\le2\pi.}
\tag{5.2}
\]

No independence between `r dot Z` and `s dot Z` is used.

The bilinear variable `H=2XY` is absolutely continuous. Indeed, if `N` is null, then for every `x!=0` the set

\[
\{y:2xy\in N\}=N/(2x)
\]

is null, while `P(X=0)=0`; Fubini gives `P(2XY in N)=0`.

Because `H` and `R` depend on disjoint original-coordinate banks, Theorem 3.1 yields

\[
\boxed{
 p_Q\in C_0(R),\qquad
 \|p_Q\|_\infty\le2\pi.
}
\tag{5.3}
\]

This sharpens the partner report's valid general pair-log estimate on the same block-independent family,

\[
\|p_Q\|_\infty\le3+\log(16\pi)=6.917318\ldots,
\]

to the simpler

\[
2\pi=6.283185\ldots.
\]

The improvement is not a contradiction: the partner pair-log mechanism was designed to survive arbitrary cross-coupling. Here `B=0` between the two original-coordinate blocks, so genuine independence allows the stronger same-height convolution step.

If the active semidefinite bank consists of exactly two ORIGINAL coordinates, the partner source notes that the two-dimensional joint cap is `1`, so the semidefinite bound is `pi/sqrt(P)` rather than `2pi/sqrt(P)`. In particular, for arbitrary independent cap-one `X,Y,Z_1,Z_2`,

\[
\boxed{
Q=2XY+Z_1^2+Z_2^2
\quad\Longrightarrow\quad
p_Q\in C_0(R),\quad \|p_Q\|_\infty\le\pi.
}
\tag{5.4}
\]

Again the continuity comes after the height certificate and costs nothing.

## 6. Exact sharp rank-two endpoint from this run

The early calculation in this run shows that the constant `2pi` in the partner's general semidefinite rank-two theorem is itself sharp before the extra independent smoothing block is added.

Let `X_1,...,X_4` be iid `Unif[-1/2,1/2]`, and set

\[
Y_1={X_1+X_2\over\sqrt2},\qquad
Y_2={X_3+X_4\over\sqrt2},\qquad
R=Y_1^2+Y_2^2.
\tag{6.1}
\]

The matrix of `R` in the original coordinates is

\[
S_0={1\over2}\begin{pmatrix}1&1\\1&1\end{pmatrix}
\oplus
{1\over2}\begin{pmatrix}1&1\\1&1\end{pmatrix},
\]

which is positive semidefinite of rank two with nonzero eigenvalues `1,1`.

Each `Y_j` has the triangular density

\[
g(y)=\sqrt2(1-\sqrt2|y|)\mathbf 1_{|y|\le1/\sqrt2}.
\]

For `0<t<1/2`, the full circle of radius `sqrt(t)` lies in the support square, and polar coarea gives

\[
p_R(t)={1\over2}\int_0^{2\pi}
 g(\sqrt t\cos\theta)g(\sqrt t\sin\theta)\,d\theta.
\]

Using

\[
\int_0^{2\pi}(|\cos\theta|+|\sin\theta|)d\theta=8,
\qquad
\int_0^{2\pi}|\sin\theta\cos\theta|d\theta=2,
\]

one obtains exactly

\[
\boxed{
 p_R(t)=2\pi-8\sqrt{2t}+4t,
 \qquad 0<t<1/2.
}
\tag{6.2}
\]

Hence

\[
\boxed{\|p_R\|_{\infty,\mathrm{ess}}=2\pi.}
\tag{6.3}
\]

Moreover `p_R=0` a.e. for `t<0`, while `p_R(t)->2pi` as `t downarrow0`; therefore no continuous density representative exists. This is a sharp bounded-but-discontinuous rank-two semidefinite endpoint.

## 7. Adding one independent square: exact target-valid square-root cusp

Now add a fifth independent variable

\[
V\sim\mathrm{Unif}[-1/2,1/2]
\]

and define

\[
T=R+V^2.
\tag{7.1}
\]

The ORIGINAL-coordinate matrix is

\[
A_*=S_0\oplus[1],
\]

whose nonzero spectrum is exactly

\[
\{1,1,1\}.
\]

Thus `T` is a literal exact-rank-three instance of the owner target.

The square `V^2` has probability density

\[
h(s)=s^{-1/2}\mathbf1_{(0,1/4)}(s).
\tag{7.2}
\]

By Theorem 3.1 and (6.3), immediately

\[
\boxed{p_T\in C_0(R),\qquad \|p_T\|_\infty\le2\pi.}
\tag{7.3}
\]

Here the regularity can be calculated exactly at the lower support edge. For `0<t<1/4`, both `s` and `t-s` remain in the ranges where (6.2) and (7.2) apply, so

\[
\begin{aligned}
p_T(t)
&=\int_0^t
\left(2\pi-8\sqrt{2(t-s)}+4(t-s)\right)s^{-1/2}\,ds\\
&=4\pi\sqrt t
 -4\pi\sqrt2\,t
 +{16\over3}t^{3/2}.
\end{aligned}
\tag{7.4}
\]

The beta integrals used are

\[
\int_0^t s^{-1/2}ds=2\sqrt t,
\]

\[
\int_0^t(t-s)^{1/2}s^{-1/2}ds
=t\,B(1/2,3/2)={\pi\over2}t,
\]

and

\[
\int_0^t(t-s)s^{-1/2}ds
=t^{3/2}B(1/2,2)={4\over3}t^{3/2}.
\]

Since `p_T(t)=0` for `t<0`, (7.4) shows

\[
\boxed{
 p_T(t)=4\pi\sqrt t+O(t)
 \quad(t\downarrow0).
}
\tag{7.5}
\]

Consequences:

- `p_T` is continuous at the quadratic boundary, exactly as the rank-three qualitative theorem predicts;
- it is not locally Lipschitz at `0`;
- more strongly, for every `alpha>1/2`,
  \[
  \lim_{t\downarrow0}{|p_T(t)-p_T(0)|\over t^\alpha}=\infty,
  \]
  so this single target-valid cap-one product instance has no local `C^{0,alpha}` regularity at the boundary for any `alpha>1/2`;
- at the endpoint `alpha=1/2`,
  \[
  \lim_{t\downarrow0}{p_T(t)\over\sqrt t}=4\pi.
  \]

Thus rank three is enough for `C_0`, but even in a positive-semidefinite exact-rank-three uniform example one cannot strengthen the qualitative target to a blanket Lipschitz or `C^{0,alpha}`, `alpha>1/2`, conclusion.

For this particular square smoother, the compiler also has an explicit translation modulus. From (7.2), for `0<=a<=1/4`, direct integration gives

\[
\|h(\cdot+a)-h\|_1=4\sqrt a.
\tag{7.6}
\]

Hence any independent density `f` with `||f||_infinity<=K` satisfies

\[
\boxed{
\|(f*h)(\cdot+a)-f*h\|_\infty
\le4K\sqrt{|a|},\qquad |a|\le1/4.
}
\tag{7.7}
\]

For the present `K=2pi`, this gives the safe global local modulus `<=8pi sqrt{|a|}`; the exact boundary asymptotic (7.5) shows the true leading coefficient at zero is `4pi`.

## 8. What this settles and what remains unpaid

The regularity hierarchy is now especially transparent in a product-preserving chamber:

1. **Absolute continuity:** already holds for every nonzero quadratic matrix under an absolutely continuous input law; no rank-three or cap hypothesis is needed.
2. **Bounded density:** rank two semidefinite is already enough, with the partner's sharp orientation-free constant `2pi/sqrt(P)`, but continuity can fail sharply at the support boundary.
3. **Continuous density:** adding any independent nonconstant quadratic block gives `C_0` with **exactly the same previously paid height constant**. In the target block-diagonal chamber with two same-sign large curvatures, this yields the universal bound `2pi`.
4. **Higher regularity:** even exact-rank-three cap-one target instances can have a square-root cusp, so Lipschitz and all Hölder exponents above `1/2` fail in general.

The full QFORM conjecture remains open because a general symmetric matrix is not block diagonal in the original independent coordinates. Cross-couplings destroy the genuine independence used in Theorem 3.1; a spectral rotation cannot be substituted. The remaining global step is therefore structural: aggregate or reorganize those cross-couplings in the original product coordinates until a paid bounded-density resource can be combined with a genuine smoothing resource without taking a prohibited worst-fiber or projection-only shortcut.

No pointwise quadratic Fourier decay, post-rotation independence, arbitrary-joint coarea height estimate, or two-sheet X-ray-only argument is used anywhere in this report.