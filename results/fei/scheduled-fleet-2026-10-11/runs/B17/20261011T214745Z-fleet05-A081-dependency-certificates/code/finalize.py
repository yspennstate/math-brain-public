from pathlib import Path
import json,hashlib,datetime
from dependency_check import statement_hash,validate,key
RUN=Path(__file__).resolve().parents[1]; OWN=RUN.parents[1]
BASE=Path(r'~\mop_fei100\reports\fei-2026-10-11')
def load(p):
    raw=p.read_bytes()
    return json.loads(raw.decode('utf-16' if raw.startswith((b'\xff\xfe',b'\xfe\xff')) else 'utf-8-sig'))
def save(p,v):p.write_text(json.dumps(v,indent=2,ensure_ascii=False)+'\n',encoding='utf-8')
protocol=load(BASE/'EXECUTION_PROTOCOL.json'); g=load(RUN/'PROOF_DEPENDENCIES.json'); v=validate(g)
assert v['status']=='STRUCTURALLY_VALID' and not v['errors']
tests=load(RUN/'out/TEST_RESULTS.json'); fixed=load(RUN/'out/FIXTURE_REVALIDATION.json'); interval=load(RUN/'out/INDEPENDENT_INTERVAL.json'); reproduced=load(RUN/'out/B09_REPRODUCTION.json')
save(RUN/'out/B09_REPRODUCTION.json',reproduced)
save(RUN/'out/BUILD.json',load(RUN/'out/BUILD.json'))
assert tests['status']==fixed['status']==interval['status']==reproduced['status']=='PASS'
assert tests['graph_cases']==66067 and fixed['fixture_count']==13
assert all(not r['eligible_for_mathematical_review'] for r in v['candidate_routes'])
admitted=[key(n) for n in g['nodes'] if n['status'].startswith('IMPORTED_')]
assert len(admitted)==7
assert all(not v['unresolved_closure'][k] for k in admitted)
hashes=load(RUN/'out/registry_hash_audit.json'); assert all(x['match'] for x in hashes)
save(RUN/'out/VALIDATION.json',v)
statement='For the frozen 2026-10-11-execution-v2 registry snapshot, the A081 certificate encodes all three registered versions, preserves the two admitted roots and their five source-bound subclaims, and exposes the pending B09 theorem dependency. Its seven-node admitted subgraph is acyclic with no unresolved dependency. Five alternative FEI routes retain explicit unproved premises; none is a completed FEI proof. The structural cycle checker agrees with independent Kahn elimination on all 66,067 labeled directed graphs of order at most four, including loops.'
hyp=['Only the exact local source bytes and statements pinned in PROOF_DEPENDENCIES.json','Imported acceptance/certification is limited to the original stated scope','Source theorem truth, edge entailment and review independence require mathematical reconstruction','All discrete entropy statements use the units declared on each node']
claim={'claim_id':'A081-VERSIONED-DEPENDENCY-CERTIFICATE','version':1,'exact_statement':statement,'hypotheses':hyp,'statement_sha256':statement_hash(statement,hyp),'contributors':['A081'],'proof_source':{'run_id':RUN.name,'path':'REPORT.md','certificate':'PROOF_DEPENDENCIES.json','checker':'code/dependency_check.py','validation':'out/VALIDATION.json','exhaustive_check':'out/TEST_RESULTS.json'},'proof_dependencies':[{'claim_id':c['claim_id'],'version':c['version'],'statement_sha256':c['statement_sha256']} for c in g['nodes'] if c['claim_id'] in ['B05-SPARSE-ACTIVATION-VARIANCE-REFUND-NOGO','B09-TAXFREE-AND-COUNTEREXAMPLE-REPAIRED']],'review_records':[],'status':'LOCAL_CERTIFICATE_CHECKED_PENDING_INDEPENDENT_REVIEW','supersedes':[],'refutes':[],'first_unproved_line':None,'next_consumers':['A001','A083','A090','A094','A096','A098','A099']}
assert set(claim)==set(protocol['required_per_run']['claim_fields'])
save(RUN/'CLAIMS.json',[claim])
progress={'protocol_revision':protocol['revision'],'run_id':RUN.name,'stream':'B17','packet_id':'A081','gap_id':'FEI-B17-A081-INITIAL','attempt_id':'A081-stage1-dependency-schema','method':'Frozen exact versioned graph; source-byte and statement hashes; DFS/Kahn exhaustive graph check; independent rational interval reproduction','mathematical_delta':'No new FEI bound. Encoded seven admitted nodes from two registered roots; exposed unversioned Maassen-Uffink premise and five unpaid FEI route endpoints; independently certified the repaired two-bit margin using 32 terms and dyadic range reduction.','deliverable_status':'LOCAL_COMPLETE_PENDING_INDEPENDENT_REVIEW','mathematical_status':'STRUCTURAL_CERTIFICATE_CHECKED; FULL_FEI_OPEN','claim_versions_used':[key(n) for n in g['nodes'] if n['claim_id'].startswith('B05-') or n['claim_id'].startswith('B09-')],'claims_created_or_changed':['A081-VERSIONED-DEPENDENCY-CERTIFICATE@1'],'source_artifacts':['out/source_inventory.json','out/source_pin_audit.json','PROOF_DEPENDENCIES.json','DEPENDENCY_VALIDATOR.md','out/VALIDATION.json','out/TEST_RESULTS.json','out/FIXTURE_REVALIDATION.json','out/INDEPENDENT_INTERVAL.json'],'next_consumers':claim['next_consumers'],'next_action':'A090 independently reconstruct admitted source edges and interval proof; A094 alternate. Consume only a changed source/claim version after this finite baseline is accepted. B09 reviewer must pin exact Maassen-Uffink version and applicability before admission.','stagnant_substantive_attempts':0,'blockers':['B17 STREAM_NOTES.md absent at prescribed path; no contrary instruction available.','B09 core theorem review and its primary dependency pin remain pending.','Full FEI and all five candidate-route universal payment premises remain open.'],'packet_ids':['A081']}
progress_keys={'packet_ids' if x.startswith('packet_ids (') else x for x in protocol['required_per_run']['progress_fields']}
assert set(progress)==progress_keys
save(RUN/'PROGRESS.json',progress); (RUN/'PACKET_DELTA.json').write_bytes((RUN/'PROGRESS.json').read_bytes())
now=datetime.datetime.now(datetime.timezone.utc).isoformat()
report=f'''# exact target, quantifiers, hypotheses and units

A081, B17, run {RUN.name}. Deliverables are PROOF_DEPENDENCIES.json and DEPENDENCY_VALIDATOR.md. Artifact complete locally; independent acceptance pending. Full FEI remains OPEN.

The ultimate target is exists finite C>=0, for every n>=0 and every Boolean sign f on the uniform cube, H_2(f)<=C I(f). H_2 is squared-Fourier Shannon entropy in bits, I is spectral expected cardinality, zero atoms contribute zero, and constants have H=I=0. C must be independent of n and f. Neither a finite graph check nor the two-bit biased helper refutation resolves this target.

The certificate has {len(g['nodes'])} exact versioned nodes, {len(g['sources'])} source pins, seven admitted nodes from two registered root results, one pending registered theorem, and five separate conditional routes. Proof dependencies point from conclusions to premises; workflow feedback is separate. Hypotheses, entropy units, actual physical versus spectral influence, source bytes and locators, acceptance states, and open premises are explicit.

# sources actually read, revisions and theorem locators

Read EXECUTION_PROTOCOL.json in full, revision {protocol['revision']}, then campaign README, CURRENT_STATUS, CLAIM_REGISTRY, OBSTRUCTION_REGISTRY, PACKET_STATUS, STREAM_NEXT_ACTIONS and plan TeX. The source-reading helper reads and hashes full byte strings; mathematical inspection focuses on theorem interfaces, proof passages and scope. out/source_inventory.json records byte hashes and line counts. This does not independently audit every analytic theorem in the manuscripts.

Read the supplement CAMPAIGN, CLAIMS, COUNTEREXAMPLES, SEED_LEMMAS, NATIVE_MAPPING and source notes; SOURCES.json supplies original versus packaged provenance. Read earlier B05, B09, B19 reports and the repaired B09 report/code. Important pins: B05 original 80cc2e5027efa56d79c4ecdf7d4949759ef2068b section 6; B19 accepting review 7955d427222392911dc6af2e4ee3aa8aab67ac8c sections 2.1-2.5; B09 pending report adb671ffcda143fa68347806bb96e8c305621a7d; repaired counterexample a1ff93577685acd461b154b04e0c1aa0c65645c8, verification/B09_interval_repair_20261011. All three registry statement hashes match the protocol convention exactly.

Threshold interfaces inspected: 38-page Theorem A, Proposition 5.5, section 5.8, Proposition 7.1/Corollary 7.2, section 8.3, Proposition 8.9/Corollary 8.10; native archived TeX labels thm:A, prop:joint-witness, comp:identities, comp:closure, prop:activation, cor:activation-equivalence resolve PDF text extraction loss. The 29-page version has different constants (Creg<13.415 versus current Creg<8.937) and section numbering. It is a distinct source, not a substitute version. The archived current TeX fails equality with the related public source hash 85e9c4f36026eb5890be5686d03bf5264e524144686ee203ed799e3d41ac7017, even after CRLF normalization. It is pinned by its actual local SHA256; public-release identity or theorem acceptance is not inferred from that hash comparison.

Percolation 30-page and other 31-page versions are separately pinned. Theorem 1.1 concerns specified rectangle crossings, with physical pivotal I versus biased spectral J; section 4.4 retains arm-estimate and influence-lower-bound hypotheses. Theorem 1.3 is discrete triangular-site singularity, not continuum singularity. The other version makes its sharp total-variation overlap exponent conditional, whereas the 30-page abstract states the sharp exponent; no version substitution is made. Neither source supplies arbitrary-Boolean FEI.

The board was read at stage start; B17 lead notes and A004 status were absent. A001 REPORT.md and GAP_MAP.json are source-pinned navigation. A001 already inspected 37 routes and tensor admission, so this packet supplies the verifier and evidence-bound graph rather than repeating that mathematical audit. No pending A001 claim is silently admitted.

# complete derivation or exact first unsupported line

The admitted B05 chain is explicit: the even-k bent point-surgery source gives actual Boolean G,H with flat coefficient magnitudes and e_W=d^2, d=2^(-3k). Its accepted review proves max theta<=4delta, delta=2^-k, and L>=(1-delta)d(k-2). It then proves V<=4delta*d and M=12k*d^2. For fixed finite K,A,B>=0,

    (L-Kd-AV-BM)/d >= (1-delta)(k-2)-K-4A*delta-12B*k*d -> infinity

along even k. These edges lie within the independently accepted original no-go scope. They do not refute existential block selection, every restriction tree, or FEI. The seven-node admitted subgraph contains no desired FEI premise and no unresolved leaf.

The second admitted chain is the repaired fixed biased AND gate. For independent p=1/8,q=1/4, g=(-1)^(XY), the squared Fourier masses are exactly (225,7,3,21)/256. M_A=H(masses)-h2(3/32); J_A=h2(3/32)-(1/8)h2(3/4). Independent reproduction bounds J_A-M_A in [0.119545016024424957,0.119545016024424958] bits and strictly above 1195/10000. This refutes universal tax-free J_A<=M_A only. It accepts neither the full B09 uncertainty lemma nor an endpoint tax-necessity claim.

The new independent implementation derives those four masses from p,q. It multiplies each positive logarithm argument by a dyadic factor until its mantissa lies in [1,2). With z=(x-1)/(x+1)<=1/3, ln x=2 sum_j>=0 z^(2j+1)/(2j+1); after 32 terms the nonnegative tail is at most 2z^65/[65(1-z^2)]. Division by a positive rational ln2 enclosure uses a nonnegative mantissa numerator; the exact integer dyadic exponent is added afterward. Entropy subtraction reverses interval endpoints, and final decimals round outward. All computations and the strict comparison are rational.

The pending B09 root exposes its first source gap: the registry names Maassen-Uffink in unversioned prose. Exact theorem version, bases, overlap constant, units, source and applicability remain unpinned. Its stronger global influence payment and endpoint optimality are separately unproved. No rejected interval implementation is imported as a rigorous sign certificate.

Five alternative proof routes retain their own unpaid premises: aggregate erasure B<=KI; existential proper-block conditional entropy payment; complete joint reference expectation payment including representation and all costs; arbitrary balanced-core two-cell selector FEI; and arbitrary rare activated-core FEI. The latter two are full-strength equivalent endpoints, by disjoint tensor amplification and fresh-sign balancing, with r_t=ceil(2log2(t+1)) for rare activation. Their completed implication proofs do not establish the universal class estimates. Regular, read-once composition, rank-piece, and geometric hypotheses are never discarded. Natural rank logs and corrected biased entropy are distinct from ordinary Shannon entropy.

The structural proof is as described in DEPENDENCY_VALIDATOR.md: active-stack edges witness cycles, while DFS finishing order puts every dependency before its conclusion in an acyclic graph. Induction then checks admitted closure. Independent Kahn elimination uses a different representation. The exact first unsupported semantic step in any attempted full proof is a valid proof of one of the displayed universal unpaid premises, followed by source/edge reconstruction. A machine check of text fields does not establish logical entailment of their hypotheses.

# executed validation with domain, arithmetic, commands and outputs

Frozen specs: out/FROZEN_SPEC.json and out/INTERVAL_FROZEN_SPEC.json. Graph domain: all 66,067 labeled adjacency masks for orders 0..4, including loops, no symmetry reduction, integer arithmetic, about 32 MB estimated memory, declared 60-second pilot. DFS/Kahn comparisons passed all cases; DAG counts are 1,1,3,25,543. Measured graph-test runtime was {tests['elapsed_seconds']:.3f} seconds. Thirteen mutation fixtures passed, including direct/transitive FEI circularity, stale hashes/versions, unadmitted accepted dependencies, missing sources and unexplained units. Workflow feedback remains permitted. After final unit/source additions, fixtures and byte validation passed again in {fixed['elapsed_seconds']:.3f} seconds; unchanged cycle enumeration was not needlessly repeated.

Copied original repaired B09 checker reproduced PASS with 1200 Fraction terms; its internal runtime was not separately instrumented. No live own reproduction process remained when checked. The independent range-reduced certificate passed at 32 terms, 33 exact dyadic-log cases, one specified Boolean gate, in {interval['elapsed_seconds']:.4f} seconds, about 16 MB estimated memory. It proves containment in the same 18-decimal rational interval. Finite cases are certificates only at their stated domain. No FEI Boolean-family search, GPU, dimension escalation, solver or job exceeding the 300 MB memory threshold was launched.

Commands executed from A081:

```text
python -X utf8 read_sources.py
python -X utf8 inspect_target.py
python -X utf8 runs/{RUN.name}/code/build_certificate.py
python -X utf8 runs/{RUN.name}/code/test_certificate.py
python -X utf8 runs/{RUN.name}/code/reproduce_B09.py
python -X utf8 runs/{RUN.name}/code/independent_interval.py
python -X utf8 runs/{RUN.name}/code/test_certificate.py --fixtures-only
python -X utf8 runs/{RUN.name}/code/finalize.py
```

Source audit: all three registry hashes match; all twelve curated packaged source hashes match after CRLF-to-LF normalization. Full-note original blobs match where full originals are bundled. Curated excerpts are not asserted to match their complete originals. B09 and B19 report blobs and the seed blob match after normalization. The archived threshold/public-source mismatch is explicit, not hidden by assigning the related public commit to local bytes.

# proof dependencies and changed downstream conclusions

No shared registry was edited and no FEI conclusion changed. B05 remains accepted at local no-go scope; repaired B09 counterexample remains certified; full B09 theorem remains pending. Admitted roots preserve registry statements and hashes. Subclaim proofs use the accepting B19 review and repaired source, not a status field alone. A001's pending map is navigation, not a premise proving FEI.

A001/A083/A096/A099 can consume the exact version and source schema. A098 can distinguish saved artifacts, accepted mathematics and unpaid leaves. A090/A094 can use the cycle witnesses and admitted closure for independent review. A041/B19 must pin the B09 primary uncertainty theorem and cannot use the repaired finite helper to accept the entire theorem. Five candidate routes are alternatives; no AND aggregation of unrelated campaign gaps is implied. Rarity, proper geometric classes, orthogonality, dyadic source versions, and corrected entropy cannot be broadened by ledger labels.

# one next mathematical action and independent reviewer

Primary reviewer A090: independently reconstruct the B05 subclaim edges and the fixed biased-gate coefficient/32-term interval derivation; then audit that the final FEI claim never enters an admitted premise and that each conditional route retains its unpaid universal assumption. A094 is the alternate independent reviewer, with recusal if either materially repairs this version. B09's mathematical reviewer should supply the exact primary Maassen-Uffink version before the pending root can enter the accepted graph. Once this finite baseline is accepted, update only for a specific changed statement/source or a new downstream application.

# actual persistence receipts or precise save blocker

All deliverables are saved inside A081 only, including required REPORT.md, CLAIMS.json, PROGRESS.json and byte-identical PACKET_DELTA.json, plus certificate, validator guide, code and exact outputs. STATUS.md has exactly two lines; WORKLOG.md is appended and LEARNED.md updated. out/ARTIFACT_RECEIPTS.json lists output hashes and sizes; out/FINAL_VALIDATION.json checks protocol fields, current source bytes, registry hashes, progress compatibility, admitted closure and the 20 MB file cap. Finalized {now}.

No external persistence, supervisor copy, mirror verification, independent acceptance, public release or downstream mathematical use is claimed. No git, email, brain writes, protected trading files, shared source modification or other-agent writes occurred. Missing lead notes did not prevent authorized independent work.
'''
(RUN/'REPORT.md').write_text(report,encoding='utf-8')
assert all(('# '+f) in report for f in protocol['required_per_run']['report_fields'])
(OWN/'STATUS.md').write_text('STATE: A081 dependency certificate complete locally: 30 versioned nodes, seven admitted subclaims/roots, 66,067 graph cases and independent rational margin passed; FEI OPEN; review pending.\nNEXT: A090 reconstruct source edges and interval proof; A094 alternate; B09 needs exact Maassen-Uffink pin. Update this baseline only for changed sources or downstream use.\n',encoding='utf-8')
with (OWN/'WORKLOG.md').open('a',encoding='utf-8') as f:
    f.write(f'\n{now} — Stage 1 A081/B17: read protocol, registries, sources, board and A001 map; B17 notes absent. Built 30-node graph, preserved registry statement hashes and seven-node admitted closure, exposed unpinned MU premise and five conditional routes. Exhaustive 66,067 DFS/Kahn graph cases plus 13 fixtures passed. Reproduced repaired two-bit margin; independent dyadic/Fraction 32-term certificate passed in {interval["elapsed_seconds"]:.4f}s. Public-source equality fails for archived threshold TeX; pin exact local bytes. All deliverables saved, independent review pending, FEI open.\n')
