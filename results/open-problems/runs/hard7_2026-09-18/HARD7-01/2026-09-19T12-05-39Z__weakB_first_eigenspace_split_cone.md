Model actually running: **GPT-5.6 Sol. Reasoning level: UNVERIFIED — this is not GPT-6 at maximum, and I do not claim otherwise. No source-metric movement: `D_B=2 -> D_B=2`. Methods tried: B12 / B16 / B25.**

# HARD7-01 run 16 — the deficient first Dirichlet eigenspace is source-safe

Status: **PARTIAL / source OPEN / STUCK1 recovery continuation**.

## 1. Continuity, source, ownership, and required reads

This run continues the exact admitted HARD7-01 target from

`runs/hard7_2026-09-18/HARD7-01/2026-09-19T11-02-33Z__weakB_dirichlet_spectral_margin.md`.

The exclusive create-only reservation remains

`operations/claims/B-WEAK-EVEN-LOGCONCAVE.md`,

owner **HARD7-01**, status `CLAIMED / source OPEN / research PARTIAL only`. No claim file is overwritten or aliased.

I reread the controlling HARD7 file, `operations/NEW_METHODS_2026-09-16.md`, the owner directive, campaign `INDEX.md` and `RANKING.md`, root `POSTED.md`, `RESULTS.md`, `QUEUE.md`, the canonical claim, the latest HARD7-01 report, and the newest visible neighboring R02 report (`runs/R02/20260919T1208Z_successor_gate_kressner_owned_p0157_reassigned_3_6_11_3f7c9a12.md`). A repository search of the intake corpus for the weak `(B)` aliases recovered no competing intake claim. The neighboring R02 state is an unrelated successor-admission gate and does not collide with this target.

The source statement remains:

> For every integer `n>=1`, every even log-concave probability measure `mu` on `R^n`, and every origin-symmetric convex body `K`, prove that `t -> mu(e^t K)` is log-concave on `R`.

The frozen source metric remains

`D_B = largest d such that the exact weak (B)-conjecture is proved for every admissible (mu,K) in every dimension n<=d`.

The verified planar baseline is still Saroglou's theorem, so

\[
\boxed{D_B:2\longrightarrow2}.
\]

This run proves a new restricted theorem inside the homogeneous recovery slice. It does **not** prove the full three-dimensional weak `(B)` conjecture and therefore does not move `D_B`.

### Current-literature sentinel, 2026-09-19

I reran bounded searches for `"(B)-conjecture" even log-concave 2026`, `"weak (B)" conjecture even log-concave measure 2026`, and `"log-concavity of dilates" even log-concave 2026`. The current hits still include:

- Cordero-Erausquin--Rotem, *Improved log-concavity for rotationally invariant measures of symmetric convex sets*, Ann. Probab. 51 (2023), arXiv:2111.05110: rotationally invariant class, not all even log-concave measures;
- Armeniakos--Ulivelli, *A strengthening of the dimensional Brunn-Minkowski conjecture implies the (B)-Conjecture*, arXiv:2602.23350, submitted 26 February 2026: implication/structured classes, not the full source;
- Eli Putterman, *Sharp stability for the (B)-theorem*, arXiv:2608.08472, submitted 9 August 2026: stability of the already-proved Gaussian `(B)` theorem and its strong/functional Gaussian generalizations, not the general even-log-concave conjecture.

I found no full all-dimensional resolution in this bounded search. This is negative bounded-search evidence only, not a worldwide openness or novelty certificate.

## 2. Checkpoint inherited from run 15

For the common-degree homogeneous slice, let `phi,psi` be even convex `C^2` positively `p`-homogeneous functions, let

\[
H=\phi+\psi,\qquad S_H=\{z:H(z)=1\},
\]

and let `nu_H` be cone probability on `S_H`. Put

\[
U=\phi|_{S_H},\qquad m=\mathbb E_{\nu_H}U.
\]

