"""Independent fixed-root referee: actual Boolean sources and exact compressed cells."""
from pathlib import Path
from fractions import Fraction as F
from itertools import product
import sys,time,json
sys.dont_write_bytecode=True
import audit as a
ROOT=Path(__file__).resolve().parents[1]
def add(*v):return a.lin(*[(1,x) for x in v])
def sub(x,y):return a.lin((1,x),(-1,y))
def avg(v):return a.lin(*[(F(1,len(v)),x) for x in v])
def dot(v,w):return sum((x*y for x,y in zip(v,w)),F())
def module():
 h=a.core(2);G=a.carrier((1,)*64,63);H=a.carrier(h,63)
 t=tuple((H if z&1 else G)[z>>1] for z in range(512))
 return t,G,H
def outer():
 f,G,H=module();t=tuple(f[z>>2]*(-1 if (z&1) and (z&2) else 1) for z in range(2048))
 p,ds,H0,M,TC=a.stats(t);Q=tuple([F(1,2048)]*2048)
 a.ck(ds==(F(1,2),)*11,'all11 actual physical influences')
 a.eq(H0,a.const(F(17,2)),'full source entropy');a.eq(a.kl(p,Q),a.const(F(5,2)),'full original product KL')
 S=a.const(F(27,2));c,R,r,O,E,Kc,z=a.move(t,2,Q)
 a.ck(r==[F(1,8),F(7,8)],'actual s prediction');a.eq(E,{},'prefix E0')
 bills=[];Hs=[]
 for b in [0,1]:
  cc,rr,pr,ov,ev,k,z=a.move(c[b],1,R[b]);a.ck(pr==[F(1,2)]*2,'outer pivot fair')
  a.eq(ov,{},'pivot O0');a.eq(ev,{},'pivot E0')
  for j in [0,1]:
   a.eq(k[j],Kc[b],'pivot retains inherited K')
   bill=sub(a.stats(cc[j])[4],k[j]);a.gt(bill,'both signed sibling reset debits positive')
   bills.append(bill);Hs.append(a.stats(cc[j])[2])
 B=avg(bills);a.eq(B,a.lin((1,a.const(3)),(F(-1,2),a.log(7))),'exact original pending reserve')
 a.eq(B,add(a.const(1),O),'outcome cost plus one')
 a.eq(avg(Hs),a.const(F(9,2)),'full terminal entropy')
 a.gt(sub(B,a.const(F(3,2))),'half-bit extension fails by more than1')
 a.gt(sub(a.lin((F(1,8),S)),B),'same source reserve<S/8')
 a.gt(a.lin((F(5,8),S),(-1,a.kl(p,Q)),(-1,B)),'old quarter and full pipeline remain; remainder>S/8')
 a.ck(4096<4802,'all-l log guard');a.ck(all(8*l+10<=9*l+8 for l in range(2,5)),'linear comparison base control')
 return {'source_bits':11,'H':H0,'I':sum(ds),'K':a.kl(p,Q),'S_outer':S,'B':B,'terminal_H':avg(Hs),'reset_debits':bills,'all_l_proof':'PROOF.md; finite controls do not imply all-l'}
P=(F(1,2),F(1,8),F(3,8),F());Q4=(F(1,64),F(1,64),F(3,4),F(7,32))
def selectors():
 rows=[];c=a.lin((F(1,2),a.log(F(16,7))));f,G,H=module()
 for L in range(1,5):
  cells=list(product(range(4),repeat=L));p0=tuple(__import__('math').prod(P[x] for x in z) for z in cells);q0=tuple(__import__('math').prod(Q4[x] for x in z) for z in cells)
  a.eq(a.kl(p0,q0),a.const(F(5*L,2)),'actual compressed original A')
  for t in range(L+1):
   for b in product([0,1],repeat=t):
    p=p0;q=q0;R=F(1);Os={};local=[list(Q4) for _ in range(L)]
    for j,out in enumerate(b):
     k=[F(1,2) if not p[s] else F(int((z[j]!=0)==bool(out))) for s,z in enumerate(cells)]
     reach=dot(q,k);R*=reach
     other=1-reach;Os=add(Os,a.lin((F(-1,2),a.log(4*reach*other))))
     q=tuple(q[s]*k[s]/reach for s in range(len(q)))
     # Actual physical conditional spectrum; source-zero rows remain zero.
     p=tuple(2*p[s]*k[s] for s in range(len(p)));a.ck(sum(p)==1,'fair physical child')
     lr=F(1,8) if out==0 else F(7,8)
     local[j]=[Q4[x]*(F(1,2) if x==3 else F(int((x!=0)==bool(out))))/lr for x in range(4)]
    Rformula=(1-F(25,32)**L)*F(1,2)**t+F(25,32)**L*__import__('math').prod(F(1,50) if x==0 else F(49,50) for x in b)
    a.ck(R==Rformula,'actual global joint likelihood')
    T=tuple(__import__('math').prod(local[j][z[j]] for j in range(L)) for z in cells)
    Kg=a.kl(p,q);Kt=a.kl(p,T);d=sub(Kg,Kt)
    predlocal=__import__('math').prod(F(1,8) if x==0 else F(7,8) for x in b)
    a.eq(d,a.log(R/predlocal),'exact signed likelihood correction')
    fullH=a.lin((L-t,a.stats(f)[2]),(b.count(0),a.stats(G)[2]),(b.count(1),a.stats(H)[2]))
    a.eq(fullH,a.const(F(13*L+t,2)-5*b.count(0)),'complete actual terminal entropy')
    if L==2 and b==(0,):
     mass=sum((q[s] for s,z in enumerate(cells) if z[0] in [1,2] and z[1]==3),F())
     a.ck(mass==F(343,848),'positive global mass on local-reference zero set')
     a.ck(all(not T[s] for s,z in enumerate(cells) if z[0] in [1,2] and z[1]==3),'forward reference KL infinite guard')
    rows.append({'L':L,'b':b,'global_history_probability':R,'K':Kg,'K_tensor':Kt,'d':d,'O':Os,'full_terminal_H':fullH})
   same=[v for v in rows if v['L']==L and len(v['b'])==t]
   delta=avg([v['d'] for v in same]);Om=avg([v['O'] for v in same])
   a.eq(add(avg([v['K'] for v in same]),Om),a.const(F(5*L,2)),'FAIR mean retains original A, not each path')
   a.eq(delta,sub(a.lin((t,c)),Om),'expected deficit exact')
   a.ge(sub(a.lin((-1,a.log(1-F(25,32)**L))),Om),'uniform mixture bound')
   if L==4 and t==L:a.gt(sub(delta,a.const(F(L,4))),'linear omitted terminal deficit')
 return {'history_cases':len(rows),'rows':rows}
