from pathlib import Path
import json,hashlib,copy,re,datetime
R=Path(__file__).resolve().parents[1];A=R.parents[1];BASE=R.parent/'20261023T110044Z-account03-A099-candidate-assembly'
def get(p):return json.loads(p.read_text(encoding='utf-8'))
def put(n,x):(R/n).write_text(json.dumps(x,indent=2,ensure_ascii=False)+'\n',encoding='utf-8')
def sha(p):return hashlib.sha256(p.read_bytes()).hexdigest()
main=get(R/'out/EXACT_AUDIT.json');pilot=get(R/'out/PILOT.json');spec=get(R/'out/FROZEN_SPEC.json')
assert main['status']==pilot['status']=='PASS'
assert main['lifted_trees']==300 and main['geometric_transactions']==66
assert main['seconds']<180 and pilot['seconds']<55
assert sha(R/'code/check.py')==spec['checker_sha256']
assert sha(R/'code/prior_exact.py')==spec['helper_sha256']
receipts=get(R/'out/SOURCE_RECEIPTS.json')
for x in receipts:
 p=Path(x['path']);assert sha(p)==x['sha256']
 who=next(s for s in ['A085','A096','A003','A097'] if '/'+s+'/' in p.as_posix())
 q=R/'out'/f'{who}_{p.name}';q.write_bytes(p.read_bytes());x['copy_sha256']=sha(q)
put('out/SOURCE_RECEIPTS.json',receipts)
old=get(BASE/'CLAIMS.json');claims=copy.deepcopy(old)
selected=[('A085','A085-ARBITRARY-CORE-ZERO-CREDIT-DEPTH-OBSTRUCTION','lem:v10lift'),
 ('A096','A096-ISOSPECTRAL-TARGET-GEOMETRIC-ACCOUNT','thm:v10geo'),
 ('A097','A097-NECESSARY-FLOOR-ADMISSION-SAME-ORIGINAL-OWNER','lem:v10floor'),
 ('A003','A003-MATCHED-DEFERRAL-INFLUENCE-COMPRESSION','thm:v10rate')]
originals=[]
for who,cid,label in selected:
 src=next(c for c in get(R/'out'/f'{who}_CLAIMS.json') if c['claim_id']==cid)
 c=copy.deepcopy(src);originals.append(src)
 if who=='A085':
  for producer in ['A096','A097']:
   other=next(x for x in get(R/'out'/f'{producer}_CLAIMS.json') if x['claim_id']==cid)
   assert other['exact_statement']==c['exact_statement'] and other['statement_sha256']==c['statement_sha256']
   for review in other['review_records']:
    if review not in c['review_records']:c['review_records'].append(copy.deepcopy(review))
 c['review_records'].append(dict(reviewer='A099',verdict='HOLDS_AT_EXACT_STATED_SCOPE',
  source_statement_sha256=c['statement_sha256'],source_claim_copy=f'out/{who}_CLAIMS.json',
  reconstruction=f'STAGE10_ADDITIONS.tex, label {label}; own code/check.py and out/EXACT_AUDIT.json',
  independence='Independent coefficient/complete-ledger proof and rational fourth-power representation; no source-author checker imported or run; no substantive repair supplied.',
  scope='Exact supplied-source or declared finite-core class scope only. No universal initial source pricing, FEI proof, universal necessity or full-chain audit acceptance.'))
 c['status']='INDEPENDENTLY_RECONSTRUCTED_HOLDS_AT_EXACT_STATED_SCOPE';claims.append(c)
assert claims[:len(old)]==old
assert len({(c['claim_id'],c['version']) for c in claims})==len(claims)
put('CLAIMS.json',claims)
annex=(R/'STAGE10_ADDITIONS.tex').read_text(encoding='utf-8')
text=(BASE/'CANDIDATE_MANUSCRIPT.tex').read_text(encoding='utf-8')
assert text.count('\\end{document}')==1
text=text.replace('\\end{document}',annex+'\n\\end{document}')
assert '?' not in annex
(R/'CANDIDATE_MANUSCRIPT.tex').write_text(text,encoding='utf-8')
dag=get(BASE/'out/PROOF_DEPENDENCIES.json')
nodes=dag['nodes'];ids={x['claim_id'] for x in nodes}
for who,cid,label in selected:
 c=next(x for x in claims if x['claim_id']==cid)
 deps=['A085-ARBITRARY-CORE-ZERO-CREDIT-DEPTH-OBSTRUCTION'] if who in ['A097','A003'] else []
 nodes.append(dict(claim_id=cid,version=1,proof_dependencies=deps,tex_label=label,statement_sha256=c['statement_sha256'],scope='Independent complete reconstruction at unchanged exact source scope'))
 ids.add(cid)
