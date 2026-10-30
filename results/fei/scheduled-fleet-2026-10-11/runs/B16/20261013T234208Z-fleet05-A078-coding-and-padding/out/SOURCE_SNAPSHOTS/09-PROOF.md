# One common data bit: actual signed packet transport

All bits are independent uniform signs. Branches G(s,X), H(s,Y) share at most the one physical bit s; X,Y,z are mutually disjoint, and z is a fresh selector. Let F=(G+H)/2+z(G-H)/2. Put phi(p)=p log2(1/p), Phi(p,q)=phi(p)+phi(q)-phi(p+q), with continuous zero boundaries.

## 1. A symmetric shift bound with an exact comparison row

For arbitrary real u,d,v, define

    S(u,d;v)=[Phi((u+v)^2,d^2)+Phi((u-v)^2,d^2)]/4
                  -Phi(u^2,d^2)/2.

Then

    -Phi(u^2,d^2)/2 <= S(u,d;v) <= Phi(v^2,d^2)/2.       (1)

The lower bound is immediate. In natural units,

    Phi_nat(u^2,d^2)=integral_(0)^(d^2) ln(1+u^2/t) dt.

Differentiate in d^2 and use the zero boundary. For t>0 the symmetric-difference integrand is the log of

    A=((u+v)^2+t)((u-v)^2+t)/(u^2+t)^2
     =1+2v^2(t-u^2)/(u^2+t)^2+v^4/(u^2+t)^2.

Since (t-u^2)/(u^2+t)^2<=1/t and 1/(u^2+t)^2<=1/t^2, A<=(1+v^2/t)^2. Integrate and divide by four and ln2 to prove (1); all singularities at zero are integrable. Degenerate cases follow by continuity. In particular

    -|u d| <= S(u,d;v) <= |v d|,                        (2)

by Phi(a^2,b^2)<=2|ab|. For an elementary proof, differentiate Phi_nat(1,t^2)/(2t) on (0,1]. Its derivative numerator (t^2-1)ln(1+t^2)-t^2 ln(t^2) is nonnegative by ln(1+x)<=x and -ln x>=1-x. The maximum is ln2 at t=1. Homogeneity and symmetry give the envelope. The upper comparison (1) is exact at u=0; it retains the actual other-branch row instead of a child-kappa logarithm.

## 2. Private-coordinate rows

For a private X query i, common frequency indices C are empty and {s}, or empty alone after s is fixed. Let g_C=Ghat(C), d_C=Ghat(C union {i}), h_C=Hhat(C). Nonempty private X rows are copied at amplitudes +/-Ghat/2 and give half their original erasure. Private Y rows have zero i amplitude. Only the common C rows collide, giving exactly

    B_i(F)=[B_i(G)+B_i(H)]/2+D_i,
    D_i=sum_C S(g_C,d_C;h_C),                           (3)

with B_i(H)=0. For private Y interchange the branches. Thus

    -sum_C Phi(g_C^2,d_C^2)/2 <= D_i
                    <= sum_C Phi(h_C^2,d_C^2)/2.        (4)

The common coefficients transform a bounded one-bit conditional private mean, so

    |h_empty|+|h_s|=max(|E(H|s=+1)|,|E(H|s=-1)|)<=1,

and likewise for g. After s is fixed use |E H|<=1. Physical half-differences D_iG in {-1,0,1} give |d_C|<=Inf_i(G). Applying (2) to (4) yields

    |D_i|<=Inf_i(G)=2 Inf_i(F).                         (5)

The two rows are priced jointly using the same physical influence.

## 3. The common physical query

At s write mu=Ghat(empty), nu=Hhat(empty), a=Ghat({s}), b=Hhat({s}). Only the empty-private rows overlap, giving

    D_s=[Phi((mu+nu)^2,(a+b)^2)
                   +Phi((mu-nu)^2,(a-b)^2)]/4
                    -[Phi(mu^2,a^2)+Phi(nu^2,b^2)]/2.   (6)

The positive sum is at most

    [|(mu+nu)(a+b)|+|(mu-nu)(a-b)|]/2
       <=max(|mu|,|nu|)(|a|+|b|)<=|a|+|b|,

using |mu+nu|+|mu-nu|=2max(|mu|,|nu|). The negative part has magnitude at most |mu a|+|nu b|<=|a|+|b|. Since |a|<=Inf_s(G), |b|<=Inf_s(H), and Inf_s(F)=[Inf_s(G)+Inf_s(H)]/2, (5) also holds at s. The actual shared physical influence is counted once, not two nominal allowances.

