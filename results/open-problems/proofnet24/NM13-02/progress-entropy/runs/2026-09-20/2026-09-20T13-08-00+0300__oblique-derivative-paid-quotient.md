Model actually run: GPT-5.6 Sol. Reasoning level: UNVERIFIED — not authenticated as GPT-6 at maximum.

# NM13-02 T01 — oblique-derivative paid quotient peeling and a rigid near-isospectral obstruction

## 0. Parent scope/bound versus mechanism gain

**Parent problem.** Friedgut--Kalai Fourier entropy--influence (FEI): prove a finite universal constant `C` such that
\[
H(\widehat f^{\,2})\le C I(f)
\]
for every Boolean function on every finite uniform cube.

**Parent status before -> after:** **OPEN -> OPEN.**

**Universal finite upper bound before -> after:** **UNKNOWN -> UNKNOWN.**

No finite-dimensional computation, fresh-control theorem, or restricted stopping class below is promoted to full FEI.

**Mechanism gain in this run.** P03's newest report isolates exact/approximate child-spectrum matching through a Hellinger defect `M_i`, proves exact isospectral branching costs zero, and asks for a hereditary approximate-isospectral payment rather than another minor-child/curvature scalar. This run proves a physical realization of that payment using **oblique multiplicative derivatives**:

1. for every translation vector `v` crossing a queried physical coordinate `i`, the child Hellinger defect is bounded by the folded density of the oblique derivative `D_v f`;
2. the hereditary allocation is paid by the **transverse total influence** of one child of `D_v f`;
3. the entire one-step entropy decrement is paid by at most twice that transverse derivative influence;
4. a row-echelon family of approximate signed translations can therefore be quotient-peeled with total hereditary surcharge bounded by the sum of their oblique derivative influences;
5. this is applied to a **signed-translation-rigid tri-defect family** on which P03's previous minor-child and coordinate-curvature surcharges still diverge linearly in dimension, while one oblique approximate-symmetry peel costs less than `2/3` of the root total influence asymptotically and leaves only already-certified one-/two-defect branches.

This directly advances P03's exact unresolved approximate-isospectral obstruction without taking ownership of P03's exact Hellinger formulas or peer claims.

## 1. Dependencies and preserved handoff

The controlling policy is `operations/PROGRESS20_2026-09-20.md`, blob `4a207f06e5c8294c83bcabcd9a1477f26f54b441`. LIVE20 assigns NM13-02 to T01 hereditary entropy/recombination theory paired with P03.

Newest P03 substantive dependency:

`proofnet24/P03-fei/runs/2026-09-20/2026-09-20T12-28-55+0300__fei-isospectral-splicing-symmetry-quotient.md`, blob `3421c0cbfd22031554befb962ec92cd0c8bb45b9`.

It proves, for the two physical children `g,h` of a split, with squared Fourier laws `P,Q`, Hellinger affinity `A=sum sqrt(PQ)`, and defect `M=(1-A)/2`, the exact child-spectrum representation of the hereditary allocation, `M<=j_i`, a KL-rebate upper bound, `JS(P,Q)<=2M/ln2`, and exact zero allocation/decrement when `P=Q`. It also proves exact signed-translation quotient peeling and exhibits the antipodal two-defect family where both the minor-child and coordinate-derivative-curvature surcharges are `(n-1) Inf_i` although the true local allocation is zero. Its stated live target is an approximate-isospectral hereditary theorem.

Compact NM13-02 handoff retained unchanged:

- quadratic phases admit the exact rank telescope and hereditary constant `1`;
- queried influence plus weighted residual leaf influence is an exact budget, enabling branch-dependent max-splicing;
- one-point perturbations of arbitrary quadratic phases have hereditary constant
  \[
  C_\chi=2+\frac1{\sqrt e\ln2}=2.875038774914527\ldots;
  \]
- quadratic-normalized Wiener, two-flat, variance-separator, and derivative-spectral-flat results remain restricted to their proved classes;
- the newest guarded derivative-spectral-flat theorem is complementary: it handles derivatives whose spectra are flat, whereas the present theorem is strongest when an **oblique derivative is nearly constant**, i.e. the opposite spectral regime;
- the false pointwise-erasure shortcut, fixed-coefficient drift, Han absolute-overlap selector, derivative-degree scalar schedule, blind root-curvature selector, and fixed-`s<2` Renyi route remain retired.

