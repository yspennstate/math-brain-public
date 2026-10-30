# Addendum — lead r16 consumed after the immutable report

A later complete campaign-lead result landed after `REPORT.md` was sealed:

- fleet04/B10 r16, science commit `f168b1f11b4b5d2d7fce0e1bc977d28cbb654c48`, report `proofnet24/collective-POS3/fleet04/B10/20260922T064124Z-B10-POS3-r16/REPORT.md`, report blob `78e86dcdaef62417888ef6d8b66bf3b6d062f2c9`.

R16 losslessly re-anchors every first heavy-cover defect mark to a fully outward boundary pair `(r,x)` or `(y,r)`, and in the low-endpoint branch produces two distinct fully outward pairs each carrying `>2E/33` marked extensions. Its remaining global implication is now **OUTWARD-STATE RECYCLING**: after the first genuinely outward fork/corridor state is entered, prove that later transfers cannot cycle among outward states without an authorized exit.

The B19 reciprocity lemma and exact witness remain source-valid, but their interpretation sharpens. They do **not** contradict r16's first-export theorem. Instead they act exactly one step later:

- for an `F2/T_L` boundary blocker `t`, r16 records the fully outward pair `(t,x)`;
- the Hasse edge `t lessdot a` with pivot `x` creates the next heavy state `(t lessdot a; x)` whenever `t prec_* x`;
- in that new state the old cover successor `y` is a canonical `U_R` return channel;
- dually an `F3/U_R` transition has the reciprocal return geometry.

Thus r16 correctly removes *immediate interior recoding* as a fake return, while B19 shows that a genuine return can occur after one outward heavy-state transition. The exact 515-extension core realizes

`S0=(5 lessdot 6;10) --72--> S1=(1 lessdot 10;5) --105--> S0`.

This cycle is not in r16's strict two-packet low-endpoint branch: at `S0`, the endpoint minorities are `141/515` and `161/515`, both at or above `3/11`; at `S1` they are `128/515` and `141/515`, so the second is again just above `3/11`. The core also has balanced pairs, including the secondary cross-pair `(2,10)=49/103`. Hence no r16 theorem and no POS3 statement is refuted.

What the exact cycle rules out is a local proof of `OUTWARD-STATE RECYCLING` based only on acyclicity of the outward heavy-state graph, distance from the old interval, or monotone decrease of the unique heaviest canonical active weight. The first outward state can return, and the selected weight can increase (`72 -> 105`). Therefore a valid proof must use r16's *full two-packet / endpoint-scale information and the complete canonical frontier*, especially secondary cross-pairs needed to orient nonselected channels.

Updated first unpaid implication for this B19 line:

> **TWO-PACKET / FULL-FRONTIER RETURN EXCLUSION.** Starting from r16's two fully outward packets in the low-endpoint branch, or from an endpoint pair already at the `3/11` scale, prove that one complete outward-state transition cannot return with all primary and secondary frontier pairs still unbalanced unless a controlled amount of exact charge moves to a genuinely new strong-order frontier or another authorized structural exit occurs.

The named partner fleet03/B10 zero-boundary-defect theorem remains essential: the return cannot be broken by inventing an additive probability correction at the first non-exact boundary.

Outcome remains `ESSENTIAL_STEP_APPLIED`; parent POS3 remains OPEN; execution context remains `WITHOUT_VERIFIED_BRAIN`.
