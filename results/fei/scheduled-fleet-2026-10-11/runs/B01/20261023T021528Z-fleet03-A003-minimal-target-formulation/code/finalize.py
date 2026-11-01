from pathlib import Path
import json,hashlib,datetime
R=Path(__file__).resolve().parents[1];A=R.parents[1]
ROOT=Path(r'~\brain_workers\FEI100_20261011')
CAM=Path(r'~\mop_fei100\reports\fei-2026-10-11')
SUP=Path(r'~\mop_fei100\research_pushes\2026-10-11-full-fei-100-agents')
PREV=A/'runs/20261021T233555Z-fleet03-A003-minimal-target-formulation'
P96=ROOT/'agents/A096/runs/20261023T010221Z-fleet03-A096-live-gap-ledger'
P97=ROOT/'agents/A097/runs/20261021T232544Z-fleet03-A097-cross-route-transfer'
P85=ROOT/'agents/A085/runs/20261022T234859Z-fleet03-A085-certificate-adversary'

def read(p):return json.loads(p.read_text(encoding='utf-8'))
def dump(p,x):p.write_text(json.dumps(x,indent=2,ensure_ascii=False)+'\n',encoding='utf-8')
def sha(b):return hashlib.sha256(b).hexdigest()
v=read(R/'out/VALIDATION.json');t=read(R/'out/TRANSPORT_VALIDATION.json')
assert v['status']==t['status']=='EXACT_PASS'
assert v['source_sha256']==sha((R/'code/verify_absorption.py').read_bytes())
assert v['counts']['retained_nonconstant_siblings']==896
protocol=read(R/'out/PROTOCOL_SNAPSHOT.json')
prod=read(P96/'CLAIMS.json');pclaim=prod[0];integrated=prod[1]
dump(R/'out/SOURCE_CLAIMS_A096.json',prod)
dump(R/'out/SOURCE_CLAIMS_A097.json',read(P97/'CLAIMS.json'))
(R/'IMPLICATIONS_BASELINE.md').write_bytes((PREV/'IMPLICATIONS.md').read_bytes())

# Re-read and pin all required intake, recording actual decodings rather than
# allowing Windows' default codepage to manufacture a text defect.
sources=[];excerpts=[]
paths=[CAM/n for n in ['EXECUTION_PROTOCOL.json','README.md','CURRENT_STATUS.md','CLAIM_REGISTRY.json','OBSTRUCTION_REGISTRY.json','PACKET_STATUS.json','STREAM_NEXT_ACTIONS.json']]
paths+=list(CAM.glob('*.tex'))
paths+=[SUP/n for n in ['CAMPAIGN.md','CLAIMS.md','COUNTEREXAMPLES.md','SEED_LEMMAS.md','NATIVE_MAPPING.md']]
paths+=list((SUP/'sources').glob('*.md'))+list((SUP/'sources').glob('*.txt'))
paths+=list((ROOT/'context').glob('*.txt'))
paths += [ROOT/'BOARD.md',ROOT/'claude/B01/STREAM_NOTES.md',A/'STATUS.md',A/'LEARNED.md',PREV/'REPORT.md',PREV/'IMPLICATIONS.md',PREV/'DERIVATION.md',P96/'DERIVATION.md',P96/'REPORT.md',P96/'CLAIMS.json',P97/'REPORT.md',P97/'CLAIMS.json',P85/'PROOF.md']
for p in paths:
    if not p.is_file(): raise FileNotFoundError(str(p))
    b=p.read_bytes()
    try: text=b.decode('utf-8-sig');encoding='utf-8-sig'
    except UnicodeDecodeError:text=b.decode('cp1252');encoding='cp1252 (legacy export)'
    lines=text.splitlines()
    sources.append({'path':str(p),'sha256':sha(b),'bytes':len(b),'lines':len(lines),'decoding':encoding})
    terms=['calibrat','original','C018','C019','C020','C024','B01','A003','source','signed','residual']
    hits=[{'line':i+1,'text':line[:350]} for i,line in enumerate(lines) if any(z.lower() in line.lower() for z in terms)]
    excerpts.append({'path':str(p),'hits':hits[:35]})
