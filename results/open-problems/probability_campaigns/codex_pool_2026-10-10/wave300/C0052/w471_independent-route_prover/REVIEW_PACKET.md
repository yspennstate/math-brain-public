# C0052 review packet for w473

Disposition requested: KEEP/FIX/DROP on each conditional claim, separately from the parent problem. No parent-solved claim, independent KEEP, or formal-check receipt is supplied by the author. Current openness is UNKNOWN; novelty is not asserted.

Read STATEMENT_PACKET.md first for the exact primary target. ROUTE_PRECOMMIT.md establishes the independent-method checkpoint. ATTEMPT.md contains the full proofs, assumptions, prior-attempt digest, failed closure, and single hardest gap. CLAIMS.jsonl contains individually labeled source, conditional-result, gap, and control rows. SOURCE_STATUS.json and LOCAL_SOURCE_RECEIPT.json separate primary-source verification from unreviewed historical intake/store material.

Claims to audit:

1. L1: For bounded symmetric S of positive variance V, assuming all MGF zeros are imaginary, F(z)=product_j(1+z^2/y_j^2), V=2 sum y_j^-2 and kappa4=-12 sum y_j^-4. For r=sqrt(V)y_1, B=3-E(S/sqrt(V))^4 obeys 12/r^4<=B<=6/r^2. Gaussian weak convergence of such a sequence is equivalent to r escaping to infinity. Check multiplicities, the order of H(w)=F(sqrt(w)), the absence of an exponential factor, and uniform integrability.
2. L2: In the subcritical infinite-volume free Gibbs state on Z^3, assuming nonnegative/summable two-point function, positive finite exponential xi, and nonpositive/summable U4, choose ell capturing chi/2, R=max(1,ceil(xi),ell), and the block |x|_infinity<=2R. The first block-field zero times the block standard deviation satisfies g_+>=3/r^4. Check the block is the actual Gibbs marginal, the all-index sum, the inner-cube estimate V>=N chi/16, N>=64 xi^3, and the direction of the inequality. The reverse implication r->infinity implies g_+->0 is not claimed.
3. Control: N independent fair spins (also scaled by a positive constant) satisfy the Lee–Yang property while r=pi sqrt(N)/2 and B=2/N. In the scaled example the raw zero tends to zero while normalized zeros escape. This refutes an insufficient generic implication, not C0052.

The remaining conjectural step is liminf_{beta increasing to beta_c} r_beta<infinity for the exact blocks in L2. An eventual uniform bound is stronger. Thermodynamic first-zero convergence, a different box boundary law, or a small finite-volume experiment cannot substitute for this step. Any new referee lemma requires the separately named independent referee w476.

Validation: MEASUREMENTS.json reports 23 analytical/finite cases, including 15 complete enumerations of 1,620 spin configurations, and eight integer geometry checks, with zero failures. Maximum relative cumulant discrepancy is 4.17e-15. Run python -X utf8 ~/brain_workers/w471/check_lemmas.py if an independent replay is needed. FINITE_CONTROLS.jsonl saves each completed case. This is a numerical diagnostic, not proof of the critical estimate, independent mathematical review, or formal verification.

BUNDLE_STATE.json identifies the DRAFT inbox file. Its four entries are concepts with explicit review-pending labels and owner-own-work sources. Three internal relations follow the derivation and control boundaries; a cited existing C0052 target is included only if found in the read-only canonical-store check. No relation says the parent problem is proved. REVIEW_HASHES.json freezes local review artifacts only; the coordinator owns bundle source manifests/digests and store integration.

Author served-model receipt: unavailable in response-side metadata accessible in this session. Requested gpt-6.1-sol/max/Fast settings are not served-identity evidence. Referee served-model evidence and independent-review result remain pending.

NEXT: Audit the factorization/application and the g_+>=3/r^4 bridge; retain the normalized first-zero bound as the open proof obligation.
