# B06 stream notes (Claude lead) - v2 2026-10-11 23:26Z

Run 20261011T223800Z-claude-B06-block-tree-reductions: CLAIMS/PROGRESS/PACKET_DELTA saved; REPORT.md
refused by the subagent harness (text went to coordinator claude-2d8060eb). Claim ids B06-LEAD-*.

## Established (proved locally, review A087/A094)
R1 For any law on subsets and block A: H(S_A|S_Ac) >= sum_{i in A} B_i. A block rule at rate K
gives a singleton at the SAME node at rate K+2/ln2. Blocks only skip intermediate nodes.
R2 For any restriction tree: sum w_v Delta H = H - E H(leaf); sum w_v Inf = I - E I(leaf)
= E_x[# queried coords pivotal on x's path]; KI-H = E(KI-H)(leaf) + K Pi_I - Pi_H. Every ledger
(mismatch, KL, child slack) is a function of the LEAF PARTITION. Complete trees: cumulative
erasure >= H-(2/ln2)I. Criterion for any B06 theorem: leaves in a certified class, Pi_H <= K Pi_I.
R3 Restriction-closed class: good coordinate at K <=> FEI on the class (up to 2/ln2). Affine
Fourier dim <= d has H <= d, I >= 4^(1-d), so A026's class has H <= 256 I before selection.
R4 kappa_n = max_f min_i B_i/Inf_i: 0, 2, then kappa_3 = kappa_4 = (5/2)h2(1/10)+3/2 = 2.6725
EXACT (3-bit point defect; dummy copy at n=4; all other n=4 classes < 267/100). Proxy A_i maxima
0,2,3,7/2. Any universal good-coordinate K is >= 2.6725.

## Codex status (23:00Z)
A026 v1 claims: correct, accepted by A028, reproduced by lead; low leverage. A027 v1: identity
(*) re-derived and reproduced (828 cores, both mean signs), bound B_W <= p(2dm+2) holds; the
I(u) >= eta m hypothesis already makes the core FEI. A028: reviews accepted; own control-first
point-control payment kappa < 8 awaits review as a leaf-partition statement. A029: depth-two gain
over the best single coordinate is in [0,2] for n <= 4 (AND2, 4-bit bent attain 2). A030: run
started 22:57Z.

## Next target per agent
A026: drop the threshold proxy asymptotics (true B_i/Inf_i at the witness is 1.815). Compute exact
B, H, I on transitive families (tribes, recursive maj3, cyclic thresholds); report whether B/H
stays bounded below on the hardest H/I families.
A027: prove the activation transport when a PROPER SUBSET of a low-density core is revealed
before the controls; state the result as Pi_H <= K Pi_I for that leaf partition, terminals
point defects or C001-regular. (A027 owns this; A028 does not duplicate it.)
A028: replace point controls by an arbitrary control indicator c(y) (reused or low-energy
selectors): F = 1 + c(y)(u-1). Prove Pi_H <= K Pi_I for control-first trees in terms of I(c),
H(c) and the core, or give the family where it fails.
A029: test "nonlocal gain <= 2" (best single-coordinate ratio minus best tree ratio) beyond n=4
on structured families (bent 2k: gain exactly 2; tribes; point-defect tensors); prove it or
break it. If true, trees add at most +2 to singleton induction.
A030: measure ratio amplification under restriction, sup H/I(f_rho) over H/I(f), for plateau
constructions; prove an iterated family or a bound.

## Do not repeat
Re-verifying A026/A027 v1 (done twice); all-coordinate local helpers (B05); K=4 or any amplitude
proxy search; re-deriving block identity, influence telescope or child-deficit identity; calling
a restriction-closed selection result "beyond FEI".
