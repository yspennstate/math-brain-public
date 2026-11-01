# F0127: verified literature answer

Date: 2026-10-11.

## Exact statement and scope

Aldous, *Interacting particle systems as stochastic social dynamics*, Bernoulli 19(4) (2013), 1122–1149, DOI 10.3150/12-BEJSP04, arXiv:1309.6766. Section 5.5 starts on PDF page 15; Open Problem 2 itself is on PDF page 16.

Let V_n have n vertices, symmetric nonnegative off-diagonal rates nu_ij with connected support and sum_{j != i} nu_ij=1. Section 5 walkers have generator Q_ij=nu_ij/2, Q_ii=-1/2. Stationarity is uniform. Let M_ij be the first meeting time of independent Q-walks from i,j, including M_ii=0. Set m_n=tau_meet=n^{-2} sum_{i,j} E M_ij. Start one coalescing walker at every vertex and call the full coalescence time C_n.

Assumption (5.2) is, for every epsilon>0,

    n^{-2} |{(i,j): E M_ij not in ((1-epsilon)m_n,(1+epsilon)m_n)}| -> 0.

The exact question is: "Assuming (5.2), under what further conditions can one prove" E C_n ~ 2m_n? The source says (5.2) implies TV mixing time o(m_n), but presents its fixed-m argument as likely, not as a proved theorem in this article. Standardization (2.2) is a convention for constant-row-sum geometries, not a restriction on all geometries in the source; this answer respects the user's standardized subclass.

## Literature answer

A sufficient additional condition is:

    Q_n is transitive, and t_rel(Q_n)/m_n -> 0.

Here permutations preserving all transition rates must act transitively; transitivity of the unweighted support alone is insufficient. Relaxation time refers to the continuous-time generator, not a discrete-time absolute spectral gap.

Then E C_n/m_n -> 2. More strongly, Law(C_n/m_n) converges in L1 Wasserstein distance to Law(S), where S=sum_{k=2}^infinity Z_k and the Z_k are independent exponentials of rates binom(k,2).

This follows from Jonathan Hermon (2022), *Some inequalities for reversible Markov chains and branching random walks via spectral optimization*, Annales de l'Institut Henri Poincare, Probabilites et Statistiques 58(3), 1650–1668, DOI 10.1214/21-AIHP1208, arXiv:1908.08525, Theorem 1; and Roberto Imbuzeiro Oliveira (2013), *Mean field conditions for coalescing random walks*, Annals of Probability 41(5), 3420–3461, DOI 10.1214/12-AOP813, arXiv:1109.5684, Theorem 1.1.

Oliveira is already Aldous's reference [42], not a post-source result. The post-source advance is Hermon's relaxation-to-mixing bound. Hermon's introduction explicitly explains the resulting resolution of the Aldous–Fill transitive spectral criterion. These are sufficient conditions, not a characterization. Under these stronger hypotheses the conclusion does not require (5.2), so it also holds when (5.2) is imposed.

## Complete derivation from the cited theorems

All times below are for Q_n. Write H_t=exp(tQ_n), let a_2,...,a_n be the positive eigenvalues of -Q_n, and put K=sum_{r=2}^n 1/a_r. Symmetry and transitivity give, for every vertex o,

    H_t(o,o)=Tr(H_t)/n=(1+sum_{r=2}^n exp(-a_r t))/n.

First establish E_pi T_o=K and m_n=K/2, with pi uniform. For the hitting time T_o from stationarity, put F(s)=E_pi exp(-sT_o), s>0. The strong Markov property gives

    1/n = integral_[0,t] H_{t-u}(o,o) P_pi(T_o in du).

This includes mass at zero. Taking Laplace transforms by Tonelli,

    1/(ns)=F(s) R(s),
    R(s)=1/(ns)+(1/n)sum_{r=2}^n 1/(s+a_r),
    F(s)=[1+s sum_{r=2}^n 1/(s+a_r)]^{-1}.

The hitting time has finite mean on a finite irreducible chain; alternatively monotone convergence applied to (1-exp(-sT_o))/s identifies the mean directly. Hence E_pi T_o=K. By transitivity, max_o E_pi T_o=K.

For an independent pair started at (o,o), the probability of being on the diagonal at time t is sum_z H_t(o,z)^2=H_{2t}(o,o), by symmetry and the semigroup identity. For a stationary pair this probability is 1/n. Let M be its first diagonal hitting time, G(s)=E exp(-sM). Its location at M may be random, but transitivity makes the diagonal return probability independent of that location. The same renewal argument gives

    1/(ns)=G(s)[1/(ns)+(1/n)sum_{r=2}^n 1/(s+2a_r)],
    G(s)=[1+s sum_{r=2}^n 1/(s+2a_r)]^{-1}.

