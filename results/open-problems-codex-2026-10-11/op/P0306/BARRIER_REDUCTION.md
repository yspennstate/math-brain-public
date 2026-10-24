# Quantitative requirement for the second new approach

11 October 2026. This is a conditional reduction, not a proved LQG barrier estimate.

The second proposed approach in SECOND_ATTEMPT.md uses annular merger barriers under the Gaussian-tilted law from ATTEMPT.md. Here is the exact finite probabilistic step needed to turn such barriers into an arm bound without making an independence assumption.

Fix s>1 and dyadic r=2^(-n). Work under the corresponding tilted probability measure P_{r,s}. Let A_r be the two-arm hit event and Z_r the nonnegative normalized diameter. Suppose there is a filtration F_0 subset ... subset F_n and events G_j in F_j such that

1. A_r is a subset of intersection_{j=1}^n G_j;
2. P_{r,s}(G_j | F_{j-1}) <= rho_s < 1 almost surely;
3. E_{r,s}[Z_r^s | F_n] <= M_s almost surely.

All constants must be uniform in r and in the relevant interval locations. Events G_j represent survival without a forced merger across successive half-annuli. These hypotheses are requirements, not properties established for the LQG field here.

Let B_j=intersection_{i=1}^j G_i. Because B_{j-1} belongs to F_{j-1}, the tower property gives

P(B_j)=E[1_{B_{j-1}} E[1_{G_j}|F_{j-1}]] <= rho_s P(B_{j-1}).

Induction starting with B_0 the whole space gives P(B_n)<=rho_s^n. The inclusion A_r subset B_n and nonnegativity then yield

E[1_{A_r}Z_r^s] <= E[1_{B_n}Z_r^s]
 = E[1_{B_n}E[Z_r^s|F_n]] <= M_s rho_s^n
 = M_s r^{q_s},  q_s=-log(rho_s)/log(2).

The weighted covering reduction in ATTEMPT.md would apply if

q_s+xi Q s-xi^2 s^2 > 1

for s arbitrarily close to one from above. A uniform family with q_s tending to q_1>1-xi Q+xi^2 would suffice by continuity. At gamma=sqrt(8/3), d_gamma=4, this threshold is q_1>1/3, equivalently rho_1<2^(-1/3). Thus a strictly uniform tilted merger probability exceeding 1-2^(-1/3), approximately 0.2063, together with the conditional diameter bound would suffice near s=1 in this reduction.

Referee checks: the tower-property iteration uses conditional probability bounds, not independent annuli. The weighted estimate uses hypothesis 3; an ordinary diameter moment bound does not supply it. The law varies with r and s, so a barrier theorem only under the original untilted law cannot be substituted. The required geometric event inclusion is exact, and must accommodate boundary arms and interval locations. No verified source or brain card supplies all three hypotheses with the stated quantitative threshold. This is another precise remaining gap.

An alternative avoids the very strong pointwise conditional bound in hypothesis 3. If 0<E_{r,s}[Z_r^s]<=M_s, define the diameter-size-biased law nu_{r,s} by density Z_r^s/E_{r,s}[Z_r^s] relative to P_{r,s}. The exact identity

E_{r,s}[1_{A_r}Z_r^s]=E_{r,s}[Z_r^s] nu_{r,s}(A_r)

shows that hypotheses 1 and 2 imposed under nu_{r,s}, together with the ordinary uniform moment bound under P_{r,s}, give the same conclusion by the same induction. If the moment is zero the conclusion is immediate without defining nu. This formulation changes the missing barrier estimate to a condition under a diameter-size-biased, already Gaussian-tilted law. It is not legitimate to transfer an untilted barrier probability to this law without proof.
