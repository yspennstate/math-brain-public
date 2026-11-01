"""Local P0117 draft packet and bounded, read-only mathematical diagnostics."""
from pathlib import Path
from itertools import combinations
from heapq import heappush, heappop
import difflib
import json
import os
import sqlite3
import sys
import time

ROOT = Path(__file__).resolve().parent
DB = Path('~/math-brain-build/local/population/brain.sqlite3')
QUERY = 'P0117 bigeodesic fixed endpoints adaptive boundary union conditioning'
sys.dont_write_bytecode = True
os.environ['MATH_BRAIN_SEMANTIC'] = '0'  # invocation-local diagnostic; no model loading

def dump(path, obj):
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(json.dumps(obj, ensure_ascii=False, indent=2)+'\n', encoding='utf-8')

def entry(key, title, statement, assumptions):
    return dict(key=key, namespace='probability.fpp.audit', logical_name=key,
                kind='concept', title=title, statement=statement, proof_text=None,
                assumptions=assumptions, domain='planar first-passage percolation',
                source=dict(source_id='owner-own-work:P0117:w394:'+key,
                            url='urn:owner-own-work:P0117:w394:'+key,
                            revision='draft-pending-w395-2026-10-10',
                            license='owner-own-work (campaign derivation and hypothesis audit)',
                            excerpt=None))

