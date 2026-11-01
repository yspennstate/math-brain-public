Model actually run: **GPT-5.6 Sol. Reasoning level: UNVERIFIED. This is not authenticated as GPT-6 at maximum.**

# P03 FEI — dependent-branch recombination is pointwise dominated by hereditary allocation

## 0. Parent status and exact movement

**Parent problem.** Friedgut--Kalai Fourier entropy--influence (FEI): prove one finite universal constant `C` such that

\[
H(\widehat f^{\,2})\le C I(f)
\]

for every Boolean function on every finite uniform cube.

**Source-level status before -> after:** **OPEN -> OPEN.** The unrestricted universal finite constant remains **UNKNOWN -> UNKNOWN**. P03's inherited native finite-dimensional atlas remains **6 -> 6**. No finite enumeration or restricted class below is counted as closure.

**Mechanism-level movement.** The previous P03 run isolated hereditary allocation `B_i=H(S_i\mid S_{-i})` and dependent-branch recombination `J_i^{rec}=JS(P_i,Q_i)` as two local terms in the restriction entropy decrement. This run proves the universal, fresh-variable-free pointwise inequality

\[
\boxed{J_i^{\rm rec}(f)\le B_i(f)}
\tag{0.1}
\]

for every Boolean function and every physical coordinate. Therefore every adaptive physical restriction tree satisfies

\[
\boxed{S_{\mathcal T}\le R_{\mathcal T}},
\tag{0.2}
\]

where `R_T` is the weighted hereditary-allocation sum and `S_T` the weighted dependent-recombination sum. For every full physical restriction tree,

\[
\boxed{R_{\mathcal T}\le H(f)\le2R_{\mathcal T}}.
\tag{0.3}
\]

Thus dependent-branch recombination is **not a separate universal obstruction**: full FEI is equivalent, up to a factor two in the constant, to a universal hereditary allocation bound. The coefficient one in (0.1), and hence the factor two in (0.3), are sharp.

This is a full-scope structural theorem on the original fixed cube, not a restricted-control theorem. It does **not** prove FEI because the missing universal estimate `R_T<=K I(f)` is still open.

## 1. Dependencies consumed and scope preserved

The progress-first directive was followed. I read the complete dependencies needed for the live obstruction, not the whole repository.

- `operations/PROGRESS20_2026-09-20.md`, blob `4a207f06e5c8294c83bcabcd9a1477f26f54b441`: P03 remains T01 FEI owner; the current companion is NM13-02; progress first; one immutable report; restricted results do not close FEI.
- `operations/PROB10_2026-09-20.md`: the fresh-control theorem at commit `ef1087448014f0f6e5c9b4671c200a4020d8e3ea` is explicitly restricted. Its complete supporting report `proofnet24/P03-fei/scheduled-continuation/runs/2026-09-19/2026-09-19T22-18-30Z__report.md` proves
  \[
  L(\Gamma_cf)\le12\Delta_{\rm aff}(\Gamma_cf)
  \]
  only after appending fresh controls, with `c>=3` and `2^{-c}M_0(f)<=1`. It does not yield a fixed-domain hereditary theorem and is not used as one here.
- Current `proofnet24/P03-fei/README.md`, blob `1156fab7d6b2e8360bcbaa138855b97345b8def1`: full FEI remains open. The latest concave-restriction continuation supplies the exact fibre identity used below and the strict concavity of its scalar cap. The polynomial-core/tag and affine-fibre theorems remain restricted classes.
- Latest own substantive report `proofnet24/P03-fei/runs/2026-09-20/2026-09-20T12-28-55+0300__fei-isospectral-splicing-symmetry-quotient.md`: for a physical split it establishes the exact decomposition
  \[
  \Delta_iH=B_i+J_i^{\rm rec},
  \]
  the child-spectrum Hellinger defect, a KL rebate for `B_i`, and exact zero-cost isospectral splicing. Its live target is structure-sensitive hereditary allocation on the remaining signed-translation-rigid core.
