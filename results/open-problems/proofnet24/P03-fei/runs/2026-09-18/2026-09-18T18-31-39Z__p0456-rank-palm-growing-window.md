Model actually run: **GPT-5.6 Sol. Reasoning level: UNVERIFIED. This is not GPT-6 at maximum.**

**NO SOURCE-LEVEL METRIC MOVEMENT; NEW GROWING-WINDOW STRENGTHENING.** The admitted coefficient frontiers remain saturated at `c_LK^cert=a_LK^fine=b_LK^sqrt=0`; HARD recoveries remain `0/2`. This run uses Section-B methods **#8 GO THE OTHER WAY AND DISCRETIZE, #20 FIND WHY THE ALGORITHM FAILS, #27 SWAP THE QUANTIFIERS**. The main advance is an exact finite-rank repair of the weakest Palm lemma in Claim 293 and a uniform Poisson/connectivity theorem on every sublinear offset window `|k-log n|<=C_n`, `C_n=o(log n)`.

# P03 / P0456 run report — rank-Palm repair and a growing Poisson window

Run timestamp: **2026-09-18T18:31:39Z**  
Track: **P03**  
Canonical target: **P0456**  
Repository / branch: `yspennstate/math-open-problems` / `master`  
Category: **HARD OUTSIDE**

---

## 1. Continuity, source status, repository screen, and audit gate

The exclusive canonical assignment remains

`operations/claims/P0456.md`,

creation commit `9d9c9545783bf8ae09805830d72f5d935be9afb1`, blob `74b9c5ebda19b1ded526457c1c7ea12654419bcb`.

The newest complete P03 report entering this run was

`proofnet24/P03-fei/runs/2026-09-18/2026-09-18T17-31-34Z__p0456-sizebias-localblock-coupling.md`,

creation commit `56c152443ca91e636cb88af9ad31508d110aeb42`, blob `9e1eed2b7addb38197250b033fef14fb98777716`; its exact-commit chunked readback recovered `**End of complete run report.**`.

I preserve Claims 274, 276, 278, 280, 282, 284, 286 and the source-matching/audit chain 288--293.

This invocation reread/recovered the root `README.md`, `proofnet24/HOURLY_PROTOCOL_2026-09-15.md`, current `FLEET_RULES.md`, `operations/new_methods_2026-09-16/OWNER_DIRECTIVE.md`, campaign `probability_campaign_2026_09/INDEX.md` and `RANKING.md`, root `POSTED.md` and `RESULTS.md`, the canonical P0456 claim, the complete Claim-288 one-root marked-saddle proof, the Claim-291 bounded-omission/small-component kernel, the Claim-293 Palm coupling, and the current P26/P04 streams. Several shared-root and campaign surfaces are connector-truncated; I do **not** represent those as byte-for-byte rereads of their whole histories. Exact-path reads and targeted searches were used for controlling facts.

`RESULTS.md` still contains a compact stale P03/FEI row; it is not used to reset the much newer P0456 state. P0457 remains a distinct diameter question and is not touched here.

### Fresh source / literature check

The primary source is still:

Hossein Dabirian and Vijay Subramanian, *Connectivity of a family of bilateral preference random graphs*, *Journal of Applied Probability* 63(2) (June 2026), 552--579, published online 18 December 2025, DOI `10.1017/jpr.2025.10051`.

Cambridge still lists the same paper and model: iid continuous weights on `K_n`, with an edge retained iff it is among the `k` lightest incident edges at both endpoints. The source's Section 1.1 records the unresolved displayed band

`log n -(1/2) loglog n sqrt(log n) <= k <= log n +(1/2) loglog n sqrt(log n)`

and explicitly points to sharper/exact sufficient conditions as the route to closing the gap. The source's Lemmas 10--14 and Theorems 4--6 remain the published coarse-window framework used by the preserved chain.

Fresh bounded 2026-09-18 searches for the exact title/DOI/authors, `LK(n,k) Poisson isolated vertices`, `LK(n,k) log n+c connectivity`, and bilateral-preference constant-window results recovered the primary paper and adjacent random-graph work but no later theorem matching Claims 288--293 or the strengthening below. This is dated bounded negative evidence only; **publication novelty remains UNVERIFIED**.