For `X` with density proportional to `e^{-H}`, the exact radial-angular computation gives, with `k=n/p`,

\[
\operatorname{Cov}(\phi(X),\psi(X))
=
k\Big[m(1-m)-(k+1)\operatorname{Var}_{\nu_H}(U)\Big].
\tag{2.1}
\]

For the first unresolved calibration `n=3,p=2`, the target is

\[
\boxed{
\operatorname{Var}_{\nu_H}(U)\le \frac25 m(1-m).
}
\tag{2.2}
\]

Run 15 specialized to

\[
H_q(x)=\left(\sum_{i=1}^3|x_i|^q\right)^{2/q},\qquad q>2,
\tag{2.3}
\]

and proved that under cone measure

\[
W_i=|Z_i|^q,\qquad (W_1,W_2,W_3)\sim\operatorname{Dirichlet}(1/q,1/q,1/q),
\tag{2.4}
\]

while the exact unconditional inverse-Hessian gap is

\[
\lambda_1=\lambda_{\rm unc}(3,q)=\frac{3q}{2(q-1)}<3.
\tag{2.5}
\]

Thus the **first nonconstant Dirichlet eigenspace** is precisely the spectral sector where the naive ambient-gap proof fails. Run 15 controlled all splits with a positive relative curvature margin. The present run attacks the remaining curvature-boundary possibility inside that dangerous first eigenspace.

## 3. B16 — COMPUTE THE FIRST EIGENSPACE EXACTLY: a convexity cone for affine angular splits

Every function in the first nonconstant Wright--Fisher eigenspace, plus a constant, has the form

\[
U_\alpha(W)=\alpha_1W_1+\alpha_2W_2+\alpha_3W_3.
\tag{3.1}
\]

The associated `2`-homogeneous summand is

\[
\phi_\alpha(x)
=H_q(x)U_\alpha(x)
=\left(\sum_j|x_j|^q\right)^{2/q-1}
\sum_i\alpha_i|x_i|^q.
\tag{3.2}
\]

Write

\[
R_q:=\frac q{q-2}.
\]

### Theorem 3.1 — exact convexity cone in dimension three

For `q>2`, the function `phi_alpha` in (3.2) is convex if and only if either `alpha=0`, or

\[
\boxed{
\min_i\alpha_i>0,
\qquad
\max_i\alpha_i\le R_q\min_i\alpha_i.
}
\tag{3.3}
\]

Equivalently,

\[
\alpha_i\ge0,
\qquad
(q-2)\alpha_i\le q\alpha_j
\quad\hbox{for every }i,j.
\tag{3.4}
\]

#### Necessity

Restriction to the `i`th coordinate axis gives

\[
\phi_\alpha(te_i)=\alpha_i t^2,
\]

so convexity forces every `alpha_i>=0`.

Now restrict to the `(i,j)` coordinate plane and set `x_i=1`, `x_j=t`, all other coordinates zero. For `t>0`,

\[
\phi_\alpha(1,t)
=(\alpha_i+\alpha_jt^q)(1+t^q)^{2/q-1}.
\]

As `t downarrow 0`,

\[
\phi_\alpha(1,t)
=
\alpha_i+
\left(\alpha_j-\frac{q-2}{q}\alpha_i\right)t^q
+O(t^{2q}).
\tag{3.5}
\]

If the displayed coefficient were negative, the second derivative would be negative for all sufficiently small positive `t`, contradicting convexity. Hence

\[
\alpha_j\ge\frac{q-2}{q}\alpha_i.
\]

Interchanging `i,j` gives (3.4), hence (3.3). If one coefficient is zero, (3.4) forces all to be zero.

#### Sufficiency: the Hessian interval for one coordinate mode

Put

\[
F_i(x):=H_q(x)W_i(x)
=|x_i|^q\left(\sum_j|x_j|^q\right)^{2/q-1}.
\tag{3.6}
\]

Let `A=Hess H_q` and `B_i=Hess F_i`. I claim the sharp matrix interval

