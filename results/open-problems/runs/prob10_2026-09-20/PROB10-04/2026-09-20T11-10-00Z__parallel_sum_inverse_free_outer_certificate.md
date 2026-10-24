Model actually run: **GPT-5.6 Sol. Reasoning level: UNVERIFIED — not GPT-6 maximum.**

# PROB10-04 run 12 — inverse-free parallel-sum certificate for the Díaz outer problem

Repository / branch: private `yspennstate/math-open-problems` / `master`.

Status: **PARTIAL / source OPEN**.

**SOURCE-METRIC NO MOVEMENT.** For the owner-frozen classical iid proper-clause model, the explicitly source-verified decimal bracket used by this track remains

\[
[\alpha_L,\alpha_U]=[3.52,4.4898],\qquad
W=0.9698\longrightarrow0.9698.
\]

This run makes a required method change rather than adding another local rescue motif. The main result is an exact **inverse-free matrix-splitting theorem** for the remaining three-dimensional outer Hessian. It replaces the interval-unstable condition involving two covariance inverses by a sufficient linear-matrix inequality containing only covariance matrices and a frozen rational split matrix. On the inherited finite-decimal saddle surrogate, the best simple scalar split has minimum covariance-LMI eigenvalue about `0.0114689`, whereas a six-decimal matrix split has minimum eigenvalue about `0.0720353`; the latter LMI is verified by exact rational Sylvester tests on that surrogate. This is auxiliary mechanism progress only, not a threshold endpoint.

The three materially different approaches tried were:

1. **scalar collinear parallel split** `T=tI` — works at the inherited saddle surrogate but with a relatively small margin;
2. **full matrix parallel split** — succeeds and yields the new exact theorem/box compiler, with a much larger diagnostic margin;
3. **support-only covariance domination** using only finite support ranges — fails decisively in a concrete direction, overpaying the copy variance by a factor about `5.16`.

No finite SAT/UNSAT instance, annealed fit, physics threshold, or unaudited neighboring candidate is counted as source-level progress.

## 1. Continuity, ownership, and consumed evidence

I continued only the scoped **cluster-aware weighted-counting / overlap-variational** route in

- `operations/claims/PROB10-04.md`, blob `1095e6bfb106b53e810af56f2605521abb7143b4`.

I did not overwrite historical parent claim `F0097`, did not take over NM13-06's constructive lower-bound route, and did not promote NM13-13's interpolation candidate into the external source metric.

Consumed repository state included:

- current `operations/PROB10_2026-09-20.md`;
- current root `POSTED.md` exclusion registry;
- the canonical scoped claim above;
- preserved pre-refocus handoff `runs/hard7_2026-09-18/HARD7-06/2026-09-19T23-49-30Z__handoff_to_prob10-04.md`, blob `e59380417dc476970e22b72b66c59ffbffa4af3a`, which keeps the actual F0095 / binary-cascade 3-colourability work separate from random 3-SAT;
- preceding PROB10-04 report `runs/prob10_2026-09-20/PROB10-04/2026-09-20T10-08-00Z__outer_covariance_compensation_and_support_oracles.md`, which proved the exact covariance Hessian identity and support oracles;
- neighboring upper-route report `proofnet24/NM13-13/progress-3sat/runs/2026-09-20/2026-09-20T09-53-37Z__t04_four_node_gaussian_tail_43888762.md`, status `OPEN / PARTIAL; CANDIDATE_FULL ... pending later independent review`, with project candidate `4.3888762`;
- neighboring constructive report `proofnet24/NM13-06/progress-3sat-construction/runs/2026-09-20/2026-09-20T12-25-17__t04_two_menu_collision_branching.md`, status `OPEN / PARTIAL`, which analyzes a distinct majority-repair/menu route.

The new idea and exact missing lemma were frozen **before code** in

`artifacts/prob10_2026-09-20/PROB10-04/2026-09-20T10-44-30Z__parallel_sum_split_idea_before_code.md`

at creation commit `1eb8f7c032d03852ea708b1b38e7960e816081df`.

The complete theorem proof is frozen in

`artifacts/prob10_2026-09-20/PROB10-04/2026-09-20T10-55-00Z__parallel_sum_split_theorem.md`

at creation commit `a46e352be92514848fea420d37893ae9c693a393`.

