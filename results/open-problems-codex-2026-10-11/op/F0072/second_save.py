from pathlib import Path
import json
R=Path(__file__).resolve().parent
claims=[
('For grounded finite unit-edge continuous SOS, positive-domain partitions obey z(S)=sum_v_in_S z(S minus {v})/cut(S). Partial-wall partitions, contacts and first moments have exact formulas R2-R5.','proved','Exact finite-graph reduction','The exponential-size formulas do not yet establish wall-edge asymptotics.','Minimum-coordinate split, cross-sign factorization; exact rational tests in coarea_checks.json.'),
('z is log-supermodular; sign-set weights w(S)=z(S)z(V minus S) satisfy the attractive Boolean lattice condition.','proved','A new structural consequence','No quantitative sign-buffer enlargement bound.','Increasing one-vertex ratios, positive-domain monotonicity and telescoping; exhaustive exact check on all subset pairs of the three-site graph.'),
('The auxiliary universal reflected-contact inequality r_union>=r_half^2 is false on the three-site zero-boundary Z^2 domain: corrected ratios are 3/4 and 33/38.','counterexample','Hostile test','Counterexample to an attempted lemma, NOT to F0072; alternative exponents remain unproved.','Corrected independent leaf integration and exact rational recursion agree; 4332<4356; corrected Lean check reported separately.'),
('A power-sized positive sign buffer with failure probability tending to zero uniformly at all wall sites implies uniform logarithmic wall-edge repulsion by inequality SB.','proved','A precise sign-buffer criterion','GAP-SB has not been proved.','Exact sign-sector factorization; conditional full-wall stochastic comparison; central bound; r=M^alpha, a<alpha/(2d).'),
('For a wall B_M buffered by N-M>=delta M, some alpha>0 yields a positive sign buffer of radius comparable to M^alpha at every wall site with failure probability tending to zero uniformly.','conjecture','GAP-SB','Need Z(A union D)/Z(A) -> 1 uniformly, not just Boolean lattice attractiveness.','Small exact computations are not an asymptotic proof.'),
('The SOS energy under any homogeneous finite hard-wall cone has Gamma(n,rate=1) distribution.','proved','Exact energy distribution','Global energy equipartition does not bound individual boundary contacts.','Exact scaling of the partition function and gamma Laplace transform.'),
]
existing=[json.loads(x) for x in (R/'CLAIMS.jsonl').read_text(encoding='utf8').splitlines() if x.strip()]
with (R/'CLAIMS.jsonl').open('a',encoding='utf8') as stream:
 for claim,status,section,gap,checks in claims:
  if any(x['claim']==claim for x in existing):continue
  stream.write(json.dumps({'problem_id':'F0072','claim':claim,'status':status,'proof_location':'SECOND_ATTEMPT.md, '+section,'remaining_gap':gap,'checks':checks},ensure_ascii=False)+'\n')
s=(R/'SECOND_ATTEMPT.md').read_text(encoding='utf8')
print('Structural explanation present:', 'root-separator' in s or 'general explanation on graphs separated' in s)
print('Temperature check present:', '## Temperature check' in s)
data=json.loads((R/'coarea_checks.json').read_text(encoding='utf8'))
print('Exact experiment cases:',[x['name'] for x in data])
for x in data:
 if x['name']=='3x3_reflected_half_boxes':print(json.dumps({k:v for k,v in x.items() if k!='rows'}))
 if x['name']=='4x4_buffered_central_2x2_wall':print(json.dumps(x))
p=R/'gap_recall_2.txt'
if p.exists():print(p.read_text(encoding='utf8')[:10000])
print('Claim records:',len([x for x in (R/'CLAIMS.jsonl').read_text(encoding='utf8').splitlines() if x.strip()]))