The restricted fresh-control theorem remains restricted because it appends controls and does not prove fixed-domain/full FEI.

### Primary-source status checked 20 September 2026

A fresh bounded source check recovered:

- González--MacManus--Pereyra, arXiv:2606.00246, submitted 29 May 2026, still explicitly states universal FEI as a conjecture and says the key restriction inequality would imply full FEI if universal; the paper proves stopping-tree/restricted-class results, not a universal constant.
- Li--Han, arXiv:2512.03117, submitted 2 December 2025, improves Han's general inequality but still retains the coordinate-profile term `sum_i I_i log(1/I_i)` rather than `H<=C I`.

No source-matching universal FEI resolution was recovered. This is a bounded status check, not a novelty certificate.

## 2. Setup: oblique derivative across a physical pivot

Work on `F_2^n`. For `v in F_2^n`, define the multiplicative directional derivative
\[
D_v f(x):=f(x)f(x+v).
\]
Fix a coordinate `i` with `v_i=1`. Write `x=(b,y)` with `b=x_i` and let `w` be `v` with the `i`-th bit deleted. Let
\[
g(y)=f(0,y),\qquad h(y)=f(1,y),\qquad \widetilde h(y)=h(y+w).
\]
Then
\[
d(y):=g(y)\widetilde h(y)=D_vf(0,y).
\tag{2.1}
\]
The other `i`-child of `D_vf` is the translate `d(y+w)`, since `D_vf(x+v)=D_vf(x)`.

Let
\[
\delta:=\min_{\sigma\in\{\pm1\}}
\Pr_y[g(y)\ne \sigma\widetilde h(y)]
=\min\{\Pr[d=-1],\Pr[d=1]\}\le\frac12.
\tag{2.2}
\]
Multiplying a child by a global sign and translating its input changes Fourier signs only, not coefficient magnitudes or its squared Fourier law.

## 3. Hellinger defect is controlled by oblique physical mismatch

Let `a_T=hat g(T)` and `b_T=hat h(T)`. P03's child-spectrum defect is
\[
M_i=\frac14\sum_T (|a_T|-|b_T|)^2.
\tag{3.1}
\]

### Lemma 3.1
For every `v_i=1`,
\[
\boxed{M_i\le\delta.}
\tag{3.2}
\]

### Proof
Choose `sigma` attaining (2.2). The Fourier coefficients of `sigma*widetilde h` are
\[
\sigma(-1)^{w\cdot T}b_T,
\]
so their absolute values equal `|b_T|`. Therefore
\[
\sum_T(|a_T|-|b_T|)^2
\le
\sum_T\left(a_T-\sigma(-1)^{w\cdot T}b_T\right)^2.
\]
By Parseval, the right side is
\[
\mathbb E_y(g(y)-\sigma\widetilde h(y))^2=4\delta.
\]
Divide by four. QED.

Thus P03's approximate isospectrality parameter has an immediate physical upper bound whenever the two branches become close after an **oblique residual translation**, even if they are not close without that alignment.

## 4. Two entropy lemmas

### Lemma 4.1 — hereditary allocation is at most `h_2(M)`
P03's exact fiber formula has weights `q_T=(a_T^2+b_T^2)/2`, minority masses `m_T`, and
\[
B_i(f)=\sum_T q_T h_2(m_T/q_T),\qquad \sum_Tm_T=M_i.
\]
Concavity of binary entropy gives
\[
\boxed{B_i(f)\le h_2(M_i).}
\tag{4.1}
\]

### Lemma 4.2 — Jensen--Shannon is at most `h_2(M)`
For arbitrary probability laws `P,Q`, set
\[
M=\frac12\left(1-\sum_T\sqrt{P_TQ_T}\right).
\]
Then
\[
\boxed{\operatorname{JS}(P,Q)\le h_2(M).}
\tag{4.2}
\]

### Proof
For each `T` with `P_T+Q_T>0`, write
\[
s_T=\frac{P_T+Q_T}{2},\qquad
P_T=s_T(1+t_T),\quad Q_T=s_T(1-t_T),\quad 0\le t_T\le1,
\]
after swapping the labels if needed. Then `sum s_T=1` and the local Jensen--Shannon contribution in bits is
\[
s_T\left[1-h_2\!\left(\frac{1+t_T}{2}\right)\right].
\tag{4.3}
\]
Put
\[
u_T=\frac{1-\sqrt{1-t_T^2}}2.
\]
Then the local contribution to `M` is `s_T u_T`.

