Model actually run: **GPT-5.6 Sol. Reasoning level: UNVERIFIED. This is not GPT-6 at maximum.**

# P03 / P0456 run report — sparse deleted competitors remove the sqrt(log n) proof-route constant

**MOVEMENT: `b_LK^sqrt: C_* -> 0`, where `C_*=e phi(Phi^{-1}(e^{-1}))=1.0244099529838058...`.** This is the theoretical minimum of the admitted fixed-coefficient proof-frontier metric at scale `sqrt(log n)`, so its unchanged count resets to `0`; HARD recoveries remain `0/2`. The already saturated coarser metrics remain `c_LK^cert=0` and `a_LK^fine=0` and are not used to manufacture a stuck count.

Main new claim:

`P03-P0456-SPARSE-DELETION-SQRTLOG-ZERO-286 = PROVED / FINER-WINDOW-PARTIAL / PUBLICATION-NOVELTY-UNVERIFIED`.

For every fixed real `b<0`, if

`k <= log n + b sqrt(log n)`,

then `LK(n,k)` is disconnected with high probability. For every fixed `b>0`, if

`k >= log n + b sqrt(log n)`,

then `LK(n,k)` is connected with high probability.

Equivalently, the fleet fixed-coefficient frontier at the `sqrt(log n)` scale is now zero. This does **not** decide `k=log n+o(sqrt(log n))`, the coefficient-zero case, an `O(1)` critical window, or a limiting law.

The three Section-B moves used substantively were **B1 CHANGE THE CATEGORY, B17 LOOK FOR YOUR NUMBERS SOMEWHERE ELSE, B20 FIND WHY THE ALGORITHM FAILS**.

---

## 1. Continuity, source, and repository status

The canonical exclusive claim remains `operations/claims/P0456.md`, creation commit `9d9c9545783bf8ae09805830d72f5d935be9afb1`, blob `74b9c5ebda19b1ded526457c1c7ea12654419bcb`.

I continued from the newest complete P03 report

`proofnet24/P03-fei/runs/2026-09-18/2026-09-18T10-27-17Z__p0456-normal-race-sqrtlog-bracket.md`,

creation commit `178c78981fef27ef696dfed3bb7652d3c26ec1d2`, blob `c7cde8162b8b2736ce8b1c1979434512325b181b`, and preserve Claims 274, 276, 278, 280, 282 and 284.

Repository continuity this invocation recovered/reread the root README, `proofnet24/HOURLY_PROTOCOL_2026-09-15.md`, `FLEET_RULES.md`, `operations/new_methods_2026-09-16/OWNER_DIRECTIVE.md`, campaign `probability_campaign_2026_09/INDEX.md` and `RANKING.md`, the current P0456 claim/history, the newest own report, and relevant P04 material for the directed peer audit. Root ledger/directory surfaces are connector-truncated, so I do not claim a byte-for-byte reread of every large surface; exact-path and targeted reads were used where needed.

Primary source freshly rechecked 2026-09-18:

Hossein Dabirian and Vijay Subramanian, *Connectivity of a family of bilateral preference random graphs*, Journal of Applied Probability 63(2) (June 2026), 552--579, DOI `10.1017/jpr.2025.10051`, especially Section 1.1 and Lemmas 10--14.

Section 1.1 still explicitly says the paper does not know connectivity in the displayed band

`log n -(1/2) loglog n sqrt(log n) <= k <= log n +(1/2) loglog n sqrt(log n)`

and attributes the gap to analytically convenient sufficient conditions. On pp. 567--569, Lemma 10 gives `P(B)=O(k^3/n)`, Lemma 11 conditions on the bad-side events and removes the `s` preferred-neighbor edges before applying a type-permutation estimate, Lemma 12 propagates this into the exceptional pair probability, and Lemma 13 gives exact conditional independence on `B^c`.

A fresh bounded literature search for the exact title/authors/DOI, `LK(n,k)`, and bilateral-preference connectivity recovered the source and adjacent material but no later source-matching closure. This is dated bounded negative evidence only, not a worldwide openness or publication-novelty certificate.

