Model actually running: **GPT-5.6 Sol. Reasoning level: UNVERIFIED** — this is **not GPT-6 at maximum**; GPT-6 / maximum reasoning was requested, but no authenticated runtime reasoning-effort telemetry or binding model/effort selector is exposed.

# H0024: a closed-hull series criterion and a source-valid survival family at exact first-order equality

Target: `H0024`, Gustavo Oshiro de Carvalho, Fábio Prates Machado, José Hermenegildo Ramírez-González, *Extinction and Survival in an Interval-Activation Frog Model on Z with Random Survival Parameters and Symmetric Random Walks*, arXiv:2607.27082v1, Theorem 3.5(ii) / Remark 3.6.

Status of the full source after this note: **PARTIAL / OPEN**. The strict constant gap was already closed in the preceding R7-05 run. This note advances the unresolved equality boundary by proving a new general survival criterion and then constructing a source-valid nearest-neighbour frog model that survives although the first-order critical coefficient converges exactly to the threshold value one.

No numerical evidence is used below.

## 1. Setup: directed interval marks and closed hulls

Let `((L_x,R_x))_{x in Z}` be iid copies of an almost surely finite pair `(L,R)` of nonnegative integer-valued random variables. Dependence between `L` and `R` at one site is arbitrary. When site `x` is activated it activates the integer interval

`J_x=[x-L_x,x+R_x] cap Z`.

Starting from one active site, iteration produces an interval at every finite stage. Call a finite integer interval `I=[a,b] cap Z` **closed** if

`J_x subseteq I` for every `x in I`.

For the frog model, after site `x` wakes, the union of all intervals swept by its frogs is exactly of this form with

`L_x=max_i D^<_{x,i}`, `R_x=max_i D^->_{x,i}`.

Hence the directed interval process is not a comparison process here: it is an exact encoding of interval activation.

For `n>=0`, write

`p_n := P([0,n] is closed)`.

If

`F(u,v):=P(L<=u,R<=v)`, then site independence gives the exact product

`p_n = prod_{k=0}^n F(k,n-k)`.                                      (1.1)

A finite activation cluster has a finite interval hull, and that hull is closed. Conversely a closed interval containing the initial site traps the entire activation process. Thus finite activation and existence of a finite closed containing interval are equivalent.

## 2. Method B18 — translate survival into the expected number of closed hulls

The useful language is not generation-by-generation growth but the count of all finite absorbing hulls containing the origin.

Define

`N_0 := # { (i,j) in N_0^2 : [-i,j] is closed }`.

By translation invariance and (1.1),

`E[N_0] = sum_{i,j>=0} p_{i+j}
       = sum_{n>=0} (n+1) p_n`.                                    (2.1)

The following theorem is the key new point.

### Theorem 2.1 (finite closed-hull intensity forces survival)

If

`sum_{n>=0} (n+1) p_n < infinity`,                                (2.2)

then the directed interval-activation process starting from the origin survives with positive probability.

### Proof

Assume for contradiction that the process from the origin is finite almost surely. By translation invariance, the process from every fixed `x in Z` is finite almost surely. Since `Z` is countable, with probability one this holds simultaneously for every `x`.

On that full-probability event let `H(x)` be the finite interval hull of the activation cluster started from `x`. As noted above, `H(x)` is closed.

We now construct infinitely many different finite closed intervals containing zero. Put

`I_0=H(0)=[a_0,b_0]`.

Inductively, suppose `I_k=[a_k,b_k]` is finite and closed. Start the process at the adjacent site `b_k+1`, and let

`H(b_k+1)=[c_k,d_k]`.

Because this hull contains `b_k+1`,

`c_k <= b_k+1 <= d_k`.

Therefore `I_k` and `H(b_k+1)` overlap or are adjacent. Their union is an interval. It is also closed: every site belonging to `I_k` has its whole mark inside `I_k`, and every site belonging to `H(b_k+1)` has its whole mark inside that hull, so every mark in the union stays in the union. Set

`I_{k+1}=I_k union H(b_k+1)`.

Its right endpoint is at least `b_k+1`, hence strictly larger than the right endpoint of `I_k`. Thus the `I_k` are infinitely many distinct finite closed intervals containing zero. Consequently

`N_0=infinity` almost surely.

But (2.2) and (2.1) give `E[N_0]<infinity`, which implies `N_0<infinity` almost surely. Contradiction. Therefore survival has positive probability. QED.

### Interpretation

This argument is deliberately one-way. Divergence of the series in (2.2) is not asserted to imply extinction. What has been proved is the rigorous contrapositive:

`almost-sure extinction => sum_n (n+1)p_n = infinity`.             (2.3)

It is a global obstruction to extinction that is invisible to a pointwise tail coefficient.

## 3. Method B27 — swap pointwise tail inequalities for a cumulative product criterion

Assume now that the two marginal tails agree:

`q_n=P(L>n)=P(R>n)`, `f_n=1-q_n`,