with (OWN/'LEARNED.md').open('a',encoding='utf-8') as f:
    f.write('\nA081 stage 1 durable facts: protocol statement hash is SHA256 of compact sorted JSON {statement,hypotheses}; all three current registry hashes match. Proof edges require exact versions; conditional implications cannot discharge their premise using FEI. Advisory feedback is permitted but all proof cycles are rejected. B05 no-go uses L/d >=(1-2^-k)(k-2), V/d<=4*2^-k, M/d=12k*2^-3k; scope is fixed-price local refunds only. B09 AND masses (225,7,3,21)/256, p=1/8,q=1/4, yield J-M in [0.119545016024424957,0.119545016024424958] bits. Dyadic reduction to [1,2), 32 rational atanh terms and tail 2z^65/(65(1-z^2)) reproduce this interval exactly. Original interval quotient must account for negative numerators. B09 full lemma remains pending with unversioned MU dependency. LF-normalized hashes reproduce original source pins; packaged excerpt hashes differ from complete original blobs. The archived threshold source is not byte-identical to the published source hash. A001 already maps 37 FEI routes; reuse that pending audit as navigation. Baseline accepted closure differs from source-complete imports awaiting acceptance; never promote status text to proof.\n')
assert (RUN/'PROGRESS.json').read_bytes()==(RUN/'PACKET_DELTA.json').read_bytes()
receipts=[]
for p in sorted(RUN.rglob('*')):
    if not p.is_file() or '__pycache__' in p.parts or p.name in ['ARTIFACT_RECEIPTS.json','FINAL_VALIDATION.json']: continue
    raw=p.read_bytes(); assert len(raw)<20*1024*1024
    receipts.append({'path':str(p.relative_to(RUN)),'bytes':len(raw),'sha256':hashlib.sha256(raw).hexdigest()})
save(RUN/'out/ARTIFACT_RECEIPTS.json',receipts)
result={'status':'PASS','nodes':len(g['nodes']),'sources':len(g['sources']),'admitted_nodes':admitted,'candidate_routes_all_conditional':True,'registry_hashes_match':True,'protocol_report_fields':7,'protocol_claim_fields_exact':True,'protocol_progress_fields_exact':True,'progress_field_annotation':'Protocol display label packet_ids (one primary ID, for compatibility) is serialized as packet_ids, per explicit user compatibility requirement.','progress_delta_byte_identical':True,'artifact_count':len(receipts),'max_artifact_bytes':max(x['bytes'] for x in receipts),'independent_review':'PENDING_A090_OR_A094','full_FEI':'OPEN'}
save(RUN/'out/FINAL_VALIDATION.json',result); print(json.dumps(result,indent=2))
