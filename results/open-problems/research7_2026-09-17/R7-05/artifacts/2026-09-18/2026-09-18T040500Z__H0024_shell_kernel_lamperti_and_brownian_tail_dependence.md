Model actually running: **GPT-5.6 Sol. Reasoning level: UNVERIFIED** — this is **not GPT-6 at maximum**; GPT-6 / maximum reasoning was requested, but no authenticated runtime model/effort telemetry or binding selector is exposed.

# H0024 — exact shell kernel, thin-shell Lamperti reduction, and source-specific Brownian tail dependence

Status: **PARTIAL / SOURCE OPEN**.  This note does not settle the full critical-line phase diagram in Oshiro de Carvalho–Machado–Ramírez-González.  It develops three new exact structural statements for the already-admitted H0024 target and identifies a source-specific bivariate quantity that the one-sided tail asymptotic cannot see.

Run target: H0024, Gustavo Oshiro de Carvalho, Fábio Prates Machado, José Hermenegildo Ramírez-González, *Extinction and Survival in an Interval-Activation Frog Model on Z with Random Survival Parameters and Symmetric Random Walks* (2026), arXiv:2607.27082v1, Theorem 3.5(ii) / Remark 3.6.

Captured run-start master: `16929aca2178483282ef60aff1ff9b134dcdfa37`.
Fresh pre-write master: `37ff7d745ad23dd2aee21c3726e7c2db34c17195`.
Canonical claim: `operations/claims/H0024.md`.
Previous R7-05 report: `research7_2026-09-17/R7-05/runs/2026-09-18/2026-09-18T025411Z__report.md` @ `83516e04d01d0b78b8c2f0ae1eddf908ce6c438d`.

The mathematical idea comes first.  The previous run showed that fixed-scale closed-interval counting loses a logarithm exactly at the unresolved boundary.  Rather than count traps again, expose the activated interval breadth-first.  The unexplored boundary shell is fresh iid data, so its next left/right extensions have an exact finite-dimensional transition kernel.  In the genuinely two-sided *thin-shell* regime that kernel has a universal scaling limit with strictly positive logarithmic fresh-shell drift.  Hence the difficult regime is forced onto the one-sided faces.  In the finite-variance source regime, those faces are not described by two independent marginal tails: a frog that makes a macroscopic excursion to one side retains a quantitatively nontrivial macroscopic excursion law on the other side.  Brownian potential theory gives that bivariate tail law in closed form.

---

## 1. B1 — change category: the activation cluster is a random closure operator

Let `(L_x,R_x)_{x in Z}` be iid pairs of finite nonnegative integer-valued marks.  No independence of `L_x` and `R_x` at a fixed site is assumed.  Site `x` carries

`J_x=[x-L_x,x+R_x] cap Z`.

For a finite integer interval `I`, define

`Phi(I)=conv( union_{x in I} J_x ) cap Z`.

Because `x in J_x`, one always has `I subseteq Phi(I)`.  Starting from `I_0={0}`, set `I_{k+1}=Phi(I_k)`.

### Theorem 1 (fixed-point formulation)

1. `I_k` is exactly the interval hull of the sites activated after `k` breadth-first generations.
2. A finite interval `I` is closed in the usual H0024 sense iff `Phi(I)=I`.
3. The activated cluster of the origin is finite iff the increasing iteration from `{0}` reaches a finite fixed point.
4. The finite closed intervals containing `0` form a distributive lattice under intersection and union.
5. On the extinction event the final activated interval is the least closed interval containing `0`.

### Proof

The first assertion is induction.  At generation `k`, exactly the marks centered at sites already reached are allowed to add sites, and their union has interval hull `Phi(I_k)`.  Assertion 2 is the definition: `Phi(I)=I` exactly when every `J_x`, `x in I`, remains inside `I`.  Since the iteration is monotone, a finite fixed point stops all future growth; conversely, if the activated set is finite, its final interval is unchanged by exposing all of its marks and hence is fixed.

