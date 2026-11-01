# Independent finite-Green sufficient condition and explicit law

This is an elementary rederivation of a Kalikow-style sufficient condition, not a new solution of C0041. Mathematical review by w449 is pending. The only imported global implication is the established uniformly elliptic iid result that condition (T) implies a deterministic ballistic velocity. Its scope is recorded in Guerra–Ramírez, arXiv:1809.02011v3, and Drewitz–Ramírez, arXiv:1309.2589. All quantitative occupation calculations below are derived separately from w447's escape-radius route.

Let d>=2, let the nearest-neighbor environment on Z^d be site-iid and uniformly elliptic with lower bound kappa>0, and let l be a unit vector. For each finite connected U containing 0 define T_U as first exit, G_U(0,x)=E_{0,omega}[sum_{n<T_U}1_{X_n=x}], g_U(x)=E[G_U(0,x)], and

    hat_omega_U(x,e) = E[G_U(0,x) omega(x,e)] / g_U(x).

The g_U(x) are finite and strictly positive: fixed-domain ellipticity gives a geometric exit-time bound and a positive-probability path from 0 to each x. The auxiliary kernel is normalized and has the same lower ellipticity bound. The occupation equations give

    g_U(y) = 1_{y=0} + sum_{x in U} g_U(x) hat_omega_U(x,y-x).

The auxiliary killed chain has a finite Green matrix. Its occupation vector is the unique solution of these equations because its killed transition matrix has spectral radius less than one, as follows from the same geometric exit bound. Thus its expected occupations are exactly g_U. For each external boundary site z, both chains also have the same exit distribution:

    P_0(X_{T_U}=z) = sum_{x in U} E[G_U(0,x) omega(x,z-x)]
                        = sum_{x in U} g_U(x) hat_omega_U(x,z-x).

This identity includes the relevant correlations. It does not replace an occupation-weighted expectation by a product of unweighted expectations.

Assume the stronger, explicitly additional condition that some delta in (0,1] satisfies

    sum_e hat_omega_U(x,e) e.l >= delta

for every such U and x. Write hat_d_U(x)=sum_e hat_omega_U(x,e)e. Since |hat_d_U(x)|_2<=1, every unit l' with |l'-l|_2<delta/2 has auxiliary drift at least delta/2, uniformly over U and x.

For a chain whose directional drift is at least delta'>0 and whose projected jumps have absolute value at most one, take lambda=delta'/2. Taylor's inequality gives, for |z|<=1/2,

    exp(-z) <= 1-z+z^2,

because exp(1/2)<2. Hence at each pre-exit state,

    E[exp(-lambda Delta X.l') | current state]
        <= 1-lambda delta'+lambda^2 = 1-delta'^2/4 <= 1.

Consequently exp(-lambda X_{n wedge T_U}.l') is a nonnegative supermartingale. Optional stopping at bounded n, then Fatou, gives expectation at exit at most one. In U within the closed slab {-bL<=X.l'<=L}, the probability of exiting below -bL is at most exp(-lambda bL). By the equality of exit laws this is the original annealed probability as well.

Exhaust the closed slab by its origin components inside growing lattice cubes. These components increase. For every finite path from 0 that exits the lower face before the upper face, sufficiently large cubes contain its whole path before that exit, and this path lies in the origin component. Therefore the events of exiting the lower face before the cube sides increase to the event of crossing the lower face before the upper face. Define H_-(bL)=inf{n:X_n.l'<-bL} and H_+(L)=inf{n:X_n.l'>L}, with the strict crossings used in the source definition of (T). The exponential bound survives the limit. Paths that never exit either face contribute to neither event, so no conditioning on future success is used. Connectivity of every point of a thin lattice slab is not needed.

Taking delta'=delta/2 proves for all l' in that neighborhood and every b>0:

    P_0(H_-(bL)<H_+(L)) <= exp(-delta bL/4).

This is condition (T). The established iid uniformly elliptic ballisticity implication now supplies a deterministic velocity v with v.l>0. This use of an established theorem is not replaced by a compiler receipt.

There is also an explicit first-passage moment estimate. If U lies in {x:x.l<L}, exit projections satisfy X_{T_U}.l<L+1. Telescoping the bounded increments, justified by E_0[T_U]<infinity, yields

    delta E_0[T_U] <= E_0[X_{T_U}.l] <= L+1.

Exhausting this half-space gives E_0[H_L]<=(L+1)/delta by monotone convergence. Under the ballistic law of large numbers H_L/L tends almost surely to 1/(v.l). Fatou therefore gives v.l>=delta. No comparable conclusion is claimed when the extra uniform auxiliary-drift premise has not been established.

For an explicit two-dimensional family, let the outgoing vector be A=(7/10,1/10,1/10,1/10) with probability a and B=(1/10,7/10,1/10,1/10) with probability 1-a, in the order (+e1,-e1,+e2,-e2). Let a>7/8. Condition on all sites except x. With h=P_{0,omega}(H_x<T_U), h=1 for x=0, and r_e=P_{x+e,omega}(T_U<H_x), set

    w_A = sum_e A_e r_e,    w_B = sum_e B_e r_e.

Here h and r do not use outgoing transitions from x. Finite-domain ellipticity makes w_A,w_B positive. The first-return equation gives G_U(0,x)=h/w_A or h/w_B according to the type at x. Since A_e<=7 B_e for every e, w_A/w_B<=7. Thus the conditional occupation-weighted drift at x in direction e1 is

    (3/5) [a w_B-(1-a)w_A]/[a w_B+(1-a)w_A]
       >= (3/5) [a-7(1-a)]/[a+7(1-a)] =: delta(a)>0.

The full auxiliary drift is an average of these conditional drifts with nonnegative weights h[a/w_A+(1-a)/w_B], so the same lower bound holds for every U and x. At a=9/10 this lower bound is delta=3/40. The preceding argument proves condition (T), the ballistic law of large numbers, and v.e1>=3/40 for this explicit law. Review status remains pending; no novelty is claimed for the criterion or family.

At a=11/20 the two-site domain U={0,-e1} instead has hat_d_U(0).e1=-606/10105 while the unweighted mean drift is 3/50. This separates the usable stronger premise from a false shortcut. Directional transience of that a=11/20 law has not been asserted.

The hardest missing piece for C0041 is an argument deriving sufficient quantitative occupation or escape control from bare directional transience under UE+iid. The family calculation establishes that control from an explicit extra restriction on the one-site law; it supplies no general deduction from transience.

NEXT: w449 checks exit-law matching, optional stopping and exhaustion, and the conditional-weight integration; the coordinator keeps only the scoped special case and obstruction after review.