\[
\boxed{
-\frac{q-2}{2}A\preceq B_i\preceq\frac q2 A.
}
\tag{3.7}
\]

It is enough to work on one open orthant and normalize `S=sum x_j^q=1`; the coordinate hyperplanes follow by continuity. Let

\[
D=\operatorname{diag}(x_j^{q-2}),
\qquad
s_j=x_j^{q/2},
\qquad
w=x_i^q,
\qquad |s|=1.
\]

After congruence by `D^{-1/2}`, the Hessians are

\[
\widetilde A
=2\big[(q-1)I-(q-2)ss^T\big],
\tag{3.8}
\]

and, writing `e=e_i`,

\[
\begin{aligned}
\widetilde B_i={}&q(q-1)ee^T-(q-2)(q-1)wI\\
&-q(q-2)\big[s(\sqrt w\,e)^T+(\sqrt w\,e)s^T\big]
+2(q-2)(q-1)wss^T.
\end{aligned}
\tag{3.9}
\]

On the orthogonal complement of `span{e,s}`, both shifted forms in (3.7) are plainly nonnegative. On `span{e,s}`, write

\[
s=\sqrt w\,e+\sqrt{1-w}\,f.
\]

For

\[
L=\widetilde B_i+\frac{q-2}{2}\widetilde A,
\]

direct simplification gives

\[
L_{ff}=(q-2)(1-w)\big[2(q-1)w+1\big]\ge0,
\tag{3.10}
\]

\[
\det L
=(q-2)(1-w)\big[2(q-1)^2+(3q-2)w\big]\ge0.
\tag{3.11}
\]

For

\[
M=\frac q2\widetilde A-\widetilde B_i,
\]

one has

\[
M_{ee}=w(q-2)\big[(2q-1)-2(q-1)w\big]\ge0,
\tag{3.12}
\]

\[
\det M
=w(q-2)\big[q(2q-1)-(3q-2)w\big]\ge0.
\tag{3.13}
\]

Thus both two-by-two restrictions are positive semidefinite, proving (3.7).

Consequently the two boundary rays

\[
\frac{q-2}{2}H_q+F_i,
\qquad
\frac q2H_q-F_i
\tag{3.14}
\]

are convex. Their coefficient vectors are positive multiples of

\[
(R_q,1,1)
\quad\hbox{and}\quad
(1,R_q,R_q)
\tag{3.15}
\]

(up to permutation).

Now sort `alpha=(a,b,c)` with `a<=b<=c`. If `c<=R_q a`, then

\[
\alpha
=\lambda(1,1,1)+\mu(1,1,R_q)+\nu(1,R_q,R_q),
\tag{3.16}
\]

where

\[
\lambda=\frac{R_qa-c}{R_q-1},
\qquad
\mu=\frac{c-b}{R_q-1},
\qquad
\nu=\frac{b-a}{R_q-1}.
\tag{3.17}
\]

All three coefficients are nonnegative. The three summands in (3.16) correspond to convex functions by `H_q` itself and (3.14). This proves sufficiency and Theorem 3.1.

**Outcome B16.** The whole first Dirichlet eigenspace is no longer a numerical search: its source-realizability cone is explicit and exact.

## 4. B12 — FIND WHAT IS CONSERVED: complementarity forces a sharp coefficient-range cap

A source-valid split requires **both** `phi_alpha` and

\[
\psi_\alpha=H_q-\phi_\alpha=\phi_{\mathbf 1-\alpha}
\]

to be convex.

Sort again

\[
a\le b\le c,
\qquad d:=c-a.
\]

Theorem 3.1 applied to `alpha` gives

\[
c\le R_qa,
\]
which is exactly

\[
a\ge\frac{q-2}{2}d.
\tag{4.1}
\]

Applied to the reversed complement coefficients

\[
1-c\le1-b\le1-a,
\]
it gives

\[
1-a\le R_q(1-c),
\]
which is exactly

