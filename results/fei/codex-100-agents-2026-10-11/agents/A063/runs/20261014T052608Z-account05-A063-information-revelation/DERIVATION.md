# Two-query history information on the B05 rare selector

All information is in bits. The common lift is the already established A037 canonical lift; the coarsening refund is the already established A063 R_A=I(S_A;X_A|S_C). Neither baseline is claimed anew.

## Exact barrier comparison

For a fixed block A refined into canonical singleton queries define Gamma_h=B_h-J_h>=0. The old coarsening identities immediately give

    B_A-J_A = 2 R_A + sum_h p_h Gamma_h.

Thus R_A<=(B_A-J_A)/2 is precisely the accumulated per-step MU inequality. It is not an additional stronger uncertainty bound. Equality requires Gamma_h=0 at every reached node. The old AND2 example has B_A=2, J_A=0, sequential B=J=1 and R_A=1; it proves sharpness with positive refund. No new census or MU reproof is needed.

The unsaved 2026-10-12 stage also observed the already paid bound R_A<= (2/ln2)I_A(f)-J_A, obtained by summing J_h<= (2/ln2)d_h and using the same fixed-block influence conservation. This is persisted here as a baseline consequence, not a new universal mechanism. It prevents treating order refunds as an unlimited entropy account.

## A two-query refund is an actual first-outcome information

Let A={i,j}, W=S_C, and query i before j. The first canonical kernel depends on the root spectrum only through (S_j,W), and the second kernel depends only on (W,X_i). Therefore

    R_{i then j}=I(S_j;X_i|W).

The deleted S_i is conditionally independent of X_i given S_j,W, and X_j is conditionally independent of all root spectral labels given W,X_i; the conditional chain rule proves the formula. It holds for every actual Boolean f, with zero fibers omitted. The other order gives R_{j then i}=I(S_i;X_j|W). This reduces the refund calculation to a two-by-two conditional probability table rather than a full root/history tree.

## Actual Boolean family and six exact coefficient classes

Let k>=4 be even, r=2k, delta=2^-k, p=2^-r=delta^2, d=p*delta. On k binary data bits let b_k=(-1)^(x1*x2+...+x_(k-1)*x_k), whose Fourier coefficients c_T are +/-s with s=2^(-k/2) and c_empty=s. Physical sign y=+1 selects b and y=-1 selects its actual singleton flip b-2*1_{x=0}. All r point controls activate only at their zero vertex. Thus

    F=1+A_r(z)[b_k(x)-1-(1-y)1_{x=0}]

is exactly B05's Boolean source, and Inf_y=d. No arbitrary real amplitude replacement occurs.

Take A={y,z1}; W consists of the data Fourier mask T and the remaining r-1 control mask U. Arrange the root coefficients as a two-by-two matrix with rows spectral y, columns spectral z1. Put C_T=p(c_T-1_{T=empty}-delta), B=p*delta. If W is nonempty the matrix is

    [ C_T  C_T ]
    [ B    B   ].

At W=empty it is

    [ A    C ]       C=-p(1-s+delta), A=1+C, B=d.
    [ B    B ].

There are (2^k+2^(k/2))/2 positive data coefficients and (2^k-2^(k/2))/2 negative coefficients, with the empty data coefficient in the positive group. The remaining-control masks have multiplicities 1 and 2^(r-1)-1. These give six classes and exactly 2^(k+r-1) residual masks. Walsh expansion of the physical formula proves every entry and multiplicity.

## All refund is in the empty residual packet

For nonempty W, the spectral z1 marginal is uniform and the conditional y-outcome kernel is independent of spectral z1 because its two columns coincide. Thus I(S_z1;X_y|W=w)=0. Conversely the z1 physical outcome is deterministically the activation sign +1 under either spectral-y row: I(S_y;X_z1|W=w)=0. The two-query formula therefore gives

    R_yz = q_empty I(S_z1;X_y|W=empty),
    R_zy = q_empty I(S_y;X_z1|W=empty).

