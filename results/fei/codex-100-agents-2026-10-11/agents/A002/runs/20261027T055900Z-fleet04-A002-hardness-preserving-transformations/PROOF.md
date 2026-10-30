# One Gibbs budget across an adaptive affine-reset tree

The local capacity is paid once per actual query. It is not a new source account. The complete terminal reserve and the dependence on the unqueried spectrum stay in the identity.

## 1. Scope and the local identity

Let f be a Boolean sign on a finite uniform cube. Entropies are in bits. Write a(f) for the minimum influence over invertible affine input maps and output characters, and D_C(f)=H(f)-C a(f), C>0. These finite operations preserve entropy. At the root choose an actual representative with I=a. At every internal node v, choose a nonempty block A_v of the current physical coordinates, retain every complete restriction, then replace each child by an actual entropy-preserving affine/character representative with I=a. Stop at any nodes. The tree is finite; each query lowers the coordinate dimension. Randomized policies are also allowed by averaging finite deterministic policies. No nonlinear phase multiplication is free.

Let rho_v be the actual physical probability of reaching node v. Child probabilities are rho_v/2^r_v, where r_v=|A_v|. Keep these reaches through every reset. Put sigma_v=I_A(f_v), R_v=E_x I(g_x)-E_x a(g_x)>=0, where g_x are the COMPLETE unreset children. Let P_v be the squared Fourier law in this node's own coordinates, B_v the remaining coordinates, and

    J_v=H(f_v)-E_x H(g_x)-H(Z_A|Z_B).

The block Fourier chain rule and fibrewise log-Sobolev give 0<=J_v<=c sigma_v for c=2/ln(2), or for any specified larger c. These are properties of complete Boolean children, not individual unsigned rows. Set

    gamma=C-c, theta=1/(1+2^gamma), kappa=log2(1+2^(-gamma)),
    Q_v=Ber(theta)^r_v,
    W_v=D_2(P_v || Q_v tensor P_(v,B)), G_v=c sigma_v-J_v.

All reference probabilities on A are strictly positive; zero exterior fibres are omitted. Expanding cross entropy gives

    W_v=r_v kappa+gamma sigma_v-H(Z_A|Z_B).

Physical influence splitting is I(f_v)=sigma_v+E I(g_x). Resetting the children decreases that last mean influence by R_v and preserves their entropies. Therefore, with d_v=D_C(f_v) and d_child evaluated AFTER reset,

    d_v-E_x d_child+C R_v+W_v+G_v=r_v kappa.       (1)

No criticality is used in (1). This independently reconstructs the local content of A051's conditional Gibbs certificate and A054's capacity bound. The c=3 version used in the exact checker is a weaker rational-reference instance, not a numerical replacement for 2/ln(2). Full-block queries down to constants also satisfy (1): B is then the singleton empty label and the same Parseval/log-Sobolev derivation applies.

## 2. Adaptive summation and the complete terminals

Multiply (1) by rho_v and sum over internal nodes. Every nonroot internal deficit occurs once with each sign, since the reset child is exactly the next node. Leaves occur only as children. Define

    M=sum_internal rho_v r_v = expected number of queried physical bits,
    R=sum_internal rho_v R_v,
    S=-sum_leaves rho_l D_C(f_l),
    W=sum_internal rho_v W_v, G=sum_internal rho_v G_v.

Then the exact equality is

    D_C(f_root)+S+C R+W+G=kappa M.                (2)

Every complete leaf occurs with its original physical reach. W is a SUM of local divergences on possibly different spectral coordinate spaces. No common spectral path coupling or global path-KL identity is asserted. Neither descendants' stationarity nor their deficit maximality is needed. The construction assumes optimal representatives at the root and after each query; raw unoptimized representatives would introduce additional signed endpoint/reset corrections.

At a least-essential-dimension positive-C-deficit witness, any tree that queries at least once on every path has only proper children as terminals. Every terminal and every affine/character representative of it is a C-nonviolator, so S>=0. Thus

    C R+W+G+S=kappa M-D_root < kappa M.          (3)

