import math,time,json,pathlib
R=pathlib.Path(__file__).resolve().parent
start=time.monotonic();states=[((),(),())];results=[]
for n in range(1,9):
 if time.monotonic()-start>180 or len(states)>200000:
  break
 new=[];full=(1<<(n-1))-1
 for state in states:
  masks=[]
  for order in state:
   mm=[0];mask=0
   for a in order:mask|=1<<(a-1);mm.append(mask)
   masks.append(mm)
  third={mask:k for k,mask in enumerate(masks[2])}
  for a,A in enumerate(masks[0]):
   for b,B in enumerate(masks[1]):
    if A&B:continue
    c=third.get(full^(A|B))
    if c is None:continue
    child=tuple(order[:cut]+(n,)+order[cut:] for order,cut in zip(state,(a,b,c)))
    new.append(child)
    if len(new)>1000000:
     print('cap exceeded before completing n',n);break
   else:continue
   break
  else:continue
  break
 else:
  states=new
  assert len(set(states))==len(states)
  H=len(states);f=math.factorial(n)
  rec={'n':n,'H':H,'collision_numerator':H,'collision_denominator':f**3,'R_H_over_factorial':H/f,'beta_estimate':(H/f)**(1/n),'elapsed':time.monotonic()-start}
  # Parent counts by deletion give each fixed-first extension multiplicity.
  results.append(rec);print(json.dumps(rec),flush=True)
  (R/'balanced_counts.json').write_text(json.dumps(results,indent=2),encoding='utf8')
  continue
 break
print('completed through',results[-1]['n'] if results else 0)
