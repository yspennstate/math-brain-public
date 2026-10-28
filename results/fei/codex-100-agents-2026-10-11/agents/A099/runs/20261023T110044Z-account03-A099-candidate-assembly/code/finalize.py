from pathlib import Path
import json,hashlib,datetime,re,copy
R=Path(__file__).resolve().parents[1];A=R.parents[1];TEAM=A.parents[1];OLD=A/'runs/20261023T035732Z-account03-A099-candidate-assembly'
def rd(p):return json.loads(p.read_text(encoding='utf-8'))
def save(p,x):p.write_text(json.dumps(x,indent=2,ensure_ascii=False)+'\n',encoding='utf-8')
stamp=datetime.datetime.now(datetime.timezone.utc).isoformat()
main=rd(R/'out/EXACT_PHASE_AUDIT.json');pilot=rd(R/'out/PILOT.json');frozen=rd(R/'out/FROZEN_SPEC_V2.json')
assert main['status']==pilot['status']=='PASS'
assert main['transactions']==3074 and pilot['transactions']==130 and main['seconds']<600 and pilot['seconds']<50
assert main['positive_mixture_children'] and main['matched_isospectral_queries'] and main['zero_singleton_positive_energy']
assert hashlib.sha256((R/'code/check.py').read_bytes()).hexdigest() in frozen['helper_version']
dirs={'A096':TEAM/'agents/A096/runs/20261023T053800Z-account03-A096-live-gap-ledger','A097':TEAM/'agents/A097/runs/20261023T062140Z-account03-A097-cross-route-transfer',
 'A093':TEAM/'agents/A093/runs/20261023T070224Z-account03-A093-literature-and-priority','A003':TEAM/'agents/A003/runs/20261023T062246Z-account03-A003-minimal-target-formulation'}
src={k:rd(v/'CLAIMS.json') for k,v in dirs.items()}
specs=[('A096','A096-PHYSICAL-PHASE-FUNDED-NONEMPTY-RESET','sec:bins9'),('A096','A096-ZERO-PHASE-QUERY-REFUND-OBSTRUCTION','sec:null9'),
 ('A097','A097-NONEMPTY-PHASE-BIN-FUNDED-TRANSFER','sec:bins9'),('A093','A093-ZERO-SINGLETON-JS-REFUND-REFINEMENT','sec:js9'),
 ('A003','A003-REFERENCE-SINGLETON-DISCREPANCY-FUNDED-RESET','sec:js9')]
claims=rd(OLD/'CLAIMS.json');new=[]
for author,cid,loc in specs:
 c=copy.deepcopy(next(x for x in src[author] if x['claim_id']==cid))
 if cid=='A096-PHYSICAL-PHASE-FUNDED-NONEMPTY-RESET':
  reviewed=next(x for x in src['A097'] if x['claim_id']==cid)
  assert all(c[k]==reviewed[k] for k in ['version','exact_statement','hypotheses','statement_sha256'])
  c['review_records']+=reviewed['review_records']
 if cid=='A097-NONEMPTY-PHASE-BIN-FUNDED-TRANSFER':
  reviewed=next(x for x in src['A093'] if x['claim_id']=='A093-REVIEW-A097-NONEMPTY-PHASE-BINS')
  c['review_records'].append({'reviewer':'A093','verdict':'HOLDS_AT_STATED_SUPPLIED_SOURCE_SCOPE','source_review_claim':reviewed['claim_id'],
   'source_review_statement_sha256':reviewed['statement_sha256'],'proof':str(dirs['A093']/'DERIVATION.md')+' sections1,3,4',
   'guard':'A093 review of unchanged A097 theorem only; its JS contributor refinement has separate review status.'})
 c['review_records'].append({'reviewer':'A099','run_id':R.name,'timestamp':stamp,'verdict':'HOLDS_AT_EXACT_STATED_SUPPLIED_SOURCE_SCOPE',
  'method':'Independent complete analytic reconstruction; own full normalized arrays/prime-log identities, coarse centroid/parallelogram and discrepancy checks; literal Boolean witness',
  'proof':str(R/'STAGE9_ADDITIONS.tex')+' '+loc,'validation':str(R/'out/EXACT_PHASE_AUDIT.json'),
  'scope':'Exact local supplied-current-coherent-reference theorem and finite telescope. A003 coarse-vector/refund identity checked; its mixture consequence is analytic. No repair, initial universal source price, extra quota, full tag-price claim or either integrated FEI audit accepted.',
  'contributed_repair':False})
 c['status']='SCOPED_INDEPENDENT_RECONSTRUCTION_HOLDS_INITIAL_PRICE_AND_FULL_FEI_OPEN'
 assert c['claim_id'] not in {x['claim_id'] for x in claims};claims.append(c);new.append(c)