For the Stein step I also rechecked Larry Goldstein and Gesine Reinert, *Total Variation Distance for Poisson Subset Numbers*, *Annals of Combinatorics* 10 (2006), 333--341, DOI `10.1007/s00026-006-0291-9`. Its standard size-bias inequality is methodology only, not prior art for P0456.

### Fresh outside-audit screen

A repository-wide search for `P0456`, the exact Claim-288/289/293 identifiers, `audit`, and `PASS` found **no P26 or distinct OTHER-track full-chain audit** of the P0456 source-matching proof. The newest concrete P26 report recovered during this run is

`proofnet24/P26-proof-audit-recovery/runs/2026-09-18/2026-09-18_21-01-00__run-report.md`,

creation commit `029f855a2435c3a87df0328d0aeab2ad87c2e985`; it audits a historical P04/I0101 harmonic-orbit claim, not P0456. P04 remains rotation-stopped and has no genuinely new mathematical theorem for the directed P03->P04 duty. No repeat peer audit is fabricated.

Therefore the closure gate remains

`P0456_ACTIVE_AUDIT_PENDING / OUTSIDE_AUDITS_FOUND_0_OF_2`.

Self-audits do not count. No final paper folder is created.

---

## 2. Preserved candidate-complete chain and new claim

The source-matching chain remains:

- `P03-P0456-POISSON-CRITICAL-WINDOW-288 = PROVED / SOURCE-MATCHING-CANDIDATE-COMPLETE / AUDITS-PENDING / PUBLICATION-NOVELTY-UNVERIFIED`;
- `P03-P0456-UNIFORM-POISSON-INTERACTION-REPAIR-289 = PROVED / SELF-AUDIT-REPAIR / SOURCE-MATCHING-STRENGTHENING / AUDITS-PENDING / PUBLICATION-NOVELTY-UNVERIFIED`;
- `P03-P0456-MARKED-POISSON-CROSSCHECK-290 = PROVED / SELF-AUDIT-STRENGTHENING / AUDITS-PENDING / PUBLICATION-NOVELTY-UNVERIFIED`;
- `P03-P0456-PAIR-SMALLCOMP-AUDIT-KERNEL-291 = PROVED / SELF-AUDIT-KERNEL / SUPPORTING / AUDITS-PENDING / PUBLICATION-NOVELTY-UNVERIFIED`;
- `P03-P0456-FINITE-PALM-INTERACTION-GRAPH-292 = PROVED / SELF-AUDIT-STRENGTHENING / SUPPORTING / AUDITS-PENDING / PUBLICATION-NOVELTY-UNVERIFIED`;
- `P03-P0456-LOCALBLOCK-SIZEBIAS-STEIN-293 = PROVED / SELF-AUDIT-STRENGTHENING / SUPPORTING / AUDITS-PENDING / PUBLICATION-NOVELTY-UNVERIFIED`.

This run adds:

### Claim `P03-P0456-RANK-PALM-SUBLINEAR-WINDOW-294`

**Status:** `PROVED / SELF-AUDIT-STRENGTHENING / SUPPORTING / AUDITS-PENDING / PUBLICATION-NOVELTY-UNVERIFIED`.

Let `C_n>=0` be any deterministic sequence with

`C_n=o(log n)`.                                                (2.1)

Uniformly over all integers `k` satisfying

`|k-log n|<=C_n`,                                              (2.2)

let `Z_n` be the number of isolated vertices of `LK(n,k)` and set

`lambda_n=n e^{-k}`.                                          (2.3)

Then

`d_TV(Law(Z_n),Poisson(lambda_n)) -> 0`,                      (2.4)

and

`P(LK(n,k) is connected)=exp(-lambda_n)+o(1)`,               (2.5)

uniformly under (2.2).

The proof is genuinely uniform beyond every fixed bounded offset: `lambda_n` may tend to zero, a positive finite value, or infinity at an arbitrary subpolynomial rate. This does **not** claim that `o(log n)` is the largest possible window for Poisson approximation; the maximal growing window remains open.