---

## 2. Idea before calculation — B20 finds the exact loss in Claim 284

Claim 284 used the source's necessary condition from Lemma 11 verbatim. For a first block of `s=lambda sqrt(k)` preferred neighbors, it deleted all edges from a selected neighbor `i` to the other first-`s` preferred neighbors and therefore replaced the true rejection requirement

`at least k competing edges before (v,i)`

by the pessimistic outside-edge requirement

`at least K=k-s-O(1) outside competitors before (v,i)`.

At the `sqrt(k)` scale this deterministic subtraction is exactly the `+lambda sqrt(k)` term in Claim 284's coefficient

`C(lambda)=lambda+H(lambda)`.

B20 asks whether those `s` deleted competitors are actually present before the target edge. They are not: an internal edge between two of the first `s` preferred neighbors has to beat an incident order statistic of size about `s/n`. There are only `O(s^2)` such edges. For fixed `lambda` and `s=lambda sqrt(k)`, the expected number of **active** deleted competitors is therefore polynomially small in `k` divided by `n`, not order `s`.

The correct category (B1) is consequently a **marked point-process race with sparse collision marks**, not an adversarial deletion of `s` positions. Once the sparse collisions are separated, the ordered-race exponent is `H(lambda)`, without the `+lambda`. Since `H(lambda)` decreases to zero as `lambda -> infinity`, every fixed nonzero coefficient at the `sqrt(log n)` scale can be handled.

I first tried to refute this by asking whether the source bad-pair conditioning could force many of the deleted internal edges to become early. It does not at source scale: after disjointizing the source bad events, a direct witness count gives an extra factor `1/n` for an active internal collision. The resulting intersection is only polynomial in `k` times `n^{-2}`, which is negligible after normalization for every fixed negative `sqrt(log n)` offset.

---

## 3. The race without the artificial deletion shift

Retain Claim 284's notation

`A_K(T)=E[(T-G_K)_+]`,  `G_K~Gamma(K,1)`,

and

`a(x)=phi(x)+x Phi(x)`.

For fixed `lambda>0`, set

`s=lambda sqrt(K)+O(1)`

and let all but a fixed number `h` of the first `s` individual deadlines be enforced. Claim 284's ordered-deadline proof, before the source substitution `K=k-s-O(1)`, gives

`log P(race_K) <= -K +(H(lambda)+o(1)) sqrt(K)`,              (1)

where

`H(lambda)=sup_x {-x+lambda[1+log(a(x)/lambda)]}`.             (2)

The unique optimizer `x_lambda` satisfies

`lambda=x_lambda+phi(x_lambda)/Phi(x_lambda)`.                 (3)

At the optimizer,

`H(lambda)=-x_lambda+lambda[1+log Phi(x_lambda)]`.             (4)

The envelope derivative from Claim 284 is

`H'(lambda)=log Phi(x_lambda)<0`.                              (5)

Moreover `x_lambda -> +infinity` as `lambda->infinity`; using the normal Mills asymptotics in (3)--(4),

`phi(x_lambda)/Phi(x_lambda) ~ phi(x_lambda)`,

`1-Phi(x_lambda) ~ phi(x_lambda)/x_lambda`,

shows

`H(lambda) -> 0`.                                              (6)

Thus for every `epsilon>0` there is a **fixed** `lambda=lambda(epsilon)` such that

`H(lambda)<epsilon`.                                          (7)

The finite source permutations have type-list sizes `n-O(s)` rather than infinite Poisson streams. Exactly as in Claim 284, the relevant prefix has length `O(k^{3/2})`; for `k=O(log n)` its without-replacement likelihood ratio to the iid word is `1+o(1)`. Hence (1) transfers unchanged at `sqrt(k)` order.

The rest of the run is devoted to proving that the true graph event can use `K=k-O(1)` rather than `k-s-O(1)` except on an `n^{-1}`-rare collision event.

---

