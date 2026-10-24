from fractions import Fraction as Q
from collections import defaultdict
from pathlib import Path
import json, hashlib, time

OUT=Path(__file__).resolve().parents[1]/'out'
start=time.perf_counter(); checks=0
def check(b):
    global checks
    assert b
    checks+=1
def fwht(v):
    a=list(v); h=1
    while h<len(a):
        for i in range(0,len(a),2*h):
            for j in range(i,i+h):
                x,y=a[j],a[j+h];a[j],a[j+h]=x+y,x-y
        h*=2
    return a
def core(x):
    z0,z1,z2=(x>>i&1 for i in range(3));u=x>>3
    neg=(u==0 and (z2==0 or z0*z1==1)) or (u==1 and z1*z2==1)
    return 1-2*int(neg)
def factors(n):
    ans={}; p=2
    while p*p<=n:
        while n%p==0:ans[p]=ans.get(p,0)+1;n//=p
        p+=1
    if n>1:ans[n]=ans.get(n,0)+1
    return ans
def entropy(prob):
    v=defaultdict(Q)
    for p in prob.values():
        if p:
            for prime,e in factors(p.denominator).items():v[prime]+=p*e
            for prime,e in factors(p.numerator).items():v[prime]-=p*e
    return {a:b for a,b in v.items() if b}
def combine(*parts):
    v=defaultdict(Q)
    for weight,d in parts:
        for a,b in d.items():v[a]+=weight*b
    return {a:b for a,b in v.items() if b}
def marginal(joint,select):
    d=defaultdict(Q)
    for key,p in joint.items():d[select(key)]+=p
    return dict(d)
def ln_bounds(x,N=12):
    x=Q(x);check(x>=1)
    z=(x-1)/(x+1)
    low=2*sum((z**(2*j+1)/Q(2*j+1) for j in range(N)),Q(0))
    high=low+2*z**(2*N+1)/Q(2*N+1)/(1-z*z)
    return low,high
def log2_bounds(n):
    k=n.bit_length()-1
    lo,hi=ln_bounds(Q(n,2**k),16); a,b=ln_bounds(2,16)
    return k+lo/b,k+hi/a
def interval(v):
    lo=hi=Q(0)
    for a,b in v.items():
        x,y=log2_bounds(a)
        lo+=b*(x if b>=0 else y);hi+=b*(y if b>=0 else x)
    return [str(lo),str(hi)]
def vec(v):return {str(a):str(b) for a,b in sorted(v.items())}

truth=[core(x) for x in range(512)]
check(truth.count(-1)==7)
walsh=fwht(truth); spectrum={s:Q(a*a,512**2) for s,a in enumerate(walsh) if a}
check(sum(spectrum.values())==1)
edges=[sum(truth[x]!=truth[x^(1<<i)] for x in range(512) if not x>>i&1) for i in range(9)]
check(edges==[1,3,5,5,7,7,7,7,7])
check(sum(Q(s.bit_count())*p for s,p in spectrum.items())==Q(49,256))
full=[truth[x&511]*(-1 if (x>>9).bit_count()%2 else 1) for x in range(1<<17)]
fullpath=OUT/'truth_table.txt'
fullpath.write_text(''.join('1\n' if a==1 else '-1\n' for a in full),encoding='ascii')
fw=fwht(full)
check(all(a==0 for s,a in enumerate(fw) if s>>9!=255))
check(all(fw[s|(255<<9)]==256*walsh[s] for s in range(512)))
full_edges=[sum(full[x]!=full[x^(1<<i)] for x in range(1<<17) if not x>>i&1) for i in range(17)]
check(full_edges==[e*256 for e in edges]+[65536]*8)
del full,fw

