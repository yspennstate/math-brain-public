Model actually run: **GPT-5.6 Sol. Reasoning level: UNVERIFIED. This is not GPT-6 at maximum.**

**NO SOURCE-LEVEL COEFFICIENT-METRIC MOVEMENT; NEW FIRST-CORRECTION THEOREM.** The saturated frontiers remain `c_LK^cert=a_LK^fine=b_LK^sqrt=0`; HARD recoveries remain `0/2`. This run uses fresh Section-B methods **#6 DEFORM TO A POINT YOU CAN SOLVE, #16 COMPUTE EVERY SMALL CASE AND STARE AT THE SEQUENCE, #30 DO ONE SCALE / ONE DIRECTION AT A TIME**. The substantive advance is that Claim 297's direct-tilt exponent is not merely an upper-bound proof exponent: at the critical window it is the true leading exponent of the clean one-root correction, with an explicit Laplace prefactor. The one-root clean correction is then shown to dominate sparse internal-edge, pair-interaction, and size-two-component corrections. A quantitative component recheck is strong enough to transfer the correction to connectivity.

# P03 / P0456 run report — one-defect deformation, exact Gamma checker, and first critical-window correction

Run timestamp: **2026-09-18T22:28:49Z**  
Track: **P03**  
Canonical target: **P0456**  
Repository / branch: `yspennstate/math-open-problems` / `master`  
Category: **HARD OUTSIDE**

---

## 1. Continuity, source status, repository screen, and audit gate

The exclusive assignment remains

`operations/claims/P0456.md`,

creation commit `9d9c9545783bf8ae09805830d72f5d935be9afb1`, blob `74b9c5ebda19b1ded526457c1c7ea12654419bcb`.

The newest complete P03 report entering this invocation was

`proofnet24/P03-fei/runs/2026-09-18/2026-09-18T21-28-15Z__p0456-direct-tilt-asymmetric-poisson-band.md`,

creation commit `06736e4dcff7e30b7b5b4cec235e8cc3df538d04`, blob `2f21e006ee9d07dcc4dd383e5bb7d7daf7214573`; exact-commit readback had recovered `**End of complete run report.**`.

I preserve Claims 274, 276, 278, 280, 282, 284, 286 and the candidate-complete/supporting chain 288--297.

This invocation reread/recovered root `README.md`, `proofnet24/HOURLY_PROTOCOL_2026-09-15.md`, current `FLEET_RULES.md`, `operations/new_methods_2026-09-16/OWNER_DIRECTIVE.md`, campaign `probability_campaign_2026_09/INDEX.md` and `RANKING.md`, root `POSTED.md`, the canonical P0456 claim, the newest P03 report, current P26 evidence, and neighboring P0457 only for nonduplication. Large connector-rendered policy/campaign surfaces can truncate and are not represented here as byte-for-byte rereads; exact-path reads controlled every mathematical dependency used below. P0457 remains a distinct diameter target and is not resumed.

### Fresh primary-source / prior-art verification

The primary source remains Hossein Dabirian and Vijay Subramanian, *Connectivity of a family of bilateral preference random graphs*, *Journal of Applied Probability* 63(2) (June 2026), 552--579, DOI `10.1017/jpr.2025.10051`, published online 18 December 2025.

Fresh Cambridge retrieval on 18 September 2026 rechecked the literal model and source theorem chain. Theorem 3 gives disconnection for

`k <= log n + t' loglog n sqrt(log n)` with fixed `t'<-1/2`,

Theorem 6 gives connectivity for the same scale with fixed `t'>1/2`, and Lemma 10 gives the source bad-interaction bound `P(B)=O(k^3/n)`. Section 1.1 still identifies the displayed coefficient band as unresolved and attributes the gap to analytically simpler sufficient conditions.

Fresh bounded web searches for the title/DOI/authors, `LK(n,k) Poisson isolated vertices`, `LK(n,k) log n+c connectivity`, `bilateral preference Poisson`, and the direct-tilt constant below found the Cambridge source and adjacent material but no later source-matching critical-window or first-correction theorem. This is dated bounded negative evidence only; **publication novelty remains UNVERIFIED**.

### Fresh outside-audit screen

