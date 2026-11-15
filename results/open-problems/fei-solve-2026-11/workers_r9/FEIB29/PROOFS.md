# The summed B direction

Every assertion in this file marked PROVED has a derivation below. The numerical evidence is separate. Logarithms are base two; E(f)=sum_i E_i(f), B(f)=I(f)-W1(f), and p_i=Inf_i(f). Constants and characters have E=0. Ratios with B=0 are omitted.

## 1. Equivalence to FEI without a stability theorem

PROVED. For R subset [n], put g=chi_R f. Then

    ghat(S)=fhat(S symmetric_difference R),
    E_i(g)=E_i(f),
    Inf_i(g)=p_i if i not in R, and 1-p_i if i in R.

The Fourier identity follows by multiplying characters. Translation by R sends the unordered Fourier pair {T,T+i} to another such pair, possibly swapping its endpoints. Phi is symmetric, so each coordinate's erasure is invariant, not just their sum.

The Boolean derivative D_i f takes values 0,+1,-1. Consequently

    |fhat({i})|=|E D_i f| <= E|D_i f|=p_i,
    B_i=p_i-fhat({i})^2 >= p_i(1-p_i).

Choose R={i:p_i>1/2}. Then

    D(f):=I(chi_R f)=sum_i min(p_i,1-p_i) <= 2 B(f).              (1)

If E(h)<=K I(h) for every Boolean h, apply it to chi_R f to obtain

    E(f)<=K D(f)<=2K B(f).                                    (2)

Conversely B<=I, so a universal B inequality implies the erasure version of FEI. The supplied erasure sandwich H-(2/ln 2)I<=E<=H then proves equivalence to ordinary entropy FEI. If K_E, K_B, K_H denote the respective optimal constants, including infinity, the proved comparisons are

    K_E <= K_B <= 2 K_E,
    K_E <= K_H <= K_E+2/ln 2.

No equality of these three optimal constants is asserted. In particular, the near-dictator constant identified below is K_E, not automatically the full entropy constant K_H.

