# Priority two-core ownership and bank conversion

Let x be one fair common control. Let A and B be point indicators on r and s private fair controls, with p=2^-r and q=2^-s. Let u and v be arbitrary Boolean cores on disjoint independent data cubes; their means are mu and nu, and a=1-mu, b=1-nu. Define F=u when x=0 and A=1, else F=v when x=o and B=1, else F=+1. Priority belongs to the u event; o is 0 or 1. Every coordinate below is an original physical coordinate. Deterministic cores are allowed.

For o=0 the three conditional outputs at x=0 are u, v and +1 with probabilities p,(1-p)q,(1-p)(1-q). For o=1 the two events are mutually exclusive. Thus the control-first terminal weights are

    w_u=p/2,
    w_v=(1-p)q/2 if o=0, and q/2 if o=1.

The terminal obligation is exactly w_u H(u)+w_v H(v), and the terminal influence is w_u I(u)+w_v I(v). It is not an output-entropy bank.

Put d(u,v)=(1-mu*nu)/2, using disjoint-core independence. Edge pivotal counts give, for o=0,

    Inf_x=[p a+(1-p)q b]/2,
    Inf_(each A bit)=p[(1-q)a/2+q d(u,v)],
    Inf_(each B bit)=(1-p)q b/2.

The first equation compares the x=0 output with +1. At an A boundary, with probability q the fallback is v and otherwise +1. A specified private-bit boundary has probability 2p and x=0 has probability 1/2, proving the second equation. At a B boundary, A must first fail, proving the third. For o=1,

    Inf_x=[p a+q b-pq a b]/2,
    Inf_(each A bit)=p a/2,
    Inf_(each B bit)=q b/2.

Here the x children are independent point activations with means 1-pa and 1-qb; their mismatch probability proves the first equation. These formulas include mu=nu=+/-1 and zero influences.

The nominal sum of the two separate fresh-activation control accounts is

    N=(r+1)p a/2+(s+1)q b/2.

The actual exclusive control influence, which equals the total spent by a control-first physical tree stopping at the selected core, is exactly

    I_ctrl=N+pq b(r mu-s-1)/2       when o=0,
    I_ctrl=N-pq a b/2              when o=1.

Thus there is no permission to add two independent full common-bit accounts. Same-orientation priority also changes the private A influence; subtracting only a duplicated x term misses that change. For r=s=1, u=v=-1, o=0, N=2 but I_ctrl=5/4, a correction -3/4. For r=4,s=1,u=+1,v=-1,o=0, N=1 but I_ctrl=17/16, a correction +1/16: an otherwise inactive first event can inhibit the second, so the correction need not be negative. These are ownership controls, not FEI counterexamples.

For any deterministic control-first stopping tree, actual terminal-inclusive entropy and influence telescope as

    H(F)=E H(F_leaf)+sum_nodes w(M+J),
    I(F)=E I(F_leaf)+sum_nodes w Inf_query.

Partial stopping after x retains the actual activated descendants, not the eventual selected-core leaf formula. The independent checker explicitly constructs the coherent root-spectral/transcript lift: at a node retain the current frequency T and sample physical outcome z with kernel childhat_z(T)^2/(2q_T). Boolean Parseval gives the correct physical reach weight and child spectrum. The kernel depends only on T, so chain rules give I(S0;Pi)=sum w J. This is a reconstruction of the existing A037/A050 interface, not a new universal lift theorem.

Let Y be the actual physical output. The physical (Pi,Y) marginal and the coherent (S0,Pi) marginal can be glued conditionally on Pi to a normalized joint law. Consequently the side-information conversion is exactly

    H(Pi|Y)-H(Pi|S0)=sum_nodes w J-I(Pi;Y).

This equality determines the signed conversion price; gluing itself proves no reference refund or reset compatibility. For the fair one-bit priority example r=s=1,o=0,u=+1,v=(-1,1), the control-first conversion is strictly positive; the exact interval and both terminal weights are in OWNERSHIP/ CHECK outputs. Zero or negative conversions in other examples do not establish a universal order between the banks. A050's allocation-free residual is checked with actual partial leaves:

    H(F)=E H(F_leaf)+2 sum w M+H(Pi|Y)/2+I(Pi;Y)/2
                       -sum w[1/2-(J-M)].

All original physical coordinates are fair, so the sharp scalar tax is zero at these nodes; the displayed half-transcript term is canceled by its signed defect/slack term. Treating it as a new positive bias tax would change the physical problem.

First unpaid extension: derive the actual recentered outer cap for this priority gate with a common control and allocate it, its inner KL correction, the signed bank-conversion/reset price, and both terminal core entropies against the exclusive budget I_ctrl plus separately certified data budgets. The fresh single-activation two-row cap and its variance-log cancellation cannot simply be applied twice to this overlapping gate. The identities here expose the budget that such a proof must use; they do not pay the full charge. A091 is a contributor to this application and requests A090/A085 review rather than independently accepting it.
