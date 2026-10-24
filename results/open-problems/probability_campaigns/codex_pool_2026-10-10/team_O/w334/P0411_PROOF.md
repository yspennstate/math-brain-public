P0411: exact integral consequences
Label: author-checked proof for the displayed normalized integral; cached source identification checked and blind audit pending. The even-dimensional density and median questions remain open here.

Put n = d-1 >= 1 and, for q > 0, define
I_n(q) = integral over R^n of [sqrt((q+1)^2/4+|z|^2)-(q-1)/2]^(-2n) dz,
c_n = I_n(1), and H_d(u) = c_n exp(-n u)/I_n(exp(2u)).
This is the exact representation quoted in the existing P0411 attempt card. The representation has now been checked against the cached paper, Proposition 5.1 and formula (5.1), arXiv:2303.16831. Substitute x=exp(-u)z in its integral for 1/H_d(u): this gives exactly the displayed normalized I_n formula. Physical radii satisfy u>=0. Conjecture 7.5 was also read in the cached text: its even-dimensional clause explicitly uses the variable u in H_d(u)=exp(-(d-1)u)/f(u), so the sixth coefficient targets that literal clause. These are author source checks, not an independent KEEP.

1. Strict monotonicity. The bracket is at least 1 and is positive. Its q derivative is (q+1)/(4 sqrt((q+1)^2/4+|z|^2))-1/2, which is strictly negative when z is nonzero. The integrals are finite: the integrand is bounded near zero and is O(|z|^(-2n)) at infinity. Pointwise strict comparison on a set of positive measure gives I_n(q_2)>I_n(q_1) for q_2>q_1. Hence exp(nu)H_d(u)=c_n/I_n(exp(2u)) strictly decreases. No interchange of derivative and integral is required.

2. Odd d = 2m+1. In radial coordinates substitute w = sqrt((q+1)^2/4+r^2)-(q-1)/2. Then r^2=(w-1)(w+q), w >= 1, and r dr=(w+(q-1)/2)dw. After the surface-area factor cancels in normalization,
I_(2m)(q)/surface_area = integral from 1 to infinity of w^(-4m)(w-1)^(m-1)(w+q)^(m-1)(w-1/2+q/2) dw.
Every coefficient of q in this polynomial is strictly positive: expand (w+q)^(m-1); both w-1/2 and 1/2 are positive on w >= 1. The degree is m. Explicitly, put B(a,b)=(a-1)!(b-1)!/(a+b-1)! for positive integers. For k=0,...,m,
A_(m,k) = binom(m-1,k)[B(2m+k,m)-B(2m+k+1,m)/2]
             + binom(m-1,k-1)B(2m+k,m)/2,
with out-of-range binomial coefficients zero. Then
p_m(q) = [2/B(m,m)] sum_(k=0)^m A_(m,k) q^k,
1/H_(2m+1)(u) = exp(2m u) p_m(exp(2u)).
The beta identity follows from t=1/w. Each coefficient is a positive rational number. At q=1 the original radial integral equals B(m,m)/2, so p_m(1)=1. For m=1 this gives p_1(q)=(q+2)/3.

3. Dimension two and a negative Maclaurin coefficient. Here n=1, c_1=pi. In the original integral substitute z=exp(u)cosh(u)sinh(v). With b=tanh(u), let L(b)=integral over R of 1/(cosh(v)-b) dv. The substitution x=tanh(v/2) gives L(b)=4 cosh(u) arctan(exp(u)). Moreover integral cosh(v)/(cosh(v)-b)^2 dv = L(b)+b L'(b). Differentiating this explicit expression yields
1/H_2(u) = [4 cosh(u)^2 arctan(exp(u))+2 sinh(u)]/pi.
At u=0 this is 1, as required by normalization.

Let S(u)=integral from 0 to u of sech(v) dv. Since arctan(exp(u))=pi/4+S(u)/2,
f(u)=exp(-u)/H_2(u)
     = exp(-u)cosh(u)^2 + (2/pi)exp(-u)[cosh(u)^2 S(u)+sinh(u)].
Now S(u)=u-u^3/6+u^5/24+O(u^7), and
cosh(u)^2 S(u)+sinh(u)=2u+u^3+13u^5/60+O(u^7).
The first term has sixth coefficient (1+2+3^6)/(4*6!)=61/240. The second has sixth coefficient (2/pi)[-2/120-1/6-13/60]=-4/(5pi). Therefore
[u^6] f = 61/240-4/(5pi) < 61/240-14/55 = -1/2640 < 0,
using the classical bound pi<22/7. Thus positivity of all Maclaurin coefficients is false for this function in u. This does not refute a claim phrased in another variable or about another density.

Checks: normalization at u=0; the n=d-1 convention; the factor in the radial Jacobian; convergence at infinity; the factor 2/pi; and the literal variable in the source statement. The literal variable has been checked in cached Conjecture 7.5; the independent auditor must verify the identification and coefficient argument. The accompanying exact series computation and positive-coefficient calculations check the algebra, not the source identification.
