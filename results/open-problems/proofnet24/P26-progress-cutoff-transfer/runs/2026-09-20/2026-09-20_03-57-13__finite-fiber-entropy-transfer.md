Model actually running: **GPT-5.6 Sol. Reasoning level: UNVERIFIED** — GPT-6/maximum was requested, but authenticated runtime metadata does not establish that setting, so I do not claim it.

# P26 / T08 — finite-fiber entropy/TV transfer and a new non-LRE transitive blow-up class

**Status:** `CANDIDATE_FULL` for the restricted transfer theorem and explicit class below; **PARTIAL / OPEN** for Salez Problem 2.3. Publication novelty is **UNVERIFIED** pending later independent review.

Repository/branch: `yspennstate/math-open-problems` / `master`.
Controlling policy: `operations/PROGRESS20_2026-09-20.md`.
Report root: `proofnet24/P26-progress-cutoff-transfer/runs/2026-09-20/`.

## 0. Compact handoff and coordination

The previous P26 run proved an exact line-graph incidence transfer:
for a `d`-regular base graph, the rate-one continuous-time walk on the line graph projects to the base walk at time scale `d/[2(d-1)]`, with an `O(1)` local information loss and an exact total-variation sandwich.  It then applied that transfer to edge-transitive long-range-expander bases, obtaining a 4-regular vertex-transitive spectral-expander cutoff family which is not itself long-range expanding.

Before continuing that route I read the current live companion report
`proofnet24/NM13-01/progress-cutoff/runs/2026-09-20/2026-09-20T00-00-13Z__line-graph-lre-transfer.md`.
That report independently develops the same line-graph mechanism.  Under `PROGRESS20`, historical C28 is now the live slot `NM13-01`.  Continuing line graphs in P26 would therefore duplicate the companion rather than coordinate with it.

**Complementary split adopted in this run.**

- `NM13-01` / historical C28 successor retains the direct transitivity / line-graph local-mode route.
- `P26` moves to a different exact mechanism: finite equal-fiber quotients and lexicographic local blow-ups.  The new theorem below does not use the line-graph incidence identities and applies to a different graph operation.

No historical or peer file is modified.

## 1. Exact source and current scope

Justin Salez, `arXiv:2508.21055v1` (28 August 2025), uses the rate-one continuous-time convention
\[
H_t=e^{t(P-I)}
     =e^{-t}\sum_{k\ge0}\frac{t^kP^k}{k!},
\]
i.e. independent mean-one exponential holding times.  Problem 2.3 asks literally to prove that all vertex-transitive expanders exhibit cutoff.  Here an expander sequence has diverging size, uniformly bounded degree, and spectral gap bounded away from zero.

The two most relevant newer exact-scope results checked this run are:

1. **Pedrotti--Salez, arXiv:2607.05345 (6 July 2026), _The local product condition implies cutoff_.**  Their universal theorem replaces the equilibrium Poincare constant by a non-equilibrium refinement `gamma_*` and gives a window of order `1/gamma_*` under their hypotheses.  This is a powerful cutoff criterion, but it does not presently derive the needed lower bound on `gamma_*` from vertex transitivity plus spectral expansion alone.
2. **Altschuler, arXiv:2609.14945v1 (14 September 2026), _Long-range expanders: construction and cutoff_.**  For fixed degree, long-range expansion implies cutoff with a Gaussian `Theta(sqrt(log n))` window, and Ramanujan expansion implies long-range expansion.  The paper explicitly proves the strict hierarchy
   \[
   \text{Ramanujan}\Longrightarrow\text{long-range expansion}
   \Longrightarrow\text{spectral expansion},
   \]
   with neither converse.  Thus long-range expansion is not synonymous with the source hypothesis.

The internal PROB10-08 run of 20 September further quantified Altschuler's argument for a vanishing long-range constant `c_n`, under
`c_n^{-3} log log n=o(log n)`.  That is useful neighboring progress, but it remains a metric-growth hypothesis and is not the theorem below.

The posted Abelian-Cayley/Product-Condition material concerns Salez Problem 2.4, not Problem 2.3, and is not reopened here.

