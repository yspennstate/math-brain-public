# FOREST / account02 B01 — two-cut forbidden-interval straddling and rank influence budget

**Run:** `B01-20260922T0529Z-forest-r15`  
**Outcome:** `ESSENTIAL_STEP_APPLIED`  
**Execution context:** `WITHOUT_VERIFIED_BRAIN`  
**Parent target:** OPEN; no full-proof claim.

## 1. Current control and source scope

Fresh owner controls were resolved from `yspennstate/math-research-brain` main at entry (`480fb18e2942d64e2671e904c5f89a726658d62d`) and reread through the current main during the run. Owner revision remains `2026-09-22.2`, directive `COLLECTIVE-OPEN-PROBLEMS-20260921T234023Z`; account02/B01 is FOREST research and new brain-installation / benchmark work remains stopped. The same-hour create-only login already existed and was preserved; this invocation has its own immutable start/finish records. Whole-README and isolated OWNER-MESSAGE SHA-256 are left `null / UNVERIFIED_CURRENT_RUN_BYTE_PIPELINE` rather than inferred from Git SHA-1.

The source target is unchanged: for a finite simple graph, under the unit uniform law on all acyclic edge subsets, prove pairwise edge negative correlation. Primary source: Grimmett--Winkler, *Negative association in uniform forests and connected graphs*, Random Structures & Algorithms 24 (2004), 444--460, arXiv `math/0302185`, DOI `10.1002/rsa.20012`.

Latest complete lead version consumed: account01/B01 `20260922T050946Z-b01-forest-auto11`, shared handoff blob `4cee205cb7d254caf785692838111988a0b8a155`, canonical report creation commit `79044b575c4b689248892f37b9930e983dddabca`. It keeps the fixed-graph Cocks globalization rejected fail-closed and derives a source-safe rank-homogeneous covariance budget.

Named OTHER-account result consumed: account03/B02 handoff `20260922T051758Z`, blob `c165e7c6b6ca991a97c5ed3d646611f91cf96adc`. I use its exact proper-2-sum counting identity only; I do **not** import its Cocks-dependent weighted closure. Own immediately preceding scalar debt handoff: `FOREST-2CUT-SCALAR-DEBT-v1-account02-B01-20260922T050132Z.md`, blob `16ed30da33730e074857a58410f270651a24c262`.

For the complete-log-concavity input used below, I bind the exact independent-set homogenization statement to Anari--Liu--Oveis Gharan--Vinzant, *Log-Concave Polynomials III: Mason's Ultra-Log-Concavity Conjecture for Independent Sets of Matroids*, arXiv `1811.01600`, whose source statement explicitly says that the homogenization of the generating polynomial of matroid independent sets is completely log-concave. I do not need a fixed-graph weighted Rayleigh theorem.

## 2. Compact conditional end-to-end route

Assume the simple source conjecture fails. Since every simple graph is a loopless multigraph, choose an **edge-minimal loopless-multigraph counterexample** `G` and a violating pair `e,f`. Working in the larger loopless class is legitimate for contradiction: source failure makes this class of counterexamples nonempty, and edge-minimality then pays every smaller loopless unit instance. Parallel marked edges cannot violate because their joint inclusion is impossible.

For a proper 2-separator `{u,v}` with both marks in one bridge `B` and a non-singleton outside `O`, let `D,C` be the outside forest counts with `u,v` respectively disconnected/connected and put

`lambda = C/D`.

The exact two-terminal gluing identity reduces the parent gap to

`Delta_G(e,f) = D^2 R(lambda)`,

where

`R(s)=d0 + m s + d1 s^2`

is the marked gap in `B` after adding a virtual `uv` edge of activity `s`. Minimality pays `d0>=0`, `d1>=0`, and `R(1)>=0`. The prior run stopped at the possibility that the actual `lambda` falls into a negative interval of this quadratic.

**New step in this run:** if such a negative interval exists and contains the actual `lambda`, then *every physical edge of the outside bridge must straddle the entire forbidden interval in its deletion/contraction terminal-connectivity response*. Summing those forced influences and applying the lead's rank-homogeneous variance bound gives an explicit rank obstruction. Thus the 2-cut debt is no longer an arbitrary scalar-weight question.

## 3. Exact two-terminal scalar, with the real outside response retained

Split forests of `B` according to whether they connect `u,v`. If a `B`-forest connects `u,v`, the outside must be disconnected, giving factor `D`. If it separates `u,v`, the outside can be any forest, giving factor `C+D=D(1+lambda)`. This is exactly the same multiplier as a virtual `uv` edge of activity `lambda`, hence the displayed factorization.

The partner's proper-2-sum formula is the same bookkeeping in matroid notation. This run uses the identity but not the partner's subsequent weighted-Cocks inference.

Let

`J={s>=0 : R(s)<0}`.

