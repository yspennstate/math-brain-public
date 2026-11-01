# FOREST / fleet02 B02 — spectral-cap comparison + independent review of `FOREST-KN-HERMITE-REDUCTION-v1`

**Run:** `B02-20260922T013646Z-forest-r12`  
**Outcome:** `ESSENTIAL_STEP_APPLIED`  
**Lead candidate review:** `PASS_SOURCE_BOUND_REVIEW_1`  
**Parent target:** `OPEN` under collective protocol pending a second independent end-to-end review  
**FULL_PROOF_CANDIDATE:** `false` for this worker/run; no solved-problem promotion  
**Context:** `WITHOUT_VERIFIED_BRAIN`

## 1. Control and scope

Fresh owner controls were read from `yspennstate/math-research-brain` at initial main
`2026-09-22.2`; active directive is
`COLLECTIVE-OPEN-PROBLEMS-20260921T234023Z`; B02 is assigned FOREST research.
Older brain-installation and benchmark work is stopped. A final freshness comparison to
main `a2b3fdce0ed79e3ab67973fe56b206ae21d979fe` found no changes to
`AGENTS.md`, `scheduled_tasks/README.md`, `fleet.json`, `roles.json`,
`PROTOCOL.md`, ORDER, TARGETS, or ASSIGNMENTS during this run.

The canonical status-login write was attempted and blocked by the platform safety layer;
the scoped scientific start record was created instead. No scheduler mutation was made.

## 2. Latest lead version consumed

I consumed the latest lead handoff
`fleet01/B01` / `FOREST-KN-HERMITE-REDUCTION-v1`,
handoff blob `cad5f1b8546f44f200d441b71095a9fde4a20d4b`,
and its immutable private scientific report created at commit
`77e2822624d2ea3881807aa7bfa56174563728c6`
(readback blob `e11be369a70e59449ea744da6f1e32040889c216`).

The lead's end-to-end candidate is:

1. prove the unit forest inequality for every complete graph `K_n`;
2. use Cocks's fixed-graph theorem to upgrade `M(K_n)` to independence correlation for
   all positive weights;
3. use Semple--Welsh Proposition 3.5 (minor closure);
4. every finite simple graph is an edge-deletion restriction of a complete graph.

I independently audited this chain below.

## 3. Source-valid fixed-graph reduction: review PASS

The published Semple--Welsh paper, *Negative Correlation in Graphs and Matroids*,
Combin. Probab. Comput. 17 (2008), gives exactly the two source facts needed.

First, their definition says a matroid is **independence correlated** when
`Delta_I(M;y)>=0` for every distinct pair and every **positive real-valued weighting**
`y` of the ground set.

Second, the final note records Cocks's result in the fixed-graph scope:

> if Conjecture 1.1 holds for a graph `G`, then `M(G)` is independence correlated.

This is the decisive point: the unit all-forests inequality on one fixed graph upgrades
that same graphic matroid to all positive edge weights. The same paper's Proposition 3.5
proves that independence-correlated matroids are closed under deletion and contraction
(by the `epsilon -> 0+` and `epsilon -> infinity` limits of the weighted Rayleigh
difference).

Hence, if unit pNC is known on `K_n`, then `M(K_n)` is independence correlated, every
deletion restriction is independence correlated, and setting surviving weights to one
gives unit pNC for every simple graph on at most `n` vertices. Isolated vertices are
matroid-invisible and do not alter forest counts. I find no scope mismatch in this
reduction.

Source:
Charles Semple and Dominic Welsh, DOI `10.1017/S0963548307008978`,
especially the definition of independence correlation, Proposition 3.5, and the final
note citing Cocks.

## 4. Independent audit of the complete-graph Hermite proof: review PASS

Let

`R = z exp(R)`, `T=R-R^2/2`, `F=exp(T)`, and `A=T'=exp(R)`.

For `K_n`, let `Z_n` be the total forest count, `E_n` the count containing one fixed
edge, and `J_adj,n`, `J_dis,n` the counts containing a fixed adjacent or disjoint marked
edge pair.

