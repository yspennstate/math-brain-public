"""Independent event enumeration: no author checker imports; exact arithmetic only."""
import argparse, itertools as it, json, math, time
from fractions import Fraction as Q
from pathlib import Path

START=time.perf_counter()
COUNTS={"assertions":0,"tables":0,"activated_tables":0,"assignments":0,
        "root_minors":0,"base_events":0,"lift_events":0,"core_only_events":0}

def check(v):
    COUNTS['assertions']+=1
    assert v
    if time.perf_counter()-START>60:
        raise RuntimeError('frozen 60 second limit')

def subsets(n):
    return [tuple(j for j in range(n) if m>>j&1) for m in range(1,1<<n)]

def tables(n):
    supports=subsets(n)
    out=[]
    for mask in range(1,1<<len(supports)):
        tab=tuple(supports[i] for i in range(len(supports)) if mask>>i&1)
        if all(not(set(a)<=set(b)) for a,b in it.permutations(tab,2)):
            out.append(tab)
    return out

def fwht(values):
    a=list(values); h=1
    while h<len(a):
        for i in range(0,len(a),2*h):
            for j in range(i,i+h):
                a[j],a[j+h]=a[j]+a[j+h],a[j]-a[j+h]
        h*=2
    # Truth bit 1 means physical sign +1; raw Walsh uses (-1)^bit.
    return [(-1)**i.bit_count()*v for i,v in enumerate(a)]

def truth(tab,n):
    return [1 if any(all(x>>j&1 for j in R) for R in tab) else -1 for x in range(1<<n)]

def influence(values,n):
    return Q(sum(values[x]!=values[x^(1<<j)] for x in range(1<<n) for j in range(n)),1<<n)

def roots_and_graph(owned,tab):
    V=tuple(sorted(owned))
    edges={(u,v) for u in V for v in V if u!=v and set(owned[u])&set(tab[v])}
    reach={(v,v) for v in V}|edges
    for k in V:
        reach|={(a,b) for a in V for b in V if (a,k) in reach and (k,b) in reach}
    comps=[]; todo=set(V)
    while todo:
        a=min(todo); C={b for b in todo if (a,b) in reach and (b,a) in reach}
        comps.append(tuple(sorted(C))); todo-=C
    sources=[C for C in comps if not any(v in C and u not in C for u,v in edges)]
    return list(it.product(*sources)),edges

def actual_key(owned,roots,groups):
    queue=list(sorted(roots)); trace=[]
    while queue:
        a=queue.pop(0)
        row=tuple((j,tuple(groups[a,j])) for u,j in sorted(groups) if u==a)
        trace.append((a,tuple(owned[a]),row))
        for j,children in row:
            queue.extend(children)
    check(len(trace)==len(owned) and len({row[0] for row in trace})==len(owned))
    return tuple(sorted(roots)),tuple(trace)

def base_events(owned,tab,roots,edges):
    V=tuple(sorted(owned)); nonroot=tuple(v for v in V if v not in roots)
    parent_lists=[tuple(u for u in V if (u,v) in edges) for v in nonroot]
    events=[]; canonical=[]
    for parents in it.product(*parent_lists):
        par=dict(zip(nonroot,parents)); good=True
        for v in nonroot:
            seen=set(); cursor=v
            while cursor not in roots:
                if cursor in seen:
                    good=False; break
                seen.add(cursor); cursor=par[cursor]
            if not good: break
        if not good: continue
        attaches=[tuple(sorted(set(owned[par[v]])&set(tab[v]))) for v in nonroot]
        for js in it.product(*attaches):
            groups={}
            for v,j in zip(nonroot,js):
                groups.setdefault((par[v],j),[]).append(v)
            canonical.append(groups)
            keys=tuple(sorted(groups))
            for orders in it.product(*(tuple(it.permutations(groups[k])) for k in keys)):
                G=dict(zip(keys,orders)); key=actual_key(owned,roots,G)
                events.append((G,key))
    check(len({key for G,key in events})==len(events))
    return events,canonical

def padd(a,b):
    d=dict(a)
    for m,c in b.items():
        d[m]=d.get(m,0)+c
        if not d[m]: del d[m]
    return d

def pscale(a,c):
    return {m:x*c for m,x in a.items() if x*c}

def pmul(a,b):
    d={}
    for m,c in a.items():
        for k,e in b.items():
            x=tuple(u+v for u,v in zip(m,k)); d[x]=d.get(x,0)+c*e
    return {m:c for m,c in d.items() if c}

def detpoly(mat,numvars):
    n=len(mat); out={}; unit={(0,)*numvars:1}
    for perm in it.permutations(range(n)):
        sign=(-1)**sum(perm[i]>perm[j] for i in range(n) for j in range(i+1,n))
        prod=unit
        for i,j in enumerate(perm): prod=pmul(prod,mat[i][j])
        out=padd(out,pscale(prod,sign))
    return out

