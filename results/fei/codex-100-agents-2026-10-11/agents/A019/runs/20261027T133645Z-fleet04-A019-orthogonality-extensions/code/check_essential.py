import sys,json,time,hashlib,importlib.util,itertools
from pathlib import Path
from fractions import Fraction as Q
R=Path(__file__).resolve().parents[1]
HP=R.parent/'20261026T211700Z-fleet04-A019-orthogonality-extensions/code/stage.py'
sp=importlib.util.spec_from_file_location('a019_logs',HP);h=importlib.util.module_from_spec(sp);sp.loader.exec_module(h)
count=0
def ck(b):
    global count
    count+=1
    assert b,count
def spectrum(t):
    a=list(t);step=1
    while step<len(a):
        for i in range(0,len(a),step*2):
            for j in range(step):v,w=a[i+j],a[i+j+step];a[i+j]=v+w;a[i+j+step]=v-w
        step*=2
    return tuple(Q(v*v,len(a)**2) for v in a)
def restrict(t,z,b):return tuple(t[(i&((1<<z)-1))|((i>>z)<<(z+1))|(b<<z)] for i in range(len(t)//2))
def fold(p,z):return tuple(p[(i&((1<<z)-1))|((i>>z)<<(z+1))]+p[(i&((1<<z)-1))|((i>>z)<<(z+1))|(1<<z)] for i in range(len(p)//2))
def edges(t):
    return sum(Q(sum(t[x]!=t[x^(1<<i)] for x in range(len(t))),len(t)) for i in range(len(t).bit_length()-1))
def ce(p,q):
    lo=hi=Q(0)
    for a,b in zip(p,q):
        if a:
            ck(b>0);l,u=h.lg(1/b);lo+=a*l;hi+=a*u
    return lo,hi
def outer(t,ref):
    w=(-1,1,1,1)
    true=tuple(1 if e==0 else t[i]*w[s] for s in range(4) for i in range(len(t)) for e in range(2))
    P=spectrum(true);QQ=[ref[i]/16+(Q(1,4) if i==s==0 else 0) for s in range(4) for i in range(len(t)) for e in range(2)]
    ck(sum(P)==sum(QQ)==1);return true,P,QQ
def fixture(k,m,b):
    d=Q(1,2**k);rho=Q(1,2**b);mu=(1-d)**m;p=rho*(1-mu)/2
    labels=['q','u']+['v%d'%i for i in range(b)]
    for j in range(m):labels+=['z%d_%d'%(j,i) for i in range(k)]+['x%d'%j]
    def gval(i):
        g=1
        for j in range(m):
            if all(not(i>>labels.index('z%d_%d'%(j,z))&1) for z in range(k)) and not(i>>labels.index('x%d'%j)&1):g=-g
        return g
    def core(i):
        active=all(not(i>>labels.index('v%d'%z)&1) for z in range(b)) and gval(i)==-1
        return 1-2*(i&(1<<labels.index('q'))!=0) if active else 1-2*(i&(1<<labels.index('u'))!=0)
    original=tuple(core(i) for i in range(1<<len(labels)));P=spectrum(original);ref=tuple(v/2+(Q(1,2) if i==1 else 0) for i,v in enumerate(P))
    ck(sum(ref)==1)
    avI=Q(0);avsector=Q(0);avsource=Q(0);avM=Q(0);total=Q(0);Clo=Chi=Q(0);profiles=[]
    for controls in itertools.product((0,1),repeat=k*m):
        M=sum(all(controls[j*k+i]==0 for i in range(k)) for j in range(m));weight=Q(1,2**(k*m+1))
        for qb in (0,1):
            t=original;r=ref;ll=list(labels)
            for name,value in [('q',qb)]+[('z%d_%d'%(j,i),controls[j*k+i]) for j in range(m) for i in range(k)]:
                z=ll.index(name);t=restrict(t,z,value);r=fold(r,z);ll.pop(z)
            cleaned=0
            for j in range(m):
                if any(controls[j*k+i] for i in range(k)):
                    z=ll.index('x%d'%j);a=restrict(t,z,0);bb=restrict(t,z,1);ck(a==bb)
                    t=a;r=fold(r,z);ll.pop(z);cleaned+=1
            ck(cleaned==m-M)
            active=[ll.index('x%d'%j) for j in range(m) if 'x%d'%j in ll]
            ck(len(active)==M)
            for z in active:ck(any(t[i]!=t[i^(1<<z)] for i in range(len(t))))
            # Literal projected ORIGINAL reference is compared to source product law.
            Rsource=tuple(d**s.bit_count()*(1-d)**(M-s.bit_count()) for s in range(1<<M))
            ck(sum(Rsource)==1);ck(Rsource[-1]==d**M)
            a=rho/2 if M else Q(0);expected=[Q(0)]*len(t);expected[1]=(1-2*p)/2;expected[0]+=Q(1,2)
            for s in range(1<<M):
                for uv in range(1<<(b+1)):expected[uv+(s<<(b+1))]+=rho*rho*(Rsource[s]+(1-2*mu if s==0 else 0))/8
            ck(tuple(expected)==r)
            full,PP,QQ=outer(t,r);actual4=4*edges(full);sigma=1-2*qb
            target=6+(b-1-Q(sigma,2))*rho*(M>0)+rho*M;ck(actual4==target)
            indices=[idx for idx in range(len(PP)) if any((idx>>1)&(1<<z) for z in active)]
            sectorMass=sum(PP[i] for i in indices)
            sector=Q(0)
            if M:
                ck(sectorMass==rho/4)
                for i in indices:
                    if PP[i]:ck(PP[i]==rho*rho/64);ck(QQ[i]==rho*rho*d**M/128)
                sector=sectorMass*(2*b+7+k*M)
            else:ck(sectorMass==0)
            c0,c1=ce(PP,QQ);ck(c0>=sector)
            # Strengthen the physical frontier to FULL cleanup: M0 padding is
            # irrelevant too. All remaining physical variables must be essential.
            ct=t;cr=r;cl=list(ll)
            if not M:
                for name in [name for name in cl if name.startswith('v')]:
                    z=cl.index(name);left=restrict(ct,z,0);right=restrict(ct,z,1);ck(left==right)
                    ct=left;cr=fold(cr,z);cl.pop(z)
            cleanFull,cleanP,cleanQ=outer(ct,cr)
            ck(edges(cleanFull)==edges(full))
            for z in range(len(cleanFull).bit_length()-1):ck(any(cleanFull[i]!=cleanFull[i^(1<<z)] for i in range(len(cleanFull))))
            cleanlo,cleanhi=ce(cleanP,cleanQ);ck(cleanlo>=sector)
            if not M:ck(cleanhi<c0)
            else:ck(cleanP==PP and cleanQ==QQ)
            c0,c1=cleanlo,cleanhi
            # Remainder bound is only certified under its stated mu<1/8.
            if mu<Q(1,8):ck(c1-sector<2*b+8)
            avI+=weight*actual4;avsector+=weight*sector;avM+=weight*M;avsource+=weight*k*M;total+=weight;Clo+=weight*c0;Chi+=weight*c1
            profiles.append({'control':list(controls),'q':qb,'M':M,'source_I':M,'source_CE':k*M,'cleanup_children_collapsed':2**(cleaned+(b if not M else 0)),'conditional_weight':str(weight*2),'sector_mass':str(sectorMass),'sector_CE':str(sector),'all_remaining_physical_coordinates_essential':True})
    pi=1-mu
    ck(total==1);ck(avM==m*d);ck(avsource==k*m*d);ck(avI==6+(b-1)*rho*pi+rho*m*d)
    ck(avsector==rho*((2*b+7)*pi+k*m*d)/4)
    ck(avI-Clo<6+b*rho-rho*m*d*(Q(k,4)-1))
    return {'k':k,'m':m,'b':b,'physical_control_patterns':2**(k*m),'q_profiles':len(profiles),'average_4I':str(avI),'average_source_excess':str((k-4)*m*d),'average_sector_CE':str(avsector),'CE_interval':[str(Clo),str(Chi)],'profiles':profiles}
def block_census():
    out=[]
    for k in range(1,7):
        d=Q(1,2**k);n=k+1;t=(-1,)+(1,)*(2**n-1);p=spectrum(t);ck(p[0]==(1-d)**2);ck(all(x==d*d for x in p[1:]));ck(edges(t)==n*d)
        # Exact entropy<=4I certificate, no logarithmic interval required.
        D=2**(2*k);a=(2**k-1)**2;left=2**int(4*n*d*D)*a**a;right=D**D;ck(left>right)
        # Project controls; the essential x literal has cost k and influence1.
        rr=p
        for z in range(k):rr=fold(rr,0)
        ck(rr==(1-d,d));active=t
        for z in range(k):active=restrict(active,0,0)
        ck(active==(-1,1));ck(edges(active)==1)
        out.append({'k':k,'I':str(n*d),'P0':str(p[0]),'remaining_R':list(map(str,rr)),'active_CE':k,'active_I':1,'certificate_left_hex':hex(left),'certificate_right_hex':hex(right)})
    return out
def main():
    start=time.perf_counter();pilot='--pilot' in sys.argv
    fixtures=[fixture(*z) for z in ([(1,2,1)] if pilot else [(1,2,1),(2,2,1),(1,3,2),(5,1,1)])]
    blocks=[] if pilot else block_census();diagonal=[]
    for t in range(8,65):
        rho=Q(1,2**t);d=rho;m=2**(2*t+4);ck(rho*m*d==16);upper=22+t*rho-4*t;ck(upper<-9);ck(m*d>7);ck(Q(31)**31>Q(2)**152)
        diagonal.append({'b':t,'k':t,'m':str(m),'reserve_upper':str(upper),'disagreement_upper':str(rho/4),'mu_upper':str(1/(1+m*d))})
    result={'status':'PASS','assertions':count,'helper_support_checks':h.checks,'fixtures':fixtures,'block_census':blocks,'diagonal':diagonal,'seconds':time.perf_counter()-start,'helper_sha256':hashlib.sha256(HP.read_bytes()).hexdigest(),'scope':'Exact finite cases verify formulas; analytic derivation proves all b,k,m. No FEI counterfamily.'}
    ck(result['seconds']<60);(R/'out'/('PILOT.json' if pilot else 'CHECKS.json')).write_text(json.dumps(result,indent=2),encoding='utf-8',newline='\n')
    print(json.dumps({k:result[k] for k in ['status','assertions','seconds','helper_support_checks']}))
if __name__=='__main__':main()
