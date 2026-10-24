Model actually run: **GPT-5.6 Sol. Reasoning level: UNVERIFIED — GPT-6 maximum was requested, but this runtime exposes no authenticated applied-model / reasoning-effort selector or attestation, so GPT-6 maximum is not claimed.**

# PROB10-08 proof artifact — pre-entropic long-range growth is enough for cutoff

Status: **new repository theorem / PARTIAL for Salez Problem 2.3 / not independently audited / worldwide novelty UNVERIFIED**.

This artifact gives the complete proof of the mathematical claim retained in this bounded iteration. It is deliberately separate from the older R16 product-varentropy, synchronous-tensor, moving-window/Poincare, Hecke/information-curvature, tree-subcommutation, vanishing-LRE, graph-cover, line-graph, and finite-fiber blow-up routes.

## 1. Frozen source convention

Let `G_n=(V_n,E_n)` be finite, connected, simple, `d`-regular graphs, with fixed `d>=3`, `n=|V_n| -> infinity`, and

`P_n=A_n/d`.

We use Salez's rate-one continuous-time simple random walk convention

`H_t = exp(t(P_n-I))`.

Write

`q=d-1`, `v=(d-2)/d`, `L_n=log_q n`,

and let `pi_n` be uniform measure. Assume the one-sided spectral gap

`1-lambda_2(P_n) >= gamma > 0`

uniformly in `n`. No lower bound on `lambda_n(P_n)` is assumed; continuous time removes the periodicity obstruction.

For a set `S`, write `B(S,r)={y: dist(y,S)<=r}`.

## 2. New weaker growth hypothesis

Fix `c in (0,1]`. Let `rho_n>=0` be any sequence. Say that `G_n` has **pre-entropic long-range growth with defect rho_n** if for every nonempty `S subset V_n` and integer `r>=0` satisfying

`|S| q^r <= n exp(-rho_n)`,

one has

`|B(S,r)| >= c |S| q^r`.                                      (PE)

Unlike Altschuler's long-range expansion, (PE) imposes **no condition at all** after the tree-volume scale reaches `n exp(-rho_n)`. In particular, with `rho_n=A log log n`, growth is required only up to `n/(log n)^A`, not to a fixed positive fraction of all vertices.

The retained theorem is the following.

## 3. Main theorem

### Theorem PE-CUTOFF

Fix `d>=3`, `c>0`, and `gamma>0`. Let `(G_n)` satisfy the frozen assumptions above and (PE).

There is a constant `C=C(d,c)` such that, uniformly in `x` and every nonbacktracking length `j` at or beyond the entropic radius,

`H(K_j(x,.)) >= log n - Delta_n`,

where

`Delta_n <= rho_n + C log log n + C`.                           (3.1)

Here `K_j(x,.)` is the endpoint law of a length-`j` nonbacktracking walk started at `x`, and the entropic radius is

`j_n=min{j>=1: d q^(j-1)>=n}=L_n+O_d(1)`.

Consequently, for every fixed `epsilon in (0,1/2)`, if `rho_n=o(log n)`,

`| t_mix^(n)(epsilon) - (d/(d-2)) L_n |`

`    <= C_(d,c,gamma,epsilon) [ sqrt(L_n) + rho_n + log log n + 1 ]`       (3.2)

for all sufficiently large `n`. Hence

`[t_mix(epsilon)-t_mix(1-epsilon)]/t_mix(1/2)`

` = O_(d,c,gamma,epsilon)( L_n^(-1/2) + (rho_n+log log n+1)/L_n ) = o(1)`. (3.3)

Thus rate-one continuous-time SRW exhibits total-variation cutoff.

If in addition

`rho_n=o(sqrt(log n))`,

then the full square-root Gaussian profile is retained: for every fixed real `z`,

`sup_x | ||delta_x H_(T_n+z sqrt(L_n))-pi_n||_TV - Phi(-v^(3/2) z) | -> 0`, (3.4)

where

`T_n=L_n/v=(d/(d-2))L_n`.

In particular, for every fixed `A<infinity`, the condition

`|B(S,r)|>=c|S|q^r whenever |S|q^r<=n/(log n)^A`

plus a uniform one-sided spectral gap already gives the **same** cutoff center, `Theta(sqrt(log n))` window, and Gaussian profile as full long-range expansion.

The theorem itself does not require vertex transitivity. Restricting it to vertex-transitive sequences gives a source-admissible special class for Salez Problem 2.3.

---

## 4. Lemma 1 — transfer only the needed pre-entropic growth to oriented edges

Let

`Omega={(u,w): u~w}`, `N=dn`,

