Model actually running: **GPT-5.6 Sol. Reasoning level: UNVERIFIED — this is not GPT-6 at maximum, and I do not claim otherwise. No source-metric movement: `D_B=2 -> D_B=2`. Methods tried: B4 / B15 / B27.**

# HARD7-01 run 14 — weighted-Poincaré port: an exact \(\ell_4\) spectral obstruction and curvature-complementary extreme splits

Status: **PARTIAL / source OPEN / STUCK1 recovery execution 1**.

## 1. Continuity, ownership, required reads, and source sentinel

This invocation resumes the exact HARD7-01 target from

`runs/hard7_2026-09-18/HARD7-01/2026-09-19T09-04-12Z__weakB_stuck1_cone_spectral_port.md`

created at commit

`796ff801c1aca10928cf1e5793e71d693ba299e3`.

That report was the mandatory STUCK1 thinking-only run. It selected one recovery: port the sharp weighted-Poincaré/spectral mechanism from the solved rotationally invariant `(B)` theorem to the variable cone geometry forced by a convex homogeneous split. This run executes that recovery rather than restarting the literature survey or returning to the discarded radial-mixture route.

The active create-only canonical claim remains

`operations/claims/B-WEAK-EVEN-LOGCONCAVE.md`

with owner **HARD7-01**, status `CLAIMED / source OPEN / research PARTIAL only`. Repository-wide exact-name/alias searches for `(B)-conjecture`, `B-conjecture`, log-concavity of dilates, the claim ID, and the frozen metric recovered no competing canonical owner. The newest neighboring R02 state was also inspected; it is currently on an unrelated successor-admission gate and does not claim this target.

At run start I reread/reconciled:

- `operations/hard7_2026-09-18/CONTROL.md`;
- `operations/NEW_METHODS_2026-09-16.md`;
- `operations/new_methods_2026-09-16/OWNER_DIRECTIVE.md`;
- `probability_campaign_2026_09/INDEX.md` and `RANKING.md`;
- root `POSTED.md`, `RESULTS.md`, and `QUEUE.md`;
- `operations/claims/B-WEAK-EVEN-LOGCONCAVE.md`;
- the newest own HARD7-01 report above;
- the newest visible neighboring R02 report/commit;
- indexed intake/claim/alias searches.

The connector does not provide a trustworthy byte-stream of every large append-only intake JSONL in one bounded call, so I do not falsely claim a byte-for-byte reread of every row. I did check the current campaign/root surfaces, exact claim, neighboring state, and indexed intake/alias evidence.

### Exact source target retained

For every integer \(n\ge1\), every even log-concave probability measure \(\mu\) on \(\mathbb R^n\), and every origin-symmetric convex body \(K\), prove that
\[
t\longmapsto \mu(e^tK)
\]
is log-concave on \(\mathbb R\).

The frozen source quantity remains
\[
D_B:=\max\{d:\text{the exact weak `(B)` statement is proved for all admissible }(\mu,K)
\text{ in every }n\le d\}.
\]
Saroglou's planar theorem gives the verified source baseline
\[
\boxed{D_B=2}.
\]
This run proves structural lemmas for the homogeneous common-degree recovery but does **not** prove the unrestricted \(n=3\) source statement, so
\[
\boxed{D_B:2\longrightarrow2}.
\]
There is **no source-metric movement**.

### Fresh current-literature sentinel — 2026-09-19

I reran bounded current searches for the exact weak `(B)` statement and its standard aliases. The primary/current items recovered were:

