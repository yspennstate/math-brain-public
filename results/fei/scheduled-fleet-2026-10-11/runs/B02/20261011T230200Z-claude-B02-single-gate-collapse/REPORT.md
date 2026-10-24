# B02 lead run: the single-gate collapse of the posterior forest bound, and why tribes kills it

Run 20261011T230200Z-claude-B02-single-gate-collapse, stream B02 (joint Fourier-set coding), primary packet A006.

## Exact target, quantifiers, units
Logs are base 2 unless written ln. f: {-1,1}^n -> {-1,1} nonconstant, P_f(A) = fhat(A)^2, v = Var f = 1 - P_f(empty),
H = -sum P_f log P_f, I = sum |A| P_f(A) = sum_j Inf_j. gamma = 6/5, K_ref = 3 + 2 log 3 + log(6e) = 10.197.
Target: decide what thm:posteriorforest gives with ONE gate, and whether any single-gate table can reach H <= K I with an
absolute K. This is a sub-question of the C020 whole-set witness cost route, not FEI itself.

## Sources actually read
- mop_fei100/reports/fei-2026-10-11/source_material/reductions/paper/forests.tex, lines 1-135: setup (ordered covers,
  ranks r_{l,t}, strict predecessor sets U_i^{l,t}, pi_l, b_l, packing eq:forestpacking, Lambda, Z), the queue, partition
  forests, eq:forestcost (kappa_l = |A cap R_l|), thm:posteriorforest with eq:posteriorforest, eq:minforest and its proof.
- The same report: EXECUTION_PROTOCOL.json, STREAM_NEXT_ACTIONS.json (B02), the plan B02 section, CLAIMS.md (C008,
  C018-C020, C024), SEED_LEMMAS.md; the A006, A007, A008 run reports under agents/A00x/runs/.

## Results
**L1 (single-gate collapse, PROVED).** For every nonconstant f with relevant support R and every cover of R by M >= 1
ordered subsets R_t (ranks r_t, strict predecessors U_j^t),

    H(f) <= h2(v) + (K_ref + log M) I(f)
            + (6/(5 ln 2)) sum_A P_f(A) sum_{j in A} min_{t: j in R_t} ln( r_t(j) / (|A cap U_j^t| + 1) ).

Proof. Apply eq:minforest with N = 1, h_1 = f (a one-term union) and lambda_1 = 1 (the packing holds with equality).
Every spectral A lies in R, so each A has exactly one partition forest: tau = 1, one root, no edges; kappa_1 = s_1 = |A|,
so the subset term gamma s log(kappa/s) is 0, and L_1 = 0. Lambda = log(1 + pi_1) and Z = pi_1/(1 + pi_1), so
v(Lambda + log Z) = v log pi_1, while the root rarity b_1 = log(1/pi_1) is paid on every A != empty, v b_1 in total.
The two cancel exactly, for every pi_1. The label term is sum_A P_f(A) |A| log M = I log M. QED.

**L2 (closed form for one order, PROVED).** For M = 1, sum_{j in A} ln(|A cap U_j| + 1) = ln |A|! and
sum_{A containing j} P_f(A) = Inf_j(f). So the rank term equals sum_j Inf_j ln r(j) - E_{P_f} ln |A|!, and by the
rearrangement inequality it is minimized by ordering the coordinates by decreasing influence. Hence for every nonconstant f

    H(f) <= h2(v) + K_ref I(f) + (6/(5 ln 2)) [ sum_{i=1}^n Inf_(i) ln i - E_{P_f} ln |A|! ],
    where Inf_(1) >= Inf_(2) >= ... are the sorted influences.

The one-gate, one-order forest bound gives FEI exactly when the influence-rank sum exceeds E ln |A|! by at most O(I).
Heuristically (not checked in this run) it holds for spectrally dense transitive functions such as Majority, which are already FEI.

**O1 (tribes obstruction to every single-gate table, PROVED).** Tribes T_{m,w} is the OR of m disjoint ANDs of width w;
q = 1 - 2^{-w}. Exact spectrum (true = -1): P(A) = 4 q^{2(m-k)} 4^{-wk} for A touching k >= 1 blocks and
P(empty) = (2q^m - 1)^2. Then Inf_j = 2^{1-w} q^{m-1}, I = 2mw q^{m-1} 2^{-w}, E k = 4m q^m 2^{-w}, v = 4q^m(1 - q^m),
and H = -P0 log P0 - 2v(1 + m log q) + 2 E k (w + log q), because log P(A) is affine in k.

The single-block sets containing j carry mass J_0 = 2 q^{2m-2} 2^{-w} = q^{m-1} Inf_j. For such A,
|A cap U_j^t| + 1 <= |A| <= w, so the rank term of j is at least min_t ln(r_t(j)/w), and it is never negative. Assign each j
to a minimizing piece. Ranks inside one piece are distinct, so sum_j min_t ln r_t(j) >= sum_t ln(n_t!) >= n ln(n/(eM)) by
convexity, with n = mw. Hence for every M and every ordered M-cover

    RHS(L1) >= h2(v) + K_ref I + (1 - gamma q^{m-1}) I log M + gamma q^{m-1} I log(m/e).