## 4. Sparse-collision lemma for one vertex

Use the equivalent convention that iid edge weights `U_e` are Uniform `[0,1]` and **smaller is preferred**. Fix a vertex `v`, let

`X_(1)<...<X_(n-1)`

be its incident order statistics, and let `S` be its first `s=floor(lambda sqrt(k))` preferred neighbors.

Define the active internal-collision event

`C_v = {there exist distinct i,j in S with U_{ij}<max(U_{vi},U_{vj})}`.

Let `L>3` be fixed and define

`G_v={X_(s)<=Lk/n}`.

Conditional on all incident weights at `v`, the internal edges among `S` are independent uniforms. On `G_v`,

`P(C_v | incident weights at v)
 <= binom(s,2) X_(s)
 <= O_lambda(k^2/n)`.                                         (8)

(The sharper typical order is smaller; the displayed bound is deliberately coarse.)

The complement of `G_v` is exponentially negligible. Indeed

`P(G_v^c)=P(Bin(n-1,Lk/n)<=s-1)`

and the elementary binomial lower-tail estimate gives

`P(G_v^c) <= exp[-Lk+O(s log k)]
           = exp[-Lk+O_lambda(sqrt(k) log k)]`.                (9)

Now fix an integer `kappa>=0`. If `deg(v)<=kappa`, at least `s-kappa` vertices in `S` reject `v`. On `C_v^c`, none of the internal `S`-edges can precede either endpoint's edge to `v`. Consequently every such rejecting neighbor must have at least **k** edges from outside `{v} union S` before its target edge. Those outside-edge sets are disjoint for distinct neighbors. Therefore, conditional on the incident deadlines at `v`, the event is exactly bounded by the ordered individual-deadline race (1) with threshold `K=k` and at most `kappa` omitted deadlines.

On `G_v cap C_v` we simply use the collision probability (8), but to keep the global low-degree bound exponentially sharp we combine it with the always-valid source-style race in which all `s` internal edges are pessimistically available. Conditional on the incident deadlines the collision edges and the outside-edge race use disjoint edge sets, so

`P(G_v cap C_v cap {deg(v)<=kappa})
 <= O_lambda(k^2/n)
    exp[-k+(C(lambda)+o(1))sqrt(k)]`,                          (10)

where `C(lambda)=lambda+H(lambda)` is Claim 284's finite constant for this fixed `lambda`.

Combining (1), (8)--(10), and (9) yields, for every fixed `lambda,L,kappa`,

`P(deg(v)<=kappa)
 <= exp[-k+(H(lambda)+o(1))sqrt(k)]
  + O_lambda(k^2/n) exp[-k+(C(lambda)+o(1))sqrt(k)]
  + exp[-Lk+O_lambda(sqrt(k)log k)]`.                          (11)

Since `k=log n+O(sqrt(log n))`, the last two terms are negligible compared with the first on every fixed-coefficient window. By (7), for every `epsilon>0` and every fixed `kappa`,

