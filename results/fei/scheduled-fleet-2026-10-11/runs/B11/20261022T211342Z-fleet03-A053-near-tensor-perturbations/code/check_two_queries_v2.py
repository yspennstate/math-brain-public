from pathlib import Path
from fractions import Fraction as F
from functools import lru_cache
from itertools import combinations
from datetime import datetime,timezone
import json,hashlib,time,sys
RUN=Path(__file__).resolve().parents[1]; AGENT=RUN.parents[1]; BASE=Path(r'~')
def save(name,obj):
 p=RUN/name;p.parent.mkdir(parents=True,exist_ok=True);p.write_text(json.dumps(obj,indent=2,ensure_ascii=False)+'\n',encoding='utf-8')
def write(name,text):(RUN/name).write_text(text.strip()+'\n',encoding='utf-8')
prior=AGENT/'runs/20261014T052310Z-fleet05-A053-near-tensor-perturbations'
(RUN/'code/arithmetic.py').write_bytes((prior/'code/inherited_arithmetic.py').read_bytes())
import arithmetic as lib
from arithmetic import fwht,infs,coded_truth
sources=[]
def readsource(p,encoding='utf-8'):
 data=p.read_bytes();s=data.decode(encoding);sources.append({'path':str(p),'sha256':hashlib.sha256(data).hexdigest(),'bytes':len(data),'encoding':encoding});return s
for name in ['PACKING_CRITICAL_EXCLUSION.md','REPORT.md','CLAIMS.json'] :readsource(prior/name)
r=BASE/'mop_fei100/reports/fei-2026-10-11'
for name in ['EXECUTION_PROTOCOL.json','README.md','CURRENT_STATUS.md','CLAIM_REGISTRY.json','OBSTRUCTION_REGISTRY.json','PACKET_STATUS.json','STREAM_NEXT_ACTIONS.json','FEI_100_agent_research_plan.tex']:readsource(r/name)
proto=json.loads((r/'EXECUTION_PROTOCOL.json').read_text(encoding='utf-8'))
push=BASE/'mop_fei100/research_pushes/2026-10-11-full-fei-100-agents'
for name in ['CAMPAIGN.md','CLAIMS.md','COUNTEREXAMPLES.md','SEED_LEMMAS.md','NATIVE_MAPPING.md']:readsource(push/name)
for p in (push/'sources').glob('*.md'):readsource(p)
locators={}
for p in (BASE/'brain_workers/FEI100_20261011/context').glob('*.txt'):
 try:s=readsource(p)
 except UnicodeDecodeError:s=readsource(p,'cp1252')
 lines=s.splitlines();locators[p.name]={'lines':len(lines),'locators':[{'line':i+1,'text':' '.join(lines[i:i+3])[:500]} for i,l in enumerate(lines) if any(t in l.lower() for t in ['theorem 1.1','proposition 8.6','block restriction','singularity'])][:12]}
