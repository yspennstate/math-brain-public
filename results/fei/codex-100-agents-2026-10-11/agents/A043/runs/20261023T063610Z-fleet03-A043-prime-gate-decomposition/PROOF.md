# Freeze the paid sector before normalizing the unpaid scale charge

All logarithms and cross entropies are natural. This is an author reconstruction and refinement of A044's complete dyadic reference, not a payment of the universal scale charge or a proof of FEI. It consumes the new B09 dependency rather than continuing isolated prime56067 collars.

## Definitions and complete reference

Let f:{0,1}^n->{-1,1} be Boolean at a finite independent interior product law. Contract deterministic coordinates first. Write v_i=4p_i(1-p_i), v_A=product v_i, c_A=hat f(A)/sqrt(v_A), P_A=hat f(A)^2 for nonempty A. Actual physical mixed derivatives give |c_A|<=1. Put

    w=Var(f), Delta=I-Var(f),
    R=sum_{|A|>=3}(|A|-2)P_A,
    M=sum_{|A|>=2}P_A=Delta-R,
    E=sum_{A nonempty}P_A ln(1/c_A^2).

Zero-mass terms are omitted. For occupied A let j_A be the unique integer >=0 with 1/2<2^j_A|c_A|<=1, assigning exact dyadic boundaries to the upper mantissa 1. Let W_A=v_A 4^-j_A. Then P_A<=W_A<4P_A. Define

    J_hi=ln4 sum_{|A|>=2}P_A j_A,
    Z_hi=sum_{|A|>=2}W_A,
    n_hi=M ln(Z_hi/M)  if M>0, and 0 otherwise.

The new complete reference Q_* is defined on ALL Fourier labels:

    Q_*(empty)=P_empty,
    Q_*({i})=P_{i},
    Q_*(A)=M W_A/Z_hi       for |A|>=2, if M>0.

All unoccupied labels have zero reference mass. If M=0 put Q_*=P. This is one probability distribution with every occupied label admitted. It is an auxiliary reference, not a conditioned Boolean spectrum. Its construction retains the actual singleton terminal law as well as the empty atom and the full high-degree terminal law.

Write E_1 for the singleton part of E. Direct substitution gives

    K_*=KL(P||Q_*)=M KL(P_hi/M || W_hi/Z_hi),
    E=E_1+J_hi+n_hi-K_*,                                    (1)
    0<=n_hi<=(ln4)M=(ln4)(Delta-R).                          (2)

At M>0 the upper inequality is strict, but the weak form includes M=0. Indeed Z_hi<4M, so (2) follows by monotonicity of ln. Also E_hi-J_hi>=0, hence 0<=K_*<=n_hi. No positive off-support atom has been discarded. For FULL ordinary cross entropy, add the SAME physical-bias term sum_nonempty P_A ln(1/v_A) and empty term P_empty ln(1/P_empty) to the corrected cross entropy E_1+J_hi+n_hi. The correction is the same for every reference comparison below.

## Paid singleton sector and the exact remaining scale obligation

Let D_i=(f|i=1-f|i=0)/2, d_i=E D_i^2, t_i=|E D_i|. Booleanity gives d_i>=t_i. The scalar ln r<=r-1 gives h(t)=2t^2 ln(1/t)<=2t(1-t). Actual Parseval gives

    sum_i v_i(d_i-t_i^2)=2Delta-R.

Therefore the actual singleton reserve is

    S=4Delta-2R-E_1
     =sum_i v_i[2(d_i-t_i)+2t_i(1-t_i)-h(t_i)]>=0.          (3)

This is the SAME reserve used in earlier A043 stages and A044's proof. It is not newly available after some other debit. Define the exact high-degree mantissa refund

    U=sum_{|A|>=2}P_A ln(4u_A^2)>=0,
    u_A=2^j_A|c_A| in (1/2,1].

Since E_hi-J_hi=(ln4)M-U, one has the exact identity

    E=J_hi+(4+ln4)Delta-(2+ln4)R-S-U.                      (4)

Thus the universally unpaid scale is J_hi, not the singleton dyadic charge. In particular

    E<=J_hi+(4+ln4)Delta-(2+ln4)R.                         (5)

For the candidate sharp constant 4+ln4, (4) says that the exact remaining inequality is

    J_hi <= (2+ln4)R+S+U.                                 (6)

No proof of (6) for arbitrary primes is supplied. The nonnegative refund U and original S must not be deleted and then silently reused. The sector transfer below accounts for them inside the same complete reference.

## Exact comparison with A044's complete flat reference

Let A=w-M be the total singleton mass, Z_1=sum_singletons W_i, Z=Z_1+Z_hi. A044's reference Q_flat has empty mass P_empty and nonempty mass w W_A/Z. Its ordinary KL is K_flat, and its corrected cross entropy is

    C_flat^+=J_all+w ln(Z/w),
    J_all=J_1+J_hi.

For 0<A<w let R_1=P_single/A and V_1=W_single/Z_1. The complete KL chain rule on the partition {empty, singleton, high} gives

    K_flat-K_* = A KL(R_1||V_1)
                  +w d_Bern(A/w || Z_1/Z)>=0.              (7)

Both full terminal laws are retained. To see (7), first condition on nonempty (total mass w); then condition on the singleton/high sector. The within-high term is precisely K_*; the within-singleton term and Bernoulli sector term are the two terms displayed. The empty term is zero because both references agree with P there.

