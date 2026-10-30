# Phase-degree guard and a signed cubic-star conditional rebate

Uniform independent physical coordinates; all entropies are in bits. This stage consumes the B07 lead v2 instruction and A088's independent acceptance of A033 v1. It does not reopen that proof or claim a new universal constant.

## 1. The requested guards, with exactly stated admission

For the three-bit point defect f=1-2*1_(z=0), the GF(2) phase is P=(1+z_1)(1+z_2)(1+z_3). It has degree three, and every nonconstant directional phase derivative has degree two and weight 1/4. Thus d=2 ADMITs it; d=1 EXCLUDEs it. Its spectrum has one mass 9/16 and seven masses 1/16, so

    H=4-(9/8)log2(3), I=3/4,
    H/I=16/3-(3/2)log2(3),
    kappa(2)=8-3log2(3),
    kappa(2)I-H=2-(9/8)log2(3)>0.

The last strict sign is exactly 3^9<2^16. The two-address test is not empty: conditioning on two spectral coordinates leaves one coordinate, so a product-law hypothesis would be vacuous, but the GF(2) directional-degree hypothesis is still checked on all physical residual variables. We do not assert the constant-two inequality for cubic phases.

For N=4^k, psi_N=N^(-1/2)sum_j x_j is normalized, dyadic, real, with H=log2 N=2k and I=1. At all-plus input psi_N=sqrt(N), not +/-1. Its physical derivative in coordinate j is the constant N^(-1/2), whose square is 1/N, not a {0,1} indicator. Its square-convolution coefficient at {i,j} is 2/N. Its multiplicative derivative at the all-plus input is N-2, not a sign. The exact Booleanity/pivotal-indicator hypothesis excludes it; a GF(2) phase derivative is UNDEFINED for this real source, not a low-degree polynomial. Replacing GF(2) phase degree by real Fourier degree one is invalid. The relaxed kappa(2) inequality fails for N>=16, since kappa(2)<4 follows from 3^3>2^4. psi_4 happens to pass that scalar inequality, which is not evidence of Booleanity.

The entropy subadditivity in A033 v1 is generic. Its Boolean-specific input is the two-sided weight gap for an exact pivotal GF(2) indicator. We explicitly distinguish these steps.

## 2. Nonflat cubic-star class and its signed spectrum

Let m>=1, x be 2m physical bits, s one fresh physical bit, and let Q(x) be an arbitrary GF(2) quadratic polynomial whose polar bilinear form is nondegenerate (rank 2m). Set

    b(x)=(-1)^Q(x), f(s,x)=(-1)^(s Q(x)).

The complete proof of bent flatness is short. For Fourier label T,

    bhat(T)^2=E_u chi_T(u) E_x b(x)b(x+u).

For u!=0, Q(x)+Q(x+u) is a nonconstant affine linear form because the polar form is nondegenerate, so the inner signed average is zero. For u=0 it is one. Hence bhat(T)^2=2^(-2m) for EVERY T. This uses exact sign-valued quadratic phase and its signed correlation, not a generic marginal entropy bound. Write M=2^m, N=M^2, beta=E b=+/-1/M. Every physical derivative of b is a nonconstant affine character, so Inf_i(b)=1/2.

The exact selector expansion is

    f=(1+b)/2+(-1)^s(1-b)/2.

Consequently the joint squared spectrum on (S_s,S_x) has two exceptional atoms at S_x=empty,

    p_plus=(1+beta)^2/4, p_minus=(1-beta)^2/4,

and every other data label has two atoms of mass q=1/(4N). The data marginal has empty mass (1+beta^2)/2 and  N-1 equal nonempty masses 1/(2N). Set v=(1-beta^2)/2<1/2. Its entropy is exactly

    H(S_x)=h2(v)+v log2(N-1),
    I_x(f)=m/2, Inf_s(f)=(1-beta)/2.

All directional phase derivatives of f have degree two. The v1 bound gives H(S_x|S_s)<=kappa(2)m/2. The signed spectrum above gives the stronger result

    H(S_x|S_s) <= 3 I_x(f)=3m/2.                 (1)

For m>=2, conditioning and the exact marginal give H(S_x|S_s)<=H(S_x)<=1+m<=3m/2. For m=1, f is a three-bit point defect up to input flips, a linear output character, and/or swapping the selector's physical values. The spectral selector entropy is h2(1/4)=2-(3/4)log2(3), and exactly

    H(S_x|S_s)=2-(3/8)log2(3)<=3/2,

equivalently 3^3>=2^4. This handles the smallest case explicitly rather than inferring a conditional law from its dimension.

The full entropy also obeys H(f)<=3I(f). For m=1 this is 3^9>=2^14. For m>=2, split on the empty/nonempty data event. The nonempty joint support has 2(N-1) equally weighted atoms and the empty event has two atoms, giving

    H(f)<=1+v(2m+1)+(1-v)=2+2mv<=m+2.