readsource(BASE/'brain_workers/FEI100_20261011/BOARD.md');readsource(BASE/'brain_workers/FEI100_20261011/claude/B11/STREAM_NOTES.md')
peer=BASE/'brain_workers/FEI100_20261011/agents/A052/runs/20261021T222218Z-fleet03-A052-critical-source-structure'
readsource(peer/'REPORT.md');readsource(peer/'PATH_CODE_PROOF.md')
readsource(BASE/'brain_workers/FEI100_20261011/agents/A054/runs/20261014T055856Z-fleet05-A054-connectedness-alternatives/REPORT.md')
save('out/SOURCE_RECEIPTS.json',sources);save('out/MANUSCRIPT_LOCATORS.json',locators)
PROOF=r'''
# Retaining ancestor packing pays the second physical query

All cubes are uniform; all functions are Boolean signs; entropy uses bits. Let n>=3, p=2^(-n), let F have Fourier support of minimum Hamming distance at least 3 (a singleton has infinite distance), and let G differ from F at exactly one physical vertex v. Put s=|supp Fhat|. Choose a coordinate i of maximum influence in G. In each actual child G_b=G|_(x_i=b), choose a remaining coordinate j_b of maximum influence in that child. T is this depth-two physical tree and its four leaves have their actual probability 1/4. Neither j_b nor a leaf reference is identified across different branches.

Write Q=Inf_i(G)+(Inf_(j_0)(G_0)+Inf_(j_1)(G_1))/2. This is influence consumed, not a renewed child budget. Then

    H(G)-E_T H(G_leaf) < (71/2)p,
    Q >= 4p,
    H(G)-E_T H(G_leaf)-9Q < -p/2.                 (1)

Consequently, for every real K>=9 and D_K(h)=H(h)-K I(h),

    D_K(G)-E_T D_K(G_leaf) < -p/2,
    E_T D_K(G_leaf) > D_K(G)+p/2.                (2)

These are paid-tree and actual-terminal statements. They do not prove FEI(9) for this neighborhood: an unclosed terminal can retain arbitrary-core hardness.

## 1. Inherited support, coefficients and exact rows

Radius-one packing in the ORIGINAL spectrum gives s(n+1)<=2^n. Projection of that support through a single physical query is injective, because two indices with the same projection differ in at most one bit. No coefficients merge. Each seed child F_b has exactly s nonzero coefficients with the same magnitudes, and its support has distance at least 2. A further singleton projection is again injective; hence H(F_b)=H(F_b restricted at j) for both signs and every remaining j. The unedited child therefore has exactly zero second-query entropy decrement.

Exactly one first-level child contains the physical edit. This child is a one-point edit of F_b on m=n-1 bits, with point mass p'=2p. It retains the ORIGINAL count bound s<=1/((n+1)p), which is stronger than replacing s by a generic distance-two packing estimate.

Every distance-at-least-two Boolean spectrum on m>=2 bits has a zero coefficient. All its integer Walsh sums are congruent modulo 4 to minus twice its negative truth count: for nonempty characters the Walsh sum of the constant vector is zero, and reducing the negative-vertex character sum modulo 2 removes the character signs. A zero Walsh coefficient therefore makes every Walsh sum a multiple of 4. Every nonzero coefficient has magnitude at least 4p'. Editing one point changes every coefficient by magnitude 2p'. In each singleton Fourier row the old anchor thus remains at least as large as its newly created partner. Ties cause no problem.

## 2. A row bound with the original s retained

Let U on m>=2 bits have support distance>=2 and exactly s coefficients. Let V be a one-point edit, q=2^(-m). For a singleton query there are s occupied old rows and 2^(m-1)-s empty old rows. The edit amplitude is 2q. Every empty row has mass 8q^2 and contributes twice its mass to the actual entropy decrement. Their total contribution is 8q-16s q^2 <=8q.

The occupied rows have total off-anchor squared mass b=4s q^2. If their total mass is A<=1, their conditional spectral entropy is at most A h2(b/A)<=b log2(1/b)+b/ln2, with zero terms defined by continuity. The occupied physical-channel entropy is at most (2/ln2)b. This is the two-point log-Sobolev bound, applied separately to each row and recentered on its larger coefficient. Thus, whenever b<=b0<=1,

    L_j(V) <= 8q + b0[log2(1/b0)+3/ln2].       (3)

The replacement uses that t[log2(1/t)+3/ln2] is increasing on (0,1], since its derivative is log2(1/t)+2/ln2>0. No lower bound on a row's total mass or a selected influence is used. This is a subnormalized occupied-row calculation; the newly created rows are retained separately.

For completeness the channel bound follows from Ent(w^2)<=(w0-w1)^2/2 in natural units. After normalizing w0^2+w1^2=2, its comparison function has derivative u/sqrt(1-u^2)-atanh(u)>=0 for 0<=u<1; differentiating this last expression gives (1-u^2)^(-3/2)-(1-u^2)^(-1)>=0. Absolute values only reduce the right side. Applying to w=(a+b,a-b), and exchanging a,b by multiplying the queried character, gives channel <=2 min(a^2,b^2)/ln2. Endpoints follow by continuity. The exact physical row decrement is spectral conditional entropy plus this channel, so it includes both actual child signs.

## 3. Uniform constants through the first query

For the original root take q=p and b0=4p/(n+1). Equation (3) gives

    L_i(G) <=8p+(4p/(n+1))[n+log2(n+1)-2+3/ln2]
           <(31/2)p.                              (4)

Indeed ln2>2/3 (the first positive term 2/3 in its atanh series), while log2(n+1)<=(n+1)/2 for integer n>=3. Equality holds in the latter at n=3; its induction uses (n+2)/(n+1)<=5/4<sqrt(2). The resulting upper coefficient is 14+6/(n+1)<=31/2. The strict logarithm inequality makes (4) strict.

For the edited child take q=2p and b0=16p/(n+1). This b0 is at most 1/2 for n>=3. The ORIGINAL support count gives b=4s(2p)^2<=b0. Now (3) yields, for EVERY remaining coordinate j,

    L_j(G_edited) <=16p+(16p/(n+1))[n+log2(n+1)-4+3/ln2]
                  <40p.                           (5)

The bracket is less than n+log2(n+1)+1/2, hence less than (3/2)(n+1). The other child has second-query decrement zero by Section 1. Averaging both complete children gives

    L_tree = L_i(G)+(L_(j_0)(G_0)+L_(j_1)(G_1))/2
           <(31/2)p+20p=(71/2)p.                  (6)

Only half the cost in (5) is charged. It is not a statement that each second query is separately paid from its child influence.

## 4. One influence owner and all actual terminals

Use the previously independently reconstructed A053 packing lemma I(G)>=2np (PACKING_CRITICAL_EXCLUSION, Section 3, accepted analytically by A054). Its boundary cases n=3 and constant seeds are included there. For clarity its nonconstant n>=4 proof bounds both physical sign classes by indicator Fourier uncertainty using support size<=s+1. After editing, each sign class has probability at least a=(3n-1)p/4<=11/64. Boolean Poincare gives I(G)>=4a(1-a)>2np. The constant case is I(G)=2np; at n=3 the seed must be a signed character and the direct influence formula gives the same bound.

Set I=I(G), a=Inf_i(G), and b=(Inf_(j_0)(G_0)+Inf_(j_1)(G_1))/2. Greedy choice and the physical influence identity give

    a>=I/n,
    b>=(I-a)/(n-1),
    Q=a+b>=2I/n>=4p.                              (7)

For the middle implication, (n-1)b>=I-a and na>=I; multiplying and adding yields n(n-1)Q>=2(n-1)I. All canceled denominators are positive since n>=3. Zero child influences are allowed; any maximizing index is admissible.

The exact physical telescope is I(G)-E_T I(G_leaf)=Q, with the four actual leaves and their original weights. Combining this with (6)--(7) proves (1)--(2). In particular if the root violates K>=9, at least one ACTUAL terminal has deficit strictly greater than D_K(G)+p/2. A least-dimensional violation cannot have this structure. No component, normalized row, recentered phase or arbitrary reference has been assigned an actual-child reserve.

## 5. Boundary of the argument

Two queries can project the original distance-three support to distance one. At that point a third query can merge two old coefficients. Equations (3)--(5) do not apply: the old-anchor uniqueness hypothesis fails. Paying that coherent signed interface, including all actual terminal deficits and earlier booked debits, is the first unsupported continuation. Generic affine minimality cannot replace actual child eligibility, as A052's path-code construction shows. This theorem buys exactly one more physical level from the ancestor packing and one influence owner; it makes no universal FEI claim.
'''
write('TWO_QUERY_PROOF.md',PROOF)
(AGENT/'STATUS.md').write_text('STATE: A053 stage17 two-query proof saved; exact verification running; full FEI OPEN.\nNEXT: Verify inherited support count, both child costs, greedy debit and complete terminal telescope; then attack distance-one signed merging.\n',encoding='utf-8')
START=time.perf_counter();lib.START=START;count=0