def draft():
    entries = [
      entry('p0117-anchored-boundary-exhaustion', 'DRAFT P0117 bigeodesic anchored boundary exhaustion',
        'DRAFT; independent check by w395 pending. On nearest-neighbor Z^2 with finite strictly positive edge weights, let S_R={x: ||x||_infinity=R}. Let E_R mean some globally minimizing finite simple path between distinct vertices of S_R passes through 0. First-exit truncation makes E_R decreasing. An infinite branch of the finite sets of oriented simple witnesses truncated inside [-R,R]^2 shows that intersection_R E_R is exactly existence of a bigeodesic through 0. For a stationary random law, absence everywhere follows if P(E_R) tends to zero. Equation (4.25) of Auffinger-Damron-Hanson, arXiv:1511.03262, already uses this boundary-pair reduction; no novelty is asserted. This global event need not be measurable from inside edges alone at fixed R.',
        ['Nearest-neighbor undirected Z^2', 'Finite strictly positive weights', 'Global path minimization; simple paths', 'Stationarity only for the final everywhere-absence consequence']),
      entry('p0117-refuted-fixed-endpoint-promotion', 'DRAFT P0117 refuted fixed-endpoint to adaptive boundary union route',
        'DRAFT, refuted inference: even uniform vanishing of fixed endpoint origin-hit probabilities does not imply vanishing of the adaptive union over all boundary endpoint pairs. If q_R is the largest pair probability on S_R, the bare union bound gives P(E_R)<=min(1,(32R^2-4R)q_R). It proves decay only with a stronger premise such as a subsequence on which (32R^2-4R)q_R tends to zero. This is a sufficient bound for that particular argument, not a necessary condition for absence. No independence or conditional multiplication is used. An environment-selected endpoint pair cannot be substituted into a deterministic-pair theorem without a selector or union argument.',
        ['E_R and S_R as in anchored-boundary-exhaustion', 'There are 8R boundary vertices', 'The queried theorem concerns deterministic endpoints, not an adaptive selector']),
      entry('p0117-growing-pair-family-counterexample', 'DRAFT P0117 adaptive endpoint union counterexample',
        'DRAFT; independent check by w395 pending. Let U be uniform on [0,1) and M_R=32R^2-4R. For j=0,...,M_R-1 let A_(R,j)={j/M_R<=U<(j+1)/M_R}. These endpoint-event analogues each have probability 1/M_R, uniformly tending to zero, but their adaptive union has probability one for every R. Their union events are constant and hence nested. This refutes promotion of individual fixed endpoint bounds to adaptive union decay. It is a probability counterexample to an inference, not a non-atomic iid FPP counterexample.',
        ['R is a positive integer', 'Uniform U on [0,1)', 'Finite half-open partition at each radius']),
      entry('p0117-global-box-filtration-scope', 'DRAFT P0117 global versus box minimizer conditioning scope',
        'DRAFT; independent check by w395 pending. A fixed-radius box-minimizer event is determined by inside edges; the analogous global-minimizer event need not be. Set every edge induced by B_1 to weight 1. In one completion all other edges also have weight 1, and the horizontal S_1 chord through 0 is globally minimizing. In a second completion give every edge of the S_2 perimeter and every nearest-neighbor edge from S_1 to S_2 weight 1/20; all remaining edges have weight 1. Each S_1 pair has an outside bypass of at most ten cheap edges, costing at most 1/2, while any simple through-origin path costs at least 2. The completions agree inside B_1, but only the first has a globally minimizing S_1 chord through 0. The local box event is true in both. This scope distinction matters before conditioning on an inside-edge filtration. It is a deterministic positive-weight example, not an iid FPP counterexample.',
        ['Undirected nearest-neighbor Z^2', 'Specified deterministic completions', 'B_1=[-1,1]^2 and S_2={||x||_infinity=2}']),
      entry('p0117-conditional-killing-divergence-gap', 'DRAFT P0117 conditional annular killing divergence gap',
        'DRAFT hypothesis audit of w393 L1-L3, directly read by w394; further referee check pending. Use decreasing finite-box geodesic events E_n in the filtration F_n of inside edges. If predictable q_n in [0,1] satisfy P(E_(n+1)|F_n)<=1_(E_n)(1-q_n), and sum q_n diverges almost surely on infinite survival, the compensated indicator 1_(E_n) exp(sum_(j<n)q_j) is a nonnegative supermartingale and rules out survival. Positive q_n alone is insufficient: independent q_n=1/(n+1)^2 leave limiting survival probability 1/2. For an iid atomless law with mass arbitrarily near zero, the cheap-ring construction gives q_n=G([0,m/(8(n+1))))^(8(n+1)), m the minimum of the origin incident weights. These specific lower bounds are summable and therefore do not provide the needed divergence. No bound on the true killing hazards is inferred.',
        ['Decreasing F_n-measurable events', 'Specified conditional inequality', 'Divergence along survival is an additional premise', 'Support near zero is needed only for the displayed ring construction']),
      entry('p0117-midpoint-hypothesis-rate-audit', 'DRAFT P0117 midpoint theorem adaptive endpoint rate audit',
        'DRAFT source-to-need comparison. Ahlberg-Hoffman arXiv:1609.02447, A1 and Theorem 2.1, apply to atomless iid weights with finite E[min(X1,X2,X3,X4)^2]; all deterministic diverging endpoint sequences have origin-hit probabilities tending to zero. Maximizing over each finite S_R pair set therefore yields q_R->0, but supplies no adaptive union decay rate. Dembin-Elboim-Peled arXiv:2204.02332v5 Theorem 1.2 instead needs absolute continuity, a finite exponential moment, and more than 40 limit-shape extreme points; its bound C log^2(D+2)/D^(1/16) is insufficient for summing 32R^2-4R pairs. Theorem 1.3 bounds the union over common-height pairs ((-n,s),(n,s)), s in Z, by C log^2(n)/n^(1/24), already handling that restricted selector family. An arbitrary bigeodesic through 0 is not proved to have witnesses in that family. Source checks and these failed substitutions do not prove P0117. A separate September 24, 2026 OpenAI preprint claims the full moment-class result; its mathematical validity is still under audit.',
        ['Each cited theorem retains its own distribution and geometry hypotheses', 'D is the smaller endpoint-to-vertex distance', 'No arbitrary endpoint replacement stability is assumed'])
    ]
    relations = [
      dict(from_key=entries[2]['key'],to_key=entries[1]['key'],kind='refutes',
           rationale='The M_R partition events satisfy uniform vanishing but have union probability one, contradicting precisely the documented fixed-endpoint promotion.'),
      dict(from_key=entries[1]['key'],to_key=entries[0]['key'],kind='semantic_association',
           rationale='The refuted route is an attempted way to bound the exact boundary event in the anchored reduction.'),
      dict(from_key=entries[3]['key'],to_key=entries[4]['key'],kind='semantic_association',
           rationale='The conditional killing lemma requires F_n-measurability; the deterministic example distinguishes box events from global events at fixed n.'),
      dict(from_key=entries[5]['key'],to_key=entries[1]['key'],kind='semantic_association',
           rationale='The source audit checks the hypotheses and quantitative strength of the endpoint bounds used by this refuted route.'),
      dict(from_key=entries[0]['key'],to_existing_logical='math:probability.core:open-problem-p0117-absence-of-bi-infinite-geodesics-in-planar-iid-fpp',kind='semantic_association',
           rationale='The boundary reduction concerns exactly the full bi-infinite-geodesic absence target of the existing P0117 concept; no open-status promotion is made.')
    ]
    return dict(spec='mathbrain-draft-v1',author_agent='w394',bundle_slug='p0117-adaptive-endpoint-audit-20261010',entries=entries,relations=relations)