The factor two is sharp: G=-1,H=s gives D_s=B_s(F)=1 and Inf_s(F)=1/2, with inherited erasures zero. Irrelevant declared common bits are permitted. A negative fixture is G(s,x),H(s,y) each +1 only at its zero vertex. At x,

    D_x=-3/2+(5/8)log2(5)<0,

since 5^5=3125<4096=2^12; Inf_x(F)=1/4. Signed credit is retained and is not spent twice.

## 4. Every adaptive data-only prefix

A finite prefix T queries unfixed s,X,Y coordinates in any adaptive order and stops at arbitrary leaves; z stays unqueried. Restrictions preserve the at-most-one-common-bit class. Put both cores on the common data cube by adding dummy private coordinates to the other core. With actual reach probabilities w_v, define

    Pi=sum_v w_v Inf_i(F_v)=I(F_root)-E I(F_leaf),
    D_T=sum_v w_v D_i,
    C_T=(1/2)sum_v w_v[B_i(G_v)+B_i(H_v)].

Then

    B_T(F)=C_T+D_T,
    sum_v w_v |D_i|<=2Pi, hence |D_T|<=2Pi.             (7)

This spends the original physical influence telescope once, even when query choices depend on either core's private answers. Dummy queries preserve each inherited core telescope. C_T and terminal core spectra remain unpaid obligations.

## 5. Terminal entropy and an outer-potential reserve

Let C={empty,{s}} or {empty} if s is fixed. Define

    R=2-sum_C(g_C^2+h_C^2)
       +sum_C[phi((g_C+h_C)^2/4)+phi((g_C-h_C)^2/4)
                             -phi(g_C^2)/2-phi(h_C^2)/2].

Counting all Fourier copies gives

    H(F)=[H(G)+H(H)]/2+R,                               (8)
    E H(F_leaf)=E[H(G_leaf)+H(H_leaf)]/2+E R_leaf.        (9)

Noncommon private coefficients contribute half their entropy plus their mass; common rows contribute exactly the displayed terms. If z is then queried, its decrement is R_leaf and its expected remaining core entropy is [H(G_leaf)+H(H_leaf)]/2. Hence R>=0 by the actual selector decrement identity.

For any Boolean physical split Delta_i H=B_i+JS_i and 0<=JS_i<=(2/ln2)Inf_i. A self-contained scalar proof uses

    [(1+t)ln(1+t)+(1-t)ln(1-t)]/2<=1-sqrt(1-t^2).

The derivative of the right minus left is t/sqrt(1-t^2)-atanh(t)>=0: its derivative is (1-t^2)^(-3/2)-(1-t^2)^(-1)>=0. Applied to paired amplitudes and summed, this gives JS<=2sum min(u^2,v^2)/ln2<=2Inf_i/ln2. The entropy identity follows by cancelling the common marginal entropy.

Subtract the half-core decrements in (8). The remaining node price is D_i+JS_i(F)-[JS_i(G)+JS_i(H)]/2. Both JS terms lie in [0,(2/ln2)Inf_i(F)], since Inf_i(F) is half the core sum. Therefore, for K=2+2/ln2<5,

    |R_root-E R_leaf|<=K Pi.                            (10)

A complete data-first continuation has R_leaf=0: the wrapper becomes a constant or character. Consequently

    0<=R_root<=K I_data(F), I_data(F)=[I(G)+I(H)]/2,      (11)
    H(F)<=[H(G)+H(H)]/2+K[I(G)+I(H)]/2.                 (12)

For any partial prefix, Pi+E I_data(F_leaf)=I_data(F_root). The optional selector suffix uses only the remaining K I_data(F_leaf) reserve for its R_leaf price. Prefix and suffix thus fit one outer-potential bank. Both inherited terminal core entropies remain explicit and unpriced; (12) does not certify arbitrary cores.

## 6. Scope and the first unpaid extension

This closes the two-frequency collision for arbitrary biased sign cores, one fresh selector, one common physical data bit, disjoint private coordinates and all adaptive data prefixes. It does not cover the priority three-output shared-activation-control gate, correlated private inputs or unrestricted shared bits. With two or more common bits the conditional mean can have Fourier l1 norm greater than one, so (5) no longer follows. A nested selector hierarchy also needs ownership accounting before reusing the outer reserve.

The first unsupported universal line is a dimension-independent, source-owned retained-profile correction for multiple shared frequencies, together with paid inherited terminal core entropy. NEXT tests a two-bit common mean profile and a rare derivative using the exact comparison rows (4), not a free l1 constant.