def ck(value):
 global count
 count+=1
 if not value:raise AssertionError(count)
 if time.perf_counter()-START>55:raise RuntimeError('frozen 55s mathematical pilot guard')

def restrict(t,i,b):return tuple(v for x,v in enumerate(t) if (x>>i&1)==b)
@lru_cache(None)
def spec(t):return tuple(fwht(t))
@lru_cache(None)
def influence(t):return tuple(infs(t))
@lru_cache(None)
def factors(a):
 result=[];d=2
 while d*d<=a:
  c=0
  while a%d==0:a//=d;c+=1
  if c:result.append((d,c))
  d+=1
 if a>1:result.append((a,1))
 return tuple(result)

def clean(v):return {k:x for k,x in v.items() if x}
def plus(a,b,scale=F(1)):
 v=dict(a)
 for k,x in b.items():v[k]=v.get(k,F(0))+scale*x
 return clean(v)
def scale(v,c):return clean({k:x*c for k,x in v.items()})
@lru_cache(None)
def Hvec(t):
 N=len(t);n=N.bit_length()-1;v={2:F(2*n)}
 for w in spec(t):
  if w:
   for prime,e in factors(abs(w)):v[prime]=v.get(prime,F(0))-F(2*w*w*e,N*N)
 return clean(v)
