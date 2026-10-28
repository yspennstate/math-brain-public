"""Full finite stopping hull, compared with actual inherited source-pair credit.
The profile engine is attributed A084 source, copied unchanged and pinned.
"""
from profile_engine import *
import profile_engine as engine
from itertools import combinations,product

def short(t):
    if t==(1,):return 'P'
    m=(len(t)-1).bit_length()
    return ('A' if sum(x==-1 for x in t)==1 else 'L')+str(m)

def job(physical,pilot=False):
    start=time.perf_counter();dag=graph();ids=tuple(sorted(dag,key=lambda t:(len(t),t)));axes=tuple(j-2 for j in physical)
    for z in range(16):
        for a,b in [(0,2),(1,3)]:
            zz=z^((1<<a)|(1<<b)) if (z>>a&1)!=(z>>b&1) else z;ck(K4[z]==K4[zz])
    states={};records=[]
    @lru_cache(None)
    def solve(key):
        ts=[G]*4
        for a,t in zip(axes,key):ts[a]=t
        p=full(tuple(ts));R=pos(neg(p['S']));winner='stop';actions=[]
        for side,t in enumerate(key):
            # All physical coordinates are represented, including equivalent choices.
            for i,kids in dag[t]:
                args=[]
                for c in kids:
                    arg=list(key);arg[side]=c;args.append(tuple(arg))
                zs=[solve(arg) for arg in args];r=mean([z['R'] for z in zs])
                physical_d=p['q'][axes[side]]*core(t)['ds'][i]
                ck(p['I']-sum(z['I'] for z in zs)/2==physical_d)
                if cmp(r,R)>0:R=r;winner=[side,i]
                actions.append((side,i,tuple(args),r))
        node={'S':p['S'],'I':p['I'],'R':R,'winner':winner,'actions':actions};states[key]=node
        records.append({'types':[short(t) for t in key],'S':pack(p['S']),'I':str(p['I']),'R':pack(R),'winner':winner})
        # Crash-safe bounded chunks, without retaining a multi-megabyte temporary string.
        if len(records)%128==0:
            save('CERT_'+''.join(map(str,physical))+'_'+str((len(records)-1)//128).zfill(2)+'.json',records[-128:])
        if len(records)%32==0:ck(time.perf_counter()-start<(55 if pilot else 300))
        return node
    root=solve((G,)*len(axes));A=neg(root['S']);ck(cmp(A,{})>0)
    if len(records)%128:save('CERT_'+''.join(map(str,physical))+'_'+str(len(records)//128).zfill(2)+'.json',records[-(len(records)%128):])
    margins=[minus(A,r) for _,_,_,r in root['actions']]
    root_equal=not minus(root['R'],A)
    result={'physical_cores':physical,'states':len(states),'root_credit':pack(A),'root_hull':pack(root['R']),'root_equal_exactly':root_equal,'root_margins':[list(map(str,ev(m))) for m in margins],'prefixes':[]}
    save('PARTIAL_'+''.join(map(str,physical))+'.json',result)
    if not pilot:
        # The source allocator uses its EXACT pair hull. Minima are propagated over
        # actual paths, not inferred from a fresh optimal triple allocation.
        for admitted in combinations(range(3),2):
            def jointkey(pairkey):
                key=[G]*3
                for side,t in zip(admitted,pairkey):key[side]=t
                return tuple(key)
            @lru_cache(None)
            def pairsolve(key):
                node=states[jointkey(key)];R=pos(neg(node['S']))
                for side,t in enumerate(key):
                    for i,kids in dag[t]:
                        zs=[]
                        for c in kids:
                            arg=list(key);arg[side]=c;zs.append(pairsolve(tuple(arg)))
                        r=mean(zs)
                        if cmp(r,R)>0:R=r
                return R
            pairroot=(G,G);pairA=pairsolve(pairroot);ck(pairA==A)
            incoming={pairroot:A};paths={pairroot:[]}
            for key in sorted(product(ids,repeat=2),key=lambda k:sum(len(t) for t in k),reverse=True):
                if key not in incoming:continue
                credit=incoming[key]
                for side,t in enumerate(key):
                    for i,kids in dag[t]:
                        args=[]
                        for c in kids:
                            arg=list(key);arg[side]=c;args.append(tuple(arg))
                        reserve=minus(credit,mean([pairsolve(arg) for arg in args]));ck(cmp(reserve,{})>=0)
                        for b,arg in enumerate(args):
                            childcredit=add(pairsolve(arg),reserve)
                            if arg not in incoming or cmp(childcredit,incoming[arg])<0:
                                incoming[arg]=childcredit;paths[arg]=paths[key]+[[physical[admitted[side]],i,b]]
            ck(len(incoming)==144)
            worst={};witness=None;cuts=[]
            for key in product(ids,repeat=2):
                need=states[jointkey(key)]['R'];credit=incoming[key];gap=minus(need,credit)
                cut={'types':[short(t) for t in key],'credit':pack(credit),'triple_requirement':pack(need),'gap':pack(gap),'path_reduced_coordinates':paths[key],'reach':str(F(1,1<<len(paths[key])))}
                cuts.append(cut)
                if cmp(gap,worst)>0:worst=gap;witness=cut
            pr={'admitted_pair':[physical[i] for i in admitted],'cuts':144,'extra_initial_credit_threshold':pack(worst),'threshold_interval':list(map(str,ev(worst))),'witness':witness}
            result['prefixes'].append(pr)
            save('CUTS_'+''.join(map(str,physical))+'_'+''.join(map(str,pr['admitted_pair']))+'.json',cuts)
            save('PARTIAL_'+''.join(map(str,physical))+'.json',result)
    result.update({'helper_checks':engine.CHECKS,'seconds':time.perf_counter()-start,'full_fei':'OPEN','external_review':'PENDING','root_policy_scope':'only declared finite cores; no all-dimensional theorem'})
    ck(result['seconds']<(55 if pilot else 300))
    save(('PILOT' if pilot else 'TRIPLE_'+''.join(map(str,physical)))+'.json',result)
    print(json.dumps({k:v for k,v in result.items() if k not in ['root_credit','root_hull','root_margins']}),flush=True)

if __name__=='__main__':
    try:
        if '--pilot' in sys.argv:job([2,4],True)
        else:job(list(map(int,sys.argv[1:4])))
    except Exception as exc:
        save('FIRST_FAILURE.json',{'error_type':type(exc).__name__,'error':str(exc),'argv':sys.argv,'checks':engine.CHECKS,'not_a_certificate':True})
        raise