lookup={x['claim_id']:x for x in nodes};done=set();active=set()
def visit(i):
 if i in done:return
 assert i not in active,('cycle',i)
 active.add(i)
 for d in lookup[i]['proof_dependencies']:
  key=d['claim_id'] if isinstance(d,dict) else d
  assert key in lookup,('missing dependency',key);visit(key)
 active.remove(i);done.add(i)
for i in lookup:visit(i)
dag['v10_scope']='No new universal inference. Prior47 nodes unchanged; four source-bound theorem nodes added. A097 recipe probabilities explicitly derived here, no unreviewed A083 payment theorem imported.'
put('out/PROOF_DEPENDENCIES.json',dag)
newnames=[cid+'@1' for _,cid,_ in selected]
progress=get(BASE/'PROGRESS.json')
progress.update(run_id=R.name,attempt_id='A099-assembly-v10',
 method='Independent all-scope reconstruction and source assembly: nullspace depth, geometric ancestor normalizer, declared-floor admission, entropy/influence ledger separation',
 mathematical_delta='Four exact source statements integrated unchanged and independently reconstructed. Arbitrary-core zero-credit depth does not price its source; all terminal targets cost ancestor KL PLUS -logZ; declared floor paid from explicit original finite-core35/4 with reserve>77/32; free deferral preserves original entropy capacity but SAME current-influence compression is FEI(K)-equivalent. No universal FEI improvement.',
 deliverable_status='COMPLETE_SINGLE_SOURCE_PROTOCOL_AND_SCOPED_RECONSTRUCTIONS',
 mathematical_status='FOUR_NEW_SCOPED_RECONSTRUCTIONS_FULL_FEI_OPEN',
 claim_versions_used=[dict(claim_id=x['claim_id'],version=x['version']) for x in nodes],
 claims_created_or_changed=newnames,
 source_artifacts=['CANDIDATE_MANUSCRIPT.tex','STAGE10_ADDITIONS.tex','CLAIMS.json','out/SOURCE_RECEIPTS.json','out/PROOF_DEPENDENCIES.json','out/EXACT_AUDIT.json'],
 next_consumers=['A003','A050','A079','A085','A094','A096','A097','B20'],
 next_action='A050/A011/A097 specify a useful arbitrary-core compatible continuation class and prove its actual reached full conversion cost fits SAME unused original margin, or supply a noncircular O(I(core)) initial capacity. A085/A094 independently challenge the integrated chain; two complete-chain audits remain pending.',
 stagnant_substantive_attempts=0,
 blockers=['Universal arbitrary-core influence-priced initial reference remains unproved','Paid declared-floor family is finite-core/class-relative, not universal','Two independent integrated full-chain reconstructions pending','PDF/Lean not built; remote supervisor mirrors unverified','Brain self-care degraded/unverified; stale personal-context notes are not proof premises'],packet_ids=['A099'])