We use the elementary inequality
\[
h_2(x)\ge4x(1-x),\qquad 0\le x\le1.
\tag{4.4}
\]
For completeness: by symmetry reduce to `[0,1/2]`; for `F(x)=h_2(x)-4x(1-x)`,
\[
F'(x)=\log_2\frac{1-x}{x}-4+8x,
\qquad
F''(x)=8-\frac1{\ln2\,x(1-x)}.
\]
Since `x(1-x)` is increasing on `[0,1/2]`, `F''` changes sign at most once; `F'(0+)=+infty`, `F'(1/4)=log_2 3-2<0`, and `F'(1/2)=0`. Hence `F` increases once and then decreases to `F(1/2)=0`, so `F>=0`.

Apply (4.4) first at `(1+t)/2` and then at `u`:
\[
1-h_2\!\left(\frac{1+t}{2}\right)\le t^2,
\qquad
h_2(u)\ge4u(1-u)=t^2.
\]
Thus the bracket in (4.3) is at most `h_2(u_T)`. Summing and using concavity,
\[
\operatorname{JS}(P,Q)
\le\sum_Ts_Th_2(u_T)
\le h_2\!\left(\sum_Ts_Tu_T\right)
=h_2(M).
\]
QED.

This bound is complementary to P03's `JS<=2M/ln2`: the linear estimate is stronger for tiny `M`, while (4.2) matches the binary-entropy scale needed below and is tight at disjoint laws (`M=1/2`, `JS=1`).

### Lemma 4.3 — sparse Boolean phase entropy is paid by edge boundary
For `0<=delta<=1/2`,
\[
\boxed{h_2(\delta)\le 2\delta\log_2(1/\delta).}
\tag{4.5}
\]
Indeed, in natural logs the difference between the right side and `h` is
\[
G(\delta)=-\delta\ln\delta+(1-\delta)\ln(1-\delta).
\]
It vanishes at `0` and `1/2`, while
\[
G'(\delta)=-\ln(\delta(1-\delta))-2,
\qquad
G''(\delta)=\frac{2\delta-1}{\delta(1-\delta)}<0
\]
on `(0,1/2)`. Hence `G'` crosses zero once and `G` rises then falls back to zero.

By the cube edge-isoperimetric inequality, a Boolean phase with minority density `delta` satisfies
\[
I(d)\ge2\delta\log_2(1/\delta).
\tag{4.6}
\]
Therefore
\[
\boxed{h_2(\delta)\le I(d).}
\tag{4.7}
\]

## 5. Main local theorem: oblique derivative pays allocation and full decrement

### Theorem 5.1 — oblique-derivative payment
With the notation of Section 2,
\[
\boxed{B_i(f)\le I(d),}
\tag{5.1}
\]
and, writing
\[
\Delta_iH(f):=H(f)-\frac{H(g)+H(h)}2,
\]
\[
\boxed{\Delta_iH(f)\le2I(d).}
\tag{5.2}
\]
Since the two `i`-children of `D_vf` are translations of each other,
\[
I(D_vf)=\operatorname{Inf}_i(D_vf)+I(d),
\]
so in particular
\[
\boxed{B_i(f)\le I(D_vf),\qquad \Delta_iH(f)\le2I(D_vf).}
\tag{5.3}
\]

### Proof
By Lemma 3.1, `M_i<=delta<=1/2`. Lemma 4.1 and monotonicity of `h_2` on `[0,1/2]` give
\[
B_i(f)\le h_2(M_i)\le h_2(\delta)\le I(d),
\]
using (4.7).

P03's exact one-step decomposition is
\[
\Delta_iH=B_i+\operatorname{JS}(P,Q).
\]
By Lemmas 4.1 and 4.2,
\[
\Delta_iH\le2h_2(M_i)\le2h_2(\delta)\le2I(d).
\]
The final comparison with `I(D_vf)` follows from the exact influence split of `D_vf` and equality of the residual influences of its two translated `i`-children. QED.

