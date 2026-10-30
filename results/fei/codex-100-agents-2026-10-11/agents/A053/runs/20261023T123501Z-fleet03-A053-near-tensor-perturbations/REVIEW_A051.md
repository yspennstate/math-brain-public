# Scoped independent reconstruction of reference-error occupation

Source: A051 runs/20261023T113401Z-fleet03-A051-near-extremizer-definition/STOPPING.md, read whole. Acceptance here is sections1--2 and equations1--3a only. No repair is supplied.

Transport the SAME fixed root signed character and the actual Boolean function through each affine input map, output character and restriction. Comparing the two commutes with each map, so the event Z of their disagreement is a fixed original-input event. Conditional on a visited current node the unqueried current cube is uniform; each daughter has probability1/2. Thus q_v=P(Z|v) has the exact daughter-average martingale identity. This is not a newly optimized character at every node.

The standard one-query channel bound, retained as its stated source dependency, is L_v<=phi(m_v), phi=h2+2x/ln2 and directional minority m_v<=min(2q_v,1/2). Phi is increasing and concave on[0,1/2]. Clipping2q at1/2 yields an increasing concave function of q: its derivative decreases to a positive value and then drops to zero. These facts justify Jensen on the actual INTERNAL-NODE occupation measure.

Directly, sum_internal w_v=E tau, while sum_internal w_v q_v=sum_internal P(Z and visit v)=E[1_Z tau]. These are finite sums of the same event indicators; no independence is presumed. Dividing by the first total and applying Jensen gives the claimed entropy loss bound, including all terminal entropies by exact telescoping. At zero query occupation both totals vanish and no ratio is formed. Nonincreasing-I resets additionally imply E I_leaf<=I_root.

The exact identity D_root+S_leaf+K(Q+R)=H_root-E H_leaf follows by substituting the definitions, with Q+R=I_root-E I_leaf and S_leaf=E[K I_leaf-H_leaf]. It preserves both the signed terminal reserve and the original influence expenditure. This proves the stated compensated admission bound, not a paid query selector.

Independent.py reproduces a small complete physical guard: for the three-bit zero-vertex error, query until the first1. Then e=1/8, E tau=7/4, E[1_Z tau]=3/8, but e E tau=7/32. Thus replacing the occupied error moment by an independence product is already false on an actual small Boolean tree.

Verdict HOLDS at sections1--2 scope, conditional only on the explicitly retained source one-query channel inequality, also rederived independently in the new LINEAR_RADIUS_PROOF equation5 at the coordinate level. The source large activation family and its2058-bit constants are read context but are not independently accepted by this review. No universal stopping payment, independent-agent acceptance of A053's new radius theorem, or shared-registry adoption is claimed. In particular a noncharacter code seed cannot be inserted as a new fixed character reference without proving the required channel estimate for that reference.
