# Influence-priced smoothing, and the unpaid initial entropy

All logs are base2. For EVERY Boolean g on any finite uniform cube, write P_g for its squared Fourier law, J=I(g), and u for the uniform law on frequency subsets. If J>0 put epsilon=min(1/2,J/4) and q_g=(1-epsilon)P_g+epsilon*u. If J=0 put q_g=P_g. Then

0<=K_g=KL(P_g||q_g)<=J,
H(g)<=CE(P_g,q_g)<=H(g)+I(g).

Proof: q_g>=(1-epsilon)P_g, so K_g<=-log2(1-epsilon). For0<J<=2, integrate1/(1-t)<=2 on[0,epsilon], obtaining K_g<=2epsilon/ln2<J because ln2>1/2. The latter follows by integrating1/t>1/2 on[1,2]. For J>=2, K_g<=1<=J. For J0 the assertion is exact. Positive J gives a full-support reference; constants use their exact point law. No fixed positive smoothing floor is admitted at constants.

## Persistent first-mark conversion through arbitrary adaptive DATA histories

Let a finite physical restriction tree query previously unqueried coordinates of arbitrary g, and stop at an arbitrary adapted frontier. Let F be an event first declared on a prefix-free set of tree nodes and then retained on descendants: a path marks at most once. Let q_old,h be ANY already supplied reference, finite on the support of P_h. On marked histories prescribe the actual CURRENT influence-tuned q_h above, including after each subsequent data query. Off marked histories keep q_old. Both full KLs remain in

D_h=K_new,h-K_old,h=CE_new,h-CE_old,h<=I(g_h).

At first marking charge D_h. On each realized later edge charge D_child-D_parent; these realized differences telescope PATHWISE to terminal D, with no clipping and no fresh descendant allowance. Their CONDITIONAL EXPECTATIONS are E[D_child|h]-D_h; those expected node charges telescope only AFTER reach weighting. A conditional average increment is not claimed to telescope on an individual realized path. Therefore

E[1_F D_terminal]<=E[1_F I(g_terminal)]<=I(g).

The last inequality is an actual physical influence ledger: I(g_h)=Inf_i(g_h)+(I(g_h|i0)+I(g_h|i1))/2. Multiplying by reaches and summing gives E I(terminal)=I(g)-sum_nodes reach*Inf_query. The marked part is no greater because influence is nonnegative. Thus one ORIGINAL extra coefficient of I(g) pays every such terminal conversion from any supplied OLD reference. This is a universal CONVERSION theorem. It does not supply the old cross-entropy or create unused credit inside an already exhausted old4I account. A purported unchanged4I extension would still have to exhibit its unused original margin.

## Fixed half-smoothing cannot be the universal initial supplier

This corroborates the fixed-mixture obstruction already noted by A029 on the current BOARD; it is not claimed as a new general no-go. For the actual Boolean point-defect family g_n=1 except at one vertex, delta=2^-n, n>=3,

P(empty)=(1-2delta)^2>=9/16; I(g_n)=2n delta.

For q_half=(P+u)/2, q_half(empty)<=(1+delta)/2<=9/16. Hence CE(P,q_half)>=(9/16)log2(16/9)>9/32, since(16/9)^2>2. Thus CE(P,q_half)/I(g_n)>9*2^n/(64n), unbounded. This is an initial-reference counterexample, NOT an FEI counterexample. In fact its entropy/influence is bounded; no such conclusion about FEI follows from the inflated reference cost.

The influence-tuned rule removes this artificial constant floor: K<=I even on this low-influence family. Its initial price remains H+K, so it does not solve the source problem.

## Exact universal bridge and first unsupported line

Existence of an absolute K with CE(P_g,q_g)<=K I(g) for EVERY Boolean g is EQUIVALENT to full FEI, with constants shifting by at most1: CE>=H gives FEI(K); FEI(C) gives CE<=H+I<=(C+1)I. This is an equivalence, not a new sufficient hypothesis asserted true. The first unsupported universal line is H(g)<=C I(g), or a NONCIRCULAR structural construction paying the equivalent initial CE. Influence-priced reset overhead alone cannot prove it. The new result prices conversion without a unit floor and specifies exactly what initial payment is still missing.

Compared with stage21, its bound>153/256 is neither changed nor generalized for free: that was a particular original4I account. This stage supplies a distinct generic one-additional-I conversion tariff. The original stage21 theorem and negative quarter-branch remain untouched. Independent-person review is pending.
