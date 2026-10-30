# exact target, quantifiers, hypotheses and units

Complete the unfinished biased-child stability application directed by B05 v2: locate log(1/mean) splits, decide whether their erasure satisfies B_v>4d_v, and compute expected odd-face credit divided by original physical influence. All physical coordinates are independent uniform bits. An outer gate sees the actual independent child output means; a fair physical restriction does not change the measure of untouched inputs. Entropy is in bits. q_v=I(f_v0 f_v1)/2; node weights are physical reach probabilities. This report proves a fixed-K=4 order obstruction and its repair on an explicit family, not full FEI.

# sources actually read, revisions and theorem locators

EXECUTION_PROTOCOL.json revision 2026-10-11-execution-v2; BOARD.md snapshot 2026-10-14 02:43 UTC; B05 STREAM_NOTES.md v2 (2026-10-11 23:4xZ), especially the A024 target and SOME-tree bridge; B05 lead REPORT.md 20261011T225000Z, Lemmas 1-2 and Theorem 4. Own stage-1 CLAIMS.json/LEARNED.md and source implementation; own unfinished stage-2 DERIVATION.md and runtime-stop receipt. Current source bytes and SHA256 are in out/SOURCE_RECEIPTS.json. Initial campaign/paper intake remains documented by the stage-1 source receipts; no new theorem is imported from unread paper revisions.

Board overlap checked: A016 distinguishes raw derivative boundary and owned complete reserves; A025 reports all-s unfiltered overcharge with zero bad credit on its overlap family; A023 and A057 now retain one marked terminal/controller reserve. The present witness is an actual single-use mixed odd-face charge at bad nodes inside a nonfactorable two-child gate. It therefore does not rename tensor-spectator raw-boundary overcharge or contradict their paid scopes. No source acceptance is inferred from a board receipt.

# complete derivation or exact first unsupported line

DERIVATION.md gives the complete proof. For F=A+B h with W=B^2 and t=E W, q_x(F)=t q_x(h)+(Inf_x(h)/2)I(1-2W). The event's sign influence is essential; using the Fourier energy of the 0/1 W loses a factor four. For arbitrary disjoint substitution, Q(F)=sum_i a_i Q(f_i)+(1/2)sum_{i<j}gamma_ij I(f_i)I(f_j), with gamma_ij the biased probability that the corresponding gate face is odd. Counting same-block and mixed-block faces proves the formula, including deterministic child limits.

The five-bit selector c uses a four-bit bent sign and its one-point flip. Its mean is 3/16, influence 37/16, selector influence 1/16 and selector credit 1/4. Integer inequalities certify both B_s(c)>1/4 and B_s(c)-Lbin(3/16,1/16)>1/4. The latter preserves badness under any nonignored disjoint outer gate. The exact negative empty-fiber credit is retained, and the erasure formula used from stage 1 is reconstructed here.

Let G_L be the product of L copies, P_N a fresh parity, F_LN=1-(1+P_N)(1-G_L)/2. Its influence is [37L/16+(1-(3/16)^L)N]/2. In the complete selectors-first order every selector is bad, its mean contrast beta=-M/3 produces a genuine log(1/M), and its credit is (4+N)/32. Thus the bad bill is at least L(4+N)/32. Setting N=L^2 gives bill/I>=L/53, unbounded. Nevertheless the total signed mean residual is at most L(2L+4)16^(-(L+1)). The growing cost is the mixed-face term, not this tiny mean-log bank.

In the complete parity-first order the first N-1 queries have zero erasure, the last is K4-good, and the remaining product selectors contribute exactly L/8 expected bad credit. Data nodes are good. Hence bill/I<=4/37, tending to zero for N=L^2. Both trees have constant leaves and exactly zero terminal entropy. Also H(F_LN)<=5L+1 and I>=13N/32; H/I tends to zero in the obstruction regime. This is no FEI counterexample.

First unsupported universal line: for every Boolean f, a history-measurable tree can assign only O(I(f)) odd-face credit to its bad nodes, with inherited controller/core costs retained. Nothing here establishes that line. The refutation concerns EVERY tree at fixed K=4 only; it does not refute a different threshold K or the lead's SOME-tree statement.

# executed validation with domain, arithmetic, commands and outputs

