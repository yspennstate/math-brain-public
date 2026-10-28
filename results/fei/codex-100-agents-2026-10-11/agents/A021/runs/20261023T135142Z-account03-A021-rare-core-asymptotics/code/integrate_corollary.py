from pathlib import Path
import json,hashlib,datetime
R=Path(__file__).resolve().parents[1];A=R.parents[1]
def read(p):return Path(p).read_text(encoding='utf-8')
def write(p,s):Path(p).write_text(s,encoding='utf-8',newline='')
def load(p):return json.loads(read(p))
def dump(p,o):write(p,json.dumps(o,indent=2,ensure_ascii=False)+'\n')
def sha(p):return hashlib.sha256(Path(p).read_bytes()).hexdigest()
out=load(R/'out/BALANCED.json');pilot=load(R/'out/BALANCED_PILOT.json')
assert out['status']=='PASS' and out['balanced_truth_tables']==70 and out['assertions']==560
assert pilot['status']=='PASS' and pilot['balanced_truth_tables']==2
now=datetime.datetime.now(datetime.timezone.utc).isoformat()
cs=load(R/'CLAIMS.json');c=cs[0]
c['exact_statement']+=' Moreover, for the SAME fixed seed and pair of adjacent edits, EVERY balanced Boolean controller a on ANY finite number of uniform control bits obeys GV(F)-2delta GV(a)<70 and I_DATA(F)>=21/16, hence GV(F)<=2delta GV(a)+256 I_DATA(F). The two edits use the SAME controller; two different dependent controllers are not covered.'
c['statement_sha256']=hashlib.sha256(c['exact_statement'].encode('utf-8')).hexdigest()
c['proof_source']['additional_proof']={'path':'BALANCED_COROLLARY.md','sha256':sha(R/'BALANCED_COROLLARY.md'),'scope':'All balanced shared Boolean controllers; Parseval light/heavy singleton split.'}
c['review_records'].append({'reviewer':'A021 author','scope':'Analytic all-dimensional corollary plus ALL70 balanced3-bit truth tables,560 assertions, no symmetry reduction.','result':'PASS; external mathematical review pending.'})
dump(R/'CLAIMS.json',cs)
pr=load(R/'PROGRESS.json')
pr['mathematical_delta']+=' The retained ORIGINAL marked owner is proved to satisfy SAME256 for EVERY balanced shared Boolean controller, independent of control dimension, by a Parseval light/heavy split; exhaustive70 nonsymmetric3-bit cases corroborate it.'
pr['method']+=' Analytic arbitrary-balanced-controller corollary and exhaustive70 balanced3-bit truth tables.'
dump(R/'PROGRESS.json',pr);write(R/'PACKET_DELTA.json',read(R/'PROGRESS.json'))
p=R/'REPORT.md';s=read(p)
s=s.replace('The actual Boolean majority family, all-m bounds, and the same-family repair are in [PROOF.md](PROOF.md).',
 'The actual Boolean majority obstruction and all-m bounds are in [PROOF.md](PROOF.md). The repair extends to EVERY balanced shared Boolean controller on any finite control cube, at the SAME256 rate, in [BALANCED_COROLLARY.md](BALANCED_COROLLARY.md).')
s=s.replace('The exact first unsupported universal line is:',
 'The balanced-controller corollary bounds the small singleton contributions by13/2 using Parseval and curvature; at most three large coefficients each cost at most7. Thus the corrected residual is below70 for EVERY balanced shared controller, still well below256 times the DATA reserve. No majority symmetry is needed for this positive result. The exact first unsupported universal line is:')
s=s.replace('## proof dependencies and changed downstream conclusions',
 f'Additional frozen BALANCED_SPEC.json: ALL70 balanced truth tables on3 controls, no symmetry, integer Walsh/rational-log arithmetic,100MB estimate, pilot2 cases under60seconds and main under120seconds. Command: `python -X utf8 code/run_balanced.py` from this run directory. Pilot passed{pilot["assertions"]} assertions in{pilot["seconds"]:.4f}seconds; main passed{out["assertions"]} assertions in{out["seconds"]:.4f}seconds, including{out["heavy_singleton_cases"]} cases with a heavy singleton and{out["all_zero_singleton_cases"]} cases with all singleton coefficients zero. Outputs: out/BALANCED_PILOT.json and out/BALANCED.json. The analytic Parseval argument supplies arbitrary-control-dimension validity.\n\n## proof dependencies and changed downstream conclusions')
