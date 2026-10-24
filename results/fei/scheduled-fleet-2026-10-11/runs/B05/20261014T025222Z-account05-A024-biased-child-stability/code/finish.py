from pathlib import Path
import json,hashlib,datetime
R=Path(__file__).resolve().parents[1]; A=R.parents[1]
def sha(data): return hashlib.sha256(data).hexdigest()
def write(name,obj): (R/name).write_text(json.dumps(obj,indent=2,ensure_ascii=False)+'\n',encoding='utf-8')
shared=Path('~/brain_workers/FEI100_20261011')
sources=[shared/'BOARD.md',shared/'claude/B05/STREAM_NOTES.md',shared/'claude/B05/runs/20261011T225000Z-claude-B05-odd-face-transport/REPORT.md',Path('~/mop_fei100/reports/fei-2026-10-11/EXECUTION_PROTOCOL.json'),A/'STATUS.md',A/'LEARNED.md',A/'runs/20261011T223622Z-account05-A024-biased-child-stability/CLAIMS.json',A/'runs/20261011T223622Z-account05-A024-biased-child-stability/code/check.py',A/'runs/20261012T032452Z-account05-A024-biased-child-stability/DERIVATION.md',A/'runs/20261012T032452Z-account05-A024-biased-child-stability/out/METHOD1_RUNTIME_STOP.json']
receipts=[]
for p in sources:
    data=p.read_bytes(); receipts.append({'path':str(p),'bytes':len(data),'sha256':sha(data)})
