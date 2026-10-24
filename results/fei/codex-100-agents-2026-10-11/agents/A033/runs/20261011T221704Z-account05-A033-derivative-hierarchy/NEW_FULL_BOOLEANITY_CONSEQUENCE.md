# Complete hierarchy and directional phase payment

Entropy is in bits. All input coordinates are independent uniform signs. This is a source-complete, scoped consequence, not a solution of full FEI and not a claim of novelty for low algebraic degree bounds.

## 1. The exact hierarchy, rather than an unspecified prefix

For real Fourier amplitudes a indexed by subsets of [n], write C(U)=sum_S a_S a_(S xor U). The complete convolution hierarchy is C(empty)=1 and C(U)=0 for EVERY nonempty U. Indeed C(U) is the Fourier coefficient of f^2; these equations are equivalent to f(x)^2=1 at every physical vertex. The order-r relaxation keeps only |U|<=r.

The complete physical-face hierarchy says E[f^2 | x_A=t]=1 for every A and every t. Its order-r version keeps |A|<=r. Expanding that conditional expectation gives sum_(U subset A) C(U) chi_U(t), proving exact equivalence to the corresponding convolution order. At full depth A=[n], it gives pointwise Booleanity.

For coordinate i let A_i=(f_+ + f_-)/2 and B_i=(f_+ - f_-)/2 on the residual cube. Complete Booleanity gives, POINTWISE,

    A_i B_i=0,    A_i^2+B_i^2=1,    A_i,B_i in {0,+1,-1}.

These follow directly from f_+^2=f_-^2=1; conversely the first two imply (A_i +/- B_i)^2=1. For n>=1 the pointwise pair identities for even one physical split imply the full convolution hierarchy. The zero-dimensional endpoint is |f|=1. Thus this condition is not another bounded shift prefix. In particular Q_i=B_i^2 is an EXACT indicator of the pivotal event, not a near-indicator inferred from a small defect.

For 0/1 physical variables z, write the unique Boolean phase f(z)=(-1)^(P(z)), where P is its multilinear GF(2) polynomial. The multiplicative derivative is

    Delta_i f(z)=f(z)f(z xor e_i)=(-1)^(partial_i P(z)),
    Q_i(z)=(1-Delta_i f(z))/2=partial_i P(z) in {0,1}.

For distinct coordinates A, Delta_A f is the product of f at all translated vertices of the A-face and equals (-1)^(partial_A P). All these derivatives are exact signs. Global phase degree <=r is equivalent to Delta_A f=1 for all |A|=r+1. Our structural bound below is instead directional: degree(partial_i P)<=d for i in a chosen block X, as a polynomial on ALL remaining physical variables. It is not real Fourier degree, a degree bound only in X, or a bound on a spectral conditional law. It allows arbitrary Y-only phase terms.

## 2. An additional nonlinear consequence: a two-sided derivative weight gap

If a nonzero GF(2) polynomial Q has degree at most d, then Pr(Q=1)>=2^(-d). Here is a complete proof. The degree-zero nonzero polynomial is constant one. Otherwise choose a variable appearing in Q, write Q=R+z_j T over GF(2), with nonzero T of degree <=d-1. For each residual assignment with T=1, exactly one of Q(z_j=0),Q(z_j=1) is one. Therefore Pr(Q=1)>=Pr(T=1)/2>=2^(-d). Variables absent from Q can be omitted. Applying this to Q and 1+Q proves

    Q nonconstant, degree Q<=d  =>  2^(-d)<=Pr(Q=1)<=1-2^(-d).

For the exact pivotal indicator Q_i this gives J_i=min(Inf_i,1-Inf_i)>=2^(-d_i), where d_i=degree(partial_i P)>=1. Constant Q_i has Inf_i=0 or 1 and J_i=0. This weight gap uses exact indicator Booleanity plus a structural degree bound; dyadic real Fourier coefficients alone do not imply it.

## 3. Quantitative spectral and physical block consequences

Define kappa(0)=0, and for integer d>=1,

    kappa(d)=h2(2^(-d))/2^(-d)
            =d*2^d-(2^d-1)log2(2^d-1)
            =d+(2^d-1)log2(1+1/(2^d-1)) < d+1/ln 2.

If every nonconstant partial_i P, i in X, has degree <=d, then

    H(S_X | S_Y) <= kappa(d) sum_(i in X) J_i,
    H(f) <= H(S_Y)+kappa(d) sum_(i in X) J_i,       (1)