1. D. Cordero-Erausquin and L. Rotem, *Improved log-concavity for rotationally invariant measures of symmetric convex sets*, Ann. Probab. 51 (2023), arXiv:2111.05110. Its introduction explicitly states the conjecture that every even log-concave measure has the `(B)` property, proves the rotationally invariant class, and says the proof uses new sharp weighted Poincaré inequalities.
2. C. Saroglou, *More on logarithmic sums of convex bodies*, Mathematika 62 (2016), arXiv:1409.4346. This gives the planar baseline.
3. S. Armeniakos and J. Ulivelli, *A strengthening of the dimensional Brunn-Minkowski conjecture implies the (B)-Conjecture*, arXiv:2602.23350 (2026). It proves an implication and hereditarily-convex cases, not the unrestricted source.
4. E. Putterman, *Sharp stability for the (B)-theorem*, arXiv:2608.08472 (2026). This concerns the already proved Gaussian theorem and its stability, not unrestricted even log-concave measures.
5. D. Cordero-Erausquin and A. Eskenazis, *Concavity principles for weighted marginals*, arXiv:2506.16941 (2025), for additional structured classes.

The bounded search recovered no paper claiming the full all-dimensional source statement. This is negative evidence from a bounded search, not a worldwide novelty certificate.

## 2. Recovery setup from run 13

Run 13 reduced the common-degree homogeneous correlation problem to a sharp angular variance inequality.

Let \(\phi,\psi\) be even convex \(C^2\), positively \(p\)-homogeneous functions of the same degree, let
\[
H=\phi+\psi,\qquad S_H=\{z:H(z)=1\},
\]
and let \(\nu_H\) be cone probability on \(S_H\). Put
\[
U(z)=\phi(z),\qquad 0\le U\le1,\qquad m=\mathbb E_{\nu_H}U.
\]
For \(X\) with density proportional to \(e^{-H(x)}\), cone polar coordinates give
\[
X=RZ,\qquad Y:=R^p\sim\Gamma(n/p,1),\qquad Z\sim\nu_H,\qquad Y\perp Z.
\]
Writing \(k=n/p\),
\[
\operatorname{Cov}(\phi(X),\psi(X))
=
k\Big(m(1-m)-(k+1)\operatorname{Var}_{\nu_H}(U)\Big).
\tag{2.1}
\]
Thus the common-degree correlation statement is exactly
\[
\operatorname{Var}_{\nu_H}(U)
\le
\frac{p}{n+p}m(1-m).
\tag{2.2}
\]

For the first unsolved test case \(n=3,p=2\), the target is
\[
\operatorname{Var}_{\nu_H}(U)\le \frac25m(1-m).
\tag{2.3}
\]

The question for this recovery is whether the sharp weighted-Poincaré mechanism from the rotationally invariant theorem can force (2.2) on an arbitrary cone geometry.

## 3. B4 — PROVE SOMETHING WEAKER, COMPLETELY: a spectral-transfer lemma for convex 2-homogeneous splits

This section gives a complete local theorem in the \(p=2\) common-degree slice. It is weaker than the source, but it identifies exactly what a successful spectral port would need.

Assume for now that \(H,\phi,\psi\) are \(C^2\) away from the origin and that
\[
A(z):=\nabla^2H(z)
\]
is positive definite on \(S_H\). Set
\[
B(z):=\nabla^2\phi(z).
\]
Convexity of \(\phi\) and \(\psi=H-\phi\) gives
\[
0\preceq B\preceq A.
\tag{3.1}
\]
Define
\[
P:=A^{-1/2}BA^{-1/2},\qquad a:=A^{1/2}z.
\]
By Euler's identity for 2-homogeneous functions,
\[
Az=\nabla H(z),\qquad z^\top Az=2H(z)=2,
\tag{3.2}
\]
and similarly
\[
z^\top Bz=2\phi(z)=2U(z).
\tag{3.3}
\]
Hence
\[
|a|^2=2,\qquad a^\top Pa=2U.
\tag{3.4}
\]

Use the Hessian metric \(A\) on the tangent space to \(S_H\). For a smooth function \(f\) on \(S_H\), let
\[
\Gamma_H(f)
\]
denote the squared norm of its tangential differential in the inverse \(A\)-metric. Under \(v\mapsto w=A^{1/2}v\), the tangent condition is \(w\perp a\). Since
\[
dU(v)=\langle Bz,v\rangle=\langle Pa,w\rangle,
\]
the tangent gradient is the orthogonal projection of \(Pa\) onto \(a^\perp\). Using (3.4),
\[
\Gamma_H(U)=|Pa-Ua|^2.
\tag{3.5}
\]

