from pathlib import Path
import json,hashlib,datetime,re,shutil,subprocess

RUN=Path(__file__).resolve().parents[1]; OWN=RUN.parents[1]
BASE=OWN/'runs/20261014T061720Z-fleet05-A099-candidate-assembly'
SOURCE=Path('agents/A096/runs/20261014T094929Z-fleet05-A096-live-gap-ledger')
NOW=datetime.datetime.now(datetime.timezone.utc).isoformat()
def read(p):return json.loads(p.read_text(encoding='utf-8'))
def save(p,d):p.write_text(json.dumps(d,indent=2,ensure_ascii=False)+'\n',encoding='utf-8')
full=read(RUN/'out/EXACT_TRANSPORT.json');pilot=read(RUN/'out/PILOT.json')
assert full['status']==pilot['status']=='PASS'
assert full['roots_and_references']==828 and full['single_queries']==2412
assert full['adaptive_histories']==828 and full['tensor_cases']==32
assert full['seconds']<55 and pilot['seconds']<60

claims=read(RUN/'CLAIMS.json');old=read(BASE/'CLAIMS.json');originals=read(SOURCE/'CLAIMS.json')
assert claims[:len(old)]==old
hash_conventions=[]
for c,source in zip(claims[len(old):],originals):
    assert {k:v for k,v in c.items() if k not in ['review_records','status']}=={k:v for k,v in source.items() if k not in ['review_records','status']}
    statement=c['exact_statement'];hyp=c['hypotheses'];candidates={'raw_statement':statement}
    for key in ['statement','exact_statement']:
        for ascii in [True,False]:
            for sep in [None,(',',':')]:
                candidates[str((key,ascii,sep))]=json.dumps({key:statement,'hypotheses':hyp},sort_keys=True,ensure_ascii=ascii,separators=sep)
    matches=[key for key,value in candidates.items() if hashlib.sha256(value.encode('utf-8')).hexdigest()==c['statement_sha256']]
    assert matches, c['claim_id']
    hash_conventions.append({'claim_id':c['claim_id'],'original_statement_sha256':c['statement_sha256'],'matched_conventions':matches})
    c['review_records'][-1].update(verdict='HOLDS_AT_EXACT_ORIGINAL_SCOPE',timestamp=NOW,
      validation=str(RUN/'out/EXACT_TRANSPORT.json'),
      review_guard='Only this scoped statement; not universal cheap-source/reset existence or either integrated audit')
    c['status']='ONE_SCOPED_INDEPENDENT_A099_REVIEW_INTEGRATED_CHAIN_OPEN'
save(RUN/'CLAIMS.json',claims);save(RUN/'out/HASH_CONVENTIONS.json',hash_conventions)

dag=read(RUN/'out/PROOF_DEPENDENCIES.json')
nodes={n['claim_id']:n for n in dag['nodes']};assert len(nodes)==len(dag['nodes'])
visited=set();stack=set()
def walk(k):
    assert k not in stack, ('cycle',k)
    if k in visited:return
    assert k in nodes,('missing',k)
    stack.add(k)
    for d in nodes[k]['proof_dependencies']:walk(d)
    stack.remove(k);visited.add(k)
for k in nodes:walk(k)
for n in dag['nodes']:
    if n['claim_id'] in {x['claim_id'] for x in originals}:
        n['review_scope']='A099 HOLDS at exact original scope after independent reconstruction; integrated chain open'
save(RUN/'out/PROOF_DEPENDENCIES.json',dag)

text=(RUN/'CANDIDATE_MANUSCRIPT.tex').read_text(encoding='utf-8')
assert '\\input{' not in text and '\\include{' not in text
assert text.count('\\begin{conjecture}')==4
assert (RUN/'STAGE6_ADDITIONS.tex').read_text(encoding='utf-8') in text
assert not re.search(r'Theorem~\\ref\{(?:lem|cor|prop):',text)
new_claim_fields=set(read(Path('math-open-problems/reports/fei-2026-10-11/EXECUTION_PROTOCOL.json'))['required_per_run']['claim_fields'])
assert all(set(c)==new_claim_fields for c in claims)