and define

`A_m=prod_{k=0}^m f_k`, with `A_{-1}=1`.

Since

`F(u,v) <= min(P(L<=u),P(R<=v)) = f_{min(u,v)}`,

(1.1) yields, for `m>=0`,

`p_{2m+1} <= A_m^2`,

and

`p_{2m} <= f_m A_{m-1}^2 <= A_{m-1}^2`.                           (3.1)

Therefore a simple tail-only sufficient condition for survival is

`sum_{n>=1} n A_{floor((n-1)/2)}^2 < infinity`.                    (3.2)

This changes the quantifiers relative to the source criterion. The source proves survival from a uniform eventual pointwise inequality `liminf n q_n>1` (after the H0024 normalization). Criterion (3.2) only asks that the **cumulative** excess in the tail be strong enough to make one series summable. The normalized coefficient may converge to one and may even cross one repeatedly.

If `q_n=O(1/n)`, then `sum q_n^2<infinity` and

`A_n = exp(-sum_{k<=n} q_k + O(1))`.                               (3.3)

Thus another convenient sufficient condition is

`sum_{n>=1} n exp(-2 sum_{k<=n/2}q_k) < infinity`.                 (3.4)

No independence of `L` and `R` within a site is used anywhere in Theorem 2.1 or (3.1)-(3.4).

## 4. Logarithmic boundary corollary

Suppose

`q_n = (1/n)(1 + a/log n + O(1/(log n)^2))`                       (4.1)

for some `a>1/2`. Then

`sum_{k<=n} q_k = log n + a log log n + O(1)`,                    (4.2)

because `sum 1/(k(log k)^2)<infinity`. Since `sum q_k^2<infinity`, (3.3) gives

`A_n asymp 1/(n (log n)^a)`.                                      (4.3)

Combining (3.1) and (4.3),

`(n+1)p_n <= C/(n (log n)^{2a})`

for all large `n`. Since `2a>1`, the closed-hull series converges. Theorem 2.1 gives:

### Corollary 4.1

For arbitrary within-site dependence between the two directed reaches, (4.1) with `a>1/2` implies positive-probability survival.

In particular, the first-order equality `n q_n -> 1` does **not** force extinction.

The number `1/2` here is the exact convergence threshold of this proved series mechanism. This note does not claim that `a=1/2` is the full process threshold.

## 5. Method B4 — a complete source-valid equality family

We now realize Corollary 4.1 inside the exact H0024 source hypotheses, rather than in an abstract interval model.

Take:

1. exactly one frog at every site, `eta_x=1`, so `m=E[eta_0]=1`;
2. simple symmetric nearest-neighbour random walk, so the source finite-variance regime has `sigma^2=1`, `r=2`, and the source constant is `kappa=sqrt(2)`;
3. the critical lifetime-density exponent `beta=1/2`;
4. a parameter `a>1/2` and a slowly varying function satisfying, for all sufficiently large `x`,

`ell(x) = (1/sqrt(2)) (1 + 2a/log x)`.                             (5.1)

Choose the survival-parameter density near one to be exactly

`f_pi(p)=(1-p)^(-1/2) ell((1-p)^(-1))`.                            (5.2)

By taking the neighbourhood of one sufficiently small, its total mass is less than one; complete the density arbitrarily on the remaining compact subinterval so that it integrates to one. This preserves (5.2) near one and therefore satisfies the source assumption.

Equation (5.1) has

`ell(x) -> 1/sqrt(2) = 1/(m kappa)`.                               (5.3)

Thus this family lies exactly on the unresolved first-order equality boundary: the source's strict survival hypothesis `liminf ell(n^2)>1/sqrt(2)` does not apply.

### Lemma 5.1 (exact nearest-neighbour first-passage transform)

Let `tau_n^+` be the first time simple symmetric random walk started at zero hits `n`. For `0<p<1`,

`E[p^{tau_n^+}] = lambda(p)^n`,

where

`lambda(p)=(1-sqrt(1-p^2))/p = exp(-arcosh(1/p))`.                 (5.4)

Proof: the function `u_j=E_j[p^{tau_n^+}]` solves

`u_j=(p/2)(u_{j-1}+u_{j+1})`, `j<n`, `u_n=1`,

with the bounded solution proportional to the root `lambda^{-1}`/`lambda` of the characteristic equation. The root in `(0,1)` is the displayed `lambda`, and translation gives `u_0=lambda^n`. QED.

For a frog with geometric lifetime satisfying `P(L>=k | pi=p)=p^k`, the event `D^->>=n` occurs exactly when `L>=tau_n^+`. Hence, with

`s_n=P(D^->>=n)`,

(5.4) gives

`s_n = integral_0^1 lambda(p)^n f_pi(p) dp`.                       (5.5)

### Lemma 5.2 (second-order critical tail)

For the density (5.1)-(5.2),

