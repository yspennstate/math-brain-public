from pathlib import Path
from datetime import datetime,timezone
import json,hashlib,re
RUN=Path(__file__).resolve().parents[1];ROOT=RUN.parent.parent
BASE=Path(r'~\mop_fei100\reports\fei-2026-10-11')
def read(p):return p.read_text(encoding='utf-8-sig')
def obj(p):return json.loads(read(p))
def save(n,v):(RUN/n).write_text(json.dumps(v,indent=2,ensure_ascii=False)+'\n',encoding='utf-8')
def sha(p):return hashlib.sha256(p.read_bytes()).hexdigest()
assert ROOT.name=='A099'
for n in ['STAGE5_ADDITIONS.tex','CANDIDATE_MANUSCRIPT.tex']:
    p=RUN/n;t=read(p)
    t=t.replace('scope by A098 and reconstructed here by A099. All costs are in bits. It','scope by A098 and reconstructed here by A099~\\cite{A097e,A098e}. All costs are in bits. It')
    t=t.replace('The following complete derivation is A096 version 1 at author scope;','The following complete derivation is A096 version 1 at author scope~\\cite{A096e};')
    t=t.replace("A100 independently accepted the original A073 family statement; this","A100 independently accepted the original A073 family statement~\\cite{A100e}; this")
    p.write_text(t,encoding='utf-8')
v=obj(RUN/'out/VALIDATION.json')
ok=len(v['build'])==2 and all(b.get('returncode')==0 for b in v['build'])
v['PDF_complete_two_passes']=ok
if not (RUN/'out/CANDIDATE_MANUSCRIPT.log').exists():v['overfull_boxes']=None
t=read(RUN/'CANDIDATE_MANUSCRIPT.tex');labels=re.findall(r'\\label\{([^}]+)\}',t)
refs=re.findall(r'\\(?:ref|eqref)\{([^}]+)\}',t)
cites=[c.strip() for z in re.findall(r'\\cite\{([^}]+)\}',t) for c in z.split(',')]
bibs=re.findall(r'\\bibitem(?:\[[^]]*\])?\{([^}]+)\}',t)
assert len(labels)==len(set(labels));assert not(set(refs)-set(labels));assert not(set(cites)-set(bibs))
v['static_tex_validation']={'duplicate_labels':False,'missing_refs':[],'missing_citations':[],'claim':'Static source structure only; compiler timed out'}
save('out/VALIDATION.json',v)
p=obj(RUN/'PROGRESS.json')
if ok:p['source_artifacts'].append('out/CANDIDATE_MANUSCRIPT.pdf')
else:
    p['deliverable_status']='COMPLETE_PROTOCOL_AND_SINGLE_SOURCE_PDF_BUILD_TIMEOUT'
    p['blockers'].append('Verified current PDF unavailable: bounded 45-second compiler timeout before log creation; complete source saved')
save('PROGRESS.json',p);save('PACKET_DELTA.json',p)
protocol=obj(BASE/'EXECUTION_PROTOCOL.json');report=read(RUN/'REPORT.md')
for h in protocol['required_per_run']['report_fields']:assert '## '+h in report,h
assert report.rstrip().splitlines()[-1].startswith('Universal bridge:')
assert set(p)=={s.split(' (')[0] for s in protocol['required_per_run']['progress_fields']}
assert (RUN/'PROGRESS.json').read_bytes()==(RUN/'PACKET_DELTA.json').read_bytes()
for c in obj(RUN/'CLAIMS.json'):assert set(c)==set(protocol['required_per_run']['claim_fields'])
(ROOT/'STATUS.md').write_text('STATE: A099 v5 source/protocol saved: supplied-reference negative-cell floor spends one source bank (10-tax, 2C0+10) with A098/A099 scoped audits; Jensen remainder sharpened; actual child-bank obstruction retained; full FEI OPEN; PDF build timed out.\nNEXT: A097/A096 transport actual incoming reference through an active-bit restriction, paying reset/normalizer and surviving terminal row from the same remaining bank; A094/A085 audit full assembly.\n',encoding='utf-8')
stamp=datetime.now(timezone.utc).isoformat()
with (ROOT/'WORKLOG.md').open('a',encoding='utf-8') as f:
    f.write(f'\n{stamp}: {RUN.name}: v5 single-source assembly saved, 12 preserved claim records, 30 dependency nodes, four unchanged universal conjectures. Independently reconstructed A097 negative-cell floor at full original scope including arbitrary supplied source and independent terminal; own pilot 32 assertions and full 18 instances/54 references/633 assertions PASS. Consumed exact A098 acceptance. Reconstructed A100 Jensen bound with exact 77^4<2*65^4 certificate, consumed its full original A073 review without rewriting original digest. Reproduced A096 non-flat remainder and sharp actual child-bank threshold-five obstruction at author scope. Complete source/protocol and local receipts saved; bounded PDF compiler timed out before log creation. Hereditary actual incoming-reference bank transport and both integrated audits remain open.\n')
