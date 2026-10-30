import sys,json,hashlib,platform
from pathlib import Path
from datetime import datetime,timezone
R=Path(__file__).resolve().parents[1];HOME=R.parents[1]
SOURCE=HOME.parent/'A067'/'runs'/'20261023T015109Z-fleet03-A067-hypercontractive-refinement'
OLD=HOME/'runs'/'20261022T215524Z-fleet03-A088-booleanity-referee'
BASE=Path('~/brain_workers/FEI100_20261011')
PROTO=Path('math-open-problems/reports/fei-2026-10-11/EXECUTION_PROTOCOL.json')
def read(p):return p.read_text(encoding='utf-8-sig')
def load(p):return json.loads(read(p))
def save(p,data):p.write_text(json.dumps(data,indent=2,ensure_ascii=False)+'\n',encoding='utf-8')
def sha(p):return hashlib.sha256(p.read_bytes()).hexdigest()
proof=R/'PROOF.md';check=load(R/'out'/'CHECK.json');scope=load(R/'out'/'REAL_SCOPE.json')
assert check['status']==scope['status']=='PASS'
source_claim=next(c for c in load(SOURCE/'CLAIMS.json') if c['claim_id']=='A067-EDITED-INTACT-PAIR-CONDITIONAL-SOURCE-TRANSFER')
assert hashlib.sha256(source_claim['exact_statement'].encode('utf-8')).hexdigest()==source_claim['statement_sha256']
original_hash=source_claim['statement_sha256']
source_claim['review_records'].append({
 'reviewer':'fleet03/A088','verdict':'HOLDS_AT_EXACT_CANONICAL_SELECTED_HISTORY_SCOPE',
 'independent':True,'substantive_repair':False,'source':str(proof),
 'source_proof_sha256':sha(SOURCE/'PROOF.md'),'source_statement_sha256':original_hash,
 'method':'Independent literal Walsh/physical edges and direct original-spectrum marginalization; separate grouped finite-sum reconstruction and exact log intervals; no source helper imported',
 'validation':[str(R/'out'/'CHECK.json'),str(R/'out'/'REAL_SCOPE.json')],
 'note':'Previous source-family attribution and clean-history background remain credited. No repair or strengthening of the reviewed source statement. Positive partner payment remains outside its scope.'})
source_claim['status']='INDEPENDENTLY_ACCEPTED_AT_STATED_SCOPE_LOCAL_RECEIPT'
save(R/'CLAIMS.json',[source_claim])
progress=load(OLD/'PROGRESS.json')
progress.update({
 'run_id':R.name,'attempt_id':'A088-edited-source-review-and-positive-partner-objection-v1',
 'method':'Independent exact Boolean source audit; quantitative residual-only payment obstruction; actual normalized real commuting-phase diagnostic',
 'mathematical_delta':'A067 intact-pair source-transfer v1 independently HOLDS unchanged. Next actual exposed-partner debit is positive; combined E>r for every m>=2, E>=99/640 for m>=4, and E/r diverges. Full CE and terminal KL retained. A real nonBoolean commuting-phase guard preserves all seven tested node spectra and Dirichlet energies. Full FEI OPEN.',
 'deliverable_status':'COMPLETE_LOCAL_SOURCE_BOUND_HANDOFF',
 'mathematical_status':'SOURCE_REVIEW_HOLDS_EXACT_SCOPE_RESIDUAL_ONLY_EXTENSION_FALSE_FULL_FEI_OPEN',
 'claim_versions_used':[
  {'claim_id':source_claim['claim_id'],'version':1,'statement_sha256':original_hash},
  {'claim_id':'A067-POSTCORE-BENT-FLAG-SAME-CHILD-BANK','version':1,'statement_sha256':'c8972812430c4b66c2874a9746d9fe2f5305397434ca62d56dc42755c2c3bee1'},
  {'claim_id':'A088-CANONICAL-CLEAN-HISTORY-SIGNED-TRANSPORT','version':1,'scope_used':'Only the proved all-m original residual upper bound in prior PROOF section 1; reproduced here'}],
 'claims_created_or_changed':[{'claim_id':source_claim['claim_id'],'version':1,'status':source_claim['status']}],
 'source_artifacts':[str(proof),str(R/'out'/'CHECK.json'),str(R/'out'/'REAL_SCOPE.json'),str(SOURCE/'PROOF.md'),str(SOURCE/'CLAIMS.json')],
 'next_consumers':['A067','A070','A094','A096','B14','B18','B20'],
 'next_action':'A067/A070/A094: price the SAME exposed-partner profile using a genuinely additional source or an allowed total-rate bound, with old D, original references, both full children and full terminal KL. Fixed residual plus prior intact-query credit is quantitatively insufficient; no further telescope-only payment.',
 'stagnant_substantive_attempts':0,
 'blockers':['Full FEI and arbitrary-core history payment OPEN','Residual-only positive-partner extension disproved; no additional funded conversion source yet','Independent review of the new narrow obstruction/real gauge and supervisor mirror adoption unverified','Owner-model/state-of-mind memory stale: brain self-care degraded/unverified; not used as mathematical premises'],
 'packet_ids':['A088']})
