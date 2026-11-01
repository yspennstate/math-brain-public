from pathlib import Path
from datetime import datetime, timezone
import json, hashlib
ROOT=Path(__file__).resolve().parents[1]
AGENT=ROOT.parents[1]
def sha(b): return hashlib.sha256(b).hexdigest()
def save(name,obj): (ROOT/name).write_text(json.dumps(obj,indent=2,ensure_ascii=False)+'\n',encoding='utf-8')
sources=[]
base=Path(r'~\mop_fei100\reports\fei-2026-10-11')
supp=Path(r'~\mop_fei100\research_pushes\2026-10-11-full-fei-100-agents')
worker=Path(r'~\brain_workers\FEI100_20261011')
paths=[base/n for n in ['EXECUTION_PROTOCOL.json','README.md','CURRENT_STATUS.md','CLAIM_REGISTRY.json','OBSTRUCTION_REGISTRY.json','PACKET_STATUS.json','STREAM_NEXT_ACTIONS.json','FEI_100_agent_research_plan.tex']]
paths += list((base/'runs').rglob('REPORT.md'))
paths += [supp/n for n in ['CAMPAIGN.md','CLAIMS.md','COUNTEREXAMPLES.md','SEED_LEMMAS.md','NATIVE_MAPPING.md']]
paths += [p for p in (supp/'sources').rglob('*') if p.is_file()]
paths += [worker/'BOARD.md',worker/'claude'/'B15'/'STREAM_NOTES.md']
paths += list((worker/'context').glob('*.txt'))
paths += list((worker/'agents'/'A082'/'runs').rglob('REPORT.md'))
excerpts=[]
for p in paths:
    b=p.read_bytes()
    try: t=b.decode('utf-8'); enc='utf-8'
    except UnicodeDecodeError: t=b.decode('cp1252',errors='replace'); enc='cp1252 (replacement for undefined bytes if any)'
    sources.append({'path':str(p),'bytes':len(b),'sha256':sha(b),'decoded_with':enc,'role':'context/navigation unless cited in REPORT.md'})
    if p.parent.name=='context':
        lines=t.splitlines(); excerpts.extend(['\nFILE '+p.name, t[:5500]])
        hits=[i for i,l in enumerate(lines) if any(s in l.lower() for s in ['composition','restriction','theorem 1','theorem 7','proposition 7'])]
        for i in hits[:10]: excerpts.append('\n'.join(lines[max(0,i-2):i+12]))
