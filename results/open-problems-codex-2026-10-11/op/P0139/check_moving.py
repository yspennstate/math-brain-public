"""Finite moving-clock/reroot checks and the zero-area energy boundary.

These checks supplement, and do not replace, the complete proofs.
"""
import bisect
import json
import math
import random
from pathlib import Path

random.seed(13912)

def wedge(x,y):
    return x[0]*y[1]-x[1]*y[0]

def minus(x,y):
    return (x[0]-y[0],x[1]-y[1])

def circle_g(u,R,phase):
    return (R*(math.cos(2*math.pi*u+phase)-math.cos(phase)),
            R*(math.sin(2*math.pi*u+phase)-math.sin(phase)))

def circle_A(u,R):
    k=math.floor(u)
    v=u-k
    return k*math.pi*R*R+0.5*R*R*(2*math.pi*v-math.sin(2*math.pi*v))

# Verify full-period central area and seam corrections by analytic circles.
reroot_error=0.0
terminal_error=0.0
for _ in range(4000):
    R=random.uniform(0.001,1)
    theta=random.random()
    v=random.random()
    phase=random.uniform(-math.pi,math.pi)
    b=circle_A(theta+v,R)-circle_A(theta,R)-0.5*wedge(circle_g(theta,R,phase),circle_g(theta+v,R,phase))
    expected=0.5*R*R*(2*math.pi*v-math.sin(2*math.pi*v))
    reroot_error=max(reroot_error,abs(b-expected))
    c=circle_A(theta+1,R)-circle_A(theta,R)-0.5*wedge(circle_g(theta,R,phase),circle_g(theta+1,R,phase))
    terminal_error=max(terminal_error,abs(c-math.pi*R*R))

def schedule(level,eps,lam):
    rows=[]
    for k in range(1,level+1):
        for j in range(1,2**(k-1)+1):
            s=(2*j-1)/2**k
            d=2**(1-2*k)
            rows.append({'id':(k,j),'root':s+eps*s*(1-s),
                         'duration':d*(1+eps*(s-0.5)),
                         'radius':d*d*(1+eps*math.cos(math.pi*s))})
    rows.sort(key=lambda l:l['root'])
    prefix=0.0
    for row in rows:
        row['start']=prefix+lam*row['root']
        row['end']=row['start']+row['duration']
        prefix+=row['duration']
    return rows,prefix+lam

def clock(rows,T,lam,t):
    if t<=0:return 0.0
    if t>=T:return 1.0
    i=bisect.bisect_right([l['start'] for l in rows],t)-1
    if i<0:return t/lam
    row=rows[i]
    if t<=row['end']:return row['root']
    return row['root']+(t-row['end'])/lam

# Precompute starts to keep the test inexpensive.
def fast_clock(rows,starts,T,lam,t):
    if t<=0:return 0.0
    if t>=T:return 1.0
    i=bisect.bisect_right(starts,t)-1
    if i<0:return t/lam
    row=rows[i]
    if t<=row['end']:return row['root']
    return row['root']+(t-row['end'])/lam

def finite_splice(rows,starts,T,lam,t,kept):
    f=fast_clock(rows,starts,T,lam,t)
    y=(f,0.0)
    e=(0.0,0.0)
    b=0.0
    for row in kept:
        u=min(1,max(0,(t-row['start'])/row['duration']))
        R=row['radius']
        z=(R*(1-math.cos(2*math.pi*u)),-R*math.sin(2*math.pi*u))
        e=(e[0]+z[0],e[1]+z[1])
        b+=0.5*R*R*(2*math.pi*u-math.sin(2*math.pi*u))
    return (y[0]+e[0],y[1]+e[1]),b+0.5*wedge(y,e)

ref,Tr=schedule(18,0.0,1e-9)
sr=[l['start'] for l in ref]
ref_kept=[l for l in ref if l['id'][0]<=3]
times=sorted({0.0,1.1,*[1.1*j/1800 for j in range(1801)],*[random.uniform(0,1.1) for _ in range(700)]})
ref_clock=[fast_clock(ref,sr,Tr,1e-9,t) for t in times]
ref_coords=[finite_splice(ref,sr,Tr,1e-9,t,ref_kept) for t in times]
moving=[]
for level in (3,4,5,6,8,10,12):
    eps=2.0**(-level)
    lam=eps
    rows,T=schedule(level,eps,lam)
    starts=[l['start'] for l in rows]
    kept=[l for l in rows if l['id'][0]<=3]
    fs=[fast_clock(rows,starts,T,lam,t) for t in times]
    coords=[finite_splice(rows,starts,T,lam,t,kept) for t in times]
    assert all(-1e-10<=f<=1+1e-10 for f in fs)
    assert all(fs[i]<=fs[i+1]+1e-10 for i in range(len(fs)-1))
    err_clock=max(abs(f-g) for f,g in zip(fs,ref_clock))
    err_first=max(math.hypot(*minus(x,y)) for (x,a),(y,b) in zip(coords,ref_coords))
    err_global_area=max(abs(a-b) for (x,a),(y,b) in zip(coords,ref_coords))
    err_inc_area=0.0
    for _ in range(3000):
        s,t=sorted(random.sample(range(len(times)),2))
        xn,an=coords[s];yn,bn=coords[t]
        xr,ar=ref_coords[s];yr,br=ref_coords[t]
        incn=bn-an-0.5*wedge(xn,yn)
        incr=br-ar-0.5*wedge(xr,yr)
        err_inc_area=max(err_inc_area,abs(incn-incr))
    moving.append({'levels':level,'loops':len(rows),'lambda':lam,'terminal_time':T,
                   'sampled_clock_uniform_error':err_clock,
                   'finite_retained_first_error':err_first,
                   'finite_retained_global_area_error':err_global_area,
                   'sampled_finite_retained_increment_area_error':err_inc_area})

p=2.8
r=2.4
boundary=[]
for N in (16,64,256,1024,4096):
    rad=N**(-1/p)
    tree=[(0,0),(0,rad),(0,0),(0,-rad),(0,0)]
    a=sum(0.5*wedge(x,y) for x,y in zip(tree,tree[1:]))
    assert a==0
    boundary.append({'N':N,'radius':rad,'terminal_area':a,
                      'selected_target_p_energy':N*rad**p,
                      'selected_stronger_r_energy':N*rad**r,
                      'output_pvar_lower_bound':0.8})

assert reroot_error<1e-12 and terminal_error<1e-12
assert moving[-1]['sampled_clock_uniform_error']<moving[0]['sampled_clock_uniform_error']
assert moving[-1]['finite_retained_first_error']<moving[0]['finite_retained_first_error']
assert moving[-1]['sampled_finite_retained_increment_area_error']<moving[0]['sampled_finite_retained_increment_area_error']
out={'seed':13912,'reroot_checks':4000,'reroot_max_error':reroot_error,
     'terminal_area_max_error':terminal_error,'physical_time_samples':len(times),
     'reference_levels':18,'reference_lambda':1e-9,
     'qualification':'Reference is a fine finite approximation to the dense atomic clock. Sampled errors are numerical evidence, not the infinite theorem.',
     'moving_clock_sequence':moving,'zero_area_boundary':boundary}
Path('moving_checks.json').write_text(json.dumps(out,indent=2),encoding='utf8')
print(json.dumps(out,indent=2))
