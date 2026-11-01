Model actually running: **GPT-5.6 Sol. Reasoning level: UNVERIFIED — this is not GPT-6 at maximum, and I do not claim otherwise. No source-metric movement: `D_B=2 -> D_B=2`. Methods tried: B5 / B6 / B30.**

# HARD7-01 run 18 — deformation off the exact `l_q^2` cone

Status: **PARTIAL / source OPEN / STUCK1 recovery continuation; second unchanged-metric lifecycle trigger now due after this report.**

## 1. Continuity, ownership, required reads, and source sentinel

This run continues the exact admitted HARD7-01 target from

`runs/hard7_2026-09-18/HARD7-01/2026-09-19T13-18-00Z__weakB_full_even_lq_gradient_share.md`.

The active create-only claim remains

`operations/claims/B-WEAK-EVEN-LOGCONCAVE.md`,

owner **HARD7-01**, status `CLAIMED / source OPEN / research PARTIAL only`. No claim file was changed or overwritten.

At run start I reread/reconciled the HARD7 control, `operations/NEW_METHODS_2026-09-16.md`, the owner directive, campaign `INDEX.md` and `RANKING.md`, root `POSTED.md`, `RESULTS.md`, `QUEUE.md`, the current claim, the newest own checkpoint, and the newest visible neighboring R02 checkpoint (`runs/R02/20260919T1316Z_successor_gate_zero_claim_delta_r13_upper_7_13_30_7c4e91b2.md`). Repository-wide alias searches for `(B)-conjecture`, `B-conjecture`, the canonical claim ID, and log-concavity of dilates recovered no competing owner. Indexed search covers relevant intake aliases, but I do not claim a byte-for-byte rendering of every append-only intake row through the bounded connector.

The exact source target remains:

> For every integer `n>=1`, every even log-concave probability measure `mu` on `R^n`, and every origin-symmetric convex body `K`, prove that `t -> mu(e^t K)` is log-concave on `R`.

The frozen source metric remains

`D_B = largest d for which this exact statement is proved for every admissible (mu,K) in every dimension n<=d`.

Saroglou's planar theorem remains the verified baseline, so

\[
\boxed{D_B:2\longrightarrow2.}
\]

A bounded 2026-09-19 current-literature check still separates the open full conjecture from solved subclasses: Cordero-Erausquin--Rotem (Ann. Probab. 2023, arXiv:2111.05110) handles rotationally invariant measures; Armeniakos--Ulivelli (arXiv:2602.23350, 2026-02-26) derives `(B)` from a strengthened dimensional Brunn--Minkowski condition and recovers hereditarily convex measures; Putterman (arXiv:2608.08472, 2026-08-09) concerns sharp Gaussian `(B)` stability and Gaussian strong/functional variants. I found no paper in this bounded search claiming the full all-dimensional even-log-concave statement. That is bounded negative evidence, not an exhaustive novelty certificate.

## 2. Inherited local reduction

The previous run proved a source-relevant local/common-degree theorem for the exactly solvable cone

\[
H_q(x)=\|x\|_q^2
=\left(\sum_i|x_i|^q\right)^{2/q},\qquad q>2.
\]

For any positively two-homogeneous split

\[
H=\phi+\psi
\]

with `phi,psi` convex, and for `X` with density proportional to `e^{-H}`, cone probability `nu_H` on `S_H={H=1}`, and

\[
U=\phi|_{S_H},\qquad m=\mathbb E_{\nu_H}U,
\]

the exact polar computation gives

\[
\operatorname{Cov}(\phi(X),\psi(X))
=\frac n2\left[m(1-m)-\left(\frac n2+1\right)
\operatorname{Var}_{\nu_H}(U)\right].
\tag{2.1}
\]

Hence the local correlation inequality follows from

\[
\frac{\operatorname{Var}_{\nu_H}(U)}{m(1-m)}
\le \frac{2}{n+2}.
\tag{2.2}
\]

