Model actually run: **GPT-5.6 Sol. Reasoning level: UNVERIFIED. This is not GPT-6 at maximum.**

**NO SOURCE-LEVEL COEFFICIENT-METRIC MOVEMENT; NEW DIRECT-TILT / ASYMMETRIC POISSON STRENGTHENING.** The saturated frontiers remain `c_LK^cert=a_LK^fine=b_LK^sqrt=0`; HARD recoveries remain `0/2`. This run uses fresh Section-B methods **#9 RANDOMIZE, #12 FIND WHAT IS CONSERVED, #15 BREAK THE SYMMETRY ON PURPOSE**. The substantive advance is a direct change-of-measure estimate for the exact one-root marked integral: instead of splitting the saddle and taking the worse of two exponents, it integrates the beta-tail defect against the saddle large-deviation density and therefore adds the two rates. This enlarges the rigorously certified lower fixed-fraction Poisson band and removes any fixed-fraction restriction on the upper side by combining the central theorem with the published monotone connectivity theorem.

# P03 / P0456 run report — direct exponential tilt, likelihood-ratio martingale, and asymmetric Poisson band

Run timestamp: **2026-09-18T21:28:15Z**  
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

`proofnet24/P03-fei/runs/2026-09-18/2026-09-18T20-34-28Z__p0456-optimized-saddle-fraction-band.md`,

creation commit `690ee0e87e631eed7adcce61d92546a1050cff9c`, blob `a9e4ec988683f13e6084ba76edce764e5aac4fa0`; exact-commit readback had recovered `**End of complete run report.**`.

I preserve Claims 274, 276, 278, 280, 282, 284, 286 and the candidate-complete/supporting chain 288--296.

This invocation reread/recovered root `README.md`, `proofnet24/HOURLY_PROTOCOL_2026-09-15.md`, current `FLEET_RULES.md`, `operations/new_methods_2026-09-16/OWNER_DIRECTIVE.md`, campaign `probability_campaign_2026_09/INDEX.md` and `RANKING.md`, root `POSTED.md`, the canonical P0456 claim, the newest complete P03 report, current P26 evidence, and neighboring P0457 only for nonduplication. Large connector-rendered policy/campaign surfaces can truncate and are not represented here as byte-for-byte rereads; exact-path reads controlled every imported mathematical dependency used below. P0457 remains a distinct diameter problem and is not resumed.

### Fresh primary-source / prior-art verification

The primary source remains Hossein Dabirian and Vijay Subramanian, *Connectivity of a family of bilateral preference random graphs*, *Journal of Applied Probability* 63(2) (June 2026), 552--579, DOI `10.1017/jpr.2025.10051`, published online 18 December 2025.

Fresh Cambridge HTML retrieval on 18 September 2026 again recovered the exact source status. The paper states that Theorems 3 and 6 give disconnection for

`k <= log n + t' loglog n sqrt(log n)` with fixed `t'<-1/2`,

and connectivity for

`k >= log n + t' loglog n sqrt(log n)` with fixed `t'>1/2`.

Section 1.1 still says that connectivity is unknown in the displayed band with coefficients `-1/2` and `+1/2`, and attributes the gap to analytically simpler sufficient conditions. The source also explicitly defines the bilateral-preference model used here. Fresh bounded searches for the title/DOI/authors, `LK(n,k) Poisson isolated vertices`, `LK(n,k) log n+c connectivity`, and current bilateral-preference work again found the source and adjacent work but no later source-matching Poisson/constant-window theorem. Searches for the new direct-tilt constant below likewise found no source match. These are dated bounded negative searches only; **publication novelty remains UNVERIFIED**.

### Fresh outside-audit screen

A fresh repository commit/search screen after Claim 296 found no P26 or distinct OTHER-track full-chain audit of Claims 288/289. The newest concrete P26 work visible after the prior report continues auditing preserved P04/I0101 claims, not P0456. P04 remains rotation-stopped with no genuinely new theorem for the directed P03->P04 duty, so no repeat audit is fabricated.