### 4.1 Labelled decomposition

The lead's coefficient identities are correct:

`Z_n = n![z^n]F`.

Deleting one required edge splits its tree component into two rooted labelled trees,
hence

`E_n = (n-2)![z^(n-2)] F A^2`.

Deleting two adjacent required edges gives three rooted components:

`J_adj,n = (n-3)![z^(n-3)] F A^3`.

For two disjoint required edges there are exactly two cases.

* If they lie in distinct tree components, deleting them gives four rooted components:
  contribution `F A^4`.
* If they lie in the same tree, deleting them gives three components. Exactly one
  middle component contains one endpoint of each marked edge; there are four choices
  for that endpoint pair. The middle component is a tree with two prescribed labelled
  vertices, EGF `T''=A'=A^2/(1-R)`, and the two outer components contribute `A^2`.

Thus

`J_dis,n = (n-4)![z^(n-4)] F A^4 (1+4/(1-R))`.

I find no missing or double-counted case in the factor `1+4/(1-R)`.

### 4.2 Hermite coefficient identities

For

`C_m(a)=m![z^m] exp(aR-R^2/2)`

and `x=m+a`, Lagrange inversion independently gives, for `m>0`,

`C_m(a)=(m-1)![u^(m-1)](a-u)exp(xu-u^2/2)`,

which by the probabilists' Hermite generating function equals

`He_m(x)-m He_(m-1)(x)`.

The `m=0` case is immediate. A direct Cauchy change of variable
`z=u exp(-u)`, `dz=exp(-u)(1-u)du`, gives

`m![z^m] exp(aR-R^2/2)/(1-R)=He_m(m+a)`.

All four forest counts therefore use the common Hermite argument `x=n+1`.

Writing `H_j=He_j(n+1)` and `D_j=H_j-jH_(j-1)`:

`Z_n=D_n`, `E_n=D_(n-2)`, `J_adj,n=D_(n-3)`.

With `k=n-4`,

`J_dis,n = 5H_k-kH_(k-1) = J_adj,n + H_k`.

Thus the disjoint pair is indeed the harder orbit.

### 4.3 One-variable gap and root bound

Set

`s = k H_(k-1)/H_k = H_k'(n+1)/H_k(n+1)`.

The recurrence gives

`J_dis/a = 5-s`,
`E/a = 2n+6-3s`,
`Z/a = n^2+3n+10-(n+4)s`,
where `a=H_k>0`, and hence

`E^2-Z J_dis = a^2 G_n(s)`

with

`G_n(s)=(5-n)s^2+(n^2-4n-6)s-n^2+9n-14`.

The roots `lambda_i` of `He_k` are the eigenvalues of the standard symmetric Hermite
Jacobi matrix, are symmetric about zero, and satisfy
`sum lambda_i^2=k(k-1)`. Since `x=n+1=k+5` lies to the right of all roots,

`s=sum_i 1/(x-lambda_i)`.

Pairing `+/-lambda` and using
`2x/(x^2-lambda^2) >= 2/x+2lambda^2/x^3` yields

`s >= k/x + k(k-1)/x^3
   = (n-4)(n-1)(n+4)/(n+1)^3 =: L_n`.

Also `D_k=H_k(1-s)>0`, so `0<=s<1`.

For `n>=6`, `G_n'(1)=n^2-6n+4>0` and `G_n'` decreases in `s`, so `G_n`
is increasing on `[0,1]`. Exact substitution gives

`G_n(L_n)=P(n)/(n+1)^6`

where

`P(n)=2n^6+70n^5-33n^4+185n^3+1369n^2-3147n+1170`.

Putting `n=t+6` gives

`P(t+6)=2t^6+142t^5+3147t^4+33233t^3+187651t^2+551661t+666396>0`.

The small cases `K_2`--`K_5` are exact. Therefore the complete-graph argument is
internally sound.

### 4.4 Independent exact regression

I wrote an independent checker from scratch (not the lead checker). It brute-enumerates
all forests of `K_2` through `K_6`, compares the four counts to the Hermite formulas,
and exactly checks the rational `L_n`/`G_n` identities through `n=500`.

