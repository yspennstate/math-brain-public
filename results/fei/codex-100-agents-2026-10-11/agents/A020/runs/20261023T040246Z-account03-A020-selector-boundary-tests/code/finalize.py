from pathlib import Path
import json,hashlib,datetime
R=Path(__file__).resolve().parents[1];A=R.parents[1];B=A.parent
def read(p):return p.read_text(encoding='utf-8')
def write(p,s):p.write_text(s,encoding='utf-8')
def dump(p,x):write(p,json.dumps(x,ensure_ascii=False,indent=2)+'\n')
def sha(p):return hashlib.sha256(p.read_bytes()).hexdigest()
protocol=Path(r'math-open-problems/reports\fei-2026-10-11\EXECUTION_PROTOCOL.json')
P=json.loads(read(protocol));check=json.loads(read(R/'out/CHECK.json'))
assert check['status']=='PASS'
source=B/'A016/runs/20261023T000905Z-account03-A016-addressing-benchmark'
prior=A/'runs/20261022T231605Z-account03-A020-selector-boundary-tests'
board=B.parent/'BOARD.md';lead=B.parent/'claude/B04/STREAM_NOTES.md'
sources=[protocol,board,lead,source/'REPORT.md',source/'CLAIMS.json',prior/'REPORT.md',prior/'CLAIMS.json',prior/'code/check.py']
dump(R/'out/SOURCE_RECEIPTS.json',[{'path':str(p),'sha256':sha(p),'bytes':p.stat().st_size} for p in sources])
claims=[]
def claim(cid,statement,hyp,unproved):
 d=dict(claim_id=cid,version=1,exact_statement=statement,hypotheses=hyp,
  statement_sha256=hashlib.sha256(json.dumps({'exact_statement':statement,'hypotheses':hyp},sort_keys=True,separators=(',',':')).encode()).hexdigest(),
  contributors=['A020'],proof_source='REPORT.md; code/check.py; out/CHECK.json',
  proof_dependencies=['A020 stage7 same Boolean family, original Q and old U; direct coefficient reconstruction here','A016-FULL-SIGNED-TENSOR-PADDING-TRANSFER@1 (source boundary consumed, not assumed for new proofs)'],
  review_records=[],status='PROVED_LOCALLY_REVIEW_PENDING',supersedes=[],refutes=[],first_unproved_line=unproved,next_consumers=['A016','A018','A019','A090','A091','A094','B20'])
 claims.append(d)
claim('A020-RARE-HISTORY-FULL-RESERVE-NOGO',
 'For the original eligible A020/A016 reference on G_m=g3^m, k>=5, m=r+1>=4, query q then the first bit of r blocks. At the actual history with all r outcomes1, both q-sign terminals have 4I-CE-U <= 6+(2k+5)2^-k/8 -(7*2^-k/64)r log2(8/5). Hence the original full signed reserve is unbounded below over histories at fixed k; at k5,r4096 it is strictly below -241/256 at both complete terminals. This refutes all-history local eligibility for the same Q; it does not refute A016 fixed-subset averaged payment or FEI.',
 ['Uniform independent bits; g3 is -1 only at000, s2=[-1,1,1,1], A=point_k(1-G_m)/2, h=chi_u off A and chi_q on A, F=1 at gate0 and hs at gate1',
  'Original Q_h=(P_h+point_q)/2 and Q_F(e,T)=(Q_h(T_core)P_s(T_mask)+point_empty(T))/4 at both gate frequencies; every descendant uses its exact frequency marginal',
  'Same old U=L_q+E in [0,5/8), no new admission, reset or terminal omission; distinguished history has total physical reach2^-r and each q sign half that',
  'Other histories retained with original references and actual reaches; no lower bound on their local signed profiles is asserted'],
 'Whether an averaged adaptive paid stopping policy always avoids or repairs this local failure remains open.')