where Y=[n]\X and S is the full squared Fourier sample. The d=0 case means all these derivatives are constant, so every spectral X-bit is deterministic and its conditional entropy is zero.

Proof: the marginal spectral inclusion probability is q_i=Inf_i=E Q_i by Parseval for B_i. For 0<t<=1/2, h2(t)/t is decreasing: its derivative is log2(1-t)/t^2<0. Hence the weight gap gives h2(q_i)=h2(J_i)<=kappa(d)J_i. Entropy subadditivity and conditioning give H(S_X|S_Y)<=sum_(i in X)h2(q_i). This proves (1). The sharper nonuniform statement is H(S_X|S_Y)<=sum_(i in X, d_i>=1)kappa(d_i)J_i.

Using the accepted exact physical-block identity C006, let f_t be the actual restriction obtained by fixing X uniformly. Then

    H(f)-E_t H(f_t)
      =H(S_X|S_Y)+I(t; restriction-spectrum-on-Y)
      <=[kappa(d)+2/ln 2] I_X(f).                 (2)

This is a genuine C019 block payment with terminal entropy retained. The channel bound is separately imported from BLOCK_RESTRICTION_IDENTITY_2026-09-18.md, not proved by (1). No proper-block choice is guaranteed universally. If X=[n], (1) directly proves H<=kappa(d)D_char<=kappa(d)I. In particular arbitrary cubic Boolean phases have H<=[8-3 log2 3]D_char; quadratic phases give H<=2D_char. These elementary class consequences are calibration, not new claims about prior art.

Directional phase degree is hereditary under physical restrictions. If X is revealed sequentially, this preserves the same d bound at each node. The total expected queried influence is exactly I_X(f): for any still-free i, averaging its influence over restrictions of other coordinates returns its original influence, by counting the same i-edges. Thus (2) can also be recovered by summing singleton restriction payments with a single use of the X-influence budget. All terminal Y entropy remains.

## 4. Exact correlation rebate and the high-degree gap

Let TC_X=sum_(i in X)h2(q_i)-H(S_X), and MI=I(S_X;S_Y). Both are nonnegative, and exactly

    H(S_X|S_Y)=sum_(i in X)h2(q_i)-TC_X-MI.

Consequently our weighted degree estimate can retain these rebates:

    H(S_X|S_Y)<=sum_(i in X,d_i>=1)kappa(d_i)J_i-TC_X-MI.  (3)

For the n-bit point defect f=1-2*1_(z=0), each partial_i P is a degree n-1 monomial (after affine translation), q_i=2^(1-n), and each weight bound is tight. Thus the bill in (3), before the correlation rebate, is

    sum_i h2(q_i) = I(f)*kappa(n-1),
    I(f)=2n/2^n,
    H(f)/I(f) -> 4,
    TC/I=kappa(n-1)-H/I = n-5+log2(e)+o(1).

The H/I limit follows directly from p_empty=(1-2/2^n)^2 and every nonempty p=4/4^n: the nonempty entropy is 8*2^(-n)(1-2^(-n))(n-1), while the empty entropy is O(2^(-n)). The kappa limit follows from m ln(1+1/m)->1, bounded between m/(m+1) and 1. Hence a universal attempt to pay the raw degree/granularity bill by O(I) fails on actual Boolean functions. Increasing d is not a route to full FEI. A universal theorem would need a signed mechanism paying this growing bill through TC or another nonreused rebate.

## 5. Tensor admission and the exact first unsupported inference

For any fixed phase h(X) satisfying the d condition and any arbitrary Boolean g(Y), f=h(X)g(Y) still satisfies every directional condition on X. Its spectrum is a product, so H(S_X|S_Y)=H(h), H(S_Y)=H(g). Formula (1) deliberately preserves H(g). A fixed derivative bound on X does not pay joint entropy; applying such a claim to arbitrary tensor powers of g would recover full FEI. Likewise Q(X,Y) can couple the cubes, but a bounded mixed-phase degree must be checked on all remaining physical variables, including Y.

The first unsupported universal line is a dimension-independent signed/correlation transport inequality that cancels the high-degree marginal bill in (3), or a physical stopping rule that always selects a bounded-degree block and pays its remaining terminal entropy without reusing influence. Neither is asserted. This is the shortest remaining bridge to C018/C019 within this mechanism.
