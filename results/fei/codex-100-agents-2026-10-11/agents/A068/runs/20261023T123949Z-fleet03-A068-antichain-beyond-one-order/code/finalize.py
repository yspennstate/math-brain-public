from pathlib import Path
import json,hashlib,datetime
R=Path(__file__).resolve().parents[1]; A=R.parents[1]
def read(p):return p.read_text(encoding='utf-8-sig')
def put(p,s):p.write_text(s,encoding='utf-8')
def sha(p):return hashlib.sha256(p.read_bytes()).hexdigest()
def js(p,v):put(p,json.dumps(v,indent=2,ensure_ascii=False)+'\n')
v=json.loads(read(R/'out'/'check.json')); au=json.loads(read(R/'out'/'audit.json'))
assert v['status']==au['status']=='PASS'
assert v['counts']=={'invoice_cases':2304,'physical_marginals':18432,'character_guards':8,'paid_roots':48,'paid_terminals':192}
protocol=Path(r'math-open-problems/reports\fei-2026-10-11\EXECUTION_PROTOCOL.json')
p=json.loads(read(protocol)); req=p['required_per_run']
sources=[protocol,A/'STATUS.md',Path(r'BOARD.md'),Path(r'claude\B14\STREAM_NOTES.md'),A/'runs'/'20261023T065356Z-fleet03-A068-antichain-beyond-one-order'/'REPORT.md']
for a,d in [('A066','20261023T113807Z-fleet03-A066-semigroup-dissipation'),('A097','20261023T121505Z-fleet03-A097-cross-route-transfer')]:
 sources.append(A.parent/a/'runs'/d/'REPORT.md')
