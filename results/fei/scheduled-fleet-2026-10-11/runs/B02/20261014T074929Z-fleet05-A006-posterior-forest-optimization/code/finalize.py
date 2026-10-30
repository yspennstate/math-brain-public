from pathlib import Path
from fractions import Fraction as F
from datetime import datetime,timezone
import json,hashlib,copy
BASE=Path(__file__).resolve().parents[1]; AGENT=BASE.parents[1]
SHARED=Path('~/brain_workers/FEI100_20261011')
PROTOCOL=Path('~/mop_fei100/reports/fei-2026-10-11/EXECUTION_PROTOCOL.json')
def digest(p):return hashlib.sha256(p.read_bytes()).hexdigest()
def write(name,x):
    (BASE/name).write_text(json.dumps(x,indent=2,ensure_ascii=False)+'\n',encoding='utf-8')
def statement_hash(s,h):return hashlib.sha256(json.dumps({'statement':s,'hypotheses':h},sort_keys=True,separators=(',',':')).encode()).hexdigest()
protocol=json.loads(PROTOCOL.read_text(encoding='utf-8-sig'))
old=AGENT/'runs/20261014T035304Z-fleet05-A006-posterior-forest-optimization'
sourceA010=SHARED/'agents/A010/runs/20261014T062324Z-fleet05-A010-universal-residual-falsifier'
forest=Path('~/mop_fei100/reports/fei-2026-10-11/source_material/reductions/paper/forests.tex')
sources=[PROTOCOL,SHARED/'BOARD.md',SHARED/'claude/B02/STREAM_NOTES.md',forest,
         old/'ROOT_LAW_RELAXATION.md',old/'JOINT_EDGE_SLICE.md',old/'REVIEW_A008.md',
         sourceA010/'REPORT.md',sourceA010/'PROOF.md',sourceA010/'CLAIMS.json',sourceA010/'REVIEW_A006.md',sourceA010/'code/caps.py']
write('out/SOURCES.json',[{'path':str(p),'sha256':digest(p),'bytes':p.stat().st_size} for p in sources])
start_status=AGENT/'STATUS.md'
if not (BASE/'out/START_STATUS.md').exists(): (BASE/'out/START_STATUS.md').write_bytes(start_status.read_bytes())
star=json.loads((BASE/'out/STAR_FULL.json').read_text()); graph=json.loads((BASE/'out/GRAPH_CAP_FULL.json').read_text()); joint=json.loads((BASE/'out/CHECK_SUMMARY.json').read_text())
assert all(F(r['Gamma_cap'])<F(r['I'])/6 for r in star['rows'])
assert all(F(r['bit_gap_over_I'])<F(41,10) for r in graph['rows'])
validation={'star_full_gap_bits_below_I_over_3_cases':31,'graph_full_gap_bits_below_41I_over_10_cases':63,
            'graph_actual_distinct_runs':graph['actual_distinct_runs'],'graph_strict_cap_improvements':graph['strict_cap_improvements'],
            'graph_worst_bit_gap_over_I':graph['worst_bit_gap_over_I'],
            'reported_full_run_assertions':star['assertions']+graph['assertions']+joint['assertions'],
            'note':'reported counters exclude additional assertions inside imported independent ownership and matching enumerators',
            'prior_run_recovery':'Prior 035304 run retained untouched; its full job and ledgers were unconfirmed. Current stage actually executed the full n4 joint-slice census.',
            'helper_provenance':'Original star v1 executed at FROZEN_SPEC hash. Optional edges argument added for graph enumeration and separately frozen in FROZEN_SPEC_INCIDENCE; default-star mathematics unchanged.',
            'max_expected_memory_MB':100,'jobs_over_300_MB':0,'memok_required':False,'all_outputs':'PASS'}
write('out/VALIDATION.json',validation)
root_s='For every fixed finite family of distinct actual once-per-gate partition runs covering the positive nonempty squared Fourier spectrum, write complete output numerators W_A=sum_T k_AT lambda_T and D=sum_T pi_T lambda_T. With p_lambda(T)=pi_T lambda_T/D and K_AT=k_AT/pi_T, Q_A=K_A dot p_lambda. At any positive globally feasible weight vector h_T=sum_A P_A K_AT/Q_A and v=sum_A P_A satisfy p_lambda dot h=v. The complete actual bit cost C is within 2(max_T h_T-v) of its joint infimum over all feasible positive weights and all actual run posteriors in the SAME family. The simplex objective is convex; its relaxation supplies a lower bound without asserting that K is stochastic or that the physical all-weight objective is convex.'
root_h=['Fixed actual gate table, ordered covers, positive rarities and original queue; complete factors and nonempty-root conditioning retained',
        'Each gate visited at most once and owned subsets partition the output; no duplicate descriptions counted as runs',
        'Family and physical Boolean f fixed before choosing a Fourier output; positive output mass on positive nonempty spectrum',
        'C measured in bits; supporting objective G in natural units; ln2>1/2']
