# B20: the erasure constant K_E is low-influence complete (activation transfer with an explicit bias-erasure price)

## exact target, quantifiers, hypotheses and units

Uniform measure on {-1,1}^n, f Boolean (values +-1), Fourier law P_f(S) = fhat(S)^2. Influence I(f) = sum_i Pr[f(x) != f(x^i)]. Entropies in bits. The erasure functional of C018 is

    B(f) = sum_i H(S_i | S_{-i}) = sum_i sum_{S not containing i} phi(fhat(S)^2, fhat(S+i)^2),
    phi(a,b) = a log2((a+b)/a) + b log2((a+b)/b)   (phi(a,0) = phi(0,b) = 0; phi is 1-homogeneous),

K_E = sup B/I over all Boolean f with I > 0, and C018 gives K_E <= C_FEI <= K_E + 2/ln 2. For s: N -> [0,inf) with s(N) = o(N), let

    K_E(s) = sup { B(F)/I(F) : F Boolean on N coordinates, 0 < I(F) <= 2^(-s(N)) }.

Target (Theorem 4 below): for every Boolean f with I(f) > 0, B(f) <= (K_E(s) + 2/(sqrt(e) ln 2)) I(f). So K_E <= K_E(s) + 1.7501, and with C018, C_FEI <= K_E(s) + 2/(sqrt(e) ln 2) + 2/ln 2 <= K_E(s) + 4.636. This transfers the low-influence completeness of FEI (Shalev, arXiv:1806.03646v2, Theorem 3 and Section 3.2; the activation construction is attributed there to Wan, Wright and Wu, as the campaign note LOW_INFLUENCE_SOURCE_NOTE records) from H to the exact missing term B of C018. Status: author-proved here, independent review pending (A090 primary, A094 alternate). Novelty is not claimed; it is an adaptation of a known reduction to a different functional.

## sources actually read, revisions and theorem locators

EXECUTION_PROTOCOL.json (revision 2026-10-11-execution-v2); mop_fei100 CAMPAIGN.md, CLAIMS.md (C000-C035), COUNTEREXAMPLES.md (X001-X013), SEED_LEMMAS.md; research_pushes/2026-10-11-full-fei-100-agents/sources/ERASURE_REDUCTION.md sections 1-5 (definition of B, inequality (5) K_E <= C_FEI <= K_E + 2/ln 2, the L-form L <= B <= L + I/ln 2); sources/ROUTE_MAP_CURATED.md lines 15, 47, 97 and 226 (sparse activation; the Shalev and Wan-Wright-Wu attribution); sources/LOG_ALLOCATION_CURATED.md section 4 (sparse activation defeats mismatch-weighted refunds). Codex runs read in full or in the parts used: A096 20261011T215017Z-account05-A096-live-gap-ledger (REPORT and claims) and A097 20261011T221240Z-account05-A097-cross-route-transfer (REPORT). BOARD.md as of 22:16Z. The Shalev paper itself was not re-read; only the campaign attribution of it is cited, and no step below depends on it.

## complete derivation or exact first unsupported line

**1. Tensor additivity.** For f on X and h on a disjoint Y, the product f(x)h(y) has Fourier coefficients fhat(S)hhat(T), so its law is P_f x P_h. For i in X, H(S_i | S_{-i}, T) = H(S_i | S_{-i}) by independence; hence B(f (x) h) = B(f) + B(h). Flipping x_i changes f(x)h(y) iff it changes f(x), so I(f (x) h) = I(f) + I(h). For h_m = f^(x)m (m copies on disjoint blocks), B(h_m) = m B(f) and I(h_m) = m I(f).

**2. Exact activation formula.** For Boolean h on n coordinates and k >= 1 let F(x,y) = h(x) if y = y* (one fixed point of {-1,1}^k), else 1. Put delta = 2^-k, c = 1 - hhat(empty) in [0,2], g = h - 1. Then F = 1 + 1_{y*}(y) g(x), and the indicator has |1hat(T)| = delta for every T. Hence

    Fhat(empty,empty) = 1 - delta c;  Fhat(S,empty) = delta hhat(S) (S nonempty);  |Fhat(S,T)| = delta |ghat(S)| (T nonempty),

