# B05 (Claude lead): odd-face transport for the rare logarithm

Run 20261011T225000Z-claude-B05-odd-face-transport, protocol 2026-10-11-execution-v2, stream B05, primary packet A023
(amortized rarity budget), gap G-R-SELECT. Full FEI remains OPEN.

## 1. Target, quantifiers, units

f : {0,1}^n -> {-1,1}, n >= 1. Fourier weights p_S = \hat f(S)^2, H(f) = -sum p_S log2 p_S (bits), I(f) = sum |S| p_S.
For a coordinate i: g = f|x_i=0, h = f|x_i=1 on {0,1}^(n-1), a = \hat g, b = \hat h,
q_T = (a_T^2 + b_T^2)/2, e_T = (a_T - b_T)^2/4, theta_T = e_T/q_T, d = Inf_i(f) = sum e_T = Pr[g != h],
B_i(f) = sum_T q_T h2(theta_T) = H(S_i | S_-i), and Delta_i H = H(f) - (H(g)+H(h))/2 = B_i + JS(a^2, b^2) (C005).
For a Boolean u on m bits, I(u) = 2 |dD|/2^m where D = {u = -1} and dD is its edge boundary.
Odd faces: N_odd(f) is the number of 2-dimensional faces of {0,1}^n whose four values multiply to -1 (equivalently,
f restricted to the face is not affine over F_2). Q(f) = 2^(1-n) N_odd(f), and Q = 0 for n <= 1.
A restriction tree splits one live coordinate per internal node v; w_v = 2^(-depth(v)); g_v, h_v, d_v, B_v are the
node's children, influence and conditional entropy. c_JS = 2/ln 2 (C005); the self-contained alternative c_JS = 4
follows from Topsoe's JS_nats <= (ln 2/2) Delta with Delta = sum (a^2-b^2)^2/(a^2+b^2) <= 8 min(d, 1-d).

## 2. Results (claims B05-ODDFACE-*, version 1)

### Lemma 1 (isoperimetric payment of the rare logarithm; PROVED)
For every f and i,
  B_i(f) <= h2(d) <= (1/2) I(g h) + log2(e) d,   and   d log2(1/d) <= (1/2) I(g h) <= (1/2)(I(g) + I(h)).
Proof. The weights q_T sum to 1 and sum q_T theta_T = d, so concavity of h2 gives B_i <= h2(d).
(1-d) ln(1/(1-d)) <= d gives h2(d) <= d log2(1/d) + d log2 e. Let D = {g != h} = {gh = -1}, |D| = s = d 2^(n-1).
The edge-isoperimetric inequality of the cube (Harper 1964, Bernstein 1967, Hart 1976: any s vertices span at most
(s/2) log2 s edges) gives |dD| >= s log2(2^(n-1)/s), that is (1/2) I(gh) = |dD|/2^(n-1) >= d log2(1/d). An edge cut
by gh is cut by g or by h. Equality needs D a subcube and theta_T constant on the support of q; the bent one-point flip
at a selector meets both up to the log2 e term.

### Lemma 2 (exact odd-face telescope; PROVED)
For every f and i, Q(f) = (1/2) I(g h) + (Q(g) + Q(h))/2.
Proof. A 2-face of {0,1}^n lies in x_i = 0 (a face of g), in x_i = 1 (a face of h), or has directions {i, j}; a face
of the last kind sits over an edge (y, y+e_j) of {0,1}^(n-1), its corner product is u(y)u(y+e_j) with u = gh, so it is
odd exactly when u cuts that edge. Hence N_odd(f) = |dD| + N_odd(g) + N_odd(h); multiply by 2^(1-n).
Consequences. In every adaptive tree, sum over internal v of w_v (1/2) I(g_v h_v) = Q(f) - sum over leaves of w Q(leaf)
<= Q(f), and each odd face is charged at exactly one node (the first split along one of its two directions). Also
Q(f) = (1/4) sum_i I(f|x_i=0 f|x_i=1) = (1/2) sum_{i<j} Pr_x[the {i,j}-face through x is non-affine].
The credit telescopes by the same law as influence (I(f) = Inf_i + (I(g)+I(h))/2) but never reuses influence.

