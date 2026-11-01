"""Write only local, reviewable P0104 artifacts. Never submit or ingest."""
import hashlib
import json
from pathlib import Path

R=Path(__file__).resolve().parent
for name in ['drafts','review','outbox','proposals']:
    (R/name).mkdir(exist_ok=True)
def write(name,value):
    (R/name).write_text(json.dumps(value,indent=2,ensure_ascii=False)+'\n',encoding='utf-8')

source_status={
 'task':'P0104','worker':'w370','as_of':'2026-10-10','current_openness':'UNKNOWN',
 'primary_target':{'title':'50 years of first-passage percolation','authors':['Auffinger','Damron','Hanson'],
   'url':'https://arxiv.org/pdf/1511.03262','section':'3.1; equation (3.1); Questions 13 and 15',
   'locations_as_read':'Equation: printed pages 33-34; both questions: printed page 36 (zero-based PDF page 36).',
   'exact_mathematical_content':'For iid nonnegative nearest-neighbor lattice FPP, establish a variance fluctuation exponent chi<1/2 for d>=2 under suitable distributional conditions; obtain chi=1/3 for d=2, and chi>0 in suitable dimensions. The source does not specify all suitable conditions or one meaning of its asymptotic symbol.',
   'short_quotes':['under suitable conditions on F','For suitable d, show that χ > 0.'],
   'scope_notes':'The surrounding discussion allows ratio convergence, two-sided comparability, or exponent-only n^(2chi+o(1)); it expects mild moment conditions and no flat edges. None is silently asserted for every continuous law.'},
 'precise_specialization':{'graph':'undirected nearest-neighbor Z^2','edge_weights':'iid Exp(1)',
   'passage_time':'T_n = inf over finite paths from (0,0) to (n,0) of the sum of edge weights',
   'target':'lim_n log Var(T_n)/(2 log n) = 1/3',
   'quantifiers':'one fixed law and direction; limit along all integers n -> infinity',
   'not_automatic':'positive limiting Var(T_n)/n^(2/3), weak limit law, curvature, or universality over all laws'},
 'known_inputs':[
   {'url':'https://arxiv.org/pdf/1306.1197','version':'v2','theorem':'1.1',
    'hypotheses':['d>=2','iid nonnegative edge weights with Borel law mu','mu({0})<p_c(d)','E t_e^2 (log t_e)_+<infinity'],
    'conclusion':'For lattice x with ||x||_1>1, Var T(0,x)<=C(mu,d)||x||_1/log||x||_1.',
    'gap_to_target':'Only chi_var<=1/2; no fixed polynomial saving or matching KPZ lower bound.'},
   {'url':'https://arxiv.org/html/1401.0917v2','theorem':'1.1, two-sided assertion (1.5)',
    'hypotheses':['d>=2','iid nonnegative edge weights','mu({0})<p_c(d)','E exp(2 alpha t_e)<infinity for some alpha>0'],
    'conclusion':'P(|T(0,x)-ET(0,x)|>=lambda sqrt(||x||_1/log||x||_1))<=c1 exp(-c2 lambda), all lambda>=0 and ||x||_1>1.',
    'gap_to_target':'This is a larger deterministic scale, not the unknown actual standard deviation. Our rare-event sequence satisfies such a tail bound but has variance exponent 3/8.'},
   {'url':'https://arxiv.org/html/2604.01214v1','theorem':'Section 2.1.1, Theorem 2.1',
    'scope':'Rotationally invariant Riemannian FPP model under the paper-specific framework; Q_n comparable to standard deviation.',
    'full_lattice_hypotheses_verified':False,
    'gap_to_target':'Canonical iid lattice Exp(1) FPP has no established transfer to these model assumptions. No application made.'}],
 'history_checked':[
   {'path':'~/<private-repo>/06_math_research/probability_1000_intake_claude_20260907/RANKING_2026-09-07.csv','line':550,'result':'Historical tier 5 / attempted_un only.'},
   {'artifact':'canonical_target_card.json','node_id':'claim_32684d2ece2943d218971312722a87f42333b030b9c7a29f034d6c11f31f8f1d','result':'Current store marks the original problem as unverified, historical attempted_unsolved.'},
   {'artifact':'exact_target_cards.json','node_id':'claim_9ffe9930e9d9ed5c9d98ff4d61a32155d942cd754628487fc173a2d2c6493b2f','result':'The old attempt already contains the n/log n exponent gap; the initial independent obstruction is not new.'},
   {'artifact':'target_nodes.json','result':'Owner FPP campaign correction retains an unavailable uniform engine/transport implication and explicitly leaves chi=1/3 unmoved; no owner solution inferred.'},
   {'paths':['probability_1000_attempts_H_20260912','probability_1000_attempts_I_20260914','prob1000_lean_20260908'],
    'result':'Targeted P0104 scans found no new matched proof in H/I; Lean annotated ranking repeats attempted_un. This is a limited search, not a complete retirement audit.'},
   {'path':'~/math-research-brain/local/population','result':'Expected canonical store location absent; used the explicitly named live population store read-only instead.'}],
 'literature_check':'Targeted public primary searches and the 2026 Riemannian paper establish no solution for the fixed lattice target. Current global openness remains UNKNOWN.',
 'formal_check':{'executed':False,'theorem':None,'assumptions':None,'trusted_axioms':None,'admitted_placeholders_counted':False},
 'brain_scar':'perceptron_proof_open_gaps_fleet_2026_07_12',
 'source_checks_are_mathematical_proofs':False
}
write('SOURCE_STATUS.json',source_status)

