from pathlib import Path
import datetime,json,hashlib,copy
R=Path(__file__).resolve().parents[1];A=R.parent.parent
B=Path('~/brain_workers/FEI100_20261011')
P=Path('math-open-problems/reports/fei-2026-10-11/EXECUTION_PROTOCOL.json')
now=datetime.datetime.now(datetime.timezone.utc).isoformat()
def read(p):return p.read_text(encoding='utf-8-sig')
def sha(b):return hashlib.sha256(b).hexdigest()
def write(p,s):
    assert p.resolve().is_relative_to(A.resolve())
    p.parent.mkdir(parents=True,exist_ok=True);p.write_text(s,encoding='utf-8')
def dump(p,o):write(p,json.dumps(o,indent=2,ensure_ascii=False)+'\n')
protocol=json.loads(read(P));formal=json.loads(read(R/'out/FORMAL.json'))
sharp=[json.loads(read(R/'out'/f)) for f in ('CHECK_0_1536_SHARP.json','CHECK_1536_3072_SHARP.json','ARBITRARY_P_SHARP.json')]
wrap=[json.loads(read(R/'out'/f)) for f in ('WRAPPER_0_16.json','WRAPPER_16_33.json')]
repro=json.loads(read(R/'out/REPRODUCE.json'))
assert all(o['status']=='PASS' for o in sharp+wrap+[repro])
assert sum(o['cases'] for o in sharp)==4118
assert sum(o['roots'] for o in wrap)==924 and sum(o['queries'] for o in wrap)==2244
assert sum(o['exact_assertions'] for o in sharp)==61770
assert sum(o['exact_assertions'] for o in wrap)==13468
assert repro['cases']==256 and repro['exact_assertions']==512
source_dirs=[B/'agents/A057/runs/20261021T223314Z-fleet03-A057-coherent-restriction-remainder',B/'agents/A059/runs/20261022T224007Z-fleet03-A059-decomposition-depth']
sources=[P,B/'BOARD.md',B/'claude/B19/STREAM_NOTES.md',A/'runs/20261021T203312Z-fleet03-A091-composition-referee/PROOF.md',A/'runs/20261014T094139Z-fleet05-A091-composition-referee/PROOF.md',A/'runs/20261014T094139Z-fleet05-A091-composition-referee/code/check.py',A/'runs/20261014T094139Z-fleet05-A091-composition-referee/code/exact.py']
claims=[];source_checks=[]
expected=['8ca618ec7267510ef30f1740ba259d912a06222b3ad24590c0ee6b2916217c9b','c3cae3f63caa425b7fb7d244a072d72f73f198d9d1be431671ff5f185578ea28']
for idx,sd in enumerate(source_dirs):
    sources += [sd/'PROOF.md',sd/'CLAIMS.json']
    original=json.loads(read(sd/'CLAIMS.json'))[0]
    assert original['statement_sha256']==expected[idx]
    forms={'raw_exact_statement':sha(original['exact_statement'].encode('utf-8'))}
    for key in ('statement','exact_statement'):
        forms[key+'_and_hypotheses']=sha(json.dumps({key:original['exact_statement'],'hypotheses':original['hypotheses']},sort_keys=True,separators=(',',':')).encode('utf-8'))
    matched=[k for k,v in forms.items() if v==expected[idx]]
    source_checks.append({'claim_id':original['claim_id'],'original_statement_sha256':expected[idx],'payload_conventions_matching':matched,'computed_hashes':forms,'statement_preserved_byte_for_byte':True})
    c=copy.deepcopy(original)
    c['review_records'].append({'reviewer':'A091/fleet03','run_id':R.name,'review_source':str(R/'REVIEW.md'),'method':'Independent Fourier-sector/physical table reconstruction and analytic endpoint/account audit; no repair of source statement.','verdict':'HOLDS_EXACT_LOCAL_SCOPE' if idx==0 else 'HOLDS_LOCAL_WRAPPER; STOPPED_CHAIN_CONDITIONAL_ON_EXPLICIT_IMPORTS','exact_validation':{'cases':4118,'direct_character_cases':256,'assertions':62282} if idx==0 else {'roots':924,'queries':2244,'assertions':13468},'formal_status':formal['status'],'formal_scope':'signed-disagreement scalar only; no Lean verification obtained'})
    c['status']='INDEPENDENTLY_ACCEPTED_EXACT_LOCAL_SCOPE' if idx==0 else 'LOCAL_WRAPPER_INDEPENDENTLY_ACCEPTED_FULL_BUNDLE_CONDITIONAL_IMPORTS'
    c['proof_source']={'original':original['proof_source'],'original_source_directory':str(sd),'independent_reconstruction':str(R/('PROOF.md' if idx==0 else 'REVIEW.md'))}
    assert c['exact_statement']==original['exact_statement'] and c['hypotheses']==original['hypotheses'] and c['contributors']==original['contributors']
    assert set(c)==set(protocol['required_per_run']['claim_fields'])
    claims.append(c)
