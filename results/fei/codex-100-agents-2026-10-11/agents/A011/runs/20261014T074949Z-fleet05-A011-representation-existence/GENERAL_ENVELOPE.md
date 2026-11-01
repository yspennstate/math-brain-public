# Arbitrary-core point edit: explicit paid envelope with a cost factor

This is a conditional one-operation repair of the existing point-edit reference interface. It is not a new universal FEI proposal: iteration increases the rate. All logarithms base2, ideal complete-reference cost with separate global integer rounding.

Let g be ANY Boolean function on n>=1 uniform data bits, y* any point, r>=1 fresh point controls, p=2^-r,t=2^-n. Put F=g-2g(y*)1_x*1_y*, a_T=ghat(T), b_T=g(y*)chi_T(y*) in{+-1}, P_T=a_T^2. Supply any data subprobability R of mass s<=1 positive on P support and finite cost c=CE(P,R); zeros off that support are allowed. Write C=2pt(n-d), E=2ptd, J=2rpt, where d is the ORIGINAL pivotal degree at y*. Then I(F)=I(g)+C-E+J. Every erased edge is retained.

## Pointwise domination and the complete output reference

The actual data marginal is q_T=a_T^2-4pt b_T a_T+4pt^2. Completing the square and using Young's inequality,

    -4pt b_T a_T <= a_T^2+4p^2t^2,
    q_T <=2P_T+4pt^2(1+p)<=2P_T+6pt^2.

Put beta=6pt in(0,3/2] and U_n(T)=t. The positive envelope need not itself be the true law or a physical mixture. Define

    Rdagger=(R+beta U_n)/(1+beta),
    Qdagger(U,T)=Rdagger(T)K_true(U|T).

All data fibers q_T are positive, since q_T=(a_T-2ptb_T)^2+4p(1-p)t^2>0. Thus K_true is normalized on every fiber. The whole reference mass is M=(s+beta)/(1+beta)<=1, and every true output atom is covered. The exact full cost and residual debt are

    CE_F=CE(q,Rdagger)+B,
    CE_F-H(F)=D(q||Rdagger), B=H(selector spectral set | data spectral set).

No analytical envelope label is sampled or transmitted, and no reference mass or KL is discarded.

## Quantitative price of its use

Because Rdagger is a subprobability, all log(1/Rdagger(T)) are nonnegative. Pointwise domination therefore bounds the ACTUAL data cross entropy by

    CE(q,Rdagger)<=2CE(P,Rdagger)+beta CE(U_n,Rdagger)
                 <=2c+2log(1+beta)
                    +beta[n+log((1+beta)/beta)].

This is a bound under the actual q, not a renormalization of the envelope. For beta<=3/2, log(1+beta)<=2beta, log(1/beta)=n+r-log6, and2beta<=3. Hence the data bill is at most2c+beta[2n+r-log6+7]. The true conditional selector bound from direct point-edit coefficients is B<=4p(1-p)tn+8rpt<=4ptn+8rpt. Combining,

    CE_F <=2c+pt[16n+14r+42-6log6]
          <=2c+30pt(n+r)
          =2c+15(C+E+J).                       (G)

For the second inequality, n,r>=1 implies14n+16r>=30, and log6>=2 gives42-6log6<=30. Thus no floating constants or asymptotic parameter restriction are used. The bound is intentionally conservative.

## One source bank, including its extra inherited-cost debit

At K>=15 let S_K=K I(g)-c. The exact physical identity and(G) imply

    K I(F)-CE_F >= S_K-c+(K-15)(C+J)-(K+15)E.   (B)

The extra c is explicitly charged to the same unused source reserve; it is not spent a second time for free. All incident old pivotal edges are distinct cube edges, so I(g)>=2td and E<=p I(g)<=I(g)/2. Consequently, whenever c<=C0 I(g), C0>=0, rate K=4C0+15 pays the whole reference:

    K I(F)-CE_F >= [K-2C0-(K+15)/2]I(g)
                   +(K-15)(C+J)>=0.

This includes I(g)=0 provided the supplied source cost is0. A positive-cost model for a constant source does not satisfy the conditional hypothesis and is not silently reset.

Any independent Boolean terminal h with prescribed complete finite-cost reference retains exactly c_h+CE_F and D_h+D(q||Rdagger) under the fixed product model, and physical influence adds. Conditional c_h<=C_h I(h) gives max(C_h,4C0+15) for the tensor. The terminal reference mass also multiplies and is not discarded.

## History with missing reference mass retained

Given this incoming subprobability model Q of mass M, query a fair physical coordinate j. Let m=(P_0+P_1)/2, r be Q marginalized over queried membership, and pi_b=P_b/(2m) on positive m fibers. On zero true fibers choose any normalized posterior, explicitly retaining positive reference r there. Set Rtilde_b=2r pi_b, Z_b=sum Rtilde_b, and R_b=M Rtilde_b/Z_b. Then Z_0+Z_1=2M, each inherited child reference retains mass M, and on true atoms

    P_b/R_b=(m/r)(Z_b/M).

The full ledger is

    CE_parent=avg CE_child+Delta_j+L_j-avg log(Z_b/M),

with L_j the measured incoming conditional divergence. The divergence release is nonnegative, since log is concave and the normalized Z_b/M sum to2. Repeating actual inheritance, with original physical reaches, telescopes the full leaf costs and signed query costs to the SAME incoming CE; its original bank is therefore sufficient for that whole ledger. This is cost disintegration, not an influence price for every child model or authorization to construct fresh descendant floors. For independent subprobability terminal references, keep their original mass using product-compatible zero-fiber choices rather than normalizing it away.

## Exact remaining universal line

The construction now supplies a paid complete reference for EVERY one-point core edit conditional on an influence-paid source model. Its limitation is quantitative and explicit: inherited c has coefficient2 and the admitted rate becomes4C0+15. Recursively constructing arbitrary Boolean functions by point edits therefore gives no dimension-independent rate. The missing universal step is to absorb this extra c and erased-edge debit from one inherited unused reserve at a FIXED rate through an actual selected history, or find a sharper envelope with no repeated rate inflation. The weak unequal-amplitude two-query example proves that simply charging every physical query by a constant times its own influence cannot substitute for that one-use bank.