src={'source_id':'owner:w370:p0104-independent-bridge-20261010','url':str(R/'INDEPENDENT_BRIDGE.md'),
     'revision':'draft-2026-10-10','license':'owner-own-work (campaign derivation; independent referee pending)','excerpt':None}
def entry(key,logical,title,statement,assumptions,kind='concept'):
    return {'key':key,'namespace':'probability.fpp','logical_name':logical,'kind':kind,'title':title,
            'statement':statement,'proof_text':None,'assumptions':assumptions,'domain':'probability; FPP bridge audit','source':src.copy()}
entries=[
 entry('variance-exponent','variance-fluctuation-exponent-in-a-fixed-direction','Variance fluctuation exponent in a fixed direction',
       'For a sequence of real random variables T_n with 0<Var(T_n)<infinity, its variance fluctuation exponent is chi_var=lim_{n->infinity} log Var(T_n)/(2 log n), if this limit exists. This definition concerns variance only; it does not assert a weak limiting law or equivalence to a typical-fluctuation or transversal exponent.',
       ['Positive finite variances','The limit is asserted only when it exists'],kind='definition'),
 entry('uniform-kurtosis-bridge','weak-scaling-to-variance-with-uniform-standardized-fourth-moments','DRAFT conditional weak-scaling to variance bridge',
       'DRAFT concept; referee pending. Let X_n be real with 0<sigma_n^2=Var(X_n)<infinity and E|X_n-EX_n|^4<=K sigma_n^4 for one finite K and every n. For positive a_n and deterministic m_n, if (X_n-m_n)/a_n converges weakly to a nondegenerate real Z, then Z has finite positive variance and Var(X_n)/a_n^2 converges to Var(Z). No independence across n is required. The proof is recorded in the campaign audit; neither this moment condition nor n^(1/3) nondegenerate weak scaling has been established here for iid planar lattice FPP.',
       ['One uniform standardized fourth-moment constant K','Nondegenerate weak limit at the asserted scale','Deterministic centers; positive scales']),
 entry('weaker-route','larger-scale-concentration-does-not-justify-kpz-variance','Refuted candidate replacement of moment control by larger-scale concentration',
       'DRAFT refuted route. The candidate inference says that nondegenerate n^(1/3) weak scaling, a uniform exponential tail bound for centered fluctuations at sqrt(n/log n), and a variance upper bound C n/log n force variance exponent 1/3. This inference is false for arbitrary random-variable sequences; the rare-event countermodel in this bundle satisfies those premises and has variance exponent 3/8. No claim of an iid lattice FPP counterexample is made.',
       ['Abstract random-variable sequences, not a lattice model']),
 entry('rare-event','rare-event-obstruction-to-kpz-variance-from-weak-scaling','DRAFT rare-event obstruction retaining subdiffusive-scale tails',
       'DRAFT concept; independent referee pending. For n>=4, put a_n=n^(1/3), s_n=sqrt(n/log n), and p_n=n^(-1/4). Let Z,S be independent symmetric signs and B_n an independent Bernoulli(p_n). Set Q_n=n+a_n Z+s_n B_n S. Then (Q_n-n)/a_n converges weakly to a symmetric sign, Var(Q_n)=n^(2/3)+n^(3/4)/log n, and chi_var=3/8. Moreover P(|Q_n-EQ_n|>=t s_n)<=exp(2.1-t) for every t>=0, Var(Q_n)<=(3/e+1)n/log n, and the standardized fourth moment is asymptotic to n^(1/4). These are abstract sequence statements and do not establish or refute lattice KPZ.',
       ['Independence of the signs and Bernoulli variable for each n','No independence across n used']),
 entry('interval-variance','uniform-interval-anticoncentration-lower-bounds-variance','DRAFT quantified anti-concentration implies a variance lower bound',
       'DRAFT concept; w369 proof audited by w370, referee w371 pending. If a real square-integrable X satisfies P(X in I)<=1-epsilon for every closed interval I of one fixed length L>0, with epsilon in (0,1], then Var(X)>=epsilon L^2/4. Apply the assumption to the interval centered at EX and integrate squared deviations outside it. A variance lower bound alone does not imply such uniform anti-concentration. This corrects the categorical logical explanation on recalled card claim_3ccc6fc493b4e17b5c29966949004f575c51205c8a4f0ba3bc516d0b752ebea4, without restating the cited paper theorem.',
       ['Square integrability','The bound holds for every interval of the same positive length','One positive probability deficit epsilon'])]