The matching checker/output are

- `artifacts/prob10_2026-09-20/PROB10-04/2026-09-20T11-02-00Z__parallel_sum_split_exact.py`, creation commit `7ccf60f72e01309aef13e5346311d81a0b89ae7e`;
- `artifacts/prob10_2026-09-20/PROB10-04/2026-09-20T11-02-00Z__parallel_sum_split_exact.out`, creation commit `662c4ab49595fecc15ddb971ff5fa659800494f3`.

## 2. Source/model baseline checked again

The exact target remains: `m=floor(alpha n)` independent clauses; each clause samples three distinct variables uniformly and then independent fair signs.

The bounded source check for this run keeps the following distinctions explicit.

- Hajiaghayi--Sorkin, `https://arxiv.org/abs/math/0310193`, give the classical iid-model satisfiable lower endpoint `3.52` used here.
- Díaz--Kirousis--Mitsche--Pérez-Giménez, `https://doi.org/10.4230/LIPIcs.FSTTCS.2008.1750`, give the explicit `4.4898` a.a.s.-unsatisfiable upper endpoint. Their proof is precisely the configuration-model / positively-unbalanced / single-flip count whose final outer optimization this route is trying to strengthen.
- Carenini, ECCC TR26-145, publication 16 August 2026, gives an `O(n/log n)` scaling window for every fixed `k>=3`; this is a sharp-window theorem, not identification or convergence of the `k=3` center.
- Chatterjee--Coja-Oghlan--Greenhill--Pfenninger--Rolvien--Zakharov--Zampetakis, published online 27 March 2026, still describe exact satisfiability-threshold identification as open for small fixed `k>=3`, while giving a stronger **symbolic interpolation upper frontier**. Therefore this report calls `[3.52,4.4898]` the track's verified **explicit-decimal** source bracket, not the strongest symbolic formulation known in the literature.
- Ding--Sly--Sun, `https://arxiv.org/abs/1411.0650`, is a sufficiently-large-`k` threshold theorem and is not silently specialized to `k=3`.
- ESA 2025, `https://drops.dagstuhl.de/entities/document/10.4230/LIPIcs.ESA.2025.103`, studies a different `k`-wise-independent clause model and is not substituted for the iid target.

The original Díaz final validation used a coarse three-dimensional outer grid after proving strict concavity only in inner variables. The previous PROB10-04 run replaced the local outer-curvature mystery by an exact Hessian identity; this run attacks the remaining certification obstacle directly.

## 3. Inherited exact Hessian identity

Write the outer copy macrostate as

\[
y=(u,v,w)=(\ell_{ps},\ell_{ns1},\ell_{ns2}).
\]

Let `Sigma_V(y)` and `Sigma_C(y)` be the variable-side and clause-side Gibbs covariance matrices for the three copy-count coordinates. Let

\[
H_{\rm copy}(y)=D(y)^{-1},
\]

where the copy covariance is

\[
D(y)=
\begin{pmatrix}
\dfrac{u(\lambda_p-u)}{\lambda_p}&0&0\\[2mm]
0&\dfrac{v(\lambda_n-v)}{\lambda_n}&-\dfrac{vw}{\lambda_n}\\[2mm]
0&-\dfrac{vw}{\lambda_n}&\dfrac{w(\lambda_n-w)}{\lambda_n}
\end{pmatrix}.
\tag{3.1}
\]

The preceding run proved exactly, in the interior,

\[
\boxed{
\nabla^2\Phi(y)=D(y)^{-1}-\Sigma_V(y)^{-1}-\Sigma_C(y)^{-1}.
}
\tag{3.2}
\]

Direct interval evaluation of (3.2) is awkward: each outer box requires enclosing two inverse covariance matrices, and inversion creates dependency blow-up. The goal of this run was to remove those inversions from the **sufficient** certificate.

## 4. Attack 1 — scalar collinear split

For SPD matrices `A,B`, define the parallel sum

\[
P=(A^{-1}+B^{-1})^{-1}.
\]

The key variational identity is

\[
\boxed{
x^TPx=\min_z\left[z^TAz+(x-z)^TB(x-z)\right].
}
\tag{4.1}
\]

Restricting the minimizer to `z=tx` gives

\[
P\preceq t^2A+(1-t)^2B.
\tag{4.2}
\]