### Theorem 3 (unconditional inequality; PROVED given C005, self-contained with c_JS = 4)
For every Boolean f, H(f) <= (log2 e + c_JS) I(f) + Q(f), that is H <= (3/ln 2) I + Q ~ 4.328 I + Q with C005.
Proof: a complete tree has H = sum w (B + JS) and I = sum w d; apply Lemma 1 at every node, JS <= c_JS d, Lemma 2.
This is not FEI. Q/I = (r-1)/2 on AND_r, Q/I grows with the width on tribes, and on the B05 family Q/I = 4.84 (k=4)
and 7.09 (k=6). The credit has to be spent only where it is needed.

### Theorem 4 (localized reduction; PROVED)
For every f, every (adaptive) restriction tree T whose leaves are constant functions, and every K >= log2 e,
  H(f) <= (K + c_JS) I(f) + sum over v in T with B_v > K d_v of w_v (1/2) I(g_v h_v).
Proof: B_v <= K d_v at good nodes; at bad nodes B_v <= (1/2) I(g_v h_v) + log2(e) d_v <= (1/2) I(g_v h_v) + K d_v.
Bad nodes are rare splits: B_v <= h2(d_v) and h2(d)/d decreases, so B_v > K d_v forces d_v < delta_K where
h2(delta_K) = K delta_K. Hence FEI holds with C = K + c_JS + K' on any family whose members admit trees with bad-node
odd-face credit at most K' I(f).
First unproved line (the localized odd-face bridge, OPEN): for some absolute K, K' and every Boolean f there is a tree
with sum over {v : B_v > K d_v} of w_v (1/2) I(g_v h_v) <= K' I(f).
The strongest case against the value of Theorem 4: O-ACTIVATION-EQUIV (C013) says rarity alone is FEI-strength, so the
localized bridge may be no easier than FEI and the theorem may only relabel the problem. The check that would settle the
worry in one direction is the tower of Section 6: if the bad-node credit there outgrows I, this currency is retired.

### Proposition 5 (the B05 no-go family is paid; root bound PROVED, ledgers certified by exact counts)
Family (archived B05): bent b on k bits (k >= 4 even), b' = b with the point x = 0 flipped, controls z in {0,1}^r active
iff z = 0, selector y; F = 1 off the activation, F = b on y = 0, F = b' on y = 1. Exactly
  I(F) = 2^(-k-r) + 2^(-r)(k/2 + k 2^(-k)) + r 2^(-r)(1 - 2^(-k/2) + 2^(-k))
(Inf_y; data = average of I(b) = k/2 and I(b') = k/2 + k 2^(1-k); control = r 2^(1-r) Pr[F' = -1]); it matches the exact
spectrum at (k,r) = (4,8) and (6,12) to the last bit. In the selector-first tree the root disagreement set is one point
of the (k+r)-cube, so its credit is (k+r) 2^(-k-r) <= 2^(1-k) I(F), because I(F) >= 2^(-r)(k + r)/2 for k >= 2.
Exact ledgers, bad-node credit over I(F) at K = 4 (orders selector-first, control-first, data-first,
control-data-selector): k=4, r=8: 0.0851, 0.0284, 0, 0; k=6, r=12: 0.0249, 0.0113, 0.0193, 0.0057, with at most two bad
nodes per tree. The refutation of every fixed price L <= K d + A V_post + B M_inf leaves the odd-face transport alone: at
the selector the credit is about 3k d (it sees the k + r live coordinates), the size of the logarithm itself, and it is a
vanishing fraction of I(F) because the activation's control influence dominates.

## 3. Independent checks of the Codex runs

