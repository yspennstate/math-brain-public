import json
from fractions import Fraction as F
from pathlib import Path
ROOT=Path(__file__).resolve().parents[1]
def main():
 p=json.loads((ROOT/'out'/'transitive_certificates.json').read_text())
 c=json.loads((ROOT/'out'/'child_certificates.json').read_text())
 r=next(r for r in p['records'] if r['name']=='cyclic-window-10-2-1')
 assert all(F(other['H_over_I']['upper'])<F(r['H_over_I']['lower']) for other in p['records'] if other['name']!=r['name'])
 boxes={}
 for key in ['H_over_I','B_over_I','B_over_H']:
  low=F(r[key]['lower']);high=F(r[key]['upper']);scale=10**10
  floor=(low*scale).numerator//(low*scale).denominator
  ceil=-((-high*scale).numerator//(-high*scale).denominator)
  assert F(floor,scale)<=low<=high<=F(ceil,scale)
  boxes[key]={'lower':str(F(floor,scale)),'upper':str(F(ceil,scale))}
 result={'finite_max_HI_case':r['name'],'finite_max_certified_by_disjoint_intervals':True,'benchmark_boxes':boxes,'family_summaries':{},'selected_first_children':[]}
 for fam in ['tribes','recursive_majority','cyclic_window_threshold','odd_cyclic_threshold']:
  rows=[r for r in p['records'] if r['family']==fam]
  result['family_summaries'][fam]={'cases':len(rows),'max_HI_display':max((r['H_over_I']['display_midpoint'],r['name']) for r in rows),'max_BI_display':max((r['B_over_I']['display_midpoint'],r['name']) for r in rows),'B_zero_cases':sum(not r['B_prime_log'] for r in rows),'min_BH_display':min((r['B_over_H']['display_midpoint'],r['name']) for r in rows if r['B_over_H'])}
 for child in c['records']:
  if child['parent'] in ['cyclic-window-10-2-1','maj3-depth-2','odd-cyclic-11','tribes-4-3']:
   result['selected_first_children'].append({'parent':child['parent'],'branch':child['branch'],'I_child':child['I_child'],'min_relevant_B_over_I':child['min_relevant_B_over_I']})
 (ROOT/'out'/'ANALYSIS.json').write_text(json.dumps(result,indent=2)+'\n',encoding='utf-8')
 print(json.dumps(result,indent=2))
if __name__=='__main__':main()
