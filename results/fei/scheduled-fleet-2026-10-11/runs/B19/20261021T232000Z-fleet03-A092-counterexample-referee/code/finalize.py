from pathlib import Path
import hashlib,json,datetime

R=Path(__file__).resolve().parents[1]
HOME=R.parents[1]
FLEET=HOME.parents[1]
RUN=R.name
def write(p,s):
    with p.open('w',encoding='utf-8',newline='') as f:f.write(s)
def save(p,v):write(p,json.dumps(v,indent=2,ensure_ascii=False)+'\n')
def read(p):return json.loads(p.read_text(encoding='utf-8-sig'))
def sha(p):return hashlib.sha256(p.read_bytes()).hexdigest()

reset=read(R/'out/REVIEW.json');canonical=read(R/'out/CANONICAL_REVIEW.json')
assert reset['status']==canonical['status']=='PASS'
assert reset['case_count']==6
peer85=FLEET/'agents/A085/runs/20261021T174013Z-fleet03-A085-certificate-adversary'
peer47=FLEET/'agents/A047/runs/20261021T221810Z-fleet03-A047-boundary-search'
claims85=read(peer85/'CLAIMS.json');claims47=read(peer47/'CLAIMS.json')
c85=next(c for c in claims85 if c['claim_id']=='A085-ABSOLUTE-TV-RESET-OBSTRUCTION')
c47=next(c for c in claims47 if c['claim_id']=='A047-CANONICAL-FULL-SOURCE-PRICE-OBSTRUCTION')
records=[(c85,peer85,'ACCEPT_AT_STATED_SCOPE_UNCHANGED','All clauses, including all-n positive sign, exact matching account, full support, n2 endpoint, minimality and multiplicative repair.'),
         (c47,peer47,'ACCEPT_ALL_R_SUBSTATEMENT_ONLY_UNCHANGED','Only explicit m=2^(r+2),r>=2 no-finite-K canonical complete-price obstruction, H<=4I and sharp whole-owner consequence. Finite m64 numerical excess, r2 limiting constant and A050 theorem are not independently accepted here.')]
for c,p,verdict,scope in records:
    c['review_records'].append({'reviewer':'A092/fleet03','verdict':verdict,'scope':scope,
       'source_statement_sha256':c['statement_sha256'],'source_claim_file_sha256':sha(p/'CLAIMS.json'),
       'source_proof_sha256':sha(p/'PROOF.md'),'reconstruction':str(R/'PROOF.md'),
       'source_changes':'NONE; independently written code; no substantive mathematical repair'})
    c['status']='INDEPENDENTLY_ACCEPTED_AT_STATED_SCOPE_BY_A092' if c is c85 else 'PARTIALLY_REVIEWED_ALL_R_SUBSTATEMENT_INDEPENDENTLY_ACCEPTED_BY_A092'
save(R/'CLAIMS.json',[c85,c47])

source_receipts=read(R/'out/SOURCE_RECEIPTS.json')
for p in [peer47/'PROOF.md',peer47/'REPORT.md',peer47/'UNIVERSAL_REFERENCE_OBSTRUCTION.md',peer47/'CLAIMS.json',peer85/'CLAIMS.json']:
    source_receipts.append(dict(path=str(p),sha256=sha(p),bytes=p.stat().st_size,encoding='utf-8'))
