Model actually run: **GPT-5.6 Sol. Reasoning level: UNVERIFIED. This is not GPT-6 at maximum.** **NO SOURCE-LEVEL COEFFICIENT-METRIC MOVEMENT.** The saturated metrics remain `c_LK^cert=a_LK^fine=b_LK^sqrt=0`; no stuck count is manufactured from saturation, and HARD recoveries remain `0/2`. This run uses **#5 ADD A PARAMETER AND DIFFERENTIATE IN IT, #11 DUALIZE, #29 ADD THE POINTS AT INFINITY**. The substantive advance is a one-parameter interpolation and exact saddle-law dualization of Claim 307 which yields a uniform source-scale relative bound `M/M_0=1+O(exp(-k/20))`. A completely split-free global likelihood-ratio proof is impossible in the naive form because the true beta-marked integral has positive mass below the mean while the mean-replacement saddle has zero mass there, and its likelihood ratio is singular at the mean. The upper endpoint is benign. The source chain is strengthened but remains outside-audit pending.

# P03 / P0456 run report — interpolated beta law, dual saddle measure, and boundary compactification

Run timestamp: **2026-09-19T08:27:37Z**  
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

`proofnet24/P03-fei/runs/2026-09-19/2026-09-19T07-31-46Z__p0456-clean-saddle-monotone-quantifier.md`,

creation commit `a7b3e51f67ee81d1d11c5b5388591bc3ebac8230`, blob `1fb2fddda828a0042327b0c5fc2d4955fbcae8c7`; exact-commit readback had recovered `**End of complete run report.**`.

I preserve Claims 274, 276, 278, 280, 282, 284, 286 and Claims 288--307. Claims 288/289 remain internally source-matching candidate-complete but outside-audit pending. Claim 301 remains valid only with the explicit repairs/strengthenings 302--307. This run adds Claim 308 below. It does not move any saturated coefficient metric.

At run start I reread/recovered root `README.md`, `proofnet24/HOURLY_PROTOCOL_2026-09-15.md`, current `FLEET_RULES.md`, `operations/new_methods_2026-09-16/OWNER_DIRECTIVE.md`, campaign `probability_campaign_2026_09/INDEX.md` and `RANKING.md`, root `POSTED.md`, target-scoped `RESULTS.md` / `QUEUE.md` evidence, the canonical P0456 claim, the complete newest P03 report, current P26 evidence, P03 handoff history, task-health/ownership evidence, and neighboring P0457 only for nonduplication. Large connector-rendered policy/root surfaces are truncated, so those were targeted exact-path and exact-string reads rather than a claim of byte-for-byte visual rereading of every row. P0457 remains the separate diameter target owned by NM13-04.

The available scheduler control surface still has prompt/title/schedule/enablement/timing fields and no binding model-family selector or reasoning-effort selector. Thus `GPT-6 / maximum` remains prompt-only. Runtime identity exposed here is GPT-5.6 Sol; reasoning level is UNVERIFIED.

### 1.1 Incoming outside-audit screen

The newest concrete P26 report recovered is

`proofnet24/P26-proof-audit-recovery/runs/2026-09-19/2026-09-19_10-01-31__run-report.md`,

whose run begins by identifying itself as an independent audit of **R06 / ROMERO-2025-SPLIT8**, not P0456. Fresh repository searches for `P0456` together with `PASS`, `audit`, and the repaired Claim-288/289/301--307 identifiers recover no P26 or genuinely distinct OTHER-track end-to-end audit of the repaired P0456 source chain.

Therefore the closure gate remains

`P0456_ACTIVE_AUDIT_PENDING / OUTSIDE_AUDITS_FOUND_0_OF_2`.

Self-audits do not count. I do not label the source CLOSED and do not create the final paper package.

### 1.2 Fresh primary-source and literature check

The primary source remains Hossein Dabirian and Vijay Subramanian, *Connectivity of a family of bilateral preference random graphs*, *Journal of Applied Probability* 63(2) (June 2026), 552--579, DOI `10.1017/jpr.2025.10051`, published online 18 December 2025.

