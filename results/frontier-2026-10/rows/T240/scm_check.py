import numpy as np, importlib.util, sys
sys.argv=['x','0.5']
spec=importlib.util.spec_from_file_location('s','scm_plateau.py'); s=importlib.util.module_from_spec(spec)
import io,contextlib
with contextlib.redirect_stdout(io.StringIO()): spec.loader.exec_module(s)
eta=0.5
for eps in (1e-2,1e-3,1e-4):
    z=np.array([0.2,0.0,0.2,1e-3+eps,1e-3,1e-3,1e-3]); dt=0.1; t=0; tl=None
    while t<4000:
        z=z+dt*s.rhs(z,eta); t+=dt
        g=s.eg(z)
        if tl is None and abs(z[3]-z[4])>0.2: tl=t
    print('eps %.0e: specialised (|R11-R12|>0.2) at t=%s; t=4000: eg=%.2e R=%s Q=%s'%(eps,('%.0f'%tl) if tl else 'never',g,np.round(z[3:],3),np.round(z[:3],3)))
