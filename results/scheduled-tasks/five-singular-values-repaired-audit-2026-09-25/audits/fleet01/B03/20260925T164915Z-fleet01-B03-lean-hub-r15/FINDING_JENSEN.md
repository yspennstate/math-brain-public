# L323--329 Jensen finding
Verdict: PASS mathematically; Lean UNCHECKED.

The repaired text now explicitly uses |E F_t|^2 <= E|F_t|^2 and then averages the conditional pointwise estimate. This step uses no independence internally.

New formalization progress: local candidates hub_jensen_sq and hub_jensen_then_average isolate the exact probability-space inequality and its composition with an integrable pointwise upper bound. They are UNCOMPILED because this runtime has no lean/lake; no formal credit is claimed.
