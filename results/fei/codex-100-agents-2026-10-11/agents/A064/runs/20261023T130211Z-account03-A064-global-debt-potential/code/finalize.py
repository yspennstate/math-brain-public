from pathlib import Path
import json,hashlib,copy,datetime

ROOT=Path(__file__).resolve().parents[1]
AGENT=ROOT.parents[1]
BASE=AGENT.parent
PROTO=Path(r'math-open-problems/reports\fei-2026-10-11\EXECUTION_PROTOCOL.json')
SOURCE=BASE/'A061/runs/20261023T113614Z-account03-A061-entropy-process'
def read(p):return json.loads(p.read_text(encoding='utf-8'))
def sha(p):return hashlib.sha256(p.read_bytes()).hexdigest()
def write(p,v):p.write_text(json.dumps(v,indent=2,ensure_ascii=False)+'\n',encoding='utf-8',newline='\n')
def text(p,v):p.write_text(v,encoding='utf-8',newline='\n')

def main():
 protocol=read(PROTO)
 main=read(ROOT/'out/MAIN.json');pilot=read(ROOT/'out/PILOT.json');audit=read(ROOT/'out/A061_AUDIT.json');rare=read(ROOT/'out/RARE_BRANCH.json');capital=read(ROOT/'out/INITIAL_CAPITAL.json')
 for v in (main,pilot,audit,rare,capital):assert v['status']=='PASS'
 assert main['counts']['states']==6656 and main['ordered_pairs']==256
 total=sum(v['exact_assertions'] for v in (main,audit,rare,capital))
 oldstatus=(AGENT/'STATUS.md').read_text(encoding='utf-8');text(ROOT/'out/INPUT_STATUS.md',oldstatus)
 original=read(SOURCE/'CLAIMS.json')[0]
 assert original['claim_id']=='A061-FIXED-PRODUCT-ONE-PREFIX-HALFBIT-OBSTRUCTION' and original['version']==1
 assert sha(SOURCE/'PROOF.md')==original['proof_source']['sha256']
 review=copy.deepcopy(original)
 review['review_records'].append({'reviewer':'A064/account03','verdict':'INDEPENDENT_RECONSTRUCTION_HOLDS_UNCHANGED','proof':str(ROOT/'AUDIT.md'),'certificate':str(ROOT/'out/A061_AUDIT.json'),'independence':'No A061 executable imported; own prior FWHT, independent physical edges and full normalized reference transport. All-l character/owner proof reconstructed in AUDIT.md. Producer status and statement hash preserved; global registry not mutated.'})
 statement=(
 'For F(u,v,y)=g(y) at v=0 and (-1)^u h(y) at v=1, every finite ordinary y-prefix preserves the FULL reference form Q(su=b,sv=c,T)=w_b R_b(T)/2 whenever it holds initially, with actual normalized Bayes sector updates and fair source-zero extensions. At any such node let L_b=KL(p_b||R_b)-TC(p_b), a_b=R_b(supp p_b), r_0=1/2+(w_0 a_0-w_1 a_1)/2, r_1=1-r_0, c_b=log2(w_b/r_b). Querying protected v has erasure credit0, actual child KL=KL(p_b||R_b)+log2(r_b/w_b), and EXACT least optional inherited/product reset reserve B=mean_b[c_b-L_b]_+ <=1/2+mean_b[-L_b]_+. Both the half-bit supremum and the coefficient of average negative eligibility are sharp. Product sector references imply L_b>=0, but genuine product-root eligibility is not hereditary. For every declared finite ordinary-prefix action tree, the explicit signed backward envelope G=max(0, admitted B, admitted mean G_child-E_actual) yields potential current K+G before pivot, K_b+[c_b-L_b]_+ between pivot/reset, current K afterward, and controls expected current terminal KL plus all outcome KL at every stopping cut by K_root+G_root; full terminal entropy is added on BOTH sides. One supplied original owner must fund K_root+G_root with all old consumption retained and nested pending reserve topped up only once. A verified rare-activation family has epsilon=2^-k, initial K=5/2, B=3-(log2 7)/2, initial extra reserve epsilon B, growing conditional potential on probability-epsilon paths, expected terminal K=5/2+epsilon, outcome cost epsilon(B-1), and full terminal H=17/2-4epsilon. Conversely any policy class admitting immediate pivot and every product stopping cut needs total INITIAL capital K+G>=TC(f) on g=h=f for EVERY starting reference. Tensor-point cores give TC(f_m)>=m^2-5m-2 and I(F_m)=m+1, so this full product-stop class has no universal influence-priced initial account. No FEI theorem or counterexample is claimed.'
 )
 claim={
 'claim_id':'A064-PREFIX-SECTOR-ELIGIBILITY-DEBT','version':1,'exact_statement':statement,
 'hypotheses':['Finite uniform physical cubes; arbitrary Boolean g,h on same core coordinates; all logarithms in bits. Initial w_b>0 sum1, R_b normalized supporting p_b, full Q=w_b R_b/2 in each mask sector.',
 'Before protected v, only ordinary core coordinates are queried. No u query before v is admitted. Prefixes, action choices and stopping cuts are finite and predictable.',
 'Actual coherent reference kernel, fair on EVERY zero-source erased row; reference-only mass is retained. No global product/tensor factorization after an interacting query is assumed.',
 'At pivot children may independently retain their inherited reference or reset once to their actual marginal products; after that choice only inherited-reference physical continuation is admitted. Intermediate cuts before reset are included.',
 'Original owner S, initial booked K and old consumed omega are supplied hypotheses. Initial funding requires S-omega-K>=G; a nested pending theta from the SAME reference is replaced by G with only G-theta top-up. No owner renewal.',
 'Rare-branch construction uses genuine physical dummy bits with deterministic empty spectral indicators. All-k conclusion is analytic; actual truth-table validation uses only k=1,2.',
 'Initial-capital impossibility applies to a class admitting ALL actual product stops, not to every selected query rule, arbitrary narrowed eligible stops, FEI, or full-entropy coding policies.'],
 'statement_sha256':hashlib.sha256(statement.encode('utf-8')).hexdigest(),'contributors':['A064/account03'],
 'proof_source':{'path':str(ROOT/'PROOF.md'),'sha256':sha(ROOT/'PROOF.md'),'validation':[str(ROOT/'out'/n) for n in ['MAIN.json','A061_AUDIT.json','RARE_BRANCH.json','INITIAL_CAPITAL.json']]},
 'proof_dependencies':[{'claim':'A061-FIXED-PRODUCT-ONE-PREFIX-HALFBIT-OBSTRUCTION@1','acceptance':'A064 independent unchanged reconstruction HOLDS, recorded in this run','scope':'Explicit l2 rare-branch fixture and consumed hereditary-half-bit obstruction; sector formula and initial-capital corollary are reconstructed self-contained.'}],
 'review_records':[{'reviewer':'A064','verdict':'AUTHOR_PROOF_AND_EXACT_CHECKS_COMPLETE; NOT_EXTERNAL_ACCEPTANCE','certificate_assertions_excluding_pilot':total,'pilot_assertions_separate':pilot['exact_assertions']}],
 'status':'AUTHOR_PROVED_EXACTLY_CHECKED_PENDING_INDEPENDENT_REVIEW','supersedes':[],
 'refutes':['UNREGISTERED-CANDIDATE: freedom to choose the original reference can universally influence-price total initial capital for all actual product stopping cuts'],
 'first_unproved_line':None,'next_consumers':['A061','A062','A065','A087','A094','B20']}
 write(ROOT/'CLAIMS.json',[claim,review])
 report_fields=protocol['required_per_run']['report_fields']
 text(ROOT/'REPORT.md',f'''# A064: prefix-sector eligibility and global debt

## {report_fields[0]}

The closed local target is an exact reference eligibility formula after arbitrary finite ordinary prefixes, with a signed global potential and every stopping boundary specified. The theorem is PROOF.md sections1-3. Its new input is the persistent conditional-sector reference form and exact branchwise product-reset bill; the KL backward envelope itself is standard. Section4 gives actual arbitrarily rare branches on which the potential increases. Section5 proves that universal influence-priced initial funding for the full product-stop class is impossible. Full FEI remains OPEN.

## {report_fields[1]}

Read the current BOARD.md (12:58 UTC revision), B13 STREAM_NOTES.md (v2), own STATUS.md and relevant rolling lessons, machine-wide AGENTS.md, and execution protocol. Consumed A061-FIXED-PRODUCT-ONE-PREFIX-HALFBIT-OBSTRUCTION@1, its full PROOF.md sections0-7 and unchanged CLAIMS payload. Own prior exact helper is pinned by SHA256 in FROZEN_SPEC.json. Campaign baseline, registries and papers remain the inherited completed intake; no new paper result is a premise. Current A062/A065/A087 statuses were read for routing, without using an unread new proof as a theorem. Source artifacts are pinned in out/SOURCE_PINS.json.

## {report_fields[2]}

At every ordinary-prefix node the FULL normalized reference has Q(b,c,T)=w_b R_b(T)/2. Let L_b=D(p_b||R_b)-TC_b. The exact pivot/reset reserve is mean[log(w_b/r_b)-L_b]_+, where r_0=1/2+(w_0 a_0-w_1 a_1)/2. It is at most1/2+mean[-L_b]_+. Actual Bayes predictions, erased credit E_v=0 and child KL are derived including all source-zero rows. The finite signed envelope G and potential current K+G control every declared cut; terminal H is explicitly retained on both sides. The half-bit and negative-eligibility coefficients are sharp.

A061's hoped-for ordinary-prefix extension is refuted and independently HOLDS unchanged as an obstruction. AUDIT.md reconstructs the all-l field spectrum, reference normalization and SAME-owner repair. The exact l2 source requires B=3-(log2 7)/2>3/2, not half a bit. The rare activation of this SAME fixture has initial reserve epsilon B, epsilon=2^-k, terminal expected KL5/2+epsilon, cost epsilon(B-1), and full H17/2-4epsilon. Equality holds in the expected terminal bound.

The initial-capital obstruction is stronger than a bad product reference: if every product cut is admitted, K+G>=TC(core) for ANY initial reference. Explicit tensor-point cores have TC/I unbounded even after the fresh mask. Thus the first unsupported universal line must instead select eligible reference changes and pay full terminal entropy from one influence-priced original account. Another reference choice alone cannot repair the full-stop class.

## {report_fields[3]}

Frozen specifications precede each search. Main validation: ALL256 ordered two-bit core pairs, two reference fixtures per pair (genuine original marginal product; unequal weights with distinct positive nonproduct sector references), ALL13 ordered ordinary-history states per fixture. Total6656 states, {main['counts']['ordinary_transports']} ordinary full/sector transports, {main['counts']['pivot_transports']} pivot transports, {main['counts']['postreset_transports']} post-reset core transports and {main['counts']['reference_only_pivots']} pivots with reference-only erased mass. Main PASS: {main['exact_assertions']} exact assertions in {main['seconds']:.3f}s. This small-core census has no negative L sectors; the genuine 11-bit A061 audit supplies the required negative-eligibility case.

A061 audit PASS: {audit['exact_assertions']} exact assertions in {audit['seconds']:.3f}s, actual2048-entry truth table and full normalized descendants; four proper influence1/2 queries after reset. Rare dummy check PASS: {rare['exact_assertions']} assertions in {rare['seconds']:.3f}s, actual k1,2 and maximum dimension13. Point-capital check PASS: {capital['exact_assertions']} assertions in {capital['seconds']:.3f}s, actual point dimensions2,4,6,8; source tensor additivity is proved, not an expanded tensor search. Total primary exact assertions={total}. Pilot {pilot['exact_assertions']} assertions/{pilot['seconds']:.3f}s is separate and excluded.

Commands: python -B -X utf8 code/check.py pilot; code/check.py main; code/audit.py; code/rare.py; code/capital.py (run from this run directory, or use their full run-relative paths). Integer FWHT, independent physical edges, rational probabilities, exact prime-log identities and proved96-bit outward intervals. No floating search evidence is called a proof. Each job is bounded, sequential and estimated below120MB; no job over300MB or memok trigger. A pre-execution scalar substitution in audit.py was corrected to l=2 explicitly and re-frozen in AUDIT_SPEC_AMENDMENT.json; no result-dependent domain change. No failed mathematical certificate was hidden.

## {report_fields[4]}

Source A061@1 is accepted unchanged by this independent reconstruction; its producer status/hash are preserved with the A064 review appended. New A064-PREFIX-SECTOR-ELIGIBILITY-DEBT@1 is author-proved and exactly checked, with A087/A094 external review pending. No A061 implementation was executed. The prior A064 no-prefix half-bit theorem remains valid; its hereditary extension is false. The debt formula now states exactly which signed sector loss must be measured, and the total-capital obstruction rules out universally cheap closure over all product cuts. No campaign registry, peer source or source version was edited.

## {report_fields[5]}

Next mathematical action: use the exact signed sector bill to specify a narrowed eligibility rule for reference changes, then bound its FULL entropy/reference payment from the SAME original influence-priced account on an arbitrary indecomposable core. The all-product-stop class is now excluded by proof; widening its finite census cannot fix it. Independent reviewers A087/A094 should first reconstruct the prefix-sector normalization, least-reserve recursion, rare activation boundary and total-capital obstruction.

## {report_fields[6]}

Four protocol files and code/out artifacts are written locally. PROGRESS.json and PACKET_DELTA.json are identical with packet_ids=[A064]. Exact schemas, statement hashes, proof hashes, output PASS records and file sizes are checked by code/verify.py; out/MANIFEST.json supplies byte hashes and is read back. Rolling STATUS.md, WORKLOG.md and LEARNED.md are updated. Supervisor publication/mirror state is unobserved; no git or external messages were used. All new writes are inside A064. Brain self-care remains degraded/unverified: personal model/state/dream freshness warnings affect personal context; these notes are excluded from mathematical premises. No research job remains running after verification.

Universal bridge: This stage advances C019 stopping-tree payment and C024 history transfer by replacing an invalid hereditary half-bit assumption with an exact all-prefix conditional-sector eligibility formula and its signed minimal reserve, including a genuinely rare growing branch and every full terminal. It also proves that influence-priced total initial capital for closure over ALL product cuts is impossible regardless of the reference. The remaining universal bridge is a selected eligible entropy/reference policy funded from the SAME original account, with old consumption and both terminal H and KL retained. Defining and pricing that selection is the shortest route because the broader capital target is now refuted, while another isolated class or deeper finite tree cannot remove this obstruction.
''')
 progress={
 'protocol_revision':protocol['protocol_revision'] if 'protocol_revision' in protocol else protocol.get('revision','2026-10-11-execution-v2'),
 'run_id':ROOT.name,'stream':'B13','packet_id':'A064','gap_id':'G-R-MISMATCH','attempt_id':ROOT.name+'-sector-eligibility',
 'method':'Independent unchanged A061 obstruction review; exact conditional-sector Bayes reconstruction; sharp signed eligibility debit; finite backward potential; rare-branch construction; any-reference initial-capital obstruction.',
 'mathematical_delta':f'Exact all-prefix sector eligibility theorem; all cuts and initial conditions; rare-branch equality; any-reference full-product-stop capital obstruction. {total} primary exact assertions, pilot excluded.',
 'deliverable_status':'COMPLETE_LOCAL_ARTIFACTS; independent new-claim review pending; supervisor mirrors unobserved',
 'mathematical_status':'SCOPED_THEOREM_PROVED_AND_EXACTLY_CHECKED; SOURCE_A061_HOLDS_UNCHANGED; FULL_FEI_OPEN',
 'claim_versions_used':['A061-FIXED-PRODUCT-ONE-PREFIX-HALFBIT-OBSTRUCTION@1'],
 'claims_created_or_changed':['A064-PREFIX-SECTOR-ELIGIBILITY-DEBT@1','A061-FIXED-PRODUCT-ONE-PREFIX-HALFBIT-OBSTRUCTION@1: independent unchanged review appended locally'],
 'source_artifacts':[str(SOURCE/'PROOF.md'),str(SOURCE/'CLAIMS.json'),str(ROOT/'PROOF.md'),str(ROOT/'AUDIT.md'),str(ROOT/'out/MAIN.json')],
 'next_consumers':['A061','A062','A065','A087','A094','B20'],
 'next_action':'Select eligible reference-change cuts using exact signed sector bill, then price full terminal entropy/reference payment from SAME original influence account; A087/A094 review new theorem. Universal full-product-stop initial capital is refuted.',
 'stagnant_substantive_attempts':0,'blockers':['New theorem awaits A087/A094 review.','No universal influence-priced original entropy/reference account with selected eligible stops has been proved.','Supervisor mirror verification unobserved.','Personal-context brain self-care degraded; excluded from proof premises.'],'packet_ids':['A064']}
 write(ROOT/'PROGRESS.json',progress);(ROOT/'PACKET_DELTA.json').write_bytes((ROOT/'PROGRESS.json').read_bytes())
 status=f'STATE: Exact all-prefix sector reset bill and rare-branch potential proved; {total} primary exact checks PASS; A061 obstruction independently HOLDS; full-product-stop initial capital/I unbounded for ANY reference; FEI OPEN.\nNEXT: Select eligible reference-change cuts using signed sector bill and pay FULL entropy/reference from SAME original influence account; A087/A094 review; do not seek cheap capital for all product stops.\n'
 text(AGENT/'STATUS.md',status)
 stamp=datetime.datetime.now(datetime.timezone.utc).isoformat(timespec='seconds')
 with (AGENT/'WORKLOG.md').open('a',encoding='utf-8',newline='\n') as f:
  f.write(f'\n{stamp} — {ROOT.name}: consumed A061 one-prefix obstruction and independently reconstructed it unchanged. Proved persistent conditional-sector reference form, exact signed reset eligibility bill, all-cut finite debt potential, rare activation equality and any-reference full-product-stop initial-capital obstruction. Main {main["exact_assertions"]} + source audit {audit["exact_assertions"]} + rare {rare["exact_assertions"]} + capital {capital["exact_assertions"]} = {total} primary assertions PASS; pilot excluded. New external review pending; FEI open. Pre-execution audit scalar check corrected and frozen; cmd-shell bootstrap quoting failed before any computation and was replaced by normal PowerShell invocation. Brain personal context stale, not used as proof. Only A064 mutated; no research jobs left.\n')
 with (AGENT/'LEARNED.md').open('a',encoding='utf-8',newline='\n') as f:
  f.write('\nFor fresh two-sector F(g,h), actual ordinary prefixes preserve Q(b,c,T)=w_b R_b(T)/2 INCLUDING all zero-source mass; w and R update by actual sector Bayes laws. At pivot r0=1/2+(w0a0-w1a1)/2, E=0, inherited K_b=D_b+log(r_b/w_b), signed reset J_b=log(w_b/r_b)-(D_b-TC_b). Exact optional-reset reserve is mean[J_b]+ <=1/2+mean[TC_b-D_b]+. Product sector references are eligible; product-root eligibility is not hereditary (A061 obstruction independently HOLDS). Finite signed backward G=max(0,B,mean G_child-E) gives minimal all-cut K+G, with full H added to both terminal sides. Physical dummy activation makes branches arbitrarily rare while potential grows, initial reserve scales by2^-k and expected terminal K+cost equality remains exact. Crucial: for g=h, admitting all product cuts forces K+G>=TC(g) for EVERY starting reference. Tensor-point TC/I is unbounded, so no reference choice can universally influence-price this full-stop class. The remaining route must SELECT eligible entropy/reference changes and pay full terminal entropy, not price every product stop or omit H.\n')
 pins=[]
 for p in [PROTO,SOURCE/'PROOF.md',SOURCE/'CLAIMS.json',ROOT/'code/exact.py',ROOT/'out/INPUT_STATUS.md']:
  pins.append({'path':str(p),'sha256':sha(p)})
 write(ROOT/'out/SOURCE_PINS.json',{'pins':pins,'source_statement_hash_producer_preserved':original['statement_sha256'],'source_exact_statement_raw_utf8_hash':hashlib.sha256(original['exact_statement'].encode('utf-8')).hexdigest(),'new_statement_hash_scheme':'raw UTF8 exact_statement','source_status':'unchanged producer payload plus appended local independent review; no source tree mutation'})
 schema={'required_claim_fields':protocol['required_per_run']['claim_fields'],'required_progress_fields':['packet_ids' if s.startswith('packet_ids ') else s for s in protocol['required_per_run']['progress_fields']],'report_fields':report_fields}
 write(ROOT/'out/SCHEMA.json',schema)
 print(json.dumps({'status':'WRITTEN','primary_exact_assertions':total,'pilot_separate':pilot['exact_assertions'],'new_claim':claim['claim_id']+'@1','source_review':'HOLDS unchanged','new_external_review':'pending'}))
if __name__=='__main__':main()
