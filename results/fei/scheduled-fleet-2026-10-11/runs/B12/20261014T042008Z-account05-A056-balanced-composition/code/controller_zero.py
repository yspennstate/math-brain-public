from check import *
start=time.perf_counter();count=0
cs=[tuple((1-v)//2 for v in table(1,k)) for k in range(4)]+[(1,0,0,0),(0,1,1,1)]
for c in cs:
 dims=(len(c).bit_length()-1,1,1,1)
 for gc,hc in [(6,12),(7,1),(12,10),(0,15)]:
  for weighted in [False,True]:
   for i in range(3,sum(dims)):
    E,O,C,D=check(c,table(2,gc),table(2,hc),dims,i,weighted)
    assert E==O==C=={};count+=1
result={'helper_version':'A056-controller-zero-release-v1','controller_queries':count,'erasure_outcome_calibration_KL':'ALL EXACTLY ZERO','result':'ALL PASS','seconds':time.perf_counter()-start}
(R/'out/controller_zero.json').write_text(json.dumps(result,indent=2)+'\n',encoding='utf-8');print(json.dumps(result,indent=2))
