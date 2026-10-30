"""Persist the stage's checked local records, with exact protocol schemas."""
from pathlib import Path
from datetime import datetime,timezone
import hashlib,json

RUN=Path(__file__).resolve().parent.parent; HOME=RUN.parent.parent
ROOT=HOME.parent.parent
def read(p): return p.read_text(encoding='utf-8')
def write(p,s): p.write_text(s,encoding='utf-8')
def put(p,x): write(p,json.dumps(x,ensure_ascii=False,indent=2)+'\n')
def sha(p): return hashlib.sha256(p.read_bytes()).hexdigest()
now=datetime.now(timezone.utc).isoformat()
fixed=json.loads(read(RUN/'out'/'verification.json'))
adaptive=json.loads(read(RUN/'out'/'adaptive.json'))
assert fixed['status']==adaptive['status']=='PASS'
assert (fixed['cuts'],fixed['projections'],adaptive['frontiers'],adaptive['source_restriction_nodes'])==(12288,33866,3168,3614)
assert fixed['helper_sha256']==sha(RUN/'code'/'verify.py')
assert adaptive['helper_sha256']==sha(RUN/'code'/'adaptive.py')
report=read(RUN/'REPORT.md')
report=report.replace('Bounded adaptive validation and final receipts are pending at this checkpoint.','Both frozen exact validations PASS; local protocol records and receipts are saved. Independent review remains pending.')
report=report.replace('Adaptive results will be entered after execution.','The v1.1 pilot passed144 frontiers/1766 assertions in0.047s. The full adaptive run passed352 parents,3168 frontiers and3614 original-source restriction nodes:60790 assertions and58 certified log signs in1.552s. Together the two full runs certify1517305 assertions. out/adaptive.json records the helper hash and directly computed adaptive pruning guard.')
report=report.replace('Proof checkpoint and frozen verifier saved locally in the permitted run. Final schema checks, exact results, source hashes, receipts and rolling-file updates will be recorded before completion.','All four protocol files, two frozen specs, both verifiers, exact outputs, source hashes and rolling-file updates are saved locally. out/SCHEMA_CHECK.json verifies exact protocol field sets, report headings, two-line STATUS, file-size bounds and byte-identical compatibility copy; out/RECEIPTS.json records artifact sizes and SHA256 values. Independent review, supervisor pickup, registry adoption and external mirror verification are not claimed.')
write(RUN/'REPORT.md',report)

