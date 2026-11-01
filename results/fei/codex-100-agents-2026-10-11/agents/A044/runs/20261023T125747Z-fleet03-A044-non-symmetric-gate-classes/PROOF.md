# Singleton import has a single all-depth entropy owner

All logarithms are natural. This is an author analytic proof, pending
independent review. It consumes A043's one-boundary singleton import
theorem and A041's joint telescope, and separates their source accounts.
It proves a depth-independent payment for the TOTAL singleton import,
including the original refund. It does not pay arbitrary prime J_hi.

## Definitions and physical scope

Let f be a Boolean sign under a finite independent interior product law.
Contract deterministic coordinates and constant children first. Write
v_i=4p_i(1-p_i), c_S=hat f(S)/sqrt(v_S), P_S=v_S c_S^2.
For occupied nonempty S choose j_S>=0 so 1/2<u_S=2^j_S|c_S|<=1.
Dyadic boundary values use u_S=1. Booleanity gives |c_S|<=1.
All quantities below omit zero-mass labels. Set

    Delta_f=I_f-Var(f), R_f=sum_(|S|>=3)(|S|-2)P_S,
    M_f=sum_(|S|>=2)P_S=Delta_f-R_f,
    E_1(f)=sum_single P_S ln(1/c_S^2),
    J_1(f)=ln4 sum_single P_S j_S,
    L_1(f)=E_1(f)-J_1(f)=sum_single P_S ln(1/u_S^2),
    J_hi(f)=ln4 sum_high P_S j_S,
    L_hi(f)=sum_high P_S ln(1/u_S^2).

Every summand of L_1,L_hi is nonnegative. The actual Boolean derivative
D_i=(f|i=1-f|i=0)/2 is in {-1,0,1}. If t_i=|E D_i| and
d_i=E D_i^2 then d_i>=t_i, and h(t)=2t^2 ln(1/t)<=2t(1-t)
by ln x<=x-1. Actual Parseval gives

    sum_i v_i(d_i-t_i^2)=2Delta_f-R_f,
    E_1(f)<=4Delta_f-2R_f.                              (1)

This records the original singleton bank. No auxiliary reference is
assumed Boolean and no bank is renewed after a prior debit.

## Exact entropy lost from the singleton sector at one boundary

Let F=g(f_1,...,f_m) be a genuine disjoint physical composition, with g
evaluated at the ACTUAL independent child-output law. Put

    w_i=Var(f_i)>0, a_i=I_i(g)/w_i,
    s_i=P_g({i}), b_i=(I_i(g)-s_i)/w_i>=0,
    M_i=M(f_i).

The occupied Fourier label S decomposes uniquely into outer set A and
nonempty child labels T_i. The exact physical identities are

    c_F(S)=c_g(A) product_(i in A)c_i(T_i),
    P_F(S)=P_g(A) product_(i in A)P_i(T_i)/w_i.           (2)

A FINAL singleton is exactly A={i}, T_i a singleton. Thus its log
coefficient is the sum of the root-singleton and child-singleton logs.
Partitioning the complete expectations, rather than dropping terminal
entropy, gives the exact nonnegative entropy transport

    B_out=sum_i (s_i/w_i) M_i ln(1/c_g({i})^2),
    B_in =sum_i b_i E_1(f_i),
    E_1(g)+sum_i a_i E_1(f_i)-E_1(F)=B_out+B_in.         (3)

Terms with s_i=0 are zero without assigning a log to a zero coefficient.
For B_out, the root singleton is lost precisely when its selected child
label is high. For B_in, a child singleton is lost precisely when its
outer label has degree at least two. These disjoint events account for
every term in (3), using the true conditional label experiment in (2).

A043's actual singleton SCALE imports are

    T_out=ln4 sum_i (s_i/w_i) M_i j_g({i}),
    T_in =sum_i b_i J_1(f_i), T=T_out+T_in.

Define their actual imported singleton MANTISSA refund by

    V_out=sum_i (s_i/w_i) M_i ln(1/u_g({i})^2),
    V_in =sum_i b_i L_1(f_i), V=V_out+V_in>=0.

Since ln(1/c^2)=j ln4+ln(1/u^2), (3) yields

    T+V+E_1(F)=E_1(g)+sum_i a_i E_1(f_i).              (4)

This is the new split. The import is paid by the singleton entropy
ACTUALLY lost, and V is the part of that same payment left over after
the scale debit. The full singleton terminal is retained exactly.

## All-depth theorem and the separate high-carry refund

Consider any finite genuine disjoint formula with literal leaves.
Let omega_root=1 and omega_child=omega_parent a_i. Each node's
T_v,V_v is computed at the boundary between its gate and its ACTUAL
child subfunctions, as above. Put

    T_tot=sum_internal omega_v T_v,
    V_tot=sum_internal omega_v V_v,
    R_tree=sum_internal omega_v R(g_v),
    S_tree=sum_internal omega_v[4Delta(g_v)-2R(g_v)-E_1(g_v)].

Both V_tot,S_tree are nonnegative. Weighted telescoping of (4), whose
literal-leaf terms are zero, and exact Delta additivity give

    T_tot+V_tot+E_1(F)=sum_internal omega_v E_1(g_v),
    Delta(F)=sum_internal omega_v Delta(g_v),
    T_tot+V_tot+E_1(F)+S_tree=4Delta(F)-2R_tree.          (5)

In particular the TOTAL import, with no depth or fan-in surcharge, obeys

    0<=T_tot<=4Delta(F)-2R_tree-E_1(F)<=4Delta(F).       (6)

