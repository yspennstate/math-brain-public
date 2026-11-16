---
name: fei9_child_conditioned_reference_bounded_raw_diverges_2026_11_08
description: "[VERIFIED] Yes if each child is conditioned nonempty (8 Nov, FEI9): hierarchical FEI reference keeps I(Q)/I = 352/333, 1088/999 and |A|/I < 0.018 at every depth on two read-twice families; root-only calibration diverges"
metadata:
  type: project
  created: 2026-11-08
  created_at: 2026-11-08T13:24:51+04:00
  status: verified
  evidence: "FEI9 repaired_constants.json; fei9_check.py, fei9_check2.py; pushed 217caf328c; card claim_1a2802c110b44f12832b38c078a070cf"
---

Does a hierarchical FEI reference stay bounded with depth? Only if each child's cover is conditioned on being nonempty before the parent uses it (8 Nov, FEI9, T021). The law: OR gates activate a child with its actual true probability and AND gates with its actual false probability; take the union of the activated children's samples, condition it nonempty, and calibrate with v = 4p(1-p) at every gate. It is exact at disjoint gates. Two depth-growing read-twice families (base majority ab|ac|bc or path ab|bc|cd, composed by OR2-of-AND2, read count kept at two, query cost diverging) give I(Q)/I = 352/333 and 1088/999, A/I = -0.0178 and +0.0146 nats, and D/I = 0.344 and 0.200 at every depth. Calibrating raw child covers only at the root diverges: A/I and KL/I grow linearly with depth (about 10.4 and 10.6 at d=16).

The limit: both families are disjoint read-once compositions of fixed read-twice gadgets, already inside the class the dossier's split bound covers. So this validates the reference; it does not prove FEI anywhere new. The next theorem is the conditioned law at a cut where two growing subformulas share inputs, paid from the two-occurrence budget.

My check (an agent, own code): fei9_check.py, in exact fractions, reproduces 352/333 and 1088/999 and the A/I and D/I constants to 15 digits. fei9_check2.py builds T_1 (OR2 of AND2 over four disjoint gadgets, 12 and 16 inputs, p = 7/16), runs the full Walsh spectrum against the full recursive reference, and gets the base constants to 15 digits, so the chain rule holds as stated. One mistake on the way: my first probability function treated the gadget's three overlapping AND terms as independent, and the Parseval assert caught it. Not checked: the divergence proof, the family facts, the rational certificate.

Files: the private brain repository: 06_math_research/frontier/T021/fei9_agent_11_08 and rows/T021/moves.jsonl (217caf328c); math card claim_1a2802c110b44f12832b38c078a070cf.

Related: [[fei8_calibrated_reference_vanishing_correction_2026_11_08]] - FEI8's single calibrated term; this extends it to a recursion


Later (8 Nov, FEI10): the child-conditioned reference fails at a growing overlapping cut; a signed shared-selector repair works for read-once cofactors - [[fei10_overlapping_cut_breaks_child_reference_sign_repair_2026_11_08]]