def bounds(v):
 lo=hi=F(0)
 for k,c in v.items():
  a,b=lib.log2(F(k))
  if c>=0:lo+=c*a;hi+=c*b
  else:lo+=c*b;hi+=c*a
 return lo,hi

def L(t,i):return plus(plus(Hvec(t),Hvec(restrict(t,i,0)),-F(1,2)),Hvec(restrict(t,i,1)),-F(1,2))
def D(t,K=9):return plus(Hvec(t),{2:sum(influence(t))},-F(K))

rows=[];roots=[];first_cases=second_cases=greedy_trees=0
fixtures=[]
for sign in [-1,1]:
 for s in range(8):fixtures.append(('character3_'+str(sign)+'_'+str(s),tuple(sign*(-1 if (x&s).bit_count()%2 else 1) for x in range(8))))
for code in range(16):fixtures.append(('coded2_'+str(code),tuple(coded_truth([-1 if code>>x&1 else 1 for x in range(4)]))))
fixtures.append(('coded_PD3',tuple(coded_truth([-1]+[1]*7))))
for name,f in fixtures:
 N=len(f);n=N.bit_length()-1;p=F(1,N);supp=[i for i,w in enumerate(spec(f)) if w];s=len(supp)
 ck(s*(n+1)<=N)
 for x,y in combinations(supp,2):ck((x^y).bit_count()>=3)
 ck(sum(w*w for w in spec(f))==N*N)
 g=list(f);g[0]*=-1;g=tuple(g);I=sum(influence(g));ck(I>=2*n*p)
 # Independent direct Walsh summation for each root (not used by the FWHT path).
 direct=tuple(sum(v*(-1 if (x&t).bit_count()%2 else 1) for x,v in enumerate(g)) for t in range(N))
 ck(direct==spec(g))
 first=[]
 for i in range(n):
  first_cases+=1;rootL=L(g,i);ck(bounds(rootL)[1]<F(31,2)*p)
  projected=set(t&((1<<i)-1)|((t>>(i+1))<<i) for t in supp);ck(len(projected)==s)
  childrecords=[]
  for b in [0,1]:
   oldchild=restrict(f,i,b);child=restrict(g,i,b);cs=[t for t,w in enumerate(spec(oldchild)) if w]
   ck(set(cs)==projected);ck(len(cs)==s)
   for x,y in combinations(cs,2):ck((x^y).bit_count()>=2)
   ck(Hvec(oldchild)==Hvec(f));ck(all(w%4==0 for w in spec(oldchild)))
   iv=influence(child);j=max(range(n-1),key=lambda k:iv[k]);secondrecords=[]
   for k in range(n-1):
    second_cases+=1;lv=L(child,k);ck(L(oldchild,k)=={})
    if b==1:ck(lv=={})
    else:
     ck(bounds(lv)[1]<40*p)
     q=2*p;minor=F(0);empty_mass=F(0);occupied=0
     old=spec(oldchild);new=spec(child);Nc=len(child)
     for t in range(Nc):
      if t>>k&1:continue
      u=t|1<<k;ck(not(old[t] and old[u]));ck(min(new[t]**2,new[u]**2)==4)
      if old[t] or old[u]:minor+=F(4,Nc*Nc);occupied+=1
      else:empty_mass+=F(new[t]**2+new[u]**2,Nc*Nc)
     ck(occupied==s);ck(minor==4*s*q*q);ck(minor<=16*p/(n+1));ck(empty_mass==4*q-8*s*q*q)
    secondrecords.append({'j':k,'L_interval':[str(x) for x in bounds(lv)],'influence':str(iv[k])})
   childrecords.append({'b':b,'greedy_j':j,'influence':str(iv[j]),'second_queries':secondrecords})
  if influence(g)[i]==max(influence(g)):
   greedy_trees+=1;leaves=[];treeL=dict(Hvec(g));Q=influence(g)[i]
   for b in [0,1]:
    c=restrict(g,i,b);j=childrecords[b]['greedy_j'];Q+=influence(c)[j]/2
    for z in [0,1]:
     leaf=restrict(c,j,z);leaves.append(leaf);treeL=plus(treeL,Hvec(leaf),-F(1,4))
   ck(Q>=2*I/n);ck(Q>=4*p);ck(I-sum(sum(influence(t)) for t in leaves)/4==Q)
   ck(bounds(treeL)[1]<F(71,2)*p)
   bank=plus(treeL,{2:Q},-F(9));ck(bounds(bank)[1]<-p/2)
   terminal_bank=dict(D(g))
   for leaf in leaves:terminal_bank=plus(terminal_bank,D(leaf),-F(1,4))
   ck(bank==terminal_bank)
   first.append({'i':i,'Q':str(Q),'entropy_drop_interval':[str(x) for x in bounds(treeL)],'D9_root_minus_mean_complete_terminal_interval':[str(x) for x in bounds(bank)],'required_margin':str(p/2),'children':childrecords})
 rows.append({'name':name,'n':n,'support_count':s,'I_root':str(I),'greedy_trees':first})
 save('out/CASES.json',{'status':'IN_PROGRESS','completed_roots':len(rows),'cases':rows})