def finite_diagnostic():
    vertices=[(x,y) for x in range(-2,3) for y in range(-2,3)]
    sphere=lambda v:max(abs(v[0]),abs(v[1]))
    inside=lambda v:sphere(v)<=1
    def neighbors(v):
        for d in [(1,0),(-1,0),(0,1),(0,-1)]:
            w=(v[0]+d[0],v[1]+d[1])
            if w in vertices: yield w
    def weight(v,w,cheap):
        ring=sphere(v)==2 and sphere(w)==2
        connector={sphere(v),sphere(w)}=={1,2}
        return 1 if cheap and (ring or connector) else 20
    def distance(start,end,cheap,box=False):
        todo=[(0,start)]; best={start:0}
        while todo:
            d,v=heappop(todo)
            if d!=best[v]: continue
            if v==end:return d
            for w in neighbors(v):
                if box and not inside(w):continue
                nd=d+weight(v,w,cheap)
                if nd<best.get(w,10**9):best[w]=nd;heappush(todo,(nd,w))
        raise AssertionError('disconnected diagnostic')
    boundary=[v for v in vertices if sphere(v)==1]
    pairs=list(combinations(boundary,2))
    result={}
    for cheap in [False,True]:
        hits=[];box_hits=[]
        for a,b in pairs:
            if distance(a,b,cheap)==distance(a,(0,0),cheap)+distance((0,0),b,cheap):hits.append([a,b])
            if distance(a,b,cheap,True)==distance(a,(0,0),cheap,True)+distance((0,0),b,cheap,True):box_hits.append([a,b])
        result['cheap_completion' if cheap else 'constant_completion']={
          'global_origin_hit_pairs':len(hits),'box_origin_hit_pairs':len(box_hits),
          'max_boundary_pair_distance_scaled_by_20':max(distance(a,b,cheap) for a,b in pairs)}
    assert result['constant_completion']['global_origin_hit_pairs']>0
    assert result['cheap_completion']['global_origin_hit_pairs']==0
    assert result['constant_completion']['box_origin_hit_pairs']==result['cheap_completion']['box_origin_hit_pairs']>0
    result.update(vertices=25,unordered_boundary_pairs=28,integer_scale=20,
                  global_justification='The finite-box distances exhibit bypasses of cost <=1/2. In the full second environment any path through 0 has cost >=2. The constant environment is globally the l1 metric.',
                  proof_status='finite diagnostic plus explicit analytic full-lattice comparison; independent referee pending')
    dump(ROOT/'verification/filtration_counterexample.json',result)
    return result

def warns(body):
    b=body.lower()
    return 'endpoint' in b and 'union' in b and any(x in b for x in ['adaptive','selector','selected']) and any(x in b for x in ['refuted','insufficient','does not','not imply','no adaptive'])