Fresh Cambridge retrieval on 19 September 2026 again verifies Section 1.1 unchanged. It says connectivity is not known throughout

`log n - 0.5 loglog n sqrt(log n) <= k <= log n + 0.5 loglog n sqrt(log n)`,

and explicitly attributes the gap to analytically simpler sufficient conditions, including the no-intersection condition in the isolated-vertex proof. The PDF was inspected directly (including rendered page inspection); Lemmas 10--14 and Theorems 3--6 retain their source roles. In particular Lemma 10 has the `O(k^3/n)` pair bad-interaction estimate; Theorem 3 is the lower disconnectedness theorem and Theorem 6 the upper connectivity theorem.

Fresh bounded searches for the DOI/title/authors, 2026 bilateral-preference connectivity, isolated-vertex Poisson limits, and author updates recovered the Cambridge article and current bibliographic records but no later theorem closing this exact constant window. This is dated bounded negative evidence only. **Publication novelty remains UNVERIFIED.**

---

## 2. What this run attacks

Claim 307 already removed the high-order correction machinery from the source-scale one-root proof. Its clean marked integral is

`M(m,N;k,h)
 = (m)_{k+1}/k! * int_0^1 Q_h(x)^k (1-x)^(m-k-1) dx`,       (2.1)

where

`q_h(x)=P(Bin(N,x)>=h)`,
`Q_h(x)=int_0^x q_h(t)dt=E[(x-B_h)_+]`,
`B_h~Beta(h,N-h+1)`,
`mu=E B_h=h/(N+1)`.

Its exact mean replacement is

`Q_0(x)=(x-mu)_+`,

and

`M_0=(m)_{k+1}/k! * int_mu^1 (x-mu)^k(1-x)^(m-k-1)dx
    =(1-mu)^m`.                                               (2.2)

Claim 307 proved `M/M_0->1` uniformly by a four-region argument. The present run asks whether one can expose the comparison itself as a monotone deformation and then dualize it under the exact mean-replacement saddle law.

The answer has two parts:

1. **Yes:** the interpolation is globally monotone and convex, and one endpoint derivative controls the entire relative error.
2. **No:** an ordinary globally bounded Radon--Nikodym comparison against the mean saddle is impossible, because the mean saddle has no support below `mu` while the true beta-marked integrand does. Even above `mu`, the pointwise ratio is singular as `x downarrow mu`. A lower-boundary split is structurally necessary. The upper endpoint `x=1`, after compactification, is harmless.

This yields a simpler quantitative source-scale theorem and an exact explanation of why a truly one-line pointwise likelihood-ratio argument cannot exist in the naive form.

---

## 3. Claim 308

### Claim `P03-P0456-INTERPOLATED-DUAL-CLEAN-SADDLE-308`

**Status:** `PROVED / SELF-AUDIT-SIMPLIFICATION / SOURCE-MATCHING-SUPPORT / AUDITS-PENDING / PUBLICATION-NOVELTY-UNVERIFIED`.

Fix finite constants `C,A,M`. Let `k=k_n` be integer with

`|k-log n|<=C`,

and let integer parameters `m,N,h` satisfy

`|m-n|+|N-n|<=A k`,
`|h-k|<=M`,

with `m>k` and `N>=h` for all large `n`. Define `M=M(m,N;k,h)` by (2.1), `mu=h/(N+1)`, and `M_0=(1-mu)^m`.

Then, uniformly over all such parameters,

`1 <= M/M_0 <= 1 + O_{C,A,M}(exp(-k/20))`.                  (3.1)

Consequently

`M(m,N;k,h)=e^{-h}[1+O_{C,A,M}(exp(-k/20))]`.                (3.2)

The center in (3.2) is **quota-aware**. It is `e^{-h}`, not uniformly `e^{-k}` over bounded shifts `h=k+O(1)`. In the actual clean one-root isolation problem `h=k`, so

`M(m,N;k,k)=e^{-k}[1+O_C(exp(-k/20))]`.                      (3.3)

The proof uses no first- or second-correction result from Claims 298--300.

More structurally, define the mean-preserving interpolation