Therefore m_n=E M=(1/2)sum_{r=2}^n 1/a_r=K/2. The pair chain is finite irreducible, so its diagonal hitting time is integrable. Both identities include stationary starts already at their target.

Hermon's Theorem 1, at epsilon=1/2, gives

    t_mix^(infinity)(1/2)
       <= t_rel max{1, log[max_x E_pi T_x / ((1/2)t_rel)]}.

His rate-one generator P-I includes our Q=(nu-I)/2 by taking P=(I+nu)/2. No time units change. Substituting max_x E_pi T_x=2m_n gives

    t_mix^(infinity)(1/2)/m_n
       <= r_n max{1, log(4/r_n)},  r_n=t_rel/m_n.

This tends to zero when r_n->0: r log(4/r)=r log 4+r log(1/r), and log u/u->0 as u->infinity, for example because log u <=2 sqrt(u) for u>=1. Relative-density error <=1/2 implies TV distance <=1/4, by taking half its pi-weighted sum. Thus Oliveira's TV mixing time is also o(m_n).

Oliveira's Theorem 1.1 concerns finite irreducible reversible transitive generators, full occupancy initially, and gives, with rho_n=t_mix/m_n,

    d_W(Law(C_n/m_n),Law(S))
       = O((rho_n log(1/rho_n))^(1/6)) -> 0.

Thus the early reduction from n particles is covered by the published theorem; no unproved Stage 2 is inserted. Monotone convergence and telescoping give

    E S=sum_{k=2}^infinity 2/[k(k-1)]
       =lim_{N->infinity} 2(1-1/N)=2.

For every coupling U,V, |EU-EV|<=E|U-V|. Taking the infimum gives |EU-EV|<=d_W(Law(U),Law(V)); consequently E C_n/m_n->2. This justifies convergence of means, not only weak convergence.

## Other sufficient conditions already in Oliveira

Theorem 1.1 directly gives the conclusion under transitivity and t_mix=o(m_n).

Theorem 1.2 covers nontransitive chains. Define alpha_n=(1+q_max t_mix)pi_max. If alpha_n->0 and alpha_n log(1/alpha_n)(log n)^4->0, the same Wasserstein and mean limits hold. In the present standardized half-speed symmetric setting, q_max=1/2 and pi_max=1/n. A convenient stronger sufficient condition is t_mix=o(n/(log n)^5): eventually 1/n<=alpha_n<1, so log(1/alpha_n)<=log n, and alpha_n(log n)^5=(1+t_mix/2)(log n)^5/n->0. This condition was known at the source's publication and is not a later resolution.

## Referee audit

- Source statement, symmetry, standardization and half-speed convention checked against the primary PDF.
- Hermon's exact Theorem 1 and coalescence discussion read. His proposed broader nontransitive extension is a belief, not a theorem used here.
- Oliveira's Theorems 1.1 and 1.2 explicitly control L1 Wasserstein distance and means. Distributional convergence alone would not suffice.
- All quantities use the same generator. Multiplying its speed by c divides meeting, mixing, relaxation and coalescence times by c and preserves the relevant ratios.
- Independent uniform starts include equal starting vertices. On the half-speed complete graph, distinct-start meeting hazard is 1/(n-1), so m_n=(n-1)^2/n. With k clusters the merger rate is binom(k,2)/(n-1), so E C_n=2(n-1)^2/n. The ratio is exactly 2 for n>=2. Exact rational checks for n=2,...,50 are saved in normalization_checks.txt.
- The earlier intake Stage 1 sketch is not accepted as a proof under (5.2) alone: meeting hazards, multiple-collision errors and survivor-location estimates require justification. None is assumed here.
- No Lean certificate or independent proof of the two published theorems is claimed. This is a literature resolution with an explicit proof of applicability; the user's stop-after-literature rule applies.

## Precise limitation

This record does not prove that (5.2) alone suffices for arbitrary nontransitive weighted geometries, and does not give necessary-and-sufficient conditions. OpenAlex and Semantic Scholar returned HTTP 429; exhaustive literature coverage is not claimed. The SOLVED_IN_LITERATURE verdict answers the stated request for further sufficient conditions, not an unrestricted conjecture under (5.2) alone.
