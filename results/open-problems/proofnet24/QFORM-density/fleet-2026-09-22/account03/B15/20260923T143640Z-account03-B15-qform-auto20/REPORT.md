SIGNED IN - working on the quadratic-form bounded-density conjecture (universal constant), account account03, slot B15, 2026-09-23T14:36:40Z.
attacking: continuity from quantitative small-ball regularity; sharpen the new four-row |t|^{-3/2} Fourier branch to endpoint C^{0,1/2} and compile it through Gaussian heat height.

# Endpoint half-Hölder regularity for the four-row QFORM branch

**Programme:** `QFORM-DENSITY-3EIG-20260922`  
**Worker:** `account03/B15`  
**Run:** `20260923T143640Z-account03-B15-qform-auto20`  
**Outcome:** `PROVED_SUPPORTING_REGULARITY_THEOREM / PARTNER_RESULT_APPLIED / FULL_TARGET_OPEN`  
**Execution:** `WITHOUT_VERIFIED_BRAIN`

## 1. Exact scope and source pins

The full owner target remains open. This report proves a quantitative regularity strengthening of a newly completed product-preserving branch; it does not prove the unrestricted universal height theorem.

The fresh branch consumed is account01/B11, canonical source
`yspennstate/math-open-problems@5653e2950f7147ab93f976d3b67feab16f27deed`, path
`proofnet24/QFORM-density/fleet-2026-09-22/account01/B11/20260923T141542Z-account01-B11-QFORM-auto11/REPORT.md`.
Its theorem `QFORM-FOURROW-L2-MATCHING-v1` treats
\[
Q=\beta U^2+2\alpha VH+R_T(X_T)+\sum_{i\in S}q_i(X_i),
\qquad U=a\cdot X_S,\quad H=h\cdot X_S,\quad V=c\cdot X_T,\quad C=\|c\|_2>0,
\]
under the original cap-one product law. If four distinct rows \(v_r=(a_r,h_r)\) admit disjoint nonparallel pairs \((i,j)\), \((k,l)\), with
\[
\Delta_1=|\det(v_i,v_j)|>0,\qquad \Delta_2=|\det(v_k,v_l)|>0,
\]
then its proved joint four-coordinate Plancherel estimate is
\[
|\phi_Q(t)|\le \min\{1,K|t|^{-3/2}\},
\tag{1.1}
\]
where
\[
K=\sqrt2\,\pi^{3/2}|\beta|^{-1/2}(|\alpha|C)^{-1}(\Delta_1\Delta_2)^{-1/2}.
\tag{1.2}
\]
This is not the refuted law-uniform one-dimensional van-der-Corput shortcut.

The assigned completed partner consumed is account04/B15,
`yspennstate/math-open-problems@ad7e5daa036cc8330b1432285ad40fec611d37dd`, path
`proofnet24/QFORM-density/fleet-2026-09-22/account04/B15/20260922T211430Z-account04-B15-heat-regularity-r4/REPORT.md`.
For every probability law \(\mu\), it proves the exact Gaussian heat-height identity
\[
\sup_{\varepsilon>0,y}(\mu*\gamma_\varepsilon)(y)=\|p_\mu\|_\infty,
\tag{1.3}
\]
with value \(+\infty\) if no bounded density exists; for \(p\in C_0\), the heat maxima increase to \(\max p\) as \(\varepsilon\downarrow0\).

## 2. New endpoint Fourier regularity compiler

### Theorem 2.1 — `QFORM-T32-ENDPOINT-HOLDER-v1`

Let \(Z\) be real and suppose
\[
|\phi_Z(t)|\le\min\{1,K|t|^{-3/2}\}\qquad(t\ne0)
\tag{2.1}
\]
for some \(K>0\). Then \(Z\) has a density \(p\in C_0(\mathbb R)\),
\[
\|p\|_\infty\le {3\over\pi}K^{2/3},
\tag{2.2}
\]
and the endpoint half-Hölder bound
\[
\boxed{[p]_{C^{0,1/2}}\le {6K\over\pi}.}
\tag{2.3}
\]
The exponent \(1/2\) is reached without a logarithmic loss; the usual weighted-moment argument only gives exponents strictly below \(1/2\).

