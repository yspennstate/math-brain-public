from pathlib import Path
import json,hashlib,copy

R=Path(__file__).resolve().parents[1];HOME=R.parents[1];FLEET=HOME.parents[1]
SRC=FLEET/'agents/A071/runs/20261023T113913Z-fleet03-A071-search-space-design'
PROTO=Path(r'math-open-problems/reports\fei-2026-10-11\EXECUTION_PROTOCOL.json')
def rd(p):return json.loads(p.read_text(encoding='utf-8-sig'))
def wr(p,s):p.write_text(s,encoding='utf-8',newline='\n')
def js(p,x):wr(p,json.dumps(x,indent=2,ensure_ascii=False)+'\n')
def sha(p):return hashlib.sha256(p.read_bytes()).hexdigest()
protocol=rd(PROTO);v=rd(R/'out/VALIDATION.json');pilot=rd(R/'out/PILOT.json');h=rd(R/'out/RESTRICTION_HULL.json')
assert v['status']==h['status']=='PASS'
assert v['helper_sha256']==sha(R/'code/review.py')==rd(R/'out/FROZEN_SPEC.json')['helper_sha256']
assert h['helper_sha256']==sha(R/'code/restriction_hull.py')==rd(R/'out/HULL_FROZEN_SPEC.json')['helper_sha256']
assert (h['all_physical_restrictions'],h['full_query_rows'])==(2187,5103)
producer=rd(SRC/'CLAIMS.json');claims=[]
for old in producer:
 c=copy.deepcopy(old)
 c['review_records'].append({'reviewer':'A092','independent_reviewer':True,'run_id':R.name,'date_utc':'2026-10-23','verdict':'INDEPENDENTLY_ACCEPTED_UNCHANGED_STATEMENT_AT_STATED_SCOPE','method':'Original full truth table, direct character sums plus butterfly/edge reproduction, exact symbolic prime logs and integer signs; separate analytic all-dimensional Lipschitz/coupling proof. No producer helper imported.','proof_files':['PROOF.md','code/review.py','out/CIRCUIT_CERTIFICATE.json','out/VALIDATION.json'],'supplemental_refinement':{'scope':'THIS literal circuit only, all real K>=3','all_physical_restrictions':2187,'physical_query_rows':5103,'true_full_stopping_deficit_hull':'0','certificate':'out/RESTRICTION_HULL.json'},'limitations':['No universal nonempty-component coherence or initial source-price proof','No refutation of A089 conditional rerouting, all possible owner allocations, or FEI','Empty-component influence payer must actually be unused after all old debits']})
 c['status']='INDEPENDENTLY_ACCEPTED_AT_STATED_SCOPE'
 assert all(c[k]==old[k] for k in ['exact_statement','hypotheses','statement_sha256','version','proof_dependencies'])
 assert set(c)==set(protocol['required_per_run']['claim_fields'])
 claims.append(c)
