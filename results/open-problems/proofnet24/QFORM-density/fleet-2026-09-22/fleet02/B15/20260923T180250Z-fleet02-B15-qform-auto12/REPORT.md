SIGNED IN - working on the quadratic-form bounded-density conjecture (universal constant), account fleet02, slot B15, 2026-09-23T18:02:50Z.
attacking: expected-conditional-height regularity compiler and rough-input bridge; derive a source-valid obstruction to extending the completed Gaussian-mixture branch to arbitrary rough cap-one inputs.

# fleet02/B15 auto12 — Gaussian-mixture BV barrier and corrected ruled rough bridge

Programme: `QFORM-DENSITY-3EIG-20260922`  
Run: `20260923T180250Z-fleet02-B15-qform-auto12`  
Role: absolute continuity and regularity; complementary constructions/source-valid counterexamples.  
Execution context: `WITHOUT_VERIFIED_BRAIN`.  
Status: `NEW SOURCE-VALID APPROXIMATION OBSTRUCTION / RULED ROUGH BRIDGE RECHECKED / FULL QFORM OPEN`.

## 1. First unpaid implication

The central theorem is still

\[
\boxed{
\sup_{\substack{n\ge3,\ s_3(A)\ge1\\ X_i\text{ independent},\ 0\le f_i\le1}}
\|p_{X^TAX}\|_\infty<\infty .}
\tag{1.1}
\]

Equivalently one needs a universal linear small-ball estimate.  Absolute continuity and instancewise continuity are qualitatively different statements and do not pay (1.1).

This run attacks a very specific rough-input completion proposal suggested by the newly completed full-matrix Gaussian-mixture theorem: prove the theorem on Gaussian component mixtures with the cap-compatible inverse-scale budget, approximate arbitrary cap-one marginals weakly by that class, and invoke the completed fleet03/B15 zero-loss weak trace.  The new theorem below proves that the approximation premise is false in a quantitatively strong way, even inside smooth/analytic cap-one sources.

## 2. Sources actually consumed

The owner-pinned Claude source at

`yspennstate/math-open-problems@e5f71d79eff325201dd0274053d20268ce65b837`,
`proofnet24/QFORM-density/interactive/20260922T211500Z-decoupling-brascamp-lieb/`

was read in all three required files `RESULTS.md`, `FOURIER_ROUTE_REPORT.md`, and `COUNTEREXAMPLE_SEARCH.md`.  I use its completed ruled Theorem C below at an actual interval/tent inequality.  I also consumed the current audit/continuation, which records the corrected scope: the one-sheet theorem with an affine term requires that term to lie in the quadratic range.

The designated partner result used in the approximation obstruction is fleet03/B15 auto18,

`yspennstate/math-open-problems@be22adf9f67e9fa02063418c000bc5ee2d2d0c43`,

which proves uniform convergence of unnormalised interval profiles at atomless weak limits and, in particular, zero-loss passage of a previously proved common estimate `mu_m(I)<=C|I|` to the weak limit.  The newer fleet03/B15 auto24 result,

`yspennstate/math-open-problems@2cf10318752f8dd0def28ab14d799e23f381ba10`,

proves the exact heat-height functional and the compiler

\[
H(\mathcal L(Y))\le E\,H(\mathcal L(Y\mid W)).
\tag{2.1}
\]

The Gaussian-mixture theorem being stress-tested is

`yspennstate/math-open-problems@9dabaf2aaf66687c2b4437fdb359b1aeb4a804bc`,
`NEW_GAUSSIAN_MIXTURE_FULL_THEOREM.md`.

It proves the full arbitrary-rank/sign QFORM bound for

\[
X_i=M_i+\sqrt{T_i}G_i,
\qquad E T_i^{-1/2}\le\sqrt{2\pi},
\tag{2.2}
\]

with constant `I_3<3` when `s_3(A)>=1`.  The unrestricted rough-input theorem is explicitly left open there.

## 3. New theorem: the inverse-scale Gaussian-mixture class has a hidden BV bound

Write `sigma=sqrt(T)`.  Let

\[
g(x)=\int \gamma_\sigma(x-m)\,\Pi(dm,d\sigma)
\tag{3.1}
\]

be any Gaussian location-scale mixture, with

\[
K(\Pi):=\int\sigma^{-1}\,d\Pi<\infty.
\tag{3.2}
\]