- `proofnet24/P03-fei/continuations/2026-09-20-concave-restriction/REPORT.md`: for each parent Fourier fibre it writes the whole decrement as `w Psi(t)`, where the two summands are exactly the hereditary binary entropy and the branch Jensen--Shannon term. That exact identity is reconstructed in Section 2 rather than treated as a black box.
- Newest companion NM13-02 substantive report `proofnet24/NM13-02/progress-entropy/runs/2026-09-20/2026-09-20T13-08-00+0300__oblique-derivative-paid-quotient.md`: it proves approximate-isospectral payments from oblique derivatives, including `B_i<=I(d)` and `Delta_iH<=2I(d)` on its hypotheses. The theorem here is complementary: it compares the recombination and allocation pieces for **every** split, with no derivative hypothesis. No peer file or claim was edited.
- `POSTED.md` was checked for exact-scope exclusions. No posted universal FEI theorem or exact theorem below is being relabeled.

A bounded current source check of González--MacManus--Pereyra, arXiv:2606.00246, still states universal FEI as a conjecture: their key restriction inequality would imply full FEI if universal, while the paper proves stopping-tree/restricted classes. The Friedgut--Kalai 1996 attribution remains standard in current FEI literature. Han's current general bound still contains the coordinate logarithmic profile term and is not `H<=CI`. A bounded search did not surface the exact pointwise comparison (0.1); that is only negative search evidence, so **publication priority is UNVERIFIED**.

## 2. Exact one-fibre decomposition

Fix a Boolean function `f` and a physical coordinate `i`. For a residual Fourier label `T` not containing `i`, write the two parent coefficients

\[
u=\widehat f(T),\qquad v=\widehat f(T\cup\{i\}),
\]

and put

\[
w=u^2+v^2.
\]

If `w=0`, this fibre contributes zero to every quantity below. Assume `w>0` and define

\[
t=\frac{\min\{u^2,v^2\}}{w}\in[0,1/2].
\tag{2.1}
\]

The two physical children have Fourier coefficients

\[
a=u+v,\qquad b=u-v.
\tag{2.2}
\]

Their average squared mass on this residual label is

\[
\frac{a^2+b^2}{2}=u^2+v^2=w.
\]

The queried spectral bit, conditioned on `S_{-i}=T`, has masses `u^2/w` and `v^2/w`. Hence the hereditary allocation contribution of this fibre is exactly

\[
B_T=w h_2(t).
\tag{2.3}
\]

For recombination, let

\[
p=\frac{a^2}{a^2+b^2}=\frac{(u+v)^2}{2w}.
\tag{2.4}
\]

Swapping child labels replaces `p` by `1-p` and does not change entropy. Since

\[
\left|p-\frac12\right|=\frac{|uv|}{w}=\sqrt{t(1-t)},
\]

we may use

\[
p_*=\frac12+\sqrt{t(1-t)}\in[1/2,1].
\tag{2.5}
\]

The equally weighted Jensen--Shannon contribution of this fibre is therefore

\[
J_T=w\,[1-h_2(p_*)].
\tag{2.6}
\]

Equations (2.3) and (2.6) give the existing exact restriction identity

\[
\Delta_iH(f)=\sum_T(B_T+J_T)
=\sum_Tw\left[h_2(t)+1-h_2\!\left(\frac12+\sqrt{t(1-t)}\right)\right].
\tag{2.7}
\]

The new point is that the second summand is bounded by the first **fibre by fibre**.

## 3. Scalar lemma

### Lemma 3.1
For every `x in [0,1]`,

\[
\boxed{h_2(x)\ge4x(1-x).}
\tag{3.1}
\]

Equality holds exactly for `x in {0,1/2,1}`.

### Proof
By symmetry it suffices to work on `[0,1/2]`. Put

\[
F(x)=h_2(x)-4x(1-x).
\]

Then `F(0)=F(1/2)=0` and on `(0,1/2)`

\[
F'(x)=\log_2\frac{1-x}{x}-4+8x,
\]

\[
F''(x)=8-\frac1{\ln2\,x(1-x)}.
\tag{3.2}
\]

Because `x(1-x)` is strictly increasing on `[0,1/2]`, `F''` has at most one zero there. Also

\[
F'(0+)=+\infty,
\qquad
F'(1/4)=\log_2 3-2<0,
\qquad
F'(1/2)=0.
\]