assert len(claims)==2
js(R/'CLAIMS.json',claims)
total=v['exact_assertions']+h['exact_assertions']
delta={'protocol_revision':protocol['revision'],'run_id':R.name,'stream':'B19','packet_id':'A092','gap_id':'C019-SIGNED-NONEMPTY-COMPONENT-COHERENCE','attempt_id':'A092-stage20-independent-envelope-referee','method':'Literal Boolean truth tables; independent direct characters/physical edges; symbolic entropy forms and exact integer signs; all-restriction stopping hull; independent analytic universal empty-component proof.','mathematical_delta':'A071 two scoped claims independently accepted unchanged: U_K=C_plus+sum(q_j*rho_K) fails superharmonicity for EVERY real K>=3 by G in(0.107184,0.107185), query influence9/64. Universal EMPTY component V=phi(Ef)+3I is superharmonic and <=9I/2. ALL2187 actual restrictions have H<=3I and true stopping deficit hull0, so proposed stock is overprotection, not unavoidable FEI debt.','deliverable_status':'COMPLETED_LOCALLY','mathematical_status':'TWO_SCOPED_CLAIMS_INDEPENDENTLY_ACCEPTED; FULL_FEI_OPEN','claim_versions_used':[{'claim_id':c['claim_id'],'version':c['version'],'statement_sha256':c['statement_sha256']} for c in claims],'claims_created_or_changed':[{'claim_id':c['claim_id'],'version':c['version'],'change':'Independent A092 acceptance; exact statement, hypotheses and hash preserved'} for c in claims],'source_artifacts':[str(SRC/n) for n in ['CLAIMS.json','REPORT.md','PROOF.md','VACUUM_PROOF.md']]+['PROOF.md','out/SOURCES.json','out/CIRCUIT_CERTIFICATE.json','out/VALIDATION.json','out/RESTRICTION_HULL.json'],'next_consumers':['A071','A072','A074','A075','A080','A089','A094','B15','B19','B20'],'next_action':'A071/A089/A080 test NONEMPTY signed-correction coherence near an actual nonempty coefficient cancellation, retaining a paid full empty component, BOTH terminals, old owner labels and actually unused original influence stock; A074/A094 review. Do not repair by merely increasing K or donating spent influence.','stagnant_substantive_attempts':0,'blockers':['Universal nonempty correction coherence and influence-paid initial envelope remain unproved.','Supervisor mirroring/downstream adoption unverified.'],'packet_ids':['A092']}
assert set(delta)=={x.split(' (')[0] for x in protocol['required_per_run']['progress_fields']}
js(R/'PROGRESS.json',delta);(R/'PACKET_DELTA.json').write_bytes((R/'PROGRESS.json').read_bytes())
report=f'''# A092 stage20: independent stopping-envelope counterexample referee

## exact target, quantifiers, hypotheses and units

Independently audit A071-POSITIVE-OUTER-CORRECTION-ENVELOPE-FAILS@1 and A071-VACUUM-COMPONENT-ENVELOPE@1. Literal disjoint Boolean circuit F=h(g3,g2,g2), where g_m is negative only at0 and h positive only on three positive signs; query original bit0. Entropy in bits; uniform physical coordinates; BOTH complete children retained. The proposed U_K=C_plus+sum(q_j*rho_K(inner_j)) fails full-query superharmonicity for EVERY real K>=3. Its missing mean stock is 0.107184<G<0.107185; actual query influence9/64. Separately V=phi(Ef)+3I is an all-dimensional superharmonic envelope for the EMPTY Fourier entropy term and V<=9I/2. These exact scopes are independently accepted. Full FEI is OPEN.

## sources actually read, revisions and theorem locators

Latest BOARD read: supervisor12:16UTC; current A092 STATUS stage19; full B19 leadv2 (historical endpoint/selector targets already completed in earlier stages). Fresh useful objection consumed by dispatch: A071 run {SRC.name}, complete CLAIMS, REPORT, PROOF sections1--5 and VACUUM_PROOF. Current EXECUTION_PROTOCOL revision {protocol['revision']} and machine-wide AGENTS read. Fresh source paths and SHA256 are in out/SOURCES.json. Earlier campaign/paper intake remains background; no new paper-priority statement or unexamined literature theorem is invoked. Owner campaign endpoint2026-10-23 14:49UTC supersedes the protocol's older endpoint. No A071 implementation imported or executed.

Read-only math recall was attempted once through runpy and failed because its sibling recall_client module was not on that invocation's import path; this is an infrastructure failure, not evidence the store lacks the result. No recall output or stale personal note is used as a proof premise.

## complete derivation or exact first unsupported line

PROOF.md contains the independent complete derivation. All128 parent values are constructed as AND-of-OR clauses of sizes3,2,2. Both children retain all six remaining physical variables; the outcome1 child's two dummy coordinates are kept. Direct character sums give full H; physical influences independently check Fourier I and pivotal weights. Complete C=H(F)-sum(q_j H(inner_j)) is positive at parent and both children by three exact integer-power comparisons. Point cores of sizes0..3 and every restriction satisfy H<=3I, the only logarithmic endpoint being3^9>2^14. Consequently all inner stopping hulls vanish for all real K>=3, so U=C at these three states.

The exact drift is G=-37/16-(567/512)log2(3)-(25/1024)log2(5)+(3087/2048)log2(7)>0, certified by7^3087>2^4736*3^2268*5^50. Parent and both full-child I are111/64,27/16,3/2, whose difference is9/64. Adding lambda I needs lambda>=(64/9)G>0.762198 on this row; this is a necessary local repair, not a universal sufficient coefficient. Mean-conserved owner relabeling cannot fund both candidate children from EXACTLY U(parent), but an actual unused extra payer or a different envelope can. A089's conditional rerouting theorem and every possible allocation are not refuted.

For the universal component, phi(t)=-t^2 log2(t^2) is globally2/ln2-Lipschitz, with ln2>2/3. Physical coupling gives |mu0-mu1|<=2Inf_j, so the mean increase of phi is <=3Inf_j. Exact influence telescoping proves V superharmonic in EVERY dimension. Also phi(Ef)<=Var(f)/ln2<=3I/2, hence V<=9I/2. This pays ONLY the empty entropy term. It does not create an unused owner when inserted after earlier debits. On the witness, empty drift is85/512-(25/1024)log2(5); subtracting it leaves a strictly negative nonempty drift, exactly7^3087<2^5076*3^2268.

Additional exact closure: EVERY one of this circuit's2187 labelled physical restrictions satisfies H<=3I; all5103 outgoing query rows retain both full children. Backward stopping-tree induction yields the ACTUAL full stopping deficit hull0 for the parent and all descendants, at K=3 and every K>=3. Thus this counterexample exposes candidate overprotection rather than unavoidable FEI debt. It does not extend to larger circuits by extrapolation. First unsupported universal line: pay/cohere the NONEMPTY signed correction plus inherited inner stopping hulls from actually unused original influence, with the full empty bill and all old bookings retained.

## executed validation with domain, arithmetic, commands and outputs

out/FROZEN_SPEC.json precedes the main checks. Commands: `python -B -X utf8 code/review.py --pilot`, then `python -B -X utf8 code/review.py`. Literal states have dimensions7,6,6; direct character sums are checked against a separate butterfly transform and physical edge counting. Point-core sizes0..3 are exact. Universal-component sanity census uses all16 two-bit tables/32 queries in the pilot and all256 labelled three-bit tables/768 queries in the primary. Pilot: {pilot['exact_assertions']} exact assertions PASS in {pilot['seconds']:.3f}s. Primary: {v['exact_assertions']} exact assertions PASS in {v['seconds']:.3f}s. Universal quantifiers follow the analytic proof, not the finite census.

Separate frozen command `python -B -X utf8 code/restriction_hull.py` enumerates all2187 original-circuit restrictions and5103 query rows, PASS: {h['exact_assertions']} exact assertions in {h['seconds']:.3f}s. All states are visited;68 byte-identical full truth tables are memoized without omitting any state or query. Exact immediate deficit signs and child induction prove the full stopping hull0. Combined PRIMARY plus restriction audit: {total} exact assertions; pilot counts are NOT added. Counts include normalization and identity checks, not independent theorems.

Arithmetic is exact integer/Fraction/symbolic prime-log arithmetic. Clearing symbolic-log denominators generates the integer sign certificates independently of numerical logarithms. Reported decimal brackets use the earlier A092 rigorous44-term rational-log helper, including proved range reduction, rounding and tail bounds. out/CIRCUIT_CERTIFICATE.json records original parent/child tables, all C/H forms, empty masses, integer exponents, integer hashes and bounds. out/RESTRICTION_HULL.json records the exhaustive stopping result. No producer checker, floating proof, Lean certificate or all-dimensional inference from a finite pass. Estimated memory90MB; pilot55s/primary120s/restriction55s limits; no >300MB job, GPU, detached process, dimension escalation or helper agent.

## proof dependencies and changed downstream conclusions

Both exact source statements, hypotheses, versions and SHA256 are preserved in CLAIMS; independent A092 review records are added. Proofs are reconstructed from finite Fourier orthogonality, physical coupling/influence telescoping, elementary calculus, entropy definitions and the explicitly checked integer inequalities. A071/A072/A074/A075/A080/A089/A094 may consume the local obstruction and universal EMPTY-component lemma at their respective scopes. Raising K cannot restore the candidate because its inner hulls stay0. The signed nonempty correction remains a universal obligation; the finite favorable remainder cannot be assumed hereditary. Prior A096 parity obstruction remains accepted and is not rerun here.

## one next mathematical action and independent reviewer

A071/A089/A080 test the NONEMPTY signed correction near one actual nonempty Fourier coefficient cancellation, after explicitly paying the complete empty component from an unused ORIGINAL owner. Preserve old debit labels, spent donors and BOTH full terminals; test superharmonicity together with initial influence price. A074/A094 review that concrete transaction. A092 can independently referee its truth table and strict sign. This targets the current universal coherence gap; extending a closed finite hull census or merely increasing K leaves that gap unchanged.

## actual persistence receipts or precise save blocker

Four protocol files, independent proof, frozen specs, code and exact outputs are saved inside A092. Rolling STATUS is two lines; WORKLOG and LEARNED append the new scoped facts. out/PERSISTENCE.json validates exact schema keys, unchanged source statement/hypothesis/hash fields, helper hashes, byte-identical progress/delta, file limits and every listed artifact SHA256. Research writes are confined to A092; session wake/checklist are explicitly directed administrative actions. No git, email, peer message, shared registry, other-agent edit, trading access, process shedding or restart. Supervisor copy, remote adoption and downstream use are unverified.

Compute-state timestamp13:57:59 local was unchanged across two reads more than30s apart and the governor log was read; historical memory figures are not claimed current. No competing governor or large job was launched. Checklist working updateT-20261023-427 failed with its lock timeout; final administrative disposition is recorded separately. Brain self-care is degraded/unverified: model98.7h, state83.3h and dream34h stale at wake; affected personal continuity is excluded from mathematical premises. No research computation remains running.

## Universal bridge

This stage moves C019 stopping-tree payment and C024 history-transfer auditing by independently certifying a missing mean stockG>0.107184 bits for the proposed envelope at EVERY K>=3, while proving its literal witness's actual stopping deficit hull is0 across all2187 restrictions. It independently closes the universal EMPTY-component payment V<=9I/2 without discarding that terminal bill. The NONEMPTY correction's universal coherence and influence-paid initial owner remain open. NEXT tests a nonempty cancellation with that complete empty payment and SAME actually unused original stock, old debit labels and both terminals; this is the shortest route to the remaining universal envelope, whereas another finite-census extension cannot supply it. Full FEI remains OPEN.
'''
wr(R/'REPORT.md',report)
status=f'STATE: A092 stage20 saved: A071 envelope obstruction ALL K>=3 and universal EMPTY V<=9I/2 independently HOLDS;all2187 restrictions true hull0;{total} exact checks PASS;FEI OPEN.\nNEXT: A071/A089/A080 test NONEMPTY coefficient cancellation with paid full empty term,SAME unused original owner,old debits/both terminals;A074/A094 review;do not raise K or reuse spent donor.\n'
wr(HOME/'STATUS.md',status)
entries=[('WORKLOG.md',f'2026-10-23 12:13 UTC stage20: Consumed A071 new actual seven-bit envelope objection. Independently reconstructed all full truth tables/spectra/physical influences and exact integer drift. Accepted both unchanged scoped claims: U_K fails for ALL real K>=3 byG in(.107184,.107185), queryInf9/64; universal EMPTY component V=phi(mean)+3I<=9I/2 paid under every query. Supplemental exhaustive2187 restrictions/5103 query rows prove actual full deficit hull0 for ALL K>=3. Primary{v["exact_assertions"]}+restriction{h["exact_assertions"]}={total} assertions PASS; pilots not added. All research artifacts/hashes saved; nonempty universal coherence/source-price open; no research job left running.\n'),('LEARNED.md','2026-10-23 stage20 durable referee fact: Literal AND-of-OR(3,2,2), query bit0, has full correction envelope drift G=-37/16-(567/512)log2(3)-(25/1024)log2(5)+(3087/2048)log2(7)>0.107184 for everyK>=3 because ALL inner hulls0. Exact sign7^3087>2^4736*3^2268*5^50; actual queryInf9/64. All2187 physical restrictions haveH<=3I, so TRUE full stopping hull0: candidate overprotection is not necessary FEI debt. Independently accepted universal EMPTY component V=phi(mean)+3I<=9I/2, paid by mean coupling/global Lipschitz; its payer must actually be unused. Empty-term subtraction gives negative nonempty drift on this witness only; no universal coherence follows.\n')]
for name,line in entries:
 with (HOME/name).open('a',encoding='utf-8',newline='\n') as f:f.write('\n'+line)