\[
a\le1-\frac q2d.
\tag{4.2}
\]

Combining (4.1)--(4.2),

\[
\boxed{d\le\frac1{q-1}.}
\tag{4.3}
\]

This is the useful conserved/complementary quantity: although the ambient first eigenfunction `W_1` has too much variance for the naive spectral proof, a genuine convex split and its convex complement cannot separate their three first-mode coefficients by more than `1/(q-1)`.

Since

\[
m=\mathbb E U_\alpha=\frac{a+b+c}{3},
\]
we also have

\[
\boxed{
\frac{3q-4}{6}d
\le m\le
1-\frac{3q-4}{6}d.
}
\tag{4.4}
\]

Indeed `m>=a+d/3` and `m<=a+2d/3`, then use (4.1)--(4.2).

**Outcome B12.** The complement `1-alpha` supplies exactly the restriction absent from the relaxed bad mode: source validity caps both angular amplitude and how close its mean can approach `0` or `1`.

## 5. B25 — COUNT THE SAME THING TWICE: exact Dirichlet variance gives a sharp first-eigenspace theorem

For symmetric Dirichlet law (2.4), with total parameter `3/q`, the exact covariance matrix gives

\[
\operatorname{Var}(U_\alpha)
=
\frac{q}{q+3}
\left[
\frac13\sum_i\alpha_i^2
-\left(\frac13\sum_i\alpha_i\right)^2
\right].
\tag{5.1}
\]

Equivalently,

\[
\operatorname{Var}(U_\alpha)
=
\frac{q}{3(q+3)}\sum_i(\alpha_i-m)^2.
\tag{5.2}
\]

For three numbers in an interval of length `d`,

\[
\frac13\sum_i(\alpha_i-m)^2\le\frac{2d^2}{9},
\tag{5.3}
\]

with equality when the middle coefficient coincides with one endpoint. Therefore

\[
\operatorname{Var}(U_\alpha)
\le\frac{2qd^2}{9(q+3)}.
\tag{5.4}
\]

Let

\[
c_q:=\frac{3q-4}{6}.
\]

From (4.4), and because `c_q d<1/2` whenever `d<=1/(q-1)`, one has

\[
m(1-m)\ge c_qd(1-c_qd).
\tag{5.5}
\]

Thus

\[
\frac{\operatorname{Var}(U_\alpha)}{m(1-m)}
\le
\frac{2qd}{9(q+3)c_q(1-c_qd)}.
\tag{5.6}
\]

The right side is increasing in `d`, so (4.3) yields the sharp bound

\[
\boxed{
\frac{\operatorname{Var}(U_\alpha)}{m(1-m)}
\le
R_{\rm aff}(q)
:=
\frac{8q}{(q+3)(3q-4)(3q-2)}.
}
\tag{5.7}
\]

The bound is attained, up to permutation and complement, by

\[
\alpha
=
\left(
\frac{q-2}{2(q-1)},
\frac{q-2}{2(q-1)},
\frac{q}{2(q-1)}
\right).
\tag{5.8}
\]

Indeed both `alpha` and `1-alpha` lie on the boundary of the convexity cone in Theorem 3.1, `d=1/(q-1)`, and equality holds in (4.4) and (5.3).

Most importantly,

\[
(q+3)(3q-4)(3q-2)-20q
=3(q-2)(3q^2+9q-4)>0
\quad(q>2),
\]
so

\[
\boxed{R_{\rm aff}(q)<\frac25\qquad(q>2).}
\tag{5.9}
\]

### Exact `q=4` calibration

For the cone that produced the ambient spectral obstruction,

\[
R_{\rm aff}(4)=\boxed{\frac2{35}},
\tag{5.10}
\]

attained at permutations/complements of

\[
\alpha=(1/3,1/3,2/3).
\]

Here

