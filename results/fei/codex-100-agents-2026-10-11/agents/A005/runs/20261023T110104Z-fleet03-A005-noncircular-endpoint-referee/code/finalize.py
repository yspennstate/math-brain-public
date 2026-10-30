from pathlib import Path
import json,hashlib,datetime
R=Path(__file__).resolve().parents[1];OWN=R.parents[1];AGENTS=OWN.parent;TEAM=AGENTS.parent
def read(p):return json.loads(p.read_text(encoding='utf-8'))
def save(p,t):p.write_text(t,encoding='utf-8',newline='\n')
def js(p,o):save(p,json.dumps(o,indent=2,ensure_ascii=False)+'\n')
def sha(p):return hashlib.sha256(p.read_bytes()).hexdigest()
check=read(R/'out/CHECK.json');other=read(R/'out/INDEPENDENT.json');pilot=read(R/'out/PILOT.json')
assert check['status']==other['status']==pilot['status']=='PASS'
assert check['assertions']==152876 and other['assertions']==934
total=check['assertions']+other['assertions']
protocol_path=Path(r'math-open-problems/reports\fei-2026-10-11\EXECUTION_PROTOCOL.json')
protocol=read(protocol_path)
runs={
 'A002':'20261023T053821Z-fleet03-A002-hardness-preserving-transformations',
 'A051':'20261023T050752Z-fleet03-A051-near-extremizer-definition',
 'A052':'20261023T055856Z-fleet03-A052-critical-source-structure',
 'A055':'20261023T042040Z-fleet03-A055-extremal-obstruction-referee'}
proofs={'A002':'REVIEW_A051.md','A051':'COMPACTNESS.md','A052':'PRECONDITIONING_PROOF.md'}
sources=[protocol_path,TEAM/'BOARD.md',TEAM/'claude/B01/STREAM_NOTES.md']
for a,run in runs.items():
    p=AGENTS/a/'runs'/run
    sources.append(p/'REPORT.md')
    if a in proofs:sources.extend([p/proofs[a],p/'CLAIMS.json'])
prev=OWN/'runs/20261023T035753Z-fleet03-A005-noncircular-endpoint-referee'
sources.extend([prev/'REPORT.md',prev/'CLAIMS.json'])
js(R/'out/SOURCE_RECEIPTS.json',[{'path':str(p),'bytes':p.stat().st_size,'sha256':sha(p),'scope':'Observed read-only bytes; mutable path not an immutable revision'} for p in sources])
old=read(prev/'CLAIMS.json')[0]
js(R/'out/PREVIOUS_REVIEW.json',{
 'claim':old['claim_id']+'@1','statement_sha256':old['statement_sha256'],
 'source':str(AGENTS/'A055/runs'/runs['A055']/'REPORT.md'),
 'reviewer':'A055','reported_verdict':'SCOPED HOLDS WITHOUT REPAIR',
 'scope':'DERIVATION Sections2--6; prior-stage paid-pair hardness; no whole FEI endorsement',
 'consumption':'Acceptance consumed from source-bound REPORT; original run unchanged; registry adoption unverified'})
