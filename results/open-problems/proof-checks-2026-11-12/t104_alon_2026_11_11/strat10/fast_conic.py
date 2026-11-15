"""NUMERICAL only: vectorized conic discovery, unchanged rational acceptance."""
import os
for k in ('OPENBLAS_NUM_THREADS','OMP_NUM_THREADS','MKL_NUM_THREADS','VECLIB_MAXIMUM_THREADS'):os.environ[k]='1'
import ast,inspect,types
import numpy as np
from scipy import sparse
import clarabel
import cells,cubic_cells,padding
from cubic_discovery import SETTINGS
COUNT=30
class Floats(ast.NodeTransformer):
    def visit_Call(self,node):
        node=self.generic_visit(node)
        if isinstance(node.func,ast.Name)and node.func.id=='F':
            if len(node.args)==2:return ast.copy_location(ast.BinOp(node.args[0],ast.Div(),node.args[1]),node)
            return ast.copy_location(ast.Call(ast.Name('float',ast.Load()),node.args,[]),node)
        return node

def compile_functions(functions,namespace):
    tree=ast.parse('\n'.join(inspect.getsource(f)for f in functions));tree=ast.fix_missing_locations(Floats().visit(tree));exec(compile(tree,'<numerical float formulas>','exec'),namespace)
old={};compile_functions([cells.base_value,cells.lower_value,cells.residual_blocks],old)
old['DIRECTIONS']=cells.DIRECTIONS
ns={'cells':types.SimpleNamespace(**{k:v for k,v in old.items()if k!='__builtins__'}),'CUBIC_DIRECTIONS':cubic_cells.CUBIC_DIRECTIONS}
compile_functions([cubic_cells.cubic_lower,cubic_cells.lower_value,cubic_cells.residual_blocks,padding.base_coefficients],ns)

def ctrl(x,axis):
    y=np.array(x,copy=True);sl=[slice(None)]*x.ndim;sl[axis]=1
    y[tuple(sl)]=2*np.take(x,1,axis=axis)-(np.take(x,0,axis=axis)+np.take(x,2,axis=axis))/2
    return y

def solve(verts,lo,hi,ahi,d_zero=False,alo=.56,allN=False):
    lo,hi,ahi,alo=map(float,(lo,hi,ahi,alo));p=np.array(verts,float).T
    pp=tuple(x[None,:,None,None]for x in p)
    aa=np.array([alo,(alo+ahi)/2,ahi])[None,None,:,None];rr=np.array([lo,(lo+hi)/2,hi])[None,None,None,:]
    units=np.r_[np.zeros((1,COUNT)),np.eye(COUNT)];vec=tuple(units[:,i,None,None,None]for i in range(COUNT))
    val=ns['lower_value'](pp,aa,rr,vec)
    values=[val]
    if allN:
        base=ns['base_coefficients'](pp,aa,rr);extra=val-ns['cells'].base_value(pp,aa,rr)
        values=[b/c+extra for b,c in zip(base,(16,8,1))]
    polys=np.concatenate([ctrl(ctrl(v,2),3).reshape(COUNT+1,-1)for v in values],axis=1)
    rows=np.c_[-(polys[1:]-polys[0]).T,np.ones(polys.shape[1])].tolist();rhs=polys[0].tolist()
    for i in range(20,COUNT):
        row=[0.]*(COUNT+1);row[i]=-1.;rows.append(row);rhs.append(0.)
    cones=[clarabel.NonnegativeConeT(len(rhs))]
    v2=tuple(units[:,i,None]for i in range(COUNT));r2=np.array([lo,(lo+hi)/2,hi])[None,:]
    blocks=ns['residual_blocks'](r2,v2)
    for b in blocks:
        b=[ctrl(np.broadcast_to(x,(COUNT+1,3)),1)for x in b]
        for k in range(3):
            soc=np.array([b[0][:,k]+b[2][:,k],b[0][:,k]-b[2][:,k],2*b[1][:,k]])
            rows.extend(np.c_[-(soc[:,1:]-soc[:,0,None]),np.zeros(3)].tolist());rhs.extend(soc[:,0].tolist());cones.append(clarabel.SecondOrderConeT(3))
    for i in range(4):
        for k,l in((2,1),(4,3)):
            for coeff in((1,1,0),(1,-1,0),(0,0,2)):
                row=[0.]*(COUNT+1);row[5*i]=-coeff[0];row[5*i+k]=-coeff[1];row[5*i+l]=-coeff[2];rows.append(row);rhs.append(0.)
            cones.append(clarabel.SecondOrderConeT(3))
    return clarabel.DefaultSolver(sparse.csc_matrix((COUNT+1,COUNT+1)),np.r_[np.zeros(COUNT),-1.],sparse.csc_matrix(rows),np.array(rhs),cones,SETTINGS).solve()
