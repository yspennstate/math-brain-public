SIGNED IN - working on the quadratic-form bounded-density conjecture (universal constant), account account04, slot B12, 2026-09-24T00:21:54Z.
attacking: a multidimensional hub-aligned shear theorem yielding an actual six-mode principal square-Gram gate under arbitrary signed aligned spectral packets and a deterministic dense local-row tail.

# account04/B12 — multidimensional hub-aligned spectral-packet stability

Programme: `QFORM-DENSITY-3EIG-20260922`  
Run: `20260924T002154Z-account04-B12-multihub-shear-r8`  
Status: **PROVED SUPPORTING STABILITY THEOREM / FULL QFORM OPEN**  
Continuity: **not claimed; the compiler used below gives essential boundedness.**

## 1. Scope and source pins

The target remains the unrestricted product-law statement: the coordinates are independent real variables with arbitrary probability densities bounded by one; the coefficient matrix is arbitrary symmetric and has at least three singular values at least one. No moment, support, iid, log-concavity, Gaussian, or post-rotation independence hypothesis is added.

Fresh owner control, current request, assignment, correction inbox, and memory protocol were read from `yspennstate/math-research-brain/main`. The source corrections excluding arbitrary-joint coarea, conditional-cap independence, a universally good fixed minor, and treating a small matrix as a small random quadratic error are retained.

The completed designated partner actually applied is account01/B12:

- commit `ed9688b66bfacef09bc1203f55f3649b5b8f8cc9`;
- `proofnet24/QFORM-density/fleet-2026-09-22/account01/B12/20260923T231842Z-account01-B12-QFORM-auto11/REPORT.md`;
- theorem `QFORM-HUB-ALIGNED-SPECTRAL-PACKET-STABILITY-v1`.

Its exact shear identity and shear singular factor are used below. The actual density receiver is the completed account02/B12 six-mode theorem at commit `c635fcdce6aa206c68f1f14e061cf617d72376fb`, `QFORM-SIX-SQUARE-MODE-PAIR-COMPILER-v2`.

The required Claude package at `e5f71d79eff325201dd0274053d20268ce65b837` and the later hub continuation at `c4c23b784395630c094ba299a50712209921d1ae` were retained at their proved scopes. Nothing below assumes the open single-hub conditional-adaptation estimate.

## 2. Aligned packets on a physical hub plane

Split the ORIGINAL coordinates as \(H\sqcup J\), where \(|H|=m\). Let \(U\in\mathbb R^{m\times p}\) have orthonormal columns. Suppose a baseline has physical blocks
\[
 C_0=U\Lambda_0U^T,\qquad
 B_0=UW_0^T+R,\qquad U^TR=0.
\tag{2.1}
\]

Let
\[
 E=\sum_a\theta_a v_av_a^T
\tag{2.2}
\]
be any finite signed spectral packet. No restriction is imposed on the number, signs, or magnitudes of the \(\theta_a\). Assume only that every physical footprint lies in the same \(p\)-plane:
\[
 P_Hv_a=Uz_a .
\tag{2.3}
\]
Writing \(b_a=P_Jv_a\), its physical blocks are exactly
\[
 E[H,H]=U\left(\sum_a\theta_a z_az_a^T\right)U^T,
\qquad
 E[H,J]=U\left(\sum_a\theta_a z_ab_a^T\right).
\tag{2.4}
\]
Consequently \(A_*=A_0+E\) has
\[
 C_*=U\Lambda U^T,\qquad B_*=UW^T+R,
\tag{2.5}
\]
where
\[
 \Lambda=\Lambda_0+\sum_a\theta_a z_az_a^T,\qquad
 W^T=W_0^T+\sum_a\theta_a z_ab_a^T.
\tag{2.6}
\]
The transverse carrier \(R\) is exactly invariant. Thus arbitrarily many unbounded signed modes collapse to the two aggregate objects \(\Lambda,W\) on the physical hub plane.

