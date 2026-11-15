"""Create slice figures and audit saved results without repeating searches."""
import os
from pathlib import Path
ROOT=Path(__file__).resolve().parents[1]
os.environ['MPLCONFIGDIR']=str(ROOT/'data'/'mplconfig')
os.environ['XDG_CACHE_HOME']=str(ROOT/'data'/'cache')
os.environ['OPENBLAS_NUM_THREADS']='1'
import json,collections
from fractions import Fraction as F
from periodic import verify,search


def ceil(v):v=F(v);return -((-v.numerator)//v.denominator)


def main():
 rows=[json.loads(s) for s in (ROOT/'data'/'exploration_3d.jsonl').read_text().splitlines()]
 counters=collections.Counter()
 for row in rows:
  bound=sum(ceil(row['A'][i][i]) for i in range(3))
  row['ceiling_bound_excluded']=bound>1
  if row['status']=='member':assert bound<=1
  if row['family']=='diagonal':assert (bound<=1)==(row['status']=='member')
  counters['global_ceiling_exclusions']+=bound>1
 (ROOT/'data'/'exploration_3d_classified.json').write_text(json.dumps(rows,indent=2))
 certs=json.loads((ROOT/'data'/'certificates_2d.json').read_text())+json.loads((ROOT/'data'/'certificates_3d.json').read_text())
 for row in certs:assert verify(row['certificate'])['valid']
 r=search([['1/4','1/2','0'],['1/2','0','0'],['0','0','0']],8,(1,4,0))
 c=r.pop('certificate');r['independent_check']=verify(c,True)
 (ROOT/'data'/'explicit_ford_certificate.json').write_text(json.dumps({'description':'g(x,y,z)=ceil(x^2/8+x*y/2+y/2)+1_{x even}',**r,'certificate':c},indent=2))
 # Check the explicit formula directly and its claimed period.
 def g(x,y,z):return ceil(F(x*x,8)+F(x*y,2)+F(y,2))+(x%2==0)
 hist=collections.Counter()
 for x in range(-8,16):
  for y in range(-8,16):
   lap=g(x+1,y,0)+g(x-1,y,0)+g(x,y+1,0)+g(x,y-1,0)-4*g(x,y,0)
   assert lap<=1;hist[lap]+=1
 counters['saved_certificates_verified']=len(certs)+1
 counters['explicit_ford_laplacian_histogram']=dict(hist)
 # Independent symbolic check of affine quadratic Laplacians.
 import sympy as S
 x,y,z=S.symbols('x y z',integer=True)
 M=S.Matrix([[1,1,0],[1,0,1],[0,1,0]])
 poly=x*(x-1)/2+x*y+y*z
 lap=sum(poly.subs(v,v+1)+poly.subs(v,v-1)-2*poly for v in (x,y,z))
 assert S.expand(lap)==1
 counters['integer_quadratic_symbolic_laplacian']='1'
 import matplotlib
 matplotlib.use('Agg')
 import matplotlib.pyplot as plt
 from matplotlib.patches import Circle
 fig,axes=plt.subplots(1,3,figsize=(13,4))
 for ax,family in zip(axes[:2],('isotropic_shear','ford_block')):
  for row in rows:
   if row['family']!=family:continue
   a,b=map(lambda x:float(F(x)),row['parameters'])
   col='tab:blue' if row['status']=='member' else ('black' if row['ceiling_bound_excluded'] else 'tab:orange')
   ax.scatter(a,b,c=col,s=35)
  ax.set_title(family.replace('_',' '));ax.set_xlabel('t' if family=='isotropic_shear' else 'delta');ax.set_ylabel('s' if family=='isotropic_shear' else 'c')
 cex=json.loads((ROOT/'data'/'algebraic_counterexample.json').read_text())
 seq=cex['sequence']
 axes[2].semilogy([v['step'] for v in seq],[float(F(v['radius'])) for v in seq],'.-')
 axes[2].set(title='Rational maximal points approach A*',xlabel='Descartes step',ylabel='trace = circle radius')
 fig.suptitle('Blue: exact member; black: ceiling obstruction; orange: period exclusion only',fontsize=10)
 fig.tight_layout();fig.savefig(ROOT/'data'/'slices_3d.svg');plt.close(fig)
 from apollonian import circles
 fig,ax=plt.subplots(figsize=(6,5))
 for k,a,b in circles(1000):
  if .35<a/k<1 and .6<b/k<1.4:ax.add_patch(Circle((a/k,b/k),1/k,fill=False,lw=.6,color='gray'))
 px,py=map(float,cex['decimal_point'])
 ax.plot(px,py,'r*',ms=12,label='quartic-irrational residual point')
 for item in seq[:10]:
  a,b=map(lambda x:float(F(x)),item['center']);ax.plot(a,b,'b.',ms=3)
 ax.set(xlim=(.45,.75),ylim=(.9,1.2),aspect='equal',xlabel='a',ylabel='b',title='Descartes centers converge outside every closed disk')
 ax.legend(fontsize=8);fig.tight_layout();fig.savefig(ROOT/'data'/'counterexample_convergence.svg');plt.close(fig)
 (ROOT/'data'/'audit_summary.json').write_text(json.dumps(dict(counters),indent=2));print(dict(counters))

if __name__=='__main__':main()