root={'claim_id':'A006-JOINT-ROOT-LAW-LOWER-CERTIFICATE','version':1,'exact_statement':root_s,'hypotheses':root_h,
      'statement_sha256':statement_hash(root_s,root_h),'contributors':['A006'],'proof_source':{'derivation':'ROOT_LAW_RELAXATION.md','validation':'out/CHECK_4.json'},
      'proof_dependencies':[{'source':str(forest),'sha256':digest(forest),'locator':'original conditioned queue and thm:posteriorforest','acceptance':'definition, no universal cost assumption'}],
      'review_records':[{'reviewer':'A010','verdict':'WHOLE_SOURCE_DOCUMENT_HOLDS_NO_REPAIR','source':str(sourceA010/'REVIEW_A006.md'),'source_sha256':digest(sourceA010/'REVIEW_A006.md'),
                         'reviewed_proof_sha256':digest(old/'ROOT_LAW_RELAXATION.md'),'scope':'whole unchanged proof document; formal claim registered in this stage after source-bound review'}],
      'status':'PROVED; SOURCE_DOCUMENT_INDEPENDENTLY_ACCEPTED_LOCALLY','supersedes':[],'refutes':[],'first_unproved_line':None,
      'next_consumers':['A010','A008','A009','A086','A094','Claude/B02','B20']}
s='For every finite positive width-two graph prime table with both endpoint orders and original queue, every nonempty k-edge root subset T and every nonnegative vertex-price certificate y satisfying y_u+y_v>=1 on T yield p_lambda(T)<=min(1,4^(1-k)(sum_v y_v)^(k-1)/k^k) for all positive graph-packing-feasible weights. Recomputing h from the entire distinct actual partition family and maximizing h dot p over these capped root laws gives a valid global joint weight/posterior bit-gap bound 2 Gamma_cap. For every star f_m=x0 AND OR_m, m>=2, the COMPLETE full partition numerators are W_B=lambda_B/32^k, W_{0}=sum_i lambda_i/32, and W_{0 union B}=lambda_B[a_k+b_k sum_(i outside B)lambda_i], where a_k=(k-1)!/(3*8^k*k*(k+1)), b_k=k!/(16*8^k*(k+1)*(k+2)). At uniform weights1/m the capped root LP reduces exactly to cardinalities and its bit gap is less than (91/24)I for every m. Exact rational certificates improve this to I/3 for every m=2,...,32. On all63 labelled nonempty n4 graph tables at weights1/(2 max degree), full partition recomputation and rational primal-dual certificates give bit gap less than (41/10)I, with57 strict improvements over the uncapped tangent gap. These are optimization-gap statements within the fixed full event family, not universal coding-cost payment.'
h=['Uniform physical Boolean signs; spectrum is actual squared Fourier spectrum; full positive graph edge prime table',
   'Both endpoint orders give singleton subset probability1/4 and pair probability1/6; full original chronological queue probabilities',
   'Fixed full partition event family with one root per source SCC; distinct complete runs, no overlapping owner blocks or repeated visits',
   'Positive weights globally packing-feasible; table/family fixed before sampling A; variance and complete bit cross-entropy distinguished from surrogate residual',
   'Cardinality reduction applies to relaxation at uniform star reference; all-weight infimum is not restricted to symmetric weights',
   'Finite graph census n4 only and star finite certificate m2..32 only; all-m star bound separately proved']
caps={'claim_id':'A006-FULL-PARTITION-INCIDENCE-CAP-CERTIFICATE','version':1,'exact_statement':s,'hypotheses':h,'statement_sha256':statement_hash(s,h),
      'contributors':['A006'],'proof_source':{'derivation':'FULL_PARTITION_CAPS.md','code':['code/star_full.py','code/incidence_caps.py'],'certificates':['out/STAR_FULL.json','out/GRAPH_CAP_FULL.json','out/VALIDATION.json']},
      'proof_dependencies':[{'claim_id':root['claim_id'],'version':1,'statement_sha256':root['statement_sha256'],'acceptance':'source document independently accepted by A010'},
                            {'claim_id':'A010-ROOT-LAW-GAP-OBSTRUCTION-AND-PACKING-CAPS','version':1,'statement_sha256':'8fe13a285543eed587ae80558a5a84279ee27e45240ee127db4b14005140ef84','acceptance':'whole unchanged claim independently reconstructed in REVIEW_A010.md; author code not imported'}],
      'review_records':[],'status':'AUTHOR_PROVED_AND_EXACT_CERTIFICATES; INDEPENDENT_REVIEW_PENDING','supersedes':[],'refutes':[],
      'first_unproved_line':None,'next_consumers':['A010','A008','A009','A014','A015','A086','A094','Claude/B02','B20']}