write('out/SOURCE_RECEIPTS.json',receipts)
prior=A/'runs/20261012T032452Z-account05-A024-biased-child-stability/out/METHOD1_RUNTIME_STOP.json'
(R/'out/PRIOR_RUNTIME_STOP.json').write_bytes(prior.read_bytes())
statement='For disjoint uniform physical Boolean blocks F=g(f_1,...,f_k), let a_i=E(D_i g)^2 and gamma_ij be the probability, over other induced outputs, that the i,j gate face has corner product -1. With Q(f)=2^(1-n)N_odd(f), Q(F)=sum_i a_i Q(f_i)+(1/2)sum_{i<j}gamma_ij I(f_i)I(f_j). A query x in child h of F=A+B h has q_x(F)=t q_x(h)+(Inf_x(h)/2)I(1-2B^2), t=E B^2. For the explicit five-bit bent/point-flip selector c of DERIVATION.md, d=1/16,m=3/16,I(c)=37/16 and B_s(c)-Lbin(m,d)>1/4; hence its queried selector remains K=4 bad in every nontrivial disjoint outer composition. For F_LN=1-(1+P_N)(1-product_{j=1}^L c_j)/2, L,N>=1, I=[37L/16+(1-(3/16)^L)N]/2. A complete selectors-first tree spends at least L(4+N)/32 bad odd-face credit; for N=L^2 its ratio to I is at least L/53. A complete parity-first tree spends exactly L/8, ratio at most 4/37. The selectors-first signed mean residual bank is between zero and L(2L+4)16^(-(L+1)); it contains beta^2 log(1/M^2)/2+O(beta^2) at beta=-M/3. Thus at fixed K=4 every-tree O(I) credit is false, while this family satisfies a some-tree bound and has H/I tending to zero when N=L^2. No universal some-tree bound is asserted.'
claims=[{'claim_id':'A024-MIXED-FACE-ORDER-OBSTRUCTION','version':1,'exact_statement':statement,'hypotheses':['finite Boolean signs on independent uniform physical blocks','bits for all entropy units','fair singleton restrictions; induced child output laws, not biased physical inputs','L,N positive integers; c and two complete orders exactly as in DERIVATION.md','bad means erasure B_v>4 Inf_query; expected node credit q_v=I(f_v0 f_v1)/2','event influence I(1-2W), not Fourier energy of a 0/1 indicator'], 'statement_sha256':sha(statement.encode()),'contributors':['account05/A024'],'proof_source':{'path':str(R/'DERIVATION.md'),'locators':'equations (1)-(8), exact erasure reconstruction and endpoint safety, no FEI counterexample','certificates':['out/INTEGER_CERTIFICATES.json','out/SIGN_CERTIFICATES.json','out/TREE_LEDGER.json','out/VALIDATION.json','out/REPLAY.json']},'proof_dependencies':[{'claim_id':'A024-BIASED-CHILD-TRANSPORT','version':1,'status':'PROVED_LOCALLY_PENDING_INDEPENDENT_REVIEW; used erasure clause reconstructed self-contained here'},{'claim_id':'B05-ODDFACE-TELESCOPE','version':1,'status':'lead author-proved; direct face-count reconstruction here'}],'review_records':[{'reviewer':'A024','scope':'distinct implementation replay, not independent agent review','artifact':'out/REPLAY.json','verdict':'PASS_LOCAL_REPLAY'}],'status':'PROVED_LOCALLY_PENDING_INDEPENDENT_REVIEW','supersedes':[],'refutes':['Unregistered EVERY-tree K=4 bad-node odd-face O(I) strengthening; not B05-ODDFACE-LOCALIZED-BRIDGE'],'first_unproved_line':None,'next_consumers':['B05','A021','A023','A025','A039','A057','A087','A094','B20']}]
write('CLAIMS.json',claims)
progress={'protocol_revision':'2026-10-11-execution-v2','run_id':R.name,'stream':'B05','packet_id':'A024','gap_id':'B05-ODDFACE-LOCALIZED-BRIDGE','attempt_id':'A024-02-mixed-face-order-completion','method':'Resume unfinished 20261012 proof; bounded-cache exact verification, direct seed character-transform replay, and all-parameter Boolean construction; no dimension escalation','mathematical_delta':'At genuine log(1/mean) selector splits, all nodes are K4 bad but signed mean bank exponentially small. Mixed-face selector-first credit/I>=L/53 for N=L^2, while parity-first exact credit=L/8<=4I/37. General disjoint odd-face transport and robust seed badness proved without endpoint division. Every-tree fixed-K4 strengthening refuted; some-tree bridge remains open.','deliverable_status':'COMPLETE_LOCAL_ARTIFACT; INDEPENDENT_REVIEW_AND_MIRROR_PENDING','mathematical_status':'PACKET_LEAD_SPLIT_CLASSIFICATION_RESOLVED_LOCALLY; UNIVERSAL_SOME_TREE_BRIDGE_AND_FULL_FEI_OPEN','claim_versions_used':['A024-BIASED-CHILD-TRANSPORT@1 (erasure clause reconstructed)','B05-ODDFACE-TELESCOPE@1 (face count reconstructed)','B05-ODDFACE-LOCALIZED-REDUCTION@1 (motivation only)'],'claims_created_or_changed':['A024-MIXED-FACE-ORDER-OBSTRUCTION@1'],'source_artifacts':['DERIVATION.md','FROZEN_SPEC.json','FROZEN_SPEC_REPLAY.json','code/check_stage2.py','code/replay.py','out/VALIDATION.json','out/REPLAY.json','out/INTEGER_CERTIFICATES.json','out/SIGN_CERTIFICATES.json','out/TREE_LEDGER.json','out/SYMBOLIC_ROWS.json','out/SOURCE_RECEIPTS.json','out/PRIOR_RUNTIME_STOP.json'],'next_consumers':claims[0]['next_consumers'],'next_action':'Replace parity controller by arbitrary Boolean W and derive the exact controller-first mixed-face/bad-node transfer with inherited controller erasure and terminal core retained; A087/A094 independently reconstruct seed and two-order all-parameter proof.','stagnant_substantive_attempts':0,'blockers':['No local access or compute blocker. History-dependent general-controller query selection and inherited terminal payment remain unproved; external review and supervisor mirror copies pending.'],'packet_ids':['A024']}
write('PROGRESS.json',progress); write('PACKET_DELTA.json',progress)
report='''# exact target, quantifiers, hypotheses and units

Complete the unfinished biased-child stability application directed by B05 v2: locate log(1/mean) splits, decide whether their erasure satisfies B_v>4d_v, and compute expected odd-face credit divided by original physical influence. All physical coordinates are independent uniform bits. An outer gate sees the actual independent child output means; a fair physical restriction does not change the measure of untouched inputs. Entropy is in bits. q_v=I(f_v0 f_v1)/2; node weights are physical reach probabilities. This report proves a fixed-K=4 order obstruction and its repair on an explicit family, not full FEI.

# sources actually read, revisions and theorem locators

EXECUTION_PROTOCOL.json revision 2026-10-11-execution-v2; BOARD.md snapshot 2026-10-14 02:43 UTC; B05 STREAM_NOTES.md v2 (2026-10-11 23:4xZ), especially the A024 target and SOME-tree bridge; B05 lead REPORT.md 20261011T225000Z, Lemmas 1-2 and Theorem 4. Own stage-1 CLAIMS.json/LEARNED.md and source implementation; own unfinished stage-2 DERIVATION.md and runtime-stop receipt. Current source bytes and SHA256 are in out/SOURCE_RECEIPTS.json. Initial campaign/paper intake remains documented by the stage-1 source receipts; no new theorem is imported from unread paper revisions.

Board overlap checked: A016 distinguishes raw derivative boundary and owned complete reserves; A025 reports all-s unfiltered overcharge with zero bad credit on its overlap family; A023 and A057 now retain one marked terminal/controller reserve. The present witness is an actual single-use mixed odd-face charge at bad nodes inside a nonfactorable two-child gate. It therefore does not rename tensor-spectator raw-boundary overcharge or contradict their paid scopes. No source acceptance is inferred from a board receipt.

# complete derivation or exact first unsupported line

DERIVATION.md gives the complete proof. For F=A+B h with W=B^2 and t=E W, q_x(F)=t q_x(h)+(Inf_x(h)/2)I(1-2W). The event's sign influence is essential; using the Fourier energy of the 0/1 W loses a factor four. For arbitrary disjoint substitution, Q(F)=sum_i a_i Q(f_i)+(1/2)sum_{i<j}gamma_ij I(f_i)I(f_j), with gamma_ij the biased probability that the corresponding gate face is odd. Counting same-block and mixed-block faces proves the formula, including deterministic child limits.

The five-bit selector c uses a four-bit bent sign and its one-point flip. Its mean is 3/16, influence 37/16, selector influence 1/16 and selector credit 1/4. Integer inequalities certify both B_s(c)>1/4 and B_s(c)-Lbin(3/16,1/16)>1/4. The latter preserves badness under any nonignored disjoint outer gate. The exact negative empty-fiber credit is retained, and the erasure formula used from stage 1 is reconstructed here.

Let G_L be the product of L copies, P_N a fresh parity, F_LN=1-(1+P_N)(1-G_L)/2. Its influence is [37L/16+(1-(3/16)^L)N]/2. In the complete selectors-first order every selector is bad, its mean contrast beta=-M/3 produces a genuine log(1/M), and its credit is (4+N)/32. Thus the bad bill is at least L(4+N)/32. Setting N=L^2 gives bill/I>=L/53, unbounded. Nevertheless the total signed mean residual is at most L(2L+4)16^(-(L+1)). The growing cost is the mixed-face term, not this tiny mean-log bank.

In the complete parity-first order the first N-1 queries have zero erasure, the last is K4-good, and the remaining product selectors contribute exactly L/8 expected bad credit. Data nodes are good. Hence bill/I<=4/37, tending to zero for N=L^2. Both trees have constant leaves and exactly zero terminal entropy. Also H(F_LN)<=5L+1 and I>=13N/32; H/I tends to zero in the obstruction regime. This is no FEI counterexample.

First unsupported universal line: for every Boolean f, a history-measurable tree can assign only O(I(f)) odd-face credit to its bad nodes, with inherited controller/core costs retained. Nothing here establishes that line. The refutation concerns EVERY tree at fixed K=4 only; it does not refute a different threshold K or the lead's SOME-tree statement.

# executed validation with domain, arithmetic, commands and outputs

Frozen specs preceded execution. Commands from the A024 workspace: `python -X utf8 runs/20261014T025222Z-account05-A024-biased-child-stability/code/check_stage2.py --pilot`, then the same command without `--pilot`, then `python -X utf8 runs/20261014T025222Z-account05-A024-biased-child-stability/code/replay.py`.

Pilot PASS: 16 roots, 112 splits, two complete trees; 363 recorded exact equality checks and 138 logarithm-sign calls; 0.172 seconds. Full PASS: all 16 two-input gates times all 16 two-bit companion children, 256 seven-bit roots, 1,792 physical splits, 184 bad nonignored root selectors; six (L,N) pairs (1,1),(1,2),(1,4),(2,1),(2,2),(2,4), both complete orders, maximum truth-table dimension 14. There were 5,673 recorded exact equality checks, 1,990 sign calls, and 205 memoized tree states; runtime 6.518 seconds. Positivity assertions and integer comparisons additionally pass. No symmetry deletion or automatic n increase.

Integer Walsh spectra and Fraction influence/face ledgers are exact. Entropy differences are prime-log forms; rational atanh sums with proved geometric-tail remainder bound certify 45 distinct nonzero signs (24 terms, 48 if needed). Replay uses a direct character-sum transform, independently coded rational log intervals, both seed integer inequalities and all 12 saved ledger formula cross-checks; PASS in 0.0375 seconds. This implementation replay is not independent agent acceptance, nor a second full tree traversal. Thirty-two symbolic rational rows are illustrations only; the infinite family is settled by the analytic proof. Memory estimates 150 MB main/30 MB replay are below the memok threshold; no observed peak-memory measurement is claimed.

The unfinished 20261012 uncached full job hit its 180-second watchdog, without a failed mathematical assertion. Its receipt is retained in out/PRIOR_RUNTIME_STOP.json and the original run remains untouched. Bounded caches completed the same frozen finite domain here with a 300-second cap. Earlier incomplete artifacts are not relabeled as a completed stage.

# proof dependencies and changed downstream conclusions

Used A024-BIASED-CHILD-TRANSPORT@1 only for its erasure clause, reconstructed directly; used B05-ODDFACE-TELESCOPE@1 with direct face counting. Local proofs are complete; external acceptance remains pending. The lead's localized FEI reduction is motivation, not a premise needed for the obstruction. Corrected FEI+ remains sum_nonempty P log2(product input variances/P), without output-variance numerator; uniform H=Eplus+e(mean^2).

Downstream: mean-log affordability cannot justify selector-first restriction. Inner KL rebates do not buy mixed odd faces. The selector is robustly bad even after genuine biased disjoint substitution, but order can place every mixed face at a good parity query. A025's zero-bad overlap result and A057's owned signed release remain compatible. This is completion of the productive unfinished packet under the dispatch rule, not opening an unrelated broad candidate while reviews are pending.

# one next mathematical action and independent reviewer

Replace the parity controller by arbitrary Boolean W and derive the exact controller-first transfer of mixed faces, retaining W's own erasure and both actual terminal child functions. Determine the first controller node where this transfer lacks an influence-owned price. This generalizes the demonstrated repair toward a history-dependent policy. Independent reviewers: A087/A094 for the exact seed sign, deterministic endpoints and all-parameter two-order proof; B05 consumes the distinction between cheap mean bank and mixed-face ownership.

# actual persistence receipts or precise save blocker

The four protocol files, proof, frozen specifications, scripts, exact ledgers/certificates and replay outputs are saved in this run. out/PERSISTENCE_RECEIPTS.json records SHA256 and bytes for every other run file after writing. STATUS.md, WORKLOG.md and LEARNED.md are updated locally. All files are below 20 MB; no local save blocker. Supervisor copies, mirrors, independent acceptance and downstream use are pending and not claimed.

## Universal bridge

This stage moves B05-ODDFACE-LOCALIZED-BRIDGE and C019 stopping-tree payment by closing the lead's biased-child split classification and proving exact mixed-face transport: log(1/mean) nodes really are bad, their mean bank is exponentially small, and the same Boolean family separates a divergent selectors-first bill/I>=L/53 from a parity-first bill/I<=4/37. The universal gap is still a policy assigning mixed faces to paid good queries while retaining arbitrary controller and terminal-core deficits; no all-dimensional FEI bound follows yet. The next controller-first transfer is the shortest route because it isolates precisely the order-dependent term that defeats the local credit rule, rather than adding another isolated function-class entropy estimate.
'''
(R/'REPORT.md').write_text(report,encoding='utf-8')
now=datetime.datetime.now(datetime.timezone.utc).isoformat()
(A/'STATUS.md').write_text('STATE: A024 mixed-face completion saved: K4 selectors-first bill/I>=L/53, parity-first <=4/37; 5673 exact checks and certificate replay PASS; review pending, FEI OPEN.\nNEXT: Transfer mixed faces under arbitrary controller-first restrictions with controller erasure and actual terminal cores retained; A087/A094 review seed and order proof.\n',encoding='utf-8')
with (A/'WORKLOG.md').open('a',encoding='utf-8') as f: f.write('\n'+now+' — Resumed productive unfinished 20261012 calculation in latest assigned 20261014 run. Prior uncached watchdog retained; bounded-cache exact full domain passed in 6.518s: 256 compositions,1792 splits,12 trees,5673 equality checks,1990 sign calls. Separate direct-transform/sign replay passed (45 distinct signs). Proved mixed-face transport, robust K4 bad seed, divergent selectors-first credit and parity-first repair; mean-log bank exponentially small. Some-tree bridge and full FEI open; no external review/mirror claimed.\n')
with (A/'LEARNED.md').open('a',encoding='utf-8') as f: f.write('''
2026-10-14 mixed-face completion: for disjoint F=A+B h, q_x(F)=t q_x(h)+(Inf_x h/2)I(1-2B^2); event boundary uses the sign, not 0/1 Fourier energy. General Q(F)=sum a_i Q(f_i)+(1/2)sum gamma_ij I(f_i)I(f_j), no variance denominators.

Five-bit bent/point-flip seed c has mean3/16,I37/16,d_selector1/16 and nonempty erasure>1/4; integer certificate 2^182*13^156>5^210*3^162. Its selector stays K4 bad in any nonignored disjoint outer composition. The negative empty-sector subtraction is indispensable to the exact statement.

For parity-activated product F_LN, all selectors-first mean-log splits are bad. With N=L^2 their expected bad-face bill/I>=L/53, although total signed mean bank<=L(2L+4)16^(-(L+1)). Complete parity-first instead has exact bad bill L/8<=4I/37 and zero terminal entropy. Every-tree fixed-K4 O(I) is false; SOME-tree bridge remains open. H/I tends to zero, so this is not an FEI counterexample. Mixed faces must be allocated to good queries, not paid by tiny mean/KL banks.

Bounded caching repaired a runtime-only failure on the same domain (no dimension escalation). Exact sign replay checks 45 distinct rational-log certificates; it is implementation reproduction, not independent agent review. Preserve prior unfinished run history.
''')
protocol=json.loads(sources[3].read_text(encoding='utf-8-sig'))
expected=set(protocol['required_per_run']['progress_fields']);expected.remove('packet_ids (one primary ID, for compatibility)');expected.add('packet_ids')
assert set(progress)==expected
assert set(claims[0])==set(protocol['required_per_run']['claim_fields'])
assert json.loads((R/'PROGRESS.json').read_text())==json.loads((R/'PACKET_DELTA.json').read_text())
assert all('# '+field in report for field in protocol['required_per_run']['report_fields'])
assert len((A/'STATUS.md').read_text().splitlines())==2
manifest=[]
for p in sorted(R.rglob('*')):
    if p.is_file() and p.name!='PERSISTENCE_RECEIPTS.json':
        data=p.read_bytes();assert len(data)<20*1024*1024
        manifest.append({'path':str(p.relative_to(R)),'bytes':len(data),'sha256':sha(data)})
write('out/PERSISTENCE_RECEIPTS.json',manifest)
print(json.dumps({'status':'SAVED_AND_SCHEMA_CHECKED','run':R.name,'files':len(manifest)+1,'largest_bytes':max(x['bytes'] for x in manifest),'progress_fields':len(progress),'claim_fields':len(claims[0])}))