`B_theta ~ (1-theta) delta_mu + theta Law(B_h)`, `0<=theta<=1`,

and

`Q_theta(x)=E[(x-B_theta)_+]
           =(x-mu)_+ + theta[Q_h(x)-(x-mu)_+]`.

Let

`M_theta=(m)_{k+1}/k! * int_0^1 Q_theta(x)^k(1-x)^(m-k-1)dx`.

Then `M_theta` is increasing and convex in `theta`, and

`0 <= M_1-M_0 <= M_1'`.                                      (3.4)

After dualizing to the exact mean-replacement saddle law, (3.4) becomes a single endpoint expectation estimate plus one singular lower-boundary term. A split-free **ordinary** likelihood-ratio comparison is impossible because the true integral has positive `x<mu` mass whereas the mean-replacement saddle has zero such mass. Under the projective coordinate

`y=(x-mu)/(1-x)`,

the upper endpoint `x=1` is the point `y=infinity`; the likelihood-ratio correction tends to `1` there. The only structural boundary obstruction is at the lower endpoint `x=mu` (and the collapsed region below it).

---

## 4. #5 ADD A PARAMETER AND DIFFERENTIATE IN IT

Put

`Delta(x)=Q_h(x)-(x-mu)_+`.

Because `b -> (x-b)_+` is convex and `E B_h=mu`, Jensen gives

`Delta(x)>=0` for every `x`.                                  (4.1)

The interpolation above is exactly

`Q_theta(x)=(x-mu)_+ + theta Delta(x)`.

Differentiation under the finite integral gives

`M_theta'
 = k (m)_{k+1}/k! * int_0^1
     Delta(x) Q_theta(x)^(k-1)(1-x)^(m-k-1) dx >=0`,          (4.2)

and

`M_theta''
 = k(k-1) (m)_{k+1}/k! * int_0^1
     Delta(x)^2 Q_theta(x)^(k-2)(1-x)^(m-k-1) dx >=0`.        (4.3)

Thus the derivative does **not** change sign: the beta dispersion monotonically increases the clean integral away from its point-mass-at-the-mean value. Convexity gives

`M_1-M_0=int_0^1 M_theta' dtheta <= M_1'`,                    (4.4)

which is (3.4).

So it is enough to bound one endpoint derivative. This is the useful simplification: instead of comparing `Q_h^k` and `(x-mu)^k` separately in every bulk region, we compare the single defect factor `Delta Q_h^(k-1)`.

---

## 5. #11 DUALIZE — exact expectation under the mean saddle

For `x>=mu`, write

`a=x-mu`,
`R(x)=E[(B_h-x)_+]`.

The identity `E(B_h-mu)=0` gives

`Q_h(x)=a+R(x)`,                                               (5.1)

so, for `a>0`, define

`r(x)=R(x)/a >=0`.                                             (5.2)

Normalize the mean-replacement integrand:

`d nu_0(x)
 = [(m)_{k+1}/(k! M_0)]
   (x-mu)^k (1-x)^(m-k-1) dx`, `mu<x<1`.                     (5.3)

This is a probability law. Exactly,

`Z=(X-mu)/(1-mu) ~ Beta(k+1,m-k)` under `nu_0`.               (5.4)

Also define the normalized true contribution from below the mean,

`S_-
 = [(m)_{k+1}/(k! M_0)]
   int_0^mu Q_h(x)^k(1-x)^(m-k-1)dx`.                        (5.5)

Then the interpolation has the exact dual form

`M_theta/M_0
 = theta^k S_- + E_{nu_0}[(1+theta r(X))^k]`.                (5.6)

Indeed, below `mu` the mean-replacement hinge is zero, so `Q_theta=theta Q_h`; above `mu`, `Q_theta=a+theta R=a(1+theta r)`.

Differentiating (5.6) at `theta=1`,

`M_1'/M_0
 = k S_- + k E_{nu_0}[r(X)(1+r(X))^(k-1)]`.                  (5.7)

Combining (4.4) and (5.7),

