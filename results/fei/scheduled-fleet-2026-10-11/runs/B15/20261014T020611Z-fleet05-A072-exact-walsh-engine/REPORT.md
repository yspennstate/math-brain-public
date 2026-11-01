# exact target, quantifiers, hypotheses and units

For EVERY actual nonconstant uniform Boolean core with minority probability 0<p<=1/16, bound the price of A071's one-flipped-block escape, independently of dimension. Entropy is in bits; E(g)=min_i B_i/Inf_i over relevant coordinates. The gate and disjoint-copy convention are specified in PROOF.md. Result: finite escape to minority bias (1/16,1/4), E loss at most (3/16)log2(192e)<111/64, and H/I upper increment at most45/22. Author proof complete; independent review pending; full FEI OPEN.

# sources actually read, revisions and theorem locators

EXECUTION_PROTOCOL.json revision2026-10-11-execution-v2; BOARD.md snapshot2026-10-14 02:02 UTC; B15 STREAM_NOTES.md v2; own stage3 status, helper and report. New dependencies consumed: A071 run20261014T013355Z PROOF.md (one flipped block and exact composition identities), A080 run20261014T005622Z REPORT.md (actual rare high-E core and common-sign obstruction), A084 run20261014T000747Z REPORT.md (moderate continuum), A089 run20261014T000812Z REPORT.md (slope criterion), and A075 run20261014T005346Z REPORT.md (rare localization and retained entropy ledger). Exact accessible source hashes are recorded separately. These guide the target; the new proof reconstructs its own complete chain and has no unreviewed theorem dependency.

# complete derivation or exact first unsupported line

PROOF.md proves the stated universal-over-cores escape theorem. Key bounds are R_j>=-q_j Phi(m^2,beta_i^2), |beta_i|<=min(Inf_i,2p), and sigma(p)>3p. The erasure loss is a summable O(p log(1/p)) quantity. Spectral entropy subadditivity and the proved scalar inequality h2(vq)<=q h2(v)+v h2(q) give C<=120p^2 log2(e/(5p)); Q>=11/4 and I>=2p log2(1/p) make its normalized cost summable. The exact identity H(F)/I(F)=H(g)/I(g)+C/(Q I(g)) retains every signed terminal correction and the starting core entropy.

First unsupported universal line: an absolute admission/exposure bound for the moderate-bias terminal core, with a finite global budget if later operations create additional excursions. No complete physical restriction-tree ledger or absolute bound on H/I or E follows from this stage. Explicitly, sup E over0<p<=1/16 is at most sup E over1/16<p<1/4 plus (3/16)log2(192e). A uniform moderate-bias bound therefore controls the rare sector after just one escape.

# executed validation with domain, arithmetic, commands and outputs

SPEC.json was frozen before computation. Commands: `python -X utf8 code/verify.py --pilot` and `python -X utf8 code/verify.py`, run from this run directory (the actual invocation used their workspace-relative paths). Pilot passed in0.315 seconds; full run passed in1.731 seconds. Frozen estimated memory100MB, so the >300MB memok condition was not triggered; peak memory was not instrumented. No dimension escalation or heavy search.

The exact six-bit J gate passes integer Walsh Parseval, sign-valued inverse, direct character sums and independent edges. Five rational biases1/16 through1/256 pass rational biased Parseval/inverse and pivotal-vs-spectral influences, all30 block reserve checks, polynomial equality and terminal upper bounds. Four actual12-bit compositions from two-bit core masks1,14,6,10 pass all16384 signed Fourier coefficient identities, inverse signs, Parseval and48 physical coordinate edge counts. Large tables use FWHT and its inverse, without the quadratic direct character-sum check. Every structural check precedes entropy comparisons. Logs use the earlier independently derived48-term rational atanh enclosure, not floats. Per-case exact outputs and the final summary are in out/. The finite checks validate implementation; the all-dimensional conclusion is the analytic proof.

# proof dependencies and changed downstream conclusions

No proof dependencies beyond the elementary facts reconstructed in PROOF.md. Scoped independent review accepts A071's polynomial/bias-escape clause only; it does not certify A071's ten-orbit or g3 numerical clauses. A080's common-sign obstruction survives. A084's moderate common-sign theorem is not extended or re-reviewed here. This stage prices escape from A080's rare sector instead of excluding rare high-E cores. Composition levels are never substituted for physical restriction queries, and all starting entropy survives.

# one next mathematical action and independent reviewer

A075/A089 should close the moderate-bias terminal admission/exposure bound with a global payment preventing repeated excursions from accumulating an unbounded bill. A074/A092 should reconstruct the Phi loss bound, scalar thinning inequality, edge-isoperimetric normalization and signed terminal telescope independently. This is a continuation of the same admission gap, not another finite census.

# actual persistence receipts or precise save blocker

All four protocol files, frozen spec, proof, code, exact outputs, scoped review and hashes are saved locally in this run. Rolling STATUS.md, WORKLOG.md and LEARNED.md are current. out/manifest.json records byte lengths and SHA256, excluding itself. Each file is below20MB. PROGRESS.json and PACKET_DELTA.json have identical content. Independent review, remote mirroring and downstream adoption remain unverified; no writes outside A072 were made.

## Universal bridge

This stage moves the B15 erasure-selection admission bridge underlying C018: every rare core, in arbitrary dimension, can be transported back to moderate minority bias with E loss <111/64 and complete signed H/I upper bill <=45/22. It does not prove the total-erasure C018 inequality or C019 physical stopping-tree payment. The remaining obstruction is an absolute terminal admission/exposure bound and ownership of repeated excursion costs. That single global payment is the shortest route forward because the construction now transports arbitrary cores, while another bounded-dimension class computation cannot close the remaining universal line.