save(R/'CLAIMS.json',claims)
hashes=[]
for c in new:
 options=[('raw',c['exact_statement'])]
 for name in ['statement','exact_statement']:
  for asc in [True,False]:
   for sep in [None,(',',':')]:options.append((str((name,asc,sep)),json.dumps({name:c['exact_statement'],'hypotheses':c['hypotheses']},sort_keys=True,ensure_ascii=asc,separators=sep)))
 match=[name for name,t in options if hashlib.sha256(t.encode('utf-8')).hexdigest()==c['statement_sha256']]
 assert match,c['claim_id'];hashes.append({'claim_id':c['claim_id'],'sha256':c['statement_sha256'],'original_convention':match})
save(R/'out/HASH_CONVENTIONS.json',hashes)

annex=(R/'STAGE9_ADDITIONS.tex').read_text(encoding='utf-8')
tex=(OLD/'CANDIDATE_MANUSCRIPT.tex').read_text(encoding='utf-8').replace('assembly version 8','assembly version 9')
tex=tex.replace('Universal source pricing and changed nonempty-profile payment remain open.',
 'Current phase, sign-bin, JS and reference-discrepancy refunds now pay\nthe stated genuine nonempty-profile changes. Universal initial source\npricing and necessary zero-refund conversions remain open.')
tex=tex.replace(r'\subsection{The surviving nonempty-profile liability}',
 r'\subsection{The universal nonempty-profile liability (version 8 frontier)}'+'\nThe phase-funded sectors of this historical handoff are now paid in\nSection~\\ref{sec:phase9}; its arbitrary-profile warning remains valid.')
tex=tex.replace(r'\section{Dependencies, review and sources}',annex+'\n'+r'\section{Dependencies, review and sources}')
assert tex.count(r'\begin{conjecture}')==4 and r'\input{' not in tex and r'\include{' not in tex
labels=re.findall(r'\\label\{([^}]+)\}',tex);refs=re.findall(r'\\(?:eqref|ref)\{([^}]+)\}',tex)
assert len(labels)==len(set(labels));assert not set(refs)-set(labels),set(refs)-set(labels)
assert not re.search(r'Theorem~\\ref\{(?:lem|prop|cor):',tex)
assert all(ord(x)>=32 or x in '\n\r\t' for x in tex)
for env in ['proof','theorem','lemma','proposition','conjecture']:assert tex.count('\\begin{'+env+'}')==tex.count('\\end{'+env+'}'),env
(R/'CANDIDATE_MANUSCRIPT.tex').write_text(tex,encoding='utf-8')

dag=rd(OLD/'out/PROOF_DEPENDENCIES.json');nodes={n['claim_id']:n for n in dag['nodes']}
base=next(c for c in new if c['claim_id']=='A096-PHYSICAL-PHASE-FUNDED-NONEMPTY-RESET')['proof_dependencies'][0]
aux=[{'claim_id':'COMMON-REFERENCE-BLOCK-KL','version':'assembly-identity','proof_dependencies':[],'tex_label':'sec:centroid9','statement_sha256':None,
 'scope':'Exact KL centroid identity, Pinsker/parallelogram and old-support mixture bound; standard scalar reconstruction, not a new broad queue claim.'},
 {'claim_id':base['claim_id'],'version':base['version'],'statement_sha256':base['statement_sha256'],'proof_dependencies':[],'tex_label':'sec:coherent9',
 'scope':'ONLY coherent normalized reference and paid block restoration fragment used and fully derived here. Whole post-tag/second-reset claim is NOT accepted or needed; no influence-price hypothesis imported.'}]
