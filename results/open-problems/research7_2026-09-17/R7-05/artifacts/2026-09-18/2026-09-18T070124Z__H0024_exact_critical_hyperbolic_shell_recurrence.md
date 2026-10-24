Model actually running: **GPT-5.6 Sol. Reasoning level: UNVERIFIED** — this is **not GPT-6 at maximum**; GPT-6 / maximum reasoning was requested, but no authenticated runtime model/effort telemetry or binding selector is exposed.

# H0024 — an exact critical source law, harmonic shell identities, and the recurrent logarithmic limit

Target: `H0024`, Gustavo Oshiro de Carvalho, Fábio Prates Machado, José Hermenegildo Ramírez-González, *Extinction and Survival in an Interval-Activation Frog Model on Z with Random Survival Parameters and Symmetric Random Walks* (2026), arXiv:2607.27082v1, Theorem 3.5(ii) / Remark 3.6.

Run-start master: `f7e9092a2de8687deb482a6a4e780ab2c383bcc0`.
Fresh pre-write master: `a0ac2724202cac7887e1f2f374a19a380b046b72`.
Canonical claim: `operations/claims/H0024.md` remains `CLAIMED / ACTIVE` by R7-05.
Previous report: `research7_2026-09-17/R7-05/runs/2026-09-18/2026-09-18T055000Z__report.md` @ `04957b731ee82bcb1aa9014c0d0767ebd63e0cc1`.

Status remains **PARTIAL / SOURCE OPEN**.  The full critical-line source is not settled here.  The point of this note is to replace the asymptotic “simplest equality model” used in the preceding recovery run by a literal exactly solvable source law, derive exact shell identities for that law, and determine the correct limiting category of the thin-shell dynamics.

The three methods are **B7 / B24 / B28**.  The mathematical idea precedes computation; no simulation is used.

---

## 1. B7 — take the limit, but first make the equality model exact

The previous recovery isolated the one-frog, one-frog-per-site, simple symmetric nearest-neighbour finite-variance case at the normalized first-order equality

`n P(D^+ >= n) -> 1`.

There is a particularly clean source-valid law for which this equality is not merely asymptotic.

### Definition 1.1 (hyperbolic critical survival law)

Let `T` be exponential with rate one and set

`pi = sech(T)`.

Given `pi`, give the frog the source geometric lifetime

`P(L >= k | pi)=pi^k`, `k>=0`,

and let its motion be simple symmetric nearest-neighbour random walk.

### Proposition 1.2 (this is exactly a source critical-line law)

The density of `pi` is

`f_pi(p)= exp(-arcosh(1/p)) / [p sqrt(1-p^2)]`, `0<p<1`,             (1.1)

and therefore

`f_pi(p) ~ [2(1-p)]^(-1/2)` as `p up to 1`.                       (1.2)

Thus the source exponent is `beta=1/2`, and its slowly varying factor tends to

`ell(x) -> 1/sqrt(2)`.

For simple symmetric nearest-neighbour motion the source has `kappa=sqrt(2)`, so with one frog per site

`E[eta_0] kappa ell(n^2) -> 1`.                                    (1.3)

Hence this model sits at the literal unresolved first-order equality, not on either strict side.

#### Proof

The change of variables `p=sech t` gives

`|dt/dp|=1/[p tanh t]=1/[p sqrt(1-p^2)]`.

Multiplying by the exponential density `e^{-t}` proves (1.1).  As `p up to 1`, `t=arcosh(1/p)~sqrt(2(1-p))`, so `e^{-t}->1` and `sqrt(1-p^2)~sqrt(2(1-p))`; this gives (1.2).  An asymptotically positive constant is slowly varying, and the source's nearest-neighbour constant `kappa=sqrt(2)` then gives (1.3).  QED.

### Proposition 1.3 (the one-sided displacement tail is exact)

For every integer `n>=0`,

`P(D^+ >= n)=1/(n+1)`.                                             (1.4)

Consequently, for the directed site mark `(L,R)=(D^-,D^+)`,

`P(L>m)=P(R>m)=1/(m+2)`, `m>=0`.                                  (1.5)

#### Proof