Executed source:
`lead_hermite_independent_audit.py`,
2668 bytes,
SHA-256 `4e320a504c35fa6fe09fabbdbb2376cdd597c91ab6aceaf1431b5be099eb9fc7`.

Captured output:
`lead_hermite_independent_audit.out`,
251 bytes,
SHA-256 `3cce554d398260658bd7aeb8fe6a2a64b4d13f2341490e592806f96b51620a58`.

Output ends:

`HERMITE_BOUND_AND_GAP_REGRESSION_PASS_6_TO_500`
`INDEPENDENT_AUDIT_PASS`.

The computation is regression only; the all-`n` proof is the symbolic argument above.

## 5. New source-valid log-concavity comparison for the unrooted unit law

This is a separate theorem strengthening the prior spectral comparison and directly
addresses B02's assigned polynomial/probabilistic route.

Let

`P_G(z)=sum_{F acyclic} prod_{e in F} z_e`.

For a graphic matroid these monomials are **exactly all unrooted forests**, of all sizes
and all component counts. By Anari--Liu--Oveis Gharan--Vinzant
(arXiv:1811.01600), the homogenized independent-set polynomial of any matroid is
completely log-concave. Restricting the homogenizing coordinate to `1` preserves
ordinary log-concavity, so `P_G` is log-concave on the positive orthant. Evaluating at
`z=1` is exactly the uniform unit-weight forest law.

Let `p_i=P(X_i=1)`, `v_i=p_i(1-p_i)`, and let `C=(rho_ij)` be the Pearson
correlation matrix. At `z=1`,

* for `i != j`, `(nabla^2 log P_G)_ij = Cov(X_i,X_j)`;
* multiaffinity gives `(nabla^2 log P_G)_ii=-p_i^2`.

Therefore `-nabla^2 log P_G` is PSD. Congruence by
`diag(v_i^(-1/2))` gives the exact matrix inequality

`D-C >= 0`, where `D=diag(1/(1-p_i))`.

The forest family is down-closed. Removal `F -> F\{i}` injects forests containing
edge `i` into forests excluding it, hence `p_i<=1/2`. Consequently `D<=2I`, and

`2I-C = (D-C)+(2I-D) >= 0`.

Thus the uniform unrooted forest Pearson correlation matrix satisfies the **spectral
cap**

`0 <= C <= 2I`.

The lower inequality is automatic because `C` is a correlation matrix. The upper
inequality is the nontrivial complete-log-concavity consequence. This does **not** imply
entrywise Rayleigh signs; it is a spectral statement only.

## 6. New minimal-counterexample cap

Consume the lead's earlier exact minimal-counterexample geometry. Suppose `e,f` violate
the target and put

`c=rho_ef>0`.

For every third edge `g`, the lead's total-covariance argument gives
`rho_eg rho_fg >= c`, and both factors are negative. The positive-correlation graph on
external edges is a matching. Choose an external subset `S` of size

`s >= ceil((m-2)/2)`

whose pairwise correlations are nonpositive. Write

`alpha_g=-rho_eg>0`,
`beta_g=-rho_fg>0`,
`A=sum_(g in S)(alpha_g+beta_g)`,
`tau=2 sum_{g<h in S} rho_gh <=0`.

From `alpha_g beta_g>=c`,

`A>=2s sqrt(c)`.

PSD of `C`, tested on `(t,t,1_S)`, gives

`A^2 <= 2(1+c)(s+tau)`.

PSD of the new matrix `2I-C`, tested on `(-t,-t,1_S)`, gives

`A^2 <= 2(1-c)(s-tau)`.

Hence

`4s^2 c <= 2 min{(1+c)(s+tau),(1-c)(s-tau)}`.

The maximum possible value of the minimum over `tau<=0` occurs where the two affine
terms meet, at `tau=-cs`, and equals `s(1-c^2)`. Therefore

`c^2+2sc-1 <=0`,

so every minimal-counterexample violation obeys

`rho_ef <= sqrt(s^2+1)-s = 1/(sqrt(s^2+1)+s)`.