and let `Q` be the nonbacktracking transition matrix on oriented edges,

`Q((u,w),(w,z))=1/q` for `z != u`.

For `F subset Omega`, let `B_Omega(F,r)` be its directed radius-`r` ball.

### Lemma 4.1

There exist constants `a=a(d,c)>0` and `theta=theta(d,c)>0` such that whenever (PE) holds,

`|B_Omega(F,r)| >= a |F| q^r`                                  (4.1)

for every nonempty `F subset Omega` and every `r>=0` satisfying

`|F|q^r <= theta N exp(-rho_n)`.                               (4.2)

### Proof

This is the exact place where Altschuler's Lemma 3.2 uses long-range expansion, but we stop before macroscopic saturation instead of extending the estimate to every radius.

Choose an integer `k>=1`, depending only on `(d,c)`, such that

`q^(-k) <= c(q-1)/2`.                                          (4.3)

Fix `F subset Omega`. Let `C` be the set of terminal vertices of states in `B_Omega(F,2k)`. Let `U subset C` consist of terminal vertices not reached at any positive time up to `2k`.

Exactly as in Altschuler's path-reversal argument, the `|U|q^k` nonbacktracking continuations of the chosen incoming edges have distinct endpoints; hence

`|U| <= q^(-k)|C|`.                                            (4.4)

We also have

`|C| >= |F|/d`,                                                 (4.5)

because at time zero at most `d` oriented edges of `F` have the same terminal vertex.

For an upper bound, each initial state has at most

`K_k:=1+q+...+q^(2k)`

states in its directed ball of radius `2k`, so

`|C| <= K_k |F|`.                                               (4.6)

Now let `r=2k+ell`, `ell>=0`. A shortest graph path from `C` to a vertex of `B_G(C,ell)` that has not been reached by directed time `2k+ell` must start in `U`, and its first step must reverse the chosen incoming edge. Thus, as in Altschuler,

`|B_Omega(F,2k+ell)|`

` >= |B_G(C,ell)| - |U|(q^ell-1)/(q-1)`.                       (4.7)

Set

`theta := q^(2k)/(d K_k)`.

If `|F|q^(2k+ell) <= theta N exp(-rho_n)`, then by `N=dn` and (4.6),

`|C|q^ell <= K_k |F|q^(r-2k) <= n exp(-rho_n)`.

Therefore (PE) applies to `(C,ell)` and gives

`|B_G(C,ell)| >= c|C|q^ell`.

Using (4.3)-(4.4) in (4.7),

`|B_Omega(F,r)| >= (c/2)|C|q^ell`

` >= [c/(2d q^(2k))] |F|q^r`.                                 (4.8)

For `r<2k`, trivially

`|B_Omega(F,r)|>=|F|>=q^(-2k)|F|q^r`.

Thus (4.1) holds with

`a=min{q^(-2k), c/(2d q^(2k))}`.

This proves the lemma. ∎

### What was removed from the published LRE proof

The published Lemma 3.2 continues from the first scale at which `|C|q^ell` reaches `n`, uses monotonicity, and obtains directed growth all the way to a positive fraction of the whole state space. None of that continuation is needed below. For cutoff, reaching `N exp(-rho_n)` states already leaves only `rho_n+O(log log n)` nats of entropy to produce.

---

## 5. Lemma 2 — truncated directed growth still gives near-maximal endpoint entropy

The next statement is the exact truncated form of Altschuler's forest induction.

### Lemma 5.1

Let a directed graph have `N` states and exactly `q>=2` incoming and `q` outgoing edges at every state. Assume there are `a, M>0` such that

`|B(S,r)| >= a|S|q^r`                                          (5.1)

whenever `S` is nonempty and

`|S|q^r <= M`.                                                  (5.2)

Then there exist constants `C0>=1` and `delta>0`, depending only on `(a,q)`, such that a simple random walk started uniformly on any nonempty `S` satisfies

`H(Y_h) >= log|S| + h log q - delta^(-1) log(qh+1)`             (5.3)

whenever

`|S| q^(h+C0) <= M`.                                           (5.4)

### Proof

Choose `C0` with

`q^(-C0) <= a(q-1)/2`,

and put

`delta=a(q-1)/(2q)`.

Induct on `h`, simultaneously over all pairs `(S,h)` satisfying (5.4). The case `h=0` is immediate.

Let `Gamma_r(S)` be the directed shell at exact distance `r`. As in Altschuler,

`|Gamma_(r+1)(S)| <= q |Gamma_r(S)|`.

Since (5.4) allows us to apply (5.1) at radius `h+C0`, the same shell calculation gives

`|Gamma_h(S)| >= delta |S|q^h`.                                (5.5)

