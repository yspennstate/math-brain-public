Model actually running: **GPT-5.6 Sol. Reasoning level: UNVERIFIED — this is not GPT-6 at maximum, and I do not claim otherwise. No source-metric movement: `D_B=2 -> D_B=2`. Methods tried: B1 / B3 / B6.**

# HARD7-01 run 11 — reverse hazard, radial-score flux, and a nonhomogeneous sufficient class for weak `(B)`

Status: **PARTIAL / source OPEN**.

## 1. Continuity, source sentinel, and ownership

This run resumes the admitted target from

`runs/hard7_2026-09-18/HARD7-01/2026-09-19T06-01-14Z__handoff_weakB_admission_boundary_flux.md`

at commit

`6ccad840b072c61df3370eb468b873e3cf9e9939`.

The canonical create-only claim remains

`operations/claims/B-WEAK-EVEN-LOGCONCAVE.md`,

owned by HARD7-01 and marked `CLAIMED / source OPEN / research PARTIAL only`. No competing owner or equivalent active claim was found in the repository alias search this run.

At run start I reread/reconciled the controlling files

- `operations/hard7_2026-09-18/CONTROL.md`,
- `operations/NEW_METHODS_2026-09-16.md`,
- `operations/new_methods_2026-09-16/OWNER_DIRECTIVE.md`,
- `probability_campaign_2026_09/INDEX.md`,
- `probability_campaign_2026_09/RANKING.md`,
- root `POSTED.md`, `RESULTS.md`, and `QUEUE.md`,
- the canonical weak-`(B)` claim,
- the newest HARD7-01 checkpoint,
- the newest materially neighboring R02 report available at run time,

and reran repository-wide alias/ownership searches for `(B)-conjecture`, `B-conjecture`, and `D_B`. Those searches include indexed intake material; no equivalent intake assignment or canonical claim collision was recovered. I do not represent the very large append-only intake corpus as byte-for-byte reread through a bounded connector response.

### Exact source statement retained

For every integer `n>=1`, every even log-concave probability measure `mu` on `R^n`, and every origin-symmetric convex body `K`, prove that

\[
t\longmapsto \mu(e^tK)
\]

is log-concave on `R`.

The frozen source metric remains

\[
D_B:=\max\{d:\text{the exact statement is proved for every such }(\mu,K)
\text{ in every }n\le d\}.
\]

Saroglou's planar theorem gives the verified baseline `D_B=2`.

### Fresh current-literature screen — 2026-09-19

The bounded fresh screen checked the exact weak statement and its nearby aliases against the current primary/arXiv literature. The relevant newest papers found were:

1. D. Cordero-Erausquin and L. Rotem, *Improved log-concavity for rotationally invariant measures of symmetric convex sets*, Ann. Probab. 51 (2023), arXiv:2111.05110. This proves `(B)` for rotationally invariant log-concave measures, not all even log-concave measures.
2. C. Saroglou, *More on logarithmic sums of convex bodies*, Mathematika 62 (2016), arXiv:1409.4346. This gives the log-Brunn--Minkowski implication and the full planar case.
3. D. Cordero-Erausquin and A. Eskenazis, *Concavity principles for weighted marginals*, arXiv:2506.16941 (2025). This develops weighted-marginal concavity principles and recovers substantial structured classes; it does not claim the unrestricted all-dimensional weak conjecture.
4. S. Armeniakos and J. Ulivelli, *A strengthening of the dimensional Brunn-Minkowski conjecture implies the (B)-Conjecture*, arXiv:2602.23350, submitted 2026-02-26. It proves a stronger-dimensional-BM implication and the hereditarily-convex class, not the full conjecture.
5. E. Putterman, *Sharp stability for the (B)-theorem*, arXiv:2608.08472, submitted 2026-08-09. This is a sharp stability theorem for the Gaussian `(B)` theorem and strong/functional variants; it does not prove weak `(B)` for every even log-concave measure.

No current primary paper found in this bounded search claimed the full all-dimensional even-log-concave statement. This is **bounded negative evidence only**, not an exhaustive worldwide openness or novelty certificate.

The source metric therefore starts and ends this run at

\[
\boxed{D_B:2\longrightarrow2.}
\]

**No movement.** This is the second consecutive no-movement run on the newly admitted weak-`(B)` target; it does not yet trigger Section I. The restricted theorem below is not credited as `D_B=3`.