save(R/'out/SOURCE_RECEIPTS.json',source_receipts)
now=datetime.datetime.now(datetime.timezone.utc).isoformat()
progress=dict(protocol_revision='2026-10-11-execution-v2',run_id=RUN,stream='B19',packet_id='A092',
 gap_id='G-R-MISMATCH',attempt_id='A092-stage17-full-support-reset-and-full-canonical-price-review',
 method='Independent original Boolean truth-table/physical-edge reconstruction, complete-reference accounting, positive-series rational log certificates and all-dimensional analytic audit',
 mathematical_delta='A085 absolute-TV reset obstruction independently accepted unchanged: full support, matching cheap root, two nonconstant children, TV->0 but Z>3/8. A047 all-r canonical complete-price substatement independently accepted unchanged: explicit CE/I>r-1 with H<=4I, excluding every finite rate for that reference. No universal FEI bound.',
 deliverable_status='COMPLETE_LOCAL_ARTIFACT',mathematical_status='TWO_SCOPED_OBSTRUCTIONS_INDEPENDENTLY_REVIEWED;FULL_FEI_OPEN;NOT_LEAN_CHECKED',
 claim_versions_used=['A085-ABSOLUTE-TV-RESET-OBSTRUCTION@1 (all clauses independently accepted)',
                      'A047-CANONICAL-FULL-SOURCE-PRICE-OBSTRUCTION@1 (all-r substatement only independently accepted)'],
 claims_created_or_changed=['A085@1 A092 independent acceptance unchanged','A047@1 all-r substatement A092 independent acceptance unchanged; composite remainder not reviewed'],
 source_artifacts=['REPORT.md','PROOF.md','CLAIMS.json','code/review.py','code/canonical.py','out/FROZEN_SPEC.json','out/CANONICAL_SPEC.json','out/PILOT.json','out/REVIEW.json','out/CANONICAL_REVIEW.json','out/LEAN_ADMISSION.json','out/SOURCE_RECEIPTS.json','out/PERSISTENCE.json'],
 next_consumers=['A047','A048','A050','A083','A085','A087','A094','A096','A097','A099','A100','B19','B20'],
 next_action='Replace blanket complete coordinate-product pricing with a normalized correlation-preserving incoming reference; price one prescribed inherited mixed data/control reset by its actual signed weighted likelihood from SAME unused ancestor source after old bookings, retaining both complete terminals and channel bills. A096/A097 supply transaction; A087/A094 review.',
 stagnant_substantive_attempts=0,
 blockers=['Universal useful-reference/selected-reset payment remains unpaid; exact gate denied compiler admission (memok1), so no Lean result; supervisor adoption, remote copy and downstream consumption unverified.'],
 packet_ids=['A092'])
save(R/'PROGRESS.json',progress);save(R/'PACKET_DELTA.json',progress)