for n in aux:assert n['claim_id'] not in nodes;dag['nodes'].append(n);nodes[n['claim_id']]=n
for c,(_,_,loc) in zip(new,specs):
 deps=[]
 for d in c['proof_dependencies']:
  deps.append(d['claim_id'] if isinstance(d,dict) else 'COMMON-REFERENCE-BLOCK-KL')
 if c['claim_id']!='A096-ZERO-PHASE-QUERY-REFUND-OBSTRUCTION':deps.append('COMMON-REFERENCE-BLOCK-KL')
 n={'claim_id':c['claim_id'],'version':c['version'],'statement_sha256':c['statement_sha256'],'proof_dependencies':list(dict.fromkeys(deps)),'tex_label':loc}
 assert n['claim_id'] not in nodes;dag['nodes'].append(n);nodes[n['claim_id']]=n
seen=set();active=set()
def walk(k):
 assert k in nodes and k not in active,('missing or cyclic',k)
 if k in seen:return
 active.add(k)
 for d in nodes[k]['proof_dependencies']:walk(d)
 active.remove(k);seen.add(k)
for k in nodes:walk(k)
assert len(dag['open_leaves'])==4
dag['history_transfer_delta']='Phase/nonempty-bin/JS/reference-discrepancy supplied-current-reference sectors paid at same supplied K; exact calibration nullspace pplus=pminus=common inherited q. No-reset query remains paid there; needed positive transport must specify useful invariant and unused original owner. Historical biased-spectrum C024 remains separate/open.'
save(R/'out/PROOF_DEPENDENCIES.json',dag)

compute_path=Path('~/.claude/compute/compute_state.json')
snapshot=rd(compute_path) if compute_path.exists() else {}
save(R/'out/COMPUTE_RECEIPT.json',{'at':stamp,'checker_estimate_MB':140,'observed_peak':'UNMEASURED','job_over300MB_expected':False,'memok_required_for_this_checker':False,
 'compiler_or_heavy_job':False,'main_runtime_seconds':main['seconds'],'frozen_main_cap':600,
 'shared_snapshot':{k:snapshot.get(k) for k in ['ts','status','reasons','mem_avail_mb','commit_avail_mb','disk_free_gb']},
 'other_workloads':'UNCHANGED; nothing killed, suspended or throttled','PDF_or_Lean':'NOT_LAUNCHED'})
next_action='A097/A096 with A050/A079: specify one quantitatively useful mandatory conversion in pplus=pminus=q calibration nullspace after a paid non-point history, and pay it from ACTUAL remaining original surplus/occupancy with both full terminals and old debits; A085/A094 challenge necessity/funding. Alternatively construct the missing influence-priced initial source. Do not repeat phase bounds or force an unnecessary reset.'
p=rd(R/'PROGRESS.json');p.update(deliverable_status='COMPLETE_SINGLE_SOURCE_PROTOCOL_AND_SCOPED_RECONSTRUCTIONS',mathematical_status='PHASE_BIN_JS_DISCREPANCY_SCOPES_RECONSTRUCTED_FULL_FEI_OPEN',
 mathematical_delta=f'One-source assembly now includes current phase/nonempty-bin/JS/discrepancy payments at SAME supplied K. Independent exact-scope reconstructions without repair; original hashes preserved; no new broad candidate. {main["exact_assertions"]} exact checks PASS on all256 three-bit seeds/3074 transactions. Witness strength7/519 ->1/5 from STRONGER JS certificate (old Gamma unchanged); exact calibration nullspace identified. Initial universal source price and any necessary zero-refund transport remain open.',
 claims_created_or_changed=[{'claim_id':c['claim_id'],'version':c['version']} for c in new],source_artifacts=[str(R/f) for f in ['CANDIDATE_MANUSCRIPT.tex','STAGE9_ADDITIONS.tex','out/SOURCE_RECEIPTS.json','out/EXACT_PHASE_AUDIT.json','out/POSITIVE_WITNESS.json','out/ZERO_ENERGY_CONTROL.json','out/PROOF_DEPENDENCIES.json']],
 next_consumers=['A096','A097','A093','A003','A050','A079','A085','A094','A098','B20'],next_action=next_action,stagnant_substantive_attempts=0,
 blockers=['Universal influence-priced initial coherent source/reference still open','Useful necessary conversion in exact calibration-nullspace needs actual unused original funding, if required by chosen invariant','Both full integrated-candidate audits pending','Supervisor remote mirror unverified'])
