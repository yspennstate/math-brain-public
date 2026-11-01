# Scoped check of the recent manuscript's duration bridge

Primary source: September 23, 2026, Directional transience implies ballisticity, PDF pp. 11-12, Proposition 2.5, and its strategy on p. 4. The local source is sources/recent_ballisticity.pdf. This is not an audit of the entire manuscript or its formalization.

The manuscript explicitly assumes its equation (5) at Proposition 2.5: for one fixed beta in (0,1), P_env(a_N < N^(-beta)) decays faster than every power of N, where a_N=P_{0,omega}(T_N<T_{-1}) for a coordinate height. It also uses spatial confinement and a width-tail argument to turn this into a time moment. These inputs have not been independently established here. In particular the hard crossing estimate occupies later sections; the source claim is not an accepted proof receipt in this packet.

The local time accounting does not make the geometric-attempt-count mistake. On its good environment event, a visit to x has probability at least h_N=kappa N^(-beta) of being the last visit before strip exit: step to x+e_1 and reach N levels higher before dropping back to the new layer. This excludes another visit to x. A finite confined set of at most C N^(2d-1) sites then turns visit counts into elapsed time.

An independent version of that counting lemma is as follows. Let T be a stopping time and B a deterministic finite set of M>=1 states. Assume that at each kth visit to any x in B before T, conditional on the visit history, the probability of no further visit to x before T is at least h, where 0<h<1. The next-visit events can then be iterated by the tower property, giving P(K_x>=m)<=(1-h)^(m-1), m>=1, for the number K_x of visits to x before T. Each conditional step is at the actual visit's stopping-time sigma-field. Independence of visits is unnecessary. The case h=1 follows separately because no site is revisited before T.

For an integer t>=M, on the event that X_0,...,X_{T-1} all lie in B and T>t, at least one site has at least floor(t/M) visits. The union bound therefore gives

P(T>t, pre-exit path confined to B) <= M (1-h)^(floor(t/M)-1).

With M<=C N^v, h>=kappa N^(-beta), and t=N^A, any fixed A>v+beta makes the right side decay faster than every power of N. Add the probability of failed confinement and the bad-environment event. This proves a conditional duration-tail reduction, assuming those events have the necessary tails. It supplies the cost estimate absent from a bare geometric attempt-count argument.

For regeneration, one must also bound the chance that the first word's width exceeds N and justify the precise no-backtracking conditioning. Proposition 2.5 states these as separate steps. The present audit neither supplies equation (5) nor certifies those earlier spatial/renewal steps.

The primary comparator configuration names solution module OAI.Probability.Ballisticity.Main and permits propext, Quot.sound and Classical.choice. The actual Main.lean supplies the top-level proof by invoking directional_transience_implies_ballisticity_unit. It is separate from the challenge comparator's admitted template. No transitive axiom report, successful comparator run or independent check of the imported bridge has been obtained here. Therefore there is no completed formal-check receipt.

NEXT: Check the actual super-polynomial crossing estimate, or prove the quantitative slow-region classification premise in PAIRED_AUDIT.md; neither follows from the finite-box lemmas alone.
