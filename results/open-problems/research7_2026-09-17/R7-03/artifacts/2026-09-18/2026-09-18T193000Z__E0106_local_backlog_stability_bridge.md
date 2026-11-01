Model actually running: **GPT-5.6 Sol. Reasoning level: UNVERIFIED** — this is **not GPT-6 at maximum**; no authenticated runtime model/effort telemetry or binding selector is exposed.

# E0106 / Konstantopoulos Open Problem 5 — local-backlog stability theorem and source-scope boundary

Date of source/status check: 2026-09-18 UTC  
R7-03 native ID: `6aabe7be74008191b526b109ee4e9e80`  
Run start snapshot: `52c62596ee2a1d70730c1d06cf6af3481b022923`  
Fresh pre-write master: `d689f81ee0daa75224433e7c3a9dbc3c9c6196c5`

## 1. Why this candidate reappeared

The older R7-03 admission cursor called the residue-2 E slice complete after `E0095`. That was a history/cursor gap: the canonical intake continues beyond `E0095`, and `E0106` satisfies the exact shard rule

```text
sum(ord(c) for c in "E0106") % 7 = 2.
```

No `operations/claims/E0106.md` existed at the fresh pre-write master. I therefore screened E0106 as an existing canonical outside-source candidate rather than inventing a new problem.

## 2. Exact outside source and source statement

- Author: Takis Konstantopoulos.
- Title: *The mobile Boolean model: an overview and further results*.
- arXiv: `1407.6834`, submitted 25 July 2014; the manuscript itself is dated 11 July 2013.
- URL: `https://arxiv.org/abs/1407.6834`.
- Exact locator: **Open problem 5**, printed PDF p. 18 (PDF page index 17 in the arXiv file).
- Canonical intake: `probability_1000_intake_E_20260908/problems.jsonl`, `E0106`.

The source introduces an independent space-time Poisson process of customers in `R^d x R_+`; the Brownian Boolean model is an exogenous space-time serving mechanism that clears customer points whenever it meets them; it asks for necessary and sufficient **stability conditions**.

The source does not define, in or immediately around Open Problem 5, the state space or the word `stability`: it does not say whether the intended criterion is local finiteness of backlog, existence of a translation-invariant stationary backlog, finite local mean, positive recurrence of a finite-volume truncation, or some other queueing notion. That missing predicate is the source-scope issue at the end of this note.

The source does, however, give the exact Poisson-void formula for detection. For a homogeneous mobile Boolean model with center intensity `lambda`, Brownian motion `B`, deterministic grain `D`, and target `K`,

```text
P(S_K > t)
 = exp(-lambda E vol( union_{0<=s<=t} [B_s + D - K] )).
```

For a point target and a ball grain of radius `r`, the exponent is the expected volume of the radius-`r` Wiener sausage.

## 3. Correction of the previous E0106 attempt

The canonical prior attempt `E0106-A001` compared the customer arrival intensity with the asymptotic growth rate of expected Wiener-sausage volume. It inferred a dimension-dependent traffic-capacity threshold and suggested instability for every positive arrival rate in low dimensions.

That comparison is not valid for the source mechanism as written. The Brownian Boolean service field is **exogenous and nonexclusive**: clearing one customer does not consume service capacity, delay a sensor, or prevent the same grain from clearing arbitrarily many other customers. There is therefore no conservation law of the form

```text
customer input rate < service-volume production rate.
```

The correct primitive quantity for local backlog is instead the **waiting time of one customer**. If that waiting time has finite mean, a Campbell/Fubini calculation gives a finite stationary customer density for every finite arrival intensity.

This is the obstruction-first outcome of this screen: the earlier low-dimensional `capacity balance` is a false route, not evidence of instability.

## 4. A pathwise Wiener-sausage bound valid in every dimension

Let `gamma:[0,t] -> R^d` be any continuous path and let

```text
W_r(gamma,t) = union_{0<=s<=t} (gamma(s) + B_r),
```

where `B_r` is the closed Euclidean ball of radius `r>0`. Write

```text
m = min_{0<=s<=t} gamma_1(s),
M = max_{0<=s<=t} gamma_1(s).
```

### Lemma 4.1 (projection-range lower bound)

For every continuous path,

```text
vol_d(W_r(gamma,t))
 >= omega_{d-1} r^{d-1} (M-m),                       (4.1)
```

with the usual convention `omega_0=1`.

### Proof

