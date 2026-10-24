# Interleaved selector reserve: independent reconstruction and extension

All entropies are bits. A finite uniform control cube chooses a label L among independent Boolean cores u_j on pairwise disjoint data cubes; constant output states are allowed. F=u_L. At an actual physical history h, let q_j=P(L=j|h), m_j=E(u_j|h), V_j=1-m_j^2 and psi(q)=q log2(1/q), psi(0)=0. Define R_h=sum_j psi(q_j)V_j. Reached histories fix physical coordinates, so their unrevealed control and data coordinates remain independent. This holds for adaptive choices: each individual reached history is a rectangular cylinder, even though the union of histories need not be.

## 1. Exact first-revelation accounting

At a query of data coordinate i belonging to core j, the selector probabilities and other core means are unchanged. If beta=hat u_j({i}), the two child means are m_j +/- beta. Thus V_j-average V_j(child)=beta^2=t, and

    R_h-average R_child = psi(q_j)t.                         (1)

At a control query, all core means remain unchanged and q_j=(q_j^0+q_j^1)/2. Thus

    D_h=R_h-average R_child
       =sum_j V_j[psi(q_j)-{psi(q_j^0)+psi(q_j^1)}/2]>=0.   (2)

The inequality is concavity, not a reference-KL refund. Summing the two node types on any finite adaptive physical restriction prefix gives exactly

    sum_data w_h psi(q_j,h)t_h + sum_control w_h D_h
           + E_leaf R_leaf = R_root.                      (3)

Actual stopping leaves remain on the left. Therefore the data rarity account can never exceed its initial reserve, irrespective of interleaving. A control query releases this reserve; it does not inject a fresh copy.

## 2. Quantitative release at each physical control edge

For a,b>=0, the scalar Jensen gap is

    psi((a+b)/2)-(psi(a)+psi(b))/2
      =(a+b)/2*[1-h2(a/(a+b))] <= |a-b|/2.

This follows from h2(z)>=2 min(z,1-z), including zero endpoints. Couple the two controller slices by the same remaining control assignment z, giving labels L0(z),L1(z). Then |q_j^0-q_j^1|<=E_z|1_{L0=j}-1_{L1=j}|. For distinct labels j,k, independent cores have mismatch probability (1-m_j*m_k)/2 and

    V_j+V_k <=2(1-m_j*m_k)=4*P(u_j!=u_k).

Constants satisfy the same inequality with V=0 and m=+/-1. Consequently

    0<=D_h<= (1/2)E_z[(V_L0+V_L1)1_{L0!=L1}]
           <=2 Inf_i(F_h).                                (4)

Labels selecting the same actual core must first be merged: distinct labels here have disjoint independent cores or constant outputs. No shared-data extension is asserted.

The factor 2 in (4) and (5) is sharp. Let one fair control choose between two independent dictator cores u,v (a second dummy control embeds this in the frozen census). Then q_u=q_v=1/2, V_u=V_v=1, R_root=1, and I_ctrl=1/2. Querying that control gives deterministic selectors at both children, so D_root=1=2 Inf_control. This is a sharp reserve-release witness, not a sharp full-erasure price.

## 3. Initial reserve is paid once

For each 0/1 selector C_j, indicator edge isoperimetry gives 2psi(q_j)<=I(C_j), where I(C_j) is probability-of-change influence. One slice induction proves this: crossing edges dominate |a-b|; the remaining induction step is exactly the scalar h2 inequality above. Summing weighted selector edge changes and using the independent-core mismatch inequality gives

    R_root <= (1/2)sum_j V_j I(C_j) <=2 I_ctrl(F).           (5)

I_ctrl is the actual exclusive physical influence, not a sum of nominal activation accounts. (1)-(5) are source-independent reconstructions of A057's reserve mechanism and its extension to controller exposure.

## 4. Reviewed cap and its precise interleaved consequence

At a data query of core j, write F=C_j u_j+W with C_j W=0, W^2=1-C_j. The auxiliary cube includes all controls and other independent cores. Put a=W+m_j C_j, c=C_j, and M(s)=sum_T Phi(ahat(T)^2,s chat(T)^2), Phi(A,B)=(A+B)h2(B/(A+B)). Orthogonality gives sum ahat^2=1-q_j V_j and sum V_j chat^2=q_j V_j. Concavity of homogeneous binary entropy gives M(V_j)<=h2(q_j V_j). The recentered cap is min{M(V_j),(t/V_j)M(V_j)+q_j t log2(V_j/t)}, with cap zero for V_j*t=0. Using h2(x)<=x log2(e/x), the variance logarithms cancel exactly and

    cap <= q_j t[log2(1/q_j)+log2(e)+log2(1/t)]
         <= c_data q_j Inf_i(u_j)+psi(q_j)t,
    c_data=(1+2/e)/ln2.

For the final inequality use |beta|<=d=Inf_i(u_j), t<=d, and t log2(1/t)<=[2/(e ln2)]d: divide by d>=sqrt(t) and maximize sqrt(t) ln(1/t). This independently reconstructs the price in A057 PROOF Sections 1 and 3. The separate scalar envelope dominating M(t), coherent N corollary, and fresh activation suffix are not accepted by this scoped review.

On any interleaved prefix, let Pi_data=sum_data w_h Inf_i(F_h). Physical influence telescoping implies Pi_data<=I_data(F): restriction to any other coordinate preserves remaining-coordinate influence in expectation, while querying that coordinate removes its current influence. Combine the local cap bound with (3):

    sum_data w_h cap_h
       <=c_data Pi_data+R_root-E_leaf R_leaf-sum_control w_h D_h
       <=c_data I_data(F)+2 I_ctrl(F).                     (6)

This prices ONLY caps at data queries. It does not price control-query erasure, product-reference Bayes resets, signed inner decrements, or actual terminal Fourier entropy. It extends the proved data-only selector reserve to arbitrary interleaving without reopening the controller resource. No universal FEI constant follows.

## 5. Source scope and first unsupported line

The A057 source's final sentence says its selector inequality does not pay an arbitrary controller reserve and uses priority widths r,s>=1. That sentence conflicts with its own Section 3 and current claim: Section 3 proves the arbitrary partition payment (5). This is a stale scope sentence; the Section 3 argument is valid. Our review accepts only the reconstructed positive-cap/selector-reserve subclaim and records the documentary inconsistency. It does not mark the entire bundled claim independently accepted.

The first unsupported universal line is: the control-query erasure and signed source-compatible product/occupancy reset, plus the inner data decrements and E_leaf H(F_leaf), can be paid from the remaining physical influence without spending R_root again. Equations (3) and (6) retain a usable terminal reserve but provide no such entropy/reset bound. Next compare one actual Bayes reset with the release D_h on a three-state priority controller after a nonconstant data prefix, retaining both actual child cores.