review="""# Independent source reconstructions and validation scope

A002-BOUNDED-DATA-FRONTIER-ESCAPE@1: scoped HOLDS without repair at REVIEW_A051 Section4, including all-leaf signed error E and rp/prd spending, under ORIGINAL DATA queries and no intervening input reset. DERIVATION Section5 reconstructs the proof using tensor additivity, untouched-factor minimum influence, exact activated linear minimum and full scalar entropy profile. The source's original restrictions are essential to its all-leaf conclusion. No source census totals are adopted.

A052-ORIGINAL-PARTITION-COMPENSATED-RESET-INVARIANCE@1: scoped HOLDS without repair at PRECONDITIONING_PROOF Sections1--2. The triangular map bijects original fibres; full H and optimized I are invariant fibrewise; subtraction of root I gives the exact compensated Delta. Pullback transports every threshold span and old booked subspace, preserving quotient ranks. All-k examples, critical claims and source census remain outside this independent acceptance.

The new character-error frontier theorem supplies a different mechanism for changed partitions, control queries and arbitrary branch-dependent affine resets. Its all-policy conclusion is for EXPECTED complete terminal deficit. The inactive-control constant-child guard explicitly refutes any attempted upgrade to every leaf. Its deficit bound excludes influence-increasing resets; entropy-only bound does not.

Main finite checks use FWHT and exact prime-log entropy vectors; independent replay uses direct character sums, physical endpoint counts, differently evaluated mixed input maps and direct rational-log entropy intervals. This is a different implementation by A005, not independent-agent acceptance of the new result. All-depth Jensen/supermartingale statements are analytically proved, not inferred from depth2 data.
"""
save(R/'REVIEW.md',review)
statement="""For a finite uniform Boolean sign g let e(g)=(1-max_S abs(ghat(S)))/2. Every invertible affine input map and output-character multiplication preserves e and H; each actual physical single-coordinate restriction satisfies E_b e(g_b)<=e(g), and every directional minority probability is at most min(2e(g),1/2). Put phi(x)=h2(x)+2x/ln2 and a=min(2e(root),1/2). For EVERY finite adaptive tree of maximum single-coordinate query depth r, permitting arbitrary branch-dependent affine/character resets, all complete original terminal reaches retained, H(root)-E H(leaves)<=r phi(a). If each reset does not increase actual influence, then E D_K(leaves)>=D_K(root)-r phi(a), K>=0. For activation F=1+1[k controls=0](g^tensor(t)-1), k>=2,p=2^-k, a canonical full-span affine-minimal seed g with H0=H(g),q=I(g), and every such frontier, E D_K(leaves)>=p[t(H0-Kq)-(10+2K)k-15-2r(k+3/ln2)]. With t2^k and rk/2^k->0 this retains seed deficit in expectation despite bounded-I/L2 escape; with t2^l,k2l and rl/2^l->0 it retains normalized deficit while I(root)->0 and the seed ratio survives. A positive seed deficit therefore forces at least one violating complete leaf, even after full affine resets, and all-terminal nonviolation requires maximum depth at least [t(H0-Kq)-(10+2K)k-15]/[2(k+3/ln2)] when its numerator is positive. The actual point8 seed at K15/4,k20,t2^20 gives expected complete terminal deficit>595/1048576 for EVERY admissible frontier of maximum depth64. Constant inactive-control leaves are retained; every-leaf positivity is not asserted."""
deps=[
 'CLAUDE-B11-R1@1: established single-coordinate JS<=2 Inf/ln2; together with B_i<=h2(Inf_i) gives the consumed local entropy bound',
 'A051-AFFINE-MINIMUM-BASIS-CRITICAL-REDUCTION@1: previously reviewed finite affine canonicalization criterion',
 'A051-TAIL-CERTIFIED-FINITE-APPROXIMATION-AND-ESCAPE@1: COMPACTNESS Sections2--3 exact activation profile p(10k+15), tensor/affine full-span preservation; independently accepted by A002 at this scope',
 'Elementary character approximation, physical restrictions, concavity of h2 and finite entropy/influence telescopes; no FEI premise']
claim={'claim_id':'A005-ARBITRARY-AFFINE-FRONTIER-DEFICIT-RETENTION','version':1,
 'exact_statement':statement,
 'hypotheses':['Uniform finite Boolean signs and normalized real Walsh coefficients; entropy bits; K>=0',
               'r is MAXIMUM number of queried single coordinates on any path, not expected depth or number of multi-coordinate blocks',
               'Affine resets are actual invertible maps in the current remaining-variable chart plus output characters; may mix data/controls and change the next partition',
               'All complete terminal reaches and entropies retained; stopped leaves padded with idle accounting levels',
               'Entropy bound allows any affine reset; deficit bound requires each reset not increase actual child I',
               'Seed application uses positive-entropy canonical seed; seed-positive deficit implications are conditional unless a specified source deficit is exactly certified',
               'Activation k>=2; rates stated explicitly, no uncontrolled infinite optimizer or interchange of infinite sums',
               'Point8 scalar certificate never constructs its large root truth table; every terminal positivity is NOT claimed'],
 'statement_sha256':hashlib.sha256(statement.encode('utf-8')).hexdigest(),
 'contributors':['fleet03/A005'],'proof_source':['DERIVATION.md Sections1--4','code/check.py','code/independent.py','out/CHECK.json','out/INDEPENDENT.json'],
 'proof_dependencies':deps,'review_records':[],'status':'AUTHOR_PROOF_EXACT_CERTIFICATES_PENDING_INDEPENDENT_REVIEW',
 'supersedes':[],'refutes':[],'first_unproved_line':None,
 'next_consumers':['A002','A051','A052','A055','A090','A094','B20']}
