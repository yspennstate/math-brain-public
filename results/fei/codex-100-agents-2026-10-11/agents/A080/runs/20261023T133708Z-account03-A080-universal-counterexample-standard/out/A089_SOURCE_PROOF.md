# A smaller universal reserve for the signed composition correction

All Fourier transforms are normalized real transforms on independent uniform physical bits; entropy is in bits. The original disjoint partition remains fixed under restrictions. This is a coherence theorem, not an initial influence-payment theorem. Full FEI remains OPEN.

## 1. Original failed statement and actual counterexample

The proposed universal superharmonic envelope

    U_K = C_+ + sum_j q_j rho_K(g_j)

is FALSE, where C=H(h(g))-sum_j q_j H(g_j), q_j is the true pivotal probability under the other output biases, and rho_K is the full stopping hull of (H-KI)_+. A071-POSITIVE-OUTER-CORRECTION-ENVELOPE-FAILS@1 supplies a literal seven-bit witness. Let g_m be -1 only at the all-zero string, otherwise +1, and let h be +1 only at (+1,+1,+1). Take F=h(g_3,g_2,g_2), and query the first physical bit of g_3. The two full children are h(g_2,g_2,g_2) and h(+1,g_2,g_2), the latter retaining its two dummy physical bits. Every inner hull is zero for every real K>=3, while all three C values are positive. Indeed every restriction of g_m for m<=3 is constant or g_l, l<=3; their entropy/influence pairs are (0,0), (0,1), (2,1), and (4-(9/8)log2(3),3/4). The last ratio is below3 because 3^9>2^14. Hence the full hull is zero by backward induction.

The three corrections, reproduced from whole physical truth tables, are

    C_parent=57/8-(1431/1024)log2(3)-(3087/2048)log2(7),
    C_0=53/8-(1701/512)log2(3)-(25/512)log2(5),
    C_1=3-(27/16)log2(3).

Their positivity is respectively equivalent to 2^14592>3^2862*7^3087, 2^3392>3^1701*5^25, and 2^48>3^27. The positive drift is

    G=-37/16-(567/512)log2(3)-(25/1024)log2(5)
        +(3087/2048)log2(7),
    0.107184<G<0.107185,

with its strict sign equivalently 7^3087>2^4736*3^2268*5^50. The queried physical influence is9/64. This defeats the proposed envelope, including A089 stage9 NEXT, and does not refute FEI or the conditional rerouting theorem.

## 2. A Boolean coefficient constraint sharpens the exceptional row

Let g be any Boolean function and i a coordinate. Set mu=E g, t=ghat({i}), d=Inf_i(g). The two restriction means are mu+t and mu-t, so

    |mu|+|t| = max(|mu+t|,|mu-t|) <=1.

Also |t|<=d: the signed derivative has expectation t and absolute expectation d. Put a=|mu|, b=|t|. Define Phi(A,B)=(A+B)log2(A+B)-Alog2(A)-Blog2(B), with zero terms interpreted continuously. For a,b>0,

    (ln2) Phi(a^2,b^2)
      =a^2 ln(1+b^2/a^2)+b^2 ln(1+a^2/b^2)
      <=b^2+ab=b(a+b)<=b<=d.

Here ln(1+x)<=x gives the first bound, and ln(1+s^2)<=s for s>=0 gives the second. The latter follows because the derivative of s-ln(1+s^2) is (s-1)^2/(1+s^2)>=0 and its value at0 is0. Cases a=0 or b=0 follow directly: Phi=0. Thus the state-sensitive bound Phi(mu^2,t^2)<=|t|(|mu|+|t|)/ln2 improves the source's 2d/ln2 bound to d/ln2.

## 3. Independent reconstruction of the signed drift identity

For any Boolean u, pair coefficients a_L=uhat(L), b_L=uhat(L union{i}), L omitting i. Let B_i(u)=sum_L Phi(a_L^2,b_L^2), and J_i(u) be the Jensen-Shannon divergence of the squared Fourier laws of its two full restrictions. These laws are (a_L+b_L)^2 and (a_L-b_L)^2 and each is normalized; their mean is a_L^2+b_L^2. The entropy chain rule and concavity give exactly

    H(u)-mean H(u|i=b)=B_i(u)+J_i(u),   J_i(u)>=0.

The plus sign is essential. For each row let s=a^2+b^2 and x=2ab/s. Its contribution to J is s G(x)/ln2, where G(x)=((1+x)ln(1+x)+(1-x)ln(1-x))/2. On[-1,1], G(x)<=1-sqrt(1-x^2): both are even, vanish at0, and for x>=0 the derivative comparison is atanh(x)<=x/sqrt(1-x^2), itself obtained by comparing derivatives 1/(1-x^2)<=1/(1-x^2)^(3/2). Continuity treats endpoints and zero rows. Therefore each contribution is at most2 min(a^2,b^2)/ln2, and

    J_i(u)<=2 Inf_i(u)/ln2.

Now let F=h(g_1,...,g_r), on disjoint finite physical blocks. Constants, empty blocks and dummies are allowed. For a query i in block j write h=A+z_j D. Pointwise A,D lie in{0,+1,-1}, A D=0, and E D(g_-j)^2=q_j. Every full Fourier coefficient whose block-j frequency L is nonempty factors as ghat_j(L) times the corresponding Fourier coefficient of D(g_-j). Only L=empty has the extra A contribution. In the erasure pairing, let B_special be the sum of Phi contributions over all rows whose REMAINING block-j frequency is empty; it is nonnegative. Homogeneity of Phi and Parseval for D prove

    B_i(F)=q_j[B_i(g_j)-Phi(mu^2,t^2)]+B_special.