save(R/'PROGRESS.json',progress);save(R/'PACKET_DELTA.json',progress)
report='''# exact target, quantifiers, hypotheses and units

Audit A067-EDITED-INTACT-PAIR-CONDITIONAL-SOURCE-TRANSFER@1 for every canonical G_m, m>=2, using physical uniform-cube influences and base-two full spectral entropy/CE/KL. Independently verify its exact original-reference conditional law, signed intact-query credit, both actual child bills and old D. Then test its nearest unpaid exposed-partner query against the same original residual. Full FEI remains OPEN.

# sources actually read, revisions and theorem locators

At this stage's start, current BOARD (02:53 UTC), B18 STREAM_NOTES v2 and own STATUS were read. A067 stage18 STATUS, complete run20261023T015109Z REPORT/PROOF/CLAIMS, and previous A088 run20261022T215524Z PROOF/checker/PROGRESS supply the current dependency. Execution protocol v2 was read in full; its obsolete campaign end is superseded by the owner's 2026-10-23 14:49 UTC order. Earlier required campaign/supplement/paper baseline reads are inherited, not represented as new proof review. The read-only three-wording math recall returned an older bent-splice draft and unrelated cards; no recalled draft is a theorem premise. Current source bytes and helper revisions are pinned in out/SOURCES.json. The owner-model and state-of-mind notes are stale; brain self-care is degraded/unverified and those personal-context notes are not used.

# complete derivation or exact first unsupported line

PROOF1 reconstructs the actual Boolean prefixes and direct marginals of the ORIGINAL c_m law. The source likelihood ratio is constant on every next intact-pair Fourier fiber, so full CE drop is its true binary erasure and the physical marked-edge influence proves the stated negative debit. Source statement/hash unchanged; independent verdict HOLDS without repair. The signed terminal-bank telescope is existing background. Negative inherited exit banks are retained.

PROOF2--4 gives the next exposed-partner profile, both actual child bills, and the exact scalar proposal E<=r where E=e0/2+e1/4. This unregistered proposed extension is FALSE: E>r for every m>=2. For m>=4, E>=99/640>1/8>7/128>r by a short analytic inequality; m=2,3 have exact rational interval certificates. Moreover E->1/4 and r->0, so no fixed multiple of that residual alone pays this extension uniformly. This is a route obstruction, not a refutation of A067 or FEI. The complete bank still changes by E in the exact no-reset identity. The partner entropy debit is positive at all four literal dimensions; KL release does not pay its full reference debit alone.

PROOF5 tests the strongest implemented nonBoolean relaxation: a real orthogonal Fourier phase multiplier on an untouched pair commutes with every physical query in this experiment. It preserves all root and child norms, full spectra, inherited references, entropy and Dirichlet influences while destroying Booleanity at all seven nodes. The exact guard exhibits a nonempty phase convolution -15/16. Thus the two-query scalar payment calculation does not use full Boolean phase equations once its profiles are supplied. The source's complete all-pair history is NOT extended by that commuting argument.

The first unsupported universal line remains a genuinely funded conversion of positive occupancy-changing CE/actual entropy debit with signed terminal banks and full KL, or a specified paid reset. Paying it from the old residual plus the preceding credit is now excluded quantitatively. No broad new candidate is opened while prior B18 candidates await review; the new results are this source review's exact objection and scope diagnostic.

# executed validation with domain, arithmetic, commands and outputs

FROZEN_SPEC.json precedes the pilot and full job. Commands are python -X utf8 -B code/check.py pilot and full from the run. Pilot: 248 exact predicates PASS in 0.0149 seconds at m=2. After this successful pilot, log endpoints were rounded outward to 2^-90 before accumulation to bound rational denominator size; the 28-term positive atanh series and proved tail remain the same. The final full helper passed COUNT exact predicates in SECONDS seconds: 18 literal depths m=2..5, 14 actual intact queries, 150 grouped depths m=2..16, and 15 positive-partner profiles. Original references are reconstructed directly from the initial Walsh spectrum. No source helper is imported, and no floating sign is accepted.

REAL_SCOPE_SPEC.json precedes the independent direct-character guard. Command python -X utf8 -B code/real_scope.py: 59 exact predicates PASS in 0.2202 seconds; seven actual normalized nonBoolean root/child nodes, every full spectral law and physical Dirichlet energy, and failed nonempty Boolean convolutions. Main estimate 96MB/180s, guard 25MB/55s; no heavy job, GPU, automatic dimension escalation or detached job. No Lean compiler certificate is claimed.

# proof dependencies and changed downstream conclusions

The reviewed source claim is v1 with unchanged hash f7d1b7a7081a210246b0a73a236a981f43d499018500bb8ce95ca2716819e3f1. It depends on independently accepted canonical post-core source v1. The prior A088 residual upper bound is reproduced, so the obstruction does not depend on an unexplained external estimate. CLAIMS.json records only the independently reviewed source version; the unregistered residual-only extension is not promoted into a campaign theorem or attributed to A067. The original full ledger and its scope are intact. The new real relaxation refines Booleanity scope, not source validity.

# one next mathematical action and independent reviewer

A067/A070, with A094 as scope challenger, should identify an additional legitimate source or total-rate inequality for this exact occupancy-changing profile, retaining old D, original references, diminished credit, both full children and terminal KL. Any claimed payment must beat the explicit E/r divergence; another no-reset identity or a KL-only refund is insufficient. The review files are a local source-bound handoff; no message or other agent's file was written.

# actual persistence receipts or precise save blocker

The four exact protocol files, complete proof, frozen specifications, independent scripts and certificate outputs are saved in this run. STATUS has exactly STATE/NEXT; WORKLOG and LEARNED are appended. out/PERSISTENCE_RECEIPTS.json verifies schemas, byte identity of the two progress files, statement hash, UTF-8 readback and file sizes. Local persistence is complete; supervisor copy, mirror adoption and independent review of the narrow obstruction/real relaxation are unverified. Did: accepted the exact source claim and saved a quantified next-payment obstruction. Stopped: no computation remains active. Left running: nothing started by A088.

# Universal bridge

C024 history transfer and C019 stopping payment advance by an independent acceptance of the canonical all-intact-pair history, followed by an exact obstruction at its first occupancy-changing query: root-weighted new debit E exceeds the original residual for every m>=2, with E>=99/640 for m>=4 and E/r diverging. The complete original-reference signed ledger still balances; no universal influence-priced conversion or additional payment source is proved. The real phase guard shows why that finite ledger alone cannot supply missing Boolean phase control. NEXT seeks a legitimate additional source or total-rate inequality on this SAME history, rather than another isolated family entropy bound, because it must overcome the actual first unpaid step while retaining full terminal entropy and KL.
'''.replace('COUNT',str(check['checks'])).replace('SECONDS',str(round(check['runtime_seconds'],6)))
(R/'REPORT.md').write_text(report,encoding='utf-8')
stamp=datetime.now(timezone.utc).isoformat()
(HOME/'STATUS.md').write_text('STATE: A088 stage18: A067 edited intact-pair v1 independently HOLDS; next partner E>r all m>=2, E/r diverges; normalized real phase guard; exact checks PASS; FEI OPEN.\nNEXT: A067/A070/A094: fund SAME positive partner using additional source or total-rate bound; old D, original references, both full children and full terminal KL; residual-only and KL-only shortcuts fail.\n',encoding='utf-8')
with (HOME/'WORKLOG.md').open('a',encoding='utf-8') as f:f.write('\n'+stamp+' | '+R.name+' | Independently accepted A067 intact-pair source-transfer v1 unchanged; '+str(check['checks'])+' +59 exact predicates PASS. Next partner e1->1; root-weighted E>r all m>=2, E>=99/640 m>=4, E/r diverges. Actual real commuting-phase transform preserves all seven experiment nodes and full Dirichlet/spectral ledgers. Full KL retained, no FEI claim. NEXT additional funded source/total-rate bound; no work left running.\n')
with (HOME/'LEARNED.md').open('a',encoding='utf-8') as f:f.write('\n'+stamp+' | Edited-partner scope lesson: with original c_m reference after a=0, Q1(W=0,b=0)=2(A^2+A^4-2A^3 sigma), Q1(b=1)=2(A^2+A^4), Q2=4(A^2+A^4-A^3 sigma). Partner Inf=2A^2; e1=sum P1 log2(Q2/Q1)-4A^2 tends1. Intact e0 tends0; original root reaches give E=e0/2+e1/4->1/4, while r<delta(m-1/4)->0. E>=99/640 m>=4; exact m2,3 also E>r. This refutes fixed-residual withdrawals, not signed bank transport or FEI. A real T=Id-2 E_R on an untouched pair commutes with queries outside R and preserves every actual child spectrum/norm/Dirichlet influence while destroying Booleanity. Full queried-pair histories need separate treatment. Source accepted unchanged f7d1b7a7081a210246b0a73a236a981f43d499018500bb8ce95ca2716819e3f1.\n')
source_paths=[PROTO,BASE/'BOARD.md',BASE/'claude'/'B18'/'STREAM_NOTES.md',SOURCE/'PROOF.md',SOURCE/'REPORT.md',SOURCE/'CLAIMS.json',OLD/'PROOF.md',OLD/'PROGRESS.json',proof,R/'FROZEN_SPEC.json',R/'REAL_SCOPE_SPEC.json',R/'code'/'check.py',R/'code'/'real_scope.py',R/'code'/'finish.py']
save(R/'out'/'SOURCES.json',{'timestamp_utc':stamp,'python':platform.python_version(),'source_bindings':[{'path':str(p),'bytes':p.stat().st_size,'sha256':sha(p)} for p in source_paths]})
p=load(PROTO)['required_per_run'];fields=set(p['progress_fields']);fields.remove('packet_ids (one primary ID, for compatibility)');fields.add('packet_ids')
assert set(progress)==fields
assert set(source_claim)==set(p['claim_fields'])
assert (R/'PROGRESS.json').read_bytes()==(R/'PACKET_DELTA.json').read_bytes()
for h in p['report_fields']:assert '# '+h in read(R/'REPORT.md')
assert read(R/'REPORT.md').rfind('# Universal bridge')>read(R/'REPORT.md').rfind('# actual persistence')
assert len(read(HOME/'STATUS.md').splitlines())==2
files=[]
for f in sorted(R.rglob('*')):
    if not f.is_file() or f.name=='PERSISTENCE_RECEIPTS.json':continue
    assert f.stat().st_size<20_000_000
    if f.suffix in ('.json','.md','.py'):read(f)
    files.append({'path':str(f.relative_to(R)),'bytes':f.stat().st_size,'sha256':sha(f)})
save(R/'out'/'PERSISTENCE_RECEIPTS.json',{'status':'PASS','timestamp_utc':stamp,'schema_exact':True,'progress_byte_identical':True,'reviewed_statement_hash_unchanged':original_hash,'files':files,'mirror_adoption':'UNVERIFIED'})
print(json.dumps({'status':'PASS','run':str(R),'exact_checks':check['checks']+scope['checks'],'files':len(files),'reviewed_statement_hash':original_hash},indent=2))
