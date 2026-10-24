Model actually run: **GPT-5.6 Sol. Reasoning level: UNVERIFIED — this is not GPT-6 at maximum, and I do not claim otherwise.**

# P0151 analytic artifact — a failure-only one-unit cap layer

This is a self-derived theorem-sized proof artifact for `HARD7-04` and the exact sequential fixed-outdegree affine preferential-attachment model frozen in `operations/claims/P0151.md`. It strengthens the current one-sided exponent bound by changing the exploration rule in a controlled way. It does **not** determine the full critical window, prove a matching upper bound, establish the `sqrt(n)/log n` scale for the finite graph, or identify a scaling-limit law. The source problem remains open.

The central new point is that the old bridge cap `c_0(w)=min(w,2A)` is not locally saturated. A second ticket used only after the old cap ticket fails realizes a positive one-unit cap layer while leaving every previously accepted outcome untouched. The exact first-order mass in that layer is computable from the affine-PA degree recursion by a one-line tail telescoping identity.

---

## Proposition

Fix integer `m>=2` and `delta>0`. Put

`a:=m+delta`, `A:=2m+delta`, `pi:=pi_c`,

where

`pi_c:=delta/[2( m(m+delta)+sqrt(m(m-1)(m+delta)(m+1+delta)) )]`.

Inherit from the preceding HARD7-04 results the connected shadow process and the proved estimates

`gamma_E>=b13`,

`U12<1/2`,

`E W_t^2=O(t)`, `E Z_t=O(t^h)`, `h=m/A<1/2`,

where

`gamma_E:=liminf_{n->infinity} log E|C_max(n,pi_c)|/log n`

and `W_t` is the current shadow attractiveness. The `b13` proof did not change the process, so its inherited upper coefficient is still `U12`.

Let

`eta:=m(m-1)pi^2`.                                                (P.1)

The old current-birth bridge acceptance profile is

`c_0(w):=min(w,2A)`.                                              (P.2)

Define the one-unit layer

`d(w):=min(w,2A+1)-min(w,2A)
     =min(1,(w-2A)_+)`.                                          (P.3)

Let the affine-PA limiting degree proportions be

`p_m:=A/[A+m(m+delta)]`,                                         (P.4)

`p_k:=m(k-1+delta)p_{k-1}/[A+m(k+delta)]`, `k>m`.                (P.5)

Put

`K:=floor(4m+delta)+1`,
`theta:=K-(4m+delta) in (0,1]`,
`w_K:=K+delta`.                                                   (P.6)

Define the exact layer mass

`D_cap:=w_K p_K [ theta + m(w_K+1)/a ]`.                         (P.7)

Then `D_cap>0`.

Let

`M12:=1/2-U12>0`,

'tau:=min(1, M12*A/(2 eta))`.                                   (P.8)

Augment the old bridge rule as follows. Whenever an old capped bridge ticket to a target of attractiveness `w` fails, toss one additional independent coin with success probability

`tau*d(w)/(w-c_0(w))`                                            (P.9)

when `w>c_0(w)`, and zero otherwise. An extra-layer success adds that target to the connected shadow **after** all old same-birth historical-ticket rules have finished; it triggers no additional same-birth historical inspection.

Then the augmented process still lies in one true percolation component and satisfies

`gamma_E>=b14`,                                                   (P.10)

where

`b14:=b13 + tau*eta*D_cap/A^2 > b13`.                            (P.11)

Moreover its first-moment upper coefficient may be taken as

`U14:=U12+tau*eta/A <1/2`,                                       (P.12)

and the second-moment bootstrap remains

`E W_t^2=O(t)`.                                                   (P.13)

Thus the frozen source-relevant metric moves strictly from `gamma_E>=b13` to `gamma_E>=b14>b13`.

---

## 1. B5 — add a cap parameter and attack local optimality first

The first question was the negation of the intended route:

> Could the old cap `2A` already be locally optimal, so that every infinitesimal enlargement is paid for entirely by variance/upper-drift cost and yields no first-order lower drift?

For a degree-weight value `w`, increasing the cap from `2A` to `2A+1` creates exactly the layer `d(w)` in (P.3). Therefore, under the limiting degree law, the first-order bridge mass made available by this layer is

`sum_{k>=m} (k+delta)p_k d(k+delta)`.                             (1.1)

Every `p_k` is strictly positive. Since degrees are unbounded and `d(k+delta)>0` once `k+delta>2A`, (1.1) is strictly positive. Hence the cap is **not** locally saturated.

The useful issue is not merely positivity but whether the gain can be realized without invalidating the old process. Formula (P.9) does exactly that. Conditional on an old bridge target of weight `w>2A`, the old ticket succeeds with probability `c_0(w)/w`. Therefore the unconditional probability of a new-layer acceptance is

`[1-c_0(w)/w] * tau*d(w)/(w-c_0(w))
 =tau*d(w)/w`.                                                    (1.2)