Therefore the closure gate remains

`P0456_ACTIVE_AUDIT_PENDING / OUTSIDE_AUDITS_FOUND_0_OF_2`.

Self-audits do not count. No final paper folder is created.

---

## 2. Preserved chain and new theorem

The candidate-complete source-matching chain remains:

- `P03-P0456-POISSON-CRITICAL-WINDOW-288 = PROVED / SOURCE-MATCHING-CANDIDATE-COMPLETE / AUDITS-PENDING / PUBLICATION-NOVELTY-UNVERIFIED`;
- `P03-P0456-UNIFORM-POISSON-INTERACTION-REPAIR-289 = PROVED / SELF-AUDIT-REPAIR / SOURCE-MATCHING-STRENGTHENING / AUDITS-PENDING / PUBLICATION-NOVELTY-UNVERIFIED`;
- Claim 290 is the marked isolated-vertex PPP cross-check;
- Claims 291--296 are supporting P03 self-audit/strengthening kernels.

This run adds:

### Claim `P03-P0456-DIRECT-TILT-ASYMMETRIC-POISSON-297`

**Status:** `PROVED / SELF-AUDIT-STRENGTHENING / SUPPORTING / AUDITS-PENDING / PUBLICATION-NOVELTY-UNVERIFIED`.

Define, for `t>0`,

`gamma(t)=t-log(1+t)`,

`delta(t)=t-1-log t`,

and

`F(t)=gamma(t)+delta(t)=2t-1-log(t(1+t)).`                    (2.1)

Then `F` has a unique minimizer

`t_*=1/sqrt(2)`,                                                (2.2)

and

`eta_dir := min_{t>0} F(t)
          = sqrt(2)-1-log((1+sqrt(2))/2)
          = 0.225987155913497...`.                              (2.3)

Put

`alpha_dir := eta_dir/(1+eta_dir)
            = 0.184330769554524...`.                            (2.4)

Then for every fixed

`0<alpha_-<alpha_dir`,                                         (2.5)

uniformly over **all integers**

`(1-alpha_-) log n <= k <= n-1`,                               (2.6)

with `Z_n` the number of isolated vertices and

`lambda_n=n e^{-k}`,                                           (2.7)

we have

`d_TV(Law(Z_n),Poisson(lambda_n)) -> 0`,                       (2.8)

and

`P(LK(n,k) is connected)=exp(-lambda_n)+o(1)`.                (2.9)

Thus the proof is genuinely asymmetric: the lower side has the direct-tilt proof-route frontier `alpha_dir`, while the upper side has **no fixed-fraction cap at all**. This is because beyond an `o(log n)` upper neighborhood the published source connectivity theorem plus monotonicity already forces both `Z_n` and `Poisson(lambda_n)` to collapse to zero.

The constant `alpha_dir` is a proof-route constant only. It is not asserted to be a model threshold, a source constant, or a maximal range of some other method.

A clean exact corollary is the **18% lower band with unrestricted upper side**:

`0.82 log n <= k <= n-1`.                                      (2.10)

Indeed `eta_dir>9/40`. To certify that without floating point, put

`u=(sqrt(2)-1)/2`.

Since `0<u<1` and

`log(1+u) <= u-u^2/2+u^3/3`,

we get

`eta_dir >= 1/6+sqrt(2)/24 > 9/40`,                            (2.11)

where the last inequality is equivalent to `5 sqrt(2)>7`, whose square is `50>49`. Taking `eta=9/40` and `alpha_-=9/50` leaves the exact absolute-mean exponent margin

`eta(1-alpha_-)-alpha_- = 9/2000 > 0`.                         (2.12)

---

## 3. #9 RANDOMIZE — direct change of measure for the exact marked saddle

The central object from Claims 288/294/296 is the clean one-root marked probability

`M_{k,k}=C_{n,k} int_0^1 Q_k(x)^k (1-x)^(m-k-1) dx`,           (3.1)