The coefficient 4 is NOT asserted sharp. It does not replace A043's
ln4 one-boundary constant by a smaller number: it bounds a DIFFERENT
quantity, the weighted sum at ALL depths. A043's majority tower already
shows why simply renewing ln4 Delta(F) is false. Equation (5) supplies
one original bank with explicit refunds instead.

For clarity retain A043's exact high-scale decomposition at each boundary.
Let kappa(S)=j_F(S)-j_g(A)-sum_i j_i(T_i)>=0 and
C_hi=sum_(|S|>=2)P_F(S)kappa(S). Then

    J_hi(F)=J_hi(g)+sum_i a_i J_hi(f_i)+ln4 C_hi+T.       (7)

Exact corrected entropy composition plus (4) and (7) now gives the
SEPARATE mantissa identity

    ln4 C_hi+L_hi(F)=L_hi(g)+sum_i a_i L_hi(f_i)+V.       (8)

Let C_hi,tot=sum_internal omega_v C_hi,v. Telescoping again,

    ln4 C_hi,tot+L_hi(F)=sum_internal omega_v L_hi(g_v)+V_tot,
    J_hi(F)=sum_internal omega_v J_hi(g_v)
                        +ln4 C_hi,tot+T_tot.           (9)

Thus V_tot belongs to the carry bank in (9) AFTER it remains from the
scale import payment in (5). It is not available for a second debit
against J_hi. The original A041 joint bank is exactly the sum of these
two equations; here its import and high-mantissa owners are explicit.
Since L_hi(g)<=ln4(Delta_g-R_g), their sum recovers, without changing
the old theorem or adding capacity,

    T_tot+ln4 C_hi,tot+E_1(F)+L_hi(F)
      <=(4+ln4)Delta(F)-(2+ln4)R_tree.                 (10)

No additivity of R_tree and the final physical R_F is asserted.

## Complete references and ordinary KL remain attached

At every physical function h use the singleton-preserving complete law
Q_h: Q_h(S)=P_h(S) on |S|<=1, and Q_h(S)=M_h W_h(S)/Z_hi,h
on high labels, with W_h=v_S4^-j_S. At M_h=0 set Q_h=P_h.
Let n_h=M_h ln(Z_hi,h/M_h). Since P<=W<4P,

    0<=n_h<=ln4 M_h,
    K_h=KL(P_h||Q_h)=n_h-L_hi(h),
    E(h)=E_1(h)+J_hi(h)+n_h-K_h.                       (11)

Compose the COMPLETE references using
Q_tree(S)=Q_g(A) product_i Q_child,i(T_i)/w_i, including the actual
empty atom and the unique full conditional nonempty child laws.
This law preserves actual final singleton masses by induction, not
merely the total nonempty mass. Ordinary likelihood ratios multiply,
so K_tree=sum_internal omega_v K_gv. The corrected complete tree
cross entropy is

    CE_tree^+=sum_internal omega_v[E_1(g_v)+J_hi(g_v)+n_gv],
    E(F)=CE_tree^+-K_tree.                             (12)

Substituting (5) and (9) into (12) yields the explicit signed comparison
with the final flat paid-sector reference:

    K_flat-K_tree=CE_flat^+-CE_tree^+
      =ln4 C_hi,tot-V_tot+n_F-sum_internal omega_v n_gv. (13)

Equation (13) also follows directly from (8) and K=n-L_hi.
It is signed, not a positive reserve. T_tot cancels because its owner
was the transferred singleton entropy, rather than a new normalizer.
Full ordinary cross entropies append the SAME physical-bias correction
and empty entropy to both sides. Both full terminal laws and the final
singleton terminal are retained. No old KL is subtracted a second time.

If arbitrary prime gates obey J_hi(g)<=K Delta_g at every arity and
actual induced product law, (10)-(12) imply
E(F)<=(K+4+ln4)Delta(F), with no depth or fan-in dependence.
This conditional implication is unchanged from A043/A041; the new result
is the separate all-depth payment (5) and its refund ownership (8),(13).
The prime premise is still universal and unproved.

## Controls, validation and first unsupported line

For fair Maj3 towers of depth d, all occupied coefficients are dyadic,
so every mantissa, carry, normalizer and ordinary KL is zero. Here
I=(3/2)^d, Delta=I-1, E_1(F)/ln4=d(3/4)^d and the weighted
local singleton entropy is (3/2)ln4 Delta. Equation (5) therefore gives
T_tot/ln4=(3/2)Delta-d(3/4)^d, precisely A043's tower formula.
At d=4 the excess over ln4 Delta is 49ln4/64. Our all-depth bound
remains valid. This is an actual Boolean depth control, not an FEI
counterexample and not evidence for paying arbitrary prime J_hi.

The finite checker freezes 288 small physical compositions and 12
compressed tower depths. All logarithmic equalities are checked exactly
as rational prime-exponent vectors; positive refunds use their actual
mantissa arguments >=1. A separate direct-mixed-difference implementation
uses rigorous logarithm intervals on a fixed smaller domain. These
certificates validate the interface; the arbitrary-depth and arbitrary-
arity assertion follows from the explicit weighted telescope above.

The first unsupported universal line remains J_hi(g)<=K Delta_g (or
its refund-inclusive form) for arbitrary irreducible gates at all
induced laws, paid from genuinely unused original capacity. Solving
the singleton-import transport does not supply that bound. In
particular V_tot and S_tree cannot be spent once here and then offered
again as fresh scale payments. Full FEI remains OPEN.