### Interpretation
The earlier coordinate-curvature payment uses `D_{e_i}f`. Theorem 5.1 may optimize over **any** translation vector `v` with `v_i=1`. Thus a coordinate split can be cheap because its two children are almost translates even when the coordinate derivative itself has enormous boundary. Exact signed symmetry is the zero-boundary case `I(d)=0` and recovers P03's zero-cost quotient theorem.

This is the paid approximate-isospectral recombination requested by P03's newest obstruction.

## 6. Multi-pivot approximate quotient peeling

Let `v_1,...,v_r` be linearly independent translation vectors in row-echelon form with pivot coordinates `i_1,...,i_r`: `(v_k)_{i_k}=1` and `(v_k)_{i_j}=0` for `j<k`.

Query `i_1,...,i_r` in that order on every live branch. At level `k`, every earlier assignment defines a restricted function `f_a`; because `v_k` has zeros on earlier pivots, it remains a valid translation direction inside that branch.

### Theorem 6.1 — paid approximate signed-translation quotient
For this `r`-layer physical prefix `T_V`,
\[
\boxed{R_{T_V}^{\rm prefix}(f)\le\sum_{k=1}^r I(D_{v_k}f),}
\tag{6.1}
\]
and
\[
\boxed{H(f)-\sum_{\ell}w_\ell H(f_\ell)
\le2\sum_{k=1}^r I(D_{v_k}f).}
\tag{6.2}
\]

### Proof
At a level-`k` node `a`, Theorem 5.1 gives
\[
B_{i_k}(f_a)\le I(d_{a,k}),
\qquad
\Delta_{i_k}H(f_a)\le2I(d_{a,k}),
\]
where `d_{a,k}` is one `i_k`-child of `(D_{v_k}f)_a`.

The derivative `(D_{v_k}f)_a` is still invariant under translation by the residual `v_k`; hence its two `i_k`-children are translates and have equal residual influence. Therefore
\[
I(d_{a,k})
=I((D_{v_k}f)_a)-\operatorname{Inf}_{i_k}((D_{v_k}f)_a)
\le I((D_{v_k}f)_a).
\]
Averaging over all assignments `a` to the earlier pivots and iterating the exact restriction identity for total influence gives
\[
\sum_a w_a I((D_{v_k}f)_a)\le I(D_{v_k}f).
\]
Summing over `k` proves (6.1) and (6.2). QED.

### Corollary 6.2 — grafted hereditary/direct certificates
If every terminal leaf of the prefix has a hereditary certificate with constant `K`, then
\[
\boxed{R_T(f)\le K I(f)+\sum_{k=1}^r I(D_{v_k}f).}
\tag{6.3}
\]
If every terminal leaf instead satisfies direct FEI with constant `K`, then
\[
\boxed{H(\widehat f^{\,2})\le K I(f)+2\sum_{k=1}^r I(D_{v_k}f).}
\tag{6.4}
\]
Indeed the weighted average residual leaf influence is at most `I(f)`.

Hence if
\[
\sum_k I(D_{v_k}f)\le\lambda I(f),
\]
the hereditary constant is at most `K+lambda` and the direct FEI constant at most `K+2lambda`.

When each `D_{v_k}f` is constant, `lambda=0`: this recovers exact signed-translation quotient peeling but also proves a quantitative robustness statement when symmetry is only approximate.

### Corollary 6.3 — perturbations of a signed-symmetric core
If `f=f_0 e` and `f_0(x+v_k)=sigma_k f_0(x)` for each `k`, then
\[
D_{v_k}f=\sigma_k D_{v_k}e.
\]
Thus the entire quotient surcharge depends only on the **symmetry-breaking perturbation** `e`:
\[
R_{T_V}^{\rm prefix}(f)\le\sum_k I(D_{v_k}e).
\tag{6.5}
\]
The complexity of the signed-symmetric core itself does not enter this prefix cost.

## 7. Application to P03's newest obstruction: a rigid near-isospectral family

P03's antipodal two-defect function has exact translation symmetry, so its zero allocation is already explained by the exact quotient theorem. To test the genuinely unresolved **approximate** case, break that symmetry by one point.

For `n>=4`, let
\[
S_n=\{0,\mathbf1,e_1\}\subset F_2^n,
\qquad
f_n(x)=1-2\,1_{S_n}(x).
\tag{7.1}
\]

### Proposition 7.1 — signed-translation rigidity
`f_n` has no nonzero signed physical translation symmetry.

