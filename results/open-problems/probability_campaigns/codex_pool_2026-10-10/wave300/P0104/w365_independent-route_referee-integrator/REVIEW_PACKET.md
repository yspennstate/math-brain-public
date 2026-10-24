# P0104 referee packet, 2026-10-10

**Verdict.** KEEP the peer's elementary lemmas and exact reductions within their stated hypotheses; no parent-problem proof. Five itemized rows are in `VERDICTS.jsonl`. Independent exact check: `python -X utf8 ~/brain_workers/w365/audit_exact.py` returns PASS on all 16 four-edge assignments with exact fractions.

**Source.** Auffinger, Damron and Hanson, *50 years of first-passage percolation*, Questions 13 and 15, asks for chi<1/2 in d>=2 under suitable F, chi=1/3 in d=2, and chi>0 for suitable d. Section 3.1 says the asymptotic exponent notation itself has not been made precise; Definition 3.21 later supplies directional liminf/limsup log-Lp exponents. The historical campaign record under `brain_bundle_C006p01.json` accurately tags current status unverified. Present openness is therefore recorded UNKNOWN. Basu-Sidoravicius-Sly arXiv:2604.01214 proves a power upper bound for a rotationally invariant Riemannian model, not a lattice chi=1/3 result.

**w363 hardest step.** The finite Bernoulli Fourier identity is correct by coordinatewise independent retention/replacement coupling. The geodesic-forcing bounds use deterministic choice among ties; conditioning on each edge recovers the factors p and q. The explicit p=0.99 law has r=6q^(3/4)<0.19 and the union bound at n=1 is below 1/3, enough for D_n>=n/600. The exact identity Var(T_n)=D_n E_nu[1/K] leaves the harmonic spectral-mass estimate G1 fully open. A typical K scale alone is insufficient because low-degree mass dominates E[1/K]. This is the single hardest open piece for that route.

**w364 hardest step.** The four-edge shortcut remains exact on the full lattice: any other simple route costs at least 4, while a two-step route costs at most 4. Independent enumeration reproduces all means, variances and covariance. The transfer lemma follows from the centered L2 triangle inequality, but it has no proved asymptotic FPP premises. A scalar minimum over interfaces drops a matching penalty already at n=1.

**Independent route.** I recorded a stationary-cocycle covariance plan in `ATTEMPT.md` after checking that my initial resampling plan overlapped w363 and the older FPP campaign. For a stationary increment sequence, the variance identity is elementary; the difficult missing inputs are existence of a useful cocycle, an o(n^(1/3)) centered L2 approximation to passage time, and a two-sided n^(2/3) variance estimate for the cocycle. I claim no new theorem from that route.

**Prior local context.** The 2026-08 FPP campaign's verified block-chaos engine explicitly leaves chi=1/3 untouched; its scar identifies the conditional variance-ratio bound as a wall and warns that Efron-Stein has the wrong direction for a proposed fourth-moment shortcut. Searches of the named H/I attempt folders found no P0104 item. This is a bounded local check, not proof of current openness.

**Source-locator correction.** The existing `op-p0104` card in `brain_bundle_C006p01.json:2175` cites Questions 13 and 15 at “PDF pp.34 and40.” At the audited authors' PDF URL, both questions are together on PDF p.36. The exact correction row is `SOURCE_CORRECTIONS.jsonl:S1.w365.6`; it awaits a second source audit before a live-card edit.

**Audited peer versions (SHA256).** w363 `ATTEMPT.md`: `76F4E2B6AC5B661523A250AF9F35612DDBFAD0B37EAB5BE2C8D2AD35CD2356DE`; w364 `ATTEMPT.md`: `B46EDC253A9C6D17EBAF13B268D2B07B33C2383B8FC7300CD171FD9A9B89A843`; w364 `CLAIMS.jsonl`: `09180944969C08742EF1E5A9FA26D74D78320A1E6F75A04AE71E7BCA7E175AA2`.

**NEXT:** Second auditor checks the source correction and concept draft; integrator ingests the reviewed bundle and verifies retrieval. Ask w368 to review only if a genuinely new mathematical lemma is added.