Thus `F'` first decreases through zero and can only turn upward once before reaching zero at `1/2`. Consequently `F` increases from zero, then decreases to zero, and is nonnegative throughout. Strictness away from `0,1/2` on this half interval follows from the same derivative pattern; symmetry supplies the endpoint `1`. QED.

## 4. Main theorem: recombination is dominated by allocation

### Theorem 4.1 — universal local domination
For every Boolean `f` and every physical coordinate `i`,

\[
\boxed{J_i^{\rm rec}(f)\le B_i(f).}
\tag{4.1}
\]

Consequently

\[
\boxed{\Delta_iH(f)\le2B_i(f).}
\tag{4.2}
\]

### Proof
Fix one active fibre and use `t,p_*` from Section 2. Directly from (2.5),

\[
4p_*(1-p_*)=1-4t(1-t).
\tag{4.3}
\]

Apply Lemma 3.1 at `p_*`:

\[
h_2(p_*)\ge4p_*(1-p_*)=1-4t(1-t),
\]
so

\[
1-h_2(p_*)\le4t(1-t).
\tag{4.4}
\]

Apply Lemma 3.1 again, now at `t`:

\[
4t(1-t)\le h_2(t).
\tag{4.5}
\]

Multiplying (4.4)--(4.5) by `w` gives

\[
J_T=w[1-h_2(p_*)]\le wh_2(t)=B_T.
\]

Summing over all residual Fourier labels proves (4.1). Equation (4.2) follows from the exact identity `Delta_iH=B_i+J_i^{rec}`. QED.

### Equality structure
The scalar lemma has equality only at `0,1/2,1`. Therefore an active fibre has `J_T=B_T` exactly when

\[
t\in\{0,1/2\}.
\tag{4.6}
\]

These two endpoint geometries are concrete:

- `t=0`: one parent Fourier coefficient in the `i`-fibre is zero. Equivalently `|a|=|b|`, so the two child squared masses agree on that residual label. This is the fibrewise isospectral endpoint.
- `t=1/2`: `|u|=|v|`. Equivalently one of `a,b` is zero, so on that residual label only one child has spectral mass. This is the fibrewise disjoint-support endpoint.

Because every fibre deficit `B_T-J_T` is nonnegative, global equality `J_i^{rec}=B_i` holds exactly when every active fibre is of one of these endpoint types. Unlike the dyadic rigidity theorem for equality in the concave Jensen cap, this equality characterization needs no Walsh-integrality argument.

### Relation to the previous Hellinger bounds
The preceding P03 report proved

\[
J_i^{\rm rec}\le\frac{2}{\ln2}M_i
\le\frac{2}{\ln2}j_i.
\]

The new theorem can be combined, not substituted blindly:

\[
\boxed{
J_i^{\rm rec}
\le\min\left\{B_i,\frac{2}{\ln2}M_i\right\}
\le\min\left\{B_i,\frac{2}{\ln2}j_i\right\}.
}
\tag{4.7}
\]

When the true hereditary cost is much smaller than its scalar influence/Hellinger envelope, (4.1) retains that cancellation automatically.

## 5. Adaptive-tree consequence: `S_T <= R_T`

Let `T` be any adaptive physical restriction/stopping tree. At an internal node `v`, let `f_v` be the restricted Boolean function, `i(v)` the queried physical coordinate, and `w_v` the cylinder probability of reaching that node. Define

\[
R_{\mathcal T}
=\sum_{v\text{ internal}}w_v B_{i(v)}(f_v),
\]

\[
S_{\mathcal T}
=\sum_{v\text{ internal}}w_v J_{i(v)}^{\rm rec}(f_v).
\]

Applying Theorem 4.1 at every node and summing with nonnegative weights gives

\[
\boxed{S_{\mathcal T}\le R_{\mathcal T}.}
\tag{5.1}
\]

The prior sharp recombination theorem remains useful simultaneously. If

\[
J_{\mathcal T}=\sum_vw_vj_{i(v)}(f_v),
\]
then

\[
\boxed{
S_{\mathcal T}
\le\min\left\{R_{\mathcal T},\frac2{\ln2}J_{\mathcal T}\right\}.
}
\tag{5.2}
\]

