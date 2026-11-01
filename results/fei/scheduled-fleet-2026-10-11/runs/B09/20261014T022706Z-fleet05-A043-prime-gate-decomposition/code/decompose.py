from pathlib import Path
import itertools,json,time
ROOT=Path(__file__).resolve().parents[1]
start=time.perf_counter();checks=0;pair_count=0
def ck(x):
    global checks
    checks+=1
    assert x
def event(t,x):return all(t[j]==-1 or t[j]==((x>>j)&1) for j in range(len(t)))
class_counts={str(n):{} for n in range(1,5)}
truth_masks={n:set() for n in range(1,5)}
for n in range(1,5):
    terms=list(itertools.product((-1,0,1),repeat=n))
    for a,b in itertools.product(terms,repeat=2):
        J=[j for j in range(n) if a[j]!=-1 and b[j]==a[j]]
        R=[j for j in range(n) if a[j]!=-1 and b[j]!=-1 and a[j]!=b[j]]
        U=[j for j in range(n) if a[j]!=-1 and b[j]==-1]
        V=[j for j in range(n) if b[j]!=-1 and a[j]==-1]
        ck(len(set(J+R+U+V))==len(J+R+U+V))
        pair_count+=1
        key=('corner_OR' if not R else 'mux' if len(R)==1 else f'antipodal_r{len(R)}_g{int(bool(U))+int(bool(V))}')
        class_counts[str(n)][key]=class_counts[str(n)].get(key,0)+1
        truth_mask=0
        for x in range(1<<n):
            common=all(((x>>j)&1)==a[j] for j in J)
            aa=all(((x>>j)&1)==a[j] for j in U)
            bb=all(((x>>j)&1)==b[j] for j in V)
            first=all(((x>>j)&1)==a[j] for j in R)
            second=all(((x>>j)&1)==b[j] for j in R)
            actual=event(a,x) or event(b,x)
            ck(actual==(common and ((first and aa) or (second and bb))))
            truth_mask|=int(actual)<<x
        truth_masks[n].add(truth_mask)
roots=[]
for r in range(2,5):
    for g in range(3):
        n=r+g;maskdata=(1<<r)-1
        table=[]
        for x in range(1<<n):
            ag=True if g<2 else bool(x>>r&1)
            bg=True if g==0 else bool(x>>(r+g-1)&1)
            table.append(1 if (x&maskdata==maskdata and ag) or (x&maskdata==0 and bg) else -1)
        ck(all(any(table[x]!=table[x^(1<<j)] for x in range(1<<n)) for j in range(n)))
        counts=[]
        for size in range(2,n):
            for B in itertools.combinations(range(n),size):
                C=[j for j in range(n) if j not in B]
                rows={tuple(table[sum(((a>>j)&1)<<B[j] for j in range(size))+
                                  sum(((z>>j)&1)<<C[j] for j in range(len(C)))]
                            for z in range(1<<len(C))) for a in range(1<<size)}
                ck(len(rows)>2);counts.append(len(rows))
        roots.append({'r':r,'guards':g,'arity':n,'positive_assignments':[x for x,t in enumerate(table) if t==1],
                      'proper_blocks':len(counts),'minimum_distinct_rows':min(counts) if counts else None,'prime':True})
ck(pair_count==7380)
census=[]
for n,masks in truth_masks.items():
    essential=[];primes=[]
    for mask in sorted(masks):
        table=[(mask>>x)&1 for x in range(1<<n)]
        if not all(any(table[x]!=table[x^(1<<j)] for x in range(1<<n)) for j in range(n)):continue
        essential.append(mask)
        prime=n>=2
        for size in range(2,n):
            for B in itertools.combinations(range(n),size):
                C=[j for j in range(n) if j not in B]
                rows={tuple(table[sum(((a>>j)&1)<<B[j] for j in range(size))+
                                  sum(((z>>j)&1)<<C[j] for j in range(len(C)))]
                            for z in range(1<<len(C))) for a in range(1<<size)}
                if len(rows)==2:prime=False
        if prime:primes.append(mask)
    allmask=(1<<(1<<n))-1
    prime_plus_neg=set(primes)|{p^allmask for p in primes}
    census.append({'n':n,'distinct_two_term_tables':len(masks),'essential_tables':len(essential),
                   'prime_tables':len(primes),'primes':primes,'prime_tables_with_output_negation':len(prime_plus_neg)})
ck(census[-1]['prime_tables']==168)
ck(census[-1]['prime_tables_with_output_negation']==336)
out={'helper':'A043-two-term-disjoint-factor-v1','term_pairs':pair_count,'prime_skeletons':roots,
     'class_counts':class_counts,'census':census,'assertions':checks,'all_passed':True,'runtime_seconds':time.perf_counter()-start}
(ROOT/'out/decomposition_checks.json').write_text(json.dumps(out,indent=2)+'\n',encoding='utf-8')
print(json.dumps({k:v for k,v in out.items() if k not in ('prime_skeletons','class_counts','census')}))
print('census:',[{k:v for k,v in c.items() if k!='primes'} for c in census])
