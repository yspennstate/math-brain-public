from pathlib import Path
from fractions import Fraction as F
from datetime import datetime,timezone
import json,hashlib
B=Path(__file__).resolve().parents[1];A=B.parents[1];HOME=Path(r'~');TEAM=HOME/'brain_workers/FEI100_20261011'
PROTOCOL=HOME/'mop_fei100/reports/fei-2026-10-11/EXECUTION_PROTOCOL.json'
def write(p,s):p.write_text(s,encoding='utf-8',newline='\n')
def dump(p,o):write(p,json.dumps(o,indent=2,ensure_ascii=False)+'\n')
def digest(p):return hashlib.sha256(p.read_bytes()).hexdigest()
def claimhash(c):return hashlib.sha256(json.dumps({'statement':c['exact_statement'],'hypotheses':c['hypotheses']},sort_keys=True,separators=(',',':')).encode('utf-8')).hexdigest()
check=json.loads((B/'out/CHECK.json').read_text(encoding='utf-8'));pilot=json.loads((B/'out/PILOT.json').read_text(encoding='utf-8'));pair=json.loads((B/'out/PAIR.json').read_text(encoding='utf-8'))
assert check['status']==pilot['status']==pair['status']=='PASS'
assert sum(r['runs'] for r in check['rows'][:63])==3824
assert all(2*F(r['old_gap'])<F(41,10)*F(r['I']) for r in check['rows'][:63])
assert sum(r['strict_gap_improvement'] for r in check['rows'])==61
assert check['strict_star_improvements']==31
source_run=TEAM/'agents/A006/runs/20261014T074929Z-account05-A006-posterior-forest-optimization'
oldclaims=json.loads((source_run/'CLAIMS.json').read_text(encoding='utf-8'));reviewed=next(c for c in oldclaims if c['claim_id']=='A006-FULL-PARTITION-INCIDENCE-CAP-CERTIFICATE')
assert claimhash(reviewed)==reviewed['statement_sha256']
reviewed['review_records'].append({'reviewer':'A010','verdict':'HOLDS_WHOLE_EXTENSION_NO_REPAIR_UPSTREAM_AUTHOR_DISCLOSED','source':str(B/'REVIEW_A006.md'),'source_sha256':digest(B/'REVIEW_A006.md'),'scope':'full-family/all-m extension and entire n4 census independently reconstructed; earlier A010 cap premise authored by reviewer'})
reviewed['status']='INDEPENDENT_EXTENSION_RECONSTRUCTION_ACCEPTED_LOCALLY; UPSTREAM_AUTHOR_DISCLOSED'
statement=('For every finite positive width-two graph prime table, positive globally packing-feasible lambda, nonempty k-gate subset T, and certified L>0 with sum_T lambda<=L, the conditioned used-gate root-index law obeys p_lambda(T)<=1/[(1+4k/L)^k-(4k/L)^k]. For k>=2 this strictly improves the previous min(1,4^(1-k)L^(k-1)/k^k) cap. It is a sharp supremum when equal weights L/k on T are feasible and the table is allowed positive outside weights tending to zero. For every pair of incident gates i,j in any such table, singleton probabilities p_i,p_j and pair probability r obey p_i*p_j>=4r(p_i+p_j), equivalently [[p_i-4r,4r],[4r,p_j-4r]] is positive semidefinite, yielding t^2*p_i+p_j>=4(t+1)^2*r for every rational t>=0. For exactly two incident gates, positivity, normalization and this cone characterize all feasible root laws. The positive normalized law (2/3,5/18,1/18) satisfies all sharp individual caps and both individual lambda<=1 bounds but violates packing: recovered lambda=(4/5,1/3), determinant=-2/81, t=1/2 cut=-1/18. This is a root-relaxation falsifier, not a Boolean spectral or variational-cost counterexample. On the frozen 67 full-family graph references, new cap LP gaps improve strictly in61 cases; all31 frozen star sizes m2..32 improve strictly. No universal coding-cost payment or FEI solution follows.')
new={'claim_id':'A010-DENOMINATOR-CAPS-AND-JOINT-PAIR-PACKING','version':1,'exact_statement':statement,
 'hypotheses':['Fixed full positive width-two prime table, both endpoint orders and original conditioned chronological queue','Uniform actual Boolean edge DNF and full distinct partition event family for finite cost certificates','All weights positive and global; p(T) indexes used-gate monomials, not the initial roots of each actual forest','L>0 certified by packing; sharpness only with stated equal-weight feasibility, as a supremum if outside gates remain positive','Two-gate sufficiency does not assert higher-gate root-law realizability; complete cost and tangent gap remain distinct'],
 'statement_sha256':hashlib.sha256(statement.encode()).hexdigest(),'contributors':['A010'],
 'proof_source':{'derivation':'PROOF.md','code':['code/check.py','code/pair.py'],'certificates':['out/CHECK.json','out/PAIR.json'],'formal_source':'code/PairCone.lean; NOT kernel-certified'},
 'proof_dependencies':[{'claim_id':'A006-JOINT-ROOT-LAW-LOWER-CERTIFICATE','version':1,'statement_sha256':'9a0d49375a7a8ba40ae7b26ca9592229e9d3cf10310aa677e5121b90498716d5','acceptance':'previous whole source review retained; supporting inequality reconstructed'},{'claim_id':reviewed['claim_id'],'version':1,'statement_sha256':reviewed['statement_sha256'],'acceptance':'whole extension reconstructed in REVIEW_A006.md without repair'}],
 'review_records':[],'status':'ELEMENTARY_PROOF_AND_EXACT_CERTIFICATES; INDEPENDENT_REVIEW_PENDING; LEAN_RUNTIME_UNVERIFIED','supersedes':[],'refutes':['Sufficiency of separate sharp root-subset caps, even with individual lambda<=1 conditional bounds (unregistered proposed shortcut)'],'first_unproved_line':None,'next_consumers':['A006','A008','A009','A086','Claude/B02','B20']}
