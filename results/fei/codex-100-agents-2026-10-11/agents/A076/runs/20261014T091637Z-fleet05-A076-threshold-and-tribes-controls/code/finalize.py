"""Source-bound stage6 protocol persistence; no writes outside A076."""
from pathlib import Path
import json,hashlib,datetime
ROOT=Path(__file__).resolve().parents[1];AGENT=ROOT.parents[1]
BASE=AGENT.parents[1];PREV=AGENT/'runs/20261014T042128Z-fleet05-A076-threshold-and-tribes-controls'
A77=BASE/'agents/A077/runs/20261014T045011Z-fleet05-A077-sparse-defect-towers'
A27=BASE/'agents/A027/runs/20261014T043519Z-fleet05-A027-block-selection'
A28=BASE/'agents/A028/runs/20261014T051435Z-fleet05-A028-stopping-tree-payment'
PROTO=Path(r'~\mop_fei100\reports\fei-2026-10-11\EXECUTION_PROTOCOL.json')
def load(p):return json.loads(Path(p).read_text(encoding='utf-8-sig'))
def sha(p):return hashlib.sha256(Path(p).read_bytes()).hexdigest()
def save(p,v):(ROOT/p).write_text(json.dumps(v,indent=2,ensure_ascii=False)+'\n',encoding='utf-8')
pr=load(PROTO);old=load(PREV/'CLAIMS.json');incoming=load(A77/'REVIEW_A076.json')
for r in incoming:
    c=next(c for c in old if c['claim_id']==r['claim_id'])
    assert c['version']==r['version']==5 and c['statement_sha256']==r['original_statement_sha256']
save('out/CONSUMED_REVIEW.json',dict(source=str(A77/'REVIEW_A076.json'),sha256=sha(A77/'REVIEW_A076.json'),records=incoming,
 scope='Only STRUCTURED-SPECTRA v5 admission sections1-3 accepted. Sharpness/reset/equivalence and other bundle excluded. v6 not independently reviewed.'))
full=load(ROOT/'out/FULL.json');plat=load(ROOT/'out/PLATEAU_FULL.json');rep=load(ROOT/'out/REPRODUCTION.json')
pilot=load(ROOT/'out/PILOT.json');ppilot=load(ROOT/'out/PLATEAU_PILOT.json')
assert all(x['status']=='PASS' for x in [full,plat,rep,pilot,ppilot]);total=sum(x['exact_assertions'] for x in [full,plat,rep])
save('out/VALIDATION_RECEIPTS.json',dict(status='PASS',exact_assertions_excluding_pilots=total,
 full=[full,plat,rep],pilots=[pilot,ppilot],
 plateau_rerun='Initial full PASS 7318 assertions/3.932s; added explicit post-shared inherited-quarter and nonconstant-core guards within frozen mixed-history domain, then final PASS7330 assertions. No failed job or dimension escalation.',
 independent_implementation='check_spectrum.py uses direct character sums and exact four-point tensor coefficients; not an independent agent review.'))
