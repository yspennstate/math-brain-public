Model actually run: **GPT-5.6 Sol. Reasoning level: UNVERIFIED. This is not GPT-6 at maximum.** **NO SOURCE-LEVEL COEFFICIENT-METRIC MOVEMENT.** The saturated metrics remain `c_LK^cert=a_LK^fine=b_LK^sqrt=0`; no stuck count is manufactured from saturation, and HARD recoveries remain `0/2`. This run uses **#8 GO THE OTHER WAY AND DISCRETIZE, #13 FIND WHAT ONLY INCREASES, #27 SWAP THE QUANTIFIERS**. The substantive advance is an exact finite clean one-root identity and a correction of an overstrong uniformity formulation: the clean probability is uniformly `e^{-h}(1+o(1))` when the competitor quota is `h=k+O(1)`, so the actual one-root case `h=k` is `e^{-k}(1+o_C(1))`, but it is **not** uniformly `e^{-k}(1+o(1))` over bounded quota shifts. This does not downgrade the repaired source chain because shifted quotas occur only in positive interaction clusters, where the chain uses an exponential-scale `exp[-k+o(k)]` upper bound.

# P03 / P0456 run report — exact clean saddle, monotone omission domination, and quantifier correction

Run timestamp: **2026-09-19T07:31:46Z**  
Track: **P03**  
Canonical target: **P0456**  
Repository / branch: `yspennstate/math-open-problems` / `master`  
Category: **HARD OUTSIDE**

---

## 1. Continuity, controls, audit-first screen, and source status

The exclusive assignment remains

`operations/claims/P0456.md`,

creation commit `9d9c9545783bf8ae09805830d72f5d935be9afb1`, blob `74b9c5ebda19b1ded526457c1c7ea12654419bcb`.

The newest complete P03 report entering this run was

`proofnet24/P03-fei/runs/2026-09-19/2026-09-19T06-27-17Z__p0456-auditor-map-cut-barrier.md`,

creation commit `bc1ef48d81f73c2930ba4c1961366102e4fd4046`, blob `7d33e1277cd8ecf67d33265fab828c49e3db70d5`; exact-commit readback had recovered `**End of complete run report.**`.

I preserve Claims 274, 276, 278, 280, 282, 284, 286 and Claims 288--306. Claims 288/289 remain internally source-matching candidate-complete but outside-audit pending. Claim 301 remains valid with the explicit repairs and packaging in Claims 302--306. This run adds Claim 307 below. It does not change any saturated coefficient metric.

At run start I reread/recovered root `README.md`, `proofnet24/HOURLY_PROTOCOL_2026-09-15.md`, current `FLEET_RULES.md`, `operations/new_methods_2026-09-16/OWNER_DIRECTIVE.md`, campaign `probability_campaign_2026_09/INDEX.md` and `RANKING.md`, root `POSTED.md`, `RESULTS.md`, `QUEUE.md`, the canonical P0456 claim, the complete newest P03 report, current P26 evidence, and neighboring P0457 only for nonduplication. The large policy/root surfaces are connector-truncated and therefore were targeted exact-path reads, not represented as byte-for-byte visual rereads. P0457 remains the distinct diameter problem owned by NM13-04 and is not duplicated here.

The exposed task-control surface continues to provide prompt/title/schedule/enablement/timing fields but no binding model-family selector and no reasoning-effort selector. Thus `GPT-6 / maximum` remains prompt-only. Runtime identity for this report is GPT-5.6 Sol; reasoning level is UNVERIFIED.

### 1.1 Incoming outside-audit screen

There is a newer P26 report than the one named in the incoming handoff:

`proofnet24/P26-proof-audit-recovery/runs/2026-09-19/2026-09-19_10-01-31__run-report.md`,

creation commit `1b76ce59dbf22c2c87929e747b33440bfdbc3ec9`.

