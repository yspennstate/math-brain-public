from pathlib import Path
import json,hashlib,copy

R=Path(__file__).resolve().parents[1]
HOME=R.parents[1]
FLEET=HOME.parents[1]
SRC=FLEET/'agents/A096/runs/20261023T053800Z-account03-A096-live-gap-ledger'
PROTO=Path(r'math-open-problems/reports\fei-2026-10-11\EXECUTION_PROTOCOL.json')
def read(p):return json.loads(p.read_text(encoding='utf-8-sig'))
def write(p,s):p.write_text(s,encoding='utf-8',newline='\n')
def js(p,x):write(p,json.dumps(x,indent=2,ensure_ascii=False)+'\n')
def sha(p):return hashlib.sha256(p.read_bytes()).hexdigest()

protocol=read(PROTO);v=read(R/'out/VALIDATION.json');pilot=read(R/'out/PILOT.json')
assert v['status']=='PASS' and (v['families'],v['query_nodes'])==(648,2916)
assert v['helper_sha256']==sha(R/'code/check.py')==read(R/'out/FROZEN_SPEC.json')['helper_sha256']
producer=next(c for c in read(SRC/'CLAIMS.json') if c['claim_id']=='A096-ZERO-PHASE-QUERY-REFUND-OBSTRUCTION')
claim=copy.deepcopy(producer)
claim['review_records'].append({'reviewer':'A092','run_id':R.name,'date_utc':'2026-10-23','verdict':'INDEPENDENTLY_ACCEPTED_UNCHANGED_STATEMENT_AT_LOCAL_SUPPLIER_SCOPE','method':'Reconstructed original Boolean truth tables, integer Walsh transforms, independent physical influences and both full child references; direct character check at source witness; analytic proof with exact sign. No producer implementation imported.','files':['PROOF.md','code/check.py','out/VALIDATION.json','out/WITNESS.json'],'clarification':'Influence one refers to parity seed. The full displayed wrapper seed-coordinate influence is 3/8. Current local refund alone fails; no claim that original surplus is unavailable.','exclusions':['Companion A096 phase-funded theorem is not independently accepted by this review','No universal FEI counterexample','No necessity claim for the prescribed ghost target']})
claim['status']='INDEPENDENTLY_ACCEPTED_AT_STATED_LOCAL_SUPPLIER_SCOPE'
assert all(claim[k]==producer[k] for k in ['exact_statement','hypotheses','statement_sha256','version','proof_dependencies'])
assert set(claim)==set(protocol['required_per_run']['claim_fields'])
js(R/'CLAIMS.json',[claim])
delta={'protocol_revision':protocol['revision'],'run_id':R.name,'stream':'B19','packet_id':'A092','gap_id':'C024-ZERO-SINGLETON-NONEMPTY-TRANSPORT','attempt_id':'A092-stage19-zero-phase-independent-review','method':'Original truth-table/referee reconstruction; exact Fourier and physical-edge arithmetic; full-child CE and analytic logarithm sign; every labelled controller restriction.','mathematical_delta':'Independently accepts A096 zero-phase obstruction unchanged: all current query refunds vanish, while BOTH full-child nonempty replacements cost (3/8)log2(64/63)>3/512 each. Seed influence=1, wrapper influence=3/8. General parity-degree proof shows H fixed and H/I tends to zero; no FEI counterfamily.','deliverable_status':'COMPLETED_LOCALLY','mathematical_status':'LOCAL_OBSTRUCTION_INDEPENDENTLY_ACCEPTED; FULL_FEI_OPEN','claim_versions_used':[{'claim_id':producer['claim_id'],'version':producer['version'],'statement_sha256':producer['statement_sha256'],'scope':'Only zero-phase obstruction; companion phase theorem context only'}],'claims_created_or_changed':[{'claim_id':producer['claim_id'],'version':producer['version'],'change':'Independent review added; original statement/hypotheses/hash preserved'}],'source_artifacts':[str(SRC/'CLAIMS.json'),str(SRC/'DERIVATION.md'),str(SRC/'REPORT.md'),'PROOF.md','out/SOURCES.json','out/VALIDATION.json','out/WITNESS.json'],'next_consumers':['A096','A079','A085','A094','A097','B20'],'next_action':'A096/A079 specify ONE necessary zero-singleton conditional-nonempty transport and its ACTUAL unused original surplus after old debits; A094 independently tests payment with both complete terminals. Do not infer current-refund payment merely from positive influence.','stagnant_substantive_attempts':0,'blockers':['Universal influence-priced initial complete source and necessary zero-singleton transport payment remain open.','Supervisor copy/remote adoption not verified.'],'packet_ids':['A092']}
expected={k.split(' (')[0] for k in protocol['required_per_run']['progress_fields']}
assert set(delta)==expected
js(R/'PROGRESS.json',delta);(R/'PACKET_DELTA.json').write_bytes((R/'PROGRESS.json').read_bytes())

