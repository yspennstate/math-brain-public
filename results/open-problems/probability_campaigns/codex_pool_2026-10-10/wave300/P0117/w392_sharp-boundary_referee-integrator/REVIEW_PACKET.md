# P0117 referee packet for w390, w391, w395 and integrator

Verdict: **KEEP** w390 Lemmas 1 and 2, Theorem 3, Corollary 4 as an independently checked *partial* result; **KEEP** w391's constant-law example as a boundary counterexample; **FIX** the survey locator and scope attribution; **DROP** any implication from these tube results to unrestricted no-bigeodesics.

Reproduction: see `ATTEMPT.md` and itemized exact statements in `CLAIMS.jsonl`. The high/low sets have `m(2w+1)` and `m+4w+2` edges. The strict inequality is `m(h-l)>(4w+2)l`. Consecutive trap supports are disjoint at start-column spacing `m+1`. Dyadic failure probabilities are bounded by `exp[-c 2^{k(1-theta)}/sqrt(k)]` for some `theta<1`, so the first Borel-Cantelli lemma applies without inter-annulus independence. A last-first-column/first-last-column subpath stays inside the slab even if the ray backtracks. The event excludes all rays, including those chosen after seeing weights.

Critical scope: the result assumes injective geodesic rays in the ambient lattice metric and gives no bound for rays wandering outside every thin deterministic tube. This is the single hardest remaining gap to the original target. A KEEP here is not a P0117 solution.

Source: the 2015 survey's Question 31 is on printed p. 86 / PDF p. 85 in the accessible version. The September 24, 2026 preprint's Theorem 1.1 explicitly claims the full planar nonatomic minimum-of-four second-moment case; only its statement was checked here. Record current openness as UNKNOWN or CLAIMED_RESOLUTION_UNAUDITED, never as known open or established solved from this packet.

**w395 request:** Independently audit `P0117-w392-own-zero-edge-boundary` in `CLAIMS.jsonl`: with a zero atom, does a repeated walk oscillating on one zero edge satisfy the weakened every-finite-segment condition, and is its scope clearly separated from the injective theorem? Mark KEEP/FIX/DROP before promoting it to a theorem or concept node.

Brain routing: w390 owns the theorem draft. My referee packet supports its review; avoid duplicate theorem nodes. A distinct local draft concept in `draft_bundles/bundle_001.json` records the quantifier boundary and review scope. It is prepared, not submitted or ingested.

Additional same-target audit: `REVIEW_W389.md` gives independent KEEP verdicts on w389 C02 (stationary boundary-geodesic occupation identity) and C03 (unavoidable one-sided shell floor), plus a wording fix for one relation rationale. These remain separate from w390's thin-tube route.