This is a support statement about the actual function-specific history channel, not a bound on the full child entropy. The highly numerous bent packets create the local logarithmic erasure but contribute exactly zero to this two-query history refund.

## Quadratic suppression, both orders

For a Bernoulli outcome with conditional probabilities rho_v and average t, the KL/chi-square estimate ln u<=u-1 gives

    I(V;Y) <= Var(rho_V)/[t(1-t) ln2].

Write q=A^2+C^2+2B^2. For y-first the two spectral-z1 weights are q0=A^2+B^2 and q1=C^2+B^2, and rho_v=1/2+A_v B/q_v with A_0=A,A_1=C. Hence

    q Var(rho) = (q0 q1/q) B^2(A/q0-C/q1)^2 <= 2B^2.

The last inequality uses (u-v)^2<=2u^2+2v^2, A^2<=q0 and C^2<=q1. For z1-first the spectral-y weights are q0=A^2+C^2 and q1=2B^2, with rho0=1/2+AC/q0 and rho1=1. Thus q Var(rho)<=q1=2B^2.

Both outcome averages lie in [1/4,3/4]. Indeed a=1-s+delta is in [13/16,1], p<=1/256, A>=1-p, |C|<=p, B<=p/16 and q>1/2. For y-first, |t-1/2|=|B(A+C)|/q<=2B; for z1-first, |t-1/2|=|AC+B^2|/q<=4p<=1/64. Consequently

    0 <= R_yz,R_zy <= [32/(3 ln2)] d^2 <16 d^2.

Both refunds are strictly positive: in the central y-first table rho0>1/2>rho1 since A,B>0>C; in the z1-first table rho0<1/2 while rho1=1, and both row weights are positive. The strict last constant uses ln2>2/3, proved by its elementary positive atanh series. The bound is all-even-k analytic; finite interval checks below certify named exact instances only.

## The selector logarithm is not refunded by this small block

B05's selector bound is B_y >= (1-delta)(k-2)d. It can be reconstructed directly here: on each nonempty data packet the selector coefficients are a=p(c_T-delta), b=d, so q/b^2=(c_T/delta-1)^2+1>=1/(4delta). The inequality q h2(b^2/q)>=b^2 log2(q/b^2), summed over (2^k-1)2^r such packets, gives exactly (1-delta)(k-2)d. Thus this corollary uses the source bound with its proof reconstructed, not a floating certificate. Thus for either order

    R_A/B_y <=16d/[(1-delta)(k-2)] ->0.

In the selector-first order the MU deficit includes Gamma_y=B_y-J_y, with J_y<3d. For every even k>=6 it therefore gives

    (B_A-J_A)/2 >= (15/32)d,

whereas the actual refund is <=16d^2. Thus the actual-channel support bound is asymptotically much sharper than the raw accumulated MU ceiling. The block uncertainty barrier itself is still exactly per-step MU; the improvement uses the Boolean activation coefficient matrix and its information kernel.

This obstruction is narrow: it rules out paying the selector's unbounded B_y/d bill by the two-query refund from only one added control. It does not rule out paying the entire two-query block from its much larger actual control influence, querying more controls, existing control-first stopping certificates, or full FEI. Four terminal restrictions remain: inactive branches are constant, active branches retain B05's G and H with r-1 controls and all data. Their spectral entropy is never set to zero.

## First unsupported line and next mechanism

A terminal-certified reserve or compatible prescribed-witness reference must pay inherited erased/core entropy in addition to these revealed-information charges. The first unsupported universal line is that a source-owned shared-control/witness correction plus that full retained terminal bill has a dimension-independent influence price. The one-control refund cannot supply the logarithmic source bill. A064 and A097 already identify shared-control ownership and excess shared-data collision as the remaining mechanisms; this result should be used as their rare-selector information control rather than starting another refund-only search.
