# Final reference after fully exposed cancellation

Boolean signs, finite uniform cubes, physical influence, entropy and cross entropy in bits. Let c,u be two coordinates, Z a disjoint nonempty m-bit block, Y any nonempty core block. Let four arbitrary Boolean signs h_cu(Y) define G(c,u,Y). Fix c*,u*,z*. Let q1=1-2*1{c=c*,u=u*}, q2=1-2*1{c=c*,Z=z*}, source g=q1 G and sequential edit mask q=q1 q2. Then the ACTUAL final output is F=gq=q2 G. The source fully sees the first private coordinate u. We also allow the output-only degenerate case q2=1.

Fix ONE positive normalized core reference R_Y on every subset of Y before sampling. Write C_R(h)=sum_T hhat(T)^2 log2(1/R_Y(T)) and B=(1/4)sum_cu C_R(h_cu). No source or final terminal entropy is omitted. We prove a complete normalized final reference with

    H(F)<=C_Q(F)<=B+2 I_Y(F)+4 I_{c,u}(F)
                    +(4+log2(20/7)) I_Z(F).              (1)

Since log2(20/7)<8/5, the last coefficient is <28/5. If EACH core has C_R(h_cu)<=K I(h_cu), then

    H(F)<=max(K+2,4+log2(20/7)) I(F).                    (2)

This is a conditional common-reference transfer, not a universal source or core reference construction. It does not bound the canceled ancestral influence sum.

## 1. Exact preservation of the inherited core reference

For fixed c,u,Z, F_Y is a scalar sign times h_cu. Thus partial Parseval gives

    P_F(S_Y=T)=(1/4)sum_cu hhat_cu(T)^2=P_g(S_Y=T),
    I_Y(F)=(1/4)sum_cu I(h_cu).                          (3)

Hence B is EXACTLY the average cross entropy of all actual final Y terminals, and also the original source terminal cost under the SAME R_Y. Both core-marginal entropy and D(P_Y||R_Y) are unchanged; there is no renewed child bank or reference reset. Nonconstant unequal branch amplitudes are allowed.

## 2. Five cells covering all control subsets

On the control coordinates D={c,u} union Z partition every nonempty Fourier subset into three singleton cells {c},{u},{c,u}, and two tail cells

    A_j={S: S_Z nonempty, 1{u in S}=j, c arbitrary}, j=0,1.

Each tail has N_m=2(2^m-1) atoms. These five cells include all 2^(m+2)-1 nonempty subsets, including unoccupied ones. On a row T of core frequency, subsets in any singleton cell trivially have constant square. For S_Z nonempty, writing rho=2^-m, expansion F=G-2*1{c=c*}*1{Z=z*}*G gives

    Fhat(S_c,S_u,S_Z,T)
      =-rho chi_(S_c)(c*) chi_(S_Z)(z*)
            [G(c*,u,Y)]hat(S_u,T).                      (4)

Thus row squared amplitudes are uniform on each A_j. Source phase signs and unequal core amplitudes do not affect this flatness. The same is true when q2=1 because the tails vanish. Cell choice never depends on T.

## 3. Normalized label weights and complete output law

Assign cell weights w_c=w_u=1/4, w_cu=1/16, w_0=7/20, w_1=7/80; they sum to one. Set R_tail(S)=w_cell/|cell|. For alpha=P_F(S_D nonempty), define

    R_D(empty)=1-alpha, R_D(S nonempty)=alpha R_tail(S),
    Q(T,S)=R_Y(T) R_D(S).                               (5)

This ONE normalized law covers the entire actual final spectrum. At alpha=0 or1 it remains normalized and covers all positive output atoms; the opposite zero-mass flag is omitted by continuity, never conditioned away from a positive output row. For 0<alpha<1 the whole law has positive mass on every atom. Q is chosen from the final output only through alpha; its core factor is the inherited R_Y. Gibbs gives H(F)<=C_Q(F).

For a uniform A_j, E|S|=1/2+j+m 2^(m-1)/(2^m-1). Consequently

    log2 |A_j|<=2 E|S|-2j.                              (6)

Indeed log2 |A_j|=1+log2(2^m-1)<=1+m and twice the mean Z degree is m/(1-2^-m)>=m. Tail label log-costs are log2(20/7)+2j. Their sum with (6) is at most 2E|S|+log2(20/7). Singleton costs are respectively2,2,4, exactly twice degree. Since the row is flat on each cell, summing ONCE over all rows yields

    E[-log2 R_tail(S_D); S_D nonempty]
      <=2 I_D(F)+log2(20/7) P_F(S_Z nonempty)
      <=2 I_D(F)+log2(20/7) I_Z(F).                     (7)

The core contribution is B by (3), and the empty/nonempty flag costs exactly h2(alpha). Therefore

    C_Q(F)<=B+h2(alpha)+2 I_D+log2(20/7) I_Z.            (8)