extensions=[
 ' Stage-6 extension: For even k>=4, canonical quadratic bent H on k shared bits, epsilon=2^-k, arbitrary Boolean private V, F=H[1+1{s=0}(V-1)] has Fhat(S,empty)=Hhat(S)-epsilon(1-mu), Fhat(S,T)=epsilon Vhat(T) for T nonempty; I(F)=k/2+k epsilon(1-mu)+epsilon I(V), H(F)=epsilon H(V)+k+R(mu)+J_k(mu), R=k epsilon(1-mu^2), |J_k prime|<=40epsilon, J_k(1)=0. Every private query has exact Delta H(F)=epsilon Delta H(V)+release_R+Delta J, release_R=k epsilon Vhat(i)^2 and |Delta J|<=40Inf_private(F). Arbitrary private stopping trees telescope the same R and retain full input/terminal entropy; B-tree price is43 with epsilon inherited input B. Supplied H(V)<=C0 I(V) transfers at C=max(C0,5), and exact signed surplus has carrier remainder U_C>=3k/16. More generally H with 2^q equal-magnitude nonzero Fourier rows on d bits (q even<=d,H(0)=1,2^(-d+q/2)<=1/4) has H(F)=epsilon H(V)+q+R+K+J, with R=d epsilon(1-mu^2), explicit convex K, |J prime|<=60epsilon. Thus Delta H(F)<=epsilon Delta H(V)+release_R+60Inf_private(F), retaining all old zero rows and signed negative K drift. The bank is the point-product specialization of A028 v5; it is not a second independent reserve.',
 ' Stage-6 extension: In the actual mux G=quadratic_bent_H[1-2*1{s=0,x=0}],H, selector z unqueried, any surviving private point-prefix of m>=2 bits has consumed private influence m epsilon 2^-m, root R=k epsilon(2^(1-m)-2^(-2m)), terminal mean R=k epsilon 2^-m, and releases k epsilon(2^-m-2^(-2m)). Both branch cores and every mux terminal remain nonconstant, while the original selector-mismatch account has zero conditional expected release. At m2 the first/second weighted R releases are k epsilon/16 and k epsilon/8; no reserve is renewed. Literal private V gives residual (Delta H(F)-epsilon Delta H(V))/Inf_private(F)>=k-40, so dropping R is impossible at any universal local price; parity V postpones all bank release to the second query. For the SAME k6,m3 source, x1,x2,s1,x3 exposure with every sibling retained and z untouched is paid by inherited signed input entropy, one original R bank, private physical price60 and shared physical price6. The zero shared child has d5,q4 Fourier rows with zeros and explicit signed carrier surplus>=55/32 at C>=5; the other shared child is retained quadratic/literal. Full inherited quarter-core erasures are recorded at all private queries, including after the shared query. No arbitrary unequal-height carrier payment or arbitrary-V certificate is asserted.'
]
claims=[]
for c,ext in zip(old,extensions):
    cid=c['claim_id'];c['version']=6;c['exact_statement']+=ext
    c['statement_sha256']=hashlib.sha256(c['exact_statement'].encode()).hexdigest()
    c['hypotheses'].append('Stage6 phase point family on independent shared/private uniform cubes; k even>=4 for full-bent transfer, or equal-magnitude nonzero carrier support2^q with explicit alpha<=1/4 for plateaued drift. Inherited input entropy certificate remains supplied; mixed history only at declared source, no new bank. Bits.')
    c['proof_source'].update(stage6=str(ROOT/'PHASE_BANK_PROOF.md'),stage6_locator='sections1-6 equations1-13',stage6_validation=str(ROOT/'out/VALIDATION_RECEIPTS.json'))
    c['proof_dependencies'].append(cid+'@5')
    c['proof_dependencies'].append('A028-UNBALANCED-ACTIVATION-STOPPING-PAYMENT@5 sections4,7: point-product bank specialization independently derived here; general pending theorem not assumed')
    c['supersedes']=[cid+'@5']
    for r in incoming:
        if r['claim_id']==cid:c['review_records'].append(dict(claim_version=5,record=r,source=str(A77/'REVIEW_A076.json'),guard='Only admission sections1-3; no v6 or sharpness/reset acceptance'))
    c['status']='AUTHOR_PROVED_PENDING_INDEPENDENT_REVIEW'
    c['next_consumers']=['A077','A078','A027','A028','A092','A088','A094','B16','B20']
    c['first_unproved_line']=None
    assert set(c)==set(pr['required_per_run']['claim_fields']);claims.append(c)
save('CLAIMS.json',claims)
now=datetime.datetime.now(datetime.timezone.utc).isoformat()
sources=[PROTO,BASE/'BOARD.md',BASE/'claude/B16/STREAM_NOTES.md',PREV/'CLAIMS.json',PREV/'PRIVATE_ADMISSION_PROOF.md',PREV/'code/arithmetic.py',
 A77/'PROOF.md',A77/'REVIEW_A076.json',A27/'DERIVATION.md',A28/'DERIVATION.md',A28/'CLAIMS.json']