### Proof

The envelope is integrable, so Fourier inversion gives \(p\in C_0\). Put \(T=K^{2/3}\), so \(KT^{-3/2}=1\). Then
\[
\|p\|_\infty\le {1\over\pi}\left(T+K\int_T^\infty t^{-3/2}dt\right)={3T\over\pi}.
\]
For \(h\ne0\), symmetry and \(|e^{iu}-1|\le\min(2,|u|)\) give
\[
|p(x+h)-p(x)|\le {1\over\pi}\int_0^\infty\min(2,|h|t)\min(1,Kt^{-3/2})dt.
\tag{2.4}
\]
If \(0<|h|\le T^{-1}\), put \(R=|h|^{-1}\ge T\). Splitting at \(T,R\),
\[
\begin{aligned}
\pi|p(x+h)-p(x)|
&\le |h|\int_0^Tt\,dt+|h|K\int_T^Rt^{-1/2}dt+2K\int_R^\infty t^{-3/2}dt\\
&={|h|T^2\over2}+2K|h|(R^{1/2}-T^{1/2})+4KR^{-1/2}\\
&=6K|h|^{1/2}-{3\over2}|h|T^2\le6K|h|^{1/2},
\end{aligned}
\]
using \(R=|h|^{-1}\) and \(KT^{1/2}=T^2\). If \(|h|\ge T^{-1}\), then
\[
|p(x+h)-p(x)|\le2\|p\|_\infty\le6T/\pi\le(6K/\pi)|h|^{1/2}.
\]
This proves (2.3). \(\square\)

## 3. Quantitative small-ball recovery

For every \(y\in\mathbb R\) and \(r>0\),
\[
\left|\Pr(|Z-y|\le r)-2rp(y)\right|
\le\int_{-r}^r|p(y+u)-p(y)|du
\le {4\over3}[p]_{C^{0,1/2}}r^{3/2}.
\]
Therefore
\[
\boxed{\left|{\Pr(|Z-y|\le r)\over2r}-p(y)\right|\le {4K\over\pi}r^{1/2}.}
\tag{3.1}
\]
At a true density maximizer \(y_*\),
\[
\|p\|_\infty\le {\Pr(|Z-y_*|\le r)\over2r}+{4K\over\pi}r^{1/2}.
\tag{3.2}
\]
Thus this branch has finite-radius recovery of the density at every center, with an explicit square-root error.

## 4. Application to the fresh four-row QFORM theorem

Substituting (1.2) into (2.3), every instance covered by `QFORM-FOURROW-L2-MATCHING-v1` satisfies
\[
\boxed{
[p_Q]_{C^{0,1/2}}
\le6\sqrt{2\pi}\,|\beta|^{-1/2}(|\alpha|C)^{-1}(\Delta_1\Delta_2)^{-1/2}.
}
\tag{4.1}
\]
The scalar coefficient is \(6\sqrt{2\pi}=15.0397696477\ldots\).

For account01/B11's target-valid six-coordinate family,
\[
\beta=\alpha=C=1,\qquad \Delta_1=\Delta_2={1\over2\sqrt2},\qquad \Delta_1\Delta_2={1\over8}.
\]
Hence
\[
\boxed{[p_Q]_{C^{0,1/2}}\le24\sqrt\pi=42.5388924217\ldots .}
\tag{4.2}
\]
The source theorem also gives
\[
\|p_Q\|_\infty\le6\,2^{1/3}<7.560.
\tag{4.3}
\]
For every center and radius in this concrete family,
\[
\boxed{\left|{\Pr(|Q-y|\le r)\over2r}-p_Q(y)\right|\le16\sqrt\pi\,r^{1/2}.}
\tag{4.4}
\]

