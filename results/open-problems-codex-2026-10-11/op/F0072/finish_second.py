from pathlib import Path
import json,hashlib
R=Path(__file__).resolve().parent
lean=json.loads((R/'lean_coarea_check.json').read_text(encoding='utf8'))
source=R/'CoareaReflectionCorrect.lean'
assert lean['exit_code']==0 and lean['source_sha256']==hashlib.sha256(source.read_bytes()).hexdigest()
text=source.read_text(encoding='utf8');assert 'sorry' not in text and 'native_decide' not in text
checks=json.loads((R/'death_count_checks.json').read_text(encoding='utf8'))
assert len(checks['results'])==9
coarea=json.loads((R/'coarea_checks.json').read_text(encoding='utf8'));assert len(coarea)==3
probe=json.loads((R/'coarea_probe.json').read_text(encoding='utf8'))
assert probe['peak_sampled_RSS_bytes']<1024**3
for k in [1,2,3]:assert (R/f'gap_recall_{k}.txt').exists()
new=[
 {'problem_id':'F0072','claim':'For a cube wall A=B_M in any B_N, N>=M, the low-site count K_h is dominated by a negative-binomial immigration birth law with r=(2M+1)^(d-1), p=exp(-2dh). Consequently P(K_h>=m)<=exp(-p m/2+r log 2).','status':'proved','proof_location':'SECOND_ATTEMPT.md, Stronger quantitative partial result','remaining_gap':'A count bound does not control a selected wall-edge or corner site.','checks':'Full contact-rate bound and explicit Markov coupling; nonexplosion and independent Yule-family law; exact generator-rate identities and nine finite checks in death_count_checks.json.'},
 {'problem_id':'F0072','claim':'For every eta>0 and 0<a<1/(2d), the probability that at least eta|B_M| wall sites have height <=a log M is at most exp(-c M^(d-2da)) for sufficiently large M, uniformly over N>=M.','status':'proved','proof_location':'SECOND_ATTEMPT.md, consequence of COUNT','remaining_gap':'Uniform pointwise lower bounds at the partial wall boundary and general-potential extensions remain unproved.','checks':'Substitute p=M^(-2da), r=(2M+1)^(d-1), m=ceil(eta(2M+1)^d) into the proved negative-binomial bound; 2da<1 makes the negative exponent dominate.'},
 {'problem_id':'F0072','claim':'The corrected reflection counterexample cross multiplication 3*1444<1089*4 is kernel-checked in Lean.','status':'proved','proof_location':'CoareaReflectionCorrect.lean; lean_coarea_check.json','remaining_gap':'Only the finite arithmetic is formalized, not the leaf integrals, coarea reduction, or count theorem.','checks':'lake env lean from ~/lean_verify, exit 0; decide +kernel; no sorry or native_decide; SHA-256 '+lean['source_sha256']}
]
lines=(R/'CLAIMS.jsonl').read_text(encoding='utf8').splitlines();old=[json.loads(x) for x in lines if x.strip()]
with (R/'CLAIMS.jsonl').open('a',encoding='utf8') as stream:
 for c in new:
  if not any(x['claim']==c['claim'] for x in old):stream.write(json.dumps(c,ensure_ascii=False)+'\n')
p=R/'SECOND_ATTEMPT.md';s=p.read_text(encoding='utf8')
marker='## Final verification and closure'
if marker not in s:
 s+='\n'+marker+'\n\nThe corrected CoareaReflectionCorrect.lean passed lake env lean (exit 0), using decide +kernel. Checked source SHA-256: '+lean['source_sha256']+'. This verifies the finite cross multiplication only. ReflectionArithmetic.lean and lean_second_check.json belong to the superseded numerical setup and are not cited as verification of the corrected Gibbs counterexample.\n\nThe death-chain uniformization checks passed all nine cases in '+str(checks['seconds'])+' seconds. Its three-site root marginal agreed with the independent leaf-integral CDF to maximum error 4.218847493575595e-15. On the 3x3 full-wall square all nine count-tail thresholds were compared with the negative-binomial bound at four levels; all passed. The Poisson truncation bounds are recorded in death_count_checks.json. These checks substantiate the finite implementation; the written coupling and geometric-family proof establish COUNT for all finite volumes.\n\nFinal STATE: DONE. VERDICT: PARTIAL. There is new exponential concentration for the fraction of low wall sites, but no proved uniform selected-site lower bound at partial-wall edges or corners. No counterexample to F0072 and no matching published solution is claimed.\n'
 p.write_text(s,encoding='utf8')
p=R/'ATTEMPT.md';s=p.read_text(encoding='utf8')
marker='Second-attempt quantitative strengthening:'
if marker not in s:
 s+='\n'+marker+' the coarea/death-chain route also proves that, for every eta>0 and 0<a<1/(2d), the probability of eta|B_M| or more wall heights <=a log M is bounded by exp(-c M^(d-2da)), uniformly over N>=M for large M. The exact negative-binomial domination and complete proof are in SECOND_ATTEMPT.md, Stronger quantitative partial result. Nine finite generator/analytic checks passed, and the corrected reflection cross multiplication passed Lean. This strengthens the averaged bound without filling the selected-site edge gap. Final verdict remains PARTIAL.\n'
 p.write_text(s,encoding='utf8')
p=R/'STATUS.md';s=p.read_text(encoding='utf8')
s=s.replace('STATE: WORKING','STATE: DONE',1)
s=s.replace(s.splitlines()[1], 'NEXT: Prove uniform survival to a log M at each partial-wall edge/corner site for the conditioned coarea death chain, or establish the sufficient power-sized positive sign buffer.',1)
assert 'VERDICT: PARTIAL' in s
s+='\n2026-10-12: Completed the requested serious second attempt. Proved exact coarea and attractive-death-chain reductions, refuted the naive reflection comparison, and proved negative-binomial domination of low wall-site counts with an exponential fraction-tail bound uniform in N. Corrected an initial leaf-integration coefficient error detected by exact recursion. Both relevant finite test suites passed; corrected Lean cross-product arithmetic passed. Gap-specific brain recalls completed. STATE: DONE, VERDICT: PARTIAL; the selected wall-edge/corner lower bound is still unproved.\n'
p.write_text(s,encoding='utf8')
claims=[json.loads(x) for x in (R/'CLAIMS.jsonl').read_text(encoding='utf8').splitlines() if x.strip()]
for c in claims:
 assert c['problem_id']=='F0072'
 assert c['status'] in ['proved','proved_special_case','counterexample','numerical_evidence','conjecture']
 assert all(k in c for k in ['claim','proof_location','remaining_gap','checks'])
assert (R/'STATUS.md').read_text(encoding='utf8').splitlines()[0]=='STATE: DONE'
assert '## Two approaches not pursued in the first attempt' in (R/'SECOND_ATTEMPT.md').read_text(encoding='utf8')
print(json.dumps({'state':'DONE','verdict':'PARTIAL','claim_records':len(claims),'corrected_lean_exit':lean['exit_code'],'finite_death_checks':len(checks['results'])}),flush=True)