For every `y in [m,M]`, continuity of the first coordinate gives some time `s_y` with `gamma_1(s_y)=y`. In the hyperplane `{x_1=y}`, the ball `gamma(s_y)+B_r` has a `(d-1)`-dimensional cross-section equal to a radius-`r` ball, hence of measure `omega_{d-1}r^{d-1}`. The slice of the entire union at coordinate `y` contains that cross-section. Integrating the slice measures over `y in [m,M]` by Fubini gives (4.1). No disjointness of the moving balls is needed. QED.

Now let `B` be standard `d`-dimensional Brownian motion. The first coordinate is standard one-dimensional Brownian motion, whose range satisfies

```text
E[max_{s<=t} B_s^1 - min_{s<=t} B_s^1]
 = 2 sqrt(2t/pi).
```

Therefore

```text
E vol_d(W_r(B,t))
 >= c_{d,r} sqrt(t),

c_{d,r} := 2 omega_{d-1} r^{d-1} sqrt(2/pi) > 0.     (4.2)
```

The bound is deliberately crude. Its value is that it is uniform across dimensions and needs no detailed Wiener-sausage asymptotics.

## 5. One-customer waiting time has finite mean in every dimension

Consider the homogeneous Brownian Boolean model with germ intensity `lambda>0`, independent standard Brownian motions, and ball grain `B_r`, `r>0`. Let `T` be the time from a stationary observation epoch until a fixed point is first covered by the service field, counting time zero as in the source detection convention.

By the source's Poisson-void identity and (4.2),

```text
P(T>t)
 = exp(-lambda E vol_d(W_r(B,t)))
 <= exp(-lambda c_{d,r} sqrt(t)).                     (5.1)
```

Hence

```text
E T
 = integral_0^infinity P(T>t) dt
 <= integral_0^infinity exp(-a sqrt(t)) dt
 = 2/a^2
 < infinity,                                           (5.2)
```

where `a=lambda c_{d,r}>0`.

Thus a point customer has finite mean service delay for every `d>=1`, every positive mobile-particle intensity, and every positive sensing radius. In particular there is no special instability at `d=1` or `d=2` under this exogenous service model.

The source itself derives much sharper dimension-dependent detection asymptotics; for example it records exponential-scale behavior `exp(-2 pi lambda t/log t)` in dimension two. Such a tail is also integrable. The elementary bound above is enough for stability and avoids needing those sharp asymptotics.

## 6. Translation to a stationary backlog and exact mean density

To state a rigorous queueing theorem, extend the Brownian service system to two-sided time in the standard stationary way: at time zero the mobile centers form a homogeneous Poisson process of intensity `lambda`, and each center carries an independent two-sided Brownian trajectory. Let independent customer arrivals form a space-time Poisson process of intensity `nu dx dt`.

A customer `(x,s)` remains present at time `t>=s` exactly when the service field has not covered `x` during `[s,t]`.

For a bounded Borel set `A`, let `N_0(A)` be the number of customers located in `A` at time zero that arrived at some time `s<=0` and have not yet been cleared.

### Theorem 6.1 (stationary local-backlog stability)

For `lambda>0`, `r>0`, `d>=1`, and every finite customer intensity `nu<infinity`, the above construction gives a time-translation invariant backlog process that is locally finite almost surely. Moreover,

```text
E N_0(A) = nu |A| E T,                                (6.1)
```

and in particular the stationary mean customer density is exactly

```text
rho_backlog = nu E T < infinity.                      (6.2)
```

### Proof

Condition on a customer arrival at `(x,-u)`, `u>=0`. By independence of customer arrivals and the service field, and by spatial/time stationarity of the two-sided Brownian Boolean model, the probability that this customer is still present at time zero is exactly `P(T>u)`.

Campbell's theorem for the space-time Poisson arrival process, followed by Tonelli, gives

```text
E N_0(A)
 = nu integral_A dx integral_0^infinity P(T>u) du
 = nu |A| E T.
```

Equation (5.2) makes this finite. Since `N_0(A)` is a nonnegative integer-valued random variable, finite expectation implies `N_0(A)<infinity` almost surely. Applying this to a countable exhaustion of `R^d` by bounded boxes proves local finiteness of the entire stationary backlog. Time-translation invariance follows from the two-sided stationary construction. QED.

### Corollary 6.2 (monotone convergence from empty past)