\[
m=\frac49,
\qquad
\operatorname{Var}(U)=\frac8{567},
\qquad
\frac{\operatorname{Var}(U)}{m(1-m)}=\frac2{35}.
\]

The target allows `2/5`, so the exact slack in normalized variance is

\[
\boxed{\frac25-\frac2{35}=\frac{12}{35}.}
\tag{5.11}
\]

This rules out the **entire first nonconstant Dirichlet eigenspace** as a source-valid counterexample on every three-dimensional `l_q^2` cone with `q>2`, even though that is exactly the eigenspace responsible for the deficient ambient spectral gap.

**Outcome B25.** Counting variance through the exact Dirichlet covariance and counting admissible amplitude through convex-split complementarity close the dangerous linear spectral sector completely.

## 6. What the theorem removes, and the next quantitative obstruction

Run 14 found that the raw first mode has ambient Hessian-metric eigenvalue below `3`. Run 15 showed that a positive uniform curvature margin repairs the loss. This run now shows something stronger on the curvature boundary: **even at zero margin, no source-realizable affine first-mode split can come remotely close to violating the `2/5` target.**

For `q=4`, the Wright--Fisher/Hessian-metric eigenvalues by polynomial degree are

\[
\lambda_d
=\frac{q^2}{2(q-1)}d\left(d-1+\frac3q\right),
\]
so

\[
\lambda_1=2,
\qquad
\lambda_2=\frac{28}{3}.
\tag{6.1}
\]

If an arbitrary source-realizable unconditional `U` is decomposed orthogonally as

\[
U-m=U_1+U_{\ge2},
\qquad
V_1=\|U_1\|_2^2,
\quad
V_2=\|U_{\ge2}\|_2^2,
\]
then the inherited first-order energy cap implies the **conditional algebraic** estimate

\[
4V_1+\frac{34}{3}V_2\le2m(1-m).
\tag{6.2}
\]

Therefore a bound as weak as

\[
\boxed{
V_1\le\frac{19}{55}m(1-m)
}
\tag{6.3}
\]

would already force

\[
V_1+V_2\le\frac25m(1-m).
\]

The pure first-eigenspace source-valid theorem above is much stronger (`2/35 < 19/55`), but orthogonal projection need not preserve the convex-split cone. I **do not** claim (6.3) for general splits. It is the next precise quantitative target: transfer enough of the coefficient-range rigidity to the first spectral projection of an arbitrary source-realizable split.

That is a narrower obstruction than the previous “classify all curvature-complementary splits” checkpoint.

## 7. Exact self-check

The finite/symbolic algebra used above was checked by

`artifacts/hard7_2026-09-18/HARD7-01/2026-09-19T12-05-39Z__affine_eigenspace_check.py`

creation commit

`3d773c8102772c7d11d392d58f5cad49f6debcff`,

with archived output

`artifacts/hard7_2026-09-18/HARD7-01/2026-09-19T12-05-39Z__affine_eigenspace_check.out`

creation commit

`67203151aae33f917c6b674b4f9e82bb68d783a8`.

The output ends

`ALL_EXACT_CHECKS_PASS = True`.

It checks the two shifted two-dimensional Hessian determinants/diagonal entries in (3.10)--(3.13), the exact formula for `R_aff(q)`, the factorization proving `R_aff(q)<2/5`, the `q=4` extremal mean/variance/ratio, `lambda_1=2`, `lambda_2=28/3`, and the conditional first-projection threshold `19/55`. This is a **self-check**, not an independent audit, and the on-page proof remains the theorem-sized justification.

Both artifact commits were read back successfully at their returned commit SHAs before this report was written.

## 8. Method outcomes and lifecycle

- **B16 / COMPUTE EVERY SMALL CASE AND STARE AT THE SEQUENCE:** rather than sample affine angular modes, derive their full source-realizability cone exactly; the `q=4` calculation then generalizes to every `q>2`.
- **B12 / FIND WHAT IS CONSERVED:** using both summands, not one, produces the invariant coefficient-range cap `d<=1/(q-1)` and the accompanying mean window.
- **B25 / COUNT THE SAME THING TWICE:** exact Dirichlet covariance plus the convexity-cone amplitude count gives the sharp source-valid first-eigenspace ratio `R_aff(q)` and excludes the full deficient eigenspace.