If `I` and `K` are closed and both contain `0`, then they overlap.  Their union is therefore an interval.  For `x in I union K`, the mark `J_x` lies in whichever closed interval contains `x`, hence lies in `I union K`; so the union is closed.  If `x in I cap K`, then `J_x subseteq I` and `J_x subseteq K`, hence `J_x subseteq I cap K`; the intersection is closed.  Ordinary interval union/intersection are distributive.  Finally, every closed interval containing `0` contains every iterate `I_k`, so it contains the terminal finite iterate.  This proves minimality.  QED.

This formulation matters because H0024 is not merely a collection of overlapping random intervals: it is a monotone random fixed-point problem.  A successful equality argument can therefore target the dynamics of the least fixed point rather than another first-moment trap count.

---

## 2. B20 — the exact breadth-first shell kernel

Use the breadth-first iteration above.  Suppose the current interval is

`I=[A,B]`, `N=B-A`,

and the preceding interval was `[A+ell,B-r]`.  The fresh, still-unexposed shell is therefore

`S=[A,A+ell-1] union [B-r+1,B]`,

where `ell,r>=0`, `g=ell+r>0`.

After translating `A` to zero, write

`F(a,b)=P(L<=a,R<=b)`.

Define the next left and right extension counts

`U=max_{x in S} (L_x-(x-A))_+`,

`V=max_{x in S} (R_x-(B-x))_+`.

Then the next interval is `[A-U,B+V]`, and its fresh shell has exactly `U` sites on the left and `V` sites on the right.

### Theorem 2 (exact three-coordinate Markov kernel)

Conditionally on the exploration history up to the moment before the marks in `S` are exposed, for every integers `u,v>=0`,

`P(U<=u,V<=v | N,ell,r)`

`= prod_{j=0}^{ell-1} F(j+u,N-j+v)`

`  * prod_{j=N-r+1}^{N} F(j+u,N-j+v)`.       (2.1)

Consequently the breadth-first process is Markov in the state `(N,ell,r)` with update

`(N,ell,r) -> (N+U+V,U,V)`,

and absorption occurs exactly at `(U,V)=(0,0)`.

### Proof

All marks in the fresh shell are unexposed and independent across sites.  For a fresh site at translated location `j`, the event that it creates no left extension beyond `u` is `L<=j+u`; the event that it creates no right extension beyond `v` is `R<=N-j+v`.  Both must hold at every fresh site.  Multiplying the same-site joint probabilities over the two disjoint fresh blocks gives (2.1).  The stated update is then deterministic.  QED.

This is an exact state compression: no older interior marks occur in the transition law because they have already been exposed and, by definition of the current interval, cannot extend it further.

### Why the obvious algorithm fails

Equation (2.1) also pinpoints the obstruction.  In a macroscopic shell, both arguments of `F` can be of the same order, and the transition law depends on the *bivariate* tail of `(L,R)`, not only on the marginal `q_n=P(L>n)=P(R>n)`.  The source's one-sided asymptotic for `D^->` therefore cannot by itself identify the equality kernel.

---

## 3. B21 — import a Lamperti viewpoint: the universal thin-shell kernel

Assume for this section only the critical first-order marginal tails

`P(L>n)~1/n`, `P(R>n)~1/n`,          (3.1)

with arbitrary dependence of `L` and `R` at one site.

Consider deterministic states `(N_k,ell_k,r_k)` satisfying

`N_k -> infinity`, `g_k:=ell_k+r_k -> infinity`, `g_k/N_k -> 0`,

and

`ell_k/g_k -> theta in (0,1)`.

Let `(U_k,V_k)` be the next extensions from Theorem 2.

### Theorem 3 (universal interior thin-shell scaling)

For every fixed `x,y>0`,

`P(U_k/g_k<=x, V_k/g_k<=y | N_k,ell_k,r_k)`

` -> [x/(x+theta)] [y/(y+1-theta)]`.         (3.2)

Equivalently,

`(U_k/g_k,V_k/g_k) => (theta Z_1,(1-theta)Z_2)`,

where `Z_1,Z_2` are independent with