### Proof
If `f_n(x+v)=f_n(x)`, then `S_n+v=S_n`. Any nonzero translation partitions the cube into two-cycles, so every invariant set has even cardinality, contradicting `|S_n|=3`.

If `f_n(x+v)=-f_n(x)`, translation sends `S_n` to its complement, forcing `|S_n|=2^{n-1}`, again impossible for `n>=4`. QED.

Thus P03's exact signed-symmetry quotient theorem does **not** apply.

Take the oblique vector
\[
v=\mathbf1.
\]
Then
\[
S_n\triangle(S_n+v)=\{e_1,e_1+\mathbf1\},
\]
so `D_v f_n` is exactly an antipodal two-defect phase. At the pivot `i=1`, the aligned child mismatch `d` is a one-point defect on `n-1` variables. Therefore
\[
\boxed{I(d)=(n-1)2^{2-n}.}
\tag{7.2}
\]
The root influences are
\[
\boxed{
\operatorname{Inf}_1(f_n)=2^{1-n},
\qquad
\operatorname{Inf}_j(f_n)=3\,2^{1-n}\ (j>=2),
}
\tag{7.3}
\]
so
\[
\boxed{I(f_n)=(3n-2)2^{1-n}.}
\tag{7.4}
\]
Consequently
\[
\boxed{
\frac{I(d)}{I(f_n)}
=\frac{2(n-1)}{3n-2}<\frac23.
}
\tag{7.5}
\]
Theorem 5.1 therefore pays the root hereditary allocation using less than `2I(f_n)/3`, uniformly in dimension.

### The old surcharge obstruction persists
At the same physical query `i=1`, the two children are:

- a one-point defect on `n-1` variables, with influence `(n-1)2^{2-n}`;
- an antipodal two-defect on `n-1` variables, with influence `(n-1)2^{3-n}`.

Hence P03's minor-child surcharge satisfies
\[
\boxed{
\frac{\min\{I(f_n^0),I(f_n^1)\}}
{\operatorname{Inf}_1(f_n)}=2(n-1).
}
\tag{7.6}
\]
The coordinate derivative `D_{e_1}f_n=f_n^0f_n^1` is a one-point defect on `n-1` variables, so
\[
\boxed{
\frac{\frac12 I(D_{e_1}f_n)}
{\operatorname{Inf}_1(f_n)}=n-1.
}
\tag{7.7}
\]
Thus even the better of the previous positive minor-child/coordinate-curvature surcharges diverges linearly, exactly as in P03's mechanism obstruction, **but now the function is signed-translation-rigid**. The zero-cost exact quotient explanation has genuinely been removed.

The oblique theorem still sees the near-symmetry: the aligned mismatch is only one point, and its boundary is a bounded fraction of the *global* influence budget.

### Hereditary stopping consequence
Both root children are already covered by preserved NM13-02 history:

- one-point defects are one-point perturbations of the constant quadratic phase and admit hereditary constant `C_chi`;
- antipodal two-defects have an exact one-dimensional translation symmetry and quotient to a one-point defect, so they inherit the same constant.

Querying coordinate `1`, applying Theorem 5.1, and grafting those leaf certificates gives
\[
R_T(f_n)
\le I(d)+C_\chi\frac{I(f_n^0)+I(f_n^1)}2.
\]
Using the exact influence identity and (7.2)--(7.4),
\[
\boxed{
\frac{R_T(f_n)}{I(f_n)}
\le
\frac{(n-1)(2+3C_\chi)}{3n-2}
<C_\chi+\frac23
=3.541705441581194\ldots .
}
\tag{7.8}
\]
This is an all-dimensional hereditary theorem for a signed-translation-rigid approximate-isospectral family. It is not a proof of full FEI.

The key demonstrated gain is qualitative: **local query influence is not the only conserved currency available for dependent-branch recombination.** A sparse oblique directional derivative can price an approximate quotient step against global influence even when every coordinate-local surcharge is unbounded relative to the queried influence.

## 8. Sanity checker executed

Executed file:

`proofnet24/NM13-02/progress-entropy/runs/2026-09-20/2026-09-20T13-08-00+0300__oblique-derivative-paid-quotient-check.py`

Creation commit: `23b55b59fbabb2ea8789d0d7140520ba4ab9cc42`.

Archived output:

`proofnet24/NM13-02/progress-entropy/runs/2026-09-20/2026-09-20T13-08-00+0300__oblique-derivative-paid-quotient-check.out`

Creation commit: `5ce0e5bcc97d90a5be239d5a79c4792ef8268472`.

The checker:

- exhaustively tested all `1,570` `(f,v,i)` cases through dimension three modulo global sign with `v_i=1`;
- tested `1,200` deterministic dimension-four cases;
- verified `M_i<=delta`, `B_i<=I(d)`, and `Delta_iH<=2I(d)` with maximum numerical violation exactly `0.0` in all three metrics;
- directly checked the rigid tri-defect formulas and absence of any nonzero signed translation symmetry for dimensions `4,...,12`;
- recovered the old surcharge ratios `2(n-1)` and `n-1` and the new oblique cost ratio tending to `2/3`.

Status: `PASS`. The computations are sanity checks only; the theorem is analytic.

## 9. Failure/limitation and next attack

This theorem does **not** prove that every Boolean function has a nonzero direction `v` with
\[
I(D_vf)=O(I(f))
\]
in a way that can be iterated for a dimension-free total surcharge. The trivial product inequality only gives `I(D_vf)<=2I(f)` for each fixed `v`; summing this over many pivots would still incur depth growth. Therefore the universal FEI obstruction is not removed.

The next nonredundant target is an **amortized directional-derivative basis theorem**: either prove that every signed-translation-rigid connected high-degree core admits a row-echelon family of directions whose *total* derivative boundary is paid by a constant multiple of the influence consumed before a certified leaf is reached, or construct a rigid counterfamily where every useful direction has large derivative boundary. The latter would delimit the approximate-isospectral route decisively.

This is materially different from the retired minor-child, coordinate-curvature, derivative-degree, fixed-Renyi, and absolute-overlap scalar routes.

## 10. ledger_delta

```yaml
ledger_delta:
  worker: NM13-02
  parent_problem: Friedgut-Kalai Fourier entropy-influence
  parent_scope_before: OPEN
  parent_scope_after: OPEN
  universal_constant_before: UNKNOWN
  universal_constant_after: UNKNOWN
  fresh_control_status: restricted_only_unchanged
  p03_dependency:
    report: proofnet24/P03-fei/runs/2026-09-20/2026-09-20T12-28-55+0300__fei-isospectral-splicing-symmetry-quotient.md
    exact_live_obstruction: approximate-isospectral/Hellinger-defect hereditary payment on signed-translation-rigid connected cores
  new_theorems:
    - oblique alignment gives Hellinger defect M_i <= folded mismatch density delta
    - hereditary allocation B_i <= I((D_v f)|pivot-child) for every v crossing the queried coordinate
    - Jensen-Shannon(P,Q) <= h_2(M) and full decrement Delta_i H <= 2 I((D_v f)|pivot-child)
    - row-echelon approximate signed-translation quotient prefix has allocation <= sum_k I(D_{v_k} f)
    - same prefix has full entropy decrement <= 2 sum_k I(D_{v_k} f)
    - perturbations of an exact signed-symmetric core pay only the directional derivatives of the symmetry-breaking perturbation
  application:
    family: tri-defect f_n = 1 - 2*1_{0,1^n,e_1}
    signed_translation_rigid: true for n>=4
    old_minor_surcharge_over_query_influence: 2(n-1)
    old_half_coordinate_derivative_surcharge_over_query_influence: n-1
    oblique_aligned_derivative_cost_over_total_influence: 2(n-1)/(3n-2) < 2/3
    hereditary_constant: < C_chi + 2/3 = 3.541705441581194
  checker:
    exhaustive_oblique_cases_n_le_3: 1570
    dimension4_sample_cases: 1200
    rigid_tri_defect_dimensions: 4..12
    max_M_minus_delta: 0.0
    max_B_minus_I_d: 0.0
    max_DeltaH_minus_2I_d: 0.0
    status: PASS
  source_level_gain: none; full FEI remains open
  mechanism_gain: quantitative robustification of exact signed-translation quotient via oblique derivative boundary
  residual_obstruction: dimension-free amortization of directional-derivative boundaries over a full stopping tree
  next_attack: amortized row-echelon directional-derivative basis or rigid counterfamily
  novelty_status: UNVERIFIED
  independent_review_status: pending
```

**End of substantive run report.**