No division by an inner variance occurs. Under a physical query, q_j is unchanged. Every q_k, k!=j, has its conditional mean conserved, since it is affine in the distribution of g_j and that output law is the mixture of the two restriction laws. All other core entropies are unchanged. Subtracting the weighted inner entropy decrements gives the exact identity

    mean C_child-C_parent
      =q_j[Phi(mu^2,t^2)+J_i(g_j)]-B_special-J_i(F).

This reconstructs A072-SIGNED-COMPOSITION-DRIFT-COHERENT-ENVELOPE@1 unchanged. Its original4/ln2 bound and conditional owner propagation survive. The sharpened statement below is a separate contributed extension, not a silent amendment or independent review of our own extension.

## 4. Sharpened universal replacement

Combining Sections2-3 gives, for every finite Boolean outer gate, arbitrary disjoint Boolean inner blocks and every physical query,

    mean C_child-C_parent
      <= q_j[ |t|(|mu|+|t|)+2d ]/ln2
      <= (3/ln2) Inf_i(F) < (9/2) Inf_i(F)

when Inf_i(F)>0; the weak9/2 inequality also holds at zero influence. The last step uses Inf_i(F)=q_j d and ln2>2/3, obtained from the first term of ln2=2 sum_(k>=0) (1/3)^(2k+1)/(2k+1). The retained exact identity is stronger whenever its nonnegative subtractions matter. We do not claim3/ln2 is optimal.

For kappa=3/ln2 or9/2, define V=C+kappa I(F). The exact influence decrement is I(parent)-mean I(children)=Inf_i(F), as follows from physical edges or Fourier pairing. Thus V is superharmonic for every query. At full revelation it is0, so finite backward induction proves V>=0 at every state, even though C itself can be negative.

Fix K>=0. Define each full inner stopping hull by rho(g)=max((H(g)-K I(g))_+, max_i mean rho(g|i=b)), with zero at constants. Then

    A_K=C+kappa I(F)+sum_j q_j rho(g_j)

is nonnegative and superharmonic for every physical query. For the queried block use its hull inequality and unchanged q_j; for every other term use the conserved conditional mean of q_k and unchanged rho(g_k). Also rho(g_j)>=H(g_j)-K I(g_j) implies C+sum q_j rho(g_j)>=H(F)-K I(F), so A_K majorizes (H(F)-K I(F))_+. A fixed original partition includes all cores from the start; merely admitting one changes no potential. Changing the partition requires a separate comparison.

The seven-bit witness consumes mean drift G, whereas a rational9/2 influence reserve releases(9/2)(9/64)=81/128. Its strictly positive surplus is81/128-G, with both full children and dummy coordinates preserved. This pays the failure row from an ACTUALLY SUPPLIED reserve.

## 5. Owners and the first unpaid line

Given genuinely supplied incoming credit a>=A_K(parent), put a_b=A_K(child_b)+a-mean A_K(children). Then a_b>=0, mean a_b=a, and a_b>=A_K(child_b). Every old nonnegative credit owner c uses c_b=c*a_b/a when a>0; if a=0, both child credits and every old credit owner are zero. Thus each owner conserves its conditional mean. With S_b=H(F_b)-K I(F_b), booked debits d_b=S_b+a_b are nonnegative. Let T=mean d_b. Keep all old signed debit labels and add the signed query charge e=mean S_b-S_parent; their total is T. For T>0 use their common kernel d_b/T, of conditional mean1. For T=0 use kernel1, keeping their signed zero-total labels and both zero child totals. Old reaches, stopped siblings and spent outside donors remain unchanged. This is bookkeeping for a supplied bank; an influence component is not a fresh donor after its original owner has spent it.

There is an all-partition price sandwich. Section3 proves that H itself is superharmonic. Its nonnegative stopping payoff (H-KI)_+ is at most H, so finite backward induction gives0<=rho_K(g)<=H(g). Also rho_K(g)>=H(g)-K I(g). Thus the inner savings sigma_j=H(g_j)-rho_K(g_j) satisfy0<=sigma_j<=K I(g_j), and exactly

    A_K=H(F)+kappa I(F)-sum_j q_j sigma_j,
    H(F)+(kappa-K)I(F)<=A_K<=H(F)+kappa I(F).

These bounds hold for EVERY fixed disjoint partition, even if one chooses a different partition for each F. In particular K=0 gives A_0=H+kappa I for every partition. At any fixed K, an initial bound A_K<=L I would imply FEI with constant L+K-kappa; conversely FEI with constant C implies A_K<=(C+kappa)I. This is a precise equivalence of the existential finite constants, not an assertion of them.

First unsupported universal line: supply A_K initially from O(I) of the SAME unused original owners for arbitrary Boolean functions. Singleton physical-bit cores give the sharper identity rho=0,C=H(F),A_K=H(F)+kappa I(F), but the general sandwich shows that nontrivial partitions do not evade the FEI-equivalent initial-price problem at fixed K. The25% reduction of the analytic drift coefficient moves universal coherence, not this initial-price bridge. No unconditional history-transfer or universal FEI theorem is asserted.