def minor(owned,tab,roots):
    V=tuple(sorted(owned)); nonroot=tuple(v for v in V if v not in roots)
    coords=tuple((u,j) for u in V for j in owned[u]); m=len(coords)
    index={a:i for i,a in enumerate(coords)}
    weights={}
    for u in V:
        for v in V:
            if u==v: continue
            w={}
            for j in set(owned[u])&set(tab[v]):
                expo=[0]*m; expo[index[u,j]]=1; w[tuple(expo)]=1
            weights[u,v]=w
    mat=[]
    for v in nonroot:
        row=[]
        for u in nonroot:
            if u==v:
                p={}
                for a in V:
                    if a!=v: p=padd(p,weights[a,v])
            else: p=pscale(weights[u,v],-1)
            row.append(p)
        mat.append(row)
    return detpoly(mat,m),coords

def struct_z(owned,tab,selected):
    # 2^(-C_tau)=z_tau^gamma, with EXACT rational z_tau.
    z=Q(1)
    for gate,coords in owned.items():
        order=tab[gate]; k=len(set(order)&set(selected)); s=len(coords)
        z*=Q(s,k)**s
        for j in coords:
            rank=order.index(j)+1
            previous=len(set(order[:rank-1])&set(selected))
            z*=Q(previous+1,rank)
    return z

def addformal(d,z,c):
    d[z]=d.get(z,Q(0))+c

def congestion_z(owned,tab,selected):
    return math.prod(Q(len(js),len(set(tab[l])&set(selected)))**len(js) for l,js in owned.items())