`boxed{ P(deg(v)<=kappa)
        <= exp[-k+(epsilon+o(1))sqrt(k)] }.                    (12)

For `kappa=0`, Claim 278 supplies the matching source-valid lower bound

`P(I_v)>=(1-k/(n-k))^(n-1)=exp[-k-o(1)]`.                     (13)

Hence we obtain the sharp one-vertex asymptotic through the entire `sqrt(k)` order:

`boxed{ (log P(I_v)+k)/sqrt(k) -> 0 }`.                        (14)

Thus the coefficient `d` asked for in this run is exactly `d=0`.

---

## 5. Sparse collisions inside the source bad-pair event

Let the source bad-side event for vertex 1 be

`A_1=B_{1;2} union B_{1 union 2} union B_{1->2}`,

so `P(A_1)=O(k^3/n)` by Lemma 10. Let `S=R_1^{<=s}\{2}` and let `C_1` be the event that an edge internal to `S` precedes at least one of its two incident target edges `(1,i)`.

The key point is that the bad-event witness and an active internal collision require **two distinct rare rank coincidences**. A direct disjoint witness count gives

`boxed{ P(A_1 cap C_1)=O_lambda(k^6/n^2) }`.                  (15)

Here is the count. Disjointize `A_1` in the source order.

1. `B_{1;2}` fixes vertex 2 among the first `k` ranks at vertex 1. Rank identities are independent of the numerical order statistics at vertex 1, while the internal `S`-edges are disjoint from vertex 1. Using `E X_(s)=s/n` and a union over at most `s^2` internal pairs gives `O((k/n)(s^3/n))`.

2. On `B_{1;2}^c`, the overlap event `B_{1 union 2}` has probability `O(k^2/n)` uniformly once `R_1^{<=k}` is fixed (this is the exact hypergeometric calculation in source (8)). Its defining edges are incident to vertex 2, not internal to `S`; multiplying the same internal-pair union bound gives `O((k^2/n)(s^3/n))`.

3. On the complements of the preceding two events, a `B_{1->2}` witness consists of `i in R_1^{<=k}` and `j in R_2^{<=k} union {2}` with `j in R_i^{<=k}`. Here `R_2^{<=k}` is disjoint from `R_1^{<=k}`, so the witness edge is not an internal `S`-edge. If it shares an endpoint with a candidate internal collision, lowering that competing internal edge can only make the outside witness **less** likely to occupy a top-`k` rank. By exchangeability, its conditional top-`k` probability is therefore at most `k/(n-1)`. Union over the `O(k^2)` outside witnesses and `O(s^2)` internal pairs, and use `E X_(s)=s/n`. This is `O(k^3 s^3/n^2)`, which is `O(k^6/n^2)` because `s=O(sqrt(k))`.

This proves (15); the deliberately loose polynomial power is immaterial.

On `A_1 cap C_1^c`, isolation of vertex 1 has a much stronger necessary condition than the source's `k-s-2` condition. For every `i in R_1^{<=s}\{2}`, all internal edges to the other first-`s` neighbors lie after `(1,i)`. The only excluded edge which can still precede `(1,i)` is `(i,2)`, so at least `k-1` elements of the source set `E'_i` must precede `(1,i)`. The source's conditioning in Lemma 11 still gives a uniform type permutation on the disjoint `E'_i` lists with only the type-0 deadline order retained. Applying (1) with threshold `K=k-1` therefore gives

`P(I_1 cap C_1^c | A_1)
 <= exp[-k+(H(lambda)+o(1))sqrt(k)]`.                           (16)

Together with (15),

`P(I_1 cap A_1)
 <= O(k^3/n) exp[-k+(H(lambda)+o(1))sqrt(k)]
    +O_lambda(k^6/n^2)`.                                      (17)

By symmetry the same bound holds for the vertex-2 bad-side event. The source Lemma-12 decomposition consequently sharpens to

`boxed{
P(I_1 I_2 cap B)
 <= O(k^3/n) exp[-k+(H(lambda)+o(1))sqrt(k)]
    +O_lambda(k^6/n^2).
}`                                                               (18)

This identifies precisely what Claim 284's ordered-deadline algorithm discarded: it replaced an `n^{-1}`-sparse family of genuinely early deleted competitors by `s=lambda sqrt(k)` adversarial competitors at every deadline. That replacement, and not the Gamma race itself, created `C_*`.

---

## 6. Disconnection for every fixed negative sqrt(log n) coefficient

Assume

`k=log n+b sqrt(log n)+O(1)`

with fixed `b<0`. Choose `epsilon<|b|/3` and then choose a fixed `lambda` so that `H(lambda)<epsilon` by (7).

Let `p_n=P(I_v)`. From (13),

`n p_n >= exp[log n-k-o(1)]
        = exp[|b|sqrt(log n)-o(sqrt(log n))] -> infinity`.      (19)

Source Lemma 13 gives exact conditional independence on `B^c`. As in source Lemma 14, the first conditional-independence term is asymptotic to one because

