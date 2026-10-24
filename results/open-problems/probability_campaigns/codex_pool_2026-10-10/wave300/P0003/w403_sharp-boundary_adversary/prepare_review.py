"""Prepare this worker's draft packet; never ingest or write a live store."""
from pathlib import Path
import json
import math
from check_honeycomb_pinch import honeycomb_route, rational_xy, ANCHORS

ROOT = Path(__file__).resolve().parent
INBOX = Path('~/math-brain-inbox/w403')


def save_json(path, data):
    path.write_text(json.dumps(data, ensure_ascii=False, indent=2) + '\n', encoding='utf-8')


def entry(key, logical, title, statement, kind='concept'):
    return {
        'key': key, 'namespace': 'probability.self-avoiding-walk',
        'logical_name': logical, 'kind': kind, 'title': title,
        'statement': statement, 'proof_text': None,
        'assumptions': ['Draft campaign mathematics; independent mathematical review pending',
                        'No conclusion about the actual SAW sampling law or the P0003 SLE conjecture'],
        'domain': 'probability theory; topology of scaling limits',
        'source': {'source_id': 'owner-probability-w403-p0003-pinch-20261010',
                   'url': 'urn:probability-research:20261010:w403:p0003-pinch',
                   'revision': 'author-proof-exact-reproduction-20261010-v1',
                   'license': 'owner-own-work; draft campaign counterexample and criterion, no novelty claim',
                   'excerpt': None},
    }


def make_figure():
    width, height = 860, 390
    def point(x, y, panel):
        return 34 + 405*panel + 48*(x + 2*math.sqrt(3)), 344 - 48*(y + 2)
    routes = honeycomb_route(16)
    path = routes[0] + [v for route in routes[1:] for v in route[1:]]
    finite = [(float(x)*math.sqrt(3),float(y)) for x,y in (rational_xy(v,16) for v in path)]
    limit = [(float(x)*math.sqrt(3),float(y)) for x,y in ANCHORS]
    def points(values,panel):
        return ' '.join(f'{a:.3f},{b:.3f}' for a,b in (point(x,y,panel) for x,y in values))
    parts=[f'<svg xmlns="http://www.w3.org/2000/svg" width="{width}" height="{height}" viewBox="0 0 {width} {height}" role="img" aria-label="Simple honeycomb path and its non-simple pinched-loop uniform limit">',
           '<rect width="100%" height="100%" fill="white"/>',
           '<style>text{font:14px sans-serif;fill:#172b4d}.title{font-size:18px;font-weight:bold}</style>']
    for panel, title in [(0,'N = 16: simple honeycomb path'),(1,'Uniform limit: closed loop')]:
        x,y=point(-2*math.sqrt(3),4,panel)
        parts.append(f'<rect x="{x}" y="{y}" width="{192*math.sqrt(3)}" height="288" rx="3" fill="#f8fafc" stroke="#94a3b8"/>')
        parts.append(f'<text x="{34+405*panel}" y="27" class="title">{title}</text>')
    rx,ry=point(0,3,1)
    parts.append(f'<rect x="{rx}" y="{ry}" width="{48*math.sqrt(3)}" height="144" fill="#fed7aa"/>')
    parts.append(f'<polyline points="{points(finite,0)}" fill="none" stroke="#2563eb" stroke-width="2.2"/>')
    parts.append(f'<polyline points="{points(limit,1)}" fill="none" stroke="#c2410c" stroke-width="2.5"/>')
    for panel, coord in [(0,finite[len(routes[0])-1]),(0,tuple(float(c) for c in (rational_xy(routes[4][-1],16)[0]*math.sqrt(3), rational_xy(routes[4][-1],16)[1]))),(1,(0,0))]:
        x,y=point(*coord,panel)
        parts.append(f'<circle cx="{x:.3f}" cy="{y:.3f}" r="4" fill="#dc2626"/>')
    parts.append('<text x="34" y="373">Neck = sqrt(37)/N; speed &lt;= 28</text>')
    parts.append('<text x="439" y="373">Contains a rectangle of area 3sqrt(3)</text>')
    parts.append('</svg>')
    (ROOT/'honeycomb_pinch.svg').write_text('\n'.join(parts)+'\n',encoding='utf-8')