Because (3.1) is equivalent to \(0\preceq P\preceq I\),
\[
|Pa|^2=a^\top P^2a\le a^\top Pa=2U.
\]
Combining with (3.4)-(3.5),
\[
\boxed{\Gamma_H(U)\le 2U(1-U).}
\tag{3.6}
\]

This is the exact first-order energy restriction imposed by a convex split.

Now define the even spectral gap for this Hessian metric by
\[
\lambda_{\rm even}(H)
:=
\inf_{\substack{f\ {\rm even}\\ f\not\equiv{\rm const}}}
\frac{\int_{S_H}\Gamma_H(f)\,d\nu_H}
{\operatorname{Var}_{\nu_H}(f)}.
\tag{3.7}
\]
For our even \(U\),
\[
\lambda_{\rm even}(H)\operatorname{Var}(U)
\le
\mathbb E\Gamma_H(U)
\le
2\mathbb E[U(1-U)]
=
2\big(m(1-m)-\operatorname{Var}(U)\big),
\]
so
\[
\boxed{
\frac{\operatorname{Var}(U)}{m(1-m)}
\le
\frac{2}{\lambda_{\rm even}(H)+2}.
}
\tag{3.8}
\]

Substituting (3.8) into (2.1) with \(p=2\), \(k=n/2\), yields the explicit transfer estimate
\[
\boxed{
\operatorname{Cov}(\phi(X),\psi(X))
\ge
\frac n2\,m(1-m)\,
\frac{\lambda_{\rm even}(H)-n}{\lambda_{\rm even}(H)+2}.
}
\tag{3.9}
\]
Therefore
\[
\boxed{\lambda_{\rm even}(H)\ge n}
\tag{3.10}
\]
would be sufficient for the common-degree \(p=2\) correlation inequality.

### Calibration: the quadratic case

If \(H\) is quadratic, an invertible linear change of variables makes \(H(x)=|x|^2\). Then \(A=2I\), \(\nu_H\) is spherical measure, and
\[
\Gamma_H(f)=\frac12|\nabla_S f|^2.
\]
The first nonconstant even spherical harmonics have degree \(2\) and Laplace eigenvalue \(2n\), hence
\[
\lambda_{\rm even}(H)=n.
\]
Thus (3.10) is sharp at the quadratic model and reproduces the known Gaussian common-degree case.

**Outcome B4.** The weighted-Poincaré idea does transfer cleanly to an exact conditional theorem. The entire port collapses to whether the variable cone geometry keeps an even Hessian-metric gap at least \(n\).

## 4. B15 — BREAK THE SYMMETRY ON PURPOSE: the \(\ell_q\) cone destroys the universal gap

The quadratic calibration is too symmetric. To test whether (3.10) could hold for every convex 2-homogeneous \(H\), take the anisotropic family
\[
H_q(x)=\Big(\sum_{i=1}^n |x_i|^q\Big)^{2/q},\qquad q>2.
\tag{4.1}
\]
On
\[
S_q=\left\{z:\sum_i|z_i|^q=1\right\},
\]
cone measure has the standard Dirichlet coordinate law
\[
(W_1,\ldots,W_n):=(|Z_1|^q,\ldots,|Z_n|^q)
\sim {\rm Dirichlet}(1/q,\ldots,1/q).
\tag{4.2}
\]
Take the even degree-zero test function
\[
f(Z)=W_1.
\]

Away from the coordinate hyperplanes (a cone-measure null set), write \(u_i=x_i^{q-1}\). On \(S_q\),
\[
A=\nabla^2H_q
=
2(q-1)\operatorname{diag}(x_i^{q-2})
+
2(2-q)uu^\top.
\tag{4.3}
\]
For the degree-zero extension \(f=x_1^q/\sum_jx_j^q\),
\[
g:=\nabla f
=
q\big(x_1^{q-1}e_1-W_1u\big),
\qquad g\cdot x=0.
\tag{4.4}
\]
The rank-one term in (4.3) disappears in the inverse quadratic form because
\[
D^{-1}u=\frac{x}{2(q-1)},\qquad g\cdot x=0,
\]
where \(D=2(q-1)\operatorname{diag}(x_i^{q-2})\). Hence
\[
\Gamma_{H_q}(W_1)
=
g^\top A^{-1}g
=
\frac{q^2}{2(q-1)}W_1(1-W_1).
\tag{4.5}
\]