save('SOURCE_MANIFEST.json',dict(captured_at=now,hash_scope='actual save-time bytes, not retroactive snapshots',sources=[dict(path=str(p),sha256=sha(p),bytes=p.stat().st_size) for p in sources],
 read_scopes=dict(board='2026-10-14 09:12 UTC; board and separately reread middle B06-B14 summaries',lead='B16 v2 unchanged; initial assigned majority/tribes controls completed earlier',
 A077='PROOF sections1-7 and REVIEW_A076 actual file; geometric exit mechanism is prior work, not rediscovered',
 A027='Complete DERIVATION: signed supplied-child admission and future-control nonrenewal',
 A028='Complete DERIVATION and current claim: one mixed-query bank; conservation is distinct from signed local payment')))
nextact='At the already booked private/shared/private history, replace the carrier by the first unequal-height threshold control (Maj5 point edit). Derive a signed row-profile estimate from SAME unused boundary/source surplus, retaining old debits, quarter inherited core and both full terminals. A092/A088 or A094 review v6; A027/A028 consume.'
progress=dict(protocol_revision=pr['revision'],run_id=ROOT.name,stream='B16',packet_id='A076',gap_id='FEI-B16-A076-INITIAL',attempt_id='A076-stage6-flat-carrier-same-bank-mixed-history',
 method='Exact bent/plateaued spectra; signed Lipschitz profile and convex zero-row refund; original boundary bank through private/private/shared/private exposure; exact rational certificates and independent direct Walsh reconstruction',
 mathematical_delta='Pays repeated private collisions with both cores nonconstant, then one shared-data query and another private exposure from the SAME original R bank. Explicit inherited input entropy remains. New actual local prices40/60 and source-surplus identities supplement A028 bank conservation; no arbitrary-core certificate.',
 deliverable_status='COMPLETE_LOCAL_PENDING_V6_REVIEW',mathematical_status='SCOPED_SAME_BANK_MIXED_PAYMENT_AUTHOR_PROVED; UNEQUAL_HEIGHT_AND_FULL_FEI_OPEN',
 claim_versions_used=['A076-STRUCTURED-SPECTRA@5 admission sections1-3 independently accepted by A077','A076-TRIBES-PAYMENT-DISCRIMINATION@5 retained, no new independent acceptance','A028-UNBALANCED-ACTIVATION-STOPPING-PAYMENT@5 sections4,7 specialized/rederived, general proof not assumed','A027 stage5 supplied signed child-surplus admission context','A077 stage5 geometric-release theorem context only'],
 claims_created_or_changed=[c['claim_id']+'@6' for c in claims],
 source_artifacts=['PHASE_BANK_PROOF.md','SOURCE_MANIFEST.json','code/arithmetic.py','code/check_phase.py','code/check_plateau.py','code/check_spectrum.py','code/finalize.py','out/FROZEN_SPEC.json','out/PLATEAU_SPEC.json','out/REPRODUCTION_SPEC.json','out/VALIDATION_RECEIPTS.json','out/HISTORY_LEDGERS.json','out/MIXED_HISTORY.json','out/COMPRESSED.json','out/CONSUMED_REVIEW.json'],
 next_consumers=['A077','A078','A027','A028','A092','A088','A094','B16','B20'],next_action=nextact,stagnant_substantive_attempts=0,
 blockers=['Unequal nonzero carrier heights lack a proved signed local price','Arbitrary inherited input entropy is still FEI-strength; no supplied universal certificate','v6 independent review, supervisor adoption and mirrors unobserved'],packet_ids=['A076'])
