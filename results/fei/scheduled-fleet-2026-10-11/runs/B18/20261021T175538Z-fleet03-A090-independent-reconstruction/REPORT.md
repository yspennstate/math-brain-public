# A090 independent reconstruction: the original bank pays every no-reset history on the neutral fixture

## exact target, quantifiers, hypotheses and units

Verdict: **HOLDS** for the six quantitative payment and frozen-escrow conclusions in A001-NEUTRAL-CORE-ACTUAL-DATA-TRANSFER@1, and for the abstract no-reset identity in A096-PAID-FLOOR-NO-RESET-HISTORY@1. A001's separate comparison with a named pending shadow reservation is not independently accepted because that reservation is not defined in the statement. A096's priced A097 application is accepted only conditionally on its explicitly supplied A097 floor bound. That floor's proof is not independently accepted by this report. Full FEI remains **OPEN**.

All entropies, cross-entropies and divergences are in bits. Functions are actual Boolean signs on finite uniform physical cubes. Influence means ordinary flip influence. A reference Q is normalized and positive wherever the actual squared Fourier law P is positive; reference-only mass and the empty Fourier set are retained. Only fresh physical coordinates are queried, with fair outcome probabilities, on a finite possibly adaptive tree. Children inherit the same reference by marginalization unless an explicit reset cost is charged.

The finite fixture is the nine-bit sign F(y,x)=b(y)+1[y=0](Maj3(x)-1), with six data bits, three fresh majority bits, and b positive exactly when its first three data bits are zero. Its original core influence quota is 4 I0=3, with I0=(I(b)+I(b-2*1_origin))/2=3/4. The incoming reference for the stronger conclusion below is Q=P_F, accompanied by the actual Fourier phases. No arbitrary incoming Q or unrelated pre-existing charge is silently admitted.

## sources actually read, revisions and theorem locators

The execution protocol is fei-execution-protocol/2, revision 2026-10-11-execution-v2, read in full. The current user endpoint 2026-10-23 14:49 UTC overrides its older endpoint. BOARD.md, written 2026-10-21 17:55 UTC, A090 STATUS.md and LEARNED.md, and B18 STREAM_NOTES.md v2 were read. The latter's old five-variable census instruction is superseded in dispatch by the productive saved same-reference gap; no new census is run.

Statements were read from A001/runs/20261014T074909Z-fleet05-A001-quantifier-audit/CLAIMS.json and A096/runs/20261014T094929Z-fleet05-A096-live-gap-ledger/CLAIMS.json. The A097 conditional premise was read from A097/runs/20261014T050248Z-fleet05-A097-cross-route-transfer/CLAIMS.json. No producer DERIVATION.md or checker was imported or used to reconstruct these implications. The current A099 claim package and the campaign indices were inspected for scope and dependencies.

Original definitions and the physical restriction amplitudes u+v,u-v are in the supplement sources/ERASURE_REDUCTION.md, sections 1 and 4, read in full. Threshold_paper_38pp.txt, section 8.2, Proposition 8.6 and equations (75)-(79), was read directly, together with introductions and targeted locators in both threshold versions and both percolation versions. Those paper text files are cp1252, not UTF-8; decoding was explicit after a strict UTF-8 read failed. The percolation theorems and earlier threshold bounds supply no premise in this proof. Campaign, seed, counterexample and mapping files were inspected at relevant sections; this is not an independent review of the entire manuscripts. SOURCE_RECEIPTS.json records the local byte hashes and review scope. No external publication, mirror save or new literature search is claimed.

## complete derivation or exact first unsupported line

Let a_T and a_(T+j) be actual signed parent amplitudes and put p_0=a_T^2, p_1=a_(T+j)^2, m=p_0+p_1. The child probabilities at T are (a_T+a_(T+j))^2 and (a_T-a_(T+j))^2. Their average is m. Booleanity ensures each child law is normalized. This is a physical restriction statement, not spectral conditioning.

Put q_0=Q(T), q_1=Q(T+j), q=q_0+q_1. The full conditional occupancy divergence is

R_j = sum_T sum_(e=0,1) p_e log2(p_e q/(m q_e)),

with zero-p terms omitted. For m>0, q>0 by finite CE. On each such fiber the two normalized conditional distributions are (p_e/m) and (q_e/q), so R_j is a sum of m-weighted KL divergences and is nonnegative. All Q-only mass remains in q. Gibbs' inequality follows from ln t<=t-1 applied on the positive-p support, including the possible missing reference mass. No independence across fibers or coordinates is assumed.

Direct expansion, fiber by fiber, gives

