# Interacting physical tangent blocks with one committed account

All functions are actual Boolean signs on a uniform cube. Entropies are in bits. Put c=2/ln(2) and K=4+c. This is an author proof, pending independent review. It applies established block entropy machinery to the physical half-cube invariant; it does not claim a new general multiplexer inequality or full FEI.

## 1. Physical lower bound, without restrictions on interactions

Let q be quadratic over F2 on n ORIGINAL physical coordinates, Q its alternating polar matrix, i a coordinate with Q_i nonzero, P={partial_i q=1}, and g=(-1)^q(1-2*1_E). Let e_out=|E intersect P^c|. Take any set J not containing i with Q_ij=0 and Q_j not in span_F2{Q_i} for every j in J. No condition is imposed on Q_jk for j,k in J.

For every such j, j-edges stay within P and within P^c. Independence of Q_j,Q_i makes partial_j q balanced on P^c. The original quadratic therefore has j-pivotal probability 1/4 in P^c. Each outside edited vertex changes at most one undirected j-edge, losing at most 2/2^n of total probability. Thus

 Inf_j(g)>=1/4-2 e_out/2^n.

This is the stage18 physical counting argument, reproduced here so the new application is source-complete. Inside edits are unrestricted. In particular, e_out<=2^n/32 gives Inf_j(g)>=3/16 for all j in J, even when the rows interact.

## 2. Apply the established full-block entropy split once

Let I_J=sum_(j in J) Inf_j(g) and let L_J=average_a H(g|J=a), with the entire restricted Boolean function in each terminal. The established uniform selector-block identity gives

 D_J:=H(g)-L_J=B_J+M_J,
 B_J=H(S_J|S_Jc), 0<=M_J<=c I_J,

where S has the ORIGINAL squared Fourier law. Consequently

 B_J<=H(S_J)<=sum_(j in J) h2(Inf_j(g)).

The function h2(t)/t decreases for 0<t<=1. Also h2(3/16)<3/4: after multiplying by 16 ln(2), this is equivalent to 3^3*13^13>2^52, an integer inequality. Hence, if e_out<=2^n/32,

 D_J<=K I_J.                                      (1)

The corresponding exact ORIGINAL physical influence identity is

 I(g)=I_J+average_a I(g|J=a).                       (2)

Equations (1)-(2) pay the whole interacting block at the SAME K. There is no assumption that a later singleton query remains locally K4-good. This is a direct application of the lead's established multiplexer/selector-density machinery, rather than a re-proof of that general bound. The new mathematical scope is removal of pairwise polar noninteraction and allowance of a bounded amount of outside contamination, with arbitrary inside edits and full retained leaves.

For clean outside half, the same argument yields the sharper coefficient 4 h2(1/4)+c=8-3 log2(3)+c; the unchanged K is retained for compatibility with the prior stopping account.

## 3. Exact account through every adaptive prefix

Commit to this J at a reached node. Let T be ANY finite adaptive prefix that queries only unused coordinates of J, with a stop decision depending only on already observed query outcomes. It may choose coordinates differently in different histories. For each terminal v let w_v=2^(-depth(v)), g_v its FULL conditional Boolean function, J_v the unqueried members of J, and I_v^J=sum_(j in J_v) Inf_j(g_v). Finish by querying all J_v in any order, keeping every full final leaf. Define

 A_T=sum_(internal v) w_v Inf_(j_v)(g_v),
 D_T=H(g)-sum_(terminal v) w_v H(g_v),
 R_T=sum_(terminal v) w_v [H(g_v)-average_b H(g_v|J_v=b)].

Every full completion has the SAME partition J=a. The entropy and influence telescopes therefore give, exactly,

 D_T+R_T=D_J,
 A_T+sum_v w_v I_v^J=I_J.                          (3)

Both D_T and R_T are nonnegative by the Boolean selector entropy split. From (1), the committed original account Z_T=K I_J-D_T obeys

 Z_T-R_T=K I_J-D_J>=0.                            (4)

This is a nonrenewing account: the right-hand side is independent of T, all previous entropy debits remain, and BOTH full child entropies enter each split. It is deliberately NOT claimed that D_T<=K A_T or that every descendant has an eligible tangent row. Nor may the reserved remaining-J influence be spent again on a full child FEI bill. The original I_J is allocated once to this committed block; the final terminals retain only the influence outside J in (2). The unused remainder and its still owed completion bill are explicit in (3)-(4).

