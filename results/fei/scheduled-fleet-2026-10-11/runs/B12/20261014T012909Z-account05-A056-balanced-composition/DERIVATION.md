# Biased controller with coherent shared-data rows

All entropies are bits. Write phi(r)=r log2(1/r), phi(0)=0, b=1/ln(2), A=b/e, B=3b+2. Let a(W) be a Boolean sign controller on a uniform block disjoint from data. Put c=(1-a)/2, p=E c, V=4p(1-p). Let G(S,X), H(S,Y) be Boolean signs with S,X,Y mutually disjoint uniform blocks. F=cG+(1-c)H. Empty blocks and constant functions are admitted. Branch means are unrestricted.

## Exact spectrum and physical influence

Embed branch Fourier coefficients x_T,y_T in the union data cube. Set q_T=(x_T-y_T)^2/4, alpha_T=p x_T+(1-p)y_T, d=sum_T q_T=P(G!=H). For every data T,

    Fhat(empty,T)=alpha_T,
    Fhat(U,T)=-ahat(U)(x_T-y_T)/2, U nonempty.

These follow directly from F=(G+H)/2-a(G-H)/2 and independence of W. Thus, with Hplus(a)=sum_{U nonempty} phi(ahat(U)^2),

    H(F)=d Hplus(a)+sum_T [phi(alpha_T^2)+V phi(q_T)].

The nonempty-control factorization uses phi(rs)=s phi(r)+r phi(s). Hence

    Pi=H(F)-p H(G)-(1-p)H(H)=d Hplus(a)+sum_T K_p(x_T,y_T),
    K_p(x,y)=phi((p x+(1-p)y)^2)+V phi((x-y)^2/4)
              -p phi(x^2)-(1-p)phi(y^2).

Conditioning on W gives each physical data influence p Inf_i(G)+(1-p)Inf_i(H), with a missing branch influence zero. Flipping controller coordinate i changes F exactly when a changes and G!=H, events on independent blocks. Thus

    I(F)=p I(G)+(1-p)I(H)+d I(a).

In particular a shared data bit contributes once, at its weighted actual influence. Neither d=(1-EG EH)/2 nor the disjoint-core mean-only entropy correction is valid when S is shared. Instead d=(1-<u,v>)/2, where u,v are the shared-block Fourier vectors of the conditional means E_XG, E_YH. Conditional private independence is essential to this last expression.

## Uniform-in-bias scalar price (including p=0,1)

We prove for all real x,y and 0<=p<=1,

    K_p(x,y) <= V [A |x^2-y^2| + B (x-y)^2/4].                 (1)

K is homogeneous of degree two: coefficients of log(scale^2) cancel because alpha^2+Vq=p x^2+(1-p)y^2. If max(|x|,|y|)=0 the result is immediate. Otherwise normalize this maximum to one. For f(z)=phi(z^2), f''(z)=-4 log2|z|-6b >= -6b on [-1,1] away from zero. f is continuously differentiable at zero, so f(z)+3bz^2 is convex on the whole interval. Jensen yields

    f(px+(1-p)y)-p f(x)-(1-p)f(y) <= 3b p(1-p)(x-y)^2=3b Vq.

Therefore K<=V[phi(q)+3bq]. If xy>=0, let h=|x-y|<=1. Here q=h^2/4, and maximization of w log2(1/w^2) gives phi(q)<=2b sqrt(q)/e=Ah. Also |x^2-y^2|=h(2-h)>=h. If xy<0 then q lies in [1/4,1], so phi(q)<=2q. Both cases imply (1); scale back using homogeneity. This is an analytic continuum proof, independent of the finite grid.

## Exact named residual and restricted admissions

Let C be all shared-only subsets, u=(x_T)_{T in C}, v=(y_T)_{T in C}. Define

    v_G=1-||u||_2^2, v_H=1-||v||_2^2,
    sigma=sum_{T in C}|u_T^2-v_T^2|.

Every T outside C belongs to at most one branch support, so sum_T |x_T^2-y_T^2|=v_G+v_H+sigma. Summing (1) gives the all-dimensional residual formula

    Pi <= d Hplus(a)+V [A(v_G+v_H+sigma)+B d].                 (2)