Because `R` is quadratic with `d0>=0` and `d1>=0`, `J`, if nonempty, is one open interval `(alpha,beta)` in the projective half-line `0<=s<=infinity`. The endpoint `beta=infinity` is allowed in the degenerate linear-tail case. Since `R(1)>=0`, `1` is not in `J`. If `d1>0`, the finite roots are

`alpha,beta = (-m -/+ sqrt(m^2-4 d0 d1))/(2 d1)`.

A parent violation is precisely `lambda in (alpha,beta)`.

## 4. New theorem A — every outside edge straddles the forbidden interval

Fix an outside edge `h`. Under the unit outside-forest law let `Y=1[u connected to v]`. Write

`q_i = P(Y=1 | X_h=i)`,  i=0,1,

and, when finite, the corresponding odds

`lambda_i=q_i/(1-q_i)`.

Then in a minimal counterexample with `R(lambda)<0`,

`q_0 <= alpha/(1+alpha) < beta/(1+beta) <= q_1`,

with `infinity/(1+infinity)=1`.

### Proof

Let `D_i,C_i` be exact outside counts with `X_h=i` and terminal state disconnected/connected. Add a new virtual unit `uv` edge `g` to the outside. This augmented outside has `|E(O)|+1 < |E(G)|`, because the marked bridge contains at least the two distinct marks. Edge-minimality therefore gives unit negative correlation for `h,g`. Its exact Rayleigh gap is

`Delta_{h,g}=D_0 C_1-C_0 D_1 >=0`.

Thus the terminal-connectivity odds are monotone under conditioning on `h`, equivalently `q_0<=q_1`. Also `q=P(Y=1)=lambda/(1+lambda)` is the ordinary mixture of `q_0,q_1`, so `q_0<=q<=q_1`.

Now delete or contract `h` in the **whole** counterexample. Both are smaller loopless unit instances (loops created by contraction are irrelevant to forests). The same exact 2-cut factorization says the marked gap in the deletion child is proportional to `R(lambda_0)` and the contraction child to `R(lambda_1)`; if a conditional disconnected count vanishes, the projective endpoint is `lambda_i=infinity` and the child gap is governed by the nonnegative leading coefficient `d1`. Hence neither child response lies in the open negative interval `J`.

Since the parent response lies inside `J`, while `q_0<=q<=q_1`, the deletion response must lie on or below the lower endpoint and the contraction response on or above the upper endpoint. This proves the straddling claim. In particular **every outside edge has strictly positive influence on terminal connectivity**. An outside edge with zero influence would immediately rule out the same-bridge violation. QED.

Define the forced probability-width

`delta = beta/(1+beta) - alpha/(1+alpha) > 0`.

The theorem gives for every outside edge

`P(Y=1|X_h=1)-P(Y=1|X_h=0) >= delta`.          (4.1)

This is a source-generated statement about the actual outside bridge; no arbitrary external field has been introduced.

## 5. New theorem B — rank influence budget

Let `r` be the graphic-matroid rank of the outside bridge, `K` its forest size, `mu=E K`, and

`q=P(Y=1)=lambda/(1+lambda)`.

Any same-bridge 2-cut violation must satisfy

`boxed:  delta <= 2 sqrt( q(1-q)/r )`

or equivalently

`boxed:  r delta^2 <= 4 lambda/(1+lambda)^2 <= 1.`               (5.1)

Thus

`r <= 4 lambda / ((1+lambda)^2 delta^2) <= 1/delta^2`.          (5.2)

### Proof

For an outside edge put `p_h=P(X_h=1)`. Exact binary covariance gives

`Cov(X_h,Y)=p_h(1-p_h)[P(Y=1|X_h=1)-P(Y=1|X_h=0)]`.

By (4.1),

`Cov(X_h,Y) >= delta p_h(1-p_h)`.

Deletion is an injection from forests containing `h` to forests omitting `h`, hence `p_h<=1/2`. Therefore

`sum_h p_h(1-p_h) >= (1/2) sum_h p_h = mu/2`.                  (5.3)

There is also an elementary lower bound `mu>=r/2` for every loopless matroid at activity one. If `i_k` is the number of independent sets of size `k`, every independent `k`-set extends to a basis and hence has at least `r-k` addable elements. Double counting extensions gives

`(k+1)i_{k+1} >= (r-k)i_k`.

Thus `i_k/binom(r,k)` is nondecreasing in `k`; pairing `k` with `r-k` (or applying monotone tilting to the symmetric binomial weights) yields `mu>=r/2`.

Summing the edge covariances now gives

`Cov(K,Y) = sum_h Cov(X_h,Y) >= delta mu/2 >= delta r/4`.       (5.4)

The lead's source-safe rank-homogeneous complete-log-concavity argument gives

`Var(K) <= mu(r-mu)/r <= r/4`,                                 (5.5)

