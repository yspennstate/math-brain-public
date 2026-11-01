from pathlib import Path
source=Path(__file__).with_name('check_embeddings.py').read_text(encoding='utf-8')
# Load only the versioned exact arithmetic and cube utility definitions;
# do not run the completed embedding census a second time.
exec(compile(source.split('activation_cases=tensor_cases=surgery_cases=0')[0],str(Path(__file__).with_name('check_embeddings.py')),'exec'))

cases=0
record=None
for n in range(4):
    for word in range(1<<(1<<n)):
        g=[-1 if word>>x&1 else 1 for x in range(1<<n)]
        K=[-1]*len(g)+g
        T=K+[1]*len(K)
        mu=Q(sum(g),len(g)); N=n+2
        neg={x for x,v in enumerate(T) if v==-1}
        seen={min(neg)}; frontier=list(seen)
        while frontier:
            x=frontier.pop()
            for i in range(N):
                y=x^(1<<i)
                if y in neg and y not in seen:
                    seen.add(y);frontier.append(y)
        check(seen==neg)
        check(all(x>>(N-1)==0 for x in neg))
        check(Q(len(neg),len(T))==(3-mu)/8)
        check(Q(1,4)<=Q(len(neg),len(T))<=Q(1,2))
        check(influences(T)==[i/4 for i in influences(g)]+[(1+mu)/4,(3-mu)/4])
        check(sum(influences(T))==sum(influences(g))/4+1)
        check(entropy(K)==activation_H([-x for x in g],1))
        check(entropy(T)==activation_H(K,1))
        E=add(entropy(T),scale(entropy(g),Q(-1,4)))
        lo,hi=bits_enclosure(E)
        check(lo>=0 or not E)
        check(hi<=Q(9,2))
        tags=3<<n
        check(block_drop(T,tags)==add(entropy(T),scale(entropy(g),Q(-1,4))))
        C=Q(2)
        check(add(block_drop(T,tags),{2:-C},scale(deficit(T,C),-1))==scale(deficit(g,C),Q(-1,4)))
        check(restrict(T,tags,1<<n)==g)
        if n==3 and word==1:
            dl,du=bits_enclosure(deficit(T,C))
            sl,su=bits_enclosure(scale(deficit(g,C),Q(1,4)))
            # The finite wrapper need not violate C=2; its failed test still
            # displays the hard-core deficit, and tensor limits admit C.
            check(sl>Q(1,10))
            record={'core':'three-bit point defect','C':'2','wrapper_deficit_bits_interval':[str(dl),str(du)],'criticality_shortfall_bits_interval':[str(sl),str(su)],'shortfall_strictly_greater_than':'1/10','wrapper_violation_asserted':False}
        cases+=1
result={'status':'PASS','helper_version':'A055-check-connected-tags-v1','tagged_seeds':cases,'assertions':COUNT,'helper_elapsed_seconds':time.perf_counter()-START,'fixed_witness':record}
(ROOT/'out/TAG_CHECK.json').write_text(json.dumps(result,indent=2)+'\n',encoding='utf-8')
print(json.dumps({k:v for k,v in result.items() if k!='fixed_witness'},indent=2))