claims[-1]['refutes']=['Unregistered proposed extension: every history on this original eligible family preserves nonnegative full signed reserve']
claim('A020-ZERO-INFLUENCE-GHOST-CLEANUP',
 'On the same distinguished history, additionally query the two remaining coordinates of every killed block. Both outcomes are identical actual functions at each cleanup query, its physical influence is zero, and the original-reference row penalty (5/8)^r becomes1 by marginalization. With k>=5,r>=3, every complete cleanup terminal retains 4I-CE-U>5/4 for both original q signs. No bank or reference is reset. This exact cleanup repairs this family, without proving a universal cleanup policy.',
 ['All family, reference, query-history and old-debit hypotheses of A020-RARE-HISTORY-FULL-RESERVE-NOGO@1',
  'Cleanup only after all distinguished outcomes1, when each queried seed is already the constant+1; query its other two physical coordinates',
  'All2^(2r) cleanup outcomes retained; they have identical functions and original-reference marginals, each conditional reach2^(-2r)'],
 'Generalize ghost cleanup to interacting restrictions with no truly irrelevant physical coordinate, or pay their physical influence from an averaged same-reference source.')
claims[-1]['proof_dependencies']=['A020-RARE-HISTORY-FULL-RESERVE-NOGO@1 family/reference algebra; cleanup bound is rederived directly']
dump(R/'CLAIMS.json',claims)
report=r'''# A020 stage 8: rare-history ghost loss, and a zero-influence repair

Full FEI remains OPEN. The SAME eligible original reference can acquire arbitrarily negative local full signed reserve along a rare, actual physical history. Thus merely replacing the failed half-bank by the full signed reserve does not give an all-history invariant. On this family an exact zero-influence cleanup restores reserve greater than5/4 after the SAME old debit. A016's short-history and fixed-subset averaged theorems are not refuted. Both new claims await independent review.

## exact target, quantifiers, hypotheses and units

Use uniform independent0/1 bits, chi_z=(-1)^z, and base2 logarithms. Let g3 be-1 at000 and+1 elsewhere, G_m the product of m disjoint seeds, and A=point_k(v)(1-G_m)/2. Set h=chi_u off A and chi_q on A; F=1 at fresh gate x0 and hs at x1, with the fixed two-bit sign s=[-1,1,1,1]. Write rho=2^-k, mu=(3/4)^m, beta=(1-mu)/2 and p=rho beta. The supplied original reference is Q_h=(P_h+point_q)/2 and Q_F(e,T)=(Q_h(T_core)P_s(T_mask)+point_empty(T))/4 at BOTH gate frequencies. It is normalized and supports every true Fourier atom. No reference is renewed. Every later code is the exact frequency marginal of this Q_F.

Take k>=5,m=r+1>=4. Query q, then the first physical bit of each of r seeds, leaving one entire seed unqueried. Analyze the history where all r seed queries return1. Both q outcomes remain; their combined physical reach is2^-r and each has reach2^(-r-1). Keep the original booked debit U=L_q+E with its exact conversion, not its upper bound. On this history the actual function is independent of all2r remaining coordinates in the killed seeds. The optional cleanup queries those coordinates and retains all its physical outcomes. Reserve means4I-CE(F,Q)-U in bits, using the full signed account.

## sources actually read, revisions and theorem locators

Read current BOARD snapshot2026-10-23 03:54UTC, B04 STREAM_NOTES v2, own STATUS and stage7 helper/report/claims. Read A016 run20261023T000905Z-account03-A016-addressing-benchmark REPORT in full and both claims. Its stage8 already performed my saved tensor-bit/padding-bit NEXT, so that test is not repeated as a research target. Its full claim A016-FULL-SIGNED-TENSOR-PADDING-TRANSFER@1 distinguishes four/eight local terminals from a fixed-subset averaged guarantee. The present work consumes its explicit first unsupported line concerning arbitrary mixed histories. A016's independent acceptance of A020 stage7's admission no-go is recorded as source evidence; no blanket acceptance of earlier work is inferred.

Execution protocol revision2026-10-11-execution-v2 and machine rules were reread. Prior required campaign and paper readings are carried forward; no new paper theorem is a premise. Read-only math recall returned general restriction/FEI cards and unrelated matches; none supplies this local ledger. No external literature or novelty claim is made. Source byte hashes are in out/SOURCE_RECEIPTS.json. The current owner deadline2026-10-23 14:49UTC supersedes the static historical endpoint. Brain self-care is degraded/unverified because personal owner-model/state notes are stale; those notes are not mathematical inputs.

## complete derivation or exact first unsupported line

1. Original eligibility and old debit are retained. At q fixed the common core spectrum P has masses(1-p)^2 at{u}, p^2 atempty and two copies of Ahat(T)^2 at nonempty activation frequencies. With c=CE(P,(P+point_empty)/2) and J_A=4 sum|T|Ahat(T)^2,

I(h_q)=1-p+J_A/2, I(F)=3/2+J_A/4, CE_root=c/2+3.

The exact already booked debit is

L_q=(1/2)log((9+p^2)/8)+(p^2/8)log((9+p^2)/(1+p^2)),
E=(1+(p/2)^2)/2 * [1-h2((1+p/2)^2/(2(1+(p/2)^2)))], U=L_q+E.

Thus0<=U<5/8, with no conversion omitted. For completeness the original eligibility uses H0=4-(9/8)log3<3, J_A=2kp+3rho m/4 and c<93/64+rho mH0/2. The last bound follows directly from

L_B=eta(beta^2)+(mH0-eta(mu^2))/4+(1-mu^2)/2 <= mH0/4+3/2,
H(P)=eta((1-p)^2)-eta(p^2)+4kp+2rho L_B,
c=H(P)+1-p^2 log((1+p^2)/p^2), eta(t)=t log(1/t).

Indeed eta((1-p)^2)<3p, p<rho/2, and (2k+9/2)2^-k<=29/64 for k>=5 (the expression decreases with k). Consequently c<1+(4k+3)p+3rho+rho mH0/2<=93/64+rho mH0/2. This gives the original root margin4I-CE>291/128; also the core is rate4 eligible and the original unused half-bank S=2-2p+J_A-c/2>159/128. These were accepted independently by A016 and are rechecked on every frozen width. The local failure below does not start from an ineligible source.

2. Exact rowwise inherited likelihood. The seed squared Fourier law is9/16 atempty and1/16 at each of seven nonempty frequencies. Erasing one of its coordinates gives projected law(5/8,1/8,1/8,1/8) on its other two coordinates. Each physical outcome1, however, makes that seed the constant+1. Thus the actual terminal has zero Fourier frequency on all2r surviving killed-block coordinates, whereas the ORIGINAL projected reference assigns a factor d=(5/8)^r there.

Let the unqueried seed frequency be t, and write e_u,e_v for the remaining u/padding frequencies. The projected squared coefficients of B=(1-G_m)/2 are exactly

bbar(T)=P_G,projected(T)/4+(1-2mu)point_empty(T)/4.

On the actual support, where all killed-block frequencies arezero, put b_t=[d P_g3(t)+(1-2mu)1_(t=0)]/4. Then the exact original q-erased, tensor-erased core reference on that support is

Q_c(e_u,e_v,t)=[rho^2 b_t+(1-2p)1_(e_u=1,e_v=0,t=0)+1_(e_u=0,e_v=0,t=0)]/2.

This is a SLICE of a normalized ambient reference; it is not renormalized. All other reference atoms remain as ghosts. Ambient normalization follows from sum bbar=beta, sum projected core P=2rho beta+1-2p=1 and the added point mass. The outer full reference remains Q_c/16+point_empty_data/4 at each gate frequency.

3. Unbounded negative complete terminals. At the distinguished history G becomes the one remaining g3, so A is now the point event on k+3 bits. Write a=rho/8. Both q signs have the same core squared law: mass(1-a)^2 at{u}, and a^2 at every other frequency of the k+4 effective core bits. The other2r coordinates are physically irrelevant. Their gate/mask Fourier interference is retained in the full F spectrum. Both complete full-code costs are identical because the supplied gate reference is uniform; the two influences differ:

4I(F_terminal)=6+(2k+4-sign_q)a.

Consider ONLY the rows with nonempty live-seed frequency. There are seven live choices,2^k padding frequencies, two u sectors, four mask frequencies and two gate frequencies. Each full true squared coefficient is rho^2/1024; each full original-reference atom is rho^2 d/2048. Their total true mass is7rho/64. Every other full atom has nonnegative code length and is kept, so

CE_terminal >= (7rho/64)log[2048/(rho^2 d)]
> (7rho/64)r log(8/5).

Therefore, since U>=0, BOTH complete signed profiles obey

4I-CE-U <= 6+(2k+5)rho/8 -(7rho/64)r log(8/5),

which tends to minus infinity at any fixed k. For an explicit exact witness choose k5,r4096,m4097. Since(8/5)^2>2, the selected rows alone cost strictly more than7 bits. Both4I are at most6+15/256. Hence BOTH reserves after the SAME U are<-241/256. The original Boolean dimension is12301, the precleanup terminal ambient dimension8204 and its actual function has only12 effective variables. No exponential table is allocated for this witness. Exact intervals give full CE about12.990925 and signed reserves about-7.02531,-7.01750; these decimals are illustrations, not certificates.

The complementary histories are not deleted. For every one of the2^r seed-outcome strings and both q outcomes the code is the same supplied frequency marginal, the physical reach is2^(-r-1), and full true terminal cost/influence are retained. Literal small cases verify the entire physical ledger, not only the distinguished branch. The exhibited negative history has exponentially small reach. This disproves the unregistered extension that every intermediate history remains locally eligible. It does NOT contradict A016's stated fixed-subset averaged theorem, nor imply any unbounded H/I: the actual terminal function is fixed while only its inherited reference changes with r.

4. Exact zero-influence cleanup. At the distinguished history each killed seed is already constant+1. Query BOTH its remaining physical coordinates. Both outcomes give identical actual functions, hence each cleanup coordinate has physical influencezero. Their reference frequencies must nevertheless be marginalized. Summing the complete projected seed law changes its empty-frequency factor from5/8 to1; after all2r cleanup queries the row formula above has d=1, with the SAME original p,mu and the SAME U. It is not a new conditional lift or bank. Every one of the2^(2r) cleanup histories has the identical true function and identical original-reference marginal; their conditional reaches2^(-2r) sum toone.

For the restored core reference Q_c^clean and the actual terminal spectrum P_a, Q_c^clean>=P_a/4 atomwise. At nonempty live frequency equality Q_c^clean=P_a/2 holds. At zero live frequency away from{u}, b_0=(25/16-2mu)/4>=9/64 because mu<1/2, so the bound is immediate, with an extra positive point atempty. At{u}, Q_c^clean>=(1-2p)/2>(1-rho)/2>=31/64>P_a({u})/4. This proof accounts for all atoms; after cleanup the effective reference is normalized, without a support-slice renormalization.

Thus CE(P_a,Q_c^clean)<=H(P_a)+2. The full supplied outer code obeys CE_F<=CE_core/2+3 by its actual latent mixture of the nonconstant data law and its constant component. This is a complete-code upper bound, including their coincident Fourier support and gate interference. It follows either from the data marginal and the log-sum inequality, or directly from the uniformly coded gate and the two latent mixture components. Since

P_a=(1-2a)point_{u}+2a Uniform_(2^(k+4)),
H(P_a)<=h2(2a)+2a(k+4).

Therefore the smaller of the two full signed profiles BEFORE U is at least

2+(k-1)a-(1/2)h2(2a)>15/8.

Here2a<=1/128<1/32, h2 increases up to1/2 and h2(1/32)<1/4, the latter exactly certified by31^31>2^152. Subtracting the SAME U<5/8 leaves>5/4 at every complete cleanup terminal. Exact witness reserves are about2.46811 and2.47593. For any supplied Q the exact physical transition is average W_child=W_parent-4Inf_i+L_i with L_i=sum P(e,T)log[Q'(T)/Q(e,T)]>=0. Every cleanup Inf_i iszero, so the repaired reserve is supplied by the released inherited ghost cost, not by invented selector influence or a refreshed source.

First unsupported universal line: construct a stopping policy or source potential that can always perform an analogous inexpensive cleanup when branch equalities are approximate, interacting, or leave no exactly irrelevant coordinate. This family supplies an exact counterexample to unconditional local eligibility AND an exact repair, not a universal policy. A016's initial four/eight terminals and fixed-subset averages remain valid at their stated scope.

## executed validation with domain, arithmetic, commands and outputs

FROZEN_SPEC.json was written before any search. CLEANUP_EXTENSION_SPEC.json and ROOT_ELIGIBILITY_EXTENSION_SPEC.json preceded the respective extensions. Frozen compressed cases are k5,r1,4,16,64,256,1024,4096, with both q signs, the exact original reference, original U and cleanup profile. The r1 formula case is below the theorem's m>=4 range and validates only the algebra. Literal tables use k1,r1 andr2, original dimensions12 and15: they independently build the ORIGINAL Boolean function and all original Fourier/reference atoms, physically restrict both q outcomes and every seed-outcome history, compare the support slice to the compressed row formula, verify exact projected true laws and all physical influence telescoping, and check the complete signed CE transition with all complementary histories. They also verify every cleanup coordinate is actually irrelevant and that full original-reference marginalization equals the derived cleaned code.

The arithmetic helper is the read-only A020 stage7 checker, hash-bound in SOURCE_RECEIPTS; no importing bytecode is written to its directory. Integer Walsh transforms and Fraction arithmetic give exact coefficients, physical edge influences and reference identities. Logarithms use100-bit outward dyadic bounds: range reduction to[1,2),48 terms of2 sum z^(2j+1)/(2j+1), tail at most2 z^97/[97(1-z^2)], and separately enclosed ln2. Signs and rational thresholds use interval endpoints. Saved intervals are outward rounded again to100-bit dyadics; this changes no internal calculation. Interval overlap checks are consistency checks; exact Walsh identities and the displayed analytic algebra prove equalities.

Initial pilot passed2119 assertions. The first full run hit Python's4300-digit STRING conversion limit while saving U at r4096; no mathematical assertion failed. out/FIRST_FAILURE.txt preserves the failure and repair. Output now saves bounded dyadic endpoints and symbolic p rather than printing its huge rational numerator. The cleanup pilot passed2211 assertions in2.548seconds. The final checker command is `python -X utf8 code/check.py`; its exact counts and elapsed time are recorded below from out/CHECK.json. No floating-point result is used as a proof.

FINAL_CHECK_RECEIPT

The memory estimate is95MB, below the300MB admission threshold; no large job or compiler was started, and no memok waiver is asserted. Latest read compute snapshot was statusok,3633MB physical availability,8651MB commit availability,39.4GB disk; current jobs from other owners remain untouched. No GPU, window, detached job, git, remote compute, external message, research brain write or other-agent mutation is used. Research writes are only in A020. No formal proof assistant check is claimed. Both new mathematical statements have analytic proofs and exact bounded validation, with independent review pending.

## proof dependencies and changed downstream conclusions

The same-reference family and old-U interface come from A020 stage7 and are reconstructed algebraically here. A016 accepted that earlier admission no-go; this run consumes its replacement full-reserve boundary. The present local no-go and cleanup theorem do not depend on the numerical success of A016's checker or any unproved FEI inequality. No part of A016-FULL-SIGNED-TENSOR-PADDING-TRANSFER@1 is refuted at its explicit short-history/averaged scope. Do not change that claim to an all-history invariant: the new explicit original-reference witness invalidates that extension. Likewise the original half-bank no-go remains true; zero-influence cleanup repairs the full physical code, not the disproved admission inequality.

The mechanism changes from attempting a pointwise full-reserve invariant to quotienting or querying physically irrelevant but spectrally ghost-bearing coordinates before assessing local source eligibility. Such cleanup cannot simply be assumed available in a general interacting selector. Full H/I on these actual terminal functions is constant in r, so the new unbounded code cost is not an FEI counterexample. Claim DAG: first new claim depends on the original coefficient interface; cleanup uses that same algebra and its own atomwise proof. Both source-complete pending new claims are the stage's two-candidate limit.

## one next mathematical action and independent reviewer

Prove or refute a cleanup-closed stopping potential: after a history, erase all exactly irrelevant physical coordinates in the supplied reference before applying a reserve test, then query one genuinely relevant coordinate while retaining all original physical reaches and old U. The first test should replace one killed constant seed by a nearly constant interacting branch, where cleanup now has nonzero influence. A016/A019 should independently reconstruct the7rho/64 row mass,5/8 projection factor and explicit k5,m4097 local failure; A018/A090/A091/A094 should challenge the zero-influence repair and its approximate-equality extension. This is source-bound handoff only, not a sent message or claimed review receipt.

## actual persistence receipts or precise save blocker

All four protocol files, frozen specs, checker, failure note, pilot/full outputs and source hashes are local to this new A020 run. STATUS remains exactly two lines; WORKLOG is appended and LEARNED records the two exact statements. out/PERSISTENCE_RECEIPTS.json records byte hashes and sizes, exact protocol schemas, JSON parsing, claim hashes and identical PROGRESS/PACKET_DELTA. Its local readback is verified after writing. Supervisor adoption, independent acceptance, mirror verification and downstream use remain pending; no GitHub save is claimed. Brain self-care remains degraded/unverified for stale personal owner/state notes, independently of the exact research certificates.

## Universal bridge

This stage moves C024 history transfer and C019 stopping-tree payment by closing a new false local invariant on the SAME supplied eligible source: at k5,m4097 an actual history makes both full signed original-reference reserves less than-241/256 despite retaining U, so arbitrary-history eligibility cannot follow from A016's averaged theorem. It also proves an exact same-reference repair: query2r physically irrelevant ghost coordinates at zero influence and retain>5/4 after that SAME U at every cleanup terminal. The remaining universal step is to pay cleanup when no exact irrelevant coordinate exists and to keep averaged stopping profiles honest. NEXT is the shortest route to a universal bridge because it tests the precise missing ownership operation under approximate branch equality, rather than repeating a finite selector class or the refuted admission.
'''
report=report.replace('FINAL_CHECK_RECEIPT',f"Final run: PASS, {check['assertions']} exact assertions;7 compressed two-sign profiles,7 cleanup two-sign profiles,7 original-source eligibility checks and2 literal complete-history cases; elapsed {check['runtime_seconds']} seconds.")
write(R/'REPORT.md',report)
progress=dict(protocol_revision=P['revision'],run_id=R.name,stream='B04',packet_id='A020',gap_id='G-LOWSEL-COLLISION-SAME-REFERENCE-HISTORY-BANK',attempt_id='A020-stage8-rare-history-ghost-cleanup',method='Exact inherited row projection; actual physical rare history; original Q/U; zero-influence ghost cleanup',mathematical_delta='All-history local full signed eligibility refuted by actual k5,m4097 history; exact zero-influence cleanup restores >5/4 after same old U. Averaged payment remains open.',deliverable_status='COMPLETE_LOCALLY_SAVED; INDEPENDENT_REVIEW_AND_SUPERVISOR_MIRROR_PENDING',mathematical_status='TWO_SCOPED_CLAIMS_PROVED_LOCALLY; FULL_FEI_OPEN',claim_versions_used=['A020-UNBOUNDED-NONFLAT-ADMISSION-NOGO@1','A016-FULL-SIGNED-TENSOR-PADDING-TRANSFER@1','A016-REVIEW-A020-UNBOUNDED-ADMISSION-NOGO@1'],claims_created_or_changed=[c['claim_id']+'@1' for c in claims],source_artifacts=[str(p) for p in sources],next_consumers=['A016','A018','A019','A090','A091','A094','B20'],next_action='Test cleanup-closed original-reference stopping potential when a killed seed is replaced by a nearly constant interacting branch, retaining all physical reaches and old U.',stagnant_substantive_attempts=0,blockers=['Full FEI unresolved','Independent review and supervisor mirror/adoption pending','No general guarantee of zero-cost cleanup for interacting near-equal branches','Brain self-care degraded/unverified: stale personal owner-model/state notes'],packet_ids=['A020'])
dump(R/'PROGRESS.json',progress);dump(R/'PACKET_DELTA.json',progress)
for obj,fields in [(progress,'progress_fields')]:assert set(obj)=={s.split(' (')[0] for s in P['required_per_run'][fields]}
for c in claims:assert set(c)==set(P['required_per_run']['claim_fields'])
for field in P['required_per_run']['report_fields']:assert '## '+field in report
assert read(R/'PROGRESS.json')==read(R/'PACKET_DELTA.json')
write(A/'STATUS.md','STATE: A020 stage8 saved: SAME-Q/U full reserve fails on actual rare history (both <-241/256 at k5,m4097); zero-influence ghost cleanup restores both >5/4. Exact checks PASS; review pending; FEI OPEN.\nNEXT: Test cleanup-closed stopping potential on nearly equal interacting branches; retain original Q, U and all physical reaches. A016/A019 review ghost row mass and cleanup; A018/A094 challenge approximate repair.\n')
stamp=datetime.datetime.now(datetime.timezone.utc).isoformat()
with (A/'WORKLOG.md').open('a',encoding='utf-8') as f:f.write(f'\n{stamp} stage8 {R.name}: consumed A016 stage8 rather than repeat saved NEXT. Derived exact5/8 ghost projection per killed seed, actual rare-history unbounded negative full reserve, explicit k5,m4097 both <-241/256 after same U. Cleanup erases2r irrelevant coordinates at zero influence, restores>5/4 both signs. {check["assertions"]} assertions PASS, {check["runtime_seconds"]}s. Serialization4300-digit output failure repaired by outward saved dyadic bounds, no math assertion failure. Full FEI OPEN; review/mirror pending; self-care stale personal notes.\n')
with (A/'LEARNED.md').open('a',encoding='utf-8') as f:f.write('\nStage8 durable facts: a supplied eligible Q need not preserve local full4I-CE-U under long actual restrictions. On g3 product, conditioning first bits1 kills seeds physically but original projected seed law keeps empty mass5/8. Leave one seed live: selected full rows mass7rho/64 have original Q atoms rho^2(5/8)^r/2048; CE grows linearly in r, actual I constant. k5,r4096 gives both signed reserves<-241/256, without refuting averaged fixed-subset payment or FEI. Query remaining killed-block bits: actual influencezero, original reference projection factor becomes1 and atomwise Qcore>=Ptrue/4 restores complete reserve>5/4 after sameU. Before reserve admission, distinguish irrelevant physical bits from their inherited spectral ghost mass. Universal approximate/interacting cleanup still unpaid.\n')
files=sorted([p for p in R.rglob('*') if p.is_file() and p.name!='PERSISTENCE_RECEIPTS.json'])
for p in files:
 assert p.stat().st_size<20_000_000
 if p.suffix=='.json':json.loads(read(p))
receipt={'status':'PASS','at_utc':stamp,'schemas':'exact protocol fields verified','report_fields':'all seven exact headings plus terminal Universal bridge','claims':'hashes compact sorted statement/hypotheses; review pending','packet_delta':'byte-identical PROGRESS','local_only':True,'files':[{'path':str(p.relative_to(R)),'bytes':p.stat().st_size,'sha256':sha(p)} for p in files]}
dump(R/'out/PERSISTENCE_RECEIPTS.json',receipt)
for x in receipt['files']:assert sha(R/x['path'])==x['sha256']
assert len(read(A/'STATUS.md').splitlines())==2
print(json.dumps({'status':'PASS','checks':check['assertions'],'claims':len(claims),'files_hashed':len(files),'mirror':'PENDING','full_FEI':'OPEN'}))
