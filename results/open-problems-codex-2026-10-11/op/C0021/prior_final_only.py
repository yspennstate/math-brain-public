"""Independently reconstruct archived P52 and check only its final cost/legality.
No intermediate patch-gain estimates are needed for a valid upper bound.
"""
import ast,pathlib,base64,zlib,time,ctypes
from fractions import Fraction
from functools import lru_cache
P=pathlib.Path(__file__).parent;started=time.monotonic();calls=0
class Mem(ctypes.Structure):
 _fields_=[('cb',ctypes.c_ulong),('PageFaultCount',ctypes.c_ulong)]+[(n,ctypes.c_size_t) for n in ['PeakWorkingSetSize','WorkingSetSize','QuotaPeakPagedPoolUsage','QuotaPagedPoolUsage','QuotaPeakNonPagedPoolUsage','QuotaNonPagedPoolUsage','PagefileUsage','PeakPagefileUsage']]
def _guard():
 global calls
 calls+=1
 if calls%2048:return
 if time.monotonic()-started>240:raise RuntimeError('bounded final-only time cap')
 m=Mem();m.cb=ctypes.sizeof(m);ctypes.windll.psapi.GetProcessMemoryInfo(ctypes.c_void_p(-1),ctypes.byref(m),m.cb)
 if m.WorkingSetSize>850000000:raise RuntimeError('bounded final-only memory cap')
src=(P/'prior_policy_checker.py').read_text();tree=ast.parse(src)
needed={'norm','queries','V','q_frac','lottery_frac','R_frac','child_opt_moves','base_policy','full'}
ns=globals()
for node in tree.body:
 if isinstance(node,ast.FunctionDef) and node.name in needed:
  s=ast.get_source_segment(src,node)
  if node.decorator_list:s='@lru_cache(None)\n'+s
  if node.name=='norm':s=s.replace('def norm(ch):\n','def norm(ch):\n    _guard()\n')
  exec(compile(s,'extracted_prior_definitions','exec'),ns)
patches={}
for node in tree.body:
 if isinstance(node,ast.Assign) and len(node.targets)==1 and isinstance(node.targets[0],ast.Name) and node.targets[0].id in {'BASE40_B85','EXTRA6_B85','EXTRA15_B85'}:
  patches.update(ast.literal_eval(zlib.decompress(base64.b85decode(ast.literal_eval(node.value))).decode()))
assert len(patches)==52
try:
 for s,ab in patches.items():assert ab in queries(s)
 @lru_cache(None)
 def final_cost(t):
  if t in ('+','-'):return Fraction(0)
  a,b=patches[t] if t in patches else base_policy(t)
  assert (a,b) in queries(t)
  return 1+(final_cost(a)+final_cost(b))/2
 cost=final_cost(full(4));assert cost==Fraction(1332467382289843607,36028797018963968)
 import json,math
 out=dict(cost=str(cost),decimal=float(cost),sigma_lower=1-math.log(float(cost))/(4*math.log(3)),patches=len(patches),policy_states=final_cost.cache_info().currsize,seconds=time.monotonic()-started,legal_actions_checked=True)
 (P/'prior_policy_verified.json').write_text(json.dumps(out,indent=2),encoding='utf8');print(out,flush=True)
except RuntimeError as e:print('INCOMPLETE',e,flush=True)