From (4.2),
\[
m=\frac1n,\qquad
\operatorname{Var}(W_1)
=
m(1-m)\frac{q}{n+q},
\tag{4.6}
\]
and
\[
\mathbb E[W_1(1-W_1)]
=
m(1-m)\frac{n}{n+q}.
\tag{4.7}
\]
Therefore the exact Rayleigh quotient of this even test mode is
\[
\boxed{
\frac{\mathbb E\Gamma_{H_q}(W_1)}
{\operatorname{Var}(W_1)}
=
\frac{nq}{2(q-1)}.
}
\tag{4.8}
\]
For every \(q>2\),
\[
\frac{nq}{2(q-1)}<n.
\]
Consequently the wholesale universal-gap port
\[
\lambda_{\rm even}(H)\ge n\quad\hbox{for every convex 2-homogeneous }H
\]
is false in this natural Hessian metric.

For the exact smallest witness \(n=3,q=4\),
\[
\operatorname{Var}(W_1)=\frac8{63},\qquad
\mathbb E[W_1(1-W_1)]=\frac2{21},
\]
\[
\Gamma(W_1)=\frac83W_1(1-W_1),\qquad
\frac{\mathbb E\Gamma(W_1)}{\operatorname{Var}(W_1)}=2<3.
\tag{4.9}
\]

This does **not** refute the source or the common-degree covariance statement. It refutes only the naïve attempt to port the rotational theorem by demanding the same universal even spectral gap on every variable cone.

### The first-order energy cap itself is still insufficient

The failure is stronger. In the same \(n=3,q=4\) model define
\[
U=\frac1{20}+\frac{17}{20}W_1.
\tag{4.10}
\]
Then \(0<U<1\), \(U\) is even, and \(\mathbb EU=1/3\). Its normalized variance is
\[
\frac{\operatorname{Var}(U)}{m(1-m)}
=
\frac{289}{700}
>
\frac25=\frac{280}{700},
\tag{4.11}
\]
with exact violation
\[
\frac9{700}.
\]

Yet \(U\) satisfies the **same pointwise first-order cap** (3.6):
\[
2U(1-U)-\Gamma(U)
=
\frac{289W_1^2-238W_1+57}{600}.
\tag{4.12}
\]
The quadratic has vertex
\[
W_1=\frac7{17}
\]
and exact minimum
\[
\boxed{\frac1{75}>0}.
\tag{4.13}
\]
So evenness, \(0\le U\le1\), and the sharp pointwise bound
\[
\Gamma_H(U)\le2U(1-U)
\]
still do not imply the target variance inequality.

Why is (4.10) not a source counterexample? Reconstruct the formal split
\[
\phi(x)
=
H_4(x)U(x)
=
\frac1{20}H_4(x)
+
\frac{17}{20}\frac{x_1^4}{H_4(x)},
\qquad
\psi=H_4-\phi.
\tag{4.14}
\]
At \(x=(1,1,1)\), direct exact differentiation gives
\[
\nabla^2\phi
=
\sqrt3
\begin{pmatrix}
16/9&-2/5&-2/5\\
-2/5&-1/9&16/45\\
-2/5&16/45&-1/9
\end{pmatrix},
\tag{4.15}
\]
and
\[
\nabla^2\psi
=
\sqrt3
\begin{pmatrix}
-2/9&-2/45&-2/45\\
-2/45&5/3&-4/5\\
-2/45&-4/5&5/3
\end{pmatrix}.
\tag{4.16}
\]
Thus
\[
\partial_{22}\phi(1,1,1)=-\frac{\sqrt3}{9}<0,
\qquad
\partial_{11}\psi(1,1,1)=-\frac{2\sqrt3}{9}<0.
\tag{4.17}
\]
Both convexity constraints fail. The exact bad angular mode is excluded not by the universal gap and not by the first-order cap, but by **second-order compatibility of the two convex summands**.

