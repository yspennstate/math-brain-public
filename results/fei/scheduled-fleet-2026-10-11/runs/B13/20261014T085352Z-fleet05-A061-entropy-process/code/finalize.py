from pathlib import Path
from fractions import Fraction as F
from datetime import datetime,timezone
from hashlib import sha256
import json,time

RUN=Path(__file__).resolve().parents[1];OWN=RUN.parents[1];TEAM=OWN.parents[1]
SRC=TEAM/'agents/A064/runs/20261014T060409Z-fleet05-A064-global-debt-potential'
REF39=TEAM/'agents/A039/runs/20261014T055326Z-fleet05-A039-projection-under-restrictions'
REF38=TEAM/'agents/A038/runs/20261014T051947Z-fleet05-A038-occupancy-term-audit'
PROTOCOL=Path('~/mop_fei100/reports/fei-2026-10-11/EXECUTION_PROTOCOL.json')
now=datetime.now(timezone.utc).isoformat()
def dump(p,v):p.write_text(json.dumps(v,indent=2,ensure_ascii=False)+'\n',encoding='utf-8')
start=time.perf_counter()
ex=json.loads((RUN/'out/EXHAUSTIVE_CHECK.json').read_text());assert ex['status']=='PASS' and len(ex['records'])==3072
expected={(m,i,j) for m in range(256) for i in range(3) for j in ['x','b']+[f'y{k}' for k in range(3) if k!=i]}
actual={(r['mask'],r['first_core_coordinate'],r['third_query']) for r in ex['records']};assert actual==expected
maximum=F();witness=None
for r in ex['records']:
 upper=F(r['total_positive_bookings'][1]);lower=F(r['original_mean_S4'][0])
 assert upper*20<lower
 ratio=upper/lower
 if ratio>maximum:maximum=ratio;witness={k:r[k] for k in ('mask','first_core_coordinate','third_query')}
assert time.perf_counter()-start<30
dump(RUN/'out/BOUND_CERTIFICATE.json',{'status':'PASS','exact_assertions':3072,'coverage':'all256 labelled cores x3 first core queries x4 common third queries','bound':'W3<Sbar/20; remaining SAME owner>19Sbar/20','maximum_certified_ratio_upper':str(maximum),'maximum_upper_record':witness,'arithmetic':'Fraction comparisons on outward interval endpoints; no floating signs','source_sha256':sha256((RUN/'out/EXHAUSTIVE_CHECK.json').read_bytes()).hexdigest(),'seconds':time.perf_counter()-start})
pilot=json.loads((RUN/'out/PILOT_CHECK.json').read_text());named=json.loads((RUN/'out/FULL_CHECK.json').read_text())
total=ex['exact_assertions']+3072;assert total==209787
claim=json.loads((SRC/'CLAIMS.json').read_text(encoding='utf-8'))[0]
assert claim['claim_id']=='A064-OWNED-NONFLAT-TWO-CONVERSION-REFERENCE-RESERVE'
claim['review_records'].append({'reviewer':'A061','at':now,'verdict':'INDEPENDENTLY_RECONSTRUCTED_FULL_STATED_FINITE_INTERFACE_HOLDS',
 'scope':'All256 source cores and all768 two-query policies: canonical root, physical coherent reference reach with source-zero/reference-positive fibers, same original child owner and retained terminal KL/entropy. General reference potential proved independently. Exact same-owner third-query continuation additionally checked on3072 policies; no larger-dimensional or adaptive third-coordinate extrapolation.',
 'method':'Separate moment-entropy occupancy evaluation and own integer-Walsh/physical-edge checker; exact Fraction root brackets and enclosing logs. No source-agent code copied/executed, no repair to source statement.',
 'source_run':RUN.name,'proof_source':['ACCOUNT.md','code/check_third.py','out/EXHAUSTIVE_CHECK.json','out/BOUND_CERTIFICATE.json'],
 'substantive_repair':False,'scope_exclusions':['No universal unused S4 owner','No four-query or arbitrary-core theorem','No new independent acceptance of unrelated bundled A064 claims']})
