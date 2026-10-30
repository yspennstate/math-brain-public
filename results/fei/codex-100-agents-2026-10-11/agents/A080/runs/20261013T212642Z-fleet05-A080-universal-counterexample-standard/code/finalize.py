from pathlib import Path
import json,hashlib,datetime
R=Path(__file__).resolve().parents[1]
A=R.parents[1]
BASE=A.parents[1]
run=R.name
now=datetime.datetime.now(datetime.timezone.utc).isoformat()
def sha(b): return hashlib.sha256(b).hexdigest()
def save(p,x): p.write_text(json.dumps(x,indent=2,ensure_ascii=False)+'\n',encoding='utf-8')
protocol_path=Path('~/mop_fei100/reports/fei-2026-10-11/EXECUTION_PROTOCOL.json')
protocol=json.loads(protocol_path.read_text(encoding='utf-8-sig'))
lead_path=BASE/'claude/B16/runs/20261011T225600Z-claude-B16-retained-kl-sandwich/CLAIMS.json'
lead=json.loads(lead_path.read_text(encoding='utf-8-sig'))['claims'][0]
sources=[protocol_path,BASE/'BOARD.md',BASE/'claude/B16/STREAM_NOTES.md',lead_path,
 BASE/'agents/A075/runs/20261013T212622Z-fleet05-A075-search-to-theorem-bridge/DERIVATION.md',
 BASE/'agents/A075/runs/20261011T231030Z-fleet05-A075-search-to-theorem-bridge/REPORT.md',
 BASE/'agents/A074/runs/20261012T043949Z-fleet05-A074-independent-reproducer/REPORT.md',
 BASE/'agents/A078/runs/20261012T023229Z-fleet05-A078-coding-and-padding/CORE_TRANSPORT_PROOF.md']
