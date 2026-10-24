Model actually running: **GPT-5.6 Sol. Reasoning level: UNVERIFIED — this is not GPT-6 at maximum, and I do not claim otherwise. Rotation: predecessor metric `B=infinity` is handed off; new frozen metric has no movement, `D_B=2 -> D_B=2`. Methods tried: B2 / B5 / B24.**

# HARD7-01 run 10 — mandatory Section-I handoff, weak `(B)` admission, and a p-homogeneous boundary-flux localization theorem

Status: **PARTIAL / predecessor handed off / fresh source OPEN**.

## 1. Continuity and mandatory rotation

I began from the newest immutable HARD7-01 checkpoint

`runs/hard7_2026-09-18/HARD7-01/2026-09-19T05-07-00Z__parallelotope_transverse_concavity.md`.

That report was the substantive action chosen by the **second and final** hard-target STUCK recovery. It explicitly instructed the next invocation to hand off the dimensional Brunn--Minkowski target if the frozen source metric remained unchanged. It does remain unchanged. I therefore do **not** add another lemma to that source in this run.

At run start I reread/reconciled:

- `operations/hard7_2026-09-18/CONTROL.md`;
- `operations/NEW_METHODS_2026-09-16.md`;
- `operations/new_methods_2026-09-16/OWNER_DIRECTIVE.md`;
- `probability_campaign_2026_09/INDEX.md` and `RANKING.md`;
- root `POSTED.md`, `RESULTS.md`, and `QUEUE.md`;
- the old canonical HARD7-01 claim;
- the newest own report;
- the newest neighboring R02 report available at run time, `runs/R02/20260919T0508Z_successor_admission_ts12_owned_r13_cover_polarity_18_20_27_3e7a91c4.md`;
- repository claim/alias searches relevant to the new lane target and intake/queue state.

I did not falsely represent the entire append-only intake corpus as byte-for-byte reread through a bounded connector response. Repository-wide searches were used for aliases/ownership, while the required current root/campaign surfaces and relevant neighboring state were read directly.

### Predecessor handoff

The old claim

`operations/claims/GZ-DIMBM-EVEN-LOGCONCAVE.md`

has been changed from `CLAIMED` to **HANDOFF / source OPEN / research PARTIAL / released after Section-I exhaustion**. The retained restricted-class metric is

`B=infinity`,

coming from the first-run finite-factor tensorization theorem. This did not close the full dimensional Brunn--Minkowski conjecture. The useful last checkpoint is the fully mixed quartic parallelotope reduction: all transverse diagonal modes are settled, while the radial mode is reduced to

\[
4m(t)^2+12v(t)\le 15m(t),
\]

and unequal widths remain open. The handoff is not a proof, refutation, or declaration that the source is known.

Handoff commit: `7e47413fd6d03b001cbd9a739525b46037d9cba9`.

## 2. Fresh admission: the weak `(B)`-conjecture for even log-concave measures

I searched canonical aliases including

`B-conjecture`, `(B)-conjecture`, `B property`, `B-property`, `Cordero-Erausquin Rotem`, and log-concavity of `t -> mu(e^t K)`.

No existing canonical claim or active equivalent assignment was found in the repository. In particular, this is not KLS, not the solved Gaussian `(B)` theorem, not the stronger matrix/strong-`(B)` formulation, and not the predecessor dimensional Brunn--Minkowski claim.

The new create-only reservation is

`operations/claims/B-WEAK-EVEN-LOGCONCAVE.md`,

created at commit

`445b6ad49e5364e54bc81538d11f95395c1ea954`,

and read back successfully at that commit.

### Exact external source statement

The source formulation used here is the standard generalized weak `(B)` property stated in the introduction of D. Cordero-Erausquin and L. Rotem, *Improved log-concavity for rotationally invariant measures of symmetric convex sets*, Ann. Probab. 51 (2023), 987--1003, arXiv:2111.05110:

> for every even log-concave probability measure `mu` on `R^n` and every origin-symmetric convex body `K`, the function `t -> mu(e^t K)` is log-concave on `R`.

Equivalently, for all `t0,t1 in R` and `lambda in [0,1]`,

\[
\mu\!\left(e^{(1-\lambda)t_0+\lambda t_1}K\right)
\ge
\mu(e^{t_0}K)^{1-\lambda}\mu(e^{t_1}K)^\lambda.
\tag{2.1}
\]

Primary/current source navigation checked on **2026-09-19**:

