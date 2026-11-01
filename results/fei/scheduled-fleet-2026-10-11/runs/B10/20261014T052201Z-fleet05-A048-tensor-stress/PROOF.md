# Sparse activation, common conditional kernels, and the retained seed bill

Uniform cubes, Boolean signs and bit entropies throughout. Controller trees may stop at actual nonconstant terminal functions. Every physical influence and terminal reference cost below is retained.

## 1. Exact activation criterion

Partition the seed coordinates into retained U and spectator Z. Let A(C) be a nonconstant Boolean INDICATOR on disjoint controller coordinates, 0<Pr(A=1)<1, and define F=1+A(g(U,Z)-1). Resolve A by any complete physical controller prefix, stopping at g or +1. There is one hereditary conditional spectral kernel k(s_Z|s_U), independent of controller frequencies and their history, if and only if

    ghat(empty_U,s_Z)=0 for every nonempty s_Z,

equivalently E_U g(U,Z) is a constant as a physical function of Z.

Sufficiency: for s_U nonempty every coefficient is Ahat(s_C) ghat(s_U,s_Z), so conditional Z laws do not depend on s_C or the restricted controller. For s_U empty the hypothesis leaves only s_Z empty, even in the interfering constant/activation row. Set k(.|empty_U) to the empty point mass; at a zero-mass nonempty U row choose any normalized law. Every restriction of A has the same factorization. Necessity: the inactive terminal +1 requires the empty-U kernel to be the empty-Z point mass. The active terminal g has that same kernel; hence it has no pure-Z nonempty coefficient. This argument needs the stated active and inactive terminals; a degenerate controller does not establish necessity.

Let mu=E g and beta=Var_Z(E_U g)=sum_{s_Z!=empty} ghat(empty_U,s_Z)^2. For disjoint T-fold tensor copies with copied partitions, beta_T=(mu^2+beta)^T-mu^(2T). Thus beta>0 remains strictly positive under every finite tensor power. A balanced independent factor placed in retained U instead makes E_U g identically zero. That is a real physical factor, not a dummy; its influence must be counted.

## 2. Guarded arbitrary seed: Boolean quotient and exact terminal capacity

For ANY Boolean seed g on n bits, T>=1 and m>=1, set h=g^tensor T on disjoint seed blocks Z, add a fresh fair retained sign x, put t=2^-m and

    F_{m,T,g}=1+AND_m(C)*(x*h(Z)-1).

All controller queries in the short-circuit prefix are essential, because their active output is balanced. Its physical quotient is the fixed (m+1)-bit Boolean function

    F0_m=1+AND_m(C)*(x-1).

The conditional spectator kernel is

    k(.|s_x=empty)=point mass at empty_Z,
    k(.|s_x={x})=P_h.

This is precisely A050's hereditary conditional-k class. It is usually NOT an independent spectator kernel, and the arbitrary seed does not become a Boolean constant in the full account. Expanding the Fourier coefficients proves

    H(F)=H(F0_m)+t*T*H(g),
    I(F)=t*(m+1+T*I(g)),
    R_removed(controller prefix)=m*t,
    E H(F_leaf)=t*T*H(g),
    E I(F_leaf)=t*(1+T*I(g)).

Every relevant seed coordinate has influence t times its old influence; the guard has influence t; every root controller has influence t. The inactive terminal is +1, and the active terminal is x*h. Therefore none of the seed or guard costs can be charged away as a controller terminal constant. Tensor multiplication contributes exactly t*T*H(g), without a T log T entropy term.

The quotient law has empty mass (1-t)^2 and 2^(m+1)-1 other masses t^2. Hence exactly

    H0_m=-2(1-t)^2 log2(1-t)+2m(2t-t^2).

Using -ln(1-t)<=t/(1-t),

    H0_m<=4mt+(2/ln2)t(1-t)<7mt,

where ln2>2/3 by its positive atanh series. This prices the entire actual controller prefix at a finite fixed coefficient, while keeping the arbitrary seed terminal entropy. It is a scoped price, not full FEI.

## 3. ONE normalized reference, including nonmatching seed KL

Let Q_g be any normalized seed reference dominating P_g, and use Q_h=Q_g^tensor T. At the root choose quotient reference P_F0_m itself, and lift it by the kernel

    k_Q(.|empty_x)=empty point mass,
    k_Q(.|{x})=Q_h.

Its full normalization is immediate by conditional summation. Its cross-entropy and source KL are

    CE(P_F,Q_F)=H0_m+t*T*CE(P_g,Q_g),
    KL(P_F||Q_F)=t*T*KL(P_g||Q_g).