dump(R/'out/SOURCE_RECEIPTS.json',sources);dump(R/'out/SOURCE_EXCERPTS.json',excerpts)

statement=('For a normalized finite reference S, vacuum calibration C_p(S), and any positive mass-preserving frequency map M fixing the empty point mass, C_r(M C_p(S))=C_r(M S) whenever p<1 and the final calibration is admissible; the constant-parent case p=1 also holds for physical Boolean descendants, which necessarily have r=1. Consequently every finite adaptive physical-query policy returning repeatedly to the direct marginal of ONE fixed original source followed by vacuum calibration is pathwise identical to calibrating the CURRENT inherited reference after its first reset, provided intervening operations are only physical frequency deletions and vacuum calibrations. Under the explicitly supplied A096 likelihood hypotheses, all erasures and full terminal cross entropies therefore remain bounded by c+(1-m^2)log2(1/gamma), with zero surcharge for the number of returns. This supplies neither a universally influence-priced reference nor a likelihood floor for arbitrary Boolean functions.')
claim={'claim_id':'A003-VACUUM-CALIBRATION-ABSORPTION','version':1,'exact_statement':statement,'hypotheses':['Finite normalized references; finite CE on actual Boolean support; full normalizers and reference-only atoms retained.','M is positive and mass preserving and sends delta_empty to delta_empty; physical maps delete queried frequency coordinates.','ONE fixed original source throughout each exit; no new edit floor, nonempty-shape change or source replacement between calibrations.','At p=1 only physically admissible constant descendants r=1 are claimed; no q=1,p<1 calibration.','For the transfer consequence only: D(empty)=m=P_g(empty), total D<=1, finite c=CE(P_g,D), S>=D, Q(empty)>=m, Q(T)>=gamma D(T), gamma in (0,1].'],'statement_sha256':sha(statement.encode('utf-8')),'contributors':['A003; A096 original supplied-likelihood transfer credited'],'proof_source':['DERIVATION.md','MINIMAL_TARGET.md','code/verify_absorption.py','out/VALIDATION.json','code/verify_transport.py','out/TRANSPORT_VALIDATION.json'],'proof_dependencies':[{'claim_id':pclaim['claim_id'],'version':pclaim['version'],'statement_sha256':pclaim['statement_sha256'],'source':str(P96/'CLAIMS.json'),'scope':'Only the explicit original first-frontier supplied-likelihood theorem; proof reconstructed in DERIVATION.md section3. Absorption identity has no external dependency.'}],'review_records':[{'reviewer':'A003 author reconstruction and source-scope repair','verdict':'AUTHOR_PROOF_AND_EXACT_FINITE_CHECKS; independent acceptance pending','independence':'Fresh array implementation and generic stochastic-map cases; A003 is contributor to repaired extension and does not count as an independent accepting reviewer.'}],'status':'PROVED_PENDING_INDEPENDENT_REVIEW','supersedes':[],'refutes':[],'first_unproved_line':None,'next_consumers':['A096','A085','A094','A097','A073','A099','B01 lead','B20']}
dump(R/'CLAIMS.json',[claim])
next_action='A096/A085 independently check the absorption repair and consume it in their selective-exit theorem; then construct and price ONE nonempty-shape-changing source transport satisfying MINIMAL_TARGET equation(4), from the SAME unused ancestor bank, instead of testing more pure-calibration returns.'
progress={'protocol_revision':protocol['revision'],'run_id':R.name,'stream':'B01','packet_id':'A003','gap_id':'G-R-MISMATCH','attempt_id':'A003-stage18-vacuum-absorption','method':'Consume A096 selective-frontier theorem; repair scope by exact vacuum-ray absorption; exhaustive small Boolean paths and full selective ledgers; isolate signed nonempty transport.','mathematical_delta':'Repeated returns to one original source after vacuum calibration and physical deletion are exactly current-reference calibrations. They require ZERO added reserve: c+(1-m^2)log(1/gamma) remains, and conditional negative-cell K=2C0+10/rate18 with >=7e_root reserve remains. The genuine remaining bill is nonempty-shape transport minus actual calibration/query KL refunds.','deliverable_status':'COMPLETE_LOCAL_SOURCE_BOUND_HANDOFF','mathematical_status':'SCOPED_ABSORPTION_PROVED_PENDING_INDEPENDENT_REVIEW; FULL_FEI_OPEN','claim_versions_used':[{'claim_id':pclaim['claim_id'],'version':pclaim['version'],'statement_sha256':pclaim['statement_sha256'],'source':str(P96/'CLAIMS.json'),'status':'first-frontier theorem reconstructed at supplied hypotheses; repeated-return extension is new contributor repair'},{'claim_id':integrated['claim_id'],'version':integrated['version'],'statement_sha256':integrated['statement_sha256'],'source':str(P96/'CLAIMS.json'),'status':'negative-cell numerical application conditional on exact upstream creating/live/source-bank chain; not blanket independent acceptance'}],'claims_created_or_changed':[claim['claim_id']+'@1'],'source_artifacts':['DERIVATION.md','MINIMAL_TARGET.md','IMPLICATIONS_BASELINE.md','FROZEN_SPEC.json','FROZEN_AMENDMENT.json','FROZEN_TRANSPORT.json','out/VALIDATION.json','out/TRANSPORT_VALIDATION.json','out/SELECTIVE_CHECKER_CORRECTION.json','out/SOURCE_RECEIPTS.json'],'next_consumers':claim['next_consumers'],'next_action':next_action,'stagnant_substantive_attempts':0,'blockers':['Universal influence-priced source admission and useful nonempty-shape transport selection are OPEN.','Independent acceptance and downstream source adoption remain pending; supervisor copying and remote mirroring are unverified.','No Lean/kernel certification claimed; proof is explicit author mathematics plus exact finite arithmetic.'],'packet_ids':['A003']}
dump(R/'PROGRESS.json',progress);(R/'PACKET_DELTA.json').write_bytes((R/'PROGRESS.json').read_bytes())