save(R/'out/SOURCES.json',{'captured_at':now,'note':'Read-only local snapshots; live draft hashes identify observed contents, not publication or acceptance. Prior-stage context retained without re-reading every paper.','sources':[{'path':str(p),'sha256':sha(p.read_bytes())} for p in sources]})
v=json.loads((R/'out/VALIDATION.json').read_text(encoding='utf-8'))
save(R/'out/SUMMARY.json',{k:x for k,x in v.items() if k!='records'})
lead['review_records'].append({'reviewer':'A080','kind':'independent analytic reconstruction and separate exact-rational physical truth-table/tree implementation','result':'ACCEPT','source':str(R/'REVIEW_LEAD.md'),'validation':str(R/'out/TREE_REVIEW.json'),'scope':'Full stopping-tree statement including arbitrary leaf entropy and influence. No substantive repair supplied. Majority-Lambda claim not reviewed.'})
lead['status']='INDEPENDENTLY_REVIEWED_LOCAL_ACCEPTANCE'
source_statement_hash=lead['statement_sha256']
lead['statement_sha256']=sha(lead['exact_statement'].encode())
lead['proof_source']={'original_source':str(lead_path),'original_proof':lead['proof_source'],'independent_reconstruction':str(R/'REVIEW_LEAD.md'),'source_supplied_statement_sha256':source_statement_hash,'hash_note':'The source-supplied hash differs from SHA-256 of the observed UTF-8 exact_statement. The local statement_sha256 fingerprints that exact unchanged text; no shared source or mathematical statement was changed.'}
statement='For every k,l>=0, let r=2k+l and f=1-2*1_A on the uniform binary r-cube, where A consists of zero, all unit vectors and k disjoint matched two-unit vectors. For every nonconstant such f, H(f)/I(f)<=20. Uniformly over all k,l with r tending to infinity, H(f)/I(f) tends to 4 and every relevant coordinate ratio B_i(f)/Inf_i(f) tends to 2. For every r>=64 every relevant coordinate ratio is strictly less than 11/5. Therefore no sequence drawn from this whole partial-matching family has unbounded H/I, although k=3,l=0 has minimum coordinate ratio greater than 368/125.'
new={'claim_id':'A080-PARTIAL-MATCHING-UNIFORM-NOGROWTH','version':1,'exact_statement':statement,'hypotheses':'Actual Boolean sign outputs, uniform physical cube, base-2 Fourier entropy. B_i is entropy of squared Fourier membership in coordinate i conditional on the other Fourier coordinates. Ratios exclude coordinates with zero influence and constant functions.','statement_sha256':sha(statement.encode()),'contributors':['A080 (uniform asymptotic proof and exact checker)','A075 (credited partial-matching spectrum and physical-restriction formulas in contemporaneous live draft; independently reconstructed here)'],'proof_source':[str(R/'MATCHING_ASYMPTOTICS.md'),str(R/'code/check.py'),str(R/'out/VALIDATION.json')],'proof_dependencies':['Elementary Walsh orthogonality and physical edge identity (derived here)','Binary entropy deficit inequality (reconstructed in REVIEW_LEAD.md)'],'review_records':[{'reviewer':'A080 (self)','kind':'analytic all-dimensional proof with independent representations within one implementation, integer Walsh/edge checks r<=10 and rational log enclosures r<=64','result':'PASS; external independent review pending'}],'status':'PROVED_AUTHOR_REVIEW_PENDING','supersedes':[],'refutes':[],'first_unproved_line':None,'next_consumers':['A075','A074','A089','A092','B16 lead','B20']}
save(R/'CLAIMS.json',{'run_id':run,'stream':'B16','claims':[lead,new]})
next_action='Require and audit an actual restriction/recentering or composition operation that changes the paired spectral profile and retains gain at every newly relevant coordinate, with all leaf entropy and influence paid; do not extend the partial-matching dimension census.'
progress={'protocol_revision':protocol['revision'],'run_id':run,'stream':'B16','packet_id':'A080','gap_id':'B16-ACTUAL-BOOLEAN-UNBOUNDED-H-OVER-I','attempt_id':'A080-stage2-sandwich-review-and-matching-asymptotics','method':'Independent analytic stopping-tree reconstruction; source-bound finite-to-infinite obstruction for partial matchings, with frozen exact rational verification.','mathematical_delta':'Accept B16-RETAINED-KL-SANDWICH@1 locally after independent reconstruction. Prove uniform partial-matching H/I->4, all relevant B_i/Inf_i->2, H/I<=20 throughout and B_i/Inf_i<11/5 for r>=64. Retire this scaling mechanism without withdrawing its finite six-bit witness.','deliverable_status':'COMPLETE_LOCAL_SAVED','mathematical_status':'NARROW_NO_GROWTH_THEOREM_PROVED_AUTHOR; LEAD_SANDWICH_INDEPENDENT_ACCEPTANCE; FULL_FEI_OPEN','claim_versions_used':['B16-RETAINED-KL-SANDWICH@1 (independently reconstructed)'],'claims_created_or_changed':['B16-RETAINED-KL-SANDWICH@1 (review record only, original statement preserved)','A080-PARTIAL-MATCHING-UNIFORM-NOGROWTH@1'],'source_artifacts':[str(R/'out/SOURCES.json'),str(R/'REVIEW_LEAD.md'),str(R/'MATCHING_ASYMPTOTICS.md'),str(R/'out/VALIDATION.json')],'next_consumers':['B16 lead','A075','A074','A089','A092','B20'],'next_action':next_action,'stagnant_substantive_attempts':0,'blockers':['Full FEI remains open: no actual Boolean family with proved unbounded H/I and no dimension-independent retained-Q/I bound. New narrow theorem awaits external review; shared registry and mirror not modified.'],'packet_ids':['A080']}
save(R/'PROGRESS.json',progress);save(R/'PACKET_DELTA.json',progress)
report='''# A080 B16: independent retained-KL review and partial-matching scaling obstruction

## exact target, quantifiers, hypotheses and units

Review B16-RETAINED-KL-SANDWICH@1 for every actual Boolean sign function on the uniform cube and every adaptive physical stopping tree, retaining arbitrary terminal entropy and influence. Then audit the scalable partial-matching extension of the finite B15 six-bit selectable-erasure obstruction. Entropies and logarithms are in bits. Dimensions are arbitrary in the proof; finite verification uses a separately frozen domain. Full FEI remains OPEN.

## sources actually read, revisions and theorem locators

EXECUTION_PROTOCOL.json revision 2026-10-11-execution-v2; BOARD.md supervisor update 2026-10-13 21:24 UTC; B16 STREAM_NOTES.md v2 (2026-10-11 23:25Z), A080 direction and retained-KL statement; lead CLAIMS.json run 20261011T225600Z, B16-RETAINED-KL-SANDWICH@1; ISOSPECTRAL_SPLICING_CURATED.md node identities and retained-KL target (8.1). Prior-stage papers and baseline standards were retained as context, without claiming a fresh paper review.

Current input also includes A074 stage2 REPORT finite f6 certificate; A075 original REPORT and live 20261013T212622Z DERIVATION.md partial-matching spectrum, influence and restrictions; A078 stage2 CORE_TRANSPORT_PROOF.md; A089 stage2 RESULTS.md. Local source fingerprints for the primary inputs are in out/SOURCES.json. A075's concurrent draft is credited explicitly: this stage adds uniform asymptotics and the all-dimensional no-growth verdict, rather than claiming the family formulas as original. No external brain queries were needed.

## complete derivation or exact first unsupported line

REVIEW_LEAD.md reconstructs all six steps of the lead's version 1 and accepts it independently. For every stopping tree, Q_T+E H(leaf)<=H(root)<=Q_T+E H(leaf)+(3/ln2) M_T and M_T<=I(root)-E I(leaf). The minority mass is min(u^2,v^2), equivalently (|a|-|b|)^2/4 in child coefficients. Replacing it by an unoriented child difference would be incorrect. The lead's phrase 'tree selection is irrelevant for Q' means equivalence of existence of a universal bound up to the additive influence budget, not numerical independence of Q from query order. No repair to the formal claim was needed. Its majority-Lambda evidence was not accepted as an asymptotic theorem.

MATCHING_ASYMPTOTICS.md gives the complete separate derivation. For k matched pairs and l isolated coordinates, r=2k+l, a=1+3k+l, N=2^r; nonempty Fourier numerators are -2(a-4u-2v) with multiplicities binom(k,u)3^u binom(l,v), while the empty coefficient is replaced by 1-2a/N. Paired and isolated influences are 2(a-4)/N and 2(a-2)/N. Regular paired-row entropy deficits cost at most 16/(N ln2), or 8/(N ln2) for isolated rows. The exceptional constant row costs at most b(2r+log2 e), where b=4(a-c)^2/N^2. These bounds prove uniformly over all partial matchings that every relevant coordinate B_i/Inf_i tends to 2, with an explicit upper bracket below 11/5 at all r>=64. All nonconstant functions in the family satisfy H/I<=20, with uniform limit 4. The original f6 still has min_i B_i/Inf_i>368/125; that finite obstruction remains valid.

First unsupported universal line: supply an actual Boolean operation or family producing unbounded H/I, or prove the retained-Q tree bound uniformly. This stage supplies neither. It closes the proposed partial-matching scaling mechanism and reviews an exact universal identity without claiming a universal FEI inequality.

## executed validation with domain, arithmetic, commands and outputs

FROZEN_SPEC.json was saved before search. Pilot: all 16 partial-matchings through r=6 and all 22 Boolean truth tables through n=2; PASS, 964 assertions, 0.036 seconds. Full: all 1,089 partial-matchings through r=64 and all 278 Boolean truth tables through n=3; PASS, 41,101 assertions, 73.931 seconds. Actual integer Walsh spectra, physical boundary influence and direct paired entropy checks run through r=10. Exhaustive adaptive complete-tree extrema are computed by dynamic programming for n<=3. Arbitrary stopping-tree scope is justified by analytic telescoping, not inferred from a finite census.

Commands, from the A080 folder:

`python -X utf8 runs/20261013T212642Z-fleet05-A080-universal-counterexample-standard/code/check.py --pilot`

`python -X utf8 runs/20261013T212642Z-fleet05-A080-universal-counterexample-standard/code/check.py`

All algebraic data use integers and Fraction. Logarithms use a positive 32-term atanh expansion after range reduction to [1,2), with tail bounded by 2 z^(65)/(65(1-z^2)); division uses certified ln2 endpoints and outward rounding to 2^-90. Output float values are display only. The code proves the finite strict rational comparisons using enclosure endpoints; the dimension-uniform conclusion follows from the analytic error bounds, not extrapolation. Frozen memory estimate 100 MB; no job exceeding 300 MB was planned, so the memok gate was not triggered. One job at a time; no automatic dimension escalation. Exact endpoints and per-dimension checkpoints are in out/VALIDATION.json and out/MATCHING_PARTIAL.json; compact counts in out/SUMMARY.json.

## proof dependencies and changed downstream conclusions

The sandwich review reconstructs the node entropy identities and physical tree telescoping directly, rather than relying on the lead's floating census. Its statement and version are preserved in CLAIMS.json with an added A080 acceptance record. The source's supplied statement hash does not match its observed UTF-8 exact_statement; proof_source preserves that supplied hash and records the discrepancy, while the local statement_sha256 fingerprints the unchanged exact text. This is a provenance correction, not a proof repair. The narrow matching theorem uses elementary Walsh orthogonality, physical edge counting and the reconstructed binary deficit inequality; it needs no unproved FEI assumption. A075's restriction closure introduces only partial matchings, point defects and constants, so there is no unpaid complex descendant hidden in the family.

A075/A074/A089 can retain the finite selection obstruction but should cease pursuing this specific enlargement as a divergent mechanism. Tensoring and dummy coordinates do not repair its bounded ratio, under the earlier A080 standard. This does not rule out distinct recentering, graph families, or composition mechanisms. New theorem: author proof complete, external independent review pending. Lead claim: independent local acceptance recorded. Shared registry adoption, downstream mathematical use and mirror verification are separate and unclaimed.

## one next mathematical action and independent reviewer

NEXT_ACTION

A075/A074/A089 are the source-bound consumers; request A092 or A088 to reconstruct the asymptotic row bounds and entropy/influence limit independently. No messages or other agents' folders were modified. This handoff is recorded locally for the supervisor.

## actual persistence receipts or precise save blocker

All four protocol files, proof notes, frozen specification, exact checker and outputs are saved in this run. STATUS.md, WORKLOG.md and LEARNED.md are current. out/PERSISTENCE_RECEIPTS.json records SHA-256 and byte counts of run artifacts and rolling files; its own hash is excluded to avoid circularity. Every file is below 20 MB. Local persistence is complete; copying to GitHub, mirror verification and registry adoption await the supervisor. There is no local save blocker.

**Universal bridge:** This stage independently accepts the B16 retained-KL stopping-tree bridge adjacent to C018/C019, preserving the exact error (3/ln2) M_T and M_T<=I-E I(leaf); it does not reduce that universal constant. It additionally retires the scalable partial-matching route quantitatively: H/I converges uniformly to 4, all coordinate erasure ratios converge to 2, and every ratio is below 11/5 from dimension 64 onward, despite the finite six-bit ratio exceeding 368/125. What remains is a dimension-independent retained-Q payment or an actual Boolean divergent family. Auditing a new gain-changing operation with complete physical and terminal costs is the shortest next route because merely raising this family's dimension has now been proved unable to cross that universal gap.
'''.replace('NEXT_ACTION',next_action)
(R/'REPORT.md').write_text(report,encoding='utf-8')
(A/'STATUS.md').write_text('STATE: Sandwich @1 independently accepted locally; partial-matchings H/I->4 and coordinate erasure ratios->2 proved; FEI OPEN, new theorem review pending.\nNEXT: Audit an actual gain-changing recentering/composition with full physical and terminal costs; A092/A088 review row bounds, A075/A074/A089 consume obstruction.\n',encoding='utf-8')
with (A/'WORKLOG.md').open('a',encoding='utf-8') as f:
 if run not in (A/'WORKLOG.md').read_text(encoding='utf-8'):
  f.write('\n'+now+' | '+run+' | Independently reconstructed lead stopping-tree sandwich, accepting formal version 1 without repair; clarified order-dependent Q values. Built on credited A075 partial-matching formulas and proved uniform H/I->4, coordinate erasure/Inf->2, global H/I<=20 and erasure/Inf<11/5 for r>=64. Pilot PASS 964 assertions; full PASS 41101 assertions, 1089 families and 278 Boolean tables in 73.931s. Saved source-bound obstruction; next mechanism must change paired profile and pay all controls/leaves. Full FEI OPEN; external review/mirror pending.\n')
