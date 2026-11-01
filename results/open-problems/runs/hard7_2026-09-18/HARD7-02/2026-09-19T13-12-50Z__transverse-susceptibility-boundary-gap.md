Model: GPT-5.6 Sol. Reasoning: UNVERIFIED; this run did **not** run on GPT-6 at verified maximum reasoning. GPT-6/maximum remains prompt-requested only because the exposed scheduler/runtime surface has no binding model selector, reasoning-effort selector, authenticated effort telemetry, or guaranteed execution duration. **No movement in the frozen source metric: `S=5 -> 5`. Final-recovery methods tried: B5, B15, B29.**

# HARD7-02 final recovery, run 2 — transverse Hermitization susceptibility, exact endpoint deformation, and a uniform `eta -> 0` coherence gap

Status of Campbell–O'Rourke Question 1.8: **PARTIAL / source question remains OPEN in bounded current-status search.**

This is the second ordinary substantive execution after the second and final Section-I recovery checkpoint

`runs/hard7_2026-09-18/HARD7-02/2026-09-19T11-12-38Z__stuck2-joint-hermitization-susceptibility-plan.md`.

The preceding final-recovery run was

`runs/hard7_2026-09-18/HARD7-02/2026-09-19T12-14-36Z__joint-channel-coherence-final-recovery.md`

at creation commit `af181169aa9376049eeb188dc7a358bbd3a44507`. It proved a positive two-channel overlap recursion and strict fixed-`eta` coherence loss for the family

