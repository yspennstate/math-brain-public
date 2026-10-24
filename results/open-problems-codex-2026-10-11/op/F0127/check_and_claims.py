from pathlib import Path
from fractions import Fraction
import json
checks=[]
for n in range(2,51):
 m=Fraction((n-1)**2,n)
 c=sum((Fraction(2*(n-1),k*(k-1)) for k in range(2,n+1)),Fraction())
 assert c==2*m
 checks.append(f'n={n}: stationary_mean_meeting={m}, mean_coalescence={c}, ratio={c/m}')
Path('normalization_checks.txt').write_text('\n'.join(checks)+'\n',encoding='utf-8')
claims=[('For irreducible symmetric rate-transitive standardized chains Q_n=nu_n/2, t_rel=o(tau_meet) implies E T_coal/tau_meet -> 2.','proved_special_case','Complete derivation from the cited theorems','No assertion that (5.2) alone suffices for nontransitive geometries.',['Hermon 2022 Theorem 1','Oliveira 2013 Theorem 1.1','stationary hitting and meeting identities derived','Wasserstein implies convergence of means']),('For a finite symmetric transitive continuous-time chain, stationary mean meeting time is half the sum of reciprocals of positive eigenvalues of -Q, and E_pi T_o is the full sum.','proved','Complete derivation from the cited theorems','None under stated hypotheses.',['strong Markov renewal and Laplace transforms','stationary diagonal mass included']),('For standardized half-speed symmetric chains, t_mix=o(n/(log n)^5) suffices for E T_coal/tau_meet -> 2 without transitivity.','proved_special_case','Other sufficient conditions already in Oliveira','Sufficient, not necessary conditions.',['Oliveira Theorem 1.2','q_max=1/2 and pi_max=1/n','explicit alpha bound']),('For the half-speed complete graph n>=2, E T_coal=2(n-1)^2/n and tau_meet=(n-1)^2/n.','proved_special_case','Referee audit','None for complete graphs.',['pair hazard','cluster-count holding times','exact Fraction checks n=2,...,50'])]
with open('CLAIMS.jsonl','w',encoding='utf-8') as f:
 for claim,status,loc,gap,checks in claims:
  f.write(json.dumps(dict(problem_id='F0127',claim=claim,status=status,proof_location='ATTEMPT.md: '+loc,remaining_gap=gap,checks=checks),ensure_ascii=False)+'\n')
print('Saved 49 exact checks and four claims.')
