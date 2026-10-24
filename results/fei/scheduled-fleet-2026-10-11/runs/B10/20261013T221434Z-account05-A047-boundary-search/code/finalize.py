from pathlib import Path
from datetime import datetime,timezone
from fractions import Fraction as Q
import json,hashlib
R=Path(__file__).resolve().parents[1];ROOT=R.parents[1];TEAM=ROOT.parents[1]
P=Path(r'~\mop_fei100\reports\fei-2026-10-11\EXECUTION_PROTOCOL.json')
protocol=json.loads(P.read_text(encoding='utf-8-sig'))
d=json.loads((R/'out/CHECK.json').read_text());pilot=json.loads((R/'out/PILOT.json').read_text());side=json.loads((R/'out/SIDEINFO_BOUNDARY.json').read_text())
assert d['status']=='PASS' and d['trees']==3848 and len(d['closed_chains'])==16 and d['overlap_trees']==512
assert d['assertions']==393251 and pilot['trees']==264 and pilot['runtime_seconds']<60 and d['runtime_seconds']<300
ce=d['half_I_conversion_counterexample'];assert ce['r']==5 and Q(ce['excess_Gamma_minus_I']['lower'])>0 and Q(ce['Gamma_over_2I']['lower'])>Q(1,2)
assert len(side)==16 and Q(side[-1]['ratio_conversion_over_2removed']['lower'])>16000
statement=('For every Boolean sign f under a finite independent interior product law and finite deterministic fresh-coordinate singleton stopping tree with transcript Pi, let R=I_phys(f)-E I_phys(f_leaf). '
 'On the coherent root-spectrum lift, append any finite Z=(W,A) by one conditional root law P(Z|S0) and retain Z->S0->Pi. '
 'With o=I(Y;Pi), j_Z=I(Z;Pi), Gamma_Z=H(Pi|Y)-H(Pi|Z), one has Gamma_Z=j_Z-o, o<=R, j_Z<=4R/ln2, '
 'and o/2+[Gamma_Z]_+/2=max(o,j_Z)/2<=2R/ln2; uniform inputs sharpen j_Z<=2R/ln2 and the joint bound to R/ln2. '
 'Consequently any charge B<=o/2+H(Pi|Y)/2 obeys B<=H(Pi|Z)/2+2R/ln2 (uniform R/ln2). '
 'Compatible fair point-defect computing trees have Gamma_S0/(2I)->3/4, and r=5 certifies Gamma_S0/(2I)>1/2. '
 'Without the root-Markov hypothesis, setting A_future=Pi after the first essential query on fair r-bit point defects makes the conversion/(2R) unbounded. '
 'No conditional-history bank supply, arbitrary reset payment, or universal Fourier entropy-influence bound is established.')
claim={'claim_id':'A047-PAID-COMPATIBLE-CONDITIONING-CONVERSION','version':1,'exact_statement':statement,
 'hypotheses':['finite actual Boolean sign and independent interior product law','physical pivotal influence and actual inherited child spectra','finite deterministic singleton stopping tree with no repeated coordinate on a path','one root conditional witness/side-information append, then same coherent reveal kernel','bits; all terminal Fourier/output balances retained'],
 'statement_sha256':hashlib.sha256(statement.encode()).hexdigest(),'contributors':['A047'],
 'proof_source':['REPORT.md','DERIVATION.md','code/conversion.py','out/CHECK.json','code/sideinfo.py','out/SIDEINFO_BOUNDARY.json','out/HALF_I_COUNTEREXAMPLE.json'],
 'proof_dependencies':[], 'review_records':[],'status':'SCOPED_CONVERSION_PROVED_AND_CERTIFIED_LOCALLY_REVIEW_PENDING','supersedes':[],
 'refutes':['Exploratory universal conversion-only allowance Gamma_+/2<=I/2','Exploratory finite influence bound for arbitrary future-derived side conditioning'],
 'first_unproved_line':'A compatible normalized reference supplies H(Pi|W,A)/2 once and pays signed erasure, descendant resets and full terminal Fourier entropy.',
 'next_consumers':['A092','A087','A088','A039','A050','A064','A097','B10','B20']}
