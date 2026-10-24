Model actually running: **GPT-5.6 Sol. Reasoning level: UNVERIFIED** — this is **not GPT-6 at maximum**; GPT-6 / maximum reasoning was requested, but no authenticated runtime model/effort telemetry or binding selector is exposed.

# H0024 recovery — boundary compactification, excursion law, and negative projective drift

Status: **PARTIAL / SOURCE OPEN**.  This note executes the single recovery action selected in the preceding STUCK1 diagnosis.  It does not classify the full critical line.  It proves new source-valid structure in the simplest finite-variance equality model and corrects one qualitative point in the diagnosis: in the actual finite-variance source, same-frog left/right dependence makes a cross-revival typically arrive with a macroscopic near-side excursion as well, so the cross-revival correction to the projective logarithm is only order `s`, whereas the one-sided normalization loss is order `s log(1/s)`.

Target: H0024, Gustavo Oshiro de Carvalho, Fábio Prates Machado, José Hermenegildo Ramírez-González, *Extinction and Survival in an Interval-Activation Frog Model on Z with Random Survival Parameters and Symmetric Random Walks* (2026), arXiv:2607.27082v1, Theorem 3.5(ii) / Remark 3.6.

Recovery special case: one frog per site; simple symmetric nearest-neighbour walk; finite-variance critical line `beta=1/2`; slowly varying factor tending to the normalization for which the one-sided reach satisfies `P(L>n)~P(R>n)~1/n`.  The source finite-variance bivariate regular-variation statement proved in the preceding R7-05 artifact is reused with its exact hypotheses.

The preceding exact shell kernel is also reused.  In a right-only fresh shell of width `g`, current span `N`, write sites by their distance `h=0,...,g-1` from the right endpoint.  Then

`U=max_h (L_h-(N-h))_+`,

`V=max_h (R_h-h)_+`,

and the next state is `(N+U+V,U,V)`.

Throughout, `s=g/N`.

---

## 1. Input: the finite-variance bivariate tail measure

The preceding R7-05 finite-variance theorem gives, after the equality normalization `P(L>n)~1/n`, a homogeneous bivariate tail kernel

`J(a,b)=a^(-1) H(b/a)`, `a,b>0`,

such that

`n P(L>an, R>bn) -> J(a,b)`.

For simple symmetric nearest-neighbour walk the previously derived function is

`H(t)=1+1/t-[pi/(1+t)] csc(pi/(1+t))`, `t>0`.

The facts used below are

`H(t)=1-(pi^2/6)t+O(t^2)` as `t downarrow 0`,

and, by symmetry/homogeneity,

`H(t)=t^(-1) H(1/t)`.

Consequently the conditional macroscopic opposite excursion given a large excursion to one side has no atom at zero and has an integrable logarithmic singularity there.

No independence between `L` and `R` is assumed or used.

---

# B29 — add the points at infinity: an explicit two-chart boundary compactification

The one-sided face has two different natural scales.  The near-side extension is normally of order `g`; a cross-revival is rare when `s` is small but is of order `N`.  A single Euclidean rescaling hides one of these.  The correct compactification therefore has a **near chart** `(V/g)` and an **excursion chart** `(U/N,V/N)`.

## Theorem 1 (near chart and exact cross-revival mass)

Fix `s in (0,1)`.  Let `N->infinity` and `g/N->s` through integer states with a right-only fresh shell.  Then:

1. for every `z>0`,

   `P(V/g <= z) -> z/(1+z)`;

2. `P(U=0) -> 1-s`, hence `P(U>0)->s`;

3. for every `u>=0`,

   `P(U>uN) -> s/(1+u)`.

### Proof

For the near side,

`P(V<=zg)=prod_{h=0}^{g-1} [1-q_R(h+zg)]`,

where `q_R(m)=P(R>m)~1/m`.  Uniform convergence for regularly varying functions on compact positive ratio intervals gives

`log P(V<=zg)`

`= -sum_{h<g} 1/(h+zg)+o(1)`

`-> -int_0^1 dx/(x+z)`

`= log[z/(1+z)]`.

The sum of squared tails is `O(1/g)`, so the logarithmic replacement is valid.  This proves (1).

Similarly,

`P(U=0)=prod_{h<g}[1-q_L(N-h)]`,

and therefore

`log P(U=0) -> -int_0^s dt/(1-t)=log(1-s)`.

For `u>=0`,

`P(U<=uN)=prod_{h<g}[1-q_L(N(1+u)-h)]`,

hence

`log P(U<=uN) -> -int_0^s dt/(1+u-t)`

`=log[(1+u-s)/(1+u)]`.

Thus `P(U>uN)->s/(1+u)`.  QED.

The second item is useful conceptually: in the macroscopic limiting kernel, the one-sided boundary emits a cross-revival excursion with exactly mass `s`; this is not merely an `O(s)` statement.

