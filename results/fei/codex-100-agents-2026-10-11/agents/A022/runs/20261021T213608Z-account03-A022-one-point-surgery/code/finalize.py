from pathlib import Path
import json, hashlib, datetime

run=Path(__file__).resolve().parents[1]; owner=run.parents[1]
def sha(p): return hashlib.sha256(p.read_bytes()).hexdigest()
def save(name,obj): (run/name).write_text(json.dumps(obj,indent=2,ensure_ascii=False)+'\n',encoding='utf-8')
protocol=Path('math-open-problems/reports/fei-2026-10-11/EXECUTION_PROTOCOL.json')
rules=json.loads(protocol.read_text(encoding='utf-8-sig'))
sources=[]
base=protocol.parent
targets=[base/n for n in ['EXECUTION_PROTOCOL.json','README.md','CURRENT_STATUS.md','CLAIM_REGISTRY.json','OBSTRUCTION_REGISTRY.json','PACKET_STATUS.json','STREAM_NEXT_ACTIONS.json','FEI_100_agent_research_plan.tex']]
supp=Path('math-open-problems/research_pushes/2026-10-11-full-fei-100-agents')
targets += [supp/n for n in ['CAMPAIGN.md','CLAIMS.md','COUNTEREXAMPLES.md','SEED_LEMMAS.md','NATIVE_MAPPING.md']]
targets += list((supp/'sources').glob('*.md'))
ctx=Path('~/brain_workers/FEI100_20261011')
targets += list((ctx/'context').glob('*.txt'))
targets += [ctx/'BOARD.md',ctx/'claude/B05/STREAM_NOTES.md',ctx/'claude/B05/runs/20261011T225000Z-claude-B05-odd-face-transport/REPORT.md']
targets += list(owner.glob('runs/2026101*/REPORT.md'))
excerpts=[]
for p in targets:
    raw=p.read_bytes()
    try: txt=raw.decode('utf-8-sig'); encoding='utf-8-sig'
    except UnicodeDecodeError: txt=raw.decode('cp1252'); encoding='cp1252'
    sources.append({'path':str(p),'sha256':hashlib.sha256(raw).hexdigest(),'bytes':len(raw),'encoding':encoding,
                    'use':'read for orientation and scope; theorem premises only as explicitly identified in REPORT'})
    if p.suffix=='.txt':
        lines=txt.splitlines()
        for i,l in enumerate(lines):
            if 'Proposition 8.6' in l or 'Proposition 7.1' in l or 'Theorem 1.3' in l:
                excerpts.append(p.name+':'+str(i+1)+'\n'+'\n'.join(lines[i:i+34]))
(run/'out/source_excerpts.txt').write_text('\n\n'.join(excerpts),encoding='utf-8')
save('out/source_manifest.json',sources)
prior=owner/'runs/20261014T103056Z-account05-A022-one-point-surgery/CLAIMS.json'
old=json.loads(prior.read_text(encoding='utf-8'))[0]
new_statement='Refinement of v5, with inherited statements at their original scope: for arbitrary Boolean seed b, distinct controlled vertex flips on independent controls, and any positive normalized complete data spectral reference Q, CE_Q(P_data)-CE_Q(P_b)=-4*2^-k E sum_{x in D,y outside D} b(x)b(y)K_Q(x xor y), K_Q(d)=2^-k sum_S log2(1/Q(S))chi_S(d). Full H(F)=CE_Q(P_b)+L+kV+phi(1-V)-2^-k sum_j phi(mu_j^2)+W_Q-M-D(P_joint||Q tensor R), with exact controller marginal R and actual influence including adjacent E(A_j A_l) correction as in REPORT(1)-(6). The fixed original bank C I(b)-CE_Q(P_b)-U pays iff REPORT(7) holds; no reset is implied. Product references have zero kernel between vertices differing in two blocks. For b=g^{tensor t}, t>=2, g=-1 only at 000 on three bits, every single-vertex flip activated by any independent indicator A satisfies H(F)+U<=4I_data(F)+2^(-3t)H(1-2A) for 0<=U<=t/64. Full FEI and arbitrary mixed-history bank eligibility remain open.'
claim={k:old.get(k) for k in rules['required_per_run']['claim_fields']}
claim.update(version=6,exact_statement=new_statement,statement_sha256=hashlib.sha256(new_statement.encode()).hexdigest(),
    hypotheses=['Uniform Boolean data seed; independent uniform control block','Distinct edited data vertices; controller events may be dependent','Positive normalized complete reference Q; Q=P_b only with full support','Rate-4 application requires the stated tensor seed and t>=2; full controller entropy retained','Entropy in bits; phi(0)=0'],
    contributors=['A022 account03 current stage','A022 account05 inherited v5 at original scope'],
    proof_source={'current':'REPORT.md','inherited_v5':str(prior.parent/'REPORT.md'),'validation':['out/exact_checks.json','out/bank_checks.json','out/lean_check.txt']},
    proof_dependencies=[{'claim_id':old['claim_id'],'version':5,'role':'inherited scope only; new reference formula reconstructed directly'},'finite Walsh orthogonality','entropy chain rule and KL nonnegativity'],
    review_records=old.get('review_records',[]),status='ANALYTIC_PROOF_AUTHOR_EXACT_CHECKED; INDEPENDENT_REVIEW_PENDING; UNIVERSAL_FEI_OPEN',
    supersedes=[{'claim_id':old['claim_id'],'version':5,'scope':'new reference refinement; inherited assertions unchanged'}],refutes=[],
    first_unproved_line='Arbitrary mixed physical histories satisfy the SAME inherited-bank inequality (7) with fixed rate and both terminal debts.',
    next_consumers=['A021','A025','A028','A029','A087','A094','B05'])
