from pathlib import Path
ROOT=Path(__file__).resolve().parents[1]
exec(compile((ROOT/'code/check.py').read_text(encoding='utf-8').split('cases=')[0],str(ROOT/'code/check.py'),'exec'))
def raw_point(w):
 N=1<<w;t=[-1 if x==N-1 else 1 for x in range(N)];p={}
 for s in range(N):
  a=sum(t[x]*(-1 if (s&x).bit_count()%2 else 1) for x in range(N))
  if a:p[s]=F(a*a,N*N)
 ck(sum(p.values())==1);return p
def inherited(w,spike):
 p=raw_point(w);pc=raw_point(w-1);v=1-p.get(0,F(0));q={s:pw if s==0 else F(5,6)*pw+(v/6 if s==spike else 0) for s,pw in p.items()}
 pe={};qe={}
 for s,pw in p.items():u=s>>1;pe[u]=pe.get(u,F(0))+pw
 for s,qw in q.items():u=s>>1;qe[u]=qe.get(u,F(0))+qw
 joint={u:qw*pc.get(u,F(0))/(2*pe[u]) for u,qw in qe.items()};Z=sum(joint.values());qq={u:qw/Z for u,qw in joint.items() if qw}
 ck(sum(q.values())==sum(qq.values())==1)
 fresh=factor_ref(w-1,F(1,6));delta=add(kl(pc,fresh),scale(kl(pc,qq),-1))
 return pc,qq,fresh,delta,Z
rows=[]
for w in range(2,7):
 pc,old,fresh,delta,Z=inherited(w,(1<<w)-1);d=F(1,1<<w);E=1-4*d+8*d*d;eta=2*d*d/(3*E);B=d/(1+8*d)
 ck(Z==(1+eta)/2)
 for s,pw in pc.items():
  expected=(1-eta)/(1+eta) if s==0 else (1+B)/(1+eta) if s==(1<<(w-1))-1 else 1/(1+eta)
  ck(old[s]/fresh[s]==expected)
 if w==2:ck(not delta)
 else:ck(bounds(delta)[1]<0)
 rows.append({'width':w,'active_reset_interval':list(map(str,bounds(delta)))})
pc,old,fresh,delta,Z=inherited(3,1)
ck(Z==F(9,20));ck(old[0]==F(11,36));ck(all(old[s]==F(25,108) for s in [1,2,3]))
closed=scale(lv(F(6875,6561)),F(1,4));ck(not add(delta,scale(closed,-1)))
ck(bounds(delta)[0]>0 and 6875>6561)
obj={'status':'PASS','cases':6,'assertions':COUNT,'runtime_seconds':time.perf_counter()-START,'full_spike':rows,'countercontrol':{'actual_Boolean_core':'3-bit point defect, all8 spectral atoms positive','initial_reference_spike':'queried singleton','fresh_reference_spike':'full remaining2bit block','alpha':'1/6','inherited_active_reference':{str(s):str(x) for s,x in old.items()},'active_signed_reset_exact':'(1/4)log2(6875/6561)>0','reach_weighted_reset_exact':'(1/8)log2(6875/6561)>0','interval':list(map(str,bounds(delta))),'scope':'Full-block spike hypothesis matters; no arbitrary-reference nonpositive-reset claim'}}
save('CONTROL.json',obj);print(json.dumps({k:v for k,v in obj.items() if k not in ['full_spike','countercontrol']}))