with ghat(S) = hhat(S) for S nonempty, |ghat(empty)| = c, and sum_S ghat(S)^2 = E g^2 = 2c. Influence: flipping x_i matters only at y = y*, so I_x = delta I(h); flipping y_j matters only between y* and its neighbour, and only where h(x) = -1, so I_y = 2k delta Pr[h = -1] = k delta c. Therefore **I(F) = delta (I(h) + k c)** exactly. Slicing B(F) by T for the x-coordinates and by S for the y-coordinates:
- x-part, T nonempty (2^k - 1 slices, masses delta^2 ghat(S)^2): (delta - delta^2)[B(h) - Sf + Sg];
- x-part, T empty (mass (1 - delta c)^2 at S empty, delta^2 hhat(S)^2 otherwise): delta^2[B(h) - Sf] + sum_i phi((1 - delta c)^2, delta^2 hhat_i^2);
- y-part: for S nonempty the two atoms of every pair (S,T), (S,T+j) have equal mass, one bit each, total delta(1 - hhat_0^2); for S empty the pairs with T_{-j} nonempty give (delta - 2 delta^2) c^2, and the pair (empty,empty), (empty,{j}) gives phi((1 - delta c)^2, delta^2 c^2).

Here Sf = sum_i phi(hhat_0^2, hhat_i^2), Sg = sum_i phi(c^2, hhat_i^2), hhat_0 = hhat(empty), hhat_i = hhat({i}). So, exactly,

    B(F) = (delta - delta^2)[B(h) - Sf + Sg] + delta^2 [B(h) - Sf] + sum_i phi((1 - delta c)^2, delta^2 hhat_i^2)
           + k [ delta (1 - hhat_0^2) + (delta - 2 delta^2) c^2 + phi((1 - delta c)^2, delta^2 c^2) ].        (A)

Dropping nonnegative terms (Sg and the last two groups; B(h) - Sf >= 0 because Sf is a sub-sum of B(h)): **B(F) >= delta [B(h) - Sf]**. The y-part divided by I_y equals 2 - 2 delta c + phi((1 - delta c)^2, delta^2 c^2)/(delta c), which tends to 2 as k grows; for h = -1 this is the point defect, B/I -> 2.

**3. Bias-erasure price.** Sf <= (2/(sqrt(e) ln 2)) I(h), about 1.7501 I(h). Proof: phi(a,b) = b log2((a+b)/b) + a log2(1 + b/a) <= b log2(e/b) when a + b <= 1 (Parseval and log2(1+u) <= u log2 e). Next, |hhat({i})| = |E[(h(x) - h(x^i)) x_i]|/2 <= Inf_i(h), and b -> b log2(e/b) is increasing on (0,1], so phi(hhat_0^2, hhat_i^2) <= Inf_i^2 log2(e/Inf_i^2) <= Inf_i sup_{0<t<=1} t log2(e/t^2) = Inf_i 2/(sqrt(e) ln 2), the maximum being at t = e^(-1/2). Sum over i.

**4. Theorem.** Let s(N) = o(N). For every Boolean f with I(f) > 0, B(f) <= (K_E(s) + 2/(sqrt(e) ln 2)) I(f).

Proof. Replace s by s_bar(N) = max over M <= N of s(M). Then s_bar is nondecreasing, s_bar(N) = o(N), and K_E(s_bar) <= K_E(s) because the admissible class only shrinks; so it suffices to prove the bound with s_bar. Assume K = K_E(s_bar) is finite. Fix f on n coordinates. For m >= 1 put h_m = f^(x)m, k_m = ceil(s_bar(2mn) + log2(3mn)) + 1, and F_m = Act_{k_m}(h_m) on N_m = mn + k_m coordinates. For m large, k_m <= mn, so N_m <= 2mn and, by Section 2,

    0 < I(F_m) = 2^(-k_m) (m I(f) + k_m c_m) <= 2^(-k_m) (mn + 2 k_m) <= 2^(-k_m) 3mn <= 2^(-s_bar(2mn)) <= 2^(-s_bar(N_m)).

Therefore B(F_m) <= K I(F_m). By Sections 1-3,

    delta_m [m B(f) - 1.7501 m I(f)] <= B(F_m) <= K delta_m (m I(f) + 2 k_m).

Divide by m delta_m: B(f) <= (K + 1.7501) I(f) + 2K k_m/m, and k_m/m -> 0 because s_bar(2mn) = o(m). QED.