Frozen specs preceded execution. Commands from the A024 workspace: `python -X utf8 runs/20261014T025222Z-fleet05-A024-biased-child-stability/code/check_stage2.py --pilot`, then the same command without `--pilot`, then `python -X utf8 runs/20261014T025222Z-fleet05-A024-biased-child-stability/code/replay.py`.

Pilot PASS: 16 roots, 112 splits, two complete trees; 363 recorded exact equality checks and 138 logarithm-sign calls; 0.172 seconds. Full PASS: all 16 two-input gates times all 16 two-bit companion children, 256 seven-bit roots, 1,792 physical splits, 184 bad nonignored root selectors; six (L,N) pairs (1,1),(1,2),(1,4),(2,1),(2,2),(2,4), both complete orders, maximum truth-table dimension 14. There were 5,673 recorded exact equality checks, 1,990 sign calls, and 205 memoized tree states; runtime 6.518 seconds. Positivity assertions and integer comparisons additionally pass. No symmetry deletion or automatic n increase.

Integer Walsh spectra and Fraction influence/face ledgers are exact. Entropy differences are prime-log forms; rational atanh sums with proved geometric-tail remainder bound certify 45 distinct nonzero signs (24 terms, 48 if needed). Replay uses a direct character-sum transform, independently coded rational log intervals, both seed integer inequalities and all 12 saved ledger formula cross-checks; PASS in 0.0375 seconds. This implementation replay is not independent agent acceptance, nor a second full tree traversal. Thirty-two symbolic rational rows are illustrations only; the infinite family is settled by the analytic proof. Memory estimates 150 MB main/30 MB replay are below the memok threshold; no observed peak-memory measurement is claimed.

The unfinished 20261012 uncached full job hit its 180-second watchdog, without a failed mathematical assertion. Its receipt is retained in out/PRIOR_RUNTIME_STOP.json and the original run remains untouched. Bounded caches completed the same frozen finite domain here with a 300-second cap. Earlier incomplete artifacts are not relabeled as a completed stage.

# proof dependencies and changed downstream conclusions

Used A024-BIASED-CHILD-TRANSPORT@1 only for its erasure clause, reconstructed directly; used B05-ODDFACE-TELESCOPE@1 with direct face counting. Local proofs are complete; external acceptance remains pending. The lead's localized FEI reduction is motivation, not a premise needed for the obstruction. Corrected FEI+ remains sum_nonempty P log2(product input variances/P), without output-variance numerator; uniform H=Eplus+e(mean^2).

Downstream: mean-log affordability cannot justify selector-first restriction. Inner KL rebates do not buy mixed odd faces. The selector is robustly bad even after genuine biased disjoint substitution, but order can place every mixed face at a good parity query. A025's zero-bad overlap result and A057's owned signed release remain compatible. This is completion of the productive unfinished packet under the dispatch rule, not opening an unrelated broad candidate while reviews are pending.

# one next mathematical action and independent reviewer

Replace the parity controller by arbitrary Boolean W and derive the exact controller-first transfer of mixed faces, retaining W's own erasure and both actual terminal child functions. Determine the first controller node where this transfer lacks an influence-owned price. This generalizes the demonstrated repair toward a history-dependent policy. Independent reviewers: A087/A094 for the exact seed sign, deterministic endpoints and all-parameter two-order proof; B05 consumes the distinction between cheap mean bank and mixed-face ownership.

# actual persistence receipts or precise save blocker

The four protocol files, proof, frozen specifications, scripts, exact ledgers/certificates and replay outputs are saved in this run. out/PERSISTENCE_RECEIPTS.json records SHA256 and bytes for every other run file after writing. STATUS.md, WORKLOG.md and LEARNED.md are updated locally. All files are below 20 MB; no local save blocker. Supervisor copies, mirrors, independent acceptance and downstream use are pending and not claimed.

## Universal bridge

This stage moves B05-ODDFACE-LOCALIZED-BRIDGE and C019 stopping-tree payment by closing the lead's biased-child split classification and proving exact mixed-face transport: log(1/mean) nodes really are bad, their mean bank is exponentially small, and the same Boolean family separates a divergent selectors-first bill/I>=L/53 from a parity-first bill/I<=4/37. The universal gap is still a policy assigning mixed faces to paid good queries while retaining arbitrary controller and terminal-core deficits; no all-dimensional FEI bound follows yet. The next controller-first transfer is the shortest route because it isolates precisely the order-dependent term that defeats the local credit rule, rather than adding another isolated function-class entropy estimate.
