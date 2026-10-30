SIGNED IN - working on the quadratic-form bounded-density conjecture (universal constant), account fleet02, slot B01, 2026-09-24T08:06:57Z.
attacking: almost-single-leaf stability in the finite-leak rank-one two-hub arrowhead; spend the two Schur singular directions before the weak tail.

# Early calculation: uniform arrowhead stability

Let the residual coefficient on two original hub coordinates H and an original product leaf bank Y be

S = [[B, w c^T], [c w^T, D]],

with B symmetric 2x2, D diagonal, and assume s_2(S)>=1. All affine terms are arbitrary. Set delta=1/4 and rho=3/4.

Key observation: if a chosen cross packet E has operator norm <delta, deleting only that packet gives S0 with s_2(S0)>=rho by singular-value Weyl. The block-diagonal S0 then allocates its two large singular directions among a fixed hub/heavy-leaf core and diagonal leaves. Conditioning on the deleted-packet variables turns the deleted cross packet into affine terms; it is never treated as a small random quadratic perturbation.

Small total cross case ||w|| ||c||<delta: compare S with B direct_sum D. If B has two singular values >=rho or two leaf diagonals have modulus >=rho, the orientation-free rank-two affine half-Riesz theorem gives <=128 rho^(-1/2). In the mixed allocation, one singular value of B and one leaf diagonal are >=rho; the literal 3x3 hub-hub-leaf block differs from B direct_sum [d] by an off-diagonal perturbation of norm <delta, so its second singular value is >=rho-delta=1/2. The previous B01 3D theorem therefore gives H_(1/2)<=169 sqrt(2)<240.

Heavy-leaf small-tail case: if c_h^2>||c||^2/2 and q=||w|| ||c_tail||<delta, retain the heavy leaf in the 3x3 core C_h and delete only the tail cross packet. Then S0=C_h direct_sum D_tail and s_2(S0)>=rho. The allocations C_h twice-large and two tail diagonals are paid respectively by the 3D theorem and rank-two affine theorem. In the mixed allocation, s_1(C_h)>=rho and one tail |d|>=rho. Keeping that leaf and conditioning the rest gives dY^2+2Y<u,Z>+Z^T C_h Z with ||u||<delta. Completing Y changes C_h by uu^T/d, norm at most delta^2/rho=1/12, so the Schur core has operator norm at least 2/3. Some physical coefficient has magnitude at least 2/9, hence H_(1/4)<=4(9/2)^(1/4). The pinned logarithmic two-square interface gives H_(1/2)<45 in this branch.

If the heavy tail q>=delta, then q_h=||w|| |c_h|>q and the completed grouped heavy-leaf theorem gives H_(1/2)<=2^(23/8)(q_h q)^(-1/4)<=2^(31/8)<15. If no leaf is heavy and ||w||||c||>=delta, the grouped spread theorem gives H_(1/2)<=2^(13/4) delta^(-1/2)<20.

Therefore the candidate uniform theorem is H_(1/2)(R)<240 for the entire rank-one two-hub arrowhead class whenever s_2(S)>=1. This would remove the theta^(-1/4) almost-single-leaf loss completely. Full QFORM remains open; the outer scalar pivot is still paid separately by the pinned square peel.