## Theorem 2 (excursion chart)

Let `X_s=U/N` and `Y_s=V/N` under the same `N->infinity`, `g/N->s` limit.  Then, as `s downarrow0`, conditional on `U>0`,

`(X_s,Y_s) => (X,Y)`,

where the limiting pair is characterized for `u,v>0` by

`P(X>u,Y>v)=J(1+u,v)`.

In particular,

`P(X>u)=1/(1+u)`,

`P(Y>v)=H(v)`.

Therefore `X>0` and `Y>0` almost surely in the excursion limit.

### Proof

For one fresh site at distance `h=tN` from the right endpoint, the event that this same site produces both `U>uN` and `V>vN` is

`{L>N(1+u-t), R>N(v+t)}`.

By the bivariate regular-variation input, its probability is

`N^(-1) J(1+u-t,v+t)+o(N^(-1))`

uniformly for `t` in compact subintervals of `[0,s]` when `u,v>0`.  Summing over the `g~sN` fresh sites gives

`P(exists one site producing both inequalities)`

`=int_0^s J(1+u-t,v+t) dt+o(s)`.

The probability that the two macroscopic inequalities are produced by two distinct sites is `O(s^2)`: each macroscopic one-sided exceedance has total probability `O(s)`, and different sites are independent.  Hence

`P(U>uN,V>vN)=s J(1+u,v)+o(s)`

as `s downarrow0`, after the `N->infinity` limit.  Theorem 1 gives `P(U>0)=s+o(s)`, so division by the conditioning probability proves the joint survival formula.  Taking `v downarrow0` and using `H(0+)=1` gives the `X` marginal; taking `u downarrow0` gives the `Y` marginal.  The absence of atoms at zero follows because both marginal survival functions tend to one at zero.  QED.

### Consequence: the diagnosis's naive `s log(1/s)` revival gain is absent in the source law

If left/right extremes at a site were treated as independent, a cross-revival could arrive while the near-side extension remained only `O(g)`, and adding `U=O(N)` would increase the fresh-shell logarithm by `log(N/g)=log(1/s)`.  Theorem 2 shows that this is not the typical source event.  Conditional on cross revival, the same source dependence supplies `V=YN` with `Y>0` in the scaling limit.  The projective gain from adding `U` to the already macroscopic `V` is therefore only `O(1)` per cross-revival.  Since cross-revival probability is `O(s)`, its mean correction is only `O(s)`.

---

# B13 — find what only increases/decreases: the boundary projective logarithm has negative leading drift

To avoid the finite-state singularity at immediate absorption, define the regularized next projective score

`Lambda_N(U,V)=log[((U+V) vee 1)/(N+U+V)]`.

The current one-sided state has score `log(g/N)=log s`.  For fixed `s`, the probability of `U+V=0` tends to zero as `N->infinity`, so the regularization does not affect the limiting drift.

Let

`D(s)=lim_{N->infinity, g/N->s} E[ Lambda_N(U,V)-log(g/N) ]`,

whenever the limit is taken along the source special case above.

## Theorem 3 (negative one-sided projective drift)

There is a finite constant `kappa_H in (0,infinity)` such that

`D(s)= -s log(1/s) + kappa_H s + o(s)`

as `s downarrow0`.

In particular, there exists `s_0>0` such that

`D(s)<0` for all `0<s<s_0`.

The constant is the finite excursion expectation

`kappa_H = E[ log(1+X/Y) - log(1+X/(1+Y)) ]`,

with `(X,Y)` from Theorem 2.

### Proof

First ignore the far-side extension `U` and use only `V`.  Write `Z=V/g`.  By Theorem 1, `Z` converges to the beta-prime variable with CDF `z/(1+z)`.  Its logarithm is integrable and

`E log Z=0`.

The exact integral already established in the preceding R7-05 artifact is

`E log(1+sZ)= -s log s/(1-s)`.

Therefore the limiting `V`-only projective drift is

`B(s)=E[log(V/g)-log(1+V/N)]`

`= s log s/(1-s)`

`= -s log(1/s)+o(s)`.

Now compare the full score with the `V`-only score.  Away from the vanishing event `V=0`, the exact correction is

`C_N=log(1+U/V)-log(1+U/(N+V))`,

which is nonnegative and is zero when `U=0`.  Theorem 1 gives `P(U>0)->s`.  Theorem 2 gives, conditional on `U>0` and then `s downarrow0`,

`(U/N,V/N)=>(X,Y)`.

For the limiting correction function

`c(x,y)=log(1+x/y)-log(1+x/(1+y))`,

we have

`0<=c(x,y)<=log(1+x/y)`

`<=log(1+x)+log(1+1/y)`.

The first dominating term is integrable because `P(X>x)=1/(1+x)`, and indeed

`E log(1+X)=int_0^infinity P(X>e^t-1) dt=1`.