A bounded dated search for `lexicographic product random walk cutoff`, `graph blow-up random walk cutoff`, and `clique extension random walk cutoff expander` did not locate the exact theorem below.  This is only negative search evidence; publication priority remains **UNVERIFIED**.

## 2. Parent problem before / after

### Before this run

The full T08 parent was OPEN.  P26 and NM13-01 already had a line-graph special-class theorem.  Altschuler covered fixed-degree long-range expanders, while the repository also had restricted product/tensor classes and a vanishing-LRE extension.

### After this run

The full T08 parent remains OPEN, but the proved source-compatible scope is enlarged by a structurally different class:

> **Every fixed finite vertex-transitive lexicographic blow-up of a continuous-time cutoff base inherits the same cutoff profile after an explicit constant time rescaling.  Applying this to explicit cubic vertex-transitive Ramanujan graphs gives a 7-regular vertex-transitive spectral-expander family that is provably not long-range expanding and has rate-one continuous-time cutoff with an `O(sqrt(log n))` window.**

For the concrete `K_2` fiber the center is
\[
\frac72\log_2 |V(G_n)|
=\frac72\log_2 |V(G_n\circ K_2)|+O(1).
\]

This is a new parent-scope class, not an audit receipt or an auxiliary constant.

## 3. Abstract finite-fiber transfer criterion

Let `G=(V,E)` be a finite connected `d`-regular graph with SRW kernel `P` and uniform law `pi_V`.  Let `F` be a fixed connected `s`-regular graph on `r>=2` vertices, with SRW kernel `W` and uniform law `u`.  Write
\[
X=G\circ F
\]
for the lexicographic product: `(x,i)` is adjacent to `(y,j)` whenever either `x~y` in `G`, or `x=y` and `i~j` in `F`.

Then `X` is
\[
D=rd+s
\]
regular.  Let `Q` be its discrete SRW kernel, and let
\[
H^G_t=e^{t(P-I)},\qquad H^X_t=e^{t(Q-I)},\qquad
H^F_t=e^{t(W-I)}
\]
be the **rate-one** continuous-time semigroups.

Define the Markov kernels

- `C : X -> V`, the projection `C((x,i),x)=1`;
- `U : V -> X`, the uniform fiber lift `U(x,(x,j))=1/r`;
- `W_hat`, the fiberwise copy of `W` on `X`;
- `T=CPU`, i.e. from `(x,i)` take one base SRW step and then choose a uniform point in the new fiber.

Set
\[
a=\frac{rd}{rd+s},\qquad b=\frac{s}{rd+s},
\qquad a+b=1.
\]

### Theorem 3.1 — exact finite-fiber entropy/TV transfer

For every `t>=0` and every start `z=(x,i)`:

1. the discrete output kernel is exactly
   \[
   \boxed{Q=aT+b\widehat W;}
   \tag{3.1}
   \]
2. the continuous-time projection is exactly
   \[
   \boxed{H^X_t C=C H^G_{at};}
   \tag{3.2}
   \]
3. more strongly, the whole law has the exact decomposition
   \[
   \boxed{
   \delta_{(x,i)}H^X_t
   =(\delta_xH^G_{at})U
    +e^{-at}\,
      \delta_x\otimes\bigl(\delta_iH^F_{bt}-u\bigr);
   }
   \tag{3.3}
   \]
4. writing
   \[
   d_G^x(t)=\|\delta_xH^G_t-\pi_V\|_{\rm TV},\qquad
   d_X^{(x,i)}(t)=\|\delta_{(x,i)}H^X_t-\pi_X\|_{\rm TV},
   \]
   one has the quantitative sandwich
   \[
   \boxed{
   d_G^x(at)\le d_X^{(x,i)}(t)
   \le d_G^x(at)+e^{-at}d_F^i(bt)
   \le d_G^x(at)+e^{-at}.
   }
   \tag{3.4}
   \]
5. for every probability law `mu` on `X`, with `nu=mu C`,
   \[
   \boxed{
   D(\mu\|\pi_X)
   =D(\nu\|\pi_V)
    +\sum_x\nu(x)
      D\!\left(\mu(\cdot\mid x)\middle\|u\right),
   }
   \tag{3.5}
   \]
   and therefore
   \[
   \boxed{
   0\le D(\mu\|\pi_X)-D(\mu C\|\pi_V)\le\log r.
   }
   \tag{3.6}
   \]