This is full reference cross entropy, not merely a conditional erasure fragment. No extra channel is charged: the supplied COMMON R_Y already retains its actual mixture/reference cost in B. Individual separate entropy certificates H(h)<=KI(h) do NOT imply admission to this common R_Y.

## 4. Boolean flag payment, reproduced from the reviewed A067 lemma

For any Boolean F, alpha<=Var(F)=v<=I(F). If v>=1/2, h2(alpha)<=1<=2I. If v<1/2, let minority density p<=1/2, so v=4p(1-p) and p<1/4. The scalar inequalities h2(t)<=t log2(e/t), monotonicity of t log2(e/t) for t<=1, and e<4 give

    h2(alpha)<=h2(v)<=4p log2(e/(4p))
                    <=4p log2(1/p)<=2I(F).              (9)

The last step is Boolean cube isoperimetry I(F)>=2p log2(1/p). For completeness split a set into child densities p0,p1. Its crossing influence is at least |p0-p1|. The difference of target2p log2(1/p) from average child targets is2p[1-h2(t)] for t=p0/(p0+p1), at most2p|2t-1|=|p0-p1| by concavity h2(t)>=2min(t,1-t). Induction starts at dimension zero. Constants have zero flag cost. This is one global flag payment, not a reusable child surplus.

Combine (8) with (9) to prove (1). Equation(3) and the common-reference core hypothesis give (2). The strict rational coefficient bound follows from 20^5<2^8*7^5.

## 5. Concrete nonfactorizing and canceled-event scopes

For Y three bits take the fixed tree (y0,(y1,y2)), code lengths L(empty)=1, L({y0})=3, all other nonempty lengths5, Kraft sum13/16. Its normalized reference R_Y(T)=2^-L(T)/(13/16) has C_R(h)<=Gamma_Y(h). Choose h00=Maj3, h01=y0, h10=-y0, h11=-Maj3. The respective Gamma/I ratios are3,3,3,3; all four actual terminals have K=3 under ONE R_Y. They are unequal and not all scalar multiples of one core. Thus every m>=1 and every fixed event assignment has H(F)<(28/5)I(F). This is a derived example, not a novelty claim against known small-selector FEI classes.

A070's exposed unequal-width obstruction has all four h_cu equal to a nonconstant point sign on Y. It is included with the inherited R_Y retained. The divergent bill 7I(g)+12I(q) is NEVER assumed paid by final influence; only the new actual output reference is charged. The older complete-cancellation output F=y is the allowed q2=1, G=y case: alpha=0 and B=C_R(y), so no positive control bill survives. This reconstructs the final-reference target on that output without asserting a positive ancestral signed-conversion bank.

## 6. One actual core query with the same inherited reference

Query i in Y physically, giving F_+,F_- in the SAME output family with restricted cores. Carry the inherited reference by marginalizing its frequency bit: R'_Y(U)=R_Y(U)+R_Y(U+i). The same R'_Y serves all four cores and both physical children. Let alpha_+,alpha_- be actual child control tail probabilities. Partial Parseval gives alpha=(alpha_++alpha_-)/2 and makes the parent's control marginal the average child control marginals. Tail-label/cardinality charges therefore average exactly, while updating only the final empty/nonempty prior refunds its actual binary Jensen-Shannon term. Denote the full reference cost in(5) by C_Q; then

    C_Q(F)-(C_(Q_+)(F_+)+C_(Q_-)(F_-))/2
      =sum_T P_F(S_Y=T) log2(R'_Y(T minus i)/R_Y(T))
         +h2(alpha)-(h2(alpha_+)+h2(alpha_-))/2.           (10)

Both terms are nonnegative; (10) is an EXACT identity, including constants and zero-tail children by continuity. It preserves all actual restricted terminal bills, source/core marginal debt and the same five-cell label law. Neither term is a newly available child slack: this is the actual complete-reference decrement. For every K the physical ledger is

    K I(F)-C_Q(F)
      =E_child[K I(F_child)-C_(Q_child)(F_child)]
          +K Inf_i(F)-Delta C_Q.                        (11)

Influence restriction satisfies I(F)=Inf_i(F)+E I(child). Thus any query-price deduction still requires the exact signed term K Inf_i-Delta C_Q together with unused child slack; nonnegativity of the decrement alone does not pay it. We do not assert Delta C_Q<=K Inf_i.

## 7. Exact unsupported universal line

The scoped result is proved. Universal FEI would require a common core reference with a sufficiently unused certified surplus to pay the retained2I_Y reserve, or a signed refund reducing that reserve while preserving the SAME R_Y under further actual core queries. Separately paid unrelated references for four cores cannot be substituted for R_Y. Arbitrary source dependence on Z destroys five-cell row flatness. The exact cancellation normal form is not an algorithm finding such a factorization for arbitrary Boolean functions. No same-constant recursion, C019 physical ownership or general private-source payment is established.