new['statement_sha256']=claimhash(new)
dump(B/'CLAIMS.json',[new,reviewed])
next_action='Add rational asymmetric pair-PSD cuts to the SAME full shared/leafless root LP with exact primal-dual certificates; then distinguish residual complete-cost payment from any remaining relaxation gap. A006/A008/A086 review.'
progress={'protocol_revision':'2026-10-11-execution-v2','run_id':B.name,'stream':'B02','packet_id':'A010','gap_id':'G-J-COST','attempt_id':'A010-stage6-denominator-and-joint-pair-packing','method':'Whole independent A006 full-family reconstruction; denominator-complete AM-GM caps; exact joint two-gate PSD constraint and rational falsifier; independent parent-map coefficients','mathematical_delta':'A006 full-partition extension reconstructed without repair. Denominator caps strictly improve61/67 full graph LP gaps and31/31 star LP gaps. Separate sharp caps still fail joint packing; exact two-gate cone and transferable asymmetric cuts derived. No variational-cost growth found.','deliverable_status':'COMPLETE_LOCAL_ARTIFACTS','mathematical_status':'SCOPED_PROOF_AND_EXACT_CERTIFICATES; FULL_FEI_OPEN; NEW_REVIEW_PENDING; LEAN_RUNTIME_UNVERIFIED','claim_versions_used':[{'claim_id':reviewed['claim_id'],'version':1},{'claim_id':'A006-JOINT-ROOT-LAW-LOWER-CERTIFICATE','version':1}], 'claims_created_or_changed':[{'claim_id':new['claim_id'],'version':1},{'claim_id':reviewed['claim_id'],'version':1,'change':'local extension review added without statement change'}], 'source_artifacts':['PROOF.md','REVIEW_A006.md','out/CHECK.json','out/PAIR.json','out/SOURCES.json'],'next_consumers':new['next_consumers'],'next_action':next_action,'stagnant_substantive_attempts':0,'blockers':['Universal complete same-reference cost payment remains unpaid. Pair cones are necessary only for tables of three or more gates. Lean check produced no compiler result. Supervisor mirroring and external adoption unverified.'],'packet_ids':['A010']}
dump(B/'PROGRESS.json',progress);write(B/'PACKET_DELTA.json',(B/'PROGRESS.json').read_text(encoding='utf-8'))
report='''## exact target, quantifiers, hypotheses and units

A010/B02 stage6, C020 / PI-J, G-J-COST. Strengthen a global all-weight/all-posterior lower certificate for the SAME full partition event family of actual positive graph edge DNFs. Natural-unit tangent gaps convert to bits with ln2>1/2; all complete costs and Fourier entropies are in bits. Quantifiers, positivity, equal-weight sharpness and event-index meaning are explicit in PROOF.md and CLAIMS.json. This is an interface proof and a scoped falsifier of a relaxation, not a variational counterfamily or FEI disproof. Full FEI remains OPEN; the current user's 23 October deadline supersedes the older protocol date.

## sources actually read, revisions and theorem locators

EXECUTION_PROTOCOL.json v2 read in full; current BOARD snapshot21 October16:12UTC, B02 lead notesv2, own STATUS/LEARNED/WORKLOG and stage5 proof/helper chain. Current campaign README/status/registries/plan and supplemental CAMPAIGN/CLAIMS/COUNTEREXAMPLES/SEED_LEMMAS/NATIVE_MAPPING were consulted for scope and navigation; earlier baseline/paper reading is inherited, not claimed as a fresh wholesale reread. The four supplied paper text versions were inspected at their relevant introduction/rank/spectral sections; these files decode as cp1252, unlike the UTF-8 reports. No external paper theorem is a new premise. Original source_material/reductions/paper/forests.tex, conditioned queue/forestpacking/forestrootconstants/thm:posteriorforest supply the exact queue definition. A006 stage074929 FULL_PARTITION_CAPS.md, CLAIMS, REPORT and helper definitions were read; own code imports none of its helpers. A007 joint occupation, A008 connected-scale and A009 private-leaf reports identify the next shared/leafless gap. out/SOURCES.json pins source bytes; navigation reads do not certify their theorem claims. One two-wording math-brain recall yielded no relevant root-cap result; no returned card is used as a premise.

## complete derivation or exact first unsupported line

REVIEW_A006.md reconstructs the entire unchanged A006-FULL-PARTITION-INCIDENCE-CAP-CERTIFICATE@1, including full-star enumeration, cardinality LP, all-m91/24 bit-gap bound and all63 n4 certificates. Verdict HOLDS without repair, with this reviewer's authorship of its earlier A010 cap input disclosed. This is an independent extension reconstruction, not a second independent origin of that upstream premise.

PROOF.md strengthens physical root-index caps by keeping every elementary-symmetric term in the nonempty-conditioning denominator. AM-GM gives p(T)<=1/[(1+4k/L)^k-(4k/L)^k], with precise sharp-supremum conditions. It improves the old caps strictly for every k>=2 and transfers to complete families independently of ownership. The full tangent LP remains only a lower relaxation of feasible weights.

An exact joint constraint replaces the proposed sufficiency of those separate caps: incident singleton/pair probabilities satisfy a2x2 PSD cone. For exactly two gates this is necessary and sufficient; for larger tables it is necessary only. Its rational quadratic forms yield asymmetric linear cuts. The positive point(2/3,5/18,1/18) obeys even sharp caps and individual conditional-weight bounds, but reconstructs weights(4/5,1/3), violating their shared row. The t=1/2 cut is exactly-1/18. This rejects a relaxed root law, not an actual Boolean squared spectrum or all-weight infimum.

First unsupported universal line: pay the COMPLETE same-reference cost by KI on arbitrary shared/leafless incidence, and eventually arbitrary Boolean prime tables. A small or shrinking certification gap pays neither cost. Pair cuts alone do not impose higher multiplicative root-law compatibility.

## executed validation with domain, arithmetic, commands and outputs

FROZEN_SPEC.json preceded the pilot; SPEC_REVISION.md records correction of a mislabeled fourth n5 graph BEFORE the first full run. The first pilot stopped on an absent out directory; PILOT_REPAIR.md preserves this infrastructure failure, which is excluded from successful counters. Final pilot:7 n3 graphs,3 star sizes,293 exact assertions,0.101211s. Full:all63 labelled nonempty n4 graphs plus exactly four n5 graphs(C5,K2,3,bowtie,house),31 cardinality stars m2..32;5593 assertions,5878 distinct chronological runs counted by parent-map slot factorials,3.758917s. No graph symmetry reduction. New caps strictly improve61 graph gaps and all31 star gaps. Every full n4 h vector and old capped optimum matches A006 exactly; all3824 distinct n4 runs are accounted for.

PAIR_SPEC.json preceded pair.py:all120 positive grid weights(i/16,j/16),i+j<=16, and all136 positive probability vectors of denominator18. Exact lambda reconstruction, determinant signs, root-law regeneration and separating cuts pass1761 assertions in0.063291s. Total successful reported assertions, including pilot overlap,7647. Integer Walsh transforms, physical flips, exact Fraction arithmetic, feasible packing primal/vertex dual equality and cap LP primal/threshold dual equality are checked. Floating values are display runtimes only. Every graph checkpoints immediately.

Commands from A010: python -X utf8 runs/RUN/code/check.py --pilot; same without --pilot; python -X utf8 runs/RUN/code/pair.py, where RUN is this directory's basename. Frozen memory estimates110MB/30MB, main jobs<60s, no GPU, detached work, automatic dimension escalation or other-agent edits. All jobs completed. Before the optional Lean attempt, memok.py exited0:physical free9.6GB,commit free23.9GB. lean_check.py --stmt attempted the determinant equivalence with45s timeout; receipt RUNTIME_UNVERIFIED after53.557s, compiler_exit_code null, no target or axioms verified. A properly laid-out formal source is saved in code/PairCone.lean but has not been checked. Rung: elementary proof plus exact certificates, NOT Lean-checked. The timeout is not evidence against the algebra.

## proof dependencies and changed downstream conclusions

The original conditioned queue and A006 root-law supporting inequality remain the baseline. A006's full-family extension is accepted locally unchanged, with the upstream-author disclosure above. The new denominator bound uses only positive elementary-symmetric AM-GM and packing. The PSD cone follows by positive-denominator cancellation, verified exactly; it supplies a new transferable constraint rather than a new entropy theorem. New claim independent review remains pending. No shared registry, source, other-agent output, brain store or remote repository was changed; supervisor copying and adoption are unobserved.

## one next mathematical action and independent reviewer

Add the rational asymmetric pair-PSD cuts to the SAME complete shared/leafless incidence LP, retaining h, physical packing, normalization and actual spectrum, and obtain rounded rational primal-dual certificates. Compare any remaining gap with COMPLETE cost, never with entropy alone. A006/A008/A086 should review the denominator equality conditions, pair sufficiency scope and finite certificates. This changes mechanism from independent caps to joint physical constraints, rather than repeating the already-closed star calculation.

## actual persistence receipts or precise save blocker

REPORT.md, CLAIMS.json, PROGRESS.json and byte-identical PACKET_DELTA.json, proofs, review, frozen specs, independent code and exact outputs are saved in this A010 run. code/finalize.py validates protocol field sets, statement hashes, current two-line STATUS, report fields, output counts and20MB limits; out/RECEIPTS.json records hashes/sizes. Rolling WORKLOG and LEARNED are updated. Only local persistence is verified. No git, mail, brain writes or publication; shared copying, mirror verification and downstream consumption remain unverified.

## Universal bridge

C020/PI-J moves by one whole full-family reconstruction and stronger transferable root-law constraints: complete-denominator caps improve61/67 frozen graph certificates and31/31 stars, while an exact joint-packing falsifier shows why separate sharp caps still cannot represent the variational infimum. The unknown universal constant is unchanged, and complete-cost payment and higher-gate compatibility remain unpaid. NEXT inserts the derived asymmetric physical pair cuts into the same shared/leafless full-family certificate before testing cost growth; it addresses the universal falsifier's missing joint constraint instead of adding another isolated FEI class result.
'''.replace('runs/RUN/','runs/'+B.name+'/')
write(B/'REPORT.md',report)
write(A/'STATUS.md','STATE: A010 stage6 saved: A006 full-family extension reconstructed; denominator caps improve61/67 graphs and31/31 stars; joint pair-PSD cone excludes sharp-cap falsifier;7647 exact assertions; FEI OPEN.\nNEXT: Add asymmetric rational pair-PSD cuts to SAME full shared/leafless root LP; exact primal-dual replay, then price COMPLETE cost separately; A006/A008/A086 review.\n')
stamp=datetime.now(timezone.utc).strftime('%Y-%m-%d %H:%M UTC')
entry=f'\n{stamp} stage6: Whole A006 full-partition extension reconstructed without repair(upstream A010 authorship disclosed); independent full coefficients match63 n4 tables. Denominator-complete caps improve61/67 graph and31/31 star LP gaps. Exact pair-PSD packing law and positive rational sharp-cap falsifier;7647 successful assertions including pilot overlap. Lean attempt runtime-unverified; no kernel claim. Full FEI and complete cost remain OPEN.\n'
for name,text in [('WORKLOG.md',entry),('LEARNED.md','\n2026-10-21 stage6: For a nonempty k-gate subset with sum weights<=L, exact-denominator AM-GM gives root cap 1/[(1+4k/L)^k-(4k/L)^k], sharp as a supremum if equal weights L/k are feasible. For incident gates, singleton p,q and pair r satisfy pq>=4r(p+q), equivalently [[p-4r,4r],[4r,q-4r]] PSD. On exactly two gates positivity/normalization plus this cone is sufficient; not on larger tables. Positive(2/3,5/18,1/18) obeys sharp individual caps and individual weight<=1 but recovers lambda(4/5,1/3),sum17/15; asymmetric cut t1/2=-1/18. Sharp separate root caps remain a relaxation, not the physical infimum. A006 full-family extension reconstructed unchanged; stronger cap gaps are not complete-cost payments.\n')]:
 p=A/name;old=p.read_text(encoding='utf-8');
 if text.strip() not in old:write(p,old+text)
