Model: GPT-5.6 Sol. Reasoning: UNVERIFIED; this run did **not** run on GPT-6 at verified maximum reasoning. GPT-6/maximum remains prompt-requested only because the exposed scheduler/runtime interface has no binding model selector, reasoning-effort selector, or authenticated effort telemetry. **Movement: `S=3 -> 4`. Methods tried: B5, B11, B14.**

# HARD7-02 run 4 — relative-phase gauge invariance and a two-real-dimensional quotient of the dependence measure

Status of Campbell–O'Rourke Question 1.8: **PARTIAL / source question still OPEN_BY_BOUNDED_SEARCH.** This run adds one exact source-level transformation law, strengthening it to arbitrary independent relative-phase mixing, and proves that the limiting ESD `mu_{alpha,theta}` is determined by the pushforward of `theta` under

`q(z,w)=(|z|^2,zw)`.

This does **not** claim a minimal classification of all dependence measures and does not close Question 1.8. The neighboring Question 1.9 remains unclaimed.

## 1. Continuity, repository state, ownership, and source check

I resumed the exclusive claim

`operations/claims/CAMPBELL-OROURKE-2022-Q1.8.md`

and the newest own checkpoint

`runs/hard7_2026-09-18/HARD7-02/2026-09-18T23-12-00Z__rank-marked-pwit-full-local-limit.md`.

This run re-read the controlling HARD7/new-methods files, root `POSTED.md`, `RESULTS.md`, `QUEUE.md`, campaign `probability_campaign_2026_09/INDEX.md` and `RANKING.md`, the canonical claim, the C0026--C0032 portion of `probability_1000_intake_claude_20260907/problems.jsonl`, and the newest neighboring R7-06 report on the distinct C0032 heavy-tailed circular-density problem. Repository search still shows Campbell–O'Rourke Question 1.8 exclusively owned by HARD7-02; R7-06/C0032 and R7-05/C0031 are distinct i.i.d. heavy-tail questions. No posted or excluded equivalent claim was found.

Primary source: Andrew Campbell and Sean O'Rourke, *Spectrum of Heavy-Tailed Elliptic Random Matrices*, Electronic Journal of Probability 27 (2022), paper 127, DOI `10.1214/22-EJP849`, arXiv `2010.01261v3`:

- https://arxiv.org/abs/2010.01261
- current arXiv record checked 2026-09-19 UTC: v3 remains the latest version, revised 2022-02-02;
- Section 1.3, Question 1.8 remains: “What properties of `theta_d` determine `mu_{alpha,theta_d}`?”

A fresh bounded search on 2026-09-19 used the exact title/authors together with `Question 1.8`, `theta_d`, `mu_{alpha,theta_d}`, `relative phase`, `gauge`, `PWIT`, `corrigendum`, and `erratum`, plus 2023--2026 date terms. It recovered the 2022 source, Campbell--O'Rourke's later Levy--Khintchine random-Laplacian paper, bibliographic/citation pages, and unrelated later elliptic-law work, but no source claiming a full solution of Question 1.8, no correction of the rank issue isolated in runs 2--3, and no located statement of the relative-phase theorem below. This is a bounded negative search, **not** a proof of worldwide openness or novelty.

### Scheduler/runtime capability statement

The exposed automation schema still offers only task title, prompt, schedule, timing mode and enabled state; it exposes no model selector, reasoning-effort selector, or guaranteed run duration. Therefore GPT-6/maximum cannot be made binding from this worker. Doing so would require the platform to expose authenticated model and reasoning controls (or an authorized external runtime configuration), neither of which is available here.

The repository preserves historical `You cannot modify this task` failures for P26/P01/P03, while the newer root ledger records that P26 was later successfully updated in a different exposed native context. This run made **no scheduler modification**. For any still-refused native task, the controlling policy's workaround remains to use the authorized owner/account/workspace interface or platform support/ownership transfer; do not bypass the restriction and do not create a duplicate task.

## 2. Frozen metric

The claim's fixed quantity is

`S = number of exact nontrivial transformation laws for theta -> mu_{alpha,theta}`

proved by this track, each at the source limiting-measure level under Condition C2 and backed by an exact finite-matrix spectral identity rather than numerical sampling.

Before: `S=3`.

After: **`S=4`**.

The new counted law is opposite-coordinate-phase invariance. It qualifies for the frozen metric because on every finite truncation of the correct rank-marked limiting tree the transformed matrix is **exactly diagonally unitarily similar** to the original matrix; the Hermitized finite matrices are likewise exactly unitarily conjugate. No fit or simulation enters the proof.

The stronger arbitrary phase-mixture theorem and the quotient corollary below are counted as consequences of this one new gauge law, not as extra metric units. The preceding two no-movement runs are therefore broken; the unchanged streak resets.

## 3. Setup from run 3