At m = 2^w we have q = 1 - 1/m, so q^{m-1} <= 1/2 and the M term is nonnegative; then RHS/I >= K_ref + gamma q^{m-1} log(m/e), which is
K_ref + 0.44 (w - 1.44) - o(1) and tends to infinity, while H/I tends to 4 (closed form; 4.025 at w = 60).

On the same family the one-gate-per-block forest (gates = the m ANDs, lambda = 1, pi = 2^{-w}, block order) has the closed
form bound = h2(v) + v(Lambda + log Z) + K_ref I + E k (w + (6/(5 ln 2)) phibar(w)), with
phibar(w) = [2^{w-1} ln w! - sum_s C(w,s) ln s!] / (2^w - 1). Its ratio to I is 12.61 at w = 2 and 13.34 at w = 60, with
limit K_ref + 2(1 + gamma/2) = 13.40. The single-gate lower bound passes it at w = 9 and then grows linearly.

Meaning: in any universal table the gate name and root rarity must be paid once per used gate per set; per-coordinate piece
labels under a single gate cannot replace gates. This is a route obstruction for the single-gate sub-route of C020, not an
FEI statement.

**Reviews of the pending stream candidates (partial, independent code).**
- A006: exact FWHT spectrum and I = 1 + (m-1)2^{-m} hold for m = 1..10. Chain (i): max_m 2^{-m}[m^2 + 11m/5 + 4/5] =
  23/10, attained at m = 2 (induction step m^2 + m/5 - 12/5 >= 0 for m >= 2). Chain (ii): m^2 + 9m + 5 <= (15/2) 2^m,
  equality at m = 1 (step m^2 + 7m - 5 >= 0). D_m = (1 + 1/(4m))^m - 1 lies in [1/4, e^{1/4} - 1]. NOT reproduced: the
  star structure of the partition forests, the run counts t! and (m-t)t!, and the assembly R_m <= (43/10) I. A006 as a
  whole stays unreviewed.
- A007: root normalizer 0 <= log D - log a <= a log e holds (D = prod(1 + x_l) - 1 >= a by expanding the product, and
  D <= e^a - 1 <= a e^a); 20,000 random tables agree up to float cancellation of order 1e-7. NOT reproduced: the p^2
  suppression and the petal identity.
- A008: not reviewed in this run.

## Executed validation (commands and outputs in out/)
- python -X utf8 code/check_single_gate.py out/check_single_gate.txt : 10 tribes cases (n <= 12) with exact integer FWHT.
  Spectrum formula, I and v exactly equal; closed-form H equals the direct sum to 1e-6; the identity L2 holds (direct =
  formula) for the natural and a random order. On 59 random f with n <= 7: max |direct - formula| = 1.3e-15, the
  influence-sorted order equals the minimum over all orders (gap 0), and RHS(L1) >= H with 0 violations. Tribes table at
  m = 2^w for w = 2..60.
- python -X utf8 code/review_a006_a007.py out/review_a006_a007.txt code : the A006 and A007 items above.
Floating point is used only for logarithms; spectral identities are exact; L1, L2 and O1 rest on the written proofs.

## Proof dependencies and downstream
L1 depends only on thm:posteriorforest (eq:minforest); L2 on L1; O1 on L1 and the tribes spectrum. If thm:posteriorforest
changes, all three move with it. Downstream: C020 (a universal witness table needs a growing number of gates on tribes) and
the STREAM_NOTES target PI-J (prime-implicant tables; on tribes they are exactly the block gates).

## First unsupported line / open
PI-J stays open: with gates = all prime implicants of f^{-1}(true) and one fixed fractional lambda, is the conditioned
residual of eq:posteriorforest <= K I for all f? First unsupported line: no bound on the label-plus-rank cost
sum_{l used}[L_l + s_l log M_l] when the read of a coordinate (the number of prime implicants containing it) grows with n.
The sunflower already needs a non-uniform lambda (A009).

## Next mathematical action and reviewer
Independent review of L1, L2 and O1 (all short) by A086 or A094. Then PI-J on Majority_n, exactly for small n (A006), and
the one-gate-per-block positive side made general for read-once DNFs (A008).

## Persistence receipts
Files written: this REPORT.md, CLAIMS.json, PROGRESS.json, PACKET_DELTA.json, code/ (check_single_gate.py,
check_single_gate_lib.py, review_a006_a007.py), out/ (check_single_gate.txt, review_a006_a007.txt) and .final; stream files
claude/B02/STREAM_NOTES.md and LEARNED.md. No git, brain or mesh writes (this agent is not permitted them).

## Universal bridge
The posterior forest bound has a hidden degree of freedom: the table (gates, covers, lambda) is free. With one gate the root
normalization cancels exactly, leaving a one-line inequality whose only cost is how far each spectral set sits from the
front of a fixed order. That inequality is FEI precisely for functions whose spectrum is dense in its support, and tribes
shows it fails by a factor of log m whenever the spectrum lives on many small, separated pieces. This is the old dichotomy
between coding a set as a subset of one list and coding it as a few named blocks. The forest bound pays for block names
(gate labels and root rarity), and the evidence here says that cost cannot be avoided. Any proof of C020, and any table rule
such as prime implicants, has to choose gates that match the blocks of the spectrum, which moves the open problem to how
many blocks a coordinate can belong to and what that read costs.
