import inherited_arithmetic as lib
from inherited_arithmetic import F,Path,json,time,hashlib,fwht,quartet,entropy,infs,coded_truth,frac
from itertools import combinations
RUN=Path(__file__).resolve().parents[1]
check=lib.check
def save(name,obj):(RUN/'out'/name).write_text(json.dumps(obj,indent=2)+'\n',encoding='utf-8')
def interval(x):return [str(v) for v in x]
def verify(f,name):
    N=len(f);n=(N-1).bit_length();p=F(1,N);old=fwht(f);support=[s for s,v in enumerate(old) if v];count=len(support)
    check(count*(n+1)<=N)
    for s,t in combinations(support,2):check((s^t).bit_count()>=3)
    check(sum(v<0 for v in f)%2==0);check(all(v%4==0 for v in old))
    g=f.copy();g[0]*=-1;new=fwht(g);fi=infs(f);gi=infs(g)
    check(all(v%4==2 for v in new));check(all(new[s]==old[s]-2*f[0] for s in range(N)))
    check(sum(gi)>=2*n*p)
    if len(set(f))>1 and n>=4:
        alpha=F(min(sum(v<0 for v in g),sum(v>0 for v in g)),N)
        check(alpha>=F(n+1,N+n+1)-p)
        an=F(3*n-1,4)*p
        check(alpha>=an and an<=F(11,64))
        check(sum(gi)>=4*alpha*(1-alpha));check(4*an*(1-an)>2*n*p)
    H=entropy([F(v*v,N*N) for v in new]);records=[];beta=[];orientation=[]
    for i in range(n):
        Bup=Jup=GammaUp=F(0);minor=F(0);occupied=0;empty_mass=F(0)
        for t in range(N):
            if t>>i&1:continue
            u,v=new[t],new[t|1<<i];q=u*u+v*v;mass=F(q,N*N)
            check(not(old[t] and old[t|1<<i]))
            check(min(u*u,v*v)==4)
            mi=F(min(u*u,v*v),N*N);minor+=mi
            Bup+=mass*entropy([F(u*u,q),F(v*v,q)])[1]
            w0,w1=u+v,u-v
            hphys=entropy([F(w0*w0,2*q),F(w1*w1,2*q)])
            Jup+=mass*(1-hphys[0])
            c=frac(4*u*u*v*v,q*q)
            GammaUp+=mass*lib.log2(1+c)[1]
            if old[t] or old[t|1<<i]:occupied+=1
            else:empty_mass+=mass
        check(occupied==count);check(empty_mass==4*p-8*count*p*p);check(minor==2*p)
        ri=f[0]*f[1<<i]
        check(gi[i]==fi[i]+2*p*ri)
        oi=gi[i]-minor;check(oi==fi[i]+2*p*(ri-1));check(oi>=0)
        beta.append(minor);orientation.append(oi)
        Lupper=Bup+Jup;Vupper=Bup+GammaUp
        check(Lupper<16*p);check(Vupper<19*p)
        children=[[g[x] for x in range(N) if (x>>i&1)==b] for b in (0,1)]
        childHs=[entropy([F(v*v,len(c)**2) for v in fwht(c)]) for c in children]
        physicalUpper=H[1]-sum(v[0] for v in childHs)/2
        physicalLower=H[0]-sum(v[1] for v in childHs)/2
        check(physicalUpper<16*p)
        # Independent physical restriction agrees with row decrement within rational enclosures.
        Blo=Jlo=F(0)
        for t in range(N):
            if t>>i&1:continue
            u,v=new[t],new[t|1<<i];q=u*u+v*v;mass=F(q,N*N)
            Blo+=mass*entropy([F(u*u,q),F(v*v,q)])[0]
            Jlo+=mass*(1-entropy([F((u+v)**2,2*q),F((u-v)**2,2*q)])[1])
        check(max(physicalLower,Blo+Jlo)<=min(physicalUpper,Lupper))
        records.append({'i':i,'influence':str(gi[i]),'beta':str(minor),'orientation':str(oi),'L_upper':str(Lupper),'physical_L_upper':str(physicalUpper),'V_upper':str(Vupper),'D8_plus_S_upper':str(physicalUpper-8*gi[i])})
    selected=max(range(n),key=lambda i:gi[i]);check(gi[selected]>=2*p)
    check(F(records[selected]['L_upper'])<8*gi[selected])
    check(F(records[selected]['V_upper'])<F(19,2)*gi[selected])
    refunds=F(0);pairV=[]
    for i,j in combinations(range(n),2):
        R=F(0);Bup=Gup=F(0)
        for t in range(N):
            if t&(1<<i|1<<j):continue
            vals=[new[t],new[t|1<<i],new[t|1<<j],new[t|1<<i|1<<j]];q=sum(v*v for v in vals)
            data=quartet(*vals);R+=(data[4]+data[5])/(N*N)
            Bup+=F(q,N*N)*entropy([F(v*v,q) for v in vals])[1]
            Gup+=F(q,N*N)*lib.log2(1+data[2]/q)[1]
        check(R<=16*p);check(Bup+Gup<54*p);refunds+=R
        pairV.append({'pair':[i,j],'refund_sum':str(R),'V_upper':str(Bup+Gup)})
    dv=sum(f[0]!=f[1<<i] for i in range(n));I=sum(gi);T=sum(orientation)+refunds
    check(sum(orientation)==sum(fi)-4*p*dv)
    check(T==I-2*n*p+refunds)
    check(abs(T-sum(fi))<=4*n*p+16*F(n*(n-1),2)*p)
    return {'name':name,'n':n,'support_size':count,'physical_pivotal_edges_at_edit':dv,'I_seed':str(sum(fi)),'I_edited':str(I),'T':str(T),'Theta':str(T/I),'refund_sum':str(refunds),'selected_max_influence_coordinate':selected,'singleton_records':records,'pair_records':pairV}
def main():
    cases=[]
    for code in range(16):
        h=[-1 if code>>x&1 else 1 for x in range(4)]
        cases.append(verify(coded_truth(h),'coded2_'+str(code)))
        save('CASES.json',{'status':'IN_PROGRESS','completed':len(cases),'cases':cases})
    cases.append(verify(coded_truth([-1]+[1]*7),'coded_PD3'))
    for sign in (-1,1):
        for s in range(8):cases.append(verify([sign*(-1 if (x&s).bit_count()%2 else 1) for x in range(8)],'character3_'+str(sign)+'_'+str(s)))
    save('CASES.json',{'status':'PASS','cases':cases})
    scalars=[]
    for n in range(4,33):
        N=1<<n;p=F(1,N);an=F(3*n-1,4)*p
        check(N>=3*(n+1));check(an<=F(11,64));check(4*an*(1-an)>2*n*p)
        check((n+1)**2<=1<<(n+1))
        scalars.append({'n':n,'a_n':str(an),'variance_lower':str(4*an*(1-an)),'2np':str(2*n*p)})
    save('SCALAR_BOUNDARIES.json',{'status':'PASS','cases':scalars,'infinite_extension':'Inductions in proof; finite scalar checks are not an infinite certificate'})
    save('EXACT_CHECK.json',{'status':'PASS','assertions':lib.assertions,'Boolean_roots':33,'singleton_cuts':153,'pair_cuts':324,'scalar_boundaries':29,'runtime_seconds':time.perf_counter()-lib.START,'helper_sha256':hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),'arithmetic_helper_sha256':hashlib.sha256((RUN/'code/inherited_arithmetic.py').read_bytes()).hexdigest(),'source_counts_adopted':False})
    print((RUN/'out/EXACT_CHECK.json').read_text())
if __name__=='__main__':main()
