"""Directed simplex certificate on a nonuniform radial partition, with arbitrary centers."""
from pathlib import Path
import importlib.util,sys,hashlib
ROOT=Path(__file__).resolve().parents[1]
spec=importlib.util.spec_from_file_location('_t039_original_cell_core',ROOT/'scripts/certify_positive_cells.py')
core=importlib.util.module_from_spec(spec);sys.modules[spec.name]=core;spec.loader.exec_module(core)
import certify_positive_cells_centered as chooser
from scipy.special import ndtr,ndtri
np=core.np
original_majorant=core.majorant
class GridNumpy:
    def __getattr__(self,key):return getattr(np,key)
    def linspace(self,start,stop,num,*args,**kwargs):
        if float(start)==0. and float(stop)==8. and num>=129:
            n=int(num)-1;tail=n//8;bulk=n-tail
            sigma=1.6;split=4.
            mass=2*ndtr(split/sigma)-1
            t=np.linspace(0.,1.,bulk+1)
            inner=sigma*ndtri(.5+.5*mass*t);inner[0]=0.;inner[-1]=split
            outer=np.linspace(split,8.,tail+1)
            result=np.concatenate([inner[:-1],outer]);result[0]=0.;result[-1]=8.
            assert len(result)==num and np.all(np.diff(result)>0)
            return result
        return np.linspace(start,stop,num,*args,**kwargs)
core.np=GridNumpy()
def majorant(lo,hi,args,tabs):
    coefficients=chooser.choose_center((lo+hi)/2)
    core.pos.CENTER=tuple((float(c),) for c in coefficients)
    B,tail,info=original_majorant(lo,hi,args,tabs)
    info.update({'center_coefficients_binary64_hex':[float(c).hex() for c in coefficients],'center_selection':'Untrusted midpoint quartic fit; all subsequent bounds are directed.','partition':'Exact binary64 half-normal quantiles on [0,4] plus uniform cells on [4,8]. Quantile accuracy is not assumed.','graded_implementation_sha256':hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),'center_selection_code_sha256':hashlib.sha256(Path(chooser.__file__).read_bytes()).hexdigest()})
    return B,tail,info
core.majorant=majorant
if __name__=='__main__':raise SystemExit(core.main())