accepted=copy.deepcopy(json.loads((sourceA010/'CLAIMS.json').read_text(encoding='utf-8'))[1])
accepted['review_records'].append({'reviewer':'A006','verdict':'HOLDS_WHOLE_SCOPE_NO_REPAIR','source':str(BASE/'REVIEW_A010.md'),'source_sha256':digest(BASE/'REVIEW_A010.md'),'certificate':'out/A010_REVIEW_CERTIFICATES.json'})
accepted['status']='INDEPENDENTLY_ACCEPTED_LOCALLY; UNIVERSAL_EXTENSION_OPEN'
claims=[root,caps,accepted]
required_claim=set(protocol['required_per_run']['claim_fields'])
for c in claims:
    assert set(c)==required_claim
    assert statement_hash(c['exact_statement'],c['hypotheses'])==c['statement_sha256']
write('CLAIMS.json',claims)
next_action='On adjacent shared high-degree/leafless incidence, recompute full partition occupation numerator and exact spectral rows; use incidence-price root caps and posterior factorial credit to pay the complete cost, not merely its optimization gap. A010/A008/A086 independently review full-family formula and cap transfer.'
progress={'protocol_revision':protocol['revision'],'run_id':BASE.name,'stream':'B02','packet_id':'A006','gap_id':'B02-PIJ-COMPLETE-JOINT-WITNESS-PAYMENT','attempt_id':'A006-stage6-full-family-incidence-caps',
          'method':'Recover unfinished exact joint slices; independently review A010 whole; exhaustive ownership/SCC/chronological full partition enumeration; incidence-price LP caps and all-m cardinality proof',
          'mathematical_delta':'Full-family/all-m star optimization-gap bound91I/24; finite star m2..32 gap<I/3; full n4 graphs gap<41I/10,3824 actual runs,57 cap improvements; A010 whole HOLDS; recovered192 joint slices gap<=I/1e9',
          'deliverable_status':'COMPLETE_LOCALLY; MIRRORS_UNVERIFIED','mathematical_status':'SCOPED_THEOREM_PROVED; NEW_EXTENSION_REVIEW_PENDING; UNIVERSAL_PIJ_AND_FEI_OPEN',
          'claim_versions_used':[{'claim_id':accepted['claim_id'],'version':1,'statement_sha256':accepted['statement_sha256']},
                                 {'source':str(old/'ROOT_LAW_RELAXATION.md'),'sha256':digest(old/'ROOT_LAW_RELAXATION.md'),'acceptance':'whole-document A010 review consumed'}],
          'claims_created_or_changed':[{'claim_id':c['claim_id'],'version':c['version'],'statement_sha256':c['statement_sha256'],'change':'review appended' if c is accepted else 'registered'} for c in claims],
          'source_artifacts':['out/SOURCES.json','FULL_PARTITION_CAPS.md','ROOT_LAW_RELAXATION.md','JOINT_EDGE_SLICE.md','REVIEW_A010.md','REVIEW_A008.md','out/VALIDATION.json'],
          'next_consumers':['A010','A008','A009','A014','A015','A086','A094','Claude/B02','B20'],'next_action':next_action,
          'stagnant_substantive_attempts':0,'blockers':['Universal complete-cost payment on shared/leafless prime incidence is unproved; small tangent gap cannot pay complete reference cost','Supervisor mirror/public release not verified'],
          'packet_ids':['A006']}
