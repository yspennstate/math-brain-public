# account04/B20 r13 — proof graph and localized-window pivot/double-anchor compiler

Programme: QFORM-DENSITY-3EIG-20260922  
Run: 20260924T051424Z-account04-B20-QFORM-r13  
Status: ESSENTIAL_STEP_APPLIED / PROVED_SUPPORTING_COMPILER / FULL_TARGET_OPEN

The universal theorem is not claimed. This report records a noncircular proof graph and proves a new implication at the localized child-window leaf. All coordinates below are original coordinates. No rotated independence, moment assumption, support restriction, arbitrary-joint coarea estimate, or deletion of a nonzero coefficient tail is used.

## 1. Source pins

The Claude baseline is math-open-problems@e5f71d79eff325201dd0274053d20268ce65b837, with later directory commits 2f3340cd21be3e8b1a0d3a738e1fa7b7c6b76926 and 7ffd1ed79398611eb06752f622be0ce33dcacb5a retained as continuation/correction boundaries.

The completed account01/B20 input is math-open-problems@942f8610e8af1d2d4268f769e0fb2c76d467d02a, theorem QFORM-R46-GLOBAL-FOURSTAR-E3-OR-LATENT8-v1. Its actual surviving carrier satisfies

\[
s_2(B_8)>0.015572142004163547,
\qquad
s_1(B_8)s_2(B_8)>0.0010721022665500545,
\tag{1.1}
\]

while the retained tail obeys

\[
\|E\|_{\rm op}<\frac{\sqrt3}{32768}.
\tag{1.2}
\]

The B08 structural input is account01/B08 r35 at math-open-problems@68f8d8a91987834d73fa06849d9ec8795a3df883. The child-window receiver is account04/B08 r2 at math-open-problems@a5e66e2944c89857a41d5e18c283d53a4307be76.

## 2. Noncircular proof graph

The currently source-valid graph is:

