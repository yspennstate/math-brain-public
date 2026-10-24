from pathlib import Path
from fractions import Fraction as Q
import itertools, time, json, sys
import primitives as z
RUN=Path(__file__).resolve().parents[1]
START=time.perf_counter(); COUNTS={}
PILOT='--pilot' in sys.argv
MODE='census' if '--census' in sys.argv else 'history' if '--history' in sys.argv else 'base'
CHUNK=next((int(a.split('=')[1]) for a in sys.argv if a.startswith('--chunk=')),0)
def ck(ok,key):
    assert ok,key
    COUNTS[key]=COUNTS.get(key,0)+1
    assert time.perf_counter()-START<(55 if PILOT else 170),'frozen watchdog'
def tab(k,n): return tuple(1 if k>>j&1 else -1 for j in range(1<<n))
def mean(u):return Q(sum(u),len(u))
def variance(u):return 1-mean(u)**2
def restrict(u,i,b):
    return tuple(u[(x&((1<<i)-1))|((x>>i)<<(i+1))|(b<<i)] for x in range(len(u)//2))
def marginal(labels,cores):
    return {j:Q(labels.count(j),len(labels)) for j in range(len(cores))}
def R(labels,cores):return z.add(*(z.scale(z.phi(p),variance(cores[j])) for j,p in marginal(labels,cores).items()))
def U(labels,cores):
    return z.add(*(z.scale(z.add(z.raw(z.walsh(cores[j])),z.scale(z.phi(mean(cores[j])**2),-1)),p) for j,p in marginal(labels,cores).items()))
def assemble(labels,cores):
    a=len(labels).bit_length()-1; offsets=[];n=a
    for c in cores: offsets.append(n);n+=len(c).bit_length()-1
    return tuple(cores[labels[x&((1<<a)-1)]][(x>>offsets[labels[x&((1<<a)-1)]])&(len(cores[labels[x&((1<<a)-1)]])-1)] for x in range(1<<n))
def full(st):
    r,bmode,gmode,us=st
    s=0 if bmode in ['fail','success'] else int(bmode)
    c=1 if gmode else 0;labels=[]
    for x in range(1<<(1+r+s+c)):
        y=x&1;A=((x>>1)&((1<<r)-1))==((1<<r)-1)
        B=bmode=='success' or (bmode!='fail' and s>0 and ((x>>(1+r))&((1<<s)-1))==((1<<s)-1))
        G=2 if not c or (x>>(1+r+s))&1 else 3
        labels.append(G if not y else 0 if A else 1 if B else G)
    return tuple(labels),tuple(us)+((1,),)
def cutlabels(l,i,b):return restrict(l,i,b)
def local(f,i):
    w=z.walsh(f);bit=1<<i
    B=z.add(*(z.packet(w[k]**2,w[k|bit]**2) for k in range(len(w)) if not k&bit))
    children=[restrict(f,i,b) for b in [0,1]]
    D=z.add(z.raw(w),z.scale(z.add(*(z.raw(z.walsh(c)) for c in children)),Q(-1,2)))
    d=Q(sum(f[k]!=f[k|bit] for k in range(len(f)) if not k&bit),len(f)//2)
    return B,D,d
def other_tables(st):
    r,bmode,gmode,us=st;u,v,g=us
    s=0 if bmode in ['fail','success'] else int(bmode);c=1 if gmode else 0
    Utab=[];Htab=[];Gtab=[]
    for x in range((1<<(s+c))*len(u)*len(v)*len(g)):
        B=bmode=='success' or (bmode!='fail' and s>0 and (x&((1<<s)-1))==((1<<s)-1))
        G=2 if not c or (x>>s)&1 else 3
        base=s+c;uu=u[(x>>base)&(len(u)-1)];base+=len(u).bit_length()-1
        vv=v[(x>>base)&(len(v)-1)];base+=len(v).bit_length()-1
        gg=g[(x>>base)&(len(g)-1)] if G==2 else 1
        Utab.append(uu);Gtab.append(gg);Htab.append(vv if B else gg)
    return tuple(Utab),tuple(Htab),tuple(Gtab)
def case(st):
    r,bmode,gmode,us=st;u,v,g=us
    q=Q(1,1<<r);p=Q(0) if bmode=='fail' else Q(1) if bmode=='success' else Q(1,1<<int(bmode))
    e=1-p;labels,cores=full(st);f=assemble(labels,cores)
    ut,ht,gt=other_tables(st);uw,hw,gw=map(z.walsh,(ut,ht,gt));m,n,ng=mean(u),mean(ht),mean(gt)
    VH=variance(ht);VG=variance(gt);Vu=variance(u);Zg=variance(g)/(2 if gmode else 1)
    B,D,d=local(f,1)
    ck(d==q*(1-m*n)/2,'physical_private_influence')
    packets=[]
    for a,b,c in zip(uw,hw,gw):
        M=(1-q)*b+q*a;w=q*(a-b)
        packets.extend([z.packet((c+M)**2/4,w*w/4),z.packet((M-c)**2/4,w*w/4)])
    formula=z.add(z.scale(z.log(2),(q-2*q*q)*(1-m*n)),*packets)
    ck(B==formula,'private_coherent_identity')
    cross=sum((abs(b*c) for b,c in zip(hw[1:],gw[1:])),Q(0))
    ck(cross==e*VG,'actual_nonempty_cross_mass')
    ck(cross<=VH,'actual_cross_mass_paid_by_VH')
    k=z.add(z.phi(1-q),z.scale(z.phi(1-2*q),Q(-1,2)))
    s=(1+(1-q)*e)/2;s0=(1+e)/2;s1=(1+(1-2*q)*e)/2
    kg=z.add(z.phi(s),z.scale(z.add(z.phi(s0),z.phi(s1)),Q(-1,2)))
    kappa=z.add(z.scale(z.log(2),q*Vu/2),z.scale(k,p*variance(v)/2),z.scale(kg,Zg))
    actual=z.add(R(labels,cores),z.scale(z.add(*(R(cutlabels(labels,1,b),cores) for b in [0,1])),Q(-1,2)))
    ck(actual==kappa,'private_merged_fine_release')
    ck(z.lower_nonnegative(kappa),'private_release_nonnegative')
    ck(z.le(B,z.scale(z.log(2),(12-4*q)*d)),'full_erasure_price12_minus4q')
    ck(z.interval(z.add(D,z.scale(kappa,-1),z.scale(z.log(2),-12*d)))[1]<=2*d or not z.add(D,z.scale(kappa,-1),z.scale(z.log(2),-12*d)),'private_full_D_price')
    ck(U(labels,cores)==z.scale(z.add(*(U(cutlabels(labels,1,b),cores) for b in [0,1])),Q(1,2)),'private_U_harmonic')
    # Source A091 Y reveal, checked on the same physical function independently.
    BY,DY,dY=local(f,0);pu=q;pv=(1-q)*p;t=pu+pv
    h0=pu*(m-ng)+pv*(mean(v)-ng)
    varh=pu*(m-ng)**2+pv*(mean(v)-ng)**2-h0*h0
    kt=z.add(z.phi(1-t/2),z.scale(z.phi(1-t),Q(-1,2)))
    kapY=z.add(z.scale(z.log(2),(pu*Vu+pv*variance(v))/2),z.scale(kt,Zg))
    actualY=z.add(R(labels,cores),z.scale(z.add(*(R(cutlabels(labels,0,b),cores) for b in [0,1])),Q(-1,2)))
    ck(dY==(pu*(1-m*ng)+pv*(1-mean(v)*ng))/2,'source_Y_physical_influence')
    ck(kapY==actualY,'source_Y_merged_release')
    rhs=z.add(z.scale(z.log(2),varh/2+t*(1-t)*VG/2),z.packet((ng+h0/2)**2,h0*h0/4),z.scale(z.packet((1-t/2)**2,t*t/4),VG),z.scale(kt,-Zg))
    ck(z.add(BY,z.scale(kapY,-1))==rhs,'source_Y_exact_residual')
    ck(z.le(rhs,z.scale(z.log(2),8*dY)),'source_Y_eight_price')
    ck(z.interval(z.add(DY,z.scale(kapY,-1),z.scale(z.log(2),-8*dY)))[1]<=2*dY or not z.add(DY,z.scale(kapY,-1),z.scale(z.log(2),-8*dY)),'source_Y_full_D_price')
    return f,labels,cores
def history(st,which,coordinate):
    f,labels,cores=case(st);r,bmode,gmode,us=st
    s=0 if bmode in ['fail','success'] else int(bmode);bit=1+r+s+(1 if gmode else 0)+sum(len(x).bit_length()-1 for x in us[:which])+coordinate
    _,D,d=local(f,bit);P=marginal(labels,cores)[which];beta=z.walsh(us[which])[1<<coordinate]
    actualR=[];actualU=[];childstates=[]
    for b in [0,1]:
        newus=list(us);newus[which]=restrict(newus[which],coordinate,b);ch=(r,bmode,gmode,tuple(newus));childstates.append(ch)
        ff,ll,cc=case(ch);ck(ff==restrict(f,bit,b),'actual_data_child')
        actualR.append(R(ll,cc));actualU.append(U(ll,cc))
    dr=z.add(R(labels,cores),z.scale(z.add(*actualR),Q(-1,2)))
    du=z.add(U(labels,cores),z.scale(z.add(*actualU),Q(-1,2)))
    ck(dr==z.scale(z.phi(P),beta*beta),'data_exact_variance_log_release')
    rem=z.add(D,z.scale(dr,-1),z.scale(du,-1))
    ck(z.interval(rem)[1]<=3*P*beta*beta or not rem,'signed_data_three_price')
    # Literal stopped profile at the four actual grandchildren: no alternative frontier.
    profiles=[];ctrlspent=Q(0)
    for ch in childstates:
        ll,cc=full(ch);ff=assemble(ll,cc);_,_,di=local(ff,1);ctrlspent+=di/2
        for b in [0,1]:
            lc=cutlabels(ll,1,b);fc=restrict(ff,1,b)
            profiles.append(z.add(z.raw(z.walsh(fc)),z.scale(U(lc,cc),-1),z.scale(R(lc,cc),-1)))
    term=z.add(z.raw(z.walsh(f)),z.scale(U(labels,cores),-1),z.scale(R(labels,cores),-1),z.scale(z.add(*profiles),Q(-1,4)),z.scale(z.log(2),-12*ctrlspent))
    ck(z.interval(term)[1]<=3*P*beta*beta+2*ctrlspent or not term,'actual_two_step_stopped_payment')
def main():
    roots=histories=0
    if MODE=='census':
        pool=[tab(k,2) for k in range(16)]
        triples=list(itertools.product(pool,repeat=3))[CHUNK*512:(CHUNK+1)*512]
        for us in triples[:8] if PILOT else triples:case((1,'1',False,us));roots+=1
    elif MODE=='history':
        us=(tab(8,2),tab(7,2),tab(14,2))
        domain=list(itertools.product([1,2,3],['fail','success','1','2'],[False,True],range(3),range(2)))
        for r,b,g,j,i in domain[:2] if PILOT else domain:history((r,b,g,us),j,i);histories+=1
    else:
        pool=[tab(k,1) for k in range(4)]
        domain=list(itertools.product([1,2,3],['fail','success','1','2'],[False,True],itertools.product(pool,repeat=3)))
        for r,b,g,us in domain[:4] if PILOT else domain:case((r,b,g,us));roots+=1
    out={'status':'PASS','mode':MODE,'chunk':CHUNK,'pilot':PILOT,'roots':roots,'physical_two_step_histories':histories,'counts':COUNTS,'assertions':sum(COUNTS.values()),'seconds':time.perf_counter()-START,'arithmetic':'exact Fraction Walsh/edge tables, prime-log equalities,48-term rational atanh signs with geometric remainder','scope':'new earliest private-before-Y price and independently reconstructed source Y payment; no out-of-priority or fallback-internal-before-Y claim'}
    name=('PILOT_' if PILOT else '')+MODE+(f'_{CHUNK}' if MODE=='census' else '')+'.json'
    (RUN/'out'/name).write_text(json.dumps(out,indent=2)+'\n',encoding='utf-8');print(json.dumps(out))
if __name__=='__main__':main()