`P(Z_i<=z)=z/(1+z)`, `z>0`.                 (3.3)

The limit is independent of the same-site dependence between `L` and `R`.

### Proof

For a site in the left fresh block, the left threshold `x g_k+j` is of order `g_k`, while the right threshold `N_k-j+y g_k` is of order `N_k`.  Write `q_L(a)=P(L>a)` and `q_R(b)=P(R>b)`.  Fréchet bounds give

`0 <= P(L<=a)-F(a,b) = P(L<=a,R>b) <= q_R(b)`.

Uniformly over the left block, `q_R(b)=O(1/N_k)`, so the accumulated logarithmic error from replacing `F(a,b)` by `P(L<=a)` is `O(ell_k/N_k)=o(1)`.  The analogous replacement on the right block has error `O(r_k/N_k)=o(1)`.

Hence (2.1) equals, up to a multiplicative `1+o(1)`,

`prod_{j=0}^{ell_k-1}(1-q_L(floor(xg_k)+j))`

`* prod_{h=0}^{r_k-1}(1-q_R(floor(yg_k)+h))`.

By (3.1), uniformly on compact positive multiples of `g_k`, the logarithm of the first product is

`-sum_{j<ell_k} 1/(xg_k+j)+o(1)`

` -> - integral_0^theta dt/(x+t) = log[x/(x+theta)]`.

The sum of squared tails is `O(1/g_k)`, so replacing `log(1-q)` by `-q` is legitimate.  The same calculation on the right gives `log[y/(y+1-theta)]`.  This proves (3.2), whose factorization gives (3.3).  QED.

### Corollary 4 (strictly positive interior logarithmic fresh-shell drift)

Let

`M_theta=theta Z_1+(1-theta)Z_2`.

Then

`m(theta):=E log M_theta >0`, `0<theta<1`.    (3.4)

Indeed weighted AM-GM yields

`log M_theta >= theta log Z_1+(1-theta)log Z_2`.

The beta-prime law (3.3) satisfies `E|log Z_i|<infinity` and, by the substitution `Z=U/(1-U)` with `U` uniform on `(0,1)`,

`E log Z = integral_0^1 [log u-log(1-u)]du=0`.

The AM-GM inequality is strict almost surely because `Z_1` and `Z_2` are independent continuous variables and `theta` is interior.  Thus (3.4) follows.  It is quantitative away from the axes: on the event `{Z_1>=2,Z_2<=1/2}`, which has probability `1/9`, the AM-GM gap is at least

`log(1+3 theta)-theta log 4`.

Therefore for every `delta in (0,1/2)`,

`inf_{theta in [delta,1-delta]} m(theta) >= (1/9) min_{theta in [delta,1-delta]}[log(1+3theta)-theta log4] >0`.     (3.5)

Thus a thin shell that keeps a genuinely positive fraction of fresh sites on both sides has a strictly supercritical logarithmic multiplier.  The unresolved equality mechanism is forced toward the one-sided faces `theta=0` or `theta=1` (or toward bounded fresh-shell size, where the scaling theorem does not apply).

This is the precise place where Lamperti-type near-zero-drift ideas become relevant: the critical process is not globally zero-drift; zero drift is a boundary phenomenon of the projective shell chain.

---

## 4. The one-sided boundary layer and the exact critical scales

Take a right-only fresh shell: `ell=0`, `r=g`, with `g->infinity`, `s=g/N->0`.

The near-side extension `V` depends only on the marginal of `R`, so (3.1) gives

`V/g => Z`, `P(Z<=z)=z/(1+z)`.               (4.1)

The far-side revival event is `{U>0}`.  Marginally,

`P(U=0)=prod_{k=0}^{g-1}(1-q_L(N-k))`,

so

`P(U>0)~s`.                                  (4.2)

For every fixed `u>0`,

`P(U>uN)~s/(1+u)`,

and therefore, conditionally on `U>0`,

`U/N => W`, `P(W>u)=1/(1+u)`.                (4.3)