Choose one incoming edge for each shell vertex, producing a shortest-path forest rooted at `S`. Let `T` be the first time the walk uses a nonforest edge. Every length-`h` trajectory has probability `1/(|S|q^h)`, hence

`alpha:=Pr(T>h)=|Gamma_h(S)|/(|S|q^h)>=delta`,

and conditional on `T>h`, `Y_h` is uniform on `Gamma_h(S)`.

For a departure at time `t`, list the nonforest incoming edges at each endpoint and condition further on the index `i` of the used edge. If `S_(t,i)` is the set of endpoints admitting an `i`th such edge, then

`beta_(t,i)=|S_(t,i)|/(|S|q^t)`,

and `Y_t` is uniform on `S_(t,i)` under this conditioning.

The key point for the **truncated** version is that the induction hypothesis remains admissible:

`|S_(t,i)| q^((h-t)+C0)`

` <= |S|q^t q^(h-t+C0)`

` = |S|q^(h+C0) <= M`.                                         (5.6)

Thus the exact same conditional-entropy induction applies. If `Z` records either `T>h` or the pair `(T,i)`, then `Z` takes at most `qh+1` values and `H(Z)<=log(qh+1)`. Concavity of entropy, (5.5), and `1-alpha<=1-delta` yield

`H(Y_h) >= log|S|+h log q - delta^(-1)log(qh+1)`.

No growth estimate at any scale beyond `M` was used. ∎

---

## 6. Proposition — endpoint entropy with a quantitative defect

Apply Lemma 4.1 and Lemma 5.1 with

`M=theta N exp(-rho_n)`.

Choose the `C0` from Lemma 5.1, enlarged by a fixed `(d,c)` amount if needed. For an initial oriented edge `e`, set

`h_n=floor(log_q(theta N exp(-rho_n)))-C0`.

Because `rho_n=o(log n)` in the cutoff regime, `h_n>=0` for all large `n`. Lemma 5.1 gives

`H(Q^(h_n)(e,.))`

` >= h_n log q - delta^(-1)log(qh_n+1)`

` >= log(dn) - rho_n - C_1 log log n - C_2`.                    (6.1)

The oriented-edge kernel `Q` is doubly stochastic, so Shannon entropy is nondecreasing under one further `Q` step. Choose the fixed additive constants so that

`h_n <= j_n-1`

for all large `n`. A vertex-started nonbacktracking walk chooses one of `d` initial oriented edges uniformly and then makes `j-1` `Q`-steps. Entropy concavity and monotonicity therefore give, for every `j>=j_n`,

`H(U,Y) >= log(dn)-rho_n-C_1 log log n-C_2`,                    (6.2)

where `(U,Y)` is the final oriented edge. Since at most `d` predecessors `U` can have terminal vertex `Y`,

`H(U|Y)<=log d`.

Therefore

`H(K_j(x,.))=H(Y)>=log n-rho_n-C_1 log log n-C_3`.              (6.3)

This is (3.1), uniformly in the start `x` and all `j>=j_n`.

Define from now on

`Delta_n:=rho_n+C_1 log log n+C_3`.                             (6.4)

---

## 7. Lemma 3 — continuous-time entropy dissipation needs only the one-sided gap

### Lemma 7.1

Let `G` be a finite regular graph with one-sided normalized spectral gap at least `gamma>0`. Let `mu` be any probability law and `H_s=exp(s(P-I))`. Then

`||mu H_s-pi||_TV <= sqrt( D(mu||pi)/(4 gamma s) )`             (7.1)

for every `s>0`.

### Proof

Write `f_s=d(mu H_s)/d pi`. Relative entropy satisfies

`-d/ds D(mu H_s||pi)=E(f_s,log f_s)`,                           (7.2)

where `E` is the Dirichlet form of `I-P`. The elementary inequality

`(a-b)(log a-log b)>=4(sqrt(a)-sqrt(b))^2`

gives

`E(f_s,log f_s)>=4E(sqrt(f_s),sqrt(f_s))`.

By the one-sided Poincare inequality,

`E(sqrt(f_s),sqrt(f_s))>=gamma Var_pi(sqrt(f_s))`.

Finally,

`||mu H_s-pi||_TV^2 <= Var_pi(sqrt(f_s))`;                     (7.3)

indeed Cauchy-Schwarz applied to

`|f-1|=|sqrt(f)-1|(sqrt(f)+1)`

gives exactly this bound.

Hence

`-D'(s)>=4 gamma ||mu H_s-pi||_TV^2`.

Total variation decreases in `s`, so integration over `[0,s]` gives

