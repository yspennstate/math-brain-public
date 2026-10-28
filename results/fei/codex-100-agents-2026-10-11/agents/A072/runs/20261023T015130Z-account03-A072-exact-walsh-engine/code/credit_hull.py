"""Exact zero-new-flow stopping-credit hull in a prescribed other core."""
from component_audit import add,times,minus,mean,entp,evalp,pack,corep
from continue_spent import *
from itertools import product

COUNT=0
def test(b):
    global COUNT
    assert b
    COUNT+=1
def negative(iv):return -iv[1],-iv[0]
def positive(iv):return max(0,iv[0]),max(0,iv[1])
def overlap(a,b):test(a[0]<=b[1] and b[0]<=a[1])

@lru_cache(None)
def canonical(t):
    n=(len(t)-1).bit_length()
    for i in range(n):
        if all(t[x]==t[x^(1<<i)] for x in range(len(t))):
            reduced=child(t,i,0)
            test(child(t,i,1)==reduced)
            return canonical(reduced)
    return t

@lru_cache(None)
def independent(ts):
    # Integer inner characters/inverses/edges are checked before any entropy.
    for t in ts:corep(t)
    mus=[F(sum(t),len(t)) for t in ts];vs=[1-m*m for m in mus]
    active=[j for j,v in enumerate(vs) if v]
    n=len(active);N=1<<n;truth=[]
    for x in range(N):
        mask=0
        for j in range(6):
            bit=(x>>active.index(j)&1) if j in active else int(mus[j]==-1)
            mask|=bit<<j
        truth.append(-H[mask^1])
    moments=list(map(F,truth))
    for k,j in enumerate(active):
        m=mus[j];pp=(1+m)/2;pm=(1-m)/2
        for x in range(N):
            if x>>k&1:continue
            u,v=moments[x],moments[x|1<<k]
            moments[x]=pp*u+pm*v
            moments[x|1<<k]=pp*(1-m)*u+pm*(-1-m)*v
    mass=[F(0)]*64;raw=[]
    for T,z in enumerate(moments):
        var=F(1);mask=0
        for k,j in enumerate(active):
            if T>>k&1:var*=vs[j];mask|=1<<j
        test(var>0);raw.append(z/var);mass[mask]=z*z/var
    test(sum(mass)==1)
    for x,y in enumerate(truth):
        val=F(0)
        for T,c in enumerate(raw):
            v=c
            for k,j in enumerate(active):
                if T>>k&1:v*=1-2*(x>>k&1)-mus[j]
            val+=v
        test(val==y)
    q={}
    for k,j in enumerate(active):
        pivotal=F(0)
        for x in range(N):
            if x>>k&1 or truth[x]==truth[x|1<<k]:continue
            prob=F(1)
            for l,i in enumerate(active):
                if l!=k:prob*=(1-mus[i])/2 if x>>l&1 else (1+mus[i])/2
            pivotal+=prob
        q[j]=pivotal
        test(sum(mass[T] for T in range(64) if T>>j&1)==vs[j]*pivotal)
    hf=entp(mass);inf=F(0)
    for j in active:
        hg,_,ds=corep(ts[j])
        hf=add(hf,times(minus(hg,entp([vs[j],1-vs[j]])),q[j]))
        inf+=q[j]*sum(ds)
    return dict(H=hf,I=inf,S=add({None:4*inf},times(hf,F(-1))),mass=mass,q=q)

@lru_cache(None)
def checked(ts):
    independent_result=independent(ts)
    p=full(ts);test(p['I']==independent_result['I'])
    test(p['op']['masses']==independent_result['mass'])
    for j,q in independent_result['q'].items():test(q==p['op']['q'][j])
    overlap(evalp(independent_result['H']),p['H']);overlap(evalp(independent_result['S']),p['S'])
    test(p['I']>0)  # Retained complete functions never become constant here.
    return p,independent_result

def choose(candidates):
    # Exact profile equality handles ties; every unequal comparison is rigorous.
    winner=candidates[0]
    for c in candidates[1:]:
        if c[1]==winner[1]:continue
        a,b=evalp(c[1]),evalp(winner[1])
        if a[0]>b[1]:winner=c
        elif b[0]>a[1]:pass
        else:raise ArithmeticError('unresolved Bellman comparison; no tolerance or float verdict')
    return winner

