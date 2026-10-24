from pathlib import Path
import json,hashlib,datetime
R=Path(__file__).resolve().parents[1];A=R.parents[1]
def dump(name,obj): (R/name).write_text(json.dumps(obj,indent=2,ensure_ascii=False)+'\n',encoding='utf-8')
def sha(path):return hashlib.sha256(path.read_bytes()).hexdigest()
def append_once(path,entry):
 text=path.read_text(encoding='utf-8') if path.exists() else ''
 while text.count(entry)>1:
  i=text.rfind(entry);text=text[:i]+text[i+len(entry):]
 if entry not in text:text+=entry
 path.write_text(text,encoding='utf-8')
old=json.loads((A/'runs/20261012T020138Z-account05-A058-overlapping-compositions/CLAIMS.json').read_text(encoding='utf-8'))[0]
old['version']=3
old['exact_statement']+=' Restricted physical-tree replacement: for a fresh fair-selector mux of G(S,X)=epsilon(X)chi_{A(X)}(S) and H(S,Y)=eta(Y)chi_{B(Y)}(S), arbitrary finite shared S and disjoint private X,Y, the exact coherent collision potential R satisfies H(F)=(H(G)+H(H))/2+R, 0<=R<=(4+2/ln2)I_data(F). At each actual data query the signed erasure correction D_i relative to half the two core erasures obeys |D_i|<=4 Inf_i(F), with factor 2 at private queries. Every adaptive data prefix has |R_root-E R_leaf|<=(4+2/ln2)(I(F_root)-E I(F_leaf)). An optional selector suffix spends the remaining data reserve; both inherited terminal core entropies remain explicit. The indexed-parity hypothesis is equivalent to hereditary l1<=1 conditional-private-mean profiles.'
old['hypotheses'].append('Additional restricted physical-tree replacement has its separate indexed-parity/fresh-fair-selector hypotheses, not the earlier anchor-identification hypotheses; entropy bits, actual adaptive physical data restrictions, uniform original cube.')
old['statement_sha256']=hashlib.sha256(json.dumps({'statement':old['exact_statement'],'hypotheses':old['hypotheses']},sort_keys=True,separators=(',',':')).encode()).hexdigest()
old['proof_source']={'current':str(R/'PROFILE_REPAIR.md'),'preserved_v2':str(A/'runs/20261012T020138Z-account05-A058-overlapping-compositions/COHERENT_FIBER_REPAIR.md'),'preserved_v1':str(A/'runs/20261011T222138Z-account05-A058-overlapping-compositions/OVERLAP_ENTROPY_LEDGER.md')}
old['proof_dependencies']=[]
old['supersedes']=[{'claim_id':old['claim_id'],'version':2,'scope':'Preserves prior transfer and obstruction; supplies a scoped physical-query replacement price rather than a universal anchor-only price.'}]
old['status']='SCOPED_REPAIR_PROVED_LOCAL_REVIEW_PENDING'
old['next_consumers']=['B12','A077','A097','A056','A057','A091','A090','B20']
src=Path('~/brain_workers/FEI100_20261011/agents/A077/runs/20261013T222235Z-account05-A077-sparse-defect-towers')
review=json.loads((src/'CLAIMS.json').read_text(encoding='utf-8'))[0]
review['review_records'].append({'reviewer':'account05/A058','verdict':'ACCEPT_AT_STATED_SCOPE','source':str(R/'REVIEW_A077.md'),'method':'Independent paired-row integral, coherent Fourier counting, physical JS/influence transport reconstruction; separate exact truth-table implementation; no repair'})
review['status']='ACCEPTED_LOCAL_INDEPENDENT_REVIEW'
review['proof_source']={'author':str(src/'PROOF.md'),'review':str(R/'REVIEW_A077.md')}
dump('CLAIMS.json',[old,review])
res=json.loads((R/'out/check_indexed_full.json').read_text())
progress={'protocol_revision':'2026-10-11-execution-v2','run_id':R.name,'stream':'B12','packet_id':'A058','gap_id':'A058-COHERENT-OVERLAP-PHYSICAL-RESERVE','attempt_id':'3-profile-owned-repair','method':'Consume new one-shared-bit dependency; independent review; hereditary profile characterization and exact coherent paired-row price; physical influence telescope.','mathematical_delta':'Arbitrary-size privately indexed shared parities admit one outer collision reserve K=4+2/ln2<7; both core and stopped terminal entropies retained. Prior anchor-only no-go unchanged.','deliverable_status':'COMPLETE_LOCAL','mathematical_status':'RESTRICTED_REPAIR_PROVED; FULL_FEI_OPEN; OWN_V3_REVIEW_PENDING','claim_versions_used':['A058-ANCHORED-OVERLAP-POSTERIOR-LEDGER@2','A077-ONE-SHARED-BIT-SIGNED-TRANSPORT@1 (independently reviewed; new proof self-contained)'],'claims_created_or_changed':['A058-ANCHORED-OVERLAP-POSTERIOR-LEDGER@3','A077-ONE-SHARED-BIT-SIGNED-TRANSPORT@1 independent scoped acceptance'],'source_artifacts':['PROFILE_REPAIR.md','REVIEW_A077.md','code/check.py','out/FROZEN_SPEC.json','out/FROZEN_INDEXED_SPEC.json','out/check_pilot.json','out/check_full.json','out/check_indexed_pilot.json','out/check_indexed_full.json'],'next_consumers':['A077','A056','A057','A091','A090','B12','B20'],'next_action':'Replace one indexed-parity shared slice by a genuinely nonlinear two-bit slice and price its signed profile excess using consumed physical influence plus the retained core deficit; do not recharge the outer bank.','stagnant_substantive_attempts':0,'blockers':['No unrestricted hereditary mean-profile price or terminal-core FEI payment.','Independent review of A058 v3 pending.'],'packet_ids':['A058']}
dump('PROGRESS.json',progress);dump('PACKET_DELTA.json',progress)
report='''# exact target, quantifiers, hypotheses and units

Prove a single-owner coherent collision reserve for a nontrivial class of overlapping Boolean compositions. The class consists of fresh fair-selector muxes whose two cores are signed shared parities indexed arbitrarily by disjoint private inputs. Shared dimension, private dimensions, indexing maps, and finite adaptive data stopping trees are arbitrary. Entropy is in bits. K=4+2/ln2<7. Both inherited core entropies remain obligations. Full FEI remains OPEN.

# sources actually read, revisions and theorem locators

Read the current BOARD (2026-10-13 23:39 UTC), B12 STREAM_NOTES v2 (2026-10-11 23:30 UTC), own STATUS and LEARNED, and the execution protocol v2 in full. Consumed stage-3 REPORT/CLAIMS for A057, A091, A028 and A077; read A077 PROOF sections 1-6 in full. Also read A097 stage-3 DERIVATION.md sections 1-4 and the relevant REPORT/BOUNDARY locators. A097 already closes root reference transfer under l1 admission, with a selector-owned price; this stage claims the hereditary structural characterization and signed adaptive data-prefix reserve, not a new root FEI class closure. A028 now closes the earlier disjoint-data shared-control priority target, so that result was not repeated. The lead's old anchor-only requested price was already refuted in our v2; this stage follows the protocol's new-dependency dispatch with a scoped replacement. Earlier campaign sources and papers were read in preceding stages; no fresh claim is attributed to an unread theorem in them.

# complete derivation or exact first unsupported line

PROFILE_REPAIR.md gives a complete coherent Fourier ledger, hereditary-profile characterization, signed private/shared row prices, and physical influence telescope. The hereditary profile condition is exactly equivalent to every fully fixed private slice being a signed shared character. Thus it allows private inputs to choose among arbitrarily many shared frequencies. D is bounded by 4 times actual influence, not nominal per-core allowances. Subtracting inherited core entropy decrements adds a JS difference bounded by 2/ln2 times that same influence. Prefix plus selector suffix fits one K I_data reserve. No terminal entropy is dropped. The first unsupported universal line is a dimension-independent replacement for profile admissibility when a shared slice is genuinely nonlinear; a two-bit bent profile has l1=2 and supplies an exact boundary witness, not an FEI counterexample.

# executed validation with domain, arithmetic, commands and outputs

Frozen specs precede both pilots. Commands: python -X utf8 code/check.py pilot; full; indexed_pilot; indexed_full (from the run directory, or use its full relative script path). First suite: 256 product-character roots, all 20,736 partial data restrictions, 13,001 exact assertions, no failures, 6.383 seconds. Expanded suite exhausts all 4,096 privately indexed signed-parity core pairs with two shared bits and one private bit each; root and all immediate data restrictions give RESULTS_PLACEHOLDER. Pilots: 16 roots/1,553 checks and 64 roots/2,840 checks, both below 60 seconds. All amplitudes, influences, l1 conditions, and identities use exact Fraction arithmetic. Entropies use exact prime-log expressions and rational logarithm enclosures with a proved 24-term atanh-series geometric tail; a comparison is accepted only after an exact interval sign or symbolic equality. Rational K<7 bounds are used for finite reserve validation. No floating-point sign establishes a claim. Estimated memory below 300 MB; no memok-gated job was required. Dimensions were frozen, never escalated.

# proof dependencies and changed downstream conclusions

A077 one-shared-bit theorem v1 is independently ACCEPTED_AT_STATED_SCOPE in REVIEW_A077.md, with no substantive repair to that source. The current multibit extension is self-contained and is a scoped amendment of existing A058 v2, preserving its obstruction and transfer statements. Private-indexed parity compositions now have a physical-query replacement for the false shared-anchor-only price. This does not extend to arbitrary shared Boolean slices or priority controller gates and does not pay arbitrary terminal-core FEI. The additive K cost is not asserted reusable at every level of a deep hierarchy.

# one next mathematical action and independent reviewer

Test one genuinely nonlinear two-bit shared slice beyond the indexed-parity class, retaining the exact signed profile excess and both core deficits. Seek an exclusive physical influence price for that excess; A077 receives the exact common-frequency comparison, and A091 (alternate A090) reviews A058 v3. This directly addresses the missing hypothesis rather than enumerating another parity subclass.

# actual persistence receipts or precise save blocker

All four protocol files, proofs, frozen specs, code and exact outputs are saved inside this run. Rolling STATUS, WORKLOG and LEARNED are updated by code/finalize.py. out/MANIFEST.json records SHA256 hashes of saved artifacts; the finalizer checks exact protocol field sets and compatibility equality. These are local durable receipts only; no supervisor copy, mirror, public release or independent acceptance of A058 v3 is claimed.

Universal bridge: This stage advances C019 stopping-tree payment and the associated C018 erasure price by replacing an unpriced overlap correction with K<7 times a single consumed physical-data influence reserve for arbitrary-sized privately indexed shared parities. Complete coherent rows and both stopped terminal core entropies are retained, and the selector suffix uses the remaining reserve. Arbitrary nonlinear shared slices, inherited terminal FEI, and hierarchy-wide ownership remain open. The next nonlinear shared slice is the shortest extension toward removing the actual structural hypothesis; another fixed-parity class would not move that gap.
'''
text=f"{res['node_visits']:,} node visits / {res['exact_checks']:,} exact assertions, {res['distinct_nodes']:,} distinct nodes, no failures, {res['seconds']:.3f} seconds"
(R/'REPORT.md').write_text(report.replace('RESULTS_PLACEHOLDER',text),encoding='utf-8')
(A/'STATUS.md').write_text('STATE: A058 stage 3 complete: privately indexed shared-parity collision reserve K<7 proved; A077 v1 independently accepted; exact certificates saved; own v3 review pending, full FEI OPEN.\nNEXT: A091/A090 review v3; price one nonlinear two-bit shared slice beyond hereditary l1<=1 using physical influence and both retained core deficits.\n',encoding='utf-8')
append_once(A/'WORKLOG.md','\n2026-10-13T23:40:47Z stage 3: consumed new board and A028/A077 interfaces; previous disjoint-data priority target already closed elsewhere. Independently accepted A077 one-shared-bit transport; proved hereditary profile class equals privately indexed shared parities and paid coherent signed correction with one K<7 reserve. Exact indexed suite: '+text+'. Universal nonlinear profile and terminal FEI gaps retained.\n')
append_once(A/'LEARNED.md','\nStage 3 durable fact: hereditary l1<=1 shared conditional means are equivalent to every fully private-fixed Boolean shared slice being a signed character (Parseval + l1/l2 equality). Thus G=epsilon(X)chi_A(X)(S), H=eta(Y)chi_B(Y)(S) allow arbitrary private indexing and shared dimension. Their fair mux has signed erasure excess |D_private|<=2 InfF, |D_shared|<=4 InfF; exact coherent R potential has |Rroot-E Rleaf|<=(4+2/ln2) consumed data influence and 0<=R<=(4+2/ln2)Idata. Both core entropies stay explicit. A bent two-bit slice has l1=2 and lies outside this sufficient class; it refutes automatic admissibility, not the price itself. A077 v1 independently reconstructed and accepted at scope, with sharp one-shared-bit factor 2.\n')
protocol=json.loads(Path('~/mop_fei100/reports/fei-2026-10-11/EXECUTION_PROTOCOL.json').read_text(encoding='utf-8'))['required_per_run']
assert set(progress)=={x.split(' (')[0] for x in protocol['progress_fields']}
assert all(set(c)==set(protocol['claim_fields']) for c in [old,review])
assert (R/'PROGRESS.json').read_bytes()==(R/'PACKET_DELTA.json').read_bytes()
manifest={str(p.relative_to(R)):sha(p) for p in R.rglob('*') if p.is_file() and p.name!='MANIFEST.json'}
dump('out/MANIFEST.json',{'artifacts':manifest,'rolling_files':{str(A/n):sha(A/n) for n in ['STATUS.md','WORKLOG.md','LEARNED.md']},'validation':'protocol fields exact; packet delta equal; all listed files locally read and hashed'})
print(json.dumps({'saved_artifacts':len(manifest),'protocol_fields':'PASS','packet_delta':'IDENTICAL','full_fei':'OPEN'}))
