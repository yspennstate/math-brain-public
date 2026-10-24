"""Standard-library numerical check of the exact formulas in the proof."""
import json, math, platform
t=math.log(1+math.sqrt(3))
r1=lambda t:2*math.exp(-3*t)-math.exp(-t)
r2=lambda t:2*math.exp(-3*t)+math.exp(-t)
j1=lambda t:-1/3+math.exp(-t)-2/3*math.exp(-3*t)
j2=lambda t:5/3-math.exp(-t)-2/3*math.exp(-3*t)
errors={"J1_crossing":abs(j1(t)),"r1_crossing":abs(r1(t)-(math.sqrt(3)-2)),"r2_crossing":abs(r2(t)-(2*math.sqrt(3)-3)),"J2_crossing":abs(j2(t)-(3-math.sqrt(3)))}
assert max(errors.values())<1e-14
assert j1(2)<-.19
print(json.dumps({"kind":"numerical formula checks, not simulation or proof","python":platform.python_version(),"checks_passed":5,"errors":errors,"candidate_crossing_time":t,"candidate_J1_at_2":j1(2),"candidate_r1_at_crossing":r1(t),"candidate_r2_at_crossing":r2(t),"candidate_J2_at_crossing":j2(t)},indent=2))
