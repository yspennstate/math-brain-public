# A041 stage 2: deficit-paid two-weight slices

## exact target, quantifiers, hypotheses and units

The B09 lead directs the full two-weight target `E_ge2(F) <= K Delta(F)` for `F=2*1{w sum_A X_i+sum_B Y_j>=t}-1`, arbitrary arities, real positive w, threshold t, and every product bias. `E_ge2=sum_{|S|>=2} P(S) ln(v_S/P(S))` is in **nats**, `Delta=I-Var` is spectral deficit, and corrected FEI+ in bits is `Hplus=E/ln 2`. Deterministic inputs are contracted before normalization; signed weights can be oriented.

**Closed this stage:** the entropy target when A consists of **one exceptional physical input**, with all the stated weight/arity/bias quantifiers retained. Put `c=460+80 ln 2`, the symmetric-threshold baseline in nats. The complete proof gives

`E_ge2(F) <= (4c+12+4/e) Delta(F)` and `Hplus(F) <= [(4c+16+4/e)/ln 2] Delta(F)`.

The displayed corrected-entropy constant is **below 3000**, certified by four rational terms of the ln 2 series and e>8/3; it is deliberately unoptimized. The class contains both recovered weighted counterfamily regimes and the nonsymmetric prime family `F_n=2*1{2X+sum_{j=1}^n Y_j>=3}-1`, every n>=3, at all biases. The proof of that family's primality is included; no bounded prime-arity hypothesis is imposed.

**Still open:** arbitrary numbers of exceptional-weight inputs, all weighted biased thresholds, all biased prime gates, and full uniform FEI. For the full two-group class the stage proves exact covariance and mixed-spectrum energy identities, not an entropy bound. There is no new counterexample to FEI+ and no inference that a proper prime family settles all primes.

## sources actually read, revisions and theorem locators

The complete protocol revision `2026-10-11-execution-v2`, updated BOARD (23:29 UTC snapshot), B09 `STREAM_NOTES.md` v1 (22:45 UTC), and own STATUS/LEARNED were read at intake. Unlike stage 1, lead notes are now available. They independently reconstruct the earlier endpoint coefficient 1/2 and singleton bound, direct A041 to two-weight higher-degree entropy, and say not to repeat the rank estimate. This stage follows that direction. The lead's uniform optimal endpoint-tax development is not a premise here.

Primary baseline: the 38-page threshold text, Theorem 6.6, plus the same theorem in `baseline/current-threshold-paper.tex` at `bias:strong`; its exact constant is `C_T=80+460/ln 2`. Equation (62) supplies the coherent squared-amplitude entropy inequality. Stage 1 had read the full symmetric normalization/near-dictator proof; this stage rechecked the theorem and coefficient inequality rather than reopening the baseline. The legacy extracted text needs cp1252 decoding; treating it as UTF-8 first produced a read error, after which cp1252 succeeded. No mathematical claim was inferred from the failed read.

The original reductions `paper/biased.tex` controls and composition identity retain the exact stage-1 locators and scopes. A043's original `REPORT.md` and its complete structural/biased endpoint derivation were read for the necessary cofactor-row criterion and the universal prime-gate bridge. The new prime family's nonfactorization is reconstructed directly in this stage's proof, rather than assumed from a finite census. Updated board results from A042/A045/A096 were considered to avoid duplicating endpoint work; none of their new unreviewed claims is a premise. `out/SOURCE_RECEIPTS.json` pins the actual source bytes and locators used.

## complete derivation or exact first unsupported line

The complete analytic proof is `SLICE_DEFICIT_PAYMENT.tex`. Its key cancellation is not the earlier rank estimate. Distinct count thresholds have disjoint pivotal boundary events for every coordinate, at arbitrary product biases. Hence their cross Dirichlet form is zero. The covariance of nested tail signs is the negative of their high-degree deficit inner product, yielding `Cov(f0,f1) <= sqrt(Delta0 Delta1)`. For the band sign `g=f1-f0-1`, this gives `Delta(g)=Delta0+Delta1+2Cov <= 2(Delta0+Delta1)`.

Use the scalar coherent entropy inequality only on degree at least two, so its additive squared-amplitude overhead is paid by the higher-degree mass, which is at most the deficit. The singleton bound `4 Delta` in nats is also proved here for every Boolean sign, including the nonmonotone band; it does not require the gate to be monotone. The resulting two-tail entropy estimate is `E(g) <= (2c+10)(Delta0+Delta1)`.

