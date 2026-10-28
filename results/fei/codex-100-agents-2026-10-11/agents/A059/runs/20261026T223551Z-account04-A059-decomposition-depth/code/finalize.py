from pathlib import Path
import json,hashlib,datetime
R=Path(__file__).resolve().parents[1];BASE=R.parents[1]
def write(p,s):p.write_text(s,encoding='utf-8')
def dump(p,x):write(p,json.dumps(x,indent=2,ensure_ascii=False)+'\n')
def sha(p):return hashlib.sha256(p.read_bytes()).hexdigest()
v=json.loads((R/'out/validation.json').read_text(encoding='utf-8'))
a=json.loads((R/'out/adversary.json').read_text(encoding='utf-8'))
assert v['status']==a['status']=='PASS'
proof=R/'PROOF.md';s=proof.read_text(encoding='utf-8')
note='For an entirely rational account use k=29/13>kappa, since 3^5<2^8 implies ell<8/5. Then 9/2-2k=1/26 exactly. Every transaction below remains valid with k replacing kappa, A=2k at q=1/2, and a retained original reserve at least (1/26)tI(g) plus its previously released cash. The validation and Lean source use this rational version.\n\n'
if note not in s:write(proof,s.replace('## 2. Two tickets',note+'## 2. Two tickets'))
claim_id='A059-PREPAID-TWO-TICKETS-AND-GEOMETRIC-STOPPING'
statement=('For every finite Boolean core G in the A059@2 coherent-source expected-resource interface, the SAME original core owner (9/2)cI(G), allocated before its first use, pays TWO adaptively selected further core queries per path after any already-paid admitted prefix, with arbitrary exterior/tag interleavings and all old debits/full terminals retained. It also pays any finite-depth selected core policy independently killed after each query with continuation probability q<=1/2, without a depth bound. The rational pending rate is k=29/13 per ticket, and A=k/(1-q) for killing; unused original source includes (1/26)tI(current core) plus historical releases at q=1/2. This is an expected-resource theorem with explicit mean-zero branch innovations, not pathwise subtraction-only cash or a full-core entropy payment.')
hyp=['finite uniform Boolean cubes; entropy bits','original coherent source and exterior escrow of A059@2','original core owner allocated BEFORE first use; no already exhausted account is retrospectively recreated','two-ticket policy has at most two selected further core queries per path','geometric policy uses fresh independent dummy coordinates irrelevant to F, actual continuation q<=1/2, and retains all killed siblings','all actual old core fees, coherent mean profiles and both complete terminal functions retained']
review='''# Independent reconstruction of A060 and A091 inputs

A060 universal one-query bound: HOLDS at the written scope. PROOF Section 1 reconstructs pivotal-product influence, edge isoperimetry with its factor 2, both entropy packet bounds, the two concavity intervals and the p>=1/2 boundary. The checker verifies all 804 physical coordinate cases on n<=3, with no symmetry quotient and exact signs. This is an author reconstruction by A059, independent of A060's implementation; no repair of the source is needed.

A091 one-shot 9/2 original-core source: HOLDS at its stated expected-resource scope. A pending influence ticket is harmonic after booking its released coordinate influence into UNUSED cash. Its single selected fee is bounded by its principal. It closes once; both full actual child profiles and historical debits remain. The new two-ticket refinement allocates within this source BEFORE either fee, rather than declaring that A091's already-closed ticket can be reused. A060's smaller one-shot owner is not claimed to pay two queries.

The original bank can be divided in advance because 9/2=2*(29/13)+1/26; log2(3)<8/5 is certified by 243<256. At q=1/2 the geometric bank equals the two-ticket sum. The scalar release, full wrapper profile identity and both terminal spectra are checked independently. Neither this review nor the new theorem pays an unrestricted complete core tree. External A091/A087 review of the new theorem remains pending.
'''
write(R/'REVIEW.md',review)
claims=[dict(claim_id=claim_id,version=1,exact_statement=statement,hypotheses=hyp,statement_sha256=hashlib.sha256(statement.encode('utf-8')).hexdigest(),contributors=['A059; universal one-query input reconstructed from A060','A091 original 9/2 source; A059@2 exterior escrow'],proof_source={'path':'PROOF.md','sha256':sha(proof),'validation':['out/validation.json','out/adversary.json']},proof_dependencies=['A059-EXACT-EXCESS-ESCROW-AND-CORE-OWNER-OBSTRUCTION@2','A060 universal one-query kappa bound: PROOF.md Section1 independently reconstructed','A091 ONESHOT_PROOF.md: original 9/2 core source','B17/A057 amplitude-pair JS inequality; Boolean cube edge isoperimetry'],review_records=[{'reviewer':'A059','scope':'author adversarial checks; not independent acceptance of new claim','verdict':'PROOF_WITH_EXACT_FINITE_CONTROLS'}],status='PROVED_AUTHOR_CHECKED_INDEPENDENT_REVIEW_PENDING',supersedes=[],refutes=['Dropping independent killing from this pending-potential transaction: actual m8 rare-tag witness; not FEI'],first_unproved_line='Remove compulsory stopping or influence-price terminal entropy decay for arbitrary cores from SAME unused original capacity.',next_consumers=['A057','A060','A091','A087','B12','B20'])]
dump(R/'CLAIMS.json',claims)
progress=dict(protocol_revision='2026-10-11-execution-v2',run_id=R.name,stream='B12',packet_id='A059',gap_id='G-A059-DECOMPOSITION-DEPTH',attempt_id='stage21-original-source-two-ticket-geometric-stopping',method='Independent one-query proof reconstruction, prepaid original-source splitting, nonnegative geometric transaction and exact full-spectrum controls',mathematical_delta='SAME A091 original9/2 owner pays TWO selected further core queries, plus arbitrary-depth independently-killed policies q<=1/2, with rational original reserve1/26 and full terminals. Original core source never renewed. Universal unrestricted terminal entropy remains unpaid.',deliverable_status='COMPLETE_LOCAL_ARTIFACTS',mathematical_status='LOCAL_STOPPING_THEOREM_PROVED_REVIEW_PENDING; FULL_FEI_OPEN',claim_versions_used=['A059-EXACT-EXCESS-ESCROW-AND-CORE-OWNER-OBSTRUCTION@2','A060 PROOF.md Sections1,3a universal one-query and handoff','A091 ONESHOT_PROOF.md original9/2 owner'],claims_created_or_changed=[claim_id+'@1','A060 universal one-query and A091 one-shot original-owner: A059 scoped independent HOLDS review'],source_artifacts=['PROOF.md','REVIEW.md','SPEC.json','AUDIT_SPEC.json','code/check.py','code/adversary.py','code/Key.lean','out/validation.json','out/adversary.json','out/helper_pin.json'],next_consumers=['A057','A060','A091','A087','B12','B20'],next_action='A091/A087 review two-ticket and geometric transaction; replace compulsory independent killing by a useful necessary arbitrary-core policy with paid terminal entropy decrease from the SAME original unused capacity. Do not retry the refuted no-killing influence-refresh rule.',stagnant_substantive_attempts=0,blockers=['External review of new stopping theorem pending','Geometric stopping retains unpaid core entropy; no unrestricted complete-core source established','Supervisor mirror/registry adoption unverified'],packet_ids=['A059'])
dump(R/'PROGRESS.json',progress);dump(R/'PACKET_DELTA.json',progress)
lean=(R/'out/lean.txt').read_text(encoding='utf-8') if (R/'out/lean.txt').exists() else 'Lean admission/result pending; no Lean certification claimed.'
lean_summary='Lean key-step attempt HELD: SETUP_UNVERIFIED because compute status was distressed or unknown (exit2). No Lean certificate is claimed; see out/lean.txt.'
if 'VERIFIED_TARGET' in lean:lean_summary='Key scalar release lemma Lean target verified; this certifies only the rational ledger implication, not the universal Fourier/entropy theorem. Receipt in out/lean.txt.'
report=f'''# A059 stage21: two original tickets and arbitrary-depth paid stopping

## exact target, quantifiers, hypotheses and units

For EVERY finite Boolean core in A059@2, refine A091's SAME original (9/2)cI(G) before first expenditure to pay TWO selected further core queries after any actually paid prefix. Also prove a stopping theorem with NO bound on depth under fresh independent continuation q<=1/2. Entropy bits; expected-resource branch innovations; all old costs, actual coherent means, siblings and full terminals retained. Full FEI OPEN.

## sources actually read, revisions and theorem locators

Execution protocol2026-10-11-execution-v2 read completely; current BOARD B12/B19/B20 entries and B12 STREAM_NOTESv2; own stage20 PROOF/REPORT/rolling files; A060 run20261023T132943Z PROOF Sections1-6; A091 run20261023T140242Z REPORT and ONESHOT_PROOF. Campaign/source-plan navigation and local paper locators refreshed; prior-stage baseline not reproved. Source pins in out/SOURCES.json; paper decoding details in out/paper_intake.json. Math recall returned restriction/Booleanity warnings, not a new proof premise. Legacy campaign dates differ from the current authorized continuation; no schedule or deadline was changed.

## complete derivation or exact first unsupported line

PROOF Section1 independently reconstructs A060's universal D_iH(g)<=kappa I(g), kappa=3-2/(1+log2(3))<29/13. Its pivotal-product isoperimetry and two concavity intervals include p0,p1, constants and irrelevant coordinates. A060 input and A091 one-shot source independently HOLDS at their written scopes; REVIEW.md records that verdict.

Sections2-3 give the new mechanism. Split original9/2 into TWO labelled29/13 tickets plus1/26 BEFORE use. Transport each still-pending ticket through already-paid core queries by influence conservation and separate unused releases. Consume one ticket at each selected new query, close it once, and retain the other. All branch mean innovations are explicit. This pays the necessary SECOND query targeted by A091, without recreating a closed owner or changing A060's smaller source.

The geometric variant reserves A=k/(1-q). After fee a=tD_iH(g), expected surviving pending principal is qAt(I-p_i). The actual unused release is r=AtI-a-qAt(I-p_i)>=qAtp_i>=0. Fresh independent physical dummy coins have zero entropy debit; both stopping outcomes remain. Arbitrary finite depth follows by the local transaction induction, with no limiting interchange. At q1/2, A=58/13<9/2 and original reserve is1/26. Product-AND2 cores in fixed m4 coherent wrappers have paths with N genuine positive-cost core queries for every N. They supply an explicit growing-depth family.

First unsupported line: remove compulsory killing or fund enough terminal entropy decrease on arbitrary cores from the SAME original unused capacity. Geometric stopping may retain almost all of a large core's entropy. This is a paid stopping mechanism, not a full FEI proof. A literal m8 bent-point rare-tag witness refutes dropping killing from the SAME influence-potential refresh (D_tag>A Inf_tag); it does not refute another potential or FEI.

## executed validation with domain, arithmetic, commands and outputs

Frozen SPEC saved before pilot/main; AUDIT_SPEC before adversary. Commands: python -B -X utf8 code/check.py --pilot; code/check.py; code/adversary.py. Pilot2582 assertions PASS. Main **{v['assertions']} exact assertions PASS** in {v['seconds']:.3f}s:804 coordinate cases on all n<=3 functions,7044 outcome-adaptive two-query policies,512 generic full-spectrum coherent core edges, complete stopped n2 trees at q0,1/4,1/2, and32 compressed growing-depth rows. BOTH full terminal spectra and exact profile debit are checked.

Independent audit **{a['assertions']} assertions PASS** in {a['seconds']:.3f}s: all{a['direct_functions']} n1..3 functions reproduced by direct character sums, independent edge influence normalization, Parseval, one actual9-bit rare-tag no-killing witness, and32 independent scalar recurrence controls. The initial spec's274 function-count label was an arithmetic typo (4+16+256=276); the all-n<=3 domain was unchanged, with no symmetry quotient or omitted function. These are author-independent computational paths, not an external reviewer. Finite controls support the written all-dimensional induction; no extrapolation proves it.

Arithmetic: Fraction Walsh, exact prime-log identities and32-term rational atanh enclosures with geometric tails. No floating sign decisions. The frozen spec originally described copying A060's180-bit helper; the actual pre-execution helper pin and scripts use the previous A059 exact prime-log helper instead. Original SPEC is retained unchanged; REPLAY_SPEC records the actual helper and arithmetic before an identical-domain pilot/main replay. Estimated140MB, no measured peak. No >300MB job, GPU, worker, window, detached task or automatic dimension increase. {lean_summary}

An initial paper-locator read failed UTF8 decoding on a genuinely non-UTF8 source; explicit cp1252 fallback and source encoding are recorded. No corrupted text was treated as mathematics. No mathematical checker failure was hidden.

## proof dependencies and changed downstream conclusions

Only the scoped one-query input and A059@2 exact excess interface are needed; no FEI assumption. A091's original9/2 source now supports two prepaid transactions and geometric stopping, within exactly the same original budget. A060's one-shot kappa budget is not asserted to double. All old exterior-only/full-core and no-refresh obstructions retain their original quantifiers. New combined claim awaiting A091/A087 independent review; full FEI OPEN.

## one next mathematical action and independent reviewer

A091/A087 reconstruct the prepaid split and the two-stage core/coin transaction. A057/A060 should target paid TERMINAL entropy decay or a useful necessary arbitrary-core policy from the current unused original capacity. Another one-shot renewal or unpriced complete-core allocation does not close that gap.

## actual persistence receipts or precise save blocker

Four protocol files, proof, source review, frozen specs, code and exact outputs saved locally in this run. Final schema/statement hash/full-file-size/readback checks in out/PERSISTENCE.json; STATUS two lines and rolling logs updated. Supervisor copy, registry adoption and mirror verification NOT_OBSERVED. No git, mail, messages, brain writes or other-agent edits.

Fresh wake warned personal-context model181h/state165.6h/dream38h stale; owner notified before relying on affected notes. Mathematical premises use saved proofs. Compute snapshot showed2GB free disk, with WindowsTerminal/ffmpeg/Claude among large holders; only small exact checks launched, no work stopped or throttled.

## Universal bridge

C019 stopping-tree payment and C024 history transfer advance from ONE original-core transaction to TWO after actual exterior admission exhaustion, and to finite stopping trees of arbitrary depth with independent continuation q<=1/2, all paid from the SAME original9/2 influence owner with reserve1/26 and both full terminals. The growing-depth product-AND2 core controls carry real positive query fees. What remains is terminal entropy: the stopping rule is optional and can leave a large arbitrary core unpaid. The shortest next route to full FEI is to supply useful necessary continuation or paid terminal entropy decay from actual unused original capacity; the new rare-tag witness rules out merely removing the coin while keeping this influence-refresh update.
'''
write(R/'REPORT.md',report)
state='STATE: Stage21 original9/2 core owner prepays TWO further queries and arbitrary-depth q<=1/2 stopped policies; reserve1/26; '+str(v['assertions']+a['assertions'])+' exact main/audit assertions PASS; external review pending; FEI OPEN.'
nextline='NEXT: A091/A087 review prepaid split/geometric transactions; pay useful necessary arbitrary-core continuation or full terminal entropy decay from SAME unused original capacity; no source renewal/no-killing refresh.'
write(BASE/'STATUS.md',state+'\n'+nextline+'\n')
entry='\n2026-10-27 stage21: Reconstructed A060 universal single-query input and A091 original-owner transport. SAME9/2 owner splits into TWO29/13 tickets and1/26 reserve BEFORE expenditure; pays two selected further core queries and arbitrary-depth independently-killed policies q<=1/2. Main'+str(v['assertions'])+' and independent audit'+str(a['assertions'])+' exact assertions PASS. Actual m8 rare-tag witness kills no-killing influence-refresh rule, not FEI. Both full terminals remain; terminal entropy decay still unpaid. New theorem external review pending.\n'
for name in ('WORKLOG.md','LEARNED.md'):
 p=BASE/name;old=p.read_text(encoding='utf-8') if p.exists() else ''
 if entry.strip() not in old:write(p,old+entry)