statement=(
 'Let g_+,g_- be Boolean functions on the same finite uniform data cube X, beta an independent quadratic F2 Boolean phase on Z, '
 'F=g_beta, p=Pr(beta=+1), d=Pr(g_+!=g_-), J=I(g_+g_-), and Q_+,Q_- any normalized full references supporting their spectra. '
 'Keep the ORIGINAL Q=pQ_+ +(1-p)Q_- fixed. For every predetermined exposed E, the unchanged inherited reference '
 'Q times C_(Z\\E), C=(1-d)delta_empty+dP_beta, has average full cost CE(pP_+ +(1-p)P_-,Q)+H(C_(Z\\E)) '
 '<=Gamma_bar+4J+2I_(Z\\E)(F). For ANY finite adaptive control-only query/stopping tree, give each node alpha '
 'Q times [(1-d)delta_empty+d Uniform(V_alpha)], where V_alpha is the actual restricted quadratic phase affine Fourier support. '
 'This phase law is obtained by conditioning the ORIGINAL projected affine phase source onto V_alpha. Each return from its '
 'inherited marginalized reference decreases the full cost by exactly D(C_alpha||C_inherited)>=0. At every physical stopping '
 'frontier, average full cost <=Gamma_bar+4J+2 average remaining control influence. If beta is nonconstant and the '
 'ORIGINAL terminal full costs are <=cI(g_s), c<=143/16, the SAME original rate25 account retains at least '
 'I_X(F)/16+23 average remaining control influence after all old signed debits and exact return credits. Constant beta '
 'uses its single selected terminal reference. No individual-child nonnegative bank or positive-only booking is asserted. '
 'Indeed beta=(-1)^(z1z2), g_+=1,g_-=-1 gives a positive-only overdraft of1/2 for every rate K>=2; its adaptive '
 'stop-constant/query-character tree has final unchanged-reference cost1/2 at zero influence, cleared by the prescribed original-fiber return.'
)
claim={
 'claim_id':'A068-ORIGINAL-AFFINE-CONTROL-FRONTIERS','version':1,'exact_statement':statement,
 'hypotheses':['Uniform independent finite cubes X,Z; g_+,g_- arbitrary Boolean on the SAME X; beta degree<=2 over F2 on Z.',
 'Q_+,Q_- complete normalized references supporting the respective full spectra, including empty atoms; both physical branch bills retained.',
 'The no-reset theorem requires E fixed independently of physical outcomes. The adaptive theorem requires the explicitly prescribed original-phase affine-fiber returns, with all exact KL credits booked.',
 'Only control coordinates queried, at most once on a path; arbitrary finite adaptive choices/stopping. Data reference Q remains its original root mixture.',
 'Rate25 corollary additionally assumes ORIGINAL full terminal payment <=cI with c<=143/16. No repeated 16I_X grant and no ignoring negative credits.'],
 'statement_sha256':hashlib.sha256(statement.encode('utf-8')).hexdigest(),
 'contributors':['A068 (author proof and exact certificates)','A096/A097 original-source return direction, not imported as a theorem premise'],
 'proof_source':['REPORT.md: complete derivation or exact first unsupported line','code/verify.py','code/adaptive.py','out/verification.json','out/adaptive.json'],
 'proof_dependencies':['A068-ACTIVATED-QUADRATIC-CONTRAST@1: inherited log-sum transfer, JS<=3J, h2(d)<=J; prior REPORT SHA256 e1e09bad70759c2ee85acadcfabdd7a5e98d8f43230696562aed0e63d549eeec',
 'Quadratic flatness, projected affine rank and exact source-conditioned credit reconstructed locally.',
 'A068-QUADRATIC-CONTEXT-RANK-REFERENCE@1 / threshold C001 full-reference constant only for threshold-terminal corollary; general theorem assumes no FEI premise.'],
 'review_records':[],'status':'AUTHOR_PROVED_PENDING_INDEPENDENT_REVIEW','supersedes':[],
 'refutes':['Unchanged-reference adaptive-frontier extension and positive-only overdraft-free booking of this exact quadratic source at every rate K>=2 (not FEI).'],
 'first_unproved_line':'Scoped theorems proved; universal extension first requires one DATA query changing terminal/disagreement profiles under ORIGINAL Q_+,Q_-, old debits and full children, without a new contrast reserve. Nonquadratic control rank payment also open.',
 'next_consumers':['A070','A088','A094','A096','A097','A066','A067']}
put(RUN/'CLAIMS.json',[claim])
progress={
 'protocol_revision':'2026-10-11-execution-v2','run_id':RUN.name,'stream':'B14','packet_id':'A068','gap_id':'G-LOWSEL-COLLISION',
 'attempt_id':'A068-original-affine-source-adaptive-control-frontiers-v1',
 'method':'Original-reference spectral marginalization; affine projection rank; physical stopping martingale for the fixed data mixture; prescribed original affine-fiber returns with exact KL credits.',
 'mathematical_delta':'Fixed-set no-reset continuation and ALL adaptive control frontiers with explicit ORIGINAL affine-source conditioning; SAME rate25 owner leaves >=I_X/16+23 average remaining control influence. Exact two-bit guard refutes unchanged adaptive and positive-only payment by1/2. Full exact validation:1517305 assertions.',
 'deliverable_status':'COMPLETE_LOCAL','mathematical_status':'SCOPED_AUTHOR_PROOF_COMPLETE; INDEPENDENT_REVIEW_PENDING; FULL_FEI_OPEN',
 'claim_versions_used':['A068-ACTIVATED-QUADRATIC-CONTRAST@1','A068-QUADRATIC-CONTEXT-RANK-REFERENCE@1 for terminal corollary only','A096/A097 original-source-return reports: directional source, no unreviewed theorem imported'],
 'claims_created_or_changed':['A068-ORIGINAL-AFFINE-CONTROL-FRONTIERS@1'],
 'source_artifacts':['REPORT.md','CLAIMS.json','SPEC.json','ADAPTIVE_SPEC.json','code/verify.py','code/adaptive.py','out/verification.json','out/adaptive.json','out/SOURCES.json','out/SCHEMA_CHECK.json','out/RECEIPTS.json'],
 'next_consumers':claim['next_consumers'],
 'next_action':'Expose one actual DATA coordinate after a paid adaptive control history: retain ORIGINAL terminal references, all old transaction debits/credits and both full child bills, and pay changed disagreement without renewing16I_X.',
 'stagnant_substantive_attempts':0,
 'blockers':['Universal data-profile history transfer and nonquadratic-selector payment remain open.','Independent review, supervisor collection and shared adoption unverified.','Brain self-care degraded: stale personal model/state notes not used as mathematical premises.'],
 'packet_ids':['A068']}