js(R/'out'/'SOURCES.json',[{'path':str(s),'sha256':sha(s),'scope':'current intake / prior source; no blanket independent acceptance'} for s in sources])
statement=('For any finite frequency-label group, actual P and original normalized supporting Q, the exact full conversion CE(P,Qbar)-CE(P,Q) equals sum_orbit P(O)[D(P(.|O)||Uniform(O))-D(P(.|O)||Q(.|O))]. Product-control full costs cancel exactly without independence of actual marginals. Product GL blocks of size at most b give a one-time debit at most b I(f), and every later physical marginal is already residual-GL-invariant. For every integer K>=4, arbitrary disjoint Boolean g with original supplied complete Qg of cost Cg<=K Ig, F=t*x*Maj5*g and the original 31-label source q({1})=1-30*2^(-3K), q(other nonempty)=2^(-3K), q(empty)=0 have a paid t-prefix with old booking tau=K Ig-Cg+1/4. Unchanged-source x completion is insolvent. Averaging THIS inherited source under GL5 before x pays that query and both complete terminals from the SAME original owner K(Ig+31/8), leaving 15K/8-log2(31)-1/4>9/4 despite a genuinely noninvariant actual spectrum and zero phase energy. Necessity is for that specified same-rate continuation, not every FEI proof. Full FEI is open.')
claim={k:None for k in req['claim_fields']}
claim.update(claim_id='A068-ORIGINAL-ORBIT-SOURCE-RETURN',version=2,exact_statement=statement,hypotheses=['Finite group and complete normalized original source; zero actual masses contribute zero.','For the paid extension: K integer>=4, independent physical t,x,Maj5,core g; supplied original Qg; eligible old booking tau retained.','No generic arbitrary-core supplier or arbitrary target necessity is assumed.'],statement_sha256=hashlib.sha256(statement.encode('utf-8')).hexdigest(),contributors=['A068','A066 (consumed invariant paid-prefix mechanism; noninvariant extension by A068)'],proof_source='REPORT.md and PROOF.md; exact certificates out/check.json and out/audit.json',proof_dependencies=[],review_records=[{'reviewer':'A068','scope':'author-side independent direct-character implementation; not independent-agent acceptance','result':'PASS'}],status='AUTHOR_PROVED_PENDING_INDEPENDENT_REVIEW',supersedes=['A068-ORIGINAL-ORBIT-SOURCE-RETURN@1'],refutes=[],first_unproved_line=None,next_consumers=['A066','A070','A094','A096','A097','A079'])
js(R/'CLAIMS.json',[claim])
nextact='For an arbitrary supplied inherited core, select a necessary compatible orbit/profile return and pay its exact Phi-minus-mismatch invoice from the SAME diminished original balance after old debits and BOTH full terminals; test growing-block dictator and point-edit guards. A066/A094/A097 review.'
progress={k.split(' (')[0]:None for k in req['progress_fields']}
progress.update(protocol_revision=p['revision'],run_id=R.name,stream='B14',packet_id='A068',gap_id='G-LOWSEL-COLLISION',attempt_id='A068-stage20-noninvariant-orbit-invoice',method='Exact orbit conditional-KL decomposition; source-bound consumption of A066 paid prefix; rank-local physical marginal geometry; exact Boolean certificates',mathematical_delta='Necessary NONINVARIANT zero-energy source handoff paid at SAME K>=4 after actual prefix, arbitrary supplied core, old tau, full terminals; reserve>9/4. Exact general invoice and bounded-block one-time source return. Full FEI OPEN.',deliverable_status='COMPLETE_LOCAL',mathematical_status='SCOPED_AUTHOR_PROOF_COMPLETE;INDEPENDENT_REVIEW_PENDING;FULL_FEI_OPEN',claim_versions_used=['A068-ORIGINAL-ORBIT-SOURCE-RETURN@1 (extended; proof rederived)'],claims_created_or_changed=['A068-ORIGINAL-ORBIT-SOURCE-RETURN@2'],source_artifacts=['out/SOURCES.json','PROOF.md','SPEC.json','AUDIT_SPEC.json','out/check.json','out/audit.json'],next_consumers=claim['next_consumers'],next_action=nextact,stagnant_substantive_attempts=0,blockers=['Arbitrary initial influence-priced source and necessary arbitrary-core compatible target not proved.','Independent-agent review and supervisor mirroring pending.','Brain self-care degraded/unverified: stale personal model, state-of-mind and latest dream; prior document integrity warnings not reverified.'],packet_ids=['A068'])
js(R/'PROGRESS.json',progress); (R/'PACKET_DELTA.json').write_bytes((R/'PROGRESS.json').read_bytes())
report='''# A068 stage20: exact noninvariant orbit invoice and SAME-owner payment

## exact target, quantifiers, hypotheses and units

Extend the already-paid invariant source-return mechanism to a genuinely NONINVARIANT actual spectrum with a real paid prefix. All units bits. The exact all-distribution orbit identity and bounded-block rank reference are proved below. The concrete actual Boolean transaction holds for every integer K>=4 and an arbitrary independent core with SUPPLIED complete Qg<=K Ig; old booking tau, full inherited sources and BOTH full terminal bills remain. Source change is necessary for the specified same-rate continuation, not universally mandatory. Full FEI remains OPEN.

## sources actually read, revisions and theorem locators

Current BOARD, B14 STREAM_NOTES v2 and own stage19 STATUS were read first; protocol 2026-10-11-execution-v2 was read completely. Current A066 stage10 REPORT and A097 stage20 REPORT were read in full. A066's paid t/x prefix and source-refund mechanism are explicitly consumed and extended; A097's declared-floor necessity qualifier is retained. Their statements are not marked independently accepted. Prior baseline campaign/papers/earlier runs remain already-read context, not newly audited dependencies. out/SOURCES.json records current read-source hashes. All new mathematical steps are rederived from definitions, so proof_dependencies=[]; earlier claims are provenance, not unsupported proof premises. Current personal-context brain wake is degraded/unverified (stale personal model, state-of-mind, latest dream; earlier integrity warnings not reverified); those notes supply no theorem or current authorization.

## complete derivation or exact first unsupported line

'''+read(R/'PROOF.md')+'''

## executed validation with domain, arithmetic, commands and outputs

SPEC.json and AUDIT_SPEC.json froze helper/family/domain/count/symmetry/arithmetic/memory/runtime before their respective searches. The primary spec anticipated a stage17 sign helper; the actual orbit-invoice-v1 implementation is self-contained and uses proved rational sign bounds. out/SPEC_ERRATUM.json preserves this metadata correction without changing the original spec, family, domain or arithmetic guarantee. Pilot passed '''+str(json.loads(read(R/'out'/'pilot.json'))['assertions'])+''' assertions. Full primary passed '''+str(v['assertions'])+''' assertions in '''+str(v['seconds'])+''' seconds: all256 Boolean n3 functions, three original references, three block geometries,2304 exact invoice cases and18432 physical marginal checks; eight actual character guards; all16 Boolean n2 supplied cores at K4,5,8,48 physical roots and192 complete terminals. No symmetry quotient or dimension increase. All full spectra are integer Walsh/Fraction; physical edge influences are computed independently; full CE/KL identities are exact prime-log coefficient maps, and strict signs follow proved rational/log bounds, never floating signs. The pilot is not added to full counts.

Independent author-side audit passed '''+str(au['assertions'])+''' assertions in '''+str(au['seconds'])+''' seconds, using DIRECT character sums on Maj5 and t*x*Maj5 with NO primary/helper imports. It checks the actual transvection noninvariance, full product spectrum and all original-owner rational bounds. This is a different representation, not independent-agent acceptance or compiler/Lean certification. The all-K/all-core theorem follows the displayed proof, not finite extrapolation. Commands: `python -B -X utf8 RUN/code/check.py --pilot`; same without --pilot; `python -B -X utf8 RUN/code/audit.py`, where RUN is this directory. Frozen main55s/audit40s, estimates70/20MB, no >300MB job, heavy job, GPU, detached/windowed work or other-work intervention. Shell/host latency is separate from saved checker runtime. No current compute-health claim is inferred from stale governor snapshots.

## proof dependencies and changed downstream conclusions

Version2 extends A068-ORIGINAL-ORBIT-SOURCE-RETURN@1; prior vacuum-only obstruction and SAME25 private-literal cut remain unchanged. A066's invariant payment is no longer a barrier for this particular noninvariant Maj5 replacement: the exact entropy deficit log31-H(Maj5)>0 is included and is paid by ORIGINAL source mismatch credit. The arbitrary-core Qg remains supplied, not synthesized. Rank-local regularization preserves residual physical source shape at every adaptive path but pays neither remaining query/channel invoices nor occupancy calibration. A dictator guard proves unbounded block sizes cannot be given a universal free tariff. This is a scoped supporting extension, not another broad unreviewed universal candidate. No improvement to a universal FEI constant is claimed.

## one next mathematical action and independent reviewer

'''+nextact+'''

These are named source-bound next consumers, not messages sent, delivered review requests or acceptance receipts.

## actual persistence receipts or precise save blocker

Four exact-field protocol files, full proof, frozen specifications, primary/independent code and outputs are saved inside A068. out/RECEIPTS.json checks hashes, fields, statement hash, progress/delta byte identity, two-line STATUS and every file below20MB. WORKLOG and LEARNED append this stage. No git/mail/shared-tree/other-agent/brain-store mutation or deletion. Supervisor copying, mirror verification and independent review remain unverified; no publication receipt is claimed. No job is left running at completion.

## Universal bridge

C024 history transfer/C019 stopping-tree payment moves the consumed necessary isospectral handoff beyond actual orbit invariance: a genuinely NONINVARIANT Maj5 return after a real paid t-prefix is paid by the SAME original K>=4 account with old tau and BOTH full terminals, leaving>9/4 bits. The exact general liability is Phi minus ORIGINAL conditional mismatch credit; bounded-block GL geometry gives one-time <=bI source regularization with zero repeat residual-shape cost. The universal gain is0: an arbitrary initial supplier and a necessary compatible arbitrary-core return whose exact liability fits the diminished original account remain unpaid. NEXT targets that invoice with dictator/point-edit guards rather than repeating finite symmetric reset cycles, because source selection and payment are the surviving universal bridge.
'''
put(R/'REPORT.md',report)
put(A/'STATUS.md','STATE: Stage20: necessary NONINVARIANT Maj5 orbit handoff PAID SAME K>=4 after real prefix, old tau/full terminals; reserve>9/4; exact Phi-mismatch invoice; FEI OPEN.\nNEXT: '+nextact+'\n')
stamp=datetime.datetime.now(datetime.timezone.utc).isoformat()
for file,line in [('WORKLOG.md',f'{stamp} {R.name}: consumed A066 invariant payment; exact noninvariant orbit invoice, one-time bounded-block rank source return, necessary Maj5 same-owner payment. Primary {v["assertions"]} and direct audit {au["assertions"]} assertions PASS; pilot separate. Full FEI and independent review OPEN.'),('LEARNED.md','Stage20: Orbit-source conversion is EXACTLY sum P(O)[D(Pcond||UniformO)-D(Pcond||Qcond)], so a noninvariant spectrum need not block a paid return. Product GL blocks <=b cost at most bI ONCE and all physical marginals keep residual GL shape. Concrete t*x*Maj5*g with original peaked31-label source epsilon2^(-3K), arbitrary supplied Qg<=KIg, old tau=KIg-Cg+1/4: paid t, unchanged x insolvent, original orbit averaging then BOTH x children leave15K/8-log31-1/4>9/4 for every integer K>=4. Actual Phi>0 retained; no phase/vacuum refund invented. Dictator full-GL cost log(2^n-1) forbids free growing blocks. Necessary here means that prescribed same-rate continuation; arbitrary-source/general target payment remains open.')]:
 old=read(A/file)
 if line not in old:put(A/file,old.rstrip()+'\n\n'+line+'\n')