This is precisely the information the previous recovery lacked.

**Outcome B15.** The strongest obvious spectral port is false, but its failure exposes the missing invariant sharply: second-order convex-split integrability, not generic cone spectral geometry.

## 5. B27 — SWAP THE QUANTIFIERS: fix \(H\) first and maximize variance over convex splits

The source asks for every pair \((\phi,\psi)\). The previous routes tried to control all cone observables at once. Swap the order:

1. fix the sum \(H=\phi+\psi\);
2. fix the cone mean \(m=\mathbb E_{\nu_H}U\);
3. optimize only over convex decompositions of that fixed \(H\).

Define the fixed-mean split slice
\[
\mathcal C_m(H)
=
\left\{
\phi:
\begin{array}{l}
\phi\ \text{even, }C^2,\text{ 2-homogeneous},\\
\nabla^2\phi\succeq0,\ \nabla^2(H-\phi)\succeq0,\\
\mathbb E_{\nu_H}[\phi|_{S_H}]=m
\end{array}
\right\}.
\tag{5.1}
\]
At fixed mean,
\[
J(\phi):=
\operatorname{Var}_{\nu_H}(\phi|_{S_H})
=
\int_{S_H}(\phi-m)^2\,d\nu_H
\tag{5.2}
\]
is a convex functional of \(\phi\). Thus any search for a worst split is naturally driven toward boundary/extreme decompositions.

The useful fact is that the extreme boundary has a rigid curvature signature.

### Proposition 5.1 — curvature-complementarity of extreme splits

Let \(n\ge2\). Suppose \(H\) is even \(C^2\), 2-homogeneous and strictly convex away from the origin. If
\[
\phi\in\mathcal C_m(H),\qquad \psi=H-\phi,
\]
is an extreme point of the fixed-mean convex set \(\mathcal C_m(H)\), then there is no point \(z\in S_H\) at which both
\[
\nabla^2\phi(z)\succ0
\quad\text{and}\quad
\nabla^2\psi(z)\succ0.
\tag{5.3}
\]
Equivalently, at every direction \(z\in S_H\), at least one summand has singular Hessian:
\[
\boxed{
\det\nabla^2\phi(z)=0
\quad\text{or}\quad
\det\nabla^2\psi(z)=0.
}
\tag{5.4}
\]

#### Proof

Assume instead that both Hessians are positive definite at some \(z_0\). By evenness and continuity, there is an antipodally symmetric open angular patch \(\Omega\subset S_H\) around \(\{\pm z_0\}\), a compactly contained smaller patch \(\Omega'\Subset\Omega\), and \(\delta>0\) such that throughout the cone over \(\Omega'\),
\[
\nabla^2\phi\succeq\delta I,
\qquad
\nabla^2\psi\succeq\delta I.
\tag{5.5}
\]