put(RUN/'PROGRESS.json',progress);(RUN/'PACKET_DELTA.json').write_bytes((RUN/'PROGRESS.json').read_bytes())

status=('STATE: Stage18: SAME original Q/affine source pays every adaptive quadratic-control frontier via exact KL credits; rate25 residual>=I_X/16+23E I_Z;1517305 exact assertions PASS; FEI OPEN.\n'
 'NEXT: Expose one DATA coordinate after a paid adaptive control history; preserve original terminals, old debits/credits and both full bills; pay changed disagreement without renewed reserve; A070/A088/A094/A096/A097 review.\n')
write(HOME/'STATUS.md',status)
log=(f'\n{now} | {RUN.name} | Read new BOARD/lead and own state; consumed A096/A097 original-source-return direction. '
 'Proved fixed-set unchanged-reference continuation, then adaptive control-frontier solvency using prescribed conditioning of ORIGINAL affine phase source; exact reset KL credits, SAME original Q and root16I_X reserve. '
 'Counterguard beta=z0*z1 proves positive-only overdraft1/2 at every rate and unchanged adaptive frontier cost1/2 at zero influence; prescribed return releases exactly1/2. '
 'Main12288 cuts+33866 projections1456515 checks31.341s; adaptive3168 frontiers+3614 source nodes60790 checks1.552s PASS. '
 'No compiler or external acceptance asserted. Next actual data-profile change with old bills; full FEI OPEN.\n')
write(HOME/'WORKLOG.md',read(HOME/'WORKLOG.md')+log)
lesson=('\nOriginal affine-source control continuation (A068 stage18): the squared spectrum of a restricted quadratic phase is the ORIGINAL phase spectral law projected onto unqueried controls and conditioned on the actual affine restricted support. '
 'Support inclusion follows from signed Fourier restriction; flatness makes conditioning exact. Keep root Q=pQ_+ +(1-p)Q_- unchanged, original d, and C_alpha=(1-d)delta_empty+dP_beta_alpha. '
 'Returning the inherited control marginal to C_alpha decreases the FULL reference cost by exactly KL(C_alpha||C_inherited), including correlated data-control laws. '
 'For EVERY adaptive control-only stopping frontier, average Gamma<=original weighted terminal bills+4I(g_+g_-)+2 average remaining control influence. Root terminal c<=143/16 yields same rate25 unused capacity>=I_X/16+23E I_controls, with all old signed debits and actual reset credits. '
 'No repeated contrast grant. Fixed exposed subsets need NO reset, with projection-rank price<=2 remaining control influence. '
 'Do not extend the unchanged-reference claim to adaptive stopping: beta=(-1)^(z0z1), branches+1/-1, stop constant and query character gives final cost1/2 at zero influence. '
 'At every rate K>=2 full positive-only debit K-3/2 exceeds original bank K-2 by1/2; genuine negative reset credit1/2 closes the signed owner account. '
 'The result permits explicit source conditioning, not unchanged references, independent child-local banks, or discarded negative credits. Data queries change d and the old terminal profiles; that is the next unpaid universal transfer. '
 'Complete proof/certificates: '+RUN.name+'/REPORT.md. Full FEI OPEN; independent review pending.\n')
