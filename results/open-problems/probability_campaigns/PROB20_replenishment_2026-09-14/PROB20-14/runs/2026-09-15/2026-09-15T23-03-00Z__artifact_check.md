# PROB20-14 — balanced-prefix consistency-check execution

**Artifact:**
`probability_campaigns/PROB20_replenishment_2026-09-14/PROB20-14/artifacts/balanced_prefix_collapse_check.py`

**Artifact creation commit:** `5621773ce8aaf9a6460471276d1ede738fb61945`  
**Artifact blob:** `c00bd3a726bd9ab930a43e143b1bf747cbca8015`

The checked artifact was executed after SHA-specific readback. It uses only Python's standard library.

Observed output values:

```text
collapse sequences checked: 37448
collapse antecedent triggered: 4681
Chernoff t=1.000000, rho=0.798481569237, worst exact/bound=0.533429266816
exact binary forest/Dwass cases checked: 114
ALL ASSERTIONS PASSED
```

The exhaustive finite sequence check found no violation of the deterministic collapse lemma for `k=1,...,5` and generation values in `0,...,7`. The finite-support critical test law `P(xi=0)=0.19`, `P(xi=1)=0.80`, `P(xi=20)=0.01` satisfied the exact lower-tail probabilities below the elementary Chernoff half-drop bound for every tested `m<=40`. The critical binary law `P(xi=0)=P(xi=2)=1/2` gave exact equality between direct convolution of the excess-total-progeny law and the forest Dwass formula for all 114 tested `(b,M)` pairs (`1<=b<=6`, `0<=M<=18`).

These are consistency/algebra checks only. They are not proof evidence for the infinite-variance universal theorem and do not constitute independent mathematical review.
