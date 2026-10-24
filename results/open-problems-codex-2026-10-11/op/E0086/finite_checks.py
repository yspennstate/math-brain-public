from pathlib import Path
import itertools,json,math,time
out={};start=time.time();n=8
for h,a in [((1,0),1.0),((2,0),4-8/math.pi),((1,1),4/math.pi)]:
 counts={};killed=[0]*(n+2);far_ok=True
 for moves in itertools.product(range(4),repeat=n):
  x=y=0;sites=[(0,0)];visits={(0,0):1};nh=1;hit=False
  for move in moves:
   dx,dy=((1,0),(-1,0),(0,1),(0,-1))[move];x+=dx;y+=dy;s=(x,y)
   sites.append(s);visits[s]=visits.get(s,0)+1
   if not hit:
    if s==h:hit=True
    elif s==(0,0):nh+=1
  for k in range(1,n+2):killed[k]+=int(nh>=k)
  eligible=[v for (x,y),v in visits.items() if (x+h[0],y+h[1]) not in visits]
  m=max(eligible,default=0);counts[m]=counts.get(m,0)+1
  far_ok=far_ok and all((x+9,y) not in visits for x,y in visits)
 total=4**n;p=1-1/(2*a)
 checks=[]
 for k in range(1,n+2):
  prob=sum(v for m,v in counts.items() if m>=k)/total
  bound=(n+1)*p**(k-1)
  geo=killed[k]/total;g_bound=p**(k-1)
  assert prob<=bound+1e-14 and geo<=g_bound+1e-14
  checks.append({'k':k,'boundary_tail':prob,'union_bound':bound,'truncated_killed_tail':geo,'geometric_bound':g_bound})
 assert far_ok
 out[str(h)]={'n':n,'paths':total,'potential_kernel':a,'boundary_distribution':counts,'checks':checks,'far_offset_identity':far_ok}
out['elapsed_seconds']=time.time()-start
Path('finite_checks.json').write_text(json.dumps(out,indent=2),encoding='utf-8');print('exhaustive checks passed',out['elapsed_seconds'])