Corollaries. (i) K_E <= K_E(s) + 1.7501, and C_FEI <= K_E(s) + 4.636 by C018 (5). (ii) Through L <= B <= L + I/ln 2 (ERASURE_REDUCTION section 4), the downward-log-ratio form is low-influence complete as well: sup L/I <= sup over the low-influence class of L/I + 1.7501 + 1/ln 2. (iii) There is no first unsupported line inside this theorem. The open line of C000 is unchanged: finiteness of K_E itself (equivalently L <= K I for every Boolean f) is OPEN. This run shows only that restricting that inequality to tiny total influence, or to activated functions, does not weaken it.

## executed validation with domain, arithmetic, commands and outputs

Command, from the run folder: python -X utf8 code/check_activation.py > out/ACTIVATION_RESULTS.json (7.5 s, under 50 MB). The domain was fixed before running, with no escalation: every Boolean h on n = 1, 2, 3 (4 + 16 + 256 = 276 functions) with k = 1, 2, 3, giving 828 activated functions on up to 6 coordinates; tensor pairs with n1, n2 in {1, 2} (400 pairs); the bias-erasure bound over every Boolean function on n = 1..4 (65,812 functions). Walsh transforms use exact integer and Fraction arithmetic and influences are exact Fractions; entropies are double precision. Output: formula (A) against a direct computation of B(F), maximum error 8.9e-16 over 828 cases; I(F) = delta(I(h) + k c) exactly in all 828 (0 failures); lower bound B(F) >= delta[B(h) - 1.7501 I(h)] with 0 failures (minimum slack 0, at constant h); tensor additivity maximum error 0.0 over 400 pairs; bias-erasure bound with 0 failures and largest observed Sf/I = 1.1725, so 1.7501 is not sharp for n <= 4; point-defect y-ratio 2.0, 2.634, 2.105, 2.0009, 2.00000003 at k = 2, 4, 8, 16, 32. These are evidence for identities proved above, not the proof.

## proof dependencies and changed downstream conclusions

The theorem depends only on the definitions, Parseval, |hhat(i)| <= Inf_i, and, for Corollary (i), C018 (5). What changes downstream: (1) a stream that proposes to bound B (or L, or the A097 erasure-minus-credit term) on low-influence or activated functions is attacking full FEI with a loss of at most 1.7501; small total influence is not a simplification of C000. (2) The B05 sparse activation is the generic hard case for the erasure route, consistent with its reviewed scope; it refutes local refunds, not finiteness of K_E. (3) The root pairs (empty, {i}) of B are paid by influence with constant 1.7501 (Section 3). That level-one fragment of the missing inequality is closed; the pairs (S, S+i) with |S| >= 1 carry the entire remaining debt. (4) Review of A096: both of its claims hold under my re-derivation; the REPORT sentence "J_X = H(X)-H(X|T) <= h2(r)-h2(delta)-M_X" has a sign typo and must read "+M_X"; its final claim (5) is unaffected.

## one next mathematical action and independent reviewer

Next action: carry Section 3 one level up. Bound the sum over |S| = 1 and i not in S of phi(fhat(S)^2, fhat(S+i)^2) by C I(f), using level-two Booleanity (sum_S fhat(S) fhat(S xor U) = 0 for U nonempty) where Section 3 used |fhat(i)| <= Inf_i, or exhibit a family in which this level-one-to-two erasure divided by I diverges. Either outcome locates the level at which the B-debt of C000 first becomes unpayable by local Fourier bounds. Reviewer: A090 (primary), A094 (alternate).

## actual persistence receipts or precise save blocker

Saved in this run folder: REPORT.md, CLAIMS.json, PROGRESS.json, PACKET_DELTA.json, code/check_activation.py, out/ACTIVATION_RESULTS.json, and out/RECEIPTS.json (sizes and SHA256, written after the other files). No git, brain, mail, mesh or checklist action was taken, and nothing was written outside claude/B20.

## Universal bridge

The bridge between H and B now runs in both directions under the same reductions. B is tensor-additive and survives activation up to an explicit correction at the empty set that influence pays, exactly as H does in the Shalev reduction. So every structural simplification already known not to weaken FEI (small total influence, activated seeds, tensor powers) also fails to weaken the erasure inequality L <= K I. What remains of C000 is that inequality on arbitrary Boolean functions, with Booleanity required at the levels |S| >= 1 above the root.