write(HOME/'LEARNED.md',read(HOME/'LEARNED.md')+lesson)

sources=[
 (ROOT/'BOARD.md','current relevant agent rows'),(ROOT/'claude'/'B14'/'STREAM_NOTES.md','full lead direction'),
 (Path('math-open-problems/reports/fei-2026-10-11/EXECUTION_PROTOCOL.json'),'protocol and exact field schemas'),
 (RUN.parent/'20261022T211502Z-fleet03-A068-antichain-beyond-one-order'/'REPORT.md','full predecessor proof'),
 (RUN.parent/'20261022T211502Z-fleet03-A068-antichain-beyond-one-order'/'code'/'verify.py','exact arithmetic helper; pinned and imported'),
 (HOME.parent/'A070'/'runs'/'20261022T234315Z-fleet03-A070-analytic-route-referee'/'REPORT.md','opening derivation and positive-debit scope'),
 (HOME.parent/'A096'/'runs'/'20261023T010221Z-fleet03-A096-live-gap-ledger'/'REPORT.md','opening18 lines, original-source return direction only'),
 (HOME.parent/'A097'/'runs'/'20261023T021120Z-fleet03-A097-cross-route-transfer'/'REPORT.md','opening18 lines, original-source return direction only')]
put(RUN/'out'/'SOURCES.json',[{'path':str(p),'sha256':sha(p),'bytes':p.stat().st_size,'read_scope':scope,'text_encoding':'utf-8'} for p,scope in sources])

protocol=json.loads(read(sources[2][0]))
def find_fields(obj):
    if isinstance(obj,dict):
        if all(k in obj for k in ['report_fields','claim_fields','progress_fields']):return obj
        for value in obj.values():
            got=find_fields(value)
            if got:return got
    if isinstance(obj,list):
        for value in obj:
            got=find_fields(value)
            if got:return got
fields=find_fields(protocol);assert fields
expected_progress=[s.split(' (')[0] for s in fields['progress_fields']]
assert set(progress)==set(expected_progress)
assert set(claim)==set(fields['claim_fields'])
assert all('## '+h in report for h in fields['report_fields'])
assert report.rfind('## Universal bridge')>report.rfind('## actual persistence')
assert (RUN/'PROGRESS.json').read_bytes()==(RUN/'PACKET_DELTA.json').read_bytes()
assert len(read(HOME/'STATUS.md').splitlines())==2
assert all(p.stat().st_size<20*1024*1024 for p in RUN.rglob('*') if p.is_file())
put(RUN/'out'/'SCHEMA_CHECK.json',{'status':'PASS','utc':now,'exact_claim_fields':True,'exact_progress_fields':True,'seven_required_report_fields':True,'universal_bridge_last':True,'compatibility_byte_identical':True,'status_two_lines':True,'all_files_under_20mb':True,'full_assertions':fixed['assertions']+adaptive['assertions'],'formal_compiler':'NOT_RUN; no formal certification claimed','shared_adoption':'UNVERIFIED'})
put(RUN/'out'/'RECEIPTS.json',{'utc':now,'scope':'local persistence only; excludes this self-referential receipt',
 'artifacts':[{'path':str(p.relative_to(RUN)),'bytes':p.stat().st_size,'sha256':sha(p)} for p in sorted(RUN.rglob('*')) if p.is_file() and p.name!='RECEIPTS.json'],
 'rolling':[{'path':str(p),'bytes':p.stat().st_size,'sha256':sha(p)} for p in [HOME/'STATUS.md',HOME/'WORKLOG.md',HOME/'LEARNED.md']]})
print(json.dumps({'status':'PASS','run':RUN.name,'report_sha256':sha(RUN/'REPORT.md'),'claim_sha256':claim['statement_sha256'],'assertions':fixed['assertions']+adaptive['assertions'],'schema':'PASS','four_protocol_files':'SAVED','full_fei':'OPEN'}))