progress={'protocol_revision':protocol['revision'],'run_id':R.name,'stream':'B10','packet_id':'A047','gap_id':'FEI-B10-A047-INITIAL','attempt_id':'A047-boundary-03',
 'method':'coherent root-witness conditioning conversion with one removed-influence account; rare-output endpoint controls; exact rational joint validation',
 'mathematical_delta':'Compatible conversion plus output release costs <=2R/ln2 (uniform R/ln2); essential r5 fair defect refutes half-I conversion; future-side-info conversion is unbounded; 393251 exact main assertions.',
 'deliverable_status':'COMPLETE_LOCAL_ARTIFACT','mathematical_status':'SCOPED_REPAIR_PROVED; REVIEW_PENDING; FULL_FEI_OPEN',
 'claim_versions_used':['A050-OUTPUT-CONDITIONAL-TAX-REPAIR@1 (tax corollary only; independent A046 acceptance read)'],
 'claims_created_or_changed':[claim['claim_id']+'@1'],
 'source_artifacts':['REPORT.md','DERIVATION.md','FROZEN_SPEC.json','FROZEN_SIDEINFO_ENDPOINT.json','code/conversion.py','code/sideinfo.py','out/PILOT.json','out/CHECK.json','out/HALF_I_COUNTEREXAMPLE.json','out/SIDEINFO_BOUNDARY.json'],
 'next_consumers':claim['next_consumers'],'next_action':'Measure first descendant reference/channel injection on the existing three-event exposure tree while preserving one root witness and full terminal Fourier entropy.',
 'stagnant_substantive_attempts':0,'blockers':['Independent review and supervisor mirror pending','Compatible history bank supply and descendant reset payment still unproved'],'packet_ids':['A047']}
assert set(claim)==set(protocol['required_per_run']['claim_fields'])
assert set(progress)=={x.split(' (')[0] for x in protocol['required_per_run']['progress_fields']}
assert all(x in (R/'REPORT.md').read_text(encoding='utf8') for x in protocol['required_per_run']['report_fields'])
(R/'CLAIMS.json').write_text(json.dumps([claim],indent=2),encoding='utf8')
for n in ('PROGRESS.json','PACKET_DELTA.json'):(R/n).write_text(json.dumps(progress,indent=2),encoding='utf8')
assert (R/'PROGRESS.json').read_bytes()==(R/'PACKET_DELTA.json').read_bytes()
assert len((ROOT/'STATUS.md').read_text(encoding='utf8').splitlines())==2
sources=[P,TEAM/'BOARD.md',TEAM/'claude/B10/STREAM_NOTES.md',TEAM/'claude/B13/STREAM_NOTES.md']
for agent,run,names in [('A037','20261011T220010Z-account05-A037-conditional-credit-ledger',['REPORT.md','CLAIMS.json']),('A048','20261012T013822Z-account05-A048-tensor-stress',['REPORT.md','TAX_PAYMENT_LEDGER.tex']),('A050','20261013T212442Z-account05-A050-repair-with-scope',['REPORT.md','PROOF.md','CLAIMS.json','code/check.py']),('A046','20261013T215251Z-account05-A046-current-candidate-intake',['REPORT.md'])]:
    sources.extend(TEAM/'agents'/agent/'runs'/run/name for name in names)
receipts=[{'path':str(p),'sha256':hashlib.sha256(p.read_bytes()).hexdigest(),'bytes':p.stat().st_size} for p in sources]
(R/'out/SOURCE_RECEIPTS.json').write_text(json.dumps(receipts,indent=2),encoding='utf8')
(R/'out/VALIDATION.json').write_text(json.dumps({'protocol_fields':'PASS','progress_copies':'PASS','main_assertions':d['assertions'],'pilot_seconds':pilot['runtime_seconds'],'main_seconds':d['runtime_seconds'],'half_I_strict_certificate':'PASS at r5','future_conditioning_boundary':'PASS r16 ratio>16000','theorem_dependencies':'Elementary lift/channel reconstruction; A050 only in separately declared tax corollary','external_review':'PENDING'},indent=2),encoding='utf8')
files=[]
for p in R.rglob('*'):
    if p.is_file() and p.name!='PERSISTENCE.json' and '__pycache__' not in p.parts:
        assert 0<p.stat().st_size<20*1024*1024
        files.append({'path':str(p.relative_to(R)),'bytes':p.stat().st_size,'sha256':hashlib.sha256(p.read_bytes()).hexdigest()})
rolling=[{'path':str(ROOT/n),'sha256':hashlib.sha256((ROOT/n).read_bytes()).hexdigest()} for n in ('STATUS.md','WORKLOG.md','LEARNED.md')]
(R/'out/PERSISTENCE.json').write_text(json.dumps({'saved_at':datetime.now(timezone.utc).isoformat(),'files':files,'rolling':rolling,'mirror':'NOT_VERIFIED','independent_review':'PENDING'},indent=2),encoding='utf8')
print('PASS: exact protocol keys, progress copy, all requested outputs, strict boundary certificates, source/file receipts;',len(files),'persisted run files')
