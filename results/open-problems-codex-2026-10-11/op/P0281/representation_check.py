from pathlib import Path
import mpmath as mp,json
code=Path('tail_recheck.py').read_text(encoding='utf-8-sig').split('results=[]')[0];exec(compile(code,'tail_recheck.py','exec'))
p=uniform(3,6,mp.mpf('.5'),140);out=[]
for u,v,c in [(0,0,0),(1,0,0),(1,1,0),(1,1,1),(4,2,1),(6,3,0)]:
 z=mp.mpf(0);t=mp.mpf('.5')
 for b in range(v,41):
  for a in range(max(u,b),41):
   weight=mp.exp(-3*t)*t**(a+b+c)*(a-b+1)*(a-c+2)*(b-c+1)/(mp.factorial(a+2)*mp.factorial(b+1)*mp.factorial(c))
   z+=weight*(a-max(u,b)+1)
 r={'state':(u,v,c),'array_probability':str(z),'uniform_probability':str(p[u,v,c]),'relative_error':str(abs(z-p[u,v,c])/p[u,v,c])};out.append(r);print(r,flush=True)
Path('representation_highprecision.json').write_text(json.dumps(out,indent=2))