relations=[
 {'from_key':'rare-event','to_key':'weaker-route','kind':'refutes','rationale':'The exact variance exponent 3/8 contradicts the candidate 1/3 conclusion while the stated weak and tail premises hold.'},
 {'from_key':'rare-event','to_key':'variance-exponent','kind':'depends_on','rationale':'The claimed exponent uses precisely the logarithmic variance definition.'},
 {'from_key':'uniform-kurtosis-bridge','to_key':'rare-event','kind':'semantic_association','rationale':'The countermodel has divergent standardized kurtosis and explains the retained moment premise.'},
 {'from_key':'uniform-kurtosis-bridge','to_existing_logical':'math:probability.core:open-problem-p0104-subdiffusive-and-kpz-passage-time-fluctuation-exponents','kind':'cites','rationale':'The conditional abstract bridge concerns converting hypothetical typical fluctuations into the variance target; the lattice inputs remain open obligations.'}]
bundle={'spec':'mathbrain-draft-v1','author_agent':'w370','bundle_slug':'p0104-weak-scaling-variance-obstruction-w370-001','entries':entries,'relations':relations}
write('drafts/bundle_001.json',bundle)
write('drafts/STATE.json',{'prepared':True,'submitted':False,'reviewed':False,'ingested':False,'retrievable':False,
      'expected_destination':'~/math-brain-inbox/w370/bundle_001.json',
      'reason':'Staged locally to obey worker write-only-inside-folder and no-live-store rules. Coordinator must independently review and submit.'})