## 3. Exact multihub shear bound

Assume \(\Lambda\) is invertible and define
\[
 Q=U\Lambda^{-1}W^T,\qquad
 t=\|Q\|_{\rm op}=\|\Lambda^{-1}W^T\|_{\rm op}.
\tag{3.1}
\]
Then \(C_*Q=UW^T\). For the actual physical row block
\[
 M_*=[C_*,B_*]
\tag{3.2}
\]
the account01/B12 inverse-free shear identity gives
\[
 M_*
 \begin{pmatrix}I_m&-Q\\0&I_J\end{pmatrix}
 =[C_*,R].
\tag{3.3}
\]

Account01/B12 proved for rank one the exact factor
\[
 \gamma(t)=\frac{\sqrt{t^2+4}-t}{2}
          =\frac{2}{\sqrt{t^2+4}+t}.
\tag{3.4}
\]
For general \(Q\), apply left and right orthogonal transformations from an SVD of \(Q\). The shear decomposes into \(2\times2\) blocks
\[
 \begin{pmatrix}1&\sigma_j(Q)\\0&1\end{pmatrix}
\]
and identity blocks. Therefore the same account01 factor applies at the concrete equation
\[
 s_{\min}\!\begin{pmatrix}I_m&Q\\0&I_J\end{pmatrix}
 =\gamma(\|Q\|_{\rm op}).
\tag{3.5}
\]

Because \(U^TR=0\),
\[
 [C_*,R][C_*,R]^T
 =U\Lambda^2U^T+RR^T
\tag{3.6}
\]
is an orthogonal range sum. Hence, for every \(\ell\) with \(p+\ell\le m\),
\[
 s_{p+\ell}([C_*,R])
 \ge \min\{s_p(\Lambda),s_\ell(R)\}.
\tag{3.7}
\]
Combining (3.3), (3.5), and (3.7) yields
\[
 \boxed{
 s_{p+\ell}(M_*)
 \ge
 \gamma(\|\Lambda^{-1}W^T\|_{\rm op})
 \min\{s_p(\Lambda),s_\ell(R)\}.
 }
\tag{3.8}
\]

This is magnitude-free in every individual added eigenvalue. It spends no reserve direction on the number or rank of the aligned packet.

## 4. Dense local-row tail and actual principal-square gate

Let \(T=T^T\) be arbitrary and put
\[
 A=A_*+T,\qquad
 \varepsilon=\|P_HT\|_{\rm op}.
\tag{4.1}
\]
Only the rows touching \(H\) are charged. In particular, the entire \(J\times J\) block of \(T\) may have arbitrary norm and spectrum. Singular-value Weyl gives
\[
 \boxed{
 \sqrt{\lambda_{p+\ell}((A^2)[H,H])}
 =s_{p+\ell}(P_HA)
 \ge
 \gamma(\|\Lambda^{-1}W^T\|_{\rm op})
 \min\{s_p(\Lambda),s_\ell(R)\}
 -\varepsilon .
 }
\tag{4.2}
\]
This is an ACTUAL principal-compression spectral gate for the final matrix. No claim is made that \(X^TTX\) is small. If merely \(\|T\|_{\rm op}\le\varepsilon\), then (4.1) follows, so (4.2) includes arbitrary full-rank small dense additional spectrum of either sign.

Likewise, any extra signed spectral packet with all eigenvalues in \([-h,h]\) is absorbed by replacing \(\varepsilon\) with \(\varepsilon+h\), irrespective of its rank and orientation.

### Theorem 4.1 — `QFORM-MULTIHUB-ALIGNED-SPECTRAL-PACKET-STABILITY-v1`

