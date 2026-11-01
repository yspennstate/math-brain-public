import pathlib,json,time,math
ROOT=pathlib.Path(__file__).resolve().parent
def convergents(digits):
 p0,p1,q0,q1=0,1,1,0
 out=[]
 for a in digits:
  p0,p1=p1,a*p1+p0;q0,q1=q1,a*q1+q0
  out.append((p1,q1))
 return out
def test(name,spikes):
 digits=[0,1,2]
 for a in spikes:digits.extend([a,2])
 digits.extend([1000003,2,1000033])
 conv=convergents(digits);P,R=conv[-1]
 # q_{2m} occurs at index 2m, because index zero is the initial 0.
 towers=[(m,conv[2*m][0],conv[2*m][1],spikes[m-1],conv[2*m+2][1]) for m in range(1,len(spikes)+1)]
 N=min(towers[-1][-1],2000000)
 C=[0]*(N+1);s=w=w2=0;scat={};targets={0,N}
 for m,p,q,A,qn in towers:
  if q>N:continue
  L=(A//8)*q
  targets.update([q,min(L,N),min(qn,N)])
  targets.update(range(q,min(qn,N)+1,max(1,(min(qn,N)-q)//200)))
 for n in range(1,N+1):
  e=1 if 2*((n*P)%R)<R else -1
  s+=e;C[n]=s;w+=s;w2+=s*s
  if n in targets:scat[n]=n*w2-w*w
 results=[]
 for m,p,q,A,qn in towers:
  if q>N or A<32:continue
  K=min(A//8,N//q);L=K*q
  direction=1 if P*q-p*R>0 else -1
  failures=0
  for j in range(K):
   for r in range(1,q+1):
    if C[j*q+r]!=C[r]+j*direction:failures+=1
  assert failures==0,(name,m,'block repetition',failures)
  mean_num=sum(C[1:q+1]);square=sum(x*x for x in C[1:q+1])
  B_num=q*square-mean_num*mean_num
  assert 12*scat[L]*q*q==L*L*(12*B_num+q*q*(K*K-1)),(name,m,'variance identity')
  baseline=None
  if m>=2 and spikes[m-2]>=32:
   prev=spikes[m-2]
   assert 10000000*B_num>=prev*prev*q*q,(name,m,'baseline')
   baseline=B_num/(q*q)
  # Every selected scale must satisfy the stable-region bound with constant 1/16.
  for n in targets:
   if q<=n<=L:
    assert 256*(n*n+scat[n])*q*q>=n*n*(q*q+B_num+n*n),(name,m,n,'stable bound')
   if L<=n<=min(qn,N):
    assert 3072**2*(n*n+scat[n])>=n*n*A*A,(name,m,n,'tail bound')
  results.append(dict(m=m,q=q,A=A,next_even_q=qn,K=K,block_failures=failures,profile_variance=B_num/(q*q),baseline_checked=baseline is not None))
 # Exact reflection at phase zero.
 for y in range(1,min(N,10000)+1):
  ep=1 if 2*((y*P)%R)<R else -1
  em=1 if 2*((-y*P)%R)<R else -1
  assert ep==-em
 return dict(name=name,spikes=spikes,N=N,results=results)
def signed_boundary_checks():
 count=0
 for q in range(3,52,2):
  for p in range(1,q):
   if math.gcd(p,q)!=1:continue
   for A in [32,33,64]:
    for sign in [-1,1]:
     # delta = sign / (2*q*(A*q+1)); exact rational, safely within the lemma's margin.
     denom=2*q*(A*q+1);num=p*(denom//q)+sign
     word=[1 if 2*((r*num)%denom)<denom else -1 for r in range(1,q+1)]
     assert sum(word)==sign
     for j in range(A//8):
      for r in range(1,q+1):
       assert (1 if 2*(((j*q+r)*num)%denom)<denom else -1)==word[r-1]
     count+=1
 return count
start=time.monotonic()
res=[test('moderate_even',[32,34,36]),test('mixed_parity',[33,35,37]),test('nonmonotone_spikes',[128,32,33]),test('prior_gap',[3,17,513])]
out={'checks':res,'signed_boundary_cases':signed_boundary_checks(),'seconds':time.monotonic()-start,'note':'Exact integer coding of a long rational approximant; finite tests only. Infinite-angle proof is in ATTEMPT.md.'}
(ROOT/'finite_checks.json').write_text(json.dumps(out,indent=2),encoding='utf8')
print(json.dumps(out,indent=2));print('ALL_EXACT_FINITE_CHECKS_PASS')
