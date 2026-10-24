# Restricted replacement for the unpaid overlap price

Entropy is in bits. Let G(S,X), H(S,Y) be Boolean signs on a uniform cube, with disjoint private blocks X,Y and an arbitrary finite shared block S. A fresh uniform selector z gives F=(G+H)/2+z(G-H)/2. Assume the following hereditary condition: after every physical data restriction, each conditional private mean E_X G(S,X), E_Y H(S,Y) has Fourier l1 norm at most one on the remaining S. This condition is an explicit hypothesis, not a consequence of Booleanity.

The condition has an exact structural characterization: for every fixed private assignment x, G(S,x) is a signed shared character, and likewise for H(S,y). Thus the class is precisely

    G(S,X)=epsilon(X) chi_{A(X)}(S),
    H(S,Y)=eta(Y) chi_{B(Y)}(S),

where epsilon,eta are arbitrary Boolean signs and A,B arbitrary subset-valued private maps. Shared parities may depend nonlinearly on private inputs and may range over all shared frequencies. Sufficiency: every restricted conditional mean is a convex combination of restricted signed characters, so its Fourier l1 norm is at most one. Necessity: fix all private coordinates. The remaining Boolean shared slice has squared Fourier norm one by Parseval. Its l1 norm at most one forces exactly one nonzero coefficient, of magnitude one, hence a signed character. This also proves restriction stability. The previously considered product-character cores are a proper subclass.

At every data query define D_i=B_i(F)-(B_i(G)+B_i(H))/2, where B_i is the paired squared-amplitude erasure. Then |D_i|<=4 Inf_i(F); private queries have the stronger bound 2 Inf_i(F). These prices spend the actual physical influence once. For K=4+2/ln(2)<7 and every finite adaptive data prefix,

    |R_root-E R_leaf| <= K [I(F_root)-E I(F_leaf)].

Here R is the exact collision potential defined below. In particular 0<=R<=K I_data(F), and

    H(F) <= (H(G)+H(H))/2 + K (I(G)+I(H))/2.

This retains both core entropies, rather than pricing them by a second outer allowance. It does not prove FEI for arbitrary cores or arbitrary overlapping profiles.

Prior-result boundary: A097 stage 3 DERIVATION.md sections 3-4 already supplies a root complete-reference transfer under l1<=1 admission, priced against the selector influence, with coefficient 2+4/ln2. No new root FEI closure is claimed here. The additional conclusions are the structural characterization of hereditary admission and signed transport through every adaptive data prefix with its remaining data reserve and terminal potential. The two prices have different owners and must not both be recharged in a hierarchy.

## Exact collision ledger

Let C range over subsets of the unfixed S, and g_C,h_C be the coefficients on these common frequencies, with no private coordinates. All other frequencies occur in only one core and are copied twice at half amplitude. Direct coefficient counting gives

    H(F)=(H(G)+H(H))/2+R,
    R=2-sum_C(g_C^2+h_C^2)
      +sum_C[phi((g_C+h_C)^2/4)+phi((g_C-h_C)^2/4)
                  -(phi(g_C^2)+phi(h_C^2))/2].

This includes coherent sums and differences explicitly; it is not a disjoint-block chain rule. Querying z shows R=Delta_z H(F)=B_z(F)+JS_z(F)>=0. Common coordinates in the two cores are the same physical coordinates.

## Private rows

At a private X query let u_C=g_C, d_C=ghat(C union {i}), v_C=h_C. The collision correction is

    D_i=sum_C {[Phi((u_C+v_C)^2,d_C^2)
                       +Phi((u_C-v_C)^2,d_C^2)]/4
                        -Phi(u_C^2,d_C^2)/2}.

For each row the symmetric-shift inequality, independently reconstructed below, places the summand in [-Phi(u_C^2,d_C^2)/2, Phi(v_C^2,d_C^2)/2]. The envelope Phi(a^2,b^2)<=2|ab| and |d_C|<=Inf_i(G) therefore give |D_i|<=Inf_i(G), since both mean profiles have l1 norm at most one. Actual Inf_i(F)=Inf_i(G)/2. Private Y is identical with the roles exchanged.