Literature check: the entropy invariance, parity minimization, and exactly D<=2B already appear in Lemma 2.2 of [the author, arXiv:2610.16069v1](https://arxiv.org/html/2610.16069v1). No novelty is claimed for (1). The additional observation needed here is erasure invariance.

## 2. Uniform estimates at distance delta from a dictator

PROVED. Suppose Pr[f != s x_j]=delta<1/2, s in {+1,-1}. Set g=s x_j f. Then Pr[g=-1]=delta, and E(g)=E(f). A coordinate can have its pivotal status changed from that of s x_j only if at least one endpoint of its cube edge belongs to the error set. The union bound gives

    q_i:=Inf_i(g)<=2delta for every i.

Here q_j=1-p_j and q_i=p_i for i!=j. Therefore

    B(f)>=sum_i p_i(1-p_i)=sum_i q_i(1-q_i)
         >=(1-2delta) I(g).                                  (3)

In particular, conditional on erasure FEI with constant K_E,

    E(f)/B(f) <= K_E/(1-2delta).                             (4)

This is a dimension-free bound only conditional on FEI. Presenting it as an unconditional proof for all near-dictator functions would be incorrect.

Also fhat({j})=s(1-2delta), hence

    B(f)-I(g)=2p_j-1-W1(f)
             <=1-fhat({j})^2=4delta(1-delta).

Edge isoperimetry for the minority set of g gives I(g)>=2delta log(1/delta). Combining,

    1-2delta <= B(f)/I(g) <= 1+2(1-delta)/log(1/delta).       (5)

Thus B and I(g) are asymptotically equal uniformly in the dimension and the shape of the error set. The empty Fourier coefficient of f satisfies |fhat(empty)|<=2delta, as suggested in the brief. However, no collection of low-level estimates can turn (4) into an unconditional constant without resolving FEI; the reduction in Section 3 explains why.

PROVED quantitative stability in the proposed danger zone. If epsilon=B/I<1/8, then W1<=1 implies I<=1/(1-epsilon), B<=epsilon/(1-epsilon). For the minimizing parity R in Section 1, Poincare gives Var(chi_R f)<=D<=2B and hence fhat(R)^2>=1-2B. If |R|>=2, then B>=|R| fhat(R)^2>=2(1-2B), contradicting B<1/7. If R is empty, I=D<=2B, contradicting epsilon<1/8. Therefore R is a singleton. Its closest sign gives dictator distance

    delta=(1-|fhat(R)|)/2 <= B <=epsilon/(1-epsilon).

This proves the needed qualitative FKN-type conclusion directly, with explicit constants. It does not control the entropy hidden inside the error set.

## 3. The exact near-dictator asymptotic supremum

PROVED. Let

    K_E=sup_h E(h)/I(h),
    A(delta)=sup E(f)/B(f)

where the second supremum ranges over all finite dimensions and Boolean functions at distance exactly delta from a specified signed dictator. Feasible delta are positive dyadic rationals. Then

    K_E <= A(delta) <= K_E/(1-2delta),  0<delta<1/2,          (6)
    lim_{delta -> 0, dyadic} A(delta)=K_E.                    (7)

The statements include K_E=+infinity: then A(delta)=+infinity for every fixed feasible delta. They identify the constant exactly in terms of an existing open optimization problem; they do not supply its unknown numerical value or prove it finite.

For the lower bound, start with any nonconstant Boolean h. On independent input blocks form the balanced core

    b_t=z product_{r=1}^t h(x^(r)).

Tensor products add spectral erasure and influence, and multiplication by the fresh sign adds one influence and zero erasure. Thus

    E(b_t)=t E(h),  I(b_t)=t I(h)+1,  E b_t=0.

Fix any Boolean indicator a on fresh controls with mean p=2delta. Define

    G_t=1+a(b_t-1),  f_t=w G_t

with another fresh sign w. Then Pr[G_t=-1]=p/2=delta, so f_t has exactly the required dictator distance. Direct derivatives give

    I(G_t)=p I(b_t)+2 I(a),
    Var(G_t)=2p-p^2,
    B(f_t)=I(G_t)+Var(G_t).

In I(a), a is real-valued {0,1} and the Fourier convention is unchanged. For each data coordinate, pairs with nonempty lower data set contribute p times the corresponding core erasure, by Parseval over the control spectrum and homogeneity of Phi. A pair whose lower data set is empty contributed zero in the balanced core; its new contribution is nonnegative. Hence

    E(f_t)=E(G_t)>=p E(b_t)=p t E(h).

It follows that

    E(f_t)/B(f_t)>=p t E(h)/[p(t I(h)+1)+2 I(a)+2p-p^2]
                 ->E(h)/I(h).

Take the supremum over h. The upper bound in (6) is (3) with the definition of K_E, so (7) follows.

PROVED stronger localization. The same limiting constant is possible along near-dictators for which B->0, I->1, and W1->1, not just along examples with large influence. Take the control event to be one point on r bits, p=2^-r, t=floor(2^(r/2)). Then I(a)=rp/2 and

    B(f_t)=p[t I(h)+1+r+2-p]->0,
    E(f_t)/B(f_t)>=t E(h)/[t I(h)+r+3-p]->E(h)/I(h).

Thus even the strict I-W1 << I danger zone can carry every unrestricted erasure ratio. A claim that all sufficiently near dictators have asymptotic ratio 2 is false. Sparse subcube perturbations have ratio 2 because their core is simple, not because their dictator distance is small.

The multiplication and rare-activation ideas have prior art. [the author, Section 8.4](https://arxiv.org/html/2610.16069v1#S8.SS4) gives the analogous constant-preserving statement for full spectral entropy and cites Wan-Wright-Wu and Shalev. The proof above is supplied in full for erasure and B; no novelty claim is made.

## 4. Symmetric functions

PROVED using the established symmetric FEI theorem. For a symmetric function all p_i coincide. Its minimizing parity is either empty or all of [n]; multiplying by the full parity preserves symmetry. Apply the symmetric entropy FEI bound 12.04 from O'Donnell-Wright-Zhou to that function, and then (1):

    E(f)<=H(chi_R f)<=12.04 D(f)<=24.08 B(f).

This deliberately uses an established, nonsharp constant. The theorem and its constant are in [O'Donnell-Wright-Zhou, Theorem 1](https://yuanz.web.illinois.edu/papers/fei-icalp.pdf). No sharp symmetric B constant is claimed.

## 5. Read-once formulas of bounded gate arity

PROVED reduction from FEI+. Let V=Var(f) and H_*=sum_{S nonempty} mu(S) log(1/mu(S)). Erasure pairs whose lower endpoint is nonempty have total at most V H(mu conditioned nonempty)<=H_*: apply the general erasure<=entropy inequality to the normalized nonempty distribution. The omitted empty-to-singleton pairs obey, coordinate by coordinate,

    Phi(fhat(empty)^2,fhat({i})^2)<=2 B_i.                    (8)

Indeed, Boolean restrictions give |fhat(empty)|<=1-p_i and |fhat({i})|<=p_i. The scalar inequality Phi(u,v)<=2 sqrt(uv) then bounds the left side by 2p_i(1-p_i)<=2B_i. For completeness, the scalar inequality is the elementary h2(t)<=2 sqrt(t(1-t)); one proof sets u=e^s,v=e^-s, differentiates 2cosh(s)ln(2cosh(s))-2s sinh(s), and obtains its maximum 2ln 2 at s=0. The complete derivative calculation is also in ../FEIB27/PROOFS.md Section 6.

Thus

    E(f)<=H_*+2B(f).                                        (9)

O'Donnell-Tan's product-measure FEI+ theorem says that read-once formulas over gates of arity at most k satisfy H_*<=C_k(I-V), uniformly in formula size and depth. Since I-V=sum_{|S|>=2}(|S|-1)mu(S)<=B,

    E(f)<=(C_k+2)B(f).                                      (10)

An explicit, loose choice from their Lemma 2 and composition theorem is C_k=8^k/ln 2. To see the stated constant, their lemma bounds a nonempty-set contribution by (4^k/ln 2)Var(D_j^phi F) for any j in S. Assign each S to its least j; no j receives more than 2^(k-1) sets. Sum and use sum_j Var(D_j^phi F)<=2(I-V). Their Theorem 1 composes with the maximum gate constant, not its product.

Reference: [O'Donnell-Tan, Lemma 2 and Theorems 1-3](https://www.cs.cmu.edu/~odonnell/papers/fei-composition.pdf). For arbitrary, unbounded gate arity the class includes every Boolean function as a single gate, so a uniform constant independent of arity would be full FEI.

## 6. Exact composition rules

PROVED. Suppose psi is balanced, F has k inputs, and f=F(psi,...,psi) on disjoint blocks. Write a_i=psihat({i})^2 and p_j=Inf_j(F). For i in block j,

    E_{j,i}(f)=p_j E_i(psi)
       +sum_{A subset [k] without j} Phi(mu_F(A),a_i mu_F(A+j)).    (11)
    I(f)=I(F) I(psi),
    W1(f)=W1(F) W1(psi),
    B(f)=I(F) B(psi)+B(F) W1(psi).                           (12)

The spectral block support A is sampled from mu_F, then each active block independently samples a nonempty set from mu_psi. For pairs with a nonempty lower set within block j, active status is known and homogeneity gives the first term. The remaining pairs toggle block activity, giving the second term. Singleton sets can only come from singleton outer and singleton inner sets, proving W1.

The scalar convexity of x log x gives, for 0<=a<=1,

    a Phi(p,q)<=Phi(p,aq)<=a Phi(p,q)+aq log(1/a).

Consequently, with H1(psi)=sum_i a_i log(1/a_i),

    E(f)<=I(F) E(psi)+W1(psi) E(F)+I(F) H1(psi).             (13)

The extra term matters. The bound by max{E(F)/B(F),E(psi)/B(psi)} does not compose: the balanced three-variable one-bit address gate has ratio 1, whereas its depth-two self-composition has ratio about 1.201205. The numerical check is retained in audit.json. FEI+ provides the correct depth-independent closure in Section 5.

PROVED general biased rule used for the towers. Let c=E psi, v=1-c^2, and

    K_A(c)=sum_{D superset A} Fhat(D)c^(|D|-|A|).

For coordinate i in block j,

    E_{j,i}(f)=sum_{A subset [k] without j} v^|A|
      [Phi(K_A^2,K_{A+j}^2 a_i)
         +K_{A+j}^2(E_i(psi)-Phi(c^2,a_i))],
    Inf_{j,i}(f)=Inf_i(psi) sum_A v^|A| K_{A+j}^2,
    fhat(empty)=K_empty(c),
    fhat({j,i})^2=K_{j}(c)^2 a_i.                           (14)

Expand F in characters and collect active blocks. A Fourier coefficient with nonempty sets S_l in blocks A is K_A(c) product_{l in A} psihat(S_l). Summing squared coefficients over nonempty sets in every other active block supplies v^|A|. Separate the empty pair of psi from all other pairs to obtain (14). This is an exact identity, not an independence approximation. composition.py checks it against direct transforms before any large tower is evaluated. No truth table above 14 variables is needed for towers.

## 7. Decision trees of depth d

PROVED. For a Boolean function computed by a decision tree of maximum depth d>=1, every Fourier coefficient is an integer multiple of 2^(1-d). Expand each leaf indicator into characters, pad denominators to 2^d, and use f=1-2 times the indicator of its negative leaves. The constant coefficient has the same grid because 1 is on it. Thus every nonzero spectral atom is at least 2^(2-2d). Character translation preserves that grid.

Let g=chi_R f minimize influence. If V=Var(g), its nonempty spectral entropy is at most 2(d-1)V; the empty atom contributes at most V/ln 2, since -x ln x<=1-x. Therefore

    E(f)=E(g)<=H(g)<=[2(d-1)+1/ln 2]V
         <=[2(d-1)+1/ln 2]I(g)
         <=[4(d-1)+2/ln 2]B(f).                             (15)

This applies to arbitrary decision trees of depth d, without a read-once assumption. Constants have E=0 separately. The coefficient grid and inequalities are elementary; the result is not claimed sharp or novel.

## 8. What is still open

PROVED additional closed-form checks. For AND_n, n>=2, put q=4^(1-n), m=1-2^(1-n). All nonempty Fourier masses are q, and the empty mass is m^2. Therefore

    R(AND_n)=2+Phi(m^2,q)/[2^(1-n)-q]<=4,
    lim_{n->infinity} R(AND_n)=2.

The upper bound follows from Phi(m^2,q)<=2m sqrt(q); equality is attained at n=2. For the k-control address function, the spectral sample contains exactly one data coordinate and an independent uniform subset of the k controls. Thus

    E=k, I=1+k/2, W1=2^-k,
    R=k/[1+k/2-2^-k].

The controls each contribute one bit of erasure, while each data coordinate has zero erasure.

OPEN. A numerical universal B constant, unconditional boundedness for all near-dictator functions, and full FEI. Sections 1 and 3 explain why those requests cannot be completed independently of FEI. The class bounds above are unconditional once the cited established theorems are invoked. Numerical maxima in the other files are lower bounds, not universal upper bounds.