Thus a rare cross-revival occurs with probability of order `s` and, when it occurs, produces an extension of order the *entire span* `N`.

The near-side normalization has an exact limiting integral.  For `Z` in (4.1),

`E log(1+sZ) = - s log s/(1-s)`.              (4.4)

Proof: write `Z=T/(1-T)` with `T` uniform `(0,1)` and integrate

`log(1+sZ)=log(1-(1-s)T)-log(1-T)`.

Hence the one-sided critical normalization penalty is

`-s log(1/s)+O(s^2 log(1/s))`.               (4.5)

A cross-revival, by (4.2)-(4.3), has probability `s+o(s)` and carries a logarithmic size jump of order `log(1/s)`.  Consequently the positive and negative effects live on the same critical scale `s log(1/s)`.  First-order marginal tails cannot decide their difference.

For the second-order family

`q_n=(1/n)(1+a/log n+O(log^{-2}n))`,

the corresponding one-sided beta-prime multiplier with local coefficient `c` has

`E log Z_c = psi(c)+gamma`,

where `P(Z_c<=z)=(z/(1+z))^c`.  Since `psi(1)=-gamma` and `psi'(1)=pi^2/6`, the local perturbative drift is

`(pi^2/6) a/log g + o(1/log g)`.              (4.6)

Equations (4.5)-(4.6) show that the remaining equality problem is a boundary-layer competition between a Lamperti-scale one-sided drift and rare opposite-side regeneration.  Which term wins depends on how the two extrema at a site are coupled.  Treating them as independent is not source-valid.

---

## 5. Source-specific finite-variance theorem: exact bivariate extreme tail

The preceding section says that the missing datum is bivariate.  In the finite-variance branch of the actual H0024 source, that datum can be computed explicitly.

Assume the source hypotheses in the finite-variance regime:

`E xi_1=0`, `Var(xi_1)=sigma^2 in (0,infinity)`,

and on the critical line `beta=1/2`,

`f_pi(u)~(1-u)^(-1/2) ell((1-u)^(-1))` as `u up to 1`.

For one frog started at zero let `D^+` and `D^-` be its maximal right and left displacements before death.  For `x,y>0` define

`T_n(x,y)=max(tau^+_{ceil(nx)}, tau^-_{ceil(ny)})`,

where `tau^-_a=inf{k:S_k<=-a}`.

Then

`{D^+>=nx,D^->=ny}={L>=T_n(x,y)}`.

### Theorem 5 (Brownian bivariate critical-tail constant)

For every fixed `x,y>0`,

`lim_{n->infinity} [ n P(D^+>=nx,D^->=ny) / ell(n^2) ]`

`= K_sigma(x,y)`,                            (5.1)

where

`K_sigma(x,y)=sqrt(2) sigma [ 1/x + 1/y - (pi/(x+y)) csc(pi x/(x+y)) ]`.       (5.2)

(The event notation `D^->=ny` in (5.1) means `D^- >= ny`; the ASCII arrow is avoided below.)

### Proof

The source's proof of Proposition 3.4 applies after replacing the one-sided hitting time by `T_n(x,y)`.  Here are the points that must be checked.

First, Donsker convergence gives `S_floor(n^2 t)/n => sigma B_t`.  Brownian paths are continuous, hit both nonzero levels at continuity points of the hitting-time maps almost surely, and therefore

`T_n(x,y)/n^2 => T_B(x,y):=max(tau^+_x(sigma B),tau^-_y(sigma B))`.

Second, `T_n(x,y)>=tau^+_{ceil(nx)}` (and also the negative analogue), so every small-time and large-Laplace-parameter upper bound used in the source proof is inherited from its one-sided bound.  In particular the source's Lemmas 5.9-5.10 dominate the Potter-bound integral exactly as before.  The low-`u` part is also smaller than the corresponding one-sided integral.  Thus the same change of variables and dominated-convergence proof gives

`lim n P(D^+>=nx,D^->=ny)/ell(n^2)`

`= Gamma(1/2) E[T_B(x,y)^(-1/2)]`

