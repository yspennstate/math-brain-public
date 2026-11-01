# Exact arithmetic granularity cannot be charged collectively to influence and address entropy

30 September 2026. **Full FEI remains OPEN.** These are exact Boolean counterexamples to proposed sufficient payments for a quantized, exact-product projection theorem. They do not refute that component theorem or FEI.

## 1. Definitions

Split the physical variables into an address block z and retained block x. For Boolean f define

    g_T(x)=E_z f(z,x) chi_T(z),
    w_T=E_x g_T(x)^2,
    J_T=I(g_T)/w_T   (w_T>0).

I(g) means the squared L2 derivative energy for real g. The normalized squared Fourier law of g_T has mean set size J_T. The address law is w=(w_T), and its entropy H(w) is in bits.

Let k_T be the least nonnegative integer for which all physical values of g_T belong to 2^(-k_T) Z, and put delta_T=2^(-k_T). All examples below are dyadic. In the dominant projections used below this is also the largest commensurate real grid step.

For a normalized product component, let q_(T,i) be its Fourier inclusion marginals, and define

    q_*T=max{q_(T,i): 0<q_(T,i)<1/4},

with maximum zero for the empty set.

The investigated payments were

    W_1=sum_T w_T (k_T+1) J_T,                              (1)
    W_2=sum_T w_T q_*T [ln w_T+2k_T ln2]_+.                (2)

Neither admits a universal bound C[I(f)+H(w)]. This remains false when every nonzero component has exactly product normalized spectrum. All pointwise signed Boolean coupling identities hold, because the examples are actual Boolean functions:

    sum_T g_T(x)g_(T triangle U)(x)=1_(U=empty).

## 2. Tensor obstruction to the influence-multiplied price

Let k,r be positive even integers. Take bent Boolean phases b_k(z), b_r(x), and f(z,x)=b_k(z)b_r(x). For example use the quadratic phases consisting of disjoint paired products over F2.

Every address coefficient of b_k has magnitude 2^(-k/2), so

    g_T=+/-2^(-k/2)b_r,
    w_T=2^(-k), k_T=k/2, J_T=r/2.

Every normalized component spectrum is uniform on the retained cube, hence product with all marginals 1/2. Exactly

    W_1=(k/2+1)r/2,
    I(f)+H(w)=(k+r)/2+k.

Setting r=k makes the ratio (k+2)/8, which diverges. This is the repeated charging of an independent address's arithmetic resolution to all retained influence.

## 3. Even amplitude-normalized global granularity times J is too strong

A natural repair is to replace k_T by

    k_eff,T=log2(||g_T||_infinity/delta_T),

using the largest commensurate physical grid. The following example still defeats a global multiplier (k_eff,T+1)J_T.

Start with f_0(z_1,z_2,y)=1-2*1{z_1=z_2=y=1}, using binary physical coordinates. Address z_1,z_2. The empty-address projection takes values 1 and 1/2, with

    w_0=5/8, J_0=1/10, k_eff,0=1.

Each of the other three projections takes values 0 and +/-1/2, with

    w_T=1/8, J_T=1/2, k_eff,T=0.

Now tensor m independent copies. Every normalized component is a product of one-bit laws and is therefore exactly product. Under its address law, let L count the copies with empty address label. Then L is Binomial(m,5/8), and

    k_eff,T=L,
    J_T=m/2-(2/5)L.

The physical grid is exactly 2^(-m): some nonzero physical value equals that number, and every value is its integer multiple. Its supremum is 2^(-(m-L)), establishing the displayed k_eff exactly.

Using E L=5m/8 and Var L=15m/64 gives

    sum_T w_T(k_eff,T+1)J_T=5m(m+1)/32.                     (3)

On the other hand,

    I(f)=3m/4,
    H(w)=m[3-(5/8)log2 5].                                (4)

Thus the proposed ratio again diverges linearly. A tensor-additive scalar complexity cannot generally be multiplied by total component influence without repeated charging.

## 4. The refined q_* logarithmic price fails without any retained tensor factor

The stronger counterexample has only **one retained bit**. It therefore also prevents repairing (2) merely by removing independent retained factors or assigning one exact arithmetic denominator to each retained coordinate.

Fix k>=3 address bits. Let h_base(z)=1-2*1{z_1=z_2=1}, independent of the other k-2 bits. Flip its value at the single negative input

    z^0=(1,1,0,...,0)

from -1 to +1, obtaining h_k. Put

    epsilon=2^(1-k),
    mu=E h_k=1/2+epsilon.

Define the genuine Boolean function on k+1 variables by

    f_k(z,0)=1,
    f_k(z,1)=h_k(z).

Address all z bits and retain only y. The empty-address projection has physical values

    g_empty(0)=1,  g_empty(1)=mu.

