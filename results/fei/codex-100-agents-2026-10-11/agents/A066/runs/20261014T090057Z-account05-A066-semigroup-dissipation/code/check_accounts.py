from pathlib import Path
from fractions import Fraction as Q
from functools import lru_cache
from itertools import permutations
import json,sys,time
run=Path(__file__).resolve().parents[1]
old=run.parent/'20261014T042048Z-account05-A066-semigroup-dissipation/code/check_quotient.py'
ns={'__file__':str(old)}
exec(compile(old.read_text().split('cases=rows=0')[0],str(old),'exec'),ns)
test,add,plus,bounds,walsh=[ns[k] for k in ['test','logadd','combine','bound','physical_spectrum']]
started=time.perf_counter();mode=sys.argv[1]
def entropy(probabilities):
    result={}
    for p in probabilities:
        if p:add(result,1/p,p)
    return result
def restrict(values,i,y):
    return tuple(values[(x&((1<<i)-1))|((x>>i)<<(i+1))|(y<<i)] for x in range(len(values)//2))

@lru_cache(None)
def state(b,q):
    d=(len(b)-1).bit_length();r=(len(q)-1).bit_length();delta=Q(1,len(b));s=b[0]
    values=tuple(b[y]+(q[z]-s if y==0 else 0) for y in range(len(b)) for z in range(len(q)))
    test(all(v in [-1,1] for v in values))
    A=walsh(values);p=[a*a for a in A];qa=walsh(q);qp=[a*a for a in qa]
    test(sum(p)==1)
    H=entropy(p);Hq=entropy(qp);G=plus((Hq,delta));R=delta*d*(1-qa[0]**2)
    I=sum(S.bit_count()*v for S,v in enumerate(p))
    empty=entropy([p[0]])
    return {'b':b,'q':q,'r':r,'d':d,'delta':delta,'values':values,'p':p,'qa':qa,'H':H,'G':G,'R':R,'I':I,'empty':empty}

@lru_cache(None)
def node(b,q,i):
    f=state(b,q);r=f['r'];d=f['d'];delta=f['delta']
    if i<r:
        children=[(b,restrict(q,i,y)) for y in [0,1]]
        beta=f['qa'][1<<i];Rdrop=delta*d*beta*beta;Drelease=Q(0)
    else:
        j=i-r;bc0=restrict(b,j,0);bc1=restrict(b,j,1)
        children=[(bc0,q),(bc1,(bc1[0],)*len(q))]
        Rdrop=delta*(1-f['qa'][0]**2);Drelease=Rdrop
    childrenstates=[state(*c) for c in children]
    Hdrop=plus((f['H'],1),*[(c['H'],Q(-1,2)) for c in childrenstates])
    Gdrop=plus((f['G'],1),*[(c['G'],Q(-1,2)) for c in childrenstates])
    test(f['R']-sum(c['R'] for c in childrenstates)/2==Rdrop)
    ei=Q(sum(f['values'][x]!=f['values'][x^(1<<i)] for x in range(len(f['values']))),len(f['values']))
    test(f['I']-sum(c['I'] for c in childrenstates)/2==ei)
    bit=1<<i;M={}
    for T in range(len(f['p'])):
        if T&bit:continue
        lower,upper=f['p'][T],f['p'][T|bit]
        if upper:add(M,(lower+upper)/upper,upper)
    if i<r:
        qa=f['qa'];Eq=sum(qa[S]**2 for S in range(len(q)) if S&bit)
        test(ei==delta*Eq)
        Mq={}
        for U in range(len(q)):
            if U&bit:continue
            lower,upper=qa[U]**2,qa[U|bit]**2
            if upper:add(Mq,(lower+upper)/upper,upper)
        rho=1-delta+delta*(qa[0]**2+beta**2)
        Mc=plus((Mq,delta))
        if beta:add(Mc,rho/(delta*(qa[0]**2+beta**2)),delta*beta*beta)
        loss=plus((Mc,1),(M,-1))
        if loss:test(bounds(loss)[0]>=0)
        # Scalar theorem uses 2/e; 2/e<3/4 provides an exact rational finite guard.
        extra=plus((Mc,1),(Mq,-delta),({2:Rdrop},-1))
        test(bounds(extra)[1]<=Q(3,4)*ei)
        test(bounds(plus((M,1),(Gdrop,-1),({2:Rdrop},-1)))[1]<=Q(3,4)*ei)
        test(bounds(plus((Hdrop,1),(Gdrop,-1),({2:Rdrop},-1)))[1]<=Q(15,4)*ei)
    else:test(not Gdrop)
    Bdrop=plus((f['empty'],1),*[(c['empty'],Q(-1,2)) for c in childrenstates])
    heatdrop=plus((Hdrop,Q(1,2)),(Bdrop,Q(-1,2)))
    return children,M,Hdrop,Gdrop,Rdrop,Drelease,ei,Bdrop,heatdrop

@lru_cache(None)
def prefix(b,q,order):
    f=state(b,q)
    if not order:
        return {'M':{},'CH':{},'DH':{},'PC':Q(0),'DR':Q(0),'leafH':f['H'],'leafG':f['G'],'leafR':f['R'],'leafI':f['I'],'boundary':{},'heat':{}}
    i=order[0];childs,M,Hdrop,Gdrop,Rdrop,Drel,ei,Bdrop,Kdrop=node(b,q,i)
    control=i<f['r'];next_order=tuple(j-(j>i) for j in order[1:])
    out={'M':M if control else {},'CH':Hdrop if control else {},'DH':{} if control else Hdrop,'PC':ei if control else Q(0),'DR':Drel,'leafH':{},'leafG':{},'leafR':Q(0),'leafI':Q(0),'boundary':Bdrop if control else {},'heat':Kdrop if control else {}}
    for bc,qc in childs:
        c=prefix(bc,qc,next_order)
        for key in ['M','CH','DH','leafH','leafG','boundary','heat']:out[key]=plus((out[key],1),(c[key],Q(1,2)))
        for key in ['PC','DR','leafR','leafI']:out[key]+=c[key]/2
    capacity=plus((f['G'],1),(out['leafG'],-1),({2:f['R']-out['leafR']-out['DR']},1))
    test(bounds(plus((out['M'],1),(capacity,-1)))[1]<=Q(3,4)*out['PC'])
    test(bounds(plus((out['CH'],1),(capacity,-1)))[1]<=Q(15,4)*out['PC'])
    test(plus((f['H'],1),(out['leafH'],-1),(out['CH'],-1),(out['DH'],-1))=={})
    test(plus((out['heat'],2),(out['CH'],-1),(out['boundary'],1))=={})
    test(f['R']-out['leafR']-out['DR']>=0)
    return out

rootpairs=orders=prefixes=0
for d in ([1] if mode=='pilot' else [1,2]):
    for r in ([1] if mode=='pilot' else [1,2]):
        for bm in range(1<<(1<<d)):
            b=tuple(1 if bm>>x&1 else -1 for x in range(1<<d))
            for qm in range(1<<(1<<r)):
                q=tuple(1 if qm>>x&1 else -1 for x in range(1<<r));rootpairs+=1
                for order in permutations(range(d+r)):
                    orders+=1
                    for stop in range(1,d+r+1):prefix(b,q,order[:stop]);prefixes+=1
test(rootpairs==(16 if mode=='pilot' else 400))
test(orders==(32 if mode=='pilot' else 6944))
test(prefixes==(64 if mode=='pilot' else 26944))
out={'mode':mode,'root_pairs':rootpairs,'orders':orders,'stopping_prefixes':prefixes,'cached_physical_states':state.cache_info().currsize,
     'assertions':ns['ns']['assertions'],'elapsed_seconds':time.perf_counter()-started,
     'arithmetic':'Exact prime-log identities and Fraction physical telescopes; rational enclosure signs with 2/e<3/4 finite guard',
     'terminal_retention':'Full actual entropy split CH+DH+leafH checked; signed heat boundary retained; data R release excluded from control spend.'}
(run/'out').mkdir(exist_ok=True)
(run/'out'/('CHECK_'+mode.upper()+'.json')).write_text(json.dumps(out,indent=2)+'\n',encoding='utf-8');print(json.dumps(out))