def compressed_kl(t,C,Q):
 p=a.stats(t)[0]
 return a.kl(tuple(c*x for c in C for x in p),tuple(x for row in Q for x in row))
def compressed_move(t,i,C,Q):
 p=a.stats(t)[0];cs=[a.child(t,i,b) for b in [0,1]];ps=[a.stats(v)[0] for v in cs]
 pairs=[(s,s|(1<<i)) for s in range(len(t)) if not (s>>i)&1]
 pe=tuple(p[u]+p[v] for u,v in pairs);qe=[tuple(row[u]+row[v] for u,v in pairs) for row in Q]
 U=[[[] for c in C] for b in [0,1]];Z=[[[] for c in C] for b in [0,1]]
 for c,pc in enumerate(C):
  for s,(u,v) in enumerate(pairs):
   oldzero=Q[c][u]*int(not(pc*p[u]))+Q[c][v]*int(not(pc*p[v]))
   for b in [0,1]:
    k=ps[b][s]/(2*pe[s]) if pc and pe[s] else F(1,2)
    U[b][c].append(qe[c][s]*k);Z[b][c].append(oldzero*k*int(bool(pc*ps[b][s])))
 reach=[sum((sum(row) for row in mat),F()) for mat in U];a.ck(sum(reach)==1 and min(reach)>0,'actual normalized compressed prediction')
 rr=[tuple(tuple(x/reach[b] for x in row) for row in U[b]) for b in [0,1]]
 K=compressed_kl(t,C,Q);Kc=[compressed_kl(cs[b],C,rr[b]) for b in [0,1]]
 Ke=a.kl(tuple(pc*x for pc in C for x in pe),tuple(x for row in qe for x in row))
 E=sub(K,Ke);O=a.lin((F(-1,2),a.log(4*reach[0]*reach[1])))
 a.eq(K,add(E,O,avg(Kc)),'global physical KL chain including erasure');a.ge(E,'actual global erasure nonnegative')
 reentry=[sum((sum(row) for row in Z[b]),F())/reach[b] for b in [0,1]]
 return cs,rr,reach,O,E,Kc,reentry