Thus a fixed fiber costs at most `log r` units of information, while along the actual walk the TV error beyond the projected base walk is exponentially small at rate `a`.

### Proof

Equation (3.1) is just edge counting.  From `(x,i)` there are `rd` cross-fiber neighbors over the `d` neighboring base vertices and `s` internal fiber neighbors.  The kernel `T` assigns probability `1/(rd)` to each cross-fiber neighbor, and `W_hat` assigns probability `1/s` to each internal neighbor, hence the weights `a=rd/D`, `b=s/D`.

The elementary fiber identities are
\[
UC=I_V,\qquad \widehat W C=C,\qquad U\widehat W=U.
\tag{3.7}
\]
Consequently
\[
T\widehat W
=CPU\widehat W=CPU=T,
\qquad
\widehat WT
=\widehat WCPU=CPU=T.
\tag{3.8}
\]
Hence `T` and `W_hat` commute.  Since `a+b=1`,
\[
Q-I=a(T-I)+b(\widehat W-I),
\]
so
\[
H^X_t
=e^{at(T-I)}e^{bt(\widehat W-I)}.
\tag{3.9}
\]

Also, for every integer `k>=1`,
\[
T^k=CP^kU
\tag{3.10}
\]
because `UC=I_V`.  Starting from `z=(x,i)` and expanding the first exponential,
\[
\begin{aligned}
\delta_z e^{at(T-I)}
&=e^{-at}\delta_z
 +e^{-at}\sum_{k\ge1}\frac{(at)^k}{k!}\delta_xP^kU\\
&=(\delta_xH^G_{at})U
  +e^{-at}(\delta_z-\delta_xU).
\end{aligned}
\tag{3.11}
\]
Applying the commuting fiber semigroup gives (3.3), since uniform `u` is stationary for `W`.

Projection by `C` kills the signed fiber correction in (3.3), proving (3.2).  Total variation contracts under `C`, yielding the lower bound in (3.4).  Uniform lifting preserves TV exactly, and the correction has TV norm
\[
e^{-at}\|\delta_iH^F_{bt}-u\|_{\rm TV},
\]
which proves the upper bound.

Finally `pi_X=pi_V\otimes u`, because `X` is regular.  Relative entropy on a product partition obeys the ordinary chain rule, giving (3.5); a law on an `r`-point fiber has relative entropy at most `log r`, giving (3.6).  This proves the theorem.  ∎

## 4. Quantitative cutoff-window consequence

Let
\[
d_G(t)=\max_xd_G^x(t),\qquad d_X(t)=\max_{x,i}d_X^{(x,i)}(t).
\]
Taking maxima in (3.4) gives the particularly simple transfer criterion
\[
\boxed{
d_G(at)\le d_X(t)\le d_G(at)+e^{-at}.
}
\tag{4.1}
\]

Hence, for every `epsilon in (0,1)`,
\[
\boxed{
\frac1a\,t^G_{\rm mix}(\epsilon)
\le t^X_{\rm mix}(\epsilon)
\le
\frac1a\max\left\{
t^G_{\rm mix}(\epsilon/2),\log(2/\epsilon)
\right\}.
}
\tag{4.2}
\]

Indeed the lower bound is (4.1), while for the upper bound choose
\[
s=\max\{t^G_{\rm mix}(\epsilon/2),\log(2/\epsilon)\}
\]
and `t=s/a`.

### Corollary 4.1 — cutoff and profile preservation

Suppose a graph sequence `G_n` has rate-one continuous-time cutoff at centers `T_n -> infinity` with window `w_n=o(T_n)`, in the quantitative sense
\[
t^G_{\rm mix}(\epsilon)=T_n+O_\epsilon(w_n)
\qquad(\epsilon\in(0,1)\text{ fixed}).
\]
For any fixed fiber `F`,
\[
X_n=G_n\circ F
\]
has cutoff at
\[
\boxed{T_n/a}
\]
with window
\[
\boxed{O(w_n)}
\]
(the implicit factor is the fixed constant `1/a`).

