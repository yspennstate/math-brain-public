# A product-reference conversion can cost arbitrarily much at one fair query

All entropies are in bits. This concerns actual Boolean physical restrictions and the prescribed fair extension on source-zero/reference-positive rows. It does not disprove FEI. The elementary entropy-process baseline is already established and is not claimed again here.

## The exact obstruction

For every integer l>=2 there is an explicit Boolean sign F_l on 3l+3 bits with a distinguished fair query i, such that:

* Every coordinate of F_l and every surviving coordinate of BOTH actual physical children has influence exactly 1/2.
* The spectral indicator S_i is independent of all remaining spectral indicators. Thus h2(d_i)-B_i=0.
* All spectator Jensen gaps h2(d_j)-mean_b h2(d_j(F_b)) are zero.
* The actual entropy drop is Delta H=2, B_i=1 and JS_i=1.
* For the incoming actual product reference Q, coherent erasure and the actual physical child kernel, extended fairly on zero source rows, predict r_G=2^(-l-1), r_H=1-r_G.
* Consequently O=(l-1)/2-(1/2)log2(1-2^(-l-1)) and signed conversion D=O+mean TC_child-TC_parent=1+O. In particular D/d_i>l+1.

Thus no finite universal current-query price D<=C d_i exists for these prescribed product conversions. Even O<=c*(h2(d_i)-B_i+sum spectator Jensen gaps) fails for every finite c. This does not refute choosing a different coordinate, preserving the incoming Bayes reference without immediate product conversion, using an actually unused ancestor account, or FEI.

## An explicit balanced core with nearly full Fourier support

Let K be the field with 2^l elements and let psi:K->{-1,1} be any fixed nontrivial additive character. Identify the physical cube on each K with l independent uniform bits, and use the characters psi(alpha*a+beta*b+gamma*x), indexed by K^3. The trace pairing, or equivalently any nontrivial additive character composed with multiplication, identifies every character uniquely. Nondegeneracy follows because multiplication by a nonzero element is bijective and psi is nontrivial.

Define the actual Boolean core on 3l bits by

    h_l(a,b,x)=psi(a) * (1-2*1_{x=a*b}).

For gamma=0 its Fourier coefficient is

    (1-2^(1-l))*1_{alpha=1,beta=0}.

For gamma!=0, averaging x first gives

    -2^(1-l) E_(a,b) psi((1+alpha)*a+beta*b+gamma*a*b).

For each a the b average vanishes except when beta+gamma*a=0. There is exactly one such a, since gamma is nonzero. Hence EVERY coefficient with gamma!=0 is nonzero, of magnitude 2^(1-2l). This is the elementary bilinear bent calculation; no probabilistic existence or uncomputed family is used.

The gamma=0 coefficient has magnitude c=1-2^(1-l)>0 for l>=2. The empty coefficient is zero, so h_l is balanced. Its Fourier support has cardinality

    s_l=(2^l-1)*2^(2l)+1.

Its squared spectrum has one atom c^2 and M_l=(2^l-1)*2^(2l) atoms of mass t_l=2^(2-4l). Parseval follows directly from c^2+M_l*t_l=1. Its entropy is the fully specified quantity

    H_h=-c^2 log2(c^2) + M_l*t_l*(4l-2).

All denominators used above are positive and l>=2 is essential: at l=1 the distinguished coefficient vanishes, changing the support count.

## Flatten every influence without changing the support counts

Add two physical bits u,v and let B(u,v)=(-1)^(u*v). Its four Walsh coefficients have magnitude 1/2. In old physical coordinates w=(u,v,a,b,x), define G_old=B and H_old=B*h_l. Their spectral laws are independent products of the flat two-bit bent spectrum with respectively the empty atom and the core spectrum. Their Fourier supports are disjoint because h_l has zero empty coefficient.

Apply the SAME invertible physical linear shear to BOTH children: in new bits t set w_u=t_u+sum_(j!=u)t_j (mod2), w_j=t_j for j!=u. This is an invertible cube permutation. New Fourier indicators are s'_u=s_u and s'_j=s_u+s_j for j!=u. The old s_u is a fair bit independent of EVERY other old spectral indicator, for both children, because the bent factor is independent and flat. Thus every new spectral indicator is fair for both G and H, proving all child influences exactly 1/2. Fourier entropy and support cardinality are preserved by the invertible shear. This changes influences by a proved calculation; arbitrary physical linear maps do not generally preserve influences.

Write n=3l+2. Both child product references are uniform on the 2^n spectral atoms. Child entropies are H_G=2 and H_H=2+H_h, and their actual certified S4=4I-H values are respectively 2n-2 and 2n-2-H_h. Since H_h<=3l=n-2 by the finite-support entropy bound, both S4 are >=n. This explicitly supplies certified child surplus for this family; it does not declare it previously unused or universally available.