`P(I_1 cap B)/(p_n P(B^c))
 <= P(B)/p_n
 <= exp[k-log n+O(log k)+o(1)] ->0`                            (20)

for fixed `b<0`.

For the exceptional pair term, divide (18) by `p_n^2`. Its first part is at most

`exp[k-log n+(H(lambda)+o(1))sqrt(k)+O(log k)]
 = exp[(b+H(lambda)+o(1))sqrt(log n)] ->0`.                    (21)

The second part satisfies

`O(k^6/n^2)/p_n^2
 <= k^6 exp[2k-2log n+o(1)]
 = exp[2b sqrt(log n)+O(loglog n)] ->0`.                       (22)

Thus `E[I_1 I_2]/E[I_1]^2 <=1+o(1)`. Together with (19), the source second-moment argument gives an isolated vertex with high probability. Hence `LK(n,k)` is disconnected whp for every fixed `b<0`.

---

## 7. Connectivity for every fixed positive sqrt(log n) coefficient

Now assume fixed `b>0` and

`k=log n+b sqrt(log n)+O(1)`.

Choose `epsilon<b/3` and a fixed `lambda` with `H(lambda)<epsilon`. Taking `kappa=5` in (12),

`n P(deg(v)<=5)
 <= exp[log n-k+(epsilon+o(1))sqrt(k)] ->0`.                   (23)

Therefore, with high probability there is no connected component of size at most six.

For fixed component sizes `7<=r<=12`, retain Claim 280's source-valid exponential-score/Cayley crossing-edge estimate. Its leading logarithmic coefficient is

`1-5r/32<0`,

so the union probability is `o(1)` uniformly under the present perturbation `k=log n+O(sqrt(log n))`. Claim 278's retained large-component estimate handles `13<=r<=n/2` with the same margin. These arguments do not use mean degree.

Thus with high probability no component has size at most `n/2`; hence the graph is connected. This proves the positive half for every fixed `b>0`.

Combining Sections 6 and 7 proves Claim 286 and

`boxed{ b_LK^sqrt: C_* -> 0 }`.

---

## 8. B17 — where the old constant appears, and what the search did not show

I searched for the exact expression

`e phi(Phi^{-1}(e^{-1}))`,

for the equivalent variational problem involving

`phi(x)+x Phi(x)=E[(x-Z)_+]`,

and for Gamma-race / queueing formulations using the inverse Mills ratio. The bounded search found standard appearances of `phi/Phi` as the inverse Mills ratio / one-sided Gaussian truncation hazard, including contemporary diffusion/reliability discussions, but no source matching the exact constant `C_*` or this Gamma-race extremization.

This is useful negative evidence about B17 only. It does **not** certify publication novelty of Claim 284 or Claim 286. The inverse-Mills identities themselves are standard.

---

## 9. Directed second audit — P04 / I0101

The newest P04 run at `10:50:12Z` created no mathematical claim; it was a stuck-recovery/rotation handoff. I therefore audited a concrete substantive P04 claim not previously in P03's audit exclusion list:

`P04-I0101-THETAPLUS-PURITY-OBSTRUCTION-40 = PROVED / STRUCTURAL-PARTIAL`,

from

`proofnet24/P04-closure-local-paley/runs/2026-09-18/2026-09-18T06-11-29Z__run-report.md`,

creation commit `511ad6b4abab85c5a13903a58b602847d11adc07`, exact blob `bf2682fbd0f0ffdaca0259422add84aca906a4e6`.

Independent audit ID:

`P03-AUDIT-P04-I0101-THETAPLUS-PURITY-OBSTRUCTION-287 = PASS (CLAIM-SCOPED)`.

Re-derivation: for theta-plus dual feasible `X`, let

`T=<J,X>`, `Delta=-2<A_K,X>`, and write unordered edge sums `s_G,s_K`. Since `tr X=1`,

`T=1+2(s_G+s_K)`,  `Delta=-4s_K`,

so

`s_G=[2(T-1)+Delta]/4`.