For any other source the same inequality requires S>=0 as an explicit assumption; it does not follow from D_root>0. In particular a stopping leaf equal to the violating root has negative reserve. For D_root>0 and S>=0, M>=D_root/kappa; kappa>0 for every finite C,c. This is a necessary occupation condition, not a lower bound on useful funding.

## 3. Occupied rows along the tree

At node v choose any event E_v determined by Z_A. Let p_v=P_v(E_v), q_v=Q_v(E_v). For a nontrivial pattern event q_v is in (0,1). If 0<p_v<1, the exact chain rule reads

    W_v=d2(p_v||q_v)+p_v W_(v,1)+(1-p_v)W_(v,0),
    W_(v,1)=D_2(P_v|E_v || (Q_v|E_v) tensor P_(v,B)).

The exterior reference is the UNCONDITIONAL actual marginal P_(v,B). Replacing it by the conditional exterior marginal removes I(1_E;Z_B), an unpaid term. If p_v=0, define p_v W_(v,1)=0 without inventing an occupied law. If p_v=1, omit the complementary term. Set

    V=sum_internal rho_v p_v,
    U=sum_internal rho_v p_v W_(v,1),
    E=sum_internal rho_v[W_v-p_v W_(v,1)]>=0.

Substitute into (2):

    D_root+S+C R+G+E+U=kappa M.                  (4)

If S>=0 and D_root>0, U<kappa M. A supplied condition V>=eta*kappa*M>0 implies U/V<1/eta. This is an intensity-weighted mean over node events, not conditioning on a single transported root event. It gives no bound on each individual W_(v,1). Neither the root's rarity nor an absolute small KL certificate supplies this relative occupation hypothesis. Different node/block ceilings cannot be added as independently available original money.

## 4. Hypotheses, phases and old debits

The denominator kappa is positive, and division by V is used only when V>0. C>0 makes C R nonnegative. Without optimal node representatives equation (1) in this form is false; without complete terminals S need not be the actual reserve. Reset minima exist because all input/output operations are finite. Dummy coordinates cause no difficulty, but essential-dimension minimality is used when asserting S>=0.

If a nonlinear Boolean phase or any other entropy-changing normalization takes the optimized child h to an optimized h', retain its EXACT signed deficit change pi=D_C(h)-D_C(h'). A direct telescoping computation gives

    D_root+S+C R+W+G=kappa M+sum_phase_edges rho_edge*pi.    (5)

This statement is an accounting extension only; pi can have either sign. Its bound must come from the actual phase theorem on the actual source. An arbitrary phase can turn f into a constant and cannot be called a free affine reset. If a debit C*b, b>=0, has already been booked against a residual account B, only B-C*b is available for a new invoice. Equations (2)--(5) do not remove that booking or authorize another use of it. No phase estimate or original account is silently renewed.

## 5. Verification and the unpaid line

Checks that can fail: Walsh normalization; minimizing physical I rather than centered a; missing child reset savings; nonuniform reaches after adaptive branches; a negative complete terminal reserve; dropping the exterior dependence; p=0 or p=1; counting a new spectral space as a common path law. The exact checker uses direct integer Walsh sums, direct physical directional differences, exhaustive basis minima as a second check on the greedy reset, all labelled signs through n=3 and every deterministic stopping/query-coordinate policy for a fixed canonical reset rule. Entropies and KL values are exact prime-log vectors; signs are decided by integer products. This validates finite instances, not the all-dimensional induction. The induction itself is cancellation in (1) with actual reaches. A separate literal-leaf replay checks reaches without using the profile recursion.

FIRST UNSUPPORTED UNIVERSAL LINE: derive an ORIGINAL proper-pair choice with sufficient UNUSED funding from signed Booleanity, unused quotient rank and exact nonnegative complete-child reserves, keeping the actual phase price, all mixed rows and old debits. Equations (2)--(4) give an upper capacity shared by an entire continuation, not a lower source payment. The universal FEI constant improves by zero.
