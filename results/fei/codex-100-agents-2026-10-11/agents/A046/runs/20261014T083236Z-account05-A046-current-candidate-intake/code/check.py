from pathlib import Path
from fractions import Fraction as Q
from functools import lru_cache
import itertools,json,time,runpy
ROOT=Path(__file__).resolve().parents[1]
h=runpy.run_path(str(ROOT.parent/'20261014T012528Z-account05-A046-current-candidate-intake'/'code'/'layers.py'))
add,mul,sub,Z,phi,term,fmt=h['add'],h['mul'],h['sub'],h['ZERO'],h['phi'],h['term'],h['fmt']
@lru_cache(None)
def sp(g):
    arr=list(g);step=1
    while step<len(arr):
        for base in range(0,len(arr),2*step):
            for k in range(base,base+step):a,b=arr[k],arr[k+step];arr[k],arr[k+step]=a+b,a-b
        step*=2
    return tuple(Q(x,len(g)) for x in arr)
def influence(g,i):return Q(sum(g[x]!=g[x^(1<<i)] for x in range(len(g))),len(g))
def It(g):return sum((influence(g,i) for i in range(len(g).bit_length()-1)),Q(0))
def child(g,i,b):return tuple(y for x,y in enumerate(g) if x>>i&1==b)
def entropy_g(g):return h['old']['entropy']([x*x for x in sp(g)])
def Fhat(ws,mask,t,spectrum):
    A=h['coeff'](ws,mask)
    return Q(mask==0)*(t==0)+(spectrum[t]-(t==0))*A
def selector(g,j,L,R,T):
    a=1-sp(g)[0];q,r=Q(1,2**R),Q(1,2**T);eta=Q(1,2**(L+R+T));e=q+r-q*r-eta;rho=Q(1,2**(j-1));d=rho*a*e/2
    B=Z;tot=Q(0)
    for mask,count in h['rows']((j-1,R,T,L)):
        for t in range(len(g)):
            u=Fhat((None,R,T,L),mask,t,sp(g));v=Fhat((j-1,R,T,L),mask,t,sp(g))
            x,y=((u+v)/2)**2,((u-v)/2)**2
            B=add(B,mul(count,phi(x,y)));tot+=count*(x+y)
    assert tot==1
    if not d:assert B==Z
    elif j>=4 or a*e<=Q(1,16):assert B[1]<4*d
    return a,e,d,B
def bank(g,j,L,R,T):
    q,r=Q(1,2**R),Q(1,2**T);eta=Q(1,2**(L+R+T));e=q+r-q*r-eta
    JB=(L+R+T)*eta;JC=R*q*(1-r)+T*r*(1-q);alpha=Q(1,2**j)
    M=min(j,0 if min(R,T)>=4 else 3);a=1-sp(g)[0]
    return alpha*(a*M*(JB+JC)+a*e*M*(M-1)/2+M*e*It(g))
def data(g,j,L,R,T,i):
    g0,g1=child(g,i,0),child(g,i,1);s0,s1=sp(g0),sp(g1)
    B=Z;hmix=Z;hc=Z;tot=Q(0)
    for mask,count in h['rows']((j,R,T,L)):
        for t in range(len(g0)):
            u=Fhat((j,R,T,L),mask,t,s0);v=Fhat((j,R,T,L),mask,t,s1)
            aa,bb=((u+v)/2)**2,((u-v)/2)**2;qq=aa+bb
            B=add(B,mul(count,phi(aa,bb)));hmix=add(hmix,mul(count,term(qq)))
            hc=add(hc,mul(Q(count,2),add(term(u*u),term(v*v))));tot+=count*qq
    assert tot==1
    J=sub(hmix,hc);D=add(B,J)
    q,r=Q(1,2**R),Q(1,2**T);eta=Q(1,2**(L+R+T));e=q+r-q*r-eta;alpha=Q(1,2**j);pi=eta+alpha*e
    rel=bank(g,j,L,R,T)-(bank(g0,j,L,R,T)+bank(g1,j,L,R,T))/2
    M=min(j,0 if min(R,T)>=4 else 3)
    assert rel==alpha*M*e*influence(g,i)
    assert 0<=rel<=3*pi*influence(g,i)
    coreD=sub(entropy_g(g),mul(Q(1,2),add(entropy_g(g0),entropy_g(g1))))
    residual=sub(sub(D,mul(pi,coreD)),(rel,rel))
    return {'query':i,'physical_influence':str(pi*influence(g,i)),'release':str(rel),'B_data_bits':fmt(B),'JS_data_bits':fmt(J),'signed_after_terminal_increment_and_release':fmt(residual),'child_terminal_entropy_bits':[fmt(mul(pi,entropy_g(g0))),fmt(mul(pi,entropy_g(g1)))],'child_banks':[str(bank(g0,j,L,R,T)),str(bank(g1,j,L,R,T))]}