def mixed(pilot):
 t,G,H=module();p=a.stats(t)[0];cs,lr,rl,ol,el,kl,z=a.move(t,0,tuple([F(1,512)]*512))
 groups=[]
 for s,(pg,ph) in enumerate(zip(a.stats(G)[0],a.stats(H)[0])):groups.append(0 if pg else 1 if ph==F(1,16) else 2 if ph else 3)
 a.ck(tuple(groups.count(c) for c in range(4))==(4,4,192,56),'actual carrier cell degeneracies')
 for c in range(4):a.ck(sum((p[s] for s in range(512) if groups[s>>1]==c),F())==P[c],'actual nine-bit Boolean cell source masses')
 rows=[];outsidecounts=(4,4,192,56);pending={};branchK={};postinstall_queries=0
 for b in [0,1]:
  rg=F(53,256) if b==0 else F(203,256)
  Oold=a.lin((F(-1,2),a.log(4*F(53,256)*F(203,256))))
  for which in [0,1]:
   if which==0:
    actual=cs[b];C=P;Rlocal=lr[b];outsideR=Q4;outsideK=a.const(F(5,2));outsideH=a.const(F(13,2))
    mat=tuple(tuple(Q4[c]*F(1,256)*(F(1,2) if c==3 or groups[s]==3 else F(int((groups[s]!=0)==bool(b))))/rg for s in range(256)) for c in range(4))
    indices=[2] if pilot else range(2,8)
   else:
    actual=t;C=(F(1),F(),F(),F()) if b==0 else (F(),F(1,4),F(3,4),F())
    Rlocal=tuple([F(1,512)]*512)
    outsideR=tuple(Q4[c]*(F(1,2) if c==3 else F(int((c!=0)==bool(b))))/rl[b] for c in range(4))
    outsideK=a.kl(C,outsideR);outsideH=a.stats(cs[b])[2]
    mat=tuple(tuple(Q4[c]*F(1,512)*(F(1,2) if c==3 or not p[s] else F(int((c!=0)==bool(b))))/rg for s in range(512)) for c in range(4))
    indices=[4] if pilot else range(3,9)
   Kg=compressed_kl(actual,C,mat);Kt=add(a.kl(a.stats(actual)[0],Rlocal),outsideK);d=sub(Kg,Kt)
   branchK[b]=Kg;pending[b]=a.maximum(pending.get(b,{}),a.pos(a.lin((-1,d))))
   a.eq(Kg,add(kl[b],a.const(F(5,2)),a.log(rg/rl[b])),'conditional global K after selector; root average deferred')
   for i in indices:
    glob=compressed_move(actual,i,C,mat);loc=a.move(actual,i,Rlocal)
    ktchild=[add(v,outsideK) for v in loc[5]];dc=[sub(glob[5][j],ktchild[j]) for j in [0,1]]
    eta=sub(loc[4],glob[4]);expected=add(d,eta,loc[3],a.lin((-1,glob[3])))
    a.eq(avg(dc),expected,'full signed cocycle; local-minus-global erasure retained')
    if which==0:a.eq(eta,{},'same-module erasure differences cancel')
    else:
     pairs=[(s,s|(1<<i)) for s in range(512) if not (s>>i)&1]
     rho=sum((p[u]+p[v] for u,v in pairs if bool(p[u])!=bool(p[v])),F())
     a.eq(eta,a.lin((rho,a.log(F(4,3)))),'other-module exact nonzero erasure defect')
     a.ck(rho==([F(),F(5,8),F(5,8),F(5,8),F(7,64),F(7,64)][i-3]),'all six ordinary boundary masses')
    a.eq(add(avg(glob[5]),glob[3],glob[4]),Kg,'conditional inherited K with full erasure credit')
    candidate=sub(avg([a.pos(a.lin((-1,v))) for v in dc]),glob[4])
    pending[b]=a.maximum(pending[b],candidate)
    for j in [0,1]:
     installed=tuple(tuple(outsideR[c]*x for x in loc[1][j]) for c in range(4))
     a.eq(compressed_kl(glob[0][j],C,installed),ktchild[j],'ACTUAL installed local tensor KL')
     later=compressed_move(glob[0][j],0,C,installed);postinstall_queries+=1
     a.eq(add(avg(later[5]),later[3],later[4]),ktchild[j],'actual post-install global query paid without renewed allocation')
    fullH=avg([add(a.stats(c)[2],outsideH) for c in glob[0]])
    rows.append({'selector_outcome':b,'queried_module':which+1,'data_index':i,'global_prediction':glob[2],'local_prediction':loc[2],'E_global':glob[4],'E_local':loc[4],'extra_erasure_correction':eta,'d_parent':d,'d_children':dc,'reference_zero_to_source_positive_mass':glob[6],'full_terminal_H':fullH})
 a.eq(add(avg(list(branchK.values())),Oold),a.const(5),'FAIR root average retains original A5')
 B=avg(list(pending.values()));a.ge(sub(a.const(5),B),'same original second A cap pays all admitted mixed installations')
 return {'query_cases':len(rows),'postinstall_queries':postinstall_queries,'exact_minimal_extra_booking':B,'branch_pending':pending,'rows':rows,'outside_atom_counts':outsidecounts,'root_original_A':5,'root_original_S':23,'old_quarter_remainder':F(49,4)}
if __name__=='__main__':
 start=time.perf_counter();mode=sys.argv[1];pilot='--pilot' in sys.argv
 out={'outer':outer,'selectors':selectors,'mixed':lambda:mixed(pilot)}[mode]()
 a.ck(time.perf_counter()-start<55,'frozen55-second cap')
 out.update(status='PASS',assertions=a.COUNT,seconds=time.perf_counter()-start)
 path=ROOT/'out'/(mode.upper()+('_PILOT' if pilot else '')+'.json')
 path.write_text(json.dumps(a.serial(out),indent=2)+'\n',encoding='utf-8',newline='\n')
 print(json.dumps(a.serial({k:v for k,v in out.items() if k!='rows'})))