The tree entropy identity already proved in P03 is

\[
H(f)=R_{\mathcal T}+S_{\mathcal T}+H_L,
\tag{5.3}
\]
where

\[
H_L=\sum_{\ell\text{ leaf}}w_\ell H(f_\ell).
\]

Hence every stopping tree satisfies

\[
\boxed{H(f)\le2R_{\mathcal T}+H_L.}
\tag{5.4}
\]

For a full physical restriction tree all leaves are constants, so `H_L=0` and

\[
\boxed{R_{\mathcal T}\le H(f)\le2R_{\mathcal T}.}
\tag{5.5}
\]

The left inequality is just (5.3) with `S_T>=0`; the right inequality is new from (5.1).

## 6. Full FEI is equivalent, up to factor two, to hereditary allocation

For nonconstant `f`, define the optimized full-tree allocation ratio

\[
\mathcal A(f):=\inf_{\mathcal T\text{ full}}
\frac{R_{\mathcal T}(f)}{I(f)}.
\tag{6.1}
\]

Equation (5.5) yields immediately

\[
\boxed{
\mathcal A(f)
\le\frac{H(f)}{I(f)}
\le2\mathcal A(f).
}
\tag{6.2}
\]

Thus the following two universal statements are quantitatively equivalent up to a factor two:

1. there is a finite `K` such that every Boolean function has a full physical tree with `R_T<=K I(f)`;
2. there is a finite `C` such that every Boolean function satisfies FEI `H(f)<=C I(f)`.

Indeed, (1) gives (2) with `C=2K` by (5.4), while (2) gives `R_T<=H(f)<=CI(f)` for **every** full tree by (5.3).

This should be read carefully. It does **not** prove that `K` exists. It removes the need for a separate universal payment theorem for `S_T`: once `R_T` is paid, dependent-branch recombination costs at most the same amount.

It also does not revive the previously refuted root-level pointwise converse involving `sum_i B_i`. Here `R_T` is a weighted sum along an adaptive full restriction tree. The failed statement and (6.2) are different assertions.

## 7. Sharper stopping-tree transfer

Let

\[
Q_{\mathcal T}=\sum_vw_v\operatorname{Inf}_{i(v)}(f_v)
\]
be the queried physical influence budget and

\[
I_L=\sum_\ell w_\ell I(f_\ell).
\]
The exact influence budget is

\[
Q_{\mathcal T}+I_L=I(f).
\tag{7.1}
\]

Suppose a stopping tree satisfies

\[
R_{\mathcal T}\le KQ_{\mathcal T}
\tag{7.2}
\]

and every stopping leaf satisfies

\[
H(f_\ell)\le C_0 I(f_\ell).
\tag{7.3}
\]

The old recombination payment gives

\[
S_{\mathcal T}\le\frac2{\ln2}J_{\mathcal T}
\le\frac2{\ln2}Q_{\mathcal T},
\]
while the new theorem gives `S_T<=R_T<=KQ_T`. Hence

\[
S_{\mathcal T}
\le\min\left\{K,\frac2{\ln2}\right\}Q_{\mathcal T}.
\]
Using (5.3), (7.1)--(7.3),

\[
H(f)
\le
\left[K+\min\left\{K,\frac2{\ln2}\right\}\right]Q_{\mathcal T}
+C_0I_L.
\]
Therefore

\[
\boxed{
H(f)
\le
\max\left\{
C_0,
K+\min\left(K,\frac2{\ln2}\right)
\right\}I(f).
}
\tag{7.4}
\]

The previous generic transfer had the internal-node coefficient `K+2/ln2`. Equation (7.4) is strictly better whenever `K<2/ln2`.

### Concrete inherited restricted improvement
Companion NM13-02 has an existing hereditary constant for one-point perturbations of arbitrary quadratic phases,

\[
C_\chi=2+\frac1{\sqrt e\ln2}
=2.875038774914527\ldots .
\]

Since

\[
C_\chi<\frac2{\ln2}=2.885390081777926\ldots,
\]
Theorem 4.1 changes the generic direct conversion for that hereditary certificate from

\[
C_\chi+\frac2{\ln2}
=5.760428856692455\ldots
\]