## Shared physical rows

At a shared query i, C now ranges over subsets of S minus {i}. Set mu_C=ghat(C), a_C=ghat(C union {i}), nu_C=hhat(C), b_C=hhat(C union {i}). Exactly

    D_i=P-N,
    P=sum_C[Phi((mu_C+nu_C)^2,(a_C+b_C)^2)
                   +Phi((mu_C-nu_C)^2,(a_C-b_C)^2)]/4,
    N=sum_C[Phi(mu_C^2,a_C^2)+Phi(nu_C^2,b_C^2)]/2.

P,N are nonnegative. Each P row is at most
(|mu_C|+|nu_C|)(|a_C|+|b_C|), using the envelope and the triangle inequality. Every |a_C|<=Inf_i(G), |b_C|<=Inf_i(H): these are Fourier coefficients of the physical half-difference, which takes values in {-1,0,1}. Hereditary profile admissibility gives sum_C|mu_C|<=1, sum_C|nu_C|<=1. Hence P<=2(Inf_i(G)+Inf_i(H)). Similarly N<=Inf_i(G)+Inf_i(H). Since |P-N|<=max(P,N), |D_i|<=2(Inf_i(G)+Inf_i(H))=4 Inf_i(F). No independence between G and H is used for this influence equality: it follows by conditioning on the fresh selector.

## Scalar and physical transport reconstruction

In natural units Phi(u^2,d^2)=integral_0^(d^2) ln(1+u^2/t)dt. The symmetric difference has integrand one quarter of ln A, where
A=((u+v)^2+t)((u-v)^2+t)/(u^2+t)^2 <=(1+v^2/t)^2.
Integrating gives the asserted upper comparison; nonnegativity gives the lower comparison. For the envelope, by homogeneity and symmetry it suffices to show Phi_nat(1,t^2)/(2t)<=ln2 for 0<t<=1. Its derivative has the sign of (t^2-1)ln(1+t^2)-t^2 ln(t^2). This is nonnegative: ln(1+t^2)<=t^2 and -ln(t^2)>=1-t^2 bound the numerator below by zero. The ratio therefore attains its maximum ln2 at t=1. Endpoints follow by continuity.

For a physical split Delta_i H=B_i+JS_i, with 0<=JS_i<=(2/ln2)Inf_i. One proof uses [(1+t)ln(1+t)+(1-t)ln(1-t)]/2<=1-sqrt(1-t^2); the derivative difference is nonnegative since its derivative is (1-t^2)^(-3/2)-(1-t^2)^(-1)>=0. Summing the paired amplitude comparisons gives the displayed JS bound.

Subtracting the two inherited core decrements from the exact R ledger gives
Delta_i R=D_i+JS_i(F)-(JS_i(G)+JS_i(H))/2.
The two nonnegative JS quantities each lie in [0,(2/ln2)Inf_i(F)]. Thus |Delta_i R|<=K Inf_i(F). The finite physical influence telescope yields the prefix bound even for adaptive queries. A complete data continuation leaves constant cores, hence a constant or character wrapper and R_leaf=0. It spends I_data(F)=(I(G)+I(H))/2. At an arbitrary stop, an optional selector query spends R_leaf from the remaining K I_data(F_leaf) reserve. The original inherited terminal entropies remain exactly (H(G_leaf)+H(H_leaf))/2.

## Honest boundary

The first unsupported line for unrestricted overlap is a dimension-independent replacement for the hereditary mean-profile l1 bound. It is false that Booleanity supplies l1<=1: on two shared bits a quadratic bent sign has four coefficients of magnitude 1/2, so l1=2. This is a failure of this sufficient hypothesis, not a counterexample to the desired price or FEI. Shared-controller priority selectors and arbitrary interleaved controller queries are also outside this theorem. The constant 4 is not claimed sharp.