def main():
    measurement=json.loads((ROOT/'measurements'/'honeycomb_pinch.json').read_text(encoding='utf-8'))
    peer=json.loads((ROOT/'measurements'/'peer_mode.json').read_text(encoding='utf-8'))
    assert measurement['all_passed'] and peer['all_passed']
    definition=entry('macroscopic-return-event','macroscopic-self-return-event',
        'Macroscopic near-return event for a continuous curve',
        'For a continuous curve gamma:[0,1]->C and r>=0,q>0, E(r,q) is the event that there exist s<t with |gamma(s)-gamma(t)|<=r and diameter(gamma([s,t]))>=q. A nonconstant self-return is equality gamma(s)=gamma(t) with a positive-diameter intervening subcurve. Constant waiting intervals are not nonconstant self-returns.', 'definition')
    definition['assumptions']=['gamma is continuous on the compact interval [0,1]']
    rejected=entry('rejected-simple-limit-bridge','rejected-self-avoidance-tightness-simple-limit-bridge',
        'Rejected bridge: discrete self-avoidance and tightness force a simple trace',
        'DRAFT ROUTE AUDIT. The auxiliary implication that tight laws on simple honeycomb paths with distinct fixed endpoints in a fixed simply connected domain must have simple limiting traces is false. There are deterministic such laws converging uniformly, with speed bounded by 28, whose limiting trace contains a closed rectangle. This refutes only the auxiliary implication; it supplies no claim about the uniform fixed-length or critical-fugacity SAW law.')
    counterexample=entry('honeycomb-loop-pinch','honeycomb-simple-paths-uniform-limit-closed-loop',
        'Honeycomb simple paths can pinch into a macroscopic loop',
        'DRAFT AUTHOR PROOF; independent review pending. For even N>=8 let the regular honeycomb vertices be H(i,j)=(sqrt(3)i/2,3j/2-((i+j) mod 2)/2), with horizontal nearest neighbors and upward vertical edges at even i+j, and scale by 1/N. Concatenate: row 0 from (-4N,0) to (-4,0); ascent to (-3,2N) alternating columns -4,-3; row 2N to (2N-1,2N); descent to (2N,0) alternating columns 2N-1,2N; row 0 to (3,0); descent to (4,-N) alternating columns 3,4; row -N to (4N,-N). Each ascent/descent takes the available vertical edge then switches columns after every vertical step except the last. Shared corners are counted once. The path is vertex-simple with 22N-12 edges. Giving each of seven routes time 1/7 yields speed <=28 and uniform error <=5/N relative to the polygon with anchors (-2sqrt(3),0),(0,0),(0,3),(sqrt(3),3),(sqrt(3),0),(0,0),(0,-3/2),(2sqrt(3),-3/2). All interior vertices lie in D=(-2sqrt(3),2sqrt(3))x(-2,4); endpoints are fixed distinct smooth boundary points. The limit contains the boundary of [0,sqrt(3)]x[0,3] and is not a simple arc. The neck anchors have distance sqrt(37)/N while the excursion diameter tends to 2sqrt(3). The laws here are point masses, not the actual SAW sampling law.')
    criterion=entry('self-return-criterion','uniform-weak-limit-macroscopic-self-return-criterion',
        'Criterion for excluding nonconstant returns in a uniform weak limit',
        'DRAFT AUTHOR PROOF; independent review pending. Suppose P_n converges weakly to P on C([0,1],C) with the uniform metric. For r>=0,q>0, let E(r,q) be the curves for which some s<t have |gamma(s)-gamma(t)|<=r and diameter(gamma([s,t]))>=q. Then P gives probability zero to every nonconstant self-return if and only if, for every q>0, lim_{r down to 0} limsup_{n to infinity} P_n(E(r,q))=0. Constant waiting intervals are permitted. No boundary avoidance, conformal invariance, Loewner or SLE conclusion is included.')
    bundle={'spec':'mathbrain-draft-v1','author_agent':'w403',
            'bundle_slug':'p0003-honeycomb-pinch-obstruction-w403-20261010',
            'entries':[definition,rejected,counterexample,criterion],
            'relations':[
                {'from_key':'honeycomb-loop-pinch','to_key':'rejected-simple-limit-bridge','kind':'refutes',
                 'rationale':'The explicit vertex-simple paths converge uniformly to a trace containing a closed rectangle, defeating the claimed sufficiency of tightness and self-avoidance.'},
                {'from_key':'self-return-criterion','to_key':'macroscopic-return-event','kind':'depends_on',
                 'rationale':'The criterion is stated using this exact macroscopic near-return event.'},
                {'from_key':'honeycomb-loop-pinch','to_key':'self-return-criterion','kind':'semantic_association',
                 'rationale':'For the deterministic paths E(r,1) has eventual probability one for every r>0; the criterion identifies the omitted probability estimate.'},
                {'from_key':'honeycomb-loop-pinch',
                 'to_existing_logical':'math:probability.core:open-problem-p0003-hexagonal-self-avoiding-walk-scaling-limit',
                 'kind':'semantic_association',
                 'rationale':'A topology obstruction to a stronger SAW scaling-limit bridge; not a refutation or solution of the fixed-length SLE question.'}]}
    local=ROOT/'bundle_001.json'
    save_json(local,bundle)
    INBOX.mkdir(parents=True,exist_ok=True)
    destination=INBOX/'bundle_001.json'
    if destination.exists():
        assert destination.read_bytes()==local.read_bytes(), 'Existing draft differs; preserve it'
    else:
        partial=INBOX/'bundle_001.json.part'
        assert not partial.exists(), 'Preserve an existing unfinished draft'
        partial.write_bytes(local.read_bytes())
        partial.rename(destination)
    # No integrator or live-store write is authorized for this worker.
    source=json.loads((ROOT/'SOURCE_STATUS.json').read_text(encoding='utf-8'))
    source.update({
        'current_openness':'UNKNOWN','novelty_claim':False,
        'assigned_primary_source':{'author':'Geoffrey R. Grimmett','title':'Selected problems in probability theory',
            'url':'https://arxiv.org/pdf/2205.07318','version':'v1, 2022-05-15',
            'locator':'Question 2.2, PDF/printed p.3, extracted lines 88-89',
            'short_quote':'Does a uniformly distributed n-step SAW from the origin of H converge weakly, when suitably rescaled',
            'own_words_statement':'Does an appropriately rescaled uniform n-step self-avoiding walk from the honeycomb origin converge weakly as n tends to infinity to an SLE(8/3) random curve?',
            'specified':['fixed-length uniform law','origin start','free endpoint','honeycomb lattice','SLE parameter 8/3'],
            'unspecified':['rescaling','SLE variant and stopping convention','parametrization','curve topology'],
            'statement_complete_to_source':True,'fully_formal_convergence_theorem_statement':False},
        'related_primary_sources':[
            {'url':'https://arxiv.org/pdf/1206.2092','locator':'Conjecture 1.5 and section 3.3, PDF pp.9 and 23',
             'scope':'Variable-length critical a-to-b chordal ensemble; no equivalence to P0003 is proved here'},
            {'url':'https://arxiv.org/pdf/math/0204277','locator':'Sections 2.2 and 3.4.5, PDF pp.5-7 and 24',
             'scope':'Conformal-restriction classification requires simple-path support; simplicity discussion uses additional continuity and conditioning input'},
            {'url':'https://arxiv.org/pdf/1007.0575','locator':'Section 4, PDF pp.9-10',
             'scope':'Exact connective constant and local relation do not prove observable or SLE convergence'},
            {'url':'https://arxiv.org/pdf/2310.17299',
             'scope':'Quantitative sub-ballisticity; does not certify SLE convergence or current openness'}],
        'local_prior_checks':{
            'read_only_store':'file:~/math-brain-build/local/population/brain.sqlite3?mode=ro',
            'query_scope':'Only title matches for P0003 or hexagonal self-avoiding; two nodes returned',
            'problem_node_id':'claim_1f7a2a12ab2a649bf165699aa2efee71c08bca2100b4609c325b8f2d99b4f0dd',
            'attempt_node_id':'claim_7d17eca1121391c711c3f35ad1dfd9fec7313bf8f51990c4a397f115c4d88f69',
            'prior_attempt':'Finite-graph fugacity DMP; explicitly lacks tightness, conformal invariance and SLE identification',
            'no_exact_hits':['H_20260912 and I_20260914 targeted exact record searches','additional intake D/E/F/G/H/I P0003 exact record searches'],
            'lean_check':'Named annotated ranking only; no P0003 formal proof receipt identified',
            'team_o':'Targeted board search returned no P0003 row',
            'solved_retired_status':'No independently verified solution/retirement in these bounded checks; no exhaustive absence claim'},
        'brain_hints':{'recall_query':'P0003 hexagonal self-avoiding walk SLE scaling limit adversary proof mistakes',
            'result':'Completed under 60-second gate; absent P0003/hexagonal memories, weak separation; top three read as hints',
            'top_three':['the_math_brain_cannot_serve_a_number_it_cannot_tokenize_2026_09_05',
                         'uniform_relu_global_lipschitz_audit_2026_07_10','recall_symbol_channel_matched_notation_glue_2026_10_06'],
            'proof_scar':'perceptron_proof_open_gaps_fleet_2026_07_12'},
        'mathematical_proof_of_target':False,'formal_check_receipt':None,
        'submitted':True,'reviewed':False,'ingested':False,'retrievable':False,
        'submitted_path':str(destination),'reviewer':'w404',
        'source_hash_check_is_mathematical_proof':False})
    for item in source.get('primary_candidates',[]):
        if '0204277' in item['url']: item['checked']='Targeted primary sections 2.2 and 3.4.5'
        if '1007.0575' in item['url']: item['checked']='Targeted primary section 4'
    save_json(ROOT/'SOURCE_STATUS.json',source)
    save_json(ROOT/'LIFECYCLE.json',{'submitted':{'state':True,'path':str(destination)},
        'reviewed':{'state':False,'reviewer':'w404','receipt':None},
        'ingested':{'state':False,'receipt':None},'retrievable':{'state':False,'receipt':None},
        'theorem_promotion':'Not authorized until independent mathematical check',
        'formal_check_receipt':None})
    hook={'id':'saw-pinch-w403-01','area':'math','event':'stage-start',
        'cue':'A scaling-limit argument infers simplicity from discrete self-avoidance or tightness alone without a macroscopic near-return estimate',
        'fire_when':'Tight honeycomb SAWs have a limit; it is therefore simple and the simple-path restriction classification applies',
        'silent_when':'The actual-law macroscopic near-return estimate is already proved, or no inference of limiting simplicity is made',
        'text':'Simple lattice paths can pinch into a macroscopic loop in a uniform limit. Tightness alone does not preserve simplicity; check a mesh-uniform near-return estimate before using the simple-path SLE/restriction characterization. A support example does not refute the SAW law.',
        'evidence':'~/brain_workers/w403/CLAIMS.jsonl w403-CX-001; 5 exact cases, 5401 vertices; measurements/honeycomb_pinch.json',
        'proposer':'w403'}
    assert len(hook['text'])<=300
    hook_line=json.dumps(hook,ensure_ascii=False,separators=(',',':'))+'\n'
    (ROOT/'hooks_proposal.jsonl').write_text(hook_line,encoding='utf-8')
    patches=ROOT/'patches';patches.mkdir(exist_ok=True)
    live='~/primary_directive/hooks1000/proposals/math-w403.jsonl'
    patch=f'--- a/{live}\n+++ b/{live}\n@@ -0,0 +1 @@\n+'+hook_line
    (patches/'01_math_hook_pinch.diff').write_text(patch,encoding='utf-8')
    make_figure()
    print(json.dumps({'local_bundle':str(local),'submitted_bundle':str(destination),
                      'entries':len(bundle['entries']),'relations':len(bundle['relations']),
                      'hook_text_characters':len(hook['text']),'submitted':True,
                      'reviewed':False,'ingested':False,'retrievable':False}))


if __name__=='__main__': main()
