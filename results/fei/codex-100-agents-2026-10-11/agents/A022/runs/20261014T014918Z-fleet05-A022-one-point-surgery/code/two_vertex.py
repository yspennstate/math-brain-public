from pathlib import Path
from fractions import Fraction as Q
import time,json
RUN=Path(__file__).resolve().parents[1]
ns={'__file__':str(RUN/'code/check.py'),'__name__':'two_vertex_kernel'}
exec((RUN/'code/check.py').read_text(encoding='utf-8').split('\ncases=0')[0],ns)
stats=ns['stats'];phi=ns['phi'];add=ns['add'];interval=ns['interval'];fwht=ns['ns']['fwht']
START=time.perf_counter();checks=0;rows=[];Amask=Xmask=0
for z in range(16):
    x=[(z>>i)&1 for i in range(4)];events=[x[1]*x[2],x[1]*x[3],x[0]*x[2]*x[3]]
    if any(events):Amask|=1<<z
    if sum(events)%2:Xmask|=1<<z
def ck(v):
    global checks
    assert v
    checks+=1
def walk(f,k,Ha,Hc,depth=0):
    if time.perf_counter()-START>60:raise TimeoutError('frozen cap')
    H,inf=stats(f);m=k//2
    if depth==m:return Q(0),sum(inf[:m]),sum(inf[m:]),H
    B,JS,d=ns['split'](f);ck(d>=Q(1,4))
    l=walk(f[::2],k,Ha,Hc,depth+1);r=walk(f[1::2],k,Ha,Hc,depth+1)
    removed=d+(l[0]+r[0])/2;data=(l[1]+r[1])/2;ctrl=(l[2]+r[2])/2
    leafH=add((Q(1,2),l[3]),(Q(1,2),r[3]))
    ck(removed+data+ctrl==sum(inf));return removed,data,ctrl,leafH
for Bmask in (Xmask,43690):
    A=tuple(Q((Amask>>z)&1) for z in range(16));B=tuple(Q((Bmask>>z)&1) for z in range(16))
    a=tuple(1-2*x for x in A);c=tuple(1-2*x for x in B)
    Ha,ia=stats(a);Hc,ic=stats(c);alpha=sum(A)/16;beta=sum(B)/16;zeta=sum(x*y for x,y in zip(A,B))/16
    ahat=tuple(Q(x,16) for x in fwht(A));bhat=tuple(Q(x,16) for x in fwht(B))
    for k in (6,8):
        for v,w in ((0,2),(0,5)):
            if time.perf_counter()-START>60:raise TimeoutError('frozen cap')
            m=k//2;dm=(1<<m)-1;N=1<<k;delta=Q(1,N);f=[]
            for u in range(N*16):
                x=ns['data_vertex'](u&dm,(u>>m)&dm,k);z=u>>k;s=ns['bent'](x,k)
                active=(x==v and A[z]) or (x==w and B[z]);f.append(-s if active else s)
            f=tuple(f);H,inf=stats(f)
            bv=ns['bent'](v,k);bw=ns['bent'](w,k)
            expected=[]
            for j in list(range(0,k,2))+list(range(1,k,2)):
                expected.append(Q(1,2)+2*delta*(alpha*bv*ns['bent'](v^(1<<j),k)+beta*bw*ns['bent'](w^(1<<j),k))
                    -(4*delta*bv*bw*zeta if w==v^(1<<j) else 0))
            ck(tuple(inf[:k])==tuple(expected));ck(sum(inf[k:])==delta*(sum(ia)+sum(ic)))
            natural_b=tuple(ns['bent'](x,k) for x in range(N));bhat_data=tuple(Q(x,N) for x in fwht(natural_b))
            root=()
            for S in range(N):
                cv=bv*((-1)**((S&v).bit_count()%2));cw=bw*((-1)**((S&w).bit_count()%2))
                root=add((1,root),(1,phi((bhat_data[S]-2*delta*(cv*alpha+cw*beta))**2)))
            for T in range(1,16):
                u=bv*ahat[T];z=bw*bhat[T]
                root=add((1,root),(N//2,phi(4*delta*delta*(u+z)**2)),(N//2,phi(4*delta*delta*(u-z)**2)))
            ck(H==root)
            removed,data,ctrl,leafH=walk(f,k,Ha,Hc)
            inherited=add((delta,Ha),(delta,Hc))
            ck(sum(inf[:k])==removed+data);ck(ctrl==sum(inf[k:]))
            ck(interval(add((1,H),(-1,inherited)))[1]<=9*sum(inf[:k]))
            ck(interval(add((1,leafH),(-1,inherited)))[1]<=9*data)
            rows.append({'k':k,'vertices':[v,w],'A_mask':Amask,'B_mask':Bmask,'EA':str(alpha),'EB':str(beta),'EAB':str(zeta),
                'I_data':str(sum(inf[:k])),'I_ctrl':str(ctrl),'I_access':str(removed),'I_terminal_data':str(data),
                'inherited_H_coefficient_each':str(delta),'access_bad_credit':'0','verdict':'PASS'})
result={'cases':len(rows),'checks':checks+ns['CHECKS']+ns['ns']['CHECKS']+ns['ns']['ns']['ASSERTIONS'],
    'runtime_seconds':time.perf_counter()-START,'verdict':'PASS','rows':rows}
(RUN/'out/TWO_VERTEX_RESULTS.json').write_text(json.dumps(result,indent=2)+'\n',encoding='utf-8')
print(json.dumps({k:v for k,v in result.items() if k!='rows'}))
