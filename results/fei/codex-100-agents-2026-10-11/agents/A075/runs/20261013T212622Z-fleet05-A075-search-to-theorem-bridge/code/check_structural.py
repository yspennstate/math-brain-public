from pathlib import Path
import itertools, json
engine_path=Path(__file__).with_name('check_matching.py')
exec(compile(engine_path.read_text(encoding='utf-8').split('\nfinite=[];',1)[0],str(engine_path),'exec'),globals())
graph_cases=path_cases=0
for n in range(6):
    edges=list(itertools.combinations(range(n),2))
    for mask in range(1<<len(edges)):
        selected=[e for j,e in enumerate(edges) if mask>>j&1]
        A={0}|{1<<i for i in range(n)}|{(1<<i)|(1<<j) for i,j in selected}
        t=[-1 if x in A else 1 for x in range(1<<n)]
        W,ds,bs,hs=certify_table(t); a=len(A)
        degrees=[sum(i in e for e in selected) for i in range(n)]
        for i in range(n):
            delta=a-2*(1+degrees[i])
            ck(ds[i]==Q(2*delta,1<<n)); ck(W[1<<i]==-2*delta)
        if n>4:
            i=min(range(n),key=lambda j:degrees[j]); ck(ds[i]>0)
            delta=a-2*(1+degrees[i]); ck(Q(delta,a)>=1-Q(4,n))
            lo,hi=enclose(scale(bs[i],1/ds[i]))
            U=2+Q(8,n-4)+Q(n*n+n+2,1<<n)*(2*n+Q(3,2))
            ck(hi<U)
        graph_cases+=1
for n in range(10):
    for m in range(n+1):
        A={(1<<j)-1 for j in range(m+1)}; a=m+1; N=1<<n
        t=[-1 if x in A else 1 for x in range(N)]
        W,ds,bs,hs=certify_table(t)
        for i in range(n):
            b=m-1 if i<m else a
            c=2*(i+1)-m-1 if i<m else a
            ck(ds[i]==Q(2*b,N)); ck(W[1<<i]==-2*c)
        if n>m:
            i=m; lo,hi=enclose(scale(bs[i],1/ds[i]))
            upper=2+Q(2*a,N)*(2*n+Q(3,2)); ck(hi<upper)
        elif m>=2:
            i=(m-1)//2; ck(abs(2*(i+1)-m-1)<=1)
            lo,hi=enclose(scale(bs[i],1/ds[i]))
            upper=2+Q(4,n-1)+Q(2,(n-1)*N)*(2*n+Q(3,2)); ck(hi<upper)
        path_cases+=1
ck(graph_cases==1100); ck(path_cases==55)
graph_cut=2+Q(8,12)+Q(274,65536)*Q(67,2)
dummy_path_cut=2+Q(22,1024)*Q(43,2)
full_path_cut=2+Q(4,9)+Q(2,9*1024)*Q(43,2)
ck(graph_cut<Q(368,125)); ck(dummy_path_cut<Q(368,125)); ck(full_path_cut<Q(368,125))
ck(2*16**3-Q(5,2)*16**2-Q(15,2)*16-8>0)
ck(4*10**2-10-8>0)
out={'graph_tables':graph_cases,'path_tables':path_cases,'exact_assertions':checks,'graph_all_n_ge_16_E_upper_at_cutoff':str(graph_cut),'padded_path_all_n_ge_10_E_upper_at_cutoff':str(dummy_path_cut),'full_path_all_n_ge_10_E_upper_at_cutoff':str(full_path_cut),'runtime_seconds':time.perf_counter()-start,'uniform_graph_root_bound':'2+8/(n-4)+(n^2+n+2)(2n+3/2)/2^n for n>4','uniform_path_root_bound':'max{2+2(n+1)(2n+3/2)/2^n, 2+4/(n-1)+2(2n+3/2)/((n-1)2^n)} for n>=2, nonconstant and m>=2 for full path','first_unsupported_line':'These root estimates do not establish general descendant payment or imply a universal Boolean bound.'}
ck(time.perf_counter()-start<60)
(ROOT/'out'/'STRUCTURAL_VALIDATION.json').write_text(json.dumps(out,indent=2)+'\n',encoding='utf-8')
print(json.dumps(out,indent=2))