The true kernel P_h and the reference kernel Q_h may differ. Their nonzero conditional KL is kept explicitly, not silently omitted contrary to A050's matching hypothesis. Controller coherent branches depend only on (controller frequencies,x frequency). The same reveal kernel therefore transports Q_F with physical branch predictions and quotient-actual Bayes references. All controller conditional-erasure KL and outcome KL are zero; no chosen-child reset is performed. The seed KL is retained completely at the active terminal and zero at inactive terminals:

    KL_root=E KL_terminal=t*T*KL(P_g||Q_g).

At root and every prefix, the seed entropy/cross-entropy is the current activation probability times its full original bill. It is a martingale, not an available bank for repeated controller withdrawals. If Q_g=P_g, the full kernel matches A050 exactly and this source KL is zero, but the seed terminal entropy is STILL t*T*H(g). More generally this is an explicit nonmatching conditional reference whose full bill is conserved, not a universal price for arbitrary conditional resets.

## 4. The admitted class is same-constant FEI-complete

If H(F)<=C I(F) for every guarded activation above, fix m,g and let T grow. The exact identities imply

    H0_m+t*T*H(g)<=C*t*(m+1+T*I(g)).

Divide by t*T and let T->infinity to obtain H(g)<=C I(g). Constants satisfy it trivially. Conversely full FEI(C) implies its subset bound. Thus the optimal constant over this hereditary-k class is exactly the full uniform FEI optimum (possibly infinite). The same conclusion holds for the subclass with minority probability and total influence tending to zero: choose m(T)=ceil(2 log2(T+1)), so t is between 1/[2(T+1)^2] and 1/(T+1)^2. Then I(F)->0, Pr(F=-1)=t/2->0, and, for I(g)>0, H(F)/I(F)->H(g)/I(g). All dimensions and limits are analytic, not automatically enlarged computational jobs.

This specializes existing balancing/activation/tensor admission ledgers, including A002's baseline. The new use is a source-exact boundary of A050's common-k repair: even with a genuine simple Boolean quotient, exact matching kernels and a paid controller prefix, its admitted class retains the entire arbitrary-seed FEI target in the active terminal. It is not an isolated class closure or a new proof of FEI.

## 5. First spectator-data query reinstates the seed decrement

Query one physical seed coordinate z_i, leaving controls and guard unqueried. Each child is another guarded activation of the actual child seed, so both quotient laws are STILL P_F0_m. Therefore

    D_{z_i}H(F)=t*D_iH(g), Inf_{z_i}(F)=t*Inf_i(g)

(for one selected tensor copy). The conditional spectator entropy drift is the whole seed decrement; no quotient charge absorbs it. This query is INSIDE spectator block Z, outside A050's paid outside-Z drift lemma.

Finite exact boundary: take m=T=1 and g the two-bit AND-sign, whose H(g)=2, queried influence=1/2 and both children have Fourier entropy zero. F has four coordinates, H(F)=3, both physical child entropies 2, queried influence 1/4, and conditional spectator drift 1. The quotient entropy drift is zero. Since (2/ln2)*(1/4)<3/4<1, the outside-Z drift allowance cannot be extended unchanged to this spectator query. No source claim does that. Both nonconstant child quotient functions, all terminal influence and any remaining seed reference KL remain actual costs.

## 6. Independent reconstruction of A050 v1 at its stated scope

For source/reference laws with identical k(z|u), the KL chain rule gives full KL equal to quotient KL and full CE equal to quotient CE plus L=E H(k). Summation normalizes each lifted reference. At a controller query, k cancels in the actual reveal kernel; a z-independent normalized fallback covers source-zero/reference-positive rows. The quotient and full branch predictions/Bayes references agree after lifting, so conditional-erasure, outcome and signed reset terms agree. The quotient U marginal is a martingale, hence L_root=E L_leaf. This proves the complete signed prefix telescope with terminals, not just a root factorization.

For a query i outside Z, write T for all other quotient frequencies. Exact entropy splitting gives M_full-M_quot=-I(S_i;S_Z|T), J_full-J_quot=I(B;S_Z|T), so DeltaL is their difference. Its positive part is at most J_full<=2Inf_i/ln2 by the scalar amplitude/channel inequality reconstructed in our stage 3 proof. If p/q=r(T) on all rows, erasure keeps that ratio and the same-kernel Bayes child ratio is r(T) times its branch normalization, independent of Z. Thus child conditional spectator laws match; all quotient, signed reset and terminal obligations remain. The source example h3 has DeltaL=1-(3/8)log2(3)>0, proved by 3^3<2^8. These facts reconstruct the entire original claim unchanged; our spectator-query boundary and admitted-class hardness do not repair or refute it.

## First unsupported universal line

The arbitrary active seed's full terminal entropy/reference cost, or its first selected spectator-query erasure, is paid by genuinely unused child slack through the SAME normalized reference and one physical influence budget. Tensor powers and sparse activation show that omitting this line loses the full FEI target at the same constant, even though controller kernel transport is exact and locally paid. Next work must name a noncircular source of that terminal/seed debit; proving another controller-only kernel identity cannot replace it.
