# Canonical overlapping light: a bounded-variance product-source case

**Status:** Proved scoped all-level consequence of the two-bank Rényi-tail Fourier theorem. This applies to genuine original-coordinate products, including arbitrary translates of single unit-interval laws. It does not establish the unrestricted conjecture: original density caps alone permit arbitrarily large or infinite variances and do not give the required tail sum.

## Abstract two-bank statement

Let \(H\) have a probability density at most one and be independent of two random light-bank vectors \(A=(L_A,V_A,P_A)\) and \(B=(L_B,V_B,P_B)\). Assume \(A,B\) are independent, have joint three-dimensional densities bounded by \(M_A,M_B\), and have finite \(P\)-coordinate variances at most \(V_A,V_B\). For \(L=L_A+L_B\), \(V=V_A+V_B\), \(P=P_A+P_B\), and **every** \(\beta,\varepsilon,s\in\mathbb R\), the output
\[
 Q=2HL+\beta L^2+V^2+2\varepsilon LP
\]
has an essentially bounded density with
\[
\|p_Q\|_\infty
 \le C(M_A M_B)^{1/3}
       (1+V_A)^{1/6}(1+V_B)^{1/6},
 \tag{1}
\]
where \(C\) is an absolute constant. No independence of \(L_j,V_j,P_j\) **within** either bank is assumed. The bank means can be arbitrarily large, and the estimate is uniform in them.

The ingredient is the proved all-\(\beta\) two-bank Rényi-tail theorem: with unit P-bin masses \(m_{A,k}=\mathbb P(P_A\in[k,k+1))\) and \(m_{B,j}\) analogously, it gives
\[
 \|p_Q\|_\infty\le3\cdot2^{2/3}(M_A M_B)^{1/3}
 \Big(\sum_k m_{A,k}^{2/3}\Big)
 \Big(\sum_j m_{B,j}^{2/3}\Big).
 \tag{2}
\]
For a scalar \(Z\) with variance at most \(V\), set \(R=\max(1,\sqrt V)\) and divide the probability mass of each unit bin among the central region \(S_{-1}=\{|Z-\mathbb EZ|<R\}\) and outer regions \(S_j=\{2^jR\le|Z-\mathbb EZ|<2^{j+1}R\}\). Write \(m_{k,j}=\mathbb P(Z\in I_k,\,Z\in S_j)\). The central region meets at most \(2R+3\) bins and has total mass at most one. The \(j\)-th outer region meets at most \(C2^jR\) bins and Chebyshev bounds its total mass by \(V/(2^jR)^2\). Apply \((\sum_jm_{k,j})^{2/3}\le\sum_jm_{k,j}^{2/3}\) and Hölder's inequality \(\sum_{k\in S}m_{k,j}^{2/3}\le |S|^{1/3}(\sum_{k\in S}m_{k,j})^{2/3}\) to get
\[
 \sum_{k\in\mathbb Z}m_k^{2/3}
 \le C R^{1/3}
   +C\sum_{j\ge0}(2^jR)^{1/3}
       \bigl(V/(2^jR)^2\bigr)^{2/3}
 \le C_0R^{1/3}\le C_0(1+V)^{1/6}.
 \tag{3}
\]
Equations (2)–(3) prove (1). The positive bin decomposition is why arbitrary shifts of \(P_A,P_B\) cause no loss.

The same shell proof works for a direct **bank-level** moment bound \(\mathbb E|P_j-c_j|^p\le W_j\), for some real center \(c_j\), with any \(p>1/2\): choose \(R=\max(1,W_j^{1/p})\). The outer shell series has ratio \(2^{(1-2p)/3}<1\), giving \(\sum_km_{j,k}^{2/3}\le C_p(1+W_j)^{1/(3p)}\). Consequently (2) bounds the canonical density by \(C_p(M_AM_B)^{1/3}(1+W_A)^{1/(3p)}(1+W_B)^{1/(3p)}\). This is an abstract bank condition; a common \(p\)-moment bound on many individual originals does not by itself verify the required bank moment uniformly in dimension when \(p<2\).

## Genuine original-coordinate product corollary

Let the leaf originals \(X_i\) be independent, each with a probability density at most one and \(\operatorname{Var}(X_i)\le V_0\), with no restriction on their individual means. Let \(\ell,v,p\) be **orthonormal** coefficient vectors on those original coordinates, and suppose the maximum row leverage obeys
\[
 \max_i(\ell_i^2+v_i^2+p_i^2)\le1/24.
\]
Randomly split the leaf originals into independent banks \(A,B\). With positive probability each restricted Gram matrix of \((\ell,v,p)\) lies between \(I_3/4\) and \(3I_3/4\): the Frobenius variance of its deviation from \(I_3/2\) is at most \((3/4)(1/24)=1/32<1/16\), so a physical cut with both Gram bounds exists. The standard fixed-dimensional projection-density bound for independent cap-one originals then gives absolute joint density caps \(M_A,M_B\le M_3\) for the three-dimensional bank projections. Independence of the original coordinates gives
\[
 \operatorname{Var}(P_A)=\sum_{i\in A}p_i^2\operatorname{Var}(X_i)\le V_0,
 \qquad
 \operatorname{Var}(P_B)\le V_0.
\]
Therefore (1) gives \(\|p_Q\|_\infty\le C M_3^{2/3}(1+V_0)^{1/3}\), uniform in the number of leaf originals, both spectral signs, every \(\varepsilon\), and even arbitrary \(\beta\). The hub original \(H\) needs only its density cap and independence; it need not have bounded variance.

In particular, every leaf \(X_i\) **uniform on any single interval of length one**, with arbitrary center, satisfies \(\operatorname{Var}(X_i)=1/12\). Such genuine original-product inputs meet this theorem uniformly, including the difficult-looking negative-target range \(|\varepsilon|\ll-s\ll1\). This is a scoped conclusion because the full problem allows disconnected densities with unbounded centered variance and no uniform Rényi-tail sum.

For this interval subclass, Hoeffding's inequality gives the stronger bank tail
\(\mathbb P(|P_A-\mathbb EP_A|\ge t)\le2e^{-2t^2}\), since every summand \(p_iX_i\) is supported on an interval of length \(|p_i|\) and \(\sum_{i\in A}p_i^2\le1\); likewise for bank B. Thus the Rényi sums in (2) are bounded directly by a Gaussian series. The variance proof above also covers many non-interval laws, including unbounded-support originals with a common finite variance bound. A separate archived exact-rank-three unit-interval result already covers the interval case within its spectral gate. The present Fourier corollary is useful chiefly because it handles broader finite-variance laws and arbitrary \(\beta,\varepsilon\); the canonical quadratic has rank three in the span of \(H,L,V,P\), since \(H\) and \(P\) appear only through \(H+\varepsilon P\).

The exact all-\(\beta\) two-bank Rényi-tail theorem and its proof are at `proofnet24/QFORM-density/interactive/20260923T205630Z-finite-p-support-fourier/ALL_BETA_ADDENDUM.md` in the same research repository. Its theorem does not allow arbitrary bank-local quadratic phases, and neither does the present application.