save('out/SOURCE_RECEIPTS.json',sources)
(ROOT/'out'/'PAPER_LOCATORS_READ.txt').write_text('\n'.join(excerpts),encoding='utf-8')
statement=('For every Boolean outer f and balanced Boolean inner g on disjoint uniform blocks, H(f composed g)=H(f)+I(f)H(g), I(f composed g)=I(f)I(g), and B_(j,i)=I_j(f)B_i(g)+sum_T phi(p_f(T),p_f(T+j)ghat({i})^2). The correction vanishes iff ghat({i})=0 or B_j(f)=0. Any F with H(F)>(K+2/ln2)I(F), K>=0, has a constructively selectable physical restriction where every relevant i satisfies B_i>K I_i. Recursive Maj3 has I_d=(3/2)^d, H_d=4((3/2)^d-1), B_d=0, and for every d>=2 has an explicit AND3 restriction with every B_i/I_i=4+(5/2)log2(5)-(9/2)log2(3).')
claim={'claim_id':'A075-BALANCED-COMPOSITION-RESTRICTION-BRIDGE','version':1,'exact_statement':statement,'hypotheses':['Boolean sign functions','uniform physical cube','balanced inner function','disjoint blocks','entropy in bits','K>=0 for extraction','strict entropy deficit for extraction'],'statement_sha256':sha(statement.encode()),'contributors':['A075; B15 lead supplied calibration and target; A082 credited for point-defect constant'],'proof_source':str(ROOT/'REPORT.md'),'proof_dependencies':['Elementary Walsh expansion and entropy chain rule','ERASURE_REDUCTION.md sections 1,2,4 reconstructed within REPORT.md; no unreviewed theorem assumed'],'review_records':[],'status':'AUTHOR_PROVED_SCOPED_RECONSTRUCTION_REVIEW_PENDING','supersedes':[],'refutes':['Unconditional omission of singleton-collision correction from B(f composed g)=I(f)B(g)'],'first_unproved_line':None,'next_consumers':['A071','A074','A091','A026','A028','B15','B20']}
save('CLAIMS.json',[claim])
progress={'protocol_revision':'2026-10-11-execution-v2','run_id':ROOT.name,'stream':'B15','packet_id':'A075','gap_id':'G-R-SELECT','attempt_id':'A075-COMPOSITION-BRIDGE-1','method':'Exact balanced-substitution expansion, singleton collision repair, rational prime-log checks, constructive positive-potential restriction extraction','mathematical_delta':'Reconstructed composition identities with exact necessary/sufficient collision condition; proved constructive extraction and explicit recursive-majority AND3 hereditary bottleneck. Universal FEI payment remains open.','deliverable_status':'COMPLETE_LOCAL_ARTIFACT','mathematical_status':'SCOPED_BRIDGE_AUTHOR_PROVED; FULL_FEI_OPEN; INDEPENDENT_REVIEW_PENDING','claim_versions_used':['ERASURE_REDUCTION.md sections 1,2,4 re-derived; B15 STREAM_NOTES v1 calibration repaired; A082 witness reconstructed, finite theorem not assumed'],'claims_created_or_changed':[claim['claim_id']+'@1'],'source_artifacts':['REPORT.md','CLAIMS.json','out/FROZEN_SPEC.json','code/check.py','out/VALIDATION.json','out/SOURCE_RECEIPTS.json','out/PAPER_LOCATORS_READ.txt','out/MANIFEST.json'],'next_consumers':claim['next_consumers'],'next_action':'Consume A071 certified n=5/6 seed; extract recursive-composition hereditary bottleneck, seeking actual selectable erasure above Kstar; A074/A091 independently reconstruct current proof.','stagnant_substantive_attempts':0,'blockers':['No independently reviewed stronger A071 seed available in inputs; universal residual payment remains unproved'],'packet_ids':['A075']}
save('PROGRESS.json',progress); save('PACKET_DELTA.json',progress)
(AGENT/'STATUS.md').write_text('STATE: A075 packet complete locally: exact composition collision repair and constructive restriction bridge; 27,328 exact assertions passed; review pending; full FEI OPEN.\nNEXT: A074/A091 reconstruct; consume A071 certified seed and extract hereditary bottleneck exceeding Kstar, retaining actual physical terminal cost.\n',encoding='utf-8')
with (AGENT/'WORKLOG.md').open('a',encoding='utf-8') as f: f.write(datetime.now(timezone.utc).isoformat()+': Completed scoped composition proof and constructive C018 extraction; exact 1560-case check passed in 4.265 seconds. Recursive Maj3 roots B=0, explicit AND3 restrictions force Kstar. Saved full run and receipts; no mirror/acceptance claim.\n')
(AGENT/'LEARNED.md').write_text('Balanced disjoint substitution always has H(F)=H(f)+I(f)H(g), I(F)=I(f)I(g). True erasure also has singleton collision sum phi(p_f(T),p_f(T+j)ghat({i})^2); it vanishes exactly if singleton mass vanishes or outer B_j=0.\nRecursive Maj3: H_d=4((3/2)^d-1), I_d=(3/2)^d, B_d=0; each depth>=2 contains a physical AND3 restriction with all-coordinate erasure price Kstar=4+(5/2)log2(5)-(9/2)log2(3). Thus root zero erasure is not hereditary ease.\nAny H>(K+2/ln2)I yields a computable physical restriction with every relevant B_i>K I_i by positive-potential descent, using rational slack and exact prime-product decisions. Computable does not mean efficient; universal upper payment remains unpaid.\n',encoding='utf-8')
manifest=[]
for p in sorted([p for p in ROOT.rglob('*') if p.is_file() and p.name!='MANIFEST.json']+[AGENT/n for n in ['STATUS.md','WORKLOG.md','LEARNED.md']]):
    b=p.read_bytes(); assert len(b)<20_000_000
    manifest.append({'path':str(p),'bytes':len(b),'sha256':sha(b)})
save('out/MANIFEST.json',manifest)
proto=json.loads((base/'EXECUTION_PROTOCOL.json').read_text(encoding='utf-8'))['required_per_run']
expected={x.split(' ')[0] for x in proto['progress_fields']}
assert set(progress)==expected
assert set(claim)==set(proto['claim_fields'])
assert json.loads((ROOT/'PACKET_DELTA.json').read_text())==json.loads((ROOT/'PROGRESS.json').read_text())
print(json.dumps({'saved_run':str(ROOT),'source_files_loaded':len(sources),'manifest_entries':len(manifest),'schema_exact':True,'full_fei':'OPEN'},indent=2))