It is an independent P26 audit of **R06 / ROMERO-2025-SPLIT8**, the finite `n=8` split-reliability layer. It is not an audit of P0456. Repository-wide searches for `P0456` together with `PASS`, `audit`, and the repaired Claim-288/289/301--306 identifiers still recover no P26 or genuinely distinct OTHER-track end-to-end audit of the repaired P0456 source chain.

Therefore the closure gate remains

`P0456_ACTIVE_AUDIT_PENDING / OUTSIDE_AUDITS_FOUND_0_OF_2`.

Self-audits do not count. No source-CLOSED label and no final paper package are created.

### 1.2 Fresh primary-source and literature check

The primary source remains Hossein Dabirian and Vijay Subramanian, *Connectivity of a family of bilateral preference random graphs*, *Journal of Applied Probability* 63(2) (June 2026), 552--579, DOI `10.1017/jpr.2025.10051`, published online 18 December 2025.

Fresh Cambridge retrieval on 19 September 2026 again verifies Section 1.1 unchanged. The authors explicitly state that connectivity is not known throughout

`log n - 0.5 loglog n sqrt(log n) <= k <= log n + 0.5 loglog n sqrt(log n)`,

and say their gap arises from analytically simpler sufficient conditions, including the no-intersection condition in the isolated-vertex argument. They state that a more elaborate or exact sufficient condition could close the gap.

The source's Lemma 10 still gives `P(B)=O(k^3/n)` for its pair bad-interaction event; Lemmas 13--14 still supply the conditional-independence/pair-ratio part of the disconnectedness proof; Theorem 3 remains the lower disconnectedness theorem for fixed `t'<-1/2`; Theorem 6 remains the upper connectivity theorem for fixed `t'>1/2`.

Fresh bounded searches for the exact DOI/title/authors and for 2026 bilateral-preference connectivity, Poisson isolated vertices, and follow-up work recovered the Cambridge paper and bibliographic/author records but no later source-matching constant-window theorem. This is dated bounded negative evidence only. **Publication novelty remains UNVERIFIED.**

---

## 2. What this run audits

Claim 306 deliberately reduced the source proof to a short auditor-facing chain:

`fixed-r joint isolation -> factorial moments -> Claim-305 finite Brun TV -> literal component elimination -> connectivity`.

Within that map, the largest remaining analytic black box was the clean one-root rejection saddle. Earlier Claims 297--300 contain sharper large-deviation and correction expansions, but an auditor of the source theorem should not have to trust those refinements. The present run therefore starts from the exact finite order-statistic/binomial formula and proves only the relative asymptotic needed at fixed `|k-log n|<=C`.

A second purpose is to test the quantifier order requested in the handoff. That test finds a precise failure: bounded **quota shifts** change the leading constant by `e^{shift}`. The corrected theorem is uniform when centered at the shifted quota `h`, not when centered at the original `k`. This is a genuine correction of a proposed strengthening, not a gap in the source chain.

---

## 3. Claim 307

### Claim `P03-P0456-CLEAN-SADDLE-MONOTONE-QUANTIFIER-307`

**Status:** `PROVED / SELF-AUDIT-STRENGTHENING / SOURCE-MATCHING-SUPPORT / AUDITS-PENDING / PUBLICATION-NOVELTY-UNVERIFIED`.

Fix finite constants `C,A,M`. Let `k=k_n` be integer with

`|k-log n|<=C`,

and let integer parameters `m,N,h` obey

`|m-n|+|N-n| <= A k`,

`|h-k|<=M`,

with `m>k`, `N>=h` for large `n`. Let

`q_h(x)=P(Bin(N,x)>=h)`,

`Q_h(x)=int_0^x q_h(t)dt`.

Define the exact clean marked probability

`M(m,N;k,h)
 := (m)_{k+1}/k! * int_0^1 Q_h(x)^k (1-x)^(m-k-1) dx`.      (3.1)

Then, uniformly over all such parameters,

`M(m,N;k,h) = (1-h/(N+1))^m [1+o_{C,A,M}(1)]`

and hence