Therefore, if

\[
D-t^2\Sigma_V-(1-t)^2\Sigma_C\succ0,
\tag{4.3}
\]

then the target Hessian is negative definite.

At the inherited finite-decimal `alpha=4.4898` saddle surrogate, `t=0.1309` gives

\[
\lambda\bigl(D-t^2\Sigma_V-(1-t)^2\Sigma_C\bigr)
\approx
(0.0114688933,\ 0.0325324720,\ 0.5956867961).
\tag{4.4}
\]

So the scalar split works locally, but its smallest margin is only about `0.01147`. This makes it unattractive for a global interval cover.

## 5. Attack 2 — full matrix split: exact theorem

The scalar restriction is unnecessary. Let `T` be any real matrix. Evaluating (4.1) at `z=Tx` yields

\[
\boxed{
P\preceq R_T:=T^TAT+(I-T)^TB(I-T).
}
\tag{5.1}
\]

The minimizing split is

\[
T_*=(A+B)^{-1}B,
\tag{5.2}
\]

for which equality holds.

### Theorem 5.1 — inverse-free strict-concavity certificate

Let `A,B,D` be SPD. If there are a fixed matrix `T` and `eta>0` with

\[
\boxed{
D-T^TAT-(I-T)^TB(I-T)\succeq\eta I,
}
\tag{5.3}
\]

then

\[
\boxed{
D^{-1}-A^{-1}-B^{-1}\prec0.
}
\tag{5.4}
\]

If in addition `R_T\preceq L I`, then quantitatively

\[
\boxed{
D^{-1}-A^{-1}-B^{-1}
\preceq
-\frac{\eta}{L(L+\eta)}I.
}
\tag{5.5}
\]

### Proof

From (5.1) and (5.3),

\[
D\succeq R_T+\eta I\succeq P+\eta I.
\]

Inversion reverses Loewner order on the positive cone, hence

\[
D^{-1}\preceq(P+\eta I)^{-1}.
\]

Since `P^{-1}=A^{-1}+B^{-1}`,

\[
D^{-1}-A^{-1}-B^{-1}
\preceq
(P+\eta I)^{-1}-P^{-1}\prec0,
\]

which proves (5.4). If `R_T\preceq LI`, then `P\preceq LI`. On an eigenvalue `lambda` of `P`, the positive matrix

\[
P^{-1}-(P+\eta I)^{-1}
\]

has eigenvalue

\[
\frac{\eta}{\lambda(\lambda+\eta)}
\ge \frac{\eta}{L(L+\eta)},
\]

proving (5.5). QED.

Applied to (3.2), take

\[
A=\Sigma_V,\qquad B=\Sigma_C.
\]

Then (5.3) is a strict outer-concavity certificate containing **no covariance inverse**. This is the main mathematical gain of the run.

## 6. Rational split at the inherited saddle surrogate

Using the preceding run's printed finite-decimal covariance surrogate only to propose a split, I rounded the pointwise optimizer to

\[
T_6=
\begin{pmatrix}
0.325811&0.026584&0.244991\\
0.276295&0.421851&-0.006373\\
0.399423&-0.105053&0.566593
\end{pmatrix}.
\tag{6.1}
\]

The matching checker then treats every displayed decimal in `Sigma_V`, `Sigma_C`, `lambda_p`, `lambda_n`, `u`, `v`, `w`, and `T_6` as an exact rational number. Thus the following claim is exact **for that finite-decimal surrogate**:

\[
D-T_6^T\Sigma_VT_6-(I-T_6)^T\Sigma_C(I-T_6)\succ0.
\tag{6.2}
\]

Sylvester's criterion is verified with exact `Fraction` arithmetic. The three leading principal minors are positive; numerically they are

\[
0.6651866931449382,\quad
0.1662043642561221,\quad
0.03017311880569629.
\]

The corresponding floating eigenvalues are

\[
\boxed{
0.0720352865448,\quad0.462529383793,\quad0.905598275218.
}
\tag{6.3}
\]

The exact pointwise parallel-sum gap computed from the same surrogate has eigenvalues

\[
0.0720352865469,\quad0.462529383793,\quad0.905598275219,
\]

so the six-decimal rational split loses essentially no pointwise margin. Relative to the scalar split's minimum `0.0114688933`, the minimum LMI margin is larger by a factor about