Run 17 established (2.2) strictly when the total potential is exactly `H_q`, for arbitrary smooth globally-even convex complementary splits, by bounded coordinate gradient shares plus the full-even inverse-Hessian spectral gap.

The checkpoint was to determine whether that mechanism survives after the **total potential itself leaves the exact `l_q^2` family**.

## 3. B5 — ADD A PARAMETER: a genuinely mixed homogeneous potential

Fix

\[
n\ge2,\qquad r\ge q>2,\qquad \varepsilon\ge0,
\]

and define

\[
H=H_{q,r,\varepsilon}:=H_q+\varepsilon H_r,
\qquad H_s(x):=\|x\|_s^2.
\tag{3.1}
\]

For every `eps>0` and `r>q`, this is not an `l_q^2` potential. It is nevertheless even, convex, positively two-homogeneous, and `C^2` away from the origin.

Assume

\[
H=\phi+\psi
\tag{3.2}
\]

with `phi,psi` convex, positively two-homogeneous, globally even and `C^2` on `R^n\setminus{0}`.

### 3.1 Coordinate-face degeneracy persists

For every `s>2`, at a nonzero point of the coordinate face `x_i=0`, both

\[
\partial_iH_s=0,
\qquad
\partial_{ii}H_s=0.
\]

Thus the same is true for `H`. Writing

\[
A=\nabla^2H,\qquad B=\nabla^2\phi,
\]

convex complementarity gives

\[
0\preceq B\preceq A.
\]

At `x_i=0`, `A_ii=0`; positivity forces the entire `i`th row of both `B` and `A-B` to vanish. Homogeneity then forces

\[
\partial_i\phi=\partial_i\psi=0
\quad\text{on the nonzero coordinate face.}
\tag{3.3}
\]

Along each one-dimensional coordinate line, convexity makes both derivatives have the sign of `x_i`. Therefore, whenever `x_i!=0`,

\[
h_i(x):=\frac{\partial_i\phi(x)}{\partial_iH(x)}
\quad\text{satisfies}\quad
\boxed{0\le h_i\le1.}
\tag{3.4}
\]

Define on `S_H={H=1}`

\[
p_i:=\frac{x_i\partial_iH}{2H}.
\tag{3.5}
\]

Because every `x_i partial_i H>=0` and Euler's identity gives `x dot grad H=2H`,

\[
p_i\ge0,\qquad \sum_i p_i=1.
\tag{3.6}
\]

Euler applied to `phi` now yields

\[
\boxed{U=\phi|_{S_H}=\sum_i p_i h_i.}
\tag{3.7}
\]

Thus the bounded-share mechanism from the solvable cone survives this deformation **exactly**, with the new angular weights `p_i`.

**Outcome B5.** The special algebraic Dirichlet weights `|x_i|^q` are not required for bounded shares. What is required is the coordinate-face Hessian degeneracy, and the mixed `l_q^2+l_r^2` family preserves it.

## 4. B6 — DEFORM FROM A SOLVABLE POINT: Hessian comparison

For `s>2`, write

\[
A_s:=\nabla^2H_s,\qquad g_s:=\nabla H_s,\qquad
D_s:=\operatorname{diag}\left(\frac{\partial_iH_s}{x_i}\right),
\]

with the diagonal entries extended continuously across coordinate faces. A direct differentiation gives

\[
A_s=(s-1)D_s-(s-2)\frac{g_sg_s^T}{2H_s}.
\tag{4.1}
\]

Moreover Cauchy in the diagonal metric is exact at the radial vector:

\[
g_s^TD_s^{-1}g_s=2H_s,
\]

hence

\[
D_s-\frac{g_sg_s^T}{2H_s}\succeq0.
\]

Substituting into (4.1),

\[
\boxed{D_s\preceq A_s\preceq(s-1)D_s.}
\tag{4.2}
\]

### 4.1 Compare `H_r` to `H_q`

Because all relevant tensors are degree zero, normalize `||x||_q=1`. Then