assert set(progress)=={x.split(' (')[0] for x in pr['required_per_run']['progress_fields']}
save('PROGRESS.json',progress);save('PACKET_DELTA.json',progress)
report=f'''# A076 stage6: one carried bank through nonconstant private collisions

## exact target, quantifiers, hypotheses and units

Pay the next private collision when BOTH actual branch cores stay nonconstant, then carry the same account through a shared-data query and another private exposure. On independent uniform shared/private cubes take F=H(s)[1+1{{s=0}}(V(x)-1)]. For a k-bit quadratic bent carrier, k even>=4, derive exact spectra and signed entropy transfer for EVERY Boolean V. Extend the local payment to carriers having equal-magnitude nonzero Fourier rows with zeros, under the explicit alpha<=1/4 hypothesis. Entropy/JS/erasure are bits. The actual mixed source k6,m3 has the original selector unqueried and every terminal retained. Full FEI remains OPEN.

## sources actually read, revisions and theorem locators

Read the full execution protocol v2, own STATUS/WORKLOG/LEARNED, BOARD.md dated 2026-10-14 09:12 UTC with middle stream summaries reread, and unchanged B16 notes v2. Prior majority/tribes lead assignment was already completed. Read A077 stage5 PROOF sections1-7 and actual REVIEW_A076.json; its v5 statement hash matches. Read complete A027 stage5 DERIVATION (signed child admission; future-control nonrenewal), and A028 stage5 DERIVATION sections1-7/current claim (boundary bank conservation, release-only obstruction). SOURCE_MANIFEST pins the bytes and scopes. A guessed A077 REVIEW.json did not exist; directory listing identified REVIEW_A076.json. No acceptance is inferred from the missing path.

A077 already pays geometric point-defect exits. This stage uses phase-point edits whose two branch cores remain nonconstant, so it does not repeat that mechanism. A028 already owns the boundary bank: the new result is an actual local signed entropy price and a physically mixed continuation, beyond bank conservation alone.

## complete derivation or exact first unsupported line

PHASE_BANK_PROOF.md sections1-6 contains the complete derivation. Exact paired rows yield H(F)=epsilon H(V)+k+R+J and I(F)=k/2+k epsilon(1-mu)+epsilon I(V). The single original R=k epsilon(1-mu^2) is A028's point-product boundary reserve. The signed remainder has |J'|<=40epsilon; therefore every private query costs epsilon times its inherited input entropy decrement, its exact R release, and at most40 actual private influence. This telescopes for arbitrary private stopping trees, with terminal R and both actual terminal spectra retained. A supplied input H/I certificate transfers at max(C0,5); the source surplus is explicit and signed.

For plateaued carriers, exact zero-row counting adds a CONVEX profile K and a remainder with |J'|<=60epsilon. K contributes a nonpositive signed decrement. This proves local payment from the SAME R plus60 actual private influence, including the Fourier zeros created by one shared query. The inherited epsilon input entropy is never erased or called free.

In the point-edit mux, selector mismatch has zero expected release under private exposure; it cannot pay the second collision by a reset. At m2 the same R releases k epsilon/16 at the first query and k epsilon/8 at the second in root-weighted units. All branch cores remain nonconstant. The original k6,m3 source then follows x1,x2,s1,x3. Its shared query costs at most6 actual influence, releases part of the old boundary bank, and leaves a d5,q4 zero-row child plus the complete quadratic/literal sibling. The next private query satisfies the new plateaued estimate, keeps the prior debits and exact terminal influence/entropy, and has a source surplus lower bound55/32 at target C>=5. The actual inherited quarter-core B is saved at every private node, including after the shared query.

The first unsupported universal line is the signed estimate for carriers with UNEQUAL nonzero Fourier heights, with the same unused source surplus and inherited input entropy. Arbitrary V still needs its supplied full input certificate. A universal arbitrary-V certificate would itself prove FEI; neither a new isolated class constant nor this bank conservation supplies it.

## executed validation with domain, arithmetic, commands and outputs

All three specifications were frozen before their searches. Main pilot:22 roots/36 private queries, {pilot['exact_assertions']} exact assertions in {pilot['elapsed_seconds']:.3f}s. Main full:every labelled V on0..3 private bits and k4,6, **556 roots,1608 private queries, six complete point-prefix ledgers**, {full['exact_assertions']:,} assertions in {full['elapsed_seconds']:.3f}s. Compressed literal/parity bank witnesses at k4,6,8,16,32,64 use proved exact multiplicities, not sampled tables.

The new plateaued domain was separately frozen after its analytic derivation: d5,q4 and every labelled V on0..3 private bits. Pilot:{ppilot['exact_assertions']} assertions. Full:**278 roots,804 private queries plus the actual mixed history**, {plat['exact_assertions']:,} assertions in {plat['elapsed_seconds']:.3f}s. An initial passing plateau run had7318 assertions; the final run adds explicit post-shared quarter-core and nonconstant-core guards on the same domain. Independent direct character sums/product coefficients passed {rep['exact_assertions']:,} assertions on22 roots in {rep['elapsed_seconds']:.3f}s. This is independent implementation, not independent-agent review. Total full/reproduction assertions excluding pilots: **{total:,} PASS**.

Commands: `python -X utf8 code/check_phase.py --pilot`, then without `--pilot`; similarly `code/check_plateau.py`; `python -X utf8 code/check_spectrum.py`, each relative to this run. FWHT/Fraction spectra, separate physical edges, prime-exponent exact log identities, and24-term rational atanh logarithm bounds with proved tails and outward70-bit rounding. No floating comparison establishes a sign. Compressed outputs use outward90-bit storage. Main jobs were estimated below180 MB, cache cleared per root, peaks not measured; no job expected over300 MB, so no heavy-job memok gate was triggered. No failed compute job or automatic domain escalation occurred.

## proof dependencies and changed downstream conclusions

Extend the same two A076 bundles to v6. Incoming A077 acceptance is scoped ONLY to STRUCTURED-SPECTRA v5 admission sections1-3; it does not accept earlier bundle material, v5 sharpness/reset/equivalence, the second bundle, or v6. A028's bank is explicitly credited and its point specialization is rederived. A027's admission and A077's geometric theorem are contextual dependencies, not premises declaring arbitrary children certified. The analytical estimates here use exact rows and elementary derivative bounds; B-tree corollaries use the established JS<=2Inf/ln2 inequality. No third broad unreviewed candidate is opened.

A027/A028 now have an actual local signed bill and a carried nonconstant-terminal mixed history in a concrete source, beyond their conservation-only reserve. A077/A078 receive the second-collision alternative to geometric point exits. A092/A088/A094 receive the source-bound proof, full ledger and exact first unequal-height gap. No external review, downstream adoption or remote mirror is claimed for v6.

## one next mathematical action and independent reviewer

{nextact}

## actual persistence receipts or precise save blocker

The four required protocol files, proof, source hashes, frozen specs, code, exact outputs and rolling files are saved inside A076. PERSISTENCE_RECEIPT.json records actual file hashes and sizes after protocol/statement-hash/packet-copy checks; it cannot hash itself. All files are below20 MB. Shared source trees were read only. Supervisor copying, GitHub/brain persistence, and independent acceptance are unverified.

## Universal bridge

This stage moves **C019 stopping-tree payment** from A076's single private antichain and A077's geometric exits to repeated collisions with two nonconstant cores, then one shared physical query and another private collision, using exactly ONE original A028 boundary bank. The added prices are40 for a full bent carrier and60 for plateaued nonzero rows; inherited input entropy, quarter-core erasures, booked debits and both terminal laws remain explicit. What remains is a signed price for unequal nonzero Fourier heights and a supplied certificate for arbitrary inherited inputs. NEXT targets the first unequal-height threshold carrier on the same booked history because that is the missing row-profile mechanism needed for universal restriction induction, rather than another standalone class H/I bound.
'''
(ROOT/'REPORT.md').write_text(report,encoding='utf-8')
status='STATE: A076 stage6 saved: one boundary bank pays nonconstant private/private/shared/private history; exact bent/plateaued signed prices40/60; '+str(total)+', exact assertions PASS; v6 review pending; FEI OPEN.\nNEXT: Unequal-height threshold carrier (Maj5 point edit) on SAME booked history: price signed row remainder from unused R/source surplus, retaining inherited input entropy, quarter core and both terminals; A092/A088/A094 review.\n'
(AGENT/'STATUS.md').write_text(status,encoding='utf-8')
with (AGENT/'WORKLOG.md').open('a',encoding='utf-8') as f:
    f.write(f'\n## {now} (requested stage 2026-10-14 09:16 UTC)\nConsumed A077 scoped v5 admission acceptance; read A027/A028 one-bank constraints. Derived exact arbitrary-private-input bent phase-point entropy/influence, signed40-influence profile, nonnegative original boundary release and supplied-input max(C0,5) transfer. Extended to zero-containing plateaued carriers with convex refund and signed60 price; actual k6,m3 x1/x2/s1/x3 history keeps both nonconstant cores, original selector, inherited quarter and all terminals, no bank renewal. {total} full/reproduction exact assertions PASS; main22.571s, plateau final8.690s; no heavy/failed job. Unequal nonzero row heights and arbitrary inherited input certificate remain open. Two existing bundles extended to v6, independent review pending.\n')
