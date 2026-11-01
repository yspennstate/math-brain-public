"""Structural proof-certificate verifier. No inference validity is automated."""
import hashlib,json,re
from pathlib import Path

def statement_hash(statement,hypotheses):
    return hashlib.sha256(json.dumps({'statement':statement,'hypotheses':hypotheses},sort_keys=True,separators=(',',':')).encode()).hexdigest()

def key(n): return f"{n['claim_id']}@{n['version']}"

def cycle_witness(adj):
    state={}; stack=[]; positions={}; order=[]
    def visit(v):
        state[v]=1; positions[v]=len(stack); stack.append(v)
        for w in adj[v]:
            if state.get(w)==1: return stack[positions[w]:]+[w]
            if not state.get(w):
                hit=visit(w)
                if hit: return hit
        stack.pop(); positions.pop(v); state[v]=2; order.append(v)
    for v in adj:
        if not state.get(v):
            hit=visit(v)
            if hit: return hit,[]
    return [],order

ADMITTED={'IMPORTED_ACCEPTED','IMPORTED_CERTIFIED'}

def validate(g,check_files=True):
    errors=[]; warnings=[]; nodes={}; sources=g.get('sources',{})
    for n in g['nodes']:
        if not isinstance(n.get('version'),int) or n['version']<1: errors.append('INVALID_VERSION')
        k=key(n)
        if k in nodes: errors.append('DUPLICATE_VERSION:'+k)
        nodes[k]=n
        if n.get('statement_sha256')!=statement_hash(n['exact_statement'],n['hypotheses']): errors.append('STATEMENT_HASH:'+k)
        if not n.get('units') or not n.get('hypotheses'): errors.append('MISSING_UNITS_OR_HYPOTHESES:'+k)
        if n['status'] in ADMITTED:
            if not n.get('proof_sources'): errors.append('ACCEPTED_WITHOUT_SOURCE:'+k)
            if not n.get('evidence'): errors.append('ACCEPTED_WITHOUT_EVIDENCE:'+k)
        for pin in n.get('proof_sources',[]):
            if pin['source_id'] not in sources: errors.append('MISSING_SOURCE:'+k); continue
            if not pin.get('locator'): errors.append('MISSING_LOCATOR:'+k)
        if n['status'] not in ADMITTED: warnings.append('NOT_ADMITTED:'+k)
    for sid,s in sources.items():
        if not re.fullmatch('[0-9a-f]{64}',s.get('local_sha256','')): errors.append('SOURCE_HASH_FORMAT:'+sid)
        if check_files:
            p=Path(s['local_path'])
            if not p.is_file() or hashlib.sha256(p.read_bytes()).hexdigest()!=s['local_sha256']: errors.append('SOURCE_BYTES:'+sid)
    adj={k:[] for k in nodes}
    for n in nodes.values():
        for d in n.get('proof_dependencies',[]):
            k=key(n); dep=d.get('claim_key')
            if dep not in nodes: errors.append('MISSING_EXACT_DEPENDENCY:'+str(dep)); continue
            if d.get('statement_sha256')!=nodes[dep]['statement_sha256']: errors.append('DEPENDENCY_HASH:'+k)
            if not d.get('hypothesis_instantiation'): errors.append('MISSING_HYPOTHESIS_INSTANTIATION:'+k)
            if n['units']!=nodes[dep]['units'] and not d.get('unit_conversion'): errors.append('UNIT_CONVERSION_REQUIRED:'+k)
            adj[k].append(dep)
    cycle,order=cycle_witness(adj)
    if cycle:
        errors.append(('CYCLE_THROUGH_FINAL_FEI:' if g['final_claim'] in cycle else 'PROOF_CYCLE:')+' -> '.join(cycle))
    unresolved={}
    if not cycle:
        for k in order:
            leaves=set()
            if nodes[k]['status'] not in ADMITTED: leaves.add(k)
            for d in adj[k]: leaves.update(unresolved[d])
            unresolved[k]=sorted(leaves)
            if nodes[k]['status'] in ADMITTED and leaves: errors.append('ACCEPTED_DEPENDS_ON_UNRESOLVED:'+k)
    routes=[]
    for r in g.get('candidate_routes',[]):
        required=r['requires']
        if r['conclusion'] not in nodes or any(x not in nodes for x in required): errors.append('ROUTE_MISSING_VERSION:'+r['route_id']); continue
        if r['conclusion'] in required: errors.append('ROUTE_ASSUMES_CONCLUSION:'+r['route_id'])
        reachable=set(); pending=list(required)
        while pending:
            x=pending.pop()
            if x in reachable: continue
            reachable.add(x); pending.extend(adj[x])
        if r['conclusion'] in reachable and r['conclusion'] not in required: errors.append('ROUTE_TRANSITIVELY_ASSUMES_CONCLUSION:'+r['route_id'])
        missing=sorted({y for x in required for y in unresolved.get(x,[x])})
        routes.append({'route_id':r['route_id'],'unresolved_claim_versions':missing,'eligible_for_mathematical_review':not missing})
    return {'status':'REJECT' if errors else 'STRUCTURALLY_VALID','errors':errors,'warnings':warnings,'cycle':cycle,'dependency_first_order':order,'unresolved_closure':unresolved,'candidate_routes':routes,'semantic_proof_check':'NOT_AUTOMATED','final_FEI':'OPEN'}

if __name__=='__main__':
    import sys
    print(json.dumps(validate(json.loads(Path(sys.argv[1]).read_text(encoding='utf-8'))),indent=2))