to

\[
\boxed{2C_\chi=5.750077549829055\ldots .}
\tag{7.5}
\]

This small numerical improvement is **restricted** and is not the principal result of the run. The principal gain is the universal mechanism (4.1)--(6.2).

## 8. Sharpness

The coefficient one in (4.1) is optimal. Consider the two-variable function whose two restrictions in a control coordinate `t` are

\[
f^{t=0}(x)=1,
\qquad
f^{t=1}(x)=(-1)^x.
\tag{8.1}
\]

Equivalently, in truth-table order `(t,x)=(0,0),(1,0),(0,1),(1,1)`,

\[
f=(1,1,1,-1).
\]

At the control split, the two child spectral laws are point masses on disjoint residual Fourier labels. Thus the queried spectral bit is perfectly uncertain given the residual label in the parent representation and the child label is perfectly identifiable in recombination:

\[
B_t=1,
\qquad
J_t^{\rm rec}=1.
\tag{8.2}
\]

The parent has four equal squared Fourier coefficients, hence

\[
H(f)=2.
\]
Its total influence is `I(f)=1`. Completing the restriction tree by querying the remaining variable after `t`, the descendants are characters/constants and contribute no further entropy decrement. Therefore

\[
R_{\mathcal T}=1,
\qquad
S_{\mathcal T}=1,
\qquad
H(f)=2R_{\mathcal T}.
\tag{8.3}
\]

So neither (4.1) nor the factor two in (5.5) can be improved universally by a smaller constant. The earlier one-point-defect calculations are also asymptotically consistent with `H/R -> 2` on their canonical full trees.

## 9. Executed sanity checker

A new checker was executed before persistence. It exhaustively enumerated **all 65,812 Boolean functions in dimensions 1 through 4** and **all 262,948 physical coordinate splits**. For each split it independently computed Walsh coefficients and checked:

- the exact identity `Delta_iH=B_i+JS_i`;
- `JS_i<=B_i`;
- the ratio `JS_i/B_i` on positive-cost cases;
- the endpoint characterization of numerical equality;
- the controlled-character sharpness witness;
- the inherited one-point-quadratic constant conversion.

Actual output:

- maximum `JS_i-B_i`: `0.0`;
- maximum `JS_i/B_i` where `B_i>0`: `1.0`;
- maximum `|Delta_iH-(B_i+JS_i)|`: `6.661338147750939e-16`;
- equality cases containing an intermediate fibre `0<t<1/2`: `0`;
- sharp witness: `B=1`, `JS=1`, `H=2`, `I=1`;
- status: `PASS`.

These are finite self-checks, not independent audits or a proof of unrestricted FEI. The theorem itself is analytic in Sections 2--4.

Preserved checker:

`proofnet24/P03-fei/runs/2026-09-20/2026-09-20T14-29-48+0300__check_recombination_dominated.py`

- creation commit `d396934048bc061ecebed60a1657fd9fe808bfaa`
- Git blob `e73ec276eefc7df7793b5994386b67ae46def3ca`
- local executed-file SHA-256 `83d31ab6bc09926584f844e311e32afae2dd7cf46ae186efd31a6df7c7b76275`

Preserved actual output:

`proofnet24/P03-fei/runs/2026-09-20/2026-09-20T14-29-48+0300__recombination_dominated_check.json`

- creation commit `1b49dc9c2b35b7306f9fa468d382bed0170d902e`
- Git blob `7e6356c6209808f7a8f4875fd27385229a8c85e7`
- local executed-output SHA-256 `6d219b09ce6a29362c42c84fd24810fc758af5b807fbd87362f021dbc0c338e0`

## 10. Failed-route history preserved

Nothing here revives the previously refuted or retired shortcuts. In particular:

- no all-constant pointwise resolvent inequality is used;
- no false pointwise erasure shortcut is used;
- no fixed-coefficient affine-drift payment is used;
- no Han absolute-overlap selector is used;
- no derivative-degree scalar schedule is used;
- no blind curvature/query ratio is used;
- no fixed `s<2` Renyi potential is used;
- no root-level replacement of joint conditional entropies by a payable sum of marginals is used;
- no fresh controls are appended.

