# Vacuum-calibrated inherited owners and a zero-refund Boolean family

Author proof, independent-person review pending. All logarithms are base2. FEI remains OPEN.

## 1. Universal reference operation

Let P,r be probability laws on a finite set with distinguished empty atom0 and D(P||r)<infinity. Put p=P(0), q=r(0). Define C_P(r)(0)=p and C_P(r)(s)=(1-p)r(s)/(1-q) for s!=0. If p=1 use point_empty; if p<1 then q<1 by finite KL. The case q=1,p=1 uses the same convention. Exact KL disintegration gives

 D(P||r)=D(Bern(p)||Bern(q))+D(P||C_P(r)).             (1)

Thus calibrating vacuum odds while retaining the inherited nonempty profile NEVER costs positive signed target-minus-inherited KL. It releases exactly the binary vacuum KL. This holds for arbitrary finite laws, not just Fourier laws. It is not a claim that a prescribed different nonempty profile is free.

## 2. Every physical controller history, one original owner

Let a be ANY finite Boolean function on the uniform cube, P its squared Walsh spectrum. Choose 0<=sigma<=1/2 and any normalized law nu on the nonempty frequencies. If p=P(0)<1, set q0=(p,(1-p)nu) and r0=(1-sigma)P+sigma q0; at p=1 take r0=P. The ONLY original mismatch payment is

 D0=D(P||r0)<=-log2(1-sigma)*(1-p)<=Var(a)<=I(a).       (2)

This follows by conditioning on the nonempty row and r0>= (1-sigma)P within that row. Constants have D0=0. No lower bound I(a)>=1 is used.

At every physical query, push the current r along the ACTUAL phase channel for a: for paired amplitudes u,v, erase their coordinate and give outcome b probability (u+(-1)^b v)^2/[2(u^2+v^2)], with fair extension on zero pairs. Propagate every reference atom, including off-actual-support atoms. Normalize by the actual reference branch masses rho_b>0 to obtain inherited r_b^-; then use r_b=C_(P_b)(r_b^-). BOTH physical children have actual mass1/2.

Let E_v be the KL erased by pairing, O_v=D((1/2,1/2)||(rho_0,rho_1)), and Z_vb=D(Bern(P_b(0))||Bern(r_b^-(0))). KL chain rule and(1) give the exact nonnegative debit identity

 D_v=E_v+O_v+(Z_v0+Z_v1)/2+(D_v0+D_v1)/2.            (3)

For EVERY finite adaptive physical stopping tree, with original control reaches p_v, telescope ONCE:

 D0=sum_internal p_v[E_v+O_v+average_b Z_vb]
                      +sum_leaves p_e D(P_e||r_e).     (4)

No dimension bound, balancedness, product structure, fixed query order or complete tree is required. Every resulting reference has its actual leaf vacuum. This is a universal reference-history closure theorem; it supplies no bound on H(a)/I(a).

Adding the actual entropy telescope yields the single original CE-owner identity

 CE(P,r0)=sum_internal p_v[Delta H_v+E_v+O_v+average Z_vb]
                         +sum_leaves p_e CE(P_e,r_e). (5)

Every old entropy spend and both terminal KLs remain. The source credit on a query is the actual CE decrement; it is never replaced by a fresh smoothed supplier. Equations(3)--(5) also hold on a control tree induced by arbitrary DATA stopping decisions whenever the active control cylinders partition the original control cube, as in A021@3. DATA queries do not themselves alter this control-only owner identity.

For completeness Delta H_v>=0: pairing gives the projected law Q=(P_0+P_1)/2, so H(P_parent)-average H(P_b)=H(queried frequency bit|other frequencies)+JS(P_0,P_1). Thus every term spent in(5) is nonnegative. The tree identities follow by finite induction with the actual reach p_v, rather than any independence assumption on successive query costs.

## 3. Application to the already diminished A021/A022 account

Consume A021-NONFLAT-INHERITED-REFERENCE-DATA-QUERY@3 and A022's prepaid-owner handoff (run20261023T120109Z, PROOF1--4) only at their author-proved, pending-review scope. Original t>=2, delta=8^-t, g negative at000, b=g tensor t, F=b except F(v,z)=b(v)a(z). DATA has a fixed block-first order and pathwise cap3floor(t/2)+2; CONTROL occurs only on active data cylinders. Keep prescribed q_h, frozen inactive references, old U<=t/64, original reaches and every earlier spend. A021's SAME bank B_H is >=t/32 for t2 and >=t/16 for t>=3.