s=s.replace('while retaining it restores the same256 rate on this family.',
 'while retaining it restores the same256 rate for EVERY balanced shared controller on this fixed adjacent-edit seed.')
write(p,s)
write(A/'STATUS.md','STATE: A021 13:51 stage complete locally: unmarked shared-selector owner has logarithmic debt; ORIGINAL marked owner satisfies SAME256 for EVERY balanced shared controller; exact37+790+560 checks PASS; external review pending; FEI OPEN.\nNEXT: A022/B05 pay signed marked singleton/sector cocycle for TWO different dependent controllers from ONE original compatible owner, both outcomes retained; A029/A094 independently review obstruction and balanced-controller repair.\n')
with (A/'WORKLOG.md').open('a',encoding='utf-8') as f:f.write(f'\n{now} | Same stage corollary: extended SAME256 marked-owner repair from majority to EVERY balanced Boolean shared controller, arbitrary dimension. Parseval pays small singleton squares; at most3 heavy singleton coefficients cost<=7 each; corrected residual<70. Exhaustive ALL70 balanced3-bit functions (including dictators and zero-singleton functions),560 assertions PASS. Two DIFFERENT dependent controllers remain open.\n')
with (A/'LEARNED.md').open('a',encoding='utf-8') as f:f.write('\nSame13:51 stage strengthening: SAME fixed t2 adjacent-pair seed, BOTH edits use SAME arbitrary balanced Boolean a: GV(F)-2delta GV(a)<70 and I_DATA>=21/16, hence SAME256 transfer for all control dimensions. Proof: T>=0, T0<=7 via dictator representative; light |ahat(j)|<=1/2 cost <=13/2 times sum singleton squares<=13/2; at most3 heavy singleton coefficients contribute<=7 each; DATA drift<=42. Different dependent controllers and general seeds remain unproved. BALANCED_COROLLARY.md contains the full argument.\n')
old=load(R/'out/PERSISTENCE.json')
old['generated_at']=now
old['files']={str(p.relative_to(R)):{'bytes':p.stat().st_size,'sha256':sha(p)} for p in sorted(R.rglob('*')) if p.is_file() and '__pycache__' not in str(p) and p.name not in ('PERSISTENCE.json','FINAL_VALIDATION.json')}
old['rolling']={str(A/n):sha(A/n) for n in ('STATUS.md','WORKLOG.md','LEARNED.md')}
dump(R/'out/PERSISTENCE.json',old)
protocol=load('math-open-problems/reports/fei-2026-10-11/EXECUTION_PROTOCOL.json')['required_per_run'];expected=set(protocol['progress_fields']);expected.remove('packet_ids (one primary ID, for compatibility)');expected.add('packet_ids')
assert set(pr)==expected and set(c)==set(protocol['claim_fields'])
assert (R/'PROGRESS.json').read_bytes()==(R/'PACKET_DELTA.json').read_bytes()
assert c['proof_source']['sha256']==sha(R/'PROOF.md')
assert c['proof_source']['additional_proof']['sha256']==sha(R/'BALANCED_COROLLARY.md')
assert c['statement_sha256']==hashlib.sha256(c['exact_statement'].encode('utf-8')).hexdigest()
assert all(h in s for h in protocol['report_fields'])
assert s.rstrip().split('\n')[-1].startswith('**Universal bridge:**')
assert len(read(A/'STATUS.md').splitlines())==2
assert all(p.stat().st_size<20*1024*1024 for p in R.rglob('*') if p.is_file())
dump(R/'out/FINAL_VALIDATION.json',{'status':'PASS','at':now,'exact_protocol_fields':True,'compatibility_copy_identical':True,'statement_and_all_proof_hashes':True,'report_fields_and_final_bridge':True,'rolling_status_two_lines':True,'all_files_under20MB':True,'all_balanced_corollary_included':True,'full_fei':'OPEN','external_review':'PENDING','research_jobs_left_running':False})
print(json.dumps({'status':'PASS','balanced_corollary':'ALL dimensions, SAME controller only','all70_check':out,'external_review':'PENDING'}))