The key technical repair is stronger than Claim 293 Lemma 5.1: it is an exact binomial/rank identity valid for **all** selected-neighbour deadlines, including extreme deadlines and arbitrary numbers of already-active internal competitors.

---

## 3. #20 attack the weakest point first — an exact binomial tail-ratio lemma

Claim 293 Lemma 5.1 used the statement

`E[Bin(N,d) | Bin(N,d)>=h]=O(k)`

for `d=O(k/n)` and `h<=k+O(1)`. Its two-case explanation was the weakest new point and had to survive extreme deadlines. Instead of patching the prose, I prove a finite exact inequality which is stronger and removes the delicate regime split entirely.

### Lemma 3.1 (exact conditional binomial mean)

Let

`X~Bin(N,p)`, `mu=Np`, and `1<=h<=N`.

Then

`E[X | X>=h] <= mu+h`.                                       (3.1)

For `h=0` the same inequality is trivial.

#### Proof

Let `Y~Bin(N-1,p)`, and write

`A=P(Y=h-1)`, `B=P(Y>=h)`.

The standard size-bias identity gives

`E[X 1_{X>=h}]=Np P(Y>=h-1)=mu(A+B)`,                        (3.2)

whereas

`P(X>=h)=pA+B`.                                               (3.3)

Thus (3.1) is equivalent to

`[mu-(mu+h)p] A <= hB`.                                      (3.4)

If the coefficient on the left is nonpositive there is nothing to prove. Otherwise use the first term of the upper tail:

`B >= P(Y=h)
   = A * (N-h)p/[h(1-p)]`.                                   (3.5)

Therefore

`hB >= A (N-h)p/(1-p)`.                                      (3.6)

It remains only to check

`(N-h)p/(1-p) >= mu-(mu+h)p`.                                (3.7)

For `p>0`, divide by `p` and multiply by `1-p`. The difference between the two sides becomes

`N-h-[N(1-p)-h](1-p)
 = p(2N-Np-h)>=0`,                                           (3.8)

because `p<=1` and `h<=N`. This proves the lemma. `square`

This exact inequality is the missing uniform tail-ratio statement. In particular, it remains valid when `Np` is far below, comparable to, or far above `h`.

---

## 4. #8 discretize — a nested-rank lemma for one external edge

The Palm low-edge question can be expressed without continuous-density heuristics.

Let `U_1,...,U_N` be iid Uniform[0,1]. For `t in [0,1]` put

`X_t=#{i:U_i<=t}`.

### Lemma 4.1 (nested-threshold rank bound)

For `0<=D<=d<=1` and `0<=h<=N`,

`P(U_1<=D | X_d>=h) <= D + h/N`.                             (4.1)

More exactly, when `d>0`,

`P(U_1<=D | X_d>=h)
 = (D/d) E[X_d | X_d>=h]/N`.                                 (4.2)

#### Proof

Conditional on `X_d=j`, the `j` points below `d` are exchangeable iid Uniform[0,d] locations, so

`E[X_D | X_d=j]=(D/d)j`.                                    (4.3)

Averaging (4.3) over `X_d>=h` gives (4.2). By exchangeability,

`P(U_1<=D | X_d>=h)=E[X_D | X_d>=h]/N`.                     (4.4)

Lemma 3.1 gives

`E[X_d | X_d>=h] <= Nd+h`,                                  (4.5)

and (4.1) follows. `square`

If instead `d<D`, then

`P(U_1<=D | X_d>=h)
 <= d+h/N+(D-d)/(1-d)`.                                      (4.6)

Indeed the first part is Lemma 4.1 at `D=d`, and conditional on `U_1>d`, the residual location of `U_1` is Uniform[d,1] and is independent of the threshold-count event contributed by the other points.

### Corollary 4.2 (uniform Palm low-edge bound, repaired Claim 293 Lemma 5.1)

Fix `L<infinity`. Let `V` be the Palm root, `S` its top-`k` neighbour set, and `a in S`. Conditional on all root-star data and all local internal edges except a specified external edge `{a,x}` with `x notin {V} union S`, the Palm isolation condition at `a` has the form