# Source receipts identify exact bytes, without implying wholesale theorem acceptance.
sources=[PROTOCOL,TEAM/'BOARD.md',TEAM/'claude/B02/STREAM_NOTES.md',source_run/'FULL_PARTITION_CAPS.md',source_run/'CLAIMS.json',source_run/'out/GRAPH_CAP_FULL.json',HOME/'mop_fei100/reports/fei-2026-10-11/source_material/reductions/paper/forests.tex']
for folder in [HOME/'mop_fei100/reports/fei-2026-10-11',HOME/'mop_fei100/research_pushes/2026-10-11-full-fei-100-agents']:
 names=['README.md','CURRENT_STATUS.md','CLAIM_REGISTRY.json','OBSTRUCTION_REGISTRY.json','PACKET_STATUS.json','STREAM_NEXT_ACTIONS.json','FEI_100_agent_research_plan.tex'] if folder.name=='fei-2026-10-11' else ['CAMPAIGN.md','CLAIMS.md','COUNTEREXAMPLES.md','SEED_LEMMAS.md','NATIVE_MAPPING.md']
 sources.extend(folder/name for name in names)
sources.extend((TEAM/'context').glob('*.txt'))
dump(B/'out/SOURCES.json',[{'path':str(p),'sha256':digest(p),'bytes':p.stat().st_size} for p in sources])
receipt=HOME/'AppData/Local/Temp/lean_check/3abe421efc7f47f7b609d242f053d747'
if receipt.exists():
 copied=[]
 for p in receipt.iterdir():
  if p.is_file() and p.stat().st_size<100000:
   dst=B/'out'/('LEAN_'+p.name);dst.write_bytes(p.read_bytes());copied.append({'source':str(p),'saved':dst.name,'sha256':digest(dst)})
 dump(B/'out/LEAN_RECEIPTS.json',{'status':'RUNTIME_UNVERIFIED','seconds':53.557,'compiler_exit_code':None,'admission':'memok exit0;physical9.6GB;commit23.9GB','files':copied,'later_formal_source':'code/PairCone.lean NOT CHECKED'})
