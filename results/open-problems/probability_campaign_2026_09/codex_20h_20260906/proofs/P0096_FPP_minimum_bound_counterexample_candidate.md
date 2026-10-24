# P0096: continuous-law counterexample to the four-edge lower bound

Status update19:18Z2026-09-06: ALREADY REFUTED IN THE LITERATURE. Ahlberg1911.09949 (2019;published2020) explicitly settles this question. The proof below is retained as an author-checked rederivation; no novelty or original solved-open credit. The two-page primary paper was read in full; no independent review of this document occurred.

## Source and exact target

Auffinger, Damron and Hanson, *50 years of first-passage percolation*, arXiv:1511.03262, manuscript26September2016, Question12 (PDF p.33; repeated p.146), asks whether iid nonnegative edge passage times on Z^2 with F(0)=0 always satisfy

\[\mu(e_1)\geq \mathbb E\min(\tau_1,\tau_2,\tau_3,\tau_4).\]

E_4 denotes expectation of a minimum of four independent copies, not a fourth moment. The survey motivates this by Alm-Deijfen's simulation study, arXiv:1412.5924 (December2014). That paper describes an observed relation for selected distribution families. The target here is the survey's universal formulation, not a universal theorem attributed to the simulation authors.

Primary sources: https://arxiv.org/pdf/1511.03262 and https://arxiv.org/pdf/1412.5924. The two standard time-constant inputs below are stated in the latter paper, equations(2),(3), PDF p.3.

## Construction and lower bound

Independently for each lattice edge e, take eta_e in {0,1} with P(eta_e=0)=3/4 and an independent U_e uniform on [0,1]. For 0<epsilon<=1 put

\[\tau_e^{(\epsilon)}=\eta_e+\epsilon U_e.\]

The resulting iid law is bounded and absolutely continuous: its density is 3/(4epsilon) on (0,epsilon) and 1/(4epsilon) on (1,1+epsilon). It has no atoms, F_epsilon(0)=0, and infimum of support zero. Every moment exists.

For four independent copies, the event that all eta values equal1 has probability (1/4)^4=1/256. Their minimum is at least1 on this event, so

\[\mathbb E\min_{1\le i\le4}\tau_i^{(\epsilon)}\geq1/256.\tag{1}\]

## Time constants tend to zero

For bounded iid nonnegative edge weights the established subadditive formula is

\[\mu(e_1)=\inf_{n\ge1}\mathbb E T(0,ne_1)/n.\tag{2}\]

The established positivity criterion says mu(e_1)>0 iff F(0)<p_c(Z^2)=1/2. Hence the eta-only model has mu_0=0 because its zero mass is3/4. Each positive-epsilon model has mu_epsilon>0.

Fix n and couple all epsilon values with the same eta,U. Trivially T_epsilon(0,ne_1)>=T_0(0,ne_1). Given delta>0, choose a finite path gamma whose eta-cost is at most T_0(0,ne_1)+delta. Such a path exists by the definition of an infimum; a minimizing path is not assumed. Since U_e<=1,

\[T_\epsilon(0,ne_1)\le T_0(0,ne_1)+\delta+\epsilon|\gamma|.\]

First send epsilon to zero and then delta to zero. This proves T_epsilon(0,ne_1) tends almost surely to T_0(0,ne_1). The straight coordinate path gives 0<=T_epsilon(0,ne_1)<=2n. Dominated convergence therefore gives convergence of expectations.

For each fixed n, (2) now implies

\[\limsup_{\epsilon\downarrow0}\mu_\epsilon(e_1)
\leq \mathbb E T_0(0,ne_1)/n.\]

Take the infimum over n and use mu_0=0. Nonnegativity yields

\[\lim_{\epsilon\downarrow0}\mu_\epsilon(e_1)=0.\tag{3}\]

By(1),(3), every sufficiently small positive epsilon satisfies

\[0<\mu_\epsilon(e_1)<1/256\leq\mathbb E\min_{i\le4}\tau_i^{(\epsilon)}.\]

Thus this explicit family eventually reverses the proposed universal inequality. The proof gives existence of a small-enough parameter, not a numerical cutoff. All sufficiently large integers k give examples with epsilon=1/k.

## Adversarial checks and limits

The argument never interchanges an infinite-path minimization with a limit. It uses a finite approximate minimizer for each fixed n, then an upper bound valid for every n. No uniform bound on geodesic length is needed.

The limiting distribution has an atom at zero; the actual counterexample distributions do not. Their support has a gap, which the survey's stated hypotheses do not prohibit. Thus this is stronger than an atomic-law loophole.

A local entrance cost remains positive even when long travel can exploit a supercritical cheap-edge network; dividing a single entrance cost by distance explains the failure of the proposed bound. As a second literature lane, Cox-Kesten continuity of the time constant, cited in Alm-Deijfen, gives the same limiting conclusion for this bounded weakly convergent family. The direct proof above does not need that general continuity theorem.

Searches for Question12, Alm-Deijfen lower bounds, and minimum-of-four counterexamples did not locate a matching prior construction in the inspected results. This does not establish novelty. Before promotion, recheck source notation and standard theorem hypotheses, compare the original simulation discussion and later errata, and obtain independent review. No mathematical gap has been identified in the current argument, but neither independent review nor current open status is claimed.


## Later-literature correction and an explicit parameter

Ahlberg, Tertiles and the time constant, https://arxiv.org/pdf/1911.09949, Theorem1 and final paragraph, already gives counterexamples. The publication is Journal of Applied Probability57(2),407-408(2020), DOI10.1017/jpr.2020.9. The earlier search statement above records the preliminary search only and is superseded by this finding.

For our family, its two-thirds quantile is8epsilon/9. Ahlberg proves mu<=2t_(2/3), so epsilon=1/1024 gives mu<=1/576<1/256<=E minfour. This is an explicit atomless bounded example derived from an established theorem. The continuity argument above remains a separate qualitative derivation. No original solution is claimed.