`X_d>=h_a`,                                                   (4.7)

where `d=W(V,a)` and **only**

`0<=h_a<=k`                                                   (4.8)

is needed. In particular, no assumption `h_a=k-O(1)` is required.

For any threshold `D<=Lk/n` independent of the target edge after the indicated exposure,

`P(W(a,x)<=D | Top_k(V)=S, I_V=1, exposed data)
 <= C_L k/n`                                                  (4.9)

uniformly whenever `k=o(n)`.

#### Proof

Every internal competitor at `a` below the root proposal deadline is already fixed by the exposure. If there are `r_a` such competitors, the root edge is rejected precisely when the independent external-star count below `d` is at least

`h_a=max(0,k-r_a)`,                                          (4.10)

so (4.7)--(4.8) are exact. External stars belonging to distinct selected neighbours are edge-disjoint once internal selected-selected edges have been exposed, hence the other Palm rejection constraints do not further reweight these external edges.

If `D<=d`, Lemma 4.1 yields

`P(W(a,x)<=D | ...)
 <= D+h_a/N
 <= Lk/n+k/(n-O(k))=O_L(k/n)`.                              (4.11)

If `d<D`, use (4.6): because `D=o(1)`, its right side is at most

`2D+h_a/N=O_L(k/n)`                                          (4.12)

for large `n`.

The ordinary (non-Palm) local law is easier: without the rejection conditioning the edge is simply uniform after whatever root-top-`k` truncation applies. For the root endpoint `a=V`, conditioning on the root `k`th threshold `T=t` and `x notin S` makes `W(V,x)` Uniform[t,1], again giving `O_L(k/n)`.

Thus (4.9) holds pointwise in the deadline data, not merely after averaging. `square`

### What the attack found

I tried specifically to break Claim 293 at the two extreme regimes:

- very small selected-neighbour proposal deadline `d`, where `X_d>=h` is a severe upper-tail conditioning;
- very large `d`, where many internal competitors may already be active and `h_a` can be far below `k`.

Neither produces a counterexample. Lemma 4.1 handles both with the same exact finite-rank inequality. This materially strengthens Claim 293's weakest lemma.

---

## 5. The exact finite ranks that can flip a distant isolation mark

The Palm coupling of Claim 293 is retained exactly. Choose a uniform root `V`, let `S` be its first `k` neighbour labels, put

`A={V} union S`,                                               (5.1)

and couple the ordinary and isolated-root Palm graphs by sharing every edge wholly outside `A` and resampling only the local block of edges touching `A`.

Fix `w notin A`. Let

`R_w = kth smallest edge from w to V\A`.                     (5.2)

Because the far block is shared, a change in `I_w` can occur only through one of two finite rank mechanisms.

### Type P: proposal-rank witness

Some changed edge `{w,a}`, `a in A`, enters the relevant first-`k` ranks of `w` in at least one copy. On the event

`R_w<=Lk/n`,                                                  (5.3)

this requires a changed local edge of weight at most `Lk/n`. There are at most `|A|=k+1` candidate local edges.

### Type R: reciprocity-rank witness

Suppose the proposal list of `w` itself is unchanged. For one of its at most `k` far proposed neighbours `u`, the bilateral status of `{w,u}` can change only if some changed edge `{u,a}`, `a in A`, crosses below the fixed deadline `W(w,u)`. Under (5.3), every such proposal deadline is at most `Lk/n`. There are at most

`k(k+1)`                                                     (5.4)

candidate changed edges.

These are the **only** possibilities. Acceptance of `{w,u}` at `u` counts raw edge weights incident to `u`; it has no recursive dependence on whether those competitor edges themselves survive bilateral preference. Hence there is no hidden depth-two exploration.

### Lemma 5.1 (bare rank-witness bound)

For either copy of the local block, and uniformly for `k=o(n)`,

`P(w has a Type-P or Type-R witness, R_w<=Lk/n)
 <= C_L k^3/n`.                                               (5.5)

#### Proof