\[
\eta_x=\operatorname{Law}\bigl(\sqrt{x}e^{i\phi},\sqrt{1-x}e^{-i\phi}\bigr),
\qquad
\vartheta_x=\frac12(\eta_x+\tau_\#\eta_x),
\quad 0<x\le\frac12,
\]

but found that a **real** spectral shift probes a parity-signed overlap rather than the positive one. The present run changes the direction of attack rather than adding another lemma to that signed recursion. The key new observation is that a **purely imaginary spectral shift removes that parity cancellation exactly**. At `alpha=1` the resulting positive susceptibility has a normalized coherence defect that stays uniformly away from zero as `eta downarrow 0` for every fixed interior `x<1/2`.

This still does **not** prove

\[
\mu_{1,\vartheta_{1/4}}\ne\mu_{1,\vartheta_{1/2}},
\]

because converting the normalized transverse susceptibility gap into an unregularized logarithmic-potential difference still requires a source-level comparison of the raw curvature coefficient. No closure label is upgraded.

## 1. Continuity, repository-wide exclusions, ownership, and current status

At run start I re-read or refreshed the required control state:

- `operations/hard7_2026-09-18/CONTROL.md`;
- `operations/NEW_METHODS_2026-09-16.md`;
- `operations/new_methods_2026-09-16/OWNER_DIRECTIVE.md`;
- root `POSTED.md`, `RESULTS.md`, and `QUEUE.md`;
- `probability_campaign_2026_09/INDEX.md` and `RANKING.md`;
- `operations/claims/CAMPBELL-OROURKE-2022-Q1.8.md`;
- the complete HARD7-02 chain through STUCK2 and final-recovery run 1;
- the relevant non-Hermitian intake block `C0026--C0032` in `probability_1000_intake_claude_20260907/problems.jsonl`;
- neighboring heavy-tail records, including the R7-06 terminal C0032 handoff and the R7-05 C0031 handoff/claim history.

The intake block confirms that C0026--C0030 contain already-resolved local-universality/elliptic-law/oriented-graph/Weyl items plus the excluded Bernoulli least-singular-value target C0029, while C0031 and C0032 are the distinct iid heavy-tail almost-sure-convergence and explicit-density questions. They are not aliases of Campbell–O'Rourke Question 1.8. R7-06 has terminally handed off C0032 after its own recovery exhaustion, and repository ownership search still identifies Question 1.8 uniquely with HARD7-02. No posted author manuscript, Bernoulli-singularity target, Gaussian row-submatrix/least-singular-value manuscript, Toeplitz/Hankel target, additive-spike target, or gated-product target collides with this claim.

### Primary source

Andrew Campbell and Sean O'Rourke, *Spectrum of Heavy-Tailed Elliptic Random Matrices*, Electronic Journal of Probability **27** (2022), paper 127, DOI `10.1214/22-EJP849`, arXiv `2010.01261v3`:

- https://arxiv.org/abs/2010.01261
- https://doi.org/10.1214/22-EJP849

Section 1.3 asks exactly:

> **Question 1.8.** What properties of `theta_d` determine `mu_{alpha,theta_d}`?

Theorem 1.6 is the proved convergence theorem under Condition C2; it is not being relabeled as open.

### Bounded current-literature refresh — 2026-09-19

Fresh searches used the exact source title/authors together with `Question 1.8`, `theta_d`, `mu_{alpha,theta_d}`, dependence measure, PWIT, Hermitization, and 2025--2026 terms. They recovered the 2022 source and the 2025 Carpenter--O'Rourke preprint *The Limiting Spectral Distribution for Sparse Elliptic Random Matrices* (`arXiv:2508.04891`). That sparse finite-variance result concerns a different model and does not claim the heavy-tailed dependence classification in Question 1.8. I located no later paper explicitly claiming a full resolution of Question 1.8. This is bounded negative evidence only, not a worldwide novelty certificate.

### Runtime / scheduler capability

The exposed automation surface for this worker still has no binding model selector, reasoning-effort selector, authenticated effort telemetry, or guaranteed duration. GPT-6/maximum therefore cannot be made binding from this surface; doing so would require an authorized platform scheduler/runtime interface that actually exposes those fields and reports the selected runtime.

The repository preserves historical `You cannot modify this task` failures for P26/P01/P03, while `RESULTS.md` records that P26 was later editable in a different authorized native context. If a task still rejects modification, the compliant workaround is the authorized owner/account/workspace context or platform support/ownership transfer. It is not a permission bypass and not a duplicate schedule. No scheduler mutation was attempted here.

## 2. Frozen metric and Section-I state

The canonical claim freezes

`S = number of exact nontrivial full-source transformation laws theta_d -> mu_{alpha,theta_d}`

under the established counting rule.

Before this run: `S=5`.

After this run: **`S=5` — no movement.**

The results below are fixed-regularization and boundary-susceptibility theorems, not a sixth full transformation law for the planar limiting ESD, so they are deliberately not counted.

This is the **second** ordinary no-movement run after STUCK2. The final-recovery unchanged streak is therefore two. There is no STUCK3. If the next ordinary final-recovery run also leaves `S` unchanged, the Section-I terminal rotation rule activates: Question 1.8 must be handed off and HARD7-02 must rotate to a fresh eligible hard target.

## 3. Starting point: the common-gauge two-channel representation

From final-recovery run 1, on one rooted PWIT every edge `e` carries a radial mark `r_e>0` and an independent fair coin

\[
C_e\in\{x,1-x\}.
\]

After a common unitary tree gauge, the two zero-shift self-adjoint channel operators have positive edge weights

\[
t_{+,e}=r_e\sqrt{C_e},
\qquad
t_{-,e}=r_e\sqrt{1-C_e}.
\tag{3.1}
\]

In particular

\[
t_{+,e}t_{-,e}=\beta_x r_e^2,
\qquad
\beta_x=\sqrt{x(1-x)}.
\tag{3.2}
\]

At `x=1/2`, `H_+=H_-` pathwise. For fixed `eta>0`, set

\[
R_\pm=(H_\pm-i\eta)^{-1},
\qquad
\nu_\pm=R_\pm\delta_o,
\qquad
\langle\delta_o,R_\pm\delta_o\rangle=iq_\pm,
\quad q_\pm>0.
\tag{3.3}
\]

The positive overlap is

\[
Z_x(\eta)=\langle\nu_+,\nu_-\rangle>0
\tag{3.4}
\]

and the normalized coherence is

\[
\kappa_x(\eta)
=\frac{\eta\,\mathbb E Z_x(\eta)}{\mathbb E q_+}.
\tag{3.5}
\]

The preceding run proved

\[
\kappa_{1/2}(\eta)=1,
\qquad
0<\kappa_x(\eta)<1\quad(0<x<1/2)
\tag{3.6}
\]

for every fixed `eta>0`, but did not control the boundary `eta downarrow 0`.

## 4. B5 — differentiate the dependence parameter at the Hermitian endpoint

Write

\[
x=\frac12-\varepsilon,
\qquad 0\le\varepsilon<\frac12,
\]

and encode the fair edge coin by independent signs `sigma_e in {+1,-1}` so that

\[
C_e=\frac12+\sigma_e\varepsilon.
\]

Put

\[
a_e=\frac{r_e}{\sqrt2},
\]

let `H` be the positive weighted tree adjacency with edge weights `a_e`, and let `V` be the signed adjacency with edge weights `sigma_e a_e`. Define

\[
h_\varepsilon
=\frac{\sqrt{1+2\varepsilon}+\sqrt{1-2\varepsilon}}2,
\qquad
d_\varepsilon
=\frac{\sqrt{1+2\varepsilon}-\sqrt{1-2\varepsilon}}2.
\tag{4.1}
\]

Then **edge by edge, exactly**,

\[
H_+(\varepsilon)=h_\varepsilon H+d_\varepsilon V,
\qquad
H_-(\varepsilon)=h_\varepsilon H-d_\varepsilon V.
\tag{4.2}
\]

The elementary identities

\[
h_\varepsilon^2+d_\varepsilon^2=1,
\qquad
h_\varepsilon d_\varepsilon=\varepsilon
\tag{4.3}
\]

show that, with

\[
\rho=d_\varepsilon^2,
\]

we have

\[
\rho(1-\rho)=\varepsilon^2,
\qquad
\rho=\varepsilon^2+O(\varepsilon^4),
\qquad
h_\varepsilon=\sqrt{1-\rho}.
\tag{4.4}
\]

Thus the first possible endpoint response is quadratic in `varepsilon`, not linear.

### Proposition 4.1 — exact finite-tree endpoint curvature formula

Fix a finite tree truncation, a real spectral shift `t`, and `eta>0`. After the constant channel rotation

\[
P=2^{-1/2}
\begin{pmatrix}I&I\\I&-I\end{pmatrix},
\]

the regularized Hermitized matrix becomes

\[
M_\rho=
\begin{pmatrix}
\sqrt{1-\rho}\,H-tI-i\eta I & \sqrt\rho\,V\\
\sqrt\rho\,V & \sqrt{1-\rho}\,H+tI-i\eta I
\end{pmatrix}.
\tag{4.5}
\]

Let

\[
R_{-t}=(H-tI-i\eta I)^{-1},
\qquad
R_{+t}=(H+tI-i\eta I)^{-1}.
\tag{4.6}
\]

Then

\[
\boxed{
\left.\frac{d}{d\rho}\log\det M_\rho\right|_{\rho=0}
=-\frac12\operatorname{Tr}(R_{-t}H+R_{+t}H)
-\operatorname{Tr}(R_{+t}VR_{-t}V).
}
\tag{4.7}
\]

Equivalently, because `rho=varepsilon^2+O(varepsilon^4)`,

\[
\boxed{
\left.\frac{d^2}{d\varepsilon^2}\log\det M_{\varepsilon}\right|_{\varepsilon=0}
=-\operatorname{Tr}(R_{-t}H+R_{+t}H)
-2\operatorname{Tr}(R_{+t}VR_{-t}V).
}
\tag{4.8}
\]

#### Proof

Equation (4.5) follows by inserting (4.2) in the two-channel real-shift block and conjugating by `P`. Schur complementation gives

\[
\det M_\rho
=\det A_\rho\,
\det\bigl(D_\rho-\rho V A_\rho^{-1}V\bigr),
\]

where

\[
A_\rho=\sqrt{1-\rho}\,H-tI-i\eta I,
\qquad
D_\rho=\sqrt{1-\rho}\,H+tI-i\eta I.
\]

At `rho=0`, both diagonal derivatives equal `-H/2`. Differentiating the logarithmic determinants gives (4.7). Equation (4.4) then gives (4.8). `QED`

The signed perturbation can also be averaged **exactly** over the independent edge signs at the endpoint. Writing

\[
V=\sum_e \sigma_e a_e S_e,
\]

where `S_e` is the two-endpoint adjacency flip on edge `e`, independence and `E sigma_e sigma_f=1_{e=f}` yield

\[
\mathbb E_\sigma\operatorname{Tr}(R_{+t}VR_{-t}V)
=\sum_e a_e^2\operatorname{Tr}(R_{+t}S_eR_{-t}S_e).
\tag{4.9}
\]

So the endpoint dependence deformation is reduced to an explicit radial-tree edge sum rather than an uncontrolled bivariate perturbation.

**B5 outcome:** succeeded as an exact deformation formula. It does not by itself prove that the full limiting ESD varies with `x`, because the infinite-tree/`eta downarrow 0` passage and possible cancellation in (4.8) still matter. It does show precisely what any local equality proof would have to cancel at second order.

## 5. B15 — break the spectral-shift symmetry: imaginary shifts see the positive overlap

The preceding run used only a real shift and therefore encountered the alternating-depth susceptibility. The off-axis direction behaves differently.

Let `J` be the depth-parity involution on either scalar channel,

\[
J\delta_v=(-1)^{d(v)}\delta_v.
\tag{5.1}
\]

Because each `H_\pm` is a zero-diagonal tree adjacency,

\[
JH_\pm J=-H_\pm.
\tag{5.2}
\]

Choose the channel labels so that at even depth the `+` component uses the upper bipartization copy. For a general spectral shift

\[
z=a+ib,
\]

a same-vertex Hermitization edge has weight `-z` at even depth and `-bar z` at odd depth. Therefore, after the common gauge from the preceding run, the **exact** channel block is

\[
\boxed{
\mathcal B_z-i\eta I
=
\begin{pmatrix}
H_+-i\eta I & -aI-ibJ\\
-aI+ibJ & H_--i\eta I
\end{pmatrix}.
}
\tag{5.3}
\]

This is the missing directional structure.

### Proposition 5.1 — real and imaginary quadratic susceptibilities are different transforms

On every finite tree truncation, write `s=a^2` for a pure real shift and `s=b^2` for a pure imaginary shift. At zero shift,

\[
\left.\frac{d}{ds}\log\det(\mathcal B_{\sqrt s}-i\eta I)\right|_{s=0}
=-\operatorname{Tr}(R_-R_+),
\tag{5.4}
\]

whereas

\[
\boxed{
\left.\frac{d}{ds}\log\det(\mathcal B_{i\sqrt s}-i\eta I)\right|_{s=0}
=-\operatorname{Tr}(R_-JR_+J)
=\operatorname{Tr}(R_-R_+^*).
}
\tag{5.5}
\]

#### Proof

Equation (5.4) is the preceding run's Schur-complement identity. For `z=ib`, (5.3) gives off-diagonal blocks `-ibJ` and `ibJ`, so Schur complementation gives the first expression in (5.5). From (5.2),

\[
J R_+ J
=J(H_+-i\eta)^{-1}J
=(-H_+-i\eta)^{-1}
=-(H_++i\eta)^{-1}
=-R_+^*.
\tag{5.6}
\]

Substitution gives the second expression. `QED`

At the root, the diagonal kernel of the positive trace term is exactly the overlap from (3.4):

\[
\langle\delta_o,R_-R_+^*\delta_o\rangle
=\sum_v R_-(o,v)\overline{R_+(o,v)}
=Z_x(\eta).
\tag{5.7}
\]

Thus the source-level expected-root transverse susceptibility is

\[
\boxed{
\chi_x^\perp(\eta):=\mathbb E Z_x(\eta),
}
\tag{5.8}
\]

while the real-shift susceptibility uses the parity-signed object `X_x` from the previous run. The two directions are not merely two estimates of the same quantity: they are **exactly different Hermitization probes**.

At the Hermitian endpoint,

\[
\chi_{1/2}^\perp(\eta)
=\mathbb E\|R\delta_o\|^2
=\frac{\mathbb E q}{\eta},
\tag{5.9}
\]

whereas for an interior point

\[
\frac{\eta\chi_x^\perp(\eta)}{\mathbb E q}
=\kappa_x(\eta)<1.
\tag{5.10}
\]

**B15 outcome:** succeeded and removes the principal sign obstruction from final-recovery run 1. A transverse (`Im z`) quadratic response sees the positive joint coherence directly; no alternating-depth cancellation remains.

## 6. B29 — add the boundary `eta=0`: exact alpha=1 marginal control

The remaining danger is that (5.10) could become equality as `eta downarrow 0`. For `alpha=1` that can be ruled out.

Put

\[
U_k=r_k^2.
\]

The radial Poisson intensity becomes

\[
\frac12u^{-3/2}\,du.
\tag{6.1}
\]

For a fair `C in {x,1-x}`, define

\[
m_x:=\mathbb E\sqrt C
=\frac{\sqrt x+\sqrt{1-x}}2.
\tag{6.2}
\]

The marginal cavity sum

\[
S_+=\sum_k U_k C_k q_{+,k}
\]

has Laplace transform

\[
\mathbb E e^{-tS_+}=e^{-\lambda_\eta\sqrt t},
\tag{6.3}
\]

where the exact two-message RDE from the preceding run gives

\[
\lambda_\eta
=\sqrt\pi\,m_x\,\mathbb E\sqrt q,
\qquad
q=(\eta+S_+)^{-1}.
\tag{6.4}
\]

Using

\[
y^{-1/2}=\frac1{\sqrt\pi}\int_0^\infty t^{-1/2}e^{-ty}\,dt
\]

and substituting `t=u^2`, (6.4) becomes the scalar equation

\[
\boxed{
\lambda_\eta
=2m_x\int_0^\infty e^{-\eta u^2-\lambda_\eta u}\,du.
}
\tag{6.5}
\]

The right side is strictly decreasing in `lambda`, so the positive solution is unique. Put

\[
\lambda_0=\sqrt{2m_x}.
\tag{6.6}
\]

Since the integral in (6.5) is at most `1/lambda_eta`,

\[
\lambda_\eta\le\lambda_0.
\]

Conversely, using this upper bound inside the integrand,

\[
\lambda_\eta
\ge2m_x\int_0^\infty e^{-\eta u^2-\lambda_0u}\,du
\longrightarrow\lambda_0.
\]

Hence

\[
\boxed{\lambda_\eta\longrightarrow\sqrt{2m_x}.}
\tag{6.7}
\]

Moreover

\[
\mathbb E q
=2\int_0^\infty u e^{-\eta u^2-\lambda_\eta u}\,du
\longrightarrow\frac2{\lambda_0^2}
=\frac1{m_x}.
\tag{6.8}
\]

For every fixed `r>0`,

\[
\mathbb E q^r
=\frac2{\Gamma(r)}
\int_0^\infty u^{2r-1}e^{-\eta u^2-\lambda_\eta u}\,du,
\tag{6.9}
\]

so all positive moments of `q` are uniformly bounded for sufficiently small `eta`. This gives the tightness and uniform integrability needed below; no finite-size simulation enters.

## 7. The new boundary theorem: the interior coherence defect cannot disappear

Normalize the two resolvent columns to unit vectors:

\[
e_\pm
=\sqrt{\frac{\eta}{q_\pm}}\,\nu_\pm,
\qquad
\|e_\pm\|=1,
\]

and put

\[
c_\eta:=\langle e_+,e_-\rangle
=\frac{\eta Z_x(\eta)}{\sqrt{q_+q_-}}
\in[0,1].
\tag{7.1}
\]

The root/subtree decomposition of the resolvent columns defines probability vectors

\[
p_{0,\pm}=\eta q_\pm,
\tag{7.2}
\]

and, for every child `k`,

\[
p_{k,+}=q_+U_kC_kq_{+,k},
\qquad
p_{k,-}=q_-U_k(1-C_k)q_{-,k}.
\tag{7.3}
\]

Indeed the cavity equations imply

\[
p_{0,\pm}+\sum_kp_{k,\pm}=1.
\]

Let `c_{eta,k}` be the corresponding normalized child overlap. The positive-overlap recursion is exactly

\[
c_\eta
=\sqrt{p_{0,+}p_{0,-}}
+\sum_k\sqrt{p_{k,+}p_{k,-}}\,c_{\eta,k}.
\tag{7.4}
\]

Since every `c_{eta,k}` lies in `[0,1]`,

\[
c_\eta\le A_\eta
:=\sqrt{p_{0,+}p_{0,-}}
+\sum_k\sqrt{p_{k,+}p_{k,-}}
\le1.
\tag{7.5}
\]

The last inequality is Hellinger/Cauchy--Schwarz, with exact deficit

\[
1-A_\eta
=\frac12\left[
(\sqrt{p_{0,+}}-\sqrt{p_{0,-}})^2
+\sum_k(\sqrt{p_{k,+}}-\sqrt{p_{k,-}})^2
\right].
\tag{7.6}
\]

### Theorem 7.1 — uniform boundary separation for every interior `x`

For `alpha=1` and every fixed

\[
0<x<\frac12,
\]

there exist `delta_x>0` and `eta_x>0` such that

\[
\boxed{
\kappa_x(\eta)\le1-\delta_x
\qquad(0<\eta<\eta_x).
}
\tag{7.7}
\]

Equivalently,

\[
\boxed{
\limsup_{\eta\downarrow0}\kappa_x(\eta)<1.
}
\tag{7.8}
\]

#### Proof

By channel symmetry,

\[
\mathbb E\frac{q_++q_-}{2}=\mathbb E q.
\]

From (7.1) and (7.5),

\[
\kappa_x(\eta)
=\frac{\mathbb E[\sqrt{q_+q_-}\,c_\eta]}{\mathbb E q}
\le
\frac{\mathbb E[\sqrt{q_+q_-}\,A_\eta]}{\mathbb E q}.
\tag{7.9}
\]

Define the nonnegative defect

\[
D_\eta
:=\frac{q_++q_-}{2}
-\sqrt{q_+q_-}\,A_\eta.
\tag{7.10}
\]

Then

\[
1-\kappa_x(\eta)
\ge\frac{\mathbb E D_\eta}{\mathbb E q}.
\tag{7.11}
\]

Suppose, toward contradiction, that a sequence `eta_n downarrow 0` has `kappa_x(eta_n) -> 1`. Equation (6.8) keeps the denominator bounded away from zero and infinity, so (7.11) gives

\[
\mathbb E D_{\eta_n}\to0,
\qquad
D_{\eta_n}\to0
\quad\text{in probability}.
\tag{7.12}
\]

Now

\[
D_\eta
=\frac12(\sqrt{q_+}-\sqrt{q_-})^2
+\sqrt{q_+q_-}\,(1-A_\eta).
\tag{7.13}
\]

Let `U_(1)` be the largest Poisson radial mark and let `C_(1),q_{+,(1)},q_{-,(1)}` be its coin and child cavity pair. Such a largest mark is finite, positive and unique almost surely because

\[
\mathbb P\{U_{(1)}\le u\}=e^{-u^{-1/2}},
\qquad u>0.
\tag{7.14}
\]

Equations (7.6) and (7.13) imply the two lower bounds

\[
D_\eta\ge\frac12(\sqrt{q_+}-\sqrt{q_-})^2,
\tag{7.15}
\]

and

\[
D_\eta\ge
\frac12\sqrt{q_+q_-}
\left(\sqrt{p_{(1),+}}-\sqrt{p_{(1),-}}\right)^2.
\tag{7.16}
\]

The marginal convergence (6.7)--(6.9) makes the root cavity pairs and child cavity pairs tight, with every subsequential marginal limit supported on `(0,infinity)`. The law of `U_(1)` is fixed. Therefore, after a subsequence, the joint tuple

\[
(q_+,q_-,U_{(1)},C_{(1)},q_{+,(1)},q_{-,(1)})
\]

converges in distribution; use a Skorokhod representation for this finite tuple. From (7.12), (7.15), and (7.16), its limit must satisfy almost surely

\[
q_+=q_-
\tag{7.17}
\]

and

\[
p_{(1),+}=p_{(1),-}.
\tag{7.18}
\]

Since `U_(1)>0` and all cavity variables are positive, (7.3), (7.17), and (7.18) force

\[
C_{(1)}q_{+,(1)}
=(1-C_{(1)})q_{-,(1)}.
\tag{7.19}
\]

But the parent-edge coin `C_(1)` is independent of the child cavity pair and is fair on `{x,1-x}`. For any fixed positive pair `(r_+,r_-)`, at most **one** of the two coin values can satisfy

\[
Cr_+=(1-C)r_-
\]

when `x ne 1/2`: if both did, dividing the two equalities would force `x=1-x`. Hence the conditional probability of (7.19) is at most `1/2`, contradicting the almost-sure equality forced by (7.12). Therefore no sequence can have `kappa_x(eta)->1`, proving (7.8) and hence (7.7). `QED`

### Consequence for the transverse Hermitization response

Combining (5.8), (6.8), and Theorem 7.1,

\[
\boxed{
\limsup_{\eta\downarrow0}
\frac{\eta\chi_x^\perp(\eta)}{\mathbb E q_x(\eta)}<1
\quad(0<x<1/2),
}
\tag{7.20}
\]

whereas at the Hermitian endpoint the same ratio is exactly `1` for every `eta>0`.

For the concrete recovery pair `x=1/4` versus `x=1/2`, the joint-dependence defect therefore survives all the way to the regularization boundary in this normalized transverse susceptibility. This is stronger than the preceding run's fixed-`eta` statement.

What is **not** proved is that the raw coefficient

\[
\eta\chi_{1/4}^\perp(\eta)
\]

has a different limit from its endpoint counterpart: `E q_x` itself depends on `x`, and Theorem 7.1 supplies a qualitative, not explicit, `delta_x`. Thus no unregularized logarithmic-potential inequality and no ESD inequality is claimed.

**B29 outcome:** succeeded. The previous possible failure mode `kappa_x(eta) -> 1` as `eta downarrow 0` is rigorously excluded for every interior `x` at `alpha=1`.

## 8. Exact finite algebra self-check

Only after the analytic route above was developed did I build a checker for the finite algebra used in B5/B15 and the Hellinger identity used in B29.

Code:

`artifacts/hard7_2026-09-18/HARD7-02/2026-09-19T13-12-50Z__transverse-susceptibility-check.py`

creation commit:

`d2ff77a64c04b80d91c585d96b61f5e87364e55c`

Archived output:

`artifacts/hard7_2026-09-18/HARD7-02/2026-09-19T13-12-50Z__transverse-susceptibility-check.out`

creation commit:

`12f6ac5fbe1da8434ecd596df6849d9c4ffa9b0e`

The executed exact SymPy self-check verifies:

1. `h^2+d^2=1`, `hd=varepsilon`, and `d^2(1-d^2)=varepsilon^2`;
2. the bipartite identity `J R(i eta) J=-R(i eta)^*`;
3. the imaginary-shift determinant coefficient
   `-Tr(R_- J R_+ J)=Tr(R_- R_+^*)`;
4. equality of the local positive susceptibility with the channel overlap in the one-edge model;
5. the endpoint `d/d rho log det` formula (4.7) in an exact two-vertex model;
6. the algebraic Hellinger-affinity deficit identity.

Its final line is

`ALL_EXACT_CHECKS_PASS = True`.

This is explicitly a **self-check**, not an independent proof of the PWIT or boundary theorem.

## 9. What changed mathematically

The frozen source metric did not move, but the final recovery obligation changed materially.

Before this run the blocker was:

> the physical real-shift susceptibility is parity-signed, so the fixed-`eta` positive channel-coherence defect might be invisible to the logarithmic potential, and the defect might also vanish as `eta downarrow 0`.

After this run:

1. the full spectral shift is decomposed exactly as `-Re(z) I - i Im(z) J` between the two channels;
2. a pure imaginary shift probes the **positive** overlap `Z`, eliminating the parity cancellation exactly;
3. at `alpha=1`, the normalized positive susceptibility has a strict interior gap that is **uniform all the way to `eta=0`**;
4. the endpoint `x`-deformation has an exact second-order determinant formula, with independent edge signs averaged to a radial edge-local quadratic form.

The remaining source-level obstruction is now narrower:

\[
\boxed{
\text{turn the normalized transverse gap into a nonzero difference of the}
\atop
\text{raw unregularized logarithmic-potential curvature (or find an exact cancellation).}
}
\tag{9.1}
\]

For `x=1/4` this means either obtaining a quantitative bound strong enough to compare

\[
\eta\,\mathbb E Z_{1/4}(\eta)
=\kappa_{1/4}(\eta)\,\mathbb E q_{1/4}(\eta)
\]

with the endpoint value, or deriving another source-visible functional from the transverse block formula that avoids this normalization.

## 10. Honest labels and next-run rotation

Status remains **PARTIAL**. The source question is not called PROVED or REFUTED. No simulation is used to infer an infinite-volume statement. No sufficient hypothesis is relabeled necessary. No finite-tree identity is relabeled as the full planar ESD theorem.

This run used **B5/B15/B29**, different from final-recovery run 1's B3/B7/B11 and STUCK2's B1/B20/B30. If one further ordinary final-recovery execution occurs, it must use a different triple. A useful nonrepeating direction would be B17/B23/B27: identify the exact stable-law constant needed to beat the normalization, assume ESD equality and derive its forced curvature identity, and swap the order of `eta downarrow0` versus the `z`-directional second difference under a rigorously stated uniform-integrability condition.

If that next ordinary run leaves `S` unchanged, it is the third post-STUCK2 no-movement run and must end with the terminal handoff/rotation prescribed by Section I; no STUCK3 is permitted.

## 11. Capability honesty / ledger delta

No email, Drive, public posting, paid compute, workflow execution, scheduler mutation, neighboring-track edit, shared-root ledger edit, force push, or permission bypass was made.

```yaml
ledger_delta:
  track: HARD7-02
  target: Campbell-O'Rourke 2022 Question 1.8
  canonical_claim: operations/claims/CAMPBELL-OROURKE-2022-Q1.8.md
  status: PARTIAL
  metric: S
  before: 5
  after: 5
  movement: no movement
  section_I: final_recovery_sequence_run_2_after_STUCK2
  unchanged_streak_after_STUCK2: 2
  methods: [B5, B15, B29]
  new_exact_reduction: complex spectral shift becomes -Re(z)I - i Im(z)J between common-gauge channels
  new_theorem: alpha=1 interior normalized transverse coherence has limsup_eta_to_0 < 1
  endpoint_deformation: exact quadratic logdet coefficient at x=1/2
  remaining_obligation: quantitative/raw transverse curvature comparison or exact cancellation at eta_to_0
  exact_checker: artifacts/hard7_2026-09-18/HARD7-02/2026-09-19T13-12-50Z__transverse-susceptibility-check.py
  exact_output: artifacts/hard7_2026-09-18/HARD7-02/2026-09-19T13-12-50Z__transverse-susceptibility-check.out
  exact_check_result: ALL_EXACT_CHECKS_PASS=True
  runtime_model: GPT-5.6 Sol
  runtime_reasoning: UNVERIFIED
```