assert all(('## '+x) in report for x in protocol['required_per_run']['report_fields'])
assert report.rstrip().endswith('Full FEI remains OPEN.')
assert len(status.splitlines())==2
assert (R/'PROGRESS.json').read_bytes()==(R/'PACKET_DELTA.json').read_bytes()
files=[]
for p in sorted(R.rglob('*')):
 if p.is_file() and p.name!='PERSISTENCE.json':
  assert p.stat().st_size<20*1024*1024
  files.append({'path':str(p.relative_to(R)),'bytes':p.stat().st_size,'sha256':sha(p)})
receipt={'status':'PASS','protocol_exact_fields':True,'two_source_claims_statement_hypotheses_hash_unchanged':True,'progress_delta_byte_identical':True,'status_two_lines':True,'primary_plus_restriction_exact_assertions':total,'all_files_under20MB':True,'files':files,'full_fei':'OPEN','remote_mirror':'UNVERIFIED','research_jobs_left_running':[]}
js(R/'out/PERSISTENCE.json',receipt)
for item in files:assert sha(R/item['path'])==item['sha256']
print(json.dumps({'status':'PASS','accepted_claims':[c['claim_id'] for c in claims],'primary_plus_restriction_assertions':total,'hashed_files':len(files),'FEI':'OPEN','research_jobs_left_running':0}))
