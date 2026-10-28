from pathlib import Path
import json
R=Path(__file__).resolve().parents[1]
s=(R/'code/check.py').read_text(encoding='utf-8')
s=s.replace('CAP=F(1,8);VALUES=(F(0),F(1,64),F(1,16))','CAP=F(1,2);VALUES=(F(1,2),F(1),F(2))')
start=s.index('@lru_cache(None)\ndef state(')
end=s.index('@lru_cache(None)\ndef children(',start)
s=s[:start]+'''@lru_cache(None)
def state(args,ra,epsilon):
 s=p.shaped(args,ra);base=s['base'];a,g,h,rg,rh=args
 V=1-b.spectrum(a)[0];gamma=sum(F(x!=y,len(g)) for x,y in zip(g,h));eta=V*gamma
 Q=list(s['Q']);q=b.spectrum(b.mux(a,g,h));C={};na=len(a);nd=len(g)
 for t in range(nd):
  inds=[u+na*t for u in range(na)];qt=sum(q[j] for j in inds)
  if not qt:continue
  k=sum(q[j] for j in inds[1:])/qt
  if epsilon=='legacy':
   ell=F(15,16)*k+F(1,32)
   if k in (0,1):ck(ell==k,'legacy only at actual interior rows')
   else:ck(F(1,2)<=ell*(1-k)/(k*(1-ell))<=2,'literal legacy relative odds range')
  else:
   ck(F(1,2)<=epsilon<=2)
   ell=epsilon*k/(1+(epsilon-1)*k)
  row=sum(Q[j] for j in inds);non=sum(Q[j] for j in inds[1:])
  if ell:
   ck(non>0,'conditional profile available')
   B=[Q[j]/non for j in inds[1:]]
  else:B=[F(0)]*(na-1)
  Q[inds[0]]=row*(1-ell)
  for j,v in zip(inds[1:],B):Q[j]=row*ell*v
  C=e.add(C,e.scale(b.kl((1-k,k),(1-ell,ell)),qt))
 Q=tuple(Q);cap=eta/2
 nn(C);nn(sub(const(cap),C),'one original influence-scaled allowance')
 plus=e.add(s['S'],const(cap),e.scale(C,-1));nn(plus)
 D=e.add(s['D'],C);T=e.add(s['T'],const(cap));eq(D,b.kl(q,Q));eq(D,sub(T,plus))
 return dict(Q=Q,C=C,D=D,T=T,S=plus,old=s,epsilon=epsilon,cap=cap,eta=eta)

'''+s[end:]
s=s.replace("pair=(F(1,16),F(0))", "pair=('legacy',F(1))")
s=s.replace("pair=(F(1,16),F(1,64))", "pair=(F(2),F(1,2))")
s=s.replace("first=state(data[1],ra,F(0))", "first=state(data[1],ra,F(1))")
s=s.replace("st=state(*cc[0],F(1,16))", "st=state(*cc[0],'legacy')")
s=s.replace("result=walk(data[1],ra,F(0)", "result=walk(data[1],ra,F(1)")
s=s.replace('const(CAP/2)',"const(first['cap']/2)").replace('3*m-F(497,256)','3*m-F(263,128)')
start=s.index('def guard():');end=s.index('def main():',start)
s=s[:start]+'''def guard():
 rows=[];C=e.scale(e.lg(F(9,8)),F(1,2));ck(9**8>2*8**8)
 for depth in (1,2,4,8):
  a=tuple(1 if y%2==0 else -1 for y in range(1<<(depth+1)))
  g=(1,-1,1,-1);h=(1,1,-1,-1)
  args=(a,g,h,b.spectrum(g),b.spectrum(h));ra=b.spectrum(a)
  s=state(args,ra,F(2));eq(s['C'],C);ck(s['eta']==F(1,2))
  rootzero=state(args,ra,F(1));eq(rootzero['old']['T'],{});eq(rootzero['old']['S'],{})
  aa,cs,A,rec=edge(args,ra,F(2),1,(F(1),F(1)))
  eq(rec['raw'],e.scale(C,-1));eq(e.add(rec['E'],rec['O']),{})
  signed=C;positive=e.scale(C,depth)
  if depth>=4:nn(sub(positive,const(F(1,4))))
  nn(sub(const(F(1,4)),signed))
  rows.append(dict(depth=depth,signed=enc(signed),positive_parts=enc(positive),allowance='1/4',canonical_T={},canonical_S={}))
 return rows

'''+s[end:]
s=s.replace("'pilot.json' if MODE=='pilot' else 'main.json'","'logit_pilot.json' if MODE=='pilot' else 'logit_main.json'")
(R/'code/logit_check.py').write_text(s,encoding='utf-8',newline='\n')
print('RELATIVE_CHECKER_PREPARED')