with (A/'LEARNED.md').open('a',encoding='utf-8') as f:
 if run not in (A/'LEARNED.md').read_text(encoding='utf-8'):
  f.write('\n## '+run+'\n\nRetained-KL sandwich @1 holds for arbitrary stopping trees with leaf terms. Its minority mass is min(u^2,v^2)=(|a|-|b|)^2/4, and the total additive entropy cost is <=(3/ln2) M_tree <=(3/ln2)(I-E I_leaf). Complete-tree Q values may depend on order, while finiteness of a universal Q/I bound is equivalent across trees and to FEI.\n\nFor the actual sparse partial-matching family (zero, units, k disjoint paired two-unit vectors; r=2k+l), replacing the empty Fourier coefficient is essential. Uniformly H/I->4 and every relevant B_i/Inf_i->2, H/I<=20 for all nonconstant members, and every coordinate ratio<11/5 at r>=64. The B15 f6 finite min-ratio>368/125 survives but cannot be amplified by this enlargement. Exact proof: runs/'+run+'/MATCHING_ASYMPTOTICS.md. Family formulas and restriction closure credited to A075 concurrent work, independently reconstructed here; asymptotic proof added here.\n')
claims=json.loads((R/'CLAIMS.json').read_text(encoding='utf-8'))['claims']
for c in claims: assert set(c)==set(protocol['required_per_run']['claim_fields'])
required={x.split(' (')[0] for x in protocol['required_per_run']['progress_fields']}
assert set(progress)==required
assert (R/'PROGRESS.json').read_bytes()==(R/'PACKET_DELTA.json').read_bytes()
assert len((A/'STATUS.md').read_text(encoding='utf-8').splitlines())==2
files=list(R.rglob('*'))+[A/'STATUS.md',A/'WORKLOG.md',A/'LEARNED.md']
files=[p for p in files if p.is_file() and p.name!='PERSISTENCE_RECEIPTS.json']
assert all(p.stat().st_size<20_000_000 for p in files)
save(R/'out/PERSISTENCE_RECEIPTS.json',{'saved_at':now,'state':'LOCAL_SAVED','independent_review':'Lead sandwich acceptance A080; new theorem external review pending','mirror_verification':'NOT_PERFORMED','files':[{'path':str(p),'bytes':p.stat().st_size,'sha256':sha(p.read_bytes())} for p in files]})
print(json.dumps({'artifact_audit':'PASS','run':str(R),'files':len(files),'maximum_bytes':max(p.stat().st_size for p in files),'full_fei':'OPEN'},indent=2))
