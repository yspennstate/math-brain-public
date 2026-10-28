# account03/B03 r22 — volume-marginal weighted Riesz endpoint

**Programme:** QFORM-DENSITY-3EIG-20260922  
**Assignment:** Decoupled time integral  
**Run:** `20260922T235821Z-account03-B03-QFORM-r22`  
**Status:** supporting theorem proved; full QFORM **OPEN**; continuity **OPEN**.  
**Execution:** `WITHOUT_VERIFIED_BRAIN`.

## 1. Sources and live mathematical constraints


The newest required Claude Fourier input is:
`yspennstate/math-open-problems@e5f71d79eff325201dd0274053d20268ce65b837:proofnet24/QFORM-density/interactive/20260922T211500Z-decoupling-brascamp-lieb/FOURIER_ROUTE_REPORT.md`.
The latest path-specific commit for the companion geometric report is
`2f3340cd21be3e8b1a0d3a738e1fa7b7c6b76926`.

I use only the proved volume-sampling decoupling/Brascamp--Lieb estimate from the Fourier report. I do **not** use uniform pointwise one-coordinate oscillatory decay, independence after spectral rotation, a conditional density cap for a sum/difference pair, arbitrary-joint rank-three coarea, or a uniformly good single physical minor. Those interfaces are refuted in the live correction inbox.