Repository-wide searches for `P0456`, exact Claim-288/289/297 identifiers, `audit`, and `PASS` still find no P26 or distinct OTHER-track full-chain audit of the source-matching proof. The newest concrete P26 report recovered is

`proofnet24/P26-proof-audit-recovery/runs/2026-09-19/2026-09-19_00-57-29__run-report.md`,

which audits historical P04/I0101 Claim 15 and not P0456. P04 remains rotation-stopped with no genuinely new theorem for the directed P03->P04 duty. Therefore no repeated peer audit is fabricated.

The closure gate remains

`P0456_ACTIVE_AUDIT_PENDING / OUTSIDE_AUDITS_FOUND_0_OF_2`.

Self-audits do not count. No final paper folder is created.

---

## 2. Preserved chain and new theorem

The source-matching candidate-complete chain remains:

- `P03-P0456-POISSON-CRITICAL-WINDOW-288 = PROVED / SOURCE-MATCHING-CANDIDATE-COMPLETE / AUDITS-PENDING / PUBLICATION-NOVELTY-UNVERIFIED`;
- `P03-P0456-UNIFORM-POISSON-INTERACTION-REPAIR-289 = PROVED / SELF-AUDIT-REPAIR / SOURCE-MATCHING-STRENGTHENING / AUDITS-PENDING / PUBLICATION-NOVELTY-UNVERIFIED`;
- Claim 290 is the marked isolated-vertex PPP cross-check;
- Claims 291--297 are supporting P03 self-audit/strengthening kernels.

This run adds:

### Claim `P03-P0456-FIRST-CORRECTION-LAPLACE-298`

**Status:** `PROVED / SELF-AUDIT-STRENGTHENING / SUPPORTING / AUDITS-PENDING / PUBLICATION-NOVELTY-UNVERIFIED`.

Define

`eta := sqrt(2)-1-log((1+sqrt(2))/2)
      = 0.2259871559134973329...`,                              (2.1)

and

`C_* := (1+sqrt(2))/sqrt(2 pi (2-sqrt(2)))
      = 1.2583924237283632381...`.                             (2.2)

Let `k=k_n` be integer with

`k-log n -> c in R`,                                          (2.3)

and write

`lambda_n=n e^{-k}`,

`eps_n=k^{-1/2} e^{-eta k}`.                                  (2.4)

Then for every fixed vertex `v`,

`P(I_v)
 =e^{-k}[1+C_* eps_n+o(eps_n)].`                              (2.5)

Consequently, for `Z_n=sum_v I_v`,

`mu_n:=E Z_n
 =lambda_n[1+C_* eps_n+o(eps_n)].`                            (2.6)

Moreover the size-bias/Palm coupling of Claims 293--294 is quantitatively smaller than this correction:

`d_TV(Law(Z_n),Poisson(mu_n))=o(eps_n).`                      (2.7)

Finally the probability of a nontrivial connected component is also `o(eps_n)`, and therefore

`P(LK(n,k) connected)
 = exp(-lambda_n)
   [1-lambda_n C_* eps_n+o(eps_n)].`                           (2.8)

Thus at the true `O(1)` critical window the first proved correction is generated by the **clean one-root beta-saddle defect**. The sparse internal-edge correction, pair-interaction correction, and size-two-component correction are all strictly smaller, of order `n^{-1+o(1)}` (up to powers of `log n`) rather than `n^{-eta}/sqrt(log n)`.

Equation (2.8) is a supporting asymptotic refinement of the source-matching candidate theorem, not a protocol closure. No publication-priority claim is made.

---

## 3. #6 DEFORM TO A POINT YOU CAN SOLVE — the one-defect model

Start from the clean one-root integral used in Claims 288/297. In the notation of those reports,

`M_{k,k}=C_{n,k} int_0^1 Q_k(x)^k (1-x)^(m-k-1) dx`,          (3.1)

where

`m=n+O(1)`, `N=n+O(k)`,

`B_k~Beta(k,N-k+1)`,

`beta=E B_k=k/(N+1)`,

`Q_k(x)=E[(x-B_k)_+]`,                                        (3.2)

and

`C_{n,k}=(m)_{k+1}/k!`.

The mean-replacement integral is

`M_0
 =C_{n,k} int_beta^1 (x-beta)^k(1-x)^(m-k-1)dx
 =(1-beta)^m
 =e^{-k}[1+O(k^2/n)].`                                       (3.3)