Type P has `O(k)` candidates and Type R has `O(k^2)`. For an ordinary local edge the probability to fall below a fixed `O(k/n)` deadline is `O(k/n)`. For a Palm local edge it is `O(k/n)` by Corollary 4.2. A union bound over both coupled copies gives (5.5). `square`

Choose `L` so that the lower-tail Chernoff rate

`rho_L=L-1-log L`                                             (5.6)

is larger than `5`. Then, since `k=(1+o(1))log n` in the growing window considered later,

`P(R_w>Lk/n) <= exp[-rho_L k+o(k)] = n^{-5+o(1)}`.           (5.7)

Thus the finite rank representation gives the Palm coupling obstruction in purely combinatorial order-statistic terms.

---

## 6. Typical rather than worst-case influence, uniformly for `k~log n`

A bare witness probability `O(k^3/n)` is not enough after summing over `n` outside vertices; the rare-isolation factor is essential.

Suppose `I_w` differs between the ordinary and Palm copies. Then `w` is isolated in at least one copy and a Type-P/Type-R witness occurs, except on (5.7). Fix a witness-labelled candidate edge. Once its relevant rank crossing is exposed, omit every rejection deadline directly touched by that witness. Claim 291's bounded-omission marked-saddle lemma gives, uniformly whenever

`k=(1+o(1))log n`,                                            (6.1)

`P(the remaining rejection conditions for w) <= exp[-k+o(k)]`. (6.2)

The rank crossing itself costs `O(k/n)` by Corollary 4.2. Summing over `O(k^2)` witness-labelled candidates and both coupled copies gives

`P(I_w(G) != I_w(G^s))
 <= (C k^3/n) exp[-k+o(k)] + n^{-5+o(1)}.`                   (6.3)

Summing (6.3) over the `n-O(k)` vertices outside `A`,

`E[number of outside isolation-mark flips]
 <= C k^3 exp[-k+o(k)] + n^{-4+o(1)}
 = n^{-1+o(1)}`                                               (6.4)

under (6.1).

For the `k` selected vertices in `S`, a mark change still forces an isolation event with only a bounded number of local deadlines distinguished; the same bounded-omission lemma yields

`E[number of selected-vertex flips] <= k exp[-k+o(k)]=n^{-1+o(1)}`. (6.5)

At the Palm root itself, `I_V(G^s)=1`, and in the comparison

`Z_n^s-(Z_n+1)`                                               (6.6)

the residual root contribution is just `-I_V(G)`, of expectation

`P(I_V)=exp[-k+o(k)]=n^{-1+o(1)`.                            (6.7)

Consequently the exact Claim-293 size-bias coupling now satisfies the growing-window estimate

`E|Z_n^s-(Z_n+1)| = n^{-1+o(1)}`                             (6.8)

uniformly whenever (6.1) holds. No deterministic Lipschitz statement is used; Claim 293's `Theta(n)` worst-case influence example remains valid.

By the standard Goldstein--Reinert size-bias Stein inequality,

`d_TV(Law(Z_n),Poisson(mu_n))
 <= (1-e^{-mu_n}) E|Z_n^s-(Z_n+1)|`,                         (6.9)

where `mu_n=E Z_n`. Hence

`d_TV(Law(Z_n),Poisson(mu_n))=n^{-1+o(1)}`                  (6.10)

uniformly for `k=(1+o(1))log n`.

I use (6.10) only as an asymptotic order statement; no sharp constant is claimed.

---

## 7. #27 swap the quantifiers — uniform one-root asymptotics on `o(log n)` offsets

To replace `mu_n` by the explicit `lambda_n=n e^{-k}` when `lambda_n` may itself grow, a merely relative `1+o(1)` one-root estimate is not enough. We need the error to beat the possible subpolynomial growth of `lambda_n`.

Claim 288's exact marked-saddle proof already contains this quantitative margin. I record it explicitly.

Let the clean outside-neighbour marking probability be

`M_{k,k}=(m)_{k+1}/k! int_0^1 Q_k(x)^k(1-x)^(m-k-1) dx`,     (7.1)

with

`m=n+O(1)`, `N=n+O(k)`,

`Q_k(x)=E[(x-B_k)_+]`,

`B_k~Beta(k,N-k+1)`,