js(R/'CLAIMS.json',[claim])
next_action='A002/A051 independently review character-error supermartingale and all-policy frontier budget; A052/A055 force original-pair lower funding using genuine NONNEGATIVE smaller-affine-child reserves, independent quotient rank, SAME unused bank and mixed interaction.'
progress={'protocol_revision':protocol['revision'],'run_id':R.name,'stream':'B01','packet_id':'A005',
 'gap_id':'C019-CRITICAL-ORIGINAL-PAIR-LOWER-FUNDING','attempt_id':'A005-stage19-character-error-affine-frontier',
 'method':'Consume A055 acceptance; scoped independent A002/A052 reconstructions; best-character-error supermartingale, symmetric local entropy bound, levelwise Jensen and full signed telescope',
 'mathematical_delta':'Original-data/no-reset restriction removed for expected frontier deficit. Every adaptive affine/control policy of depth r has loss<=r phi(min(2e,1/2)); explicit rare-core lower bound and depth requirement. Point8 depth64 ALL-policy certificate595/1048576. Universal FEI constant gain0.',
 'deliverable_status':'COMPLETE_LOCAL_VERIFIED','mathematical_status':'FULL_FEI_OPEN; scoped new theorem author-proved, independent-agent review pending',
 'claim_versions_used':deps+['A002-BOUNDED-DATA-FRONTIER-ESCAPE@1: Section4 independently reconstructed','A052-ORIGINAL-PARTITION-COMPENSATED-RESET-INVARIANCE@1: Sections1--2 independently reconstructed','A005-PAID-PAIR-WEAK-AFFINE-CORE-HARDNESS@1: A055 scoped acceptance consumed'],
 'claims_created_or_changed':[claim['claim_id']+'@1'],
 'source_artifacts':['out/SOURCE_RECEIPTS.json','out/PREVIOUS_REVIEW.json','DERIVATION.md','REVIEW.md','out/FROZEN_SPEC.json','out/CHECK.json','out/INDEPENDENT.json'],
 'next_consumers':claim['next_consumers'],'next_action':next_action,'stagnant_substantive_attempts':0,
 'blockers':['Universal critical original-pair lower-funding/selection still unproved; affine frontiers cannot grant terminal nonviolation to arbitrary positive-deficit cores',
             'Independent-agent acceptance of new theorem, registry adoption, supervisor copying and brain ingestion unverified',
             'Brain self-care degraded: owner-model97.5h/state82h/dream32.8h stale at wake; personal context and memory consolidation unverified'],
 'packet_ids':['A005']}
