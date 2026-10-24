import json,math,time
from fractions import Fraction as F
from collections import deque
from pathlib import Path
root=Path(__file__).resolve().parents[1]
def save(key,statement,data):
    data.update(problem_id=key,audit_status='PENDING w347',command='python -B -X utf8 checks/batch_two.py')
    (root/'checks'/f'{key}_receipt.json').write_text(json.dumps(data,indent=2),encoding='utf-8')
    with (root/'results.jsonl').open('a',encoding='utf-8') as f: f.write(json.dumps({'row':'S1.O.w331.'+key,'problem_id':key,'label':'proof of obstruction or boundary case; exact/numerical controls','statement':statement,'proof_path':str(root/'proofs'/f'{key}.md'),'measurement':data,'audit_status':'PENDING w347'})+'\n')
    print(json.dumps(data),flush=True)
start=time.perf_counter(); harmonics=[]; total=F(0)
for j in range(1,1025):
    total+=F(1,j)
    centre=F(1,2)+F(1,2**(j+2)); radius=F(1,2**(j+5))
    nextcentre=F(1,2)+F(1,2**(j+3)); nextradius=F(1,2**(j+6))
    assert centre-radius>nextcentre+nextradius and centre+radius<1 and centre-radius>F(1,2)
    assert F(1,2**j)*F(2**j,j)==F(1,j)
    if j in [8,64,1024]: harmonics.append({'N':j,'expected_truncated_bump_supremum':float(total),'max_expected_pointwise_bump':1})
save('P0229','Continuous finite cost fields with E L(z)<=3|z| can have an infinite mean supremum, also over an independent infinite uniform sample; route geometry still needs additional increment control.',{'exact_disjoint_ball_checks':1024,'harmonic_truncations':harmonics,'elapsed_seconds':time.perf_counter()-start})
start=time.perf_counter(); count=0
for field in [[-3,0,2],[-1,1,1],[0],[2,3,5,7]]:
    for z in [-3,-1,0,1,3]:
        shifted=[x+z for x in field]; assert max(shifted)==max(field)+z
        for t in range(-4,12):
            assert sum(y>=t for y in shifted)==sum(x>=t-z for x in field); count+=1
save('C0008','A common independent Gaussian mode gives a bounded covariance change but translates every height and changes every centred-maximum limit by Gaussian convolution; this is a limit-identification warning, not a counterexample to the full covariance hypotheses.',{'threshold_shift_checks':count,'sigma1_characteristic_attenuation_t1':math.exp(-.5),'elapsed_seconds':time.perf_counter()-start})
start=time.perf_counter(); controls=[]
for V in [1000,10**6,10**9]:
    a=V**(1/3); h=V**(-2); inside=a; outside=a/(1+a*a/16)+.075*V*V
    assert .75-h>.5+1/a and outside>inside
    controls.append({'V':V,'window_peak_log_derivative':inside,'outside_log_derivative':outside,'ratio':outside/inside})
save('C0067','Monotone C1 functions can be uniformly within a factor exp(0.1) of a baseline susceptibility shape while their logarithmic-derivative maxima lie outside every fixed V^(-1/3) window; values alone do not prove torus derivative location.',{'max_value_ratio':math.exp(.1),'derivative_controls':controls,'elapsed_seconds':time.perf_counter()-start})
start=time.perf_counter(); boxes=[]
for n in [3,5,9,17]:
    heights=[3]*(n*n); origin=(n*n)//2; heights[origin]=4; odometer=[0]*(n*n); q=deque([origin]); queued={origin}; dissipated=0
    while q:
        v=q.popleft(); queued.remove(v)
        if heights[v]<4: continue
        times=heights[v]//4; heights[v]-=4*times; odometer[v]+=times
        r,c=divmod(v,n)
        for rr,cc in [(r-1,c),(r+1,c),(r,c-1),(r,c+1)]:
            if 0<=rr<n and 0<=cc<n:
                w=rr*n+cc; heights[w]+=times
                if heights[w]>=4 and w not in queued: q.append(w);queued.add(w)
            else: dissipated+=times
    assert all(0<=x<=3 for x in heights) and sum(heights)+dissipated==3*n*n+1
    boxes.append({'side':n,'origin_topplings':odometer[origin],'total_topplings':sum(odometer),'dissipated':dissipated})
assert all(boxes[i]['origin_topplings']<boxes[i+1]['origin_topplings'] for i in range(len(boxes)-1))
save('C0098','Every configuration at least 3 everywhere with a height-4 seed explodes on Z2 by recurrence; iid laws on {3,4} are decided exactly by whether P(4)>0. A stable background plus a finite perturbation need not stabilise.',{'sink_box_controls':boxes,'zero_toppling_stable_height_laws':4,'elapsed_seconds':time.perf_counter()-start})
