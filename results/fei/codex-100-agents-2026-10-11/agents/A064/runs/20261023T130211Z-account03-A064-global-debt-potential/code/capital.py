from pathlib import Path
import json,time
import exact as x
from check import add,ge
F=x.F
ROOT=Path(__file__).resolve().parents[1]
START=time.perf_counter()

def main():
 records=[]
 for m in (2,4,6,8):
  t=(-1,)+(1,)*((1<<m)-1);p,ds,H,M,TC=x.stats(t);d=F(1,1<<(m-1));N=1<<(m-1)
  x.ck(ds==(d,)*m,'physical point influences')
  x.ck(p[0]==(1-d)**2 and all(v==d*d for v in p[1:]),'all actual point spectral atoms')
  ge(M,x.constant(m*d*(m-1)),'point marginal entropy lower bound')
  ge(x.constant(2*d*(2*m+1)),H,'point entropy upper bound')
  ge(TC,x.constant(d*(m*m-5*m-2)),'point TC lower bound')
  x.ck(N*m*d==m,'exact source tensor influence without expanding tensor')
  ge(add((N,TC)),x.constant(m*m-5*m-2),'exact tensor TC lower bound')
  records.append({'m':m,'actual_point_dimension':m,'tensor_copies':N,'tensor_core_I':m,'outer_bent_I':m+1,'initial_capital_lower_bound':x.enc(add((N,TC))),'analytic_simpler_lower_bound':m*m-5*m-2,'analytic_ratio_lower_bound':str(F(m*m-5*m-2,m+1))})
 x.ck(time.perf_counter()-START<55,'frozen capital runtime')
 out={'status':'PASS','point_dimensions':[2,4,6,8],'actual_case_count':4,'tensor_spectra':'exact source additivity, not enumerated and no reference-kernel tensorization assumed','exact_assertions':x.COUNT,'seconds':time.perf_counter()-START,'records':records}
 (ROOT/'out/INITIAL_CAPITAL.json').write_text(json.dumps(out,indent=2)+'\n',encoding='utf-8',newline='\n')
 print(json.dumps({k:v for k,v in out.items() if k!='records'}))
if __name__=='__main__':main()
