from pathlib import Path
from fractions import Fraction as F
import json,hashlib,datetime
import audit_hull as a
R=a.R;A=R.parents[1]
ROOT=Path(r'~\brain_workers\FEI100_20261011')
source=ROOT/'agents/A072/runs/20261023T015130Z-fleet03-A072-exact-walsh-engine'
protocol_path=Path(r'~\mop_fei100\reports\fei-2026-10-11\EXECUTION_PROTOCOL.json')
now=datetime.datetime.now(datetime.timezone.utc).isoformat()
def dump(p,z):p.write_text(json.dumps(z,indent=2,ensure_ascii=False,default=str)+'\n',encoding='utf-8')
def sha(p):return hashlib.sha256(p.read_bytes()).hexdigest()
validation=json.loads((R/'out/VALIDATION.json').read_text(encoding='utf-8'))
finance=json.loads((R/'out/FINANCIAL_VALIDATION.json').read_text(encoding='utf-8'))
assert validation['passed'] and finance['passed']
assert validation['states']==2916 and validation['query_rows']==5832 and validation['total_checks']==68500
lines=[json.loads(z) for z in (R/'out/CASES.jsonl').read_text(encoding='utf-8').splitlines()]
assert len(lines)==len({(z['core'],tuple(z['tag'])) for z in lines})==2916
def unpack(p):return {None if k=='constant' else F(k):F(v) for k,v in p.items()}
counts={};witnesses=[]
for j in (2,3,4,5):
 group=[z for z in lines if z['core']==j]
 unique={json.dumps([z['S'],z['R'],z['I']],sort_keys=True) for z in group}
 counts[j]=len(unique)
 for z in group:
  S=unpack(z['S']);R0=unpack(z['R']);si=a.ev(S)
  stop=a.mul(S,-1) if si[1]<0 else {}
  gap=a.sub(R0,stop)
  if gap:
   assert a.ev(gap)[0]>0
   witnesses.append(dict(core=j,tag=z['tag'],S=z['S'],R=z['R'],strict_future_credit_gap=a.ev(gap),winner=z['winner']))