`M(m,N;k,h) = e^{-h}[1+o_{C,A,M}(1)].`                       (3.2)

In particular, for the actual clean one-root isolation problem, `h=k`, so

`M(m,N;k,k)=e^{-k}[1+o_C(1)]`                                (3.3)

uniformly under deletion of `O_r(k)` competitors from the clean pool.

Combining (3.3) with the repaired positive-cluster estimate from Claims 302--304 gives, for every fixed vertex `v`,

`P(I_v)=e^{-k}[1+o_C(1)]`.                                   (3.4)

However, the stronger statement

`M(m,N;k,h)=e^{-k}[1+o(1)]`

**uniformly over all bounded quota shifts `h=k+O(1)` is false.** For example, with `h=k-1`,

`M(m,N;k,k-1)/e^{-k} -> e`.                                  (3.5)

The correct shifted center is `e^{-h}`. This failure does **not** downgrade Claims 288/289/301--306: the actual clean one-root probability uses `h=k`, while bounded quota reductions occur only inside positive interaction clusters, where Claims 303--304 require only the exponential-scale upper bound `exp[-k+o(k)]`. Replacing `h=k` by `h=k-O(1)` changes that bound by only a constant factor.

Finally, after Claim 302 has integrated active edges and omitted every contaminated deadline, arbitrary-rank omission sets admit a literal monotone domination: for an upper bound one may replace all surviving binomial tails by the worst tail with largest competitor pool and smallest quota, and among all omission sets of a fixed size `d`, the retained product is largest when the `d` **earliest** proposal deadlines are omitted. Thus the upper positive-cluster proof can reduce arbitrary-rank omissions to a canonical earliest-omission configuration. This does not replace Claim 302's disjointization; it applies only after that repair.

---

## 4. #8 GO THE OTHER WAY AND DISCRETIZE — exact finite clean identity

The clean probability can be derived without any continuum approximation or high-order correction.

### 4.1 Exact order-statistic formula

Expose the first `k` ordered proposal values from a root with `m` available proposal edges:

`0<X_1<...<X_k<1`.

Their joint density is

`(m)_k (1-X_k)^(m-k)`

on the ordered simplex. In the clean configuration, each proposal label has its own disjoint external competitor block of size `N`; conditional on `X_i=x_i`, rejection of the proposal at that selected neighbor has probability

`q_h(x_i)=P(Bin(N,x_i)>=h)`.

Therefore the exact clean probability is

`(m)_k int_{0<x_1<...<x_k<1}
       prod_{i=1}^k q_h(x_i)
       (1-x_k)^(m-k) dx_1...dx_k`.                            (4.1)

Integrating the first `k-1` coordinates gives

`(m)_k/(k-1)! * int_0^1 Q_h(x)^(k-1) q_h(x)
                             (1-x)^(m-k) dx`.                 (4.2)

Since `(Q_h^k)'=k Q_h^(k-1)q_h`, one integration by parts yields exactly (3.1):

`M(m,N;k,h)
 = (m)_{k+1}/k! int_0^1 Q_h(x)^k(1-x)^(m-k-1)dx`.            (4.3)

No asymptotic independence assertion enters (4.3); the disjoint clean competitor blocks are literal raw-edge blocks.

### 4.2 Exact beta representation for the binomial tail

Let

`B_h ~ Beta(h,N-h+1)`.

The elementary order-statistic/binomial identity gives

`q_h(x)=P(B_h<=x)`.

Hence, by Fubini,

`Q_h(x)=E[(x-B_h)_+]`.                                       (4.4)

There is also the exact finite Bernstein-polynomial form

`Q_h(x)
 = 1/(N+1) * sum_{j=h+1}^{N+1}
     (j-h) C(N+1,j) x^j(1-x)^(N+1-j)`.                       (4.5)

Substituting (4.5) into (4.3) produces a completely finite beta sum. If

`J=j_1+...+j_k`,

then

