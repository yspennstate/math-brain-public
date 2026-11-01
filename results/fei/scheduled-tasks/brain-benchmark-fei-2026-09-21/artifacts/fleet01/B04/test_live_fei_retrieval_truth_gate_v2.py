import hashlib, importlib.util, json, tempfile, unittest
from datetime import datetime, timezone
from pathlib import Path
MOD_PATH=Path(__file__).with_name('live_fei_retrieval_truth_gate_v2.py')
spec=importlib.util.spec_from_file_location('gatev2',MOD_PATH); m=importlib.util.module_from_spec(spec); spec.loader.exec_module(m)
FAKE='''#!/usr/bin/env python3\nimport argparse,hashlib,json\nfrom pathlib import Path\np=argparse.ArgumentParser(); p.add_argument("--order"); p.add_argument("--research-state"); p.add_argument("--results"); p.add_argument("--expected-order-git-blob"); p.add_argument("--expected-state-git-blob"); a=p.parse_args(); raw=Path(a.results).read_bytes(); print(json.dumps({"status":"PASS_LIVE_FEI_TRUTH_BOUND","full_brain_connected":False,"order_git_blob":a.expected_order_git_blob,"research_state_git_blob":a.expected_state_git_blob,"results_sha256":hashlib.sha256(raw).hexdigest()}))\n'''
def gb(b): return hashlib.sha1(b'blob '+str(len(b)).encode()+b'\0'+b).hexdigest()
def sh(b): return hashlib.sha256(b).hexdigest()
class T(unittest.TestCase):
 def setUp(self):
  self.t=tempfile.TemporaryDirectory(); d=Path(self.t.name); self.d=d; self.v=d/'v.py'; self.o=d/'o'; self.s=d/'s'; self.r=d/'r'; self.w=d/'w'; self.v.write_text(FAKE); self.o.write_text('o'); self.s.write_text('s'); self.now=datetime(2026,9,21,22,15,tzinfo=timezone.utc); self.x={"schema":m.WITNESS_SCHEMA,"source":m.WITNESS_SOURCE,"fresh_main_resolved":True,"joint_pointer_id":m.POINTER_ID,"observed_utc":"2026-09-21T22:14:30Z","control_commit":"1"*40,"control_revision":"r","readme_git_blob":"2"*40,"order_git_blob":gb(self.o.read_bytes()),"research_state_git_blob":gb(self.s.read_bytes())}; self.bind()
 def tearDown(self): self.t.cleanup()
 def bind(self):
  raw=json.dumps(self.x,sort_keys=True,separators=(',',':')).encode(); self.w.write_bytes(raw); self.r.write_text(json.dumps({"joint_pointer_id":m.POINTER_ID,"control_commit":self.x["control_commit"],"control_revision":self.x["control_revision"],"readme_git_blob":self.x["readme_git_blob"],"order_git_blob":self.x["order_git_blob"],"research_state_git_blob":self.x["research_state_git_blob"],"truth_witness_sha256":sh(raw),"full_brain_connected":False}))
 def run(self,**k): return m.validate(v1_gate=self.v,order_path=self.o,state_path=self.s,results_path=self.r,witness_path=self.w,now=self.now,expected_v1_blob=gb(self.v.read_bytes()),**k)
 def test_pass(self): self.assertEqual(self.run()["status"],"PASS_LIVE_FEI_TRUTH_BOUND_V2")
 def test_stale(self): self.x["observed_utc"]="2026-09-21T21:00:00Z"; self.bind(); self.assertRaisesRegex(m.GateError,'stale',self.run)
 def test_future(self): self.x["observed_utc"]="2026-09-21T22:20:00Z"; self.bind(); self.assertRaisesRegex(m.GateError,'future',self.run)
 def test_result_binding(self): q=json.loads(self.r.read_text()); q['control_commit']='9'*40; self.r.write_text(json.dumps(q)); self.assertRaisesRegex(m.GateError,'control_commit',self.run)
 def test_order_drift(self): self.o.write_text('x'); self.assertRaisesRegex(m.GateError,'ORDER does not match',self.run)
 def test_v1_pin(self): self.assertRaisesRegex(m.GateError,'v1 gate Git blob mismatch',lambda:m.validate(v1_gate=self.v,order_path=self.o,state_path=self.s,results_path=self.r,witness_path=self.w,now=self.now,expected_v1_blob='0'*40))
 def test_source(self): self.x['source']='fixture'; self.bind(); self.assertRaisesRegex(m.GateError,'source mismatch',self.run)
 def test_max_age(self): self.assertRaisesRegex(m.GateError,'1..3600',lambda:self.run(max_age_seconds=0))
if __name__=='__main__': unittest.main()