CE(P,Q) - CE(P_minus_j,Q_minus_j) = B_j(P)+R_j.

Cross-entropy is linear in its first argument. Since the average actual child law is P_minus_j, this is exactly

CE(P,Q) = B_j + (CE(P_plus,Q_minus_j)+CE(P_minus,Q_minus_j))/2 + R_j.   (1)

Multiplying (1) by each node's actual reach probability and summing over a finite adaptive tree cancels every internal CE term once. Therefore

sum_v w_v B_v + sum_leaf w_leaf CE(P_leaf,Q_leaf) + sum_v w_v R_v = CE(P_root,Q_root).   (2)

This proves the abstract A096 continuation theorem, including unequal stopping depths, constants, spectral zeros and retained full terminals. Its priced application follows by substituting the supplied A097 root inequality CE_root<=(2C0+10) I(F); no new estimate of that floor is needed or inferred. A reference chosen as the true child law has zero KL, but using that choice does not establish a cheap universal root bound.

For the A001 fixture, the complete root spectrum has one atom 2401/4096, seven atoms 225/4096, 56 atoms 1/4096, 256 atoms 1/16384, and 192 zeros. These counts sum to 512 entries and the probabilities sum to one. Consequently

H(F)=385/32-(2401/1024)log2(7)-(1575/2048)(log2(3)+log2(5)) < 489/200.

The strict inequality has a rational log-interval certificate in code/check.py. In particular 3-H(F)>111/200. Substituting Q_root=P_F into (2) proves, for **every** finite adaptive stopping tree on this particular fixture,

sum_v w_v B_v + sum_leaf w_leaf [H(P_leaf)+D(P_leaf||Q_leaf)] < 489/200 < 3.   (3)

Thus the same original quota pays all already executed prefix erasures, every continuation erasure, and both full terminal reference debts. The original unused margin remains greater than 111/200; each accumulated R only increases the margin. No fresh bank is created at a child. The universal quantifier over trees in (3) follows from the analytic identity, not an enumeration of all tree policies. A separately pre-booked charge d can be included only if its own remaining-budget condition d+H(F)<=3 is verified.

The six A001 data-first, majority-next policies reproduce its stated narrow bounds. For active data queries, the actual entropy-terminal margin exceeds 1.112678 and the frozen-escrow margin lies between -0.028552 and -0.028551. For dummy data queries, the corresponding margins exceed 0.634309 and lie between 0.546819 and 0.546820. Keeping the inherited terminal CE instead of terminal entropy still leaves margins greater than 0.568250 (active) and 0.571248 (dummy). These are paid from one original bank, with the actual encoder interaction already present in the actual restriction spectra.

The constant-child obstruction in A096 is also reconstructed exactly. The actual three-bit table [1,1,1,1,-1,1,1,1] with matching initial Q has, after querying bit0 and taking outcome1, a constant +1 child. Its inherited Q is (5/8,1/8,1/8,1/8), so its influence is zero but its terminal CE is log2(8/5)>0. This rejects a bound on every inherited leaf CE by that leaf's own influence. It does not reject the ancestor budget (2) or all possible paid resets.

The first unreconstructed source clause in A001 is: "The actual Maj3 encoder erasure differs positively from the pending shadow-plus-inherited reservation." The statement does not define that reservation as a formula in the restricted amplitudes, so the signed difference is not a uniquely specified quantity to check. The actual encoder erasures are included in W throughout our reconstruction, and the stated payment margins require no such comparison. This is a precise limit of this statement-only review, not a refutation of the subsidiary clause or an invitation to treat it as proved.

The first unpaid universal line is the replacement of a paid, inherited reference by a fresh cheap reference on an arbitrary non-flat child while preserving the one unused ancestor account. For prescribed fresh child references Q'_s define Delta_s=CE(P_s,Q'_s)-CE(P_s,Q_minus_j). Then the exact reset ledger is

