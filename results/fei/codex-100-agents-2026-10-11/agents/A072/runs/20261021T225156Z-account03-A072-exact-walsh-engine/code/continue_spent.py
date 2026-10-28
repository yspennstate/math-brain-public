"""All prescribed other-core queries after the exact minimal sibling transfer."""
from third_query import *
import sys

def full(ts):
    cs=[core(t) for t in ts]
    op=outer('J',tuple(c['p'] for c in cs))
    h,inf=composed(op,cs)
    return dict(ts=ts,cs=cs,op=op,H=h,I=inf,S=sub(const(4*inf),h))

def split(p,j,i):
    cs=[]
    for bit in (0,1):
        ts=list(p['ts']);ts[j]=child(ts[j],i,bit);cs.append(full(tuple(ts)))
    d=p['op']['q'][j]*p['cs'][j]['d'][i]
    ck(p['I']-sum(c['I'] for c in cs)/2==d)
    for k in range(6):ck(sum(c['op']['q'][k] for c in cs)/2==p['op']['q'][k])
    e=sub(sub(p['H'],avg([c['H'] for c in cs])),const(4*d))
    return cs,e,d

def overlaps(a,b):ck(a[0]<=b[1] and b[0]<=a[1])

def setup():
    root=full((G,)*6)
    first,e1,_=split(root,0,2)
    second,e2,_=split(first[0],0,0)
    U2=[scale(p['cs'][0]['S'],p['op']['q'][0]) for p in second]
    t2=plus(scale(e1,F(2)),e2);B2=avg(U2)
    D=[mul(div(t2,B2),u) for u in U2]
    third,e3,_=split(second[0],0,1) # surviving labels [1,3,4,5], hence original3
    U3=[scale(p['cs'][0]['S'],p['op']['q'][0]) for p in third]
    M3=[sub(p['S'],u) for p,u in zip(third,U3)]
    ck(M3[0][1]<0 and M3[1][0]>0)
    V0=plus(U3[0],M3[0]);ck(U3[1]==(0,0))
    T=plus(D[0],e3);tau=sub(T,scale(V0,F(1,2)))
    ck(tau[0]>0)
    debits=[V0,scale(tau,F(2))]
    ck(sub(third[1]['S'],debits[1])[0]>0)
    overlaps(avg(debits),T)
    return root,first,second,third,debits,D,e1,e2,e3

def main():
    start=time.perf_counter();root,first,second,third,debits,D,e1,e2,e3=setup()
    rows=[];pairs=[(b,j,i) for b in range(2) for j in range(1,6) for i in range(6)]
    if '--pilot' in sys.argv:pairs=pairs[:2]
    for b,j,i in pairs:
        p=third[b];cs,e,d=split(p,j,i);T=plus(debits[b],e)
        B=avg([c['S'] for c in cs]);mean_remaining=sub(B,T)
        # Algebraic identity B-T=S_parent-D is exact; interval overlap is a diagnostic.
        overlaps(mean_remaining,sub(p['S'],debits[b]))
        leafs=[]
        for c in cs:
            u=scale(c['cs'][j]['S'],c['op']['q'][j]);m=sub(c['S'],u)
            v=sub(u,(max(0,-m[1]),max(0,-m[0])))
            w=(max(0,m[0]),max(0,m[1]))
            leafs.append(dict(H=c['H'],I=str(c['I']),S=c['S'],raw_U=u,signed_M=m,V=v,W=w))
        positive=all(c['S'][0]>0 for c in cs)
        negative=any(c['S'][1]<0 for c in cs)
        row=dict(terminal=b,block=j,coordinate=i,incoming_debit=debits[b],physical_influence=str(d),
                 e=e,required_T=T,mean_full_B=B,mean_remaining=mean_remaining,
                 all_full_children_positive=positive,negative_full_child=negative,
                 corrected_selected_negative=any(c['V'][1]<0 for c in leafs),children=leafs)
        # Nonnegative child debit cannot fit into a negative full child capacity.
        # If all capacities are positive and 0<T<B, proportional transport works.
        if positive and T[0]>0:
            ck(sub(B,T)[0]>0 if b==1 else True)
            theta=div(T,B)
            row['booked']=[mul(theta,c['S']) for c in cs]
            row['remainders']=[sub(c['S'],a) for c,a in zip(cs,row['booked'])]
            overlaps(avg(row['booked']),T)
        rows.append(row)
        (ROOT/'out'/('PILOT_CASES.json' if '--pilot' in sys.argv else 'CONTINUATION_CASES.json')).write_text(json.dumps(rows,indent=2)+'\n',encoding='utf-8')
        ck(time.perf_counter()-start<55)
    result=dict(version='A071-spent-sibling-v1',cases=len(rows),engine_checks=engine.tests,runtime_seconds=time.perf_counter()-start,
        negative_full_child_cases=sum(r['negative_full_child'] for r in rows),
        corrected_selected_negative_cases=sum(r['corrected_selected_negative'] for r in rows),
        positive_full_children_cases=sum(r['all_full_children_positive'] for r in rows),
        nonpositive_required_debit_cases=sum(r['required_T'][1]<=0 for r in rows),
        display=[dict(b=r['terminal'],j=r['block'],i=r['coordinate'],e=display(r['e']),T=display(r['required_T']),S=[display(c['S']) for c in r['children']]) for r in rows])
    (ROOT/'out'/('PILOT.json' if '--pilot' in sys.argv else 'RESULTS.json')).write_text(json.dumps(result,indent=2)+'\n',encoding='utf-8')
    print(json.dumps({k:v for k,v in result.items() if k!='display'}))

if __name__=='__main__':main()