`0 <= M/M_0-1
 <= k S_- + k E_{nu_0}[r(X)(1+r(X))^(k-1)]`.                 (5.8)

Equation (5.8) is the desired dual statement. No named stochastic or convex order is invoked beyond the literal Jensen inequality (4.1). The normalized mean-replacement saddle law is explicit and all that remains is one expectation under a Beta law.

---

## 6. Quantitative endpoint-derivative estimate

Let

`sigma^2=Var(B_h)
 = h(N-h+1)/[(N+1)^2(N+2)]`.                                 (6.1)

Uniformly under Claim 308,

`mu=Theta(k/n)`,
`sigma=O(sqrt(k)/n)`,
`sigma^2/mu^2=(N-h+1)/(h(N+2)) <= 1/h`.                      (6.2)

We prove the right side of (5.8) is `O(exp(-k/20))`. The split below is not an artifact of a local Laplace expansion: Section 7 shows why the lower endpoint genuinely prevents a bounded global likelihood ratio.

### 6.1 Singular sector below the mean

For `x<=mu`,

`Q_h(x)<=E[(mu-B_h)_+]<=sigma`.

Hence

`S_-
 <= [(m)_{k+1}/(k! M_0)] mu sigma^k`.                        (6.3)

Using `m=Theta(n)`, `mu=Theta(k/n)`, `sigma=O(sqrt(k)/n)`, `M_0=e^{-O(k)}`, and Stirling's lower bound `k!>=(k/e)^k`,

`S_- <= exp[-(1/2)k log k+O(k)]`.                             (6.4)

Thus `kS_-` is much smaller than `exp(-k/20)`.

### 6.2 Near-mean sector

Put

`a_1=mu k^(-1/3)`.

For `0<a<=a_1`, `R(x)<=E|B_h-mu|<=sigma`, and (6.2) implies `sigma/a_1=O(k^(-1/6))`. Thus for all large `n`,

`Q_h(x)=a+R(x)<=2a_1`.

By the exact cancellation implicit in (5.3),

`E_{nu_0}[r(1+r)^(k-1); 0<a<=a_1]
 = [(m)_{k+1}/(k!M_0)]
   int_{mu}^{mu+a_1} R(x)Q_h(x)^(k-1)(1-x)^(m-k-1)dx`

`<= [(m)_{k+1}/(k!M_0)] a_1 sigma (2a_1)^(k-1)`

`<= exp[-(1/3)k log k+O(k)]`.                                 (6.5)

Again this is superexponentially small on the `e^{-c k}` scale.

### 6.3 Intermediate sector: second moment plus a Beta/Binomial tail

Put

`a_0=mu/2`.

For any centered real `Y` and `a>0`,

`(Y-a)_+ <= Y^2/(4a)`,                                       (6.6)

because on `Y>=a`, `Y-a<=Y^2/(4a)` is equivalent to `(Y-2a)^2>=0`. With `Y=B_h-mu`,

`R(x)<=sigma^2/(4a)`,

so on `a_1<a<=a_0`,

`r(x)<=sigma^2/(4a^2)<=k^(-1/3)`                             (6.7)

for all large `n`, uniformly in the fixed parameter box. Hence

`(1+r)^(k-1)<=exp(k^(2/3))`.                                  (6.8)

Under `nu_0`, `Z=a/(1-mu)~Beta(k+1,m-k)`. At `a=a_0`, let

`z_0=mu/[2(1-mu)]`.

Uniformly, for all large `n`,

`m z_0 <= (3/5)(k+1)`.                                       (6.9)

The exact Beta/Binomial identity gives

`nu_0(a<=a_0)
 =P(Bin(m,z_0)>=k+1)`

`<= exp[-(k+1)/10]`,                                         (6.10)

where the last inequality follows by stochastic domination by a binomial of mean `(3/5)(k+1)` and the elementary multiplicative Chernoff bound at factor `5/3`.

Therefore

`E_{nu_0}[r(1+r)^(k-1); a_1<a<=a_0]
 <= k^(-1/3) exp[-(k+1)/10+k^(2/3)]`.                        (6.11)

### 6.4 Far / saddle sector: exact size-biased Beta tail