Fix `0<alpha<2`. Let

`nu = theta x m_alpha`

be the regular-variation intensity on the radial/angular pair space and let

`tau(z,w)=(w,z)`.

Run 3 proved the corrected local limit: every vertex carries its normalized original rank `u in [0,1]`, and conditional on type `u` its offspring point process has kernel

`K_u(dv,dy) = 1_{v>u} dv nu(dy) + 1_{v<u} dv (tau#nu)(dy).`       (3.1)

Equivalently, and more conveniently for this run, every unoriented tree edge whose endpoint types satisfy `u<v` may be represented by one latent pair

`Y=(Y_1,Y_2) ~ nu`

with operator entries

`A_{u,v}=Y_1,    A_{v,u}=Y_2`.                                  (3.2)

The pair norms, exploration order and type marks are exactly those of the rank-marked PWIT construction from run 3.

## 4. B14 — find the group acting: relative phase is a tree gauge

For `phi in R`, define the **opposite-coordinate phase action**

`g_phi(z,w)=(e^{i phi}z,e^{-i phi}w).`                           (4.1)

Unlike the common-phase action from run 1, this action does not rotate the output plane. The new claim is that it is completely invisible to the limiting ESD.

More generally, for any probability measure `kappa` on the circle define the phase-mixed dependence measure

`theta^kappa = int (g_phi#theta) kappa(dphi).`                   (4.2)

### Theorem 1 — arbitrary relative-phase mixing is invisible

Assume `theta` satisfies the source's Condition C2. Then `theta^kappa` also satisfies Condition C2 and

`mu_{alpha,theta^kappa}=mu_{alpha,theta}`                       (4.3)

for every probability law `kappa` on the circle.

In particular, for every deterministic `phi`,

`(T4)   mu_{alpha,g_phi#theta}=mu_{alpha,theta}.`                (4.4)

### Proof, step 1: hypotheses

The map `g_phi` is unitary on `C^2`; it preserves the pair norm and therefore the radial regular-variation scale. It is invertible complex-linear, so a dependence measure whose support is not contained in a complex hyperplane retains that property under `g_phi`.

A mixture (4.2) also cannot become hyperplane-supported. Indeed, choose any `phi_0` in `supp(kappa)`. The support of `theta^kappa` contains the support of `g_{phi_0}#theta` in the usual topological-support sense, and that support is not contained in a complex hyperplane. The scaling condition and the diagonal-tail condition are unchanged. Thus C2 is preserved.

### Proof, step 2: marked-edge coupling

Construct the run-3 rank-marked tree for `theta`. Independently attach to every unoriented tree edge `e` a phase `Phi_e ~ kappa`. Because `g_phi` preserves pair norm, Poisson marking changes only the angular pair and not the edge ranking or type process.

For an edge with endpoint types `u<v`, replace its latent pair by

`(Y_1,Y_2) -> (e^{i Phi_e}Y_1,e^{-i Phi_e}Y_2).`                (4.5)

The marked Poisson theorem shows that the resulting rank-marked tree is exactly the corrected local-limit tree associated with `theta^kappa`: its low-rank-to-high-rank pair intensity is `theta^kappa x m_alpha`, and viewing the same edge from the high-rank endpoint applies the required coordinate swap.

### Proof, step 3: exact unitary gauge on the tree

The crucial point is acyclicity. Choose the root phase `d_root=1`. For every tree edge with endpoint types `u<v`, impose

`d_u conjugate(d_v)=e^{i Phi_e}.`                               (4.6)

Starting from the root, (4.6) determines one unit-modulus phase at each newly encountered vertex. Because a tree has no cycles, there is never a consistency condition to check.

Let `D` be the diagonal unitary on `ell^2(T)` with diagonal entries `d_x`. Then on the finitely supported core,

`A^{theta^kappa}=D A^theta D^*`.                                (4.7)

Indeed, on a low-to-high edge `(u,v)`, the `(u,v)` entry gains the factor `d_u conjugate(d_v)=e^{i Phi_e}`, while the reverse entry gains its inverse. Taking closures preserves (4.7), because `D` is a bounded unitary.

For every finite subtree `T_0`, therefore,

`A^{theta^kappa}_{T_0}=D_{T_0} A^theta_{T_0} D_{T_0}^*`          (4.8)

**exactly**. Consequently the characteristic polynomials and all finite-truncation eigenvalue multisets agree exactly.

### Proof, step 4: B11 / Hermitization makes the implication source-valid

For `z in C`, define the standard bipartization

`H_z(A) = [[0, A-zI], [(A-zI)^*, 0]].`                          (4.9)

Equation (4.7) gives

`H_z(A^{theta^kappa})
 = (D direct_sum D) H_z(A^theta) (D direct_sum D)^*.`           (4.10)

