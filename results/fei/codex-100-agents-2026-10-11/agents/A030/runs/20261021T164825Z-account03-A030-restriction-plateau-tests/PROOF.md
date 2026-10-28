# Equal-mean controller correction

Target (under verification): let C_j partition an arbitrary finite uniform controller cube into three labels; let u_j be independent Boolean cores on disjoint cubes with common mean m. Put q_j=E C_j, V=1-m^2, h_j=1-2C_j and F=u_kappa. All entropy is in bits. Define phi(s)=-s log2(s), with phi(0)=0, and

L(q)=phi(q^2)-phi((1-2q)^2)/4+2q(1-q).

The expected identity is

H(F)=sum_j q_j H(u_j)+(V/4)sum_j H(h_j)+V sum_j L(q_j).

For any controller coordinate i, let D_i denote the actual root-minus-mean-child entropy decrement; let R=V sum_j phi(q_j), and let kappa_i=R-E R_child. Then

E_i=D_i(F)-(V/4)sum_j D_i(h_j)-kappa_i
   =V[sum L(q_j)-E sum L(q_j_child)]-kappa_i.

The bound is E_i<=14 Inf_i(F), including V=0 and zero-influence endpoints. The following is an analytic proof, with independent review pending. The finite certificate checks its identities and fixtures; it does not substitute for the all-dimensional argument.

## Fourier derivation

Write c_j(S)=hat C_j(S) and a_j(T)=hat u_j(T). For a nonempty private Fourier set T in core j the coefficient of F at (S,T) is c_j(S)a_j(T). No other core contributes because the private blocks are disjoint. All-empty private sets have controller function sum_j m C_j=m, so this sector consists of exactly the constant coefficient m. There is no nonconstant controller coefficient in that sector. The squared masses in the other sectors sum to sum_j q_j V=V, while the constant sector has mass m^2.

Use phi(ab)=b phi(a)+a phi(b), also valid when a or b is zero. Parseval gives sum_S c_j(S)^2=q_j and sum_{T nonempty} a_j(T)^2=V. Thus

H(F)=phi(m^2)+sum_j [V sum_S phi(c_j(S)^2)+q_j(H(u_j)-phi(m^2))]
    =sum_j q_j H(u_j)+V sum_j sum_S phi(c_j(S)^2).

The last cancellation uses sum_j q_j=1. Since h_j has empty coefficient 1-2q_j and nonempty coefficients -2c_j(S),

H(h_j)=phi((1-2q_j)^2)+4 sum_{S nonempty}phi(c_j(S)^2)-8(q_j-q_j^2).

Solving this identity, and adding the empty indicator mass phi(q_j^2), gives sum_S phi(c_j(S)^2)=H(h_j)/4+L(q_j). This proves the displayed collapse. Every sum is finite. Labels of zero or full probability are included by phi(0)=phi(1)=0; surjectivity is not needed for the theorem.

## Uniform scalar estimate and physical edge coupling

The function L is continuously differentiable on [0,1], using the continuous convention x ln|x|=0 at zero, with

L'(q)=2-4q-[4q ln q+2(1-2q)ln|1-2q|+1]/ln 2.

For 0<=x<=1, |x ln x|<=1/e by elementary differentiation (the unique interior maximum of -x ln x is x=e^-1). Hence

|L'|<=(6/e+1)/ln 2+2<=55/8<7.

The rational inequalities used here are e>=8/3 (the first four nonnegative terms of its series) and ln2>=2/3 (integrate 2/(1-s^2)>=2 from 0 to 1/3). The same bound covers the derivative limits at q=0,1/2,1. Thus L is 7-Lipschitz on the closed interval. No unbounded derivative of phi(q) has been treated as bounded.

Pair the two endpoints of each physical controller i-edge and let t be the probability that its labels differ. Let q^0,q^1 be the child label distributions. Their coupling yields ||q^0-q^1||_1<=2t; because q=(q^0+q^1)/2, each ||q^s-q||_1<=t. Therefore

sum_j L(q_j)-(1/2)sum_{s,j}L(q_j^s)<=7t.

Concavity of phi gives kappa_i=V[sum phi(q_j)-(1/2)sum_{s,j}phi(q_j^s)]>=0. On a changed-label edge, the actual independent Boolean core outputs disagree with probability (1-m^2)/2=V/2. The same physical edge is used once, so d_i=Inf_i(F)=Vt/2. Consequently E_i<=7Vt=14d_i. If V=0, all cores are the same constant and both sides vanish. If t=0, the controller restrictions agree pointwise and every decrement and release is zero. No zero denominator is canceled.