claims=[
 {'id':'w370-P0104-002','kind':'counterexample','statement':entries[3]['statement'],'assumptions':entries[3]['assumptions'],
  'source':{'artifact':'INDEPENDENT_BRIDGE.md','primary_context':'https://arxiv.org/html/1401.0917v2, Theorem 1.1'},
  'proof_or_counterexample':'Exact three-variable construction, moment formulas, weak convergence bound and all-parameter exponential tail proof in INDEPENDENT_BRIDGE.md.',
  'independent_reviewer':'w371, pending','remaining_gap':'Independent check required; model is abstract and has no iid lattice realization.','status':'sketch'},
 {'id':'w370-P0104-003','kind':'conditional-bridge','statement':entries[1]['statement'],'assumptions':entries[1]['assumptions'],
  'source':{'artifact':'INDEPENDENT_BRIDGE.md','paired_claim':'w369 ATTEMPT.md L3'},
  'proof_or_counterexample':'Separate Paley-Zygmund/tightness/UI derivation, with symmetrization for arbitrary centers; paired proof checked directly in AUDIT_w369.md.',
  'independent_reviewer':'w371, pending','remaining_gap':'Uniform lattice kurtosis and nondegenerate n^(1/3) scaling not established.','status':'sketch'},
 {'id':'w370-P0104-004','kind':'audit-verdict','statement':'KEEP the exact statements L0-L4 in w369/ATTEMPT.md as conditional abstract results; do not count them as a proof of P0104.',
  'assumptions':['All hypotheses and quantifiers in the audited L0-L4 statements are retained'],
  'source':{'path':'~/brain_workers/w369/ATTEMPT.md','artifact':'AUDIT_w369.md'},
  'proof_or_counterexample':'Direct adversarial audit of interval quantifiers, arbitrary centers, independent-copy use, constants, tail endpoints and moment limits.',
  'independent_reviewer':'w370 is the independent adversary for w369; referee w371 pending',
  'remaining_gap':'Referee decision and actual lattice inputs; no account-level admission claimed.','status':'sketch'},
 {'id':'w370-P0104-005','kind':'brain-statement-correction','statement':entries[4]['statement'],'assumptions':entries[4]['assumptions'],
  'source':{'node_id':'claim_3ccc6fc493b4e17b5c29966949004f575c51205c8a4f0ba3bc516d0b752ebea4',
            'quote':'It does not by itself lower-bound the variance','artifact':'anti_concentration_card.json'},
  'proof_or_counterexample':'Apply the uniform interval bound at EX to get Var(X)>=epsilon L^2/4; source paper theorem is not reasserted.',
  'independent_reviewer':'w371 and claude-4a88bc43, pending','remaining_gap':'Only logical explanation is corrected; a fully hypothesized source theorem needs separate source verification.','status':'sketch'}]
with (R/'CLAIMS.jsonl').open('a',encoding='utf-8') as f:
    for row in claims:
        f.write(json.dumps(row,ensure_ascii=False)+'\n')
lookup={x['key']:x for x in entries}
with (R/'EDGES.jsonl').open('w',encoding='utf-8') as f:
    for rel in relations:
        row={**rel,'status':'draft, unreviewed','from_quote':lookup[rel['from_key']]['statement']}
        row['to_quote']=lookup[rel['to_key']]['statement'] if 'to_key' in rel else json.loads((R/'canonical_target_card.json').read_text(encoding='utf-8'))[0]['body']
        f.write(json.dumps(row,ensure_ascii=False)+'\n')
hook={'id':'math-w370-01','area':'math','event':'PreToolUse',
      'cue':'Using an anti-concentration recall card to decide whether a variance lower bound follows',
      'fire_when':'The recalled FPP card says uniform interval anti-concentration does not lower-bound variance.',
      'silent_when':'Only one arbitrary interval is bounded, without a uniform interval condition.',
      'text':'Check the interval quantifier: if every length-L closed interval has mass <=1-epsilon and X is square-integrable, Var(X)>=epsilon L^2/4. The reverse implication needs extra assumptions.',
      'evidence':'w370-P0104-005; anti_concentration_card.json; AUDIT_w369.md L0','proposer':'w370'}
(R/'proposals/math-w370.jsonl').write_text(json.dumps(hook,ensure_ascii=False)+'\n',encoding='utf-8')
write('outbox/peer_notices.json',[
 {'to':'w369','kind':'done','text':'P0104 L0-L4 conditional KEEP: AUDIT_w369.md. Separate 3/8 countermodel and symmetrization proof: INDEPENDENT_BRIDGE.md.'},
 {'to':'w371','kind':'ask','text':'Check w370-P0104-002/-003/-005 independently; review/REVIEW_PACKET.md identifies exact gaps and artifacts.'},
 {'to':'claude-4a88bc43','kind':'done','text':'P0104 independent audit, draft bundle and read-only attachment patch staged under w370; no live deployment or ingestion.'}])
(R/'outbox/progress.jsonl').write_text(json.dumps({'agent':'w370','row':'S1.P0104','event':'Saved independent variance-bridge audit, rare-event obstruction, exact brain correction and bounded read-only recall repair.','evidence':str(R/'AUDIT_w369.md')})+'\n',encoding='utf-8')
print(json.dumps({'claims_appended':len(claims),'draft_entries':len(entries),'draft_relations':len(relations),'submitted':False}))