If in addition
\[
d_G(T_n+zw_n)\longrightarrow \Psi(z)
\]
for every fixed `z`, then
\[
d_X\!\left(\frac{T_n+zw_n}{a}\right)
\longrightarrow\Psi(z).
\tag{4.3}
\]
The output has exactly the same limiting profile after the deterministic time rescaling.  This follows immediately from (4.1), because the error is
`exp[-T_n-zw_n] -> 0`.

This is stronger than an entropy-only transfer: the chain-rule information loss is `O(1)`, and the actual unresolved local fiber mode is killed with exponentially small weight before the `Theta(log n)` expander mixing time.

## 5. Spectral expansion and transitivity of the output

Assume now that both `G` and `F` are vertex-transitive.  The wreath-product action—an automorphism of `G` on the base coordinate together with independent automorphisms of the copies of `F`—acts transitively on `V(G)\times V(F)`.  Therefore `G\circ F` is vertex-transitive.

The spectrum also splits exactly.

- On functions constant on each fiber, `Q` acts as
  \[
  aP+bI,
  \]
  so a base eigenvalue `lambda` becomes `b+a lambda`.
- On functions with zero mean in every fiber, `T` vanishes and `Q=b W_hat`; thus a fiber eigenvalue `eta` becomes `b eta`.

If the base one-sided normalized spectral gap is
\[
1-\lambda_2(P)\ge\gamma>0,
\]
then
\[
1-\lambda_2(Q)
\ge \min\{a\gamma,1-b\}
=a\min\{\gamma,1\}.
\tag{5.1}
\]
Thus any fixed-fiber lexicographic blow-up of a vertex-transitive spectral-expander sequence is again a bounded-degree vertex-transitive spectral-expander sequence.

## 6. The output is never a uniform long-range expander

This is the point that makes the application genuinely relevant to the gap between spectral and long-range expansion.

Let `N=r|V(G)|` and `D=rd+s`.  A path of length `R` in `G\circ F` projects to a base path of length at most `R`; internal fiber moves do not change the base coordinate.  Therefore
\[
|B_{G\circ F}((x,i),R)|
\le r\,|B_G(x,R)|
\le C_{d,r}(d-1)^R.
\tag{6.1}
\]

The output is `D`-regular, so Altschuler's LRE branching base would be `D-1`.  Since `r>=2`,
\[
D-1=rd+s-1>d-1.
\tag{6.2}
\]
Choose
\[
R_N=\left\lfloor\frac12\log_{D-1}N\right\rfloor.
\]
Then `(D-1)^{R_N}=o(N)`, while
\[
\frac{|B_{G\circ F}((x,i),R_N)|}{(D-1)^{R_N}}
\le
C_{d,r}\left(\frac{d-1}{D-1}\right)^{R_N}
\longrightarrow0.
\tag{6.3}
\]
For any fixed LRE constant `c>0`, the singleton condition would require
\[
|B((x,i),R_N)|\ge c(D-1)^{R_N}
\]
for all sufficiently large `N`, because the `3N/4` branch is not yet active.  Equation (6.3) contradicts this.

Hence
\[
\boxed{
(G_n\circ F)\text{ is not a uniform long-range-expander sequence}
}
\tag{6.4}
\]
for every growing fixed-degree base sequence.

So the theorem does not merely re-apply Altschuler's long-range theorem to the output.

## 7. Concrete new transitive class: a 7-regular clique blow-up

Kaufman--Lubotzky, `arXiv:1108.2960`, Theorem 3, construct explicit `(q+1)`-regular edge-transitive Ramanujan Cayley graphs
\[
G_\alpha=\operatorname{Cay}(PSL_2(q^\alpha),S)
\quad\text{or}\quad
\operatorname{Cay}(PGL_2(q^\alpha),S)
\]
for fixed prime power `q` and growing `alpha` with `q^\alpha>17`.  Their construction is Cayley, hence vertex-transitive, and is explicitly edge-transitive.

