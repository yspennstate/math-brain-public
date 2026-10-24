import pathlib,json
p=pathlib.Path('checks.json');checks=json.loads(p.read_text(encoding='utf8'))
def integrate01(a,b):
 knots=sorted(set([a,b]+[float(i) for i in range(-30,31) if a<i<b]))
 return sum((v-u)*(int((u+v)//2)%2) for u,v in zip(knots,knots[1:]))
n=0
for c in [-10,-5,-2.2,-1,0,.1,2.7,5,10]:
 for R in [.2,1,2,5,10,15]:
  error=abs(integrate01(0,R)-integrate01(c,c+R))
  assert error<=min(R,abs(c))+1e-12;n+=1
checks.append(dict(check='sharpened indicator translation bound for Theorem D',cases=n,result='PASS'))
p.write_text(json.dumps(checks,indent=2),encoding='utf8')
print('Theorem D sharpened interval bound:',n,'cases PASS')
