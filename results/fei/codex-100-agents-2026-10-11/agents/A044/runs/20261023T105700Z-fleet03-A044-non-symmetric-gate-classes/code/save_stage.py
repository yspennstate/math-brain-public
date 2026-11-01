from pathlib import Path
import json,hashlib,copy

ROOT=Path(__file__).resolve().parents[1];AGENT=ROOT.parents[1]
def read(p):return json.loads(p.read_text(encoding='utf-8'))
def dump(p,x):p.write_text(json.dumps(x,indent=2,ensure_ascii=False)+'\n',encoding='utf-8')
def sha(p):return hashlib.sha256(p.read_bytes()).hexdigest()
main=read(ROOT/'out/CHECK.json');ind=read(ROOT/'out/INDEPENDENT.json')
assert main['status']==ind['status']=='PASS'
assert main['exact_assertions']==348673 and ind['exact_assertions']==329
assert main['helper_sha256']==sha(ROOT/'code/check_stage.py')
assert ind['helper_sha256']==sha(ROOT/'code/check_independent.py')
proofhash=sha(ROOT/'PROOF.md')
statement=('For every Boolean seed g under every finite interior independent product law, and independent selector X of arbitrary success probability e, activation F=1-X+Xg satisfies Delta_F=e Delta_g+Delta_o and J_F=e J_g+J_o+ln(4) C, where Delta_o=e(1-e)Var(g), J_o<=3ln(4)Delta_o sharply, and C=e^2 sum_T P_g(T)[j(e|c_T|)-j(e)-j(|c_T|)] has summand indices in {0,1}. The complete inherited reference retains both full terminal laws and satisfies KL_tree=KL_o+e KL_g, CE_tree^+=J_F-ln(4)C+n_o+e n_g, and KL_flat-KL_tree=ln(4)C+n_F-n_o-e n_g. For the actual activated AND2 seed g=-1+2yz at p_y=p_z=(1+t)/2 and e=1-2t, t=2^-m, m>=3, C/Delta_o=e(1+t)/(t(3+t))>=(6/25)2^m diverges. Moreover ln(4)C/L_g tends to one, while the signed flat/tree transfer tends to -[(3/4)ln3-(1/2)ln4]<0. Thus no absolute constant pays this carry from the fresh outer deficit alone. Independently, the exact activation entropy bound is E_o<=(4+ln4)Delta_o, sharp as e and a=(1-Eg)/2 tend to one. Genuine disjoint nested canalyzing decision-list gates on distinct variables therefore satisfy corrected E<=(4+ln4)(I-Var) at every product bias, with no depth or fan-in dependence; arbitrary-seed composition preserves max(C_seed,4+ln4). On the uniform cube the ordinary bit-entropy FEI constant is 2+4/ln2. These family bounds and the carry obstruction do not pay an arbitrary seed dyadic scale or prove universal FEI.')
hyp=['Actual Boolean signs; independent physical input law; deterministic coordinates contracted; natural entropy units except stated ordinary bit constant',
     'Dyadic cell j(t) has 1/2<2^j t<=1; exact upper-boundary convention; occupied labels only in sums',
     'Activation selector independent of seed at its actual induced law; a in (0,1) for displayed ratios, constant seeds separately contracted',
     'Complete reference keeps actual empty mass and all occupied nonempty labels; ordinary KL and signed conversion used once',
     'Decision-list selectors use distinct physical variables; complements handled by reflected laws; no novelty claim for known binary/read-once consequences']
