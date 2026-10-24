SIGNED IN - working on the quadratic-form bounded-density conjecture (universal constant), account account02, slot B02, 2026-09-24T02:37:12Z.

attacking: `QFORM-COUPLED-TWO-LOWRANK-CUTS-OR-LARGE-DIAGONAL-L1-v1` by propagating the live ultra-near-rank-two physical crossing to the two full one-sided physical cuts, and spending any transverse escape with the completed marginal-free sharp-HY E3 / D5 Fourier receivers.

# Early substantive calculation — full-cut exterior lift

Let `R,C` be disjoint original-coordinate sets, `O=[n]\(R union C)`, and let

`M=A[R,C]=U diag(s_j) V^T`, `x_j=s_j^2`, `x1>=x2>=...`.

Let `U2=span(u1,u2)`, `V2=span(v1,v2)` and write `P_U,P_V` for their coefficient-space orthogonal projections. Put

`G_C=A[O,C]`, `G_R=A[R,O]`,

`delta_C^2=||G_C(I-P_V)||_F^2`, `delta_R^2=||(I-P_U)G_R||_F^2`.

The two enlarged matrices

`B_C=A[C^c,C]=[M;G_C]`, `B_R=A[R,R^c]=[M,G_R]`

are literal disjoint original-coordinate cross blocks.

For one appended row `g`, exterior Cauchy--Binet gives

`sum_{i<k in R} |m_i wedge m_k wedge g|^2
 =sum_j |<g,v_j>|^2 e2(x without j)`.

For `j>=3`, `e2(x without j)>=x1*x2`. Therefore, summing the distinct three-row families and retaining the all-`M` triples,

`E3(B_C)>=E3(M)+x1*x2*delta_C^2`.          (E3-C)

The transposed argument gives

`E3(B_R)>=E3(M)+x1*x2*delta_R^2`.          (E3-R)

No random variable is rotated; `U,V` are used only in this coefficient identity.

There is also a fifth-volume companion. In the `E5(B_C)` Cauchy--Binet sum retain row quintuplets consisting of two rows from `M` and three rows from `G_C`. For a three-vector `w=g_a wedge g_b wedge g_c`, the `v1 wedge v2` component of the two-row exterior covariance contributes `x1*x2`, and it wedges only with the `Lambda^3(V2^perp)` component of `w`. Hence

`E5(B_C)>=x1*x2*E3(G_C(I-P_V))`.             (E5-C)

Likewise

`E5(B_R)>=x1*x2*E3((I-P_U)G_R)`.             (E5-R)

Thus the reviewed sharp-HY receivers apply on the actual enlarged physical cuts:

`||p_Q||inf <=10.3450832322 [E3(B_*)]^(-1/6)` with `phi_Q in L1`,

and independently

`||p_Q||inf <=(5e/sqrt(2)) [E5(B_*)]^(-1/10)` with `phi_Q in L1`.

Apply this to the live account01/B02 r42 ultra-near-rank-two packet

`x1*x2>247/576`, `E3(M)<2^-18`, `sum_{j>=3}x_j<9/1011712`.

If either enlarged full cut has `E3>=2^-18`, the full law is paid by

`||p_Q||inf <=8*10.3450832322 <82.760666`,

`integral |phi_Q| <=2*pi*8*10.3450832322 <520.000601`.

If both enlarged cuts remain below `2^-18`, (E3-C)/(E3-R) force

`delta_C^2,delta_R^2 < (576/247)2^-18 = 9/1011712`,

so the original rank-two tube propagates to both full one-sided cuts:

`dist_F(B_C,{rank<=2})^2 <= ||B_C(I-P_V)||_F^2
 <18/1011712`,

`dist_F(B_R,{rank<=2})^2 <= ||(I-P_U)B_R||_F^2
 <18/1011712`.

Numerically the distance is `<0.004218...` on each side. Thus any unspent third spectral credit can no longer hide in a diffuse transverse outside coupling: after the E3/D5 exits it is confined to the aligned rank-two carrier and/or the same-bank principal blocks. Nonzero tails are retained throughout.

This is an early checkpoint; final report will supply the full exterior proof, constants, latest-partner application, correction refresh and exact remaining implication.