js(R/'PROGRESS.json',progress);(R/'PACKET_DELTA.json').write_bytes((R/'PROGRESS.json').read_bytes())
report="""# exact target, quantifiers, hypotheses and units

A005/B01 stage19 tests whether arbitrary Boolean seed deficit survives an adaptive frontier once A002's ORIGINAL-data/no-intervening-reset restrictions are removed. Every finite uniform Boolean sign, normalized Walsh coefficients, H bits, fixed K>=0. Tree depth means MAXIMUM single-coordinate queries along a path, not expected depth or block count. We prove a uniform entropy budget for arbitrary affine reset policies, and a deficit budget when resets do not increase actual I. Full FEI remains OPEN; owner deadline23October2026 14:49UTC governs.

# sources actually read, revisions and theorem locators

BOARD header23October10:53UTC, unchanged B01 STREAM_NOTESv1, own stage18 STATUS, current protocol fields consumed; whole protocol and machine AGENTS retained from prior full session reads. Fresh substantive sources: A00205:38 REPORT/REVIEW_A051 Sections1--4; A05105:07 COMPACTNESS Sections1--4 and report context; A05205:58 REPORT/PRECONDITIONING_PROOF Sections1--5; A05504:20 REPORT's scoped acceptance of A005 prior claim. Current source claim identifiers and source hashes inspected. Exact paths/observed bytes saved in out/SOURCE_RECEIPTS. Prior campaign/registry/four-manuscript baseline reads are not represented as fresh audits. One two-wording read-only math recall returned background; its display was truncated and no stored card is a proof premise or a novelty claim.

The old lead weak-influence assignment was closed earlier. Dispatch consumes A055's scoped HOLDS of A005 stage18 without repair, and A002's explicitly excluded basis-changing/control frontier. out/PREVIOUS_REVIEW records the source-bound acceptance without editing the immutable old run. Required current-session wake completed with warnings: owner-model97.5hours, state-of-mind82hours and latest dream32.8hours stale. Brain self-care remains degraded/unverified; personal-context and memory-consolidation reliability remain affected. Current instructions/proof sources govern.

# complete derivation or exact first unsupported line

DERIVATION Sections1--6 gives the complete proof. Error e against the best signed Fourier character is invariant under every affine chart and output character, and is a supermartingale under actual restrictions: the old best character restricts to a valid signed character on each daughter. Every directional minority is<=2e. Symmetrize the established one-query entropy bound by multiplying the queried character, then apply concavity level by level, retaining all branch reaches and idle stopped leaves. This gives Hroot-EHleaf<=r phi(min(2e_root,1/2)), where phi=h2+2x/ln2. Nonincreasing actual reset influence gives the corresponding signed deficit lower bound.

For activation of t canonical seed copies with k>=2 controls, p2^-k, the resulting ALL-policy lower bound is E D_K(leaf)>=p[t D_K(seed)-(10+2K)k-15-2r(k+3/ln2)]. Every control query, changed physical partition and branch-dependent affine reset is covered. t2^k,rk/2^k->0 preserves expected seed deficit in the bounded-I escape; t2^l,k2l,rl/2^l->0 preserves normalized expected deficit while root I->0 and seed ratio survives. Genuine all-terminal nonviolation requires the explicit maximum-depth lower bound in DERIVATION Section3.

The point8 seed at K15/4,k20,t2^20 has root deficit>3731/1048576. Every permitted frontier of maximum query depth64 retains COMPLETE expected terminal deficit>595/1048576. This scalar certificate describes an actual finite Boolean formula without constructing its multi-million-coordinate table. At least one terminal violates; inactive-control constant leaves demonstrate why ALL-leaf positivity is false.

FIRST UNSUPPORTED UNIVERSAL LINE: force a paid ORIGINAL proper pair at a genuine finite least-dimensional positive fixed-K witness using NONNEGATIVE smaller-affine-child reserves, independent quotient rank, SAME unused bank and mixed interaction. The frontier theorem blocks manufacturing that eligibility from arbitrary cores; it does not select or pay a critical pair. No universal constant gain or full FEI counterfamily is claimed.

# executed validation with domain, arithmetic, commands and outputs

Frozen out/FROZEN_SPEC precedes jobs. Commands from A005: python -B -X utf8 runs/20261023T110104Z-fleet03-A005-noncircular-endpoint-referee/code/check.py --pilot; same without --pilot; then code/independent.py in this run. Pilot4037 assertions PASS in1.008s on22 base roots/22 activation roots; excluded from final count.

Primary full152876 assertions PASS in17.408s: ALL278 labelled n0..3 tables and66 frozen activated fixtures (root dimension<=6),1022 first queries,33560 complete branch/reset/query options. EVERY distinct nonincreasing affine/character image of each <=2-bit base child is generated. Independent branch maxima certify322426 Cartesian-combined policies by separability; this is NOT322426 individually replayed policies or assertions. Activated fixtures use identity, exact greedy canonical and accepted explicit shear resets, not an exhaustive higher-dimensional orbit census.

Separate direct-character/physical-edge replay934 assertions PASS in15.287s: a7-bit tensor-bent activated root after an actual data/control input shear, branch-dependent resets, four complete depth2 terminals, all directional error bounds, inactive-control constant leaf, influence-increasing reset adversary, and point8 rational scalar certificate. Total153810 NEW full assertions; this differs from preceding stage11476 because this is a different frontier domain, not a revised old total. Old totals, pilot and source-agent checks are excluded.

Arithmetic: integer FWHT versus separate direct characters, exact Fraction physical/spectral costs, prime-log entropy identities versus direct rational-log entropy intervals,24/40-term positive atanh tails with explicit error. No floating proof decisions. Constants, zero error, characters, zero coefficients and all original reaches are retained. Infinite-parameter/r-depth statements follow the analytic supermartingale/Jensen proof, not finite extrapolation. Jobs55s cap, estimated110MB RAM, peak unmeasured; no >300MB job, automatic dimension increase, GPU or detached work. Initial compute snapshot status ok,17.3GB physical free,69.3percent commit used; startup contention was reported by runtime. Existing work unchanged. No Lean attempt or formal certification claimed.

# proof dependencies and changed downstream conclusions

Consumes established channel JS<=2Inf/ln2 and B_i<=h2(Inf_i), the reviewed finite affine-basis criterion and A051 activation profile/full-span preservation. REVIEW/DERIVATION Section5 independently reconstruct A002 Section4 and A052 Sections1--2 unchanged, without repair; no whole-source/census acceptance inferred. A055's prior A005 acceptance is consumed at DERIVATION Sections2--6 only. The new theorem has author proof/exact certificates; independent-agent acceptance pending.

Changed downstream conclusion: arbitrary affine/control frontiers cannot evade rare arbitrary-seed debt merely by changing query charts; explicit maximum-depth/expected-debt constraints replace the old original-data-only scope. Nonincreasing influence is essential to deficit conservation. Root e/H invariance alone permits influence-increasing resets, but those are not free funding. No source theorem is refuted and no FEI constant improves.

# one next mathematical action and independent reviewer

A002/A051 independently reconstruct the best-character-error supermartingale, padded-level Jensen step and r-dependent scalar budget; A055/A090/A094 challenge control/mixed-chart scope and the expected-versus-every-leaf distinction. A052/A055 should force critical ORIGINAL-pair lower funding using genuine nonnegative smaller-affine-child reserves, independent quotient rank, SAME unused bank and mixed T. This targets the excluded eligibility hypothesis; another bounded frontier or root-only structural admission remains arbitrary-seed hard. Handoff saved locally; no messages sent.

# actual persistence receipts or precise save blocker

All four protocol files, complete DERIVATION/REVIEW, frozen spec, code and exact outputs saved only under A005. Finalizer checks exact required field sets, statement hash, byte-identical PROGRESS/PACKET_DELTA, seven report headings,20MB cap and two-line STATUS. out/PERSISTENCE_RECEIPT hashes every run artifact and rolling file; out/HANDOFF_CHECK is written after a separate reopened hash verification. Local persistence verified. Independent-agent review, registry adoption, supervisor copies, remote mirrors and research-brain ingestion unverified. Required runtime wake ran; no research brain/shared-source writes, git, mail, deletion or trading access. No new job remains running, and no existing work was stopped.

## Universal bridge

C019 stopping-tree payment gains a uniform all-policy barrier beyond original-data frontiers: best-character error survives affine charts and controls the complete expected terminal debt through arbitrary nonincreasing affine resets, with explicit r-dependent lower bounds and a depth64 rational counterguard to eligibility at15/4. Constant gain is0; all-terminals-paid critical original-pair selection remains unproved. NEXT exploits genuine NONNEGATIVE smaller-child reserve and independent rank at the original pair, because that is the hypothesis these arbitrary-core frontiers still fail; another short chart-changing frontier cannot close the universal unpaid step.
"""
save(R/'REPORT.md',report)
save(OWN/'STATUS.md','STATE: A005 stage19 saved: arbitrary affine/control frontiers retain rare-core expected deficit; ALL depth64 certificate595/1048576 at K15/4;153810 exact checks PASS; FEI OPEN.\nNEXT: A002/A051 review character-error frontier theorem; A052/A055 force ORIGINAL pair funding from NONNEGATIVE smaller-affine-child reserves, SAME bank and mixed T.\n')
stamp=datetime.datetime.now(datetime.timezone.utc).isoformat()
for name,entry in [
 ('WORKLOG.md',f'\n{stamp} stage19: Read BOARD10:53/B01 notes/current source dependencies; consumed A055 scoped acceptance of stage18. Independently reconstructed A002 original-data frontier Section4 and A052 compensated invariance Sections1--2. New mechanism: e=(1-max|Fourier coefficient|)/2 is affine-invariant and restriction-supermartingale, giving arbitrary affine/control tree entropy loss<=r phi(min(2e,1/2)); nonincreasing reset I yields full expected deficit retention. Point8 k20,t2^20,K15/4: every depth64 policy retains deficit>595/1048576. Primary152876+separate934=153810 full exact checks PASS; pilot4037 excluded. Critical original-pair lower funding remains OPEN. No stage jobs left; required wake warned stale owner/state/dream notes.\n'),
 ('LEARNED.md','\nStage19 durable theorem: signed-character approximation error e(g)=(1-max|ghat|)/2 is preserved by arbitrary affine/character resets and satisfies E e(child)<=e(parent). Every directional minority<=2e. With phi=h2+2x/ln2, ANY adaptive affine frontier of MAXIMUM single-coordinate depth r has Hroot-EHleaf<=r phi(min(2e_root,1/2)). If resets do not increase I, E Dleaf>=Droot-r phi. For k-control activation of t canonical seed copies: E Dleaf>=p[tDseed-(10+2K)k-15-2r(k+3/ln2)]. This includes control queries and changed partitions; unlike old A002 data-only theorem it guarantees expected debt, not every leaf. Constant inactive leaves are necessary. Maximum depth cannot be replaced by expected depth. Point8/K15/4/k20/t2^20/r64 exact residual>595/1048576. Universal gap remains ORIGINAL-pair funding from genuine nonnegative smaller-affine-child reserves, not bounded affine-frontier admission. New theorem pending independent-agent review.\n')]:
    with (OWN/name).open('a',encoding='utf-8',newline='\n') as f:f.write(entry)