## 2. B1 — CHANGE THE CATEGORY: weak `(B)` is reverse-hazard monotonicity, not shell-density log-concavity

Let `X~mu` and let `||.||_K` be the Minkowski functional of the symmetric convex body `K`. Define the scalar random variable

\[
U:=\log\|X\|_K.
\]

Then its distribution function is exactly

\[
F_U(t)=\Pr(U\le t)=\mu(e^tK)=:Q(t).
\tag{2.1}
\]

Thus weak `(B)` is the one-dimensional statement that the **CDF** of `U` is log-concave. At differentiability points, writing `q=Q'`, this is equivalent to

\[
h_-(t):=\frac{q(t)}{Q(t)}=(\log Q)'(t)
\tag{2.2}
\]

being nonincreasing. In reliability terminology `h_-` is the reverse hazard rate. This is the right scalar object.

A tempting stronger program would be to prove that the shell density `q` itself is log-concave. That route is false even in a two-dimensional example where the source theorem is known.

### Exact obstruction to shell-density log-concavity

Let

\[
K=[-1,1]^2,
\qquad
\mu=\operatorname{Unif}([-a,a]\times[-b,b]),
\qquad 0<a<b.
\]

Put `r=e^t`. Direct intersection-area calculation gives

\[
Q(t)=\mu(rK)=
\begin{cases}
\dfrac{r^2}{ab},&0<r\le a,\\[4pt]
\dfrac r b,&a\le r\le b,\\[4pt]
1,&r\ge b.
\end{cases}
\tag{2.3}
\]

Hence away from the two breakpoints

\[
q(t)=Q'(t)=
\begin{cases}
\dfrac{2r^2}{ab},&r<a,\\[4pt]
\dfrac r b,&a<r<b,\\[4pt]
0,&r>b.
\end{cases}
\tag{2.4}
\]

At `t=log a`, the one-sided values jump from `2a/b` to `a/b`. Therefore `q` is not log-concave: a positive log-concave function is continuous on the interior of its support.

But the reverse hazard is exactly

\[
\frac{q}{Q}=
\begin{cases}
2,&r<a,\\
1,&a<r<b,\\
0,&r>b,
\end{cases}
\tag{2.5}
\]

which is nonincreasing. So the source conclusion holds perfectly while shell-density log-concavity fails.

**Outcome B1.** The category change isolates a proof invariant that is exactly equivalent to the source: prove monotonicity of the reverse hazard of `log ||X||_K`. It also rigorously kills a strictly stronger shell-density route before effort is spent on it. No finite simulation is involved.

## 3. The radial score: an exact curvature formula for general smooth log-concave potentials

The previous run exploited positive homogeneity. The next step removes homogeneity completely.

Assume for this section that

\[
d\mu(x)=Z^{-1}e^{-V(x)}\,dx,
\]

where `V in C^2(R^n)` is even, convex and coercive, and that `K` is a smooth origin-symmetric convex body with `0` in its interior. Define the radial score and radial acceleration

\[
A(x):=\langle x,\nabla V(x)\rangle,
\tag{3.1}
\]

\[
C(x):=\langle x,\nabla A(x)\rangle
      =A(x)+x^T\nabla^2V(x)x.
\tag{3.2}
\]

Even convexity gives `V(0)=min V` after subtracting an irrelevant constant, hence

\[
A(x)\ge0,
\qquad
C(x)\ge A(x)\ge0.
\tag{3.3}
\]

Let

\[
Q(t)=\mu(e^tK),
\]

and let `nu_t` denote the probability measure on the fixed body `K` with density proportional to

\[
y\mapsto e^{-V(e^ty)}.
\]

Changing variables `x=e^ty` yields

\[
\log Q(t)=nt+\log\int_K e^{-V(e^ty)}dy-\log Z.
\tag{3.4}
\]

Differentiating exactly,

\[
(\log Q)'(t)=n-\mathbb E_t A,
\tag{3.5}
\]

and because

\[
\frac d{dt}\mathbb E_t A
=\mathbb E_t C-\operatorname{Var}_t(A),
\tag{3.6}
\]

we obtain

\[
\boxed{
(\log Q)''(t)
=\operatorname{Var}_t(A)-\mathbb E_t C.
}
\tag{3.7}
\]

Thus the exact weak-`(B)` obstruction for a general smooth potential is no longer a variance bound for `V`; it is

\[
\boxed{
\operatorname{Var}_t(A)>\mathbb E_t C.
}
\tag{3.8}
\]