Normalize its integrand into the probability law `nu_{n,k}` on `[beta,1]`:

`dnu(x)
 =[C_{n,k}/M_0](x-beta)^k(1-x)^(m-k-1)dx`.                   (3.4)

Then `z=(x-beta)/(1-beta)` is exactly `Beta(k+1,m-k)` under `nu`.

For `x>=beta` put

`a=x-beta`,

`R(x)=E[(B_k-x)_+]`,                                          (3.5)

so `Q_k(x)=a+R(x)`. Therefore

`M_+/M_0=E_nu[(1+R(X)/(X-beta))^k].`                          (3.6)

The region `x<beta` contributes only

`exp[-(1/2+o(1))k log k] M_0`,                                (3.7)

because `Q_k(beta)=O(sqrt(k)/N)` whereas the saddle has `x-beta~k/N`. Hence it is negligible on the scale sought below.

The deformation is to retain **exactly one** overshoot defect in (3.6). Put

`r(x)=R(x)/(x-beta)`,

`D_{1,n}:=E_nu[k r(X)].`                                     (3.8)

The theorem will follow once we compute `D_{1,n}` sharply and prove every term with two or more defects is exponentially smaller.

### 3.1 Beta-to-Gamma scaling

At the critical window `k=log n+O(1)`, `k^2/n=o(1)`. Uniformly for `y` in a fixed compact positive multiple of `k`, the density of

`Y_n:=N B_k`

satisfies

`f_{Y_n}(y)
 =[1+o(1)] y^{k-1}e^{-y}/Gamma(k)`.                           (3.9)

This follows directly from the beta density by expanding the falling-factorial normalizer and `log(1-y/N)`; the total logarithmic error is `O(k^2/n)`.

Similarly, under `nu`, with

`W_n:=N(X-beta)`,

its density on compact positive multiples of `k` is

`[1+o(1)] w^k e^{-w}/Gamma(k+1)`.                             (3.10)

Thus the first-defect asymptotic is governed by independent Gamma limits

`Y~Gamma(k,1)`,

`W~Gamma(k+1,1)`.                                             (3.11)

Writing `t=W/k`, the threshold in the overshoot is

`N X=N beta+W=k+W+o(1)=(1+t)k+o(1)`.                         (3.12)

Therefore the limiting one-defect integrand is

`A_k:=E[(k/W)(Y-k-W)_+].`                                    (3.13)

The finite-`n` first-defect term satisfies

`D_{1,n}=A_k[1+o(1)]`.                                       (3.14)

All `o(1)` terms here are relative on a fixed neighborhood of the dominant saddle; outside that neighborhood the large-deviation estimates below dominate.

---

## 4. #30 ONE SCALE / ONE DIRECTION — exact Laplace asymptotic

Let

`gamma(t)=t-log(1+t)`,

`delta(t)=t-1-log t`,

`F(t)=gamma(t)+delta(t)`.                                     (4.1)

These are the same rates discovered as upper bounds in Claim 297. We now obtain the matching first-order asymptotic.

### 4.1 Overshoot prefactor

Fix `t` in a compact subset of `(0,infinity)` and put `s=1+t`. For `Y~Gamma(k,1)`, let

`H_k(t)=E[(Y-sk)_+]`.                                         (4.2)

Its density at the boundary is, by Stirling,

`f_Y(sk)
 =[1+o(1)] [1/(s sqrt(2 pi k))] exp[-k gamma(t)].`             (4.3)

For bounded `z>=0`,

`f_Y(sk+z)/f_Y(sk)
 -> exp[-(t/s)z]`.                                            (4.4)

The ratio is uniformly dominated by an exponential on compact `t`-sets, so Watson's boundary lemma (or direct dominated convergence after splitting at `z=k^{1/3}`) gives

`H_k(t)
 =[1+o(1)] f_Y(sk) int_0^infty z exp[-(t/s)z] dz
 =[1+o(1)]
   [s/(t^2 sqrt(2 pi k))] exp[-k gamma(t)].`                  (4.5)

Because `W=kt`,

`(k/W)H_k(t)
 =[1+o(1)]
   [s/(t^3 sqrt(2 pi k))] exp[-k gamma(t)].`                  (4.6)

### 4.2 Saddle density