`M(m,N;k,h)
 = (m)_{k+1}/[k!(N+1)^k]
   * sum_{j_1,...,j_k=h+1}^{N+1}
       [prod_{a=1}^k (j_a-h) C(N+1,j_a)]
       B(J+1, k(N+1)-J + m-k)`.                              (4.6)

Equation (4.6) is an exact finite order-statistic/binomial representation of the clean saddle. It is the source-theorem-scale version of the coefficient identity previously used only in the high-order correction self-audits.

### 4.3 The conserved mean-replacement identity

Put

`mu=E B_h=h/(N+1)`.

Since `x -> (x-b)_+` is convex in `b`, Jensen gives

`Q_h(x)=E[(x-B_h)_+] >= (x-mu)_+`.                            (4.7)

Replace `Q_h` by `(x-mu)_+` in (4.3). The resulting integral is exactly

`M_0
 = (m)_{k+1}/k! * int_mu^1 (x-mu)^k(1-x)^(m-k-1)dx
 = (1-mu)^m`.                                                 (4.8)

The cancellation is exact: after `x=mu+(1-mu)z`, the remaining beta integral is

`B(k+1,m-k)=k!(m-k-1)!/m!`,

which is the reciprocal of the prefactor. This identity explains why the clean leading exponential depends on the competitor quota `h`, not on the number `k` of proposal deadlines after the latter has been integrated out.

Equation (4.7) immediately gives the clean lower bound

`M >= M_0`.                                                   (4.9)

The rest of the proof shows that beta fluctuations add only relative `o(1)` in the fixed window.

---

## 5. Two-sided relative estimate without first/second-correction machinery

Let

`sigma^2=Var(B_h)
 = h(N-h+1)/[(N+1)^2(N+2)]`.

Uniformly under the hypotheses of Claim 307,

`sigma = O_{C,A,M}(sqrt(k)/n)`,                               (5.1)

and

`mu=(k+O(1))/n`, `m/N=1+O(k/n)`.                             (5.2)

Write

`a=x-mu`,

`R(x)=E[(B_h-x)_+]`.

For `x>=mu`,

`Q_h(x)=a+R(x)`.                                              (5.3)

We split (4.3) into four elementary regions. Fix once and for all `eps=1/4`.

### 5.1 Region I: `x<mu`

For `x<=mu`,

`Q_h(x)<=E[(mu-B_h)_+]<=E|B_h-mu|<=sigma`.                   (5.4)

Using `(1-x)^(m-k-1)<=1`,

`M_I <= (m)_{k+1}/k! * sigma^k`.

Since `(m)_{k+1}<=m^{k+1}`, `m=Theta(n)`, and `sigma<=C sqrt(k)/n`, Stirling's lower bound `k!>=(k/e)^k` gives

`log M_I <= -0.5 k log k + O(k) + log n`.                    (5.5)

Because `k=log n+O(1)`, (5.5) is `-Omega(k log k)`, whereas `M_0=e^{-h+o(1)}=e^{-k+O(1)}`. Hence

`M_I=o(M_0)`.                                                 (5.6)

### 5.2 Region II: `0<=a<=eps k/n`

Here (5.1) gives

`Q_h(x)<=a+sigma <= [eps k+O(sqrt(k))]/n`.                    (5.7)

Also `(1-x)^(m-k-1)<=(1-mu)^(m-k-1)`, and the interval has length `eps k/n`. Therefore, after dividing by `M_0=(1-mu)^m`,

`M_II/M_0
 <= poly(k) [ e(eps+O(k^-1/2)) ]^k`.                      (5.8)

Because `e/4<1`, the right-hand side is `exp[-c_0 k+O(log k)]` for some fixed `c_0>0`. Thus

`M_II=o(M_0)`.                                                (5.9)

### 5.3 Region III: `eps k/n <= a <= k/(2m)`

Normalize the mean-replacement integrand:

`dnu(x)
 = [(m)_{k+1}/(k! M_0)] a^k(1-x)^(m-k-1) dx`, `x>=mu`.        (5.10)