# Read and compare all required source pins. A mutable board change is recorded, not falsified.
pins=read(RUN/'out/SOURCE_RECEIPTS.json');changed=[]
for pin in pins:
    p=Path(pin['path']); actual=hashlib.sha256(p.read_bytes()).hexdigest()
    if actual!=pin['sha256']:changed.append({'path':str(p),'old':pin['sha256'],'new':actual})
save(RUN/'out/SOURCE_READBACK.json',{'changed_since_intake':changed,
 'note':'Own rolling status intentionally advances; any mutable-board change is not used to infer new mathematical evidence.'})
assert all(x['path'].endswith('STATUS.md') or x['path'].endswith('BOARD.md') for x in changed)

# One bounded build of the revised source, without downloading anything or spawning detached work.
latex=shutil.which('pdflatex');build={'status':'UNAVAILABLE' if not latex else 'PENDING','timeout_seconds':45}
if latex:
    cmd=[latex,'-interaction=nonstopmode','-halt-on-error','-output-directory='+str(RUN/'out'),str(RUN/'CANDIDATE_MANUSCRIPT.tex')]
    try:
        proc=subprocess.run(cmd,capture_output=True,text=True,encoding='utf-8',errors='replace',timeout=45,
          cwd=RUN,creationflags=getattr(subprocess,'CREATE_NO_WINDOW',0))
        (RUN/'out/TEX_BUILD.txt').write_text(proc.stdout+'\n'+proc.stderr,encoding='utf-8')
        build.update(status='ONE_PASS_COMPLETE' if proc.returncode==0 else 'FAILED',exit_code=proc.returncode)
    except subprocess.TimeoutExpired as e:
        build.update(status='INCOMPLETE_TIMEOUT')
        (RUN/'out/TEX_BUILD.txt').write_text(str(e),encoding='utf-8')
save(RUN/'out/TEX_BUILD.json',build)

lean=read(RUN/'out/LEAN_CORE.json') if (RUN/'out/LEAN_CORE.json').exists() else {'status':'NOT_EXECUTED'}
lean_status=lean.get('status','UNVERIFIED')
if lean.get('stdout'):
    try:lean_status=json.loads(lean['stdout'])['result']['status']
    except (ValueError,KeyError):pass
report=(RUN/'REPORT.md').read_text(encoding='utf-8')
report=report.replace('Status at initial checkpoint: validation pending.',
 f"Executed pilot: {pilot['exact_assertions']} exact assertions PASS in {pilot['seconds']:.3f}s. Full: {full['exact_assertions']} exact assertions PASS in {full['seconds']:.3f}s, 828 root/reference pairs, 2412 singleton queries, 828 adaptive histories and 32 tensor cases. Exact outputs: out/PILOT.json and out/EXACT_TRANSPORT.json.")
report=report.replace('No Mathlib build is authorized by the 1.5GB job limit; a bounded core-Lean bookkeeping check may be used with explicit scope.',
 'No Mathlib build is authorized by the 1.5GB job limit. Core Lean checks only the integer RS2 bookkeeping specialization; receipt status '+str(lean_status)+'. It does not formalize entropy, KL, real-valued reset costs or FEI. The complete transport proof reaches the prose-proof plus independent exact finite-check rung, not full Lean certification.')
report=report.replace('Final validation, artifact hashes and rolling-file updates follow in code/finalize.py.',
 'code/finalize.py validates exact schemas, unchanged original statements and hash conventions, acyclic dependencies, four retained conjectures, source readback and all size ceilings. out/PERSISTENCE_RECEIPTS.json pins the actual artifacts and rolling files. The bounded revised-source PDF build is '+build['status']+'; only the TeX source is the mathematical deliverable, and no PDF visual acceptance is claimed.')
report=report.replace('The local review adds A099 only after successful independent validation.',
 'The local CLAIMS records now add A099 HOLDS at both exact original A096 statement scopes after independent validation; this supplies one scoped review and no integrated acceptance.')
(RUN/'REPORT.md').write_text(report,encoding='utf-8')