with (AGENT/'LEARNED.md').open('a',encoding='utf-8') as f:
    f.write('\nStage6 durable facts: phase-point F=H(s)[1+point(s)(V-1)] with k-bit quadratic bent H, epsilon2^-k, has exact H(F)=epsilon H(V)+k+k epsilon(1-mu^2)+J(mu), |J prime|<=40epsilon; I(F)=k/2+k epsilon(1-mu)+epsilon I(V). R=k epsilon variance is precisely A028 point-product boundary bank, not an additional reserve. Private query release=k epsilon Vhat(i)^2; actual residual beyond epsilon inherited input entropy is paid by this release+40 actual influence. Literal input requires a bank: residual/Inf>=k-40; parity postpones release to query2. In phase-point mux both branch cores remain nonconstant while disagreement has zero expected private-query release, so selector resets cannot replace R. Plateaued carrier on d bits,2^q equal nonzero rows, alpha2^(-d+q/2)<=1/4, adds exact convex K=epsilon[2(d-q)rho+(d-(2d-q)2^(q-d))rho^2] and |J prime|<=60epsilon. Its signed K drop is nonpositive; old Fourier-zero rows matter. At k6,m3 actual x1,x2,s1,x3 history same R survives; zero shared child d5,q4, other child quadratic/literal retained, shared query full price<=6 actualInf, zero-child signed carrier surplus>=55/32 at C>=5. Arbitrary V input entropy remains inherited; unequal nonzero heights lack proof. Supplied input FEI transfers for full bent carrier at max(C0,5), not a universal input certificate. A077 v5 acceptance covers admission sections1-3 only; no sharpness/reset/equivalence or v6 acceptance.\n')