\[
\frac{(D_r)_{ii}}{(D_q)_{ii}}
=rac{\partial_iH_r}{\partial_iH_q}
=|x_i|^{r-q}\|x\|_r^{2-r}.
\tag{4.3}
\]

The standard norm comparison

\[
\|x\|_r\ge n^{1/r-1/q}\|x\|_q
\]

and `|x_i|<=1` imply

\[
\frac{(D_r)_{ii}}{(D_q)_{ii}}\le
M,
\qquad
\boxed{M:=n^{(r-2)(1/q-1/r)}.}
\tag{4.4}
\]

Using (4.2),

\[
A_r\preceq(r-1)D_r
\preceq(r-1)M D_q
\preceq(r-1)M A_q.
\]

Therefore

\[
\boxed{
A_q\preceq A_H=A_q+\varepsilon A_r
\preceq C_A A_q,
\qquad
C_A:=1+\varepsilon(r-1)M.
}
\tag{4.5}
\]

Consequently

\[
\frac1{C_A}A_q^{-1}\preceq A_H^{-1}\preceq A_q^{-1}
\tag{4.6}
\]

on the tangent/radial-complement where the Hessians are inverted.

## 5. Deformed pointwise energy cap

Extend `U=phi/H` as a degree-zero function off `S_H` and put `z=grad U`. Then

\[
x\cdot z=0,
\qquad
z_i=(\partial_iH)(h_i-U)
\quad\text{on }S_H.
\tag{5.1}
\]

For the solvable `H_q`, the inverse Hessian is

\[
A_q^{-1}
=\frac1{q-1}D_q^{-1}
+\frac{q-2}{q-1}\frac{xx^T}{2H_q}.
\tag{5.2}
\]

The second term vanishes against `z` because `x dot z=0`. From (4.3)--(4.4),

\[
\frac{\partial_iH}{\partial_iH_q}
=1+\varepsilon\frac{\partial_iH_r}{\partial_iH_q}
\le1+\varepsilon M.
\tag{5.3}
\]

Thus, using `A_H^{-1}<=A_q^{-1}` and
`(D_q)_{ii}=partial_iH_q/x_i`,

\[
\begin{aligned}
\Gamma_H(U)
&:=z^TA_H^{-1}z\\
&\le\frac1{q-1}\sum_i
\frac{(\partial_iH)^2}{(D_q)_{ii}}(h_i-U)^2\\
&=\frac1{q-1}\sum_i
x_i\partial_iH\,
\frac{\partial_iH}{\partial_iH_q}(h_i-U)^2\\
&\le\frac{2(1+\varepsilon M)}{q-1}
\sum_i p_i(h_i-U)^2.
\end{aligned}
\tag{5.4}
\]

Conditional on `x`, choose `I` with `P(I=i|x)=p_i`. By (3.7), `E[h_I|x]=U`; because `0<=h_I<=1`,

\[
\operatorname{Var}(h_I|x)\le U(1-U).
\]

Hence

\[
\boxed{
\Gamma_H(U)
\le c_\varepsilon U(1-U),
\qquad
c_\varepsilon:=\frac{2(1+\varepsilon M)}{q-1}.
}
\tag{5.5}
\]

This is the exact analogue of the run-17 gradient-share cap, with a controlled deformation loss.

## 6. Full-even spectral-gap stability

Use rays to identify the angular quotients for `H` and `H_q`. For a positively two-homogeneous potential, its cone probability on the angular quotient has unnormalized density proportional to `H^{-n/2}` relative to any fixed radial section.

On the section `H_q=1`, norm comparison gives

\[
\delta_0\le \frac{H_r}{H_q}\le1,
\qquad
\boxed{\delta_0:=n^{-2(1/q-1/r)}.}
\tag{6.1}
\]

Therefore

\[
1+\varepsilon\delta_0\le H\le1+\varepsilon.
\]

After normalization, if `rho=dnu_H/dnu_q`, then