The designated partner `account04/B03` has one completed current-QFORM handoff:
`math-open-problems@28681f9af7c2307f80968df86010084019599e38`.
Its advertised L2 compiler contains a previously recorded bad weighted Cauchy--Schwarz step, so I do not use it. I use only its valid general collision lemma
\[
  \Pr\{|Y-Y'|\le \varepsilon\}\le 2\varepsilon\|p_Y\|_2^2,
\]
which is simply the convolution estimate
\(\|p_Y*\widetilde p_Y\|_\infty\le\|p_Y\|_2^2\).

## 2. Input: the volume-sampling decoupled Fourier estimate

Let \(I,J\) be disjoint sets of **original independent coordinates** and let
\[
 M=A_{I,J}.
\]
Condition on every original coordinate outside \(I\cup J\). This changes only self/linear/constant terms on the active coordinates and leaves \(M\) unchanged.

For an integer \(k\ge1\) with
\[
 Z_k:=e_k(M^TM)
     =\sum_{\substack{S\subset I,\ T\subset J\\ |S|=|T|=k}}
       \det(M_{S,T})^2>0,
\]
put
\[
 w_{S,T}=\frac{\det(M_{S,T})^2}{Z_k},
 \qquad
 \alpha_i=\sum_{S,T:\ i\in S}w_{S,T},
 \qquad
 h=\max_{i\in I}\alpha_i.
\]
Thus \(\sum_i\alpha_i=k\).

The proved Claude volume-sampling theorem gives, for every real \(q\ge1\) satisfying
\[
 q\ge 2h,
\]
the dependence-safe bound
\[
 |\phi_R(t)|^2
 \le
 \left[
   e^{k/2}(2\pi)^k q^{-k/2}|t|^{-k}Z_k^{-1/2}
 \right]^{1/q}.
 \tag{2.1}
\]
Here \(R\) denotes the conditioned quadratic-plus-linear polynomial in the active original coordinates.

For provenance: (2.1) comes from one independent-copy Cauchy--Schwarz step, with
\(W_j=X_j-X'_j\) on the \(J\)-bank. The \(W_j\)'s are independent across \(j\), with densities bounded by one. The proof never declares \(X_j-X'_j\) independent of \(X_j+X'_j\), and it never conditions on one of those conjugate variables and assigns the other a false density cap.

Taking a square root and also using \(|\phi_R|\le1\), define
\[
 a=\frac{k}{2q},\qquad
 B=(2\pi)^a\left(\frac eq\right)^{a/2}
      Z_k^{-a/(2k)}.
\]
Then
\[
 |\phi_R(t)|\le \min\{1,B|t|^{-a}\}.
 \tag{2.2}
\]

## 3. New theorem: all fractional time weights below the decoupled exponent

### Theorem 3.1 (`QFORM-VOLUME-MARGINAL-WEIGHTED-RIESZ-v1`)

Under the hypotheses above, let \(0<\gamma<a\). Then
\[
 \boxed{
 \int_{\mathbb R}|t|^{\gamma-1}|\phi_R(t)|\,dt
 \le
 \frac{2a}{\gamma(a-\gamma)}
 (2\pi)^\gamma
 \left(\frac eq\right)^{\gamma/2}
 Z_k^{-\gamma/(2k)}.
 }
 \tag{3.1}
\]

Consequently, for \(0<\gamma<\min\{1,a\}\),
\[
 \boxed{
 \sup_s\mathbb E|R-s|^{-\gamma}
 \le
 \frac{a(2\pi)^\gamma}
 {\gamma(a-\gamma)\Gamma(\gamma)\cos(\pi\gamma/2)}
 \left(\frac eq\right)^{\gamma/2}
 Z_k^{-\gamma/(2k)}.
 }
 \tag{3.2}
\]

In particular, whenever \(a>1/2\), equivalently \(q<k\),
\[
 \boxed{
 \sup_s\mathbb E|R-s|^{-1/2}
 \le
 \frac{4a}{a-1/2}
 \left(\frac eq\right)^{1/4}
 Z_k^{-1/(4k)}.
 }
 \tag{3.3}
\]

#### Proof

Let \(T=B^{1/a}\). Splitting (2.2) at \(T\),
\[
\begin{aligned}
\int_{\mathbb R}|t|^{\gamma-1}|\phi_R(t)|\,dt
&\le
2\int_0^Tt^{\gamma-1}dt
+2B\int_T^\infty t^{\gamma-a-1}dt\\
&=
2T^\gamma\left(\frac1\gamma+\frac1{a-\gamma}\right)\\
&=
\frac{2a}{\gamma(a-\gamma)}B^{\gamma/a}.
\end{aligned}
\]
Since
\[
 B^{\gamma/a}
 =(2\pi)^\gamma(e/q)^{\gamma/2}Z_k^{-\gamma/(2k)},
\]
this is (3.1).

For the Riesz step, use the standard one-dimensional kernel identity
\[
 \int_{\mathbb R}|t|^{\gamma-1}e^{itx}\,dt
 =2\Gamma(\gamma)\cos(\pi\gamma/2)|x|^{-\gamma}
\]
in the regularized/distributional sense. A rigorous positive regularization is obtained by convolving \(|x|^{-\gamma}\) with a Gaussian approximate identity; its Fourier multiplier is a positive constant times \(|t|^{\gamma-1}e^{-\epsilon t^2}\). Because (3.1) makes the Fourier-side weighted integral absolutely integrable, Fubini followed by Fatou gives
\[
 \mathbb E|R-s|^{-\gamma}
 \le
 \frac{1}
 {2\Gamma(\gamma)\cos(\pi\gamma/2)}
 \int_{\mathbb R}|t|^{\gamma-1}|\phi_R(t)|\,dt.
\]
This proves (3.2). At \(\gamma=1/2\),
\(2\Gamma(1/2)\cos(\pi/4)=\sqrt{2\pi}\);
substitution into (3.1) gives (3.3). \(\square\)

## 4. The new rank-two endpoint

Set \(k=2\). A full density bound from absolute Fourier inversion would be the logarithmic endpoint when \(q=1\), because \(a=1\). The half-Riesz weight is strictly below that endpoint and closes.

If
\[
 h<1,\qquad q=\max\{1,2h\}<2,
\]
then (3.3) gives
\[
 \boxed{
 \sup_s\mathbb E|R-s|^{-1/2}
 \le C_2(h)\,Z_2^{-1/8},
 \qquad
 C_2(h)=\frac8{2-q}\left(\frac eq\right)^{1/4}.
 }
 \tag{4.1}
\]
Equivalently,
\[
 C_2(h)=
 \begin{cases}
  8e^{1/4},&h\le1/2,\\[2mm]
  \displaystyle
  \frac4{1-h}\left(\frac e{2h}\right)^{1/4},
     &1/2<h<1.
 \end{cases}
 \tag{4.2}
\]

Numerically,
\[
 8e^{1/4}=10.272203333501931\ldots.
\]

This identifies the precise endpoint obstruction: the two-volume route does **not** fail merely because \(k=2\). It fails only as the row volume-sampling marginal approaches the genuine hub endpoint \(h=1\). A pure one-hub-plus-one-spread-direction cross bank has exactly this behavior, matching the separate hub mechanisms in the newest geometric report.

### L2 collision form

Squaring (2.2) and integrating, for \(a>1/2\),
\[
 \int_{\mathbb R}|\phi_R(t)|^2dt
 \le
 \frac{8\pi a}{2a-1}
 \left(\frac eq\right)^{1/2}Z_k^{-1/(2k)}.
 \tag{4.3}
\]
By Plancherel,
\[
 \boxed{
 \|p_R\|_2^2
 \le
 \frac{4a}{2a-1}
 \left(\frac eq\right)^{1/2}Z_k^{-1/(2k)}.
 }
 \tag{4.4}
\]
For \(k=2\),
\[
 \boxed{
 \|p_R\|_2^2
 \le
 \frac4{2-q}
 \left(\frac eq\right)^{1/2}Z_2^{-1/4}.
 }
 \tag{4.5}
\]

Applying the valid completed `account04/B03` collision lemma to an independent copy \(R'\),
\[
 \boxed{
 \Pr\{|R-R'|\le\varepsilon\}
 \le
 \frac8{2-q}
 \left(\frac eq\right)^{1/2}
 Z_2^{-1/4}\,\varepsilon.
 }
 \tag{4.6}
\]
At \(h\le1/2\) this is
\[
 \Pr\{|R-R'|\le\varepsilon\}
 \le 8\sqrt e\,Z_2^{-1/4}\varepsilon
 =13.189770165601026\ldots\,Z_2^{-1/4}\varepsilon.
\]
This is an actual partner-result application to a new inequality.

## 5. Linear small-ball transducer through one physical square

Let \(Z\) be one additional **original-coordinate** cap-one variable, independent of \(W\), and suppose after completing the physical scalar pivot
\[
 Q=d\,[Z+m(W)]^2+R(W),\qquad d\ne0.
 \tag{5.1}
\]
No independence between \(m(W)\) and \(R(W)\) is assumed.

For each fixed \(W\), the density of \(d[Z+m(W)]^2\) is bounded by
\[
 |d|^{-1/2}|u|^{-1/2}.
\]
Therefore
\[
 p_Q(s)
 \le |d|^{-1/2}\mathbb E|s-R|^{-1/2}.
\]
Combining with (4.1),
\[
 \boxed{
 \|p_Q\|_\infty
 \le
 C_2(h)|d|^{-1/2}Z_2^{-1/8}
 =
 C_2(h)\bigl(|d|^4Z_2\bigr)^{-1/8}.
 }
 \tag{5.2}
\]
Hence every interval \(J\) obeys the desired linear scaling
\[
 \boxed{
 \Pr\{Q\in J\}
 \le
 C_2(h)\bigl(|d|^4Z_2\bigr)^{-1/8}|J|.
 }
 \tag{5.3}
\]

This is the target-relevant gain of the run: a two-volume decoupled bank that is only at the logarithmic endpoint for direct Fourier inversion nevertheless supplies exactly the translation-uniform half-order potential needed by a physical square pivot.

The statement remains valid after conditioning any further original coordinates, provided the same \(d,M,Z_2,h\) certificate is unchanged; arbitrary conditioned affine terms are harmless in the source decoupling estimate.

## 6. Concrete application to the Claude rank-two diffuse residual gap

The latest geometric report explicitly leaves an analytic substep in its PSD-rank-three heavy-coordinate route: after one scalar pivot, a rank-two PSD residual with arbitrary affine terms outside its spectral range is diffuse, and the report asks for an \(e_2\)-Fourier estimate uniform in those affine terms.

The new theorem supplies exactly that missing analytic endpoint.

Let
\[
 S=V\Lambda V^T,\qquad V^TV=I_2,\qquad
 |\lambda_1|,|\lambda_2|\ge1,
\]
and suppose every row leverage
\(\ell_j=\|v_j\|^2\le1/50\).
Choose a fair random partition of the remaining original coordinates into \(I,J\).
Matrix Chernoff, exactly as in the source rank-three argument but in dimension two, gives
\[
 \Pr\{\lambda_{\min}(V_I^TV_I)<1/4
        \ \text{or}\ 
        \lambda_{\min}(V_J^TV_J)<1/4\}
 \le
 4\exp[-0.076713\ldots/(1/50)]
 <0.087.
\]
Thus a deterministic partition exists with both Gram matrices at least \(I_2/4\).

For \(M=S_{I,J}=V_I\Lambda V_J^T\), exact rank two gives
\[
 Z_2
 =\det(\Lambda)^2
   \det(V_I^TV_I)\det(V_J^TV_J)
 \ge \frac1{256}.
\]
The row volume-sampling marginal is the leverage of the same row in the frame \(V_I\), so
\[
 \alpha_i
 =v_i^T(V_I^TV_I)^{-1}v_i
 \le4\ell_i
 \le\frac{4}{50}<\frac12.
\]
Therefore \(q=1\) is admissible in (4.1), uniformly over **arbitrary affine terms**, and
\[
 \boxed{
 \sup_s\mathbb E|R-s|^{-1/2}
 \le16e^{1/4}
 =20.544406667003862\ldots.
 }
 \tag{6.1}
\]

If this residual comes from a physical scalar pivot \(d\), then
\[
 \|p_Q\|_\infty
 \le16e^{1/4}|d|^{-1/2}.
 \tag{6.2}
\]
For the particular exact-rank-three PSD heavy-coordinate branch in the Claude report, a leverage at least \(1/50\) gives \(d\ge1/50\), hence
\[
 \|p_Q\|_\infty
 \le16e^{1/4}\sqrt{50}
 =145.2708926969255\ldots.
 \tag{6.3}
\]

This is **not** a new best theorem for semidefinite exact-rank-three forms: account02/B18 already has the stronger \(3e\) result. Its value is mechanistic: it closes the previously stated \(e_2\)-with-arbitrary-linear-terms analytic substep and gives a reusable higher-rank scalar-pivot/cross-bank criterion for the N3/hybrid proof.

## 7. What remains unpaid

The unrestricted conjecture is still OPEN. The newest synthesis reduces it to the strict no-pivot class N3. The theorem here turns a scalar pivot plus a rank-two volume bank into a linear small-ball bound, but N3 supplies no uniform lower bound on that scalar pivot and earlier corrections refute forcing one uniformly good local Schur certificate.

The live residual structural problem can now be phrased more sharply on this route:

* if a two-volume cross bank has row marginal \(h\le1-\delta\), (4.1) pays its translation-uniform half-Riesz cost with an explicit \(O(\delta^{-1})\) constant;
* the only endpoint not paid by this \(k=2\) time integral is \(h\to1\), exactly the near-hub concentration regime;
* pure rank-one hub endpoints are paid by the separate hub/triangular results, but **two-sided quadratic leakage with small nonzero hub blocks** remains unclosed.

Thus the next useful implication is an aggregate-before-inversion gluing statement sending every N3 survivor either to a quantitative \(1-h\) two-volume certificate, to the already-paid \(k=3\) D'/D3 or \(k=5\) D5 branch, or to a hub theorem that tolerates the remaining two-sided leakage. This is structural, not a missing time-integral calculation.

Continuity is not established by (5.2); the result proves absolute continuity and an essential \(L^\infty\) bound in its stated scope.

## 8. Finite checks

A checker accompanying this report verifies:

1. the split-integral constants in (3.1), (3.3), (4.3)--(4.6);
2. scale homogeneity under \(M\mapsto cM\) and \((d,M)\mapsto(c d,cM)\);
3. the \(k=2,h\le1/2\) numerical constants;
4. the rank-two Chernoff failure probability at leverage \(1/50\);
5. \(Z_2\ge1/256\) implies (6.1), and then (6.3).

These checks support algebra/constants; they are not a proof substitute.
