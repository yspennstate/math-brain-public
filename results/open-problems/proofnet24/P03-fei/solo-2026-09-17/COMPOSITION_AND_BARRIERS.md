# Composition stress tests and two obstructions

All statements marked proved below have proofs here; they are self-checked research claims, not independently audited. Novelty is unverified. None refutes FEI.

## 1. Exact recursion for disjoint NAND composition

Let A be a {0,1}-valued function with mean alpha. Write c_S=Ahat(S), t_i=c_{i}. For a nonnegative, possibly unnormalized vector q, use

    H(q)=-sum q log_2 q,
    B(q)=sum_i sum_{T not containing i} E(q_T,q_{T+i}),
    E(r,s)=-r log_2 r-s log_2 s+(r+s) log_2(r+s).

Use H_A and B_A for q=c^2, whose total mass is alpha by Parseval. Let A' be the NAND of k identical copies on disjoint variables:

    A'=1-product_{j=1}^k A(x^(j)),   p=alpha^k.

The product has squared Fourier law equal to the product of k copies of c^2. The mass of every other block is alpha. E is homogeneous: E(cr,cs)=cE(r,s). Hence its erasure functional equals k alpha^(k-1) B_A, and its entropy equals k alpha^(k-1) H_A. Complementing the product changes only the empty coefficient, from p to 1-p. Therefore

    alpha'=1-p,
    t_i'=-alpha^(k-1)t_i,  with k copies of each i,
    H_A'=k alpha^(k-1) H_A+h((1-p)^2)-h(p^2),
    B_A'=k alpha^(k-1) B_A
       +k sum_i [E((1-p)^2,alpha^(2k-2)t_i^2)
                  -E(p^2,alpha^(2k-2)t_i^2)].             (10)

For f=1-2A,

    H(f)=4H_A-4h(alpha^2)-8alpha(1-alpha)+h((1-2alpha)^2),
    B(f)=4B_A+sum_i [E((1-2alpha)^2,4t_i^2)
                       -4E(alpha^2,t_i^2)].               (11)

