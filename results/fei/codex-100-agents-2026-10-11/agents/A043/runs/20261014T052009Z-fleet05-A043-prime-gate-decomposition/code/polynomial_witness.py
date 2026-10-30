from pathlib import Path
import json,time
ROOT=Path(__file__).resolve().parents[1];start=time.perf_counter()
# Reuse only the already checked arithmetic/functions, not its661-case driver.
ns={ '__file__':str(ROOT/'code/check.py') }
prefix=(ROOT/'code/check.py').read_text(encoding='utf-8').split('grid=[Q(1,16)',1)[0]
exec(compile(prefix,str(ROOT/'code/check.py'),'exec'),ns)
Q=ns['Q'];p=[Q(1,2),Q(1,1024),Q(1,1048576),Q(1,16)]
record=ns['fixture'](p)
ratio=Q(record['poly_minus4T_overD']);D=Q(record['D'])
assert ratio<0
assert record['S_ge4T']=='PASS_CERTIFIED'
assert record['sharp_Cstar']=='PASS_CERTIFIED'
out={'helper':'A043-polynomial-slack-witness-v1','point':record,
     'exact_polynomial_gap':str(ratio*D),
     'false_statement':'For this prime and all interior laws, S_poly>=4T, S_poly=sum vi[2(di-|ci|)+|ci|(1-|ci|)^2]',
     'actual_log_slack':'S>=4T passes with rational log intervals at this witness; this is not a counterexample to S>=4T or sharp Cstar',
     'all_passed':True,'runtime_seconds':time.perf_counter()-start}
(ROOT/'out/polynomial_witness.json').write_text(json.dumps(out,indent=2)+'\n',encoding='utf-8')
print(json.dumps({'polynomial_gap':out['exact_polynomial_gap'],'actual_slack':record['S_ge4T'],'sharp_Cstar':record['sharp_Cstar'],'runtime_seconds':out['runtime_seconds']}))