The second coin is legal because `0<=d(w)<=w-c_0(w)` and `tau<=1`. Thus the old accepted outcomes are a literal subset of the augmented accepted outcomes; no old ticket is weakened or resampled.

**B5 outcome:** successful. The old cap is not a local optimum, and a monotone failure-only perturbation realizes the positive derivative inside the true finite-graph exploration.

---

## 2. B16 — compute the threshold shell, then telescope the entire tail

The one-unit layer has only three degree regimes. With `K,theta` from (P.6),

`d(k+delta)=0`, `k<=K-1`,

`d(K+delta)=theta`,

`d(k+delta)=1`, `k>=K+1`.                                        (2.1)

So the limiting layer mass is

`D_cap=theta*w_K*p_K + sum_{k>=K+1}(k+delta)p_k`.                (2.2)

The infinite tail in (2.2) has an exact closed form. Write `w_k=k+delta`. The recursion (P.5) is

`[A+m w_k]p_k=m(w_k-1)p_{k-1}`.                                 (2.3)

Multiply by `w_k` and sum from `k=r+1` to `N`. After shifting the right-hand side,

`A sum_{k=r+1}^N w_k p_k
 =m w_r(w_r+1)p_r
  +m sum_{k=r+1}^{N-1} w_k p_k
  -m w_N^2 p_N`.                                                 (2.4)

The standard explicit solution of (2.3) has `p_N=O(N^{-(3+delta/m)})`, hence `w_N^2p_N->0`. Letting `N->infinity` and using `A-m=a` gives

`sum_{k>=r+1} w_k p_k
 =m w_r(w_r+1)p_r/a`.                                            (2.5)

Taking `r=K` in (2.5) and substituting into (2.2) proves exactly (P.7):

`D_cap=w_K p_K[theta+m(w_K+1)/a]>0`.                             (2.6)

This identity is more useful than a generic tail estimate: one boundary atom determines the whole weighted tail.

For the finite graph, let `N_k(t)` denote the ordinary degree-`k` count. The preceding `b13` artifact already proved, for every fixed finite degree window,

`E(N_k(t)-p_k t)^2=O(t)`.                                        (2.7)

Let

`G_t^all:=sum_{ordinary u} w_u(t)d(w_u(t))`.                      (2.8)

Because the layer is zero below `K`, fractional at `K`, and equal to one above `K`, one can either use (2.1) directly or subtract the finite head from total ordinary attractiveness. For every fixed `epsilon>0`, off an event of probability `O_epsilon(1/t)`, (2.7) and the deterministic total-attractiveness identity give

`G_t^all >= (D_cap-epsilon)t - Z_t-C`.                            (2.9)

Deleting vertices already in the shadow costs at most their attractiveness because `d<=1`, hence

`G_t:=sum_{ordinary u outside Q_t} w_u(t)d(w_u(t))
 >=(D_cap-epsilon)t-W_t-Z_t-C`                                   (2.10)

on the same good event.

The finite specialization `m=2,delta=1` was computed exactly before any paper-style bookkeeping was added. Here `A=5`, `K=10`, `theta=1`, and

`D_cap=98304/96577 = 1.017882104434803...`.                      (2.11)

The executed exact checker and output are:

- `artifacts/hard7_2026-09-18/HARD7-04/p0151_cap_layer_exact_20260920T1330Z.py` @ `ff80559d2d7c67d8ae865d45f058a9ae7dd92293`;
- `artifacts/hard7_2026-09-18/HARD7-04/p0151_cap_layer_exact_20260920T1330Z.out` @ `749cf78b27487501f98f0e79bfa2083137f33184`.

Both were read back at those exact commits and the output ends `ALL_EXACT_CHECKS_PASS`.

**B16 outcome:** successful. The first shell above the old cap exposed an exact telescoping identity for the full weighted tail rather than merely another numerical gain.

---

## 3. B18 — recode the new route as a monotone change of measure on the old ticket

Rather than inventing a new graph motif, regard each old bridge target as carrying an auxiliary acceptance variable. The old acceptance kernel is `c_0(w)/w`. The failure-only coin (P.9) changes this to

`[c_0(w)+tau d(w)]/w`.                                           (3.1)

Thus the augmented exploration is the old one under the deterministic acceptance profile

`c_tau(w):=c_0(w)+tau d(w)`,                                     (3.2)

with

`c_0(w)<=c_tau(w)<=min(w,2A+1)`.                                 (3.3)

This recoding matters because every same-birth target/duplicate estimate from the old capped-bridge proof depends only on: (i) a deterministic cap bound; (ii) the fact that accepted targets are genuine retained neighbors; and (iii) shadow connectivity. Replacing `2A` by the finite cap `2A+1` preserves those estimates with changed constants. The extra-layer targets are inserted only after old same-birth historical processing, so no new within-birth revelation cycle is introduced.

