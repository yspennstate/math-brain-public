"""Construct the rank-one coupling by exact Edmonds–Karp, without an LP solver."""
from exact_transport import Instance,rational_orthogonal,dump,ROOT,F
from collections import deque,defaultdict

def run():
    inst=Instance(rational_orthogonal(5,341501,'cayley'))
    ucols=(0,);wcols=(1,2);a=inst.law(wcols);b=inst.law((0,1,2))
    cap={};adj=defaultdict(list)
    def edge(v,w,c):
        cap[v,w]=c;cap[w,v]=F(0);adj[v].append(w);adj[w].append(v)
    s=('source',);t=('sink',)
    for B,mass in a.items():edge(s,('B',B),mass)
    for B in a:
        for C in b:
            if set(B)<=set(C):edge(('B',B),('C',C),F(1))
    for C,mass in b.items():edge(('C',C),t,mass)
    value=F(0);augmentations=0
    while True:
        pred={s:None};queue=deque([s])
        while queue and t not in pred:
            v=queue.popleft()
            for w in adj[v]:
                if w not in pred and cap[v,w]>0:pred[w]=v;queue.append(w)
        if t not in pred:break
        path=[];w=t
        while w!=s:
            v=pred[w];path.append((v,w));w=v
        amount=min(cap[e] for e in path)
        for v,w in path:cap[v,w]-=amount;cap[w,v]+=amount
        value+=amount;augmentations+=1
    assert value==1
    rows=[];first=defaultdict(F);second=defaultdict(F);union=defaultdict(F)
    for B in a:
        for C in b:
            if set(B)<=set(C):
                mass=cap[('C',C),('B',B)]
                if mass:
                    e=next(iter(set(C)-set(B)));prob=inst.Q[e][0]**2
                    assert prob>0
                    rows.append({'e':e,'B':list(B),'C':list(C),'joint_mass':str(mass),'conditional_q_e_B':str(mass/prob)})
                    first[(e,)]+=mass;second[B]+=mass;union[C]+=mass
    for got,target in [(first,inst.law(ucols)),(second,a),(union,b)]:
        assert all(got.get(k,0)==target.get(k,0) for k in got.keys()|target.keys())
    cert={'n':5,'columns1':[0],'columns2':[1,2],
          'Q':[[str(x) for x in row] for row in inst.Q],
          'coupling':[{'A':[row['e']],'B':row['B'],'mass':row['joint_mass']} for row in rows],
          'conditional_laws':rows,'method':'Exact Fraction Edmonds-Karp on the inclusion graph','augmentations':augmentations}
    dump(ROOT/'data/rank_one_flow.json',cert)
    print('Exact rank-one flow: value 1,',augmentations,'augmentations,',len(rows),'positive joint masses')
if __name__=='__main__':run()
