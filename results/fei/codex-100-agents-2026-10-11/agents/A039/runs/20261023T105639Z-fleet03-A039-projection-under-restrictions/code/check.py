"""Phase-point coherent hereditary reset, frozen domain v1."""
from pathlib import Path
from fractions import Fraction as F
import importlib.util,json,sys,time

R=Path(__file__).resolve().parents[1];OWN=R.parents[1]
old=OWN/'runs/20261023T032407Z-fleet03-A039-projection-under-restrictions/code/check.py'
spec=importlib.util.spec_from_file_location('a039_prior_exact',old);H=importlib.util.module_from_spec(spec);spec.loader.exec_module(H)
PILOT='--pilot' in sys.argv;START=time.monotonic();EXTRA=0
def ck(a,label):
    global EXTRA
    EXTRA+=1
    assert a,label
    assert time.monotonic()-START<55,'frozen55secondguard'
def phase(w):
    return [(-1 if x.bit_count()%2 else 1)*(-1 if x==0 else 1) for x in range(1<<w)]
def qlaw(table,beta=F(5,6)):
    p=H.spectrum(table)
    if sum(a>0 for a in p)==1:return p
    ck(p[-1]>0,'full-frequency spike has existing source support')
    q=[p[0]]+[beta*a for a in p[1:]]
    q[-1]+=(1-beta)*(1-p[0])
    ck(sum(q)==1 and q[0]==p[0],'normalized matching-empty q')
    ck(all((a>0)==(b>0) for a,b in zip(p,q)),'same support')
    return q
def makecore(blocks):
    vals=[1]
    for a in blocks:vals=[x*y for y in a for x in vals]
    return vals
def selector(core,epsilon=1):return [epsilon if i%2==0 else core[i>>1] for i in range(2*len(core))]
def signed(a,s):return [s*x for x in a]
def local(w,stype,eps,sign):
    vt=phase(w)
    ut={'none':[1],'character1':[1,-1],'point2':[-1,1,1,1],'phase3':phase(3)}[stype]
    p=H.spectrum(vt);pu=H.spectrum(ut);q=qlaw(vt);qu=qlaw(ut)
    table=selector(signed(makecore([vt,ut]),sign),eps)
    P=H.spectrum(table);ref=H.lift(table,H.tensor([q,qu]))
    ll=H.ratios(q,p);ss=H.ratios(qu,pu)
    full_l=[ll[(i>>1)&((1<<w)-1)] for i in range(len(P))]
    full_s=[ss[i>>(w+1)] for i in range(len(P))]
    ck(all(a==b*c*d for a,b,c,d in zip(ref,P,full_l,full_s)),'general exact likelihood identity')
    B=[a*b for a,b in zip(P,full_l)];C=[a*b for a,b in zip(P,full_s)]
    ch,r,pb,rb,ks=H.channel(table,ref,1);bb=H.erase(B,1);cb=H.erase(C,1)
    ck(sum(B)==1 and sum(C)==1,'generic isolated-factor laws normalized')
    ck(all(H.dot(cb,k)==F(1,2) for k in ks),'fair baseline output')
    ck(all(H.dot(bb,k)==ry for k,ry in zip(ks,r)),'spectator reference leaves outcome exactly unchanged')
    out=H.IV();term=H.IV()
    for y,(t,py,oldref) in enumerate(ch):
        vy=H.restrict(vt,0,y);qy=qlaw(vy)
        nr=H.lift(t,H.tensor([qy,qu]));nl=H.ratios(qy,H.spectrum(vy))
        sres=[ss[i>>w] for i in range(len(py))];br=H.ratios(bb,pb)
        ck(all(a==b*c*d/(2*r[y]) for a,b,c,d in zip(oldref,py,sres,br)),'exact normalized inherited likelihood')
        ck(all(a==py[i]*sres[i]*nl[(i>>1)&((1<<(w-1))-1)] for i,a in enumerate(nr)),'exact destination keeps spectators')
        out+=(H.KL(py,nr)-H.KL(py,oldref))*F(1,2)
        term+=H.KL(H.spectrum(vy),qy)*F(1,4)
    rhs=term-H.KL(pb,bb)+H.KL([F(1,2)]*2,r)
    ck(max(out.lo,rhs.lo)<=min(out.hi,rhs.hi),'identity interval consistency only')
    inf=F(1)-F(2,1<<w)
    ck(H.influence(vt)==w*inf,'spectral-phase actual influence formula')
    ck(out.hi<(inf/6)*H.SCALE,'influence-priced reset bound')
    if w==3 and stype=='character1':ck(out.lo>0,'actual same-profile non-point obstruction')
    return {'w':w,'spectator':stype,'epsilon':eps,'core_sign':sign,'sigma':out.json(),'outcome_probabilities':list(map(str,r)),'query_influence':str(inf),'upper_price':str(inf/6)}
def root_table(blocks):
    core=makecore(blocks)
    return [(-1 if i&2 else 1) if not i&1 else (core[i>>3] if i&4 else 1) for i in range(8*len(core))]
def rootref(table,blocks):
    P=H.spectrum(table);q=H.tensor([qlaw(v,F(7,8)) for v in blocks])
    ref=[P[i] if i>>3==0 else (q[i>>3]/16 if (i&7) in [0,1,4,5] else F(0)) for i in range(len(P))]
    ck(sum(ref)==1,'original correlated root normalized')
    return ref