For a fixed survival parameter `p`, let `tau_n` be the first time simple symmetric random walk started at zero reaches `n`.  The function

`h(j)=E_j[p^{tau_n}]`

satisfies

`h(j)=(p/2)(h(j-1)+h(j+1))`, `j<n`, `h(n)=1`,

with the bounded-at-minus-infinity solution.  Write `p=sech t`.  The characteristic equation has the root `e^{-t}` because

`(p/2)(e^t+e^{-t})=sech(t) cosh(t)=1`.

Therefore

`E_0[p^{tau_n}]=e^{-nt}`.

A frog reaches `n` before death exactly when its lifetime is at least `tau_n`, so averaging over `T~Exp(1)` gives

`P(D^+>=n)=int_0^infinity e^{-nt} e^{-t} dt=1/(n+1)`.

Symmetry gives the same left tail, and replacing `n` by `m+1` gives (1.5).  QED.

This turns the recovery model into an exact finite-state algebra problem: all one-sided shell products telescope.

### Proposition 1.4 (the same-site pair law is also explicit)

For integers `a,b>=0`, let

`F(a,b)=P(D^-<=a,D^+<=b)`.

Then

`F(a,b)=1-int_0^infinity e^{-t}
  [sinh((a+1)t)+sinh((b+1)t)]/sinh((a+b+2)t) dt`                   (1.6)

or equivalently

`F(a,b)=1-int_0^infinity e^{-t}
  cosh((a-b)t/2)/cosh((a+b+2)t/2) dt`.                            (1.7)

#### Proof

Conditional on `T=t`, set `p=sech t`.  The event complementary to `{D^-<=a,D^+<=b}` is that the walk exits the interval `[-a-1,b+1]` before its geometric death.  If `tau` is that exit time, its conditional probability is `E[p^tau]`.  Solving the same second-order difference equation now with boundary value one at both endpoints gives

`E[p^tau]=[sinh((a+1)t)+sinh((b+1)t)]/sinh((a+b+2)t)`.

Averaging against `e^{-t}dt` gives (1.6), and the elementary hyperbolic addition identity gives (1.7).  QED.

Thus the exact critical special case retains the genuine same-frog left/right dependence; no independent-front surrogate is being used.

---

## 2. Exact shell marginals in the full breadth-first chain

Use the previously proved exact shell state.  Translate the current activated interval to `[0,N]`.  Suppose the newly exposed shell consists of

- `ell` sites at `0,...,ell-1`,
- `r` sites at `N-r+1,...,N`,

with `g=ell+r>0` and `g<=N` because the preceding interval is nonempty.  Let `(U,V)` be the next left and right extension counts.  The next state is

`(N,ell,r) -> (N+U+V,U,V)`.

Even though `U,V` are dependent, their *marginals* use only (1.5), so they telescope exactly.

### Proposition 2.1 (exact marginal CDFs)

For every integer `u,v>=0`,

`P(U<=u | N,ell,r)
 = [(u+1)/(u+ell+1)] [(u+N-r+2)/(u+N+2)]`,                       (2.1)

and

`P(V<=v | N,ell,r)
 = [(v+1)/(v+r+1)] [(v+N-ell+2)/(v+N+2)]`.                        (2.2)

#### Proof

A fresh site at translated position `j` creates no left extension beyond `u` iff `L<=j+u`.  By (1.5),

`P(L<=m)=(m+1)/(m+2)`.

Multiplying over `j=0,...,ell-1` telescopes to `(u+1)/(u+ell+1)`. Multiplying over `j=N-r+1,...,N` telescopes to `(u+N-r+2)/(u+N+2)`. This proves (2.1).  The right formula follows by reflection. QED.

For a one-sided right shell `(ell,r)=(0,g)`, (2.1)-(2.2) immediately give the exact identities

`P(U>0 | N,0,g)=g/(N+2)`,                                         (2.3)

`P(V<=v | N,0,g)=(v+1)/(v+g+1)`,                                  (2.4)

and hence

`P(V>=k | N,0,g)=g/(g+k)`, `k>=1`.                                (2.5)

In particular the opposite-side revival hazard and the near-side macroscopic-jump hazard have the same first order:

`P(U>0)=g/(N+2)`,