where

`m=n+O(1)`, `N=n+O(k)`,

`B_k~Beta(k,N-k+1)`,

`beta=E B_k=k/(N+1)`,

`Q_k(x)=E[(x-B_k)_+]`,                                        (3.2)

and `C_{n,k}=(m)_{k+1}/k!`. The mean-replacement integral is

`M_0=C_{n,k} int_beta^1 (x-beta)^k (1-x)^(m-k-1) dx
    =(1-beta)^m
    =e^{-k}(1+O(k^2/n)).`                                     (3.3)

Claim 296 bounded the error by splitting at one `theta` and taking the worse of a beta-tail rate and a saddle-loss rate. The direct-tilt route instead makes the mean-replacement integrand a probability measure and averages the tail defect under it.

Define `nu_{n,k}` on `[beta,1]` by

`d nu(x)
 = [C_{n,k}/M_0]
   (x-beta)^k(1-x)^(m-k-1) dx`.                               (3.4)

After the affine change

`z=(x-beta)/(1-beta)`,                                         (3.5)

`z` is exactly `Beta(k+1,m-k)` under `nu`.

For `x>=beta`, put

`a=x-beta`,

`R(x)=E[(B_k-x)_+]`,                                          (3.6)

so that

`Q_k(x)=a+R(x)`.                                              (3.7)

Therefore the exact normalized correction on the upper side is the randomized likelihood ratio

`M_+/M_0
 = E_nu[(1+R(X)/(X-beta))^k]`.                              (3.8)

This is the useful change of category: the saddle error is no longer a worst-case pointwise defect. It is an expectation of a rare beta-tail tilt under the saddle law itself.

### 3.1 Beta-tail defect rate

Write

`t=N(x-beta)/k`.                                              (3.9)

Take first `t>=k^{-1/4}` and bounded above by a fixed constant. Then

`Nx=(1+t+o(1))k`.                                             (3.10)

The beta density is

`f(b)=k C(N,k)b^(k-1)(1-b)^(N-k)`.                            (3.11)

At `b=x`,

`f(x)=(k/x) P(Bin(N,x)=k)`.                                  (3.12)

The binomial lower-tail Chernoff estimate gives

`P(Bin(N,x)<=k)
 <= exp[-(gamma(t)+o(1))k]`,                                  (3.13)

with

`gamma(t)=t-log(1+t)`.                                       (3.14)

Moreover

`(log f)'(x)
 =(k-1)/x-(N-k)/(1-x)
 =-[t/(1+t)+o(1)]N`.                                         (3.15)

Hence after `x` the beta density decreases at exponential slope of order `tN`. Integrating that slope twice gives the overshoot estimate

`R(x)
 <= [poly(1+t,1/t)/N]
    exp[-(gamma(t)+o(1))k]`.                                  (3.16)

Consequently

`u(x):=kR(x)/(x-beta)
 <= poly(k,1/t)
    exp[-(gamma(t)+o(1))k]`.                                  (3.17)

For `t>=k^{-1/4}`, the right side tends to zero uniformly: near the lower endpoint `gamma(t)k~(1/2)sqrt(k)`, which dominates every polynomial factor. Thus

`(1+R/a)^k-1
 <= 2u(x)`                                                   (3.18)

for all large `n` on this region.

The same bound is even smaller for large fixed `t`; very large `t` can be discarded using the saddle tail below.

### 3.2 Saddle-law rate

Under `nu`, the variable `t=N(X-beta)/k` has, uniformly on compact subsets of `(0,infinity)`, density bounded by

`poly(k) exp[-(delta(t)+o(1))k]`,                              (3.19)

where

`delta(t)=t-1-log t`.                                         (3.20)

This is the standard beta/Gamma saddle rate: from (3.4), after inserting `x=beta+tk/N`, the log density relative to its mode `t=1` is

