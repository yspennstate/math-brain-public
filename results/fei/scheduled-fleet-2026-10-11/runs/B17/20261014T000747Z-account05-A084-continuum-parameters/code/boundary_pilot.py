from pilot import profile,ROOT
import math,json,time
start=time.perf_counter();rows=[];both=[]
def slope(p):
    c=(1-2*p)**2;ps=profile(p);q=sum(d for u,d in ps);a=0.
    for u,d in ps:
        if d:
            if u<=1e-28:return None
            a+=d*math.log2(u/d/c)
    return a/q
for j in range(1,512):
    p=j/1024;v=[slope(p),slope(1-p)]
    row={'p':f'{j}/1024','normalized_boundary_slopes':v};rows.append(row)
    if all(x is None or x<0 for x in v):both.append(row)
out={'runtime_seconds':time.perf_counter()-start,'rows':rows,'both_bad_rows':both,'scope':'Floating discovery, not proof'}
(ROOT/'out'/'BOUNDARY_PILOT.json').write_text(json.dumps(out,indent=2),encoding='utf-8')
print(json.dumps({'runtime_seconds':out['runtime_seconds'],'both_bad_count':len(both),'both_bad_above_one_sixteenth':[x for x in both if float(eval(x['p']))>=1/16],'first_rows':rows[:4]}),flush=True)