required_progress={x.split(' (')[0] for x in protocol['required_per_run']['progress_fields']}
assert set(progress)==required_progress
write('PROGRESS.json',progress);write('PACKET_DELTA.json',progress)
report=f'''# exact target, quantifiers, hypotheses and units

A006/B02 latest stage {BASE.name}. Optimize positive globally fixed weights and distributions on distinct actual partition runs while retaining posterior witness entropy. Target C020/PI-J complete witness payment; this stage consumes A010's cap repair and resolves its missing FULL-event-family quantifier. Complete bit cost C and surrogate residual R are kept distinct. New precise theorem and quantifiers are in CLAIMS.json and FULL_PARTITION_CAPS.md. No universal FEI claim.

# sources actually read, revisions and theorem locators

Execution protocol revision {protocol['revision']} read in full; BOARD snapshot2026-10-14 07:47UTC and B02 lead notesv2 read; own prior STATUS and interrupted source drafts recovered. A010 stage062324 REPORT, PROOF, CLAIMS and REVIEW_A006 read as wholes: all-weight uncapped obstruction and cap LP are consumed. Original forests.tex queue, source-SCC partition definition and posterior theorem supply definitions. Prior campaign/papers and completed stage4 source chain remain the already-read baseline, not newly claimed literature review. out/SOURCES.json binds exact read artifacts. Lead's historical review-first direction is honored by whole A010 reconstruction; no new broad universal candidate opened.

# complete derivation or exact first unsupported line

FULL_PARTITION_CAPS.md exhausts every star ownership: pair hub owner inside B OR singleton hub owner outside B, with complete chronological factorials and distinct-run recovery. This gives exact full numerators, a cardinality LP without restricting the physical all-weight infimum, and Gamma_cap<91/48 for every m>=2, hence bit gap<(91/24)I. Vertex-price packing certificates give valid root caps for every graph table; h must be recomputed for the full family. REVIEW_A010.md independently reconstructs its ENTIRE unchanged claim, including the bounded-choice cost, all-weight obstruction, caps and all seven finite LP certificates, no repair. Its prior uncapped failure is a certificate obstruction, not variational-cost growth. Recovered JOINT_EDGE_SLICE.md and ROOT_LAW_RELAXATION.md retain their proofs and exact limitations. First unsupported universal line: pay C (or the full surrogate residual with its constants) by KI on arbitrary shared/leafless incidence. An optimization gap alone pays neither cost.

# executed validation with domain, arithmetic, commands and outputs

FROZEN_SPEC.json preceded star pilot/full and recovered n4 joint census. FROZEN_SPEC_INCIDENCE.json preceded the new shared/leafless census. All commands used python -X utf8 with code/star_full.py --pilot, code/star_full.py, code/check.py, code/incidence_caps.py --pilot and code/incidence_caps.py from this run path. Star pilot2 cases passed; full m2..32 cardinality certificates all have gap<I/3; independent exhaustive ownership on m2,3,4 checked191 distinct runs and three integer FWHT spectra. Full n4 graph census covers63 labelled nonempty tables,3824 DISTINCT full partition events, rational packing primal=vertex dual and capped LP primal=dual; every bit gap<41I/10 and57 strictly improve the uncapped gap. Worst graph is K4, exact ratio {graph['worst_bit_gap_over_I']}. Recovered joint census:63 tables,1540 matching-star traces,192 one-edge slices (180 interiors,6 upper boundaries,6 one-gate constants), each gap<=I/10^9. Reported full-run counters total{validation['reported_full_run_assertions']} plus enumerator internal assertions; actual full runtimes {star['seconds']:.6f}s, {joint['seconds']:.6f}s, {graph['seconds']:.6f}s. Fraction arithmetic and primal-dual equality only; no floating sign. Expected memory100MB; no job expected above300MB, memok not required. No dimension escalation. Outputs saved as soon as each job completed.

# proof dependencies and changed downstream conclusions

A010 root-law theorem whole-document acceptance is adopted before registering the recovered A006 source theorem. A010-ROOT-LAW-GAP-OBSTRUCTION-AND-PACKING-CAPS@1 now has A006 whole independent acceptance with unchanged statement hash. Its matching-star lower certificate was NEVER transferred to the larger family: this stage recomputes full coefficients. The new full-family/cardinality/price-cap extension awaits A010/A008/A086 independent review. Previous A008 occupation review survives the recovered full census. Old stage035304 remains untouched and lacks final ledgers: pilot evidence was present but full execution unconfirmed; this stage actually reran and saved the full census. No retrospective completion or mirror receipt invented. Universal PI-J/FEI remain OPEN.

# one next mathematical action and independent reviewer

{next_action}

# actual persistence receipts or precise save blocker

REPORT.md, CLAIMS.json, PROGRESS.json and byte-identical PACKET_DELTA.json are saved in this run, with code, proofs, frozen specs and exact outputs. code/finalize.py checks protocol key sets, every statement SHA256 and exact finite bounds; out/RECEIPTS.json records sizes/hashes after persistence. Rolling STATUS.md is exactly two lines; WORKLOG.md and LEARNED.md appended. Each artifact<20MB. Only A006 was written; no git/mail/brain mutation or external publication. Supervisor mirrors unverified.

## Universal bridge

This stage moves C020/PI-J whole-set witness cost by closing the full-family and all-dimensional star quantifiers in the global joint certificate: all stars now have a proved gap<91I/24, the31 frozen sizes improve to<I/3, and incidence-price caps apply without alteration to full shared/leafless partition families (63 exact n4 certificates,57 strict gains). It does not turn the already-paid star class into another FEI class result; it repairs the universal optimization interface that A010 showed fails without packing. What remains is an influence-paid COMPLETE numerator/reference cost on adjacent shared high-degree incidence, and eventually arbitrary Boolean prime tables. NEXT combines these transferable physical root constraints with full occupation factorial/posterior credit at that first unpaid overlap, the shortest available route toward universal payment rather than another fixed-reference or isolated-class calibration.
'''
(BASE/'REPORT.md').write_text(report,encoding='utf-8')
assert all('# '+heading in report for heading in protocol['required_per_run']['report_fields'])
assert report.rstrip().split('\n\n')[-2]=='## Universal bridge'
status='STATE: A006 stage6 saved: FULL partition star gap<91I/24 all-m and<I/3 m2..32;63 full n4 graph gap<41I/10,3824 actual runs,57 cap gains; A010 whole HOLDS;192 recovered joint slices PASS; FEI OPEN.\nNEXT: Pay complete full-family occupation numerator on adjacent shared high-degree/leafless incidence using exact spectral rows, vertex-price root caps and factorial posterior credit; A010/A008/A086 review.\n'
start_status.write_text(status,encoding='utf-8');assert len(status.splitlines())==2
now=datetime.now(timezone.utc).isoformat()
with (AGENT/'WORKLOG.md').open('a',encoding='utf-8') as f:
    f.write(f'\n{now} — {BASE.name}: recovered interrupted n4 census (63 tables/192 slices/21872 assertions); consumed A010 all-weight gap obstruction and independently accepted whole unchanged cap theorem. Derived exact FULL star numerator including outside singleton hub owner, all-m gap91I/24 and incidence vertex-price caps. Pilot/full exact star and graph jobs PASS;31 sizes gap<I/3,63 full graph gap<41I/10,3824 actual runs,57 cap gains. Reported full assertions25652 plus enumerator checks. Old incomplete run preserved; universal complete cost remains unpaid, independent extension review pending.\n')
