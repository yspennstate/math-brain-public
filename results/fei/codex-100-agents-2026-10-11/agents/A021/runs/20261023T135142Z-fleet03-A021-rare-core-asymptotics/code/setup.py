from pathlib import Path
import hashlib,json
r=Path(__file__).resolve().parents[1];(r/'out').mkdir(exist_ok=True)
p=r.parent/'20261023T112941Z-fleet03-A021-rare-core-asymptotics/code/arithmetic.py';(r/'code/arithmetic.py').write_bytes(p.read_bytes())
obj={'helper_version':{'arithmetic':hashlib.sha256(p.read_bytes()).hexdigest(),'checker':hashlib.sha256((r/'code/check.py').read_bytes()).hexdigest()},'family':'actual t2 tensor point-defect seed with BOTH adjacent vertices0,1 multiplied by SAME balanced odd majority; actual selector h=y*a','pilot_control_widths':[3],'main_control_widths':[3,5,7],'case_count':3,'max_total_bits':13,'symmetry':'none; all physical coordinates checked','arithmetic':'integer FWHT, exact Fraction upper-set V and prime logs with40-term rational enclosures','memory_estimate_mb':180,'pilot_max_seconds':60,'main_max_seconds':120,'asymptotic_bridge':'analytic majority coefficient induction and uniform curvature bounds, not extrapolation'}
(r/'SEARCH_SPEC.json').write_text(json.dumps(obj,indent=2)+'\n',encoding='utf-8');print('SPEC_FROZEN')
