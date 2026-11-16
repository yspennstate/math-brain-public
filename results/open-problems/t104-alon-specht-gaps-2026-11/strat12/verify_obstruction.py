"""PROVED: strict certificates are impossible on nine inherited OPEN boxes.

The witnesses are in Q[s]/(s^2-d), d in {5,15}, s>0. Arithmetic below uses
integer/rational coefficients only; enclosure comparisons square rationals.
These witnesses have connected=0 and are NOT feasible counterexamples.
"""
import json
from pathlib import Path
from fractions import Fraction as F
from math import prod
from exact_bernstein import data,active_constraints

HERE=Path(__file__).resolve().parent
ZERO=(F(0),F(0));ONE=(F(1),F(0))

def add(x,y):return x[0]+y[0],x[1]+y[1]
def mul(x,y,d=5):return x[0]*y[0]+d*x[1]*y[1],x[0]*y[1]+x[1]*y[0]
def power(x,n,d=5):
    out=ONE
    for _ in range(n):out=mul(out,x,d)
    return out
def sign(x,d=5):
    a,b=x
    if not b:return (a>0)-(a<0)
    if not a:return (b>0)-(b<0)
    if a>0 and b>0:return 1
    if a<0 and b<0:return -1
    difference=a*a-d*b*b
    assert difference != 0 # Both supported radicands are nonsquares.
    return ((difference>0)-(difference<0))*((a>0)-(a<0))
def evaluate(p,point,d=5):
    out=ZERO
    for m,c in p.items():
        v=(F(c),F(0))
        for x,n in zip(point,m):v=mul(v,power(x,n,d),d)
        out=add(out,v)
    return out
def in_box(point,box,d=5):
    return all(sign(add(x,(-F(a),F(0))),d)>=0 and
               sign(add((F(b),F(0)),(-x[0],-x[1])),d)>=0
               for x,(a,b) in zip(point,box))
def encode(point):return [[str(a),str(b)] for a,b in point]

def witnesses():
    rat=lambda x:(F(x),F(0));root=lambda x:(F(0),F(x))
    five=[
        [rat(4),rat(-1),root(-1),rat(-1),root(-1),root(1)],
        [rat(4),rat(-1),root(-1),rat(-1),root(1),root(1)],
        [rat(4),rat(-1),root(1),rat(-1),root(-1),root(1)],
        [rat(F(3,2)),rat(-1),root(-1),rat(-1),root(F(1,2)),root(F(1,2))],
        [rat(F(3,2)),rat(-1),root(F(1,2)),rat(-1),root(-1),root(F(1,2))],
    ]
    fifteen=[
        [rat(4),rat(-1),root(F(-1,3)),rat(-1),root(F(-1,3)),root(1)],
        [rat(4),rat(-1),root(-1),rat(-1),root(F(1,3)),root(F(1,3))],
        [rat(4),rat(-1),root(F(1,3)),rat(-1),root(-1),root(F(1,3))],
        [rat(4),rat(-1),root(F(1,3)),rat(-1),root(F(1,3)),root(F(1,3))],
    ]
    return [(5,p) for p in five]+[(15,p) for p in fifteen]

def main():
    p,gs=data()
    inputs=json.loads((HERE/'STRAT11/remaining_open_boxes.json').read_text())['boxes']
    records=[]
    for radicand,point in witnesses():
        assert evaluate(p,point,radicand)==ZERO
        values={key:evaluate(g,point,radicand) for key,g in gs.items()
                if key not in ('scale14','scale_guard')}
        assert all(sign(v,radicand)>=0 for v in values.values())
        assert values['connected']==ZERO and sign(values['rank'],radicand)>0 and sign(values['ratio'],radicand)>0
        # D=tau>0 and H=0 at these five endpoints: actual a=b=1>14/25.
        t,v1,z1,v2,z2,z=point
        xs=[v1,v2,add(add(add(ONE,(-t[0],-t[1])),(-v1[0],-v1[1])),(-v2[0],-v2[1])),t,(F(-1),F(0))]
        ys=[z1,z2,(-z[0]-z1[0]-z2[0],-z[1]-z1[1]-z2[1]),ZERO,z]
        tau=ZERO
        for x,y in zip(xs,ys):tau=add(tau,add(mul(x,x,radicand),mul(y,y,radicand)))
        D=add((20*t[0],20*t[1]),(-tau[0],-tau[1]))
        assert D==tau and sign(D,radicand)>0
        assert D[1]==0
        positive_edges=[]
        for i in range(5):
            for j in range(i+1,5):
                dot=add(mul(xs[i],xs[j],radicand),mul(ys[i],ys[j],radicand))
                g=add(t,dot)
                weight=(2*g[0]/D[0],2*g[1]/D[0])
                assert weight[1]==0 and weight[0]>=0
                if weight[0]:positive_edges.append((i,j,weight[0]))
        used={v for i,j,w in positive_edges for v in (i,j)}
        if radicand==5:
            assert len(positive_edges)==2 and len(used)==4
            assert all(w==F(1,2) for i,j,w in positive_edges)
        else:
            assert len(positive_edges)==3 and len(used)==3
            assert all(w==F(1,3) for i,j,w in positive_edges)
        assert evaluate(gs['scale_guard'],point,radicand)==(-11*tau[0],-11*tau[1])
        hit_boxes=[b for b in inputs if in_box(point,b['box'],radicand)]
        hits=[b['node'] for b in hit_boxes]
        assert hits
        for box in hit_boxes:
            active=active_constraints([tuple(map(F,x)) for x in box['box']])
            assert all(sign(evaluate(g,point,radicand),radicand)>=0 for g in active.values())
        records.append(dict(radicand=radicand,point=encode(point),nodes=hits,
                            values={k:encode([v])[0] for k,v in values.items()}))
    expected=json.loads((HERE/'obstructions.json').read_text())
    assert expected['records']==records
    bank=json.loads((HERE/'certificates.json').read_text())
    open_leaves=[]
    def collect(tree,node):
        if tree['kind']=='split':
            for child in tree['children']:collect(child,node)
        elif tree['kind']=='open':open_leaves.append((node,tree))
    for r in bank['records']:collect(r['tree'],r['node'])
    # This final bank has exactly one unavoidable OPEN descendant per witness.
    assert len(open_leaves)==9
    for node,leaf in open_leaves:
        candidates=[r for r in records if node in r['nodes']]
        assert len(candidates)==1
        r=candidates[0]
        point=[tuple(map(F,x)) for x in r['point']]
        assert in_box(point,leaf['box'],r['radicand'])
    # Bernstein bases are nonnegative and sum to one on the closed box.
    # Strictly negative controls for sum lambda*g contradict its >=0 value.
    # Strictly positive controls for T-sum lambda*g contradict its <=0 value.
    # The argument also covers every product of these weakly nonnegative g's.
    print('PROVED (verify_obstruction.py): exact T=0, all weak g>=0, connected=0 at nine corner witnesses; nodes',
          [r['nodes'] for r in records])
    print('PROVED (verify_obstruction.py): neither requested strict Bernstein certificate can cover a closed box containing these witnesses, at any finite subdivision depth. These are not feasible counterexamples.')
    print('PROVED (verify_obstruction.py): five witnesses have two edges of weight 1/2; four have a triangle of weight 1/3 per edge. All nine final OPEN leaves contain one witness.')

if __name__=='__main__':main()