The previous theorem that `2/ln2` is sharp for paying recombination **by folded queried influence alone** remains correct. The new theorem does not contradict it: the sharp comparison variable here is the true hereditary allocation `B_i`, not `j_i`.

## 11. Residual obstruction and next attack

The live full-scope obstruction is now simpler and sharper:

\[
\boxed{
\text{Find a universal }K<\infty\text{ such that every Boolean }f
\text{ has a full physical tree }\mathcal T
\text{ with }R_{\mathcal T}\le K I(f).
}
\tag{11.1}
\]

By (6.2), this is equivalent to FEI up to factor two. There is no longer a need to develop an independent universal `S_T` payment before attacking (11.1).

The most nonredundant next P03 attack is therefore on the **exact profile-level allocation** itself on the signed-translation-rigid connected high-degree core. Two mechanisms should be combined rather than scalarized:

1. exact/approximate isospectral fibres, where the Hellinger/KL profile makes `B_i` small;
2. NM13-02 oblique-derivative quotient peeling, where approximate signed translations physically pay `B_i` by transverse derivative influence.

A decisive next theorem would show that after all zero-cost signed symmetries are quotiented, some physical query has either a bounded profile-level `B_i/j_i` ratio or an oblique quotient payment whose total lifetime is influence-summable. A decisive obstruction would be a signed-translation-rigid family for which every adaptive full tree has `R_T/I -> infinity`; by (6.2) such a family would actually refute FEI, so any claimed construction must be treated with correspondingly high scrutiny.

Further attempts to lower the standalone recombination coefficient, or to replace `B_i` by a previously failed marginal/degree/curvature scalar surrogate, are no longer the priority.

## 12. Source-level versus mechanism-level accounting

The source problem has not moved: unrestricted FEI is still open and no universal constant has been proved. The finite atlas is unchanged. The mechanism has moved substantially: dependent-branch recombination, previously budgeted separately by `2/ln2` times queried folded influence, is universally dominated by the exact hereditary allocation at the same node. This turns the project target from a two-ledger `R+S` closure problem into a single-ledger hereditary-allocation problem, at an unavoidable factor-two conversion.

Publication novelty/priority is **UNVERIFIED**. Independent review is pending. The executed finite checker is supporting evidence only.

```yaml
ledger_delta:
  parent_problem: "T01 Friedgut-Kalai Fourier entropy-influence"
  owner: "P03"
  companion: "NM13-02"
  source_status_before: "OPEN"
  source_status_after: "OPEN"
  universal_constant_before: "UNKNOWN"
  universal_constant_after: "UNKNOWN"
  native_finite_atlas_before: 6
  native_finite_atlas_after: 6
  theorem_scope: "all Boolean functions, every physical coordinate, every adaptive physical restriction tree"
  mechanism_gain: "proved J_i^rec <= B_i pointwise; hence S_T <= R_T and R_T <= H <= 2 R_T on every full tree"
  named_obstruction_removed: "dependent-branch recombination as a separate universal payment problem"
  logical_reduction: "full FEI is equivalent up to factor two to a universal hereditary allocation bound R_T <= K I"
  sharpness: "coefficient 1 in J_i^rec <= B_i and factor 2 in H <= 2R_T are attained by a two-variable controlled-character example"
  restricted_constant_gain: "existing one-point quadratic-phase conversion 5.760428856692455 -> 5.750077549829055"
  fresh_variables_used: false
  failed_routes_preserved:
    - "pointwise erasure shortcut"
    - "all-constant resolvent/interpolation"
    - "fixed-coefficient affine drift"
    - "Han absolute-overlap selector"
    - "derivative-degree scalar schedule"
    - "blind curvature/query payment"
    - "fixed-s<2 Renyi payment"
    - "root marginal-entropy replacement"
  residual_obstruction: "uniform full-tree hereditary allocation R_T <= K I(f) on the remaining signed-translation-rigid high-degree core"
  checker_status: "PASS"
  checker_coverage: "65,812 Boolean functions through dimension 4; 262,948 coordinate splits"
  independent_review: "PENDING"
  publication_priority: "UNVERIFIED"
```

**End of complete run report.**