`s_n = (1/n)(1 + a/log n + O(1/(log n)^2))`.                       (5.6)

#### Proof

Set

`theta=arcosh(1/p)`, so `p=sech(theta)` and `lambda(p)=e^{-theta}`.

As `theta downarrow 0`,

`1-sech(theta)=theta^2/2+O(theta^4)`,

and

`(1-sech(theta))^{-1/2} sech(theta)tanh(theta)
   = sqrt(2)(1+O(theta^2))`.                                       (5.7)

Using (5.1), the density times the Jacobian in (5.5) therefore becomes

`[1 + 2a/log(1/(1-sech theta)) + O(theta^2)] dtheta`               (5.8)

for small `theta`. Since

`log(1/(1-sech theta)) = log(2/theta^2)+O(theta^2)`,               (5.9)

(5.5), after the change `z=n theta`, is

`n s_n
 = integral_0^infinity e^{-z}
   [1 + 2a/(2 log n + log 2 - 2 log z) + O(1/(log n)^2)] dz
   + O(1/(log n)^2)`.                                              (5.10)

The displayed expansion is justified by splitting the integral into a fixed central `z` range and its small/large tails; `integral e^{-z}|log z| dz<infinity`, while the part of (5.5) with `p` bounded away from one is exponentially small in `n`.

Finally,

`2a/(2 log n + log 2 - 2 log z)
 = a/log n + O((1+|log z|)/(log n)^2)`

on the central range. Integrating and using `integral_0^infinity e^{-z}dz=1` proves (5.6). QED.

### Theorem 5.3 (source-valid survival at exact first-order equality)

For every `a>1/2`, the H0024 model specified in items 1-4 above survives with positive probability, although

`ell(n^2) -> 1/(E[eta_0] kappa)`.                                  (5.11)

#### Proof

With one frog per site, the site right-reach tail is

`q_n=P(R_0>n)=P(D^->>=n+1)=s_{n+1}`.

By (5.6),

`q_n=(1/n)(1+a/log n+O(1/(log n)^2))`.

The left and right reaches of one frog may be strongly dependent, but Corollary 4.1 permits arbitrary within-site dependence. Hence the exact interval-activation frog model survives with positive probability. Equation (5.3) gives the equality statement. QED.

## 6. What this proves about the source boundary

The preceding R7-05 run proved almost-sure extinction whenever the normalized first-order coefficient has strict upper limit below one, matching the source's strict survival constant. Theorem 5.3 now shows something qualitatively new at the missing equality boundary:

`first-order equality does not have a universal extinction verdict.`

At least one explicit logarithmic approach from the survival side,

`m kappa ell(n^2)=1+a/log n+O(1/(log n)^2)`, `a>1/2`,

still survives.

More generally, Theorem 2.1 and (3.2) supply a cumulative criterion that can handle some oscillatory/nonuniform tails for which no strict `liminf n q_n>1` is available.

What is **not** proved:

- the converse of the closed-hull series criterion;
- extinction at exact equality or under logarithmic approach from below;
- the borderline `a=1/2`;
- a full necessary-and-sufficient classification for every slowly varying `ell` allowed by H0024;
- independent closure audits or a paper package.

Therefore the source remains **PARTIAL / OPEN**.

## 7. Relation to known rumour/firework criteria

Roy-Saha's symmetric one-radius rumour model has an exact criterion in terms of the one-boundary product `a_n=prod_{i=0}^n P(I_0<=i)`: their Proposition 3.1 says no percolation iff `sum a_n` diverges. The present result is not imported from that theorem. H0024 has a genuinely directed pair `(L_x,R_x)` with arbitrary same-site dependence. The new quantity `sum (n+1)p_n` counts two-boundary closed hulls, and Theorem 2.1 is proved directly above.

The comparison is nevertheless informative: the one-sided product series is replaced here by the intensity of finite two-boundary absorbing hulls.

## 8. Frozen metric and next obstruction

The R7-05 frozen metric is

`G_crit=C_surv/C_ext`.

It was already moved to its optimal strict-constant value `1` in the preceding run. This note does not redefine that metric, so

`G_crit: 1 -> 1` (**NO MOVEMENT**).

The mathematical scope nevertheless advances: a previously unresolved equality family is proved to survive.

The central remaining obstruction is now a converse/near-converse question for the two-boundary series:

`Does divergence of sum_n (n+1)p_n, under the H0024 directed-pair structure, force almost-sure extinction, and if not, what extra renewal invariant separates the two behaviours?`

The next ordinary methods should be different from B4/B18/B27:

- **B12 — find what is conserved:** search for a renewal/mass-transport invariant of minimal closed hulls that could turn the necessary divergence condition into a criterion;
- **B15 — break the symmetry on purpose:** analyze unequal left/right second-order tails to identify which cumulative exponent controls the two-boundary process;
- **B30 — one scale at a time:** solve logarithmic blocks and identify the exact gluing obstruction across scales, especially at `a<=1/2`.