1. A literal physical cross block with positive third compound is paid by the marginal-free physical \(E_3\) receiver. This includes the global-star branch of account01/B20, with bound \(553978\).
2. In their stated scopes, \(D'\), \(D_5\), ridge-window, scalar-pivot, mixed-hub, and literal-cross volume-stability receivers are terminal paid nodes. None is used outside its own hypotheses.
3. The completed diffuse four-bank compiler either reaches a paid physical \(E_3\) node or the global latent-eight endpoint (1.1)–(1.2). The latter still retains four arbitrary same-bank quadratic blocks and the nonzero tail.
4. The selected-three diffuse route either pays by the ambient ridge theorem, scalar pivot, the small-\(s_3(C)\) literal-cross volume route, or the large-\(s_3(C)\) child ridge route.
5. Claude's ruled estimate pays only its one-sheet/ruled-side class. It is not transferred to arbitrary translated access to the convex/two-sheet side.

Therefore the open leaves are genuinely distinct:

- the global four-bank latent-\(2+2+2+2\) endpoint with its tail retained;
- the strong-arm rank-two separator endpoint;
- the localized child-window/double-anchor collar treated below;
- the shared-bank indefinite convex/two-sheet collar.

This graph does not route any open leaf back into an ancestor.

## 3. Window leverage forces a physical pivot or star

### Lemma — QFORM-WINDOW-LEVERAGE-TO-PHYSICAL-STAR-v1

Let \(C\) be real symmetric and let

\[
P_\tau=\mathbf 1_{\{|\lambda(C)|\ge\tau\}}.
\]

For every original coordinate \(j\), if \(q=(P_\tau)_{jj}\), then

\[
\|Ce_j\|_2\ge \tau\sqrt q,
\tag{3.1}
\]

and consequently

\[
\boxed{
\max\{|C_{jj}|,\ \|C_{-j,j}\|_2\}
\ge \tau\sqrt{\frac q2}.
}
\tag{3.2}
\]

Proof. By the spectral theorem,

\[
\|Ce_j\|_2^2
=\int \lambda^2\,d\mu_j(\lambda)
\ge \tau^2\mu_j(\{|\lambda|\ge\tau\})
=\tau^2q.
\]

Since \(\|Ce_j\|_2^2=C_{jj}^2+\|C_{-j,j}\|_2^2\), (3.2) follows. QED.

This is a coefficient statement; it introduces no random rotation.

## 4. Application to the live B08 survivor

Use

\[
\rho_0=2.157910236855737\times10^{-5},
\qquad
m=\rho_0L.
\]

The completed B08 route already gives:

- if \(s_3(C)\le\rho_0L\), the volume-stability branch pays by
  \[
  \|p_Q\|_\infty<66615.376/L;
  \tag{4.1}
  \]
- if \(s_3(C)>\rho_0L\) and the child window at \(m/64\) has leverage at most \(1/32\), the ridge branch pays by
  \[
  \|p_Q\|_\infty<2965832.356/L.
  \tag{4.2}
  \]

These are two certificates on the same physical deletion matrix \(C\).

Suppose the remaining child ridge gate fails. Then some child coordinate \(j\) has

\[
(P_{m/64})_{jj}>\frac1{32}.
\]

Applying (3.2) with \(\tau=m/64\) gives

\[
\boxed{
\max\{|C_{jj}|,\ \|C_{-j,j}\|_2\}
>a_0L,
\qquad
a_0:=\frac{\rho_0}{512}
=4.2146684313588616\times10^{-8}.
}
\tag{4.3}
\]

### Pivot branch

If \(|C_{jj}|\ge a_0L\), the completed all-sign scalar-pivot theorem applies to this same original coordinate \(j\), because the full matrix still has \(s_3(A)\ge L\). With

\[
C_*=1+44\cdot10^{15/2},
\]

it gives the actual bound

\[
\boxed{
\|p_Q\|_\infty
\le \frac{C_*}{\sqrt{a_0}\,L}
<\frac{6.778\times10^{12}}{L}.
}
\tag{4.4}
\]

Continuity is not imported from the scalar-pivot theorem.

Thus every unpaid localized child window lies in the off-diagonal branch

\[
\|C_{-j,j}\|_2>a_0L.
\tag{4.5}
\]

## 5. Exact double-anchor refinement

Let \(i\) be the original deletion coordinate from account01/B08, so its star satisfies

\[
\|b\|_2>\beta_0L,
\qquad
\beta_0=\frac{\sqrt3}{128\sqrt{96}}
=0.0013810679320049757\ldots .
\tag{5.1}
\]

Write the child indices as \(\{j\}\sqcup K\), put

\[
u=b_K,\qquad v=C_{K,j}.
\]

From (4.5), \(\|v\|>a_0L\). The following exhaustive alternatives hold.

1. Strong anchor edge:
   \[
   |b_j|\ge \frac{\beta_0}{\sqrt2}L.
   \tag{5.2}
   \]

2. Otherwise \(\|u\|>\beta_0L/\sqrt2\). For every \(0<\varepsilon<1\), either
   \[
   \operatorname{dist}(v,\operatorname{span}u)
   <\varepsilon\|v\|,
   \tag{5.3}
   \]
   or the literal original-coordinate cross block
   \[
   M=A[K,\{i,j\}]=[u\ v]
   \]
   satisfies
   \[
   \boxed{
   s_2(M)\ge \frac{\varepsilon a_0}{\sqrt2}L.
   }
   \tag{5.4}
   \]

Indeed, in the transverse case the determinant of the \(2\times2\) Gram matrix is at least
\(\varepsilon^2\|u\|^2\|v\|^2\). Since its smaller eigenvalue is at least determinant divided by trace,

\[
s_2(M)^2
\ge
\frac{\varepsilon^2\|u\|^2\|v\|^2}{\|u\|^2+\|v\|^2}
\ge
\frac{\varepsilon^2}{2}\min\{\|u\|^2,\|v\|^2\},
\]

which gives (5.4), because \(a_0<\beta_0/\sqrt2\).

At \(\varepsilon=1/64\),

\[
s_2(M)>4.6565947316667495\times10^{-10}L.
\tag{5.5}
\]

Hence the previously abstract localized-window leaf has been reduced to one of three literal original-coordinate packets: a paid scalar pivot, a strong edge between two anchors, or a quantitatively transverse rank-two double-anchor cross block; the only geometric collar left is (5.3).

## 6. What remains

The new lemma does not itself supply a third cross direction and therefore does not close the universal theorem. The first exact next implication is:

\[
\text{strong edge or transverse double anchor or aligned two-star collar}
\Longrightarrow
\text{a paid mixed-hub / physical }E_3\text{ receiver}.
\]

Separately, the latent-eight endpoint (1.1)–(1.2), the strong-arm separator, and the convex/two-sheet shared-bank collar remain open. Two independent end-to-end reviews are still required before any full candidate can be declared complete.