## 5. Actual application of the assigned account04/B15 partner

Let
\[
M_\varepsilon(Q)=\sup_y(p_Q*\gamma_\varepsilon)(y).
\]
The partner theorem gives the exact monotone limit
\[
M_\varepsilon(Q)\uparrow\|p_Q\|_\infty\qquad(\varepsilon\downarrow0).
\tag{5.1}
\]
The new endpoint modulus gives an explicit rate. For \(G\sim N(0,1)\),
\[
\mathbb E|G|^{1/2}={2^{1/4}\Gamma(3/4)\over\sqrt\pi}=0.8221789587\ldots,
\]
and
\[
\|p_Q-p_Q*\gamma_\varepsilon\|_\infty
\le[p_Q]_{C^{0,1/2}}\varepsilon^{1/2}\mathbb E|G|^{1/2}.
\]
Evaluating at a maximizer of \(p_Q\) and using convolution contraction gives
\[
\boxed{
0\le\|p_Q\|_\infty-M_\varepsilon(Q)
\le6\,2^{3/4}\Gamma(3/4)
|\beta|^{-1/2}(|\alpha|C)^{-1}(\Delta_1\Delta_2)^{-1/2}\,\varepsilon^{1/2}.
}
\tag{5.2}
\]
The scalar coefficient before the geometric factors is \(12.3653821475\ldots\). For the six-coordinate family,
\[
\boxed{0\le\|p_Q\|_\infty-M_\varepsilon(Q)\le34.9745822740\ldots\,\varepsilon^{1/2}.}
\tag{5.3}
\]
This is an actual quantitative use of the completed account04/B15 theorem: the exact heat-height limit is upgraded on the fresh four-row branch to a square-root convergence rate.

## 6. Full-target connection and remaining obstruction

The full conjecture is still **OPEN / NOT PROVED / NOT DISPROVED**. The geometric factor \((\Delta_1\Delta_2)^{-1/2}\) diverges in account01/B11's remaining near-star chamber \(0<M_4\ll D^2\). Endpoint regularity therefore does not replace the missing averaged matching-mass argument.

The reusable conclusion is: whenever a product-preserving QFORM branch supplies the natural rank-three envelope \(|\phi_Q(t)|\le\min(1,K|t|^{-3/2})\), it automatically supplies not just a bounded continuous density but the **endpoint** `C^{0,1/2}` modulus, finite-radius small-ball recovery at rate \(O(r^{1/2})\), and Gaussian heat-height recovery at rate \(O(\varepsilon^{1/2})\). If future work makes \(K\) universal on the remaining branch, continuity follows quantitatively at the same time as height.

## 7. Corrections and regularity ledger

No argument here uses law-uniform pointwise quadratic-phase decay, independence after spectral rotation, the refuted arbitrary-joint rank-three coarea inequality, a naive dimension-free fiber supremum, or any moment/log-concavity/compact-support/connected-support/Gaussian assumption.

A separate completed account02/B15 report source-reports a fixed-instance `C_0` density theorem for all rank-\(\ge3\) target instances, but the shared consolidated `CLAIMS.json` still marks the full continuity claim open; this run does not alter that shared status. The present theorem is independently quantitative on the stated four-row branch.

Native status remains `WITHOUT_VERIFIED_BRAIN`: repository retrieval was authenticated, but no authenticated native mathematical-receiver ingestion/use was observed.

Fresh control at start: `yspennstate/math-research-brain@7f70e05a57f62a7bc1be45aeb28899e17a585b2c`, OWNER CONTROL revision `2026-09-22.15`. Controls and live corrections must be refreshed again before publication.

No scheduler/task state, email, notification, permission, public-release, cross-account authentication, paid model/API/Codex call, installation, or remote workflow was changed.