The same conclusion composes over any external stopping tree whose reached nodes each meet the physical hypothesis and commit disjoint still-unqueried blocks: apply (1)-(2) conditionally and telescope the ACTUAL weighted influence once. This remains a conditional policy theorem, not a universal block-selection theorem.

For the packet's recursive-address ledger, after the address is fixed at a physical data label y_z, write the reached function as g*y_z. Its spectrum is just the phase spectrum shifted by that data coordinate, so H(g*y_z)=H(g) and I(g*y_z)=I(g)+1. Every control-block query above has the same influence as for g; all terminal children retain the SAME y_z and the weighted total of its influence remains one. Reusing that gate label across levels creates no new influence allowance. For several reached histories, weight their respective block charges by the actual physical reach probabilities; the influence telescope spends each original queried control once along each path, regardless of label sharing on other branches.

## 4. A genuinely bad intermediate physical query

Take the saved stage17 six-bit Boolean h(k,r) whose selected coordinate k has Inf_k(h)=1/8 and

 B_k(h)=(136 log2(17)+120 log2(5)-704)/256>1/2.

The strict sign is exactly 17^136*5^120>2^832. Introduce distinct ORIGINAL coordinates i,p,j,z, keep k,r as the six coordinates of h, and set q=i*p+j*k. Define an actual g by g=(-1)^(j*k) on p=0 and g=(-1)^z h(k,r) on p=1. Then E={x:g(x)!=(-1)^q(x)} lies entirely in P={p=1}; Q_i=e_p, and j,k are eligible tangents at the root, with Q_jk=1. Root Inf_j=1/4 and Inf_k=1/4+Inf_k(h)/2=5/16.

After the actual physical query j=0, its child is f=1 on p=0 and f=(-1)^z h on p=1, with i now irrelevant. The z tag separates the Fourier support of h from the vacuum. Each h coefficient appears in two disjoint p rows with magnitude half as large. Thus B_k(f)=B_k(h)/2 and Inf_k(f)=Inf_k(h)/2=1/16, so B_k(f)>4 Inf_k(f). This is an exact obstruction to hereditary singleton K4 payment, yet (1)-(4) pay the entire interacting block J={j,k} from the original I_J=9/16. No affine coordinate replacement, ghost coordinate debit, or branch entropy is discarded.

## 5. First unpaid universal line

The physical hypothesis need not supply any J, and no theorem pays every full final leaf from the remaining influence. Even a clean quadratic outside one half-cube permits an arbitrary Boolean function on the other half; a constant outside carrier is not a certified terminal class. The next necessary step is to select a useful next block or terminal payment after a committed interacting block, using ONLY the unallocated original physical influence and retaining all complete leaves. The ledger alone does not supply that selection or the missing FEI estimate.

More precisely, for ANY Boolean h let A_h(p,z,x)=1 on p=0 and (-1)^z h(x) on p=1. The tag separates all h frequencies from the vacuum, giving exactly H(A_h)=2+H(h)/2 and I(A_h)=1+I(h)/2. These are actual retained leaves of the construction in section4 (with h replaced by the appropriate k-cofactor). If H(A_h)<=C I(A_h) were proved uniformly for arbitrary h, then H(h)<=C I(h)+2C-4. Applying this to tensor powers of h and dividing by their number gives full FEI with the same C. Conversely full FEI at C>=2 immediately pays these leaves at C. Thus treating arbitrary constant-outside-half leaves as free terminals would hide the original universal problem. This exact localization is an obstruction warning, not a separate proposed solution.

There is also an exact obstruction to merely continuing the SAME quadratic-row selection rule. After completing J={j,k} in section4, the inherited quadratic is i*p plus a constant. All remaining polar rows except i,p are zero; the only two nonzero rows interact. Hence there is no eligible tangent, although the retained h-cofactor is arbitrary. More generally an alternating matrix of rank at most two has no pair with Q_i nonzero, Q_ij=0 and Q_j outside span(Q_i): in rank two write Q=a*b^T+b*a^T with independent a,b. Independence of its two rows forces their coefficient pairs (a_i,b_i),(a_j,b_j) to be independent, so their determinant Q_ij is one, contradicting tangency. The committed-block payment therefore cannot certify universal termination merely by iterating its existing polar-row predicate. A residual-core estimate or a paid change of reference is required.