Take `q=2`.  Then `G_\alpha` is cubic and Ramanujan.  Altschuler's Theorem 1.7 gives long-range expansion for the base.  His lazy-walk Corollary 1.13, together with Salez's exact continuous-time identity
\[
e^{t(P-I)}
=e^{2t((I+P)/2-I)},
\]
and Poisson concentration, gives the corresponding **rate-one continuous-time** cutoff at
\[
T_\alpha^{\rm base}
=3\log_2 |V(G_\alpha)|
\tag{7.1}
\]
with `O(sqrt(log |V(G_alpha)|))` window.  For completeness, the lower half in continuous time follows directly from the covering-tree radial walk: its speed is `(3-2)/3=1/3`, its fluctuations on the `Theta(log n)` scale are `O(sqrt(log n))`, and a ball of radius
`\log_2 n-C\sqrt{\log n}` has stationary mass `o(1)`.  The upper half follows by writing the rate-one walk as a rate-two Poissonization of the lazy kernel and using Altschuler's lazy cutoff plus Poisson concentration.  This is precisely Salez's continuous-time convention; no discrete/lazy center is silently reused.

Now fix `F=K_2` and define
\[
X_\alpha=G_\alpha\circ K_2.
\]
Here
\[
r=2,\quad s=1,\quad D=2\cdot3+1=7,
\qquad a=\frac67,\quad b=\frac17.
\]

By Sections 4--6:

1. `X_alpha` is **7-regular** and **vertex-transitive**;
2. it is a **spectral expander**, with one-sided gap at least `6/7` times the base gap;
3. it is **not** a uniform long-range-expander sequence: its balls grow at most on the base `2^R` scale, whereas degree seven LRE demands the `6^R` scale;
4. its exact rate-one continuous-time walk has cutoff at
   \[
   \boxed{
   T_\alpha
   =\frac{7}{6}T_\alpha^{\rm base}
   =\frac72\log_2|V(G_\alpha)|
   =\frac72\log_2|V(X_\alpha)|+O(1),
   }
   \tag{7.2}
   \]
   with window
   \[
   \boxed{O(\sqrt{\log|V(X_\alpha)|}).}
   \tag{7.3}
   \]
5. the Gaussian base profile is preserved under the `7/6` time rescaling by (4.3).

This class is structurally different from both the previous line-graph family and the historical Cartesian/synchronous product classes:
\[
A_{G\circ K_2}=A_G\otimes J_2+I\otimes A_{K_2},
\]
so every base edge becomes a complete bipartite `K_{2,2}` between fibers, rather than a matching or a Cartesian edge.

## 8. Exact sanity check actually executed

After deriving the symbolic proof, I ran an exact rational-arithmetic checker on three finite pairs:
`K_4 o K_2`, `K_5 o K_3`, and `K_4 o C_4`.

It checks:

- `Q=aT+b W_hat` against the directly constructed lexicographic-product SRW kernel;
- `UC=I`;
- `W_hat C=C` and `U W_hat=U`;
- `T W_hat=W_hat T=T`;
- the exact generator projection `(Q-I)C=a C(P-I)`;
- the strict branching-base inequality `D-1>d-1`.

Artifact:
`proofnet24/P26-progress-cutoff-transfer/artifacts/2026-09-20/2026-09-20_03-57-13__finite_fiber_transfer_exact.py`

Creation commit:
`5a6946483a4b42e09ab8a3e673907a95ed734949`.

Archived executed output:
`proofnet24/P26-progress-cutoff-transfer/artifacts/2026-09-20/2026-09-20_03-57-13__finite_fiber_transfer_exact.out`

Creation commit:
`9f6e3d486c6c22ce4c74da6281d19173040b41cf`.

Terminal marker:
`P26_T08_FINITE_FIBER_TRANSFER_EXACT_PASS`.

The checker is only a sanity check of the algebra; the theorem is symbolic and does not depend on finite enumeration.

## 9. What failed / what changed / residual obstruction

### Route deliberately abandoned this run

A second pass on line graphs was rejected after reading the live `NM13-01` report, because the companion had independently developed the same incidence factorization.  Continuing it would be duplicated effort.  This is a coordination correction, not a mathematical failure.

### New successful route