Use(2)--(5) instead of uncalibrated source inheritance. Prepay epsilon=delta D0 ONCE from that old bank. At an active terminal e of DATA reach w_e and control reach p_e use the complete reference q_h tensor M_eta(r_e), eta=delta/w_e, M_eta(r)=(1-eta)point_empty+eta r. At inactive leaves use q_h tensor point_empty; release, rather than omit, their old complete controller cost. Let L_r=delta sum_active p_e CE(P_e,r_e), C_new the complete frontier CE, and

 Bstar=4I_DATA,remaining+L_r-C_new-U-epsilon.

Write A_cal for the exact old-reference calibration credit:
sum_active w_e p_e D(M_eta(P_e)||M_delta(P_e)) plus ALL inactive frozen controller costs. It is nonnegative. Since every r_e has the actual vacuum, the mixture identity is EXACTLY

 D(M_eta(P_e)||M_eta(r_e))=eta D(P_e||r_e).            (6)

Consequently the A022 subtraction becomes

 Bstar-B_H=A_cal-epsilon,                            (7)

with no selector-erasure surplus invented. Thus Bstar>=B_H-delta and retains13t/576: t2 gives3/64>26/576; t>=3 follows from t/16-8^-t>=13t/576. The smallest displayed margin is1/576 at t2. Equation(4) tracks the original D0 into actual phase/outcome/calibration credits and BOTH full terminal debts; it is not paid again. The signed global Bstar+D_new+E_r identity is A022 PROOF4 with CE decrements from(5). All old U, entropy spend and full terminal KLs remain.

The new closure is calibration after EVERY inherited control query, including unequal-DATA-depth histories within the original cap. It is not cap removal or an influence-priced entropy supplier.

The source phase channel in(3) uses a_e's amplitudes. It is not identified with the full F_e phase channel. Actual F target-minus-inherited KL conversion is kept separately in the complete frontier account exactly as in A022 PROOF4; the comparison(7) follows from marginal CE subtraction, not from pretending those channels coincide.

In particular Z_vb is SOURCE credit, not extra cash to add to B_H. If the inherited source vacuum was mismatched before calibration, calibration removes its nonnegative mixture-selector slack V_eta=eta D(P||r)-D(M_eta(P)||M_eta(r)). The full F account may lose that old slack. Equation(7) compares the calibrated endpoints directly and never adds Z or V_eta a second time; this is why its reserve conclusion remains valid.

## 4. Parameterized actual Boolean zero-refund counterfamily

For EVERY k>=1 let a_k(z)=(-1)^(sum_{j=0}^{k-1} z_(2j) z_(2j+1)), on2k uniform bits, N=4^k. Each two-bit factor has Walsh amplitudes(+/-1/2), so the product has P_k(s)=1/N on every frequency. Its mean is2^-k, H(a_k)=2k, I(a_k)=k, hence H/I=2 exactly.

Index frequencies0,...,N-1. Define r_k(0)=r_k(1)=1/N; for the remaining N-2 frequencies give (N-2)/2 of them mass3/(4N) and the rest5/(4N). This is a normalized actual-vacuum-calibrated reference. It has r=(P+q0)/2, where q0 agrees at0,1 and has masses1/(2N) and3/(2N) on those two groups. Therefore it satisfies the original owner eligibility(2). Direct rational-log calculation gives

 D_k=(N-2)/(2N)*log2(16/15)>0,
 D_k>= (1/4)log2(16/15),
 lim_k D_k=(1/2)log2(16/15).                          (8)

For EVERY 0<eta<=1, since P_k(0)=r_k(0),

 eta D_k-D(M_eta(P_k)||M_eta(r_k))=0 EXACTLY.          (9)

The entire nonempty profile bill eta D_k survives mixture-selector erasure. Thus no positive c can guarantee a selector-erasure refund >=c eta D(P||r) for ALL actual Boolean spectra and all vacuum-calibrated profiles, even when the profiles are dominated root smoothings. For arbitrary t>=2 these a_k are actual controllers in the point-surgery family, with eta=8^-t or any admitted conditional delta/w. The global reached mismatch is delta p_e D_k, not a new supplier.

Scope: this parameterizes A022's finite isovacuum witness and refutes only the proposed positive-fraction selector-refund rule for nonempty profile mismatch. It refutes NO FEI constant, NO all-coordinate influence rule and NO universal route. Phase-query refunds can still be positive; (9) concerns the mixture selector only. The actual controller family has FEI constant2. It is not an unbounded H/I construction.

## First unsupported universal line

For the one original vacuum-calibrated owner, CE(P_a,r0)<=K I(a) for all Boolean a would imply FEI, while FEI(C) implies this certificate with C+1 by(2). The universal supplier is still FEI-equivalent. It cannot be obtained by relabelling(4) as a fresh entropy grant or by demanding a positive selector refund contradicted by(9). Removal of the DATA cap must also keep the complete terminal KL conversion. The shortest next step is to test an actually required nonempty descendant profile against the inherited calibrated profile and fund its residual signed KL from the SAME unused original owner.