assert set(claim)==set(rules['required_per_run']['claim_fields'])
save('CLAIMS.json',[claim])
progress={
 'protocol_revision':rules['revision'],'run_id':run.name,'stream':'B05','packet_id':'A022','gap_id':'G-R-MISMATCH',
 'attempt_id':'A022-stage7-signed-complete-seed-reference','method':'refine existing v5 root theorem with exact Fourier-log physical cut and unchanged inherited seed bank',
 'mathematical_delta':'Exact signed complete-reference identity including full seed/controller bills and joint KL; tensor block locality; one-point surgery of nonflat g tensor t, t>=2, paid at rate4 with t/64 original reserve, below prior high-influence guard.',
 'deliverable_status':'COMPLETE_LOCAL_ARTIFACTS','mathematical_status':'SCOPED_ANALYTIC_PROOF_EXACT_AUTHOR_CHECKED; INDEPENDENT_REVIEW_PENDING; FULL_FEI_OPEN',
 'claim_versions_used':[{'claim_id':old['claim_id'],'version':5,'role':'existing ledger refinement; no external unreviewed proof premise'}],
 'claims_created_or_changed':[{'claim_id':old['claim_id'],'version':6}],
 'source_artifacts':['REPORT.md','FROZEN_SPEC.json','BANK_SPEC.json','code/check_reference.py','code/check_bank.py','code/Bank.lean','out/pilot.json','out/exact_checks.json','out/bank_checks.json','out/lean_check.txt','out/source_manifest.json'],
 'next_consumers':claim['next_consumers'],'next_action':'Expose one actual data coordinate of the nonflat tensor construction; carry original Q and old U through BOTH children, price signed conditional loss against remaining SAME t/64 reserve; A087/A094 review.',
 'stagnant_substantive_attempts':0,'blockers':['Universal fixed-bank inequality after physical data restriction is unproved.','Independent acceptance and supervisor mirrors unverified.'],'packet_ids':['A022']}
assert set(progress)=={s.split(' (')[0] for s in rules['required_per_run']['progress_fields']}
save('PROGRESS.json',progress); save('PACKET_DELTA.json',progress)
now=datetime.datetime.now(datetime.timezone.utc).isoformat()
(owner/'STATUS.md').write_text('STATE: A022 stage7 saved: exact signed seed-reference log cut/full entropy bank; low-influence nonflat tensor point surgery at rate4 retains t/64 original reserve; 4256 cases/137425 exact main assertions PASS; review pending; FEI OPEN.\nNEXT: A087/A094 review v6; expose one actual tensor-data coordinate with original Q, old U, BOTH terminal debts and SAME remaining t/64 reserve; no reference or bank reset.\n',encoding='utf-8')
with (owner/'WORKLOG.md').open('a',encoding='utf-8') as f:
    f.write('\n'+now+' stage7: Read board/stream/last source-complete stage6; later account05 run folders contain only .final. Replaced ambient k seed bill by exact supplied-reference cross-entropy. Signed loss is physical cut in Fourier log kernel; tensor kernels have within-block interactions only. Exact full entropy retains controller L, seed mismatch, label-mixing refund and joint KL. Rate4 proof for t>=2 tensor powers of three-bit defect retains t/64 original reserve despite I(seed)/k=1/4. Pilot128/3968 and main4256/137425 exact checks PASS; main52.782s. Full FEI and arbitrary next physical-data query payment remain OPEN. New theorem is author-checked, no independent acceptance.\n')
with (owner/'LEARNED.md').open('a',encoding='utf-8') as f:
    f.write('\nStage7 signed complete-reference cut: for normalized positive Q, K_Q(d)=2^-k sum log2(1/Q(S))chi_S(d), and CE_Q(edited spectrum)-CE_Q(seed spectrum)=-4*2^-k E sum_{edited x,unedited y}b(x)b(y)K_Q(x xor y). Product reference log kernels couple only one changed block. Exact root H=CE_Q(seed)+L+kV+phi(1-V)-delta sum phi(mu^2)+W-M-D_joint; seed mismatch and both refunds must stay explicit. At one point W=4delta alpha J_b(v); J and signed neighbor count are tensor additive. Three-bit point-defect g has H=4-(9/8)log2(3), I=3/4, J(0)=-(7/4)log2(3), J(other)=(5/4)log2(3). For g tensor t,t>=2, arbitrary controlled single flip has H+U<=4I_data+delta H(controller), U<=t/64, using only original seed surplus. This is a root result; no arbitrary history reset or universal FEI consequence.\n')
checks=json.loads((run/'out/exact_checks.json').read_text(encoding='utf-8'))
assert checks['status']=='PASS' and checks['cases']==4256
assert (run/'PROGRESS.json').read_bytes()==(run/'PACKET_DELTA.json').read_bytes()
receipt={'timestamp_utc':now,'protocol_field_sets':'PASS','progress_delta_identical':True,'statement_sha256':claim['statement_sha256'],
 'independent_review':'PENDING','external_mirror':'NOT_VERIFIED','files':[]}
for p in sorted(run.rglob('*')):
    if p.is_file() and p.name!='persistence.json':
        assert p.stat().st_size<20*1024*1024
        receipt['files'].append({'path':str(p.relative_to(run)),'bytes':p.stat().st_size,'sha256':sha(p)})
save('out/persistence.json',receipt)
print(json.dumps({'protocol_fields':'PASS','files':len(receipt['files']),'sources_read':len(sources),'main':checks,'next':progress['next_action']}))