The finite-fiber quotient viewpoint isolates the slow mode exactly.  Every trajectory which has made at least one cross-fiber/base refresh is uniform in its current fiber; the only fiber-memory term has total mass `e^{-at}`.  This produces the exact sandwich (4.1), rather than an entropy-only inequality with a secondary relaxation loss.

### Residual parent obstruction

This still does **not** prove cutoff for an arbitrary vertex-transitive spectral expander.  The theorem closes a broad class under a fixed local transitive decoration, but it starts from a base family whose cutoff is already known.

The source-level missing implication remains genuinely global:

> derive a mixing-window entropy, Green-function, non-equilibrium Poincare, or equivalent information-concentration estimate from **vertex transitivity plus a fixed spectral gap alone**, without assuming long-range tree-rate growth.

Altschuler's theorem supplies this via LRE; Pedrotti--Salez would supply it from a sufficiently strong `gamma_*`; neither quantity is presently known to follow from source-level transitivity and spectral expansion.

## 10. Next P26 attack

Move from exact commuting lexicographic fibers to **finite transitive graph bundles / replacement products with a nontrivial connection action**.  The target is an approximate quotient theorem of the following form.

Let `C,U` define an equal-size transitive quotient, and suppose
\[
(Q-I)C=a\,C(P-I)+E C
\]
with a controlled commutator/error `E`, while fiber-mean-zero modes have a uniform spectral gap.  Prove a Duhamel/Green-function estimate
\[
\|H^X_tC-CH^G_{at}\|_{\rm TV}
\le \int_0^t \|E\,H^G_{as}\|_{\mathrm{appropriate}}\,ds
\]
strong enough to preserve an `O(sqrt(log n))` cutoff window when the integrated error is `o(1)` across that window.  Then instantiate it on a genuinely twisted transitive bundle, not an exact lexicographic product.

The live companion `NM13-01` remains complementary: it should continue the direct arbitrary-transitive entropy/Green-function route rather than this local quotient-perturbation closure.

## 11. ledger_delta

```yaml
ledger_delta:
  worker: P26
  parent: T08 / Salez arXiv:2508.21055 Problem 2.3
  parent_status_before: "OPEN; prior P26/NM13-01 line-graph non-LRE subclass available"
  parent_status_after: "OPEN / STRICTLY LARGER PROVED SUBCLASS"
  source_level_advance:
    theorem: "fixed finite vertex-transitive lexicographic blow-ups preserve rate-one continuous-time cutoff under explicit time rescaling"
    explicit_class: "X_alpha = G_alpha o K2 for Kaufman-Lubotzky cubic edge-transitive Ramanujan Cayley graphs"
    output_degree: 7
    output_transitive: true
    output_spectral_expander: true
    output_long_range_expander: false
    cutoff_center: "(7/2) log_2 |V(G_alpha)| = (7/2) log_2 |V(X_alpha)| + O(1)"
    window: "O(sqrt(log |V(X_alpha)|))"
  mechanism_level_advance:
    entropy_transfer: "D(mu||pi_X)=D(mu C||pi_V)+E D(mu(.|x)||u), local loss <= log r"
    exact_projection: "H_X(t) C = C H_G(a t), a=rd/(rd+s)"
    exact_law_decomposition: "base lift plus e^{-a t} fiber-memory term"
    tv_transfer: "d_G(a t) <= d_X(t) <= d_G(a t)+e^{-a t}"
    mixing_time_transfer: "a^{-1} t_G(eps) <= t_X(eps) <= a^{-1} max{t_G(eps/2), log(2/eps)}"
    profile_transfer: "same profile after time scaling 1/a"
  coordination:
    historical_C28_live_successor: NM13-01
    correction: "line-graph route already duplicated; P26 moved to finite-fiber quotient/blow-up route"
  theorem_label: "CANDIDATE_FULL_RESTRICTED / PENDING_LATER_INDEPENDENT_REVIEW"
  publication_novelty: UNVERIFIED
  full_parent_closed: false
  residual_obstruction: "transitivity + spectral gap alone still lacks a universal entropy/Green/gamma_* front"
  next_attack: "approximate quotient/Green transfer for twisted transitive graph bundles"
```

End of substantive P26 T08 report.