For `a>=a_0`,

`x>=mu+a_0=3mu/2`.

Let

`B_h^+ ~ Beta(h+1,N-h+1)`.

Size-biasing the beta density gives exactly

`E[B_h 1_{B_h>x}]=mu P(B_h^+>x)`.                            (6.12)

Since `(B_h-x)_+<=B_h 1_{B_h>x}`,

`R(x)<=mu P(B_h^+>x)`.                                       (6.13)

For all large `h`, `x>=3mu/2` implies

`(N+1)x >= (7/5)(h+1)`.                                      (6.14)

By the exact order-statistic/Binomial identity,

`P(B_h^+>x)=P(Bin(N+1,x)<=h)`.                               (6.15)

The binomial mean in (6.15) is at least `(7/5)(h+1)`, so the lower-tail multiplicative Chernoff bound with relative deficit at least `2/7` gives

`P(B_h^+>x)<=exp[-2(h+1)/35]`.                               (6.16)

Since `a>=mu/2`,

`r(x)<=2 exp[-2(h+1)/35]`.                                   (6.17)

For all large `k`, `k r(x)->0` uniformly here, and therefore

`r(x)(1+r(x))^(k-1)
 <=4 exp[-2(h+1)/35]`.                                       (6.18)

### 6.5 Combining the sectors

Equations (5.8), (6.4), (6.5), (6.11), and (6.18) give

`0<=M/M_0-1`

`<= k exp[-(1/2)k log k+O(k)]
  + k exp[-(1/3)k log k+O(k)]
  + k^(2/3) exp[-(k+1)/10+k^(2/3)]
  + 4k exp[-2(h+1)/35]`.                                     (6.19)

Because `h=k+O(1)`, every term in (6.19) is `O(exp(-k/20))` uniformly for all sufficiently large `n`. This proves (3.1).

Finally,

`m log(1-h/(N+1))=-h+O_{C,A,M}(k^2/n)`,                     (6.20)

so

`M_0=(1-mu)^m=e^{-h}[1+O(k^2/n)]`.                           (6.21)

Since `k^2/n=o(exp(-k/20))` when `k=log n+O(1)`, (3.2) follows.

---

## 7. #29 ADD THE POINTS AT INFINITY — exact boundary obstruction and benign infinity

The dual saddle law admits a useful compactification. Under `nu_0`, put

`z=(x-mu)/(1-mu)`

and then

`y=z/(1-z)=(x-mu)/(1-x)`.

By (5.4), `z~Beta(k+1,m-k)`, so `y` has the corresponding Beta-prime density

`const * y^k(1+y)^(-(m+1))`, `0<y<infinity`.                 (7.1)

Thus `x=1` is literally the added point `y=infinity`.

On `x>=mu`, the unnormalized likelihood ratio of the true clean integrand to the mean-replacement saddle is

`L(x)=(Q_h(x)/(x-mu))^k=(1+r(x))^k`.                         (7.2)

At the point at infinity, `R(1)=0` and the far-sector estimate (6.17) gives `r(x)->0` as `x->1`; hence

`L(x)->1` as `y->infinity`.                                  (7.3)

So the upper boundary is benign; no extra endpoint term is hidden there.

The lower boundary is fundamentally different. As `x downarrow mu`,

`R(x)->E[(B_h-mu)_+]>0`,

while `a=x-mu downarrow0`, so

`r(x)=R(x)/a -> infinity`.                                   (7.4)

Worse, for `x<mu` the mean-replacement integrand is identically zero while the true beta-marked integrand is positive. Therefore the true clean measure is not absolutely continuous with respect to the mean-replacement saddle measure on the full original interval. No globally bounded ordinary Radon--Nikodym derivative can compare the two.

Equation (5.6) is the correct compactified statement: it keeps the below-mean sector as the separate scalar term `theta^k S_-` and uses an exact likelihood ratio only on the mean-saddle support. The near-mean split is therefore not merely a technical defect of Claim 307's local saddle proof; it reflects an actual support singularity.

This is the precise failure of the hoped-for completely split-free likelihood-ratio proof.