Under `nu`,

`Z=(X-mu)/(1-mu) ~ Beta(k+1,m-k)` exactly.                   (5.11)

In Region III, (5.1) and `a>=eps k/n` imply

`Q_h(x)^k/a^k
 <= (1+sigma/a)^k
 <= exp[O(sqrt(k))].`                                        (5.12)

But Region III lies below one half of the natural beta saddle: uniformly,

`Z <= (1+o(1)) k/(2m)`,

whereas `E_nu Z=(k+1)/(m+1)=(1+o(1))k/m`. Standard binomial/Beta Chernoff (equivalently, the elementary density-ratio bound for the beta density) gives

`nu(Region III) <= exp[-c_1 k]`                               (5.13)

for some fixed `c_1>0`. Combining (5.12)--(5.13),

`M_III=o(M_0)`.                                               (5.14)

Only exponential separation is used; no correction exponent or Laplace prefactor is imported.

### 5.4 Region IV: `a>=k/(2m)`

This is the mean-replacement saddle region. We show that the beta overshoot `R(x)` is uniformly negligible relative to `a`.

Let `f` be the density of `B_h`. It is log-concave and

`d/db log f(b)=(h-1)/b-(N-h)/(1-b)`.                          (5.15)

From (5.2), every `x` in Region IV obeys, for all large `n`,

`x >= (1+c_2) mu`                                             (5.16)

for a fixed `c_2>0` (for example any fixed `c_2<1/2` works eventually). Hence (5.15) is at most `-c_3 N` on `[x,1]` for a fixed `c_3>0`. Therefore

`f(b)<=f(x) exp[-c_3 N(b-x)]`, `b>=x`,

and so

`R(x)=int_x^1 (b-x)f(b)db <= f(x)/(c_3 N)^2`.                (5.17)

A direct Stirling bound on the beta density at any `x>=(1+c_2)mu` gives

`f(x) <= C N k^{C'} exp[-c_4 k]`                             (5.18)

for constants depending only on `C,A,M`. Combining (5.17)--(5.18) with `a>=c k/N` gives

`R(x)/a <= k^{C''} exp[-c_4 k]`.                             (5.19)

Thus uniformly on Region IV,

`Q_h(x)^k/a^k
 = (1+R(x)/a)^k
 = 1+o(1)`.                                                   (5.20)

Consequently

`M_IV <= (1+o(1)) M_0`.                                      (5.21)

Together with the lower bound (4.9) and Regions I--III,

`M=M_0[1+o(1)]`.                                              (5.22)

All constants above are uniform over the full Claim-307 parameter set. Finally,

`log M_0
 = m log(1-h/(N+1))
 = -h + O(k^2/n)`,                                            (5.23)

so (3.2) follows.

---

## 6. Actual one-root isolation at the source window

For the actual one-root clean branch, the selected neighbor must have **k** lighter competing incident edges. Thus `h=k`, not a shifted quota. Deleting the root and the `O(k)` selected labels from each external competitor pool changes `m,N` by only `O(k)`, which is covered uniformly by Claim 307. Hence the clean external-rejection event has probability

`e^{-k}(1+o_C(1))`.                                          (6.1)

This event is sufficient for root isolation, so it supplies the lower bound.

For the upper bound, split isolation into the zero interaction cluster and positive interaction clusters exactly as in Claims 302--304. On the zero cluster, isolation forces the clean rejection event above. Every positive cluster has at least one codimension unit and, after the minimum-deadline collision repair and active-edge integration, Claim 303 supplies `exp[-k+o(k)]` for the residual necessary rejections; the positive-cluster sum is `o(e^{-k})`. Therefore

`P(I_v)=e^{-k}(1+o_C(1))`,                                   (6.2)

uniformly for `|k-log n|<=C`.

This is the complete clean one-root analytic input needed by the Claim-306 auditor map. It does not rely on Claims 298--300 or any first/second correction coefficient.

