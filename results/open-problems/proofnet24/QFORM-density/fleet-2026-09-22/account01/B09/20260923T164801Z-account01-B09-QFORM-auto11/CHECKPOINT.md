SIGNED IN - working on the quadratic-form bounded-density conjecture (universal constant), account account01, slot B09, 2026-09-23T16:48:01Z.
attacking: spend a fixed physical hub-pair's aggregate source-coordinate third volume directly, with arbitrary same-side leaf curvature, by a random original-coordinate split and the completed two-hub crossing-block theorem.

# Early substantive checkpoint

Let H={a,b} be two literal physical coordinates and L=H^c. Put M=A[H,L] (a 2 x |L| matrix) and D=A[L,L]. For i in L define

V_i := sum_{T subset L\{i}, |T|=3} det A[H union {i},T]^2,
V := sum_i V_i.

For any literal partition L=I disjoint_union J let G_J=M_J M_J^T, Delta_J=det G_J, Pi_J the orthogonal projection in R^J onto row(M_J), and

C_{I,J}:=D[I,J](Id-Pi_J),   F^2:=||C_{I,J}||_F^2.

For each i in I, Schur/Gram plus Cauchy-Binet gives the exact identity

Delta_J ||D[i,J](Id-Pi_J)||_2^2
 = sum_{T subset J, |T|=3} det A[H union {i},T]^2.

Hence

W(I,J):=Delta_J F^2
 = sum_{i in I} sum_{T subset J, |T|=3} det A[H union {i},T]^2.    (1)

If each leaf is put in J independently with probability p and in I otherwise, then every source minor in V appears in W with probability (1-p)p^3, so

E W=(1-p)p^3 V.                                                   (2)

At p=3/4, E W=(27/256)V. Therefore some physical partition satisfies W >= (27/256)V. Moreover, if max_i V_i <=(27/512)V, then for that same partition every row contribution W_i <=V_i <=W/2. Thus the row-spread hypothesis in the completed Claude two-hub crossing theorem (single_hub_core, Theorem 6.5) is automatic, and since s_1(M_J)s_2(M_J)F=sqrt(W),

||p_Q||_inf <=5.35 W^(-1/6)
 <=5.35(256/27)^(1/6)V^(-1/6)<7.784 V^(-1/6).                  (3)

If instead some i has V_i>(27/512)V, promote i to a third literal physical hub. Cauchy-Binet gives det(A[H union{i},L\{i}] A[H union{i},L\{i}]^T)=V_i. The completed three-hub theorem (same source, Theorem 6.3) then gives

||p_Q||_inf <=3 sqrt(2) V_i^(-1/6)
 < 3 sqrt(2)(512/27)^(1/6)V^(-1/6)=4 sqrt(3)V^(-1/6).          (4)

Thus the fixed-pair aggregate volume V>0 appears to imply a continuous density with the unconditional bound

||p_Q||_inf <7.784 V^(-1/6),
P{Q in B}<7.784 V^(-1/6)|B|,

with arbitrary physical 2x2 hub core and completely arbitrary leaf quadratic block D. No rotation of the product law and no small-matrix-as-small-random-error step occurs.

Next in this run: audit the exact hypotheses of Theorems 6.3/6.5 at the current Claude continuation, apply the designated account02/B09 volume identity to an actual target family, and write the full proof with source pins and remaining full-target gap.