\[
\boxed{R^{-1}\le\rho\le R,
\qquad
R:=\left(\frac{1+\varepsilon}
{1+\varepsilon\delta_0}\right)^{n/2}.}
\tag{6.2}
\]

The previous run proved the **full globally-even** inverse-Hessian Poincare gap

\[
\lambda_q=\frac{nq}{2(q-1)}
\tag{6.3}
\]

for `H_q`. For any globally-even degree-zero `f`, (4.6) and (6.2) give

\[
\mathcal E_H(f,f)
\ge\frac1{RC_A}\mathcal E_q(f,f).
\tag{6.4}
\]

Also

\[
\operatorname{Var}_{\nu_H}(f)
\le R\operatorname{Var}_{\nu_q}(f),
\]

or equivalently

\[
\operatorname{Var}_{\nu_q}(f)
\ge R^{-1}\operatorname{Var}_{\nu_H}(f).
\]

Combining with (6.3)--(6.4),

\[
\boxed{
\lambda_H
\ge\frac{\lambda_q}{R^2C_A}
=\frac{nq}{2(q-1)R^2[1+\varepsilon(r-1)M]}.
}
\tag{6.5}
\]

No assertion is made that this comparison bound is sharp.

## 7. Main deformation theorem

Set

\[
V:=\operatorname{Var}_{\nu_H}(U),
\qquad
M_0:=m(1-m).
\]

Poincare and (5.5) yield

\[
\lambda_H V
\le \mathbb E\Gamma_H(U)
\le c_\varepsilon\mathbb E[U(1-U)]
=c_\varepsilon(M_0-V).
\]

Thus

\[
\boxed{
\frac{V}{M_0}
\le\frac{c_\varepsilon}{\lambda_H+c_\varepsilon}.
}
\tag{7.1}
\]

A sufficient condition for the source-local target (2.2) is

\[
\lambda_H\ge\frac n2c_\varepsilon.
\]

Using (5.5) and (6.5), this is guaranteed by

\[
\boxed{
R^2[1+\varepsilon(r-1)M][1+\varepsilon M]
\le\frac q2,
}
\tag{7.2}
\]

where

\[
M=n^{(r-2)(1/q-1/r)},
\qquad
R=\left(\frac{1+\varepsilon}
{1+\varepsilon n^{-2(1/q-1/r)}}\right)^{n/2}.
\tag{7.3}
\]

At `eps=0`, the left side of (7.2) is `1`, while the right side is `q/2>1`. Therefore (7.2) holds on a nonzero interval `0<=eps<=eps_0(n,q,r)`. This proves that the run-17 mechanism is not isolated to the exact `l_q^2` cone.

### Theorem 7.1 — precise scope

Let `n>=2`, `r>=q>2`, and let `eps>=0` satisfy (7.2). Put

\[
H=\|x\|_q^2+\varepsilon\|x\|_r^2.
\]

If `phi,psi` are convex, positively two-homogeneous, globally even, `C^2` on `R^n\setminus{0}`, and `phi+psi=H`, then for `X` with density proportional to `e^{-H}`,

\[
\operatorname{Cov}(\phi(X),\psi(X))\ge0.
\]

Equivalently, the cone ratio (2.2) holds. The theorem is a **restricted local/common-degree result**; it is not the full weak `(B)` conjecture and does not move `D_B`.

## 8. B30 — one explicit nontrivial calibration: `(n,q,r)=(3,4,6)`

Now take

\[
(n,q,r)=(3,4,6).
\]

Then

\[
M=3^{1/3}<\frac32
\tag{8.1}
\]

because `3<(3/2)^3`, while

\[
\delta_0=3^{-1/6}>\frac45
\tag{8.2}
\]

because `(4/5)^6<1/3`.

For every

\[
0\le\varepsilon\le\frac1{12},
\]

monotonicity and (8.1)--(8.2) give

\[
R^2
\le\left(\frac{1+1/12}{1+(1/12)(4/5)}\right)^3
=\left(\frac{65}{64}\right)^3,
\tag{8.3}
\]