For one exceptional input with bias p, the restrictions f0,f1 are precisely symmetric count thresholds. Coefficients avoiding that input are the actual coherent average `(1-p) f0hat+p f1hat`; coefficients containing it are `sqrt(v) dhat`, where `d=(f1-f0)/2`, rho=E d, v=4p(1-p). The exact deficit ledger is `Delta(F)=D+delta`, `D=(1-p)Delta0+pDelta1`, `delta=v rho(1-rho)`. The high-degree avoiding-input sector costs at most `(2c+2+4/e)D`; the containing-input sector costs at most `(2c+10)D+(ln 4)delta`. This proves the displayed theorem. No incoherent-mixture substitution or physical TC estimate is used. Identical or constant restrictions and deterministic endpoints are handled directly.

For arbitrary A, merge identical symmetric B slices into cells c_s(A), with probabilities pi_s. The matrix with diagonal `Delta(f_s)` and off-diagonal `-Cov(f_s,f_u)` is an exact positive-semidefinite deficit Gram matrix. It gives `2 sum_{s<u} pi_s pi_u Cov(f_s,f_u) <= sum_s pi_s^2 Delta(f_s)`. In addition, the mixed spectral B-energy is exactly `sum_s pi_s(1-pi_s) I(f_s) <= Delta(F)`. The full ledger is `Delta(F)=sum_s pi_s Delta(f_s)+delta_A`, where `delta_A=I_A(F)-Var_A(E_B F)>=0`.

These budgets overlap and cannot be spent twice. The averaged slice deficit gives `( |S_B|-1 )P(S)` on every set with nonempty B part; delta_A gives `|S_A|P(S)` on mixed sets and `(|S_A|-1)P(S)` on pure-heavy sets. Their sum is the one conserved root deficit. This accounting is part of the proof, not a promise of an extra reserve.

**Exact first unsupported line:** there is no established arity-independent normalized entropy reference for `Fhat(S_A,S_B)=sum_s chat_s(S_A) fhat_s(S_B)` that pays all mixed coefficients and the pure-heavy high-degree sector by that ledger. The Gram inequality controls energy covariance, not the logarithmic cost of the whole spectral set. Iterating the one-exceptional theorem multiplies constants and does not close arbitrary |A|. The all-two-weight entropy target therefore remains open.

## executed validation with domain, arithmetic, commands and outputs

The domain and arithmetic were frozen before execution. `FROZEN_SPEC_V1.json` preserves the first spec; `FROZEN_SPEC.json` records v1.1's fixed output compression rule. The first pilot failed while serializing a rational entropy-ratio endpoint exceeding Python's 4,300-digit integer-to-string limit. It saved no completed census. `out/PILOT_V1_FAILURE.txt` records that failure. The repair projects saved rational intervals **outward**, exactly, onto the fixed grid 2^-80. Internal Fraction arithmetic, 20-term range-reduced atanh intervals, family, count, and runtime cap are unchanged; there is no precision or dimension escalation.

Executed command:

`python -X utf8 runs/20261011T232825Z-fleet05-A041-weighted-threshold-fei/code/check_slices.py`

Output: **PASS, 436 actual Boolean two-weight gates, 27,188 exact assertions, 1.670 seconds of observed Python runtime**. The domain includes 297 one-exceptional gates with two/three equal-weight inputs and all listed attained-score thresholds; 126 full two-group cases with |A|=|B|=2 or 3; and all 13 inherited finite weighted control cases. The memory estimate is 60 MB, below the admission threshold; no heavy job or GPU was used. The checker verifies full rational product spectra, Parseval, independently averaged physical means, exact child coefficients and pivotal/variance relations, zero cross Dirichlet forms, covariance Cauchy--Schwarz and deficit Gram entries, full root/slice/mixed-energy identities, and rational-interval finite corrected entropy ratios. Saved output is `out/EXACT_SLICES.json`; the maximum finite ratio fixture is separately in `out/MAX_RATIO_FIXTURE.json`. It does not establish an optimal constant or replace the analytic continuum proof.

Executed command:

`python -X utf8 runs/20261011T232825Z-fleet05-A041-weighted-threshold-fei/code/check_prime_fixture.py`