`k(log t+1-t)+o(k)=-k delta(t)+o(k)`.                          (3.21)

For `t<k^{-1/4}`, the saddle mass is superexponentially small on the `k` scale because `delta(t)=(1/4)log k+O(1)`. For `t` larger than any fixed `T`, `delta(t)` grows linearly, so choose `T` after the desired exponent and discard that tail as well.

### 3.3 The two rates add

Combining (3.18) with (3.19), and treating `t<k^{-1/4}` and `t>T` as just described,

`E_nu[(1+R/a)^k-1]
 <= poly(k)
    int exp[-k(delta(t)+gamma(t)-o(1))] dt
 = poly(k) exp[-(eta_dir-o(1))k]`,                             (3.22)

where

`eta_dir=min_{t>0} [delta(t)+gamma(t)]`.                       (3.23)

This is the key improvement over Claim 296: **the beta-tail defect and the saddle rarity occur simultaneously and their large-deviation costs add**. The two-region split paid only the smaller cost.

The region `x<beta` is superexponentially negligible. Indeed

`Q_k(beta)=E[(beta-B_k)_+]=O(sqrt(k)/N)`,                      (3.24)

while the dominant saddle scale has `x-beta~k/N`; taking the `k`th power therefore loses `k^{-k/2}` up to subexponential factors.

We conclude that for every fixed

`eta<eta_dir`,                                                (3.25)

uniformly on every compact positive ratio band

`c log n <= k <= C log n`,                                   (3.26)

`M_{k,k}
 =e^{-k}[1+O(poly(k)e^{-eta k})+O(k^2/n)].`                   (3.27)

The sparse internal-edge correction from Claims 286/288/294 is uniform on such bands, so exact isolation satisfies

`P(I_v)
 =e^{-k}[1+O(poly(k)e^{-eta k})+n^{-1+o(1)}].`                (3.28)

### 3.4 Optimization of the direct rate

By (2.1),

`F(t)=2t-1-log(t(1+t))`.                                      (3.29)

Then

`F'(t)=2-1/t-1/(1+t)`,                                       (3.30)

and

`F''(t)=1/t^2+1/(1+t)^2>0`.                                  (3.31)

Thus the unique minimizer solves

`2t(1+t)=1+2t`,

hence

`t_*=1/sqrt(2)`.                                              (3.32)

Substitution gives (2.3). This rate is materially larger than Claim 296's optimized split rate `0.12330156...` because it is a joint rate rather than a max-min split rate.

No matching lower bound for the actual correction is proved here, so `eta_dir` is an **upper-error exponent supplied by this proof**, not asserted to be the exact next-correction exponent.

---

## 4. From the direct one-root rate to the lower Poisson band

Fix `alpha_-<alpha_dir`. By (2.4),

`alpha_-/(1-alpha_-)<eta_dir`.                                (4.1)

Choose `eta` with

`alpha_-/(1-alpha_-)<eta<eta_dir`.                            (4.2)

For

`(1-alpha_-)log n <= k <= log n+o(log n)`,                    (4.3)

we have

`lambda_n=n e^{-k}<=n^{alpha_-}`.                             (4.4)

Equation (3.28) gives

`|nP(I_v)-lambda_n|
 <= n^{alpha_- - eta(1-alpha_-)+o(1)}
    +n^{alpha_--1+o(1)}
 =o(1).`                                                       (4.5)

The exact local-block Palm/size-bias coupling from Claims 293--295 and the rank-witness estimate of Claim 294 are uniform on every fixed compact `k/log n` band. Hence on the same lower range

`E|Z_n^s-(Z_n+1)|
 <= poly(k)e^{-k+o(k)}
 <= n^{-(1-alpha_-)+o(1)}
 =o(1).`                                                       (4.6)

The standard size-bias Stein inequality therefore gives

`d_TV(Law(Z_n),Poisson(E Z_n))->0`.                           (4.7)

Together with (4.5),

`d_TV(Law(Z_n),Poisson(lambda_n))->0`.                         (4.8)