def raw_restriction(pattern):
    free=[i for i,b in enumerate(pattern) if b==-1]
    fixed=sum((b==1)<<i for i,b in enumerate(pattern))
    return tuple(G[fixed|sum(((x>>k)&1)<<i for k,i in enumerate(free))] for x in range(1<<len(free)))

def canonical_axes(t,axes):
    axes=list(axes)
    while True:
        drop=next((i for i in range(len(axes)) if all(t[x]==t[x^(1<<i)] for x in range(len(t)))),None)
        if drop is None:return t,axes
        test(child(t,drop,0)==child(t,drop,1));t=child(t,drop,0);axes.pop(drop)

def source_review():
    source=ROOT.parents[3]/'agents/A071/runs/20261023T003633Z-account03-A071-search-space-design'
    # ROOT=.../A072/runs/run; parents[3] is the campaign root.
    saved=json.loads((source/'out/SEVEN_PROFILES.json').read_text(encoding='utf-8'))
    profiles={}
    for m in range(6):
        t=tuple(-1 if x==0 else 1 for x in range(1<<m))
        p,ind=checked(((-1,),t,G,G,G,G));profiles[m]=p
        z=saved['profiles'][str(m)];test(F(z['I'])==p['I']);overlap(z['S'],evalp(ind['S']))
    p,ind=checked(((-1,),(1,),G,G,G,G));test(F(saved['stop']['I'])==p['I']);overlap(saved['stop']['S'],evalp(ind['S']))
    chains=json.loads((source/'out/ADAPTIVE.json').read_text(encoding='utf-8'))['chains']
    receipts=[];early_account=None
    for chain in chains:
        A=negative(profiles[chain['initial']]['S']);D=(0,0);labels=[];leaves=[];reach=F(1)
        for z in chain['rows']:
            m=z['m'];ss=[profiles[m-1]['S'],p['S']]
            N=avg([positive(negative(s)) for s in ss]);P=avg([positive(s) for s in ss])
            d=profiles[m]['op']['q'][1]*F(1,1<<(m-1))
            test(profiles[m]['I']-(profiles[m-1]['I']+p['I'])/2==d)
            e=sub(sub(profiles[m]['H'],avg([profiles[m-1]['H'],p['H']])),const(4*d));T=plus(D,e)
            test(T[0]>0 and sub(A,N)[0]>0)
            if P[0]>0:
                kernels=[div(positive(s),P) for s in ss]
                credits=[plus(positive(negative(s)),mul(sub(A,N),k)) for s,k in zip(ss,kernels)]
            else:
                test(all(s[1]<0 for s in ss));test(N[0]>0)
                kernels=[div(positive(negative(s)),N) for s in ss]
                credits=[mul(A,k) for k in kernels]
            booked=[mul(T,k) for k in kernels]
            overlap(avg(credits),A);overlap(avg(booked),T)
            outgoing=[[mul(L,k) for k in kernels] for L in labels+[e]]
            for L,pair in zip(labels+[e],outgoing):overlap(avg(pair),L)
            for s,a,dv in zip(ss,credits,booked):overlap(sub(plus(s,a),dv),(0,0))
            for i in range(2):overlap(credits[i],z['credits'][i]);overlap(booked[i],z['booked'][i])
            if chain['initial']==4 and m==4:
                test(booked[1][0]>0)
                early_account=dict(credit=credits[1],debit=booked[1],labels=[pair[1] for pair in outgoing],root_reach='1/128',source_original_coordinate=2)
            leaves.append(scale(credits[1],reach/2));reach/=2
            A,D=credits[0],booked[0];labels=[pair[0] for pair in outgoing]
            if m==1:
                test(booked[1]==(0,0));test(all(pair[1]==[0,0] for pair in z['label_children']));overlap(credits[1],negative(p['S']))
                receipts.append(dict(initial=chain['initial'],stop_debit=booked[1],stop_credit=credits[1],stop_reach=str(F(1,64)*reach)))
        leaves.append(scale(A,reach));overlap(plus((0,0),sum_intervals(leaves)),negative(profiles[chain['initial']]['S']))
    return dict(profiles=7,adaptive_rows=sum(len(c['rows']) for c in chains),source=str(source),last_stopped_accounts=receipts,early_stopped_account=early_account)