For `W~Gamma(k+1,1)`, the density of `t=W/k` is

`p_k(t)
 =[1+o(1)] sqrt(k/(2 pi)) exp[-k delta(t)]`                   (4.7)

uniformly on compact positive `t`-sets.

Multiplying (4.6) and (4.7),

`A_k
 =[1+o(1)] int_0^infty
   [(1+t)/(2 pi t^3)] exp[-k F(t)] dt`,                        (4.8)

with the tails controlled by the same Chernoff/saddle bounds as Claim 297. In particular `t<k^{-1/4}` is superexponentially small on the `k` scale and large fixed `t` has strictly larger `F`.

### 4.3 Unique dominant point and prefactor

We have

`F(t)=2t-1-log(t(1+t))`,

`F'(t)=2-1/t-1/(1+t)`,

`F''(t)=1/t^2+1/(1+t)^2>0`.                                  (4.9)

Thus the unique minimizer is

`t_*=1/sqrt(2)`.                                               (4.10)

At this point

`F(t_*)=eta`,

`F''(t_*)=4(2-sqrt(2))`,                                      (4.11)

and

`(1+t_*)/(2 pi t_*^3)=(1+sqrt(2))/pi`.                        (4.12)

Laplace's method applied to (4.8) gives

`A_k
 = C_* k^{-1/2} e^{-eta k}[1+o(1)]`,                        (4.13)

with `C_*` exactly as in (2.2).

This proves the matching lower and upper asymptotic for the one-defect deformation and shows that Claim 297's direct-tilt exponent is genuinely attained.

---

## 5. Multiple defects are exponentially smaller

On the central region, put

`u(x)=k r(x)`.

Then `u(x)` is exponentially small and

`(1+r)^k=1+u+O(u^2 e^u)`.                                    (5.1)

The first term averages to `D_{1,n}`. The quadratic remainder pays large-deviation rate

`F_2(t):=delta(t)+2 gamma(t)`.                                 (5.2)

Since `gamma(t)>=0`, every term of order at least two is bounded by the `F_2` scale. The unique minimizer of `F_2` solves

`3-1/t-2/(1+t)=0`,

hence `t=1/sqrt(3)`, and

`min F_2=0.36986... > eta`.                                   (5.3)

The small-`t` and large-`t` tails are still smaller. Therefore

`E_nu[(1+r(X))^k]
 =1+D_{1,n}+o(k^{-1/2}e^{-eta k}).`                           (5.4)

Combining (3.3), (3.7), (3.14), and (4.13),

`M_{k,k}
 =e^{-k}[1+C_* k^{-1/2}e^{-eta k}
          +o(k^{-1/2}e^{-eta k})].`                           (5.5)

The sparse internal-edge correction isolated in Claims 286/288/294 is

`e^{-k} n^{-1+o(1)}`,                                        (5.6)

uniformly at `k=log n+O(1)`. Since `eta<1`, (5.6) is `o(e^{-k}eps_n)`. Hence exact isolation has the same first correction, proving (2.5).

---

## 6. #16 exact finite representation and checker

The auxiliary Gamma one-defect model (3.13) has an exact finite expression for every integer `k>=1`; this gives a useful independent check of the prefactor calculation.

For `Y~Gamma(k,1)` and `a>=0`, integer-shape incomplete-gamma identities give

`E[(Y-a)_+]
 =e^{-a}[k sum_{j=0}^k a^j/j!
          -a sum_{j=0}^{k-1} a^j/j!].`                       (6.1)

Taking `a=k+w` simplifies the bracket to

`-w sum_{j=0}^{k-1}(k+w)^j/j!
 +(k+w)^k/(k-1)!`.                                            (6.2)

Since `W~Gamma(k+1,1)`, integrating term by term yields

`A_k=e^{-k} B_k`,                                             (6.3)

where the following number is exactly rational:

`B_k=
 (k/k!) [
  (1/(k-1)!) sum_{ell=0}^k
   C(k,ell) k^(k-ell) (k+ell-1)! / 2^(k+ell)
  - sum_{j=0}^{k-1}(1/j!) sum_{ell=0}^j
   C(j,ell) k^(j-ell) (k+ell)! / 2^(k+ell+1)
 ].`                                                          (6.4)

