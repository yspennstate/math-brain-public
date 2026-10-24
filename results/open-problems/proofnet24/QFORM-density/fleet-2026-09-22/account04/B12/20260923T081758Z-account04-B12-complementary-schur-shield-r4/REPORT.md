SIGNED IN - working on the quadratic-form bounded-density conjecture (universal constant), account account04, slot B12, 2026-09-23T08:17:58Z.

# account04/B12 — complementary Schur shield for arbitrary hostile spectrum

Programme: `QFORM-DENSITY-3EIG-20260922`  
Run: `20260923T081758Z-account04-B12-complementary-schur-shield-r4`  
Status: **PROVED_SUPPORTING_THEOREM / FULL_QFORM_OPEN / NOT_INDEPENDENTLY_REVIEWED**  
Continuity: **not claimed**; all density bounds are essential-supremum bounds.

## 1. Result

This run proves a principal-block stability theorem for a low-rank arbitrary spectral addition plus an arbitrary small dense tail. The large addition may have every sign, cross zero, pass through resonances, and have unbounded operator norm. No random quadratic remainder is called small.

The key improvement over an invertibility-based Schur rescue is that the updated Schur block is allowed to be completely singular. Three protected complementary directions already suffice.

## 2. Sources and controls actually used

Fresh brain main was observed at `50f8f9aff2441d2b7230c67e8357a7395a7a099e`; OWNER CONTROL remained revision `2026-09-22.15`. I re-read `AGENTS.md`, `scheduled_tasks/README.md`, the live `CORRECTION_INBOX.json` (blob `c7000cf3822ae4935a2faf43b89ac92ea65ac0fe`), the account04/B12 assignment (blob `eefbe5aa60685c7bfc6cc1a2abc1eb856d7de454`), and the current request (blob `165c570ecb4dcc6299c38fc3298771e4a8339dac`). The advertised `MEMORY_PROTOCOL.md` was not present at the tested repository paths; no content was invented.

The required Claude source was re-read from `proofnet24/QFORM-density/interactive/20260922T211500Z-decoupling-brascamp-lieb/RESULTS.md` (current blob `62e20ee976ddeb3f42d3ee5befd6ed49edc917a5`; designated base commit `e5f71d79eff325201dd0274053d20268ce65b837`).

The completed partner theorem used at an equation is account01/B12 r28, `proofnet24/QFORM-density/fleet-2026-09-22/account01/B12/20260923T065152Z-account01-B12-QFORM-r28/REPORT.md` (blob `00c9dd6ce788a46e0f299990452f94c8fc54c117`). Its exact singular-core factorization is the algebraic input below.

## 3. Analytic receiver

The finite-dimensional physical-fiber theorem states: if an actual original-coordinate principal block \(H\) of size \(m\) has at least three eigenvalues of absolute value at least \(\gamma>0\), then, after conditioning on every outside original coordinate,

\[
\|p_{X^TAX}\|_\infty\le {2\sqrt{6\pi m}\over\gamma}.
\tag{3.1}
\]

Conditioning may generate arbitrary affine terms and arbitrary outside couplings. No spectral rotation of the random vector is made.

## 4. Three-mode complementary Schur shield

Let \(I\) be an actual original-coordinate set of size \(m=s+d\), \(d\ge3\). On this physical block write

\[
H_0=B+U\Theta U^T,
\tag{4.1}
\]

where \(B=B^T\), \(U\) has rank \(s\), and \(\Theta=\Theta^T\) is completely arbitrary. Let \(W\) be an orthonormal basis of \({\rm Ran}\,U\), and \(Z\) an orthonormal basis of its complement inside the physical block. These bases are used only for deterministic matrix algebra. Put

\[
B_{11}=W^TBW,\qquad B_{12}=W^TBZ,\qquad D=Z^TBZ.
\tag{4.2}
\]

Assume \(D\) is invertible and has at least three singular values at least \(\mu>0\). Define

\[
R=B_{12}D^{-1},\qquad
\rho=\|R\|_{\rm op},\qquad
\ell(\rho)={\sqrt{\rho^2+4}-\rho\over2}.
\tag{4.3}
\]

### Theorem 4.1 (`QFORM-THREE-MODE-COMPLEMENTARY-SCHUR-SHIELD-v1`)

For every symmetric \(\Theta\), without any magnitude or sign restriction,

\[
s_3(B+U\Theta U^T)\ge \ell(\rho)^2\mu.
\tag{4.4}
\]

If \(T=T^T\) is any ambient dense perturbation with \(\|T\|_{\rm op}\le\delta<\ell(\rho)^2\mu\), then the actual principal block satisfies

\[
s_3\bigl((B+U\Theta U^T+T)[I,I]\bigr)
\ge \gamma:=\ell(\rho)^2\mu-\delta>0,
\tag{4.5}
\]

and hence

