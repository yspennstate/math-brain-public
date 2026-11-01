import json,pathlib

def upsets(n):
 if n==0:return [0,1]
 prev=upsets(n-1);shift=1<<(n-1)
 return [a|(b<<shift) for a in prev for b in prev if a&~b==0]
rows=[]
for n in range(1,6):
 best2=best21=-1;outside=[0,0]
 for mask in upsets(n):
  v2=v21=0
  A=lambda w:bool(mask>>w&1)
  for w in range(1<<n):
   if not A(w):continue
   first={i for i in range(n) if w>>i&1 and not A(w&~(1<<i))}
   second=set(first)
   for i in range(n):
    if not w>>i&1:continue
    for j in range(n):
     if i!=j and w>>j&1 and A(w&~(1<<j)) and not A(w&~(1<<i)&~(1<<j)):second.add(i)
   v2+=len(second);v21+=len(second-first)
  best2=max(best2,v2);best21=max(best21,v21)
 rows.append(dict(n=n,max_phi2=best2,max_phi21=best21))
assert [r['max_phi2'] for r in rows]==[1,4,9,24,62]
assert [r['max_phi21'] for r in rows]==[0,2,6,12,38]
p=pathlib.Path('verification.json');data=json.loads(p.read_text());data['occupied_coordinate_variant']=rows;p.write_text(json.dumps(data,indent=2),encoding='utf8')
print(rows);print('Source table maxima reproduced under occupied-coordinate restriction.')