where the last inequality uses `mu>=r/2`.

Finally Cauchy--Schwarz and `Var(Y)=q(1-q)` give

`delta r/4 <= Cov(K,Y) <= sqrt(Var(K)Var(Y)) <= (1/2)sqrt(r q(1-q))`.

Rearranging proves (5.1)--(5.2). QED.

## 6. What this pays, and what it does not

The preceding run had only the scalar unsafe-orientation condition

`(lambda-1)(lambda d1-d0)<0`.

The new result is strictly stronger and uses the **actual outside boundary law**. A same-bridge violation now forces a common forbidden interval for every deletion/contraction response of every outside edge, and its logistic width is bounded by the outside rank. This converts the previous arbitrary-looking real parameter into a global all-edge influence requirement.

A useful immediate structural corollary is that the outside cannot contain any edge whose conditioning leaves the terminal-connectivity probability unchanged; in particular, detached or multiplicatively irrelevant forest factors cannot occur in the offending outside.

This does **not** yet close all proper 2-cuts. The first remaining implication is now quantitative and source-bound: derive from the marked bridge's exact forest counts a lower bound on its forbidden probability-width `delta` strong enough to violate (5.1) for every source-realizable outside rank/response, or construct an actual graph-side/outside pair satisfying the full straddling budget. I do not assume such a lower bound.

Cross-bridge marked pairs remain closed by the prior exact factorization into two unit augmented-bridge gaps; the unresolved 2-cut case is same-bridge only.

## 7. Exact computation used only as auxiliary regression

A separate exact integer checker in this run tested the stronger one-new-virtual-edge statement on **every labelled simple bridge graph on 6 and 7 vertices**, all distinct marked-edge pairs modulo the terminal-preserving symmetry group, and the full real activity ray `s>=0`. It found no negative weighted virtual-edge gap:

- `n=6`: 32,768 graph masks, 9 marked-pair orbits, 860,160 marked graph/pair instances, failures 0;
- `n=7`: 2,097,152 graph masks, 9 marked-pair orbits, 110,100,480 marked graph/pair instances, failures 0.

The checker does not grid the activity: for each graph it forms the exact integer quadratic and tests its real minimum on `s>=0` by its discriminant/vertex criterion. Output terminates `VIRTUAL_EDGE_N7_EXACT_SCAN_PASS`.

This is **AUXILIARY_ONLY evidence inside an ESSENTIAL_STEP_APPLIED run**. It is not counted as universal closure, not treated as novelty evidence, and does not replace theorem (5.1).

Artifacts:

- `virtual_edge_scan.py` — exact subset-zeta checker;
- `virtual_edge_scan_output.txt` — exact observed output.

## 8. Failure preservation and source discipline

Preserved failures / rejected shortcuts:

- Fixed-graph `unit-good => arbitrary-weight I-Rayleigh` remains fail-closed; no Cocks globalization is used.
- The partner's exact 2-sum identity is used, but its Cocks-dependent closure conclusion is not.
- The earlier three-terminal K4 response cone is not used as an inductive invariant; the prior run already showed abstract additivity failure.
- The finite n<=7 virtual-edge scan is not a proof.
- No rooted-forest, fixed-size, spanning-tree, or arbitrary positive-weight law is substituted for the source law.

## 9. Status and handoff

**Outcome: `ESSENTIAL_STEP_APPLIED`.** Parent FOREST remains open. The new reusable statement is `FOREST-2CUT-INFLUENCE-BUDGET-v1`: any same-bridge proper-2-cut violation forces every outside edge to straddle the same forbidden response interval and obeys the rank-width budget (5.1). The next useful attack is to relate the forbidden width directly to source-realizable marked-bridge counts, not to reintroduce arbitrary weighted closure.

Execution remained `WITHOUT_VERIFIED_BRAIN`; no production state or brain installation was used. Current-account managed inventory was inspected only for account02: 20/20 active tasks were present and hourly-valid, with no missing slot and no B01 scheduler mutation. Quiet task-level notification/email flags were observed off; account-level preference was not exposed.

Scoped privacy/secret review: report, checker, output, handoff and receipts contain only mathematical/source/control metadata allowed by the task. No credentials, scheduler identifiers, machine paths, benchmark gold, private transcripts, email/Drive material, or unrelated personal data are included. Review method was a narrow manual content scan because no repository privacy checker was required by the mathematical payload.

Model self-report: `GPT-5.6 Sol`. Requested reasoning effort: `maximum actually supported`. Configured effort: `UNKNOWN / not exposed`. Known actual reasoning effort: `UNKNOWN / not exposed`. Provider reasoning-token usage: `null / not exposed`. Provider thinking-time usage: `null / not exposed`. Observed elapsed execution is recorded in the finish receipt and is wall-clock tool/research time, not pure thinking.
