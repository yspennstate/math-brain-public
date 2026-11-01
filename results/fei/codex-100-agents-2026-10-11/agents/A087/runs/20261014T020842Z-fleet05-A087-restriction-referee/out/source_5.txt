# Interleaved stopping with biased terminals and one selector reserve

All entropy quantities below are in bits. Influences are physical probabilities
of a sign-function change on a uniform finite cube. Let a controller on a cube
Z choose a state j in a finite exclusive partition C_j. State j outputs a
Boolean u_j on its own data cube Y_j; these cubes are pairwise disjoint and
disjoint from Z. Constants +/-1 are permitted as states. The function is
F=sum_j C_j u_j. Consider ANY finite adaptive physical restriction tree that
queries controller or data coordinates in any interleaving and stops at any
frontier. Every reached node is a cylinder, so its remaining blocks are still
independent uniform cubes. Zero-probability selector states can be omitted.

At a node let q_j=E C_j, m_j=E u_j, V_j=1-m_j^2. Set

    eta(x)=x log2(1/x),
    U=sum_j q_j[H(u_j)-eta(m_j^2)],
    R=sum_j q_j log2(1/q_j)V_j.

U uses raw nonempty Fourier entropy, not normalized conditional entropy. These
potentials include biased and constant terminal cores. Define root R_0 and U_0.

## 1. Exact selector-reserve reset at a controller query

For a controller coordinate X, q_j is the average of its two slice probabilities
q_j+ and q_j-. All m_j,V_j and core spectra are unchanged. Therefore U is a
martingale at this step and

    kappa_X=R-E R_child
      =sum_j V_j [q_j log2(1/q_j)
                  -(q_j+ log2(1/q_j+)+q_j- log2(1/q_j-))/2]
      =sum_{j:q_j>0} q_j V_j D_2(P(X|C_j)||uniform) >=0.       (1)

For q_j=0 all its slice probabilities vanish. The KL expression holds also when
one slice vanishes. This is an actual physical controller reset, including
arbitrary overlapping nominal events after exclusive partitioning. It releases
the previously assigned reserve; it does not assign it again after the query.

## 2. Exact reserve loss and signed inner cancellation at a data query

Query i in core j. Let beta=hat u_j({i}), t=beta^2, d=Inf_i(u_j), q=q_j,
V=V_j, m=m_j. Core child means are m+/-beta, so

    R-E R_child=q log2(1/q)t,        Inf_i(F)=q d.             (2)

The q's do not change. Other cores and their spectra do not change. For the
actual auxiliary function W=sum_{k!=j} C_k u_k write a=W+m C_j, c=C_j.
Pointwise C_j W=0 and W^2=1-C_j. Put

    Phi(A,B)=(A+B) h2(B/(A+B)),
    M(s)=sum_T Phi(ahat(T)^2,s chat(T)^2),
    N=sum_T {paird(ahat(T),beta chat(T))-Phi(ahat(T)^2,t chat(T)^2)},
    paird(a,b)=eta(a^2)+eta(b^2)
                  -[eta((a+b)^2)+eta((a-b)^2)]/2.

The exact biased-child split, independently reconstructed by separating empty
and nonempty core Fourier rows, is

    D_i H(F)=q[D_i H(u_j)-paird(m,beta)]+M(t)+N.              (3)

The empty inner pair is negative in (3) and cannot be omitted. Since
paird(m,beta)=eta(m^2)+eta(t)-E eta(m_child^2), (3) becomes

    D_i H(F)=U-E U_child + M(t)+N-q eta(t).                  (4)

Thus every inherited core entropy difference is an exact change in U, regardless
of intervening controller queries. It is not paid again at ancestor levels.

## 3. Pointwise prices and a stopping theorem

The recentered cap from A056/A057 is

    cap=min{M(V),(t/V)M(V)+qt log2(V/t)},

zero at t=0 or V=0. It bounds M(t). Here t<=V by Parseval, and
|beta|<=d by the Boolean half-derivative. For completeness, sum ahat^2=1-qV
and sum V chat^2=qV. Concavity of the homogeneous packet gives M(V)<=h2(qV).
Using h2(x)<=x log2(e/x) in the second cap branch cancels log(V):

    cap<=q log2(1/q)t +qt/ln2+q eta(t).                     (5)

