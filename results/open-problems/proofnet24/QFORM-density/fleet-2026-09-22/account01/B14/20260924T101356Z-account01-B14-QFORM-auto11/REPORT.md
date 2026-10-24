SIGNED IN - working on the quadratic-form bounded-density conjecture (universal constant), account account01, slot B14, 2026-09-24T10:13:56Z.
attacking: finite-fragment dense extreme localization — prove bounded finite unions are dense in the partner's environment-coupled extreme class with exact constant preservation, then apply it to a strict three-eigenvalue quadratic inequality.

# B14 report: finite-fragment dense extreme localization

Status: `SUPPORTING_LOCALIZATION_THEOREM_PROVED / FULL_QFORM_OPEN`. Continuity of the unrestricted output density remains separate.

## 1. Result

Let

\[
\mathcal K=\{f:\mathbb R\to[0,1]\text{ measurable}:\int f=1\},
\]

let \(\mathcal E_1\) be all measurable \(E\subset\mathbb R\) with \(|E|=1\), and let \(\mathcal F_1\subset\mathcal E_1\) consist of sets which are bounded finite unions of intervals. The newest completed account02/B14 result `QFORM-ENVIRONMENT-COUPLED-BATHTUB-LOCALIZATION-v1` proves, for every finite positive measure space \((\Omega,\tau)\) of mass \(m\) and measurable \(H:\Omega\times\mathbb R^r\to[0,1]\),

\[
T_H(f_1,\dots,f_r):=\int_\Omega\int_{\mathbb R^r}H(\omega,x)\prod_{j=1}^r f_j(x_j)\,dx\,d\tau(\omega),
\]

\[
\sup_{f_1,\dots,f_r\in\mathcal K}T_H(f_1,\dots,f_r)
=
\sup_{E_1,\dots,E_r\in\mathcal E_1}T_H(1_{E_1},\dots,1_{E_r}).
\tag{1.1}
\]

The new observation is that the right side can be restricted, with **no change of constant**, to bounded finite unions:

\[
\boxed{
\sup_{f_1,\dots,f_r\in\mathcal K}T_H(f_1,\dots,f_r)
=
\sup_{F_1,\dots,F_r\in\mathcal F_1}T_H(1_{F_1},\dots,1_{F_r}).
}
\tag{1.2}
\]

No uniform bound on the number of intervals, support diameter, location of the intervals, or moments is asserted or needed. Those parameters may diverge along the approximating sequence.

I call (1.2) `QFORM-FINITE-FRAGMENT-DENSE-EXTREME-LOCALIZATION-v1`.

## 2. Exact-mass finite-union approximation lemma

**Lemma.** For every \(E\in\mathcal E_1\) and every \(\varepsilon>0\), there exists \(F\in\mathcal F_1\) such that

\[
|E\triangle F|<\varepsilon.
\tag{2.1}
\]

**Proof.** Choose \(R\) so that \(|E\setminus[-R,R]|<\delta\). By regularity of Lebesgue measure, approximate \(E\cap[-R,R]\) in symmetric difference by a finite union \(G\) of bounded intervals so that

\[
|E\triangle G|<2\delta.
\]

Then

\[
\big||G|-1\big|\le |E\triangle G|<2\delta.
\tag{2.2}
\]

If \(|G|>1\), trim total interval length \(|G|-1\) from the finitely many component intervals. If \(|G|<1\), add one bounded interval disjoint from \(G\) of length \(1-|G|\). The resulting bounded finite union \(F\) has \(|F|=1\), and

\[
|E\triangle F|
\le |E\triangle G|+|G\triangle F|
=|E\triangle G|+\big||G|-1\big|
<4\delta.
\]

Take \(\delta<\varepsilon/4\). \(\square\)

This is only a density statement. It does not contradict the live corrections ruling out a universal bounded-diameter reduction or a universal fixed fragment-count reduction.

## 3. Stability of the environment functional

For arbitrary unit-measure sets \(E_j,F_j\), the elementary product telescoping identity and \(0\le H\le1\) give

\[
\begin{aligned}
&\left|T_H(1_{E_1},\dots,1_{E_r})-T_H(1_{F_1},\dots,1_{F_r})\right|\\
&\qquad\le
m\sum_{j=1}^r |E_j\triangle F_j|.
\end{aligned}
\tag{3.1}
\]