assert set(claim)==set(req['claim_fields'])
assert set(progress)=={s.split(' (')[0] for s in req['progress_fields']}
for h in req['report_fields']:assert '## '+h in report
assert (R/'PACKET_DELTA.json').read_bytes()==(R/'PROGRESS.json').read_bytes()
assert len(read(A/'STATUS.md').splitlines())==2
assert claim['statement_sha256']==hashlib.sha256(claim['exact_statement'].encode('utf-8')).hexdigest()
files=[f for f in R.rglob('*') if f.is_file() and f.name!='RECEIPTS.json']
assert all(f.stat().st_size<20*1024*1024 for f in files)
js(R/'out'/'RECEIPTS.json',{'status':'PASS','files':[{'path':str(f.relative_to(R)),'sha256':sha(f),'bytes':f.stat().st_size} for f in files],'rolling':[{'path':str(A/f),'sha256':sha(A/f)} for f in ['STATUS.md','WORKLOG.md','LEARNED.md']],'statement_sha256':claim['statement_sha256'],'progress_delta_identical':True,'independent_review':'pending','remote_mirror':'unverified'})
print(json.dumps({'status':'PASS','primary_assertions':v['assertions'],'independent_author_assertions':au['assertions'],'report_sha256':sha(R/'REPORT.md'),'files':len(files),'full_fei':'OPEN'}))
