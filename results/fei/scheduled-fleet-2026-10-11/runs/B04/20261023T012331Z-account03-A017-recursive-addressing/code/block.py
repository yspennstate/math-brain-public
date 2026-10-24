from pathlib import Path
import json,time,sys
R=Path(__file__).resolve().parents[1];n=5;N=32;FULL=(1<<N)-1
inside=[x for x in range(N) if x&2];base=sum(((x>>0&1)*(x>>1&1)+(x>>2&1)*(x>>1&1)+(x>>2&1)*(x>>3&1)+(x>>4&1)*(x>>1&1)+(x>>4&1)*(x>>3&1))%2<<x for x in range(N))
low=[sum(1<<x for x in range(N) if not x>>j&1) for j in range(n)]
def swapped(f,j):s=1<<j;return ((f&low[j])<<s)|((f&(FULL^low[j]))>>s)
leaf_masks=[sum(1<<x for x in range(N) if (x>>2&1)==a and (x>>4&1)==b) for a in range(2) for b in range(2)]
child_masks=[sum(1<<x for x in range(N) if (x>>2&1)==a) for a in range(2)]
start=time.perf_counter();pilot='--pilot' in sys.argv;old=0;f=base;checks=cases=0;leaf_words=set();minchild=32;maxspent=0
for k in range(16 if pilot else 65536):
 gray=k^(k>>1)
 if k:f^=1<<inside[(gray^old).bit_length()-1]
 old=gray;diff=[f^swapped(f,j) for j in range(n)];c=[v.bit_count() for v in diff]
 assert c[2]>=8;checks+=1
 for mask in child_masks:
  v=(diff[4]&mask).bit_count();assert v>=4;checks+=1;minchild=min(minchild,v)
 A=c[2]+sum((diff[4]&mask).bit_count() for mask in child_masks)
 T=sum(sum((diff[j]&mask).bit_count() for j in [0,1,3]) for mask in leaf_masks)
 assert sum(c)==A+T;checks+=1;maxspent=max(maxspent,A)
 for mask in leaf_masks:
  xs=[x for x in range(N) if mask>>x&1];leaf_words.add(sum((f>>x&1)<<i for i,x in enumerate(xs)))
 cases+=1
out={'status':'PASS','pilot':pilot,'all_clean_half_inside_subsets':cases,'assertions':checks,'queried_original_physical_coordinates':[2,4],'remaining_physical_coordinates':[0,1,3],'all_histories_checked_per_parent':3,'minimum_second_query_influence':str(minchild)+'/16','complete_leaf_truth_tables_retained':len(leaf_words),'max_weighted_spent_influence':str(maxspent)+'/32','elapsed_seconds':time.perf_counter()-start}
(R/'out'/('block_pilot.json' if pilot else 'block_certificate.json')).write_text(json.dumps(out,indent=2)+'\n',encoding='utf-8',newline='\n');print(json.dumps(out))
