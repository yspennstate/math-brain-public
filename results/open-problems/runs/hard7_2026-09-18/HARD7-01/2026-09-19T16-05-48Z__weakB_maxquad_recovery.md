Model actually running: **GPT-5.6 Sol. Reasoning level: UNVERIFIED — this is not GPT-6 at maximum, and I do not claim otherwise. No source-metric movement: `D_B=2 -> D_B=2`. Methods tried: B19 / B21 / B28.**

# HARD7-01 run 20 — execute STUCK2 refutation recovery: max-of-quadratics search and one-cell rigidity

Status: **PARTIAL / source OPEN / second recovery executed / no frozen-metric movement**.

## 1. Continuity and repository state

This run resumes the exact admitted source target owned by `operations/claims/B-WEAK-EVEN-LOGCONCAVE.md`: for every even log-concave probability measure `mu` on `R^n` and every origin-symmetric convex body `K`, prove that `t -> mu(e^t K)` is log-concave. The frozen metric remains

`D_B = largest d for which the full source statement is proved for every admissible (mu,K) in every n<=d`.

The verified baseline is Saroglou's planar theorem, hence

\[
\boxed{D_B:2\longrightarrow2.}
\]

This is **no movement**. The structured theorem proved below is deliberately not counted as dimension-three closure.

At run start I reread/reconciled `operations/hard7_2026-09-18/CONTROL.md`, `operations/NEW_METHODS_2026-09-16.md`, the owner directive, campaign `INDEX.md` and `RANKING.md`, root `POSTED.md`, `RESULTS.md`, `QUEUE.md`, the active claim, the latest HARD7-01 STUCK2 checkpoint, and the newest visible neighboring HARD7-02 state. Repository-wide alias search for `B-conjecture`, `Cordero-Erausquin`, even log-concavity and the canonical claim found no competing owner or posted/settled equivalent. The indexed search covers the intake aliases visible to repository code search; I do not claim a byte-for-byte read of every very large append-only intake JSONL file.

The preceding STUCK2 report explicitly chose **REFUTE INSTEAD OF PROVE** and reserved B19/B21/B28 for this ordinary recovery run. This run executes that choice rather than extending the previous `l_q` safe cone.

## 2. Fresh source/current-literature sentinel — 2026-09-19

A bounded current search again found no paper claiming the unrestricted all-dimensional even-log-concave `(B)` statement.

- Cordero-Erausquin--Rotem, *Improved log-concavity for rotationally invariant measures of symmetric convex sets*, Ann. Probab. 51 (2023), proves `(B)` for the rotationally invariant class and states the general conjecture.
- Saroglou, *More on logarithmic sums of convex bodies*, Mathematika 62 (2016), proves the plane and the implication from log-Brunn--Minkowski.
- Armeniakos--Ulivelli, arXiv:2602.23350, submitted 2026-02-26, derives `(B)` from a strengthened dimensional Brunn--Minkowski hypothesis and recovers hereditarily convex measures; it does not state the unrestricted theorem.
- Putterman, *Sharp stability for the (B)-theorem*, arXiv:2608.08472, submitted 2026-08-09, studies sharp stability for the Gaussian theorem. In particular its near-equality description forces covariance principal components toward `0` or `1`; it is not a proof of the unrestricted conjecture.

Searches used combinations of `B-conjecture even log-concave`, `logarithmic concavity of dilates`, `Cordero-Erausquin Rotem`, `Saroglou`, `Putterman`, and 2026 date restrictions. This is bounded negative evidence, not a worldwide novelty certificate.

## 3. Refutation laboratory retained from STUCK2

For the common-degree `p=2`, `n=3` homogeneous test isolated in the preceding reports, let `phi,psi` be even convex two-homogeneous functions, `H=phi+psi`, `nu_H` cone probability on `S_H={H=1}`, and

\[
U=\phi/H,\qquad m=\mathbb E_{\nu_H}U.
\]