### A021 v1, section 2, remainder sign: REFUTED at order q^3 (the asymptotic conclusions survive)
A021 writes b(q) = -2(1-q)^2 log2(1-q) = 2cq - 3cq^2 + R(q) with R(q) = -4c sum_{j>=3} q^j/[j(j-1)(j-2)] and
-2cq^3/[3(1-q)] <= R <= 0. The coefficient of q^j (j >= 3) in (1 - 2q + q^2) sum q^j/j is
1/j - 2/(j-1) + 1/(j-2) = 2/[j(j-1)(j-2)] > 0, so R(q) = +4c sum_{j>=3} q^j/[j(j-1)(j-2)] and 0 <= R(q) <= 2cq^3/[3(1-q)].
A 50-digit check gives R(1/2) = +0.139326 = 4cS(1/2), R(1/16) = +2.3858e-4, R(2^-8) = +5.738e-8
(out/a021_remainder_sign.txt). The section-4 quantity G_s = R(u) - R(2u)/2 is therefore <= 0 (G_s(1/4) = -0.0536),
not >= 0. The activation formulas are right: I re-derived H(F) = q t_h + (4q - 2q^2) k - 2(1-q)^2 log2(1-q) and
I(F) = q(t_i + k) for a balanced core with k controls from \hat F(empty,empty) = 1-q, \hat F(empty,U) = -q,
\hat F(T,U) = q c_T. Every exact necessary condition (C(ti+k) >= th + 4k + 2c - q(2k+3c) + R/q) stays valid; any
sufficiency inequality that dropped R using R <= 0, and the J_tree remainder that used G_s >= 0, must be re-signed.
A021's finite checks did not test this sign, as its report says.

### A023 v1, fair selector between bent and its one-point flip: CONFIRMED
H(F'_k) <= k + 1 is the support bound on 2^(k+1) sets; exactly I(F'_k) = k/2 + (k+1) 2^(-k) and
Q(F'_k) = k/4 + k(k-1) 2^(-k-1) (asserted against exact counts for k = 4..10), so H/I < 3 for k >= 4.
A022 v1 was not checked in this run.

## 4. Executed validation

Commands, run from this directory (Python 3 with numpy and mpmath; no GPU, no window; each under 4 minutes and 150 MB):
- `python -X utf8 code/iso_check.py out/iso_check.json` -> out/iso_check.log, exit 0.
  Part A covers all 65,536 + 256 + 16 + 4 Boolean functions on n <= 4 and all 262,144 + 768 + 32 + 4 splits. The integer
  isoperimetric test s^s 2^|dD| >= 2^((n-1)s) never fails; the telescope N_odd(f) = |dD| + N_odd(g) + N_odd(h) never
  fails; Delta_i H = B + JS holds to 4.4e-16; the minimum over d > 0 of (1/2)I(gh) + log2(e) d - B is 0.1149 (n=4);
  B = 0 whenever d = 0; JS <= (2/ln 2) min(d,1-d) and JS <= 4 min(d,1-d) hold (minimum margin 0, at trivial splits);
  H <= (3/ln 2) I + Q holds (minimum margin 0, at constants); max B/d = 3.523 and max Q/I = 1.5 at n = 4.
  Part B asserts the closed forms for AND_r (r = 2..12: Q = r(r-1)2^-r, I = r 2^(1-r)), bent_k (Q = k/4), the fair
  selector F'_k (k = 4..10) and the activated bent G_{k,r} (k = 4, r = 2..8; k = 6, r = 2..5;
  Q = 2^-r [k/2 + r(r-1)(1 - 2^(-k/2)) + rk]/2).
  Part C: 24 random-order trees on 12 functions of 8 bits give sum of node cuts = N_odd exactly, sum w (B+JS) = H and
  sum w d = I to 1e-9, total credit = Q exactly; the B05 family at k = 4 under four orders; exhaustive n = 3, 4 over all
  orders: at K = 4 no function has a bad node in any order, and at K = 3 every function has an order without one.
- `python -X utf8 code/b05_ledger_k6.py out/b05_ledger_k6.json` -> out/b05_ledger_k6.log, exit 0 (n = 19).
- `python -X utf8 code/a021_remainder_sign.py` -> out/a021_remainder_sign.txt.
Walsh coefficients, edge counts and face counts are integers, and the isoperimetric test uses Python integers;
entropies are float64 with every margin printed (float error below 1e-12 at these sizes). The finite runs certify only
the finite statements they cover; Lemmas 1-2 and Theorems 3-4 rest on the proofs above.

## 5. Dependencies and downstream changes