The raw scalar JS-Hellinger bound, valid without equal individual row masses,
gives 0<=N<=2qt/ln2. Equations (2),(4),(5) yield the NEW one-step drift

    D_i H(F)<=[U+R-E(U_child+R_child)]+3qt/ln2.              (6)

In particular the 2/e singleton-log payment in the positive cap is not needed
for this full signed DATA decrement: its eta(t) charge cancels the exact
negative empty-core term. That cancellation does not pay controller decrements.

For reach weights w_v define T_data=sum_data w_v q_v t_v and
Pi_data=sum_data w_v Inf_i(F_v). Always T_data<=Pi_data. For controller nodes
write D_v=H(F_v)-E H(F_child) and retain the SIGNED residual D_v-kappa_v.
Summing (6) and the exact controller reset gives

    H(F_0)<=E H(F_leaf) +U_0-E U_leaf +R_0-E R_leaf
              +(3/ln2) T_data
              +sum_controller w_v(D_v-kappa_v).             (7)

The full influence identity on this SAME tree is

    I(F_0)=Pi_data+Pi_controller+E I(F_leaf).                (8)

Equations (7)-(8) hold for arbitrary depth, arity, adaptive choices and biased
terminals under the disjoint-independent-core hypothesis. They keep actual
terminal functions, not the terminals of a different exposure order.

There is a stronger exact accounting identity for the R bank itself:

    R_0=E R_leaf+sum_data w_v q_v log2(1/q_v)t_v
                   +sum_controller w_v kappa_v.             (9)

All three terms on the right are nonnegative. Thus no controller interleaving
can reopen the same rarity reserve. Each finite root has a bounded monotone
sum under refinement. No infinite-cube Fourier limit is claimed.

For the POSITIVE cap alone, use eta(t)<=2d/(e ln2) and (5):

    sum_data w_v cap_v +E R_leaf+sum_controller w_v kappa_v
       <=c_data Pi_data+R_0, c_data=(1+2/e)/ln2.             (10)

This extends A057's data-only prefix scope to any interleaving and adds the
actual biased terminal reserve. Only the cap bank is priced by (10).

## 4. Initial funding and no double use of control influence

Indicator edge-isoperimetry gives q log2(1/q)<=I(C)/2. A proof by slice induction
uses h2(z)>=2min(z,1-z) and crossing influence >=|q_+-q_-|. On a control edge
switching states j,k, independent data cores have mismatch
(1-m_j m_k)/2, and V_j+V_k<=2(1-m_j m_k). Summing over control edges gives

    R_0<=2 I_ctrl(F_0).                                    (11)

This is initial funding of R, not an additional consumed-query allowance.
One cannot pay (10) from 2 I_ctrl and then spend that identical control account
again on the controller sum in (7) or terminal H. The exclusive ledger is (9).
If all states are constants, U=R=kappa=0 and (7) leaves the exact arbitrary
controller entropy path. This is a Boolean scope guard showing that universal
pricing of the remaining controller-plus-terminal ledger is still FEI-strength.

## 5. Explicit growing-depth tests with biased frontiers

Let C be the all-+1 event on r controller bits, u=product_{a=1}^m y_a,
and F=1+C(u-1). Interleave controller and data bits arbitrarily; stop after
any number of queries. Before the final data bit is fixed the surviving parity
core is balanced; afterwards it is a biased constant +/-1. On a reached live
node with a unresolved controller bits and a balanced core, q=2^-a,V=1,
R=a2^-a. Revealing a control bit releases kappa=q, exactly as (1). The
other child is the constant +1. Revealing a nonfinal parity bit has t=0 and
changes neither U nor R; the final data bit has t=1 and uses the remaining
R once. Formula (9) and the terminal correction in (7) therefore hold for
arbitrarily growing r+m without a depth factor. Bias endpoints at those
frontiers are handled directly, with no division by V=0.

The previously known exact root entropy Q_r<=6r2^-r and influence
I(F)=2^-r(m+r) show H<=6I for this test family. That is an existing activation
calibration, not the new theorem. The stage's advance is the interleaved
reserve reset, biased stopping frontier and signed empty-core cancellation.

First unsupported universal line: the sum of the actual signed controller
residuals in (7), together with its actual terminal entropy and retained U
correction, is paid from an exclusive unspent physical influence account.
Shared DATA cubes are also excluded: both the independence edge funding (11)
and separate-core signed inner reconstruction can then fail. No full FEI
claim is made.
