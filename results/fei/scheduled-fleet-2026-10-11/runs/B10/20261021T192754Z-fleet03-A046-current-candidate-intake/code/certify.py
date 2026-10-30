"""Independent direct-character certificate; no foreign helper imports."""
from pathlib import Path
from fractions import Fraction as Q
from functools import lru_cache
import json, time, hashlib

ROOT=Path(__file__).resolve().parents[1]
START=time.perf_counter(); COUNT=0
ZERO=(Q(0),Q(0)); GRID=1<<110
def check(p):
    global COUNT
    assert p
    COUNT+=1
    assert time.perf_counter()-START<55
def add(a,b): return (a[0]+b[0],a[1]+b[1])
def mul(a,b): return (a[0]*b,a[1]*b) if b>=0 else (a[1]*b,a[0]*b)
def sub(a,b): return add(a,mul(b,-1))
def avg(a,b): return mul(add(a,b),Q(1,2))
def point(x): return (x,x)
def rnd(a): return (Q(a[0].numerator*GRID//a[0].denominator,GRID),Q(-((-a[1].numerator*GRID)//a[1].denominator),GRID))
def ln_unit(x):
    z=(x-1)/(x+1); v=z; s=Q(0)
    for k in range(32): s+=v/Q(2*k+1); v*=z*z
    return (2*s,2*s+2*v/(65*(1-z*z)))
LN2=ln_unit(Q(2))
@lru_cache(None)
def log(x):
    assert x>0
    k=x.numerator.bit_length()-x.denominator.bit_length()
    y=x/Q(2)**k
    if y<1: y*=2; k-=1
    assert 1<=y<=2
    l,u=ln_unit(y)
    return rnd((l/LN2[1]+k,u/LN2[0]+k))
def ent(p):
    r=ZERO
    for x in p:
        if x:r=add(r,mul(log(x),-x))
    return r
def kl(p,q):
    r=ZERO
    for x,y in zip(p,q):
        if x:
            check(y>0);r=add(r,mul(sub(log(x),log(y)),x))
    return r
@lru_cache(None)
def spectrum(f):
    # Deliberately quadratic character sum, independent of A040 FWHT.
    N=len(f)
    return tuple(Q(sum(v*(-1 if (x&t).bit_count()%2 else 1) for x,v in enumerate(f)),N) for t in range(N))
def law(f):return tuple(x*x for x in spectrum(f))
def influence(f):
    return sum((Q(sum(f[x]!=f[x^(1<<i)] for x in range(len(f))),len(f)) for i in range(len(f).bit_length()-1)),Q(0))
def inf(f,i):return Q(sum(f[x]!=f[x^(1<<i)] for x in range(len(f))),len(f))
def restrict(f,i,b):return tuple(y for x,y in enumerate(f) if (x>>i)&1==b)
def family(g):
    ans=[]
    for x in range(16*len(g)):
        s,w,u,v=((x>>i)&1 for i in range(4))
        A=(w and u and v) or (s and (u or v))
        ans.append(1+int(A)*(g[x>>4]-1))
    return tuple(ans)
def reserve(g):return ((1-spectrum(g)[0])*Q(7,8)+Q(5,8)*influence(g))/2
def product(p):
    from math import prod
    n=len(p).bit_length()-1
    m=[sum((v for x,v in enumerate(p) if (x>>i)&1),Q(0)) for i in range(n)]
    return tuple(prod(m[i] if (x>>i)&1 else 1-m[i] for i in range(n)) for x in range(len(p)))
def erase(p,i):
    out=[Q(0)]*(len(p)//2)
    for x,v in enumerate(p):out[(x&((1<<i)-1))|((x>>(i+1))<<i)]+=v
    return tuple(out)
def carry(P,Qref,children,i):
    p=erase(P,i);q=erase(Qref,i); refs=[];zs=[]
    for child in children:
        weights=[q[t]*(child[t]/(2*p[t]) if p[t] else Q(1,2)) for t in range(len(p))]
        z=sum(weights);check(z>0);zs.append(z);refs.append(tuple(v/z for v in weights))
    check(sum(zs)==1)
    return refs,zs
def erasure(f,i):
    p=law(f);q=erase(p,i);a=ent(p);return sub(a,ent(q))
def serial(x):
    if isinstance(x,Q):return str(x)
    if isinstance(x,(tuple,list)):return [serial(v) for v in x]
    if isinstance(x,dict):return {k:serial(v) for k,v in x.items()}
    return x
def record(g,certify_retirement=False):
    f=family(g);gs=[restrict(g,0,b) for b in (0,1)];fs=[restrict(f,4,b) for b in (0,1)]
    check(all(fs[b]==family(gs[b]) for b in (0,1)))
    P=law(f);Ps=[law(h) for h in fs];I=influence(f);Is=[influence(h) for h in fs]
    H=ent(P);Hs=[ent(p) for p in Ps]
    for h,p in [(f,P),*zip(fs,Ps)]:
        check(sum(p)==1);check(sum((t.bit_count()*v for t,v in enumerate(p)),Q(0))==influence(h))
    df=sub(H,avg(*Hs));dg=sub(ent(law(g)),avg(*(ent(law(h)) for h in gs)))
    U=reserve(g);Us=[reserve(h) for h in gs];release=U-sum(Us)/2
    check(release==Q(5,16)*inf(g,0))
    residual=sub(sub(df,mul(dg,Q(7,16))),point(release))
    Qroot=product(P); Qbs,zs=carry(P,Qroot,Ps,4)
    K=avg(*(kl(p,q) for p,q in zip(Ps,Qbs)))
    Rs=[product(p) for p in Ps];TC=avg(*(kl(p,r) for p,r in zip(Ps,Rs)))
    sigma=sub(TC,K)
    B_H=sub(avg(*(sub(point(4*i),h) for i,h in zip(Is,Hs))),point(sum(Us)/2))
    B_old=sub(B_H,K);B_new=sub(B_H,TC)
    check(sub(sub(B_old,sigma),B_new)[0]<=0<=sub(sub(B_old,sigma),B_new)[1])
    # Chain rule reconstructed as conditional pair divergence, including reference-only rows.
    E=ZERO;p=erase(P,4);q=erase(Qroot,4)
    for t,m in enumerate(p):
        x=(t&15)|((t>>4)<<5)
        if m:E=add(E,mul(kl((P[x]/m,P[x+16]/m),(Qroot[x]/q[t],Qroot[x+16]/q[t])),m))
    O=kl((Q(1,2),Q(1,2)),zs);A=kl(P,Qroot)
    chain=sub(A,add(E,add(O,K)));check(chain[0]<=0<=chain[1])
    out={'core':g,'core_children':gs,'P':P,'children_P':Ps,'I':I,'child_I':Is,'H':H,'child_H':Hs,'U':U,'child_U':Us,'release':release,'R':residual,'normalizers':zs,'K':K,'TC':TC,'sigma':sigma,'E':E,'net_reset':sub(sigma,E),'B_old':B_old,'B_new':B_new}
    if certify_retirement:
        check(all(influence(h)>0 for h in gs))
        separator=[]
        for b,h in enumerate(fs):
            B=erasure(h,0);d=inf(h,0);check(B[1]<4*d)
            leaves=[restrict(h,0,c) for c in (0,1)]
            leaflaws=[law(k) for k in leaves]
            # Carry actual child product reference R_b onward, without any extra reset.
            Lrefs,Lzs=carry(Ps[b],Rs[b],leaflaws,0)
            CE=[add(ent(p0),kl(p0,r0)) for p0,r0 in zip(leaflaws,Lrefs)]
            childCE=add(Hs[b],kl(Ps[b],Rs[b]))
            # Mean terminal CE is retained as an independent reported bill.
            terminalbank=sub(point(sum(4*influence(k) for k in leaves)/2),avg(*CE))
            sepdrop=sub(childCE,avg(*CE))
            ce_margin=sub(point(4*d),sepdrop)
            childbank=sub(point(4*Is[b]),childCE)
            check(ce_margin[1]<0) # erasure-good is not full-reference-good
            check(childbank[0]>0)
            telescope=sub(childbank,add(ce_margin,terminalbank))
            check(telescope[0]<=0<=telescope[1])
            # Only branch 1 is retired; branch 0 retains its entire U.
            held=Q(7,16) if b==0 else Q(0)
            after=sub(childbank,point(held));check(after[0]>0)
            separator.append({'B':B,'d':d,'good_margin':sub(point(4*d),B),'original_U':Us[b],'retired_U':Us[b]-held,'held_U':held,'leaf_P':leaflaws,'leaf_references':Lrefs,'normalizers':Lzs,'leaf_CE':CE,'leaf_I':[influence(k) for k in leaves],'terminal_bank':terminalbank,'CE_drop':sepdrop,'CE_price4_margin':ce_margin,'signed_continuation_bank':childbank,'after_held_U':after})
        retirement=sum(Us)/2
        paid=sub(add(B_new,point(retirement)),residual)
        out.update({'separator_continuation':separator,'retired_inherited_U':retirement,'post_retirement_margin':paid})
        check(residual[0]>Q(41,1000));check(B_new[1]<-Q(67,1000));check(sigma[0]>Q(3,50));check(sub(sigma,E)[1]<-Q(47,1000))
        check(paid[0]>0)
        single=Us[1]/2;held=Us[0]/2
        specific=sub(add(B_new,point(single)),residual)
        check(single==Q(17,64));check(held==Q(3,8));check(U==release+single+held)
        check(specific[0]>Q(5,32))
        check(separator[1]['signed_continuation_bank'][0]>Q(1,100))
        check(separator[0]['after_held_U'][0]>Q(11,16))
        # Full source transaction, including original root-product Q.
        sourcebank=sub(sub(point(4*I),add(H,A)),point(U))
        oldavg=avg(*(sub(sub(point(4*j),add(h,kl(p0,q0))),point(u)) for j,h,p0,q0,u in zip(Is,Hs,Ps,Qbs,Us)))
        source_drop=sub(add(H,A),avg(*(add(h,kl(p0,q0)) for h,p0,q0 in zip(Hs,Ps,Qbs))))
        identity=sub(sourcebank,add(oldavg,sub(sub(point(4*inf(f,4)),source_drop),point(release))))
        check(identity[0]<=0<=identity[1])
        out.update({'retirement_branch':1,'specific_retirement':single,'still_held_U_at_original_reach':held,'specific_payment_margin':specific,'source_full_bank':sourcebank,'source_CE_drop':source_drop})
        transfer=Q(27,64);held_final=Q(7,32)
        check(sum(x['retired_U'] for x in separator)/2==transfer)
        check(U==release+transfer+held_final)
        revised_source=add(sourcebank,point(transfer))
        revised_child=add(B_new,point(transfer))
        source_drop_new=sub(source_drop,sigma)
        actual_node_debit=sub(add(source_drop_new,point(release)),point(4*inf(f,4)))
        actual_margin=sub(revised_child,actual_node_debit)
        identity=sub(actual_margin,revised_source);check(identity[0]<=0<=identity[1])
        check(sourcebank[1]<-Q(21,50))
        check(revised_source[0]>Q(1,800))
        check(sub(revised_child,residual)[0]>Q(5,16))
        check(actual_node_debit[0]>Q(7,20))
        check(residual[1]<Q(9,200))
        out.update({'full_retirement':transfer,'remaining_U_mean':held_final,'effective_root_U':U-transfer,'revised_source_bank':revised_source,'revised_child_bank':revised_child,'full_actual_node_debit':actual_node_debit,'full_actual_payment_margin':actual_margin,'residual_only_margin_not_second_spend':sub(revised_child,residual)})
    return out

rows=[]
for name,g in [('code7',(-1,-1,-1,1,1,1,1,1)),('code1',(-1,1,1,1)),('dictator',(-1,1))]:
    row=record(g,name=='code7');rows.append(row)
    (ROOT/'out'/f'{name.upper()}.json').write_text(json.dumps(serial(row),indent=2)+'\n',encoding='utf-8')
result={'status':'PASS','checks':COUNT,'runtime_seconds':time.perf_counter()-START,'rows':3,'arithmetic':'direct character sums / Fraction / 32-term outward log bounds'}
(ROOT/'out'/'RESULT.json').write_text(json.dumps(result,indent=2)+'\n',encoding='utf-8')
print(json.dumps(result))
for row in rows:
    print('core',row['core'],'R',list(map(float,row['R'])),'B_new',list(map(float,row['B_new'])))
    if 'post_retirement_margin' in row:
        print('retirement',row['retired_inherited_U'],'margin',list(map(float,row['post_retirement_margin'])))
        print('separator margins',[list(map(float,x['good_margin'])) for x in row['separator_continuation']])
        print('terminal banks',[list(map(float,x['terminal_bank'])) for x in row['separator_continuation']])