canonical=json.dumps({'statement':statement,'hypotheses':hyp},sort_keys=True,separators=(',',':'))
claim={'claim_id':'A044-ARBITRARY-ACTIVATION-CARRY-OWNERSHIP','version':1,'exact_statement':statement,'hypotheses':hyp,
       'statement_sha256':hashlib.sha256(canonical.encode()).hexdigest(),'contributors':['A044/fleet03'],
       'proof_source':{'path':'PROOF.md','sha256':proofhash},
       'proof_dependencies':['Direct physical expansion F=1-X+Xg; scalar logarithm inequality; exact complete ordinary KL chain rule',
         {'claim_id':'A042-DYADIC-ACTIVATION-ENDPOINT-CERTIFICATE','version':1,'scope':'Consumed and independently reconstructed; general-selector extension derived here'},
         {'claim_id':'A044-COMPLETE-DYADIC-REFERENCE-CARRY','version':1,'scope':'Only optional weaker arbitrary-seed J corollary (10) uses its universal mantissa bank; sharp decision-list bound and obstruction are independent'}],
       'review_records':[],'status':'AUTHOR_ANALYTIC_PROOF_WITH_EXACT_CERTIFICATES_PENDING_INDEPENDENT_REVIEW',
       'supersedes':[],'refutes':[],
       'first_unproved_line':'Universal arbitrary-seed J_hi payment from SAME unused original capacity in a complete inherited reference; no such estimate follows from selector gate bounds.',
       'next_consumers':['A042','A043','A045','A091','B09 lead']}
claims=[claim]
for a,run,scope in [
 ('A042','20261023T055815Z-fleet03-A042-bias-endpoint-certificates','Original activation/endpoint theorem at its stated dyadic-selector scope; all reference, KL, constant and endpoint clauses analytically reconstructed.'),
 ('A043','20261023T063610Z-fleet03-A043-prime-gate-decomposition','Complete singleton-preserving reference, singleton reserve, signed sector transfer and disjoint reference composition only; excludes prime census/package and universal scale payment.')]:
    origin=AGENT.parent/a/'runs'/run
    original=read(origin/'CLAIMS.json')[0];c=copy.deepcopy(original)
    ps=c['proof_source']
    if isinstance(ps,dict):ps['path']=str((origin/ps['path']).resolve())
    elif isinstance(ps,list):c['proof_source']=[str((origin/p).resolve()) if isinstance(p,str) else p for p in ps]
    c['review_records'].append({'reviewer':'A044/fleet03','outcome':'HOLDS_SCOPED','scope':scope,
       'source_statement_sha256':original['statement_sha256'],'source_proof_sha256':sha(origin/'PROOF.md'),
       'review_source':str((ROOT/'REVIEWS.md').resolve()),'validation_source':'out/CHECK.json; out/INDEPENDENT.json',
       'global_registry_adoption':'not observed; source files unmodified'})
    claims.append(c)
dump(ROOT/'CLAIMS.json',claims)
progress={'protocol_revision':'2026-10-11-execution-v2','run_id':ROOT.name,'stream':'B09','packet_id':'A044',
 'gap_id':'A044-SIGNED-PROFILE-BOUNDED-CONGESTION','attempt_id':'substantive8-arbitrary-activation-carry-ownership',
 'method':'Consume A042/A043 new reference dependencies; independent scoped reviews; general-selector exact scale/KL derivation; actual near-identity Boolean carry obstruction; sharp activation entropy family corollary; separate exact rational implementations.',
 'mathematical_delta':'Fresh selector deficit cannot pay inherited activation carry: ratio >=(6/25)2^m; full signed KL conversion explicit and negative in limit. Outer J<=3ln4Delta for every selector bias; nested canalyzing gates sharp corrected E<=(4+ln4)Delta uniformly in arity/depth/bias. Universal seed scale remains open.',
 'deliverable_status':'COMPLETE_LOCAL_PENDING_REVIEW_OF_NEW_CLAIM',
 'mathematical_status':'UNIVERSAL_FEI_OPEN; EXACT_FAMILY_AND_OWNERSHIP_AUTHOR_PROOF',
 'claim_versions_used':['A042-DYADIC-ACTIVATION-ENDPOINT-CERTIFICATE@1','A043-PAID-SECTOR-COMPLETE-REFERENCE@1','A044-COMPLETE-DYADIC-REFERENCE-CARRY@1'],
 'claims_created_or_changed':['A044-ARBITRARY-ACTIVATION-CARRY-OWNERSHIP@1','A042-DYADIC-ACTIVATION-ENDPOINT-CERTIFICATE@1 local HOLDS_SCOPED review','A043-PAID-SECTOR-COMPLETE-REFERENCE@1 local HOLDS_SCOPED review'],
 'source_artifacts':['PROOF.md','REVIEWS.md','out/CHECK.json','out/INDEPENDENT.json','out/ADVERSARY.json','out/PILOT_REPAIR.md','out/SOURCE_RECEIPTS.json','out/PERSISTENCE.json'],
 'next_consumers':['A042','A043','A045','A091','B09 lead'],
 'next_action':'Pay actual arbitrary-seed high-degree J_hi from unused original R,S,U in A043 complete reference, retaining the signed flat/tree conversion and both full terminals; A042/A045 review this activation ownership obstruction first.',
 'stagnant_substantive_attempts':0,
 'blockers':['Universal original-owner seed-scale payment unproved.','Independent review of new A044 theorem, registry adoption and supervisor mirroring not observed.','Brain self-care degraded/unverified: stale owner-model, state-of-mind and dream notes; not mathematical premises.'],
 'packet_ids':['A044']}
