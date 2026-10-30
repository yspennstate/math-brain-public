# Exact sharp point-controller constants depend on the reserve

Bits throughout. Write eta(x)=x log2(1/x), P(z)=eta((1-z)^2)+eta(z^2)-eta((1-2z)^2)/2, and p(z)=ln(2)*P(z). Endpoints use eta(0)=0. Consider an actual live point activation F=1+A_r(u-1), r>=1, q=2^-r, m=Eu, a=1-m, V=1-m^2 and z=qa. The physical gate-query influence is z. Both actual children are retained.

## 1. Exact entropy decrement, without the loose JS bound

For any queried gate coordinate, a nonempty core frequency has equal-magnitude Fourier pair q*uhat(T), and the 2^(r-1) remaining gate masks produce total entropy decrement 2qV. Nonempty remaining gate masks at empty core frequency similarly produce 2(q-2q^2)a^2. The completely empty pair has amplitudes 1-z and -z and decrement P(z). Thus

    D=2qV+2(q-2q^2)a^2+P(z).

The single-core reserve R=q log2(1/q)V releases kappa_coarse=qV, exactly as in A091. Therefore, for z>0,

    (D-kappa_coarse)/Inf = 2+(1/q-4)z+P(z)/z.       (1)

For z=0 the function is constant +1, so influence and decrement are zero. This exact formula depends only on q,m, not the core's spectrum or dimension. It remains true at every reached physical cylinder with fresh remaining point controls, including biased and constant cores. Equal-amplitude packets have paird(c,c)=4c^2, not 2c^2.

## 2. A sharp all-dimensional bound for the coarse reserve