The target special-case inequality is

\[
\operatorname{Var}_{\nu_H}(U)\le {2\over5}m(1-m). \tag{3.1}
\]

A violation of the source-valid homogeneous criterion would be a serious refutation route; proving (3.1) for a subclass remains only PARTIAL.

The STUCK2 handoff selected finite max-of-quadratics

\[
\phi(x)=\max_i x^TA_i x,\qquad \psi(x)=\max_j x^TB_jx, \tag{3.2}
\]

because each fixed candidate has a finite semialgebraic spherical cell decomposition and can ultimately be certified exactly rather than inferred from a mesh.

## 4. B19 — MAKE IT AN ALGORITHM: coarse candidates must survive refinement

I implemented the promised candidate pipeline in the exact run artifact

`artifacts/hard7_2026-09-18/HARD7-01/2026-09-19T16-05-48Z__maxquad_recovery.py`.

For two-homogeneous `H`, the cone law has Euclidean-sphere density proportional to `H(theta)^(-3/2)`. Thus a candidate can be screened by deterministic sphere quadrature using

\[
R={\operatorname{Var}(U)\over m(1-m)},
\]

with failure threshold `R>2/5`.

The important event in this run was a **false numerical counterexample**. A random rank-one/max candidate looked like

\[
R_{20000}=0.405967564281601>0.4,
\]

but refinement of the same fixed matrices gave

\[
R_{80000}=0.394183474989145,\quad
R_{200000}=0.393917710267901,\quad
R_{600000}=0.394376418953583.
\]

Therefore the apparent violation is rejected. This is exactly why the owner rule forbids promoting discretely sampled paths/spheres to continuous claims. The matrices and deterministic quadrature are archived in the artifact; no exhaustive-search claim is made.

**Outcome B19.** The finite-cell route remains viable, but coarse global sphere meshes are not reliable near the sharp `2/5` boundary when `H` is highly anisotropic. Any future positive candidate must be followed by active-cell integration / interval bounds before it is even called a candidate counterexample.

## 5. B21 — ASK WHO ELSE HAS THIS SHAPE: Gaussian equality is a projection split

The near-threshold numerics repeatedly returned configurations close to a simple Gaussian equality model. For

\[
\phi_0(x)=x_1^2,\qquad \psi_0(x)=x_2^2+x_3^2,
\]

we have `H_0=|x|^2` and, under cone measure on the Euclidean sphere,

\[
U_0=x_1^2\sim \operatorname{Beta}(1/2,1).
\]

Hence

\[
\mathbb EU_0={1\over3},\qquad
\operatorname{Var}(U_0)={4\over45}
={2\over5}\,{1\over3}{2\over3}. \tag{5.1}
\]

So the `2/5` constant is already saturated by a rank-one/rank-two quadratic projection split. This matches the qualitative message of Putterman's 2026 Gaussian stability result: near equality is associated with principal components near `0/1`.

That suggests a precise counterexample test: start at the projection equality and activate one genuinely nonquadratic max cell. The following calculation decides that test completely.

### Proposition 5.1 — one-cell max perturbations are strictly safe

For every `a>0`, define

\[
\phi_a(x)=\max\{x_1^2,a x_2^2\},\qquad
\psi(x)=x_2^2+x_3^2,
\]

`H_a=phi_a+psi`, `U_a=phi_a/H_a`, and let `nu_a` be cone probability on `{H_a=1}`. Then

\[
\boxed{\operatorname{Var}_{\nu_a}(U_a)< {2\over5}m_a(1-m_a)}\qquad(a>0), \tag{5.2}
\]

where `m_a=E_{nu_a}U_a`. Thus this entire one-active-cell deformation of the Gaussian projection equality cannot refute (3.1).

#### Proof

For any degree-zero `F`, two-homogeneity gives

\[
\mathbb E_{\nu_a}F
={\int_{\mathbb R^3}F(x)e^{-H_a(x)}dx\over
  \int_{\mathbb R^3}e^{-H_a(x)}dx}, \tag{5.3}
\]