`beta=E B_k=k/(N+1)`.                                        (7.2)

Replacing `B_k` by its mean gives the exact beta integral

`M_0=(1-beta)^m
    =e^{-k}(1+O(k^2/n))`.                                    (7.3)

Choose the same split as Claim 288,

`x_0=beta+k/(2N)`.                                           (7.4)

For `x>=x_0`, the beta/order-statistic Chernoff bound gives constants `eta_1>0`, `C<infinity`, uniform for `k/log n` in a fixed compact subset of `(0,infinity)`, such that

`P(B_k>x)<=C e^{-eta_1 k}`.                                  (7.5)

Since `sd(B_k)=O(sqrt(k)/n)`,

`R(x):=E[(B_k-x)_+]
 <= O(sqrt(k)/n)e^{-eta_1 k/2}`.                             (7.6)

Because `x-beta>=k/(2N)`, raising

`Q_k(x)=x-beta+R(x)`                                         (7.7)

to the `k`th power changes the dominant integrand by at most

`1+O(sqrt(k)e^{-eta_1 k/2})`.                               (7.8)

On `x<x_0`, the normalized beta-integrand rate is separated from its saddle at `x-beta~k/N` by a fixed positive constant times `k`; the `O(sqrt(k)/n)` beta fluctuation cannot close that gap. Therefore this whole region contributes at most

`e^{-eta_2 k} M_0`                                           (7.9)

for some `eta_2>0`.

Combining (7.3), (7.8), and (7.9), there is an absolute `eta>0` such that

`M_{k,k}=e^{-k}[1+O(k^2/n)+O(sqrt(k)e^{-eta k})]`            (7.10)

uniformly for, say, `k/log n in [1/2,3/2]` and all sufficiently large `n`.

Now return from the clean sufficient event to exact isolation. On the high-probability root-threshold event `X_(k)<=Lk/n`, a specified internal selected-selected edge is active with probability `O(k/n)`. Exactly as in Claim 288, one active edge is bounded using the fixed-defect marked saddle and two or more active edges have probability `O(k^6/n^2)`. Choosing the root-threshold Chernoff rate larger than `3` yields

`P(I_v)
 =e^{-k}[1+O(sqrt(k)e^{-eta k})+n^{-1+o(1)}]`               (7.11)

uniformly whenever `k=(1+o(1))log n`.

The `n^{-1+o(1)}` term in (7.11) absorbs `k^2/n`, the one-active-edge relative error, the at-least-two-active-edge term after division by `e^{-k}`, and the root-threshold tail.

### Consequence for a growing offset window

Let `C_n=o(log n)` and assume (2.2). Then

`k=(1+o(1))log n`,                                           (7.12)

and

`lambda_n=n e^{-k}=n^{o(1)}`.                               (7.13)

By (7.11), with `mu_n=nP(I_v)`,

`|mu_n-lambda_n|
 <= lambda_n[O(sqrt(k)e^{-eta k})+n^{-1+o(1)}]
 =o(1)`.                                                      (7.14)

For Poisson laws,

`d_TV(Poisson(mu_n),Poisson(lambda_n))<=|mu_n-lambda_n|`,     (7.15)

so (6.10), (7.14), and (7.15) prove (2.4).

This is the successful quantifier swap:

> a single theorem holds for **every deterministic** `C_n=o(log n)`, uniformly over every integer `k` in the entire band `|k-log n|<=C_n`.

I do **not** claim that `o(log n)` is maximal. A fixed-fraction window may also be accessible after optimizing the quantitative saddle constants, but the present proof does not establish the largest fraction and I do not encode an unknown frontier as a theorem.

---

## 8. Nontrivial components vanish uniformly on the same growing window

The Poisson theorem controls isolated vertices; connectivity still requires exclusion of every nontrivial component under the literal bilateral-preference definition.

### Sizes `2<=r<=6`

Claim 291 conditions only on the necessary internal spanning-tree weights and uses, at each component vertex, the first

`p=k-(r-1)`                                                   (8.1)

**external** proposals. Those external proposals are among the global top `k` regardless of the internal tree weights. Its generalized marked-saddle/bounded-interaction argument therefore gives, for each fixed `r<=6`,