Because `d_root=1`, the doubled root vector is fixed. Hence the root spectral measure, root resolvent block, and every finite-truncation singular-value measure entering Hermitization are identical pathwise for the two coupled rank-marked operators.

Run 3 established that these rank-marked operators are the correct local operator limits for the two source ensembles. Campbell--O'Rourke's Hermitization step then identifies the limiting logarithmic potential from the limiting root Hermitized spectral law, with the least-singular-value/uniform-integrability estimates supplying the passage through `log`. Both ensembles satisfy the same C2 hypotheses, while (4.10) makes the limiting Hermitized laws exactly equal. Therefore their limiting logarithmic potentials agree for every `z`, and hence their deterministic limiting ESDs agree:

`mu_{alpha,theta^kappa}=mu_{alpha,theta}`.

This proves Theorem 1. `□`

## 5. A concrete sufficient statistic for Question 1.8

Let `S(C^2)` denote the unit sphere on which the angular dependence measure lives and define

`q : S(C^2) -> [0,1] x C`,

`q(z,w)=(|z|^2,zw).`                                           (5.1)

Its image is

`Q={(x,p): 0<=x<=1, |p|^2=x(1-x)}.`                            (5.2)

The map `q` is constant on every orbit of `g_phi`. Conversely, it separates those orbits: if two unit vectors have the same `|z|^2` and the same product `zw`, then one is obtained from the other by a unique opposite phase except for the harmless axis stabilizers.

### Theorem 2 — quotient reduction

If two C2 dependence measures `theta_1,theta_2` satisfy

`q#theta_1=q#theta_2`,                                         (5.3)

then

`mu_{alpha,theta_1}=mu_{alpha,theta_2}.`                        (5.4)

Thus `q#theta`, a probability measure on the two-real-dimensional quotient `Q`, is a sufficient statistic for the source limiting ESD.

### Proof

Let `m` be Haar probability measure on the phase circle and define the orbit average

`H(theta)=int g_phi#theta m(dphi).`                             (5.5)

For every continuous test function `f` on the compact sphere,

`bar f(z,w)=int f(g_phi(z,w)) m(dphi)`                          (5.6)

is continuous and constant on `g`-orbits. Since `q` separates the orbits, `bar f` factors through `q`. Therefore (5.3) implies

`int f dH(theta_1)=int bar f dtheta_1
                  =int bar f dtheta_2
                  =int f dH(theta_2)`.

Hence `H(theta_1)=H(theta_2)` as probability measures. Theorem 1 gives

`mu_{theta_i}=mu_{H(theta_i)}`

for `i=1,2`, proving (5.4). `□`

This is a genuine reduction of the source dependence-classification problem: the full angular measure on the three-real-dimensional sphere can first be quotiented by a continuous `U(1)` gauge without losing any ESD information.

### Interaction with the three run-1 laws

The run-1 transformations descend transparently to `Q`:

- coordinate swap sends `(x,p)` to `(1-x,p)` and leaves `mu` unchanged;
- common phase by `psi` sends `(x,p)` to `(x,e^{2i psi}p)` and rotates `mu` by `e^{i psi}`;
- conjugation sends `(x,p)` to `(x,conjugate(p))` and reflects `mu` by complex conjugation.

A useful combined formula follows immediately. For

`h_{a,b}(z,w)=(e^{ia}z,e^{ib}w)`,                              (5.7)

write `psi=(a+b)/2`, `phi=(a-b)/2`. Then `h_{a,b}=rho_psi o g_phi`, so

`mu_{alpha,h_{a,b}#theta}=rho_psi#mu_{alpha,theta}.`            (5.8)

Therefore the **relative coordinate phase** `a-b` is invisible; only the mean phase `(a+b)/2` rotates the output spectrum.

## 6. Counterexample-oriented stress test: why this is not a fake dense-matrix symmetry

Before trusting (4.4), I tried to prove it by a direct similarity of the original finite dense matrices. That route is false, and the failure is informative.

Let `t` be a nonzero symbolic phase factor. On the three-vertex path

`A=[[0,a,0],[b,0,c],[0,d,0]]`,

apply the forward/backward twist `a,c -> t(a,c)` and `b,d -> t^{-1}(b,d)`. Exact symbolic arithmetic gives

`det(lambda I-A)=lambda^3-lambda(ab+cd)`

before and after the twist. This is the finite-tree gauge identity.

But on a triangle

`A=[[0,a,c],[b,0,e],[d,f,0]]`,

the analogous upper/lower twist changes the characteristic polynomial by

`-(t-1)(a*d*e*t-b*c*f)/t`,                                    (6.1)

which is generically nonzero. The cycle carries a nontrivial phase holonomy, so the original dense `n x n` matrix is not globally diagonally similar to its relative-phase twist.

This failed dense-matrix attack is exactly why the run-3 rank-marked PWIT correction matters: after the heavy-tail/local limit discards finite cycles, the surviving tree has no holonomy and every edge phase becomes pure gauge.