put('PROGRESS.json',progress);(R/'PACKET_DELTA.json').write_bytes((R/'PROGRESS.json').read_bytes())
report=f'''# A099 v10: candidate assembly at the zero-credit source interface

## exact target, quantifiers, hypotheses and units

Assemble the strongest fully supported source, retaining universal conjectures until two independent entire-chain audits close them. This stage reconstructs four unchanged all-parameter scoped claims: arbitrary-core parity deferral, arbitrary full-target isospectral geometric accounting, sharp declared-floor admission with a supplied finite-core payer, and original entropy capacity versus remaining-influence allocation. Physical cubes uniform; Boolean values plus/minus1; entropy/CE/KL bits. Complete references, reference-only mass, both outcomes, all actual reaches and previous debits are retained. Full FEI OPEN; no new universal constant or unbounded-H/I family.

## sources actually read, revisions and theorem locators

Fresh BOARD snapshot written2026-10-23 13:18UTC, own v9 STATUS and B20 STREAM_NOTES v2 (2026-10-11); full execution protocol revision2026-10-11-execution-v2 and machine AGENTS. The owner deadline14:49UTC overrides the archived protocol date. Prior campaign registries, plan, supplements and CP1252 paper exports were read in preceding stages and remain the v9 baseline; they were not reread as a fresh whole-campaign audit. No new external literature claim is used.

Current complete proofs actually read and copied byte-identically with pinned original hashes: A085 run20261023T112613Z PROOF1--5; A096 run20261023T115236Z DERIVATION1--4; A097 run20261023T121505Z PROOF1--5; A003 run20261023T121547Z DERIVATION1--5. Their REPORT/CLAIMS sources are in out/SOURCE_RECEIPTS. A097's DERIVATION locator did not exist; the correct PROOF.md was then read. Author evidence is distinguished from A099's own reconstruction. A085's unchanged A096/A097 review records are preserved, not counted as full-chain audits. Board-only reviews from other agents are leads, not imported acceptances.

## complete derivation or exact first unsupported line

STAGE10_ADDITIONS.tex contains complete proofs and is literally inserted in the standalone CANDIDATE_MANUSCRIPT.tex. Four claims keep exact original IDs, versions, hypotheses, statements and hashes. Parity-block coefficient isometry preserves every core spectral/reference probability, including prepaid mismatch. Any fixed query depth can therefore have zero phase/JS/occupancy/ghost credit despite arbitrary core entropy. Matched ALL-bin refunds are zero; arbitrary-source finer calibration may release existing KL and is explicitly excluded from the zero-refund conclusion. Minimal entropy-bearing seed and positive full conversion formula are independently derived analytically; the original producer census is not represented as ours.

A096's general finite isospectral tree is exactly an ancestor reference plus its normalizer: Delta=D(P||Rstar)-D(P||Q0)-log2 Z and -log2 Z=mean FULL KL(transported Rstar||Qleaf). All reference-only mass is retained. At reach rho affordability is rho*Delta<=the ACTUAL unused original U. The four-atom Boolean witness has Rstar=P but positive log2(4/3)/2 bill. Omitting this normalizer is false; no named correct producer theorem is refuted.

A097's log-sum minimizer prices EVERY reference in the DECLARED fixed-vacuum event-floor class. The entropy-bearing core family needs cost(3/32)log2(27/25) for admission, despite arbitrarily long zero-credit prefixes. SAME fixed original35/4 pays after supplied eligible old booking<=1/4 with reserve>77/32. Necessity is class-relative. Ordinary inherited continuation remains possible. The source has at most64 atoms and entropy<=6; this is an explicit finite-core price, not an arbitrary-core FEI admission. The general floor proof includes complete normalization and its attained optimizer.

A003's frontier identities distinguish unchanged K L I(core)-H(core) from the stronger earmarked residual K J_frontier-H(core). Compressing any cheaply admitted matched lift to the latter core-scale endpoint at fixed K is EXACTLY FEI(K)-equivalent. The majority-three K1 guard has original residual1 and influence-earmarked endpoint-1/2. It refutes that fixed-rate heredity shortcut, never full FEI. No fresh theorem ID is invented for these existing claims.

FIRST UNSUPPORTED UNIVERSAL LINE: construct a dimension-independent O(I(core)) initial complete source/capacity for arbitrary Boolean cores, or a genuinely useful compatible arbitrary-core admission with full reached conversion cost bounded by its ACTUAL unused ORIGINAL margin after every booking. Avoiding an optional reset does not price that source. The prior four universal leaves remain explicit conjectures, and BOTH full-chain audits remain pending.

## executed validation with domain, arithmetic, commands and outputs

Frozen out/FROZEN_SPEC.json precedes both runs and pins own checker plus byte-identical own v9 exact-log helper. No source-author checker imported or executed. Commands: python -B -X utf8 {R.name}/code/init.py; then code/check.py --pilot; then code/check.py (actual commands used runs/{R.name}/ prefix from A099). Pilot PASS: {pilot['exact_assertions']:,} assertions in{pilot['seconds']:.6f}s on22 labelled cores dimension0..2 at L2. Main PASS: {main['exact_assertions']:,} assertions in{main['seconds']:.6f}s,300 lifted trees,4492 physical nodes,2096 legal query nodes,66 geometric target transactions,180 ghost-bearing leaf occurrences and6 signed wrapper parameter cases. Pilot and main counts are separate, not pooled.

Main domain: all278 labelled cores dimension0..3 at L2 plus all22 dimension0..2 at L3. A complete outcome-sensitive legal unwrapping tree is checked for each; every legal adaptive tree/all-dimension quantifier is supplied by proof, not enumeration. Direct physical edges independently verify influences; integer Walsh/Fraction probabilities verify spectra, both physical children, support multiset, entropy equality and exact influence drop. Geometric tests use actual L3 lifts of all22 small cores, three distinct full-reference recipes and unequal stopping reaches1/2,1/4,1/4 when applicable. Targets have entries v_l(s)^4/normalizer_l; weighted geometric pullback gives rational Rstar proportional to product v_l(s)^k_l. Hence Z^4 and its <=1 certificate are exact rational/integer powers, and every full CE/KL identity is exact prime-log cancellation. Ghost leaf mass is never dropped. Singleton leaf endpoints included. No irrational root approximation or floating sign verdict.

The6 wrapper cases are both signs and L1,2,3. Literal full root Boolean spectra/physical influence counts are computed at L1,2; L3 and allL source/funding identities are analytic from the unchanged core law. The seed floor cost and positive normalizer witness are exact log identities with integer ratio signs. No claim of literal full-root L3 enumeration, every adaptive policy enumeration, fresh producer-count reproduction, formal Lean verification or PDF compilation. Estimated150MB, actual peak unmeasured; pilot below55s, main below180s, no expected>300MB job or memok-dependent admission. No automatic dimension increase, GPU, detached job or unrelated workload change.

## proof dependencies and changed downstream conclusions

The previous27 claim records remain unchanged; four source claims give31 total. Prior47 dependency nodes are retained; four exact-source nodes give51. The complete DAG is checked acyclic with resolved dependency IDs. TeX labels/references and standalone inclusion are checked; four conjectures remain. A097's concrete recipe law is derived directly, without importing an unreviewed A083 tensor-payment theorem or unknown upstream history. A099 supplies independent no-repair scoped HOLDS records, preserving contributor/audit independence. Different local claim reviews do not constitute either required integrated audit.

Compared with v9 the positive initial phase/bin/JS/discrepancy suppliers remain valid, but the general zero-credit boundary now contains arbitrary-core entropy, and terminal compression retains an exact additional disagreement bill. A paid necessary DECLARED admission is now concrete; universal source pricing and compatible general-core funding remain unpaid. Universal constant improvement: ZERO. The shortest route has moved from asking for any optional positive reset to finding the actual useful arbitrary-core admission/capacity bound.

## one next mathematical action and independent reviewer

A050/A011/A097 must give an arbitrary-core, policy-compatible class whose required reached cost fits the actual original unused source margin, or establish a noncircular O(I(core)) capacity at the quotient frontier. A085/A094 should independently reconstruct the entire assembled dependency chain, with particular challenge to normalizer loss, class-relative necessity, old bookings and current-influence repricing. These are saved source-bound next consumers, not sent messages or claimed acceptances.

## actual persistence receipts or precise save blocker

Four exact-schema protocol artifacts, standalone source, complete stage proof, own portable checker/helper, frozen domain, pilot/main/witness outputs, original byte-pinned source copies, acyclic dependency manifest and validation/readback receipts are local to this A099 run. PACKET_DELTA is byte-identical to PROGRESS with packet_ids[A099]. Rolling STATUS has two lines; dated WORKLOG/LEARNED append this result. Every artifact is under20MB. Local receipts verify actual bytes; supervisor copying, public release, remote mirrors and downstream adoption remain UNVERIFIED. No git, mail, other-agent edit, shared research index mutation, brain-store write or trading-path access.

Brain self-care is degraded/unverified: fresh wake owner-model99.7h,state-of-mind84.3h,dream35h stale; current personal-context continuity is affected, and those notes are not mathematical premises. No saved-source block remains.

Did: reconstructed four exact-scope claims and assembled v10. Stopped: no unrelated work. Left running: none of this stage's research jobs.

## Universal bridge

C024 history transfer and C020 complete-reference costs inside C019 now have a complete arbitrary-target ancestor normalizer bill, the arbitrary-core/all-depth zero-credit scope boundary, sharp class-admission paid from a real finite-core original bank, and an exact separation of free entropy deferral from FEI-equivalent influence compression. The universal improvement is zero: arbitrary-core O(I) initial capacity or a useful compatible admission paid by actual unused original margin remains the first unsupported line; C018 and full FEI remain OPEN. NEXT targets that precise source/quotient-frontier inequality because deeper phase searches, optional-reset tests, normalization-free compression and relabeling an old bank cannot discharge it.
'''
(R/'REPORT.md').write_text(report,encoding='utf-8')
protocol=get(Path('math-open-problems/reports/fei-2026-10-11/EXECUTION_PROTOCOL.json'))
fields=set(protocol['required_per_run']['claim_fields'])
assert all(set(c)==fields for c in claims)
pf={x.split(' (')[0] for x in protocol['required_per_run']['progress_fields']}
assert set(progress)==pf
assert (R/'PACKET_DELTA.json').read_bytes()==(R/'PROGRESS.json').read_bytes()
assert all('## '+h in report for h in protocol['required_per_run']['report_fields'])
for src,new in zip(originals,claims[-4:]):
 for k in ['claim_id','version','exact_statement','hypotheses','statement_sha256','contributors','proof_source','proof_dependencies']:
  assert src[k]==new[k],('changed original',src['claim_id'],k)
