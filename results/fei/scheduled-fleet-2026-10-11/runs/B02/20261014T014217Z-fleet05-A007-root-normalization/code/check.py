import argparse, itertools as it, json, math, time
from pathlib import Path
from fractions import Fraction as Q

ROOT=Path(__file__).resolve().parents[1]
PREV=ROOT.parent/'20261013T220854Z-fleet05-A007-root-normalization'/'code'/'check_lift.py'
# Own previously independently implemented helpers, no author code; no bytecode writes.
ck={'__name__':'a007_own_helpers','__file__':str(PREV)}
exec(compile(PREV.read_text(encoding='utf-8'),str(PREV),'exec'),ck)
check=ck['check']; actual_key=ck['actual_key']; struct_z=ck['struct_z']
stats={'boolean_tables':0,'activated_tables':0,'data_assignments':0,'base_events':0,
       'core_maps':0,'distributed_events':0,'old_star_events':0,'complete_operator_minors':0,
       'strict_support_improvement_cases':0,'strict_positive_spectral_improvement_cases':0,
       'equal_width_root_collapse_checks':0,'occupation_sum_checks':0}
strict_witness=None

def inverse_components(owned,roots,groups):
    parent={v:u for (u,j),vs in groups.items() for v in vs}
    components={}
    for v in owned:
        a=v
        while a not in roots: a=parent[a]
        components[v]=a
    return components

def complete_operator_review(owned,tab,roots,events):
    poly,coords=ck['minor'](owned,tab,roots)
    direct=Q(0)
    for G,key in events:
        denominator=math.prod((sum(len(vs) for (u,j),vs in G.items() if u==l)+1)*
            (sum(len(vs) for (u,j),vs in G.items() if u==l)+2)*
            math.comb(len(js)+sum(len(vs) for (u,j),vs in G.items() if u==l)-1,
                     sum(len(vs) for (u,j),vs in G.items() if u==l)) for l,js in owned.items())
        direct+=Q(1,denominator)
    derived=Q(0); M=0
    for expo,coef in poly.items():
        h=dict(zip(coords,expo)); cu={l:sum(h.get((l,j),0) for j in js) for l,js in owned.items()}
        factorial=math.prod(math.factorial(k) for k in expo)
        denominator=math.prod((cu[l]+1)*(cu[l]+2)*math.comb(len(js)+cu[l]-1,cu[l]) for l,js in owned.items())
        derived+=Q(coef*factorial,denominator); M+=coef*factorial
    g=len(owned); a=sum(map(len,owned.values())); e=g-len(roots)
    check(direct==derived)
    check(Q(M,2**(a+g+e)*3**e)<=derived<=Q(M,2**g))
    # Independent beta/simplex moment evaluation via integer factorial integrals.
    expectation=Q(0)
    for expo,coef in poly.items():
        h=dict(zip(coords,expo)); moment=Q(1)
        for l,js in owned.items():
            c=sum(h[l,j] for j in js); s=len(js)
            moment*=Q(2,(c+1)*(c+2))*math.factorial(c)*Q(math.factorial(s-1)*math.prod(math.factorial(h[l,j]) for j in js),math.factorial(s+c-1))
        expectation+=coef*moment
    check(derived==expectation/Q(2**g))
    stats['complete_operator_minors']+=1

def count_added(own,roots,components,alpha,oldgroups,tab):
    c=len(roots); nonroot=[a for a in roots if a!=own]
    parents=[tuple(l for l in set(alpha.values()) if components[l]!=child) for child in nonroot]
    counts=[]
    for parvals in it.product(*parents):
        parcomp=dict(zip(nonroot,(components[l] for l in parvals)))
        valid=True
        for a in nonroot:
            seen=set(); b=a
            while b!=own:
                if b in seen: valid=False; break
                seen.add(b); b=parcomp[b]
            if not valid: break
        if not valid: continue
        choices=[tuple(j for j,l in alpha.items() if l==parent) for parent in parvals]
        for attachments in it.product(*choices):
            added={}
            for child,l,j in zip(nonroot,parvals,attachments): added.setdefault((l,j),[]).append(child)
            ks=tuple(sorted(added))
            for perms in it.product(*(tuple(it.permutations(added[k])) for k in ks)):
                groups=dict(oldgroups); groups.update(dict(zip(ks,perms)))
                counts.append(groups)
    return counts