## One actual selector query and every reference-only row

Let i be a fresh physical selector with F(i=0,t)=G(t), F(i=1,t)=H(t). For each remaining spectral set T, the parent coefficients are (Ghat(T)+Hhat(T))/2 and (Ghat(T)-Hhat(T))/2. Since the two supports are disjoint, their squares are equal. Therefore S_i is a fair bit independent of S_-i, and the erased law is (P_G+P_H)/2. Each remaining parent spectral marginal is fair as well. This proves d_i=1/2, every other d_j=1/2, B_i=1, and zero spectator Jensen gaps.

Disjoint child supports imply JS=1. The exact entropy identities are

    mean H_child=2+H_h/2,
    H_parent=4+H_h/2,
    TC_parent=(n+1)-H_parent=n-3-H_h/2,
    mean TC_child=n-2-H_h/2.

Their last difference is exactly 1; both complete terminal entropy and TC remain explicit.

The erased incoming product Q_e is uniform on the 2^n atoms. On G support the physical G kernel is 1; on H support it is 0; on every reference-only atom the declared extension is 1/2. Their Q_e masses are

    alpha=2^(-3l),
    beta=1-2^(-l)+2^(-3l),
    epsilon=1-alpha-beta=2^(-l)-2*2^(-3l)>0.

Thus r_G=alpha+epsilon/2=2^(-l-1). Dropping reference-only rows would give alpha instead and is an incorrect normalization. Both r_G,r_H are strictly positive. With O=KL(fair||r),

    O=-(1/2)log2(4r_G(1-r_G))
     =(l-1)/2-(1/2)log2(1-2^(-l-1))>(l-1)/2.

The signed conversion D=1+O therefore has D/d_i>l+1 although MI and every spectator gap are zero. The full entropy drop remains 2, so these divergent reference conversions cannot be used as entropy-drop counterexamples. Indeed I_parent=(3l+3)/2 and H_parent<=4+3l/2, giving H_parent/I_parent<2 for l>=2 since 4+3l/2<3l+3.

There is a direct one-owner repair for this family if that original owner is actually unused. Define ONCE at the parent Sbar=mean(4I_child-H_child)=2n-2-H_h/2. It satisfies Sbar>=9l/2+2. Since r_G<=1/8, -log2(1-r_G)<1, so D<(l+2)/2<Sbar/4 for every l>=2. Book this single D against Sbar; more than3Sbar/4 remains. Both complete child H+TC bills above are retained. This is an explicit all-dimensional one-transaction payment, conditional on that SAME Sbar having no other prior expenditure; it does not renew a bank at a descendant or combine it with a second copy of the child surplus.

## What this changes in the process argument

The earlier baseline CI-H is a supermartingale under the proved local hypothesis Delta H<=C*d; these particular distinguished queries satisfy that hypothesis at C=4 exactly. If the same step also requires immediate conversion to actual product references, that conversion has the independent unbounded debit above. Adding O as a supposedly free Jensen-funded compensator is invalid even when the child influence vectors agree coordinate by coordinate and both children have directly certified S4>=n.

If an original unused owner A_rem is carried into this history with earlier bookings retained, the required withdrawal for this transaction is [D]_+=1+O>(l+1)/2. It fits an available certified child reserve only after a valid ownership transfer; mere equality of influence vectors and the entropy telescope do not supply that transfer. Delaying conversion leaves the inherited Bayes reference and terminal KL bill intact and avoids asserting a free new product.

For the one-step fair filtration F_0={empty,Omega}, F_1=sigma(the actual selector), the baseline entropy decrement is exactly2 and influence loss exactly1/2. Thus 4I-H has zero conditional mean increment at this step. If the unused original Sbar is supplied, put R_0=TC_parent+Sbar and R_1=TC_child+Sbar-D. The residual account Sbar-D is positive and is counted with physical reaches1/2, not twice. Then E[R_1+O | F_0]=R_0 because mean TC_child-TC_parent=1 and D=1+O. This is a concretely paid compensated process for the proved hypothesis, with BOTH actual terminal H+TC retained; it is not a universal multi-step availability theorem.

The first unsupported universal line remains: choose a physical query/history whose complete signed conversions fit genuinely unused SAME ancestor capacity, retaining full terminal H+TC and existing bookings. This family refutes the proposed purely local product-reference price; it neither refutes that selected nonlocal line nor proves a universal eligible owner.

## Verification scope

The proof above is all-dimensional. Executed integer Walsh and rational-support checks are recorded separately for l=2,3 and boundary l=1. They test the Boolean realization, field arithmetic, shear, all influence vectors, disjoint supports, support counts, entropy identity via exact prime-log coefficients, predicted outcome normalization including every reference-only row, and the strict rational inequality behind O's lower bound. A Lean attempt addresses only the cleared algebraic step identified in its receipt; no full entropy/finite-field formalization is claimed.