`4 gamma s ||mu H_s-pi||_TV^2 <= D(mu||pi)-D(mu H_s||pi) <= D(mu||pi)`.

This is (7.1). ∎

By (6.3), every `K_j(x,.)`, `j>=j_n`, has

`D(K_j(x,.)||pi)<=Delta_n`.                                    (7.4)

Thus, after an additional continuous time

`s_(n,epsilon)=Delta_n/(gamma epsilon^2)`                       (7.5)

(up to an inessential fixed numerical factor), all these endpoint laws are within `epsilon/2` of uniform.

---

## 8. Continuous-time covering-tree decomposition

Realize the infinite rooted `d`-regular tree as the tree of finite nonbacktracking paths from `x`. Rate-one continuous-time SRW on the tree projects to rate-one continuous-time SRW on `G`.

Let `R_t` be its distance from the root. By spherical symmetry, conditional on `R_t=j` the tree endpoint is uniform on the radius-`j` sphere. Projection therefore gives the exact mixture

`delta_x H_t = sum_(j>=0) Pr(R_t=j) K_j(x,.)`.                  (8.1)

Away from the root, jumps occur at total rate one and the radial increment is `+1` with probability `q/d`, `-1` with probability `1/d`. The number of returns to zero is almost surely finite; its contribution is tight. Consequently

`(R_t-vt)/sqrt(t) => N(0,1)`,                                  (8.2)

with

`v=(d-2)/d`.

The unit asymptotic variance in (8.2) is the continuous-time Poissonized variance: for a rate-one compound Poisson sum, the variance rate is `E[X^2]=1`.

---

## 9. Mixing-time upper bound

Fix `epsilon in (0,1/2)`, and abbreviate `s_n=s_(n,epsilon/2)=O_(gamma,epsilon)(Delta_n)`.

Use (8.1) for the first `t-s_n` units of time, then apply `H_(s_n)`. From (7.4)-(7.5), every term with `j>=j_n` is within `epsilon/2` of uniform. Therefore

`d_n(t) <= Pr(R_(t-s_n)<j_n)+epsilon/2`,                        (9.1)

uniformly in the starting vertex.

Let

`T_n=L_n/v=(d/(d-2))L_n`.

Since `j_n=L_n+O_d(1)`, the CLT (8.2) implies that for a sufficiently large constant `A=A(d,epsilon)`,

`Pr(R_(T_n+A sqrt(L_n))<j_n) <= epsilon/2`

for all large `n`. Hence

`t_mix(epsilon) <= T_n + A sqrt(L_n) + C_(gamma,epsilon)Delta_n`. (9.2)

---

## 10. Mixing-time lower bound

Choose any deterministic `b_n->infinity` with `b_n=o(sqrt(L_n))`, for example `b_n=log log n`, and put

`r_n=floor(L_n-b_n)`.

The universal degree bound gives

`|B_G(x,r_n)| <= 1+d(q^(r_n)-1)/(q-1)=O_d(n q^(-b_n))`,

so

`pi_n(B_G(x,r_n))=o(1)`                                        (10.1)

uniformly in `x`.

If `R_t<=r_n`, the projected walk lies in `B_G(x,r_n)`. Therefore

`d_n(t) >= Pr(R_t<=r_n)-o(1)`.                                 (10.2)

By (8.2), for sufficiently large `A=A(d,epsilon)`,

`Pr(R_(T_n-A sqrt(L_n))<=r_n)>=1-epsilon+o(1)`.

Thus

`t_mix(1-epsilon) >= T_n-A sqrt(L_n)`                           (10.3)

and the same estimate, with a different constant, gives the lower side for `t_mix(epsilon)`.

Combining (9.2), (10.3), and (6.4) proves (3.2). Since `T_n=Theta_d(L_n)`, (3.3) follows.

If `rho_n=o(log n)`, then `Delta_n=o(L_n)`, so the right-hand side of (3.3) tends to zero: cutoff holds.

---

## 11. Gaussian profile when the growth defect is below the square-root scale

Assume now

`Delta_n=o(sqrt(L_n))`,

which follows from `rho_n=o(sqrt(log n))`.

Choose `s_n` satisfying

`Delta_n/s_n -> 0`, `s_n/sqrt(L_n) -> 0`;                      (11.1)

for example

`s_n=sqrt((Delta_n+1)sqrt(L_n))`.

Lemma 7.1 then makes every `K_j H_(s_n)`, `j>=j_n`, `o(1)`-close to uniform.

At time

`t=T_n+z sqrt(L_n)`

for fixed `z`, the upper mixture bound gives

`d_n(t) <= Pr(R_(t-s_n)<j_n)+o(1)`.