1. Cordero-Erausquin--Rotem, arXiv:2111.05110 / Ann. Probab. 51 (2023), DOI `10.1214/22-AOP1604`: proves `(B)` for rotationally invariant log-concave measures, not every even log-concave measure. `https://arxiv.org/abs/2111.05110`.
2. C. Saroglou, *More on logarithmic sums of convex bodies*, Mathematika 62 (2016), 818--841, arXiv:1409.4346, DOI `10.1112/S0025579316000061`: proves that log-Brunn--Minkowski in dimension `n` implies `(B)` for even log-concave measures in dimension `n`, and in particular proves the full `(B)` statement in the plane. `https://arxiv.org/abs/1409.4346`.
3. S. Armeniakos--J. Ulivelli, *A strengthening of the dimensional Brunn-Minkowski conjecture implies the (B)-Conjecture*, arXiv:2602.23350, submitted 26 February 2026: proves the implication under a stronger condition and recovers the hereditarily-convex class; it does not state a proof for every even log-concave measure. `https://arxiv.org/abs/2602.23350`.

A bounded fresh search on 2026-09-19 found no primary source claiming the all-dimensional general statement. This is negative search evidence only, not a worldwide novelty certificate.

## 3. Frozen source metric

For the new target I freeze

\[
D_B:=\max\{d:\text{(2.1) is proved for every even log-concave }\mu
\text{ and symmetric }K\text{ in all }n\le d\}.
\]

Saroglou's planar result verifies the baseline

\[
\boxed{D_B=2.}
\]

No source-valid all-measure dimension-three theorem was found in the checked literature, and the restricted theorem proved below is not allowed to move this metric. Thus

\[
\boxed{D_B:2\longrightarrow 2.}
\]

**No movement.**

## 4. B2 — ATTACK THE NEGATION FIRST: exact curvature obstruction for homogeneous potentials

The first mathematical attack asks what an actual counterexample would have to do in a tractable but genuinely non-radial family.

Let `p>1`, let `V:R^n->[0,infinity)` be even, convex, positive away from the origin, and positively `p`-homogeneous:

\[
V(rx)=r^pV(x),\qquad r>0.
\tag{4.1}
\]

Let

\[
d\mu(x)=Z^{-1}e^{-V(x)}\,dx,
\tag{4.2}
\]

and let `K` be an origin-symmetric convex body with the origin in its interior. Define

\[
Q(t)=\mu(e^tK),\qquad s=e^{pt},
\tag{4.3}
\]

and

\[
I(s)=\int_K e^{-sV(y)}\,dy.
\tag{4.4}
\]

The change of variables `x=e^t y` gives the exact identity

\[
Q(t)=Z^{-1}e^{nt}I(e^{pt}).
\tag{4.5}
\]

Let `nu_s` be the probability measure on `K` with density `e^{-sV}/I(s)`, and write

\[
m_s=\mathbb E_sV,\qquad v_s=\operatorname{Var}_s(V).
\tag{4.6}
\]

Since