Define G(z)=4-4z+P(z)/z for z>0. For 0<z<1/2 direct differentiation gives

    p'(z)=4[(1-z)ln(1-z)-z ln z-(1-2z)ln(1-2z)],
    p''(z)=4 ln((1-2z)^2/[z(1-z)]),
    p'''(z)=4[-4/(1-2z)-1/z+1/(1-z)]<0.

On 0<z<=1/4, p''>0 because 1-5z+5z^2>=1/16>0; hence P(z)/z is nondecreasing there. For r>=3, 0<z<=2q<=1/4 and 1/q-4>=4. Equation (1) is therefore increasing in z, so its maximum occurs at a=2, namely the ACTUAL constant core u=-1. Its value is G(2q).

Moreover

    G'(z)=-4+(z p'(z)-p(z))/(ln2*z^2),
    (z p'(z)-p(z))/z^2 = integral_0^1 t*p''(zt) dt.

The last identity follows by integrating the derivative of z p'-p and holds at zero by its finite limit. Differentiation under this integrable kernel gives G''<0 on (0,1/2). In particular G' is strictly decreasing. At z=1/8,

    G'(1/8)=126 log2(7)-60 log2(3)-256>0,

certified exactly by 7^126>3^60*2^256. Thus G increases on (0,1/8], so all r>=4 have value at most G(1/8). The two finite endpoints satisfy

    G(1/4)=12-(9/2)log2(3)=:K_pt,
    G(1/8)=32-(49/4)log2(7)+(9/2)log2(3)<K_pt,

with the strict comparison equivalent to 7^49>2^80*3^36. Both certificates are rechecked as integers by code/check.py.

For r=1,2 it remains to control the larger z range. The homogeneous entropy packet and raw JS-Hellinger inequality give, for 0<z<=1/2,

    P(z)<=2z(1-z)+2z^2/ln2,
    P(z)/z<=1+1/ln2.

The second inequality uses ln2<1. For z>=1/2 use symmetry P(z)=P(1-z) and (1-z)/z<=1 to get the same ratio bound. At r=2 equation (1) is 2+P/z; at r=1 it is 2-2z+P/z. Both are at most 3+1/ln2<9/2<K_pt. Here ln2>2/3 follows from the positive atanh series, and K_pt>9/2 follows from 3^3<2^5. The raw JS bound is independently reconstructed in REVIEW_A091.md.

We have therefore proved, in all dimensions and at every actual live point-controller node,

    0<=D-kappa_coarse<=K_pt*Inf,                    (2)

with EXACT optimal K_pt. Nonnegativity also follows from the exact formula before division. Equality is attained by r=3,u=-1: the three-control point-defect sign has D=H(point_defect_3)-H(point_defect_2)/2 and Inf=1/4. Its failed child is constant +1, its successful child is the actual two-control point defect; the latter entropy is retained. This improves A091's 3+2/ln2 coefficient for the same reserve and same query type, not its general terminal or arbitrary-core payment.

## 3. Why the same sharp constant fails with fine controller labels

Let P_internal be any Boolean function on fresh internal controls, and activate it by one fresh outer point bit: F=1+A_1(P_internal-1). If P_internal is represented as exclusive constant-sign states, the FINE reserve is zero: all selected cores have variance zero. The coarse representation instead treats P_internal as a core, with release q*Var(P_internal). More generally the fine/coarse difference is qL as in A059, with L=Var(P_internal)-sum p_j Var(u_j).

For any fine representation at q<=1/2, its average selected-core variance Vbar lies between zero and V. The exact residual is

    D-kappa_fine=2qV-qVbar+2(q-2q^2)a^2+P(z)
                <=4z(1-z)+P(z).

Thus its residual per influence is at most G(z). Equality is possible with all internal states constant, q=1/2 and any dyadic z in [0,1], by choosing P_internal negative on a fraction z of its cube. This also proves actual Boolean realizability and density for the continuum sharpness claim.

Take P_internal on FIVE bits negative exactly on indices 0,...,6, so z=7/32, mean=9/16. The actual six-bit F has outer-query influence 7/32 and kappa_fine=0. Exact prime-log comparison certifies

    (H(F)-H(P_internal)/2)/Inf_outer
       =G(7/32)>K_pt.                              (3)

Both full truth tables, their terminal spectra and physical influences are independently reproduced by direct character sums. The coarse release is 175/512, so the two residual ratios differ by (175/512)/(7/32)=25/16. The terminal is the actual mixture of P_internal and constant +1, with entropy H(P_internal)/2. It is not dropped or replaced by constant-state output entropy.

The optimal FINE point-gate coefficient is Gamma=max_(0<z<=1)G(z). Strict concavity proves a unique maximizer z_star in (1/8,1/4): G'(1/8)>0 as above, while G'(1/4)=30log2(3)-48<0 follows from 3^5<2^8. Values at z>=1/2 are below K_pt using the preceding symmetric bound, so this is the global maximum. The checker performs 40 derivative-sign bisections with certified rational logarithm intervals, then bounds Gamma between G(lo) and its concave tangent upper bound G(lo)+G'(lo)*(hi-lo). Exact dyadic Boolean approximations show this supremum is necessary, even though the maximizer need not itself be a dyadic Boolean measure. No numerical search is used as a proof of optimality.

## 4. Tensorization and the actual scope of the improvement

For products of independent copies with explicitly ADDITIVE per-factor ledgers, entropy, influence, query decrements, fine/coarse releases and terminal entropy all add. Exposing one gate bit in each copy thus multiplies both sides of the equality witness for (2), or strict witness (3), by the number of copies. A fixed additive constant cannot decrease the coarse K_pt or import it into a tensor-closed fine-ledger rule. A per-copy charge, a different single-core representation of the product, and an added qL debit are different hypotheses and not refuted by this argument.

The legitimate downstream substitution replaces only the point-controller coefficient in A091's stopped ledger by K_pt while keeping its actual U,R and terminal term. It does NOT replace A059's finer residual coefficient by K_pt, nor pay repeated fallback coordinates or arbitrary internal controller queries. The fine optimum Gamma is the sharp replacement for the outer point-gate residual at fine-state scope; it still leaves all actual internal-controller and terminal bills.

First unsupported universal line: a compatible controller policy pays its remaining internal/repeated-fallback residual together with the actual unresolved H-U-R terminal from one unspent physical account. Inherited arbitrary U remains. Full FEI is open, and neither sharp constant nor the six-bit scope counterexample is an FEI disproof.
