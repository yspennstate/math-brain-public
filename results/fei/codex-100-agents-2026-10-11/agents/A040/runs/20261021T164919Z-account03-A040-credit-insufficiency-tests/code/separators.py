from pathlib import Path
import json,time
p=Path(__file__).resolve().parents[1]
ns={"__file__":str(p/"code/check.py")};exec((p/'code/check.py').read_text(encoding='utf-8').split("mode=sys.argv")[0],ns)
F,ck,entropy,entterm,sub,add,law,fmt,infl=map(ns.get,['F','ck','entropy','entterm','sub','add','law','fmt','infl'])
rows=[]
for s,L,R,T in [(1,1,1,1),(2,1,1,1),(3,1,1,1),(4,1,1,1),(1,1,4,4)]:
 nctl=s+L+R+T
 for code in range(16):
  g=tuple(-1 if code>>x&1 else 1 for x in range(4));v=[]
  for x in range(2**(nctl+2)):
   offset=0;events=[]
   for width in [s,L,R,T]:events.append((x>>offset)&(2**width-1)==2**width-1);offset+=width
   S,W,U,V=events;A=(W and U and V) or (S and (U or V));v.append(1+A*(g[x>>nctl]-1))
  v=tuple(v);P=law(v);B=(F(0),F(0))
  for t in range(0,len(P),2):B=add(B,sub(add(entterm(P[t]),entterm(P[t+1])),entterm(P[t]+P[t+1])))
  a=F(2*sum(y==-1 for y in g),len(g));q=F(1,2**R);r=F(1,2**T);eta=F(1,2**(L+R+T));e=q+r-q*r-eta;d=F(1,2**s)*a*e
  ck(infl(v,0)==d)
  if s>=4 or a*e<=F(1,16) or e<=F(1,8):ck(B[1]<4*d if d else B==(0,0))
  rows.append({'widths':[s,L,R,T],'core_code':code,'influence':str(d),'B':fmt(B)})
out={'status':'PASS','checks':ns['checks'],'cases':len(rows),'runtime_seconds':time.perf_counter()-ns['start'],'rows':rows}
(p/'out/SEPARATORS.json').write_text(json.dumps(out,indent=2),encoding='utf-8');print({k:v for k,v in out.items() if k!='rows'})
