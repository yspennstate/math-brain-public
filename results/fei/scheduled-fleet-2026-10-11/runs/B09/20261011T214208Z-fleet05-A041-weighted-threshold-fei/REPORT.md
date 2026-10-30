# A041: biased weighted pivotal intervals and a necessary endpoint tax

## exact target, quantifiers, hypotheses and units

The packet target is an arity-independent replacement probability or entropy estimate for actual Boolean weighted thresholds under arbitrary product biases, surviving the three recovered physical-input TC/pivotal normalization controls. The stronger campaign target remains corrected FEI+: `H_mu^+(f) <= C [I_mu(f)-Var_mu(f)]` for all real weights, all arities, and all product biases. **That stronger target and full uniform FEI remain OPEN.**

Two source-complete auxiliary results are proved here, pending independent review:

1. For the i-th pivotal interval and every integer r>=1, coordinates of weight at least w_i/r have fiber height at most r. With `L=2 sum min(q_j,1-q_j)` on those coordinates and derivative spectral rank K, `E_nu (1-epsilon)^K <= min(1,r/sqrt(epsilon L))`. The positive logarithmic rank score `ln^+[L/(r^2(K+1))]` has mean at most `3+ln 2`. A simultaneous choice among all dyadic scales, using prior `pi_k=1/[(k+1)(k+2)]` and score `sup_k pi_k^2 L_k/[4^k(K_k+1)]`, retains that same constant. Summing the score against the actual coordinate Fourier masses costs at most `(3+ln 2) I` in **nats**. The proof covers arbitrary positive real weights; orientation covers signed weights, and contraction covers zero weights/deterministic biases.
2. For actual Boolean `f=1-2XY`, `X~Ber(p)`, `Y~Ber(1/4)`, revealing X, the difference between physical-child mixture information J and conditional spectral-label entropy M satisfies `lim_{p->0}(J-M)/[p log_2(1/p)]=1/2`. Thus a scalar tax valid for every Boolean one-bit reveal must have asymptotic lower coefficient at least 1/2; no finite `Kp` tax works. This result is in **bits**.

## sources actually read, revisions and theorem locators

The complete execution protocol is `fei-execution-protocol/2`, revision `2026-10-11-execution-v2`. The canonical README, CURRENT_STATUS, claims/obstructions registry, A041 packet entry, B09 dispatch entry, and weighted-guards/A041 portions of the campaign plan were read. The board was read on intake and refreshed during derivation. B09 `STREAM_NOTES.md` was absent on both checks; no lead direction was available.

The relevant primary mathematical source is recovered `source_material/reductions/paper/biased.tex`, read in full: `biasfull:hplus`, `biasfull:pivotal`, `biasfull:composition`, `biasfull:mixture`, `biasfull:weightedcounter`, `biasfull:creditremark`, and `biasfull:localTC`. Its statements are imported with their stated source scope, not elevated by registry labels. The supplemental CAMPAIGN, CLAIMS, COUNTEREXAMPLES, SEED_LEMMAS, and NATIVE_MAPPING were consulted; the normalized prior convention motivates paying the scale selection explicitly. The local `ERASURE_REDUCTION.md` and `ERASURE_RIGIDITY.md` distinguish spectral erasure from physical event-conditioned TC.

The threshold 38-page text was read for sections 3.1--3.4 (fiber antichains, Sperner and uniform relative noise), 4.1--4.3 (rank references), 6.1--6.4 (biased normalization, refresh, symmetric rank and normalization credit), and the weighted product-measure question in section 9.2. Its earlier 29-page version was checked for its different constant and scope. The percolation current/earlier introductions and normalization sections were consulted for the distinction between physical pivotal and spectral inclusion probabilities; their geometric theorems are not dependencies of this proof. No claim of a full end-to-end audit of those papers is made.

The recovered B09 run `20261011T195500Z-fleet01-B09-biased-restriction-uncertainty/REPORT.md` was read in full, as was `verification/B09_interval_repair_20261011/REPORT.md`. The endpoint lower-bound result repairs the specific unsupported inference in original B09 section 5(4); it does not independently accept B09's entire Maassen--Uffink/composition package. Seven local byte/hash receipts are in `out/SOURCE_RECEIPTS.json`. No priority or publication novelty claim is made.

## complete derivation or exact first unsupported line

`WEIGHTED_THRESHOLD_REPLACEMENT.tex` contains the full proof. A pivotal interval has width w_i and is half-open. On the selected coordinates every chain with r strict steps increases the score by at least w_i, so its support has height at most r and partitions into r antichains. Independent biased refresh has an independent fair-activation count of mean epsilon L. Conditional Sperner and `E[1/(F+1)] <= 1/(epsilon L)` give the relative noise bound. The orthonormal noise identity turns it into a derivative spectral bound. Taking epsilon=1/(2b), where b is the rank cutoff, gives the tail `sqrt(2e) exp(-u/2)`. At dyadic scale k the prior-weighted tail has factor pi_k; the factors sum exactly to one. Integration gives `3+ln 2`, without an arity factor or an uncharged choice of scale.