### Theorem 3.1 — `QFORM-GAUSSIAN-MIXTURE-BV-BARRIER-v1`

Every density (3.1) obeys

\[
\boxed{
\|g\|_\infty\le \frac{K(\Pi)}{\sqrt{2\pi}},
\qquad
\operatorname{Var}(g)\le \sqrt{\frac2\pi}\,K(\Pi).}
\tag{3.3}
\]

Moreover, if Gaussian mixtures `g_m dx` converge weakly to `g dx`, then

\[
\boxed{
\operatorname{Var}(g)
\le \sqrt{\frac2\pi}\liminf_m K(\Pi_m),}
\tag{3.4}
\]

whenever the liminf is finite.  Consequently

\[
\boxed{
\liminf_m K(\Pi_m)
\ge \sqrt{\frac\pi2}\operatorname{Var}(g).}
\tag{3.5}
\]

In particular the cap-compatible class `K<=sqrt(2*pi)` from (2.2) is contained, even after weak closure, in

\[
0\le g\le1,\qquad \operatorname{Var}(g)\le2.
\tag{3.6}
\]

### Proof

For each Gaussian component,

\[
\|\gamma_\sigma\|_\infty=(2\pi)^{-1/2}\sigma^{-1},
\qquad
\|\gamma_\sigma'\|_1=\sqrt{2/\pi}\,\sigma^{-1}.
\]

Tonelli and the triangle inequality give (3.3).

For the weak closure, first take a subsequence on which `K(Pi_m)` converges to the liminf, call the finite limit `K_*`.  The first inequality in (3.3) implies, for every nonnegative `phi in C_c`,

\[
\int\phi\,g\,dx
=\lim_m\int\phi\,g_m\,dx
\le \frac{K_*}{\sqrt{2\pi}}\int\phi,
\]

so the weak limit is absolutely continuous.  For every `phi in C_c^1`,

\[
\left|\int g\phi'\right|
=\lim_m\left|\int g_m\phi'\right|
\le \sqrt{2/\pi}\,K_*\|\phi\|_\infty.
\]

The dual characterization of total variation of the distributional derivative gives (3.4), hence (3.5).  QED.

The point is not merely that narrow Gaussian components can have high peaks.  A fixed inverse-scale budget imposes a **closed regularity constraint on the final marginal itself**, even after arbitrary random centers have been averaged out.

## 4. Smooth and analytic cap-one witnesses force arbitrarily large mixture budget

Fix `N>=2`.  Let

\[
E_N=I_1\cup\cdots\cup I_N
\]

where the `I_j` are disjoint intervals, each of length `1/N`, with positive gaps.  Let `eta_delta` be a nonnegative `C_c^infinity` approximate identity of mass one, with `delta` so small that the `2N` endpoint neighborhoods do not overlap, and set

\[
f_{N,\delta}=1_{E_N}*\eta_\delta.
\tag{4.1}
\]

Then

\[
0\le f_{N,\delta}\le1,
\qquad \int f_{N,\delta}=1,
\qquad f_{N,\delta}\in C_c^\infty,
\]

and, because the signed derivative is the sum of `2N` disjoint translated mollifier profiles,

\[
\boxed{\operatorname{Var}(f_{N,\delta})=2N.}
\tag{4.2}
\]

Therefore every Gaussian-mixture sequence converging weakly to this perfectly smooth admissible marginal must satisfy

\[
\boxed{
\liminf_m E\,T_m^{-1/2}
=\liminf_m K(\Pi_m)
\ge N\sqrt{2\pi}.}
\tag{4.3}
\]

Already `N=2` rules out approximation with the budget `sqrt(2*pi)` in the completed theorem; allowing any other fixed budget does not help because `N` is arbitrary.

The obstruction persists inside strictly positive real-analytic Schwartz cap-one densities.  Replace the compact mollifier in (4.1) by a Gaussian `gamma_delta`.  Then

\[
f_{N,\delta}=1_{E_N}*\gamma_\delta
\]

is strictly positive, real analytic, Schwartz, has mass one and cap at most one.  Since Gaussian convolution is a BV contraction and an approximate identity,

\[
\operatorname{Var}(f_{N,\delta})\to\operatorname{Var}(1_{E_N})=2N
\qquad(\delta\downarrow0)
\tag{4.4}
\]