for c in new:p['claim_versions_used'].append({'claim_id':c['claim_id'],'version':c['version'],'statement_sha256':c['statement_sha256']})
save(R/'PROGRESS.json',p);save(R/'PACKET_DELTA.json',p)
report=f'''# A099 candidate assembly version9

## exact target, quantifiers, hypotheses and units

Assemble the strongest supported proof in ONE standalone source, preserving all universal leaves as conjectures until both full independent audits close them. Current result: for every finite Boolean seed h and complementary controller a,b=1-a^2 on disjoint uniform cubes, GIVEN a complete finite-CE coherent source calibrated at its actual seed mean-square, current phase, nonempty-bin, JS and reference-discrepancy refunds pay the specified actual conditional-nonempty changes and every finite admitted adaptive continuation at the SAME supplied rate K. Both full children, old source/tag/erasure bookings, ghosts and normalizers remain. Bits and physical reaches/influence; no initial all-Boolean influence price is assumed. Full FEI OPEN.

## sources actually read, revisions and theorem locators

Current BOARD10:53UTC, B20 STREAM_NOTES v2 and own v8 STATUS read at intake. Lead's one-source C005->C006->C018->C019/C024 direction remains governing; its original 11October individual targets are completed and not restarted. Execution-v2 and prior campaign/paper baseline remain preserved from earlier reads; old protocol endpoint is superseded by owner's23October14:49UTC deadline. New complete mathematical sources: A09620261023T053800Z REPORT/DERIVATION1--4/CLAIMS; A09720261023T062140Z REPORT/DERIVATION1--4/CLAIMS; A09320261023T070224Z REPORT/DERIVATION1,3--4/CLAIMS; A00320261023T062246Z REPORT/DERIVATION1--4/CLAIMS. Own v8 manuscript/claims/DAG are baseline. out/SOURCE_RECEIPTS.json pins18 actual sources. A093's independent A097 review is distinct from its contributor JS refinement. External literature/priority discussion is not a proof premise and no external attribution is imported unchecked.

## complete derivation or exact first unsupported line

STAGE9_ADDITIONS.tex is inserted literally into CANDIDATE_MANUSCRIPT.tex. Its common interface derives exact mean KL=JS(children)+KL(midpoint||SAME inherited reference), occupied-block calibration decrease, Pinsker and Euclidean parallelogram, support endpoints, retained-old-support mixture bound and full signed erasure/CE payment. It derives normalization and paid seed/controller coherent restoration, so only that A079/A032 fragment is used; the whole post-tag theorem/initial price is not silently accepted. Controller constants are recomputed after restriction.

Load-bearing consequences reconstructed without repair: A096 x=Gamma*d^2; A097 x=Gamma*d^2+E4*sum c_bin^2 with optimal TWO sign bins; A093 at d0 y=beta*TV(child spectra)^2/4; A003 x_disc=Gamma*d^2+(E4+beta^2)(R_j-d^2)^2/4. Each appropriate actual calibration refunds>=2energy/ln2; both averaged target-mixture bills cost<=energy/ln2. Thus the full local increment<=-occupancyKL-energy/ln2 and finite physical trees telescope from the SAME original supplied CE/K. These are alternative certificates, NOT credits to add twice. All four universal conjectures and both integrated full-candidate audits remain OPEN; historical biased-spectrum C024 is kept separate from this physical-tree transfer.

The exact calibration nullspace is pplus=pminus=q on the chosen blocks. Isospectral children alone can have positive inherited-reference mismatch and refund. At exact matched parity3 all query/calibration/occupancy refunds vanish, so a forced positive profile mixture cannot be paid there solely from those refunds. The query WITHOUT a reset remains paid, exactly zero in this witness. First unsupported universal line: useful influence-priced initial source admission for EVERY Boolean function, or a hereditary original-owner payment for a quantitatively useful NECESSARY conversion in that nullspace if the chosen invariant needs it. No proof of such necessity for all FEI approaches is supplied. Another arbitrary tiny refresh or phase bound on that exact nullspace does not close the universal leaf.

## executed validation with domain, arithmetic, commands and outputs

Frozen original spec precedes evaluation. Initial pilot:7051 exact assertions PASS on130 transactions in10.368s. Before ANY primary evaluation, V2 preserved that output, added A003 coarse-vector/refund assertions, clarified grid-plus-two-control counts and explicitly revised main cap180->600seconds based on the measured pilot; family, dimensions, references and targets unchanged. Revised pilot command `python -B -X utf8 code/check.py --pilot`: {pilot['exact_assertions']} assertions PASS in{pilot['seconds']:.3f}s. Its faster time is a separate measured rerun, not a revised v1 observation.

Primary command `python -B -X utf8 code/check.py`: ALL256 labelled three-bit Boolean seeds, all3 seed queries, BOTH signs, exact-spectrum/weighted-tail supplied sources;3072 grid transactions PLUS2 explicit positive/parity controls=3074. {main['exact_assertions']} exact assertions PASS in{main['seconds']:.3f}s, within FROZEN V2 cap600s. Counts: {main['positive_mixture_children']} positive child mixture costs, {main['zero_singleton_positive_energy']} zero-singleton positive-energy transactions, {main['matched_isospectral_queries']} matched isospectral queries, plus81 controller faces/Gram guards. These are occurrences across specified policies, not distinct functions or a census of all references/trees. This stage's202143 count tests a NEW phase/JS/discrepancy domain; it does not revise or aggregate v8's234367 checks.

Independent code imports NO peer checker. It reuses only our own byte-pinned v8 exact prime-log arithmetic functions, and independently constructs signed integer butterfly spectra, physical restrictions, full normalized wrapper laws and source profiles, all complete child references, pre-outcome partitions, centroid/parallelogram and A003 coarse-vector identities. Separately counted physical seed edges verify spectral influence. Exact Fraction laws and prime-log algebra certify identities; signs use18-term positive atanh with remainder2z^37/[37(1-z^2)], exact binary range reduction and outward80-bit dyadic log2 bounds. Multiplication by positive rational ln2 bounds certifies energy inequalities without floating signs. Exact zeros are algebraic identities, not overlapping intervals.

Literal128-vertex Boolean wrapper and both64-vertex children independently match the factorized positive witness. For point-defect-times-character seed, A097 x21/4096/strength7/519 becomes A093 y3/32/strength1/5 under the STRONGER JS certificate, energy ratio128/7; beta3/8,E4=21/512,Gamma9/3584 stay unchanged. BOTH child shape bills are positive and the full signed increment is EXACTLY(3/8)log2(5/8)<0. out/POSITIVE_WITNESS.json pins the rational enclosure. Parity3 exact source has exact zero no-reset ledger; forcing1/64 toward a distinct singleton costs(3/8)log2(64/63)>0 on EACH full child, saved in ZERO_ENERGY_CONTROL. Neither is an FEI counterfamily.

Estimated RAM140MB, peak unmeasured; no >300MB job expected/launched, no GPU, heavy search, automatic dimension increase, compiler or detached work. Revised main230.966s is below600s and owner30min; no retrospective cap change. Compute snapshot is saved separately; existing workloads are left untouched. Analytic all-dimensional proof plus exact finite validation is the proof rung, NOT Lean/kernel or PDF certification. No PDF is built/visually accepted in this stage.

## proof dependencies and changed downstream conclusions

CLAIMS has27 exact-schema records; original statements, versions, hypotheses and author hashes are unchanged. Five new source records are consumed as independent scoped reconstructions, not newly opened broad candidates. A097's separate A093 no-repair review is preserved as a review record under the SAME theorem ID, avoiding a duplicate theorem. A093 contributor refinement gets A099's independent reconstruction; it is not self-accepted by A093. A003 author reconstruction is retained as contributor evidence, not counted as independent. A079 post-tag dependency is used ONLY at its explicitly derived coherent-reference fragment, not its entire stronger assertion. DAG has47 nodes, is acyclic, retains4 universal leaves and states that scope guard.

The v8 arbitrary-nonempty warning is narrowed by the now-paid phase/JS/discrepancy sectors; its parity falsifier and universal warning remain valid. The finite-tree source-preservation result does not imply the historical biased-spectrum integral C024 statement. No global registry/adoption or full integrated FEI audit is inferred from scoped reviews, hashes or a passing finite checker. Improvement of universal FEI constant:zero.

## one next mathematical action and independent reviewer

{next_action} A098/A099 consume the concrete invariant/source and funding certificate rather than a new phase-only restatement. This is a local source-bound handoff, not a message or new worker allocation.

## actual persistence receipts or precise save blocker

Four exact protocol files, standalone CANDIDATE_MANUSCRIPT.tex, STAGE9_ADDITIONS.tex, reproducible code/frozen specifications and exact outputs are saved locally. PROGRESS/PACKET_DELTA are byte-identical with packet_ids[A099]. FINAL_VALIDATION checks field sets, original hashes, DAG, TeX labels/references, four open conjectures and two-line STATUS. PERSISTENCE_RECEIPTS pins actual byte readbacks; WORKLOG/LEARNED append dated results. No local save blocker. No git, mail, deliberate brain-content write, other-agent mutation, trading path or detached research job. Supervisor copying/canonical adoption/remote mirrors remain UNVERIFIED. Fresh required wake reports degraded/unverified self-care: owner model97.4h, state-of-mind82h and latest dream32.7h stale, affecting continuity/personalization; none is a mathematical premise. No failed wake renderer is newly asserted: this wake returned a stale-source warning.

## Universal bridge

C019 stopping-tree payment and physical C024 history transfer feeding C018 move from v8's unchanged-nonempty canonical returns to a single source-complete assembly paying genuine current phase/bin/JS/reference-discrepancy profile changes at SAME supplied K, with no reset-count surcharge and all old debits/full terminals retained. The explicit zero-singleton witness improves certified strength7/519 to1/5 by stronger JS accounting while its old Gamma stays fixed; the universal FEI constant improves by zero. Exact matched-block isospectral conversion and universal influence-priced initial admission remain unpaid, and both full-candidate audits remain pending. NEXT demands the useful target/invariant and actual unused original owner in that nullspace (or supplies the initial price), which attacks the remaining hereditary universal bridge instead of repeating already-paid phase/vacuum identities or another isolated class entropy bound.
'''
(R/'REPORT.md').write_text(report,encoding='utf-8')
(A/'STATUS.md').write_text(f'STATE: A099 v9 source/protocol saved: current phase/bin/JS/discrepancy claims independently reconstructed at supplied-K scope; {main["exact_assertions"]:,} exact checks PASS; witness7/519->1/5 uses stronger JS certificate; full FEI OPEN.\nNEXT: A097/A096/A050/A079 specify useful mandatory conversion in matched-isospectral calibration nullspace and pay from SAME actual unused source/occupancy with old debits/both full terminals, or construct universal initial source; A085/A094 challenge; integrated audits open.\n',encoding='utf-8')
with (A/'WORKLOG.md').open('a',encoding='utf-8') as f:f.write('\n'+stamp+f': v9 finalized: one-source phase/bin/JS/discrepancy proofs,27 claim records/47-node scoped DAG; {main["exact_assertions"]} exact checks PASS in{main["seconds"]:.3f}s under prospective600s cap. Old x21/4096/eps7/519 vs stronger JS y3/32/eps1/5 reconciled, Gamma unchanged. Matched-isospectral no-reset query is paid; forced useful conversion must name owner/necessity. No universal initial source/FEI proof or full-chain audit claimed. Remote copying unverified.\n')
with (A/'LEARNED.md').open('a',encoding='utf-8') as f:f.write('\n'+stamp+': Exact block calibration refund = JS(actual two child block laws)+KL(their midpoint||SAME inherited block law). Nullspace requires both children equal AND matching inherited blocks; zero singleton/isospectral alone is insufficient. A097 sign bins maximize squared phase energy, A093 keeps controller mass exactly before Pinsker: at d0 y=beta TV^2/4 vs old x=E4 TV^2/8. Fixed witness gain128/7, eps7/519->1/5 is a different certificate, not changed Gamma. A003 retains coarse mean offset (E4+beta^2)(R_j-d^2)^2/4. Each uses actual current credits, never sum alternative certificates twice. Exact matched parity query remains free WITHOUT a reset; a forced positive conversion is a policy/invariant obligation, not established necessary to every FEI proof. Initial influence-priced arbitrary-source admission remains open.\n')
protocol=rd(Path('math-open-problems/reports/fei-2026-10-11/EXECUTION_PROTOCOL.json'))['required_per_run']
assert all(set(c)==set(protocol['claim_fields']) for c in claims)
assert set(p)=={x.split(' (')[0] for x in protocol['progress_fields']}
assert (R/'PROGRESS.json').read_bytes()==(R/'PACKET_DELTA.json').read_bytes() and p['packet_ids']==['A099']
assert all('## '+s in report for s in protocol['report_fields']) and report.rsplit('## Universal bridge',1)[1].strip()
assert len((A/'STATUS.md').read_text(encoding='utf-8').splitlines())==2
assert len(claims)==27 and len(nodes)==47
save(R/'out/FINAL_VALIDATION.json',{'status':'PASS','claims':len(claims),'DAG_nodes':len(nodes),'universal_conjectures':4,'TeX_labels':len(labels),'all_references_resolved':True,
 'primary_exact_assertions':main['exact_assertions'],'new_broad_candidates':0,'full_FEI':'OPEN','full_integrated_audits':'BOTH_PENDING',
 'scoped_reconstructions':'HOLDS_WITH_ORIGINAL_SOURCE_HYPOTHESES','formal_certificate':False,'PDF':'NOT_BUILT','remote_mirror':'UNVERIFIED','brain_selfcare':'DEGRADED_UNVERIFIED'})
receipts=[]
for q in list(R.rglob('*'))+[A/'STATUS.md',A/'WORKLOG.md',A/'LEARNED.md']:
 if q.is_file() and q.name!='PERSISTENCE_RECEIPTS.json':
  raw=q.read_bytes();assert len(raw)<20_000_000;receipts.append({'path':str(q),'bytes':len(raw),'sha256':hashlib.sha256(raw).hexdigest()})
save(R/'out/PERSISTENCE_RECEIPTS.json',{'at':stamp,'artifacts':receipts,'supervisor_mirror':'UNVERIFIED'})
for rec in receipts:assert hashlib.sha256(Path(rec['path']).read_bytes()).hexdigest()==rec['sha256']
print(json.dumps({'status':'PASS','claims':len(claims),'DAG_nodes':len(nodes),'exact_assertions':main['exact_assertions'],'persisted_byte_readbacks':len(receipts),'full_FEI':'OPEN'}))