## Original reserve and full terminals

For three labels, the original harmonic cut weights are w_j=V/4 on the equal-mean slice. Supply a C-priced own-history potential r_j for each actual cut h_j on ONE fixed controller policy: D_i(h_j)<=C Inf_i(h_j)+r_j-E r_j_child. The physical edge identity gives sum_j(V/4)Inf_i(h_j)=d_i. Therefore the SAME P=(V/4)sum r_j and original R=V sum phi(q_j) satisfy

D_i(F)<=(C+14)d_i+(P+R)-E(P_child+R_child).

Each child keeps its actual r_j continuation. More precisely, let s_i=C d_i+P-E P_child-(V/4)sum D_i(h_j)>=0 be the unused slack in that single declared cut transaction. The exact signed transaction is

D_i(F)-C d_i-(P+R)+E(P_child+R_child)=E_i-s_i.

Thus one can use this actual slack before charging additional influence; it is not a second bank. A complete controller-only continuation keeps the means unchanged and telescopes to

H(F)-sum_j q_j H(u_j)<=(C+14) I_controller(F)+P_root+R_root,

when the cut potentials vanish at complete controller leaves. These leaves are the actual u_j, with their full entropy and influence retained. No FEI estimate for u_j or h_j is inferred. If cut potentials have nonzero terminal values, retain their weighted terminal subtraction in the same telescope instead.

## Hypotheses and first unpaid step

Equal means are used exactly in replacing sum m_j C_j by the constant m and in w_j=V/4. Dropping equal means introduces coherent empty-private Fourier rows; an exact Boolean countercontrol in the checker breaks the identity. Disjoint independent cores are used in separating the nonempty-private sectors and in the changed-label disagreement probability. If all labels share the SAME nonconstant physical core, F is that core and the collapse generally fails (the controller terms cannot be charged as independent sectors). Uniform fair controller queries are used in the midpoint and edge coupling. No spectrum flatness, bound on controller dimension, monotonicity or lower bound on V is used.

This control-only theorem is not closed under arbitrary DATA histories: a query in one nonconstant core can make its child means differ from the other cores. The earlier general harmonic P remains a DATA martingale, but the scalar entropy collapse then fails. The first unsupported line is payment of the resulting unequal-mean coherent row correction from the SAME unused inherited account, with both actual child terminals and the old cut continuations retained. Initial admission of all three cut reserves also remains unpaid; no universal FEI constant follows from this theorem.

## Actual non-flat query and the exact unused slack

The surjective three-control label table (0,0,0,0,1,1,1,2), indexed by the least significant coordinate first, with three independent two-bit point-defect cores of mean 1/2 has V=3/4. Query control coordinate 2 first and then coordinates 0,1. At C=1 the actual cut reserves are

r_0=0, r_1=3-(9/8)log2(3), r_2=7/2-(9/8)log2(3).

The original P=39/32-(27/64)log2(3) has child values 0,9/16. The original R=3/2-(9/32)log2(3) has child values 0,3/2-(9/16)log2(3). The actual queried influence is d=3/8. Direct physical Fourier summation gives

E=-3/8+(27/64)log2(3), s=3/16,
E-s=-9/16+(27/64)log2(3) in (1/10,7/64).

Thus the SAME cut transaction has positive unused slack, but that slack alone does not cover the coherent correction. The exact additional influence rate required at this node is (E-s)/d=(9/8)log2(3)-3/2>0. All three terminal core entropies are 2, all three core influences are 1, and the weighted core reserve at C=1 is 3/2. Its mean controller drift is zero. Its value is not a free second correction budget: the original full terminal continuations still require it. This refutes only the declared no-extra-price local P+R transaction, not global reallocation, another reference, or FEI.

There is an actual non-flat predecessor: replace core 0 by U(y,x), whose y=0 child is the same point defect and y=1 child is a padded dictator. Its mean is 1/4; the other two means are 1/2. Query y, then the three controls in the declared order, then every remaining private bit. The certificate retains BOTH y children (means (1/2,1/2,1/2) and (0,1/2,1/2)), and all cut/core own-history reserves from the original policy. The complete ten-bit fixed tree satisfies D<=15 Inf+A-E A_child at every one of its 1023 internal nodes for A=P+R+sum q_j Q_1(u_j); all 1024 constant leaves have zero reserve and zero entropy. The unequal-mean sibling is certified directly on this finite tree, not admitted by the equal-mean theorem. At the first data query, P is exactly harmonic, so the equal-mean branch is reached with its original account rather than a renewed bank.