by BV lower semicontinuity plus the opposite contraction inequality.  Hence for every fixed `K<infinity` one can choose `N` and then `delta` so that this analytic cap-one source lies outside the weak closure of all Gaussian mixtures with inverse-scale budget at most `K`.

Thus neither discontinuity nor compact support is responsible for the failure.

## 5. Application of the completed partner trace theorem: why the Gaussian branch does not close rough QFORM by approximation

Fleet03/B15 auto18 proves the exact useful trace interface: if certified source laws converge weakly to a target product source and their quadratic outputs satisfy one common interval estimate

\[
\Pr(Q_m\in I)\le C|I|,
\tag{5.1}
\]

then the same estimate passes to the target law with zero loss, provided the limiting quadratic is nonconstant.  Therefore, if the class (2.2) were weakly dense in the full cap-one source class, the new full Gaussian-mixture theorem would indeed close the rough-input problem by (5.1).

Theorems 3.1 and 4.1 show that this density premise fails decisively.  Take three independent copies of `f_{N,delta}` and even the fixed target `A=I_3`.  This is an exact QFORM instance.  For every fixed mixture budget `K`, choosing `N` large makes coordinatewise weak approximation by `K`-budget Gaussian mixtures impossible.  Thus the partner trace theorem is **not** the missing step; the obstruction occurs before trace, at the source-class approximation gate.

This is not a QFORM counterexample.  The displayed target is diagonal and has the already-proved universal diagonal bound.  It is a source-valid counterexample only to the proposed theorem-transfer mechanism.

The newer partner compiler (2.1) reaches the same conclusion from another angle.  Averaging genuine conditional output heights is safe; what fails is the attempt to manufacture those conditional certificates by decomposing every rough marginal into Gaussian components whose average inverse scale is uniformly bounded.  Fragmentation can force that source-side certificate to diverge while the actual quadratic output remains perfectly bounded.

## 6. Independent audit of the ruled one-sheet rough-input bridge at the corrected scope

I also rechecked the owner-assigned ruled bridge rather than importing a continuity conclusion.

Let `S` be three **original coordinates**, condition on all others `W`, and suppose the fixed physical block

\[
B=A_{SS}
\]

is invertible with signature `(2,1)`.  Write its eigenvalues as `lambda_1,lambda_2,-mu`, all positive in magnitude, and

\[
\kappa=\min(\lambda_1,\lambda_2,\mu)>0.
\]

Conditionally,

\[
Q_w(x)=x^TBx+2d(w)^Tx+c_0(w)
      =(x+B^{-1}d(w))^TB(x+B^{-1}d(w))+c(w).
\tag{6.1}
\]

The current audit of Claude's Theorem C requires the affine term to lie in `range(B)`.  This condition is automatic here because `B` is invertible; (6.1) removes the affine term by a translation in the original three coordinates.  That translation preserves independence and each density cap.  No independence after diagonalizing `B` is asserted.

For smooth active marginals, the completed ruled theorem gives the majority/one-sheet density constant

\[
C_B
=(\lambda_1\lambda_2\mu)^{-1/2}
\int_0^{2\pi}
\frac{d\theta}{
\sqrt{\sin^2\theta/\lambda_1+
      \cos^2\theta/\lambda_2+1/\mu}}
\le \frac{\pi\sqrt2}{\kappa}.
\tag{6.2}
\]

The two geometric factors that matter are the exact coarea factor `1/2` in the ruling and the reciprocal speed of the non-arclength ruling parameter; together with the two-dimensional product-projection density cap `2` they reproduce (6.2).

For arbitrary rough cap-one active marginals, set `f_i^(eta)=f_i*gamma_eta` **before any rotation**.  Then `f_i^(eta)<=1`, independence is preserved, and

\[
\left\|\prod_{i\in S}f_i^{(\eta)}-\prod_{i\in S}f_i\right\|_1
\le\sum_{i\in S}\|f_i^{(\eta)}-f_i\|_1\to0.
\tag{6.3}
\]

Translations in (6.1) leave these `L^1` errors unchanged, uniformly in `w`.  Deterministic quadratic pushforward and restriction to the majority event contract total variation.  Hence the smooth one-sheet submeasures converge in total variation to the rough one-sheet submeasure, and the interval domination passes with the **same** constant.  Averaging over the untouched outside product law yields

