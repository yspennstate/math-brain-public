"""A075 fixed physical prefix, with exact finite and analytic rare limits."""
from block_reveal import *
from asymptotic import plus,times,mul,ev,entseries,zero,aadd,ascale,coeff,boundtriple

# s is the number of fixed original coordinates; A is the remaining sparse side.
SHAPES={'r':(0,(0,1,2)), 'a':(1,(0,1,2)), 'b':(2,(0,1)),
        'c':(2,(0,)), 'd':(3,(0,1)), 'z':(3,())}

def sparse(n,s,A):
    dim=n-s;N=1<<dim;a=len(A);p=Q(a,N)
    L=[sum((-1)**((x&z).bit_count()) for x in A) for z in range(4)]
    hg=hm((1-2*p)**2)
    for z,l in enumerate(L): hg=ar.add(hg,hm(Q(4*l*l,N*N)),Q(N//4-(z==0)))
    edges=sum((x^(1<<j)) in A for x in A for j in range(2))//2
    I=Q(2*a*dim-4*edges,N)
    if n<=8:
        t=[-1 if x in A else 1 for x in range(N)];w=ar.fwht(t)
        ar.ck(ar.entropy(w)==hg)
        ar.ck(sum(Q(x*x,N*N)*i.bit_count() for i,x in enumerate(w))==I)
    return p,I,hg,ar.add({2:4*I},hg,Q(-1))

def profile(n,name):
    base=sparse(n,*SHAPES['r']);cur=sparse(n,*SHAPES[name])
    C,q,masses=outer([cur[0]]+[base[0]]*5)
    S=ar.add(ar.add(ar.scale(cur[3],q[0]),ar.scale(base[3],sum(q[1:]))),C,Q(-1))
    U=ar.scale(cur[3],q[0]);M=ar.add(S,U,Q(-1))
    return {'C':C,'q':q,'S':S,'U':U,'M':M,'masses':masses,'I':q[0]*cur[1]+sum(q[1:])*base[1]}

def iadd(x,y):return x[0]+y[0],x[1]+y[1]
def ineg(x):return -x[1],-x[0]
def isub(x,y):return iadd(x,ineg(y))
def imul(x,y):
    v=[a*b for a in x for b in y];return min(v),max(v)
def idiv(x,y):
    ar.ck(y[0]>0);return imul(x,(1/y[1],1/y[0]))
def icon(x):return Q(x),Q(x)
def mean(x,y):return imul(iadd(x,y),icon(Q(1,2)))
def iv(e):return ar.enclose(e)
def saveiv(x):return {'lower':str(x[0]),'upper':str(x[1]),'display':[float(t) for t in x]}
def excess(p,c,d):return ar.add(ar.add(ar.scale(c['S'],Q(1,2)),ar.scale(d['S'],Q(1,2))),p['S'],Q(-1))

def finite(n):
    z={k:profile(n,k) for k in SHAPES}
    e1=excess(z['r'],z['a'],z['z']);e2=excess(z['a'],z['b'],z['c']);e3=excess(z['b'],z['d'],z['z'])
    T2=iv(ar.add(ar.scale(e1,Q(2)),e2));B2=iv(ar.scale(ar.add(z['b']['U'],z['c']['U']),Q(1,2)))
    D=imul(idiv(T2,B2),iv(z['b']['U']));T=iadd(D,iv(e3))
    Md=iv(z['d']['M']);Ud=iv(z['d']['U']);Mz=iv(z['z']['M'])
    cost=(max(Q(0),-Md[1]),max(Q(0),-Md[0]))
    V=isub(Ud,cost);Wd=(max(Q(0),Md[0]),max(Q(0),Md[1]))
    Wz=(max(Q(0),Mz[0]),max(Q(0),Mz[1]));B=imul(V,icon(Q(1,2)));Wmean=mean(Wd,Wz)
    gap=isub(T,B);tau=(max(Q(0),gap[0]),max(Q(0),gap[1]));full=isub(iadd(B,Wmean),T)
    result={'n':n,'p':str(Q(3,1<<n)),'profiles':{k:{j:val(z[k][j]) for j in ['S','U','M','C']} for k in z},
        'e1':val(e1),'e2':val(e2),'e3':val(e3),'D':saveiv(D),'T':saveiv(T),'B':saveiv(B),'W':saveiv(Wmean),'signed_T_minus_B':saveiv(gap),
        'tau':saveiv(tau),'remaining':saveiv(full),'T2_over_B2':saveiv(idiv(T2,B2)),
        'selected_child_M_negative':Md[1]<0,'selected_child_S_positive':iv(z['d']['S'])[0]>0,
        'donor_positive':Mz[0]>0,'transfer_needed':tau[0]>0,'transfer_feasible':V[0]>=0 and full[0]>0}
    if Wmean[0]>0:result['fraction']=saveiv(idiv(tau,Wmean))
    p=Q(3,1<<n)
    for j,x in [('D',D),('T',T),('B',B),('W',Wmean),('tau',tau),('remaining',full)]:result[j+'_over_p2']=saveiv(imul(x,icon(1/p**2)))
    ar.ck(z['r']['I']-(z['a']['I']+z['z']['I'])/2>=0)
    ar.ck(T2[0]>0 and B2[0]>0 and isub(B2,T2)[0]>0)
    ar.ck(iv(z['b']['M'])[0]>0 and iv(z['c']['M'])[0]>0)
    ar.ck(D[0]>0 and T[0]>0 and result['transfer_feasible'])
    (ROOT/'out'/('n'+str(n)+'.json')).write_text(json.dumps(result,indent=2)+'\n',encoding='utf-8')
    return result

def packets(n,shape):
    """Independent A(other)+core0*B(other) direct occupied-packet expansion."""
    base=sparse(n,*SHAPES['r']);cur=sparse(n,*shape)
    mu=1-2*base[0];mu0=1-2*cur[0];v=1-mu*mu;v0=1-mu0*mu0
    A=[Q(J[2*x]+J[2*x+1],2) for x in range(32)]
    B=[Q(J[2*x]-J[2*x+1],2) for x in range(32)]
    WA=ar.fwht(A);WB=ar.fwht(B)
    entropy={};counts=[Q(0)]*6;total=Q(0);masses=[Q(0)]*64
    for T in range(32):
        a=sum((WA[U]*mu**((U^T).bit_count())/32 for U in range(32) if U&T==T),Q(0))
        b=sum((WB[U]*mu**((U^T).bit_count())/32 for U in range(32) if U&T==T),Q(0))
        factor=v**T.bit_count();m0=factor*(a+mu0*b)**2;m1=factor*v0*b*b
        masses[2*T]=m0;masses[2*T+1]=m1
        entropy=ar.add(ar.add(entropy,hm(m0)),hm(m1));total+=m0+m1;counts[0]+=m1
        for j in range(5):
            if T>>j&1:counts[j+1]+=m0+m1
    ar.ck(total==1)
    I=Q(0)
    for j,c in enumerate([cur]+[base]*5):
        var=4*c[0]*(1-c[0]);mu2=1-var
        if not var:ar.ck(counts[j]==0);continue
        hc=ar.add(ar.add(c[2],hm(mu2),Q(-1)),hm(var),Q(-1))
        entropy=ar.add(entropy,hc,counts[j]/var);I+=counts[j]*c[1]/var
    return entropy,I,masses

def polynomials(t):
    ts=[t]+[Q(1)]*5;ms=[[Q(1),-2*x] for x in ts];vs=[[Q(0),4*x,-4*x*x] for x in ts]
    masses=[];qs=[]
    for T in range(64):
        c=[Q(0)];v=[Q(1)]
        for U,w in enumerate(W):
            if U&T!=T:continue
            term=[Q(w,64)]
            for j in range(6):
                if (U^T)>>j&1:term=times(term,ms[j])
            c=plus(c,term)
        for j in range(6):
            if T>>j&1:v=times(v,vs[j])
        masses.append(times(v,times(c,c)))
    total=[Q(0)]
    for m in masses:total=plus(total,m)
    ar.ck(total==[Q(1)])
    for j in range(6):
        q=[Q(0)]
        for x in range(64):
            if x>>j&1 or J[x]==J[x^(1<<j)]:continue
            term=[Q(1)]
            for k in range(6):
                if k!=j:term=times(term,[Q(0),ts[k]] if x>>k&1 else [Q(1),-ts[k]])
            q=plus(q,term)
        qs.append(q)
    C=entseries(masses)
    for j in range(6):
        h=entseries([vs[j],plus([Q(1)],mul(vs[j],Q(-1)))])
        for i in range(3):
            for k in range(min(i,len(qs[j])-1)+1):C[i]=aadd(C[i],h[i-k],-qs[j][k])
    return C,qs,masses

def coreseries(s,A):
    if not A:return [zero() for _ in range(3)]
    r=Q(1<<s);a=len(A);b=a*r/3
    L=[sum((-1)**((x&z).bit_count()) for x in A) for z in range(4)]
    E=sum((x^(1<<j)) in A for x in A for j in range(2))//2
    H1=coeff(loge=4*b);H2=coeff(loge=-12*b*b)
    for l in L:
        c=4*l*l*r*r/9
        if c:H1=aadd(H1,coeff(-3*c/(4*r),c,-3*c/(2*r)))
    c=4*a*a*r*r/9;H2=aadd(H2,coeff(c,c,2*c))
    I1=({3:8*a*r/3,2:r*(-8*a*s-16*E)/3},-8*a*r/3,Q(0))
    return [zero(),aadd(I1,H1,Q(-1)),ascale(H2,Q(-1))]

def series(name):
    s,A=SHAPES[name];t=Q(len(A)*(1<<s),3)
    C,q,masses=polynomials(t);cs=coreseries(s,A);bs=coreseries(*SHAPES['r'])
    U=[zero() for _ in range(3)];S=[ascale(x,Q(-1)) for x in C]
    for j in range(6):
        h=cs if j==0 else bs
        for i in range(3):
            for k in range(min(i,len(q[j])-1)+1):
                term=ascale(h[i-k],q[j][k]);S[i]=aadd(S[i],term)
                if j==0:U[i]=aadd(U[i],term)
    return {'C':C,'S':S,'U':U,'M':[aadd(x,y,Q(-1)) for x,y in zip(S,U)],'q':q,'masses':masses}

def sd(parent,a,b,key='S'):
    return [aadd(aadd(ascale(x,Q(1,2)),y,Q(1,2)),z,Q(-1)) for x,y,z in zip(a[key],b[key],parent[key])]

def analytic():
    z={k:series(k) for k in SHAPES};es=[sd(z['r'],z['a'],z['z']),sd(z['a'],z['b'],z['c']),sd(z['b'],z['d'],z['z'])]
    out={'profiles':{},'excesses':[]}
    for name in z:
        out['profiles'][name]={}
        for key in ['S','U','M','C']:
            out['profiles'][name][key]=[{'logs':ar.forms(x[0]),'logp':str(x[1]),'loge':str(x[2])} for x in z[name][key]]
    for e in es:
        ar.ck(e[0]==zero() and e[1]==zero() and e[2][1]==0)
        out['excesses'].append(boundtriple(e[2]))
    # Selected capacity is O(p²); other-owner remainder is O(p), with positive leading term.
    vals={}
    for label,name,key in [('Ub','b','U'),('Uc','c','U'),('Ud','d','U')]:
        v=z[name][key];ar.ck(v[0]==zero() and v[1]==zero() and v[2][1]==0)
        v=boundtriple(v[2]);vals[label]=(Q(v['lower']),Q(v['upper']));out[label]=v
    E=[(Q(x['lower']),Q(x['upper'])) for x in out['excesses']]
    T2=iadd(imul(E[0],icon(2)),E[1]);B2=mean(vals['Ub'],vals['Uc'])
    D=imul(idiv(T2,B2),vals['Ub']);T=iadd(D,E[2]);B=imul(vals['Ud'],icon(Q(1,2)))
    out['limits']={k:saveiv(v) for k,v in {'T2_over_B2':idiv(T2,B2),'D_over_p2':D,'T_over_p2':T,'B_over_p2':B,'selected_unused_over_p2':isub(B,T),'T_over_B':idiv(T,B)}.items()}
    lead=z['d']['M'][1];ar.ck(lead==z['z']['M'][1]);leading=boundtriple(lead)
    ar.ck(Q(leading['lower'])>0);ar.ck(idiv(T,B)[0]>Q(1,2) and idiv(T,B)[1]<Q(13,25))
    ar.ck(es[0][2]==zero() and es[2][2]==zero())
    out['other_M_over_p_limit']=leading
    # Fixed prefix extension: each additional zero-valued padding restriction doubles U's p² coefficient.
    out['fixed_depth_checks']=[]
    for s in [2,3,4,5,6]:
        # A=(0,1) is a codimension-(n-s-1) affine subcube indicator with one dummy bit.
        name='pair_s'+str(s);SHAPES[name]=(s,(0,1));v=series(name)
        ar.ck(v['U'][2]==ascale(z['b']['U'][2],Q(1<<(s-2))))
        ar.ck(v['M'][1]==lead)
        if s>2:
            prev=series('b' if s==3 else 'pair_s'+str(s-1))
            e=sd(prev,v,z['z']);ar.ck(all(x==zero() for x in e))
        out['fixed_depth_checks'].append({'fixed_coordinates':s,'U2_multiplier':1<<(s-2)})
    out['mass_polynomials']={k:[list(map(str,p)) for p in z[k]['masses']] for k in z}
    # Independent exact rational evaluation of every polynomial law at fixed densities.
    for p in [Q(3,64),Q(3,128),Q(1,1000)]:
        for name in z:
            s,A=SHAPES[name]
            t=Q(len(A)*(1<<s),3);C,qs,ms=outer([t*p]+[p]*5)
            ar.ck([ev(x,p) for x in z[name]['masses']]==ms)
            ar.ck([ev(x,p) for x in z[name]['q']]==qs)
    (ROOT/'out/ANALYTIC.json').write_text(json.dumps(out,indent=2)+'\n',encoding='utf-8')
    return out

if __name__=='__main__':
    start=time.perf_counter()
    if '--analytic' in sys.argv:
        out=analytic();out['checks']=ar.checks;out['seconds']=time.perf_counter()-start
        (ROOT/'out/ANALYTIC.json').write_text(json.dumps(out,indent=2)+'\n',encoding='utf-8')
        print(json.dumps({'limits':{k:v['display'] for k,v in out['limits'].items()},'checks':out['checks'],'seconds':out['seconds']}))
    else:
        spec=json.loads((ROOT/'out/FROZEN_SPEC.json').read_text(encoding='utf-8'))
        domain=spec['pilot_domain'] if '--pilot' in sys.argv else spec['parameter_domain']
        rows=[finite(n) for n in domain]
        out={'domain':domain,'checks':ar.checks,'seconds':time.perf_counter()-start,
             'summary':[{k:r[k] for k in ['n','transfer_needed','transfer_feasible','selected_child_S_positive','selected_child_M_negative','fraction']} for r in rows]}
        (ROOT/'out'/('PILOT.json' if '--pilot' in sys.argv else 'FINITE.json')).write_text(json.dumps(out,indent=2)+'\n',encoding='utf-8');print(json.dumps({'domain':domain,'checks':out['checks'],'seconds':out['seconds'],'summary':[{k:(v['display'] if k=='fraction' else v) for k,v in x.items()} for x in out['summary']]}))
    assert time.perf_counter()-start<55
