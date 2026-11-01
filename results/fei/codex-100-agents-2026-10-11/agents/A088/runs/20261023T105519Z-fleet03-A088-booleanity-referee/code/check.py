import ast,sys,json,time,hashlib
from pathlib import Path
from fractions import Fraction as F
R=Path(__file__).resolve().parents[1];OLD=R.parent/'20261023T070855Z-fleet03-A088-booleanity-referee';MODE=sys.argv[1] if len(sys.argv)>1 else 'pilot';START=time.perf_counter();COUNT=0
# Reuse only definitions from our own prior exact arithmetic, never its top-level jobs.
prior=OLD/'code'/'check.py';tree=ast.parse(prior.read_text(encoding='utf-8'))
names={'ck','exact','add','mul','sub','rounded','ln','log','weighted_log','enc','intersects','counts','state','fw','law','child','marginal','ce','inf'}
nodes=[n for n in tree.body if isinstance(n,(ast.Import,ast.ImportFrom)) or isinstance(n,ast.FunctionDef) and n.name in names]
exec(compile(ast.Module(body=nodes,type_ignores=[]),str(prior),'exec'),globals())
def state_w(m,t):
 A=F(1,1<<m);d=A*A;B=(1<<t)*A;alpha=A/(1<<t);v=1+2*d
 entries=[(B*B*(1-2*B*s)**2,B*B*(v-2*alpha*s),n) for s,n in counts(m-t)]
 ck(sum(p*n for p,q,n in entries)==sum(q*n for p,q,n in entries)==1,'post-w actual and inherited normalized')
 for p,q,n in entries:ck(p<=2*4**t*q,'post-w full likelihood bound')
 C=weighted_log([(p*n,1/q) for p,q,n in entries]);H=weighted_log([(p*n,1/p) for p,q,n in entries if p]);K=sub(C,H)
 return C,H,K
def original_block(m,t):
 # Direct grouped CE from parent and its two stopped exits; all inherited laws original.
 A=F(1,1<<m);d=A*A;u=1+d;B=(1<<t)*A;alpha=A/(1<<t);k=m-t
 C,H,K=state(m,t);Cn,Hn,Kn=state(m,t+1)
 K1=sub(exact(1),log(u));K2=weighted_log([(F(n,1<<(2*(k-1))),1/(u-alpha*s)) for s,n in counts(k-1)])
 C1=add(exact(2*k-2),K1);C2=add(exact(2*k-2),K2)
 drop=sub(C,add(mul(C1,F(1,2)),add(mul(C2,F(1,4)),mul(Cn,F(1,4)))))
 charge=mul(sub(drop,exact(3*(F(1,2)+2*B*B))),F(1,2*4**t))
 ck(charge[1]<0,'previous completed block negative credit retained')
 exitK=mul(add(mul(K1,F(1,2)),mul(K2,F(1,4))),F(1,2*4**t))
 return charge,exitK
def w_profile(m,h):
 A=F(1,1<<m);d=A*A;B=(1<<h)*A;alpha=A/(1<<h);u=1+d;v=1+2*d
 terms=[]
 for s,n in counts(m-h):
  terms.extend([(B*B*(1-B*s)**2*n,(v-2*alpha*s)/(u-2*alpha*s)),(B**4*n,(v-2*alpha*s)/d)])
 L=weighted_log(terms);q=mul(sub(L,exact(3*B*B)),F(1,2*4**h))
 ck(q[1]<d*(F(m)+F(1,3))<=F(7,48),'one global positive w earmark')
 Kw1=weighted_log([(F(n,1<<(2*(m-h))),1/(v-2*alpha*s)) for s,n in counts(m-h)])
 ck(Kw1[1]<1,'full clean w exit KL cap')
 return L,q,Kw1
def post_block(m,t):
 A=F(1,1<<m);d=A*A;v=1+2*d;B=(1<<t)*A;alpha=A/(1<<t);k=m-t
 terms0=[];terms1=[];M0=M1=F();norm0=norm1=F()
 for b in (0,1):
  for s,n in counts(k-1):
   q1=2*B*B*(v-(2*alpha*s if b==0 else 0));q2=4*B*B*(v-alpha*s)
   p1=16*B**4 if b else 4*B*B*(1-2*B*s)**2
   terms1.append((p1*n,q2/q1));M1+=p1*n*(q2/(2*q1)-1);norm1+=p1*n
   for a in (0,1):
    ss=s*(-1)**(a*b);p=B*B*(1-2*B*ss)**2;q=B*B*(v-2*alpha*ss)
    terms0.append((p*n,q1/q));M0+=p*n*(q1/(2*q)-1);norm0+=p*n
 ck(norm0==norm1==1,'both post-w query parents normalized')
 den=v*v-4*alpha*alpha
 m0=2*alpha*(alpha-2*B)/den
 m1=2*alpha*(-B*v+alpha*(1-4*B*B)+16*B**3*alpha*alpha/v)/den
 ck(M0==m0 and M1==m1,'post-w likelihood moments exact')
 ck(M0<0 and M1<0,'post-w two CE-drop moments strictly negative')
 L0=weighted_log(terms0);L1=weighted_log(terms1);ck(L0[1]<1 and L1[1]<1,'each post-w CE drop <1')
 Q=mul(sub(add(L0,mul(L1,F(1,2))),exact(3*(F(1,2)+4*B*B))),F(1,4*4**t))
 ck(Q[1]<-3*d,'same original reach post-w completed-block credit')
 K1=sub(exact(1),log(v));K2=weighted_log([(F(n,1<<(2*(k-1))),1/(v-alpha*s)) for s,n in counts(k-1)])
 ck(K1[1]<1 and K2[1]<F(1,2),'full post-w clean exit KL caps')
 Ke=mul(add(mul(K1,F(1,2)),mul(K2,F(1,4))),F(1,4*4**t))
 return L0,L1,Q,Ke