This is the nonhomogeneous analogue of the previous run's `s Var(V)>E V` obstruction.

### Boundary dual of the radial-score criterion

Fix `D=e^tK`, let

\[
I_D:=\int_D e^{-V(x)}dx,
\qquad
m_D:=\frac1{I_D}\int_D A(x)e^{-V(x)}dx,
\]

and define

\[
b_0(D):=\int_{\partial D}\langle x,n_D(x)\rangle e^{-V(x)}d\sigma(x),
\tag{3.9}
\]

\[
b_A(D):=\int_{\partial D}\langle x,n_D(x)\rangle A(x)e^{-V(x)}d\sigma(x).
\tag{3.10}
\]

Two divergence identities give

\[
\frac{b_0(D)}{I_D}=n-m_D,
\tag{3.11}
\]

and

\[
\frac{b_A(D)}{I_D}
=n m_D+\mathbb E_D C-\mathbb E_D A^2.
\tag{3.12}
\]

Subtracting `m_D` times (3.11) gives the exact dual identity

\[
\boxed{
\frac{b_A(D)-m_Db_0(D)}{I_D}
=\mathbb E_D C-\operatorname{Var}_D(A)
=-(\log Q)''(t).
}
\tag{3.13}
\]

Since `b_0(D)>0`, the source curvature condition at this scale is equivalently

\[
\boxed{
\frac{b_A(D)}{b_0(D)}\ge m_D.
}
\tag{3.14}
\]

In other words: **the boundary-flux mean of the radial score must dominate its interior mean.** Equation (3.11) also identifies the reverse hazard from B1:

\[
\boxed{
(\log Q)'(t)=\frac{b_0(e^tK)}{I_{e^tK}}.
}
\tag{3.15}
\]

So B1 and the boundary method are the same scalar mechanism in two languages.

## 4. B3 — PROVE SOMETHING STRONGER: a radial-elasticity plus angular-oscillation theorem

The identities above suggest imposing a pointwise strengthening that can feed itself across scales.

For `r>0`, write

\[
a(r):=\min_{x\in\partial(rK)}A(x),
\qquad
M(r):=\max_{x\in\partial(rK)}A(x).
\tag{4.1}
\]

### Theorem 4.1 — radial-score criterion

Assume there is a constant `kappa>0` such that

\[
C(x)\ge \kappa A(x)
\qquad\text{for every }x\ne0,
\tag{4.2}
\]

and that at every radius

\[
\boxed{
\frac{M(r)}{a(r)}\le\frac\kappa n.
}
\tag{4.3}
\]

Then

\[
t\longmapsto\mu(e^tK)
\]

is log-concave on all of `R`.

#### Proof

Fix `r>0`, set `D=rK`, and abbreviate

\[
m=\mathbb E_D A,
\qquad
M=M(r),
\qquad
a=a(r).
\]

From (4.2), along every nonzero ray `x=r theta`,

\[
\frac d{d\log r}A(r\theta)=C(r\theta)\ge\kappa A(r\theta)\ge0.
\tag{4.4}
\]

Hence `A` is nondecreasing on each ray and, because `D` is star-shaped about the origin,

\[
0\le A(x)\le M
\qquad (x\in D).
\tag{4.5}
\]

There are two cases.

**Case 1: `M<=kappa`.** Then

\[
\operatorname{Var}_D(A)
\le\mathbb E_D A^2
\le M\mathbb E_D A
\le\kappa m
\le\mathbb E_D C,
\tag{4.6}
\]

where the last step uses `C>=kappa A`. By (3.7), `(log Q)''<=0`.

**Case 2: `M>kappa`.** By (4.3),

\[
a\ge\frac{nM}{\kappa}>n.
\tag{4.7}
\]

Equation (3.11) and positivity of the boundary flux imply

\[
m\le n.
\tag{4.8}
\]

Every regular boundary point has `A>=a`, so the flux-weighted boundary mean satisfies

\[
\frac{b_A(D)}{b_0(D)}\ge a>n\ge m.
\tag{4.9}
\]

Equation (3.13) again gives `(log Q)''<=0`.

The two cases cover every `r>0`, proving the theorem. `square`

### Remarks

1. Since `M(r)/a(r)>=1`, condition (4.3) can only be nonvacuous when `kappa>=n`.
2. The theorem is not rotational: both `V` and `K` may be anisotropic.
3. The statement is strictly nonhomogeneous; no relation `V(rx)=r^pV(x)` was used.
4. The theorem is a **restricted sufficient condition**, not the unrestricted weak `(B)` conjecture and not movement of `D_B`.