`P(exists an r-component)
 <= n^r (Ck/n)^(r-1) exp[-rk+o(k)]`.                         (8.2)

When `k=(1+o(1))log n`, the right side is

`n^{1-r+o(1)} ->0`.                                          (8.3)

### Sizes `7<=r<=12`

Claim 280's exact Exp(1)-threshold/Cayley bound gives, for fixed `r`,

`log P(exists an r-component, envelope)
 <= log n -(5r/32)k+O_r(log k)`.                             (8.4)

For `r>=7` and `k=(1+o(1))log n`, the coefficient of `log n` tends to

`1-5r/32<0`,                                                  (8.5)

so all fixed sizes `7,...,12` vanish uniformly under (2.2).

### Sizes `13<=r<=n/2`

Claim 278's retained global Exp(1) threshold-envelope argument excludes this entire range with a strict negative exponential margin when `k/log n->1`. The envelope failure event is paid once before summing component sizes. Replacing `k=log n+O(sqrt(log n loglog n))` by the more general relation `k=(1+o(1))log n` changes only `o(log n)` terms in the exponent and does not change the strict sign of the retained margin.

Hence

`P(exists a nontrivial component)=o(1)`                      (8.6)

uniformly under (2.2). Combining (8.6) with (2.4),

`P(connected)
 =P(Z_n=0)+o(1)
 =exp(-lambda_n)+o(1)`,                                      (8.7)

which proves (2.5). No mean-degree inference is used anywhere.

---

## 9. Claim 294, what moved, and what did not

`P03-P0456-RANK-PALM-SUBLINEAR-WINDOW-294 = PROVED / SELF-AUDIT-STRENGTHENING / SUPPORTING / AUDITS-PENDING / PUBLICATION-NOVELTY-UNVERIFIED`

is exactly the conjunction of Sections 3--8.

It strengthens the source-matching package in three ways:

1. Claim 293's weakest Palm low-edge lemma is replaced by the exact finite inequality `E[Bin(N,p)|>=h]<=Np+h`, valid for every threshold and every `0<=h<=k`;
2. the Palm coupling is discretized to an explicit finite rank witness set of size `O(k^2)` per outside test vertex;
3. the TV-Poisson and connectivity formulas become uniform on **every** sublinear offset window `|k-log n|<=o(log n)`, not just fixed bounded offsets.

It does **not** move a source/fleet coefficient metric: all three admitted coefficient metrics were already saturated at zero. It also does not satisfy the two-outside-audit closure gate.

---

## 10. Failed routes, honesty boundaries, and remaining obligation

### 10.1 The attempted extreme-deadline counterexample failed

The most plausible failure of Claim 293 was that Palm conditioning at a selected neighbour with a very small deadline could force a specified external edge below an `O(k/n)` target with probability much larger than `k/n`. Lemmas 3.1 and 4.1 rule this out exactly. The opposite extreme, where many internal edges already satisfy the rejection count and `h_a` is much smaller than `k`, is easier, not harder.

### 10.2 No maximal growing window is proved

The established class is `C_n=o(log n)`. The proof likely survives some fixed-fraction offsets after explicit optimization of the marked-saddle exponent, but this run does not calculate a sharp fraction. Therefore no “largest window” claim is made.

### 10.3 No sharp Stein constant is claimed

Equation (6.10) records only the robust order `n^{-1+o(1)}` from the rank-witness proof. Constants were not optimized, and the principal source theorem needs none.

### 10.4 Outside audits remain the controlling blocker

Claims 288/289 remain candidate-complete but protocol-audit pending. Claim 294 is still a P03 self-audit strengthening, not an independent audit. Publication novelty remains unverified after a bounded search miss.

---

## 11. Directed peer-audit duty

The directed duty remains P03 -> P04/I0101. The newest recovered P04 files are rotation-stop/readback records and create no genuinely new mathematical claim. I therefore do **not** recycle an older P04 claim or fabricate a new peer audit in this run.

---

## 12. Metric, stuck, recovery, and next state

Current mathematical/protocol state:

`P0456_ACTIVE_AUDIT_PENDING / c_LK^cert=0 SATURATED / a_LK^fine=0 SATURATED / b_LK^sqrt=0 SATURATED / OUTSIDE_AUDITS_FOUND_0_OF_2 / CLAIM_294_GROWING_WINDOW_AUDIT_KERNEL_READY / RECOVERIES_USED=0/2`.

No saturated `0 -> 0` coefficient is counted as a stuck run. External-audit waiting is also not converted into a fake mathematical stuck count.

### Next attack

First priority remains any incoming P26 or genuinely distinct OTHER-track audit of Claims 288--294; any gap found there overrides all strengthening work.

If no such audit has arrived, use fresh Section-B methods **#10 DERANDOMIZE, #23 DO WHAT THE PROPOSER DID NOT EXPECT, #26 HUNT THE SPORADIC CASE**:

1. **#10:** replace the conditional local-block sampler in Claim 293 by an explicit monotone/rank surgery, if possible, so an outside auditor can verify the Palm coupling without invoking abstract regular conditional distributions;
2. **#23:** assume the Poisson description fails at the first correction order and search for a size-two-component or joint-isolation correction that remains visible after multiplying by `n`; compute the candidate correction before trying to prove it vanishes;
3. **#26:** probe offsets `k=(1-alpha)log n+O(1)` for fixed small `alpha>0` to locate the first actual breakdown of the Poisson approximation proof. Any fixed-fraction theorem requires a new explicitly audited rate calculation; do not extrapolate Claim 294.

If two genuine outside full-proof PASS audits arrive, create the self-contained source-matching paper folder in that same run if practical and request shared-ledger closure only through `ledger_delta`; P03 does not edit shared root ledgers itself.

---

## 13. `ledger_delta` for P26

```yaml
ledger_delta:
  track: P03
  intake: P0456
  source: "Dabirian--Subramanian, Connectivity of a family of bilateral preference random graphs, J. Applied Probability 63(2) (2026), Section 1.1"
  canonical_claim: operations/claims/P0456.md
  source_status: OPEN_IN_PUBLISHED_SOURCE__CANDIDATE_COMPLETE_INTERNAL_PROOF__AUDITS_PENDING
  source_metric_c_LK_cert: 0
  fine_metric_a_LK_fine: 0
  sqrtlog_metric_b_LK_sqrt: 0
  metrics_state: SATURATED_DO_NOT_COUNT_AS_STUCK
  metric_movement_this_run: false
  recoveries_used: 0/2
  preserved_claims:
    - P03-P0456-POISSON-CRITICAL-WINDOW-288
    - P03-P0456-UNIFORM-POISSON-INTERACTION-REPAIR-289
    - P03-P0456-MARKED-POISSON-CROSSCHECK-290
    - P03-P0456-PAIR-SMALLCOMP-AUDIT-KERNEL-291
    - P03-P0456-FINITE-PALM-INTERACTION-GRAPH-292
    - P03-P0456-LOCALBLOCK-SIZEBIAS-STEIN-293
  new_claim: P03-P0456-RANK-PALM-SUBLINEAR-WINDOW-294
  new_claim_status: PROVED_SELF_AUDIT_STRENGTHENING_SUPPORTING_AUDITS_PENDING_PUBLICATION_NOVELTY_UNVERIFIED
  new_claim_statement: "For every deterministic C_n=o(log n), uniformly over integer |k-log n|<=C_n, d_TV(Law(Z_n),Poisson(n e^-k))->0 and P(LK(n,k) connected)=exp(-n e^-k)+o(1)."
  key_repair: "Exact binomial rank bound E[Bin(N,p)|Bin(N,p)>=h] <= Np+h; Palm low-edge lemma now pointwise for all deadlines and all 0<=h<=k."
  outside_audits_found: 0/2
  closure_state: P0456_ACTIVE_AUDIT_PENDING
  paper_package_created: false
  publication_novelty: UNVERIFIED
  p04_directed_audit: "No genuinely new P04 theorem available; no repeat audit fabricated."
  next_methods: [10, 23, 26]
```

**End of complete run report.**