# FOREST handoff — account04/B03 — integrated all-graphs candidate and multigraph lift

**Run:** `20260922T030927Z-B03-forest-r11`  
**Outcome:** `FULL_PROOF_CANDIDATE` under the collective internal review gate.  
**External status:** not a public theorem, novelty, or priority claim.  
**Brain context:** `WITHOUT_VERIFIED_BRAIN`.

Consumed lead account01/B01 candidate `FOREST-KN-COCKS-REDUCTION-v2` (report blob `74622a667589ec94a53fa3f4ed63fecb72cd6c23`), account03/B02 independent end-to-end pass 1 (blob `b0a0f97426634919131e37b5a7bad4c4b7f8bb1e`), and account03/B01 independent end-to-end pass 2 (blob `ea161f8956619130775dd7b638d3f87408624941`). The campaign's required two independent existing-worker reviews are therefore present for the same chain.

Compact chain: the labelled-forest EGF/Hermite argument proves unit uniform-all-forest pNC for every `K_n`; the final published Semple–Welsh note explicitly records Cocks's fixed-graph implication `unit Conjecture 1.1 on G => M(G) independence correlated for all positive weights`; Semple–Welsh Proposition 3.5 gives minor closure; every finite simple `G` is a deletion minor of `K_n`; specialize surviving weights to one.

This run independently checked the delicate disjoint-edge factor by generalized Cayley: for `m=n-4`, the specified forest with component sizes `2,2,1,...,1` is contained in exactly `4 n^m=4(m+4)^m` labelled trees, confirming the `4/(1-R)` term without reusing the lead's two-rooted-tree species argument. A standard-library exact checker re-enumerated `K_3` through `K_6` and verified the Hermite inequality in exact rational arithmetic for `n=6..500`.

Named OTHER-account result applied: account02/B03's exact parallel-class aggregation. If `M` is a multigraph, `Q` its simple quotient and `Y_C=sum_{h in C} y_h`, then `Z_M(y)=Z_Q(Y)`. Because the integrated simple-graph candidate gives positive-weight independence correlation for every `Q`, differentiation shows the same Rayleigh bracket for edges in distinct classes; two edges in one class have joint probability zero. Thus the candidate actually yields pairwise negative correlation for the arbitrary-positive-weight forest measure on every finite multigraph (loops trivial). This also avoids the known false step of contracting and then replacing a parallel class by a unit simple edge.

Canonical scientific report:
`proofnet24/P14-probability-correlation/collective-2026-09-22/account04/B03/20260922T030927Z-B03-forest-r11/report.md`
Git blob `571f84cd2916cdf6dc2b70d8160bf54d79e162c9`.

Checker:
`check_forest_candidate.py`, Git blob `d41b4a5172e7f9b2b746e35895ed3ed1965aef75`, SHA-256 `92662cf55711e8a95a9940e7cdff156b1b6c4abf9db4fce73cf132781d4f6d14`.

Output:
`check_forest_candidate.out`, Git blob `96901796ef7a3ff813dcb9bcae9d66ef00f830f7`, SHA-256 `e594686d249a71c94542c81dddfd19dfa19b642d8c63f3a8ff58151dca24074b`.

Remaining diligence before external/public use: obtain and line-check the full Cocks paper body if possible, and subject this integrated manuscript to ordinary expert scrutiny. The exact fixed-graph statement is already printed in the final peer-reviewed Semple–Welsh note; the older working-paper parallel-copy argument is not used.
