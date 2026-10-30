# A014 stage 4: whole-set payment interface for one shared blocker bit

## exact target, quantifiers, hypotheses and units

Target C020/B03: replace the derivative-local conditioned-error repair by a single normalized whole-set reference retaining blocker activation and signed collisions. For arbitrary finite disjoint private cubes Y,Z and nested Boolean indicators h1<=h0, k1<=k0, prove an exact entropy/influence ledger and construct a normalized reference for f=1-2 h_x k_x. Units bits, uniform cube; one shared bit x. Positive blocker families sharing only x are included after orienting x. This is an interface theorem, not a dimension-independent FEI bound for unrestricted overlapping hypergraphs.

## sources actually read, revisions and theorem locators

Read EXECUTION_PROTOCOL.json revision 2026-10-11-execution-v2 in full, BOARD.md 2026-10-14 02:43 UTC snapshot, B03 STREAM_NOTES.md v2 (A014 target and universal bridge), own STATUS.md and stage-3 derivation. New source: A008 runs/20261014T021605Z-fleet05-A008-gate-label-compression/REPORT.md, sections complete derivation, proof dependencies, and Universal bridge. Its corrected occupation mass motivates the next reference comparison; no A008 theorem is a premise of our proof. A009's scalar transfer was read in the previous stage, not independently reviewed here. Prior campaign/paper source reads are retained; the known block-restriction identity is acknowledged and specialized rather than presented as a new universal identity.

## complete derivation or exact first unsupported line

DERIVATION.md equations (1)-(10) give the full proof. Physical private influence and shared influence partition one actual account. The normalized blocker spectrum has exact branch-mixture entropy, erased branch-label refund L and signed separator entropy J. Multiplying by the whole-function activation factor 4s and subtracting h2(s) gives H(f), including every terminal entropy. An explicit component-reference mixture R with uniform separator bit produces normalized Q_C, and conditioning away the empty row produces normalized Q_f. Its complete cost retains both the empty-row refund and nonempty normalizer; the exact remaining gap is v times conditional KL. No Fourier phase is discarded from the actual entropy ledger.

First unsupported line: pay the full reference excess and terminal conversion costs with an absolute constant times the ONE actual influence account, in a form that iterates through overlapping blocker components. Normalized coverage and an exact identity do not prove that payment. The old stage-3 obstruction remains valid: zero local residual does not imply zero off-support mass.

## executed validation with domain, arithmetic, commands and outputs

FROZEN_SPEC.json preceded jobs. Final helper A014-shared-blocker-v1.2 checks all 81 pointwise nested branch pairs on each two-bit private cube, hence 6,561 labelled combinations on a fixed five-bit cube, including constants and without symmetry reduction. It tests physical influence, integer Walsh amplitudes, normalized row and full laws, signed entropy identity, all four terminal entropies, full output conditioning, and complete CE/KL identities for two reference choices: exact terminal spectra and uniform terminal references.

Entropies and cross-entropies are represented as rational linear combinations of log2(prime). Each rational probability factors into numerator/denominator primes; every claimed equality is checked coefficient by coefficient. This certifies the identities exactly, without floating-point signs or an assumption of independence of logarithms. The all-dimensional derivation is separate from the finite enumeration.

Commands: `python -X utf8 code/check.py --pilot` and `python -X utf8 code/check.py` from this run (executed using their run-relative path from A014). Final validation totals and runtimes: Pilot PASS: 3,357 assertions, 0.441937 seconds. Full PASS: 269,437 assertions, 169.762459 seconds. Full census includes 6,400 nonzero blockers, 161 constant-zero blockers, 400 positive-private monotone combinations, and 6,175 functions with positive shared influence.. Outputs out/pilot.json, out/check.json and incremental out/checkpoint.json. The first lexicographic pilot accidentally selected only zero blockers; out/pilot_degenerate.json preserves that fact. The pilot domain was corrected before full execution to the 81 diagonal pairs. v1.1 validated the signed ledger, then v1.2 added complete-reference cost checks; out/ledger_check_v1_1.json preserves the earlier census. These reused runs are not independent review, and their assertion counts are not summed as distinct certificates.

Frozen memory estimate below 100 MB, pilot limit 60 seconds and full limit 300 seconds; no automatic dimension growth, GPU, windows or persistent background job. Neither job was expected above 300 MB, so no memok admission was triggered.

## proof dependencies and changed downstream conclusions

The new reference construction uses only Parseval, independent private-block products, entropy chain rule and log-sum domination; positivity and normalization are proved explicitly. It extends the existing A014 claim version, without opening another broad FEI candidate. Stage-1/3 statements remain bound to their saved proofs. A008's occupation improvement is a useful next dependency, not an adopted proof premise or independently reviewed claim. No shared index is edited and no message is sent.

The important substitution for A009/B03 is now a whole-set reference with an explicit conditional KL bill, rather than zero derivative error being treated as zero spectral cost. The missing payment is genuinely still present: terminal conversions, overlap/refund and the reference excess must use the same influence budget. Full FEI and unrestricted linear-hypergraph FEI remain open.

## one next mathematical action and independent reviewer

Compare the complete mixture reference against an occupation-based reference in the first overlapping graph blocker component, retaining the SAME terminal distributions, signed row law and (9)'s empty refund. Produce either a paid excess inequality or an actual unpaid sector, then decide whether the reference mechanism can iterate. A086/A094 should reconstruct (5) and (9); A008/A009 should challenge the occupation-reference substitution. These are artifact handoffs, not completed reviews.

## actual persistence receipts or precise save blocker

The four protocol files, full derivation, frozen specification, exact checker and outputs are saved here. out/RECEIPTS.json records SHA256 and byte sizes and validates protocol field sets. Rolling STATUS.md has exactly two lines; WORKLOG.md and LEARNED.md are updated. Local persistence is verified; independent adoption, remote mirror, supervisor copying and public release are unverified.

## Universal bridge

C020 whole-set witness cost moves from a derivative-local repair that could not pay off-support spectra to an explicit normalized reference for one shared blocker bit, with the exact activated output cost and every empty-row, terminal and signed collision term retained. No universal constant is improved: the remaining conditional KL/reference excess and terminal conversion costs lack a general influence-paid bound. NEXT compares this ledger with the corrected occupation-based whole-set mass on the same physical spectrum, directly connecting B02's mass gains to B03's unpaid all-density transfer rather than proving another isolated FEI class.