\[
\frac{0.0720352865}{0.0114688933}\approx6.28.
\]

This exact finite check is deliberately **not** an interval certificate for the true transcendental saddle and does not establish (5.3) on a neighborhood. Its purpose is to show that the inverse-free compiler has substantial numerical slack worth certifying globally.

## 7. Attack 3 — support-only covariance domination fails

A more radical route would avoid not only matrix inverses but also the Gibbs multipliers: upper-bound every directional variance solely from its finite state support. For a scalar random variable in an interval of range `R`, Popoviciu gives

\[
\operatorname{Var}(X)\le R^2/4.
\]

Summing this bound over the variable and clause blocks gives explicit support-only upper bounds for

\[
(Tx)^T\Sigma_V(Tx)
+((I-T)x)^T\Sigma_C((I-T)x).
\]

This shortcut is far too loose. At the inherited saddle surrogate with `T=T_6` and the test direction

\[
x=(-1,10,-6),
\]

the support-only upper bound is

\[
496.9676385896875,
\]

whereas the exact copy directional variance is only

\[
x^TDx=96.35650079743404.
\]

The ratio is

\[
\boxed{5.1575932550>1}.
\]

Thus a support-range-only proof cannot certify (5.3) even at this favorable point. The failure mechanism is clear: high-degree variable supports have very wide ranges, while the actual Gibbs law puts exponentially nonuniform mass on them. A successful global proof must retain at least coarse multiplier/probability information; support geometry alone throws away too much.

## 8. What changed mathematically

**Before this run:** the remaining outer problem had an exact Hessian identity but any direct strict-concavity check required interval enclosures of `Sigma_V^{-1}` and `Sigma_C^{-1}` on each outer box.

**After this run:** strict concavity has the inverse-free sufficient certificate

\[
D-T^T\Sigma_VT-(I-T)^T\Sigma_C(I-T)\succeq\eta I,
\]

with a rational `T` frozen per box. The same theorem converts a certified LMI gap into an explicit Hessian margin by (5.5). At the inherited saddle surrogate, a low-complexity rational split has `~0.0720` minimum covariance-LMI slack, versus `~0.0115` for the scalar split. The strongest attempt to remove Gibbs information entirely was falsified by a factor-`5.16` directional counterexample.

This is a mechanism improvement, not source-metric movement.

## 9. Exact missing lemma and unresolved full-scope gap

The next source-relevant lemma is now sharply formulated.

Let `P_out` be the source-relevant projected outer feasible polytope from the exact support oracles of run 11. Construct a finite box cover `P_out subset union_j B_j` and, for every surviving box, a rational matrix `T_j` plus outward interval enclosures for the covariance maps such that either

1. the rescued exponent/support upper bound is already strictly below the target level on `B_j`; or
2. one proves

\[
\boxed{
D(y)-T_j^T\Sigma_V(y)T_j-(I-T_j)^T\Sigma_C(y)(I-T_j)
\succeq\eta_j I,
\qquad \eta_j>0,
\quad y\in B_j.
}
\tag{9.1}
\]

Once (9.1) is available, Theorem 5.1 supplies strict concavity without interval covariance inversion. One must then combine the local stationary-point box with a certified annulus/boundary exponent deficit and the previously proved rescue penalty. Only after that full global optimization is paid can this route claim an improved `4.4898` endpoint.

The present run does **not** provide that interval cover. Therefore the random 3-SAT source problem remains **OPEN**, this track remains **PARTIAL**, and no closure/audit claim is made.

## 10. Actual tests and bookkeeping

The exact finite checker/output are the artifacts listed in section 1. The archived output ends

- `SUPPORT_ONLY_SHORTCUT_FAILS_AT_TEST_DIRECTION = True`;
- `EXACT_RATIONAL_SURROGATE_LMI_PASS = True`;
- `PARALLEL_SUM_SPLIT_DIAGNOSTIC_COMPLETE = True`.

The exact portion consists of rational Sylvester tests for the finite-decimal saddle surrogate. The eigenvalues and support-only ratio are floating diagnostics. No random SAT simulation was run and no finite instance is used as asymptotic evidence.

The HARD7-06 F0095/binary-cascade history remains preserved at its handoff path and is not modified or reinterpreted by this report.