**Outcome B3.** The stronger pointwise radial-elasticity hypothesis closes a full-scale argument that the raw source statement itself did not make inductive. The proof splits scales automatically according to whether the boundary radial score lies below or above `kappa`.

## 5. B6 — DEFORM TO A SOLVABLE CLASS: finite positive sums of homogeneous potentials

Theorem 4.1 immediately turns the previous run's single-degree homogeneous calculation into a genuinely nonhomogeneous class.

### Corollary 5.1 — mixed-degree homogeneous potentials

Let

\[
V=\sum_{j=1}^m V_j,
\tag{5.1}
\]

where every `V_j` is even, convex, positive away from the origin and positively homogeneous of degree `p_j`, and let

\[
p_0:=\min_j p_j.
\]

Assume

\[
p_0\ge n
\tag{5.2}
\]

and, for every `j`,

\[
\boxed{
\frac{\max_{x\in\partial K}V_j(x)}
     {\min_{x\in\partial K}V_j(x)}
\le\frac{p_0}{n}.
}
\tag{5.3}
\]

Then the probability measure

\[
d\mu=Z^{-1}e^{-V}dx
\]

has weak `(B)` for this `K`:

\[
t\mapsto\mu(e^tK)
\]

is log-concave on `R`.

#### Proof

Euler homogeneity gives

\[
A=\sum_j p_jV_j,
\qquad
C=\sum_j p_j^2V_j.
\tag{5.4}
\]

Therefore

\[
C\ge p_0 A,
\tag{5.5}
\]

so Theorem 4.1 applies with `kappa=p_0` once its angular-oscillation condition is checked.

Let

\[
m_j:=\min_{\partial K}V_j,
\qquad
M_j:=\max_{\partial K}V_j,
\qquad
\rho:=\frac{p_0}{n}.
\]

For `x=r theta`, `theta in partial K`,

\[
A(r\theta)=\sum_j p_jr^{p_j}V_j(\theta).
\]

Thus

\[
\max_{\theta\in\partial K}A(r\theta)
\le\sum_j p_jr^{p_j}M_j
\le\rho\sum_j p_jr^{p_j}m_j
\le\rho\min_{\theta\in\partial K}A(r\theta).
\tag{5.6}
\]

Hence `M(r)/a(r)<=p_0/n`, exactly (4.3). Theorem 4.1 finishes the proof. `square`

This strictly extends the previous run's single `p`-homogeneous theorem to mixtures of different homogeneity degrees. The deformation parameter is not formal: the radial score retains a one-sided differential inequality even after homogeneity is lost.

### Explicit three-dimensional nonhomogeneous anisotropic example

Take

\[
K=B_2^3,
\]

\[
A_4=\operatorname{diag}(1,1,1.1),
\qquad
A_6=\operatorname{diag}(1,1.05,1.08),
\]

and

\[
V_4(x)=(x^TA_4x)^2,
\qquad
V_6(x)=(x^TA_6x)^3,
\qquad
V=V_4+V_6.
\tag{5.7}
\]

Both summands are even convex and positive away from zero: `x -> x^TAx` is nonnegative convex and `u -> u^k` is convex nondecreasing on `[0,infinity)`.

Their spherical anisotropy ratios are exactly

\[
\frac{\max_{S^2}V_4}{\min_{S^2}V_4}=1.1^2=1.21,
\tag{5.8}
\]

and

\[
\frac{\max_{S^2}V_6}{\min_{S^2}V_6}=1.08^3=1.259712.
\tag{5.9}
\]

Here `p_0=4`, `n=3`, and

\[
1.259712<\frac43.
\]

Therefore Corollary 5.1 proves

\[
\boxed{
t\longmapsto
\frac{\int_{e^tB_2^3}e^{-[(x^TA_4x)^2+(x^TA_6x)^3]}dx}
     {\int_{\mathbb R^3}e^{-[(x^TA_4x)^2+(x^TA_6x)^3]}dx}
\text{ is log-concave.}
}
\tag{5.10}
\]

This is a fully explicit source-valid `n=3` restricted pair outside rotational invariance and outside exact homogeneity. It is **not** the full dimension-three conjecture.