Indeed, replace the indicators one coordinate at a time; all untouched indicator factors have integral one, and the changed factor contributes its \(L^1\) distance. Applying the lemma simultaneously to every \(E_j\) proves that the supremum over \(\mathcal E_1^r\) equals the supremum over \(\mathcal F_1^r\). Combining with the completed account02/B14 identity (1.1) proves (1.2).

Two features are important for QFORM. First, the approximating sets are deterministic and chosen only after the partner theorem has averaged over the entire conditioning environment; no environment-dependent active law is introduced. Second, the estimate is exactly linear in the true environment mass \(m\), so arbitrary positive outside fragmentation is still zero-tax.

## 4. Full-target concentration-constant equivalence

For a finite Borel measure \(\mu\) on \(\mathbb R\), define

\[
D(\mu):=\sup_{I}\frac{\mu(I)}{|I|},
\tag{4.1}
\]

where the supremum runs over bounded intervals of positive length. If \(D(\mu)<\infty\), the interval inequality extends by regularity to all Borel sets, so \(\mu\ll dx\) and its Radon--Nikodym derivative satisfies \(\|d\mu/dx\|_{\infty,\mathrm{ess}}\le D(\mu)\). Conversely, a density cap \(C\) gives \(D(\mu)\le C\). Thus \(D\) is exactly the relevant essential density-height functional, allowing the value \(+\infty\).

Fix any dimension \(n\) and any real symmetric matrix \(A\). For each interval \(I\), take \(\Omega\) to be a one-point environment and

\[
H_I(x)=1_{\{x^TAx\in I\}}.
\]

Equation (1.2) yields

\[
\sup_{f_1,\dots,f_n\in\mathcal K}
\Pr_f\{X^TAX\in I\}
=
\sup_{F_1,\dots,F_n\in\mathcal F_1}
\Pr_F\{X^TAX\in I\}.
\tag{4.2}
\]

Taking the supremum over intervals and using that the two suprema commute gives the exact identity

\[
\boxed{
\sup_{f_1,\dots,f_n\in\mathcal K}
D(\mathcal L_f(X^TAX))
=
\sup_{F_1,\dots,F_n\in\mathcal F_1}
D(\mathcal L_F(X^TAX)).
}
\tag{4.3}
\]

Consequently, after also taking the supremum over all target matrices \(A\) with at least three eigenvalues of modulus at least one and over all \(n\), the optimal universal QFORM density constant is **exactly unchanged** if every input density is restricted to an indicator of a bounded finite union of intervals of total length one.

This is a localization equivalence for the complete arbitrary-dimensional, rotated, indefinite target. It removes unbounded support and absence of moments as separate limiting obstructions: every universal estimate uniform in finite-union complexity automatically extends with the identical constant. What it does **not** do is provide such a uniform estimate.

## 5. Translation and outside-conditioning corollary

Let \(B\) be a fixed symmetric \(r\times r\) active block, \(\tau\) any finite positive outside/environment measure, and \(b(\omega),c(\omega)\) arbitrary measurable affine fields. For a bounded interval \(I\), put

\[
H_I(\omega,x)
=1_{\{x^TBx+b(\omega)^Tx+c(\omega)\in I\}}.
\]

Then (1.2) says exactly

\[
\boxed{
\sup_{f_j\in\mathcal K}
\int \Pr_f\{x^TBx+b(\omega)^Tx+c(\omega)\in I\}\,d\tau(\omega)
=
\sup_{F_j\in\mathcal F_1}
\int \Pr_F\{\cdots\in I\}\,d\tau(\omega).
}
\tag{5.1}
\]

Therefore conditioning-generated translations, arbitrarily distant outside fragments, unbounded outside support, arbitrary outside quadratic curvature, and absence of outside moments do not change the localization constant. If \(\tau\) is replaced by a positive submeasure of mass \(m\), both sides scale by exactly \(m\).

A proof may thus first establish a receiver uniformly for bounded finite-union active laws, provided its bound is independent of their number of components, diameter, and locations, and then pass to all cap-one laws without loss.

## 6. Completed partner result applied to an actual strict-target inequality

Let

\[
B_*=I_3-\frac23\mathbf 1\mathbf 1^T
=
\begin{pmatrix}
1/3&-2/3&-2/3\\
-2/3&1/3&-2/3\\
-2/3&-2/3&1/3
\end{pmatrix}.
\]