rows=[];blocks={};wp={};cases={}
for m in ([2] if MODE=='pilot' else range(2,21)):
 A=F(1,1<<m);d=A*A;v=1+2*d;preQ=exact(0);preK=exact(0)
 for h in range(m+1):
  if h:
   oq,ok=original_block(m,h-1);preQ=add(preQ,oq);preK=add(preK,ok)
  Lw,W,Kw=w_profile(m,h);wp[m,h]=(Lw,W,Kw)
  E=add(preQ,W);Kex=add(preK,mul(Kw,F(1,4*4**h)))
  for t in range(h,m+1):
   if t>h:
    if (m,t-1) not in blocks:blocks[m,t-1]=post_block(m,t-1)
    L0,L1,Q,Ke=blocks[m,t-1];E=add(E,Q);Kex=add(Kex,Ke)
   C,H,Kactive=state_w(m,t);Ktotal=add(Kex,mul(Kactive,F(1,4*4**t)))
   EH=add(E,Ktotal);J=F(1,3)-F(1,6*4**h)-F(1,6*4**t)+(F(t)+F(1,2))*d
   cap=F(5,12)+F(1,24*4**h)+F(1+12*t,24*4**t)
   ck(Ktotal[1]<cap<=F(19,32),'all stopped siblings and active KL under one global cap')
   ck(E[1]<F(7,48) and EH[1]<F(71,96),'whole original reserve payment')
   ck(J<F(1,2) and add(EH,exact(J))[1]<F(119,96),'old rate2 invoices retained')
   if t==m:ck(Kactive[1]<F(1,1<<80),'actual edited completion is a constant with zero full KL')
   cases[m,h,t]=(E,Ktotal,EH,J)
   rows.append({'m':m,'w_after':h,'completed_after_w':t,'E_Q3':enc(E),'full_terminal_KL':enc(Ktotal),'E_H3':enc(EH),'legacy_removed_influence':str(J)})

# Independent literal truth tables: original Q only, each stopping sibling retained.
literal=[]
def marginal_bit(q,j):
 out=[F() for _ in range(len(q)//2)]
 for x,a in enumerate(q):out[(x&((1<<j)-1))|((x>>(j+1))<<j)]+=a
 return out
def physical(v,j,b):return [a for x,a in enumerate(v) if ((x>>j)&1)==b]
def query(v,q,j,reach):
 p=law(v);a=physical(v,j,0);b=physical(v,j,1);pa,pb=law(a),law(b);qn=marginal_bit(q,j);pm=marginal_bit(p,j)
 ck(all(x in (-1,1) for x in v+a+b),'all actual Boolean query parent/children')
 ck(all((x+y)/2==z for x,y,z in zip(pa,pb,pm)),'both full actual child laws')
 I=F(sum(v[x]!=v[x^(1<<j)] for x in range(len(v))),len(v))
 L=sub(ce(p,q),mul(add(ce(pa,qn),ce(pb,qn)),F(1,2)))
 Q=mul(sub(L,exact(3*I)),reach);Kb=mul(sub(ce(pb,qn),ce(pb,pb)),reach/2)
 return a,qn,Q,Kb,I,L
for m in ([2] if MODE=='pilot' else range(2,6)):
 initial=[(-1)**sum(((x>>(2*j))&1)*((x>>(2*j+1))&1) for j in range(m))-2*(x==0) for x in range(1<<(2*m+1))];qinit=law(initial);d=F(1,4**m)
 for h in range(m+1):
  v=initial;q=qinit;E=exact(0);Ke=exact(0);J=F()
  for j in range(2*h):
   v,q,Q,Kb,I,L=query(v,q,0,F(1,2*(1<<j)));E=add(E,Q);Ke=add(Ke,Kb);J+=F(1,2*(1<<j))*I
  windex=2*(m-h);v,q,Q,Kb,I,L=query(v,q,windex,F(1,2*4**h));E=add(E,Q);Ke=add(Ke,Kb);J+=F(1,2*4**h)*I
  ck(I==4**h*d and intersects(L,wp[m,h][0]),'literal w profile/physical influence')
  for t in range(h,m+1):
   if t>h:
    for j in (0,1):
     v,q,Q,Kb,I,L=query(v,q,0,F(1,4*4**(t-1)*(1<<j)));E=add(E,Q);Ke=add(Ke,Kb);J+=F(1,4*4**(t-1)*(1<<j))*I
     ck(intersects(L,blocks[m,t-1][j]),'literal post-w query vs grouped CE')
   p=law(v);K=add(Ke,mul(sub(ce(p,q),ce(p,p)),F(1,4*4**t)));EQ,KK,EH,JJ=cases[m,h,t]
   ck(intersects(E,EQ) and intersects(K,KK) and J==JJ,'complete literal original reference account')
   literal.append([m,h,t])
out={'status':'PASS','mode':MODE,'checks':COUNT,'runtime_seconds':time.perf_counter()-START,'grouped_cuts':len(rows),'distinct_post_w_block_profiles':len(blocks),'literal_cuts':len(literal),'cuts':rows,'old_arithmetic_sha256':hashlib.sha256(prior.read_bytes()).hexdigest(),'arithmetic':'Exact rational probabilities/moments; positive28-term atanh with proved tail and outward2^-90 log endpoints'}
(R/'out').mkdir(exist_ok=True);(R/'out'/('PILOT.json' if MODE=='pilot' else 'CHECK.json')).write_text(json.dumps(out,indent=2)+'\n',encoding='utf-8')
print(json.dumps({k:out[k] for k in ['status','checks','runtime_seconds','grouped_cuts','distinct_post_w_block_profiles','literal_cuts']}))