---

## 8. Consequences for the repaired P0456 source chain

Claim 308 simplifies but does not enlarge the source theorem.

For the actual clean root, `h=k`, so (3.3) supplies the two-sided relative one-root estimate on the fixed window. The lower fixed-root joint-isolation argument in Claim 306 uses only the clean sufficient external-competitor event and therefore inherits this clean estimate directly. Positive interaction clusters may have bounded quota shifts `h=k-O(1)`, but Claims 303--304 use only an upper bound of the form `exp[-k+o(k)]`; (3.2) is quota-aware and is more than enough for that purpose.

Nothing in Claim 308 changes the defect-complexity bookkeeping, Claim 302's minimum-deadline collision repair, Claim 305's finite Brun total-variation conversion, or Claim 301/306's literal component elimination. In particular, no connectivity conclusion is inferred from mean degree.

The source-level chain remains

`fixed-r joint isolation`
` -> all fixed factorial moments`
` -> Claim-305 finite Brun TV`
` -> literal nontrivial-component elimination`
` -> P(connectivity)=exp(-lambda_n)+o(1)`

uniformly for `|k-log n|<=C`, with `lambda_n=n e^{-k}`.

Claims 288/289 remain internally candidate-complete, not externally closed.

---

## 9. Methods tried and failures

### #5 ADD A PARAMETER AND DIFFERENTIATE IN IT — SUCCESS

The mean-preserving mixture between `delta_mu` and the true beta law makes the integrated clean probability monotone and convex. The endpoint derivative controls the entire relative correction. The derivative does not change sign.

### #11 DUALIZE — SUCCESS WITH A LITERAL HYPOTHESIS BOUNDARY

Normalizing the exact mean-replacement beta integral produces the explicit saddle law `Z~Beta(k+1,m-k)`. The clean correction becomes the expectation (5.8). No named stochastic order is invoked without checking hypotheses.

### #29 ADD THE POINTS AT INFINITY — MIXED: UPPER ENDPOINT SOLVED, LOWER SUPPORT OBSTRUCTION PROVED

The projective coordinate turns `x=1` into a Beta-prime point at infinity, where the likelihood ratio tends to `1`. But the lower endpoint is singular and there is positive true mass below the support of the mean-replacement saddle. A completely split-free ordinary Radon--Nikodym proof is therefore impossible in this formulation. The correct global bookkeeping is (5.6): one singular scalar sector plus a likelihood-ratio expectation on the saddle support.

No finite computational claim was introduced in this run, so no new exact-arithmetic checker was manufactured merely as run evidence.

---

## 10. Cumulative claim/status delta

Preserved source-matching chain:

- `P03-P0456-POISSON-CRITICAL-WINDOW-288 = PROVED / SOURCE-MATCHING-CANDIDATE-COMPLETE / AUDITS-PENDING / PUBLICATION-NOVELTY-UNVERIFIED`.
- `P03-P0456-UNIFORM-POISSON-INTERACTION-REPAIR-289 = PROVED / SELF-AUDIT-REPAIR / SOURCE-MATCHING-STRENGTHENING / AUDITS-PENDING / PUBLICATION-NOVELTY-UNVERIFIED`.
- Claim 290 remains PPP; Claims 291--300 remain supporting self-audit/strengthening kernels.
- `P03-P0456-SOURCE-AUDIT-CAPSULE-301` remains proved only with explicit Repairs/strengthenings 302--308.
- Claims 302--307 retain their previous statuses.

New claim:

`P03-P0456-INTERPOLATED-DUAL-CLEAN-SADDLE-308 = PROVED / SELF-AUDIT-SIMPLIFICATION / SOURCE-MATCHING-SUPPORT / AUDITS-PENDING / PUBLICATION-NOVELTY-UNVERIFIED`.

Metrics:

`c_LK^cert=0 SATURATED`,
`a_LK^fine=0 SATURATED`,
`b_LK^sqrt=0 SATURATED`,
`HARD_RECOVERIES_USED=0/2`.

No `0 -> 0` saturated metric is counted as a stuck run.

