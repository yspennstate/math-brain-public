# QFORM one-hub transverse compression handoff

Status: new scoped deterministic lemma; full bounded-density conjecture OPEN.

Read the complete proof and exact scope: https://github.com/yspennstate/math-open-problems/blob/master/proofnet24/QFORM-density/interactive/20260923T185357Z-one-hub-transverse-compression/REPORT.md

For any original physical coordinate \(h\), write \(A=\left(\begin{smallmatrix}a&w^T\\w&B\end{smallmatrix}\right)\), \(w\ne0\), and \(P=I-ww^T/\|w\|^2\). The matrix \(A-\operatorname{diag}(a,PBP)\) has rank at most two. Thus \(s_3(A)\le\max(|a|,\|PBP\|_{\rm op})\), and every no-pivot \(s_3(A)\ge1\) state has \(\|PBP\|_{\rm op}\ge1\) for each physical hub with \(|a|<1\).

When \(a=0\), the leading hub/coupling \(2\times2\) block has an exact Schur complement \(PBP\), so \(\operatorname{rank}A=2+\operatorname{rank}(PBP)\) and inertia adds \((1,1)\). Exact rank three therefore reduces algebraically to \(2tX_hL+\beta L^2+2L\langle u,X'\rangle+\lambda V^2\), where \(|\lambda|\ge1\). The component of \(u\) perpendicular to both \(L,V\) is the unpaid transverse leakage.

Next targeted question: convert this operator-norm transverse curvature into a physical-coordinate product-law receiver that is uniform as transverse leakage tends to zero and tolerates additional spectral terms. Do not treat a rotated coordinate as independent, or delete a small quadratic remainder for unbounded rough laws. These are the same analytic obstacles isolated in the current manuscript; this lemma does not close them.

Original math repository commit: b7df69e5b8139142f4060c9b66ccf3005c8b625f.

Paid exact-rank-three branch: If the hub diagonal is zero and the transverse leakage component vanishes, the physical hub-to-light coupling norm \(t=\|Ae_h\|\) is at least \(s_3(A)\ge1\), because \(e_h\) lies in the range of the rank-three matrix. Scaling the independent hub by \(t\) preserves the density cap. The manuscript's independent-hub transverse-square theorem then yields \(\|p_Q\|_\infty\le 2\sqrt2+\sqrt2\log(1/3+4\sqrt2)<5.361\) without a spread, moment, or support assumption. The remaining analytic difficulty is the uniform transition with a nonzero transverse leakage component, and arbitrary extra spectrum.

Updated math proof commit: ff0c4de93faaff0eb572d03ce6439fe8dcb230d1.


Further exact-rank-three spectral reserve: after completing the light square, set \(\beta'=\beta-u_v^2/\lambda\), \(t=\|w\|\), \(u_\perp\perp e,v\). The remaining rank-two star has smaller singular value \((\sqrt{(\beta')^2+4(t^2+\|u_\perp\|^2)}-|\beta'|)/2\). Since the discarded square is rank one, \(s_3(A)\ge1\) implies \(t^2+\|u_\perp\|^2\ge1+|\beta'|\). In particular, a tiny physical hub edge requires an order-one transverse shear reserve. This remains a matrix-algebra condition, not an independent-coordinate density receiver.

Current math proof commit: a499ab4706b29fa1e864fad1291a9269c22793d5.


New paid nonzero-leakage branch: In the exact-rank-three null-hub normal form, if the transverse shear vector \(u_\perp\) is supported on original light coordinates disjoint from the supports of both \(e=w/\|w\|\) and \(v\), then \(P_0=\langle u_\perp,X'\rangle\) is independent of \((L,V)\). Thus \(Y=tX_h+P_0\) is also independent. The exact spectral reserve \(t^2+\|u_\perp\|^2\ge1\), plus the one-dimensional product-projection density estimate, gives \(\|p_Y\|_\infty\le2\). Use \(Z=2Y\) (density cap one) and scale the output: \(2Q=2ZL+2\lambda(V+(u_v/\lambda)L)^2+2\beta'L^2\). The pure independent-hub theorem gives \(\|p_Q\|_\infty<8.913\), uniformly even as nonzero leakage tends to zero. Explicit physical support disjointness is essential; overlapping-support leakage remains open.

Latest math report commit: 66123567266645e7a6dfdac671c86db6090b9fe4.

Source-scope clarification: apply the pure-hub theorem with the light product vector consisting only of the original coordinates supporting (e,v). The synthetic hub (2Y) depends on the disjoint original coordinates (h) and (T), so it is independent of that entire light product vector. Math report clarification commit: 9e2cbdb25195b4f806bcfcd9ff28dc1d687e6b0d.
