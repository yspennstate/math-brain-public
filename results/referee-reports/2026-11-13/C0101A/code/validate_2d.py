import os
os.environ['MPLCONFIGDIR']=str(__import__('pathlib').Path(__file__).resolve().parents[1]/'data'/'mplconfig')
import json,time
from fractions import Fraction as F
from pathlib import Path
from periodic import search_phases,verify
from apollonian import circles,circle_matrix
ROOT=Path(__file__).resolve().parents[1]

def main():
 start=time.monotonic();cs=circles(100)
 (ROOT/'data'/'apollonian_circles.json').write_text(json.dumps(cs))
 results=[];certs=[]
 for c in cs:
  if c[0]>25 or not 0<=F(c[2],c[0])<=2:continue
  r=search_phases(circle_matrix(c),max_rounds=10000)
  cert=r.pop('certificate',None)
  if cert:
   r['independent_check']=verify(cert,True);certs.append({'circle':c,'certificate':cert})
  results.append({'circle':c,**r})
  print('circle',c,r['status'],'phases',r.get('phases_tried'),flush=True)
 (ROOT/'data'/'validation_2d_circles.json').write_text(json.dumps(results,indent=2))
 (ROOT/'data'/'certificates_2d.json').write_text(json.dumps(certs))
 grid=[];r=F(1,4)
 # At trace r, only circles with curvature <=1/r can dominate A.
 for ia in range(9):
  for ib in range(9):
   a,b=F(ia,4),F(ib,4)
   expected=any(F(1,c)>=r and (a-F(x,c))**2+(b-F(y,c))**2<=(F(1,c)-r)**2 for c,x,y in cs if c<=4)
   A=[[(r+a)/2,b/2],[b/2,(r-a)/2]]
   out=search_phases(A,max_rounds=2000)
   cert=out.pop('certificate',None)
   if cert:out['independent_check']=verify(cert)
   grid.append({'a':str(a),'b':str(b),'trace':str(r),'LPS_membership':expected,**out})
   assert not cert or expected
 (ROOT/'data'/'validation_2d_grid.json').write_text(json.dumps(grid,indent=2))
 import matplotlib
 matplotlib.use('Agg')
 import matplotlib.pyplot as plt
 from matplotlib.patches import Circle
 fig,axes=plt.subplots(1,2,figsize=(11,5))
 for c,x,y in cs:
  if 0<=F(y,c)<=2:axes[0].add_patch(Circle((x/c,y/c),1/c,fill=False,lw=.6))
 axes[0].set(xlim=(0,2),ylim=(0,2),aspect='equal',title='Apollonian band: curvature <=100',xlabel='a',ylabel='b')
 for out in grid:
  color='tab:blue' if out['status']=='member' else 'white'
  axes[1].scatter(float(F(out['a'])),float(F(out['b'])),c=color,edgecolors='black',s=45,
                  marker='o' if out['LPS_membership'] else 's')
 axes[1].set(xlim=(-.1,2.1),ylim=(-.1,2.1),aspect='equal',title='Trace 1/4: circles=LPS yes; blue=certificate',xlabel='a',ylabel='b')
 fig.tight_layout();fig.savefig(ROOT/'data'/'apollonian_validation.svg');plt.close(fig)
 summary={'circles_generated':len(cs),'maximal_points_tested':len(results),
          'maximal_points_certified':sum(x['status']=='member' for x in results),
          'grid_points':len(grid),'grid_LPS_members':sum(x['LPS_membership'] for x in grid),
          'grid_certified':sum(x['status']=='member' for x in grid),
          'grid_false_positives':sum(x['status']=='member' and not x['LPS_membership'] for x in grid),
          'seconds':time.monotonic()-start}
 (ROOT/'data'/'validation_2d_summary.json').write_text(json.dumps(summary,indent=2));print(summary,flush=True)
if __name__=='__main__':main()