\[
\boxed{
\|p_{X^T(B+U\Theta U^T+T)X}\|_\infty
\le {2\sqrt{6\pi m}\over \ell(\rho)^2\mu-\delta}.
}
\tag{4.6}
\]

All coordinates outside \(I\), all outside spectrum, and all outside couplings are arbitrary.

### Proof

Apply the completed account01/B12 complementary-Schur identity. In the orthogonal physical basis \([W,Z]\),

\[
\widehat H_0
=L\begin{pmatrix}S&0\\0&D\end{pmatrix}L^T,
\qquad
L=\begin{pmatrix}I_s&R\\0&I_d\end{pmatrix},
\tag{4.7}
\]

where

\[
S=B_{11}-B_{12}D^{-1}B_{12}^T+W^TU\Theta U^TW.
\tag{4.8}
\]

No lower bound on \(S\) is assumed. It may be zero or resonant. The exact shear calculation in account01/B12 gives

\[
\sigma_{\min}(L)=\ell(\rho).
\tag{4.9}
\]

For invertible \(P,R_0\), singular values obey

\[
s_k(PMR_0)\ge \sigma_{\min}(P)\sigma_{\min}(R_0)s_k(M).
\tag{4.10}
\]

The block diagonal matrix in (4.7) has at least the three protected singular values supplied by \(D\), regardless of \(S\). Therefore

\[
s_3(\widehat H_0)
\ge \sigma_{\min}(L)^2
s_3\!\begin{pmatrix}S&0\\0&D\end{pmatrix}
\ge \ell(\rho)^2\mu.
\tag{4.11}
\]

Orthogonal conjugation back to the physical coordinates preserves singular values. The compression \(T[I,I]\) has operator norm at most \(\delta\), so the singular-value Weyl inequality proves (4.5). Finally (3.1) applied to this actual physical block proves (4.6). The perturbation \(T\) enters only through deterministic spectral perturbation. QED.

## 5. Concrete full-target inequality

Take the actual physical block \(I=\{1,\dots,5\}\), with

\[
W=(e_1,e_2),\qquad Z=(e_3,e_4,e_5),
\]

\[
B_{11}=0,\qquad
B_{12}=\begin{pmatrix}1&0&0\\0&1&0\end{pmatrix},\qquad
D=\operatorname{diag}(2,-2,2),
\tag{5.1}
\]

and \(U=W\). Let \(\Theta\) be any real symmetric \(2\times2\) matrix, with arbitrary signs and arbitrarily large eigenvalues. Let \(T\) be any symmetric ambient matrix, of arbitrary rank and dense support, satisfying \(\|T\|_{\rm op}\le1/5\). Here

\[
\mu=2,\qquad \rho={1\over2},\qquad
\ell(1/2)^2={9-\sqrt{17}\over8}.
\tag{5.2}
\]

Thus the protected physical gap is

\[
\gamma=2{9-\sqrt{17}\over8}-{1\over5}
={41-5\sqrt{17}\over20}
=1.0192235935\ldots>1.
\tag{5.3}
\]

The matrix therefore satisfies the original target hypothesis through an actual physical principal block for every \(\Theta\). Applying (4.6) at \(m=5\) gives

\[
\boxed{
\|p_{X^T(B+U\Theta U^T+T)X}\|_\infty
\le {40\sqrt{30\pi}\over 41-5\sqrt{17}}<19.051.
}
\tag{5.4}
\]

This remains true after adjoining arbitrarily many original coordinates with arbitrary symmetric self-block and arbitrary couplings to the displayed five coordinates. The \(X_i\) may have any independent probability densities bounded by one, with unbounded and fragmented supports.

## 6. Why this is stronger than resonance routing

The preceding two-core theorem routed a scalar spectral parameter away from finitely many local resonances. The present theorem requires no routing and no separation of resonance sets. The entire Schur block \(S\) may be singular for a continuum of hostile parameters. Three complementary physical modes survive because congruence by the fixed shear cannot erase them.

Equivalently: an arbitrary rank-\(s\) spectral addition is harmless whenever one can localize its physical footprint inside a bounded block and find three quantitatively nonsingular directions in the complementary compression. A small dense tail is then harmless at the matrix level even though \(X^TTX\) need not be small for unbounded inputs.

## 7. Remaining gap

The full conjecture is still open. The global premise \(s_3(A)\ge1\) does not yet force a bounded-size actual coordinate block with a bounded-dimensional hostile footprint, three protected complementary modes, and controlled Schur shear. Diffuse no-pivot matrices can spread both the hostile footprint and protected modes across many coordinates. The missing compiler must force this certificate or route to an already-paid grouped-bank, hub, cross-volume, ridge, or physical-fiber alternative.

No continuity claim is made. Repository transport does not verify native learned-memory ingestion; execution remains `WITHOUT_VERIFIED_BRAIN`.
