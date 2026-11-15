"""Untrusted quartic-center selection followed by directed operator verification."""
from pathlib import Path
import hashlib
import certify_positive_cells_scaled as scaled
import certify_positive_cells as old
import measure_operator as measure
np,base,pos=old.np,old.base,old.pos
ROOT=old.ROOT

def choose_center(rho):
    A,_,_,x,w,jt=measure.matrix(rho,n=192,cutoff=16,nv=96,centered=False)
    u=np.sqrt(2*w)*np.exp(-x*x/2)/np.sqrt(jt)
    D=u[:,None]*np.column_stack([x**j for j in range(5)])
    norm=float(u@u);mom=D.T@u
    gram=2*norm*(D.T@D)+2*np.outer(mom,mom)
    rhs=2*(D.T@(A@u))
    coefficients=np.linalg.solve(gram,rhs)
    assert np.isfinite(coefficients).all()
    return coefficients

def majorant(lo,hi,args,tabs):
    coefficients=choose_center((lo+hi)/2)
    # Every coefficient is an exact dyadic choice. Optimality is never assumed.
    pos.CENTER=tuple((float(c),) for c in coefficients)
    B,tail,info=scaled.majorant(lo,hi,args,tabs)
    info.update({'center_coefficients_binary64_hex':[float(c).hex() for c in coefficients],'center_selection':'Untrusted numerical quartic fit at the slab midpoint. Only the subsequent interval bounds are used.','centered_implementation_sha256':hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),'selection_code_sha256':hashlib.sha256(Path(measure.__file__).read_bytes()).hexdigest()})
    return B,tail,info

old.majorant=majorant
if __name__=='__main__':raise SystemExit(old.main())