sources=[]
for path in [Path('BOARD.md'),Path('claude/B12/STREAM_NOTES.md'),BASE/'runs/20261023T130150Z-account03-A059-decomposition-depth/PROOF.md',Path('agents/A060/runs/20261023T132943Z-account03-A060-composition-sharpness/PROOF.md'),Path('agents/A091/runs/20261023T140242Z-account03-A091-composition-referee/ONESHOT_PROOF.md')]:
 sources.append({'path':str(path),'sha256':sha(path)})
dump(R/'out/SOURCES.json',sources)
protocol=json.loads(Path('math-open-problems/reports/fei-2026-10-11/EXECUTION_PROTOCOL.json').read_text(encoding='utf-8'))
assert set(progress)==set(x.split(' (')[0] for x in protocol['required_per_run']['progress_fields'])
assert set(claims[0])==set(protocol['required_per_run']['claim_fields'])
assert (R/'PROGRESS.json').read_bytes()==(R/'PACKET_DELTA.json').read_bytes()
assert len((BASE/'STATUS.md').read_text(encoding='utf-8').splitlines())==2
assert claims[0]['statement_sha256']==hashlib.sha256(claims[0]['exact_statement'].encode('utf-8')).hexdigest()
receipt=[]
for p in list(R.rglob('*'))+[BASE/x for x in ['STATUS.md','WORKLOG.md','LEARNED.md']]:
 if p.is_file() and p.name!='PERSISTENCE.json':
  assert p.stat().st_size<20*1024*1024
  receipt.append({'path':str(p.resolve()),'bytes':p.stat().st_size,'sha256':sha(p)})
dump(R/'out/PERSISTENCE.json',{'status':'PASS_LOCAL_READBACK','schemas':'EXACT_FIELDS','files':receipt,'independent_review':'PENDING','remote_mirror':'NOT_OBSERVED','timestamp_utc':datetime.datetime.now(datetime.timezone.utc).isoformat()})
print(json.dumps({'status':'COMPLETE_LOCAL','checks':v['assertions']+a['assertions'],'files_hashed':len(receipt),'FEI':'OPEN'}))