claim['status']='INDEPENDENTLY_RECONSTRUCTED_FULL_STATED_FINITE_INTERFACE_HOLDS_BY_A061'
dump(RUN/'CLAIMS.json',[claim])
dump(RUN/'out/CLAIM_HASH_RECEIPT.json',{'source_recorded_hash':claim['statement_sha256'],'statement_raw_sha256':sha256(claim['exact_statement'].encode()).hexdigest(),'statement_hypotheses_sha256':sha256(json.dumps({'statement':claim['exact_statement'],'hypotheses':claim['hypotheses']},sort_keys=True,separators=(',',':')).encode()).hexdigest(),'source_statement_hypotheses_hash_unchanged':True})
sources=[PROTOCOL,TEAM/'BOARD.md',TEAM/'claude/B13/STREAM_NOTES.md',SRC/'REPORT.md',SRC/'PROOF.md',SRC/'CLAIMS.json',SRC/'code/check.py',REF39/'REPORT.md',REF38/'REPORT.md',OWN/'runs/20261014T042028Z-fleet05-A061-entropy-process/code/arithmetic.py']
dump(RUN/'out/SOURCE_RECEIPTS.json',[{'path':str(p),'bytes':p.stat().st_size,'sha256':sha256(p.read_bytes()).hexdigest()} for p in sources])
protocol=json.loads(PROTOCOL.read_text(encoding='utf-8-sig'));assert set(claim)==set(protocol['required_per_run']['claim_fields'])
progress={'protocol_revision':protocol['revision'],'run_id':RUN.name,'stream':'B13','packet_id':'A061','gap_id':'C019-SIGNED-CHILD-TERMINAL-PAYMENT','attempt_id':'A061-stage6-same-owner-third-reference-query',
 'method':'Independent root matched-moment entropy and physical reference-reach proof/checker; source two-query reconstruction plus exhaustive frozen third-query finite verification; exact saved-interval owner bound',
 'mathematical_delta':'A064 two-conversion finite interface independently HOLDS on all768 source policies. All3072 declared third-query policies use <1/20 SAME original mean S4 while all8 terminal H+TC bills remain; >19/20 owner left.209787 primary exact assertions including bound readback; no universal core-dimensional payment claimed.',
 'deliverable_status':'COMPLETE_LOCAL_ARTIFACTS','mathematical_status':'FINITE_SOURCE_REVIEW_AND_THIRD_QUERY_CERTIFICATE_COMPLETE; UNIVERSAL_ELIGIBILITY_OPEN',
 'claim_versions_used':[{'claim_id':claim['claim_id'],'version':1,'scope':'Full exact source finite interface reconstructed'},{'claim_id':'A038-CERTIFIED-CHILD-SURPLUS-CONVERSION','version':1,'scope':'Owner convention only; parity numerical theorem not assumed'}],
 'claims_created_or_changed':[{'claim_id':claim['claim_id'],'version':1,'change':'unchanged source statement local independent review; third-query verification is finite continuation certificate, no third broad candidate'}],
 'source_artifacts':['ACCOUNT.md','FROZEN_SPEC.json','EXHAUSTIVE_SPEC.json','BOUND_READBACK_SPEC.json','code/check_third.py','code/arithmetic.py','out/PILOT_CORRECTION.md','out/PILOT_CHECK.json','out/FULL_CHECK.json','out/EXHAUSTIVE_CHECK.json','out/BOUND_CERTIFICATE.json','out/SOURCE_RECEIPTS.json'],
 'next_consumers':['A064','A038','A039','A047','A050','A087','A094','B20'],
 'next_action':'Derive a selected-query signed conditional-row eligibility inequality D=O+mean TC_child-TC_parent against genuinely unused SAME ancestor capacity for arbitrary non-flat cores; include reference-only rows, prior bookings and full terminal H+TC, without assuming universal4I-H.',
 'stagnant_substantive_attempts':0,'blockers':['Arbitrary-dimensional unused child-surplus eligibility and future conditional-reference debt remain unproved.','Earlier two authored A061 claims remain externally pending; source review does not self-accept them.','Mirror and shared-index adoption unverified.'],'packet_ids':['A061']}