These methods are different from the preceding run's B7/B14/B17 and had not been used on the current weak-`(B)` target in the recovered method history.

The source metric still has no movement, but the remaining obligation moved materially: the lowest, deficient spectral sector is now fully controlled when it is itself source-realizable. The next obstruction is not “maybe the first eigenmode is bad”; it is whether a nonlinear source-valid split can carry an anomalously large **projection** onto that mode while higher modes compensate the Hessian constraints. Thus this does not trigger a new Section-I stuck run yet.

## 9. Scheduler/model capability truth

The controlling repository policy and the exposed automation surface still provide task title, prompt, schedule/timing, enabled state and related task controls, but no binding model-family selector, no reasoning-effort selector, and no guaranteed execution duration. `GPT-6 / maximum` therefore remains prompt-requested only. The actual runtime identifying this run is **GPT-5.6 Sol**; reasoning effort is **UNVERIFIED**.

The historical P26 `You cannot modify this task` result was an authorization/context boundary. `RESULTS.md` records that P26 was subsequently updated successfully from another authorized context. The lawful workaround for a refused task is its owning/authorized account or workspace, an authorized ownership/permission repair or transfer, or platform support; a repository write or duplicate schedule is not a repair. No scheduler mutation was attempted here.

## 10. Status and next checkpoint

**Status: PARTIAL. Source weak `(B)` remains OPEN in the checked literature.**

Durable new theorem in the recovery slice:

\[
\phi_\alpha=H_q\sum_i\alpha_iW_i\text{ is convex}
\iff
\max_i\alpha_i\le\frac q{q-2}\min_i\alpha_i
\quad(\alpha\ne0),
\]

and if both `phi_alpha` and `H_q-phi_alpha` are convex, then

\[
\boxed{
\frac{\operatorname{Var}_{\nu_q}(U_\alpha)}{m(1-m)}
\le
\frac{8q}{(q+3)(3q-4)(3q-2)}
<\frac25.
}
\]

For `q=4`, the sharp ratio is `2/35`.

Next checkpoint: for a general unconditional source-realizable split on the `n=3,q=4` cone, prove

\[
\|\Pi_1(U-m)\|_2^2
\le\frac{19}{55}m(1-m),
\]

or construct a genuine source-valid counterexample to that projection bound. The projection statement is only a sufficient recovery target, not the source conjecture itself.

No closure, source refutation, paper, novelty certificate, or independent audit is claimed.

```yaml
ledger_delta:
  worker: HARD7-01
  canonical_claim: B-WEAK-EVEN-LOGCONCAVE
  source_status: OPEN_IN_CHECKED_LITERATURE
  status: PARTIAL
  fixed_metric:
    name: D_B
    before: 2
    after: 2
    movement: none
  methods: [B12, B16, B25]
  new_checkpoint:
    affine_convexity_cone_n3_lq: "max(alpha)<=q/(q-2)*min(alpha), alpha nonzero"
    source_valid_affine_range: "max(alpha)-min(alpha)<=1/(q-1)"
    sharp_affine_variance_ratio: "8q/((q+3)(3q-4)(3q-2)) < 2/5 for q>2"
    q4_sharp_ratio: "2/35"
    q4_next_projection_sufficient_target: "V1/(m(1-m)) <= 19/55"
  exact_checker_commit: 3d773c8102772c7d11d392d58f5cad49f6debcff
  exact_output_commit: 67203151aae33f917c6b674b4f9e82bb68d783a8
  remaining_obligation: "transfer first-eigenspace source rigidity to the first spectral projection of arbitrary source-realizable n=3 q=4 splits, or find a genuine source-valid counterexample"
```