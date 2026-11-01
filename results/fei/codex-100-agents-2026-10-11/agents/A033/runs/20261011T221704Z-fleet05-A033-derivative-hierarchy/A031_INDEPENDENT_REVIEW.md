# Independent A033 reconstruction of A031 v1

Source: A031's DERIVATION.md and CLAIMS.json, run 20261011T214115Z-fleet05-A031-convolution-identity. No author code was executed, and no repair was supplied. This is an accepting source-bound review at the stated scopes, subject to supervisor adoption; it does not replace the requested A088/A094 reviews.

For an arbitrary real Fourier vector b let v(x)=sum_S b_S chi_S(x). If f is Boolean, multiplication T_f:v->fv is a self-adjoint isometry and involution: <fv,fw>=<v,w>, f(fv)=v. In Fourier coordinates its matrix is M_(U,S)=a_(U xor S). This physical-space reconstruction gives M^2=Id independently of the author's matrix-convolution derivation.

Choose b_S=a_S ell_S. Then c=Mb, c_0=<f,v>=sum p ell=H and Mc=b. Its R-coordinate gives a_R(ell_R-H)=sum_(U!=0)a_(R xor U)c_U. Weighted Cauchy with |U| yields p_R(ell_R-H)^2<=J_R E_log. Isometry gives sum_(U!=0)c_U^2=sum p ell^2-H^2. All sums finite; zero atoms have b=0 and no undefined logs. A largest atom minimizes ell and therefore ell_R<=H. This proves every assertion in A031-SIGNED-ENTROPY-ANCHOR v1. Verdict: ACCEPT_AT_STATED_SCOPE.

For a point defect on n bits, a_0=1-2/N, |a_U|=2/N for U!=0, and all nonzero ell equal ell_tail. Subtract ell_tail using the exact nonempty convolution cancellation. Hence c_U=a_0 a_U(ell_0-ell_tail), E_log=p_0 I Delta^2, Delta=2log2(N/2-1). Since p_0->1 and Delta/n->2, E_log/I~4n^2. No constant payment is possible.

For a product f*g on disjoint cubes, ell_(S,T)=ell_S+ell_T and the two Fourier sums factor with full cancellation: c_(U,V)=c_U(f)*1_(V=0)+1_(U=0)*c_V(g). E_log is additive. For t copies of the 3-bit point defect, p_R=(9/16)^t, I=3t/4, and E_log=t E_log(h)>0. Since every nonempty U has |U|<=3t,

    J_R>= [1-p_R]/(3t),
    sqrt(J_R E_log/p_R)>=sqrt(E_log(h)[1-p_R]/3)*(16/9)^(t/2).

This is exponential in t. It refutes the second payment precisely as A031 states. Verdict: ACCEPT_AT_STATED_SCOPE for A031-ANCHOR-POSITIVE-PAYMENT-NOGO v1. The point-defect calibration H<8I and its reciprocal-binomial asymptotic are not required premises for either registered claim.

Independent exact verification: check_derivatives.py tests multiplication by f and convolution in two separate representations for every n<=3 Boolean table and a nonconstant rational Fourier weight b_S=a_S(|S|+1). It verifies their equality, the isometry, and involution exactly. Rational weights test the linear operator, while the analytic argument above handles the logarithmic weight. This is independent proof reconstruction plus finite support; it is not a finite extrapolation.