report=f'''# exact target, quantifiers, hypotheses and units

Independently referee A085's full-support absolute-TV reset counterfamily for every integer n>=2 and A047's all-r no-finite-K substatement for every integer r>=2, m=2^(r+2). Actual Boolean signs on uniform finite cubes; Shannon/cross entropy bits; physical influence. Both complete terminal debts, unchanged old debits and reference-only support persist. A085 is accepted unchanged in full; A047 acceptance is restricted to the all-r substatement, not its composite claim's separate finite numerical/asymptotic assertions. Full FEI remains OPEN. Current owner deadline23 October2026 14:49UTC supersedes the protocol's older date.

# sources actually read, revisions and theorem locators

Protocol2026-10-11-execution-v2 read in full; campaign README/status/claim/obstruction/packet/next-action and plan; supplement CAMPAIGN/CLAIMS/COUNTEREXAMPLES/SEED_LEMMAS/NATIVE_MAPPING and source texts; current BOARD and B19 leadv2; own rolling files and last source-complete stage5 proof. Later own stages6-16 contain only .final markers and supply no recovered mathematics. Four context paper text exports were loaded: strict UTF-8 failed on their original bytes, then explicit cp1252 decoding succeeded; neither paper is used as a theorem premise. SOURCE_RECEIPTS pins bytes and encodings. Critical sources: A08520261021T174013Z PROOF Sections1-5/CLAIMS and A04720261021T221810Z PROOF Sections1-2/UNIVERSAL_REFERENCE_OBSTRUCTION/CLAIMS. No peer helper was imported or executed. One two-wording read-only math recall returned only unrelated/general contextual cards; none is a proof dependency. Wake warned of stale owner-model/state notes and the user was alerted before relying on them.

# complete derivation or exact first unsupported line

PROOF.md reconstructs both from their actual circuit definitions. A085 f is negative exactly at0,1,3 in n+1 dimensions. Root Q=P has full support and H<=8I, both children are nonconstant, I=(3n-1)2^-n and Inf_j=2^-n. A positive normalized one-child reset has TV<2^(1-2n) but expected complete bill Z>3/8, with Z->1/2 and exactly zero conditional refund. The n2 endpoint and minimal three-dimensional root are independently checked. The exact reset criterion is not refuted.

A047's actual disjoint-point tensor root has prescribed matched-empty/marginal canonical Q. Its unique positive normalizer satisfies c>1/2 at m=2^(r+2). Selected-data CE alone exceeds2r^2; the only potentially negative grouped normalizer term is greater than-1. Since I<2r+5/4, CE/I>r-1, while H<=4I. Thus no finite absolute rate pays this COMPLETE coordinate-product reference, including the sharp signed whole-owner rule. Every data-restriction terminal remains FEI-certified. This is a reference-price obstruction, not a Boolean H/I counterfamily. No new universal constant or FEI solution is claimed.

FIRST UNSUPPORTED UNIVERSAL LINE: supply a useful complete correlation-preserving incoming reference or genuinely selected inherited reset whose actual signed weighted likelihood, channel bills, old bookings and both full terminal debts fit ONE dimension-independent unused source account. The blanket complete canonical price in the previous A092 NEXT is now ruled out, not merely expensive at rate4.

# executed validation with domain, arithmetic, commands and outputs

Frozen specifications precede every executed search. Commands from the A092 working directory: python -B -X utf8 runs/{RUN}/code/review.py --pilot, then without--pilot, and python -B -X utf8 runs/{RUN}/code/canonical.py. Reset pilot:2 fixtures/{read(R/'out/PILOT.json')['assertions']} assertions PASS. Final reset:6 fixtures n2..7/{reset['assertions']} exact assertions PASS, {reset['runtime_seconds']:.6f}s mathematical runtime. Low-dimensional exhaustive loops are4+16=20 truth tables, every coordinate;8 eligible splits all lack full support. Frozen count text initially said18; corrected to20 without changing any loop or domain. Pilot is not added to the final count.

Canonical checker:3 complete small tables (m,r)=(2,2),(2,3),(3,2);4 exact large tensor-normalizer summaries r2..5,m2^(r+2);127 scalar side checks r2..128; {canonical['assertions']} exact assertions PASS in {canonical['runtime_seconds']:.6f}s. Its first run failed during result serialization because pathlib.Path was not imported. That failed run supplies no certificate; the import-only repair, unchanged domain and successful rerun are recorded in CANONICAL_SPEC. No source theorem was repaired.

Arithmetic: direct integer character sums and physical edge counts; Fraction normalization/support/TV and tensor identities; outward log bounds with44 positive atanh terms, a proved remainder,112-bit downward term rounding and100-bit mantissa enclosure. Signed terms use interval multiplication with correct endpoint reversal; positive ln2 division precedes signed exponent addition. Algebra, not interval overlap, proves identities. Small/boundary cases, every canceled denominator, support inclusion, n2, c=0 exclusion, physical reaches and the exceptional negative normalizer term are addressed in PROOF. No dimension escalation or huge truth-table construction occurred. Each helper estimates80MB, with fixed55s pilot cap; observed mathematical runtimes are the separate recorded values above, excluding shell startup. Peak memory was not measured.

The fresh memok command exited1: physical free7.6GB, commit free6.0GB against8GB required. No Lean compiler was launched. Rung: independent analytic proof with exact certificates, NOT Lean-checked. The compute snapshot was ok at its read (commit91%,free disk22GB); the intervention tail is historical, not a fresh incident. No work was stopped or throttled.

# proof dependencies and changed downstream conclusions

Both accepted statements have self-contained reconstructions: Boolean character sums, physical edge counts, finite conditional cross-entropy algebra, elementary logarithm inequalities and disjoint tensor products. No unreviewed universal lemma is assumed. CLAIMS preserves source statements/hashes, adds explicit review scope and distinguishes A047's unreviewed composite remainder. B20/A096/A097/A099 should reject absolute-TV admission; A047/A048/A050/A083 should reject universal complete coordinate-product source pricing at every finite rate. A050's G<2 theorem, A099's exact reset criterion, useful selected transactions and correlation-preserving references are not refuted. Universal FEI remains open.

# one next mathematical action and independent reviewer

Consume A096/A097's next prescribed inherited mixed data/control transaction using a normalized reference that preserves supplied core correlations. Bound its signed weighted likelihood against the SAME original remaining source after all old debits and both full terminals, rather than admitting the full canonical product price. A087/A094 review the source/quotient and terminal ownership; A085/A047 may compare this independent reconstruction with their originals. No external message or adoption is claimed.

# actual persistence receipts or precise save blocker

The four protocol files, PROOF, frozen specs, new scripts and exact outputs are saved in this run. out/PERSISTENCE.json checks exact required key sets, matching progress/delta, source hash preservation, local paths and every file<20MB; rolling STATUS has exactly two lines and WORKLOG/LEARNED append. All deliberate research writes are inside A092. No git, mail, external publication, shared-index edit, other-agent write, brain write, deletion, trading-path access, GPU, detached job or compiler launch occurred. Local artifact completion is distinct from supervisor copying, remote mirror verification and downstream use; all three remain unverified.

Universal bridge: This stage moves C019 stopping-tree payment and C024 history transfer by independently certifying two failed universal substitutions: absolute-TV reset accuracy cannot replace weighted likelihood (Z>3/8 with TV->0), and a full coordinate-product canonical source cannot be influence-priced at ANY finite rate (CE/I>r-1 despite H<=4I). Improvement to the universal FEI constant is zero. A useful selected signed transaction with preserved correlations, all old bookings, channel bills and both terminal debts remains unpaid. NEXT changes these demonstrated failing mechanisms instead of enlarging a finite census, and targets the exact surviving source-payment bridge required for full FEI.
'''
write(R/'REPORT.md',report)
write(HOME/'STATUS.md','STATE: A092 stage17 complete: A085 full-support absolute-TV reset obstruction accepted; A047 all-r canonical full-price obstruction accepted at substatement scope; exact checks PASS; FEI OPEN.\nNEXT: Pay one prescribed inherited mixed query/reset using correlation-preserving Q and SAME unused original bank, with old bookings, channel bills and both complete terminals; A096/A097 supply, A087/A094 review.\n')
for name,text in [('WORKLOG.md',f'\n{now} | {RUN}: Independently accepted A085@1 unchanged from original circuit;6 fixtures/{reset["assertions"]} assertions PASS. Independently accepted only A047@1 all-r no-finite-K canonical source substatement;{canonical["assertions"]} checks PASS. Fixed checker serialization import, same domain; failed run not counted. Initial paper UTF-8 decode failure handled explicitly as cp1252 source exports. Lean not launched: memok1 commit6.0GB<8GB. Full FEI OPEN; all local artifacts saved, no remote copy/adoption claimed.\n'),
                  ('LEARNED.md','\nStage17: A085-ABSOLUTE-TV-RESET-OBSTRUCTION@1 independently accepted unchanged. f_n=-1 at vertices0,1,3 has full support, both children nonconstant, I=(3n-1)2^-n,H<=8I. Matching Q yields zero conditional refund; one child reset TV<2^(1-2n) adds Z>3/8, tending1/2, while Inf_j=2^-n. Three dimensions minimal under these additional support/child hypotheses. Relative atom domination gives the safe -log2(1-eta) bound; TV alone cannot replace likelihood. A047-CANONICAL-FULL-SOURCE-PRICE-OBSTRUCTION@1 all-r substatement independently accepted: m=2^(r+2),r>=2, actual disjoint-point tensor root has CE(P,Qcanonical)/I>r-1 but H<=4I; unique c>1/2, data CE>2r^2, sole negative term>-1, I<2r+5/4. Thus EVERY fixed complete product-occupancy rate fails; taking the positive part later does not repair the sharp whole-owner account. Other A047 finite/asymptotic clauses remain outside this review. Preserve correlations or price a selected inherited signed transaction with SAME unused source, old bookings and both terminals.\n')]:
    with (HOME/name).open('a',encoding='utf-8',newline='') as f:f.write(text)

