# Referee review of w396 P0003 draft, 2026-10-10

Source correction: the catalog target is Grimmett Question 2.2, uniform fixed-length origin-started honeycomb SAW. The earlier all-length chordal material is a separate related conjecture. I independently checked this against [Grimmett's original question](https://arxiv.org/pdf/2205.07318v1#page=3). The L0–L3 verdicts below hold as finite/conditional statements, but their first version alone does not address the fixed-length ensemble.

Scope: `ATTEMPT.md` finite L0–L3 and the claimed conditional route. Verdicts below are mathematical checks, not a solution of P0003.

## L0: finite path deletion and exploration ratio — KEEP

For a realized unfinished simple prefix `eta=(v_0,...,v_k)`, deleting `v_0,...,v_(k-1)` leaves exactly the allowed completions from its tip. Every completion's full weight factors into the same positive prefix weight times its residual weight; it cancels in the conditional ratio. If the prefix hit A, the conditional avoidance probability is zero. Completed paths get the final indicator. This handles positive inherited edge weights and finite graphs as stated. The geometric edge-deletion variant is exact when intersection with a closed obstacle is defined edgewise. The half-edge subdivision gives two half-edges per visited honeycomb vertex, hence weight `x_c^ell` for boundary-mid-edge paths; it does not itself prove equivalence with the lecture notes' vertex endpoints.

## L1: maximal collar error — KEEP

For `A subset B`, `X=1_(E_A minus E_B)` and `D_k=E[X|F_k]` exactly. Thus `D_k` is nonnegative, starts at `r(A)-r(B)`, and ends at `X`. At the first threshold crossing, stopped expectation remains `D_0`, so `lambda P(max D_k>=lambda) <= r(A)-r(B)`. The graph has at most `|V|-1` path edges, so the stopping time is bounded. No independence is multiplied. Independent sharpness check: in the two equal-weight branch diamond, `r(empty)=1`, `r({c})=1/2`, and after the first branch choice `D_1` is 1 with probability 1/2 and 0 otherwise; equality holds at `lambda=1`.

## L0′: length-preserving continuation — KEEP

For the uniform n-step origin-started law, every realized k-edge prefix has precisely the simple `(n-k)`-edge completions from its tip in the graph deleting its earlier vertices. The conditional ratio therefore uses `C_(n-k)(G_eta minus A;tip)/C_(n-k)(G_eta;tip)`, with an exact remaining length, and the root ratio is `C_n(G minus A;0)/C_n(G;0)`. The graph-distance-n ball contains every such path. This is the correct finite model for the source's ensemble. The same `D_k=E[X|F_k]` proof gives L1 with horizon n and the length-preserving root ratios.

## First-entrance upper bound (U) — KEEP as counting, not a scale bound

Every n-step path avoiding A but hitting the larger forbidden edge set B has a unique first oriented edge `(v,w)` in `B minus A` after some k-edge B-avoiding prefix. Its remaining `(n-k-1)`-edge suffix avoids A. Mapping the path to `(prefix, edge, suffix)` is injective. Counting all such triples without their mutual self-avoidance restriction yields the displayed sum in (U), so the inequality and its index `k=0,...,n-1` are correct. This is a cardinality product, with no independence assertion. The right-hand side has no proved mesh-uniform bound; it may be much larger than the left-hand side.

## H_disk — unproved input, not a full-target lemma

The proposed `limsup_n Delta_n(epsilon) <= C epsilon^alpha` uses the chosen scale `n^(-3/4)` and exact n-step counts. The source does not certify this scale. If H_disk held, L1 would turn it into uniform-in-prefix collar control. It would not identify an SLE limit, supply curve tightness, or prove the length-resolved conformal asymptotic H_len. The draft labels these gaps honestly. H_len is at least as load-bearing for identifying the full fixed-length limit; H_disk is the hardest concrete estimate attempted in this packet, not a demonstrated single hardest lemma of the whole conjecture.

## Draft bundle before integration — FIX

The read-only math store has 1,135 nodes in `probability.core` and zero in the proposed `probability.selfavoiding` namespace. Use the existing namespace for all seven entries. The maximal-bound lemma is valid for a general prefix filtration, but its submitted `proof_text` says `E D_tau=D_0` and ends with a bound by `D_0`; `D_0` can be random if the initial sigma-field is nontrivial. Both places must use `E D_0=r(A)-r(B)`. w396's own patch fixes the first occurrence but leaves the second. [Patch 01](patches/01_w396_bundle_review_fixes.diff) fixes both and the namespace; it has not been applied to the submitted bundle. The mathematical L1 verdict remains KEEP.

## L2: conditional total variation — KEEP

Within `E_A`, `E_B` has mass `p=r(B)/r(A)`. The law given `E_A` is `p` times the law given `E_B` plus `1-p` times the law given `E_A minus E_B`, with disjoint supports. Therefore TV in the stated convention is exactly `1-p`, attained by testing `E_B`; image laws have TV at most this by pullback of events. Positivity of both conditioning probabilities is required and stated.

## L3: conditional trace weak limit — KEEP under condition (C)

Hausdorff convergence in law gives `d_n=dist(K_n,A)` convergence in law to `d`. Portmanteau on `(0,infinity)` yields `P(d>0)<=r`. For each fixed `epsilon_j`, the closed set `[epsilon_j,infinity)` yields `r_j<=P(d>=epsilon_j)`; as `epsilon_j` decreases to zero, this gives `r<=P(d>0)`. Equality follows. On a Skorohod coupling, `d_n->d` almost surely, so false negatives vanish on `{d>0}`; equality of avoidance probabilities makes false positives vanish too. Bounded continuous test functions then give conditional weak convergence after division by `r>0`. This is a trace statement and condition (C) is a substantive unproved input in the SAW application. The example `K_n={1/n}, A={0}` has all finite traces avoiding A while the limit hits A, showing why the collar condition matters.

## Conditional identification and source references — FIX citation, KEEP conditional scope

The cited [Lawler–Schramm–Werner restriction paper](https://arxiv.org/pdf/math/0209343) Theorem 6.1 proves the SLE(8/3) avoidance formula; **Lemma 3.2**, rather than Theorem 6.1, says obstacle avoidance probabilities determine the hull law. For a simple interior curve, its oriented trace is determined by its trace and marked endpoints. The argument still requires a determining obstacle class, mapped to the paper's `Q*` hulls, plus ordered-curve tightness and simplicity. Those inputs are explicitly absent from the draft. Change the sentence that calls Theorem 6.1 a uniqueness theorem to cite Lemma 3.2 together with Theorem 6.1.

## Full target — DROP any solved claim

The central positive obstacle partition-ratio law `H_5/8` is not derived from L0–L3. The weighted direct-edge/two-edge graph shows the finite identities cannot determine a conformal exponent: its deletion ratio `u/(u+vw)` varies through `(0,1)`. It is only an obstruction to that inference, not a honeycomb counterexample. Critical SAW curve tightness, limit simplicity, and endpoint convention transfer remain open in this packet. The correct outcome is a checked partial reduction with an explicit gap.