Consequently

    w_0=(1+mu^2)/2,
    q_0=(1-mu)^2/[2(1+mu^2)].                              (5)

For k>=3, 0<q_0<1/4, so q_*0=q_0. The numerator of mu=(2^(k-2)+1)/2^(k-1) is odd. Because g_empty also takes the value 1, its exact minimal grid exponent is k-1 and delta_0=epsilon.

For every nonempty T, the projection takes the two values 0 and hhat_k(T). It is nonzero here. Its normalized spectrum is the fair one-bit law, with marginal 1/2, and hence q_*T=0. Every component spectrum is exactly product, since there is only one retained coordinate.

Therefore the entire refined price is exactly

    W_2(f_k)=((1-mu)^2/4) ln(w_0/epsilon^2),                (6)

where the logarithm is positive for k>=3. Since mu tends to 1/2,

    W_2(f_k)/k -> ln2/8 >0.                               (7)

### Influence stays bounded

Before the exceptional flip, h_base has total influence 1. At z^0 exactly two of its k incident edges were boundary edges. The flip removes those two and adds the other k-2, changing the number of boundary edges by k-4. Thus

    I(h_k)=1+(k-4)epsilon,
    I(f_k)=I(h_k)/2+(1-mu)/2
          =3/4+(k-5)epsilon/2 -> 3/4.                     (8)

### Address entropy stays bounded

With Walsh characters chi_T(z)=(-1)^(sum_(i in T)z_i), the Fourier coefficients of h_k have these exact magnitudes:

- empty label: 1/2+epsilon;
- the three nonempty subsets of {1,2}: 1/2-epsilon;
- the remaining 2^k-4 labels: epsilon.

This follows by adding epsilon chi_T(z^0) to each coefficient of h_base. The address probabilities are therefore

    w_0=(1+(1/2+epsilon)^2)/2,
    w_H=(1/2-epsilon)^2/2       (three labels),
    w_L=epsilon^2/2            (2^k-4 labels).              (9)

They sum to one exactly. The tail entropy is

    -(2^k-4)w_L log2 w_L=O(k 2^(-k)) ->0.

The other four probabilities converge to (5/8,1/8,1/8,1/8), giving

    H(w)->3-(5/8)log2 5.                                  (10)

Equations (7), (8), and (10) prove W_2/[I(f_k)+H(w)] tends to infinity.

This obstruction is not a large normalized component entropy: each component has entropy at most one bit. The exact grid becomes arbitrarily fine after a vanishingly small Boolean perturbation, while the dominant component's nontrivial marginal stays near 1/10. The attempted arithmetic upper bound is valid but increasingly loose.

### Every fixed positive small-marginal cutoff has the same obstruction

The cutoff 1/4 is not essential. Given any fixed tau>0, use a base AND phase on b address bits with b fixed and large enough. Put a=2^(1-b). After the same one-point flip in k>b address bits, the dominant projection takes values 1 and mu=1-a+epsilon, with epsilon=2^(1-k). Its normalized marginal tends to

    a^2/[2(1+(1-a)^2)],

which can be chosen below tau. Its minimal dyadic grid is still epsilon, and its price divided by k tends to a^2 ln2/2>0. The exact total influence is

    I(f_k)=(b+1)a/2+(k-2b-1)epsilon/2,

which stays bounded. Its address law converges to the finite-support address law of the fixed base function, with tail entropy O(k epsilon). Thus merely shrinking the fixed cutoff, even to accommodate a very generous universal FEI constant, does not repair this payment.

## 5. Consequence for the constructive route

These examples preserve exact product spectra and the complete joint Boolean constraints. Thus neither retaining J_T in (1), replacing raw grid size by an amplitude-normalized scalar, nor replacing J_T by the largest small product marginal in (2) supplies the missing collective payment.

A surviving refinement must avoid sensitivity to an arbitrarily small grid-refining perturbation. Possible directions include an approximation-sensitive arithmetic parameter with an explicitly paid residual, or a genuinely local structural allocation. This report proves neither repair. Any residual entropy payment must be established from the actual collective Boolean family, not inferred from the exact-product component theorem.

No unrestricted FEI proof, FEI counterexample, or publication-priority claim is made.

## 6. Independent review and scope

The coordinating researcher independently checked the bent-tensor obstruction and all exact formulas of the one-retained-bit perturbation family: boundary changes, means, three old Fourier magnitudes, tail count, address probabilities, minimal dyadic grid, and the asymptotic price and entropy. The amplitude-normalized tensor calculation in Section3 is presented with its elementary binomial proof; it was not part of that independent review. No executable checker is needed for these analytic families, and no new code is directly committed to master.
