# A two-coordinate physical leaf pair handles arbitrary canonical leakage

**Status:** Proved all-level sufficient theorem for the canonical original-product quadratic, with an optimized two-dimensional square-root estimate. It is uniform in the hub law, tail fragmentation, signs, and coefficients \(\beta,\varepsilon\), but deteriorates when all physical \((L,V)\) minors are small.

Let \(H,X_1,\ldots,X_n\) be independent real variables, each with a density bounded by one, and let \(L=\ell\cdot X\), \(V=v\cdot X\), \(P=p\cdot X\) for arbitrary real coefficient vectors. Suppose two distinct original leaf coordinates \(i,j\) satisfy
\[
 D=\ell_i v_j-\ell_jv_i\ne0.
\]
For every real \(\beta,\varepsilon\), the quadratic
\[
 Q=2HL+\beta L^2+V^2+2\varepsilon LP
\]
has an all-level density bound
\[
 \|p_Q\|_\infty\le3\cdot2^{2/3}|D|^{-2/3}.
 \tag{1}
\]
No orthogonality of \(\ell,v,p\), variance bound, or support regularity is needed. In the canonical orthonormal triple, this is an admissible original-product result for every mixed-sign spectral configuration.

## Optimized planar square-root lemma

If \(H\) is independent of a planar random pair \((l,w)\), \(\|f_H\|_\infty\le1\), the planar joint density is bounded by \(K\), and \(r(l)\) is any real measurable function, then
\[
 \bigl\|p_{2Hl+r(l)+w^2}\bigr\|_\infty
 \le3\cdot2^{2/3}K^{2/3}.
 \tag{2}
\]
For a threshold \(R>0\), integrate \(H\) first on \(|l|\ge R\) to bound that part of the output density by \(1/(2R)\); no density cap on \((l,w)\) is needed there, only its total probability mass. For \(0<|l|<R\), dominate the planar law by \(K\), integrate over the two preimages of the square \(w^2\), and rearrange the resulting square-root kernel against the cap-one probability law of \(H\). At every target level \(s\), the latter integral is at most \(\sqrt{2/|l|}\), independently of \(s,r(l)\). Hence the low-\(l\) contribution is at most
\[
 K\int_{|l|<R}\sqrt{2/|l|}\,dl=4\sqrt2K\sqrt R.
\]
Minimize \(1/(2R)+4\sqrt2K\sqrt R\) at \(R=(4\sqrt2K)^{-2/3}\). The minimum equals
\(\tfrac32(4\sqrt2K)^{2/3}=3\cdot2^{2/3}K^{2/3}\), proving (2). A nonnegative test function or interval approximation handles conditional density versions.

## Physical-pair reduction

Condition on all leaves except the two original variables \((X_i,X_j)\). Their affine map to the **full** values \((L,V)\) has Jacobian determinant \(D\); since \(X_i,X_j\) are independent with density caps one, the conditional joint density of \((L,V)\) is bounded by \(K=|D|^{-1}\). The conditional value of \(P\) is an affine function \(P=\alpha L+\rho V+p_0\), because the pair map is invertible. Now complete the square without touching the independent hub:
\[
 \begin{split}
 Q&=2(H+\varepsilon p_0)L+(\beta+2\varepsilon\alpha)L^2
      +V^2+2\varepsilon\rho LV\\
  &=2(H+\varepsilon p_0)L+
    (\beta+2\varepsilon\alpha-\varepsilon^2\rho^2)L^2
      +(V+\varepsilon\rho L)^2.
 \end{split}
\]
The shear \((L,V)\mapsto(L,W=V+\varepsilon\rho L)\) has determinant one, so \((L,W)\) retains the conditional density cap \(|D|^{-1}\). The translated hub \(H+\varepsilon p_0\) remains independent of that planar pair with density cap one. Apply (2) with \(K=|D|^{-1}\), then average the bound over the conditioned other originals to get (1).

The original unoptimized planar lemma appears in the archived exact physical-coloop report at commit c8542016844451bfa5585e5e15a89ed84f1602cb. The gain \(|D|^{-2/3}\), rather than \(|D|^{-1}\), follows solely from optimizing the high/low \(L\) threshold and applies to that earlier lemma too.