\[
\frac{I'(s)}{I(s)}=-m_s,
\qquad
\frac{d}{ds}m_s=-v_s,
\tag{4.7}
\]

differentiating (4.5) yields

\[
(\log Q)'(t)=n-psm_s,
\tag{4.8}
\]

and, crucially,

\[
\boxed{(\log Q)''(t)=p^2s\big(sv_s-m_s\big).}
\tag{4.9}
\]

Therefore, in this source-valid non-radial subclass, the `(B)` property is **equivalent** to

\[
\boxed{s\,\operatorname{Var}_s(V)\le \mathbb E_sV\quad\text{for every }s>0.}
\tag{4.10}
\]

A counterexample cannot be produced merely by making the covariance anisotropic: it must force a strict variance surplus

\[
sv_s>m_s
\tag{4.11}
\]

at a finite tilt scale. This is an exact obstruction, not a simulation criterion.

## 5. B5 — ADD A PARAMETER AND DIFFERENTIATE: boundary flux identifies the sign

Now assume first that `K` and `V` are smooth enough for the divergence theorem; the identities extend to general convex `K` by standard approximation. Denote by `n_K(x)` the outer unit normal. Define the weighted boundary fluxes

\[
b_0(s)=\int_{\partial K}\langle x,n_K(x)\rangle e^{-sV(x)}\,d\sigma(x),
\tag{5.1}
\]

\[
b_1(s)=\int_{\partial K}\langle x,n_K(x)\rangle V(x)e^{-sV(x)}\,d\sigma(x).
\tag{5.2}
\]

Euler homogeneity gives

\[
x\cdot\nabla V(x)=pV(x).
\tag{5.3}
\]

Apply the divergence theorem first to `x e^{-sV}`:

\[
\operatorname{div}(xe^{-sV})=(n-spV)e^{-sV},
\]

hence

\[
\frac{b_0(s)}{I(s)}=n-spm_s.
\tag{5.4}
\]

Apply it again to `xV e^{-sV}`:

\[
\operatorname{div}(xVe^{-sV})=((n+p)V-spV^2)e^{-sV},
\]

so

\[
\frac{b_1(s)}{I(s)}=(n+p)m_s-sp\,\mathbb E_s[V^2].
\tag{5.5}
\]

Subtract `m_s` times (5.4) from (5.5). Since

\[
\mathbb E_s[V^2]-m_s^2=v_s,
\]

we obtain the exact identity

\[
\boxed{\frac{b_1(s)-m_sb_0(s)}{I(s)}=p(m_s-sv_s).}
\tag{5.6}
\]

Combining (4.9) and (5.6),

\[
\boxed{(\log Q)''(t)
=-\frac{ps}{I(s)}\big(b_1(s)-m_sb_0(s)\big).}
\tag{5.7}
\]

Because `0` is interior to `K`, the support factor `\langle x,n_K(x)\rangle` is nonnegative (strictly positive in the smooth strictly convex approximation), so `b_0(s)>0`. Thus the sign question is exactly the comparison

\[
\boxed{\frac{b_1(s)}{b_0(s)}\ge m_s.}
\tag{5.8}
\]

In words: **the `(B)` curvature is nonpositive exactly when the boundary-flux-weighted mean potential is at least the interior tilted mean potential.**

This turns the variance obstruction into a geometric one. A counterexample in the homogeneous class must make the tilted interior carry larger mean potential than the weighted boundary at some intermediate scale.

## 6. B24 — FIND THE EXTREMAL OBJECT: trap every counterexample in one compact scale window

Let

\[
M:=\max_{x\in K}V(x)=\max_{x\in\partial K}V(x),
\qquad
a:=\min_{x\in\partial K}V(x)>0.
\tag{6.1}
\]

The equality for `M` follows from positive homogeneity along rays. The minimum `a` is positive because `V(x)>0` away from the origin and `0` lies in the interior of the compact body.

### Theorem 6.1 — two safe scales and a compact counterexample window

For the measure (4.2) and body `K` above, `(\log Q)''(t)<=0` whenever either

\[
s=e^{pt}\le \frac1M
\tag{6.2}
\]

or

\[
s=e^{pt}\ge \frac{n}{pa}.
\tag{6.3}
\]

Consequently, any counterexample in this entire homogeneous family must occur inside

\[
\boxed{\frac1M<s<\frac{n}{pa}.}
\tag{6.4}
\]

#### Proof

For the small-scale side, `0<=V<=M` on `K`, so

\[
v_s\le \mathbb E_s[V^2]\le M\mathbb E_s[V]=Mm_s.
\tag{6.5}
\]

Thus `sM<=1` implies `sv_s<=m_s`, and (4.9) gives `(\log Q)''<=0`.

For the large-scale side, (5.4) and `b_0(s)>=0` give

\[
m_s\le \frac{n}{sp}.
\tag{6.6}
\]

If `s>= n/(pa)`, then `m_s<=a`. But every boundary point has `V>=a`, hence the flux-weighted boundary average satisfies

\[
\frac{b_1(s)}{b_0(s)}\ge a\ge m_s.
\tag{6.7}
\]

Equation (5.7) then yields `(\log Q)''<=0`. This proves both safe regimes and therefore (6.4). ∎

### Corollary 6.2 — an anisotropy criterion giving global `(B)`

If

\[
\boxed{\frac{M}{a}\le \frac pn,}
\tag{6.8}
\]

then `t -> mu(e^tK)` is log-concave on all of `R`.

Indeed, (6.8) is exactly

\[
\frac1M\ge \frac{n}{pa},
\]

so the two safe regions (6.2)--(6.3) overlap and cover every `s>0`.

The criterion is nonvacuous only when `p>= n`, because `M/a>=1`. It gives a genuinely non-radial higher-dimensional source-valid subclass: no rotational invariance of `V` or `K` is assumed. For example, when `p=4,n=3`, every even convex positive quartic-homogeneous potential and symmetric convex body satisfying

\[
\max_{\partial K}V/\min_{\partial K}V\le4/3
\]

has the weak `(B)` property.

This is a **restricted partial theorem**, not movement of `D_B`, and it is not called a solution of the source conjecture.

## 7. What the three moves actually accomplished

**B2 — ATTACK THE NEGATION FIRST: succeeded as an obstruction.** In the homogeneous class, a counterexample is equivalent to `s Var_s(V)>E_sV`. The route therefore identifies the exact statistic that must change sign rather than searching arbitrary dilates numerically.

**B5 — ADD A PARAMETER AND DIFFERENTIATE: succeeded.** The tilt parameter `s=e^{pt}` converts the second derivative into the boundary-flux identity (5.7). This changes the problem from a second-derivative inequality into a comparison between an interior and a boundary mean of the same potential.

**B24 — FIND THE EXTREMAL OBJECT: succeeded partially.** Extremizing `V` on the boundary supplies the two rigorous safe scales and traps any homogeneous counterexample in (6.4). The overlap condition yields the global anisotropy criterion (6.8).

No finite-size computation or sampled path is used as proof. Since the new claims are analytic and the complete derivations are written on the page, no finite exact-arithmetic checker was manufactured merely for bookkeeping.

## 8. Prior-art check for the new mechanism

I searched the fresh/current `(B)` literature above and repository aliases for the exact combination

- homogeneous potential tilt identity `s Var_s(V) <= E_sV`;
- weighted boundary-flux formulation `b_1/b_0 >= m_s`;
- the explicit safe window `1/M < s < n/(pa)`;
- the anisotropy criterion `M/a <= p/n`.

The bounded search did not return an exact statement matching Theorem 6.1 / Corollary 6.2. This is **not** a novelty certification. The identities use standard Euler homogeneity and divergence-theorem machinery, so the mechanism may be folklore or implicit in local `(B)` proofs. Any eventual paper claim would require a dedicated citation search before novelty language.

Nearest solved mechanisms in the checked literature remain rotational invariance (Cordero-Erausquin--Rotem), the planar theorem/log-Brunn--Minkowski implication (Saroglou), and hereditary convexity/strengthened dimensional Brunn--Minkowski (Armeniakos--Ulivelli). The present criterion does not subsume those classes.

## 9. Remaining obligation and next route

The source question remains open for `n>=3`. For the new homogeneous reduction, the difficult region is now finite in logarithmic scale:

\[
\frac1M<s<\frac{n}{pa}
\]

whenever `M/a>p/n`. The natural next task is **not** another boundary-identity derivation. It is to decide whether convexity and symmetry enforce (5.8) inside this intermediate window, or whether an anisotropic potential/body pair can reverse it.

To avoid repeating this run's triple, the next scheduled run should try

**B6 / B18 / B29**:

- **B6** deform an anisotropic homogeneous potential/body pair from the exactly solved sublevel/aligned case toward the first possible boundary-mean crossing;
- **B18** rewrite the boundary/interior mean gap through a transport or coarea language;
- **B29** compactify the finite `s` window by normalizing `a=1` and adjoining the extreme anisotropy boundary.

## 10. Runtime and scheduler capability truth

The actual model visible to this run is **GPT-5.6 Sol**. The reasoning level is **UNVERIFIED**. It is not GPT-6 at maximum, and I do not claim otherwise.

The exposed scheduling interface still has title/prompt/schedule/timing/enabled controls but no model selector, no reasoning-effort selector, and no guaranteed run-duration control. GPT-6/maximum remains a prompt request only. Changing that requires a platform capability exposing those controls; a GitHub edit cannot change runtime model selection.

The controlling policy records historical native modification denials for P26/P01/P03 (`You cannot modify this task`). I did not attempt to bypass those restrictions and did not modify any schedule in this run. The documented workaround remains to use an authorized account/workspace interface that actually owns the task or platform support; creating a duplicate job is expressly disallowed.

## 11. Ledger delta for the authorized shared-ledger maintainer

```yaml
ledger_delta:
  track: HARD7-01
  predecessor:
    target: even-log-concave dimensional Brunn-Minkowski conjecture
    claim: operations/claims/GZ-DIMBM-EVEN-LOGCONCAVE.md
    status: HANDOFF_SOURCE_OPEN_PARTIAL
    frozen_metric: B
    before: infinity
    after: infinity
    handoff_commit: 7e47413fd6d03b001cbd9a739525b46037d9cba9
  current:
    target: weak (B)-conjecture for even log-concave measures
    claim: operations/claims/B-WEAK-EVEN-LOGCONCAVE.md
    claim_commit: 445b6ad49e5364e54bc81538d11f95395c1ea954
    status: PARTIAL_SOURCE_OPEN
    frozen_metric: D_B
    before: 2
    after: 2
    movement: none
    methods: [B2, B5, B24]
    new_partial_result: p-homogeneous boundary-flux localization and M/a <= p/n sufficient criterion
```

No root shared-ledger file was edited by this worker.