\[
\boxed{
\Pr\{Q\in I,\ Q\ge c(W)\}
\le C_B|I|
\le \frac{\pi\sqrt2}{\kappa}|I|.}
\tag{6.4}
\]

No output continuity is used in this passage.

This applies the required `e5f71d...` completed result to the positive triangular-kernel inequality

\[
\begin{aligned}
&E\big[(\varepsilon-|Q-y|)_+\mathbf1_{\{Q\ge c(W)\}}\big]\\
&\quad=\int_0^\varepsilon
 \Pr\{|Q-y|<t,\ Q\ge c(W)\}\,dt
 \le\int_0^\varepsilon 2C_Bt\,dt
 =C_B\varepsilon^2.
\end{aligned}
\tag{6.5}
\]

Equivalently the Gaussian heat convolution of this positive submeasure is at most `C_B` at every scale and center.  This is a real essential-height payment; it is not inferred from continuity.

For the normalized exact-rank-three physical case `kappa>=1`, (6.4)-(6.5) cost at most `pi*sqrt(2)`.

## 7. Exact implication ledger: absolute continuity, essential boundedness, continuity

The notions remain separate.

### 7.1 Absolute continuity

For every nonconstant quadratic polynomial

\[
q(x)=x^TAx+b^Tx+c
\]

and every absolutely continuous joint input law, `q(X)` is absolutely continuous.  If `N subset R` is null, local coarea on

\[
E_k=\{|x|\le k,\ |\nabla q(x)|\ge1/k\}
\]

gives zero Lebesgue measure for `E_k cap q^{-1}(N)`.  The critical set `{2Ax+b=0}` is empty or a proper affine subspace, hence null; taking the union over `k` proves `q^{-1}(N)` null.  This is qualitative and has no height content.

### 7.2 Essential boundedness

A bound `mu(I)<=C|I|` for every interval is exactly the positive measure domination `mu<=C dx`, hence a density of essential height at most `C`.  Equations (6.4)-(6.5) establish this directly for the ruled majority submeasure.  The unrestricted universal owner bound (1.1) remains open.

Absolute continuity alone does not imply essential boundedness: for `X~Unif[0,1]`, `X^2` has density `1/(2sqrt(t))` on `(0,1)`.

### 7.3 Continuity

Continuity is not needed to pass either the ruled height bound or the partner weak-trace estimate.  Bounded density does not imply a continuous representative in general: `1_[0,1]` is bounded but has no continuous a.e.-equal representative.  Conversely, continuity alone does not impose a universal height: disjoint continuous triangular spikes can have summable areas and unbounded peak heights.

A completed B15 fixed-instance source reports that under the target product hypotheses every **fixed** rank-at-least-three matrix has an instance-dependent bounded `C_0` density.  Accepting that completed theorem, target instances individually enjoy all three properties, but the owner quantifier reversal is still exactly the universal essential-height problem.  A common spatial modulus is unnecessary and, by earlier B15 target-valid constructions, unavailable.

## 8. What changed and the next unpaid implication

Two proof interfaces are now sharply separated.

1. **Weak/rough trace is paid.**  Once a common small-ball bound is genuinely established on an approximating family, fleet03/B15 auto18 passes it to rough limits with zero loss.
2. **Fixed-budget Gaussian-mixture density is false.**  The new BV barrier proves that no fixed inverse-scale budget — not even a larger universal constant — is weakly dense in the arbitrary cap-one source class.  The failure persists for strictly positive analytic Schwartz marginals.

Thus the full proof cannot be completed merely by combining the `<3` Gaussian-mixture theorem with weak approximation.  It needs a product-preserving estimate that exploits separated/fragmented source structure rather than charging each narrow Gaussian component separately, or an expected conditional-output certificate whose expectation remains universal without a source-side inverse-scale budget.

Locally, on an invertible indefinite physical triple, the majority one-sheet term is already paid by (6.4)-(6.5).  The first unpaid geometric contribution there remains the product-provenance-sensitive minority/two-sheet term; the live `QFORM-TWOSHEET-XRAY-ONLY-FALSE` correction forbids replacing it by a generic X-ray norm.  Globally, matrices with no uniformly conditioned physical triple still require the current hub/volume/grouped-coordinate structural glue.

No moment, compact-support, log-concavity, identical-law, diagonal-basis, or post-rotation-independence assumption has been inserted into any positive target statement above.