because radial integration contributes the same Gamma factor to numerator and denominator.

Split `R^3` into

\[
A=\{|x_1|\ge \sqrt a |x_2|\},\qquad B=A^c.
\]

Write

\[
\alpha=\arctan(a^{-1/2}),\qquad
b={\sqrt a\over 1+a},\qquad
c={a\over1+a}. \tag{5.4}
\]

On `A`, `H_a=|x|^2`. The azimuthal fraction is `2 alpha/pi`; independence of azimuth and the third coordinate under the spherical law yields

\[
Z_A=2\sqrt\pi\,\alpha,
\]

\[
E_A U={2\over3}\left({1\over2}+{\sin2\alpha\over4\alpha}\right),
\]

\[
E_A U^2={8\over15}\left({3\over8}+{\sin2\alpha\over4\alpha}
+{\sin4\alpha\over32\alpha}\right). \tag{5.5}
\]

On `B`, `H_a=(1+a)x_2^2+x_3^2`, while integration in `x_1` contributes the interval length `2 sqrt(a)|x_2|`. After `y=sqrt(1+a)x_2`, the remaining angular density in `(y,x_3)` is proportional to `|cos theta|`, giving

\[
Z_B=2\sqrt\pi\,b,\qquad
E_B U={2c\over3},\qquad
E_B U^2={8c^2\over15}. \tag{5.6}
\]

Using

\[
\sin2\alpha=2b,\qquad
\sin4\alpha=4b(2c-1), \tag{5.7}
\]

we obtain the exact moments

\[
m_a={\alpha+b(1+2c)\over3(\alpha+b)}, \tag{5.8}
\]

\[
E U_a^2={3\alpha+b(3+2c+8c^2)\over15(\alpha+b)}. \tag{5.9}
\]

A direct simplification gives the exact defect

\[
Q_a:={2\over5}m_a(1-m_a)-\operatorname{Var}(U_a)
={2bc\big[(3-4c)\alpha+(3-2c)b\big]\over15(\alpha+b)^2}. \tag{5.10}
\]

If `0<a<=3`, both terms in the square bracket are nonnegative and the second is positive. If `a>3`, then

\[
{(a+3)b\over a-3}
={\sqrt a(a+3)\over(a+1)(a-3)}
>{1\over\sqrt a}
>\arctan(a^{-1/2})=\alpha, \tag{5.11}
\]

where the first strict inequality is equivalent to `a(a+3)>(a+1)(a-3)`, i.e. `5a+3>0`. Equation (5.11) is exactly

\[
(a+3)b>(a-3)\alpha,
\]

so the square bracket in (5.10) is positive again. Hence `Q_a>0` for every finite `a>0`, proving (5.2). `square`

The symbolic factorization in (5.10) is independently reproduced in the artifact output with `IDENTITY_OK = True`.

Two boundary facts explain the numerical difficulty:

\[
R_a\to {2\over5}\quad(a\downarrow0),\qquad
R_a\to {2\over5}\quad(a\to\infty), \tag{5.12}
\]

while every finite `a` is strict. Thus a finite mesh can easily report a fake sign near the degenerate equality strata.

By linear change of variables and rotation in the two-dimensional complementary subspace, Proposition 5.1 also covers a coordinate-free rank-one/rank-two quadratic equality split with one additional rank-one max cell supported entirely in the rank-two side. I do not enlarge that statement to arbitrary cells without proof.

**Outcome B21.** The most obvious way to leave Gaussian equality is one-sidedly safe. A genuine homogeneous counterexample cannot be obtained by merely activating one competing rank-one cell inside the complementary projection subspace. It needs a multi-cell/global interaction (or a qualitatively different geometry) that defeats the projection-stability mechanism.

## 6. B28 — REPLACE FOR ALL WITH TYPICAL: where should a counterexample live?

