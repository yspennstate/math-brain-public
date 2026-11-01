# fleet04/B08 r3 — distributed-star derivative splitting and hybrid pair-log payment

Programme: \`QFORM-DENSITY-3EIG-20260922\`  
Run: \`20260924T081435Z-fleet04-B08-QFORM-r3\`  
Status: **ESSENTIAL STEP APPLIED / FULL TARGET OPEN**

The unrestricted theorem is not proved here. Continuity is separate and is not claimed. All variables below are original-coordinate variables; no independence after a spectral rotation is used.

## Source pins and corrected scope

The Claude starting point is
\`yspennstate/math-open-problems@e5f71d79eff325201dd0274053d20268ce65b837\`,
\`proofnet24/QFORM-density/interactive/20260922T211500Z-decoupling-brascamp-lieb/\`,
including \`RESULTS.md\`, \`FOURIER_ROUTE_REPORT.md\`, and \`COUNTEREXAMPLE_SEARCH.md\`.
The later Claude-review corrections remain in force: no arbitrary-joint coarea cap, no worst conditional-density substitution, and no claim that the ruled-side estimate covers the convex/two-sheet side.

The completed fleet01/B08 input used at an actual inequality is
\`yspennstate/math-open-problems@77e8bed81a9bbe79e6443bbb37ae8a1fc84beb8c\`,
\`proofnet24/QFORM-density/fleet-2026-09-22/fleet01/B08/20260924T051232Z-fleet01-B08-qform-r43/REPORT.md\`.
It supplies, on the diffuse survivor, an original-coordinate deletion
\[
 A=\begin{pmatrix}a&b^\top\\ b&C\end{pmatrix},
 \qquad \|b\|_2>\rho_*L,
 \qquad \rho_*=0.0006247538095703261,
\]
together with
\[
 s_2(C)\ge \sqrt{47/48}\,L.
\]
It also supplies the physical-pair logarithmic receiver
\[
 p_Q(t)\le {2\sqrt2\over r}
 +{1\over\sqrt D}\,
   \mathbb E\log_+{2r^2\over \kappa |t-Z|},
 \tag{1}
\]
where \(\kappa\) is the smaller singular value of the retained indefinite physical pair and \(D\) is the absolute determinant of that pair.

## 1. A translation-uniform distributed-star lemma

### Theorem — \`QFORM-DISTRIBUTED-STAR-DERIVATIVE-SPLIT-v1\`

Let \(X\) be real with density at most one. Let \(Y\) be independent of \(X\). Suppose \(\Gamma=\Gamma(Y)\) has a density bounded by \(K\), and let \(R=R(Y)\) be completely arbitrary and possibly maximally dependent on \(\Gamma\). For
\[
 H=aX^2+X\Gamma(Y)+R(Y)
\]
and all \(t\in\mathbb R,\varepsilon>0\),
\[
 \boxed{\;
 \mathbb P(|H-t|<\varepsilon)
 \le \min\{1,\,4\sqrt{2K\varepsilon}\}.
 \;}
 \tag{2}
\]

#### Proof

Fix \(\lambda>0\) and split according to the physical derivative
\[
 \partial_XH=2aX+\Gamma(Y).
\]
Because \(X\) is independent of \(\Gamma\), conditioning on \(X=x\) gives
\[
 \mathbb P(|2aX+\Gamma|\le\lambda)\le 2K\lambda.
 \tag{3}
\]
On the complementary event, condition on \(Y=y\). The polynomial
\[
 x\longmapsto ax^2+\Gamma(y)x+R(y)-t
\]
is monotone on at most two intervals on which its derivative has modulus greater than \(\lambda\). On each interval the preimage of \((-\varepsilon,\varepsilon)\) has length at most \(2\varepsilon/\lambda\). Since the density of \(X\) is at most one,
\[
 \mathbb P\bigl(|H-t|<\varepsilon,\,
 |2aX+\Gamma|>\lambda\bigr)
 \le {4\varepsilon\over\lambda}.
 \tag{4}
\]
Thus
\[
 \mathbb P(|H-t|<\varepsilon)
 \le 2K\lambda+{4\varepsilon\over\lambda}.
\]
Taking \(\lambda=\sqrt{2\varepsilon/K}\) proves (2). Notice that neither the magnitude of \(a\) nor any relation between \(R\) and \(\Gamma\) enters the result. This is the point that makes the estimate safe under arbitrary child curvature.

## 2. Apply it to the live B08 distributed star

For independent cap-one coordinates \(Y_j\), the standard product-marginal bound gives
\[
 \left\|p_{\,2\langle b,Y\rangle}\right\|_\infty
 \le {\sqrt2\over 2\|b\|_2}
 ={1\over\sqrt2\,\|b\|_2}.
 \tag{5}
\]
Apply Theorem (2) to
\[
 X^\top AX=aX^2+2X\langle b,Y\rangle+Y^\top CY.
\]
The child term \(Y^\top CY\) is the arbitrary \(R(Y)\); it is not discarded and need not be independent of the star slope. Equations (2) and (5) give
\[
 \boxed{\;
 \sup_t\mathbb P(|X^\top AX-t|<\varepsilon)
 \le 4\,2^{1/4}\sqrt{\varepsilon/\|b\|_2}.
 \;}
 \tag{6}
\]
At the completed fleet01/B08 inequality \(\|b\|_2>\rho_*L\),
\[
 \boxed{\;
 \sup_t\mathbb P(|X^\top AX-t|<\varepsilon)
 <190.311\,(\varepsilon/L)^{1/2}.
 \;}
 \tag{7}
\]
This improves the generic fourth-root small-ball exponent on the entire distributed-star survivor to a square-root exponent, while retaining every entry of \(C\), every sign, and arbitrary tails.

## 3. Actual hybrid density payment through the completed pair-log receiver

Suppose an original-coordinate indefinite physical pair survives a completion for which the residual \(Z\) still has a distributed-star representation covered by (7). Put \(C_*=190.311\). Then
\[
 \mathbb P(|Z-u|<\rho)
 \le \min\{1,C_*\sqrt{\rho/L}\}.
 \tag{8}
\]
For \(A_0>0\), layer cake yields
\[
 \mathbb E\log_+{A_0\over|u-Z|}
 \le \int_0^\infty
 \min\{1,C_*\sqrt{A_0/L}\,e^{-s/2}\}\,ds.
 \tag{9}
\]
Choose in (1)
\[
 r={\sqrt{\kappa L}\over C_*\sqrt2}.
 \tag{10}
\]
Then the coefficient in (9) equals one, so the integral is at most \(2\). Consequently
\[
 \boxed{\;
 \|p_Q\|_\infty
 \le {4C_*\over\sqrt{\kappa L}}+{2\over\sqrt D}.
 \;}
 \tag{11}
\]
This is a full density bound for the matched hybrid, not merely a small-ball estimate.

At the completed fleet01/B08 physical-pair gate
\[
 \kappa\ge L/64,
\]
and using \(\sqrt D\ge\kappa\) for an indefinite \(2\times2\) pair, (11) gives the concrete same-matrix inequality
\[
 \boxed{\;
 \|p_Q\|_\infty< {6218\over L}.
 \;}
 \tag{12}
\]
The estimate is uniform in the Schur curvature \(a-r^\top P^{-1}r\). Hence it pays both the exactly singular and near-singular hub transition whenever the effective distributed star persists after the physical-pair completion.

## 4. Same-matrix certificate comparison

On the live matrix:

- The ridge certificate pays when the relevant child spectral window is diffuse. Its failure produces physical leverage but does not control the arbitrary child translation in (2).
- A \(D'\) or \(D_5\) volume certificate can pay when the corresponding cross-block compound and its marginal gates survive. The distributed star alone does not force \(E_3\) or \(E_5\); in particular \(D_5\) may be identically unavailable.
- The derivative-splitting certificate uses the actual star norm \(\|b\|_2\), survives arbitrary \(C\), and requires no endpoint moment. Combined with the pair-log receiver, it pays the physical-pair subbranch by (12).

Thus the first remaining B08 obstruction is narrower than the previous generic distributed-star branch: after ridge, fixed-edge, scalar-pivot, and (12) fail, every eligible physical-pair completion must either be absent/too small or cancel the effective star below the live scale. This is an explicit pair-completion alignment collar, in addition to the separate shared-bank convex/two-sheet obstruction. No claim is made that either collar is already solved.

## 5. Noncircular proof-graph update

The relevant path is now
\[
 \text{diffuse/localized router}
 \longrightarrow
 \begin{cases}
  \text{ridge payment},\\
  \text{scalar/fixed-edge payment},\\
  \text{distributed star }(\|b\|_2>\rho_*L).
 \end{cases}
\]
For the last branch,
\[
 \text{distributed star}
 \xrightarrow{\text{Theorem (2)}} \text{square-root small ball}
 \xrightarrow{\text{fleet01/B08 pair-log (1)}} \text{density bound (12)}
\]
whenever the effective star persists through an eligible physical-pair completion. The unpaid successor is the deterministic alignment implication needed to show that simultaneous cancellation across all eligible completions forces one of the already-paid volume/ridge/definite-plane branches.

The full universal bounded-density theorem and the global continuity statement remain open.