Choose two nonzero, even, smooth angular bump functions \(g_1,g_2\) with disjoint support inside \(\Omega'\). Since \(\nu_H\) gives positive mass to open patches, choose \(c>0\) so that
\[
g:=g_1-cg_2
\]
has
\[
\int_{S_H}g\,d\nu_H=0.
\tag{5.6}
\]
Extend \(g\) 2-homogeneously by writing each \(x\ne0\) uniquely as
\[
x=r z,\qquad z\in S_H,\qquad r=\sqrt{H(x)},
\]
and setting
\[
\eta(rz)=r^2g(z).
\tag{5.7}
\]
The angular support is compactly contained in \(\Omega'\), so \(\nabla^2\eta\) is bounded on \(S_H\), is zero outside the cone over \(\Omega'\), and is degree zero under radial scaling. Hence for sufficiently small \(\varepsilon>0\),
\[
\nabla^2(\phi\pm\varepsilon\eta)\succeq0,
\qquad
\nabla^2(\psi\mp\varepsilon\eta)\succeq0
\tag{5.8}
\]
everywhere away from the origin: on the support this follows from (5.5) and boundedness of \(\nabla^2\eta\); off the support nothing changes. The perturbations are even and 2-homogeneous. By (5.6),
\[
\mathbb E_{\nu_H}[(\phi\pm\varepsilon\eta)|_{S_H}]=m.
\]
Thus both
\[
\phi_+=\phi+\varepsilon\eta,\qquad
\phi_-=\phi-\varepsilon\eta
\]
belong to \(\mathcal C_m(H)\), are distinct, and
\[
\phi=\frac12(\phi_++\phi_-),
\]
contradicting extremality. \(\square\)

### Consequence for the recovery

The exact \(\ell_4\) bad mode in Section 4 can satisfy the first-order energy inequality while still being impossible because its reconstructed pair violates the second-order cone
\[
0\preceq\nabla^2\phi\preceq\nabla^2H.
\]
Proposition 5.1 says that a genuinely extremal source-valid bad split, if one exists, cannot hide in the interior of this matrix interval. It must live on the curvature-complementary boundary, direction by direction.

The natural product/subspace equality models that calibrate (2.2) have exactly this flavor: one summand supplies curvature in some directions and the other supplies the complementary curvature. This turns the next task from “prove a universal Poincaré inequality for arbitrary cones” into the much narrower geometric problem:

> classify or estimate curvature-complementary convex decompositions of a fixed 2-homogeneous \(H\), especially in \(n=3\), strongly enough to bound the variance of \(U=\phi/H\).

No existence theorem for a global maximizer of (5.2) is asserted here; Proposition 5.1 is a local characterization of extreme points in the smooth fixed-mean slice. The convexity of \(J\) explains why this is the correct boundary to investigate.

**Outcome B27.** Swapping the quantifiers succeeds in isolating a source-specific second-order extremal structure that the generic spectral theory misses.

## 6. Exact finite verification

The finite rational core of Section 4 was checked with exact `Fraction` arithmetic and archived as:

- checker:
  `artifacts/hard7_2026-09-18/HARD7-01/2026-09-19T10-14-16Z__l4_spectral_obstruction_check.py`
  created at commit `680ca1e10a56a5aeeaadc109ebc00d2fe9b654e4`;
- output:
  `artifacts/hard7_2026-09-18/HARD7-01/2026-09-19T10-14-16Z__l4_spectral_obstruction_check.out`
  created at commit `0b92e20d5202369e997359a58ee7cee18985e5a2`.

The archived output verifies
\[
\operatorname{Var}(W)=8/63,\quad
\mathbb E W(1-W)=2/21,\quad
R(W)=2,
\]
\[
\frac{\operatorname{Var}(U)}{m(1-m)}=\frac{289}{700},
\quad
\frac{289}{700}-\frac25=\frac9{700},
\]
\[
\min_{0\le w\le1}\big(2U(1-U)-\Gamma(U)\big)=\frac1{75},
\]
and the two negative Hessian entries in (4.17). It ends

`ALL_EXACT_CHECKS_PASS = True`.

This is a **self-check**, not an independent audit.

## 7. What moved mathematically, and what did not

The frozen source metric did not move:
\[
D_B:2\to2.
\]

But the STUCK1 recovery did produce a substantive route change:

1. a complete spectral-transfer inequality (3.9), showing exactly how an even cone spectral gap would imply common-degree correlation;
2. an exact \(\ell_q\) calculation proving the naïve universal gap \(\lambda_{\rm even}\ge n\) is false for every \(q>2\);
3. an exact \(n=3,q=4\) angular witness that violates the desired \(2/5\) variance ratio while still satisfying the sharp first-order energy cap, proving that first-order Poincaré data alone are insufficient;
4. an exact Hessian calculation identifying why that angular witness is not source-realizable;
5. Proposition 5.1, which forces every smooth extreme fixed-mean convex split onto a curvature-complementary boundary.

This is **PARTIAL**. It is not a proof or refutation of weak `(B)`, and no paper/closure/audit claim is made.

This is the first ordinary research run after the STUCK1 thinking report. It does not trigger another Section-I episode by itself.

## 8. Next checkpoint

The next run should not retry the universal spectral-gap statement. It should work directly on curvature-complementary extreme splits in the simplest source-valid case \(n=3,p=2\).

Use a different, previously unused triple on the current weak-`(B)` problem:

- **B12 — FIND WHAT IS CONSERVED:** search for trace/rank/determinant identities forced by
  \(\nabla^2\phi+\nabla^2\psi=\nabla^2H\) under the pointwise singular-complement condition.
- **B14 — FIND THE GROUP ACTING:** quotient the \(n=3\) curvature-complementary split by linear changes preserving \(H\) and by \(\phi\leftrightarrow\psi\), looking for normal forms.
- **B25 — COUNT THE SAME THING TWICE:** integrate Euler/Hessian identities over cone measure and compare them with the Dirichlet/product equality model, aiming to turn rank complementarity into the target variance bound.

The concrete remaining obligation is:

\[
\text{For }n=3,p=2,\quad
\operatorname{Var}_{\nu_H}(U)\le\frac25m(1-m)
\]
for every **source-realizable** convex split, or a genuine source-valid counterexample.

## 9. Scheduler/model capability truth

The exposed native automation schema still offers task title, prompt, schedule or relative start, timing mode, and enabled state. It exposes **no binding model selector, no reasoning-effort selector, no authenticated per-run model/reasoning attestation, and no guaranteed duration field**.

Therefore `GPT-6 / maximum` remains prompt text only on this surface. This run actually identifies as **GPT-5.6 Sol**, while the reasoning level is **UNVERIFIED**. I do not claim GPT-6 maximum.

Changing the actual runtime model/reasoning would require the platform to expose and honor model-family and reasoning-effort fields in the scheduler/execution routing (and ideally return trustworthy run metadata). A repository edit cannot create that capability.

The historical P26 response `You cannot modify this task` is an authorization/context boundary, not a mathematical issue. Current repository reconciliation records that P26 was later editable from another authorized context. The lawful workaround is to use the same task's owning/authorized account, workspace, admin/API surface, an authorized ownership/permission repair or transfer, or platform support. Do not duplicate the task and do not bypass permissions.

Per the owner instruction, this run did **not** modify or create any scheduler task.

## 10. Structured ledger delta

```yaml
ledger_delta:
  track: HARD7-01
  lane: HARD_OUTSIDE
  canonical_claim: B-WEAK-EVEN-LOGCONCAVE
  source_status: OPEN_IN_CHECKED_PRIMARY_AND_CURRENT_LITERATURE_BOUNDED_SEARCH_ONLY
  status: PARTIAL
  metric:
    name: D_B
    before: 2
    after: 2
    movement: none
  methods:
    - B4
    - B15
    - B27
  recovery_state:
    prior: STUCK1_THINKING_RUN_COMPLETE
    current: STUCK1_RECOVERY_EXECUTION_1
  substantive_results:
    - spectral_transfer_bound_Cov_ge_n_over_2_times_m1m_times_lambda_minus_n_over_lambda_plus_2
    - exact_lq_even_Rayleigh_quotient_nq_over_2qminus2
    - exact_n3_q4_first_order_cap_insufficiency_gap_9_over_700
    - exact_reconstructed_split_nonconvexity_at_1_1_1
    - extreme_fixed_mean_splits_have_pointwise_curvature_complementarity
  exact_checker_commit: 680ca1e10a56a5aeeaadc109ebc00d2fe9b654e4
  exact_output_commit: 0b92e20d5202369e997359a58ee7cee18985e5a2
  closure: false
  independent_audits: 0
  remaining_obligation: classify_or_control_curvature_complementary_n3_p2_convex_splits_to_force_variance_ratio_at_most_2_over_5_or_find_source_valid_counterexample
  next_methods:
    - B12
    - B14
    - B25
```
