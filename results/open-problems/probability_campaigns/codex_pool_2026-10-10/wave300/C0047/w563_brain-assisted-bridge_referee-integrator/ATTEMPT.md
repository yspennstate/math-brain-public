# C0047 bridge attempt and limits — w563, 2026-10-10

## Exact need

For every infinite finitely generated nonamenable group and every *fixed* finite symmetric generating set, prove that independent Bernoulli bond percolation on its Cayley graph has `p_c<p_u`. The original 1996 Conjecture 6 is broader and uses site percolation by convention; the modern bond statement is recorded in `SOURCE_STATUS.json`. Changing the generating set or assuming hyperbolicity supplies only a special case.

## Brain-assisted route

The stored C0047 attempt proposed `p_c<1/rho` for normalized simple-random-walk radius `rho`. Primary Theorem 4 actually needs `d*rho*p_c<1` on a d-regular Cayley graph. The degree-free inequality is automatic under nonamenability (`rho<1`, `p_c<=1`) and therefore cannot certify the phase gap. T4 makes the omission visible: `p_c=1/3`, `rho=sqrt(3)/2`, and `d*rho*p_c=2sqrt(3)/3>1`, although `p_u=1`. The corrected criterion is sufficient, not necessary. Both the stored attempt and problem cards were recovered by exact read-only lookup; the deployed math-recall query missed both in six results (see `REVIEW_PACKET.md`).

The useful bridge is conditional: if `T_{p_c}` is bounded on counting-measure `l2`, Russo plus BK continues that bound above `p_c` (w561 L02), while FKG and uniqueness rule out boundedness in the uniqueness phase (w561 L03). I independently derived both steps in `VERDICTS.jsonl`. This reduces the target to critical operator boundedness for each fixed nonamenable Cayley graph. The hyperbolic theorem supplies that in its additional geometric class. The September 2026 public manuscript claims it generally, but its Theorem 2.6 and Lemma 4.8 were not independently checked here. Its comparator Lean declarations contain `sorry`; that is not a formal receipt.

w562 supplied a bounded-congestion path coupling. I independently checked the slot product-space construction and threshold comparison. It transfers existence only. Distinct simulated clusters may be merged by extra base-open edges, so no inequality for `p_u` follows. The two overlapping length-two free-group routes give joint open probability `p^3`, not independent `p^4`, refuting a naive path replacement.

## Single hardest open piece in this packet

Prove the claimed critical `l2` boundedness with complete assumptions, or prove another fixed-graph cluster-separation lemma. An audit of the September manuscript must verify the second-moment load bound and its use in Theorem 2.6. No full C0047 proof is claimed here; current openness remains UNKNOWN because a recent public full-proof claim is not yet mathematically certified.

NEXT: Have an independent referee check the manuscript's Lemma 4.8 and Theorem 2.6 against the full definitions, or derive critical operator boundedness by a separate route.
