from functools import lru_cache
from itertools import product
import pathlib,json
P=pathlib.Path(__file__).parent;rows=[]
for n in (5,7,9):
 center=n//2
 @lru_cache(None)
 def reaches_center(w):
  if w[center]==1:return True
  for j in range(n-1):
   if w[j]>w[j+1]:
    v=w[:j]+(w[j+1],w[j])+w[j+2:]
    if reaches_center(v):return True
  return False
 tested=0;left=0;right=0
 for w in product((0,1,2),repeat=n):
  # 0=vacancy in both, 1=discrepancy, 2=particle in both.
  left_condition=any(w[i]==1 and sum(x==0 for x in w[i+1:])>=center-i for i in range(center))
  right_condition=any(w[i]==1 and sum(x==2 for x in w[:i])>=i-center for i in range(center+1,n))
  if left_condition or right_condition:
   assert reaches_center(w),(n,w,left_condition,right_condition)
   tested+=1;left+=left_condition;right+=right_condition
 rows.append({'length':n,'all_color_words':3**n,'resource_sufficient_words':tested,'left_sufficient_words':left,'right_sufficient_words':right,'reachable_in_every_tested_case':True,'cached_states':reaches_center.cache_info().currsize})
(P/'reachability_checks.json').write_text(json.dumps(rows,indent=2),encoding='utf8')
print(json.dumps(rows))