Output: **PASS** for the already included four-input gate weights `(2,1,1,1)`, threshold 3. All 16 truth-table inputs are exact, all four variables are essential, and each of its ten proper blocks has at least three cofactor rows. Spec: `PRIME_FIXTURE_SPEC.json`; output: `out/PRIME_FIXTURE.json`. The all-arity prime-family argument is analytic, not extrapolated from this fixture.

The covariance-to-deficit factor two is sharp: uniform AND_2/OR_2 tails have deficits 1/4 and covariance 1/4; their band sign is a parity with deficit one. Their two-slice majority truth table is among the frozen cases. This prevents an unsupported coefficient-one repair of the band ledger.

## proof dependencies and changed downstream conclusions

The only non-elementary entropy premise is the source-complete symmetric-threshold corrected FEI+ baseline, C004/Theorem 6.6, at the pinned current source. The scalar inequality is reproduced, and all subsequent product Fourier, covariance, singleton, and slice identities are derived here. The A043 necessary cofactor criterion is reconstructed on the page; no conditional all-prime entropy bound is assumed. No dependency on the stage-1 rank result or an unreviewed endpoint tax is used.

A044 receives an actual all-bias nonsymmetric threshold/prime class and the remaining multi-slice obstruction, instead of another constant-fit conjecture. A042/A045 receive explicit zero-deficit and deterministic contractions, and A091/A090 receive the full coherent proof and exact slice fixtures. B20 receives a bounded prime family at unbounded arity but must not adopt an all-prime or full-two-weight conclusion. Exact disjoint corrected-entropy/deficit composition would propagate the proved one-exceptional gate constant through read-once formulas using these gates and already certified gates; it does not permit shared physical inputs or resolve all primes.

The three original controls are explicitly replayed in `WEIGHTED_GUARD_LEDGER.md`: coefficient-one pivotal failure stays coefficient-one, conditional-input TC stays distinct from spectral erasure, and every member of both recovered two-branch families lies in the new proved class. No shared file, another agent folder, brain, or remote repository was modified. The current result is a scoped completion/application of the entropy gap under the lead's direction; independent review remains pending.

## one next mathematical action and independent reviewer

Use the exact multi-slice deficit Gram matrix to construct one normalized reference for the entire coherent mixed spectral set, retaining its pure-heavy sector and charging `( |S_A|+|S_B|-1 )P(S)` only once. Test the reference on the sharp majority fixture and on the recovered rare two-branch families before adding a larger domain. A091 should reconstruct the coherent entropy and covariance payments; A090 should challenge the general-matrix ledger and prime-family argument. A045 should independently check boundary contraction and all-bias normalization. No further isolated class enlargement or endpoint-tax recalculation is the proposed next step.

## actual persistence receipts or precise save blocker

All proofs, specs, scripts, exact outputs and protocol records are local to the assigned A041 stage-2 folder. `CLAIMS.json` has the fourteen required fields per claim; `PROGRESS.json` has the eighteen required fields, interpreting the protocol's parenthetical packet_ids note as documentation; `PACKET_DELTA.json` is byte-identical with packet_ids=[A041]. Rolling STATUS, WORKLOG and LEARNED are current. `out/PERSISTENCE_RECEIPTS.json` records sizes and hashes; local readback verifies them. No file exceeds 20 MB. No save blocker remains. Supervisor copy, external review, mirror verification and downstream use are not claimed.

**Universal bridge:** This stage moves the B09 lead's all-bias prime-gate bridge by paying higher-degree corrected entropy with an explicit constant on every one-exceptional-weight threshold, including a proved nonsymmetric prime family of unbounded arity; it also supplies an exact, conserved deficit interface for all two-weight slices. It does not establish C018, C019, C020 or C024 universally, and neither all two-weight gates nor all primes are closed. The remaining mathematical charge is the normalized logarithmic cost of the coherent multi-slice spectral set and its pure-heavy sector; covariance and energy are now explicitly paid. NEXT targets that single entropy-reference obstruction, with the sharp fixtures and one nonreused budget, because this is the shortest route within B09 toward an all-prime entropy payment rather than collecting more isolated classes. A slice-specific reference would still leave nonsymmetric arbitrary primes; its transfer beyond symmetric-slice geometry must be proved before any full-FEI conclusion.