Because `s_n=o(sqrt(L_n))`, (8.2) yields

`Pr(R_(t-s_n)<j_n) -> Phi(-v^(3/2)z)`.                          (11.2)

For the lower bound use `r_n=L_n-b_n` with `b_n->infinity`, `b_n=o(sqrt(L_n))`. Equation (10.1) still gives vanishing stationary ball mass, and

`Pr(R_t<=r_n) -> Phi(-v^(3/2)z)`.                              (11.3)

The upper and lower bounds match, uniformly in the start, proving (3.4).

For `rho_n=A log log n`, `Delta_n=O(log log n)=o(sqrt(log n))`, so tree-rate expansion only up to `n/(log n)^A` gives the same optimal square-root profile as full LRE.

---

## 12. Three-route comparison for this iteration

### Route A — stop LRE at the entropy scale: SUCCESS

The proof above is retained. The key observation is quantitative: if the forest argument starts with only `N exp(-rho_n)` reachable states available at tree rate, the resulting endpoint law is deficient by only `rho_n+O(log log n)` nats. Continuous-time spectral entropy production then pays exactly this deficit. Macroscopic LRE beyond that scale is unused.

This directly isolates the use of Altschuler's LRE hypothesis rather than treating the whole condition as atomic.

### Route B — derive (PE) from vertex transitivity plus ordinary spectral expansion: FAILS, with an admissible obstruction

Altschuler's Section 2.3 gives a sharp warning. Let `H_m` be a `d`-regular vertex-transitive spectral-expander sequence (one may take a vertex-transitive Ramanujan family), and let

`G_m=H_m square K_2`,

i.e. two copies of `H_m` joined by the matching between corresponding vertices. Then `G_m` is `(d+1)`-regular, vertex-transitive, and has a uniform one-sided spectral gap. But with the top branching parameter `q_top=d`,

`|B_G((x,i),r)| <= 2 |B_H(x,r)| <= C_d (d-1)^r`.

For any `rho_n=o(log n)`, choose, say,

`r=floor((1/2)log_d n)`.

Then `d^r<=n exp(-rho_n)` for all large `n`, while

`|B_G((x,i),r)|/d^r <= C_d ((d-1)/d)^r -> 0`.

So no fixed `c>0` can make (PE) hold. Thus **transitivity plus spectral expansion does not imply the successful hypothesis**, even when the allowed truncation defect is any `o(log n)` quantity. A proof of Salez Problem 2.3 must therefore use something beyond pre-entropic maximal tree growth.

This family is an obstruction to the implication, not a counterexample to cutoff.

### Route C — finite-fiber quotient / local blow-up transfer: deliberately not pursued here

The newest neighboring P26 report proves an exact finite-fiber entropy/TV transfer for lexicographic blow-ups, and the NM13 companion owns the line-graph mechanism. Continuing with another local-fiber gadget would duplicate active peer ownership and, in any case, would not isolate Altschuler's LRE use. This route was pruned after reading those reports.

---

## 13. Source before / after and remaining full-scope gap

### Source before

Salez Problem 2.3 remains the conjecture that **every** bounded-degree vertex-transitive spectral-expander sequence has total-variation cutoff. Altschuler (arXiv:2609.14945v1, submitted 14 September 2026) proves the stronger-hypothesis fixed-degree LRE case, with an optimal Gaussian profile. The arXiv record checked in this run still exposes only v1; no v2/erratum surfaced in the bounded current search.

### Source after

The source remains **OPEN**. The newly proved class is:

> fixed-degree, one-sided spectral expanders for which tree-rate set growth is known only up to `n exp(-rho_n)`, with `rho_n=o(log n)`.

For the especially clean subclass `rho_n=A log log n`, full macroscopic LRE is replaced by growth only up to `n/(log n)^A`, yet the same Gaussian `Theta(sqrt(log n))` profile is proved.

This is stronger than merely restating an entropy criterion: (3.1) is proved from the explicit graph-growth hypothesis by a complete truncated version of the oriented-edge / forest argument.

### Remaining gap

The two-copy vertex-transitive expander obstruction above shows that no argument can finish Salez 2.3 by proving even this truncated maximal-tree-growth condition from transitivity plus spectral expansion alone. The next genuinely different route has to exploit a weaker object than set-volume growth—for example a weighted/average path-collision or Green-function estimate that can survive `H square K_2` and other local product operations.

Worldwide novelty of PE-CUTOFF is **UNVERIFIED**; the bounded search did not surface this exact truncated-LRE theorem, but negative search is not a priority certificate.

No finite computational checker is applicable: all claims retained here are analytic identities/inequalities with complete proofs on the page.