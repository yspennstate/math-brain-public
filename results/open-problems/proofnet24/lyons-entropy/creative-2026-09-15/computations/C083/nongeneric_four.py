"""Two bounded optimizations at a four-site nongeneric endpoint stratum.

B has orthogonal rows; endpoint eigenvectors have an exactly zero coordinate,
so the fully-supported four-site root boundary theorem does not apply.
"""
from pathlib import Path
import json
import numpy as np
from scipy.optimize import minimize
from search import hessian

OUT=Path(__file__).resolve().parent
def kernel(x):
    theta,small,loggap=x;large=.5-10**loggap
    c=np.cos(theta);t=np.sin(theta)
    B=np.array([[large*c,large*t],[-small*t,small*c]])
    K=.5*np.eye(4,dtype=complex);K[:2,2:]=B;K[2:,:2]=B.T
    return K

def main():
    bounds=[(.2,1.3),(.1,.44),(-7,-2)];rows=[]
    for initial in [[.55,.2,-4],[1.0,.4,-6]]:
        best=[-np.inf,None];calls=[0]
        def fun(x):
            calls[0]+=1;v=hessian(kernel(x))
            if v>best[0]:best[:]=[v,np.array(x)]
            return -v
        first=-fun(initial)
        res=minimize(fun,initial,method='Powell',bounds=bounds,
                     options={'maxfev':240,'maxiter':2,'xtol':2e-3,'ftol':2e-5})
        row=hessian(kernel(best[1]),True)
        row.update({'parameters':best[1].tolist(),'initial_parameters':initial,
                    'initial_lambda_max':first,'bounds':bounds,'evaluations':calls[0],
                    'optimizer_status':int(res.status),'endpoint_zero_coordinate':1,
                    'endpoint_eigenvectors_formula':'(e0,+/-[cos(theta),sin(theta)])/sqrt(2)'})
        rows.append(row)
        print('nongeneric four:',row['lambda_max'],'evaluations:',calls[0],flush=True)
    (OUT/'nongeneric_four_results.json').write_text(json.dumps({'status':'complete','rows':rows},indent=2)+'\n')

if __name__=='__main__':main()