`= integral_0^infinity E[e^{-s T_B(x,y)}] s^(-1/2) ds`.       (5.3)

It remains to evaluate (5.3).

Put `a=sqrt(2s)/sigma` and `S=x+y`.  Let `tau` be the first exit time of `sigma B` from `(-y,x)`.  Standard one-dimensional killed-harmonic functions give

`E_0[e^{-s tau}; B_tau=x/sigma] = sinh(ay)/sinh(aS)`,

`E_0[e^{-s tau}; B_tau=-y/sigma] = sinh(ax)/sinh(aS)`.

After the first boundary is hit, reaching the opposite boundary requires a displacement of length `S`; its Laplace transform is `e^{-aS}`.  The strong Markov property therefore yields

`E[e^{-s T_B(x,y)}]`

`= e^{-aS} [sinh(ay)+sinh(ax)] / sinh(aS)`.   (5.4)

Since `s^(-1/2)ds=sqrt(2)sigma da`, (5.3) equals `sqrt(2)sigma` times

`I(x,y)=integral_0^infinity e^{-aS}[sinh(ay)+sinh(ax)]/sinh(aS) da`.       (5.5)

For `0<c<S`, expand `1/sinh(aS)=2e^{-aS}/(1-e^{-2aS})`.  Termwise integration gives

`integral_0^infinity e^{-aS}sinh(ac)/sinh(aS) da`

`= (1/(2S))[psi(1+c/(2S))-psi(1-c/(2S))]`

`= 1/c - (pi/(2S)) cot(pi c/(2S))`,           (5.6)

where the last identity uses `psi(1+z)-psi(1-z)=1/z-pi cot(pi z)`.  Sum (5.6) for `c=x,y`.  Because `x/(2S)+y/(2S)=1/2`,

`cot(pi x/(2S))+cot(pi y/(2S))=2 csc(pi x/S)`.

This gives (5.2).  QED.

### Corollary 6 (an explicit tail-dependence law)

Normalize the left threshold to one and write

`H(t):=K_sigma(t,1)/(sqrt(2)sigma)`.

Then

`H(t)=1+1/t - [pi/(1+t)] csc(pi/(1+t)), t>0,`       (5.7)

and for a single frog

`P(D^+>=tn | D^->=n) -> H(t)`

in the critical-tail sense (ratio of the two asymptotics).  In particular

`H(1)=2-pi/2 = 0.4292036732...`,               (5.8)

while

`H(t)=1-(pi^2/6)t+(pi^2/3)t^2+O(t^3)` as `t down to 0`.       (5.9)

Thus a frog responsible for an order-`n` excursion to one side almost surely has an opposite-side excursion larger than `t n` as `t down to 0`; the failure probability is only `(pi^2/6)t+o(t)`.

### Corollary 7 (site maxima preserve the same first-order dependence law)

Let a site contain an iid number `eta` of frogs with `0<E eta<infinity`, independent of the frog marks, and let `L_site,R_site` be the maxima of the frogs' left/right reaches.  Then for fixed `t>0`,

`P(R_site>=tn | L_site>=n)` has the same asymptotic ratio `H(t)`.

Proof: for one frog write `q_L,q_R,j` for the left, right and joint rare-event probabilities and `u=q_L+q_R-j` for their union.  The elementary finite-mean expansion

`E[1-(1-z)^eta]~(E eta)z`, `z down to0`,

applied to `q_L,q_R,u` gives

`P(L_site event and R_site event)`

`=P(L_site)+P(R_site)-P(L_site union R_site)~(E eta)j`.

The common factor cancels in the conditional ratio.  QED.

This corollary requires only the source assumption `E eta<infinity`; no second moment of `eta` is needed.

---

## 6. What the Brownian law says about the boundary blocker

The independent-coordinate surrogate is qualitatively wrong for the source finite-variance regime.  In a right-only thin shell with `g=sN`, a site capable of an order-`N` left revival has, by (5.7)-(5.9), a right reach of order `N` on the logarithmic scale: conditional on the far-left event, `R_site/N` has a nondegenerate law whose probability of being below `t` is only `(pi^2/6)t+o(t)` as `t down to0`.