def recurse(table,ref,blocks,weight,depth,reverse,acc):
    if depth==0 or sum((len(v)-1).bit_length() for v in blocks)==0:
        acc['leaves'].append((weight,table,ref));return
    choices=[i for i,v in enumerate(blocks) if len(v)>1]
    j=choices[-1] if reverse else choices[0]
    # Choose a bit in a block; all remaining block coordinates remain represented,
    # including dummy variables after a factor becomes constant.
    physical=1+sum((len(v)-1).bit_length() for v in blocks[:j])
    children,_,_,_,_=H.channel(table,ref,physical)
    oldp=H.spectrum(blocks[j]);inf=H.influence(blocks[j])-sum(H.influence(H.restrict(blocks[j],0,y)) for y in [0,1])/2
    node=H.IV()
    for y,(t,py,oldref) in enumerate(children):
        newblocks=list(blocks);newblocks[j]=H.restrict(blocks[j],0,y)
        nr=H.lift(t,H.tensor([qlaw(v) for v in newblocks]))
        # Equal rational reference arrays give EXACTLY zero conversion; subtracting
        # independently rounded identical nonzero KL intervals loses that equality.
        d=H.IV() if nr==oldref else H.KL(py,nr)-H.KL(py,oldref)
        node+=d*F(1,2);acc['sigma']+=d*(weight/2)
        acc['transactions']+=1
        if d.lo>0:acc['positive_children']+=1
        recurse(t,nr,newblocks,weight/2,depth-1,reverse,acc)
    ck(node.hi<=H.iv(F(inf)/6).hi,f'every reached factor query priced from actual influence; inf={inf}, node={node.json()}')
def root(widths,policy,depth):
    blocks=[phase(w) for w in widths];table=root_table(blocks);P=H.spectrum(table);Q=rootref(table,blocks)
    A0=H.KL(P,Q);H0=H.entropy(P);I0=H.influence(table)
    b,_,_,_,_=H.channel(table,Q,2)
    aa,_,_,_,_=H.channel(b[1][0],b[1][2],1)
    sigma1=H.IV();acc={'leaves':[(F(1,2),b[0][0],b[0][2])],'sigma':H.IV(),'transactions':0,'positive_children':0}
    for a,(t,p,oldref) in enumerate(aa):
        nr=H.lift(t,H.tensor([qlaw(v) for v in blocks]));sigma1+=(H.KL(p,nr)-H.KL(p,oldref))*F(1,4)
        recurse(t,nr,blocks,F(1,4),depth,policy=='divergent' and a==1,acc)
    leaves=acc['leaves'];ck(sum(w for w,t,q in leaves)==1,'complete terminal mass retained')
    Hf=sum((H.entropy(H.spectrum(t))*w for w,t,q in leaves),H.IV());If=sum(w*H.influence(t) for w,t,q in leaves)
    Kf=sum((H.KL(H.spectrum(t),q)*w for w,t,q in leaves),H.IV())
    S=H.iv(4*If)-Hf;e=H0-Hf-H.iv(4*(I0-If));bill=A0+e+sigma1+acc['sigma']
    remaining=S-H.IV(max(0,bill.lo),max(0,bill.hi))-H.iv(F(1,4))
    ck(remaining.lo>=H.iv(F(3,4)).lo,'same original owner final payment')
    price=sum(H.influence(v) for v in blocks)/12
    ck(acc['sigma'].hi<H.iv(price).hi,'entire later reset bill paid by original influence cap')
    headroom=H.iv(4*I0)-H0-A0-sigma1-acc['sigma']
    ck(headroom.lo>H.SCALE,'inclusive original source headroom >1')
    return {'widths':widths,'policy':policy,'depth':depth,'sigma1':sigma1.json(),'sigma_later':acc['sigma'].json(),'original_influence_cap':str(price),'remaining':remaining.json(),'inclusive_original_headroom':headroom.json(),'final_entropy':Hf.json(),'final_influence':str(If),'final_KL':Kf.json(),'terminal_count':len(leaves),'actual_transactions':acc['transactions'],'positive_reset_children':acc['positive_children']}
def main():
    locals=[]
    for w in ([3] if PILOT else [2,3,4,5,6]):
        for sp in (['none','character1'] if PILOT else ['none','character1','point2','phase3']):
            for eps in [1,-1]:
                for sign in [1,-1]:locals.append(local(w,sp,eps,sign))
    roots=[]
    for widths in ([[3]] if PILOT else [[2],[3],[2,2],[3,2],[3,3]]):
        for policy in (['forward'] if PILOT else ['forward','divergent']):roots.append(root(widths,policy,2 if PILOT else 3))
    out={'status':'PASS','helper_version':'A039-phase-point-hereditary-v1','pilot':PILOT,'local_parent_count':len(locals),'root_policy_count':len(roots),'checks':EXTRA+H.CHECKS,'new_checks':EXTRA,'inherited_primitive_checks':H.CHECKS,'runtime_seconds':time.monotonic()-START,'local':locals,'roots':roots,'equality_method':'exact Fraction likelihood identities; separate auditor gives exact prime-log witness; interval overlaps are consistency checks only','full_FEI':'OPEN'}
    path=R/'out'/('PILOT.json' if PILOT else 'CHECK.json');path.parent.mkdir(exist_ok=True);path.write_text(json.dumps(out,indent=2)+'\n',encoding='utf-8')
    print(json.dumps({k:v for k,v in out.items() if k not in ['local','roots']}))
if __name__=='__main__':main()