Since |beta|<=1/4, I(f)>=I_x+(1-|beta|)/2=(m+1-|beta|)/2 and m+2<=3(m+1-|beta|)/2 for m>=2. No claim of novelty is made for this proper-class FEI bound; the useful delta is the explicit conditional payment and rebate relative to v1.

There is also a SHARP complete physical-block payment, avoiding separate pricing of the channel. Reveal all data x and leave the selector s. Each actual restricted leaf is 1 or (-1)^s, hence has Fourier entropy zero. For any arbitrary disjoint Boolean spectator g(y), the leaves of f(s,x)g(y) are g(y) or (-1)^s g(y), both with entropy H(g). Therefore

    H(fg)-E_x H((fg)_x)=H(f)<=K_star I_x(fg),
    K_star=8-(9/4)log2(3),    4<K_star<9/2.       (2)

At m=1 equality holds, since I_x=1/2. For m>=2, the bound H(f)<=m+2 yields H/I_x<=2+4/m<=4<K_star. Thus m=1 attains the best constant in this class. The two strict signs are certified by 2^14<3^9<2^16. This is a complete C019 node payment with arbitrary terminal seed entropy retained, not a joint bound for an arbitrary tensor spectator.

## 3. Exact correlation credit and its size

Each data coordinate has q_i=1/4 and h2(q_i)=kappa(2)/4. The complete marginal bill is kappa(2)m/2. Define

    R_x=TC(S_x)+I(S_x;S_s).

The entropy identity gives EXACTLY

    R_x=kappa(2)m/2-H(S_x|S_s).

For m>=2 the proof gives R_x>=kappa(2)m/2-(m+1); all m satisfy R_x>= [kappa(2)-3]m/2. For m=1 the exact credit is 2-(9/8)log2(3)>0. For m>=3 the rank-dependent lower bound is stronger than the uniform coefficient improvement.

In fact H(S_x|S_s)=m+1+o(1). To see it, the empty joint atoms tend to 1/4 each, giving total entropy 1+o(1); the nonempty atoms contribute v(2m+2)=m+1+o(1). Thus H(f)=m+2+o(1). The selector marginal tends to fair, with entropy 1+o(1), so subtract it. Therefore

    R_x/m -> kappa(2)/2-1.

This is an explicit, growing correlation credit in the exact degree-bill identity. The bit entropy and support-size estimates AFTER the signed spectral calculation are generic; complete sign-valued quadratic autocorrelation supplies the realizable spectrum in the first place.

## 4. A matched non-Boolean selector control

To test the architecture as well as psi alone, replace the core b by psi_N on N physical bits and set

    F_N(s,x)=(1+psi_N(x))/2+(-1)^s(1-psi_N(x))/2.

It is normalized: the physical selector branches are the constant 1 and psi_N, each of norm one. Its real Fourier degree is at most two, and for N=4^k its coefficients are dyadic. Its joint spectral law has two empty-data atoms of mass 1/4 and, for each singleton data label, two atoms of mass 1/(4N). Consequently

    H(F_N)=2+(1/2)log2 N, I_s=I_x=1/2,
    H(S_x|S_s)=1+(1/2)log2 N.

Thus the relaxed form of (1) fails for EVERY N=4^k,k>=1: its left side is 1+k>=2 and 3I_x=3/2. Its relaxed kappa(2) version already fails for N=4, since kappa(2)<4. This is an actual normalized real counterexample, not merely the observation that a phase is undefined. Exact Booleanity and the sign-valued nondegenerate quadratic core exclude it. Physical selector normalization and low REAL degree do not.

## 5. Tensor guard and the first unpaid universal line

For any arbitrary Boolean g(y) on a disjoint cube, f(s,x)g(y) preserves the directional phase derivative condition on x. Its spectrum is a product, so

    H(S_x|S_s,S_y)=H(S_x|S_s)<=3I_x,
    H(fg)=H(f)+H(g), I(fg)=I(f)+I(g).

Equation (1) is paid on x; it does not pay H(g). Character multiplication on y or tensor powers cannot remove that residual. We do not claim a joint constant-three bound for fg without a separately certified constant-three bound for g.

Replacing the quadratic core by any balanced Boolean b on x gives exact identities

    H(S_x|S_s)=1+H(b)/2, I_x=I(b)/2.

A universal finite-K version of (1) for arbitrary balanced cores would imply H(b)<=K I(b)-2, hence full FEI in finiteness (balancing and tensor amplification remove the additive cost). Conversely FEI(K) yields the conditional inequality with coefficient K+2 because balanced b has I(b)>=Var(b)=1. Thus arbitrary-core completion is FEI-strength; it is not a free extension of this class.

The first unsupported line is a signed correlation credit of comparable size for nonquadratic cores or a broader physical phase derivative hierarchy, with a nonreusing budget and terminal seed entropy retained. The exact quadratic cancellation supplies a concrete term to replace, rather than another fixed convolution prefix. The old original atom-cap addendum remains unavailable; this stage follows the lead's concrete guards rather than treating another access attempt as mathematics.