assert len(witnesses)==92 and all(v==12 for v in counts.values())
dump(R/'out/ADVERSARIAL_WITNESSES.json',dict(naive_current_deficit_reset_fails=True,raw_states=92,exact_spectral_profile_counts_by_label=counts,witnesses=witnesses))
claim=next(z for z in json.loads((source/'CLAIMS.json').read_text(encoding='utf-8')) if z['claim_id']=='A072-OTHER-CORE-STOPPING-CREDIT-HULL')
digest=hashlib.sha256(json.dumps({'exact_statement':claim['exact_statement'],'hypotheses':claim['hypotheses']},sort_keys=True,separators=(',',':'),ensure_ascii=False).encode('utf-8')).hexdigest()
assert digest==claim['statement_sha256']=='3232af6b6b8937dc62c1e50b57a212def54049aec44fe6ad145148fa912feb10'
dump(R/'out/HASH_CONVENTION.json',dict(source_declared_digest=digest,convention='sha256 UTF8 canonical JSON {exact_statement,hypotheses}, sorted keys, compact separators, ensure_ascii=False',alternate_statement_key_digest='6f510f42a195e93610adfc511a932c165f896ce5a71dc7975c614993cd2cccc7',first_save_attempt='Held before writing CLAIMS/PROGRESS/REPORT/rolling notes: verifier incorrectly assumed payload key statement rather than source exact_statement. Source finalize.py line8 inspected; source mathematical statement/hypotheses/version/digest unchanged.',source_finalize_sha256=sha(source/'code/finalize.py'),source_files_modified=False))
claim['proof_source']=[str(source/p) for p in claim['proof_source']]+[str(R/'INDEPENDENT_PROOF.md'),str(R/'code/audit_hull.py'),str(R/'out/VALIDATION.json'),str(R/'out/FINANCIAL_VALIDATION.json')]
claim['review_records'].append(dict(reviewer='A074',independent=True,reviewed_at=now,decision='ACCEPT_UNCHANGED_CONDITIONAL_THEOREM_AND_FINITE_ONE_CORE_CERTIFICATE',statement_sha256=digest,reconstruction='Own binary inclusion-exclusion/occupied-block conditional entropy; direct inner character sums/edges; all four labels and all raw restrictions without symmetry quotient. Independent Bellman proof and signed-label zero-denominator proof. Six source policy choices reconstructed with own spectra/hulls.',scope_limit='Earlier donor-funding prefix is not independently re-audited: early positive debit and original labels are source inputs. The continuation theorem applies conditionally to every existing a=D-S,D>=0. No claim of second-core eligibility or unrestricted FEI.',checks=68500,additional_financial_checks=finance['checks']+finance['helper_checks'],artifacts=['INDEPENDENT_PROOF.md','out/VALIDATION.json','out/FINANCIAL_VALIDATION.json','out/ADVERSARIAL_WITNESSES.json']))
claim['status']='INDEPENDENTLY_ACCEPTED_CONDITIONAL_THEOREM_AND_FINITE_ONE_CORE_CERTIFICATE'
dump(R/'CLAIMS.json',[claim])
progress=dict(protocol_revision='2026-10-11-execution-v2',run_id=R.name,stream='B15',packet_id='A074',gap_id='C019-INHERITED-SIGNED-CHILD-ELIGIBILITY',attempt_id='A074-stage8-one-core-credit-hull-independent-review',method='Raw labelled stopping DAG, binary multilinear inclusion-exclusion, conditional occupied-block entropy, direct integer inner characters/edges, exact rational log profiles and outward intervals; finite Bellman induction and conserved signed-label kernels',mathematical_delta='Independent acceptance of unchanged A072-OTHER-CORE-STOPPING-CREDIT-HULL@1. Existing root credit exactly equals all-policy one-core requirement for all four labels;2916 states/5832 rows/68500 checks. Six financial policy reconstructions pass1906 additional checks;92 raw states refute current-deficit-only reset. No second-core or universal bound.',deliverable_status='COMPLETE_LOCAL_SOURCE_BOUND_INDEPENDENT_REVIEW',mathematical_status='CONDITIONAL_AND_FINITE_ONE_CORE_TARGET_ACCEPTED;FULL_FEI_OPEN',claim_versions_used=['A072-OTHER-CORE-STOPPING-CREDIT-HULL@1#'+digest],claims_created_or_changed=['Local independent acceptance record for unchanged A072 claim; shared indices untouched'],source_artifacts=[str(source/'CLAIMS.json'),str(source/'PROOF.md'),str(R/'INDEPENDENT_PROOF.md'),str(R/'out/VALIDATION.json'),str(R/'out/FINANCIAL_VALIDATION.json'),str(R/'out/source_receipts.json')],next_consumers=['A072','A071','A075','A089','A092','B15','B20'],next_action='A072/A089: on actual first-core stopped terminals, calculate the next remaining core hull against the actual carried credit, preserving every original signed label and spent donor; A092 independently review any claimed transfer. No credit reset to the instantaneous negative slack.',stagnant_substantive_attempts=0,blockers=['Second remaining core/interleaved continuation eligibility not established.','No dimension-independent bound on the unrestricted stopping-credit hull; equivalent universal FEI bill remains unpaid.','Earlier external donor-funding prefix is source input in this review.','Supervisor copying, index adoption, mirror verification and downstream use unobserved.'],packet_ids=['A074'])
dump(R/'PROGRESS.json',progress);(R/'PACKET_DELTA.json').write_bytes((R/'PROGRESS.json').read_bytes())
report=f'''# exact target, quantifiers, hypotheses and units

Independently review A072-OTHER-CORE-STOPPING-CREDIT-HULL@1, source canonical digest {digest}. Mathematical statement, hypotheses, source digest and version remain unchanged. ACCEPT its finite-DAG conditional theorem and Boolean one-core certificate. S=4I-H uses full Fourier entropy in bits on disjoint uniform physical blocks. Credit a>=0 is conserved in conditional mean, booked total D=S+a>=0, individual debit labels may be signed, stopping is always allowed, both physical outcomes remain. No new transfer flow or outside donor change is allowed. The Boolean target is exactly F_plus=J(-1,+1,g,g,g,g), g negative on{{0,1,2}} in six bits, J(x)=+1 iff x xor1 in{{0,1,2,4,8,16,32,6,17,40}}. Queries may adapt within one chosen remaining core only. Full FEI OPEN.

# sources actually read, revisions and theorem locators

At stage start read BOARD, own STATUS and B15 STREAM_NOTES v2; protocol dispatch selected the new A072 dependency rather than the already completed original witness census. Read A072 run20261023T015130Z REPORT, PROOF, CLAIMS, credit_hull.py and component_audit.py, plus HULL_CASES/validation outputs. PROOF's stopping hull, inherited-credit label kernels, one-core exhaustion, zero-denominator and universal-equivalence sections are the theorem locators. Earlier campaign/paper readings remain background; no new literature theorem is accepted here. Own earlier stage6 binary helper is imported with K=4 before any packet evaluation. No peer executable is imported or rerun. Final source byte hashes are in out/source_receipts.json. Personal brain self-care remains degraded/unverified because owner-model and state-of-mind notes are stale; they are not mathematical premises.

# complete derivation or exact first unsupported line

INDEPENDENT_PROOF.md supplies necessity and sufficiency by backwards induction: R(v)=max(0,-S(v),max_query mean R(child)). Immediate stopping and conditional-mean conservation force the lower bound. For any a>=R(v), assign child credit R(child)+a-mean R(child); all child debits S(child)+credit are nonnegative and have mean D+e. A positive-total-debit mean-one kernel transports every old signed label and the new e label. If total debit is zero, both child totals vanish and kernel1 preserves all signed cancellations. Nonnegative credit-owner labels are handled separately, including a=0. This proof is independent of any universal positivity assumption and of the earlier source donor-funding prefix.

Binary finite differences and entropy conditioned on occupied physical blocks give independent full H and I, checked against direct inner characters and pivotal edges. The raw labelled DAG retains all four original remaining core labels and all dummy query states. At each state, every allowed query is compared with the Bellman winner, physical influence telescopes exactly, all child credits/debits are nonnegative, and conditional means hold as rational log-linear identities. For each root, R=-S is an exact profile identity and R is rigorously in(2857328/10^8,2857329/10^8). Any existing actual account D>=0,a=D-S therefore has a>=R. There are twelve spectral profiles per literal core label, independently found after raw exhaustion; the source's two representative labels give24 profiles. All92 raw states with R>(-S)_+ are saved as adversarial witnesses against resetting future credit to the immediate deficit.

Six supplied policy trees are independently reconstructed using our S/R and physical labels. All44 query nodes and50 terminals preserve the six actual policy choices, true reaches, inherited labels and zero new flow. The two positive-debit initial amounts and their old labels are source inputs; their earlier funding prefix is NOT re-audited. Their additive inherited spare is kept explicitly, and general algebra proves continuation for every such amount. Interval overlaps diagnose source agreement; they are never used as equality proofs. No new source proof repair or altered hypothesis was supplied.

First unsupported line: on a stopped leaf after the first remaining core, the actual conserved credit dominates the next core's stopping hull, with all old labels and spent donor unchanged. Interleaving different remaining cores is also outside the finite application. The unrestricted hull bound R_K(f)<=L I(f) is equivalent to FEI(K+L), by immediate stopping and expected-terminal-influence monotonicity. This equivalence proves no bound on the hull.

# executed validation with domain, arithmetic, commands and outputs

FROZEN_SPEC.json precedes the pilot. An initial setup attempt stopped before its first case because out/ had not been created; out/SETUP_FAILURE.json preserves the failure and its directory-only repair. The unchanged pilot then passed729 states/1458 rows and17394 predicates in23.1117192s. FULL_SPEC_AMENDMENT.json froze a180-second full runtime allowance from this observation; domain, precision, dimension and memory estimate stayed fixed. The final full run passed2916 states/5832 rows,67261 audit+1239 helper=68500 predicates, in108.1523667s. Pilot predicates are excluded from the final count. Raw results are append-only CASES.jsonl with overwrite refusal and root checkpoints saved after each label.

Commands from A074: python -B -X utf8 runs/{R.name}/code/audit_hull.py --pilot; the same without --pilot; then python -B -X utf8 runs/{R.name}/code/audit_finance.py. The separately frozen FINANCIAL_SPEC.json precedes the policy reconstruction: six policies,44 rows,50 terminals,1374 audit+532 helper=1906 additional predicates in4.7400121s. Its runtime bound is55s. Final files are written by code/persist.py, which additionally validates all journal keys, the source digest, strict future-credit gaps and exact protocol schemas.

Fractions and direct integer character sums supply exact arithmetic. Strict comparisons use the own helper's48-term positive atanh expansion with proved tail and112-bit outward log2 rounding. Source192-bit intervals enter only comparisons or the explicitly supplied positive initial debit/labels. Four root source comparisons match. There are88 full labelled-table evaluations and22 inner tables; these are different counts from source compressed profiles. No symmetry quotient was used in the DAG. Expected memory150MB for the main job and100MB for finance, peak unmeasured; no expected>300MB job was started, so memok was not triggered. No GPU, new detached job or visible window. No Lean verification is claimed; the exact finite certificate and written real-valued induction are the proof objects.

# proof dependencies and changed downstream conclusions

The source statement-plus-hypotheses digest is independently recomputed using its declared canonical payload keys exact_statement and hypotheses. The first save attempt held before protocol/rolling writes because my verifier assumed key statement; source finalize.py line8 resolves the discrepancy. out/HASH_CONVENTION.json pins both digests and preserves the failed save receipt. The source digest is retained unchanged. Local CLAIMS.json adds independent acceptance without changing source mathematics, files or version. The load-bearing reconstruction uses character orthogonality, binary polynomial interpolation, conditional spectral entropy, exact physical restriction identities and finite backwards induction. Source's earlier A071 subsidy optimizer is not needed for this recurrence proof; it only motivates which actual initial accounts are supplied. This review independently establishes continuation for all nonnegative incoming debits, not the historical creation of donor credit. Existing saturation/no-renewal and negative-slack results remain intact. A072/A071/A089 may now consume an independently checked one-core continuation, but cannot turn it into a new draw on the same spent donor or infer a universal constant.

# one next mathematical action and independent reviewer

A072/A089 should freeze the actual stopped terminals of a first-core continuation and compare the next remaining core's exact stopping hull to each carried credit, retaining the original signed labels, true reaches and donor bookings. A092 should challenge that inequality or independently check a claimed new transfer. This directly tests the unpaid compositional step; another same-core census would repeat a closed finite target.

# actual persistence receipts or precise save blocker

Saved four protocol files, INDEPENDENT_PROOF.md, three code files, frozen specs/amendment, setup-failure receipt, pilot/full append-only journals, root checkpoints, policy validation and92 adversarial witnesses inside A074. out/schema_validation.json checks exact protocol fields, unchanged source digest,2916 unique final keys, progress/delta byte identity and two-line rolling STATUS. out/manifest.json binds every other run file by size/SHA256 and is reread for verification. All files are below20MB. STATUS, WORKLOG and LEARNED are current. No git, mail, brain write, trading access, peer mutation or deletion occurred. Supervisor copying, mirror adoption and actual downstream use are unobserved.

# Universal bridge

This stage moves C019 stopping-tree payment by independently accepting the exact inherited-credit hull and its all-policy continuation within any one remaining core:2916 raw states,5832 query rows and six retained-label policy reconstructions. It also certifies that92 raw intermediate states need more than the instantaneous negative slack, so future credit cannot be reset greedily. No universal constant improves. The unpaid bridge is eligibility of a second remaining core under the actual surviving credit, followed by unrestricted interleaving; a uniform bound for the unrestricted hull is itself equivalent to FEI. NEXT tests precisely that compositional account inequality, the shortest available route beyond the one-core result toward full FEI, without renewing a spent donor.
'''
(R/'REPORT.md').write_text(report,encoding='utf-8')
paths=[protocol_path,ROOT/'BOARD.md',ROOT/'claude/B15/STREAM_NOTES.md',source/'REPORT.md',source/'PROOF.md',source/'CLAIMS.json',source/'code/credit_hull.py',source/'code/component_audit.py',source/'code/finalize.py',source/'out/HULL_CASES.json',source/'out/VALIDATION.json',a.helper]
dump(R/'out/source_receipts.json',[dict(path=str(p),bytes=p.stat().st_size,sha256=sha(p)) for p in paths])
(A/'STATUS.md').write_text('STATE: A074 stage8 complete: A072 one-core stopping-credit hull@1 independently accepted unchanged;2916 raw states/5832 rows/68500 checks; six policy continuations/1906 additional checks;FEI OPEN.\nNEXT: A072/A089 compare second remaining-core hull to actual carried credit at first-core stopped terminals; preserve old labels/true reaches/spent donor;A092 review; no greedy credit reset.\n',encoding='utf-8')
with (A/'WORKLOG.md').open('a',encoding='utf-8') as f:f.write('\n'+now+' stage8 '+R.name+': Independent unchanged acceptance of A072-OTHER-CORE-STOPPING-CREDIT-HULL@1#'+digest+'. Own binary finite-difference conditional-entropy engine and raw all-label DAG:2916 states/5832 rows/68500 checks,108.1523667s; rootR=-S in(.02857328,.02857329) for allfour labels. Pilot17394 checks,23.1117192s; setup-only missing out directory repaired and recorded. Six source policy choices reconstructed:44 rows/50 terminals/1906 extra checks,4.7400121s; positive-debit initial funding is source input, not independently re-audited.92 strict future-credit-gap raw states saved. General finite Bellman/zero-total signed-label proof independently reconstructed. No second-core bound; full FEI OPEN. Files local only.\n')
with (A/'LEARNED.md').open('a',encoding='utf-8') as f:f.write('\n'+now+' stage8: A072-OTHER-CORE-STOPPING-CREDIT-HULL@1#'+digest+' independently accepted unchanged for the conditional finite-DAG theorem and fixed one-core Boolean application. Minimal conserved inherited credit is R=max(0,-S,max_query meanRchild); assign childR+(a-meanRchild). For signed debit labels with T=0, nonnegative child totals are zero and kernel1 preserves all signed cancellations. Stop allowed is essential to the lower bound. Fplus allfour literal corelabels: exactRroot=-Sroot in(.02857328,.02857329);2916 raw states/5832 rows checked without quotient.92 raw states require future credit beyond(-S)+, so current-deficit credit reset is invalid. Source six policy continuations reconstructed with own spectra; earlier positive-debit funding prefix remains source input. Uniform unrestricted R_K<=L I is equivalent to FEI(K+L), not a proof of that bound. Next: second-core hull against actual carried credit, keeping original labels and spent donor.\n')
proto=json.loads(protocol_path.read_text(encoding='utf-8'))['required_per_run']
assert set(progress)=={x.split(' (')[0] for x in proto['progress_fields']}
assert set(claim)==set(proto['claim_fields'])
assert all('# '+x in report for x in proto['report_fields'])
assert (R/'PROGRESS.json').read_bytes()==(R/'PACKET_DELTA.json').read_bytes()
assert len((A/'STATUS.md').read_text(encoding='utf-8').splitlines())==2
dump(R/'out/schema_validation.json',dict(passed=True,exact_protocol_fields=True,unchanged_statement_and_hypotheses_digest=digest,delta_byte_identical=True,final_unique_labelled_states=2916,raw_future_credit_obstructions=92,status_lines=2,remote_mirror_verified=False))
files=[]
for p in sorted(R.rglob('*')):
 if p.is_file() and p.name!='manifest.json':
  assert p.stat().st_size<20_000_000
  files.append(dict(path=str(p.relative_to(R)),bytes=p.stat().st_size,sha256=sha(p)))
dump(R/'out/manifest.json',dict(saved_at=now,files=files,excluded_self=True,remote_copy_verified=False))
for entry in files:
 p=R/entry['path'];assert p.stat().st_size==entry['bytes'] and sha(p)==entry['sha256']
print(json.dumps(dict(saved=True,manifest_verified_files=len(files),claim_digest=digest,main_checks=68500,financial_checks=1906,raw_states=2916,query_rows=5832,naive_credit_reset_obstructions=len(witnesses),full_FEI='OPEN')))