**B18 outcome:** successful. The apparent new exploration is a monotone perturbation of the old acceptance kernel, so the old combinatorial collision architecture is reusable rather than rebuilt.

---

## 4. Extra first-order drift

Consider the ordered current gate--bridge pairs used in the inherited capped bridge proof. Summed over the `m(m-1)` ordered pairs, the new-layer direct reward has the same denominator and retention factor as the old bridge term. By (1.2), before the inherited duplicate correction its conditional first moment is

`tau*eta*W_t*G_t/(At+O(1))^2`.                                  (4.1)

The inherited same-birth duplicate correction remains of the old forms because `c_tau<=2A+1`. In particular it is absorbed into

`C W_t^2/t^2 + C W_t/t^2`                                       (4.2)

with a changed finite constant.

Insert (2.10) into (4.1). On the finite-degree good event,

`E[Delta W_t^layer | F_t]
 >= tau*eta*(D_cap-epsilon)/A^2 * W_t/t
    -C W_t^2/t^2
    -C W_t Z_t/t^2
    -C W_t/t^2`.                                                 (4.3)

On the bad degree-count event, discard the layer entirely and keep the old process. Its probability is `O_epsilon(1/t)`. Since deterministically `W_t<=At+O(1)`, the loss from replacing `W_t 1_good` by `W_t` contributes only `O_epsilon(1/t)` after the `1/t` drift normalization.

Therefore the old `b13` recurrence gains the coefficient

`tau*eta*(D_cap-epsilon)/A^2`.                                   (4.4)

All inherited lower-order terms remain of the same types. Letting `epsilon downarrow0` after the standard normalized-product bootstrap gives

`gamma_E>=b13+tau*eta*D_cap/A^2=b14`.                            (4.5)

Strictness follows from `tau>0`, `eta>0`, and `D_cap>0`.

---

## 5. Upper drift and square budget

The layer cannot spend more than one extra cap unit per bridge target. Hence

`G_t<=sum_{u outside Q_t}w_u(t)<=At+O(1)`.                       (5.1)

Consequently the new direct first-moment upper drift is at most

`tau*eta/A * W_t/t + O(W_t/t^2)`.                               (5.2)

With `M12=1/2-U12` and the throttle (P.8),

`U14:=U12+tau*eta/A
 <=U12+M12/2
 <1/2`.                                                          (5.3)

For the square increment, `d(w)<=1`. Conditional on the current state, the extra bridge layer contributes at most a constant multiple of

`W_t/(At)^2 * sum_u w_u(t)^2`.                                   (5.4)

The inherited global bound is `E V_t=O(t)` for `V_t=sum_u w_u^2`, while deterministically `W_t=O(t)`. Thus the extra square forcing is `O(1)` after expectation. Cross terms with the old jump are absorbed by the same fixed-`m` Cauchy bound used in the previous artifacts. The usual recurrence therefore has coefficient `2U14<1` and yields again

`E W_t^2=O(t)`.                                                   (5.5)

This closes the only bootstrap obligation introduced by the new cap layer.

---

## 6. Exact `m=2, delta=1` orientation

This paragraph is orientation only; the theorem above is all-parameter. The previous run recorded

`b13 approximately 0.4602142844718363`,
`U12 approximately 0.4679953530177957`.

For `m=2,delta=1`, the exact checker gives `D_cap=98304/96577`. The cap throttle is actually inactive (`tau=1`); substituting the exact `pi_c` gives the additional exponent gain

`eta D_cap/A^2 approximately 0.00017137829`,

so

`b14 approximately 0.46038566276`.

These decimals are not used anywhere in the proof.

---

## 7. Scope and next obstruction

This theorem is a strict source-relevant movement, but it is still far from the source-level critical-window statement. It proves neither a matching `1/2` upper/lower exponent nor the logarithmic correction.

The local killed-PPT theorem from the preceding run remains the deeper route: it identifies a `(log n)^(-2)` spectral crossing and an oldest-boundary Green mass `sqrt(n)/log n`. The present cap-layer theorem shows that the finite exploration still had unused first-order tail mass even before a full local-to-finite transfer.

The next structurally different target should therefore be a **fixed-width Perron-weighted age/type slab inequality** for the actual finite graph. The aim is to replace scalar cap improvements by a finite-dimensional drift matrix whose Perron exponent approaches `1/2` as the slab width is widened after `n->infinity`. A valid theorem must keep the slab width fixed while proving the finite-graph recurrence; only afterward may the width grow. That ordering avoids pretending that local weak convergence is uniform to the `sqrt(n)/log n` component scale.

---

## 8. Validation status

The all-parameter theorem is proved on the page above. The finite `m=2,delta=1` arithmetic is independently executable and exact, but it is only a specialization check, not a substitute for the proof. This is a **self-check**, not either of the two independent outside audits required for source closure.

No source closure is claimed. Status remains **PARTIAL / SOURCE OPEN**.
