import itertools,math,json,pathlib,time
R=pathlib.Path(__file__).resolve().parent
start=time.monotonic()
def realizer_tree(pi):
 n=len(pi)
 intervals=[]
 for i in range(n):
  lo=hi=pi[i]
  for j in range(i,n):
   lo=min(lo,pi[j]);hi=max(hi,pi[j])
   if hi-lo==j-i:intervals.append((i,j+1))
 strong=[A for A in intervals if not any(max(A[0],B[0])<min(A[1],B[1]) and not (A[0]<=B[0] and B[1]<=A[1]) and not (B[0]<=A[0] and A[1]<=B[1]) for B in intervals)]
 def rec(a,b):
  if b-a==1:return 1
  proper=[I for I in strong if a<=I[0] and I[1]<=b and I!=(a,b)]
  kids=sorted(I for I in proper if not any(J!=I and J[0]<=I[0] and I[1]<=J[1] for J in proper))
  assert kids[0][0]==a and kids[-1][1]==b and all(x[1]==y[0] for x,y in zip(kids,kids[1:]))
  ranks=[min(pi[i:j]) for i,j in kids];k=len(kids)
  if ranks==sorted(ranks):factor=1
  elif ranks==sorted(ranks,reverse=True):factor=math.factorial(k)
  else:
   assert k>=4
   factor=2
  return factor*math.prod(rec(i,j) for i,j in kids)
 return rec(0,n)
def brute_r(pi):
 n=len(pi);total=0
 for sigma in itertools.permutations(range(n)):
  # sigma is a vector of ranks in first realizer.
  indegrees=[0]*n;ok=True
  for i in range(n):
   for j in range(i+1,n):
    comparable=pi[i]<pi[j]
    if comparable:
     if sigma[i]>sigma[j]:ok=False;break
     forward=True
    else:forward=sigma[i]>sigma[j]
    indegrees[j if forward else i]+=1
   if not ok:break
  if ok and sorted(indegrees)==list(range(n)):total+=1
 return total
results=[]
for n in range(1,10):
 if time.monotonic()-start>120:break
 H=0;maximum=0;complete=True
 for index,pi in enumerate(itertools.permutations(range(n))):
  if index%256==0 and time.monotonic()-start>120:
   complete=False;break
  r=realizer_tree(pi);H+=r;maximum=max(maximum,r)
  if n<=5:assert r==brute_r(pi),(pi,r,brute_r(pi))
 if not complete:
  print('Time budget exhausted during n=',n,'; incomplete total discarded',flush=True);break
 rec={'n':n,'H_by_substitution_tree':H,'R_H_over_factorial':H/math.factorial(n),'beta_estimate':(H/math.factorial(n))**(1/n),'maximum_realizers':maximum,'brute_individual_checked':n<=5,'elapsed':time.monotonic()-start}
 results.append(rec);print(json.dumps(rec),flush=True)
 (R/'substitution_check.json').write_text(json.dumps(results,indent=2),encoding='utf8')
