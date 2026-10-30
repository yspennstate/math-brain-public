# Independent closing review: sharp joint singleton source

Reviewed source: A041, runs/20261023T135351Z-fleet03-A041-weighted-threshold-fei/PROOF.md, sections2-3. Verdict: HOLDS at the stated Boolean/product/disjoint scope, without repair. This is a review, not a new proof of FEI or a new unrestricted scale-payment claim. Completion occurs after the campaign deadline because the final source reads/wake were delayed; no result is represented as independently reviewed before14:49 UTC.

All logarithms are natural. For a finite Boolean sign h under independent interior probabilities p_i, set v_i=4p_i(1-p_i). Let D_i=(h|i=1-h|i=0)/2, d_i=E D_i^2 and t_i=|E D_i|. Booleanity gives d_i>=t_i. An occupied singleton has dyadic scale j_i>=0 and mantissa u_i=2^j_i t_i in (1/2,1]; dyadic endpoints have u=1. Put

    J_1=ln4 sum_i v_i t_i^2 j_i,
    L_1=2sum_i v_i t_i^2 ln(1/u_i),
    P_source=2Delta-R=sum_i v_i(d_i-t_i^2).

Zero coefficients contribute zero. Deterministic coordinates are contracted. The source's claimed theorem is, for EVERY real alpha>=0,

    J_1+alpha L_1 <= max(ln4,2alpha) P_source.             (1)

## Independent scalar reconstruction

It is enough to establish

    t[j+ln(1/u)]<=1-t,       t=2^-j u.                   (2)

Define F_j(u)=u(j+1-ln u) for u in (1/2,1]. Its derivative is j-ln u>=0. Hence F_j(u)<=F_j(1)=j+1. For j=0 this is1=2^j; for j>=1, j+1<=2^j by induction. Thus F_j(u)<=2^j. Multiplying by 2^-j and rearranging gives (2). This proof handles every dyadic cell including u=1; no continuity of the discontinuous scale j across a cell boundary is assumed.

Multiply (2) by v_i t_i, sum, and use t_i(1-t_i)<=d_i-t_i^2. One obtains the critical joint budget

    J_1/ln4+L_1/2 <= P_source.                            (3)

For alpha<=ln2, monotonicity in alpha gives J_1+alpha L_1<=ln4 P_source. For alpha>=ln2, multiply (3) by2alpha and use (2alpha/ln4)J_1>=J_1. This proves (1), including alpha=0 and the critical alpha=ln2.

The exact Parseval identity for P_source follows by expanding D_i: v_i Var(D_i)=sum_{A containing i, |A|>=2}P(A). Counting each packet |A| times gives sum_i v_i Var(D_i)=2Delta-R. Thus the bank in (1) is the original joint-spectrum source, not a constituent representation or a new reserve.

## Sharpness on actual Boolean gates

Take the actual AND2 sign h(x,y)=-1+2xy with equal probabilities p. Then D_x=y, D_y=x, so d=t=p. The singleton masses are v p^2 each, the pair mass/deficit is Delta=4p^2(1-p)^2, and R=0.

At p=1/2, j=1,u=1, L_1=0 and J_1/(2Delta)=ln4. This forces the first branch in (1). At p>1/2, j=0,u=p, J_1=0 and

    L_1/(2Delta)=-2p ln p/(1-p) ->2 as p->1.

The last limit follows from ln(1/p)/(1-p)->1, for example by integrating1/x on[p,1] and squeezing it between1 and1/p. Therefore every alpha requires the second branch2alpha. Together the two actual Boolean regimes establish the optimality of max(ln4,2alpha). This is not an FEI counterfamily: only the singleton-source constant is sharp.

## Independent carry-tradeoff reconstruction

For each genuine disjoint composition at the actual induced product laws, partition actual final labels into outer/child singleton and high labels. Let T>=0 be singleton scale imported into high degree; V>=0 the corresponding imported singleton mantissa charge. Let C_1 be genuine dyadic carry averaged on final physical singleton labels. Exact scale addition and the retained full singleton terminal give

    J_1(F)=J_1(g)+sum_i a_i J_1(f_i)-T+ln4 C_1,
    ln4 C_1+L_1(F)+V=L_1(g)+sum_i a_i L_1(f_i),

where a_i=I_i(g)/Var(f_i) and constant children are contracted. These are the scale and mantissa parts of the same physical coefficient factorization; no independence of spectral bits is invented.

At every gate define B_alpha=k_alpha(2Delta-R)-J_1-alpha L_1>=0, k_alpha=max(ln4,2alpha). Propagate the exact nonnegative gate weights omega and telescope the two displayed equations. For literal leaves this yields

    T_tot+J_1(F)+alpha[L_1(F)+V_tot]+B_alpha,tree
       =k_alpha(2Delta_F-R_tree)+(1-alpha)ln4 C_1,tot.     (4)

Here R_tree=sum omega R(g), NOT R(F). This derives the source's entire joint carry/refund tradeoff directly by linear combination. At alpha=ln2 the singleton-carry debit is(1-ln2)ln4 C_1,tot, with ln2 of both actual mantissa terminals still committed on the left. At alpha=1 it is the full singleton-entropy owner; at alpha=0 it is the sharp dyadic singleton-scale owner. These are alternative views of ONE source and must not be added. In particular reducing the displayed carry coefficient does not make the omitted mantissa fraction free.

## Verdict and first unsupported line

No repair to A041 sections2-3 is needed. The review does not independently accept its entire upstream dependency chain or every other statement in that run. Booleanity, genuine disjointness, actual induced biases, exact degree refund and full terminal laws are essential. The scalar supplier fails for real-valued half-literals, where d<t, so arbitrary candidate spectra are excluded.

The exact remaining universal line is an arity-independent bound on actual prime-gate J_hi funded from the SAME unused original source after all singleton/import/carry commitments. Neither (1) nor(4) pays it. The earlier prime decomposition/localization theorem, paid-sector references and import obstruction remain intact. Full FEI is OPEN at campaign close; no actual Boolean unbounded-ratio family has been produced here. This stage adds an independent source review and a final precise handoff, not a new class theorem.