# Walsh numerators at each physical prefix, indexed by ambient core labels.
node={}; essential={}
for depth in range(4):
    for b in range(1<<depth):
        t=[truth[b|(a<<depth)] for a in range(1<<(9-depth))]
        coeff=fwht(t);den=len(t)
        node[depth,b]={s<<depth:Q(a,den) for s,a in enumerate(coeff) if a}
        if depth<3:
            e=sum(t[a]!=t[a^1] for a in range(0,len(t),2))
            check(e>0);essential[depth,b]=Q(e,len(t)//2)
        check(sum(a*a for a in node[depth,b].values())==1)

# Actual coherent root-to-prefix lift; the current set is the root set projected.
joint={(s,0):p for s,p in spectrum.items()}
for depth in range(3):
    nxt=defaultdict(Q)
    for (s,b),p in joint.items():
        parent=node[depth,b]; current=s&~((1<<depth)-1);T=current&~(1<<depth)
        q=parent.get(T,Q(0))**2+parent.get(T|(1<<depth),Q(0))**2
        check(q>0)
        probs=[]
        for outcome in (0,1):
            bb=b|(outcome<<depth)
            prob=node[depth+1,bb].get(T,Q(0))**2/(2*q)
            probs.append(prob)
            if prob:nxt[s,bb]+=p*prob
        check(sum(probs)==1)
    joint=dict(nxt)
    for b in range(1<<(depth+1)):
        d=marginal(joint,lambda key: (key[1],key[0]&~((1<<(depth+1))-1)))
        for T,a in node[depth+1,b].items():check(d.get((b,T),0)==a*a/Q(1<<(depth+1)))
        check(sum(p for (s,bb),p in joint.items() if bb==b)==Q(1,1<<(depth+1)))

def final_joint(adaptive):
    result={}
    for (s,b),p in joint.items():
        label=b if adaptive else 0
        W=(s&~7)|((255^(1<<label))<<9)
        for c in (0,1):result[s,b|(c<<3),W]=p/2
    return result
J=final_joint(True);Jfix=final_joint(False)
check(sum(J.values())==1)
hs=entropy(spectrum);hp=entropy(marginal(J,lambda x:x[1]));hw=entropy(marginal(J,lambda x:x[2]))
hsp=entropy(marginal(J,lambda x:x[:2]));hsw=entropy(marginal(J,lambda x:(x[0],x[2])))
hwp=entropy(marginal(J,lambda x:(x[2],x[1])))
jroot=combine((1,hs),(1,hp),(-1,hsp));jW=combine((1,hw),(1,hp),(-1,hwp))
inj=combine((1,hsw),(-1,hs))
check(hp=={2:Q(4)});check(jW=={2:Q(3)})
check(combine((1,inj),(1,jroot))=={2:Q(3)})
check(combine((1,hwp),(-1,hw))=={2:Q(1)})
check(combine((1,entropy(marginal(Jfix,lambda x:(x[0],x[2])))),(-1,hs))=={})
check(all(((255^(w>>9)).bit_length()-1)==(pi&7) for s,pi,w in J))

terminalH={};terminalI=Q(0)
for b in range(8):
    d={s:a*a for s,a in node[3,b].items()}
    terminalH=combine((1,terminalH),(Q(1,8),entropy(d)))
    terminalI+=sum(Q(s.bit_count())*p for s,p in d.items())/8
    # Every leaf has seven parity coordinates: mean zero, all last queries essential.
    check(255^(1<<b)!=0)
check(terminalI==Q(5,32))
I=8+Q(49,256);Ileaf=7+terminalI;R=I-Ileaf
check(R==Q(265,256))
check(sum(v/Q(1<<depth) for (depth,b),v in essential.items())+1==R)
lnlo,lnhi=ln_bounds(2,3)
check(lnlo>Q(265,384))
check(lnhi<Q(139,200))
check(Q(3,2)*lnlo-R>0)
check(Q(3,2)*lnhi<Q(135,128))
# An exact rational positive lower bound in bits, not just a decimal.
margin=Q(3,2)-R/lnlo
check(margin>Q(1,256))
result={
 'helper_version':'A049-shared-core-v1','n':17,'core_negative_assignments':[x for x,a in enumerate(truth) if a==-1],
 'truth_table_order':'line x+1 is F at integer x; LSB first: z0,z1,z2,u0,...,u5,y0,...,y7; cube sign coordinate is (-1)^bit',
 'truth_table_sha256':hashlib.sha256(fullpath.read_bytes()).hexdigest(),
 'core_edge_counts':edges,'full_edge_counts':full_edges,
 'essential_node_influences':{f'{d}:{b}':str(a) for (d,b),a in essential.items()},
 'I_root':str(I),'I_terminal_mean':str(Ileaf),'removed_influence':str(R),
 'H_root_prime_log_vector':vec(hs),'H_terminal_mean_prime_log_vector':vec(terminalH),
 'I_S0_Pi_prime_log_vector':vec(jroot),'injection_prime_log_vector':vec(inj),
 'I_W_Pi_bits':'3','H_Pi_given_W_bits':'1','H_Pi_given_Y_bits':'4','output_information_bits':'0',
 'conversion_bits':'3/2','ln2_rational_bounds':[str(lnlo),str(lnhi)],
 'conversion_minus_budget_lower_bits':str(margin),
 'injection_interval_bits':interval(inj),'root_information_interval_bits':interval(jroot),
 'fixed_label_injection_bits':'0','joint_nonzero_entries':len(J),
 'assertions':checks,'runtime_seconds':time.perf_counter()-start,
 'minimality_scope':'all uniform k-bit Boolean cores, fixed r distinct prefix queries essential on every reached node, parity on 2^r coordinates, one injectively prefix-indexed parity query; witness is actual ambient terminal set; strict conversion > removed influence / ln(2)',
 'global_minimality_claim':False,'FEI_status':'OPEN'
}
(OUT/'certificate.json').write_text(json.dumps(result,indent=2)+'\n',encoding='utf-8')
(OUT/'core_truth_table.json').write_text(json.dumps(truth)+'\n',encoding='utf-8')
print(json.dumps({k:result[k] for k in ('n','removed_influence','assertions','runtime_seconds','conversion_minus_budget_lower_bits','truth_table_sha256')},indent=2))
