from pathlib import Path
import json,hashlib,datetime
R=Path(__file__).resolve().parents[1]; A=R.parents[1];O=R/'out'
now=datetime.datetime.now(datetime.timezone.utc).isoformat()
run=R.name
cert=json.loads((O/'CERTIFICATE.json').read_text(encoding='utf-8'))
peer=Path('agents/A096/runs/20261027T055827Z-account04-A096-live-gap-ledger')
pc=json.loads((peer/'CLAIMS.json').read_text(encoding='utf-8-sig'))
deps=[{'claim_id':c['claim_id'],'version':c['version'],'statement_sha256':c['statement_sha256']} for c in pc[1:]]
nextaction='A096/A050/A097/A094 review the three-component certificate, then derive its actual phase/outcome-dependent physical branch transport with the SAME original account, or supply the arbitrary-core O(I) initial source. Coordinate deletion alone fails on AND2.'
claims=[]
for c in pc[1:]:
 cc=dict(c)
 cc['proof_source']={'external':str(peer/'DERIVATION.md'),'source_sha256':c['proof_source']['sha256'],'reconstruction':'DERIVATION.md section1 in this A082 run','checks':'out/CERTIFICATE.json'}
 cc['review_records']=list(c['review_records'])+[{'reviewer':'A082','verdict':'HOLDS_AT_STATED_SUPPLIED_SOURCE_SCOPE','reconstruction':'DERIVATION sections1 and3; independent integer root polynomial, sharper1/2<x<1 bracket, direct Boolean FWHT and n2 endpoint','checks':'out/CERTIFICATE.json','limits':'No arbitrary-core supplier or full physical closure of the new compressed class accepted.'}]
 cc['status']='INDEPENDENT_RECONSTRUCTION_BY_A082_HOLDS_AT_STATED_SCOPE'
 claims.append(cc)