for n in range(3,41):
 p=F(1,1<<n);ell=lib.log2(F(n+1))[1];c=3/lib.LN2[0]
 root_bound=8*p+4*p/(n+1)*(n+ell-2+c)
 child_bound=16*p+16*p/(n+1)*(n+ell-4+c)
 ck(root_bound<F(31,2)*p);ck(child_bound<40*p);ck(16*p/(n+1)<=F(1,2));ck((n+1)**2<=1<<(n+1))
 roots.append({'n':n,'root_bound':str(root_bound),'edited_child_bound':str(child_bound)})
summary={'status':'PASS','assertions':count,'Boolean_roots':len(fixtures),'first_queries':first_cases,'second_queries_in_both_children':second_cases,'greedy_two_level_trees':greedy_trees,'scalar_boundaries':len(roots),'runtime_seconds':time.perf_counter()-START,'arithmetic':'integer FWHT independently reproduced by direct Walsh sums; Fraction prime-log identities; rational atanh24 sign intervals','helper_sha256':hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),'arithmetic_sha256':hashlib.sha256((RUN/'code/arithmetic.py').read_bytes()).hexdigest(),'peak_memory':'not measured; frozen estimate 100MB','source_finite_counts_adopted':False}
save('out/CASES.json',{'status':'PASS','cases':rows});save('out/SCALAR_BOUNDARIES.json',roots);save('out/EXACT_CHECK.json',summary)
print(json.dumps(summary,indent=2))
