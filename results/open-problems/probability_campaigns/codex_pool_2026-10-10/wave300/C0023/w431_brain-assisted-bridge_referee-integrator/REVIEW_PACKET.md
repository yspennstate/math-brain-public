# C0023 referee packet — w431, 2026-10-10

## Source and status

Exact bond model, dated intake, and later primary proof claims are recorded in SOURCE_STATUS.json. The 2026-09-07 “open” card in the live store is stale as a status report because it omits a pinned 2026-08-28 Lean claim and later published claims. This packet does not independently verify those claims. Current openness: UNKNOWN. The source-scope correction is especially important: Cerf's arXiv:2608.23661 treats **site** percolation; it cannot be declared equivalent to this **bond** target without a separate reduction.

## Peer verdicts

| Claim | Verdict | Independent reproduction | Unresolved gap |
|---|---|---|---|
| w429 L1 high-density finite-range field | KEEP as an abstract counterexample | Common-anchor minimum is uniform on the union of windows; intersection and union sizes give the stated q(d,L). A connected good component shares one anchor and fits in its L-box. | No FKG/monotonicity premise; says nothing against bond critical nonpercolation. |
| w429 L2 fixed-range criterion | KEEP as a sufficient lemma | Recounted K=(r+1)^2 independent colors and bad star circuits; alpha<=1/8 gives 1-delta-8/49>0. | Its threshold worsens as r grows; contour fact is the standard square-lattice exterior-boundary lemma. |
| w429 L3 finite-event stability | KEEP | Uniform-edge coupling: event changes only if one of M iid labels lies between p and p'; probability <=1-(1-|p-p'|)^M<=M|p-p'|. | No independence of block events follows. |
| w429 L4 conditional block transfer | KEEP only with all hypotheses stated | L3 preserves the strict L2 threshold at p'=p_c-eta; L2 plus deterministic compatibility contradicts p'<p_c. | Need actual finite, compatible blocks with delta<64^(-(r+1)^2). |
| w429 CLAIMS S1.1 “any argument must” | FIX | L2-L4 establish a requirement only for this chosen block route. | Replace universal necessity wording with the exact conditional criterion; alternative methods may bypass it. |
| w430 claim 001 abstract limit counterexample | KEEP | f_n(p)=0.5 exp(-(p_*-p)n) is continuous and increasing in p, decreasing in n, tends to zero for fixed p<p_*, and equals 0.5 at p_*. | An abstract family, not a percolation counterexample. |
| w430 claim 002 critical polynomial lower bound | KEEP | Full independent derivation in ATTEMPT.md from primary Theorem 1.1; bound and uniform-rate obstruction check out. | No upper critical one-arm bound. |
| w430 claim 003 whole-tile coarsening | KEEP as a sufficient lemma | For s=r+1, tiles at coarse distance >=2 have physical distance >=s+1>r. Their all-good indicator is setwise 1-dependent and fails with probability <=s^2 delta. Apply the independently checked r=1 contour lemma; adjacent fully good tiles connect in the original lattice. | Need actual compatible critical blocks with delta*s^2<64^-4. |
| w430 claim 004 ghost-field comparison obstruction | KEEP | Primary arXiv:2304.12110 Theorem 2 uses q=p(1-m_h(p)), h>0. Conditioning on cluster size gives m_h(p)=E_p[1-exp(-h|C(0)|)] and bounded convergence gives m_h(p)->theta(p). Therefore q_h at p_c tends to p_c(1-theta(p_c)); it reaches p_c only if the target already holds. | No critical upper tail follows; e^{-hn} degenerates when h decreases to zero. |
| w429 C1 Burton-Keane application correction | KEEP as a source-application correction | The live card explicitly requires conditional edge-open probabilities strictly in (0,1). Under product Bernoulli(p) this conditional probability is p, so its own hypothesis fails at p=0 and p=1. | No change to the true endpoint conclusions, which are directly checked. |

No KEEP here implies the parent C0023 result. The strongest route improvement is w430 claim 003: the sufficient threshold is now 64^-4/(r+1)^2 instead of 64^(-(r+1)^2), so the hardest remaining block condition is delta*(r+1)^2<64^-4. At r=2 the two thresholds are 64^-9 and 64^-4/9, an exact factor of 64^5/9. Kozma--Nitzan's Conjecture 3 supplies a different bridge but asks for a uniform modulus over every finite weighted graph.

The w429 block_bridge_guard.py proposal checks the older, conservative threshold with exact integer arithmetic. I read its full source and verifier, then copied both into w431 and ran `python -X utf8 verify_bridge.py`. It passed 303 controls in 0.0479257 s, including three constructed false-density certificates reduced to zero; the verifier wrote a fresh light-compute gate. The guard relies on caller-supplied boolean evidence flags, has no live recall caller, and is a proposal only. KEEP the bounded arithmetic helper as a proposed safeguard; no deployed brain gain is established.

## Brain retrieval failure and bounded repair

Command: `python -X utf8 ~/.claude/dreaming/brain.py recall "C0023 percolation criticality bridge mistakes"`. It returned eight listed results in 25.4 s. The top three were unrelated memories (prob1000 intake, project-brain hardening, and a Bernoulli block reformulation); **0/3** identified the target theorem or sharpness gap. A read-only exact-title SQL query against `~/math-brain-build/local/population/brain.sqlite3` found the C0023 card in **0.0266 s**, and the sharpness card in **0.0253 s**. This is a query-path failure, not absence of data. Proposed bounded repair: stage one concept connecting C0023 to the exact sharpness quantifiers and one status-scope concept pointing to the primary post-intake proof claim; retest this one query after coordinator ingestion, with success requiring a correct target or gap card in top three. No after-ingestion improvement is claimed now.

## Brain card correction

Live card `math:probability.percolation:sharpness-of-the-percolation-phase-transition` says subcritical decay is exponential “right up to p_c.” Primary arXiv:1502.03051v1 Theorem 1.1 says `for p<p_c, there exists c=c(p)>0`; it does not state one rate for all p near p_c. w430's independently checked bound rules out such a uniform rate. Suggested replacement wording: “For each fixed p<p_c, one-arm probabilities decay exponentially with a p-dependent rate; this theorem alone gives no upper decay at p=p_c.”

NEXT: Coordinator or independent auditor checks the reviewed rows, integrates only status-calibrated drafts, and reruns the one-query recall probe.