dump(ROOT/'PROGRESS.json',progress);(ROOT/'PACKET_DELTA.json').write_bytes((ROOT/'PROGRESS.json').read_bytes())
report='''# A044/B09 stage19 — arbitrary activation and source ownership

## exact target, quantifiers, hypotheses and units

Extend A042 activation from dyadic selectors to every interior independent selector bias, retaining the complete inherited reference, its ordinary KL and both full terminal laws. Determine whether its extra scale carry can be paid solely from its own fresh outer deficit. All seeds are actual finite Boolean signs under independent product laws; deterministic coordinates contract. Natural entropy units throughout; ordinary uniform-cube bit constant stated separately. This is substantive8, not a fresh packet.

## sources actually read, revisions and theorem locators

Read current BOARD.md (supervisor 2026-10-23 10:53 UTC), B09 STREAM_NOTES.md v2, own STATUS.md and previous substantive7 PROOF/checker. Read A042 20261023T055815Z PROOF.md sections 1-5 and CLAIMS.json, A043 20261023T063610Z PROOF.md and CLAIMS.json, and A045 20261023T041958Z CLAIMS.json. BOARD reports A045 independent acceptance of our previous reference/carry theorem; this is not a review of the new claim. Protocol required_per_run schema rechecked. Exact source hashes are saved in out/SOURCE_RECEIPTS.json. Historical threshold/percolation sources and campaign files were consumed in prior stages; no new invocation of their theorems is needed for the present elementary obstruction and activation bound. The lead's old common-mean address target was already completed; following the current stream dependency/review bottleneck rather than repeating it.

## complete derivation or exact first unsupported line

PROOF.md derives J_F=eJ_g+J_o+ln4 C, with sharp all-bias outer-gate J_o<=3ln4 Delta_o. The actual activated-AND2 Boolean family has C/Delta_o=e(1+t)/(t(3+t))>=(6/25)2^m, t=2^-m. Thus no universal fresh-selector payment for this inherited carry exists, even at three variables. The carry asymptotically consumes the seed mantissa L_g; the signed flat/tree transfer has a negative limit, so neither can be reused as fresh capacity. Complete-reference likelihoods and ordinary KL are kept explicitly. The exact entropy gate ratio is ln4+2e ln(1/e)/(1-e)+2a ln(1/a)/(1-a)<=4+ln4, sharply. This proves the nonsymmetric nested canalyzing decision-list family bound E<=(4+ln4)Delta at every product law, independent of arity and depth; ordinary uniform bit FEI constant is 2+4/ln2. Binary/read-once consequences are not asserted novel. First unsupported universal line: pay actual arbitrary-seed J_hi from the SAME unused original capacity; no proof is supplied. Full FEI OPEN.

## executed validation with domain, arithmetic, commands and outputs

Frozen specs preceded both jobs. Main command: python -X utf8 code/check_stage.py from this run (or use the full run-relative path from A044). Domain: all 256 labeled three-bit Boolean masks at two fixed rational laws (512 seeds), four selector probabilities (2,048 activations), plus 24 explicit rational witnesses m=3,...,26. No symmetry reduction, no automatic dimension increase. Fraction arithmetic; rational reference normalization, support and likelihood identities checked before logarithms. PASS: 348,673 assertions, 120 positive-carry cases, runtime 21.712 seconds. Independent command: python -X utf8 code/check_independent.py; direct alternating mixed differences and 32-term rational atanh log intervals with proved tail, 24 witnesses; PASS: 329 assertions, runtime 19.060 seconds. Both jobs estimated 80 MB, sequential, below 60-second pilot and 300-MB admission thresholds. The first main pilot caught a missing factor (1+t) in both draft ratio and expected formula; correction preserved the lower bound. out/PILOT_REPAIR.md records the failure. No formal proof or Lean certification is claimed; no heavy job was needed.

## proof dependencies and changed downstream conclusions

REVIEWS.md independently accepts A042's original dyadic activation/endpoint theorem at its stated scope. It also accepts A043's singleton-preserving complete reference, reserve and signed sector/composition interface at the explicitly limited scope; prime-census/package and universal scale payment are not certified. Local copied claims append these reviews without modifying any source tree or globally adopting a registry status. The new obstruction is proved by direct Boolean spectrum identities; the optional weaker carry-bank corollary imports our previous universal mantissa bank. The sharp nested canalyzing entropy result uses only exact composition and ln x<=x-1. Downstream: dropping A042's dyadic selector hypothesis requires explicit carry and a signed reference conversion; outer-gate scale payment cannot be mistaken for inherited-seed payment.

## one next mathematical action and independent reviewer

Pay the actual arbitrary-seed high-degree J_hi from unused original R,S,U in A043's singleton-preserving complete reference, keeping ordinary KL and both full terminals. A042/A045 should first independently review the present carry obstruction and arbitrary-selector signed conversion; A043/A091 are consumers. Avoid another fresh-selector or singleton-rounding reserve: this actual three-variable witness already blocks that ownership shortcut.

## actual persistence receipts or precise save blocker

REPORT.md, CLAIMS.json, PROGRESS.json, identical PACKET_DELTA.json, proof/reviews, frozen specs, exact outputs and code are saved inside this A044 run. out/PERSISTENCE.json records hashes of the completed run files and rolling files; the saver rereads and checks them. STATUS.md has exactly two lines; WORKLOG.md and LEARNED.md append this result once. No shared research tree, other agent folder, remote registry or brain store was written. Supervisor mirroring and independent review of the new claim remain unobserved. Brain self-care is degraded/unverified: owner-model 97.4 hours stale, state-of-mind 82.0 hours stale and latest dream 32.7 hours stale at wake; these affect personal-context recall and were not premises of this proof. No jobs remain after the recorded validations.

**Universal bridge:** This stage moves C020 whole-set witness cost by isolating an actual inherited carry that no constant fresh-selector payment can cover, while preserving the complete signed reference/KL bill and identifying its original seed mantissa owner. It also closes the nested canalyzing family with sharp arity/depth-independent corrected constant 4+ln4 and consumes two pending review interfaces. It improves no universal FEI constant: arbitrary-seed J_hi remains unpaid. The shortest next route is the SAME unused seed R,S,U payment in the inherited singleton-preserving reference; another isolated selector estimate cannot cross the exact obstruction proved here.
'''
(ROOT/'REPORT.md').write_text(report,encoding='utf-8')
status='STATE: A044 substantive8 saved: arbitrary-selector carry/outerDelta diverges on activated AND2; sharp nested-canalyzing E<=(4+ln4)Delta; 348673+329 exact checks PASS; A042/A043 scoped HOLDS; FEI OPEN.\nNEXT: A042/A045 review carry/signed conversion; pay inherited seed J_hi from SAME unused original R,S,U in A043 complete reference with ordinary KL and both full terminals.\n'
(AGENT/'STATUS.md').write_text(status,encoding='utf-8')
marker='2026-10-23 substantive8 / 20261023T105700Z'
entries={
 'WORKLOG.md':f'\n## {marker}\nConsumed current board plus A042/A043 complete-reference dependencies and recorded scoped independent HOLDS reviews. Extended arbitrary-selector activation with exact carry and full inherited ordinary KL; actual three-variable activated AND2 gives C/Delta_outer=e(1+t)/(t(3+t)) >=(6/25)2^m. First pilot caught omitted (1+t); corrected derivation/checker and retained failure record. Main 348673 exact assertions PASS (21.712s), separate direct-mixed/log-interval 329 assertions PASS (19.060s). Proved sharp nested-canalyzing family E<=(4+ln4)Delta, no depth/arity surcharge; no novelty claim for binary/read-once consequences. Universal seed scale open; no Lean/heavy jobs. Brain self-care stale owner/state/dream, not mathematical premises.\n',
 'LEARNED.md':f'\n## {marker}\nFor arbitrary independent activation F=1-X+Xg, J_F=eJ_g+J_o+ln4 C, J_o<=3ln4 Delta_o sharply, C=e^2 sum P_T k_T with k_T in {{0,1}}. Tree corrected cross entropy is J_F-ln4 C+n_o+e n_g, and signed flat/tree KL conversion is ln4 C+n_F-n_o-e n_g. For g=-1+2yz at q=(1+t)/2, e=1-2t, actual carry/outer deficit=e(1+t)/(t(3+t)) diverges; ln4 C/L_g ->1 and KL_flat-KL_tree ->-[(3/4)ln3-(1/2)ln4]<0. The seed singleton index jumps UP at q=1/2; do not claim continuity of inherited J there. Exact entropy composition instead gives sharp nested-canalyzing E<=(4+ln4)Delta for every independent bias, hence ordinary fair-cube FEI constant 2+4/ln2, no depth/arity cost. This family result does not pay arbitrary seed J_hi.\n'}