B_j + avg_s CE(P_s,Q'_s) = CE(P,Q)-R_j+avg_s Delta_s.   (4)

A local transfer therefore needs avg Delta_s<=R_j plus a specifically identified unused reserve. Neither (1), the scoped A097 floor, nor the finite fixture certifies that inequality for every arbitrary Boolean child. More generally the existence for every f of a normalized Q with CE(P_f,Q)<=K I(f) is equivalent to FEI itself: H(P)<=CE(P,Q), and conversely Q=P gives equality. Treating that root premise as already paid would be circular. No unsupported implication is found within A001's explicitly quantified payment conclusions or A096's abstract no-reset identity; the universal fresh-floor admission remains unsupported, separately from A001's undefined subsidiary comparison.

## executed validation with domain, arithmetic, commands and outputs

Frozen spec: out/FROZEN_SPEC.json, written before execution. Independent helper: code/check.py. Command: `python -X utf8 runs/20261021T175538Z-fleet03-A090-independent-reconstruction/code/check.py` from A090. Integer Walsh transforms reconstruct exact spectra; a separate direct character-sum calculation checks all 512 root coefficients. All 278 Boolean truth tables through three variables, every coordinate and three references (matching, uniform, half-matching/half-uniform) check the exact channel identity. One outcome-dependent full tree per table/reference checks complete telescoping. No symmetry reduction or dimension escalation is used. Six labeled nine-bit stopped policies retain all terminals; nine first-query identities are checked. The constant-child witness is checked directly.

Every entropy equality is a rational linear form in logarithms of primes and cancels exactly. Signs use rational intervals for ln x=2 sum_(k=0..39) t^(2k+1)/(2k+1)+error, t=(x-1)/(x+1), with 0<=error<=2 t^81/(81(1-t^2)), after reduction to 1<=x<=2. Division by positive certified ln2 bounds gives log2 intervals. Floating displays in CHECK.json are summaries; no asserted sign depends on them. The strengthened final run and exact assertion count are recorded in out/CHECK.json.

The memory gate before the Lean attempt exited 0. The supplied lean_check.py was asked to check only the pair-average algebra identity ((u+v)^2+(u-v)^2)/2=u^2+v^2. It returned RUNTIME_UNVERIFIED after its 60-second cap, with formal_target_verified=false and no axiom certificate. out/LEAN.txt preserves that receipt. This is **not** a Lean pass or a refutation. The general result's rung is a direct mathematical proof; finite bounds have exact rational certificates. No full theorem is labeled Lean-checked. The successful certificate pilot ran in approximately 31 seconds and its memory estimate was 40 MB; no heavy search, GPU or remote compute was used.

## proof dependencies and changed downstream conclusions

A001's six payment and frozen-escrow conclusions are independently accepted unchanged; its undefined shadow-reservation comparison is left unreviewed. A096's abstract channel and arbitrary finite no-reset history theorem are independently accepted unchanged; its A097 priced corollary retains the explicit external floor premise. Its inherited-constant-leaf obstruction is independently accepted unchanged. A097's negative-cell floor is not promoted to an arbitrary-core theorem. The general accounting is standard chain-rule machinery, not a new universal FEI result.

The derived change for A001/A004/A081/A096 is (3): for this actual fixture and its matching incoming reference, the next mixed query does not require another local subsidy theorem if the reference is only marginalized and all terminal CE is retained. Every adaptive no-reset continuation fits the original quota, including prefixes already executed inside this account. A demand to reset to a prescribed descendant floor is a different obligation and must expose the signed cost in (4). This does not certify an unrelated old debit or renew a source account.

## one next mathematical action and independent reviewer

Next: A097/A094 should supply one actual weak non-flat child query, its prescribed fresh Q'_plus and Q'_minus, the actual old debit and the remaining original bank. Certify the signed reset cost avg Delta in (4) against R_j and that same unused reserve, retaining both terminal CE terms. A086/A094 should independently review this report's all-tree fixture corollary and its scope; A081/A096 are consumers. A090 contributes the corollary and therefore does not claim independent acceptance of that new corollary.

## actual persistence receipts or precise save blocker

All stage artifacts are saved only under the requested A090 run directory; rolling STATUS.md, WORKLOG.md and LEARNED.md are updated inside A090. out/CHECK.json, out/LEAN.txt and out/FROZEN_SPEC.json preserve execution evidence; SOURCE_RECEIPTS.json and out/ARTIFACT_RECEIPTS.json bind local files by SHA256. CLAIMS.json uses the exact protocol claim fields; PROGRESS.json and PACKET_DELTA.json use its progress fields with packet_ids=["A090"]. Local readback and schema checks are the persistence receipt. Supervisor/GitHub/brain adoption and any second independent acceptance remain unverified; no shared tree, brain store, external repository or other agent folder is modified.

**Universal bridge:** This stage moves C019 stopping-tree payment and C024 history transfer at a precise scoped point: A096's full no-reset telescope is independently reconstructed, and one actual non-flat A001 fixture now has every adaptive no-reset continuation paid by one original three-bit quota, with more than 111/200 bits of unused margin and full terminal KL retained. It adds no universal constant. What remains is paid fresh-floor admission on arbitrary Boolean histories, rather than another no-reset identity or another isolated finite sweep. The next signed-reset instance directly tests that missing universal interface and is the shortest remaining route from this audit to full FEI.