**Outcome B6.** Deforming away from one exactly homogeneous potential works: a positive mixed-degree family survives because its radial score has a uniform elasticity lower bound. This yields a concrete higher-dimensional nonhomogeneous class, while honestly leaving `D_B` unchanged.

## 6. What changed mathematically

The source metric did not move:

\[
D_B=2\to2.
\]

But three genuinely different routes produced source-relevant information:

- **B1 / category change:** weak `(B)` is precisely reverse-hazard monotonicity for `log ||X||_K`; an exact rectangle example disproves the stronger shell-density-log-concavity route.
- **B3 / stronger theorem:** the general radial-score identity `(log Q)''=Var(A)-E C` plus `C>=kappa A` and the scale-wise angular ratio `M/a<=kappa/n` gives a global sufficient condition.
- **B6 / deformation:** the criterion is stable under finite positive sums of homogeneous convex potentials of different degrees, producing explicit nonhomogeneous anisotropic examples in dimension three.

No numerical sample is used as a proof, and no sufficient hypothesis is advertised as necessary.

## 7. Remaining obligation and next-method precommitment

The source-level obligation is still exactly dimension three:

\[
\forall\ \text{even log-concave }\mu\text{ on }\mathbb R^3,
\ \forall\ \text{symmetric convex }K,
\qquad
\operatorname{Var}_t(A)\le\mathbb E_t C
\tag{7.1}
\]

for every scale after smooth approximation, with `A=x dot grad V` and `C=x dot grad A` in the smooth density reduction.

The present theorem controls (7.1) only when radial elasticity dominates angular oscillation. What is still absent is a mechanism forcing the boundary radial-score mean above the interior mean **without** pointwise angular control.

Because this is only the second consecutive no-movement run on the newly admitted target, Section I is not yet invoked. If the next run again leaves `D_B` unchanged, that run may do substantive work but the following invocation must obey the owner's thinking-only STUCK protocol.

To avoid repeating this run's B1/B3/B6 triple, the next mathematical attack should use a different set, with promising candidates:

- **B11 (DUALIZE):** seek a Brascamp--Lieb/Poincare dual certificate for `Var(A)<=E C` under the truncated law;
- **B15 (BREAK SYMMETRY):** search for a genuinely angular three-dimensional extremizer rather than perturbing radial measures;
- **B30 (ONE SCALE/DIRECTION AT A TIME):** localize the boundary-score deficit to angular sectors and test whether convexity forces cancellation.

## 8. Capability honesty

The actual model exposed in this run is **GPT-5.6 Sol**. The reasoning level is **UNVERIFIED**. I therefore do not claim GPT-6 maximum.

The exposed native automation interface still supplies task title, prompt, schedule/timing, enabled state and update/list operations, but no binding model-family selector, no binding reasoning-effort selector, no authenticated per-run applied-model/applied-effort receipt, and no guaranteed execution-duration field. Thus `GPT-6 / maximum` remains prompt text only on this surface.

Making that request enforceable would require an owner-authorized product/workspace/backend scheduler surface that persists explicit model-family and reasoning-effort fields into execution routing and returns authenticated runtime attestation of the applied values.

The historical P26 `You cannot modify this task` response is an authorization/context boundary. Current repository `RESULTS.md` records that P26 was later reconciled successfully from another authorized context. The lawful workaround for any future refusal is to manage the **same native task** from its owning/authorized workspace/context or use platform support; do not duplicate the job or bypass permissions. No scheduler mutation was attempted in this run.

## 9. Status and ledger delta

Status remains **PARTIAL / source OPEN**.

```yaml
ledger_delta:
  track: HARD7-01
  canonical_claim: B-WEAK-EVEN-LOGCONCAVE
  source_status: OPEN
  research_status: PARTIAL
  metric: D_B
  before: 2
  after: 2
  movement: false
  unchanged_streak_on_current_target: 2
  methods: [B1, B3, B6]
  theorem_progress:
    - general radial-score curvature identity
    - boundary-flux dual identity
    - radial-elasticity/angular-oscillation sufficient theorem
    - mixed-degree homogeneous-potential corollary
  counterexample_progress:
    - exact rectangle example refutes shell-density log-concavity as a proof route
  artifact_required: false
  artifact_reason: theorem-sized claims have full proofs on page; no finite exhaustive claim was made
  shared_root_edit: false
  scheduler_mutation: false
```

No root shared ledger, peer track, email, Drive item, public posting, workflow, permission, or other schedule was modified.