def main():
    start=time.perf_counter();cores=[tuple(-1 if mask>>x&1 else 1 for x in range(4)) for mask in range(16)]
    maj=tuple(1 if x.bit_count()>=2 else -1 for x in range(8));point=tuple(-1 if x==7 else 1 for x in range(8));par=tuple((-1)**x.bit_count() for x in range(8));one=(1,)*8
    cores+= [g for base in (maj,point,par,one) for g in (base,tuple(-x for x in base))]
    nodes=[];queries=[];twostep=checks=0
    for idx,g in enumerate(cores):
        n=len(g).bit_length()-1
        for j,(L,R,T) in itertools.product((1,2,4),((1,1,1),(1,2,2),(1,4,4))):
            a,e,d,B=selector(g,j,L,R,T);checks+=2
            alpha=Q(1,2**j);eta=Q(1,2**(L+R+T));q,r=Q(1,2**R),Q(1,2**T)
            Is=j*alpha*a*e;Io=a*((1-alpha)*(L+R+T)*eta+alpha*(R*q*(1-r)+T*r*(1-q)));Iter=(eta+alpha*e)*It(g)
            assert bank(g,j,L,R,T)<=3*(Is+Io+Iter);checks+=1
            nodes.append({'core_id':idx,'j':j,'L':L,'R':R,'T':T,'a':str(a),'a_e':str(a*e),'B_over_d':fmt(mul(1/d,B)) if d else ['0','0'],'root_bank':str(bank(g,j,L,R,T))})
            for i in range(n):
                rec=data(g,j,L,R,T,i);rec.update({'core_id':idx,'j':j,'L':L,'R':R,'T':T});queries.append(rec);checks+=3
                for k in range(n):
                    if k==i:continue
                    local=k-(k>i);g0,g1=child(g,i,0),child(g,i,1)
                    booked=bank(g,j,L,R,T)-(bank(g0,j,L,R,T)+bank(g1,j,L,R,T))/2
                    nextrel=Q(0);leaves=Q(0)
                    for cc in (g0,g1):
                        c0,c1=child(cc,local,0),child(cc,local,1)
                        nextrel+=(bank(cc,j,L,R,T)-(bank(c0,j,L,R,T)+bank(c1,j,L,R,T))/2)/2
                        leaves+=(bank(c0,j,L,R,T)+bank(c1,j,L,R,T))/4
                    assert booked+nextrel+leaves==bank(g,j,L,R,T);twostep+=1;checks+=1
        (ROOT/'out'/'CHECK.json').write_text(json.dumps({'status':'IN_PROGRESS','completed_cores':idx+1,'nodes':nodes,'data_queries':queries},indent=2)+'\n',encoding='utf-8')
        if time.perf_counter()-start>55:raise SystemExit('pilot budget stop')
    assert Q(44,31)<Q(3,2) and Q(3,2)**5<8
    assert Q(3,2)**2*Q(2,5)<Q(19,20)**2
    assert 2+Q(3,5)+Q(19,20)+Q(23,64)==Q(1251,320)<4
    assert (Q(87,56))**20<2**13 and Q(842,1215)>Q(9,13)
    assert Q(1957,720)+Q(1,4410)<Q(87,32)
    assert 2+Q(13,20)+Q(26,63)+Q(67,72)==Q(10063,2520)<4
    checks+=7
    out={'status':'PASS','core_truth_tables':len(cores),'selector_nodes':len(nodes),'actual_data_queries':len(queries),'same_owner_two_query_ledgers':twostep,'recorded_assertions':checks,'runtime_seconds':time.perf_counter()-start,'max_grouped_dimension':16,'nodes':nodes,'data_queries':queries}
    (ROOT/'out'/'CHECK.json').write_text(json.dumps(out,indent=2)+'\n',encoding='utf-8');print(json.dumps({k:v for k,v in out.items() if k not in ('nodes','data_queries')}))
if __name__=='__main__':main()
