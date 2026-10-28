from pathlib import Path
from datetime import datetime,timezone
import json,hashlib
R=Path(__file__).resolve().parents[1];A=R.parents[1]
P=A/'runs/20261023T012433Z-account03-A027-block-selection'
def read(p):return p.read_text(encoding='utf-8')
def put(p,s):
    with p.open('w',encoding='utf-8',newline='') as f:f.write(s)
def js(p,v):put(p,json.dumps(v,indent=2,ensure_ascii=False)+'\n')
def sha(p):return hashlib.sha256(p.read_bytes()).hexdigest()
main=json.loads(read(R/'out/validation.json'));ind=json.loads(read(R/'out/independent.json'));pilot=json.loads(read(R/'out/pilot.json'))
assert main['status']==ind['status']==pilot['status']=='PASS'
assert main['policies']==180 and main['negative_terminal_occurrences']>0 and main['negative_control_release_occurrences']>0
assert sha(R/'code/exact.py')==sha(P/'code/exact.py')
next_action='A087/A094 reconstruct equations(1)-(4), especially signed negative control releases. Then use A028@7/A029@2 to price ONE genuine non-point conditional-profile change after a paid DATA prefix from this SAME unused full terminal reserve, retaining original source, earlier charges and both complete terminals; no root bank renewal.'
gap='Universal useful proper core payment remains unsupported: paid projected decrement plus independently certified complete core leaves already imply core FEI; more generally the exact residual D must pay their actual deficit from an unused original source. No universal such source is supplied.'
statement='Version8 retains all prior scoped clauses. Let C=21/4, d_star=(1-1/sqrt(2))/2, u any uniform Boolean core with negative probability t<=d_star, and F=1+A_r(u-1) with r>=1 disjoint fair point controls. For EVERY finite adaptive physical mixed tree stopped on a failed control, at EVERY corresponding original-input projected frontier, define T_s to be the tangent to G_s at the SAME original t, U_s=G_s-T_s and D_s=2C*s*2^(-s)*d-T_s(d). Then D_s>=0 and a_s=T_s-T_(s-1)/2<=C*q_s on ALL d in[0,1]. The exact FULL terminal identity is [C I(F_s(v))-H(F_s(v))]+U_s(d)=2^(-s)[C I(v)-H(v)]+D_s(t,d). Hence a negative U_s is paid from that SAME full terminal surplus whenever H(v)-C I(v)<=D_s/p_s. No endpoint bias band or nonnegative control-release assumption is needed. The exact root surplus equals p_root[C Pi_I(u)-Pi_H(u)]+sum_CONTROL w(Cq-a)+sum_ACTIVE_LEAVES w[S_full+U]. Paid projected decrement at C and complete core terminal certificates at C therefore imply H(F)<=C I(F), at unchanged rate and arbitrary depth/interleaving. These two core hypotheses already imply core FEI and are not supplied universally. The D4 complete-core/no-control guard has negative U_1(1) paid by its own full dictator terminal surplus; old zero-surcharge omission guard remains valid. Root t=0 is trivial. General non-point controllers and root t>d_star excluded.'
claims=json.loads(read(P/'CLAIMS.json'));c=claims[-1]
c['version']=8;c['exact_statement']+=' '+statement
c['hypotheses'] += ['Version8 only: root t<=d_star; no descendant bias hypothesis; signed releases retained, possibly negative','Terminal requirement is exact S_full+U>=0, sufficient via core deficit<=D_s/p_s; projected decrement payment remains an independent hypothesis','All physical terminal entropy/influence and earlier control bills retained; single ORIGINAL root tangent']
c['statement_sha256']=hashlib.sha256(c['exact_statement'].encode('utf-8')).hexdigest()
c['proof_source']=str(R/'DERIVATION.md')
c['proof_dependencies']=['A027-PARTIAL-CORE-ACTIVATION-TRANSPORT@7 exact activation, original-input projection and scalar derivative certificate; old nonnegative-bank hypothesis NOT imported','This stage analytic affine intercept/slope proof and full surplus identities(1)-(4); exact and separate direct-character certificates']
c['review_records'].append({'reviewer':'A027 author second implementation','verdict':'PASS_NOT_EXTERNAL_REVIEW','scope':'D4 five prefix frontiers, direct character spectra/physical influences, both complete terminal accounts and independent rational logarithms','evidence':['out/validation.json','out/independent.json'],'formal':'NOT_RUN; no compiler or formal entropy certificate'})
c['status']='PROVED_LOCAL_ANALYTIC_WITH_EXACT_CERTIFICATES; VERSION8_INDEPENDENT_REVIEW_PENDING'
c['supersedes']='A027-PARTIAL-CORE-ACTIVATION-TRANSPORT@7; all earlier scoped results retained, new terminal payment removes endpoint condition under explicit certificates'
c['first_unproved_line']=gap
js(R/'CLAIMS.json',claims)
progress=json.loads(read(P/'PROGRESS.json'))
progress.update(run_id=R.name,attempt_id='A027-G-R-SELECT-019',method='Pay negative endpoint refund from SAME FULL terminal surplus using original affine intercept/slope; retain signed negative control releases',mathematical_delta=f'Endpoint-band condition removed under explicit same-rate terminal certificates; root range enlarged1/16->d_star because only original-root convexity is used; rate21/4 unchanged. {main["policies"]} policies/{main["assertions"]} exact checks, {main["negative_terminal_occurrences"]} negative terminal occurrences, {main["negative_control_release_occurrences"]} negative releases; separate direct-character {ind["assertions"]} checks PASS. Universal constant improvement zero.',deliverable_status='COMPLETE_LOCAL_ARTIFACT; VERSION8_REVIEW_PENDING',mathematical_status='ANALYTIC_SAME_TERMINAL_PAYMENT_WITH_EXACT_CERTIFICATES; FULL_FEI_OPEN',claim_versions_used=['A027-PARTIAL-CORE-ACTIVATION-TRANSPORT@7 exact activation/projection/scalar certificate'],claims_created_or_changed=['A027-PARTIAL-CORE-ACTIVATION-TRANSPORT@8'],source_artifacts=['REPORT.md','DERIVATION.md','FROZEN_SPEC.json','SOURCE_READS.json','code/exact.py','code/check.py','code/independent.py','code/finalize.py','out/pilot.json','out/validation.json','out/independent.json','out/PILOT_REPAIR.json'],next_action=next_action,blockers=[gap,'External A087/A094 v8 review and supervisor mirror not observed','Brain self-care personal-context sources stale; not mathematical premises'],stagnant_substantive_attempts=0)
js(R/'PROGRESS.json',progress);(R/'PACKET_DELTA.json').write_bytes((R/'PROGRESS.json').read_bytes())
sources=[(Path('~/AGENTS.md'),'machine-wide rules; PowerShell initial default decoding showed mojibake, no source corruption inferred'),(Path('math-open-problems/reports/fei-2026-10-11/EXECUTION_PROTOCOL.json'),'full protocol revision2026-10-11-execution-v2'),(Path('BOARD.md'),'stage intake and B06 entries; shared read-only'),(Path('claude/B06/STREAM_NOTES.md'),'v2 full stream direction'),(P/'DERIVATION.md','v7 exact identities and support limits'),(P/'CLAIMS.json','v7 inherited claims; no new acceptance inferred'),(P/'code/exact.py','byte-pinned exact helper'),(P/'code/check.py','activation derivative/projection reconstruction'),(Path('agents/A028/runs/20261023T023055Z-account03-A028-stopping-tree-payment/REPORT.md'),'v7 supplied-reference JS/KL slack; contextual next target, no quantitative premise imported'),(Path('agents/A029/runs/20261023T032111Z-account03-A029-child-deficit-transport/REPORT.md'),'stage7 actual profile-change criterion; contextual next target, no quantitative premise imported'),(Path('~/<private-repo>/12_cognitive_architecture/scheduled_tasks/README.md'),'current FULL-FEI-ONLY owner order'),(Path('math-open-problems/reports/fei-2026-10-11/CURRENT_STATUS.md'),'historical snapshot; current user campaign date takes precedence')]
js(R/'SOURCE_READS.json',[{'path':str(p),'sha256':sha(p),'scope':s} for p,s in sources])
report=f'''# A027 stage19: negative endpoint refund paid by its full terminal

## exact target, quantifiers, hypotheses and units

For every Boolean core u with negative probability t<=d_star=(1-1/sqrt(2))/2 and independent point controls, retain the SAME original supporting tangent through EVERY finite physical adaptive core/control tree, allowing arbitrary descendant biases. At rate C=21/4, pay a negative inherited endpoint refund using its OWN complete physical terminal surplus. All entropy is in bits and influences are actual uniform-cube flips. Exact identities hold at every frontier. The conditional full bound requires a paid projected core decrement and actual complete core terminal admission; full FEI remains OPEN.

## sources actually read, revisions and theorem locators

Current BOARD/B06 v2/own STATUS, full execution protocol v2, previous v7 DERIVATION/CLAIMS/helper/checker, current owner control README and historical campaign status were read. Current A028@7 and A029 stage7 reports were consumed: their supplied source/profile accounts are distinct from the present full point-activation remainder; no quantitative bound from them is imported. Source paths/hashes/scopes are in SOURCE_READS.json. Initial campaign/paper baseline was read in earlier stages and was not re-audited wholesale. One read-only brain recall returned neighboring cards and supplied no premise. Personal-model/state-of-mind brain records are stale, degraded/unverified and not used mathematically. A default PowerShell read displayed mojibake; subsequent relevant reads explicitly used UTF-8, with no claim that the files themselves were corrupted.

## complete derivation or exact first unsupported line

DERIVATION.md gives the full dimension-independent author proof. The exact rescaling h_s(d)=G_1(2p_s d) expands G_s as a finite weighted sum. Convexity only from0 to ORIGINAL root t gives T_s(0)<=0; the previous exact scalar bound gives G_s'(t)<=2C s p_s. Thus D_s=2C s p_s d-T_s(d)>=0 for ALL descendant d in[0,1], and each signed control tangent a_s<=Cq_s on that whole interval. The old claim that releases are nonnegative is explicitly NOT used.

The full actual terminal identity is S_full+U_s=p_s S_core+D_s. Therefore negative U_s is paid by that same terminal's full surplus whenever its core deficit is<=D_s/p_s; core FEI at C is one sufficient certificate. The root identity is C I(F)-H(F)=p_root(C Pi_I(u)-Pi_H(u))+sum_CONTROL w(Cq-a)+sum_ACTIVE_LEAVES w(S_full+U). Both physical children, original reaches, exhausted controls, failed-control constants and old charges are retained exactly once. This closes the previous D4 endpoint guard payment while preserving its refutation of zero surcharge without an endpoint hypothesis. Root range changes1/16->d_star because the new proof needs only original-root convexity; rate21/4 is unchanged. First unsupported universal line: {gap}

## executed validation with domain, arithmetic, commands and outputs

FROZEN_SPEC.json precedes search. Six explicit four-bit negative sets are gated by two CORE bits and activated by r=1,2,3 fresh point controls:18 actual roots, at most9 total bits. Ten fixed static/adaptive policies give180 cases, not exhaustive functions or all trees; core leaves can reach bias1. Only point-control permutation equivalence is used. Four original t values, s=1..8 and17 endpoint values separately check scalar inequalities. Main uses integer Walsh/Fraction spectra, prime-log equalities and 24-term rational atanh bounds with explicit tail. Queries are checked from actual physical edges; complete terminal spectra and signed refunds stay in every identity.

Pilot: {pilot['policies']} policies/{pilot['assertions']} assertions PASS in{pilot['elapsed_seconds']:.3f}s. Main: {main['policies']} policies/{main['assertions']} assertions PASS in{main['elapsed_seconds']:.3f}s, including{main['negative_terminal_occurrences']} negative terminal refund occurrences and{main['negative_control_release_occurrences']} negative control-release occurrences. These signed negative releases are an adversarial guard against accidentally importing v7's eligibility hypothesis. First pilot had a cache-cleanup authoring error (Hplus has no cache_clear), repaired without changing domain; out/PILOT_REPAIR.json records it. No mathematical assertion failed in that attempt.

Separate code imports neither main nor helper: direct character sums, independent32-term rational log bounds and physical edges check D4,r1 at all5 core-prefix frontiers, retaining all actual leaf siblings. {ind['assertions']} assertions PASS in{ind['elapsed_seconds']:.3f}s. This is internal second-implementation validation, not external review. Commands: python -X utf8 code/check.py --pilot; python -X utf8 code/check.py; python -X utf8 code/independent.py. Expected main memory160MB, runtime cap240s; pilot/independent caps60s. No anticipated >300MB job, compiler, GPU, detached work, dimension escalation or resource-shedding action was started. Peak RAM unmeasured. No formal/Lean entropy certificate is claimed.

## proof dependencies and changed downstream conclusions

Same pending candidate advances v7->v8; baseline accepted claims and prior scoped clauses remain unchanged. New proof needs v7 exact activation/projection and derivative-price certificate, not its nonnegative supporting bank or endpoint condition. The complete analytic affine argument and terminal pairing are supplied here. External v8 review remains pending. C019/C024 gain a same-account payment for the exact band-violating endpoint, but no universal constant or arbitrary-core supplier improvement. When core decrement and all core leaves are certified at C, their own telescope already proves core FEI; this conditional closure is not promoted to a universal reduction. A028/A029 general-profile results are consumed as context only.

## one next mathematical action and independent reviewer

{next_action} This is a saved handoff for supervisor routing; no peer message or observed adoption is claimed. A087/A094 should challenge especially the signed control releases, whole terminal entropy and the original-root dependence of every affine function.

## actual persistence receipts or precise save blocker

All four protocol files, complete derivation, frozen spec, code, results and source receipts are saved only inside A027. PROGRESS/PACKET_DELTA are byte-identical; exact protocol field sets, statement hashes, PASS outputs, source helper byte equality and all file sizes<20MB are checked by code/finalize.py. Rolling STATUS is two lines; WORKLOG/LEARNED are appended. out/PERSISTENCE_RECEIPT.json lists sizes/hashes; final readback will recheck them. No git/brain write/mail/shared-source mutation, supervisor copy, remote mirror, external acceptance or downstream use is claimed. Nothing has been stopped to free resources.

## Universal bridge

This stage moves C019 stopping-tree payment and C024 history transfer by closing the precise negative-endpoint debit from the SAME full physical terminal surplus at unchanged rate21/4, for arbitrary point-control interleavings and any descendant bias. The root range expands to d_star by a different scalar mechanism; signed negative control releases and both terminals remain. Universal constant improvement is zero: useful proper core/source admission remains unpaid and is FEI-equivalent when merely assumed. NEXT tests one actual changed non-point conditional profile against this original residual, using A028/A029's newly supplied interfaces; that attacks the missing reusable universal transaction rather than enumerating another isolated point-defect class.
'''
put(R/'REPORT.md',report)
stamp=datetime.now(timezone.utc).isoformat()
put(A/'STATUS.md','STATE: Stage19 saved: SAME full terminal surplus pays negative endpoint refund; no descendant bias band; original root<=d_star; rate21/4 unchanged;180 policies/34401 exact checks PASS;v8 review pending,FEI OPEN.\nNEXT: A087/A094 audit signed terminal payment; price ONE actual non-point profile change after paid DATA using SAME unused terminal reserve, old charges and both full terminals; compare A028@7/A029@2.\n')
for name,text in [('WORKLOG.md',f'\n{stamp} Stage19: proved affine whole-bias terminal payment, closing D4 guard from OWN full dictator surplus. Root band enlarged1/16->d_star because only original-root convexity needed; rate unchanged21/4. Main180 policies/34401 checks PASS; independent{ind["assertions"]} checks PASS.108 negative endpoint occurrences and436 negative releases retained. First pilot cache cleanup fixed, no domain change. Universal source/core payment open; review pending. NEXT: {next_action}\n'),('LEARNED.md',f'\n{stamp} A027@8 durable fact: D_s=2C s p_s d-T_s(d)>=0 on ALL d in[0,1] when original t<=d_star, C=21/4. T_s(0)<=0 and slope<=2C s p_s follow from finite rescaling into A=G1. EXACT S_full+U=p_s S_core+D_s pays negative endpoint U from same full terminal surplus; negative control releases must remain signed (436 actual occurrences). Core FEI is sufficient, not automatic; exact weaker eligibility is Hcore-C Icore<=D_s/p_s. Conditional core decrement plus core leaves already imply core FEI. Never promote this to universal selection. NEXT: same-reserve actual non-point conditional-profile conversion.\n')]:
    with (A/name).open('a',encoding='utf-8',newline='') as f:f.write(text)