Its spectrum is exactly \(\{1,1,-1\}\). For an arbitrary real \(3\times m\) matrix \(C\) and arbitrary symmetric \(m\times m\) matrix \(D\), set

\[
A=\begin{pmatrix}B_*&C\\C^T&D\end{pmatrix}.
\tag{6.1}
\]

By Cauchy interlacing, \(A\) has at least two eigenvalues \(\ge1\) and at least one eigenvalue \(\le-1\), so (6.1) lies in the owner's exact three-large-eigenvalue target for every \(C,D\).

Write the original independent variables as \((X,Z)\), with \(X\in\mathbb R^3\). Conditioning only on the outside original coordinates gives

\[
Q\mid Z=z
=X^TB_*X+(2Cz)^TX+z^TDz.
\tag{6.2}
\]

Now apply the completed account02/B14 environment-coupled theorem to the interval event in (6.2), and then apply the new finite-union closure (1.2). It is enough, with exactly the same interval constant, to consider active laws \(1_{F_1},1_{F_2},1_{F_3}\) with \(F_j\in\mathcal F_1\), despite the arbitrary affine field \(2Cz\) and arbitrary outside law.

The verified fixed-source three-dimensional Theorem A at `yspennstate/math-open-problems@e5f71d79eff325201dd0274053d20268ce65b837` applies to every such active law and arbitrary linear terms. Since every eigenvalue of \(B_*\) has modulus one,

\[
\Pr\{Q\in I\}\le 6\sqrt\pi\,|I|
\tag{6.3}
\]

for every bounded interval \(I\). Therefore

\[
\boxed{
\|p_Q\|_{\infty,\mathrm{ess}}
\le 6\sqrt\pi
=10.634723105433096\ldots
}
\tag{6.4}
\]

uniformly in \(m,C,D\), all independent cap-one input laws, all conditioning-generated translations, all fragment locations, and all support/moment behavior. This is an actual rotated/indefinite strict-target inequality using the designated partner theorem at the concentration-function step.

## 7. Scope and remaining implication

The unrestricted QFORM theorem remains open. The new lemma changes the localization endpoint from arbitrary measurable unit-measure sets to bounded finite unions **without changing the optimal constant**, but with completely uncontrolled complexity. It therefore does not contradict either of the live corrections:

- `QFORM-BOUNDED-DIAMETER-LOCALIZATION-FALSE`: a fixed diameter cannot preserve the exact target concentration problem;
- `QFORM-NO-UNIFORM-FRAGMENT-COUNT-BATHTUB-v1`: no universal finite fragment count preserves the exact coordinatewise optimum.

The first unpaid implication is now sharper:

`QFORM-FINITE-FRAGMENT-WHOLELAW-RECEIVER-UNIFORM-IN-COMPLEXITY-v1` — prove, from the bare spectral condition \(s_3(A)\ge1\), a product-preserving whole-law receiver whose interval bound is uniform over every bounded finite-union extreme input, with no dependence on fragment count, support diameter, or fragment locations; or route every matrix into another already completed whole-active chamber.

This is strictly a structural/analytic gap. Unbounded support and lack of moments themselves no longer require an additional localization loss.

## Source discipline

Fresh control was resolved on `yspennstate/math-research-brain` main, including control revision `2026-09-22.15`; no later owner/platform stop was observed before this write. The live correction inbox was re-read immediately before publication.

Designated partner actually consumed and applied: account02/B14 run `20260924T095839Z-account02-B14-QFORM-auto11`, canonical math commit `72f8e6c6b826f7e849a879534a7835aaa8b9f2a4`, result `QFORM-ENVIRONMENT-COUPLED-BATHTUB-LOCALIZATION-v1`.

Fixed-source theorem actually checked: `yspennstate/math-open-problems@e5f71d79eff325201dd0274053d20268ce65b837`, Theorem A with arbitrary linear terms and the n=3 constant `6 sqrt(pi)/sigma`.

Execution remains `WITHOUT_VERIFIED_BRAIN`: authenticated repository retrieval and readback are real, but no genuine native learned-memory receiver use was established. No schedule, enabled/quiet state, identity, notification, email/push, task, cross-account authentication, paid/remote call, public release, or permission change was made.