Current protocol state:

`P0456_ACTIVE_AUDIT_PENDING / OUTSIDE_AUDITS_FOUND_0_OF_2 / CLAIM_308_INTERPOLATED_DUAL_SADDLE_READY`.

---

## 11. Exact remaining obligations

1. **P26 full-chain audit:** an independent P26 worker must read and verify the repaired source-matching chain, including Claims 288/289 and the auditor-facing repairs 301--308. No such PASS exists in current repository evidence.
2. **One distinct OTHER-track audit:** a genuinely different track must independently pass the same source-matching implication chain. P03 self-checks never count.
3. **Prior art:** current negative searches are bounded evidence only. Publication novelty remains unverified.
4. **Closure/package gate:** only after both outside audits pass may P26 reconcile closure through the shared ledger and only then should the source-matching paper folder be created.

No further coefficient-window optimization is required by the source theorem; all three admitted fixed-coefficient metrics are already saturated.

---

## 12. Next concrete attack

Audit-first remains mandatory. On the next invocation, first reread every incoming P26/OTHER-track audit of Claims 288--308 and repair any concrete objection before new mathematics.

If the outside gate remains 0/2, use a nonconsecutive audit-oriented triple **#2 ATTACK THE NEGATION FIRST, #18 SAY IT IN ANOTHER LANGUAGE, #26 HUNT THE SPORADIC CASE**:

1. adversarially attack the exact fixed-r joint-isolation implication at the smallest nontrivial tuples `r=2,3`, looking specifically for a raw edge or rank event that is not represented in the repaired cluster datum;
2. restate the entire source proof as a finite sigma-field dependency diagram with no asymptotic prose between conditional-law steps, so an outside auditor can verify each factorization locally;
3. hunt sporadic boundary skeletons in which collision blocks, a one-end-early root-root edge, and one active cross edge coexist, and prove they are either impossible or charged by the existing complexity without returning to high-order correction asymptotics.

Do not enlarge the coefficient windows, compute another Poisson correction coefficient, or optimize the component cut split unless an outside auditor identifies a source-level need.

---

## 13. `ledger_delta` for P26

```text
ledger_delta:
  track: P03
  target: P0456
  source_status: OPEN_IN_PRIMARY_SOURCE / SOURCE_MATCHING_CANDIDATE_COMPLETE_INTERNAL
  metrics:
    c_LK^cert: 0 SATURATED
    a_LK^fine: 0 SATURATED
    b_LK^sqrt: 0 SATURATED
    hard_recoveries: 0/2
  add_claim:
    id: P03-P0456-INTERPOLATED-DUAL-CLEAN-SADDLE-308
    status: PROVED / SELF-AUDIT-SIMPLIFICATION / SOURCE-MATCHING-SUPPORT / AUDITS-PENDING / PUBLICATION-NOVELTY-UNVERIFIED
    statement: uniform clean marked integral M=(1-h/(N+1))^m[1+O(exp(-k/20))]=e^-h[1+O(exp(-k/20))] for fixed-window k and bounded parameter shifts; actual clean root has h=k
  preserve:
    claims: 274,276,278,280,282,284,286,288--307
    claim_301: PROVED only with explicit repairs/strengthenings 302--308
  audit_gate:
    p26_full_chain_pass: MISSING
    distinct_other_full_chain_pass: MISSING
    outside_audits_found: 0/2
  p26_request:
    action: independently audit repaired Claims 288/289/301--308 end-to-end when scheduled; do not infer closure from P03 self-audits
  closure: NOT_AUTHORIZED
  paper_package: DO_NOT_CREATE_YET
```

P26 alone may reconcile shared root ledgers. This P03 run does not edit peer files or shared ledgers.

---

## 14. Tool / repository limitations

GitHub was the only persistence/coordination destination. No Gmail, Drive, public posting, paid compute, access change, external script, workflow execution, or extra schedule was used.

Large connector-truncated repository surfaces were not represented as byte-for-byte rereads; target state was recovered through exact paths and scoped searches. Current literature search is bounded and does not certify novelty.

**End of complete run report.**