"""Exact output-energy identities and full-network continuation audits.

Standard library only. Numeric trajectories test formulas; convergence is
proved by telescoping the exact energy identity, not by numerical zeros.
"""
import json
import math
import os
import random
import resource
import time
from fractions import Fraction as R

resource.setrlimit(resource.RLIMIT_CPU, (120,120))
start = time.monotonic()
assert os.environ['OMP_NUM_THREADS'] == '1'
assert os.getpriority(os.PRIO_PROCESS,0) >= 15

# Derive both sides separately in exact arithmetic, including mixed signs
# in a and arbitrary, changing, bounded feature vectors.
rng = random.Random(227600)
exact_cases = 0
rank_one_cases = 0
for m in (1,2,3,7,16):
    for case in range(8):
        a = [R(rng.randrange(-100,101),10) for _ in range(m)]
        v = [R(rng.randrange(-10,11),10) for _ in range(m)]
        for h in map(R,('.001','.05','.9','1','1.1','1.9','1.999','2','2.001')):
            f = sum((ai*vi for ai,vi in zip(a,v)),R(0))/m
            q = sum((vi*vi for vi in v),R(0))/m
            e = sum((ai*ai for ai in a),R(0))/m
            ap = [ai-h*f*vi for ai,vi in zip(a,v)]
            ep = sum((ai*ai for ai in ap),R(0))/m
            assert ep-e == -h*(2-h*q)*f*f
            if 0<h<2:
                assert ep <= e-h*(2-h)*f*f
            if q:
                # Orthogonal decomposition independent of expansion.
                coeff = f/q
                orth = [ai-coeff*vi for ai,vi in zip(a,v)]
                assert sum((x*y for x,y in zip(orth,v)),R(0)) == 0
                e_spectral = (sum((x*x for x in orth),R(0))/m
                              +(1-h*q)**2*f*f/q)
                assert e_spectral == ep
                rank_one_cases += 1
            exact_cases += 1

e0_bound = R('8.01')**2
coefficient_lower = R('.99')
assert R('.9')*(2-R('.9')) == coefficient_lower
assert R('1.1')*(2-R('1.1')) == coefficient_lower
sum_F2 = e0_bound/coefficient_lower
assert sum_F2 == R(71289,1100)
sum_L = sum_F2/2
assert sum_L == R(71289,2200) and sum_L < R('32.405')

def sech2(x):
    e = math.exp(-2*abs(x))
    return 4*e/(1+e)**2

def state(x,m):
    # Evaluate in literal Euclidean a,B,c coordinates.
    a, b, c = x[:m],x[m:m+m*m],x[m+m*m:]
    root = math.sqrt(m)
    u = [math.tanh(cj) for cj in c]
    z = [math.fsum(b[i*m+j]*u[j] for j in range(m))/root for i in range(m)]
    v = [math.tanh(zi) for zi in z]
    aq = [ai*sech2(zi) for ai,zi in zip(a,z)]
    f = math.fsum(ai*vi for ai,vi in zip(a,v))/m
    q = math.fsum(vi*vi for vi in v)/m
    e = math.fsum(ai*ai for ai in a)/m
    g = ([vi/m for vi in v]
         +[aq[i]*u[j]/(m*root) for i in range(m) for j in range(m)]
         +[sech2(c[j])*math.fsum(aq[i]*b[i*m+j] for i in range(m))/(m*root) for j in range(m)])
    return f,q,e,g

initials = []
for m in (4,16,32):
    root = math.sqrt(m)
    for pattern in ('circulant','imbalanced_columns','independent_signs'):
        a = [rng.uniform(7.99,8.01) for _ in range(m)]
        c = [rng.uniform(1.999,2.001) for _ in range(m)]
        def sign(i,j):
            if pattern == 'independent_signs': return rng.choice((-1,1))
            return -1 if (j-(i if pattern=='circulant' else 0))%m < m//2 else 1
        b = [sign(i,j)*rng.uniform(.999,1.001)/root for i in range(m) for j in range(m)]
        initials.append((pattern,m,a+b+c))

