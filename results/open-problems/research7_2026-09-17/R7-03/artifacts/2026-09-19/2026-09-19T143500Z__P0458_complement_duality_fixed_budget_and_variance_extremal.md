Model actually run: **GPT-5.6 Sol. Reasoning level: UNVERIFIED — this was not GPT-6 at maximum, and I do not claim otherwise.** No authenticated runtime model/effort telemetry or binding selector was exposed.

# P0458 — proposal-complement duality, fixed-budget corrections, and a local-variance extremal obstruction

Worker: `R7-03`  
Native ID: `6aabe7be74008191b526b109ee4e9e80`  
Target: `P0458`  
Classification: `CLOSABLE OUTSIDE`  
Captured master at run start: `ffbe81ec2c1f686ec6a9a4a4016fe85ded799d83`  
Fresh master immediately before this artifact write: `e6055b2ab8e05db65cf622a733876085d32808fc`  
Previous own report: `research7_2026-09-17/R7-03/runs/2026-09-19/2026-09-19T133500Z__report.md` @ `b199365bd00233ef7daa1f3232931fa28a112e88`.

Outside source: Hossein Dabirian and Vijay Subramanian, *Connectivity of a family of bilateral preference random graphs*, Journal of Applied Probability 63(2) (2026), 552–579, DOI `10.1017/jpr.2025.10051`, §1.1 first additional question: characterize the limiting distribution of the standardized vertex degree in `LK(n,k)`. The final Cambridge record was rechecked on 2026-09-19. This artifact strengthens the already complete source-scope candidate; it does not change the frozen source metric.

Frozen metric: `R_unresolved = 0 -> 0` (**NO MOVEMENT**).  
Current Section-B methods: **B7 TAKE A LIMIT; B12 CONSERVED QUANTITY; B24 FIND THE EXTREMAL OBJECT**.  
Previous triple: B3/B15/B27.

## 1. Model and notation

Put independent continuous weights `U_e ~ Unif(0,1)` on the edges of `K_n`. At each vertex `v`, let `P_k^U(v)` be the set of its `k` incident edges of smallest weight. An edge `{u,v}` belongs to `LK(n,k;U)` exactly when it lies in both `P_k^U(u)` and `P_k^U(v)`.

Write

- `N=n-1` for the number of incident edges at a vertex;
- `r=N-k`;
- `D_v^{(k)}(U)` for the degree of vertex `v` in `LK(n,k;U)`;
- `H_v^{(k)}=k-D_v^{(k)}` for its outgoing-unilateral proposal count (degree deficit);
- `M_k(U)` for the total number of mutual edges in `LK(n,k;U)`;
- `A_k(U)` for the total number of unordered edges proposed by exactly one endpoint.

The previously established exact mean deficit is

\[
\delta_{n,k}:=\mathbb E H_v^{(k)}
=\frac{2B(N,N)}{B(k,k)B(r,r)}
=\frac{kr}{N}\frac{\binom{2k}{k}\binom{2r}{r}}{\binom{2N}{N}}.
\tag{1}
\]

In particular `delta_{n,k}=delta_{n,r}`.

## 2. B12 — exact proposal-complement conservation law

Define transformed weights

\[
U'_e=1-U_e.
\]

Because all incident weights are distinct almost surely, the `r=N-k` smallest `U'`-weights at a vertex are exactly the complement, among its `N` incident edges, of the `k` smallest `U`-weights. Thus for every vertex `v` and every incident edge `e`,