Start the customer system empty at time `-L` while using the stationary service field, and inspect it at time zero. For each bounded `A`, the resulting count `N_0^{(L)}(A)` increases monotonically with `L` and

```text
N_0^{(L)}(A) -> N_0(A) < infinity almost surely.       (6.3)
```

Thus the stationary local backlog is not merely an abstract invariant measure: it is the monotone limit of finite-past systems on every bounded observation window.

### Proof

Increasing `L` only adds older arrivals. The union over all finite `L` is exactly the set of all arrivals from `(-infinity,0]` that survived until zero, which defines `N_0(A)`. Theorem 6.1 shows the limit is finite almost surely. QED.

## 7. Boundary cases for the ball-grain model

The theorem above assumes the canonical nondegenerate Brownian Boolean model `lambda>0`, `r>0`.

- If `nu=0`, the backlog is empty, trivially.
- If `nu>0` and `lambda=0`, there is no service. A bounded set of positive volume receives customers forever, so no locally finite stationary backlog can be obtained from the infinite past.
- If one allows the degenerate point-grain case `r=0`, dimension matters for a different reason. In `d>=2`, a Brownian path has zero `d`-dimensional Lebesgue measure, so the source void formula for a point target gives detection probability zero; positive customer input is then unstable under the local-backlog criterion. In `d=1`, the Brownian path sweeps an interval of positive length and the range estimate still yields an integrable detection tail.

Thus, for the standard positive-radius model, **every finite arrival intensity is locally stable**; a nontrivial traffic threshold does not appear because service is nonexclusive.

## 8. What this does and does not settle

This is a complete theorem for the following precise and natural interpretation of `stability`:

> existence of a time-stationary, spatially translation-invariant backlog obtained from arrivals in the infinite past, locally finite almost surely and with finite mean customer density, together with local convergence from the empty finite-past construction.

Under that interpretation, the canonical positive-radius Brownian Boolean model is stable for every finite customer intensity, in every dimension, whenever the mobile-particle intensity is positive.

However, **I do not promote E0106 to PROVED or admit it as the R7-03 target in this run**, because the source does not specify that this is the intended stability predicate. If the author intended positive recurrence of a particular finite-volume Markov queue, a workload process with service competition, or another state variable, the model required to formulate that criterion is absent from Open Problem 5. Choosing one silently would change the source question.

The correct R7-03 disposition is therefore:

```text
E0106: SOURCE-SCOPE AMBIGUITY / HOLD FOR ADMISSION,
with a proved local-backlog theorem and a corrected prior heuristic.
```

This is substantive progress but not source-level closure.

## 9. Current-status / prior-art check

On 2026-09-18 I checked:

- the current arXiv record and full source text for `1407.6834`;
- the author's available copy of the paper, which still prints Open Problem 5;
- bounded web searches for `Brownian Boolean model stability customers queueing`, `mobile Boolean stability customers queueing`, and closely matching phrases;
- nearby later work on spatial queue stability/Poisson hail and 2026 Boolean/Brownian geometry.

The search recovered the original problem and related but different queueing models, including Poisson hail; it did not recover a later paper explicitly defining and resolving this exact exogenous Brownian-Boolean customer-stability problem. That is **negative evidence only**, not a proof of current openness or novelty.

## 10. Section-B methods and outcome

The immediately preceding R7-03 triple was B2/B6/B30, so this screen used a different triple.

1. **B18 — SAY IT IN ANOTHER LANGUAGE.** Translate `stability` into a stationary random-measure/backlog question. This exposes the one-customer detection time as the correct primitive.
2. **B23 — DO WHAT THE PROPOSER DID NOT EXPECT.** Test the opposite of a dimension-dependent traffic threshold. Because service is exogenous and nonexclusive, the result is that all finite arrival rates are stable under the local-backlog criterion for positive radius.
3. **B25 — COUNT THE SAME THING TWICE.** Campbell/Tonelli counts surviving customers by arrival age and yields the exact identity `mean backlog density = nu E T`.

The decisive auxiliary idea is the pathwise projection-range lower bound (4.1), which proves `E T<infinity` without sharp Wiener-sausage theory.

## 11. Remaining source-level blocker

The exact blocker is semantic but mathematical:

```text
What state process and recurrence/tightness property does Open Problem 5 mean by "stability"?
```

Until that is fixed by a source-valid later definition or an author-linked formulation, treating Theorem 6.1 as the unique source closure criterion would be an unsupported strengthening of the intake transcription.

No canonical claim is created in this run.