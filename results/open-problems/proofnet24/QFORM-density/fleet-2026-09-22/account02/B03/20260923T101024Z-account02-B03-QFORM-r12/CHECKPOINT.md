# account02/B03 r12 — early substantive checkpoint

Programme `QFORM-DENSITY-3EIG-20260922`.  Full target remains open.

I am attacking the strict heavy-row / near-coloop collar by isolating the selected physical right-row before the Fresnel time integral.  The useful new calculation is an L^p-L^q split that keeps the whole original product bank and never conditions on a sum/difference variable.

Let X be a cap-one physical coordinate, Y=(Y_j) an independent cap-one product bank, and Omega independent of (X,Y).  Let U=U(Omega) have density <=L while xi(Omega),F(Omega) may depend arbitrarily on U.  For nonzero A,d,alpha and

T=A(alpha X+h.Y+xi)^2+2d U(bX+g.Y)+F,

put row vectors r_j=(h_j,g_j) and G=sum_j r_j r_j^T.  Assume G>0.  After the e5 Fresnel linearisation and eta=2td u,

|phi_T(t)| <= (4 pi |tA|)^(-1/2)(2|td|)^(-1)
 int p_U(eta/(2td)) |chi_X(alpha s+b eta)| prod_j |Psi_j(h_j s+g_j eta)| ds d eta.

Take p>2 and q=p/(p-1)<2.  The first two factors have

||p_U(eta/T0) chi_X(alpha s+b eta)||_p^p
 <= (2 pi) T0 L^(p-1)/|alpha|,

using |chi_X|<=1 and Plancherel int|chi_X|^2<=2pi.  If ell_j=r_j^T G^(-1)r_j and max ell_j<=q/2, geometric BL plus the required e5 bound int|Psi|^r<=4pi/sqrt(r), r>=2, gives

||prod_j Psi_j(r_j.(s,eta))||_q^q
 <= (16 pi^2/q) det(G)^(-1/2).

Holder therefore gives pointwise decay

|phi_T(t)| <= K_q |t|^(-beta),
 beta=1/2+1/q>1,

K_q=(4pi)^(-1/2)2^(-1/q)(2pi)^(1/p)(16pi^2/q)^(1/q)
     L^(1/q)|A|^(-1/2)|d|^(-1/q)|alpha|^(-1/p)det(G)^(-1/(2q)).

This is already a real L1-time implication whenever the deletion-plane leverage has any strict margin below one.  For the clean choice q=3/2 (p=3), requiring max ell_j<=3/4,

K=(4 pi^(7/6)/3^(2/3)) L^(2/3)|A|^(-1/2)|d|^(-2/3)
  |alpha|^(-1/3)det(G)^(-1/3),

so Fourier inversion yields

||p_T||_infinity
 <= 7*2^(12/7)*3^(-4/7)
    L^(4/7)|A|^(-3/7)|d|^(-4/7)|alpha|^(-2/7)det(G)^(-2/7).

Next I am inserting the exact account03/B03 one-sided geometry.  For the selected heavy row r, alpha=h_r and det G=m^2(1-eta_r).  The two existing spectral inequalities gamma|sigma|>=s^2 and gamma sigma^2>=s^3 combine exactly as

(gamma|sigma|)^(2/7)(gamma sigma^2)^(1/7)
 = gamma^(3/7)|sigma|^(4/7) >= s,

which is the exponent needed to make the new bound target-homogeneous.  The remaining work is to write this splice carefully, state the precise surviving collar, and check constants/source scopes before publication.