This proves the lower side of Claim 297.

---

## 5. #12 FIND WHAT IS CONSERVED — the exact Palm likelihood-ratio martingale

The previous Palm proofs used local resampling. There is also an exact invariant under sequential revelation which makes clear what the Palm change of measure conserves.

Fix the root `V` and its top-`k` label set `S`. Let `D` be the root deadline vector. Reveal the selected-neighbour stars one at a time in root proposal order, and let `F_j` be the sigma-field generated by `S`, `D`, and the first `j` selected-neighbour stars. Put

`p_j=P(I_V=1 | F_j)`,

`p_0=P(I_V=1 | S,D)`,                                        (5.1)

and, on `p_0>0`,

`L_j=p_j/p_0`.                                                (5.2)

Then

`E[L_{j+1}|F_j]=L_j`,                                         (5.3)

so `(L_j)` is a nonnegative martingale. In particular

`E L_j=1`                                                     (5.4)

for every `j` after normalizing by the corresponding conditional initial probability.

More importantly, Bayes' rule gives the exact Palm Radon--Nikodym identity

`dP(. | I_V=1,S,D)/dP(. | S,D) |_F_j = L_j`.                 (5.5)

Thus the conserved quantity is the normalized conditional isolation likelihood. Sequential revelation does not change its mean; it merely redistributes the Palm tilt across the selected-neighbour stars.

This invariant is useful conceptually and as an audit device: any proposed constructive Palm surgery must reproduce the same `L_j` on every revealed sigma-field. It also explains why a naive coordinatewise deterministic surgery is not exact. However, no new quantitative Stein rate is claimed from (5.3) alone; `L_j` can have large pointwise spikes. The direct change-of-measure argument in Section 3 is what supplies the improved one-root exponent.

---

## 6. #15 BREAK THE SYMMETRY — the upper side has no fixed-fraction barrier

The symmetric band in Claims 295--296 hides a simple asymmetry.

Choose

`L_n=(log n)^(3/4)`.                                         (6.1)

### Central upper zone

For

`log n <= k <= log n+L_n`,                                   (6.2)

Claim 294 applies because `L_n=o(log n)`. Hence

`d_TV(Law(Z_n),Poisson(lambda_n))->0`                         (6.3)

and

`P(connected)=e^{-lambda_n}+o(1)`                            (6.4)

uniformly there.

### Far upper zone

For

`k>=log n+L_n`,                                               (6.5)

we have

`L_n/[sqrt(log n) loglog n] -> infinity`.                     (6.6)

Therefore the published source Theorem 6 applies already at a smaller sequence `k_0=log n+t' sqrt(log n)loglog n` for any fixed `t'>1/2`. Since the coupled graphs `LK(n,k)` are monotone increasing in `k`,

`sup_{k>=log n+L_n} P(LK(n,k) disconnected)->0`.              (6.7)

On the same range,

`lambda_n<=e^{-L_n}->0`.                                      (6.8)

Connectivity implies `Z_n=0`, so

`P(Z_n>0)<=P(disconnected)=o(1)`.                             (6.9)

Hence, uniformly for every `k>=log n+L_n` all the way to `n-1`,

`d_TV(Law(Z_n),Poisson(lambda_n))
 <= P(Z_n>0)+P(Poisson(lambda_n)>0)
 <= o(1)+lambda_n
 =o(1)`,                                                       (6.10)

and likewise

`|P(connected)-e^{-lambda_n}|
 <= P(disconnected)+(1-e^{-lambda_n})
 =o(1)`.                                                       (6.11)

Thus there is no reason to impose a fixed upper fraction at all.

### Lower connectivity flank

For completeness, the lower connectivity formula on the part of (2.6) lying outside the central `L_n` zone does not require a new component enumeration. The published source Theorem 3 gives disconnection whp once

`k<=log n-L_n`,                                               (6.12)

because `L_n` is much larger than the source's `sqrt(log n)loglog n` scale. Meanwhile

