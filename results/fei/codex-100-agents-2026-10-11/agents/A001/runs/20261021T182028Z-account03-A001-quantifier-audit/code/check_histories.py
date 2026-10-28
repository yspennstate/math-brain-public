from helpers import *
import helpers
from itertools import product
import hashlib

start=time.perf_counter()
pilot='--pilot' in sys.argv
root=tuple(encoded([1 if y&7==0 else -1 for y in range(64)],
                   [-1 if y==0 or y&7 else 1 for y in range(64)]))

@lru_cache(None)
def profile(v):
    w=tuple(fw(v)); n=len(v)
    ck(sum(a*a for a in w)==n*n)
    p=tuple(F(a*a,n*n) for a in w)
    H=entropy(p)
    I=sum((F(s.bit_count()*a*a,n*n) for s,a in enumerate(w)),F(0))
    return w,p,H,I

@lru_cache(None)
def split(v,j):
    w,p,H,I=profile(v)
    children=tuple(tuple(restrict(v,j,s)) for s in (0,1))
    childprofiles=[profile(c) for c in children]
    for s,(wc,pc,Hc,Ic) in enumerate(childprofiles):
        for t,a in enumerate(wc):
            u=insert(t,j,0)
            ck(2*a==w[u]+((-1)**s)*w[u|(1<<j)])
    e=inf(v,j)
    ck(e==sum((p[t] for t in range(len(v)) if t&(1<<j)),F(0)))
    ck(I==e+sum((cp[3]/2 for cp in childprofiles),F(0)))
    B=add(*[(1,phi(p[t],p[t|(1<<j)])) for t in range(len(v)) if not t&(1<<j)])
    meanH=add(*[(F(1,2),cp[2]) for cp in childprofiles])
    JS=add((1,H),(-1,B),(-1,meanH))
    # An exactly zero prime-log map is accepted as equality. All other
    # signs must be certified, never inferred from a floating approximation.
    ck(not JS or interval(JS)[0]>0)
    ck(not B or interval(B)[0]>0)
    return children,B,meanH,JS,e

def subcube(assignment):
    free=[j for j,a in enumerate(assignment) if a==2]
    fixed=sum((a<<j for j,a in enumerate(assignment) if a!=2),0)
    v=[]
    for t in range(1<<len(free)):
        x=fixed
        for k,j in enumerate(free): x|=((t>>k)&1)<<j
        v.append(root[x])
    return tuple(v),free

b=tuple(1 if y&7==0 else -1 for y in range(64));c=list(b);c[0]=-1;c=tuple(c)
T0=add((F(1,2),profile(b)[2]),(F(1,2),profile(c)[2]))
I0=(profile(b)[3]+profile(c)[3])/2
ck(I0==F(3,4))
Hroot=profile(root)[2]
S=add((1,const(4*I0)),(-1,T0))
gap=add((1,Hroot),(-1,T0))
margin=add((1,S),(-1,gap))
ck(margin==add((1,const(3)),(-1,Hroot)))
ck(interval(margin)[0]>0)
G=tuple(selector(b,c))
ck(Hroot==add((1,profile(G)[2]),(1,const(F(1,32)))))
Q=erase(G,0)
admission=add((1,Q),(1,const(F(5,64))))
ck(interval(add((1,admission),(-1,gap)))[0]>0)
ck(interval(add((1,S),(-1,admission)))[0]>0)

digest=hashlib.sha256(); nodes=edges=0; equality=positive=0
assignments=(tuple(2 if j not in (3,6) else vals[(3,6).index(j)] for j in range(9))
             for vals in product(range(3),repeat=2)) if pilot else product(range(3),repeat=9)
for a in assignments:
    ck(time.perf_counter()-start<55)
    v,free=subcube(a);profile(v);nodes+=1
    for k,j in enumerate(free):
        children,B,meanH,JS,e=split(v,k);edges+=1
        for s in (0,1):
            aa=list(a);aa[j]=s;vv,_=subcube(aa);ck(vv==children[s])
        if JS:positive+=1
        else:equality+=1
        # Log coefficients retain both complete terminal laws. The only
        # budget is S, and gap is the initial debit paid from that S.
        ck(add((1,profile(v)[2]),(-1,B),(-1,meanH))==JS)
        digest.update((str(a)+str(j)+str(enc(B))+str(enc(JS))).encode('utf-8'))
    if nodes%1000==0:
        (RUN/'out/CHECKPOINT.json').write_text(json.dumps({'nodes':nodes,'edges':edges,'assertions':helpers.count})+'\n',encoding='utf-8')

# Explicit sequential data policies, then full encoder resolution. The
# second query is charged in each surviving first-query branch.
second=[]
for j in range(6):
    for k in range(6):
        if j==k:continue
        if pilot and (j,k)!=(0,3):continue
        bill,terminal,leafI=tree(root,[j+3,k+3,0,1,2])
        residual=add((1,const(3)),(-1,bill),(-1,terminal))
        ck(interval(residual)[0]>0)
        firstB=erase(root,j+3)
        nextB=add(*[(F(1,2),erase(tuple(restrict(root,j+3,s)),k+3-int(k>j))) for s in (0,1)])
        # Conservation of booked costs, with no fresh descendant S4.
        terminals=add((1,terminal))
        encoder=add((1,bill),(-1,firstB),(-1,nextB))
        ck(add((1,S),(-1,firstB),(-1,nextB),(-1,encoder),(1,T0),(-1,terminals))==residual)
        second.append({'first':j,'second':k,'erasure':record(bill),'terminals':record(terminal),'remaining_original_quota':record(residual),'remaining_influence':str(leafI)})

out={'status':'PASS','scope':'one actual nine-bit Boolean fixture; all adaptive stopping trees by local induction; no arbitrary Q','nodes':nodes,'node_query_pairs':edges,'positive_JS_pairs':positive,'zero_JS_pairs':equality,'unique_profiles':profile.cache_info().currsize,'unique_splits':split.cache_info().currsize,'assertions':helpers.count,'seconds':time.perf_counter()-start,'edge_digest_sha256':digest.hexdigest(),'root':{'entropy':record(Hroot),'original_terminal_escrow':record(T0),'original_S4':record(S),'initial_entropy_increment':record(gap),'all_history_margin':record(margin),'rational_admission_Q_plus_5delta':record(admission),'unspent_after_admission':record(add((1,S),(-1,admission)))},'second_query_policies':second}
(RUN/'out'/('PILOT.json' if pilot else 'CHECK.json')).write_text(json.dumps(out,indent=2)+'\n',encoding='utf-8')
print(json.dumps({k:v for k,v in out.items() if k not in ('root','second_query_policies')}))