def verify_table(tab,n,rvals):
    global strict_witness
    stats['boolean_tables']+=1
    covered=tuple(sorted(set().union(*(set(R) for R in tab))))
    read=max(sum(j in R for R in tab) for j in covered)
    lam=[Q(1,read)]*len(tab); beta=min(Q(1),1/sum(lam)); pi=[Q(1,2**len(R)) for R in tab]
    D=math.prod(1+l*t for l,t in zip(lam,pi))-1
    values=ck['truth'](tab,n); spectrum=ck['fwht'](values); Ig=ck['influence'](values,n)
    b=Q(sum(v==1 for v in values),2**n)
    for r in rvals:
        p=Q(1,2**r); activated=tuple(tuple(range(r))+tuple(j+r for j in R) for R in tab)
        F=ck['truth'](activated,n+r); fhat=ck['fwht'](F)
        Dp=math.prod(1+p*beta*l*t for l,t in zip(lam,pi))-1
        check(Dp/(p*D)<=beta)
        check(ck['influence'](F,n+r)==p*Ig+2*r*p*b)
        for Tmask in range(1,2**n):
            for Umask in range(2**r): check(Q(fhat[Umask+(Tmask<<r)],2**(n+r))==p*Q(spectrum[Tmask],2**n))
        stats['activated_tables']+=1
        for T in ck['subsets'](n):
            if not set(T)<=set(covered): continue
            choices=[tuple(l for l,R in enumerate(tab) if j in R) for j in T]
            base=[]
            for ownerids in it.product(*choices):
                owned={}
                for j,l in zip(T,ownerids): owned.setdefault(l,[]).append(j)
                owned={l:tuple(js) for l,js in owned.items()}
                roots,edges=ck['roots_and_graph'](owned,tab)
                for R in roots:
                    events,_=ck['base_events'](owned,tab,R,edges)
                    complete_operator_review(owned,tab,R,events)
                    for G,key in events: base.append((owned,R,G,key))
                    stats['base_events']+=len(events)
                stats['data_assignments']+=1
            for U in ck['subsets'](r):
                seen=set(); oldset=set(); formal={}; predicted={}; oldformal={}
                for owned,R,G,keyold in base:
                    V=tuple(sorted(owned)); c=len(R); components=inverse_components(owned,R,G)
                    oldgroups={(l,j+r):vs for (l,j),vs in G.items()}
                    shifted={l:tuple(j+r for j in js) for l,js in owned.items()}
                    label=math.prod(lam[l] for l in V)
                    oldrootrarity=math.prod(pi[l] for l in R)
                    oldweight=label*oldrootrarity
                    oldz=struct_z(owned,tab,T)
                    occupation_direct={}
                    for coreowners in it.product(V,repeat=len(U)):
                        alpha=dict(zip(U,coreowners)); stats['core_maps']+=1
                        own=dict(shifted)
                        for l in V: own[l]=tuple(sorted(own[l]+tuple(j for j in U if alpha[j]==l)))
                        selected=tuple(sorted(U+tuple(j+r for j in T)))
                        zr=struct_z(own,activated,selected)
                        corez=struct_z({0:U},activated,U)
                        qratio=ck['congestion_z'](own,activated,selected)/ck['congestion_z'](owned,tab,T)
                        ck['addformal'](occupation_direct,qratio,Q(1))
                        check(zr/oldz>=corez*Q(len(U),r)**len(T)*qratio)
                        counts=[]; ua={a:sum(components[l]==a for l in alpha.values()) for a in R}
                        for root in R:
                            formula=1 if c==1 else ua[root]*math.prod(range(len(U)+1,len(U)+c-1))
                            events=count_added(root,R,components,alpha,oldgroups,activated)
                            check(len(events)==formula); counts.append(formula)
                            ck['addformal'](predicted,zr,p*beta**len(V)*oldweight*Q(pi[root],oldrootrarity)*formula)
                            for groups in events:
                                keynew=actual_key(own,(root,),groups)
                                check(keynew not in seen); seen.add(keynew)
                                rec={(l,j-r):vs for (l,j),vs in groups.items() if j>=r}
                                rr=tuple(sorted(set(own)-{v for vs in rec.values() for v in vs}))
                                check(rr==tuple(sorted(R)))
                                check(actual_key(owned,rr,rec)==keyold)
                                check({j:l for l,js in own.items() for j in js if j<r}==alpha)
                                rootchoices,newedges=ck['roots_and_graph'](own,activated)
                                check((root,) in rootchoices)
                                check(all((l,v) in newedges for (l,j),vs in groups.items() for v in vs))
                                ck['addformal'](formal,zr,p*beta**len(V)*label*pi[root])
                                stats['distributed_events']+=1
                        check(sum(counts)==math.prod(range(len(U),len(U)+c-1)))
                        if len(set(pi))==1:
                            check(sum(count*pi[root]/oldrootrarity for count,root in zip(counts,R))==Q(math.prod(range(len(U),len(U)+c-1)),pi[0]**(c-1)))
                            stats['equal_width_root_collapse_checks']+=1
                        # Enumerate previous root-only star independently to check inclusion.
                        for root in R:
                            if any(l!=root for l in alpha.values()): continue
                            kids=tuple(a for a in R if a!=root)
                            for js in it.product(U,repeat=c-1):
                                added={}
                                for child,j in zip(kids,js): added.setdefault((root,j),[]).append(child)
                                ks=tuple(sorted(added))
                                for perms in it.product(*(tuple(it.permutations(added[k])) for k in ks)):
                                    gg=dict(oldgroups); gg.update(dict(zip(ks,perms)))
                                    oldkey=actual_key(own,(root,),gg)
                                    check(oldkey in seen); check(oldkey not in oldset); oldset.add(oldkey)
                                    ck['addformal'](oldformal,zr,p*beta**len(V)*label*pi[root])
                    occupation_predicted={}
                    for occup in it.product(range(len(U)+1),repeat=len(V)):
                        if sum(occup)!=len(U): continue
                        baseq=ck['congestion_z'](owned,tab,T)
                        qnew=math.prod(Q(len(owned[l])+k,len(set(tab[l])&set(T))+len(U))**(len(owned[l])+k) for l,k in zip(V,occup))
                        multinomial=Q(math.factorial(len(U)),math.prod(math.factorial(k) for k in occup))
                        ck['addformal'](occupation_predicted,qnew/baseq,multinomial)
                    check(occupation_direct==occupation_predicted)
                    stats['occupation_sum_checks']+=1
                check(formal==predicted)
                check(oldset<=seen)
                stats['old_star_events']+=len(oldset)
                stats['strict_support_improvement_cases']+=len(seen)>len(oldset)
                Tmask=sum(1<<j for j in T); Umask=sum(1<<j for j in U)
                if len(seen)>len(oldset) and fhat[Umask+(Tmask<<r)]!=0:
                    stats['strict_positive_spectral_improvement_cases']+=1
                    if strict_witness is None and read>1:
                        strict_witness={'table':[list(R) for R in tab],'n':n,'r':r,'T':T,'U':U,
                          'old_events':len(oldset),'distributed_events':len(seen),
                          'F_fourier_coefficient':str(Q(fhat[Umask+(Tmask<<r)],2**(n+r))),
                          'D':str(D),'D_activated':str(Dp),'beta':str(beta),
                          'old_surrogate_mass_terms':[{"rational_base_z":str(z),"coefficient":str(k),"power":"6/5"} for z,k in sorted(oldformal.items())],
                          'distributed_surrogate_mass_terms':[{"rational_base_z":str(z),"coefficient":str(k),"power":"6/5"} for z,k in sorted(formal.items())],
                          'sign_certificate':'old actual trace set is a proper subset; every added trace has positive exact generator probability and positive surrogate weight'}

if __name__=='__main__':
    ap=argparse.ArgumentParser(); ap.add_argument('--pilot',action='store_true'); args=ap.parse_args()
    begin=time.perf_counter()
    for n in ([2] if args.pilot else [2,3]):
        for tab in ck['tables'](n): verify_table(tab,n,[1] if args.pilot else [1,2,3])
    if not args.pilot: verify_table(((0,1),(1,2),(0,2,3)),4,[1,2])
    result={'status':'PASS','helper_version':'A007-component-root-lift-v1','stats':stats,
            'assertions':ck['COUNTS']['assertions'],'elapsed_seconds':time.perf_counter()-begin,
            'arithmetic':'integer spectra, exact rational counts/probabilities, formal rational structural bases z^gamma',
            'first_unproved_line':'Psi_dist<=K I(F), uniformly over arbitrary overlapping signed prime tables'}
    result['strict_positive_mass_witness']=strict_witness
    out=ROOT/'out'; out.mkdir(exist_ok=True)
    (out/('PILOT.json' if args.pilot else 'EXACT_CHECK.json')).write_text(json.dumps(result,indent=2)+'\n',encoding='utf-8')
    print(json.dumps(result))