report=f'''# A092 stage19: independent zero-phase counterexample referee

## exact target, quantifiers, hypotheses and units

Review A096-ZERO-PHASE-QUERY-REFUND-OBSTRUCTION@1 from its actual seven-bit Boolean definition. The exact false proposed supplier funds EVERY prescribed fixed positive conditional-nonempty replacement solely from the CURRENT relevant physical query refunds. In the displayed wrapper the seed has influence1, the full wrapper coordinate has influence3/8, all query refunds are exactly0, and each complete child replacement costs (3/8)log2(64/63)>3/512 bits. BOTH children are charged, so the mean has the same positive cost. Independent acceptance is limited to this obstruction; the companion phase-funded theorem is not accepted here. Full FEI remains OPEN.

## sources actually read, revisions and theorem locators

Latest BOARD read: written 2026-10-23 06:17 UTC; own stage18 STATUS; B19 STREAM_NOTES v2 (2026-10-11, still names the already completed historical endpoint targets); complete current EXECUTION_PROTOCOL revision {protocol['revision']}. Fresh dependency consumed under dispatch: A096 run {SRC.name}, CLAIMS exact zero-phase statement, REPORT and DERIVATION Sections1--4, especially Section4 parity obstruction. Its companion Gram/Pinsker proof was read for context only. Fresh source paths/SHA256 are in out/SOURCES.json. Previous-stage paper/protocol context is retained; no fresh literature-priority assertion or unquoted paper theorem is used. Current owner campaign endpoint 2026-10-23 14:49 UTC supersedes the old protocol date. No producer checker executed or imported.

## complete derivation or exact first unsupported line

PROOF.md gives the complete independent derivation. For any fixed complementary controller a,b=1-a^2 and parity degree k>=3, F=a+sigma*b*parity_k is Boolean. Its only seed Fourier frequencies are empty and full, with complete masses A_U^2 and B_U^2. Every seed query has singleton coefficient0 but wrapper influence beta=E b. Both actual children have squared law equal to the inherited frequency marginal. No occupied frequencies collide under erasure, so B_j=0; Q=P gives conditional occupancy KL0, and each inherited child is already the true law, giving both coherent calibration refunds0. Replacing the child's parity frequency by63/64 of itself plus1/64 at a distinct nonempty singleton raises its FULL CE by beta*log2(64/63). At beta=3/8, ln(64/63)>1/64 and ln2<1 give the exact strict lower bound3/512. No floating sign is used.

The full wrapper influence is3/8, not1; the source's influence-one phrase refers to its parity seed. This clarification preserves the source claim, hypotheses and hash unchanged. It does not weaken the relevant-query obstruction. The phase-adaptive theorem correctly chooses no change at d=0 and is not refuted. With any original unused account U, node reach w and old bookings retained, the exact remaining reserve is U-w*beta*log2(64/63). This proof supplies no reason U must be insufficient. The first unsupported universal line remains an influence-priced original source/surplus that funds a NECESSARY zero-singleton profile conversion; necessity of this particular ghost target is not claimed.

H(F)=H((A_U^2)_U,(B_U^2)_U)<=r+1 is independent of k, and I(F)=sum |U|(A_U^2+B_U^2)+k*beta. Thus for a fixed controller beta>0, H/I tends to0. This is a local supplier counterexample and cannot be promoted to a Boolean FEI disproof.

## executed validation with domain, arithmetic, commands and outputs

Frozen specification: out/FROZEN_SPEC.json. Independent checker v2 traverses all3^4 labelled physical restrictions of the original controller, sigma=+-1, k=3,4,5,6, and every seed query: {v['families']} Boolean truth tables, {v['query_nodes']} physical query nodes,5832 full children. No symmetry reduction or dimension escalation. Integer Walsh butterflies reconstruct all spectra; direct character sums separately verify the unrestricted seven-bit source coefficients; physical edges verify every influence; both physical children and their COMPLETE references are constructed. Reference-only target atoms and both terminals are retained.

Commands: `python -B -X utf8 code/check.py --pilot` then `python -B -X utf8 code/check.py`. The six-node v2 pilot passed {pilot['exact_assertions']} exact assertions in {pilot['seconds']:.3f}s. Primary passed {v['exact_assertions']} exact assertions in {v['seconds']:.3f}s:3456 strictly positive full-child resets and2376 exact zero-tail unchanged endpoints. Assertion counts include bookkeeping and normalization, not independent mathematical theorems. Exact log intervals use A092's prior44-term atanh helper with proved range reduction/rounding/tail bounds; the positive sign also has the separate elementary analytic proof above. out/WITNESS.json contains the original table, exact influence, full root H interval and both full CE increments.

The first v1 pilot and primary also passed; their files are preserved. V2 replaces redundant occupancy self-equalities with actual truth-table conditional probabilities compared to the independently constructed controller reference. No mathematical or domain change. V1 and v2 assertion counts are not added. Pilot deadline55s and main180s; estimated memory90MB, no >300MB job, no GPU, detached work or formal-assistant claim.

## proof dependencies and changed downstream conclusions

The accepted claim has no proof dependencies; its source is reconstructed using Boolean Fourier expansion, exact physical restriction, and the definition of complete CE. SHA256 and exact statement/hypotheses are retained in CLAIMS with an independent A092 review record. A096/A079/A085/A094 should reject a blanket refund>=c*Inf_j inference: Gamma positive does not help at d=0. The full phase-funded theorem, universal source pricing and surplus payment are separate unresolved/review obligations. Prior stage18 refund result is not reused as a new theorem, and calibration absorption is not re-investigated.

## one next mathematical action and independent reviewer

A096/A079 specify one NECESSARY nonempty conversion on a zero-singleton child together with the actual unused ORIGINAL source surplus after all old charges. A094 checks its exact signed payment, retaining both full terminals. This consumes the new obstruction rather than inventing an unused refund or repeating another vacuum calibration. A092 may referee the original truth table and sign of that concrete transport. No message has been sent to another agent.

## actual persistence receipts or precise save blocker

The four protocol files, complete proof, frozen specs, independent helper and results are saved inside A092. out/PERSISTENCE.json checks exact protocol keys, source statement preservation, identical progress/delta bytes, helper hashes, final STATUS two-line format, file limits and every listed file SHA256. Rolling STATUS, WORKLOG and LEARNED are updated. No git, mail, brain-store write, outside-agent research write, process termination or shared-index modification. Supervisor copying, mirror adoption and downstream use remain unverified. Checklist working update encountered its infrastructure lock timeout; recorded in out/INFRASTRUCTURE.json, separate from successful math. Brain self-care is degraded/unverified for personal-context continuity; stale personalization sources are not proof premises. No research job remains running.

## Universal bridge

This stage moves C024 history-transfer auditing feeding C018 by independently certifying an exact zero-refund/positive-complete-cost Boolean obstruction: beta*log2(64/63)>3/512 in the source wrapper despite positive actual influence3/8. It removes a false universal local supplier while preserving the phase-adaptive rule and any genuinely unused original bank. The original influence-priced source and required zero-singleton transport payment remain open. The shortest route is a concrete necessary transport charged to that SAME unused original surplus with old bookings and both full terminals, because another parity computation or calibration identity cannot supply the missing universal money.
'''
write(R/'REPORT.md',report)
status='STATE: A092 stage19 saved: A096 zero-phase obstruction independently HOLDS; full-wrapper influence3/8, zero current refund, each full child cost>3/512;98806 exact checks PASS;FEI OPEN.\nNEXT: A096/A079 supply NECESSARY zero-singleton nonempty transport plus ACTUAL unused original surplus after old debits;A094 audit both full terminals;phase-funded theorem separately unreviewed.\n'
write(HOME/'STATUS.md',status)
for path,text in [('WORKLOG.md','2026-10-23 06:18 UTC stage19: Consumed new A096 dependency after BOARD closed original-source return target. Independently reconstructed parity3 signed wrapper and all physical-controller restrictions. Accepted zero-phase obstruction unchanged, clarified seed influence1 versus wrapper3/8; cost=(3/8)log2(64/63)>3/512 per full child, all current refunds0. Primary v2:648 truth tables/2916 nodes/98806 exact assertions PASS; v1 outputs retained, not added. General parity degree proof H fixed, I grows, so H/I->0. Companion phase-funded theorem unreviewed; necessary transport/original surplus open. Saved four protocol files/proof/results and local hashes; no research work left running.\n'),('LEARNED.md','2026-10-23 stage19 durable referee fact: For ANY complementary controller a,b=1-a^2 and parity_k seed k>=3, Q=P wrapper a+sigma*b*parity has zero spectral erasure/occupancy/coherent-calibration refund at every seed query. Both full-child nonempty mixtures (1-epsilon)delta_remainingParity+epsilon*delta_distinctSingleton cost beta*log2(1/(1-epsilon)), beta=E b=actual wrapper query influence. Seed influence1 must not be confused with beta. Displayed A079 beta3/8, epsilon1/64 gives cost>3/512. Fixed-controller H independent of k and I=I_controller+k beta, so H/I->0. This excludes a current-refund supplier only; unused original surplus can still pay. Prescribed target necessity and phase-funded companion theorem are separate obligations.\n')]:
 with (HOME/path).open('a',encoding='utf-8',newline='\n') as f:f.write('\n'+text)