labels=re.findall(r'\\label\{([^}]+)\}',text);refs=re.findall(r'\\(?:eqref|ref)\{([^}]+)\}',text)
assert len(labels)==len(set(labels)) and set(refs)<=set(labels)
assert not re.search(r'\\(?:input|include)\{',text)
assert not re.search(r'Theorem~\\ref\{(?:lem|cor|prop):',text)
assert text.count('\\begin{conjecture}')==4
assert len(claims)==31 and len(nodes)==51
validation=dict(status='PASS',claim_records=len(claims),unchanged_baseline_claims=len(old),DAG_nodes=len(nodes),DAG_acyclic=True,
 tex_labels=len(labels),all_refs_resolved=True,standalone_source=True,universal_conjectures=4,
 full_FEI='OPEN',integrated_independent_audits='BOTH_PENDING',PDF='NOT_BUILT',Lean='NOT_CLAIMED',
 exact_main_assertions=main['exact_assertions'],remote_mirror='UNVERIFIED',scope='No universal price or necessity imported from supplied finite-core claims')
put('out/FINAL_VALIDATION.json',validation)
stamp='2026-10-23 stage20261023T131709Z'
(A/'STATUS.md').write_text('STATE: A099 v10 saved: four exact-source nullspace/normalizer/floor/deferral claims independently reconstructed;24,876 exact checks PASS;31 claims/51 DAG nodes;full FEI OPEN.\nNEXT: A050/A011/A097 price a useful compatible ARBITRARY-core admission from ACTUAL unused original margin or construct O(I(core)) initial capacity; A085/A094 audit integrated chain; both full-chain audits pending.\n',encoding='utf-8')
with (A/'WORKLOG.md').open('a',encoding='utf-8') as f:f.write(f'\n{stamp}: Read fresh board/lead/status; independently reconstructed A085 depth/core, A096 geometric normalizer, A097 class-floor original payer and A003 distinct entropy/influence ledgers. Pilot1558/main24876 exact assertions PASS (counts separate);300 lift trees/66 geometric transactions. Source31claims/51DAG,4conjectures. No universal gain; exact remaining initial-price/admission obligation saved. Both integrated audits and remote mirror unverified.\n')
with (A/'LEARNED.md').open('a',encoding='utf-8') as f:f.write(f'\n{stamp}: An arbitrary complete isospectral target history costs D(P||Rstar)-D(P||Q0)-logZ; -logZ equals weighted FULL target-disagreement KL and can be positive even Rstar=P. Fourth-power full targets make Rstar rational at dyadic reaches and certify Z^4<=1 exactly. All-depth parity deferral preserves arbitrary-core entropy/source CE, not a universal source price. Sharp floor class cost is t KL(Ber(a/t)||Ber(ell/t)); necessity is declared-class-relative. Free entropy deferral preserves original KLI-H; replacing the bank by current KJ_F-H is an additional FEI(K)-equivalent allocation. Never infer current-influence compression from zero entropy bills.\n')
files=[]
for p in sorted(R.rglob('*')):
 if p.is_file() and p.name!='PERSISTENCE_RECEIPTS.json':
  b=p.read_bytes();assert len(b)<20_000_000
  files.append(dict(path=str(p.relative_to(R)),bytes=len(b),sha256=hashlib.sha256(b).hexdigest(),readback=True))
put('out/PERSISTENCE_RECEIPTS.json',dict(status='PASS',files=files,remote='UNVERIFIED',readback='Every listed file read as bytes after saving; receipts file deliberately excludes itself'))
assert len((A/'STATUS.md').read_text(encoding='utf-8').splitlines())==2
print(json.dumps(validation));print('Persistence PASS:',len(files),'files read back; no research jobs left running.')