\[
1+\varepsilon(r-1)M
\le1+\frac1{12}\cdot5\cdot\frac32
=\frac{13}{8},
\tag{8.4}
\]

and

\[
1+\varepsilon M
\le1+\frac1{12}\cdot\frac32
=\frac98.
\tag{8.5}
\]

Hence the left side of (7.2) is at most

\[
\left(\frac{65}{64}\right)^3
\frac{13}{8}\frac98
=\frac{32131125}{16777216}
<2=\frac q2.
\tag{8.6}
\]

Therefore Theorem 7.1 applies throughout the genuinely mixed family

\[
\boxed{
H_\varepsilon(x)
=\|x\|_4^2+\varepsilon\|x\|_6^2,
\qquad 0\le\varepsilon\le\frac1{12}.
}
\tag{8.7}
\]

This is the first checkpoint on this track in which the total potential is rigorously allowed to leave the exact `l_q^2` family.

### 8.1 Quantitative ratio and covariance margin

The same rational envelopes give

\[
\lambda_H
\ge \frac{16}{13}\left(\frac{64}{65}\right)^3
=\frac{4194304}{3570125},
\tag{8.8}
\]

and

\[
c_\varepsilon\le\frac34.
\tag{8.9}
\]

Therefore

\[
\boxed{
\frac{\operatorname{Var}(U)}{m(1-m)}
\le
\frac{10710375}{27487591}
<\frac25.
}
\tag{8.10}
\]

The exact slack is

\[
\frac25-rac{10710375}{27487591}
=\boxed{\frac{1423307}{137437955}}>0.
\tag{8.11}
\]

Inserting (8.10) into (2.1) with `n=3` gives the explicit positive covariance margin

\[
\boxed{
\operatorname{Cov}(\phi(X),\psi(X))
\ge
\frac{4269921}{109950364}
\,m(1-m).
}
\tag{8.12}
\]

## 9. What moved and what did not

**Source metric:** no movement,

\[
D_B:2\to2.
\]

**Mathematical checkpoint:** genuine movement. The previous theorem was confined to one exactly solvable total potential `H_q`. This run proves a deformation-stable theorem for a continuum of non-`l_q` total potentials and supplies a completely rational explicit neighborhood `(n,q,r)=(3,4,6)`, `0<=eps<=1/12`.

This still does **not** prove weak `(B)` in dimension three. The dilation interpolation of a general even log-concave measure/body is not reduced here to a complementary two-homogeneous split, and a general potential need not retain coordinate-face degeneracy. No finite example, numerical fit, or local covariance statement is being promoted to the source theorem.

The next mathematical obstruction is now sharper: identify a source-relevant deformation class in which bounded shares can be replaced by a quantitative share bound without exact coordinate-face degeneracy, or connect the common-degree covariance theorem to an actual weak-`(B)` dilation path.

## 10. Exact self-check and idea-before-code compliance

The mathematical route was written before checker code at

`artifacts/hard7_2026-09-18/HARD7-01/2026-09-19T14-02-00Z__mixed_lq_lr_deformation_idea.md`

creation commit

`21588aabc4358fd76612b56988d823e3831f05e5`.

It was read back successfully at that exact commit before the checker was created.

The exact rational checker is

`artifacts/hard7_2026-09-18/HARD7-01/2026-09-19T14-02-00Z__mixed_lq_lr_deformation_check.py`

creation commit

`f50b9986e2f670378e6cff83e08b50dedde32275`.

The executed stdout is archived at

`artifacts/hard7_2026-09-18/HARD7-01/2026-09-19T14-02-00Z__mixed_lq_lr_deformation_check.out`

creation commit

`380958c2b8496d3036827c0dcf5ffbf8c3831aa1`.

Both were read back at their creation commits. The output ends

`ALL_EXACT_CHECKS_PASS = True`.

