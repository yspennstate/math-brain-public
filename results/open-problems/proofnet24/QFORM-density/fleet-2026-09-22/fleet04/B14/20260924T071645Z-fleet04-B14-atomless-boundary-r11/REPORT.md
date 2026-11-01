# B14 report: atomless moving boundaries regularize ruled one-sheet mixtures

SIGNED IN — account=fleet04 slot=B14 actual_utc=20260924T071645Z run=20260924T071645Z-fleet04-B14-atomless-boundary-r11.

## Status

The full quadratic-form bounded-density conjecture remains open. This run proves a new regularity mechanism for the ruled one-sheet branch: a conditioning-generated translation may vary arbitrarily with the conditioned variables and the conditional density family may vary with it; if the random sheet boundary is atomless, the mixed one-sided density is globally continuous and vanishes at infinity. No support, moment, smoothness, interval-extremality, or post-rotation independence hypothesis is used.

The mechanism also gives a concrete next inequality in the original target class while preserving the exact physical-fiber localization estimate.

## 1. Atomless moving-boundary theorem

Let \((\Omega,\pi)\) be a probability space. Let \(b:\Omega\to\mathbb R\) be measurable and atomless:
\[
 \pi\{b=t\}=0\qquad(t\in\mathbb R).
\]
For \(\pi\)-a.e. \(\omega\), let \(h_\omega:[0,\infty)\to\mathbb R\) be continuous, vanish at \(+\infty\), and satisfy
\[
 0\le h_\omega(s)\le M.
\]
Assume only that \((\omega,s)\mapsto h_\omega(s)\) is jointly measurable. Define
\[
 H(t):=\int_\Omega {\bf1}_{\{t\ge b(\omega)\}}
 h_\omega\bigl(t-b(\omega)\bigr)\,d\pi(\omega).
\]

Then
\[
 \boxed{H\in C_0(\mathbb R),\qquad 0\le H\le M.}
\]

In particular, the conditional family \(h_\omega\) need not be independent of \(b\), constant in \(\omega\), or uniformly equicontinuous.

### Proof

The height estimate is immediate. Let \(t_n\to t\). For every \(\omega\) with \(b(\omega)\ne t\), eventually the indicators
\({\bf1}_{\{t_n\ge b(\omega)\}}\) and \({\bf1}_{\{t\ge b(\omega)\}}\) agree, and continuity of \(h_\omega\) gives pointwise convergence of the integrands. The exceptional set \(\{b=t\}\) is null. Dominated convergence, with dominating function \(M\), proves \(H(t_n)\to H(t)\).

As \(t\to-\infty\),
\[
 0\le H(t)\le M\,\pi\{b\le t\}\longrightarrow0.
\]
For \(t\to+\infty\), choose \(R\) so that \(\pi\{|b|>R\}<\varepsilon/M\). On \(\{|b|\le R\}\), \(t-b(\omega)\to+\infty\) and hence \(h_\omega(t-b(\omega))\to0\); dominated convergence makes that part tend to zero. The complement contributes at most \(\varepsilon\). Thus \(H(t)\to0\).

The theorem repairs the exact discontinuity that zero-extension can create at a deterministic one-sided boundary: atomless random translation removes the boundary jump after mixing.

## 2. Finite-mixture and rough-law compatibility

If \(\pi=\sum_{j=1}^N\alpha_j\pi_j\), then
\[
 H=\sum_{j=1}^N\alpha_j H_j,\qquad
 \|H\|_\infty\le\sum_j\alpha_j\|H_j\|_\infty\le M.
\]
Thus every finite purification/mixture reduction preserves both the interval constant and the moving-boundary conclusion. Passing from finite mixtures to arbitrary cap-one product densities uses monotone/simple approximation at the measure level; the proof above evaluates only the canonical conditional densities supplied by the ruled theorem, never an arbitrary representative of the final rough density.

## 3. Actual target-class inequality

Let
\[
 B_*:=I_3-\frac23{\bf1}{\bf1}^{T},\qquad B_*^2=I_3,
\]
so \(\operatorname{spec}(B_*)=\{1,1,-1\}\). Let \(U=(X_1,X_2,X_3)\), and let \(V,W\) be further independent cap-one variables. Put
\[
 Q=U^TB_*U+2VW.
\]
The matrix \(\operatorname{diag}(B_*,\begin{psmallmatrix}0&1\\1&0\end{psmallmatrix})\) has five eigenvalues of modulus one, so this is an honest member of the full conjecture's class.

Apply the completed fleet01/B14 physical-fiber theorem QFORM-SCHUR-COMPLETE-SQUARE-ZERO-TAX-LOCALIZATION-v1 (commit be9d93b288079c9261fea04074bac234974da89c) to the actual principal block \(B_*\), whose least absolute eigenvalue is one. For every interval \(I\),
\[
 \boxed{\Pr(Q\in I)\le6\sqrt\pi\,|I|,\qquad
 \|p_Q\|_{\infty,\mathrm{ess}}\le6\sqrt\pi.}
\]
The term \(2VW\) is retained exactly as a conditioning-generated translation; it is not bounded, truncated, or declared a small quadratic error.

Now isolate the majority one-sheet submeasure
\[
 \nu_+(E):=\Pr\{Q\in E,\ U^TB_*U\ge0\}.
\]
The ruled one-sheet theorem gives the unshifted majority-sheet density
\[
 h_+\in C_0([0,\infty)),\qquad \|h_+\|_\infty\le\pi\sqrt2.
\]
The random boundary \(b=2VW\) is atomless. Indeed \(V=0\) has probability zero, and conditioning on \(V=v\ne0\),
\[
 \Pr(2vW=t\mid V=v)=0
\]
because \(W\) has a density. Therefore the moving-boundary theorem yields
\[
 p_{\nu_+}(t)=\mathbb E\!\left[
 {\bf1}_{\{t\ge2VW\}}h_+(t-2VW)\right],
\]
and hence the new global conclusion
\[
 \boxed{p_{\nu_+}\in C_0(\mathbb R),\qquad
 \|p_{\nu_+}\|_\infty\le\pi\sqrt2.}
\]

More generally, the same conclusion holds after conditioning when the ruled density becomes \(h_\omega\) and is arbitrarily dependent on its affine boundary \(b(\omega)\); only the uniform ruled height and atomlessness of that boundary are used. This is the point needed for conditioning-generated translations and kernel leakage.

## 4. Scope and remaining obstruction

This does not turn a half-line estimate into a full rank-three proof. It regularizes the majority one-sheet contribution. The minority/two-sheet contribution can still have a deterministic boundary singularity, and atomlessness is not automatic for an arbitrary quadratic or affine boundary generated by the outside coordinates. The full bounded-density conjecture therefore remains open.

The next sharp problem is to prove either:

1. an atomless-boundary decomposition with a uniform ruled bound for every localized physical fiber; or
2. a companion two-sheet mixture estimate that pays for any boundary atoms without moment or support assumptions.

## Source pins

- Required Claude source baseline: math-open-problems@e5f71d79eff325201dd0274053d20268ce65b837, proofnet24/QFORM-density/interactive/20260922T211500Z-decoupling-brascamp-lieb/.
- Completed fleet01/B14 theorem: math-open-problems@be9d93b288079c9261fea04074bac234974da89c.
- Previous fleet04/B14 localization report: math-open-problems@deb713bc8e6df3f7e0ac5398e8cccbf00d1e7513.
- Prior Claude-review corrections retained: no post-rotation independence, no arbitrary-joint coarea inference, no deletion of small dense quadratic tails, and no promotion of a half-line estimate to a full density theorem.