dump(R/'CLAIMS.json',claims)
dump(R/'out/SOURCE_RECEIPTS.json',{'captured_at':now,'source_hash_checks':source_checks,'note':'No source statement or authorship changed; source original statement hash is preserved, matching payload convention recorded when reproduced. Capture-time file hashes follow.','sources':[{'path':str(p),'bytes':p.stat().st_size,'sha256':sha(p.read_bytes())} for p in sources]})
next_action='Audit A060 all-c exterior price and density-lowering payment from its original proof, then carry an inherited nonflat fallback through actual exposure with SAME diminished ancestor bank, old debits and both full terminal references; A087/A094 review these scope-bound acceptances.'
progress={'protocol_revision':protocol['revision'],'run_id':R.name,'stream':'B19','packet_id':'A091','gap_id':'G-LOWSEL-COLLISION','attempt_id':'A091-stage18-composition-reviews','method':'Independent full Fourier-sector partition and direct characters for A057; separate exterior normalization/log-moment/fine-reserve reconstruction and physical wrapper replay for A059.','mathematical_delta':'A057 later-query full arbitrary-A/P local bound8+8EA independently accepted; A059 c>=1/2 fine-wrapper local theorem independently holds at original rate<21; stopped chain conditional on explicit imports. Obsolete two-test/internal-fallback gaps retired at their proved scopes.','deliverable_status':'COMPLETE_LOCAL_PENDING_SUPERVISOR_COPY','mathematical_status':'SCOPED_INDEPENDENT_REVIEWS; IMPORTED_STOPPING_CHAIN_CONDITIONAL; FULL_FEI_OPEN','claim_versions_used':['A057-LATER-PRIVATE-SHARED-Y-PAYMENT@1','A059-FREQUENT-EXTERIOR-FALLBACK-PAYMENT@1','A059-INTERRUPTED-PRIORITY-STOPPING-PAYMENT@2 previously accepted','A059-INTERLEAVED-BIASED-STOPPING-RESERVE@1 previously accepted','A091-FIRST-PRIVATE-BEFORE-Y-REPEATED-FALLBACK@1','C005 baseline'],'claims_created_or_changed':[c['claim_id']+'@'+str(c['version'])+' review record only' for c in claims],'source_artifacts':['PROOF.md','REVIEW.md','SPEC.json','SPEC_REVIEW.json','SPEC_WRAPPER.json','code/later_query.py','code/reproduce.py','code/wrapper.py','code/Disagreement.lean','code/formal.py','out/SOURCE_RECEIPTS.json','out/FORMAL.json','out/REPRODUCE.json','out/CHECK_0_1536_SHARP.json','out/CHECK_1536_3072_SHARP.json','out/ARBITRARY_P_SHARP.json','out/WRAPPER_0_16.json','out/WRAPPER_16_33.json'],'next_consumers':['A057','A059','A060','A087','A090','A094','B20'],'next_action':next_action,'stagnant_substantive_attempts':0,'blockers':['Inherited nonflat source-dependent exposure/canonical reference conversion and universal core/terminal funding remain unpaid.','Formal admission held:1.7GB physical free below4GB; no compiler started; no formal proof claimed.','Brain self-care degraded: owner model87.3h and state of mind71.9h stale, owner alerted; current task/sources used instead.','Supervisor copying, mirror verification, downstream adoption and publication unobserved.'],'packet_ids':['A091']}
assert set(progress)==set(f.split(' (')[0] for f in protocol['required_per_run']['progress_fields'])
dump(R/'PROGRESS.json',progress);dump(R/'PACKET_DELTA.json',progress)
report='''# A091 composition referee stage18

## exact target, quantifiers, hypotheses and units

Resume the later-private-query before unresolved A/Y at the SAME physically merged fine U/R and both full terminals. Finite uniform cubes, actual Boolean signs, bit entropy. After source intake, accept A057's exact local theorem for arbitrary independent A,P and fresh sign x: B=P(1+x)/2 and F=(1-Y)G+Y[A u+(1-A)(B v+(1-B)G)] have B_x<=(8+8EA)Inf_x, hence12Inf_x when EA<=1/2. G is one physical fallback, selected data blocks disjoint. Audit A059's new F=K0+Cg theorem for c=EC>=1/2, exterior/internal disjointness and arbitrary private-priority depth. Full FEI remains OPEN. These are source reviews, not two new author candidates.

## sources actually read, revisions and theorem locators

Current BOARD00:51UTC, B19 notesv2, own STATUS, previous stage17 PROOF and stage6 NEXT_IDENTITY/proof/code, execution protocol2026-10-11-execution-v2. The first large board display was truncated around B12; targeted B12 intake then revealed A057 had already paid the target. The source-independent16d draft was therefore converted to a source-bound review, not relabeled as new progress. A057 source run20261021T223314Z Sections1-4 and exact CLAIMS, A059 source run20261022T224007Z equations(1)-(5) and exact CLAIMS were read in full. Original statement hashes/authors are preserved in CLAIMS.json; capture-time bytes and hash-payload comparisons are in out/SOURCE_RECEIPTS.json. B19's old biased-block assignment is a retired baseline under the rolling status/dispatch order. Current owner campaign endpoint23Oct14:49UTC overrides stale initial dates; no schedule changed.

## complete derivation or exact first unsupported line

PROOF.md reconstructs all later-B Fourier sectors independently of A057's L1 method. General P uses indicator Parseval rather than flat point spectra. The separate charges are2d+4(EA)d+4d+4(EA)d+2d, exactly recovering8+8EA. The coarse16d draft simply discarded EA<=1; source point-A specialization12d is recovered without changing physical influence. Original fine kappa is explicitly nonnegative and U harmonic, so both literal H-U-R child debts survive. Constants, zero guard, zero influence, arbitrary widths/biases and privately selected G are retained.

REVIEW.md reconstructs A059's exterior log normalization, empty earlier-row mass e, Jensen in the exterior law only, e ln(1/e) payment, last-nonempty-block bound and envelope x^2[A0+4ln(1/x)]<=A0 x. It reproduces K_*=6+(5+2/exp(1)+ln57)/ln2<21 with an independent rational Taylor/atanh certificate. eta(c r)=c eta(r)+r eta(c) shows exact cancellation of the additional original-label terms under the same fair query. No old debit or terminal is reset. The local wrapper theorem HOLDS; its stopped corollary remains conditional on the explicit imported signed-DATA/earlier/later/last-frequency chain. The stated literal23I endpoint follows with full terminals and once-only R funding; no novelty is claimed for ordinary FEI of that family.

The actual frontier is source-dependent exposure reducing exterior density below1/2 with an inherited NONFLAT fallback and prescribed reference: pay it from the SAME diminished original bank with old debits and both full terminals. A060's board reports an all-c logarithmic theorem and one fair-source payment, but neither is treated as reviewed in this stage. Generic inherited core entropy and unrestricted terminal/reference funding remain unpaid.

## executed validation with domain, arithmetic, commands and outputs

Frozen specs precede all domains. code/later_query.py used two nonzero-influence pilots, then all64 one-bit sign-core triples, all16 two-bit A indicators and point-B widths1,2,3, plus14 biased/restricted AND2 fixtures and8 private-fallback-selector fixtures:3094 physical cases. Initial weak16d checks:40222 assertions. After discovering the sharper arbitrary-P source, SPEC_REVIEW froze a justified sharper replay plus all16 two-bit P indicators times64 core triples at XOR2 A:4118 sharp cases,736 zero-influence cases,61770 exact assertions PASS. Pilot counts26 weak/30 sharp are separate. This is a stronger-hypothesis/constant audit, not an unexplained repeat or a changed old-stage count.

Commands: `python -B -X utf8 code/later_query.py --pilot --sharp`; then `0 1536 --sharp`, `1536 3072 --supplement --sharp`, and `--arbitrary-p --sharp`, observed16.276,12.362,10.675s. Arithmetic: integer FWHT, Fraction actual edges/spectra, exact prime-log identity, audited40-term atanh logarithm bounds with geometric tail and outward rational mesh. Each grouped majorization, full physical D and actual merged fine release is checked. `python -B -X utf8 code/reproduce.py` independently constructs128-entry physical tables and direct character sums:256 cases/512 exact assertions PASS,3.363s; no imported FWHT/compose/local/formula implementation.

SPEC_WRAPPER freezes all33 two-bit (C,K0) exterior tables of density>=1/2, exhaustive16 two-test signed-core pairs, and396 additional three-test signed/biased roots with three fixed width patterns. `python -B -X utf8 code/wrapper.py 0 1 --pilot` passes2 roots/4 queries/26 assertions. Main `0 16` and `16 33` pass924 roots/2244 actual internal queries/13468 exact assertions in7.547/9.039s. They independently verify the full coherent Fourier row, physical influence, original fine-release scaling, rate21, exterior normalization, each last-nonempty row ratio and rigorous natural-log moment, including all signs/constants. Source's own claimed execution was not substituted for these checks.

Main sharperA057 + direct replay + wrapper checks total75750 exact assertions; pilots/archive counts are separately retained and not counted as new independent coverage. Each job is below55s, estimated180MB (peak not measured), fixed dimensions and no GPU. Fresh memok returned1 with1.7GB physical free versus4GB required (commit18.5GB free); code/formal.py saved MEMORY_ADMISSION_HELD and started no Lean compiler. Disagreement.lean specifies only |n-z|<=1-nz under unit-interval means; no Lean pass or full formal certification is claimed. No running work was stopped to free resources.

## proof dependencies and changed downstream conclusions

CLAIMS.json copies the exact original source statements, hypotheses, versions, hashes and authors and adds review records. A057-LATER-PRIVATE-SHARED-Y-PAYMENT@1 independently ACCEPTED at full local scope. A059-FREQUENT-EXTERIOR-FALLBACK-PAYMENT@1 local wrapper independently HOLDS; stopped bundle remains CONDITIONAL on its explicitly named imports, with no independent-review credit claimed for old complete chains. No source repair was supplied. Earlier-A12+2/ln2 is unchanged. No new broad candidate is opened at the review cap; the source-independent draft is only an alternate reconstruction. The two-test gap and frequent internal-fallback gap are retired at their exact covered scopes; c<1/2/nonflat inherited source and universal terminals remain open.

## one next mathematical action and independent reviewer

Audit A060's all-c logarithmic exterior payment and its density-lowering source proof from original artifacts, then carry an inherited nonflat fallback through the actual exposure with SAME diminished ancestor bank, all booked debits and both terminal references. A087/A094 review these local acceptances; A057/A059/A060 and B20 consume the exact claims. This is a source-dependent conversion gap, not another fixed-width census.

## actual persistence receipts or precise save blocker

Four protocol files, proof/review, three frozen specs, code, exact outputs, formal-admission hold and source receipts saved inside the designated A091 run. STATUS has two lines; WORKLOG appended once and LEARNED extended. Finalizer validates protocol field sets, unchanged source statements, exact output counts/PASS, progress-delta byte identity, final Universal bridge, hashes and20MB bounds. Local persistence is verified only; supervisor copy, mirror, adoption and publication unobserved. Brain wake required an owner alert for stale87.3h owner-model/71.9h state-of-mind; this was communicated before relying on affected notes, which were not used as task authority. Checklist T-20261023-116 records this stage; no Git or outbound messages were run.

## Universal bridge

This stage advances C019 stopping-tree payment and C024 actual-history transfer by independently accepting A057's later-B payment at8+8EA (12 for live point A) with arbitrary P, and auditing A059's new frequent-exterior fine-controller payment at original K_*<21 for unbounded priority depth, with the SAME reserve and both full terminals. These reviews replace obsolete unpaid interfaces without adding another isolated class theorem. The next genuine gap is density-lowering source/reference transfer for an inherited nonflat fallback, plus the still-unpaid arbitrary inherited core and terminal entropy. Consuming A060's all-c source and then carrying its existing debit into that nonflat exposure is the shortest next route because it targets the missing history interface in the current paid account rather than restarting its budget or repeating a bounded gate census.
'''
write(R/'REPORT.md',report)
write(A/'STATUS.md','STATE: Stage18 saved: A057 later-B full local scope independently ACCEPTED;A059 c>=1/2 wrapper HOLDS,stopped chain conditional;4118+256 later checks and2244 wrapper queries PASS;formal held;FEI OPEN.\nNEXT: Audit A060 all-c density-lowering transfer,then inherited nonflat fallback exposure from SAME diminished bank/old debits/both terminals;A087/A094 review.\n')
marker=R.name
if marker not in read(A/'WORKLOG.md'):
    with (A/'WORKLOG.md').open('a',encoding='utf-8') as f:f.write('\n'+now+' '+marker+': target already solved by A057 found in targeted board intake; converted independent16d draft to exact source8+8EA review. A057 full arbitrary-P claim ACCEPTED;4118 sharp/61770 +direct256/512 PASS. A059 new frequent-exterior wrapper independently HOLDS locally;924 roots/2244 queries/13468 assertions PASS,stopped chain conditional on explicit imports. Formal admission held at1.7GB. Next A060 all-c transfer then inherited nonflat fallback with SAME bank. Full FEI OPEN.\n')