# Exact schema and byte receipts, after every final artifact is present.
assert len((AGENT/'STATUS.md').read_text().splitlines())==2
assert (ROOT/'PROGRESS.json').read_bytes()==(ROOT/'PACKET_DELTA.json').read_bytes()
for c in load(ROOT/'CLAIMS.json'):
    assert set(c)==set(pr['required_per_run']['claim_fields'])
    assert hashlib.sha256(c['exact_statement'].encode()).hexdigest()==c['statement_sha256']
for heading in pr['required_per_run']['report_fields']:assert '## '+heading in report
assert report.rstrip().split('\n\n')[-2]=='## Universal bridge'
files=[p for p in ROOT.rglob('*') if p.is_file() and p.name!='PERSISTENCE_RECEIPT.json']+[AGENT/x for x in ['STATUS.md','WORKLOG.md','LEARNED.md']]
assert all(p.stat().st_size<20_000_000 for p in files)
save('PERSISTENCE_RECEIPT.json',dict(status='VERIFIED_LOCAL',captured_at=now,full_fei='OPEN',independent_v6_review='PENDING',remote_mirror='UNVERIFIED',
 files=[dict(path=str(p),bytes=p.stat().st_size,sha256=sha(p)) for p in files]))
print(json.dumps(dict(status='SAVED_AND_PROTOCOL_CHECKED',exact_assertions=total,files=len(files)+1,largest_bytes=max(p.stat().st_size for p in files),run=str(ROOT))))