protocol=read(Path(r'~\mop_fei100\reports\fei-2026-10-11\EXECUTION_PROTOCOL.json'))
pf=[x.split(' (')[0] for x in protocol['required_per_run']['progress_fields']]
cf=protocol['required_per_run']['claim_fields']
assert set(progress)==set(pf),(set(progress)^set(pf))
assert all(set(c)==set(cf) for c in (c85,c47))
assert read(R/'PROGRESS.json')==read(R/'PACKET_DELTA.json')
assert c85['statement_sha256']==claims85[0]['statement_sha256']
assert len((HOME/'STATUS.md').read_text(encoding='utf-8').splitlines())==2
files=[p for p in R.rglob('*') if p.is_file() and p.name!='PERSISTENCE.json']
assert all(p.stat().st_size<20*1024*1024 for p in files)
save(R/'out/PERSISTENCE.json',dict(status='PASS',at_utc=now,exact_claim_fields=True,exact_progress_fields=True,
       report_fields_present=all(x in report for x in protocol['required_per_run']['report_fields']),
       matching_progress_delta=True,all_files_under20MB=True,
       files=[dict(path=str(p.relative_to(R)),bytes=p.stat().st_size,sha256=sha(p)) for p in files],
       remote_copy='UNVERIFIED',canonical_adoption='UNVERIFIED',downstream_use='UNVERIFIED'))
print(json.dumps(dict(status='PASS',files=len(files),reset_assertions=reset['assertions'],canonical_assertions=canonical['assertions'],run=str(R))))
