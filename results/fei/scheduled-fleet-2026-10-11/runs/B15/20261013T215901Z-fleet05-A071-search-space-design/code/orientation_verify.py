import json,time
from fractions import Fraction as Q
import search as s

start=time.perf_counter();items=[]
for mask in (1,((1<<64)-1)^1):
    row=s.evaluate(6,mask);p=Q(row['p']);t=Q(1,32)**2;m=1-2*p
    var=p*(1-p);q=Q(0);M=(Q(0),Q(0));packets=[]
    for T in range(32):
        C=B=Q(0)
        for z in range(32):
            h0=Q(1-2*((s.SEED>>(z<<1))&1));h1=Q(1-2*((s.SEED>>((z<<1)|1))&1))
            az=(h0+h1)/2;bz=(h0-h1)/2
            weight=p**z.bit_count()*(1-p)**(5-z.bit_count());basis=Q(1)
            for j in range(5):
                if T>>j&1:basis*=Q((z>>j)&1)-p
            C+=weight*basis*(az+m*bz);B+=weight*basis*bz
        d=var**T.bit_count();u=C*C/d;w=B*B/d;q+=w
        M=s.add(M,s.phi_pair(u,t*w));packets.append([str(u),str(t*w)])
    R=s.sub(M,s.mul(s.phi_pair(m*m,t),q))
    assert q==Q(row['q']) and R[1]<0
    pred=tuple(map(Q,row['coordinates'][0]['reserve']['rational_bounds']))
    assert max(pred[0],R[0])<=min(pred[1],R[1])
    assert Q(row['E_core']['rational_bounds'][0])>Q(9,4)
    assert Q(row['E_composed']['rational_bounds'][1])<Q(9,4)
    assert len(row['coordinates'])==6 and all(r['influence_core']=='1/32' for r in row['coordinates'])
    items.append({'core':row,'independent_reserve':s.pack(R),'outer32_packets':packets,
                  'proved_core_E_greater_than':'9/4','proved_composed_E_less_than':'9/4'})
out={'cases':items,'runtime_seconds':time.perf_counter()-start,
     'both_output_orientations_fail_same_K':True,'K':'9/4',
     'all36_coordinates_equal_by_actual_transitivity':True}
assert out['runtime_seconds']<55
(s.ROOT/'out/orientation_certificate.json').write_text(json.dumps(out,indent=2),encoding='utf-8')
print(json.dumps({'K':'9/4','both_fail':True,'runtime_seconds':out['runtime_seconds'],
 'cases':[{'mask':r['core']['mask'],'p':r['core']['p'],'E_core':r['core']['E_core']['display'],
           'E_composed':r['core']['E_composed']['display'],'reserve':r['independent_reserve']['display']} for r in items]},indent=2))