The exact checker constructs (6.4) in two independent `Fraction` forms: once as the displayed double sum and once by explicitly constructing the polynomial (6.2) and integrating every monomial. It asserts equality for `k=1,...,30`.

Artifact:

`proofnet24/P03-fei/artifacts/2026-09-18/2026-09-18T22-28-49Z__first_correction_gamma_checker.py`

creation commit `cfb9da671e9a71cf369362bf8c6d7a930eb95f47`, blob `09fadb3bf427bfc53251899425a798f2b469ce00`.

Archived output:

`proofnet24/P03-fei/artifacts/2026-09-18/2026-09-18T22-28-49Z__first_correction_gamma_checker.out`

creation commit `c488781b89e30bc9e993ba8b403c9eaf2acfaace`, blob `c66a19f0da1a89d35c32a9493d955d84e2abb257`.

The exact output begins `EXACT_IDENTITY_PASS k=1..30`. The floating diagnostics

`sqrt(k) exp(eta k) A_k`

increase through

`0.803950...` at `k=10`,
`1.085005...` at `k=40`,
`1.162247...` at `k=80`,
`1.217090...` at `k=200`,

consistent with the proved limit `C_*=1.258392...`. The decimals are diagnostics only; the theorem is the analytic Laplace proof above.

---

## 7. #30 correction hierarchy at `k=log n+c`

Keep the four mechanisms separate.

### 7.1 Clean one-root saddle defect

By (2.5), its relative size is

`C_* eps_n
 =C_* k^{-1/2}e^{-eta k}
 =n^{-eta+o(1)}`.                                             (7.1)

### 7.2 Sparse internal selected-neighbor edges

Claims 286/288/294 give relative correction

`n^{-1+o(1)}`.                                                (7.2)

This is strictly smaller than (7.1).

### 7.3 Pair/fixed-root interaction

Claims 292--294 show collision/active-edge interaction complexity has at least one factor `n^{-1+o(1)}`. The size-bias coupling sharpened this to

`d_TV(Law(Z_n),Poisson(mu_n))=n^{-1+o(1)}`                    (7.3)

at the critical window. Again this is strictly smaller than (7.1).

### 7.4 Size-two components

The external-proposal/spanning-tree argument of Claim 291 gives, for a fixed `r`,

`P(exists an r-component)=n^{1-r+o(1)} poly(k)`.               (7.4)

For `r=2` this is `n^{-1+o(1)}`, hence smaller than (7.1). The same proof works verbatim for every fixed `r` because the proposal defect `r-1` is fixed.

Therefore the clean one-root saddle correction is the first nonzero term among these four mechanisms.

---

## 8. Quantitative nontrivial-component bound at the correction scale

To transfer the correction from `P(Z_n=0)` to connectivity, an `o(1)` component bound is not enough; we need `o(eps_n)`. I rechecked the component argument with constants chosen for this scale.

Use the Exp(1)-score representation of Claims 278/280 and put

`m_n=log((n-1)/k)`,

`C=log 10`.                                                   (8.1)

Let `A` be the event that every vertex's kth-largest incident score lies in `(m_n-C,m_n+C)`.

At the upper threshold, the number of incident scores above `m_n+C` has mean `(1/10+o(1))k`. Chernoff gives

`P(Bin >=k)
 <=exp[-(log 10-0.9+o(1))k]`.                                 (8.2)

After a union bound over `n` vertices and `k=log n+O(1)`,

`P(A^c)<=n^{-(log 10-1.9)+o(1)}
       =n^{-0.402585...+o(1)}
       =o(eps_n).`                                            (8.3)

The lower-threshold failure, where a mean-`10k` binomial has fewer than `k` successes, has a much larger Chernoff exponent and is negligible relative to (8.3).

On `A`, a spanning-tree edge needed by a component has score above `m_n-C`, hence probability at most

`p_tree=10k/(n-1)`,                                           (8.4)

while every crossing edge must have score below `m_n+C`, with

`p_cross=k/[10(n-1)]`.                                       (8.5)

For fixed sizes `2<=r<=12`, use Claim 291's external-proposal proof rather than only the crossing envelope. Each vertex has `k-(r-1)` external proposals among its global first `k`, and all must be rejected outside the candidate component. The bounded-omission saddle and fixed-r interaction graph give rejection cost `e^{-rk+o(k)}`. Summing over labeled sets and Cayley trees gives