statement='For every integer n>=1 and real x>0, let M=2^n, Z=(1+x)^n-1+M*x^n, u(empty)=1/M and u(S)=(M-1)*x^|S|/(M*Z) for proper nonempty S, with the full-set mass multiplied by M+1. Then u is the nonnegative mixture a*delta_empty+b*Bplus(n,x)+c*delta_full with a=1/M, b=(M-1)*((1+x)^n-1)/(M*Z), c=(M-1)*x^n/Z and Bplus(S)=x^|S|/((1+x)^n-1) on nonempty subsets. Deleting k<n coordinates pushes Bplus to alpha*delta_empty+beta*Bplus(n-k,x), alpha=((1+x)^k-1)/((1+x)^n-1), beta=(1+x)^k*((1+x)^(n-k)-1)/((1+x)^n-1). Thus at most three such nonnegative components suffice under every deletion history; deleting all coordinates gives delta_empty. On the A096 AND2 tensor moment-projection root at every even n>=4, the unique root satisfies1/2<x<1 and the individual-atom minimum remains2^n-n. Coordinate deletion cannot be substituted for physical branch spectra: AND2 has uniform four-atom spectrum but its two children are delta_empty and delta_singleton. No universal source price, useful required stopping condition, or full physical branch closure is asserted.'
claims.append({'claim_id':'A082-THREE-COMPONENT-DELETION-CERTIFICATE','version':1,'exact_statement':statement,'hypotheses':['Finite subset alphabet; real x>0; Bplus denotes product-cardinality law conditioned nonempty.','Deletion is pushforward on frequency labels, not asserted full physical Boolean branch transport.','Root and atom-count clause restricted to specified A096 even-n AND2 tensor family; n2 excluded.'],'statement_sha256':hashlib.sha256(statement.encode()).hexdigest(),'contributors':['A082; A096 specified projection family and atom-count theorem credited'],'proof_source':{'files':['DERIVATION.md','code/check.py','out/CERTIFICATE.json','out/FROZEN_SPEC.json']},'proof_dependencies':deps,'review_records':[],'status':'ELEMENTARY_PROOF_EXACT_CERTIFICATES_PENDING_INDEPENDENT_REVIEW_NOT_LEAN_CHECKED','supersedes':[],'refutes':['Inference that exponential individual-atom count forces exponential component count in every richer reference class.','Substitution of coordinate deletion for full physical branch spectrum, even on AND2.'],'first_unproved_line':None,'next_consumers':['A096','A050','A097','A085','A094','A099','B17','B20']})
(R/'CLAIMS.json').write_text(json.dumps(claims,indent=2),encoding='utf-8')
p={'protocol_revision':'2026-10-11-execution-v2','run_id':run,'stream':'B17','packet_id':'A082','gap_id':'G-R-MISMATCH-C024-PRESCRIBED-RESET','attempt_id':'A082-stage22-independent-moment-certificate-and-compression','method':'Independent integer polynomial root certificate, exact Boolean FWHT, nonnegative structured decomposition and physical-query negative control','mathematical_delta':'A096 free projection and sharp atom count reconstruct unchanged. New sharper root bracket1/2<x<1 and exact three-component deletion closure separate atom count from description complexity. Final487 exact assertions PASS; full physical branch transport remains unpaid.','deliverable_status':'COMPLETE_LOCAL_ARTIFACT','mathematical_status':'SCOPED_A096_AUDIT_HOLDS_NEW_NARROW_CERTIFICATE_REVIEW_PENDING_FULL_FEI_OPEN','claim_versions_used':deps,'claims_created_or_changed':[{'claim_id':c['claim_id'],'version':c['version'],'change':'Independent scoped review' if i<2 else 'New narrow structured compression certificate'} for i,c in enumerate(claims)],'source_artifacts':['DERIVATION.md','out/SOURCE_RECEIPTS.json','out/FROZEN_SPEC.json','out/CERTIFICATE.json','FORMAL_TARGET.lean'],'next_consumers':['A096','A050','A097','A085','A094','A099','B17','B20'],'next_action':nextaction,'stagnant_substantive_attempts':0,'blockers':['Physical reference transport includes actual branch likelihoods and phase; coordinate deletion does not supply it.','Original arbitrary-core O(I) source and useful necessary stopping/terminal condition remain unpaid; FEI OPEN.','Fresh memok returned WAIT: physical0.9GB/commit0.1GB free. Lean not launched; saved algebraic target is uncompiled.','Independent review of new compression, supervisor adoption and mirrors unverified.'],'packet_ids':['A082']}
for name in ['PROGRESS.json','PACKET_DELTA.json']:(R/name).write_text(json.dumps(p,indent=2),encoding='utf-8')
report=f'''# A082 stage22: finite projection certificates and structured residuals

## exact target, quantifiers, hypotheses and units

Independently certify A096's supplied-source moment projection and exact atom count for EVERY even n>=4; determine whether that count also forces large structured descriptions. All CE/entropy units bits. The richer law is a three-component mixture for EVERY real x>0 and survives EVERY coordinate-deletion history. Full physical-query closure is separately tested and remains unpaid. Full FEI OPEN.

## sources actually read, revisions and theorem locators

Current BOARD20261027T0902, B17 STREAM_NOTES v2, own STATUS/LEARNED and stage21 complete REPORT/CLAIMS/DERIVATION/PROGRESS; execution protocol2026-10-11-execution-v2 read in full. Required canonical/advisory files and four paper texts were explicitly decoded by code/intake.py, with hashes/encoding in out/SOURCE_RECEIPTS.json. This machine intake is navigation, not a new independent audit of all those texts. One source used cp1252 because UTF8 decoding failed; no source was edited. The substantive new dependency read in full is A09620261027T055827Z REPORT/CLAIMS/DERIVATION sections2--3, exact statement hashes pinned in CLAIMS. Old five-bit census assignment is already complete and is not repeated. Brain recall returned adjacent FEI cautions but no new premise used here. No outside literature theorem is required.

## complete derivation or exact first unsupported line

DERIVATION gives the complete finite proofs. A096's information-projection identity and2^n-n individual-atom lower bound reconstruct at stated scope without repair. The independent root polynomial yields the stronger all-even-n bracket1/2<x<1. The calibrated law is exactly a nonnegative mixture of vacuum, nonempty-conditioned product-cardinality law, and full-set atom. This has at most three components after ANY frequency-coordinate deletion. The all-dimensional exhaustiveness theorem is stated separately: binomial and atomwise identities hold for all real parameters and dimensions; finite tests do not imply them. A real AND2 physical query has two point-law child spectra rather than its uniform deleted spectrum. FIRST UNSUPPORTED LINE: construct and price actual phase/outcome-dependent physical transport of a useful structured arbitrary-core reference, retaining full query loss and all terminals, or supply the original O(I) source. No fixed atom-count FEI necessity is asserted.

## executed validation with domain, arithmetic, commands and outputs

Frozen spec written before each bounded check. Command: python -X utf8 code/check.py. Initial pilot PASS483 assertions/168 compression profiles; its advertised case-count typo140 was corrected to168 without expanding the domain. Final v2 adds two physical children: PASS{cert['assertions']} exact assertions,16 root cases,168 compression/deletion profiles in{cert['elapsed_seconds']:.3f}s. Integer/Fraction arithmetic only;64 rational bisections per nontrivial root and independently expanded integer polynomials; direct actual Boolean FWHT at n2,4,6; n2 endpoint u=P checked exactly. Root tests n2..32 even and compression n2..8 at four frozen rational tilts do not exhaust arbitrary n; the symbolic derivation does. Estimated70MB,55s cap, no escalation/GPU/detached job. Fresh memory admission said WAIT, physical0.9GB/commit0.1GB free, so no Lean compiler or >300MB job was launched. FORMAL_TARGET.lean is an UNCOMPILED algebraic substep, not a certificate. Verification rung: elementary proof plus exact certificates; independent review pending for new compression.

## proof dependencies and changed downstream conclusions

Two exact A096 versions/hashes are independently reviewed HOLDS at supplied-source scope. Root bound strengthens its certificate without changing its theorem. New compression depends on the explicit family only. Exponential individual-atom count remains true and does not establish exponential component count in a richer class. Conversely deletion closure does not establish full physical branch closure. All original-account, scalar-mass, old-debit, query-loss and both-terminal requirements remain. No universal FEI constant improves.

## one next mathematical action and independent reviewer

{nextaction}

## actual persistence receipts or precise save blocker

All four protocol files, full derivation, frozen domain, scripts and exact output saved in A082. Rolling STATUS has exactly two lines; WORKLOG/LEARNED appended. out/PERSISTENCE_RECEIPTS.json checks schema fields, statement hashes, compatibility bytes, actual file sizes and readback hashes. Supervisor/mirror/adoption receipts unverified. No git/mail/messages/shared-research-tree/brain-store/trading changes, no deletions, no work stopped or throttled. The mandatory session wake reported stale personal-context notes; alert surfaced and those notes were not mathematical premises. Checklist lifecycle uses the required system hook only; research writes stay in A082.

## Universal bridge

C024 history transfer inside C019/C020 feeding C018 gains an independently checked source-projection boundary and an explicit compressed alternative to exponentially many atoms. The specified supplied-source family has three nonnegative components under every frequency deletion even though its atom minimum is2^n-n; the first missing operation is actual physical branch transport, exposed by an exact AND2 negative control. Numerical improvement to full FEI is zero. An ORIGINAL arbitrary-core O(I) source, useful mandatory stopping certificate and phase-sensitive hereditary residual price remain open. NEXT attacks the missing physical operation or initial supplier directly, rather than repeating the now-closed finite atom census or an optional reset.
'''
(R/'REPORT.md').write_text(report,encoding='utf-8')
(A/'STATUS.md').write_text('STATE: Stage22 saved: A096 projection/atom count independently HOLDS; sharper root1/2<x<1; three-component deletion closure;487 exact checks PASS; physical branch substitution fails on AND2;FEI OPEN.\nNEXT: '+nextaction+'\n',encoding='utf-8')
for name,msg in [('WORKLOG.md','Stage22: consumed A096 new projection dependency, independently reconstructed root/count; certified three-component nonnegative deletion closure and exact AND2 physical-branch negative control. Final487 exact assertions PASS. Compiler admission held; no heavy job, no stopped work. Full FEI OPEN.'),('LEARNED.md','For A096 even-n AND2 tensor projection, the tilt root satisfies1/2<x<1 (at1/2 conditional mean/n=1/3+(2/3)^n), simplifying the exact2^n-n atom count. Yet u is a nonnegative mixture of vacuum, conditioned-nonempty product-cardinality law, and full atom; three components survive every coordinate deletion. Atom count is not general description complexity. Full physical branches involve phase: AND2 children are two point spectra while deletion gives a uniform two-atom law. Neither this compression nor free moment matching prices an arbitrary initial source.')]:
 if msg not in (A/name).read_text(encoding='utf-8'):
  with (A/name).open('a',encoding='utf-8') as f:f.write('\n'+now+': '+msg+'\n')
