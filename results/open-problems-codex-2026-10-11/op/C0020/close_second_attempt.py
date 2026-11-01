from pathlib import Path
import json
R=Path(__file__).resolve().parent
assert (R/'greedy_lean_check.log').read_text().strip()=='exit_code=0'
assert not any(t in (R/'GreedyWitness.lean').read_text() for t in ['sorry','native_decide'])
rows=[json.loads(s) for s in (R/'CLAIMS.jsonl').read_text(encoding='utf8').splitlines()]
for row in rows:
 row['checks']=row['checks'].replace('Lean pivotal-count check pending.','Lean checked the entire pivotal-count vector with decide +kernel, exit 0 and no warnings; graph correspondence and Bellman optimality checked by exhaustive Python certificate.')
rows.append({'problem_id':'C0020','claim':'For the greedy crossing tree, H=I^2/(4 Var(F)), conditional drift d, and B(c)=E sum (c-d)_+, one has C_greedy <= (H(root)+B(c))/c for every c>0.','status':'proved','proof_location':'SECOND_ATTEMPT.md equation (11)','remaining_gap':'No improved critical-square bound on B_n(c) is proved. Such a bound at exponent 3/2+epsilon, epsilon<1/4, would improve the upper bound.','checks':'Finite conditional expectation, bounded-time telescoping and pointwise c<=d+(c-d)_+; no positivity assumption on d.'})
rows.append({'problem_id':'C0020','claim':'At a balanced monotone restricted state, for conditional influence 0<a<1 and b=(I_1-I_0)/2, the H-drift is [2Ia-a^2(1+I^2)-b^2]/(1-a^2), at most 2Ia/(1-a^2).','status':'proved','proof_location':'SECOND_ATTEMPT.md equation (12)','remaining_gap':'Using this at the initial selected greedy coordinate requires a justified influence/location estimate; it gives no query-time upper bound by itself.','checks':'Full algebra from q_0=(1-a)/2, q_1=(1+a)/2 and mean child influence I-a; the singular a=1 case explicitly excluded.'})
(R/'CLAIMS.jsonl').write_text(''.join(json.dumps(x)+'\n' for x in rows),encoding='utf8')
p=R/'STATUS.md';lines=p.read_text(encoding='utf8').splitlines();lines[0]='STATE: DONE';lines[1]='NEXT: Future work: bound B_n(c), the trajectory-weighted drift deficit in SECOND_ATTEMPT.md (11), using critical square geometry; no further work scheduled in this attempt.'
lines.append('2026-10-12: Additional attempt complete, VERDICT PARTIAL. Selected maximum-conditional-pivotal construction from two new approaches; proved its finite nonoptimality and refuted uniform drift and universal influence-based upper bounds. All 19683 Bellman states checked; Lean pivotal counts accepted, exit 0; guarded largest job 557 MiB and 62 seconds. Remaining B_n(c) estimate unproved; interval [3/2,7/4] unchanged.')
p.write_text('\n'.join(lines)+'\n',encoding='utf8')
assert p.read_text().splitlines()[0]=='STATE: DONE'
assert 'VERDICT: PARTIAL' in p.read_text()
assert len(rows)==13
check=json.loads((R/'bellman_certificate_check.json').read_text())
assert check['verified_states']==19683 and check['root_total']==2220
largest=json.loads((R/'greedy_4x3.json').read_text())
assert largest['peak_working_set_bytes']<1024**3 and largest['seconds']<480
print('Final check: DONE / PARTIAL;',len(rows),'claims; 19683-state certificate; Lean exit 0; resource limits passed.')