assert (R/'PROGRESS.json').read_bytes()==(R/'PACKET_DELTA.json').read_bytes()
assert len((HOME/'STATUS.md').read_text(encoding='utf-8').splitlines())==2
assert report.rstrip().endswith('cannot supply the missing universal money.')
assert all(('## '+field) in report for field in protocol['required_per_run']['report_fields'])
entries=[]
for p in sorted(R.rglob('*')):
 if p.is_file() and p.name!='PERSISTENCE.json':
  assert p.stat().st_size<20*1024*1024
  entries.append({'path':str(p.relative_to(R)),'bytes':p.stat().st_size,'sha256':sha(p)})
receipt={'status':'PASS','files':entries,'protocol_exact_keys':True,'statement_hypotheses_hash_preserved':True,'progress_delta_byte_identical':True,'status_two_lines':True,'all_files_under_20MB':True,'full_fei_status':'OPEN','scope':'Only zero-phase obstruction independently accepted','remote_adoption':'UNVERIFIED','jobs_left_running':[]}
js(R/'out/PERSISTENCE.json',receipt)
for item in entries:assert sha(R/item['path'])==item['sha256']
print(json.dumps({'status':'PASS','hashed_files':len(entries),'primary_assertions':v['exact_assertions'],'accepted_claim':claim['claim_id'],'statement_sha256':claim['statement_sha256'],'full_fei':'OPEN','jobs_left_running':0}))