Consequently the rare cross-revival is not an independent additional `s log(1/s)` source of logarithmic growth.  Much of that logarithmic gain is already present in the same site's near-side extreme.  This is exactly the information that is absent from the marginal asymptotic `n P(D^->=n)`.

The coincidence of the constant `pi^2/6` in (4.6) and (5.9) is mathematically suggestive but **is not claimed as a phase-boundary proof**.  It says that in the finite-variance branch, both the second-order one-sided drift and the loss of opposite-side tail dependence enter at the same canonical constant.  A valid closure now needs the actual boundary-layer Markov renewal calculation, not another independent-tail approximation.

For the stable branch `1<alpha<2`, the same source argument points to the analogous motion-dependent function

`H_alpha(t)= E[T_alpha(t,1)^(-1/alpha)] / E[(tau^-_1)^(-1/alpha)]`,

where `T_alpha(t,1)` is the completion time for a symmetric alpha-stable process to hit both `+t` and `-1`.  No closed form is asserted here.  The existence of this additional bivariate invariant already shows why the full critical-line problem can depend on more than the single marginal constant `kappa`.

---

## 7. What is proved and what is still missing

**New exact results in this note:**

- activation as a distributive random fixed-point lattice;
- the exact `(N,ell,r)` breadth-first transition kernel (2.1);
- the universal thin-shell limit (3.2) under only critical marginal tails, robust to arbitrary same-site dependence;
- strictly positive interior logarithmic fresh-shell drift (3.4)-(3.5), forcing the critical obstruction to the one-sided faces;
- exact boundary-layer marginal scales (4.1)-(4.5);
- in the finite-variance source regime, the closed-form bivariate critical-tail constant (5.2) and dependence law (5.7)-(5.9), preserved under arbitrary finite-mean site occupancy.

**Still missing for source closure:**

- a recurrence/transience/extinction classification of the boundary-layer Markov chain generated by (2.1);
- the symmetric exact-equality case, including `q_n=1/n+o(1/n)`;
- the logarithmic second-order cases left open by the previous run, including the symmetric `a<=1/2` region;
- oscillatory slowly varying `ell` crossing the first-order threshold;
- the stable-regime analogue of (5.7) at sufficient precision for the boundary-layer calculation;
- independent P26 and distinct OTHER-track audits and a self-contained source-scope paper package.

No numerical fit, finite cutoff, or search miss is being treated as source resolution.

---

## 8. Dated source / literature check used in this run

Dated 2026-09-18.

- The current arXiv record found for `2607.27082` is still v1 (submitted 29 July 2026), and its abstract still states that the critical-line sufficient conditions leave a factor-four gap.  The primary text's Remark 3.6 explicitly says that the full critical-line phase diagram is not determined by the present argument.
- Bounded exact-title, identifier, and author/follow-up searches did not surface a later explicit resolution.  This is negative evidence only, not a novelty certificate.
- Roy–Saha, *How Fast do Rumours Spread?*, Journal of Statistical Physics 191 (2024), article 130, treats a related one-dimensional rumour/long-range-percolation model and supplies useful renewal intuition, but under moment assumptions and without the present critical heavy-tail bivariate shell kernel.
- Denisov–Korshunov–Wachtel, *Markov Chains with Asymptotically Zero Drift: Lamperti's Problem* (Cambridge, 2025), and their renewal work provide the natural analogue for the remaining near-zero-drift boundary classification.  The present shell chain is not claimed to fall under an off-the-shelf theorem from those works.
- Georgiou–Menshikov–Petritis–Wade (EJP 2019) treat heavy-tailed Markov chains with asymptotically zero drift and reinforce that at a critical boundary one must compare drift and heavy-tail constants at the same scale; again, no direct source resolution is imported.

The next R7-05 run is forced by the owner protocol to be the thinking-only Section-I stuck diagnosis if the frozen metric remains unchanged in the accompanying report.