---

## 7. #27 SWAP THE QUANTIFIERS — the requested stronger statement is false, and the corrected one is enough

The incoming handoff explicitly asked for simultaneous uniformity over

- fixed `|k-log n|<=C`,
- deletion of `O_r(k)` competitors,
- bounded competitor-quota shifts.

The first two can coexist with the relative center `e^{-k}` when the quota remains exactly `h=k`. The third cannot.

Indeed, Claim 307 proves uniformly

`M(m,N;k,h)=e^{-h}(1+o(1))`.                                 (7.1)

Set `h=k-s` for a fixed integer `s`. Then

`M/e^{-k} -> e^s`.                                            (7.2)

Already `s=1` gives the explicit counterexample

`M(m,N;k,k-1)=e * e^{-k}(1+o(1))`.                           (7.3)

Therefore a statement centered at `e^{-k}` cannot be uniform over even the two quotas `k` and `k-1`.

This does **not** trigger a downgrade of the source theorem. The repaired chain uses the two contexts differently:

1. **Clean one-root / zero cluster / lower fixed-root branch:** the quota is exactly `k`, so (6.2) gives the required relative `1+o_C(1)` estimate.
2. **Positive clusters:** deleting a contaminated deadline or integrating an active edge can reduce a residual quota by at most `O_r(1)`. There the proof never requires a relative center `e^{-k}`. It only requires
   `M <= exp[-k+o(k)]`.
   Equation (7.1) gives the stronger
   `M <= exp[-k+O_r(1)+o(1)]`,
   so the codimension factor `n^{-K+o(1)}` still makes every positive cluster `o(e^{-rk})`.

Thus the correct quantifier-swapped lemma is **quota-aware**, and every hypothesis actually used by Claims 288/289/301--306 remains valid.

This is the main negative finding of the run: the proposed stronger uniformity is false for a transparent exact reason, and the report records that failure rather than hiding it behind the existing high-order machinery.

---

## 8. #13 FIND WHAT ONLY INCREASES — monotone domination of arbitrary omissions

Claim 303 handles arbitrary-rank omissions by an exact symmetric-polynomial/order-statistic calculation. For the source-facing **upper** bound, some of that bookkeeping can be replaced by a monotonicity statement once Claim 302 has already repaired/disjointized the interaction cluster.

Fix an ordered proposal array

`0<x_1<...<x_p<1`.

For each retained rejection deadline, the residual rejection probability is a binomial tail

`q_{N_i,h_i}(x_i)=P(Bin(N_i,x_i)>=h_i)`.

This function is pointwise

- increasing in `x_i`,
- increasing in the competitor-pool size `N_i`,
- decreasing in the quota `h_i`.

Let

`N_* = max_i N_i`,

`h_* = min_i h_i`,

and `q_*(x)=q_{N_*,h_*}(x)`. Then for every retained index

`q_{N_i,h_i}(x_i) <= q_*(x_i)`.                              (8.1)

Now fix the number `d` of omitted deadlines. Because `0<=q_*(x_1)<=...<=q_*(x_p)<=1`, the product of the `p-d` retained factors is maximized by omitting the `d` **smallest** factors, i.e. the earliest deadlines:

`prod_{i notin D} q_{N_i,h_i}(x_i)
 <= prod_{i=d+1}^p q_*(x_i)`                                 (8.2)

for every omission set `D` with `|D|=d`.

Equation (8.2) is literal pointwise domination. It shows that, for the upper positive-cluster estimate, arbitrary omission patterns can be compressed to the canonical earliest-omission case plus worst pool/quota parameters.

There are two important limitations.

First, (8.2) applies **after** active selected--selected/root-selected/root-root edges have been integrated out and every deadline they can contaminate has been omitted. Before Claim 302's repair, one raw edge can couple multiple deadlines and no product domination is legitimate.

