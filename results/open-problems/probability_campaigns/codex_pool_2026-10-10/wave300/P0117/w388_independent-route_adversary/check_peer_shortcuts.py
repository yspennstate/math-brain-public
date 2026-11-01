"""Fresh small exact audit controls; no peer file or original measurement is written."""
from fractions import Fraction as F
from itertools import product
from math import log, log1p
from pathlib import Path
import json
import time

started,cpu=time.monotonic(),time.process_time()
gate={"id":"w388-peer-shortcuts-20261010-v1","max_worlds":256,"max_cpu_seconds":1,
      "max_wall_seconds":30,"no_gpu":True,"scope":"exact finite pattern/entropy controls only"}
values=[F(9,8),F(11,8),F(13,8),F(15,8)]
fixed=selected=worlds=0
for a,b,c,d in product(values,repeat=4):
    worlds+=1
    fixed+=int(min(a,b)>=F(7,4) and max(c,d)<=F(5,4))
    chosen,other=((a,b),(c,d)) if a+b<=c+d else ((c,d),(a,b))
    selected+=int(min(chosen)>=F(7,4) and max(other)<=F(5,4))
assert (worlds,fixed,selected)==(256,1,0)
entropy=[]
for n in (2,4,8,16,32):
    count=2**(n-1)
    marginal=F(1,2**n)
    union=count*marginal
    assert union==F(1,2) and count<2**n
    entropy.append({"n":n,"count":count,"marginal":str(marginal),"union":str(union),
        "strict_log_cardinality_gap":"log2 (constant, not diverging)"})
length=6
radius=2*(length+1)
diamond=1+2*radius*(radius+1)
eta=F(1,4)**(2*length+2)
c=-log1p(-float(eta))/(length*diamond)
assert diamond==421 and c>0 and c<log(3)
result={"gate":gate,"command":"python -X utf8 check_peer_shortcuts.py","worlds":worlds,
    "fixed_pattern_probability":str(F(fixed,worlds)),"selected_pattern_probability":"0",
    "entropy_counterexamples":entropy,"L":length,"D":diamond,"eta":str(eta),"c":c,
    "unrestricted_path_entropy_log3_minus_c":log(3)-c,
    "wall_seconds":time.monotonic()-started,"cpu_seconds":time.process_time()-cpu,
    "scope":"Whole high/low strata are classified exactly; no route-selection frequencies or asymptotic FPP conclusion are inferred."}
assert result["cpu_seconds"]<gate["max_cpu_seconds"] and result["wall_seconds"]<gate["max_wall_seconds"]
(Path(__file__).resolve().parent/"PEER_MEASUREMENTS.json").write_text(json.dumps(result,indent=2),encoding="utf-8")
print(json.dumps({"worlds":worlds,"fixed":"1/256","selected":"0","entropy_controls":len(entropy),"c":c,"cpu_seconds":result["cpu_seconds"]}))
