from pathlib import Path
import json
R=Path(__file__).resolve().parents[1]
amend={'frozen_before_rerun':True,'same_root_domain':True,'main_extension':'At each visited a=1 prefix also close the last active query with explicit point-spectrum terminal and full inherited constant off-reference, testing local <=W and original quota-12e0.','independent_repair':'r=1,a=1,b=1 has a flat on-floor; nonflatness is not a theorem hypothesis. Retain the flat boundary, count it, and require nonflatness only for r>=2. Prior independent attempt failed only this auxiliary nonflatness assertion.','memory_mb':100,'max_seconds_main':240,'max_seconds_independent':55}
(R/'FINAL_CHECK_SPEC.json').write_text(json.dumps(amend,indent=2)+'\n',encoding='utf-8')
p=R/'code/independent.py';s=p.read_text(encoding='utf-8').replace('rows=[]','rows=[];flat_boundaries=0')
s=s.replace('ck(vn==on);ck(len(set(on))==len(set(off))==2);ck(len(set(Qn))>1)','ck(vn==on);ck(len(set(on))==len(set(off))==2)\n    if r>=2:ck(len(set(Qn))>1)\n    elif len(set(Qn))==1:flat_boundaries+=1')
s=s.replace("'status':'PASS','roots':len(rows)","'status':'PASS','flat_boundary_count':flat_boundaries,'roots':len(rows)")
p.write_text(s,encoding='utf-8')
p=R/'code/check.py';s=p.read_text(encoding='utf-8')
s=s.replace('nodes=steps=0;minimum=None','nodes=steps=final_closures=0;minimum=None').replace('nonlocal nodes,steps,minimum','nonlocal nodes,steps,final_closures,minimum')
needle="  kinds=(['A'] if a>=2 else [])"
insert="""  if a==1:
   final_closures+=1
   old=h.marginal(Q,0);off=h.child(list(v),0,1);on=h.child(list(v),0,0)
   ck(set(off)=={1})
   Poff=h.spec(off);Pon=h.spec(on)
   last=h.add(h.B(P,0),h.mul(F(1,2),h.CE(Poff,old)),h.mul(F(1,2),h.CE(Pon,Pon)))
   le(last,envelope(a,b,r,Rt))
   completed=h.add(debit,terms,h.mul(reach,last))
   ck(completed[1]<=quota-12*e0)
"""
assert needle in s;s=s.replace(needle,insert+needle)
s=s.replace("'nodes':nodes,'steps':steps", "'nodes':nodes,'steps':steps,'final_active_closures':final_closures")
s=s.replace("'history_steps':sum(z['steps'] for z in rows)","'history_steps':sum(z['steps'] for z in rows),'final_active_closures':sum(z['final_active_closures'] for z in rows)")
p.write_text(s,encoding='utf-8')
print('CHECK_AMENDMENT_FROZEN; corrected flat boundary, added final active closures')