`lambda_n>=e^{L_n}->infinity`,                                (6.13)

so `e^{-lambda_n}->0`. In the central zone Claim 294 already supplies the full connectivity formula. This completes (2.9) uniformly on the entire asymmetric range (2.6), without any mean-degree inference.

---

## 7. First-correction check and failed routes

### 7.1 What the direct tilt does and does not prove

The direct tilt gives the rigorous relative-error **upper bound**

`poly(k)e^{-(eta_dir-o(1))k}`                                 (7.1)

for the clean marked saddle. It does not prove a matching lower bound for the correction and therefore does not identify the exact first correction coefficient or exact correction exponent. The previous search for an `O(1)` correction after multiplication by the critical intensity remains negative: one-root, pair-interaction, and size-two-component corrections all vanish at the `k=log n+O(1)` scale under the proved bounds.

### 7.2 Martingale route does not replace quantitative coupling

The exact martingale (5.2) is a true conserved quantity, but it does not control the maximum or quadratic variation sharply enough by itself to yield a better Stein bound. This route is recorded as a structural success and a quantitative failure; no hidden concentration theorem is asserted.

### 7.3 Why another symmetric split was rejected

A further optimization of Claim 296's split could only improve decimals inside a weaker max-min mechanism. The direct-tilt argument instead changes the proof architecture and produces the sum-rate `delta+gamma`; this is why the present run does not report another local `theta` optimization.

---

## 8. Metric, stuck, peer-audit, and protocol state

All previously admitted fixed-coefficient metrics remain saturated:

- `c_LK^cert=0` at `sqrt(log n) loglog n`;
- `a_LK^fine=0` at `sqrt(log n loglog n)`;
- `b_LK^sqrt=0` at `sqrt(log n)`.

No saturated zero is counted as an unchanged stuck run. Claims 288--297 remain in audit/repair state. HARD recoveries remain `0/2`.

Supporting proof-route parameters now include

`eta_dir=0.225987155913497...`,

`alpha_dir=0.184330769554524...`,

but these are **not new source metrics** and are not threshold constants asserted by the paper.

Directed P03->P04 duty: the newest P04 records remain rotation-stop/readback records and create no new mathematical theorem. There is therefore no genuinely new accessible P04 claim to audit; no repeat audit is fabricated.

Outside closure audits for P0456: **0/2**. Self-audits 289--297 do not count.

Current state:

`P0456_ACTIVE_AUDIT_PENDING / OUTSIDE_AUDITS_FOUND_0_OF_2 / CLAIM_297_DIRECT_TILT_AUDIT_KERNEL_READY`.

---

## 9. Exact remaining obligations

The source-matching Claims 288/289 are candidate-complete but cannot be protocol-closed until:

1. P26 performs a genuine independent end-to-end proof audit of the source-matching chain;
2. one distinct OTHER track independently audits the same chain;
3. any objections are repaired mathematically;
4. prior-art status remains accurately bounded rather than promoted from search misses to novelty claims.

For Claim 297 specifically, the first outside-audit targets are:

- the uniform overshoot bound (3.16) when `t` approaches `k^{-1/4}`;
- the saddle-law density bound (3.19) and the exchange of the `t`-integral with the `o(k)` terms;
- the statement that the sparse internal-edge correction remains `n^{-1+o(1)}` relative uniformly on fixed compact `k/log n` bands;
- the upper-side monotonicity patch (6.7)--(6.10).

No final paper package is created before the required outside audits.

---

## 10. Next concrete attack

The next run should remain audit-first, but mathematically it should not re-optimize `eta_dir` by the same Laplace bound. Use a fresh Section-B triple, for example **#6 DEFORM TO A POINT YOU CAN SOLVE, #16 COMPUTE EVERY SMALL CASE AND STARE AT THE SEQUENCE, #30 DO ONE SCALE / ONE DIRECTION AT A TIME**.

Priority route:

