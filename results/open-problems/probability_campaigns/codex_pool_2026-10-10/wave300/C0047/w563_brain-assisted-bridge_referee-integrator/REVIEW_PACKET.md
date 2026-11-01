# C0047 referee packet — w563, 2026-10-10

Verdicts are in `VERDICTS.jsonl`. KEEP applies to the stated partial result only. Independent reproductions are recorded row by row. The hardest remaining mathematical need is `||T_{p_c}||_{2->2}<infinity` for each fixed nonamenable Cayley graph, or an alternative separation proof. The route coupling of w562 proves an existence-threshold comparison but gives no uniqueness-threshold comparison: additional base-open edges can merge distinct routed clusters.

## Source and status

Benjamini–Schramm 1996 Conjecture 6 concerns connected almost-transitive graphs of positive Cheeger constant; the paper's convention is site percolation and it says its nonplanar questions extend to bond percolation. The modern fixed-Cayley bond version appears as Conjecture 2 in Duminil-Copin's 2018 ICM survey. The 2026-09-07 C0047 ranking is `attempted_un`, not a current verdict. The owner's June solved register does not list C0047. A September 2026 public preprint asserts a full bond result, so current openness is UNKNOWN pending proof review. Its public comparator `BenjaminiSchramm.lean` has `sorry` in `full_main`, `critical_laws`, and `cayley_main`; that file provides no completed formal-check receipt. This observation alone neither proves nor refutes the preprint.

## Exact brain correction

The existing C0047 attempt card says `p_c < 1/rho` with rho the normalized simple-random-walk spectral radius. The original sufficient criterion is `rho * d * p_c < 1` for a d-regular graph. On T4, rho=sqrt(3)/2 and p_c=1/3, so the omitted degree makes the condition vacuous while the correct sufficient criterion fails. This is a source-backed FIX to the attempt, not a solution of C0047.

## Retrieval measurement and repair boundary

w562's saved deployed math-recall run returned 0 of the two exact C0047 cards in its first six hits, taking 27.775 s; a read-only exact-ID lookup of those cards took 0.106 s. This is one-query evidence. A bounded repair is an exact problem-ID/metadata fallback before semantic ranking when a query explicitly contains `C0047`, followed by a separate precision and revision-head check. No global recall control was changed.

## Reproduction gate for next referee

Verify the critical operator norm claim in the September 2026 paper directly, particularly its Theorem 2.6 and the second-moment load estimate Lemma 4.8; inspect definitions and constants against the claimed uniform conclusion. Recheck any actual Lean theorem body and trusted axioms, not just a scope note. A KEEP on L01-L05 or S1.w562.001-.005 is not a KEEP on the parent problem.

NEXT: Audit the claimed manuscript's load estimate or obtain an independent, assumption-complete proof of finite critical two-point operator norm.