with (AGENT/'LEARNED.md').open('a',encoding='utf-8') as f:
    f.write('\nStage6: Full partition star differs from matching-star when hub owner is an edge OUTSIDE the present leaf set. For k>=1, W_hub+B=lambda_B[(k-1)!/(3*8^k*k*(k+1)) + k!/(16*8^k*(k+1)*(k+2))*sum_outside lambda]. Every such ownership is a single rooted star; factorials count distinct chronological events. Full-family h has off-diagonal used-subset terms and must be recomputed before any lower transfer. Capped tangent LP reduces exactly by cardinality at uniform star reference without assuming symmetric physical weights. All-m Gamma_cap<91/48 proved with binomial and adjacent-binomial sums; bit gap<91I/24, finite m2..32<I/3. General k-edge root cap: min(1,4^(1-k)L_T^(k-1)/k^k), where any fractional vertex-cover dual supplies L_T. Rational matching/vertex-cover equality certifies L_T. Full n4 census3824 events gives gaps<41I/10 and57 strict cap gains. Small global optimization gap is not influence-payment of complete cost. A010 whole obstruction+finite cap claim independently HOLDS; Gamma uncapped diverges at EVERY star weight while an actual bounded-cost choice survives.\n')
assert (BASE/'PROGRESS.json').read_bytes()==(BASE/'PACKET_DELTA.json').read_bytes()
receipts=[]
for p in sorted(BASE.rglob('*')):
    if p.is_file() and p.name!='RECEIPTS.json' and '__pycache__' not in str(p):
        assert p.stat().st_size<20*1024*1024
        receipts.append({'path':str(p.relative_to(BASE)),'bytes':p.stat().st_size,'sha256':digest(p)})
for p in [AGENT/'STATUS.md',AGENT/'WORKLOG.md',AGENT/'LEARNED.md']:
    receipts.append({'path':str(p),'bytes':p.stat().st_size,'sha256':digest(p)})
write('out/RECEIPTS.json',{'created_utc':now,'command':'python -X utf8 code/finalize.py','artifacts':receipts,'mirrors':'UNVERIFIED','schema_checks':'PASS','statement_hash_checks':'PASS','exact_bound_checks':'PASS'})
print(json.dumps({'saved':str(BASE),'claims':len(claims),'protocol_checks':'PASS','artifacts':len(receipts),'full_reported_assertions':validation['reported_full_run_assertions'],'universal_FEI':'OPEN'}))
