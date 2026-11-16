---
name: fei10_overlapping_cut_breaks_child_reference_sign_repair_2026_11_08
description: "[VERIFIED] No (8 Nov, FEI10): at a growing overlapping read-twice cut FEI9's child-conditioned reference diverges (A/I -> -inf, D/I < 28); signed conditioning of the shared selector repairs it only for read-once cofactors; FEI open"
metadata:
  type: project
  created: 2026-11-08
  created_at: 2026-11-08T13:55:57+04:00
  status: verified
  evidence: "FEI10 PROOF.md, high_precision.csv; fei10_check.py; pushed 70596e8115"
---

Does FEI9's child-conditioned reference survive a cut where both children share many inputs and both grow deep? No (8 Nov, FEI10). Take F_d = (x AND A_d(y)) OR ((x OR AND(y)) AND (C_d OR R)), where A_d alternates AND and OR by its own probability and the two children share x and all 2^d y inputs. On it the reference's correction A/I goes to minus infinity and I(Q)/I diverges, while the true KL stays under 28 nats per unit influence. The reference keeps sampling the complex left child even though the shared selector almost always screens it out. What it lacks is sign: conditioning x once and keeping signed coefficients makes the cofactors read-once and the reference exact (Q* = P). That repair only works when the cofactors come out read-once. The general step, keeping signed information across several shared variables with read-twice cofactors, is the next move. FEI itself stays open.

My check (an agent, own Walsh transform from the definition): total influence exactly 351/256 (d=1) and 19831/16384 (d=2), Fourier entropy as stated to 12 digits, variance >= 15/16, and the d=64 bound arithmetic (141.61) all match. Not checked: the reference law Q and its entropy lower bound.

Files: the private brain repository: 06_math_research/frontier/T021/fei10_agent_11_08 and rows/T021/moves.jsonl (70596e8115).

Related: [[fei9_child_conditioned_reference_bounded_raw_diverges_2026_11_08]] - FEI9 built the child-conditioned reference this breaks at an overlapping cut

Later (8 Nov 14:31, FEI11): generalizing the signed repair to k shared selectors fails the same way, through the cofactor fallback; see [[fei11_signed_lift_fails_in_cofactor_fallback_interface_paid_2026_11_08]].