1. Consume any incoming P26/OTHER-track audit first and repair exact objections.
2. Derive, if possible, an **exact first-order asymptotic** for `M_{k,k}/e^{-k}-1`, not only an exponential upper bound. The direct tilt identifies the candidate dominant defect scale near `t=1/sqrt(2)`; test whether a one-defect Laplace expansion yields a nonzero prefactor.
3. Separate the one-root clean-integral correction from the sparse internal-edge correction and determine which truly dominates near `k=log n+c`.
4. If an exact correction exists, propagate it to `E Z_n` and compare its scale against pair interactions and size-two components before claiming any refined connectivity law.
5. Do not spend another run enlarging a fixed-fraction band unless the exact correction analysis genuinely requires it.

---

## 11. `ledger_delta` for P26

```yaml
ledger_delta:
  track: P03
  target: P0456
  source_status: OPEN_IN_PUBLISHED_SECTION_1_1
  candidate_source_closure: AUDITS_PENDING
  new_claim:
    id: P03-P0456-DIRECT-TILT-ASYMMETRIC-POISSON-297
    status: PROVED_SELF_AUDIT_STRENGTHENING_SUPPORTING
    publication_novelty: UNVERIFIED
    statement: >-
      Let eta_dir=sqrt(2)-1-log((1+sqrt(2))/2) and
      alpha_dir=eta_dir/(1+eta_dir). For every fixed alpha_-<alpha_dir,
      uniformly over all integers (1-alpha_-)log n <= k <= n-1,
      with lambda_n=n e^-k, d_TV(Law(Z_n),Poisson(lambda_n))->0 and
      P(LK(n,k) connected)=exp(-lambda_n)+o(1).
  direct_tilt_rate:
    eta_dir: 0.225987155913497
    alpha_dir: 0.184330769554524
    clean_exact_corollary: "0.82 log n <= k <= n-1"
  mechanism: >-
    Normalize the mean-replacement beta saddle to a probability law nu.
    The defect likelihood has beta-tail cost gamma(t)=t-log(1+t), while
    nu has saddle cost delta(t)=t-1-log t. The costs add inside the
    expectation; min_t(gamma+delta) occurs at t=1/sqrt(2).
  conserved_object: >-
    Sequentially revealed isolated-root Palm likelihood ratio
    L_j=P(I_V|F_j)/P(I_V|initial) is a nonnegative mean-one martingale and
    is the exact RN derivative of the Palm law on F_j.
  asymmetric_upper_side: >-
    Central o(log n) zone uses Claim 294; beyond it the published source
    Theorem 6 plus monotonicity gives connectivity whp and lambda_n->0,
    so no fixed upper-fraction cap is required.
  source_metrics:
    c_LK_cert: 0
    a_LK_fine: 0
    b_LK_sqrt: 0
    note: SATURATED_DO_NOT_COUNT_STUCK
  hard_recoveries: 0/2
  outside_audits_found: 0/2
  closure_state: P0456_ACTIVE_AUDIT_PENDING
  final_paper_package_created: false
  directed_peer_audit: "No genuinely new P04 theorem available; no repeat audit fabricated."
  prior_art: >-
    Fresh 2026-09-18 Cambridge/source and bounded current-literature checks
    found no later source-matching Poisson/constant-window theorem; negative
    search evidence only, not a novelty certificate.
```

---

## 12. Runtime / tooling honesty

The actual runtime model exposed to this report is **GPT-5.6 Sol**. The reasoning level is **UNVERIFIED**. This is not GPT-6 at maximum, and I do not claim otherwise. The available scheduling interface still does not expose a model-selector or reasoning-effort field; `GPT-6 / maximum` remains prompt-only. GitHub connector reads can truncate large rendered surfaces; exact-path reads were used for imported proof dependencies, and truncation is disclosed above. No Gmail/email, Drive, public posting, paid compute, access change, workflow execution, external script, or additional schedule was used.

**End of complete run report.**