protocol=json.loads(Path('math-open-problems/reports/fei-2026-10-11/EXECUTION_PROTOCOL.json').read_text(encoding='utf-8'))
req=protocol['required_per_run']
expected={s.split(' (')[0] for s in req['progress_fields']}
assert set(p)==expected
for c in claims:
 assert set(c)==set(req['claim_fields'])
 assert hashlib.sha256(c['exact_statement'].encode()).hexdigest()==c['statement_sha256']
assert all(x in report for x in req['report_fields'])
assert (R/'PROGRESS.json').read_bytes()==(R/'PACKET_DELTA.json').read_bytes()
assert len((A/'STATUS.md').read_text(encoding='utf-8').splitlines())==2
receipts=[]
for f in sorted(R.rglob('*')):
 if f.is_file() and f.name!='PERSISTENCE_RECEIPTS.json':
  b=f.read_bytes();assert len(b)<20*1024*1024
  receipts.append({'path':str(f.relative_to(R)),'bytes':len(b),'sha256':hashlib.sha256(b).hexdigest()})
(O/'PERSISTENCE_RECEIPTS.json').write_text(json.dumps({'at':now,'status':'PASS_LOCAL_READBACK_SCHEMA_HASHES','files':receipts,'mirrors':'UNVERIFIED'},indent=2),encoding='utf-8')
print(json.dumps({'status':'PASS_LOCAL_ARTIFACT','files_checked':len(receipts),'assertions':cert['assertions'],'full_fei':'OPEN'}))