assert set(progress)=={x.split(' (')[0] for x in protocol['required_per_run']['progress_fields']}
dump(RUN/'PROGRESS.json',progress);dump(RUN/'PACKET_DELTA.json',progress)
report=f'''# A061 stage6: same original reference owner through a third query

## exact target, quantifiers, hypotheses and units

Independently reconstruct A064-OWNED-NONFLAT-TWO-CONVERSION-REFERENCE-RESERVE@1, then carry its already booked products and original mean child surplus through one further actual physical query. Root F=-1 on x=0,a=1; v on x=1,b=1; +1 otherwise. v ranges over all256 labelled three-bit cores. Query a, then y_i in both children, then one common remaining coordinate x,b or either other core bit in all4 grandchildren. All8 actual terminal functions retained. Bits; uniform Boolean signs; original owner previously unused except for the bookings stated. No universal S4 assumption.

## sources actually read, revisions and theorem locators

Updated BOARD dated2026-10-14 08:52UTC, B13 leadv2 (still October11), own STATUS. Protocol field contract reread by finalizer; earlier complete readings retained. A064 run20261014T060409Z: REPORT, full PROOF Sections1--6, first claim in CLAIMS and source checker implementation read for audit; never copied/executed. A039 run20261014T055326Z REPORT and A038 run20261014T051947Z REPORT supply prior boundary progress. Own arithmetic from last stage reused. Exact source bytes/hashes in out/SOURCE_RECEIPTS.json. Earlier campaign/paper intake inherited; no new paper or brain claim.

## complete derivation or exact first unsupported line

ACCOUNT.md independently reconstructs normalized common-kernel KL transfer and source-zero/reference-positive rows. Initial root entropy is computed from the matched occupancy moments, with exact positive-root brackets and Gibbs maximum-entropy identity; physical predicted reaches still use EVERY ambient atom. Subsequent product references are exact rational laws. Each conversion signed debit D=O+mean TC_child-KL_parent includes its normalization and actual terminal KL, and its positive part is booked once.

The conservative tail potential K_v+future positive bookings has drift>=O_v at every physical query. It retains actual TC at leaves, so sum reached O+mean terminal CE<=A+W3+mean terminal H. No entropy, conditional KL, root reference or owner is renewed. Sbar is the SAME mean certified4I-H of original a children; W2 remains booked inside W3, and remaining owner is Sbar-W3.

The independent exhaustive certificate reproduces W2<Sbar/2 on all768 source policies, then extends all3072 declared three-query policies. Exact readback comparisons sharpen the finite total to W3<Sbar/20; more than19/20 of that SAME original owner remains, with all8 complete terminal H+TC bills retained. Source claim is accepted at its full stated finite interface, without repair. The extension is a finite verification, not a new broad universal candidate or dimension extrapolation.

First unsupported universal line: an arbitrary higher-dimensional non-flat core admits a selected query whose actual signed conditional-row debit and terminal bill fit genuinely unused inherited capacity, without assuming universal4I-H>=0 or renewing its owner. Branch-dependent third-coordinate policies and fourth queries are outside this certificate.

## executed validation with domain, arithmetic, commands and outputs

Initial FROZEN_SPEC predates targeted jobs. Commands `python -X utf8 code/check_third.py pilot` and `... full`: successful pilot2 named cores/24 policies/{pilot['exact_assertions']} assertions/{pilot['seconds']:.4f}s; targeted10 named cores/120 policies/{named['exact_assertions']} assertions/{named['seconds']:.4f}s. A zero-KL constant endpoint invalidated the first pilot's lower-bound guard; corrected using analytically proved Gibbs nonnegativity, documented in out/PILOT_CORRECTION.md. Failed-attempt assertions are not counted; no target payment inequality failed.

After the cheap unchanged-dimension pilot, EXHAUSTIVE_SPEC froze all256 cores, all3 first data bits and all4 common third coordinates, with no symmetry reduction. `... exhaustive` PASS: {ex['three_query_policies']} policies, {ex['terminal_visits']} terminal visits, {ex['nonzero_terminal_entropy_visits']} nonzero-terminal-entropy visits, {ex['reference_only_node_visits']} reference-only query-node visits, {ex['exact_assertions']} assertions in {ex['seconds']:.4f}s. Exact coverage verified. BOUND_READBACK_SPEC freezes the additional3072 saved-interval comparisons W3_upper*20<Sbar_lower. Primary total {total}; pilot and targeted overlaps excluded from that total.

Integer Walsh/direct edge influences, exact Fraction products/kernels/reach and rational root signs; root36 bisections or exact rational root,48-term positive atanh logs with proved tail and outward dyadic160 rounding. Strict budget signs use separated rational endpoints. General KL/potential inequalities are proved analytically in ACCOUNT and checked for interval consistency, never inferred from a numerical tolerance. Maximum physical dimension6 unchanged; memory estimates100--120MB, below300MB trigger. Sequential jobs, no heavy/background/GPU job, no automatic dimension escalation.

## proof dependencies and changed downstream conclusions

Local CLAIMS contains unchanged A064 source statement/hypotheses/hash with full-stated-finite-interface independent review. Canonical support, common-kernel normalization, expected owner and terminal algebra are reconstructed here; no universal source theorem assumed. Source-code inspection was read-only; separate implementation evaluates root entropy from matched moments instead of per-atom interval logs. Stronger third-query finite verification is archived in the exact certificate, without opening a third broad candidate at A061's pending cap. No substantive source repair and no contributor conflict. Older unrelated A064 bundles or A061 authored claims are not self-accepted.

The downstream continuation now has a concrete original owner and >19/20 capacity after3 booked physical queries in this complete finite domain. Terminal KL is never another spare account. Universal unused-owner eligibility remains the gap; no universal FEI constant improves.

## one next mathematical action and independent reviewer

Derive a selected-query signed conditional-row inequality for arbitrary non-flat cores: compare actual D=O+mean TC_child-TC_parent and full terminal H+TC to genuinely unused SAME ancestor capacity, with reference-only rows and previous debits included. Use the minimal finite record (core25,firsty2,thirdx) as a concrete retained-reference stress fixture, not as evidence of a dimension-free bound. A064/A038/A039 consume the remaining-owner transaction; A087/A094 independently challenge the continuum-free exact certificate and general support algebra.

## actual persistence receipts or precise save blocker

Four protocol files, ACCOUNT, three frozen specs, independent code, correction note, pilot/targeted/exhaustive outputs, bound/hash/source receipts saved within this run. STATUS is two lines; WORKLOG/LEARNED updated. Exact field sets, unchanged claim payload, full3072 coverage and identical PROGRESS/PACKET_DELTA checked. out/PERSISTENCE_RECEIPTS records local file sizes and hashes. Largest exhaustive certificate is9,842,811bytes, below20MB. Source folders untouched; supervisor mirror/shared-index adoption/additional external review unverified. No save blocker.

## Universal bridge

C024 history transfer and C019 stopping-tree ownership move by full independent review of A064's768 two-query transactions and a3072-policy third-query certificate: total positive conversions consume less than1/20 of the SAME original certified mean child surplus, leaving more than19/20 while all8 terminal H+TC bills remain. No universal constant improves; arbitrary-dimensional unused-owner eligibility and later signed conditional-row debt remain unproved. NEXT derives that selected-query comparison with prior bookings and full terminals, the shortest route toward FEI because another isolated class ratio or renewed descendant bank would bypass precisely the missing universal resource inequality.
'''
(RUN/'REPORT.md').write_text(report,encoding='utf-8')
(OWN/'STATUS.md').write_text('STATE: A061 stage6 complete: A064 two-conversion full finite interface independently HOLDS; all3072 third-query policies consume<1/20 SAME original S4 owner with8 terminals retained;209787 primary checks PASS; FEI OPEN.\nNEXT: Derive selected arbitrary-nonflat signed conditional-row eligibility against unused SAME ancestor capacity, preserving prior bookings/reference-only rows and terminal H+TC; A064/A038/A039 consume, A087/A094 review.\n',encoding='utf-8')
with (OWN/'WORKLOG.md').open('a',encoding='utf-8') as f:f.write(f'\n{now} — Stage6 reconstructed A064 full two-conversion finite interface and extended SAME owner through third actual query. All256 cores/3072 policies/24576 terminal visits PASS206715 main checks plus3072 exact owner comparisons=209787 primary. W3<Sbar/20 with terminal H+TC retained; source768 two-query half-budget independently HOLDS. Constant zero-KL pilot endpoint guard repaired with Gibbs nonnegativity; documented and excluded failed counts. Targeted/pilot overlaps excluded. Universal arbitrary-core unused-owner eligibility remains open.\n')
with (OWN/'LEARNED.md').open('a',encoding='utf-8') as f:f.write('\nStage6: matched occupancy entropy H(M)=h2(z)+zlog(c)-sum dlog(theta)-sum(z-d)log(1-theta) avoids costly per-atom interval logs while preserving all atoms for reference reach. Coherent-kernel erasure/Bayes chain retains source-zero/reference-positive rows. Conservative future-positive-booking potential retains terminal TC. Actual exposed priority all256 three-bit cores, a then any core bit then common x/b/remaining core bit:3072 policies use W3<Sbar/20 from SAME original mean a-child S4; >19/20 remains with all8 terminal H+TC. Source A064 two-conversion theorem independently reconstructed at full stated finite scope. Zero canonical KL can have a negative outward entropy-difference lower endpoint; intersect with Gibbs nonnegative half-line, never infer a false negative KL. Finite complete-case payment does not establish universal unused S4 or arbitrary-core eligibility.\n')
assert len((OWN/'STATUS.md').read_text().splitlines())==2
assert (RUN/'PROGRESS.json').read_bytes()==(RUN/'PACKET_DELTA.json').read_bytes()
paths=sorted(p for p in RUN.rglob('*') if p.is_file() and p.name!='PERSISTENCE_RECEIPTS.json')+[OWN/'STATUS.md',OWN/'WORKLOG.md',OWN/'LEARNED.md']
for p in paths:assert p.stat().st_size<20*1024*1024
dump(RUN/'out/PERSISTENCE_RECEIPTS.json',{'at':now,'files':[{'path':str(p),'bytes':p.stat().st_size,'sha256':sha256(p.read_bytes()).hexdigest()} for p in paths],'full_fei':'OPEN','mirror':'UNVERIFIED'})
print(json.dumps({'status':'SAVED','primary_assertions':total,'finite_payment':'W3<Sbar/20','policies':3072,'files':len(paths)},indent=2))
