"""Independent 2D ERW simulations. No imports from claim_files.
One worker; site marks sampled on first departure (IID lazy construction).
"""
import csv,json,math,os,random,resource,statistics,time
from pathlib import Path
ROOT=Path(__file__).resolve().parents[1]
for v in ["OPENBLAS_NUM_THREADS","OMP_NUM_THREADS","MKL_NUM_THREADS"]:os.environ[v]="1"
priority=os.getpriority(os.PRIO_PROCESS,0)
if priority<10:os.setpriority(os.PRIO_PROCESS,0,10)
as_soft,as_hard=resource.getrlimit(resource.RLIMIT_AS)
as_cap=min(2*1024**3,as_hard) if as_hard!=resource.RLIM_INFINITY else 2*1024**3
try:
 resource.setrlimit(resource.RLIMIT_AS,(as_cap,as_hard));as_limit_set=True
except (ValueError,OSError):
 as_limit_set=False # macOS rejects RLIMIT_AS; finite dict size and RSS recorded instead.
DIRECTIONS=((1,0),(-1,0),(0,1),(0,-1))
HORIZONS=(4096,16384,65536,262144)
RUNS=192
SEED=71332026

def direction_sign(i):
 # Paired blocks +16,-16,+32,-32,...; random site phase multiplies signs.
 j=i-1;block=16
 while j>=2*block:j-=2*block;block*=2
 return 1 if j<block else -1

def path(model,seed):
 rng=random.Random(seed);x=y=0;sites={};last_origin=0;last_ball=0;maxvis=0;rows=[]
 for t in range(1,HORIZONS[-1]+1):
  pos=(x,y)
  state=sites.get(pos)
  if state is None:
   mark=rng.randrange(4) if model=="summable_trap" else rng.choice((-1,1))
   state=[0,mark];sites[pos]=state
  state[0]+=1;i,mark=state;maxvis=max(maxvis,i)
  if model=="symmetric":prob=(.25,.25,.25,.25)
  elif model=="long_blocks":
   s=mark*direction_sign(i);prob=(.4+.36*s,.4-.36*s,.1,.1)
  elif model=="summable_trap":
   # Exact infinite law uses eps_i=2^(-i-6). Beyond floating precision
   # mark-following is simulated; probability of omitted deviation per
   # visited site after departure 48 is <=3*2^(-54).
   eps=math.ldexp(1.,-i-6) if i<=48 else 0.
   prob=tuple(1-3*eps if j==mark else eps for j in range(4))
  else:raise ValueError(model)
  u=rng.random();s=0
  for j,p in enumerate(prob):
   s+=p
   if u<s:break
  dx,dy=DIRECTIONS[j];x+=dx;y+=dy
  if x==0 and y==0:last_origin=t
  if abs(x)+abs(y)<=4:last_ball=t
  if t in HORIZONS:
   rows.append(dict(model=model,seed=seed,n=t,x=x,y=y,speed_x=x/t,norm_speed=(abs(x)+abs(y))/t,
    late_origin=int(last_origin>=t//2),late_ball=int(last_ball>=t//2),last_origin=last_origin,last_ball=last_ball,
    sites=len(sites),max_departures=maxvis))
 return rows

def wilson(k,n):
 z=1.95996398454;p=k/n;den=1+z*z/n;c=(p+z*z/(2*n))/den
 d=z*math.sqrt(p*(1-p)/n+z*z/(4*n*n))/den
 return [c-d,c+d]

def main():
 begin=time.monotonic();rows=[]
 for mi,model in enumerate(("symmetric","long_blocks","summable_trap")):
  for trial in range(RUNS):rows.extend(path(model,SEED+mi*100000+trial))
  print("completed",model,flush=True)
 with (ROOT/"data/walks.csv").open("w",newline="") as f:
  w=csv.DictWriter(f,fieldnames=list(rows[0]));w.writeheader();w.writerows(rows)
 summary=[]
 for model in ("symmetric","long_blocks","summable_trap"):
  for n in HORIZONS:
   a=[r for r in rows if r["model"]==model and r["n"]==n]
   selected=[r for r in a if r["late_ball"]]
   summary.append(dict(model=model,n=n,runs=len(a),late_origin=sum(r["late_origin"] for r in a),
    late_ball=len(selected),late_ball_wilson=wilson(len(selected),len(a)),
    mean_speed_x=statistics.mean(r["speed_x"] for r in a),
    selected_mean_speed_x=statistics.mean(r["speed_x"] for r in selected) if selected else None,
    selected_mean_abs_speed_x=statistics.mean(abs(r["speed_x"]) for r in selected) if selected else None,
    selected_max_norm_speed=max((r["norm_speed"] for r in selected),default=None),
    median_range=statistics.median(r["sites"] for r in a)))
 result=dict(seed=SEED,summary=summary,elapsed_s=time.monotonic()-begin,
  nice=os.getpriority(os.PRIO_PROCESS,0),workers=1,peak_rss_bytes=resource.getrusage(resource.RUSAGE_SELF).ru_maxrss,
  address_space_limit_bytes=as_cap if as_limit_set else None,trap_per_site_omitted_deviation_bound=3*2**(-54))
 (ROOT/"data/simulation.json").write_text(json.dumps(result,indent=2))
 print(json.dumps(result,indent=2))
if __name__=="__main__":main()