report=f'''# exact target, quantifiers, hypotheses and units

Prove or obstruct repeated returns to the ORIGINAL source marginal after intervening vacuum calibrations and physical queries, while retaining all previous erasures, the same original bank and every full complementary terminal. All cubes are finite uniform Boolean cubes; all entropy and CE are in bits. The main identity is C_r(M C_p(S))=C_r(M S), for admissible nonconstant calibrations and positive mass-preserving M fixing the empty atom; physical constant endpoints are explicit. It implies arbitrary repeated SAME-source returns cost ZERO more than calibrating the current inherited reference. This is an elementary source-scope repair, not a novelty or universal FEI claim. Full FEI remains OPEN.

# sources actually read, revisions and theorem locators

Read current BOARD snapshot2026-10-23 02:12UTC, B01 STREAM_NOTES v1 and own stage17 STATUS/REPORT/DERIVATION/IMPLICATIONS. Consume A096 20261023T010221Z DERIVATION sections1--5 and exact claim versions, A085 20261022T234859Z PROOF sections1--4, and A097 20261021T232544Z REPORT/CLAIMS. A001 20261023T000044Z report and peer-board updates were inspected for dispatch; their next finite fixture is not repeated. A096 already closes arbitrary first-reset exit frontiers and current-reference calibration, while marking repeated ORIGINAL-source returns unpaid. The new identity addresses that exact marked distinction.

Execution-v2, all required campaign indices/plan, supplemental notes/source texts and four supplied paper exports are read/pinned in out/SOURCE_RECEIPTS.json; prior source-complete baseline is reused, not claimed again. Actual decoding is recorded, with legacy cp1252 exports explicitly labeled. Current owner deadline23October14:49UTC takes precedence over the old protocol end date. One two-wording math recall returned weak/general matches, no matching absorption theorem, and is not a proof dependency. Required wake reports stale personal-context inputs at88.7/73.3hours; brain self-care is degraded/unverified for current owner-model/state-of-mind context. Current instructions and read-only mathematical sources are used instead.

# complete derivation or exact first unsupported line

DERIVATION section1 writes C_p(S)=bS+(1-b)delta_empty, b=(1-p)/(1-S(empty))>0. Since M fixes delta_empty, all nonempty atoms of M C_p(S) equal b times those of M S. Final calibration cancels b exactly, including every ghost/reference-only atom and the full vacuum normalizer. A physical constant parent has only constant descendants; both final references are point laws. The algebra does not assert an inadmissible p=1,r<1 identity.

Section2 gives pathwise equivalence under arbitrary adaptive choices. Section3 uses ONLY the first-reset antichain for A096's likelihood comparison, then pays every continuation by the complete-reference query chain and nonpositive binary-KL calibration. Hence the whole repeated-return tree still costs <=c+(1-m^2)log2(1/gamma). Section4 retains, conditionally on the exact upstream negative-cell source/creating/live chain, exit cost<c+22e, creating bill<W+13e, original K=2C0+10, structural rate18 and reserve>=7e_root. No extra reset-count or dimension charge is introduced. Full old constant terminals are charged their actual CE; a constant function does not make an unreset reference free.

MINIMAL_TARGET equations1--4 isolate the exact remaining transport: reset price Z is the weighted signed nonempty-shape likelihood bill minus binary-calibration KL. The same original unused bank changes by w(rho-Z), including the actual conditional-occupancy query KL refund rho. Pure-calibration histories have zero shape bill. The first unsupported universal line is constructing an influence-priced admitted source and useful nonempty-SHAPE-changing transport satisfying that SAME-bank affordability inequality for arbitrary Boolean functions. Neither the supplied-floor theorem nor this algebra supplies that construction.

# executed validation with domain, arithmetic, commands and outputs

Frozen specifications precede every search: FROZEN_SPEC, FROZEN_AMENDMENT, FROZEN_TRANSPORT. Final verify_absorption.py: {v['assertions']} exact assertions PASS in {v['runtime_seconds']:.3f}s; all256 three-bit truth tables, four full source laws, all24576 ordered two-query physical paths,2175 admissible generic stochastic-map tuples out of3375 candidates, and1024 full selective-tree ledgers. The tree leaves896 nonconstant root siblings at the final frontier and executes3072 repeated-return events. All source arrays, marginals, calibrations and Fourier spectra use exact Fraction arithmetic; atomwise absorption equality is exact. Ledger CE signs use outward rational logs. Worst whole-bill minus initial full source CE upper bound is0, attained by a zero-cost constant case. There is no Boolean-symmetry reduction and no automatic n escalation.

The original fully expanded tree pass ({read(R/'out/VALIDATION_FULL_EXPANSION.json')['assertions']} assertions) is archived separately and NOT added to final coverage. The first selective revision failed because the checker incorrectly assumed zero terminal bill for every constant actual function. out/SELECTIVE_CHECKER_CORRECTION.json preserves the failure and fix: only initially zero-cost references have that asserted zero bill; otherwise every old constant-terminal CE remains charged. The theorem itself never used that assumption.

verify_transport.py: {t['assertions']} exact assertions PASS in {t['runtime_seconds']:.3f}s across512 actual Boolean child cases, including both signs of the nonempty transport and constant children. It checks interval agreement with the exact decomposition, not a universal affordability assertion. Total final assertions across the two distinct helpers: {v['assertions']+t['assertions']}. Logs use28 positive atanh terms after binary range reduction, remainder <=2z^57/[57(1-z^2)] with0<=z<=1/3, and outward rounding at2^-80. The universal identity comes from the written scalar cancellation, not finite extrapolation. No Lean/kernel certification is claimed.

Commands from A003: python -X utf8 runs/{R.name}/code/verify_absorption.py; python -X utf8 runs/{R.name}/code/verify_transport.py; python -X utf8 runs/{R.name}/code/finalize.py. Jobs estimated120MB with55-second internal caps; all passed under7seconds. No job>300MB, GPU, detached/windowed work or shared-process interruption is started. Admission read at stage intake was OK (8512MB free RAM,28.1GB free disk).

# proof dependencies and changed downstream conclusions

The absorption identity is self-contained finite linear algebra. Its abstract repeated-frontier corollary uses A096-SELECTIVE-FRONTIER-LIKELIHOOD-TRANSFER@1, statement SHA256 {pclaim['statement_sha256']}, at its explicit supplied D,S,Q,gamma hypotheses, reconstructed in DERIVATION section3. The negative-cell constants are CONDITIONAL on A096-ARBITRARY-EXIT-FRONTIER-SAME-ANCESTOR@1 and its exact upstream live/source-bank dependencies; those dependencies are preserved in out/SOURCE_CLAIMS_A096.json. No external blanket acceptance is asserted. A003 contributes the repair and cannot count as independent acceptance of the repaired extension.

IMPLICATIONS_BASELINE preserves the old witness residual, good-coordinate erasure and full signed-Booleanity arrows with exact constants. MINIMAL_TARGET updates the reference-transfer edge without changing those constants. A096's repeated-original-source distinction can be removed when the only intervening operations are pure vacuum calibration and physical deletion. It must remain for source replacement or operations changing relative nonempty weights, such as a new edited-function floor.

# one next mathematical action and independent reviewer

{next_action} The lemma's elementary scope should be checked first by A096 or A085, especially constant-parent endpoints and absence of nonempty-shape edits. Full-chain integrated acceptance remains pending; supervisor dispatch rather than unauthorized messaging supplies the handoff.

# actual persistence receipts or precise save blocker

All four protocol files, code, frozen specs, proof and validation artifacts are saved in this unique A003 run; PACKET_DELTA is byte-identical to PROGRESS. Finalizer reads back the exact schema keys, hashes statements and code, checks every required report heading and validates the two-line rolling STATUS. out/PERSISTENCE_RECEIPT.json records actual local byte hashes after these writes. STATUS, WORKLOG and LEARNED are updated. Independent review, registry adoption, supervisor copy and remote mirror are pending and are not claimed. No git, shared-index modification or outbound message is performed. No mathematical job remains running after validation.

Universal bridge: This stage moves C019 stopping-tree payment and C024 history transfer by removing the supposed extra repeated-original-source-calibration charge entirely: zero surcharge, unchanged supplied bound c+(1-m^2)log2(1/gamma), and conditional original rate18 with>=7e_root reserve. The unresolved universal bridge is influence-priced source admission plus one useful nonempty-shape transport paid from the existing ancestor bank, not another calibration order. That transport is the shortest next route because the present exact identity already closes every finite pure-calibration interleaving, so further such examples cannot supply a missing all-Boolean FEI mechanism.
'''
(R/'REPORT.md').write_text(report,encoding='utf-8')
(A/'STATUS.md').write_text('STATE: A003 stage18 saved: vacuum calibration absorption proves repeated SAME-source returns paid at zero surcharge; exact Boolean/selective ledgers PASS; FEI OPEN; independent review pending.\nNEXT: A096/A085 review absorption repair; price one genuine nonempty-shape source transport by MINIMAL_TARGET(4) from the SAME unused ancestor bank, retaining all full old siblings and debits.\n',encoding='utf-8')
now=datetime.datetime.now(datetime.timezone.utc).isoformat()
with (A/'WORKLOG.md').open('a',encoding='utf-8') as f:f.write(f'\n- {now} stage18 ({R.name}): consumed A096 arbitrary selective-frontier result; proved C_r(M C_p S)=C_r(M S), closing repeated fixed-source returns with zero added reserve. {v["assertions"]} absorption/selective-ledger plus {t["assertions"]} transport exact assertions PASS. Preserved full old nonconstant and constant-terminal CE; corrected a checker-only constant-free assumption. Remaining universal gap is nonempty-shape transport/source admission. Files saved; independent review and supervisor remote copy pending.\n')
with (A/'LEARNED.md').open('a',encoding='utf-8') as f:f.write('''\n## Stage18: vacuum-ray absorption (2026-10-23)

For any positive mass-preserving M fixing delta_empty, C_r(M C_p(S))=C_r(M S), whenever calibrations are admissible and p<1; physical p=1 forces constant descendants r=1. Proof: C_p S=bS+(1-b)delta_empty, so M preserves proportional nonempty parts and final calibration cancels b. Thus repeated returns to ONE original source after only physical deletions and vacuum calibrations are CURRENT-reference calibrations, paid at zero surcharge. This removes the scope distinction marked unpaid in A096 20261023T010221Z. Under its supplied likelihood hypotheses, bound c+(1-m^2)log(1/gamma) stays unchanged. Its negative-cell constants remain conditional on exact upstream source/live/creating premises: K=2C0+10, structural18, reserve>=7e_root.

The new paid mechanism does NOT extend to new floors or source changes that alter relative nonempty weights. For a queried selected child, the exact reset cost is T-D_Bern(p||V0), T=(1-p) E_actual_nonempty log(V_nonempty_normalized/S_nonempty_normalized). The same-bank affordability condition is w*mean_selected T<=U+w*rho+w*mean_selected D_Bern. A universal useful selection/source construction satisfying this is OPEN. Full constant-terminal inherited CE must be retained even when actual function is constant; the selective-tree checker caught precisely that temptation. See stage18 DERIVATION and MINIMAL_TARGET for quantifiers/endpoints and exact finite certificates; independent acceptance pending.
''')