# Audit continuation from many locations in the earlier exit window. These
# are deterministic states for testing the global identity, not claimed
# random samples from the initial law or reachable stopping states.
for exit_f in (.02,.03,.05,.1,.2,.3,.5,.8,1.1,1.379):
    m=4
    shift = math.atanh(exit_f/8)/math.tanh(2)
    b = [((-1 if (j-i)%m < m//2 else 1)+shift)/2 for i in range(m) for j in range(m)]
    initials.append(('exit_window_'+str(exit_f),m,[8.]*m+b+[2.]*m))

audits = []
max_identity_error = max_telescoping_error = fd_error = 0.
growth_example = None
for label,m,x0 in initials:
    for h in (.9,1.,1.1):
        x = x0[:]
        e0 = state(x,m)[2]
        sumsq = weighted = 0.
        rows=[]
        lastf=None
        escaped = label.startswith('exit_window')
        saw_decrease = False
        for t in range(200):
            f,q,e,g = state(x,m)
            if abs(f)>=.02: escaped=True
            if lastf is not None and escaped:
                if abs(f)<abs(lastf)*.9: saw_decrease=True
                if saw_decrease and abs(f)>abs(lastf)*1.1 and abs(lastf)>1e-8:
                    if growth_example is None:
                        growth_example = dict(label=label,m=m,h=h,t=t,previous_F=lastf,F=f)
            rows.append(dict(t=t,F=f,loss=f*f/2,energy=e,Q=q,
                             m_NTK=m*math.fsum(gi*gi for gi in g)))
            y = [xi-m*h*f*gi for xi,gi in zip(x,g)]
            fp,qp,ep,gp = state(y,m)
            predicted = h*(2-h*q)*f*f
            err = abs(ep-e+predicted)
            max_identity_error=max(max_identity_error,err)
            assert err < 2e-12*max(1,e)
            assert ep<=e+2e-12*max(1,e)
            sumsq += f*f
            weighted += predicted
            assert sumsq <= e0/(h*(2-h))+1e-8
            terr=abs(e0-ep-weighted)
            max_telescoping_error=max(max_telescoping_error,terr)
            assert terr < 1e-9
            lastf=f
            x=y
            if t>2 and abs(fp)<1e-12:
                rows.append(dict(t=t+1,F=fp,loss=fp*fp/2,energy=ep,Q=qp,
                                 m_NTK=m*math.fsum(gi*gi for gi in gp)))
                break
        audits.append(dict(label=label,m=m,h=h,sum_F_squared=sumsq,
                           sum_bound=e0/(h*(2-h)),rows=rows))

# Independent gradient check at a post-exit state with a nonzero residual.
label,m,x = initials[-3]
f,q,e,g = state(x,m)
for k,gi in enumerate(g):
    xp,xm=x[:],x[:]
    xp[k]+=1e-6
    xm[k]-=1e-6
    fd_error=max(fd_error,abs((state(xp,m)[0]-state(xm,m)[0])/2e-6-gi))
assert fd_error<1e-7

# Sharpness of the general bounded-feature lemma, not of the tanh model.
# Fixed features v_i=1 give F^+=(1-h)F exactly.
boundary=[]
for h in map(R,('1.999','2','2.001')):
    a=R(1)
    values=[]
    for t in range(8):
        values.append(a)
        a=(1-h)*a
    if h<2: assert abs(values[-1])<1
    if h==2: assert values==[R((-1)**t) for t in range(8)]
    if h>2: assert abs(values[-1])>1
    boundary.append(dict(h=str(h),values=[str(x) for x in values]))

summary=dict(status='PASS',exact_identity_cases=exact_cases,
             exact_spectral_cases=rank_one_cases,
             initial_energy_bound=float(e0_bound),sum_F2_bound=str(sum_F2),
             sum_L_bound=str(sum_L),sum_L_decimal=float(sum_L),
             full_network_trajectories=len(audits),
             maximum_steps=max(len(a['rows']) for a in audits),
             max_energy_identity_error=max_identity_error,
             max_telescoping_error=max_telescoping_error,
             finite_difference_error=fd_error,
             nonmonotone_continuation=growth_example,
             largest_terminal_residual=max(abs(a['rows'][-1]['F']) for a in audits),
             nice=os.getpriority(os.PRIO_PROCESS,0),
             rss_bytes=resource.getrusage(resource.RUSAGE_SELF).ru_maxrss,
             seconds=time.monotonic()-start)
assert summary['rss_bytes']<1_000_000_000
with open('convergence_verification.json','w') as out:
    json.dump(dict(summary=summary,audits=audits,bounded_feature_boundary=boundary),out,indent=2)
print(json.dumps(summary,indent=2))