def retrieval_diagnostic(bundle):
    sys.path.insert(0,'~/math-brain-build/src')
    from math_brain.models import GraphNode,GraphEdge,NodeKind,EdgeKind
    from math_brain.retrieval import search
    start=time.perf_counter()
    with sqlite3.connect(DB.as_uri()+'?mode=ro',uri=True,timeout=2) as con:
        con.execute('PRAGMA query_only=ON')
        con.execute('BEGIN')
        count=con.execute('SELECT count(*) FROM nodes').fetchone()[0]
        edge_count=con.execute('SELECT count(*) FROM edges').fetchone()[0]
        if count>50000 or edge_count>150000:raise RuntimeError('read-only compute gate exceeded')
        nodes=[GraphNode(id=r[0],kind=NodeKind(r[1]),title=r[2],body=r[3],metadata=json.loads(r[4]))
               for r in con.execute('SELECT id,kind,title,body,metadata_json FROM nodes')]
        edges=[];skipped=0
        for r in con.execute('SELECT id,source_id,target_id,kind,rationale,weight,metadata_json FROM edges WHERE id NOT IN (SELECT edge_id FROM edge_retractions)'):
            try:kind=EdgeKind(r[3])
            except ValueError:skipped+=1;continue
            edges.append(GraphEdge(id=r[0],source_id=r[1],target_id=r[2],kind=kind,rationale=r[4],weight=r[5],metadata=json.loads(r[6])))
        con.commit()  # ends a read transaction; no writes are permitted
    additions=[GraphNode(id='draft:w394:'+e['key'],kind=NodeKind.CLAIM,title=e['title'],body=e['statement'],
                         metadata=dict(claim_kind='concept',truth_status='unverified',logical_id='math:'+e['namespace']+':'+e['logical_name'])) for e in bundle['entries']]
    added_edges=[GraphEdge(id='draft:w394:edge:'+str(i),source_id='draft:w394:'+r['from_key'],
                          target_id='draft:w394:'+r['to_key'],kind=EdgeKind(r['kind']),rationale=r['rationale'])
                 for i,r in enumerate(bundle['relations']) if 'to_key' in r]
    def run(n,e):
        tick=time.perf_counter()
        hits=search(QUERY,nodes=n,edges=e,limit=5)
        return dict(seconds=round(time.perf_counter()-tick,3),warning_bearing_hits_at_5=sum(warns(h.node.body) for h in hits),
                    hits=[dict(id=h.node.id,title=h.node.title,score=h.total_score,warns_adaptive_union=warns(h.node.body)) for h in hits])
    before=run(nodes,edges)
    after=run(nodes+additions,edges+added_edges)
    result=dict(command='python -X utf8 build_and_measure.py',database=str(DB),query=QUERY,
                node_count=count,edge_count=edge_count,unknown_edge_kinds_skipped=skipped,
                before=before,after_local_in_memory_overlay=after,elapsed_seconds=round(time.perf_counter()-start,3),
                metric='Number of top-5 returned cards that explicitly warn about an adaptive endpoint union; same query and engine.',
                limitations=['One author-chosen diagnostic query; not a blind test or broad recall improvement.',
                             'Six concept cards and four local relations added only in memory; live store unchanged.',
                             'Semantic channel disabled for both arms of this local diagnostic; no model loads.',
                             'External link omitted from measurement; coordinator resolves it during integration.',
                             'Reference corpus read by retrieval engine; no full export or private card text saved.'])
    dump(ROOT/'verification/retrieval_before_after.json',result)
    return result

def main():
    started=time.perf_counter()
    dump(ROOT/'verification/COMPUTE_GATE.json',dict(max_nodes=50000,max_edges=150000,semantic_models=False,
         finite_graph_vertices=25,finite_graph_pairs=28,store_mode='ro',scope='One diagnostic query before/after one local overlay; no GPU or training'))
    bundle=draft()
    part=ROOT/'drafts/bundle_001.part'
    dump(part,bundle)
    final=part.with_suffix('.json')
    if final.exists():raise FileExistsError('Never overwrite an existing completed draft; choose a new number')
    part.rename(final)
    dest='math-brain-inbox/w394/bundle_001.json'
    diff=''.join(difflib.unified_diff([],final.read_text(encoding='utf-8').splitlines(keepends=True),fromfile='a/'+dest,tofile='b/'+dest))
    patch=ROOT/'patches/01_p0117_audit_bundle.diff';patch.parent.mkdir(exist_ok=True);patch.write_text(diff,encoding='utf-8',newline='\n')
    diagnostic=finite_diagnostic()
    retrieval=retrieval_diagnostic(bundle)
    hook=dict(id='p0117-w394-01',area='math',event='stage-start',
              cue='adaptive endpoint|selected direction|fixed endpoint|union bound|conditional killing',
              fire_when='A proof applies a fixed deterministic-object theorem to environment-selected endpoints or multiplies unconditional survival estimates.',
              silent_when='Endpoints are fixed before sampling and only their own hit event is being bounded, or a valid predictable-hazard argument is supplied.',
              text='Check the selector and filtration. Fixed-endpoint decay does not control a growing adaptive union; count candidates and require a union bound, stability cover, or valid conditional-hazard argument.',
              evidence='~/brain_workers/w394/ATTEMPT.md:C04; verification/filtration_counterexample.json; verification/retrieval_before_after.json',proposer='w394')
    hook_path=ROOT/'proposals/math-w394.jsonl';hook_path.parent.mkdir(exist_ok=True);hook_path.write_text(json.dumps(hook)+'\n',encoding='utf-8')
    hook_dest='primary_directive/hooks1000/proposals/math-w394.jsonl'
    (ROOT/'patches/02_selector_hook.diff').write_text(''.join(difflib.unified_diff([],hook_path.read_text().splitlines(keepends=True),fromfile='a/'+hook_dest,tofile='b/'+hook_dest)),encoding='utf-8',newline='\n')
    print(json.dumps(dict(filtration=diagnostic,retrieval=retrieval,total_seconds=round(time.perf_counter()-started,3)),ensure_ascii=False))

if __name__=='__main__':main()