if 'Stage18 source-review facts:' not in read(A/'LEARNED.md'):
    with (A/'LEARNED.md').open('a',encoding='utf-8') as f:f.write('\nStage18 source-review facts: A057-LATER-PRIVATE-SHARED-Y-PAYMENT@1 independently accepted at FULL local arbitrary-A/P scope, not just pointP. Retaining EA in two Fourier sectors gives8+8EA, hence12 for EA<=1/2. The initial16 was a weaker bound from discarding those factors, not changed physical influence. A059-FREQUENT-EXTERIOR-FALLBACK-PAYMENT@1 local wrapper independently HOLDS: exterior U second moment<=(1-c)/c, empty earlier row has mass e, weighted e ln(1/e) pays apparent1/e^2, K_*<21. eta(c r) extra terms cancel in ORIGINAL fine controller drift. Stopped full bundle conditional on named imports; no universal inherited/terminal payment. Exact4118+256 later cases and2244 wrapper queries PASS;formal held before compiler. Next audit A060 all-c source, then inherited NONFLAT source exposure with SAME diminished bank, old debits, both full terminals.\n')
assert (R/'PROGRESS.json').read_bytes()==(R/'PACKET_DELTA.json').read_bytes()
assert len(read(A/'STATUS.md').splitlines())==2
assert read(R/'REPORT.md').strip().split('\n\n')[-1].startswith('This stage advances C019')
files=[p for p in R.rglob('*') if p.is_file() and p.name!='RECEIPTS.json']
assert all(p.stat().st_size<20_000_000 for p in files)
receipts={'status':'PASS','saved_at':now,'claim_fields_exact':True,'progress_fields_exact':True,'source_statements_and_authors_unchanged':True,'progress_delta_identical':True,'status_lines':2,'sharp_later_cases':4118,'direct_character_cases':256,'wrapper_roots':924,'wrapper_queries':2244,'main_exact_assertions':75750,'formal_status':formal['status'],'source_hash_checks':source_checks,'files':[{'path':str(p.relative_to(R)),'bytes':p.stat().st_size,'sha256':sha(p.read_bytes())} for p in files]}
dump(R/'out/RECEIPTS.json',receipts)
print(json.dumps({'status':'PASS','run':str(R),'reviewed_claims':[c['claim_id'] for c in claims],'sharp_later_cases':4118,'direct_replay':256,'wrapper_queries':2244,'assertions':75750,'formal':formal['status'],'source_hash_payload_matches':[c['payload_conventions_matching'] for c in source_checks]}))