For the inherited `m>=15` reduction, `s>=7`, giving

`rho_ef <= sqrt(50)-7 = 0.071067811865...`,

strictly stronger than the prior Gram-only `1/13 = 0.076923...`.

In forest-count notation, if
`Delta=Z_e Z_f-Z Z_ef`, then a hypothetical minimal violation satisfies

`0 < -Delta
   <= (sqrt(s^2+1)-s)
      sqrt(Z_e(Z-Z_e) Z_f(Z-Z_f))`.

This is the requested source-valid polynomial/probabilistic comparison. It narrows the
only remaining violation size without pretending log-concavity supplies the desired sign.

### Exact control showing the new matrix inequality adds information

For `s=7`, take the synthetic correlation geometry
`c=9/121`, `alpha=beta=3/11`, and zero pairwise external correlations. It satisfies
the old ordinary-PSD symmetric determinant:

`1-(2s-1)c = 4/121 >0`

and the old bound `c<1/13`, but violates the new spectral cap:

`1-(2s+1)c = -14/121 <0`.

Also `c^2+2sc-1=686/14641>0`. Thus `2I-C>=0` genuinely excludes a region that the
old Gram argument allowed.

Exact control source:
`spectral_cap_checker.py`, 1059 bytes,
SHA-256 `c3922dd899c2d89a1b74568d94256880d6c861adb7127ae8038a7b9226a6a5e4`.

Output:
`spectral_cap_checker_output.txt`, 357 bytes,
SHA-256 `35a36d9a21e0a65dd9543c67f33349c0608db7017306eda9454c300f44c5ffb3`.

## 7. Named partner result consumed and applied

I consumed assigned OTHER-account partner `fleet03/B03`,
`20260922T005605Z-b03-forest-r11b`,
handoff blob `e340981b9ba04a77a0b2e51e458542980b272ff3`.

Its exact activity identity is

`4 Delta = (B0+2q)(C0+2q)-D(A-q)`

and on disjoint pairs in `K_n` its exact ratio satisfies

`R_n=1-n^-2+O(n^-3)`.

Therefore no proof with a graph-independent fixed multiplicative slack can work. Both the
lead Hermite route and the new spectral cap pass this stress test: neither asserts a fixed
epsilon gap. The Hermite proof is sign-exact; the spectral cap shrinks as
`~1/(2s)` when the minimal-counterexample edge count grows.

## 8. Conditional end-to-end status

After the fresh lead version, the conditional argument is no longer missing a mathematical
implication in the chain that I could identify:

`K_n Hermite proof`
`-> Cocks fixed-graph unit-to-all-positive-weight upgrade`
`-> Semple--Welsh minor closure`
`-> every simple graph by deletion`.

This run supplies one independent, source-bound end-to-end review of exactly the five
items requested by the lead: Cocks scope, minor closure, the disjoint EGF factor,
the Hermite coefficient identities, and the root-bound/polynomial-positivity step.
I found no counterexample or scope failure.

Per the collective protocol, **do not promote the parent target yet**: a second independent
existing-worker end-to-end review is still required. The first essential remaining
obligation is therefore review/reproduction, not another unsupported lemma.

## 9. Inventory, provenance, and execution

Only fleet02's managed inventory was inspected. The current managed B01--B20 set was
20/20 enabled, unique/hourly-valid, role-aligned under the reallocation, with quiet
delivery preserved; no B02 scheduler mutation was made and no deficit was observed for
B20 repair.

Scoped secret/privacy review: no credentials, scheduler identifiers, machine paths,
private transcripts, benchmark gold, or unrelated private data are present in the
scientific artifacts.

Model self-report: `GPT-5.6 Sol`.  
Requested reasoning effort: `maximum actually supported`.  
Configured/known reasoning effort: `UNKNOWN_NOT_EXPOSED`.  
Provider reasoning/token usage: `null / NOT_EXPOSED`.  
Brain context: `WITHOUT_VERIFIED_BRAIN`.

Elapsed execution time is recorded separately in `finish.json`; it includes tool/network
time and is not pure thinking.
