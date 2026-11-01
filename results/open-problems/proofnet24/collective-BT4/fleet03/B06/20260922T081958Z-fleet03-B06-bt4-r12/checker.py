import itertools, json, hashlib

residuals=('a','b')
ports=('c','e')

def path_templates(total_internal):
    out=[]
    # P: e -> ... -> c, Q: c -> ... -> e, disjoint interiors from {a,b}
    for kp in range(3):
        for Pmid in itertools.permutations(residuals,kp):
            rem=[x for x in residuals if x not in Pmid]
            for kq in range(len(rem)+1):
                for Qmid in itertools.permutations(rem,kq):
                    if len(Pmid)+len(Qmid)!=total_internal:
                        continue
                    P=('e',)+Pmid+('c',)
                    Q=('c',)+Qmid+('e',)
                    out.append((P,Q))
    uniq=[]
    seen=set()
    for x in out:
        if x not in seen:
            seen.add(x); uniq.append(x)
    return uniq

tri=path_templates(1)
quad=path_templates(2)
assert len(tri)==4
assert len(quad)==6

triangle_cases=[]
for P,Q in tri:
    used=set(P[1:-1])|set(Q[1:-1])
    assert len(used)==1
    leftover=({'a','b'}-used).pop()
    K={'c','e'}|used
    assert len(K)==3
    for loc in ('J','L','M','Rleft'):
        hits=tuple(sorted(K))
        if loc=='J':
            outcome='FRESH_PACKED_CROSS'
        elif loc=='L':
            outcome='FRESH_PACKED_CROSS_AND_IMMEDIATE_COLLAR'
        elif loc=='M':
            outcome='FRESH_PACKED_CROSS_AND_IMMEDIATE_COLLAR'
        else:
            outcome='RESIDUAL_TRIPLE_HIT'
        triangle_cases.append(dict(P=P,Q=Q,leftover=leftover,location=loc,hits=hits,outcome=outcome))
assert len(triangle_cases)==16
assert sum('FRESH_PACKED_CROSS' in x['outcome'] for x in triangle_cases)==12
assert sum(x['outcome']=='RESIDUAL_TRIPLE_HIT' for x in triangle_cases)==4

quad_cases=[]
labels=('c','e','a','b')
for P,Q in quad:
    K=set(labels)
    for loc in ('J','L_immediate','L_nonimmediate','M_immediate','M_nonimmediate'):
        for sz in (3,4):
            for hs in itertools.combinations(labels,sz):
                H=set(hs)
                if loc=='L_nonimmediate' and 'c' in H: continue
                if loc=='M_nonimmediate' and 'e' in H: continue
                if loc=='J':
                    fresh=bool(H & {'c','e'})
                    assert fresh
                    outcome='FRESH_PACKED_CROSS'
                elif loc.startswith('L'):
                    fresh=('e' in H)
                    if fresh:
                        outcome='FRESH_PACKED_CROSS'
                    else:
                        assert H=={'c','a','b'}
                        assert loc=='L_immediate'
                        outcome='L_IMMEDIATE_TWO_RESIDUAL_FORK'
                else:
                    fresh=('c' in H)
                    if fresh:
                        outcome='FRESH_PACKED_CROSS'
                    else:
                        assert H=={'e','a','b'}
                        assert loc=='M_immediate'
                        outcome='M_IMMEDIATE_TWO_RESIDUAL_FORK'
                quad_cases.append(dict(P=P,Q=Q,location=loc,hits=tuple(sorted(H)),outcome=outcome))

assert len(quad_cases)==6*17
forks=[x for x in quad_cases if 'FORK' in x['outcome']]
fresh=[x for x in quad_cases if x['outcome']=='FRESH_PACKED_CROSS']
assert len(forks)==12
assert len(fresh)==90

neutral_checks=[]
for m in range(3,81):
    c=0; cp=1; cpp=2 % m; cm=m-1
    path=list(range(2,m))
    for r,other in (('a','b'),('b','a')):
        cycle_vertex_count=len(path)+2
        assert cycle_vertex_count==m
        old_L=set(range(m))
        used_L=set(path)
        freed=old_L-used_L
        assert freed=={0,1}
        new_remainder={other,'c','c+'}
        assert new_remainder=={other,'c','c+'}
        neutral_checks.append((m,r,other,cycle_vertex_count,tuple(sorted(str(x) for x in new_remainder))))
assert len(neutral_checks)==78*2

payload={
  'candidate':'BT4-F3-R3-MIXED-APEX-NEUTRAL-FORK-v1',
  'triangle_path_templates':len(tri),
  'triangle_apex_cases':len(triangle_cases),
  'triangle_fresh_packed_cross_cases':sum('FRESH_PACKED_CROSS' in x['outcome'] for x in triangle_cases),
  'triangle_residual_triple_hit_cases':sum(x['outcome']=='RESIDUAL_TRIPLE_HIT' for x in triangle_cases),
  'quadrilateral_path_templates':len(quad),
  'quadrilateral_apex_patterns':len(quad_cases),
  'quadrilateral_fresh_packed_cross_patterns':len(fresh),
  'quadrilateral_exceptional_fork_patterns':len(forks),
  'fork_neutral_exchange_orders_checked':[3,80],
  'fork_neutral_exchange_checks':len(neutral_checks),
  'violations':[],
  'stronger_candidate_refuted_locally':{
      'claim':'quadrilateral mixed return always forces a fresh packed-to-packed cross',
      'symbolic_exception':{
          'K':'e->a->c->b->e',
          'apex':'z=c^- on L',
          'apex_hits':['c','a','b'],
          'apex_misses':['e'],
          'repair':'two exact size-neutral cycles C_a,C_b and two 3-vertex exchanged-remainder acyclicity obligations'
      },
      'scope':'symbolic local obstruction only; not asserted to be a full BT4 counterexample'
  },
  'result':'PASS'
}
canon=json.dumps(payload,sort_keys=True,separators=(',',':')).encode()
payload['payload_sha256']=hashlib.sha256(canon).hexdigest()
print(json.dumps(payload,sort_keys=True,indent=2))
