import tag as t
import kernel as k
from fractions import Fraction as F
import json,time,sys

def main():
 start=time.monotonic();pilot='pilot' in sys.argv;out=[]
 seeds={'parity2':bytes([0,1,1,0]),'point2':bytes([1,0,0,0]),'majority3':bytes(int(i.bit_count()>=2) for i in range(8))}
 for n in ([4] if pilot else [4,6,8,10,12]):
  u=bytes(sum(((i>>j)&1)*((i>>(j+1))&1) for j in range(0,n,2))%2 for i in range(1<<n))
  v=bytes([1-u[0]])+u[1:];delta=F(1,1<<n)
  m=bytes(list(u)+list(v));qm=t.reserve(m,tuple(range(n+1)))
  for name,a in seeds.items():
   s=len(a).bit_length()-1
   f=bytes((u if (w^a[z])==0 else v)[x] for w in range(2) for x in range(1<<n) for z in range(1<<s))
   qa=t.reserve(a,tuple(range(s)))
   qe=t.reserve(f,(n+s,)+tuple(range(n+s)))
   bank=tuple(k.add(t.scaled(q,delta),r) for q,r in zip(qa,qm));gap=tuple(k.sub(q,r) for q,r in zip(qe,bank))
   row={'k':n,'seed':name,'disagreement':str(delta),'Qseed':qa,'Qprofile':qm,'Qearly':qe,'bank':bank,'gap':gap,'gap_over_delta':[[str(F(x,k.SCALE)/delta),str(F(y,k.SCALE)/delta)] for x,y in gap]}
   out.append(row)
   (t.ROOT/'out'/('BENT_PILOT.json' if pilot else 'BENT_EXACT.json')).write_text(json.dumps({'cases':out,'seconds':time.monotonic()-start,'assertions':k.ASSERTIONS},indent=2),encoding='utf-8')
   print(n,name,'gap/delta',[[float(F(x,k.SCALE)/delta),float(F(y,k.SCALE)/delta)] for x,y in gap],flush=True)
   k.check(time.monotonic()-start<55)
   t.reserve.cache_clear();k.stats.cache_clear();k.children.cache_clear()
   qm=t.reserve(m,tuple(range(n+1)))
 print('PASS',len(out),k.ASSERTIONS,time.monotonic()-start)
if __name__=='__main__':main()
