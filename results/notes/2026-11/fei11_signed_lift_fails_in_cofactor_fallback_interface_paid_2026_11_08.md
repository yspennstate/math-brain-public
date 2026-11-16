---
name: fei11_signed_lift_fails_in_cofactor_fallback_interface_paid_2026_11_08
description: "No (8 Nov, FEI11): the signed lift over k shared selectors still fails when cofactors use FEI9's fallback; |A|/I diverges, D/I < 28; the interface entropy is paid"
metadata:
  type: project
  created: 2026-11-08
  created_at: 2026-11-08T14:31:05+04:00
  status: verified
  evidence: "frontier T021 fei11_agent_11_08 (f4af5012cb); fei11_check.out"
---

Does conditioning on the shared selectors with signed Walsh coefficients (FEI10's repair, generalized to k shared variables) rescue the FEI reference law when the cofactors stay read-twice? No (8 Nov, FEI11, Codex, reviewed by an agent). The failure is in the FEI9 fallback inside the cofactors. The signed interface and the size of the shared set are not the cause.

The counterexample wraps FEI10's bad family: F = (OR_k(s) AND G_d) OR AND_k(s). Every mixed selector assignment leaves G_d intact. So A_F = (1 - 2^(1-k)) A_G and D_F = (1 - 2^(1-k)) D_G, with I(F) = (1 - 2^(1-k)) I(G) + k 2^(1-k). Hence |A|/I still diverges (>= 141.61 nats at d=64, k=66) while D/I < 28 nats. This happens even at a fixed k. The interface's own entropy is paid: H(AND_k) <= 4 ln2 times the selectors' influence.

My check (fei11_check.py): the influence identity holds exactly at 4 (d,k) pairs (863/512, 1821/1024, 52599/32768, 204353/131072), and H(AND_k)/(4 ln2 k 2^(1-k)) peaks at 0.9930 over k = 2..40. I did not recompute the signed law. The worker's two codes agree on 139,272 coefficients each and catch a planted Walsh sign.

The next move is a recursively signed interface, used all the way down instead of FEI9's fallback, that pays its entropy from true influence. FEI stays open.

Frontier T021 move 14:30, pushed f4af5012cb.

Related: [[fei10_overlapping_cut_breaks_child_reference_sign_repair_2026_11_08]] - the family this wraps and the one-selector repair it generalizes.

Later (8 Nov, FEI12): the AND_k interface ratio reaches 0.993034 at k = 40, so the 0.9930 bound above is slightly false; it is 1 - 0.2787/k and tends to 1. See [[fei12_signed_law_exact_local_bill_unpayable_transported_212_23_ln2_2026_11_08]].
