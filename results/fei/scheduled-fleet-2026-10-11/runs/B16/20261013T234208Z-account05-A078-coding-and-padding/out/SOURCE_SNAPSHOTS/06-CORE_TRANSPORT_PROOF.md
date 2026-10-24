# Arbitrary-core quarter-profile transport with physical padding cost

All inputs are independent fair signs; entropy is in bits. A core query writes g=u+zv, alpha=E v^2, mu=E u, nu=E v. Define P(g,i)=sum_T |uhat(T)|^(1/2)|vhat(T)|^(3/2), and L=6P. The universal local majorant and the entropy decrement Delta H<=L+(9/2)alpha are proved in PROFILE_LEMMA.md. This document makes no admission assumption on g.

## 1. Free physical splits

If uhat(T)vhat(T)=0 for every T, then P=Q=M=B=0. Both actual child spectra equal uhat^2+vhat^2, so their Jensen-Shannon divergence is zero and Delta H=0. Such a query is admissible at zero entropy cost regardless of its antichain or degree-transport tests. In particular a parity-core query in a mixed majority root can be free. Raw failures of those two structural tests alone are not a universal selection obstruction.

## 2. Mixed majority, including arbitrary cores

Let m>=2 be even and F(x,y)=sign(sum_{j=1}^m x_j+g(y)). This is an actual Boolean function since the argument is odd. Write c(x)=1{sum x=0}, b(x)=sign(sum x) with b=0 on ties. Then F=b+c g. Let a_m=E c=2^-m binom(m,m/2). The Fourier support of b has odd x-degree, and that of c has even x-degree, by global sign reversal.

At any core query, U=b+c u and V=c v. In odd x-degree V vanishes. In even x-degree the pair is chat(W)(uhat(T),vhat(T)); hence

    P(F,i)=a_m P(g,i),     Inf_i(F)=a_m Inf_i(g).

Every ordinary-coordinate influence is a_m: the other m-1 signs must sum to plus or minus one, each with probability a_m, and g picks which of the two. Therefore the complete physical influence is

    I(F)=a_m [m+I(g)].

The same disjoint Fourier sectors give the exact entropy identity

    H(F)=H(Maj_(m+1))+a_m H(g).

Indeed the squared spectra are b-hat(W)^2 in the odd sector (T empty) and c-hat(W)^2*g-hat(T)^2 in the even sector, of total mass a_m. Replacing g by a dictator gives Maj_(m+1) and zero core entropy. The extra ordinary influence a_m m is explicit; the transported core entropy remains unpaid. This entropy identity is also the mixed-composition baseline already in A076, not a new class result.

## 3. Activation: exact empty-sector correction

For s>=1 controls let A=1{all controls at one fixed vertex}, p=2^-s, and F=1+A(g-1). Its control Fourier coefficients have magnitude p. At a core query U=1+A(u-1), V=A v. Direct enumeration of the Fourier sectors gives the exact identity

    P(F,i)=p[P(g,i)-|mu|^(1/2)|nu|^(3/2)]
           +p(1-p)|1-mu|^(1/2)|nu|^(3/2)
           +p^(3/2)|1-p+p mu|^(1/2)|nu|^(3/2).

The first term is the sum over nonempty core frequencies, the second has empty core and nonempty control frequency, and the third is the fully empty frequency. Their signs at the chosen active vertex disappear in the absolute values. This is not a formal spectral-law construction: it was derived from the Boolean truth formula above.

Since |mu|<=1, |nu|<=E|v|=alpha, sqrt(2)<=3/2, and sqrt(p)<=1, dropping the negative term yields

    L(F,i)<=p L(g,i)+15 p alpha,
    Inf_i(F)=p alpha.

The padding charge is dimension independent, while its physical control influence is separately

    I_controls(F)=s p(1-E g),
    I(F)=p I(g)+s p(1-E g).

For a control query the other controls must be active and the core must equal -1, which gives each control influence p(1-E g). Thus this term has not been omitted or counted as a free leaf.

The complete activation spectrum also follows from the same Boolean formula. The fully empty coefficient is 1-p+p E g; every nonempty control frequency with empty core has magnitude p|E g-1|; every frequency with nonempty core has magnitude p|g-hat(T)|. Empty-sector collisions are retained exactly. No claim that activation preserves H(g) unchanged is made.

## 4. Core-first stopping tree with a paid terminal padding leaf

Take any complete physical decision tree of the core, and query those core bits first in F. At a history v the residual is again 1+A(g_v-1), with the same p and control block. Let L_tree(g)=sum_v w_v L(g_v,i_v). Core influences telescope: sum_v w_v Inf_i(g_v)=I(g). Thus

    sum_v w_v Delta H(F_v)
       <=p L_tree(g)+(39/2)p I(g).

When the core leaf is +1 the padded function is constant. When it is -1 the leaf is 1-2A, a point defect on s controls. This leaf has I=2s p and H<=4I. To check the latter directly, its empty Fourier coefficient is 1-2p and its other 2^s-1 coefficients have magnitude 2p. The nonempty entropy is 4p(1-p)(2s-2). The empty entropy is at most [1-(1-2p)^2]/ln2<=6p(1-p), using ln2>=2/3. Hence H<=p(1-p)(8s-2)<=8s p=4I, also covering s=1 by zero-mass continuity.

The probability of the -1 leaf is (1-E g)/2. Including its actual entropy and influence gives

    H(F)<=p L_tree(g)+(39/2)p I(g)+4s p(1-E g).

Consequently, if that particular core tree has L_tree(g)<=K I(g), activation satisfies H(F)<=max(K+39/2,4)I(F). The core-tree hypothesis is explicit; this does not prove it for arbitrary cores. Global output negation preserves the profile, entropy, and influence, so the same ledger applies to negative activation and to activation of -g, which occur after ordinary-coordinate restrictions of mixed majority.

## 5. Exact frontier

The transport identities hold for every Boolean core and all stated m,s. Their finite certificates check actual Walsh spectra and physical edge influences. They prevent padding from silently hiding a remaining core-profile cost, and show that the empty Fourier sector of activation incurs at most a fixed local tax.

The first unsupported universal line is a dimension-independent bound L_tree(g)<=K I(g) for some appropriate complete or paid stopping tree of every arbitrary core, or a universal replacement majorant that pays the retained Q directly. The antichain-plus-degree-transport certificate in PROFILE_LEMMA.md is sufficient, not necessary: a failed structural test must first be checked for free splits and verified tensor spectators. No universal FEI theorem or counterfamily is claimed.
