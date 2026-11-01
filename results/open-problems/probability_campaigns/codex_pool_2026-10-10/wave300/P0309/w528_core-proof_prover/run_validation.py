"""Arm a fresh bounded gate immediately before the foreground checker."""
import datetime, json, pathlib, runpy

ROOT=pathlib.Path(__file__).resolve().parent
now=datetime.datetime.now(datetime.timezone.utc)
gate={
    'gate_id':'w528-p0309-small-check-'+now.strftime('%Y%m%dT%H%M%SZ'),
    'created_utc':now.isoformat(),'purpose':'Exact derivative, atomic, cone, shell, conditional-repair, and DRAFT checks',
    'authorized_scope':'Fresh small CPU-only deterministic checks in the assigned w528 folder',
    'max_evaluations':5000,'max_cpu_seconds':5,'max_wall_seconds':60,'max_python_allocation_bytes':16*1024*1024,
    'gpu':False,'training':False,'child_agents':False,'external_data_loads':False,'status':'armed',
    'interpreter_baseline_excluded_from_allocation_cap':True,
    'pressure_policy':'Retain launcher priority; no loaded models, worker launch, GPU work, or changes to the live governor. Existing external resource gates remain in force.'
}
(ROOT/'COMPUTE_GATE.json').write_text(json.dumps(gate,indent=2)+'\n',encoding='utf-8')
try:
    runpy.run_path(str(ROOT/'verify_packet.py'),run_name='__main__')
except BaseException as exc:
    gate['status']='FAILED';gate['failure']=repr(exc)
    (ROOT/'COMPUTE_GATE.json').write_text(json.dumps(gate,indent=2)+'\n',encoding='utf-8')
    raise
