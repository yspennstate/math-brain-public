from pathlib import Path
code=Path(__file__).with_name('check.py')
exec(compile(code.read_text(encoding='utf-8').split('direct=0;generic_atoms=0')[0],str(code),'exec'))

atoms=0
for r,m in ([(3,1)] if PILOT else [(3,1),(3,2),(4,1),(4,2)]):
    n=r+2*m
    edges=list(combinations(range(r),2))+[(r+2*j,r+2*j+1) for j in range(m)]
    weights={e:(F(1,r-1) if e[0]<r else F(1)) for e in edges}
    ck(all(sum((w for e,w in weights.items() if j in e),F(0))==1 for j in range(n)))
    total=F(0)
    for mask in range(1<<n):
        A={j for j in range(n) if mask>>j&1};k=sum(j<r for j in A)
        one=sum(len(A&{r+2*j,r+2*j+1})==1 for j in range(m))
        two=sum({r+2*j,r+2*j+1}<=A for j in range(m))
        value=raw(A,n,weights)
        ck(value==clique_mass(r,k,F(1,r-1))*F(1,32)**one*F(1,48)**two)
        total+=value;atoms+=1
    totalK=sum(comb(r,k)*clique_mass(r,k,F(1,r-1)) for k in range(r+1))
    ck(total==totalK*F(13,12)**m)

rows=[]
for r in ([12] if PILOT else [12,16,24,32]):
    m=r*r;lam=F(1,r-1);s=F(r+1,2**r)*F(3,4)**m;v=4*s*(1-s)
    I=s*(F(4*m,3)+F(2*r*(r-1),r+1))
    pc=[F(comb(r,k)*(r+1-2*k)**2,2**r*(r+1)) for k in range(r+1)]
    totalK=sum(comb(r,k)*clique_mass(r,k,lam) for k in range(r+1))
    ck(totalK**4<=2**r)
    for k in range(r+1):
        a,b=lg(totalK/clique_mass(r,k,lam));ck(b<=F(21*r,4))
    ccore=add(*(logcost(1/clique_mass(r,k,lam),4*s*pc[k]) for k in range(r+1) if pc[k]))
    edgecost=add(logcost(32,F(2*m,3)*s),logcost(48,F(m,3)*s))
    zlocal=totalK*F(13,12)**m-1
    clocal=add(entropy_binary(v),ccore,edgecost,logcost(zlocal,v))
    ck(clocal[1]<=F(259,32)*I)
    zglobal=totalK*(1+lam/12)**m-1
    cglobal=add(entropy_binary(v),ccore,edgecost,logcost(1/lam,m*s),logcost(zglobal,v))
    ck(cglobal[0]>=F(2,3)*lg(r-1)[1]*I)
    HK=add(*(logcost(F(comb(r,k))/x,x) for k,x in enumerate(pc) if x))
    he=add(logcost(4/F(3),F(3,4)),logcost(12,F(1,4)))
    hs=entropy_binary(s)
    entropy=add(entropy_binary(v),(4*s*HK[0],4*s*HK[1]),(4*s*m*he[0],4*s*m*he[1]),(-4*s*hs[1],-4*s*hs[0]))
    ck(entropy[0]>=0);ck(entropy[1]<6*I)
    rows.append({'r':r,'m':m,'global_CE_over_I':[str(z/I) for z in cglobal],'local_CE_over_I':[str(z/I) for z in clocal],'true_H_over_I':[str(z/I) for z in entropy],'normalizers_retained':True})

out={'helper_version':'A014-local-scale-v1','mode':'pilot' if PILOT else 'main','large_profiles':len(rows),'independent_mixed_weight_raw_atoms':atoms,'assertions':CHECKS,'elapsed_seconds':time.monotonic()-START,'rows':rows}
(RUN/'out'/('local_pilot.json' if PILOT else 'local_check.json')).write_text(json.dumps(out,indent=2)+'\n',encoding='utf-8')
print(json.dumps({k:v for k,v in out.items() if k!='rows'}))