The theorem does not estimate conditional-input TC. For the recovered weighted family, the entire fair-activation mass is below 2, so every prior-weighted rank score is below 1/2 and all its positive logarithms vanish. In the fixed-m, q->0 local-TC regime the same conclusion holds eventually. Both controls survive directly. The pivotal-credit failure remains exactly **coefficient one**, with no inference about larger multipliers.

The elementary singleton corrected entropy is bounded by `4 Delta` in nats for every monotone gate; the proof is recorded in the TeX. The **first unsupported line** in the FEI+ continuation is a bound `sum_{|S|>=2} P(S) ln(v_S/P(S)) <= K Delta`, derived from a normalized spectral reference or another structural argument. The proven rank bound costs I; it cannot be substituted for a deficit payment near dictators. Paying that higher-degree entropy would prove weighted FEI+ with constant `(K+4)/ln 2` in bits. Exact disjoint composition would then extend the gate theorem to read-once formulas without a depth factor. This implication is conditional.

`ENDPOINT_TAX_LOWER_BOUND.tex` proves the second result directly. The four Fourier masses are `((1-2pq)^2,4p(1-p)q^2,p^2v,p(1-p)v)`, v=4q(1-q). Hence `J-M=2h_2(pv)-H(P)-p h_2(v)`. Expanding the two order-p spectral atoms yields coefficient `4q(1-2q)` on `p log_2(1/p)`, equal to 1/2 at q=1/4. The old available upper tax has coefficient one; its optimal coefficient is not determined. The lower-bound family establishes necessity through an actual signed difference.

## executed validation with domain, arithmetic, commands and outputs

The specs were saved before each execution in `FROZEN_SPEC.json` and `ENDPOINT_FROZEN_SPEC.json`. Both pilots were far below the 60-second cap and estimated below 30 MB; no heavy job, dimension escalation, GPU, external process, or memory admission was needed.

Command: `python -X utf8 runs/20261011T214208Z-fleet05-A041-weighted-threshold-fei/code/check_replacement.py`.

Output: PASS, **253 actual Boolean weighted threshold cases, 42,189 exact Fraction assertions**, observed Python runtime **1.149 seconds**. The checker uses weighted finite differences and rational squared product Fourier coefficients, independently computed means/physical edge pivotal probabilities, Parseval, every coefficient derivative relation, fiber comparable-pair checks, and squared rational noise inequalities at fixed r=1,2,4,8,16,32,64 and epsilon=1/4,1/2,1. Designated n<=4 cases also reconstruct physical refresh kernels independently of the Fourier moment. The domain is 216 three-bit cases, 24 four-bit cases, five global-control cases m=2..6, and eight local-control cases m=2..5, q=1/8,1/32. Saved output: `out/EXACT_VALIDATION.json`.

Command: `python -X utf8 runs/20261011T214208Z-fleet05-A041-weighted-threshold-fei/code/check_endpoint.py`.

Output: PASS for six two-bit AND gates q=1/4, p=2^-k, k=2..7. The four masses and the sign `J-M>0` were checked exactly with rational logarithm intervals: 24 atanh terms after power-of-two range reduction and signed four-corner division. Saved output: `out/ENDPOINT_VALIDATION.json`. The finite rows do not prove an asymptotic limit; the analytic expansion above does.

## proof dependencies and changed downstream conclusions

The rank proof uses Sperner's theorem and an explicitly reproduced elementary bound on central binomial density, product orthonormal Fourier/refresh identities proved on the page, and a normalized telescoping prior. It does not use uniform FEI, weighted FEI+, an assumed TC payment, or B09's unreviewed uncertainty theorem. The endpoint proof uses only the actual two-bit truth table, orthonormal Fourier normalization, and elementary entropy expansion.

Downstream A042/A045/A084 can use the endpoint construction and explicit contractions after independent review; A044/A091 can use the multiscale rank interface and the conditional composition statement. B20 can replace the unsupported endpoint-necessity inference with a source-complete actual Boolean lower bound. The global payment and optimal tax coefficient remain open. No shared claim registry or another agent's output was modified; independent acceptance, ingestion, mirror verification, and downstream use are not claimed.

## one next mathematical action and independent reviewer

Construct a normalized reference for the higher-degree spectral mass using the biased weight-band rank estimate, and identify explicitly the variance normalization and near-dictator terms it leaves. A091 should independently reconstruct the refresh/tail/prior proof; A090 should independently reconstruct the two-bit endpoint expansion. A045 should audit orientation and deterministic contractions. Two new complete claims are pending, so the next broad candidate should wait for review or proceed as a repair/application of these claims.

## actual persistence receipts or precise save blocker

All outputs are local to A041's authorized folder. `CLAIMS.json`, `PROGRESS.json`, and its identical compatibility copy `PACKET_DELTA.json` are written with exactly the protocol field sets. `out/PERSISTENCE_RECEIPTS.json` records each finished run artifact's size and SHA256; the rolling STATUS, WORKLOG, and LEARNED files are current. No artifact exceeds 20 MB. No save blocker was observed. Supervisor copy, GitHub/Brain persistence, independent review, and public release have not been performed or claimed.