def sum_intervals(xs):
    a=(0,0)
    for x in xs:a=plus(a,x)
    return a

def main():
    start=time.perf_counter()
    # Literal table automorphisms of J with its first two arguments fixed.
    for x in range(64):
        if x&3:continue
        for a,b in [(2,4),(3,5)]:
            y=x
            if (x>>a&1)!=(x>>b&1):y^=(1<<a)|(1<<b)
            test(H[x]==H[y])
    review=source_review();orbits=[2] if '--pilot' in sys.argv else [2,3]
    results=[];coverage=[];all_query_rows=[];finance=[]
    for j in orbits:
        states={};query_rows=[]
        @lru_cache(None)
        def solve(t):
            test(t==canonical(t));ts=[(-1,),(1,),G,G,G,G];ts[j]=t
            p,ind=checked(tuple(ts));s=ind['S'];si=evalp(s)
            stop={} if si[0]>0 else times(s,F(-1))
            test(si[0]>0 or si[1]<0 or not s)
            candidates=[('stop',stop)];actions=[]
            for i in range((len(t)-1).bit_length()):
                kids=[canonical(child(t,i,b)) for b in range(2)]
                sols=[solve(c) for c in kids];r=mean([c['R'] for c in sols])
                d=p['op']['q'][j]*corep(t)[2][i]
                test(p['I']-sum(c['I'] for c in sols)/2==d)
                e=minus(mean([c['S'] for c in sols]),s)
                actions.append(dict(coordinate=i,children=kids,R=r,e=e,physical_influence=str(d)))
                candidates.append((str(i),r))
            winner=choose(candidates);R=winner[1]
            # At each state, arbitrary actual A>=R is supported by redistributing
            # inherited credit as R_child + (A-mean R_child), no new donor flow.
            for a in actions:
                rs=[solve(c)['R'] for c in a['children']];diff=minus(R,a['R'])
                test(not diff or evalp(diff)[0]>0)
                credits=[add(r,diff) for r in rs]
                debits=[add(solve(c)['S'],credit) for c,credit in zip(a['children'],credits)]
                for c,credit,debit in zip(a['children'],credits,debits):
                    test(not credit or evalp(credit)[0]>=0)
                    test(not debit or evalp(debit)[0]>=0)
                test(mean(credits)==R)
                test(mean(debits)==add(mean([solve(c)['S'] for c in a['children']]),R))
                query_rows.append(dict(core=j,state=list(t),coordinate=a['coordinate'],physical_influence=a['physical_influence'],required_credit=evalp(R),
                    child_credits=[evalp(c) for c in credits],child_debits=[evalp(d) for d in debits],new_flow=[0,0],e=evalp(a['e'])))
            data=dict(S=s,I=p['I'],R=R,winner=winner[0],actions=actions,truth=t)
            states[t]=data
            return data
        root=solve(G);A=times(root['S'],F(-1));test(evalp(A)[0]>0)
        gap=minus(root['R'],A)
        if not gap:verdict='SAME_INHERITED_CREDIT_SUFFICES_FOR_ALL_POLICIES'
        elif evalp(gap)[0]>0:verdict='POSITIVE_EXTRA_INITIAL_CREDIT_REQUIRED_FOR_SOME_POLICY'
        else:raise ArithmeticError('unresolved root credit comparison')
        # Mechanically cover all actual partial restrictions, including dummies.
        rawstates=rawrows=0
        for pattern in product([-1,0,1],repeat=6):
            raw=raw_restriction(pattern);t=canonical(raw);test(t in states);rawstates+=1
            for i in range((len(raw)-1).bit_length()):
                kids=[canonical(child(raw,i,b)) for b in range(2)];rawrows+=1
                test(kids==[t,t] or any(kids==a['children'] for a in states[t]['actions']))
        test(len(states)==12 and rawstates==729 and rawrows==1458)
        # An attaining stopping policy certifies the lower bound, not just a pass.
        leaves=[]
        def policy(t,path,weight):
            p=states[t]
            if p['winner']=='stop':leaves.append((path,weight,p));return
            a=next(a for a in p['actions'] if str(a['coordinate'])==p['winner'])
            for b,c in enumerate(a['children']):policy(c,path+[(a['coordinate'],b)],weight/2)
        policy(G,[],F(1));test(sum(w for _,w,_ in leaves)==1)
        optimum={}
        for path,w,p in leaves:
            neg=times(p['S'],F(-1)) if evalp(p['S'])[1]<0 else {}
            optimum=add(optimum,times(neg,w))
        test(optimum==root['R'])
        # Two actual adaptive policies carry the already supplied credit and
        # every distinct signed debit label, while all outside donors stay fixed.
        if verdict=='SAME_INHERITED_CREDIT_SUFFICES_FOR_ALL_POLICIES':
            for order in ['first','last']:
                financial_leaves=[];financial_rows=[]
                def carry(t,a,labels,path,reach,axes):
                    node=states[t];D=add(node['S'],a)
                    test(not D or evalp(D)[0]>=0)
                    if not node['actions']:
                        financial_leaves.append(dict(path=path,reach=reach,credit=a,debit=D,S=node['S'],labels=labels));return
                    action=node['actions'][0 if order=='first' else -1]
                    children=[states[c] for c in action['children']]
                    spare=minus(a,action['R']);test(not spare or evalp(spare)[0]>0)
                    ac=[add(c['R'],spare) for c in children]
                    dc=[add(c['S'],x) for c,x in zip(children,ac)]
                    T=mean(dc);ep=action['e']
                    test(T==add(D,ep));test(mean(ac)==a)
                    if not T:
                        test(all(not d for d in dc));kernel=[(Q,Q),(Q,Q)]
                    else:
                        test(evalp(T)[0]>0)
                        kernel=[div(evalp(d),evalp(T)) for d in dc]
                    old=labels+[evalp(ep)]
                    outgoing=[[mul(L,k) for L in old] for k in kernel]
                    for k,L in enumerate(old):overlap(avg([o[k] for o in outgoing]),L)
                    for d,ls in zip(dc,outgoing):overlap(sum_intervals(ls),evalp(d))
                    original=axes[action['coordinate']]
                    financial_rows.append(dict(path=path,reach=str(reach),original_coordinate=original,credit=evalp(a),old_booked=evalp(D),e=evalp(ep),T=evalp(T),child_credits=[evalp(x) for x in ac],child_debits=[evalp(d) for d in dc],new_flow=[0,0]))
                    for b,c in enumerate(action['children']):
                        raw=child(t,action['coordinate'],b);remaining=[x for k,x in enumerate(axes) if k!=action['coordinate']]
                        ct,ca=canonical_axes(raw,remaining);test(ct==c)
                        carry(c,ac[b],outgoing[b],path+[(original,b)],reach/2,ca)
                carry(G,A,[],[],F(1),list(range(6)))
                test(sum(v['reach'] for v in financial_leaves)==1)
                expected_credit={};expected_debit={};expected_S={}
                for leaf in financial_leaves:
                    expected_credit=add(expected_credit,times(leaf['credit'],leaf['reach']))
                    expected_debit=add(expected_debit,times(leaf['debit'],leaf['reach']))
                    expected_S=add(expected_S,times(leaf['S'],leaf['reach']))
                test(expected_credit==A);test(expected_debit==add(expected_S,A))
                finance.append(dict(core=j,order=order,rows=financial_rows,
                    terminal_credit_mean=evalp(expected_credit),initial_credit=evalp(A),
                    terminals=[dict(path=v['path'],reach=str(v['reach']),credit=evalp(v['credit']),debit=evalp(v['debit']),S=evalp(v['S']),booked_labels=v['labels']) for v in financial_leaves],
                    source_stop_reaches=['1/1024','1/2048'],outside_donor='Original A089 outgoing A, booked donor debit, all source stopped terminals and parked2tau unchanged'))
            # Also test an ACTUAL early stopped source leaf with nonzero old
            # booked label, rather than substituting the last zero-debit leaf.
            early=review['early_stopped_account'];early_leaves=[];early_rows=[]
            overlap(plus(evalp(root['S']),early['credit']),early['debit'])
            overlap(sum_intervals(early['labels']),early['debit'])
            def carry_early(t,a,labels,path,reach,axes):
                node=states[t];D=plus(evalp(node['S']),a);test(D[0]>0)
                if not node['actions']:
                    early_leaves.append(dict(path=path,reach=str(reach),credit=a,debit=D,S=evalp(node['S']),booked_labels=labels));return
                action=node['actions'][-1];children=[states[c] for c in action['children']]
                spare=sub(a,evalp(action['R']));test(spare[0]>0)
                ac=[plus(evalp(c['R']),spare) for c in children]
                dc=[plus(evalp(c['S']),x) for c,x in zip(children,ac)]
                test(all(d[0]>0 for d in dc));T=avg(dc);test(T[0]>0)
                overlap(T,plus(D,evalp(action['e'])));overlap(avg(ac),a)
                kernel=[div(d,T) for d in dc];outgoing=[[mul(L,k) for L in labels+[evalp(action['e'])]] for k in kernel]
                for k,L in enumerate(labels+[evalp(action['e'])]):overlap(avg([ls[k] for ls in outgoing]),L)
                for d,ls in zip(dc,outgoing):overlap(sum_intervals(ls),d)
                original=axes[action['coordinate']]
                early_rows.append(dict(path=path,reach=str(reach),original_coordinate=original,credit=a,old_booked=D,e=evalp(action['e']),T=T,child_credits=ac,child_debits=dc,new_flow=[0,0]))
                for b,c in enumerate(action['children']):
                    raw=child(t,action['coordinate'],b);remaining=[x for k,x in enumerate(axes) if k!=action['coordinate']]
                    ct,ca=canonical_axes(raw,remaining);test(ct==c)
                    carry_early(c,ac[b],outgoing[b],path+[(original,b)],reach/2,ca)
            carry_early(G,early['credit'],early['labels'],[],F(1),list(range(6)))
            test(sum(F(v['reach']) for v in early_leaves)==1)
            weighted=sum_intervals([scale(v['credit'],F(v['reach'])) for v in early_leaves]);overlap(weighted,early['credit'])
            finance.append(dict(core=j,order='last-from-ACTUAL-positive-debit-stopped-leaf',rows=early_rows,terminals=early_leaves,
                initial_credit=early['credit'],initial_debit=early['debit'],initial_labels=early['labels'],terminal_credit_mean=weighted,
                source_stop_reaches=['1/128'],outside_donor='Same original spent outgoing A and booked donor; all other source terminals and parked2tau unchanged'))
        results.append(dict(core_orbit=j,verdict=verdict,initial_credit=evalp(A),required_credit=evalp(root['R']),extra_initial_credit=evalp(gap),
            exact_initial_credit=pack(A),exact_required_credit=pack(root['R']),exact_gap=pack(gap),
            states=[dict(truth=list(t),S=evalp(v['S']),H=evalp(minus({None:4*v['I']},v['S'])),I=str(v['I']),R=evalp(v['R']),winner=v['winner'],exact_S=pack(v['S']),exact_R=pack(v['R'])) for t,v in states.items()],
            attaining_policy=[dict(path=path,reach=str(w),S=evalp(p['S'])) for path,w,p in leaves]))
        coverage.append(dict(core=j,compressed_states=len(states),labelled_restrictions=rawstates,labelled_query_rows=rawrows,compressed_query_rows=sum(len(v['actions']) for v in states.values())))
        all_query_rows.extend(query_rows)
        (ROOT/'out'/('PILOT_CASES.json' if '--pilot' in sys.argv else 'HULL_CASES.json')).write_text(json.dumps(dict(orbits=results,coverage=coverage,query_rows=all_query_rows,financial_policies=finance),indent=2)+'\n',encoding='utf-8')
        test(time.perf_counter()-start<55)
    result=dict(version='A072-stopping-credit-hull-v1.1',orbits=[dict(core=r['core_orbit'],verdict=r['verdict'],initial_credit=r['initial_credit'],required_credit=r['required_credit'],gap=r['extra_initial_credit']) for r in results],
        coverage=coverage,source_review=review,exact_checks=COUNT,engine_checks=engine.tests,
        independent_states=independent.cache_info().currsize,financial_policies=len(finance),runtime_seconds=time.perf_counter()-start,scale_bits=192,full_fei='OPEN')
    (ROOT/'out'/('PILOT.json' if '--pilot' in sys.argv else 'VALIDATION.json')).write_text(json.dumps(result,indent=2)+'\n',encoding='utf-8')
    print(json.dumps({k:v for k,v in result.items() if k!='source_review'}))

if __name__=='__main__':main()