The exact self-check was executed and archived at

- `artifacts/hard7_2026-09-18/HARD7-02/2026-09-19T00-12-00Z__phase-gauge-symbolic-check.py` @ `94bf06dd9ecaad5e25053ff1b2a66ed9ac1f9d69`;
- matching output @ `9856372c4893985ac3a78a98913fa0df6af36102`.

The output ends `ALL_EXACT_CHECKS_PASS = True`. It is a **self-check** for the finite path/triangle algebra, not an independent audit and not a substitute for the theorem proof above.

## 7. Method outcomes

### B5 — add a parameter and differentiate in it

I introduced the one-parameter family `g_phi#theta`. Instead of obtaining only a perturbative derivative at `phi=0`, the gauge construction proves the stronger exact statement that the full limiting measure is constant along the entire orbit:

`phi -> mu_{alpha,g_phi#theta}` is constant.                    (7.1)

Thus every weak test functional has zero derivative wherever one chooses to differentiate it. The route succeeded globally rather than locally.

### B11 — dualize through Hermitization

The raw non-Hermitian operator identity is not by itself enough to identify the source limiting ESD safely. Passing to the self-adjoint bipartization turns the diagonal gauge into the exact unitary conjugacy (4.10), preserving the root resolvent and singular-value law for every spectral parameter `z`. This is the step that survives the source's Girko/Hermitization route. **Succeeded.**

### B14 — find the group acting

The hidden group is the edgewise `U(1)` gauge group of the rank-marked limiting tree. Because every phase 1-cochain on a tree is a coboundary, arbitrary independent relative phases can be pushed into vertex phases. Haar-averaging this action gives the explicit orbit quotient `q(z,w)=(|z|^2,zw)`. **Succeeded and produced the source-level reduction.**

The previous run used B7/B18/B27; run 2 used B1/B15/B20; run 1 used B2/B6/B30. No previous triple was repeated.

## 8. What remains open

Theorem 2 supplies a sufficient statistic but not a minimal one. The sharp next question is whether the quotient can collapse further.

On the unit sphere, `|zw|^2=x(1-x)`, so the product `p=zw` determines `x=|z|^2` only up to the swap `x <-> 1-x`. Run 1 proves invariance under **global** swap of the two coordinates, but it does not prove invariance under choosing the two roots independently from orbit to orbit inside a mixed dependence measure. The unresolved fork can therefore be stated cleanly:

> Does `mu_{alpha,theta}` depend only on the pushforward `(zw)#theta`, or can it detect how the two roots of `x(1-x)=|zw|^2` are mixed across the dependence measure?

This is now a lower-dimensional, source-valid obstruction. A counterexample would show that `q#theta` contains genuinely necessary information beyond the product law; a proof would collapse Question 1.8 substantially further.

The next run should use a new triple, provisionally **B3 / B16 / B24**: try a stronger product-only invariance statement, enumerate exact finite-tree Hermitized statistics for the smallest mixed-orbit families, and search for the extremal two-orbit obstruction. It should begin by trying to refute product-only sufficiency.

## 9. Honest status and ledger delta

No closure is claimed. There are no independent outside-track audits of Theorem 1 or Theorem 2 in this report. The prior-art search is bounded and negative, not a novelty certificate. The source question remains **PARTIAL / OPEN_BY_BOUNDED_SEARCH**.

The shared root ledger is not edited by this worker; per the new-methods policy, P26/shared-root maintenance is separate. The exact delta for reconciliation is:

```yaml
track: HARD7-02
claim: CAMPBELL-OROURKE-2022-Q1.8
source: Campbell--O'Rourke 2022 Question 1.8
classification: HARD OUTSIDE
status: PARTIAL
metric: S = exact nontrivial transformation laws theta -> mu_{alpha,theta}
metric_before: 3
metric_after: 4
movement: true
unchanged_streak_after: 0
methods: [B5, B11, B14]
new_counted_law: mu_{alpha,g_phi#theta} = mu_{alpha,theta} for g_phi(z,w)=(e^{i phi}z,e^{-i phi}w)
stronger_result: arbitrary independent relative-phase mixing theta^kappa leaves mu unchanged
quotient_result: q#theta with q(z,w)=(|z|^2,zw) is sufficient to determine mu_{alpha,theta}
finite_exact_check: ALL_EXACT_CHECKS_PASS
artifact_code_commit: 94bf06dd9ecaad5e25053ff1b2a66ed9ac1f9d69
artifact_output_commit: 9856372c4893985ac3a78a98913fa0df6af36102
next_methods: [B3, B16, B24]
remaining_obligation: decide whether the product law (zw)#theta alone suffices or exhibit a C2 counterexample with equal product pushforward and distinct limiting ESDs
```