# Actual readback, exact schemas, statement hashes and artifact size limits.
fields=protocol['required_per_run']
expected_progress={x.split(' (')[0] for x in fields['progress_fields']}
assert set(read(R/'PROGRESS.json'))==expected_progress
assert (R/'PACKET_DELTA.json').read_bytes()==(R/'PROGRESS.json').read_bytes()
for c in read(R/'CLAIMS.json'):
    assert set(c)==set(fields['claim_fields'])
    assert c['statement_sha256']==sha(c['exact_statement'].encode('utf-8'))
saved_report=(R/'REPORT.md').read_text(encoding='utf-8')
for title in fields['report_fields']:assert '# '+title in saved_report
assert saved_report.rstrip().split('\n')[-1].startswith('Universal bridge:')
status=(A/'STATUS.md').read_text(encoding='utf-8').splitlines();assert len(status)==2 and status[0].startswith('STATE: ') and status[1].startswith('NEXT: ')
manifest=[]
for p in sorted(R.rglob('*')):
    if p.is_file() and p.name!='PERSISTENCE_RECEIPT.json':
        b=p.read_bytes();assert len(b)<20_000_000
        manifest.append({'path':str(p.relative_to(R)),'bytes':len(b),'sha256':sha(b)})
dump(R/'out/PERSISTENCE_RECEIPT.json',{'status':'LOCAL_READBACK_PASS','utc':now,'protocol_schema_exact':True,'progress_compatibility_identical':True,'rolling_status_two_lines':True,'manifest':manifest,'remote_mirror':'UNVERIFIED; supervisor owns copy'})
print(json.dumps({'status':'LOCAL_READBACK_PASS','run':str(R),'artifacts':len(manifest),'absorption_assertions':v['assertions'],'transport_assertions':t['assertions'],'total_final_assertions':v['assertions']+t['assertions'],'pending':'independent review; universal source/transport construction; supervisor copy'}))