For a unate A, the coordinate difference has a constant sign. Thus |t_i|=Inf_i(f)/2 and I(f)=2 sum_i |t_i|. Unateness is preserved in the constructions below; generic non-unate functions cannot use this shortcut. Under the disjoint NAND operation,

    I(f')=k alpha^(k-1) I(f).                              (12)

These identities allow evaluation at enormous formal input dimension without claiming to have enumerated the corresponding truth tables. The floating recursion is subject to cancellation and roundoff at extreme depths; only the separate rational certificate below supports an exact numerical assertion.

## 2. Exact counterexample to the tentative erasure constant 4

Take five bits indexed by integers 0,...,31 and set A_0(x)=1{x<21}. Recursively set

    A_{d+1}(x,y)=1-A_d(x)A_d(y)

with disjoint copies, and let f=1-2A_4. This is an explicitly specified Boolean function of 80 variables.

The exact rational interval computation in `certify_nand80.py`, using (10)-(12), proves

    4.007 < B(f)/I(f) < 4.008.

Its complete output is `nand80_certificate.json`. Every arithmetic decision is rational. Each logarithm is reduced to ln(y) with 1<=y<=2 and evaluated through

    ln(y)=2 sum_{j=0}^{M-1} t^(2j+1)/(2j+1)+R,
    t=(y-1)/(y+1),
    0<=R<=2 t^(2M+1)/[(2M+1)(1-t^2)].

Here M=64; interval arithmetic rounds outwards to a 160-bit binary grid. The exact influence is

    I(f)=108826706204703411128127 / 37778931862957161709568.

This kills **only** the provisional inequality B<=4I. It does not kill B<=KI for another finite universal K, and does not refute the source conjecture. This is a deliberately tested intermediate bound, not an externally posed conjecture.

## 3. A stronger aggregate overlap bound is false for every constant

Another tempting move is to use psi(t)<=2 sqrt(t(1-t)), obtaining

    B(f)<=R(f):=2 sum_i sum_{T not containing i}|fhat(T) fhat(T+i)|. (13)

The binary inequality follows from the same scalar inequality used in Section 2 of ERASURE_REDUCTION.md, or from direct differentiation; a proof is supplied in Section 6 below. However, **there is no finite universal C for R(f)<=C I(f)**, even within the unate disjoint-NAND family described next.

For an indicator A define R_A=2 sum_edges |c_S c_T| and r_A=R_A/I(1-2A). As with B, the product rule is R_product=k alpha^(k-1)R_A. Complementing changes only the empty-to-singleton edges, so

    R_A'=k alpha^(k-1)R_A
             +2k alpha^(k-1)(1-2alpha^k) sum_i|t_i|.

Divide by (12):

    r_A'=r_A+1-2alpha^k.                                  (14)

The relation to the Boolean output is

    R(1-2A)/I(1-2A)=4r_A+2(|1-2alpha|-2alpha).

In particular, if alpha>1/2, this equals 4r_A-2. For binary NAND and successive means alpha_j>1/2, (14) therefore gives the exact relation

    R(f_d)/I(f_d)=R(f_0)/I(f_0)+4 sum_{j=1}^d(2alpha_j-1),
    alpha_{j+1}=1-alpha_j^2.                              (15)

**Unboundedness theorem.** For every positive integer d there is a finite unate Boolean f_d with R(f_d)/I(f_d)>(4/5)d.

**Proof.** Put phi=(sqrt(5)-1)/2, the fixed point of T(a)=1-a^2. Choose m=d+7 and a dyadic alpha_0 with denominator 2^m satisfying |alpha_0-phi|<2^-m, realized by a lexicographic indicator on m bits. For example use floor(2^m phi)/2^m. Since T maps [0,1] to itself and is 2-Lipschitz there,

    |alpha_j-phi|<=2^j |alpha_0-phi|<1/128  for j<=d.

The inequalities 61/100<phi<62/100 follow by substituting into a^2+a-1. Hence every alpha_j lies strictly between 3/5 and 2/3. In particular all the hypotheses used in (15) hold, and 2alpha_j-1>1/5. The initial ratio R(f_0)/I(f_0) is nonnegative and all influences are positive. Equation (15) yields the assertion. The construction uses m 2^d finite variables. QED.

Thus replacing logarithmic conditional entropy by the absolute adjacent-coefficient overlap in (13) is a dead end for a universal linear-in-influence proof. The failure is aggregate, not merely one badly chosen coordinate. A successful argument must preserve the logarithmic dependence on the spectral mass ratio or find a different cancellation.

## 4. A single-coordinate obstruction from a bent function

For even m, N=2^m and

    g(x)=(-1)^(x_1 x_2+x_3 x_4+...+x_{m-1}x_m)

on {0,1}^m, every Walsh coefficient is s_S/sqrt(N), s_S in {-1,1}. This follows by tensoring the two-bit transform (1,1,1,-1)/2. Also g(0)=1, so sum_S s_S=sqrt(N).

Let g' differ from g only at zero, and construct f with its two selector restrictions equal to g and g'. Then the selector Fourier pairs are

    u_S=s_S/sqrt(N)-1/N,   v_S=1/N.

Thus Inf_selector(f)=1/N. Write delta=1/N and c_s=1-2s sqrt(delta)+2delta. The pair mass is delta c_s and the conditional inclusion probability is delta/c_s. The expansion

    psi(t)=t log_2(1/t)+t/ln 2+O(t^2)

is uniform here as delta tends to zero, since c_s tends uniformly to 1. Summing the N pair contributions yields

    B_selector/Inf_selector = m+1/ln 2+o(1).

For the JS part, the scalar contrast z=2uv/(u^2+v^2) is 2s sqrt(delta)+O(delta), and d(z)=z^2/2+O(z^4). Consequently

    JS/Inf_selector = 2/ln 2+o(1),
    Delta_selector/Inf_selector = m+3/ln 2+o(1).           (16)

This proves unbounded failure of the every-coordinate restriction payment, reproducing the type of obstruction already recorded in the older P03 ledger. It does not refute the existence of a suitable coordinate or the aggregate erasure bound. The numerical values through m=16 are in `baseline_results.json`.

## 5. What remains worth attacking

Both the local payment and the aggregate absolute-overlap majorant can fail by arbitrarily large factors. The logarithmic residual L in ERASURE_REDUCTION.md is the live quantity. Replacing log(1+r) by either a global Jensen mean or a square-root bound loses information needed even on explicit structured Boolean examples.

The next useful theorem must control the actual weighted logarithmic spectral-edge ratios using the signed convolution identities, or provide a genuinely different route to universal FEI. Exact enumeration beyond four variables and another standalone checker are not the next proof step.

## 6. Scalar bound used in (13)

For t in [0,1], set z=|2t-1| and s=sqrt(1-z^2)=2sqrt(t(1-t)). We need psi(t)<=s. In natural logarithms this is d(z)>=ln(2)(1-s). Define F(z)=d(z)-ln(2)(1-s). We have F(0)=F(1)=0 and

    F'(z)=atanh(z)-ln(2) z/sqrt(1-z^2).

Write z=tanh(u), u>=0. The sign of F' is the sign of u/sinh(u)-ln(2). The function u/sinh(u) decreases strictly from 1 to 0: its derivative has numerator sinh(u)-u cosh(u)<0 because the derivative of that numerator is -u sinh(u)<0. Thus F' changes from positive to negative exactly once. Since both endpoints of F are zero, F>=0 on [0,1]. This proves (13), including the endpoints by continuity.