If `m=|E(G)|`, Cauchy--Schwarz gives

`s_G^2 <= m sum_{ij in E(G)} X_ij^2`,

while

`tr(X^2)>=2 sum_{ij in E(G)}X_ij^2`.

Hence

`tr(X^2)>=[2(T-1)+Delta]^2/(8m)`.

The exact localized degree estimate used by P04 is

`d_x=(p-15+S_x)/8`, `|S_x|<=2sqrt(p)`,

so

`m<=n(p-15+2sqrt(p))/16`.

Substitution gives exactly

`tr(X^2)>=2[2(T-1)+Delta]^2/[n(p-15+2sqrt(p))]`.

For `T>2sqrt(p)/3` and `Delta>=0`, multiplying by `p` and using `n=(p-5)/4` yields

`liminf p tr(X^2)>=128/9`,

and reciprocation gives the stated effective-rank bound `(9/128+o(1))p=(9/32+o(1))n`. The constants and inequality directions check. This PASS certifies Claim 40 only; it does not certify Randomstrasse Conjecture 27.

---

## 10. Exact remaining obligation and next state

All three admitted fixed-coefficient metrics are now saturated at zero:

- `c_LK^cert=0` at `sqrt(log n) loglog n`;
- `a_LK^fine=0` at `sqrt(log n loglog n)`;
- `b_LK^sqrt=0` at `sqrt(log n)`.

The live P0456 problem is therefore **coefficient zero / sub-sqrt(log n)**. No new metric is admitted in this run. The next plausible question is whether the transition is actually `O(1)` around `k=log n` and whether isolated vertices have a Poisson limit.

The strongest immediate input is (14):

`log P(I_v)=-k+o(sqrt(k))`.

What is missing is the multiplicative asymptotic, ideally

`P(I_v)=c_0 e^{-k}(1+o(1))`

with explicit `c_0`, together with a pair/factorial-moment theorem at `k=log n+O(1)` and matching control of nontrivial components. The sparse-collision argument proves only that the old `sqrt(k)` loss was artificial; it does not yet identify `c_0` or the limiting law.

A fresh next-method triple should attack that genuinely new scale rather than re-run the collision proof: **B3 PROVE SOMETHING STRONGER, B11 DUALIZE, B25 COUNT THE SAME THING TWICE**. One promising route is to Poissonize the exact marked order-statistic integral from Claim 278, derive its constant-order saddle point exactly, and count the same limiting object through a Palm/Poisson point-process description. Only after a theorem at an `O(1)` or other smaller scale should a new metric be admitted.

---

## 11. ledger_delta for P26

- P03 remains exclusively assigned to `P0456`.
- `P03-P0456-SPARSE-DELETION-SQRTLOG-ZERO-286 = PROVED / FINER-WINDOW-PARTIAL / PUBLICATION-NOVELTY-UNVERIFIED`.
- `b_LK^sqrt: C_* -> 0` (theoretical minimum), unchanged count `0`, recoveries `0/2`.
- Coarser `c_LK^cert=0` and `a_LK^fine=0` remain saturated.
- Exact source status remains PARTIAL/OPEN: coefficient zero, `o(sqrt(log n))`, and limiting law unresolved.
- `P03-AUDIT-P04-I0101-THETAPLUS-PURITY-OBSTRUCTION-287 = PASS (CLAIM-SCOPED)`; peer source report creation `511ad6b4abab85c5a13903a58b602847d11adc07`, blob `bf2682fbd0f0ffdaca0259422add84aca906a4e6`.
- No shared root ledger was edited; P26 alone owns that update.

## 12. Model/tool limitations

The actual runtime is GPT-5.6 Sol with reasoning level UNVERIFIED. The task-control interface available to this worker still exposes no trustworthy model-family selector or reasoning-effort selector, so GPT-6 / maximum remains prompt-only and is not claimed as applied runtime metadata. GitHub writes are authorized in the current context. No email, Drive, public posting, paid compute, access change, workflow execution, or peer-file edit was performed.

**End of complete run report.**