protocol=json.loads(read(Path('math-open-problems/reports/fei-2026-10-11/EXECUTION_PROTOCOL.json')))
expected=set(protocol['required_per_run']['progress_fields']);expected.remove('packet_ids (one primary ID, for compatibility)');expected.add('packet_ids')
assert set(progress)==expected
for c in claims:
    assert set(c)==set(protocol['required_per_run']['claim_fields'])
    assert c['statement_sha256']==hashlib.sha256(c['exact_statement'].encode('utf-8')).hexdigest()
assert (R/'PROGRESS.json').read_bytes()==(R/'PACKET_DELTA.json').read_bytes()
assert len(read(A/'STATUS.md').splitlines())==2
for field in protocol['required_per_run']['report_fields']:assert '## '+field in report
files=[]
for p in sorted(R.rglob('*')):
    if not p.is_file() or '__pycache__' in p.parts or p.name=='PERSISTENCE_RECEIPT.json':continue
    assert p.stat().st_size<20_000_000
    files.append({'path':str(p.relative_to(R)),'bytes':p.stat().st_size,'sha256':sha(p)})
js(R/'out/PERSISTENCE_RECEIPT.json',{'status':'PASS','timestamp':stamp,'files':files,'full_FEI':'OPEN','external_review':'PENDING','remote_mirror':'UNVERIFIED'})
print(json.dumps({'status':'PASS','files':len(files),'main_assertions':main['assertions'],'independent_assertions':ind['assertions'],'version':8,'full_FEI':'OPEN'}))