p=read(RUN/'PROGRESS.json')
p.update(deliverable_status='COMPLETE_SINGLE_SOURCE_AND_PROTOCOL',mathematical_status='A096_SCOPED_INDEPENDENT_RECONSTRUCTION_UNIVERSAL_FEI_OPEN')
p['mathematical_delta'] += ' Independent 52896-assertion reproduction PASS; no universal constant improvement.'
p['source_artifacts'] += [str(RUN/'out/EXACT_TRANSPORT.json'),str(RUN/'out/LEAN_CORE.json')]
save(RUN/'PROGRESS.json',p);save(RUN/'PACKET_DELTA.json',p)
protocol=read(Path('math-open-problems/reports/fei-2026-10-11/EXECUTION_PROTOCOL.json'))
fields=[x.split(' (')[0] for x in protocol['required_per_run']['progress_fields']]
assert set(p)==set(fields)
assert (RUN/'PROGRESS.json').read_bytes()==(RUN/'PACKET_DELTA.json').read_bytes()
assert p['packet_ids']==['A099']
for heading in protocol['required_per_run']['report_fields']:assert '## '+heading in report
assert report.rsplit('## Universal bridge',1)[1].strip()
(OWN/'STATUS.md').write_text('STATE: A099 v6 single-source assembly saved; A096 full no-reset continuation and constant-child obstruction independently HOLD; 52,896 exact assertions PASS; four universal conjectures and full FEI OPEN.\nNEXT: A097/A094 pay prescribed weak non-flat reset plus channel and both full terminals from SAME unused ancestor account; A085/A094 independently audit integrated chain.\n',encoding='utf-8')
with (OWN/'WORKLOG.md').open('a',encoding='utf-8') as f:f.write('\n'+NOW+': v6 finalized. Independently accepted exact A096 no-reset source scope and constant-child boundary; pilot 2016/full52896 exact assertions PASS (828 root/reference pairs,2412 queries,828 adaptive histories). Signed reset admission Z<=U+r made explicit, with separate channel bill. Four universal leaves and two integrated audits still open. PDF '+build['status']+'; core Lean '+str(lean_status)+' only bookkeeping. No remote copy claimed.\n')
with (OWN/'LEARNED.md').open('a',encoding='utf-8') as f:f.write('\nFor every complete normalized incoming Q supporting P_f, both actual physical children may conservatively inherit its spectral marginal v. Exactly CE_parent=B_j+mean CE_child+conditional occupancy KL. Every finite adaptive no-reset erasure/terminal history therefore telescopes from one original paid reference. This does not construct an O(I) initial model. With U=A-d-T and signed fresh-reference cost Z, final same-account balance is U+refunds-Z; charge channel or label costs separately. Matching three-bit point-defect Q=P still gives a constant child with inherited v=(5/8,1/8,1/8,1/8) and positive log2(8/5) CE at zero influence; local leaf CE/I pricing is false.\n')
assert len((OWN/'STATUS.md').read_text(encoding='utf-8').splitlines())==2
validation={'status':'PASS','claims':len(claims),'dependency_nodes':len(nodes),'universal_conjectures_open':4,
 'exact_assertions':full['exact_assertions'],'source_receipts':len(pins),'source_changes':changed,
 'full_fei':'OPEN','independent_integrated_audits':'BOTH_PENDING','lean_scope':str(lean_status),'pdf_build':build['status']}
save(RUN/'out/FINAL_VALIDATION.json',validation)
receipts=[]
for q in list(RUN.rglob('*'))+[OWN/'STATUS.md',OWN/'WORKLOG.md',OWN/'LEARNED.md']:
    if q.is_file() and q.name!='PERSISTENCE_RECEIPTS.json':
        raw=q.read_bytes();assert len(raw)<20_000_000
        receipts.append({'path':str(q),'bytes':len(raw),'sha256':hashlib.sha256(raw).hexdigest()})
save(RUN/'out/PERSISTENCE_RECEIPTS.json',{'at':NOW,'artifacts':receipts,'remote_mirror':'UNVERIFIED'})
print(json.dumps(validation))
