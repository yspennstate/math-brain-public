from pathlib import Path
import json,time,sys
from fractions import Fraction as Q
import check_profiles as C
start=time.monotonic(); PR=[2,3,5,7]; SCALE=256; DY=1<<60
pilot='--pilot' in sys.argv
logs=[]
for p in PR:
    lo,hi=C.interval({p:Q(1)})
    logs.append((lo.numerator*DY//lo.denominator,-((-hi.numerator*DY)//hi.denominator)))
def ivec(m):
    assert set(m).issubset(PR)
    a=[m.get(p,Q(0))*SCALE for p in PR]
    assert all(q.denominator==1 for q in a)
    return tuple(int(q) for q in a)
def ibounds(v):
    return (sum(c*(l if c>=0 else u) for c,(l,u) in zip(v,logs)),sum(c*(u if c>=0 else l) for c,(l,u) in zip(v,logs)))
tables={}; truth={}; children={}; influences={}; total=roots=eq=0; positive=0; worst=None; maxratio=-1; failures=[]
for n in range(0,3 if pilot else 4):
    N=1<<n; funcs=C.allfunc(n); truth[n]=funcs
    raw=[tuple(int(z*N) for z in C.fw(f)) for f in funcs]
    possible=sorted(set(z for a in raw for z in a))
    km={}
    for a in possible:
      for b in possible:
        aa,bb=Q(a,N),Q(b,N)
        km[a,b]=ivec(C.add(C.mul(Q(1,2),C.add(C.g(aa+bb),C.g(aa-bb))),C.mul(-1,C.add(C.g(aa),C.g(bb)))))
    table=[]
    for v in raw:
      row=[]
      for w in raw:
        row.append(tuple(sum(km[v[t],w[t]][j] for t in range(1,N)) for j in range(4)))
      table.append(row)
    tables[n]=table
    if n==0: continue
    roots+=len(funcs)**2
    index={f:j for j,f in enumerate(truth[n-1])}
    ch=[[[index[tuple(C.restrict(f,i,b))] for b in [0,1]] for i in range(n)] for f in funcs]
    infl=[[C.inf(f,i) for i in range(n)] for f in funcs]
    for vi,v in enumerate(funcs):
      for wi,w in enumerate(funcs):
        for i in range(n):
            total+=1; a,b=ch[vi][i],ch[wi][i]
            delta=tuple(2*table[vi][wi][j]-tables[n-1][a[0]][b[0]][j]-tables[n-1][a[1]][b[1]][j] for j in range(4))
            D=infl[vi][i]+infl[wi][i]
            payment=4*D*(2*SCALE); assert payment.denominator==1
            margin=tuple((int(payment) if j==0 else 0)-delta[j] for j in range(4))
            lo,hi=ibounds(margin)
            if not any(margin): eq+=1
            elif lo<0:
                failures.append({'n':n,'V_id':vi,'W_id':wi,'i':i,'margin_log_vector':margin,'certified_negative':hi<0,'bounds_scaled_by_512_and_2pow60':[str(lo),str(hi)]})
            dl,du=ibounds(delta)
            if dl>0: positive+=1
            # Diagnostic ranking only; the sign certificate above uses integers.
            if D:
                ratio=float(Q(dl,DY*2*SCALE)/D)
                if ratio>maxratio:
                    maxratio=ratio; worst={'n':n,'V_id':vi,'W_id':wi,'i':i,'DeltaXi_over_e_log_vector_scale512':delta,'D':str(D)}
            if total%512==0 and time.monotonic()-start>55: raise TimeoutError('frozen 55s cap')
    if time.monotonic()-start>55: raise TimeoutError('frozen 55s cap')
out={'status':'PASS' if not failures else 'COUNTEREXAMPLES_OR_UNRESOLVED','roots':roots,'queries':total,'equalities':eq,'strict_positive_collision_rows':positive,'failures':failures[:10],'failure_count':len(failures),'worst_diagnostic_ratio_lower':maxratio,'worst':worst,'log2_intervals_scaled_by_2pow60':logs,'elapsed_seconds':time.monotonic()-start,'all_dimensional_status':'OPEN'}
name='collision_pilot.json' if pilot else 'collision_full.json'
(Path(__file__).resolve().parents[1]/'out'/name).write_text(json.dumps(out,indent=2)+'\n',encoding='utf-8')
print(json.dumps(out))