Second, the worst quota may be `h_*=k-O_r(1)`, so the correct clean center is `e^{-h_*}`, not `e^{-k}`. For the positive-cluster upper bound this is harmless by Section 7.

Thus #13 succeeds as a proof-surface simplification, not as a replacement for the repaired interaction lemma.

---

## 9. Fixed-r source chain after Claim 307

The asymmetric fixed-root proof from Claim 306 is now analytically self-contained at the fixed window.

### Lower bound

For deterministic distinct roots `v_1,...,v_r`, use the sufficient event from Claim 306: all proposal labels are distinct, root-root edges are late, root thresholds obey the guard, and every selected outside label has `k` lighter competitors in its fully external raw-edge block. The blocks are disjoint. Claim 307 with `h=k` applies to each root, uniformly under deletion of `O_r(k)` competitor labels. Therefore

`P(I_{v_1}=...=I_{v_r}=1)
 >= e^{-rk}(1-o_C(1))`.                                      (9.1)

No bounded-omission lemma is used in this direction.

### Upper bound

Decompose by repaired interaction clusters. The zero cluster is bounded by the same clean `h=k` probability. Every positive cluster costs `n^{-K+o(1)}`, `K>=1`. After active-edge integration and omission, Section 8 reduces the residual root rejection problem to worst bounded pool/quota parameters and earliest omissions; Claim 303, or the quota-aware clean estimate where applicable, supplies `exp[-rk+o(k)]`. Hence

`P(I_{v_1}=...=I_{v_r}=1)
 <= e^{-rk}(1+o_C(1))`.                                      (9.2)

Combining (9.1)--(9.2), for every fixed `r`,

`P(I_{v_1}=...=I_{v_r}=1)=e^{-rk}(1+o_C(1))`.                (9.3)

The error is uniform over every deterministic fixed root tuple. Claim 305's finite Brun inequality remains the sole conversion from these factorial moments to total-variation Poisson convergence. Nothing in this run reintroduces a subsequence/Scheffe argument or an unchecked black-box Poisson theorem.

---

## 10. Literal nontrivial-component check

The component side of Claim 306 was rechecked only for consistency with the clean-saddle correction above; no new component theorem is needed.

For sizes `2<=s<=6`, internal candidate-component edges are deleted before external proposal ranks are formed. The spanning-tree event therefore uses only internal raw edges, while the external rejection event uses only external raw edges. The two factors are independent. The external rejection estimate uses `p_0=k-(s-1)` exposed proposal slots, but the selected-neighbor rejection quota is still handled by the repaired bounded-omission/cluster estimate, so Section 7's quota-aware warning causes no loss.

For sizes `7<=s<=n/2`, the one-global two-sided kth-threshold envelope of Claim 301/306 remains untouched. Its failure event is paid once, sizes 7--12 use the fixed-size exponent, and sizes 13+ use the geometric half-cut exponent. Claim 306 already proved why the current global threshold/cut route cannot absorb sizes 2--6.

No connectivity conclusion is inferred from mean degree.

---

## 11. Status, failures, and what changed

### Methods used

- **#8 GO THE OTHER WAY AND DISCRETIZE:** succeeded. The clean root saddle now has the exact finite formulas (4.3), (4.5), and (4.6), and the fixed-window relative asymptotic follows without first/second-correction machinery.
- **#13 FIND WHAT ONLY INCREASES:** succeeded with a scope restriction. After repaired disjointization, worst pool/quota parameters and earliest-deadline omission pointwise dominate every bounded omission pattern for the upper proof. It cannot be applied before active-edge integration.
- **#27 SWAP THE QUANTIFIERS:** the strongest requested formulation **fails**. Uniform centering at `e^{-k}` is false over bounded quota shifts; the exact counterexample is `h=k-1`, where the ratio tends to `e`. The corrected quota-aware theorem `e^{-h}(1+o(1))` is proved and is fully sufficient for the repaired source chain.

### New claim

`P03-P0456-CLEAN-SADDLE-MONOTONE-QUANTIFIER-307`