def run(n,r_values):
    tabs=tables(n); check(len(tabs)=={2:4,3:18}[n])
    for tab in tabs:
        COUNTS['tables']+=1
        covered=tuple(sorted(set().union(*(set(a) for a in tab))))
        read=max(sum(j in R for R in tab) for j in covered)
        lam=[Q(1,read)]*len(tab); beta=min(Q(1),1/sum(lam))
        pi=[Q(1,2**len(R)) for R in tab]
        a=sum(l*p for l,p in zip(lam,pi))
        D=math.prod(1+l*p for l,p in zip(lam,pi))-1
        g=truth(tab,n); gh=fwht(g); b=Q(sum(x==1 for x in g),1<<n)
        Ig=influence(g,n)
        check(Q(sum(x*x for x in gh),1<<(2*n))==1)
        check(Q(sum(i.bit_count()*x*x for i,x in enumerate(gh)),1<<(2*n))==Ig)
        rdata={}
        for r in r_values:
            p=Q(1,1<<r); newtab=tuple(tuple(range(r))+tuple(j+r for j in R) for R in tab)
            check(sum(Q(math.comb(r,u),2**r*(u+1)) for u in range(r+1))==Q(2-p,r+1))
            for j in range(1,r+1):
                check(sum(Q(math.comb(j-1,k),2**(j-1)*(k+1)) for k in range(j))==Q(2*(1-Q(1,2**j)),j))
            fp=truth(newtab,n+r); fh=fwht(fp)
            Dp=math.prod(1+p*beta*l*t for l,t in zip(lam,pi))-1
            check(beta*a/D<=Dp/(p*D)<=beta)
            check(influence(fp,n+r)==p*Ig+2*r*p*b)
            check(1-Q(fh[0],1<<(n+r))**2==4*p*b*(1-p*b))
            for T in range(1,1<<n):
                for U in range(1<<r):
                    check(Q(fh[U|(T<<r)],1<<(n+r))==p*Q(gh[T],1<<n))
            for U in range(1,1<<r):
                check(Q(fh[U],1<<(n+r))==2*p*b)
                coords=tuple(j for j in range(r) if U>>j&1)
                mass={}; z=struct_z({0:coords},newtab,coords)
                for l in range(len(tab)):
                    own={l:coords}; check(struct_z(own,newtab,coords)==z)
                    actual_key(own,(l,),{})
                    addformal(mass,z,p*beta*lam[l]*pi[l])
                    COUNTS['core_only_events']+=1
                check(mass=={z:p*beta*a})
            COUNTS['activated_tables']+=1
            rdata[r]=(p,newtab)
        for T in subsets(n):
            if not set(T)<=set(covered): continue
            for owners in it.product(*(tuple(l for l,R in enumerate(tab) if j in R) for j in T)):
                owned={}
                for j,l in zip(T,owners): owned.setdefault(l,[]).append(j)
                owned={l:tuple(js) for l,js in owned.items()}
                V=tuple(sorted(owned)); rootsets,edges=roots_and_graph(owned,tab)
                c=len(rootsets[0]); e=len(V)-c
                zbase=struct_z(owned,tab,T)
                labelled=math.prod(lam[l] for l in V)
                cases=[]
                for roots in rootsets:
                    events,canonical=base_events(owned,tab,roots,edges)
                    polynomial,coords=minor(owned,tab,roots)
                    from_events={}
                    for groups in canonical:
                        exp=tuple(len(groups.get(k,())) for k in coords)
                        from_events[exp]=from_events.get(exp,0)+1
                    check(polynomial==from_events)
                    moment=sum(coef*math.prod(math.factorial(h) for h in expo) for expo,coef in polynomial.items())
                    can=sum(polynomial.values())
                    Ds=[sum(v!=u and j in tab[v] for v in V) for u,j in coords]
                    up=sum(coef*math.prod((Q(Di+1,2) if Di else Q(1))**h for Di,h in zip(Ds,expo)) for expo,coef in polynomial.items())
                    check(moment==len(events))
                    check(can<=moment<=min(math.factorial(e)*can,up))
                    COUNTS['root_minors']+=1; COUNTS['base_events']+=len(events)
                    cases.append((roots,events))
                COUNTS['assignments']+=1
                for r,(p,newtab) in rdata.items():
                    # Empty-core complete event bijection and exact symbolic cost shift.
                    emptyown={l:tuple(j+r for j in js) for l,js in owned.items()}
                    newT=tuple(j+r for j in T)
                    zempty=struct_z(emptyown,newtab,newT)
                    shift=math.prod(Q(tab[l].index(j)+1,tab[l].index(j)+1+r) for l in V for j in owned[l])
                    check(zempty==zbase*shift)
                    check(shift>=Q(1,r+1)**len(T))
                    check(p**(c-1)>=p**len(T))
                    newroots,newedges=roots_and_graph(emptyown,newtab)
                    check(newroots==rootsets and newedges==edges)
                    for roots,events in cases:
                        projected=[({(l,j+r):children for (l,j),children in groups.items()},key) for groups,key in events]
                        enumerated,_=base_events(emptyown,newtab,roots,newedges)
                        check({actual_key(emptyown,roots,G) for G,key in projected}=={key for G,key in enumerated})
                        oldmass=labelled*math.prod(pi[l] for l in roots)*len(events)
                        newmass=math.prod(beta*lam[l] for l in V)*math.prod(p*pi[l] for l in roots)*len(events)
                        check(newmass==oldmass*p*(p**(c-1))*beta**len(V))
                    for U in subsets(r):
                        lifted=set(); direct={}; formula={}
                        m=math.factorial(c-1)*math.comb(len(U)+c-2,c-1)
                        for roots,events in cases:
                            for owner in roots:
                                own=dict(emptyown); own[owner]=tuple(sorted(U+own[owner]))
                                selected=tuple(sorted(U+newT))
                                zr=struct_z(own,newtab,selected)
                                corez=struct_z({0:U},newtab,U)
                                qratio=congestion_z(own,newtab,selected)/congestion_z(owned,tab,T)
                                check(zr/zbase>=corez*Q(len(U),r)**len(T)*qratio)
                                rootoptions,edgesnew=roots_and_graph(own,newtab)
                                check((owner,) in rootoptions and len(rootoptions[0])==1)
                                addformal(formula,zr,p*beta**len(V)*labelled*pi[owner]*m*len(events))
                                children=tuple(v for v in roots if v!=owner)
                                for G,keybase in events:
                                    local_count=0
                                    oldgroups={(l,j+r):vs for (l,j),vs in G.items()}
                                    for attachment in it.product(U,repeat=c-1):
                                        added={}
                                        for child,j in zip(children,attachment): added.setdefault((owner,j),[]).append(child)
                                        keys=tuple(sorted(added))
                                        for orders in it.product(*(tuple(it.permutations(added[k])) for k in keys)):
                                            groups=dict(oldgroups); groups.update(dict(zip(keys,orders)))
                                            keynew=actual_key(own,(owner,),groups)
                                            check(keynew not in lifted); lifted.add(keynew)
                                            check(all((u,v) in edgesnew for (u,j),vs in groups.items() for v in vs))
                                            recovered={(l,j-r):vs for (l,j),vs in groups.items() if j>=r}
                                            recovered_roots=tuple(sorted(set(own)-{v for vs in recovered.values() for v in vs}))
                                            check(recovered_roots==tuple(sorted(roots)))
                                            check(actual_key(owned,recovered_roots,recovered)==keybase)
                                            addformal(direct,zr,p*math.prod(beta*lam[l] for l in V)*pi[owner])
                                            local_count+=1; COUNTS['lift_events']+=1
                                    check(local_count==m)
                        check(direct==formula)
                        check(len(lifted)==sum(len(events)*len(roots)*m for roots,events in cases))

if __name__=='__main__':
    ap=argparse.ArgumentParser(); ap.add_argument('--pilot',action='store_true'); ap.add_argument('--out',required=True)
    args=ap.parse_args()
    for n in ([2] if args.pilot else [2,3]): run(n, [1] if args.pilot else [1,2,3])
    result={"helper_version":"A007-root-lift-independent-v1","status":"PASS","counts":COUNTS,
            "elapsed_seconds":time.perf_counter()-START,"arithmetic":"integers, Fraction, polynomial coefficients, formal rational bases z^gamma",
            "domain":{"n":[2] if args.pilot else [2,3],"r":[1] if args.pilot else [1,2,3]},
            "unproved":"dimension-independent influence payment of the signed nonempty-core correction"}
    Path(args.out).write_text(json.dumps(result,indent=2)+'\n',encoding='utf-8')
    print(json.dumps(result))