for name,entry in entries.items():
    p=AGENT/name;old=p.read_text(encoding='utf-8') if p.exists() else ''
    if marker not in old:
        with p.open('a',encoding='utf-8',newline='') as stream:stream.write(entry)

protocol=read(Path(r'math-open-problems/reports/fei-2026-10-11/EXECUTION_PROTOCOL.json'))['required_per_run']
assert all(set(c)==set(protocol['claim_fields']) for c in claims)
pf=['packet_ids' if x.startswith('packet_ids (') else x for x in protocol['progress_fields']]
assert set(progress)==set(pf)
assert all('## '+field in report for field in protocol['report_fields'])
assert len((AGENT/'STATUS.md').read_text(encoding='utf-8').splitlines())==2
assert (ROOT/'PROGRESS.json').read_bytes()==(ROOT/'PACKET_DELTA.json').read_bytes()
for item in read(ROOT/'out/SOURCE_RECEIPTS.json'):
    assert sha(Path(item['path']))==item['sha256']
files=[p for p in ROOT.rglob('*') if p.is_file() and p.name!='PERSISTENCE.json']
files += [AGENT/name for name in ('STATUS.md','WORKLOG.md','LEARNED.md')]
assert all(p.stat().st_size<20_000_000 for p in files)
receipt={'status':'SAVED_AND_REHASHED','files':[{'path':str(p.resolve()),'bytes':p.stat().st_size,'sha256':sha(p)} for p in files],
 'schema':'protocol required_per_run exact field sets checked','shared_sources':'all pinned source hashes unchanged','remote_mirror':'not performed; supervisor ownership','full_FEI':'OPEN'}
dump(ROOT/'out/PERSISTENCE.json',receipt)
for item in read(ROOT/'out/PERSISTENCE.json')['files']:assert sha(Path(item['path']))==item['sha256']
print(json.dumps({'status':'SAVED_AND_REHASHED','hashed_files':len(files),'claim_records':len(claims),'new_claim_sha256':claim['statement_sha256'],'exact_assertions':main['exact_assertions']+ind['exact_assertions'],'full_FEI':'OPEN'}))