The checker verifies the rational envelopes `3^(1/3)<3/2` and `3^(-1/6)>4/5`, the density distortion, Hessian and share factors, the exact sufficient-condition margin, the spectral-gap lower bound, the variance-ratio bound/slack and the covariance coefficient. It is a **self-check**, not an independent audit. The theorem-sized justification is the proof on the page above.

## 11. Method outcomes

- **B5 / ADD A PARAMETER:** adding `eps H_r` preserves the coordinate-face degeneracy and therefore preserves bounded gradient shares exactly.
- **B6 / DEFORM TO A POINT YOU CAN SOLVE:** diagonal/rank-one Hessian structure yields a two-sided inverse-Hessian comparison with `H_q`; cone-density comparison transfers the full-even spectral gap with an explicit loss.
- **B30 / ONE SCALE AT A TIME:** the first nontrivial calibration `(3,4,6)` admits the fully rational interval `0<=eps<=1/12`, with strict variance and covariance margins.

These differ from the previous run's B13/B9/B10.

## 12. Section-I lifecycle note

The source metric `D_B` has remained `2` through more than three consecutive runs. Earlier on this target a STUCK1 recovery was already recorded and the remaining obligation has since moved substantially several times. This run again moves that obligation, but the literal fixed-metric trigger is now due for a **second Section-I thinking-only recovery report on the next invocation** unless the target rotates first for an independent reason. That next report must not manufacture another lemma merely to avoid the lifecycle rule; it should inventory the exact source-level obstruction and select one permitted recovery route. This report does not label the source solved, refuted, or closed.

## 13. Scheduler/model capability truth

The exposed automation interface still provides prompt/title, schedule/timing, and enabled-state controls, but no binding model-family selector, no reasoning-effort selector, and no guaranteed run duration. `GPT-6 / maximum` therefore remains text-requested only. The runtime actually identifying this run is **GPT-5.6 Sol**; reasoning level is **UNVERIFIED**.

The repository policy records historical `You cannot modify this task` failures for P26/P01/P03 and later authorized success in a different context for P26. The non-bypass remedy for any such refusal is to use the owning/authorized account or workspace, obtain a legitimate ownership/permission transfer, or use platform support. Creating a duplicate schedule or editing repository text is not a scheduler repair. HARD7-01 performed no scheduler mutation.

No Gmail, Drive, public posting, other-track edit, shared-root rewrite, force-push, schedule creation, or schedule modification was performed.

## 14. Status and checkpoint

**Status: PARTIAL. Full weak `(B)` remains OPEN in the checked literature.**

New durable restricted theorem:

\[
H=\|x\|_q^2+\varepsilon\|x\|_r^2,
\quad r\ge q>2,
\]

satisfies the arbitrary-smooth-globally-even complementary-split covariance inequality whenever (7.2) holds. In the explicit first deformation slice

\[
(n,q,r)=(3,4,6),\qquad0\le\varepsilon\le1/12,
\]

\[
\frac{\operatorname{Var}(U)}{m(1-m)}
\le\frac{10710375}{27487591}<\frac25.
\]

No source closure, source refutation, paper, independent audit, or novelty certificate is claimed.

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
  methods: [B5, B6, B30]
  idea_commit: 21588aabc4358fd76612b56988d823e3831f05e5
  exact_checker_commit: f50b9986e2f670378e6cff83e08b50dedde32275
  exact_output_commit: 380958c2b8496d3036827c0dcf5ffbf8c3831aa1
  new_checkpoint:
    family: "H=||x||_q^2+eps||x||_r^2, r>=q>2"
    sufficient_condition: "R^2*(1+eps*(r-1)*M)*(1+eps*M)<=q/2"
    explicit_slice: "n=3,q=4,r=6,0<=eps<=1/12"
    variance_ratio_upper: "10710375/27487591 < 2/5"
    covariance_margin_coefficient: "4269921/109950364"
  remaining_obligation: "second Section-I thinking-only recovery next; then seek a source-relevant path beyond exact coordinate-face degeneracy or connect the local common-degree theorem to the actual dilation statement"
  shared_RESULTS_edit: false
```