`P(V>=N)=g/(g+N)`.                                                  (2.6)

When `g/N->0`, their ratio tends one.  This is an exact finite-state version of the previous boundary-scale diagnosis.

---

## 3. B24 — the extremal object is the harmonic-number scale

Write

`H_0=0`, `H_m=sum_{j=1}^m 1/j`.

The exact critical one-sided marginal kernel has `H_m` as its harmonic scale.

### Theorem 3.1 (exact shell harmonic-drift identity)

For the full source-valid shell chain,

`E[H_U | N,ell,r]
 = [(N+1-g)/(N+1-ell)] H_ell
   + [r/(N+1-ell)] H_{N+1}`,                                      (3.1)

`E[H_V | N,ell,r]
 = [(N+1-g)/(N+1-r)] H_r
   + [ell/(N+1-r)] H_{N+1}`.                                      (3.2)

Therefore

`E[H_U+H_V | N,ell,r] - (H_ell+H_r)`
` = [r/(N+1-ell)](H_{N+1}-H_ell)
  + [ell/(N+1-r)](H_{N+1}-H_r) >= 0`.                             (3.3)

The inequality is strict at every nonabsorbed shell state `g>0`.

For a one-sided right shell this specializes to

`E[H_U+H_V | N,0,g]-H_g
 = [g/(N+1)] H_{N+1}`.                                              (3.4)

#### Proof

Use the tail-sum identity

`E H_U=sum_{k>=1} P(U>=k)/k`.

Putting `u=k-1` in (2.1) gives

`P(U>=k)
 =1-[k/(k+ell)] [(k+N-r+1)/(k+N+1)]`
` =[g k+ell(N+1)]/[(k+ell)(k+N+1)]`.                               (3.5)

The exact partial-fraction decomposition is

`P(U>=k)
 = [ell(N+1-g)/(N+1-ell)] 1/(k+ell)
   + [r(N+1)/(N+1-ell)] 1/(k+N+1)`.                               (3.6)

Now use

`sum_{k>=1} 1/[k(k+m)]=H_m/m`, `m>=1`,

with the zero-coefficient limiting interpretation when `m=0`.  Equation (3.1) follows. Reflection gives (3.2); subtraction gives (3.3), and setting `ell=0,r=g` gives (3.4). QED.

The identity is useful because it separates the two mechanisms cleanly.  The near-side critical multiplier by itself has zero harmonic drift; all positive drift in (3.3) is the contribution of the opposite fresh block.

### Theorem 3.2 (the pure one-sided marginal chain is absorbed almost surely)

Consider the auxiliary Markov chain `G_n` on `N_0` with `0` absorbing and, for `g>=1`,

`P(G_{n+1}<=v | G_n=g)=(v+1)/(v+g+1)`.                            (3.7)

Then

`H_{G_n}` is a nonnegative martingale and

`P_g(tau_0<infinity)=1` for every finite `g`.

#### Proof

From (2.5),

`P(G_{n+1}>=k | G_n=g)=g/(g+k)`.

Therefore

`E[H_{G_{n+1}} | G_n=g]
 =sum_{k>=1} [1/k] g/(g+k)
 =sum_{k>=1}(1/k-1/(g+k))
 =H_g`.                                                            (3.8)

So `H_{G_n}` is a nonnegative martingale and converges to a finite limit almost surely.  On a hypothetical nonabsorption event, finite convergence of `H_{G_n}` forces `G_n` eventually into a finite set because `H_g up to infinity` as `g up to infinity`.  If `1<=G_n<=K`, then by (3.7)

`P(G_{n+1}=0 | G_n)>=1/(K+1)`.

An infinite tail inside that finite set therefore avoids zero with conditional probability at most `(1-1/(K+1))^m` over the next `m` steps, which tends to zero. Contradiction. QED.

This theorem is deliberately about the **marginal one-sided kernel**, not the actual shell chain conditioned on `U=0`; same-site dependence changes that conditional law.  Its role is to identify the exact critical scale.  The full process can escape the one-sided critical martingale only through the cross-side mechanism quantified by (2.3) and (3.4).