The bounded exploratory rank-one/max scan was used only as a route selector. Its strongest lesson is not that random families prove anything, but that near-threshold candidates cluster near the quadratic projection equality and that strong anisotropy makes naive quadrature unstable.

The exact one-cell theorem sharpens that empirical observation: within the first natural nonquadratic deformation direction, equality is approached only on degenerate boundary limits and the interior moves to the **safe** side. Therefore an eventual counterexample, if one exists, is plausibly exceptional rather than generic in the finite max-of-quadratics parameter space.

For the next search, “exceptional” now has a concrete meaning: at least two active cells must interact so that the high-`U` and low-`U` phases both retain substantial cone mass while the total `H` does not make either phase expensive. One-cell projection perturbations are removed from the search space.

**Outcome B28.** No probabilistic or generic theorem is claimed. The typical/random experiment only identifies a lower-dimensional danger locus and, together with Proposition 5.1, narrows the exact refutation search to genuinely multi-cell configurations.

## 7. What moved mathematically, and what did not

The source metric did not move:

\[
D_B:2\to2.
\]

What is new in this recovery is a complete restricted theorem, Proposition 5.1, and a materially improved counterexample filter:

1. the exact Gaussian projection equality is the sharp `2/5` boundary model;
2. one new rank-one max cell in the complementary plane pushes the defect strictly positive for every finite parameter;
3. both degenerate ends return to equality, explaining false numerical positives;
4. any source-relevant max-of-quadratics refutation must use at least a genuinely multi-cell mechanism, not the first active-cell perturbation.

This is genuine route progress but, per owner instruction, it is **not** relabeled as frozen-metric movement.

## 8. Section-I lifecycle consequence

This run executed the second STUCK2 recovery chosen in the previous checkpoint and still left the source obligation `D_B>=3` unchanged. Under the owner rule, HARD7-01 must **not** begin a third recovery cycle on weak `(B)`. The next HARD7-01 invocation should write the terminal handoff for this source and select a fresh eligible external hard target in the Gaussian/log-concave lane after a new admission/ownership/current-literature check. The present schedule itself must remain enabled; only the target rotates.

## 9. Artifacts and capability truth

Artifacts:

- code commit: `c07094c475a5a53a9d5f0657e66e924be6dc17e3`;
- output commit: `de44ac6da13b18fb9f19806c6d851f74150f81d4`.

The output contains the exact symbolic defect factorization and the deterministic refinement of the false numerical candidate. The sphere quadrature is explicitly labeled non-certificate.

Actual model visible to this invocation: **GPT-5.6 Sol**. Reasoning-effort telemetry: **UNVERIFIED**. I do not claim GPT-6 maximum.

The exposed task interface still has title/prompt, schedule or relative-start data, timing mode, enabled state and task identity/update operations, but no binding model selector, no binding reasoning-effort selector and no guaranteed runtime field. Making GPT-6/maximum binding would require a product/workspace/API/admin scheduling surface that stores those inference-routing fields and returns authenticated per-run telemetry. Historical `You cannot modify this task` responses are authorization-context boundaries; the compliant workaround is the owning/authorized account or platform support, not duplicate schedules or permission bypass.

No scheduler, email, Drive, public posting, workflow or other-track file was modified.

## 10. Structured ledger delta

```yaml
ledger_delta:
  worker: HARD7-01
  lane: HARD_OUTSIDE
  source: weak_B_conjecture_even_logconcave
  canonical_claim: operations/claims/B-WEAK-EVEN-LOGCONCAVE.md
  frozen_metric: D_B
  before: 2
  after: 2
  movement: none
  status: PARTIAL
  methods: [B19, B21, B28]
  new_restricted_result: one_cell_max_quadratic_projection_deformation_strictly_safe
  closure_claimed: false
  independent_audits: 0
  next_action: mandatory_source_handoff_and_fresh_admission_on_next_HARD7-01_run
```