Lemma 1 uses concavity of h2 and the cube edge-isoperimetric inequality. Lemma 2 uses nothing. Theorem 3 uses C005
(Delta_i H = B_i + JS and its JS constant), or Topsoe for c_JS = 4. Theorem 4 uses Lemmas 1-2.
Changed conclusions: (i) the retired universal fixed-price claim now has a universal replacement with an explicit
single-use credit, B_i <= (1/2) I(g h) + log2(e) Inf_i at every node; (ii) FEI reduces to the localized odd-face bridge
of Theorem 4, which the B05 no-go family satisfies with ratio at most 0.025 at k = 6; (iii) A021's remainder signs
(R and G_s) are reversed, so consumers of its J_tree remainder (A023, A087, A094) should not use R <= 0.

## 6. Next mathematical action and reviewer

Build the nested rare-flip tower: bent cores in which a one-point flip is itself activated inside a lower-level flip, so
that every tree meets bad splits at several depths, and compute the bad-node odd-face credit exactly against I at depth 2
and 3 under the frozen four-order spec. Either the credit stays O(I), which is evidence for the localized bridge and
points at its proof (a bad node's faces are bought by the control influence that made it rare), or the tower is the
obstruction that retires this currency. Independent reviewer requested: B19 (it reviewed the B05 no-go) for Lemmas 1-2
and Theorem 4; A087 and A094 for the A021 sign correction.

## 7. Persistence receipts

Saved on disk in this run directory (sha256 below). Git, brain and mesh persistence belong to the coordinator by task rule; there is no save blocker on disk.

- CLAIMS.json  d9e99ac654dd29fb2f9ca8f333d7f51a923e8c263af1f1771f5a7b6d1c794f19
- PROGRESS.json  4fe1b3a1a082e5ab58fb34ce9e5ec407b1351ea4d2ac5c070c2b66be7e4599e2
- PACKET_DELTA.json  7480f302d22a55a4dabb0b8522704e9ed5583a76753289f7b066ce5ced32c7d5
- code/iso_check.py  5374ad7d23676d244f0836d5be06c00baa495713e55527d21a88aa3f7abb51df
- code/b05_ledger_k6.py  4c4603bbfb7cfdda051b8b5f5145f8de4b4a3f36bc98088d8ffff94c15add6a0
- code/a021_remainder_sign.py  fbff59c6e8e26c51c1222e4983a9099692b56bce4f5bed22a858f35b2688bb89
- code/assemble.py  8d425808de3a7eb4157631532ef688c81a831a6cfba3717f053655251b3fd594
- out/iso_check.json  45ce65c0b31e44ae743986b16f40f2c5bb9a89f9000d54b9f1016ed8dc63db7b
- out/iso_check.log  c836ef6a44edc2bf30bff3523cdbc6ea882dc9d36de6c96d04bfb4ff8c980100
- out/b05_ledger_k6.json  7027a7649996a40810ce04b3bf49ae1b5feced6ec5a47b01560ca457f6827cb8
- out/b05_ledger_k6.log  21cb158d8d748d5b95852d70482b692066e1e4f0714a89287b16957009bd10c6
- out/a021_remainder_sign.txt  67304f7be3671fdb962cd832f7ee4a43ab94974d74c6c1d7ef43476936149327

## Universal bridge

The bridge that moved is C018/C019, the universal B bound and the stopping tree with a linearly paid charge. Before this
run the only universal local price for the rare logarithm, L <= K d + A V_post + B M_inf, was refuted (B05 no-go) and
nothing replaced it. Now every split obeys B_i <= (1/2) I(f|x_i=0 f|x_i=1) + log2(e) Inf_i, and the credit on the
right telescopes exactly: summed over any tree it is the normalized number Q(f) of odd 2-faces, each face paid once,
so it reuses no influence. That gives H <= (3/ln 2) I + Q unconditionally and H <= (K + 2/ln 2) I + (odd-face credit at
bad nodes) for any tree, and on the family that killed the fixed price the bad-node credit is at most 2.5 percent of I
at k = 6 (0.6 percent in the best order). What remains is one combinatorial statement: some tree spends only O(I) odd
faces at its bad (rare, spread) splits. Q itself is not O(I) on AND, tribes or the B05 family, so the credit must stay
local. It is the shortest route left to full FEI because the reduction is already proved, it contains no entropy at all
(only face counts at rare splits), and the one family that could break it, the nested rare-flip tower, is small enough
to compute exactly at depth 2 and 3.