with (ROOT/'LEARNED.md').open('a',encoding='utf-8') as f:
    f.write('\nNegative-cell supplied-reference floor: for g=1-2 A_a with b dummies edited at a negative full data point under r fresh point controls, CE_F<=c+10(C+E+J), I_F=I_g+C-E+J, E/I_g<=1/2. A source certificate c<=C0 I_g yields CE_F<=(2C0+10)I_F by one signed-bank debit; prescribed structural R=P_g yields 18. Full posterior KL and independent terminal cost remain. A098/A099 full scoped audits do not prove hereditary incoming-reference closure; an actual child reset must use the same remaining bank.\n\nFor arbitrary core point attachment, the sufficient statistic (gate mask, actual signed core amplitude) preserves full derivative-row KL; mask-only quotient losses fit 2 I_Y+2/(e ln2) I_X, or I_Y/2 when both core children are nonconstant. These fresh root quotas are not automatically unused child surplus. A rate-four point-sign family forces loss-only child-bank threshold five; tensoring a tiny independent nonconstant terminal retains the obstruction with both children nonconstant. FEI remains true for that fixture.\n\nFor the A073 positive-erasure bent-core/two-bit gate family, weighted Jensen gives R(delta)=(1+delta-3delta^2/4)/(1+delta^2/4), each loss/e<1/8 and summed loss<delta^2/(2 ln2), also a dedicated twentieth of one core influence. A100 original-family review joins A098; its separate Jensen refinement has A099 scoped acceptance only. Surviving row cost/e>d/2+3/4 remains unpaid.\n')
assert len(read(ROOT/'STATUS.md').splitlines())==2
files=[q for q in RUN.rglob('*') if q.is_file()]
assert all(q.stat().st_size<20_000_000 for q in files)
save('out/SCHEMA_CHECK.json',{'report_fields':True,'claim_fields':True,'progress_fields':True,'compatibility_identical':True,'all_files_below_20MB':True,'rolling_status_two_lines':True,'PDF_complete':ok,'integrated_audits':'PENDING','mirror':'NOT_VERIFIED','static_tex_structure':True})
receipts=[{'path':str(q.relative_to(RUN)),'bytes':q.stat().st_size,'sha256':sha(q)} for q in sorted(RUN.rglob('*')) if q.is_file() and q.name!='PERSISTENCE_RECEIPTS.json']
save('out/PERSISTENCE_RECEIPTS.json',{'run_id':RUN.name,'files':receipts,'self_excluded':True,'rolling_files':[{'path':str(q),'sha256':sha(q)} for q in [ROOT/'STATUS.md',ROOT/'WORKLOG.md',ROOT/'LEARNED.md']],'mirror':'NOT_VERIFIED'})
assert all(sha(RUN/r['path'])==r['sha256'] for r in receipts)
print(json.dumps({'status':'SAVED_AND_HASH_VERIFIED','files':len(receipts),'claims':len(obj(RUN/'CLAIMS.json')),'PDF_complete':ok,'full_FEI':'OPEN','integrated_audits':'PENDING'}))