The combination of (2.3), (2.5), and (3.4) sharpens the previous blocker: a surviving equality trajectory cannot be explained by repeated near-side critical growth alone.  It must extract enough mass from cross-side revivals, whose per-step hazard is exactly `g/(N+2)` and whose harmonic injection is of order `(g/N) log N`.

---

## 4. B7 continued — the interior thin-shell limit is a planar centered random walk in log coordinates

The preceding R7-05 shell theorem proved that whenever

`N->infinity`, `g=ell+r->infinity`, `g/N->0`, `ell/g->theta in (0,1)`,

then

`(U/g,V/g) => (theta Z_1,(1-theta)Z_2)`,                           (4.1)

where `Z_1,Z_2` are independent and

`P(Z_i<=z)=z/(1+z)`, `z>0`.                                        (4.2)

Because `ell~theta g` and `r~(1-theta)g`, (4.1) is equivalently

`U/ell => Z_1`, `V/r => Z_2`.                                      (4.3)

Set `X=log Z`. Then

`P(X<=x)=e^x/(1+e^x)`,                                             (4.4)

so `X` is the centered logistic law. It is symmetric, with

`E X=0`, `Var(X)=pi^2/3`,                                          (4.5)

and characteristic function

`phi_X(t)=pi t/sinh(pi t)`.                                        (4.6)

Thus the ideal finite-step logarithmic limit is

`log ell' = log ell + X_1`,
`log r'   = log r   + X_2`,                                        (4.7)

with independent centered logistic increments.

This changes the interpretation of the earlier positive drift of `log(U+V)-log(ell+r)`.  The natural two-dimensional log coordinates have **zero vector drift**.  The positive drift of the log of the sum is a convexity/radial effect, not a deterministic escape of both coordinates.

---

## 5. B28 — typical paths of the ideal thin-shell limit are recurrent, not outward-drifting

Define the ideal log chain

`Y_n=(A_n,B_n)`,

`Y_{n+1}=Y_n+(X_{n+1}^{(1)},X_{n+1}^{(2)})`,                       (5.1)

where all `X_n^(i)` are independent centered logistic variables.

### Theorem 5.1 (planar recurrence of the ideal shell limit)

The random walk `(Y_n)` is recurrent in `R^2`: for every open neighborhood `O` of its starting point,

`P(Y_n in O infinitely often)=1`.                                  (5.2)

The projective logit

`Q_n=A_n-B_n=log(ell_n/r_n)`                                       (5.3)

is a one-dimensional centered recurrent random walk.  In particular, almost surely

`limsup Q_n=+infinity`, `liminf Q_n=-infinity`,                    (5.4)

and it returns to every neighborhood of zero infinitely often.

#### Proof

The increment characteristic function in two dimensions is

`Phi(t_1,t_2)=phi_X(t_1)phi_X(t_2)`.

By (4.6), near the origin

`phi_X(t)=1-(pi^2/6)t^2+O(t^4)`,

so

`1-Phi(t_1,t_2)
 =(pi^2/6)(t_1^2+t_2^2)+O(|t|^4)`.                                (5.5)

The Chung-Fuchs recurrence integral therefore diverges logarithmically:

`int_{|t|<epsilon} Re[1/(1-Phi(t))] dt
  asymp int_0^epsilon dr/r = infinity`.

The increments are continuous and nonlattice, so the standard Chung-Fuchs criterion gives (5.2).  For the projective coordinate, the increment is `X_1-X_2`, which is symmetric, nondegenerate, centered and has variance `2pi^2/3`; the one-dimensional Chung-Fuchs criterion gives recurrence, and symmetry/nondegeneracy gives the two-sided oscillation (5.4). QED.

### Consequence 5.2

The universal interior thin-shell limit does **not** support the heuristic “positive total logarithmic shell drift implies survival.”  Typical limiting paths make arbitrarily deep excursions toward both one-sided faces and return to balanced configurations; in the full two-log coordinate system they return to bounded neighborhoods infinitely often.

This is compatible with the preceding recovery theorem: the difficult behavior is created precisely by the interaction between recurrent thin-shell excursions and rare span-scale revivals, not by a one-directional supercritical multiplier.

---

## 6. The blocker is now an excursion-transfer problem

The current exact equality special case has the following structure, all source-valid:

1. The model is literal H0024 data with `pi=sech(T)`, `T~Exp(1)`, and exact tail `P(D^+>=n)=1/(n+1)`.
2. Every one-sided shell has exact opposite-side revival hazard `g/(N+2)`.
3. Its near-side marginal kernel has the exact harmonic scale `H_g` and, in isolation, is absorbed almost surely.
4. The full harmonic shell mass `H_ell+H_r` has exact positive drift (3.3), coming only from cross-side interaction.
5. Away from the axes, the finite-step thin-shell limit is a centered planar random walk in logarithmic coordinates and is recurrent.
6. The preceding run proved negative projective drift near a one-sided face and uniform killing on every fixed bounded-shell set.

Therefore the unresolved special-case theorem can be stated more sharply than `g->infinity, g/N->0`:

> **Excursion-transfer problem.**  During a large-span thin-shell excursion, prove either that the exact source chain has a scale-uniform positive chance to reach a bounded shell and die before its next span-scale revival, or prove that the accumulated cross-revival mechanism has a positive probability of renewing the excursion forever.

The limiting planar recurrence says that a proof cannot treat the interior as irreversibly outward-drifting.  The exact hazard (2.3) says that a proof also cannot simply discard cross revivals.  What is missing is a **uniform-in-time coupling/occupation estimate** transferring the recurrent logistic log-walk approximation to the actual changing-span chain up to the first macroscopic revival.

That is a substantially narrower gluing problem than the bivariate-tail uncertainty present before STUCK1.

---

## 7. Source status and literature discipline

Dated check: **2026-09-18**.  The primary arXiv record remains `2607.27082v1`, submitted 29 July 2026, and still states that the critical-line sufficient survival/extinction constants leave a factor-four gap and that the full critical-line phase diagram is not determined.  A bounded exact-title, arXiv-ID, author, and recent follow-up search found no later source-level resolution.  The authors' 2025 general-random-survival and 2026 discrete-Weibull papers concern neighboring lifetime models and do not state a resolution of Remark 3.6.  This is negative evidence only, not a novelty certificate.

The repository `INDEX.md` contains the historical shorthand “artefact; growth is multiplicative” for H0024.  That row is not used as a closure claim: the current canonical claim and cumulative R7-05 proof state remain **PARTIAL / SOURCE OPEN**.

No P26 or distinct OTHER-track independent audit is claimed for the theorems above.

---

## 8. Frozen metric and next route

Frozen metric:

`G_crit=C_surv/C_ext`.

Before: `G_crit=1`.

After: `G_crit=1`.

**NO MOVEMENT.**  The strict constants were already matched; these are equality-boundary structural advances, not a full critical-line classification.

Methods and outcomes:

- **B7:** built a literal exact-equality source law `pi=sech(Exp(1))`, derived `P(D^+>=n)=1/(n+1)`, and identified the interior thin-shell log limit as two independent centered logistic increments.
- **B24:** found the exact harmonic-number scale.  The one-sided marginal shell kernel has `H_g` as a martingale and dies almost surely in isolation; the full chain obeys the exact cross-side drift identity (3.3), with one-sided revival hazard exactly `g/(N+2)`.
- **B28:** proved the ideal two-log thin-shell limit is a recurrent planar random walk and its projective logit is recurrent/oscillatory.  The missing step is now uniform excursion transfer, not the sign of a local interior drift.

Do not repeat B7/B24/B28 next.  If ownership and source status are unchanged, the next and potentially final ordinary H0024 run before the six-unchanged CLOSABLE handoff should use:

- **B3 — prove something stronger:** seek a stopped coupling theorem valid for an entire thin-shell excursion up to bounded-shell hit or macroscopic revival, rather than one-step convergence;
- **B12 — find what is conserved:** combine `H_ell+H_r` with a span correction to search for an exact or one-sided stopped potential that controls accumulated revival hazard;
- **B30 — localize and glue:** split at dyadic values of `g/N`, prove a scale-uniform excursion estimate on each annulus, and identify whether the constants glue to extinction or to a renewal-survival construction.

If `G_crit` remains unchanged on that next ordinary run, the cumulative ordinary unchanged count reaches six and the CLOSABLE retirement/handoff rule applies.