req=protocol['required_per_run']
assert set(claim)==set(req['claim_fields'])
assert set(progress)=={x if not x.startswith('packet_ids ') else 'packet_ids' for x in req['progress_fields']}
assert (R/'PROGRESS.json').read_bytes()==(R/'PACKET_DELTA.json').read_bytes()
assert all('# '+h in (R/'REPORT.md').read_text(encoding='utf-8') for h in req['report_fields'])
assert hashlib.sha256(read(R/'CLAIMS.json')[0]['exact_statement'].encode('utf-8')).hexdigest()==claim['statement_sha256']
assert len((OWN/'STATUS.md').read_text(encoding='utf-8').splitlines())==2
paths=sorted(p for p in R.rglob('*') if p.is_file() and p.name not in ['PERSISTENCE_RECEIPT.json','HANDOFF_CHECK.json'])
paths += [OWN/n for n in ['STATUS.md','WORKLOG.md','LEARNED.md']]
assert all(p.stat().st_size<20*1024*1024 for p in paths)
js(R/'out/PERSISTENCE_RECEIPT.json',{'status':'LOCAL_SAVE','utc':stamp,'files':[{'path':str(p),'bytes':p.stat().st_size,'sha256':sha(p)} for p in paths],'remote_copy':'UNVERIFIED; supervisor responsibility'})
for entry in read(R/'out/PERSISTENCE_RECEIPT.json')['files']:
    assert sha(Path(entry['path']))==entry['sha256']
js(R/'out/HANDOFF_CHECK.json',{'status':'PASS','verified_hashes':len(paths),'receipt_sha256':sha(R/'out/PERSISTENCE_RECEIPT.json'),'new_full_assertions':total,'full_fei':'OPEN'})
print(json.dumps({'status':'PASS','verified_hashes':len(paths),'new_full_assertions':total,'claim':claim['claim_id'],'full_fei':'OPEN'}))
