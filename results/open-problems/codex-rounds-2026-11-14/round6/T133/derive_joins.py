"""Exact endpoint jets of the rational candidate envelope."""
import os
for key in ('OMP_NUM_THREADS','OPENBLAS_NUM_THREADS','MKL_NUM_THREADS',
            'VECLIB_MAXIMUM_THREADS'):
    os.environ[key] = '1'
import json
from pathlib import Path
import resource
import signal
import sys
import time
signal.alarm(180)
resource.setrlimit(resource.RLIMIT_CPU, (180,180))
start=time.monotonic()
import sympy as s
z,w=s.symbols('z w')
A=lambda v:(1+v*v)**3/(2*v*(1-v)*(3-v*v)*(v*v+4*v+1))
f=lambda v:v*(v**4+7)/(6*(1-v)*(1+v)*(3-v*v))
D=lambda g:s.factor(((1+z*z)*s.diff(g,z)-(1+w*w)*s.diff(g,w))/6)
# Divide the tangent equation by b. These coefficients are regular at w=0.
alpha=s.cancel(A(z)/A(w))
eta=s.cancel((f(z)+f(w))/A(w))
alpha1=D(alpha)
eta1=D(eta)
X=s.factor(eta1/alpha1)
Y=s.factor(eta-alpha*X)
xp=D(X); yp=D(Y)
xpp=D(xp); ypp=D(yp)
jets={name:s.factor(g.subs(w,0)) for name,g in
      [('kappa',X),('Y',Y),('speed',xp),('Yprime',yp),
       ('Xsecond',xpp),('Ysecond',ypp)]}
jets['curvature']=s.factor(jets['Ysecond']/jets['speed']**2)
# T -> delta-T sends tan(T/3) to tan(pi/4-T/3).
complement=(1-z)/(1+z)
assert s.cancel(jets['kappa']+jets['kappa'].subs(z,complement)-1)==0
jets['curvature_difference']=s.factor(jets['curvature']-
                                      jets['curvature'].subs(z,complement))
assert jets['Y']==jets['Yprime']==0
assert jets['curvature_difference']==0
aval=A(z)
third=s.factor(((1+z*z)*s.diff(aval,z)/3-aval)/jets['speed']**2-
               aval*jets['Xsecond']/jets['speed']**3)
jets['equal_weight_third_graph_derivative']=s.simplify(third.subs(z,s.sqrt(2)-1))
assert jets['equal_weight_third_graph_derivative']!=0
for key,value in jets.items():
    print(key,'=',value)
Path('endpoint_formulas.json').write_text(json.dumps(
    {key:str(value) for key,value in jets.items()},indent=2)+'\n')
rss=resource.getrusage(resource.RUSAGE_SELF).ru_maxrss
rss_bytes=rss if sys.platform=='darwin' else rss*1024
assert rss_bytes<1024**3
print('resources',json.dumps({'elapsed_seconds':time.monotonic()-start,
    'peak_rss_MiB':rss_bytes/1024**2,'nice':os.getpriority(os.PRIO_PROCESS,0)}))