= **PROVED / SELF-AUDIT-STRENGTHENING / SOURCE-MATCHING-SUPPORT / AUDITS-PENDING / PUBLICATION-NOVELTY-UNVERIFIED**.

### Preserved source chain

- Claim 288 remains `PROVED / SOURCE-MATCHING-CANDIDATE-COMPLETE / AUDITS-PENDING / PUBLICATION-NOVELTY-UNVERIFIED`.
- Claim 289 remains `PROVED / SELF-AUDIT-REPAIR / SOURCE-MATCHING-STRENGTHENING / AUDITS-PENDING / PUBLICATION-NOVELTY-UNVERIFIED`.
- Claim 301 remains proved with Claims 302--307 as explicit repairs/strengthenings.
- Claim 305 remains the sole TV conversion.
- Claim 306 remains the auditor-facing fixed-C implication map.

There is no source-level coefficient-metric movement because all three fixed coefficient metrics are already saturated at zero. HARD recoveries remain `0/2`.

---

## 12. Exact remaining obligation and next state

The mathematics of the fixed-C source chain is internally candidate-complete, now with the clean one-root analytic step exposed by an exact finite identity and with the quota-shift quantifier issue made explicit. The protocol obligation is still independent verification:

1. a P26 end-to-end audit of the repaired source chain, including Claims 302--307;
2. one genuinely distinct OTHER-track end-to-end audit of the same source-matching chain.

Until both exist, do not label the source CLOSED and do not create/promote the final paper package.

The best next mathematical audit is no longer another correction coefficient. An outside auditor should attack the exact finite clean identity (4.1)--(4.6), the Region-I--IV relative upper bound, and the use of shifted quotas only inside positive clusters. Internally, if another run occurs before an outside audit arrives, the most useful fresh route is to eliminate the remaining coarse Region-III/IV split by deriving a single finite likelihood-ratio inequality between the exact beta-mixture integrand and its mean-replacement integrand, or to find a counterexample to such a global comparison. That would simplify the proof surface without changing the theorem.

Current protocol state:

`P0456_ACTIVE_AUDIT_PENDING / OUTSIDE_AUDITS_FOUND_0_OF_2 / CLAIM_307_CLEAN_SADDLE_QUANTIFIER_READY`.

---

## 13. `ledger_delta` for P26

```yaml
ledger_delta:
  owner_track: P03
  target: P0456
  source: Dabirian--Subramanian J. Applied Probability 63(2) Section 1.1
  source_status: ACTIVE_AUDIT_PENDING
  source_matching_claims: [288, 289]
  repaired_auditor_chain: [301, 302, 303, 304, 305, 306, 307]
  new_claim: P03-P0456-CLEAN-SADDLE-MONOTONE-QUANTIFIER-307
  new_claim_status: PROVED_SELF_AUDIT_STRENGTHENING_SOURCE_MATCHING_SUPPORT
  substantive_result: exact finite clean integral and uniform M=e^-h(1+o(1)); actual h=k gives one-root e^-k(1+o_C(1))
  quantifier_failure: uniform e^-k relative asymptotic over bounded quota shifts is false; h=k-1 gives ratio -> e
  source_chain_downgrade: false
  reason_no_downgrade: shifted quotas occur only in positive clusters where exp[-k+o(k)] suffices
  monotone_omission_domination: earliest omitted deadlines + largest pool + smallest quota, after Claim-302 disjointization only
  outside_audits_before: 0_of_2
  outside_audits_after: 0_of_2
  p26_audit: MISSING
  distinct_other_audit: MISSING
  request_to_p26: audit repaired fixed-C P0456 chain Claims 288/289/301--307 end-to-end
  c_LK_cert: 0
  a_LK_fine: 0
  b_LK_sqrt: 0
  hard_recoveries: 0_of_2
  publication_novelty: UNVERIFIED
  shared_root_edits: none
  peer_edits: none
  paper_package: not_created
```

**End of complete run report.**