The SAME difference is the complete corrected cross-entropy transfer:

    C_flat^+ - C_*^+ = K_flat-K_* >=0,
    C_*^+=E_1+J_hi+n_hi.                                  (8)

Equivalently w ln(Z/w)-n_hi-(E_1-J_1) equals the right side of (7). This exact signed identity prevents counting a decrease of the old normalizer as a second reserve: replacing the singleton scale term by actual E_1 consumes the corresponding old mantissa payment.

If A=0, Q_flat=Q_* and every term of (7) is zero; do not use a conditional singleton law. If M=0, Q_*=P, and (7) becomes w KL(P_single/w || W_single/Z_1), with sector term zero; if w=0 all laws are point mass at empty. These cases cover zero deficit and literals without undefined ratios.

The refinement is STRICT for fair-variable AND2 at probabilities p1=p2=3/4: its high sector is one atom, so Q_*=P and K_*=0, whereas singleton and pair rounding factors differ and Q_flat!=P. Gibbs' inequality then gives K_flat>0. This is an actual Boolean control, not a formal distribution violating admission.

## Genuine disjoint composition and the precise prime implication

After removing dummy coordinates, an essential gate on k>=2 coordinates is PRIME here if there is no block B with 2<=|B|<=k-1 and Boolean signs h,G such that f=G(h(x_B),x_not_B). Equivalently, no such block has exactly two distinct cofactor rows indexed by x_B (rows are functions of x_not_B). A factorization gives two rows; conversely two rows define h by their labels and G by the two row functions. One row would contradict essentiality of B. Essential binary gates are therefore prime; unary signs are literal leaves. Repeatedly factor a nonprime proper block. Each resulting gate has fewer essential inputs, so induction on arity terminates in a genuine read-once decomposition with disjoint physical leaves. No uniqueness of that decomposition is needed. The prime premise below quantifies over ALL arities and ALL induced product laws, not a census through four variables.

Consider F=g(f_1,...,f_m) on disjoint physical blocks. Evaluate g at the ACTUAL induced independent child-output law and contract constant children. Set w_i=Var(f_i)>0 and a_i=I_i(g)/w_i. For any occupied final label S, let A be its occupied-block set and T_i its nonempty child labels. The physical law factors uniquely:

    P_F(S)=P_g(A) product_{i in A}[P_i(T_i)/w_i].

Use each gate's complete reference Q_* and recursively define

    Q_tree(empty)=P_g(empty),
    Q_tree(S)=Q_*,g(A) product_{i in A}[Q_tree,i(T_i)/w_i].

The reference is normalized because each conditional child reference has nonempty mass one. It retains every original terminal label, and is positive on every occupied label. Likelihood ratios multiply on this unique disjoint representation, proving

    KL(P_F||Q_tree)=KL(P_g||Q_*,g)+sum_i a_i KL(P_i||Q_tree,i).

The corrected cross entropy decomposes with the same weights: this follows either pointwise, using v^g_A=product_i w_i at the induced law, or by adding the exact corrected entropy composition identity to the just-proved KL identity. For a finite read-once prime decomposition with literal leaves, recursively set omega_root=1, omega_child=omega_parent a_child. Then

    C_tree^+=sum_v omega_v(E_1(g_v)+J_hi(g_v)+n_hi(g_v)),
    Delta(F)=sum_v omega_v Delta(g_v),
    C_tree^+<=sum_v omega_v[J_hi(g_v)+(4+ln4)Delta(g_v)
                                      -(2+ln4)R(g_v)].     (9)

No additivity of R is asserted: its weighted gate sum remains explicit. There is no depth surcharge and no fresh source bank. If every genuine disjoint-composition prime satisfies J_hi(g)<=K Delta(g) at every interior induced product law, with a SINGLE finite K independent of arity and law, then

    E(F)<=C_tree^+<=(K+4+ln4)Delta(F).                     (10)

Conversely, a universal corrected entropy bound E<=C Delta implies J_hi<=C Delta, since each corrected entropy term is nonnegative and j_A ln4<=ln(1/c_A^2). Thus the all-prime high-degree-scale theorem is equivalent, up to the displayed additive constant, to universal product-biased corrected FEI+. It yields ordinary uniform FEI with bit constant max(K+4+ln4,1)/ln2, because the omitted empty entropy is at most Var(f) in natural units. This is a localization/equivalence, not a solution or an easier independently established premise.

## Failure controls and first unsupported line

For an actual bent tensor whose occupied normalized coefficients are dyadic, W=P. Then Q_*=P, n_hi=K_*=0, and E_hi=J_hi. Normalization and KL cannot pay that scale charge. Such tensors do not disprove FEI; they show which term still needs a mathematical estimate.

Booleanity is used exactly in (3). At the real-valued one-bit fair input f=(4+3(2x-1))/5, P_empty=16/25, P_1=9/25 and Delta=R=M=J_hi=0, while E_1=(9/25)ln(25/9)>0. It contradicts (5) if Boolean admission is dropped, even though Q_*=P is well-defined. The helper explicitly verifies this excluded control.

The first unsupported universal line remains a dimension-independent upper bound on the ACTUAL J_hi at all prime gates, funded by the unused original deficit, or the stronger exact (6). All reference identities and their composition are proved above, but none imply that bound. This stage repairs the reference/ownership interface and independently reconstructs the consumed portion of A044's proof; it leaves full FEI OPEN and awaits independent review of the refinement.