The second is integrable because the small-`y` expansion of the source law is

`P(Y<=y)=1-H(y)=(pi^2/6)y+O(y^2)`.

Thus

`E log(1+1/Y)<infinity`.

The large-`Y` tail does not enter this inverse-log bound; finiteness on compact `t` is automatic.  These estimates also give the needed uniform-integrability control after truncating `X` and `1/Y`, applying Theorem 2 on compact rectangles, and then removing the truncation.

Consequently

`E[C_N] = s kappa_H+o(s)`

in the sequential boundary limit.  Adding the `V`-only drift proves

`D(s)=s log s/(1-s)+s kappa_H+o(s)`

`= -s log(1/s)+kappa_H s+o(s)`.

Since `log(1/s)->infinity`, the right-hand side is strictly negative for all sufficiently small `s`.  QED.

### Interpretation

This is the main recovery result.  The earlier STUCK1 diagnosis correctly identified the one-sided projective boundary as the hard place, but it treated the cross-revival as potentially contributing `+s log(1/s)`.  In the actual finite-variance source law, bivariate dependence removes that compensation: conditional on a macroscopic cross-revival, the near-side excursion is itself macroscopic.  The negative normalization term therefore wins by a logarithm.

This theorem does **not** prove extinction.  It controls only the projective shell ratio near a one-sided face.  A process can have negative projective drift while its absolute fresh-shell width remains large or grows.  A closure proof still needs a two-coordinate recurrence argument coupling projective thinness to the absolute shell size.

---

# B26 — hunt the sporadic case: bounded fresh shells are uniformly killable

The other gap left by the thin-shell asymptotics is a bounded fresh shell.

Let

`a=P(L=0,R=0)`.

In the one-frog geometric-lifetime source, `a>0`: the event that the frog dies before making its first jump has probability `E(1-pi)>0` and forces both displacements to vanish.

## Theorem 4 (bounded-shell killing)

Fix `M<infinity`.  At every exploration state with `1<=g=ell+r<=M`, conditional on the entire past,

`P(next state is absorbed) >= a^M >0`.

Consequently, on the event that the breadth-first chain visits `{1<=ell+r<=M}` infinitely often, absorption occurs almost surely.

### Proof

The `g` fresh sites have not yet had their marks exposed and are independent of the exploration past.  If all `g` of them have `(L,R)=(0,0)`, then no fresh site extends either endpoint, so `U=V=0` and the next state is absorbing.  The probability is `a^g>=a^M`.

At the successive stopping times of visits to the bounded-shell set, the same conditional lower bound applies by freshness of the newly exposed shell.  Therefore the conditional probability of surviving the first `k` such visits is at most `(1-a^M)^k`, which tends to zero.  QED.

### Consequence

Any positive-probability survival mechanism in this special equality model must, on its survival trajectories, eventually avoid every fixed bounded-shell set.  Combined with Theorem 3, the remaining escape scenario is now very specific: `g_k->infinity` while the chain repeatedly approaches a one-sided projective face strongly enough that the absolute width can escape despite negative projective drift.

---

## 5. What moved mathematically and what did not

The frozen source metric remains

`G_crit=C_surv/C_ext=1`.

So the source metric has **NO MOVEMENT**.  This note nevertheless replaces the previous qualitative boundary uncertainty by two rigorous structural facts in the mandated recovery model:

1. the source-specific one-sided projective drift is strictly negative to leading order,

   `D(s)=-s log(1/s)+O(s)`;

2. bounded fresh shells have a uniform one-step killing probability and therefore cannot recur infinitely often on survival.

The unresolved bridge is now two-coordinate rather than bivariate-tail: prove that negative projective drift plus the interior positive-drift regime and bounded-shell killing force infinitely many bounded-shell visits (extinction), or construct a trajectory mechanism with `g_k->infinity` and `g_k/N_k->0` that evades them (survival).

The first alternative would settle the recovery special case; the second would identify the exact exceptional escape channel.

## 6. Next nonrepeating methods

Do not repeat B29/B13/B26 immediately.  If ownership and source status remain unchanged, the next ordinary research iteration should use:

- **B7 (take the limit):** derive a genuine two-coordinate Lamperti limit for `(log g, -log(g/N))` in the one-sided layer, using Theorem 3 for the projective drift and the exact beta-prime multiplier for the absolute shell width.
- **B24 (find the extremal object):** optimize the probability of an escape excursion that raises `g` while keeping `g/N` small; identify the extremal cross-revival geometry under the explicit excursion law `J`.
- **B28 (replace for-all by typical):** classify almost-sure survival trajectories into bounded-shell recurrence versus `g->infinity`, and prove a typical-path occupation estimate for the thin one-sided layer rather than a pointwise drift statement.

No full-source closure, no finite critical constant beyond the already matched strict constants, and no novelty claim is made here.