\[
1_{\{e\in P_r^{U'}(v)\}}=1-1_{\{e\in P_k^U(v)\}}.
\tag{2}
\]

### Theorem 2.1 (pathwise complement duality)

For every realization with distinct edge weights,

\[
\boxed{A_k(U)=A_r(1-U)}.
\tag{3}
\]

Moreover

\[
\boxed{M_k(U)-M_r(1-U)=\frac{n(k-r)}2}.
\tag{4}
\]

Consequently the centered total edge counts are exactly equal under this coupling:

\[
\boxed{M_k(U)-\mathbb E M_k
=M_r(1-U)-\mathbb E M_r}.
\tag{5}
\]

If `\bar D_k=2M_k/n` is the random sample-average degree, then

\[
\boxed{\bar D_k(U)-\bar D_r(1-U)=k-r}
\tag{6}
\]

and therefore

\[
\boxed{\bar D_k-\mathbb E\bar D_k\ \stackrel{d}=\ \bar D_r-\mathbb E\bar D_r,\qquad
\operatorname{Var}(\bar D_k)=\operatorname{Var}(\bar D_r).}
\tag{7}
\]

### Proof

For an unordered edge `e={u,v}`, encode its two proposal indicators under budget `k` by `(a_u,a_v) in {0,1}^2`. Equation (2) sends this pair under the transformed `r`-budget model to `(1-a_u,1-a_v)`. Hence a unilateral edge, whose status is `(1,0)` or `(0,1)`, remains unilateral and its orientation is reversed. This proves (3).

Each vertex makes exactly `k` directed proposals, so counting proposals by unordered edge gives the pathwise identity

\[
nk=2M_k(U)+A_k(U).
\tag{8}
\]

For the transformed `r`-budget model,

\[
nr=2M_r(1-U)+A_r(1-U).
\tag{9}
\]

Subtract (9) from (8) and use (3). This gives (4). Taking expectations and subtracting gives (5); multiplying by `2/n` gives (6)–(7). ∎

### Local orientation refinement

Let `O_v^{(k)}` be the number of unilateral edges directed outward from `v`, and `I_v^{(k)}` the number directed into `v`. Then

\[
O_v^{(k)}=H_v^{(k)},
\tag{10}
\]

and complement duality reverses every unilateral orientation, giving pathwise

\[
\boxed{O_v^{(r)}(1-U)=I_v^{(k)}(U).}
\tag{11}
\]

Since `sum_v O_v^{(k)}=sum_v I_v^{(k)}=A_k` pathwise and vertices are exchangeable,

\[
\mathbb EO_v^{(k)}=\mathbb EI_v^{(k)}.
\tag{12}
\]

Thus (11) supplies a structural proof of the exact deficit symmetry in (1):

\[
\mathbb EH_v^{(r)}=\mathbb EH_v^{(k)}.
\tag{13}
\]

However local variances need not be complement-symmetric. Indeed

\[
\operatorname{Var}(D_v^{(k)})-\operatorname{Var}(D_v^{(r)})
=\operatorname{Var}(O_v^{(k)})-\operatorname{Var}(I_v^{(k)})
=\operatorname{Cov}(O_v^{(k)}+I_v^{(k)},O_v^{(k)}-I_v^{(k)}).
\tag{14}
\]

This identity anticipates the B24 obstruction below: global edge-count fluctuations are exactly complement-dual while root-degree fluctuations can be asymmetric.

## 3. B7 — fixed-budget finite-size expansion at both sparse and dense boundaries

Fix an integer `q>=1` and let `N=n-1 -> infinity`. From (1), for `k=q` and `r=N-q`,

\[
\delta_{n,q}
=\frac{q(N-q)}N
\frac{\binom{2q}{q}\binom{2(N-q)}{N-q}}{\binom{2N}{N}}.
\tag{15}
\]

Define

\[
\mu_q:=q\frac{\binom{2q}{q}}{4^q}
=\frac{\Gamma(q+1/2)}{\sqrt\pi\,\Gamma(q)}.
\tag{16}
\]

This is exactly the fixed-complement limiting mean from the earlier mixed-Poisson theorem.

### Theorem 3.1 (two finite-size correction terms)

For each fixed `q>=1`,

\[
\boxed{
\delta_{n,q}
=\mu_q\left[
1-\frac{q}{2N}-\frac{q(q+1)}{8N^2}+O_q(N^{-3})
\right].
}
\tag{17}
\]

By exact complement symmetry, the identical expansion holds at the dense boundary `k=N-q`:

\[
\boxed{
\delta_{n,N-q}
=\mu_q\left[
1-\frac{q}{2N}-\frac{q(q+1)}{8N^2}+O_q(N^{-3})
\right].
}
\tag{18}
\]

### Proof

Divide (15) by (16). Then

\[
\frac{\delta_{n,q}}{\mu_q}
=\left(1-\frac qN\right)R_{N,q},
\qquad
R_{N,q}:=4^q\frac{\binom{2(N-q)}{N-q}}{\binom{2N}{N}}.
\tag{19}
\]

The factorial ratio has the exact product form

\[
R_{N,q}
=\frac{\prod_{j=0}^{q-1}(1-j/N)^2}
{\prod_{j=0}^{2q-1}(1-j/(2N))}.
\tag{20}
\]

Because `q` is fixed, Taylor expansion of `log(1-x)` is uniform over these finitely many factors. Writing

\[
S_1(m)=\sum_{j=0}^{m-1}j=\frac{m(m-1)}2,
\qquad
S_2(m)=\sum_{j=0}^{m-1}j^2=\frac{m(m-1)(2m-1)}6,
\]

we obtain

\[
\log R_{N,q}
=2\sum_{j=0}^{q-1}\log(1-j/N)
-\sum_{j=0}^{2q-1}\log(1-j/(2N))
\]

\[
=\frac{q}{2N}+\frac{q(2q-1)}{8N^2}+O_q(N^{-3}).
\tag{21}
\]

Exponentiating,

\[
R_{N,q}
=1+\frac{q}{2N}+\frac{q(3q-1)}{8N^2}+O_q(N^{-3}).
\tag{22}
\]

Multiplying by `(1-q/N)` gives (17). Equation (18) follows from `delta_{n,k}=delta_{n,N-k}`. ∎

For `q=1`, `mu_1=1/2`; after converting `N=n-1`, (17) reproduces the earlier exact `r=1` expansion

\[
\delta_{n,n-2}=\frac12-\frac1{4n}-\frac3{8n^2}+O(n^{-3}).
\]

### Global unilateral-edge scaling in proportional density

Because each unilateral edge contributes one outgoing deficit,

\[
A_k=\sum_v H_v^{(k)},
\qquad
\mathbb EA_k=n\delta_{n,k}.
\tag{23}
\]

If `k/N -> p in (0,1)`, the exact beta/central-binomial formula gives

\[
\delta_{n,k}\sim \sqrt{\frac{p(1-p)N}{\pi}},
\]

hence

\[
\boxed{
\frac{\mathbb EA_k}{n^{3/2}}
\longrightarrow
\sqrt{\frac{p(1-p)}{\pi}}.
}
\tag{24}
\]

The coefficient is maximized at `p=1/2`. Thus balanced proposal budget maximizes the leading expected *global asymmetry* even though, as B24 shows, it need not maximize a single vertex's degree variance.

## 4. B24 — the balanced-budget root-variance extremal principle is false

The preceding symmetry suggests a tempting conjecture: perhaps, for fixed `n`, `Var(D_v^{(k)})` is maximized at the balanced budget `k=r`. This is false already at `n=7`.

The exact finite-variance formula established in the preceding R7-03 run is evaluated with exact rational arithmetic (no floating point, no Monte Carlo) in the accompanying certificate. It gives

\[
\operatorname{Var}(D_v^{(3)})
=\frac{243059}{385385}
\approx0.6306913865,
\tag{25}
\]

where `k=3,r=3` is balanced, but

\[
\operatorname{Var}(D_v^{(4)})
=\frac{63920}{99099}
\approx0.6450115541.
\tag{26}
\]

Their exact difference is

\[
\boxed{
\operatorname{Var}(D_v^{(4)})-
\operatorname{Var}(D_v^{(3)})
=\frac{49669}{3468465}>0.
}
\tag{27}
\]

In fact the exact variances for `n=7`, `k=1,...,6` are

\[
\frac{30}{121},\quad
\frac{241676}{495495},\quad
\frac{243059}{385385},\quad
\frac{63920}{99099},\quad
\frac{178}{363},\quad
0,
\]

so the unique maximizer is `k=4`, not the balanced value `k=3`.

This is not a contradiction with complement duality. Equations (3)–(7) concern total unilateral/mutual counts and average degree. Locally, complement swaps *outgoing* and *incoming* unilateral counts, and (14) measures precisely why root-degree variances can differ. The finite counterexample therefore identifies the gluing failure between a correct global complement symmetry and an incorrect local-variance symmetry heuristic.

## 5. Consequences for the completed P0458 picture

These results do not create a new source regime: the standardized-degree question was already internally solved for all asymptotic regimes covered by the source quantifiers. They do sharpen the structural picture in three ways.

1. **Exact global duality.** The entire centered random average-degree law is invariant under `k <-> n-1-k`, not merely its expectation.
2. **Boundary matching with rates.** The sparse fixed-budget and dense fixed-complement mean deficits approach the same `mu_q` with two explicit correction terms.
3. **Local/global distinction.** Complement symmetry does not imply local degree-variance symmetry; an exact `n=7` certificate exhibits the first simple obstruction.

Frozen source metric therefore stays

```text
R_unresolved before: 0
R_unresolved after:  0
movement: NO_MOVEMENT
ordinary unchanged count: 5 -> 6
```

The mathematical source status remains **PROVED internally at source scope**. Protocol closure remains unavailable without an actual P0458-specific P26 full-proof PASS and one distinct OTHER-track full-proof PASS. The finite certificate attached to this artifact is a self-check, not an independent audit.

## 6. Literature/status boundary

The final Cambridge article was rechecked on 2026-09-19: online publication 18 December 2025; Journal of Applied Probability 63(2), June 2026, pp. 552–579. Bounded searches on 2026-09-19 for the exact title, `LK(n,k)` degree distribution/variance, the authors' later bilateral-preference work, and the citation neighborhood did not recover a later source-matching solution. That is negative evidence only and is **not** a novelty or worldwide-openness certificate.

The adjacent P0459 concentration target has a separate canonical owner. Its latest path-scoped work was read only as neighboring context; no P0459 theorem is used here, so there is no circular dependency.
