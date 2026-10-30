import json, tempfile, unittest
from pathlib import Path
import live_fei_retrieval_truth_gate_v1 as g

ORDER = f"directive {g.POINTER_ID}\n"
STATE = """Full FEI remains OPEN / NOT PROVED.
The proposed ALL-BOOLEAN Brownian closing budget and the exact positive-current O(J) budget are REFUTED at their stated scopes. This is NOT a counterexample to FEI.
The sharp comparisons are S<=pi M, P<=(pi^2/2-pi)M, and S+P<=(pi^2/2)M. They are kernel constants, not FEI constants.
A physical-block entropy payment Delta_Z H<=12 I_Z holds in the stated restricted regime. Twelve is NOT a universal FEI constant.
"""
D = "a"*64

def good_payload(ob, sb):
    common = dict(research_state_git_blob=sb, order_git_blob=ob, evidence_verified=True,
                  citation_binding_checked=True, query_digest=D, database_digest=D)
    cases = [
      dict(common, id="full_fei_status", status="OPEN_NOT_PROVED", claim="Full FEI remains open / not proved.", solved=False),
      dict(common, id="positive_current_budget_status", status="REFUTED_AT_STATED_SCOPE", claim="The positive-current O(J) budget is refuted at its stated scope; this is not a counterexample to FEI.", warnings=["superseded/refuted"], accepted_as_theorem=False, counterexample_to_fei=False),
      dict(common, id="kernel_constants_scope", status="PROVED_KERNEL_SCOPE", claim="S<=pi M, P<=(pi^2/2-pi)M, S+P<=(pi^2/2)M", scope="KERNEL_CONSTANTS_NOT_FEI_CONSTANTS"),
      dict(common, id="subcube_peeling_scope", status="PROVED_RESTRICTED_SCOPE", claim="Restricted result; Twelve is not a universal FEI constant.", coefficient="4(1+epsilon)", physical_block_payment="12 I_Z", universal_fei_constant=False),
    ]
    return dict(joint_pointer_id=g.POINTER_ID, research_state_git_blob=sb, order_git_blob=ob, full_brain_connected=False, cases=cases)

class T(unittest.TestCase):
    def run_gate(self, mutate=None, order=ORDER, state=STATE):
        with tempfile.TemporaryDirectory() as td:
            td=Path(td); op=td/'ORDER.md'; sp=td/'STATE.md'; rp=td/'r.json'
            op.write_text(order); sp.write_text(state)
            ob=g._git_blob_sha(op.read_bytes()); sb=g._git_blob_sha(sp.read_bytes())
            p=good_payload(ob,sb)
            if mutate: mutate(p)
            rp.write_text(json.dumps(p))
            return g.validate(op,sp,rp,ob,sb)
    def test_pass(self): self.assertEqual(self.run_gate()["status"],"PASS_LIVE_FEI_TRUTH_BOUND")
    def test_fei_solved_rejected(self):
        def m(p): p['cases'][0]['solved']=True
        with self.assertRaises(g.GateError): self.run_gate(m)
    def test_stale_budget_acceptance_rejected(self):
        def m(p): p['cases'][1]['accepted_as_theorem']=True
        with self.assertRaises(g.GateError): self.run_gate(m)
    def test_missing_supersession_warning_rejected(self):
        def m(p): p['cases'][1]['warnings']=[]
        with self.assertRaises(g.GateError): self.run_gate(m)
    def test_kernel_scope_promotion_rejected(self):
        def m(p): p['cases'][2]['scope']='UNIVERSAL_FEI_CONSTANTS'
        with self.assertRaises(g.GateError): self.run_gate(m)
    def test_twelve_promotion_rejected(self):
        def m(p): p['cases'][3]['universal_fei_constant']=True
        with self.assertRaises(g.GateError): self.run_gate(m)
    def test_unverified_evidence_rejected(self):
        def m(p): p['cases'][0]['evidence_verified']=False
        with self.assertRaises(g.GateError): self.run_gate(m)
    def test_bad_state_binding_rejected(self):
        def m(p): p['cases'][0]['research_state_git_blob']='0'*40
        with self.assertRaises(g.GateError): self.run_gate(m)
    def test_missing_anchor_rejected(self):
        with self.assertRaises(g.GateError): self.run_gate(state='Full FEI remains OPEN / NOT PROVED.\n')
    def test_missing_case_rejected(self):
        def m(p): p['cases']=p['cases'][:-1]
        with self.assertRaises(g.GateError): self.run_gate(m)
    def test_full_brain_promotion_rejected(self):
        def m(p): p['full_brain_connected']=True
        with self.assertRaises(g.GateError): self.run_gate(m)

if __name__=='__main__': unittest.main()