protocol=json.loads(PROTOCOL.read_text(encoding='utf-8'))['required_per_run']
for c in json.loads((B/'CLAIMS.json').read_text(encoding='utf-8')):
 assert set(c)==set(protocol['claim_fields'])
 assert c['statement_sha256']==claimhash(c)
expected=set(k.split(' (')[0] for k in protocol['progress_fields']);assert set(progress)==expected
assert (B/'PROGRESS.json').read_bytes()==(B/'PACKET_DELTA.json').read_bytes()
assert len((A/'STATUS.md').read_text(encoding='utf-8').splitlines())==2
for heading in protocol['report_fields']:assert '## '+heading in report
files=[p for p in B.rglob('*') if p.is_file() and p.name!='RECEIPTS.json'];assert all(p.stat().st_size<20_000_000 for p in files)
dump(B/'out/RECEIPTS.json',{'status':'PASS_LOCAL_PERSISTENCE_AND_SCHEMAS','generated_utc':datetime.now(timezone.utc).isoformat(),'files':[{'path':str(p.relative_to(B)),'bytes':p.stat().st_size,'sha256':digest(p)} for p in files],'rolling':[{'path':str(p),'sha256':digest(p)} for p in [A/'STATUS.md',A/'WORKLOG.md',A/'LEARNED.md']],'external_mirror':'UNVERIFIED'})
print(json.dumps({'status':'PASS','claims':2,'files':len(files),'assertions_successful_including_pilot_overlap':pilot['assertions']+check['assertions']+pair['assertions'],'n4_runs':3824,'strict_graph_improvements':61,'new_n4_worst_bit_gap_over_I':str(max(2*F(r['new_gap'])/F(r['I']) for r in check['rows'][:63]))}))