Assume \(m\ge6\), \(p+\ell\ge6\), and
\[
 g=
 \gamma(\|\Lambda^{-1}W^T\|_{\rm op})
 \min\{s_p(\Lambda),s_\ell(R)\}
 -\varepsilon
 >0.
\tag{4.3}
\]
Then every independent cap-one product input satisfies
\[
 \boxed{
 \|p_{X^TAX}\|_{\infty,\mathrm{ess}}
 \le \frac{C_m}{g},
 }
\tag{4.4}
\]
where, with \(N_2=\binom m2\),
\[
 C_m=\max\left\{
 8N_2\sqrt{6\pi m},\
 4\pi N_2,\
 3\,400^{1/3}(4N_2)^{5/6},\
 10\sqrt{2e/3}
 \right\}.
\tag{4.5}
\]

Indeed, (4.2) and \(p+\ell\ge6\) imply
\[
 \sqrt{\lambda_6((A^2)[H,H])}\ge g.
\tag{4.6}
\]
The completed account02/B12 six-mode compiler now applies to the actual final matrix \(A\), giving (4.4). This uses only original-coordinate conditioning inside that compiler.

## 5. Concrete target-class family

Take \(m=6\), \(p=2\), \(\ell=4\), and
\[
 U=(e_1,e_2),\qquad
 R=2\begin{pmatrix}0_{2\times4}\\I_4\end{pmatrix}.
\tag{5.1}
\]
Thus \(s_4(R)=2\). Permit any finite signed spectral packet whose \(H\)-projections lie in \({\rm Ran}(U)\), with arbitrary number, signs, ranks, and individual magnitudes, subject only to the final aggregate conditions
\[
 s_2(\Lambda)\ge4,\qquad
 \|\Lambda^{-1}W^T\|_{\rm op}\le1.
\tag{5.2}
\]
Also permit an arbitrary symmetric tail \(T\) satisfying only
\[
 \|P_HT\|_{\rm op}\le\frac1{100}.
\tag{5.3}
\]
The complement-only part of \(T\) is unrestricted.

Since \(\gamma(1)=(\sqrt5-1)/2\), (4.2) gives
\[
 \boxed{
 \sqrt{\lambda_6((A^2)[H,H])}
 \ge 2\gamma(1)-\frac1{100}
 =1.2260679774997898\ldots .
 }
\tag{5.4}
\]
For \(m=6\), \(N_2=15\), and
\[
 C_6=720\sqrt\pi
 =1276.1667726519715\ldots .
\tag{5.5}
\]
Therefore
\[
 \boxed{
 \|p_{X^TAX}\|_{\infty,\mathrm{ess}}
 <1040.862 .
 }
\tag{5.6}
\]

This family genuinely lies in the original target class. Coordinate row projection is a contraction, so
\[
 s_6(P_HA)\le s_6(A).
\tag{5.7}
\]
Equations (5.4)-(5.7) imply
\[
 s_6(A)>1,\qquad\text{hence}\qquad s_3(A)>1.
\tag{5.8}
\]

Thus the theorem covers an actual target-class family with arbitrarily many unbounded added modes of both signs, a two-dimensional physical hub footprint, arbitrary complement spectrum, and a fully nonseparable dense tail. The tail is charged only at the deterministic final-matrix gate.

## 6. What is new and what remains open

The account01 theorem handled a one-dimensional hub footprint and used a specialized rank-one-self receiver. The theorem here handles an arbitrary \(p\)-dimensional aligned physical footprint. In particular, the first new case \(p=2,\ell=4\) creates the six square-energy modes needed by the physical six-mode compiler; the number of unbounded signed added eigenmodes costs no spectral reserve.

The unrestricted conjecture remains open. Bare \(s_3(A)\ge1\) does not yet force a bounded original-coordinate set \(H\), a bounded-dimensional hub plane \(U\), four transverse carrier modes, and a controlled aggregate slope. The next structural obligation is to prove that failure of all such multihub certificates forces one of the already-paid projected-crossing, grouped-bank, ridge, physical-core, Schur, or Pluecker-volume exits.

No counterexample to the full conjecture was found.