`P(exists an r-component, A)
 <= n^{1-r+o(1)} poly(k)`.                                    (8.6)

Thus the whole fixed-size range `2,...,12` is `n^{-1+o(1)}=o(eps_n)`.

For `13<=r<=24`, the simpler Cayley/crossing bound gives

`P(exists an r-component,A)
 <= C(n,r) r^{r-2} p_tree^{r-1}
    (1-p_cross)^{r(n-r)}
 <= n^{1-r/10+o(1)}.                                         (8.7)

The worst case is `r=13`, namely `n^{-0.3+o(1)}=o(eps_n)`.

For `25<=r<=n/2`, use `n-r>=(n-1)/2` and `C(n,r)<=(en/r)^r`. Then

`P(exists an r-component,A)
 <= n e^r r^{-2}(10k)^{r-1} exp[-rk/20].`                     (8.8)

The first term `r=25` is `n^{-0.25+o(1)}`, and the ratio of successive upper bounds is `n^{-1/20+o(1)}`. Hence

`sum_{r=25}^{n/2} P(exists r-component,A)
 <=n^{-0.25+o(1)}
 =o(eps_n)`,                                                  (8.9)

because `0.25>eta=0.225987...`.

Combining (8.3), (8.6), (8.7), and (8.9),

`P(exists a nontrivial component)=o(eps_n).`                  (8.10)

This is the quantitative patch needed for the connectivity correction.

---

## 9. Poisson and connectivity first correction

From Claim 294's exact size-bias coupling,

`d_TV(Law(Z_n),Poisson(mu_n))=n^{-1+o(1)}=o(eps_n).`          (9.1)

By (2.6),

`mu_n-lambda_n
 =lambda_n C_* eps_n+o(eps_n)`.                               (9.2)

Therefore

`P(Z_n=0)
 =e^{-mu_n}+o(eps_n)
 =e^{-lambda_n}
  [1-lambda_n C_* eps_n+o(eps_n)].`                           (9.3)

A graph with no isolated vertices is disconnected only if it has a nontrivial component. Equation (8.10) is `o(eps_n)`, so subtracting that event from (9.3) proves (2.8).

At `k-log n->c`, `lambda_n->e^{-c}` and

`eps_n
 =k^{-1/2}n^{-eta}e^{-eta c}[1+o(1)]`.                        (9.4)

Thus the correction to the limiting Gumbel-form connectivity law has an explicit sign and coefficient: isolation is slightly more likely than the zeroth-order `e^{-k}` law, so connectivity is slightly less likely than `exp(-lambda_n)` by the amount in (2.8).

---

## 10. Adversarial self-audit of Claim 297 / 298

The four audit targets named by the preceding run were checked explicitly.

1. **Overshoot near `t=k^{-1/4}`.** This region is not part of the Laplace saddle: `delta(t)=(1/4)log k+O(1)`, so the `nu` mass is `exp[-(1/4+o(1))k log k]`. It is superexponentially smaller than `e^{-eta k}`.
2. **Saddle-density `o(k)` uniformity.** On the only relevant compact neighborhood of `t_*=1/sqrt(2)`, beta-to-Gamma log-density errors are `O(k^2/n)=o(1)`, so they are `o(1)` multiplicatively and cannot alter the prefactor.
3. **Internal-edge correction.** The retained sparse-interaction estimate is `e^{-k}n^{-1+o(1)}` at `k=log n+O(1)`, which is `o(e^{-k}eps_n)` since `eta<1`.
4. **Upper monotonicity patch.** The Cambridge source Theorem 6 is literal connectivity whp above its displayed upper window; `LK(n,k)` is monotone increasing in `k` under the natural common-weight coupling. Claim 297's unrestricted upper side therefore remains valid.

No contradiction was found. The new first-correction theorem is stronger than Claim 297 at the critical scale but remains a P03 self-audit, not an outside audit.

---

## 11. Peer audit duty

Directed P03->P04 second-audit duty remains active in principle, but the newest P04 records remain rotation-stop/readback records and create no new mathematical theorem beyond the long list already P03-audited. I therefore do not fabricate or repeat an audit.

---

## 12. Metric / stuck / recovery state

All admitted coefficient metrics are already at their mathematical minimum:

- `c_LK^cert=0` at `sqrt(log n) loglog n`;
- `a_LK^fine=0` at `sqrt(log n loglog n)`;
- `b_LK^sqrt=0` at `sqrt(log n)`.

They remain **SATURATED**, so none contributes an unchanged/stuck count. Claim 298 is a limiting-law refinement, not a new smaller coefficient metric. HARD recoveries remain `0/2`.

---

## 13. Exact remaining obligations and next attack

Protocol closure is still blocked only by independent audits and publication-novelty verification of the source-matching chain, not by the existence of a candidate mathematical answer.

Exact obligations:

1. P26 must perform an independent full-proof audit of Claims 288/289, using 291--298 as optional audit kernels rather than as receipts.
2. One distinct OTHER track must independently audit the full source-matching chain.
3. Prior-art remains a dated bounded negative search; publication novelty is UNVERIFIED.
4. The exact second correction is still open. Claim 298 identifies the first correction and its prefactor; the next term could come from the second clean defect (`min(delta+2gamma)`), the `1/k` expansion of the first-defect Laplace prefactor, or the finite-`n` `n^{-1}` mechanisms, depending on scale.

Fresh Section-B methods reserved for the next mathematical run if audits have not arrived: **#17 LOOK FOR YOUR NUMBERS SOMEWHERE ELSE, #14 EXACT FINITE REDUCTION, #3 PROVE SOMETHING STRONGER**. The natural target is an Edgeworth/Laplace second term for the one-defect integral and a comparison with the `n^{-1}` interaction layer; do not re-optimize the already-saturated connectivity window.

---

## 14. `ledger_delta` for P26 only

```yaml
ledger_delta:
  track: P03
  target: P0456
  action: preserve_active_audit_pending
  metric:
    c_LK_cert: 0
    a_LK_fine: 0
    b_LK_sqrt: 0
    saturated: true
    unchanged_count_increment: 0
    recoveries_used: 0/2
  new_claim:
    id: P03-P0456-FIRST-CORRECTION-LAPLACE-298
    status: PROVED / SELF-AUDIT-STRENGTHENING / SUPPORTING / AUDITS-PENDING / PUBLICATION-NOVELTY-UNVERIFIED
    statement: >-
      If k-log n -> c, with eta=sqrt(2)-1-log((1+sqrt(2))/2),
      C_*=(1+sqrt(2))/sqrt(2*pi*(2-sqrt(2))), eps_n=k^-1/2 exp(-eta k),
      then P(I_v)=exp(-k)(1+C_* eps_n+o(eps_n)) and
      P(connectivity)=exp(-n exp(-k))(1-n exp(-k) C_* eps_n+o(eps_n)).
  preserved_claims:
    - P03-P0456-POISSON-CRITICAL-WINDOW-288
    - P03-P0456-UNIFORM-POISSON-INTERACTION-REPAIR-289
    - P03-P0456-MARKED-POISSON-CROSSCHECK-290
    - P03-P0456-PAIR-SMALLCOMP-AUDIT-KERNEL-291
    - P03-P0456-FINITE-PALM-INTERACTION-GRAPH-292
    - P03-P0456-LOCALBLOCK-SIZEBIAS-STEIN-293
    - P03-P0456-RANK-PALM-SUBLINEAR-WINDOW-294
    - P03-P0456-FIXED-FRACTION-POISSON-BAND-295
    - P03-P0456-OPTIMIZED-SADDLE-FRACTION-BAND-296
    - P03-P0456-DIRECT-TILT-ASYMMETRIC-POISSON-297
  audit_gate:
    independent_passes_found: 0/2
    source_closed: false
  exact_artifacts:
    checker_creation_commit: cfb9da671e9a71cf369362bf8c6d7a930eb95f47
    checker_blob: 09fadb3bf427bfc53251899425a798f2b469ce00
    output_creation_commit: c488781b89e30bc9e993ba8b403c9eaf2acfaace
    output_blob: c66a19f0da1a89d35c32a9493d955d84e2abb257
  publication_novelty: UNVERIFIED
  next_state: P0456_ACTIVE_AUDIT_PENDING / CLAIM_298_FIRST_CORRECTION_AUDIT_KERNEL_READY
```

**End of complete run report.**
