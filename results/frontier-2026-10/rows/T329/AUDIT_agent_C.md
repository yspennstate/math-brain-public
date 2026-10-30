# T329 retrieval construction (DOSSIER.md, 19 Oct 05:33), audit 1 (agent C, 20 Oct 2026 02:23)

Object: the theorem W <= 6n/k + O(k log n) with O(log n)-bit weights, its proof (key, group word, shared hash, GF(2) parity
readout), the counting lower bound, and hash_memo.py with its table.

Verdict: CONFIRMED. W(n, B) = Theta(n / log n) at B = c log n holds for c at least the construction's constant, which depends on
the separation exponent a (r/delta <= n^a) and on d. Four small corrections, none of which changes the conclusion.

## Checked
- Counting bound. 2^n labellings of one fixed point set need 2^n distinct networks. W weights of B bits plus the architecture
  give at most 2^(W B + O(W log W)), so W (B + O(log W)) >= n. Correct.
- Key. A random integer direction with entries up to n^2 separates every delta-separated pair by a fixed fraction of delta,
  except with probability at most about 1/2 over the n^2/2 pairs. The largest coordinate of x_i - x_j is at least delta/sqrt d,
  and v_l takes 2n^2+1 values. A random shift keeps all n scaled projections 1/(8n) away from the integers, except with
  probability 1/4. N = poly(n), with the degree set by a and the n^2. Correct.
- Group word. 1[u >= b] = relu(u-b+1) - relu(u-b) is exact on integers. The telescoping sum gives Z_j on group j. That costs
  2 x 2 inner parameters plus 2 output weights per group, so 6, and the code measures 6.25 with the partial groups.
- Hash. sum c_i u^i mod P with uniform c_i is k-wise independent at distinct u < N < P. For a nonempty T of at most k keys,
  P(XOR of the low m bits = 0) <= ceil(P/2^m)/P <= 2^-m + 1/P (condition on all but one value). The union over 2^k subsets
  and n/k groups, with m = k + ceil(log2(n/k)) + 2, gives at most 1/2. Then the k hash vectors of each group are independent,
  and every labelling of the group is solvable. Correct.
- Arithmetic gadgets (read in hash_memo.py). The big-M product relu(2^b u - M(1 - v_b)) with M = 2^b Umax is exact. The
  reduction mod P extracts the quotient's Lkey+1 bits, and v u + c_i < P(N+1) <= P 2^(Lkey+1) fits. The readout parity is the
  low bit of the sum of the ANDs. Every node is relu(affine). The evaluator applies relu to every node in exact Fraction/int
  arithmetic and computes the key from the input coordinates. Data enter only as weights and biases (b_j, Z_j, c_i).

## Independent checks (this folder)
- repro_run1.txt. New seeds 11 and 12, d = 2 and 5, n = 2048, k = 11: 0 wrong of 300 in all four runs, 6.24-6.27 parameters per
  group. The negative control (n = 512, d = 4, random words) got 256 of 512 wrong.
- indep_rank_run1.txt (indep_rank.py). A different rank method (column-pivot elimination), 4,000 seeds per cell. P(group
  dependent) is 0.42-0.45 at m = k+1, 0.22 at k+2, 0.06 at k+4 and 0.012-0.017 at k+6. The bound is 2^k (2^-m + 1/P) =
  0.50 / 0.25 / 0.063 / 0.016. The union bound is essentially TIGHT: the failure rate is about 2^(k-m), the same as for uniformly
  random vectors. So the log2(n/k) + 2 extra bits in m are needed for one seed to work for every group, and that does not
  change the n/log n count.

## Corrections
1. "The seed worked on the first draw every time": on the new seeds, 2 of 4 runs needed a second draw. That is consistent with
   the failure probability being at most 1/2, which is all the proof uses.
2. Layer-1 parameter count. As coded, each key-bit step's ramp reads the input and every earlier bit, so the cost is O(Lkey^2)
   = O(log^2 n). The statement's O(k log n) holds for k >= log n, which is the case used. For a small k, carry the nonnegative
   residual through one relu per step (the mat() trick the code uses after layer 1), which makes it O(log n).
3. First-layer precision. The code keeps exact rationals up to about 2^61 at n = 2048, which is "roundable" but not rounded.
   The rounding goes through: rounding each weight to q = 1/(16 n d R), with R the input radius, moves t by less than 1/(16n),
   inside the 1/(8n) margin. That costs log N + log(16 n d R / delta) = O(log n) bits.
4. The constant c in B = c log n (about 4.5 in the table) belongs to this data: a 2^-12 grid, so r/delta = 4096 sqrt d, and
   direction entries up to n^2. In general c = c(a, d).

## Not covered
Literature after 2022 (a retrieval or hashing construction for bounded-bit memorization may exist; I did not search), the
depth question (O(log^2 n) here), and the exact constant. A second independent audit is needed before the memory moves to
verified.