No unspecified collision term is deleted. Since ||u-v||_2^2>=0, v_G+v_H<=4d. Pointwise |m_G(s)-m_H(s)|<=1-m_G(s)m_H(s) for conditional means in [-1,1]. Taking any Fourier coefficient gives ||u-v||_infinity<=2d. If ||u||_1,||v||_1<=Lambda, then sigma<=4Lambda d. Therefore

    Pi <= d Hplus(a)+C_Lambda Vd,
    C_Lambda=4A(1+Lambda)+B.                                  (3)

One shared bit guarantees Lambda<=1; two guarantee Lambda<=2 by Cauchy-Schwarz and L2<=1. Thus C_1<11 and C_2<13. For an exact elementary constant certificate, ln2=2 atanh(1/3)>56/81 from its first two positive terms and e>8/3 from its first five series terms. Hence b<81/56, A<243/448, C_1<4784/448<11 and C_2<5756/448<13. These constants are deliberately not sharp. Fair-controller versions already have sharper reviewed constants; this extension is the variance-scaled bound for arbitrary current bias. General shared dimension t gives Lambda<=2^(t/2), which is not a universal constant.

If an independently supplied strong controller certificate is Hplus(a)<=T[I(a)-V], (3) implies

    Pi<=max(T,C_Lambda) d I(a),

using I(a)>=V. If only Hplus(a)<=T I(a) is supplied, the constant is T+C_Lambda. No universal strong controller certificate is asserted here.

## One normalized reference and exact retained terminal debt

Supply normalized seed references R_G,R_H positive on the branch Fourier supports. At EVERY shared-only atom replace R_j(T) by the true P_j(T); on the complement rescale the original reference to mass v_j. Zero complement mass is absorbed. Denote calibrated references R_j^c and costs c_j^c. The categorical KL chain rule over each shared atom and the remaining complement proves c_j^c<=c_j; the conditional complement debt survives exactly.

Set R_T=p x_T^2+(1-p)y_T^2 and r_T=p R_G^c(T)+(1-p)R_H^c(T). For R_T>0 define a single stochastic kernel on controller subsets:

    L(empty|T)=alpha_T^2/R_T,
    L(U|T)=ahat(U)^2 q_T/R_T for U nonempty.

Normalization follows from alpha_T^2+Vq_T=R_T. If R_T=0 put L(empty|T)=1. Then Q(U,T)=r_T L(U|T) is a normalized reference, including reference-only off-support mass. It is fixed for the instance before drawing a spectral output. Because shared atoms were each calibrated and private atoms identify their unique child,

    D(P_F||Q)=p D(P_G||R_G^c)+(1-p)D(P_H||R_H^c),
    CE(P_F,Q)=p c_G^c+(1-p)c_H^c+Pi.                         (4)

One can verify these equalities directly: conditional KL vanishes since both true and reference use L; on shared atoms r=R, and on branch-unique atoms the factor p or 1-p cancels in P/reference ratios. This proves the biased analogue of the reviewed fair A097 interface without deleting posterior mismatch. Combining (3)-(4) retains both terminal bills. If their original costs are bounded by K_G I(G),K_H I(H), and the strong controller certificate is supplied, CE<=max(K_G,K_H,T,C_Lambda) I(F). These are conditional hypotheses, not newly constructed universal seed/controller certificates.

## Physical restriction and the first unsupported history line

After fixing any physical coordinates to specified signs, the remaining W,S,X,Y are still independent uniform blocks on the resulting subcube. Recompute p,V,d,u,v, calibration and kernel there; (1)-(4) remain valid, including constant controllers. A path of adaptive coordinate queries selects just such a subcube when its transcript is fixed. Conditioning on an arbitrary nonlinear event instead is not licensed as a uniform subcube restriction.

Restriction of private branch variables can create new shared-only coefficients. Parent calibration therefore does not automatically make the child reference compatible. This note proves a normalized local reference at each node; it does NOT pay the transition from an inherited reference to that rebuilt reference. The first unsupported C024 history step is bounding that actual recalibration/reset bill with an exclusive reserve. The first unsupported unrestricted C020 step is paying V A sigma beyond the admitted profile bound using retained terminal slack, rather than charging an unlimited selector coefficient. Known bent/point-flip obstructions forbid a universal selector-only repair.
