# R18 — Salem Bernoulli-convolution classification

**Run:** `2026-09-16_12-50-00_UTC__R18__tri-geometry-a7c3`  
**Repository:** `yspennstate/math-open-problems`, branch `master`  
**Status:** **OPEN.** No reciprocal-Salem parameter and no full classification is resolved in this run.

Target:
\[
\mu_\lambda=\operatorname{Law}\left(\sum_{j\ge0}\varepsilon_j\lambda^j\right),\qquad
\varepsilon_j\in\{\pm1\}\text{ iid uniform},\quad \lambda\in(1/2,1),
\]
and determine exactly when \(\mu_\lambda\ll\mathcal L^1\).

## 1. Continuity and sources

Read before working:

- repository `README.md`;
- `proofnet24/HOURLY20_PROTOCOL_2026-09-16.md`.

The protocol assigns R18 to this target and gives fallback track `proofnet24/R18-salem-bernoulli-convolutions`. A direct read of that track returned 404 and bounded code/commit searches found no prior R18 Salem report on `master`; this file therefore initializes the GitHub-backed R18 track. No missing chat/Drive state is imported as repository fact.

Primary literature checked:

- K. D. Nguyen, **Algebraic numbers and Fourier analysis: Salem's third problem**, arXiv:2604.18875v1 (20 Apr 2026), explicitly distinguishes the solved third problem from Salem's fourth problem on Bernoulli-convolution absolute continuity: https://arxiv.org/abs/2604.18875.
- P. P. Varju, **Absolute continuity of Bernoulli convolutions for algebraic parameters**, arXiv:1602.00261 / JAMS 32 (2019): AC for algebraic parameters sufficiently close to 1, quantitatively in Mahler measure, not a reciprocal-Salem classification: https://arxiv.org/abs/1602.00261.
- arXiv:1708.05544 is currently marked **withdrawn** with comment `Mistake in proof`; it is not used: https://arxiv.org/abs/1708.05544.
- A current preprint claiming Salem absolute continuity was inspected but is not treated as a verified resolution: its displayed Salem argument uses linear growth of a nontrivial unit-circle geometric sum, whereas \(|\sum_{k=1}^n\zeta^k|\le2/|1-\zeta|\) for \(|\zeta|=1,\zeta\ne1\). This records a proof-step obstruction, not a claim that the theorem statement is false.

The concrete test parameter remains the reciprocal of Lehmer's degree-10 Salem number,
\[
\theta_L\approx1.176280818259916,\qquad \lambda_L=\theta_L^{-1}\approx0.8501371309270435,
\]
which was not found decided in accepted literature in this bounded check.

Repository peers read:

1. `hard8_2026-09-16/HARD8-06/runs/2026-09-16/2026-09-16T09-40-33Z__report.md` (reciprocal Salem/Lehmer arithmetic);
2. `probability_1000/bernoulli_convolution_two_thirds_2026_09_07/bc23_L2_dictionary.tex` (independent Bernoulli-convolution L2 program).

## 2. R18-GH-C001 — quantitative translated neutral-orbit discrepancy

**PROVED**, using Salem's rational independence and a standard Baker-Wustholz lower bound.

Let the four neutral representatives of Lehmer's Salem number be
\[
z_s=e^{2\pi i\alpha_s},\qquad s=1,\dots,4.
\]
There exist \(C_L<\infty\), \(\delta_L>0\) such that every consecutive interval
\[
I=\{m,\dots,m+N-1\}
\]
has star discrepancy
\[
\boxed{D^*\left(\frac1N\sum_{n\in I}\delta_{(z_1^n,\dots,z_4^n)}\right)
\le C_LN^{-\delta_L}.}\tag{2.1}
\]
The bound is uniform in \(m\).

**Proof.** For nonzero \(h\in\mathbb Z^4\), put \(\zeta_h=\prod_s z_s^{h_s}\). Salem's theorem that \(\pi\) and the neutral arguments are Q-linearly independent gives \(\zeta_h\ne1\). Baker-Wustholz for the fixed algebraic numbers \(z_s\) gives
\[
|1-\zeta_h|\ge c_L(1+\|h\|_\infty)^{-\tau_L}.
\]
Thus, uniformly in the translated starting point,
\[
\left|\frac1N\sum_{n=m}^{m+N-1}\zeta_h^n\right|
\le \min\left(1,\frac{C_L(1+\|h\|_\infty)^{\tau_L}}N\right).
\]
Erdos-Turan-Koksma in dimension four, truncated at \(H\), gives crudely
\[
D^*\le C(H^{-1}+H^{\tau_L+4}/N).
\]
Taking \(H\asymp N^{1/(\tau_L+5)}\) proves (2.1), e.g. \(\delta_L=1/(\tau_L+5)\).

For consecutive intervals \(I,J\) of lengths \(N,T\), the Cartesian empirical measure is literally the product of the two empirical measures. Hence every axis box in \(\mathbb T^8\) has discrepancy
\[
\boxed{O_L(\Delta_{N,T}),\qquad \Delta_{N,T}=N^{-\delta_L}+T^{-\delta_L}.}\tag{2.2}
\]
This is deterministic product averaging, not an independence assumption on arithmetic phases.

## 3. R18-GH-C002 — exact phase geometry of the residual three-term alphabet

**PROVED.** For nonzero real coefficients define
\[
f_q(u,v)=q_1+q_2u+q_3uv,\qquad |u|=|v|=1,
\]
and set \(r_i=|q_i|\). For the residual magnitudes \(r_i\in\{1,2,3,4\}\), the 64 ordered triples split exactly into

- 34 strict-triangle classes, \(\max r_i<\sum_{j\ne i}r_j\);
- 18 degenerate-triangle classes, equality;
- 12 nontriangle classes, strict reverse inequality.

For a strict class, \(f_q=0\) has exactly two torus solutions. Explicitly
\[
\Re u=\frac{q_3^2-q_1^2-q_2^2}{2q_1q_2},\qquad
uv=\frac{-q_1-q_2u}{q_3}.
\]
In phase variables \(u=e^{i\alpha},v=e^{i\beta}\), at any zero
\[
\partial_\alpha f=-iq_1,\qquad \partial_\beta f=iq_3uv.
\]
The real Jacobian determinant has magnitude
\[
\boxed{J_q=2\,\operatorname{Area}(r_1,r_2,r_3)>0.}\tag{3.1}
\]
Across the finite strict alphabet,
\[
\boxed{J_q\ge\sqrt3/2,}\tag{3.2}
\]
attained by \((1,1,1)\).

For a nontriangle triple define
\[
d(q)=\max r_i-\sum_{j\ne i_{\max}}r_j>0.
\]
Then reverse triangle inequality gives the pointwise gap
\[
\boxed{|f_q(u,v)|\ge d(q).}\tag{3.3}
\]
The run-specific checker exhausts the finite alphabet and verifies (3.1)--(3.3) numerically/exactly where finite enumeration applies.

## 4. R18-GH-C003 — deterministic two-gap four-neutral small balls

**PROVED**, depending on C001--C002.

For positive gaps \(a,b\), define
\[
\mathbf A_q(a,b)=\left(q_1+q_2z_s^a+q_3z_s^{a+b}\right)_{s=1}^4
=\left(f_q(z_s^a,z_s^b)\right)_{s=1}^4.
\]
Let \(I,J\) be consecutive positive-integer intervals of lengths \(N,T\), and \(\Delta=\Delta_{N,T}\).

### Strict triangle

For all sufficiently small \(\eta\),
\[
\boxed{\frac1{NT}\#\{(a,b)\in I\times J:\|\mathbf A_q(a,b)\|_2\le\eta\}
\le C_L(\eta^8+\Delta).}\tag{4.1}
\]

**Proof.** By the inverse function theorem and (3.2), each scalar sublevel \(|f_q|\le\eta\) is contained in two axis rectangles of side \(O(\eta)\) around the two zeros; compactness controls the complement. Requiring all four neutral coordinates small therefore puts \((z^a,z^b)\in\mathbb T^8\) in at most \(2^4=16\) axis boxes, total Haar volume \(O(\eta^8)\). Apply (2.2). Because the alphabet is finite, constants are uniform over strict classes and signs.

### Degenerate triangle

For all sufficiently small \(\eta\),
\[
\boxed{\frac1{NT}\#\{(a,b)\in I\times J:\|\mathbf A_q(a,b)\|_2\le\eta\}
\le C_L(\eta^6+\Delta\eta^{-2}).}\tag{4.2}
\]

**Proof.** After fixed sign/phase shifts reduce to \(r_1=r_2+r_3\) and the unique scalar zero \(u=-1,v=1\). Put \(u=-e^{ix},v=e^{iy}\). Then
\[
\Im f=-(r_1x+r_3y)+O(|(x,y)|^2),
\]
\[
\Re f=\tfrac12[r_2x^2+r_3(x+y)^2]+O(|(x,y)|^3).
\]
The quadratic form is positive definite, so \(|f|\le\eta\) implies
\[
|(x,y)|\le C\sqrt\eta,\qquad |r_1x+r_3y|\le C\eta.
\]
Thus one scalar sublevel is a tilted strip of length \(O(\sqrt\eta)\), width \(O(\eta)\), coverable by \(O(\eta^{-1/2})\) axis squares of side \(O(\eta)\). Four neutral coordinates require \(O(\eta^{-2})\) boxes in \(\mathbb T^8\), with total volume \(O(\eta^6)\); summing the box discrepancy yields \(O(\Delta\eta^{-2})\).

### Nontriangle

By (3.3),
\[
\boxed{\|\mathbf A_q(a,b)\|_2\ge2d(q)}\tag{4.3}
\]
for every \(a,b\).

The exponents in (4.1)--(4.2) come from exact phase geometry, not independent-phase heuristics.

## 5. R18-GH-C004 — growing-truncation inverse-square bounds

**PROVED.** Put \(F_q(a,b)=\|\mathbf A_q(a,b)\|_2^{-2}\) at nonzero packets.

For strict triangles, (4.1) with \(\eta=U^{-1/2}\) gives
\[
\mathbb P(F_q>U)\le C_L(U^{-4}+\Delta),
\]
and layer cake yields
\[
\boxed{\mathbb E\min(F_q,K)\le C_L(1+\Delta K).}\tag{5.1}
\]
Thus the average is uniformly bounded up to \(K\asymp\Delta^{-1}\).

For degenerate triangles,
\[
\mathbb P(F_q>U)\le C_L(U^{-3}+\Delta U),
\]
so
\[
\boxed{\mathbb E\min(F_q,K)\le C_L(1+\Delta K^2).}\tag{5.2}
\]
The cutoff may grow to \(K\asymp\Delta^{-1/2}\).

For nontriangle classes,
\[
\boxed{F_q(a,b)\le[4d(q)^2]^{-1}}\tag{5.3}
\]
pointwise.

These are deterministic truncated inverse-square estimates. A sparse sequence deeper than the discrepancy scale can still obstruct the untruncated sum, so C004 is not an AC theorem.

## 6. R18-GH-C005 — exact transfer-operator sufficient criterion for L2 absolute continuity

**PROVED SUFFICIENT CRITERION; not verified for Lehmer in this run.**

Let \(\eta_\lambda=\mu_\lambda*\widetilde\mu_\lambda\), the law of \(X-X'\). Then
\[
Z\stackrel d=D+\lambda Z',\qquad
\mathbb P(D=-2,0,2)=(1/4,1/2,1/4).
\]
Define
\[
h_r(x)=\frac{\eta_\lambda([x-r,x+r])}{2r},
\]
and
\[
(L_\lambda f)(x)=\lambda^{-1}\left[
\tfrac14f((x+2)/\lambda)+\tfrac12f(x/\lambda)+\tfrac14f((x-2)/\lambda)
\right].
\]
Self-similarity gives the exact identity
\[
\boxed{h_r=L_\lambda h_{r/\lambda}.}\tag{6.1}
\]
If for some \(R>0\) there is a bounded nonnegative \(g\) with
\[
h_R\le g,\qquad L_\lambda g\le g,\tag{6.2}
\]
then \(\mu_\lambda\) has an \(L^2\) density.

**Proof.** For \(r_n=R\lambda^n\), positivity and (6.1)--(6.2) give \(h_{r_n}\le g\). Monotonicity of interval mass fills the scales between \(r_{n+1}\) and \(r_n\), giving a uniform bound on all small-scale \(h_r\). With \(\kappa_r=(2r)^{-1}1_{[-r,r]}\),
\[
\|\mu*\kappa_r\|_2^2
=\iint\frac{(2r-|x-y|)_+}{4r^2}\,d\mu(x)d\mu(y)
\le\frac{\eta_\lambda([-2r,2r])}{2r}=2h_{2r}(0).
\]
Thus \(\mu*\kappa_r\) is bounded in \(L^2\). Weak \(L^2\) compactness along \(r_j\downarrow0\), together with weak convergence \(\mu*\kappa_{r_j}\to\mu\), identifies \(\mu=f\,dx\) with \(f\in L^2\).

No certificate \(g\) satisfying (6.2) is proved here for \(\lambda_L\).

## 7. R18-GH-X001 — failed block-return contraction

**DISPROVED ROUTE.** For the expanding difference recursion
\[
X_{n+1}=\theta_LX_n+D_n,
\]
the checker finds floating final-return contractions on \([-2,2]\); e.g. at block length 5,
\[
q_5\approx0.341796875,\qquad \theta_L^5q_5\approx0.7697<1.
\]
Multiplying such block probabilities is invalid because the event only constrains the block endpoint: trajectories may leave \([-2,2]\) and re-enter. A valid iteration must keep the full state or prove a genuine positive-operator inequality such as C005. The numerical values are diagnostics only.

## 8. Peer audits

### HARD8-06 local discriminant energy — PASS

Source: `hard8_2026-09-16/HARD8-06/runs/2026-09-16/2026-09-16T09-40-33Z__report.md`.

Its Theorem 4.1 states
\[
v_p(\operatorname{Disc}R)\ge e^{-1}\sum_aN_a(N_a-1)
\ge e^{-1}(s^2/q-s).
\]
Independent check: equal-residue pairs in \(K/\mathbb Q_p\) have \(v_K(\beta_i-\beta_j)\ge1\), hence rationally normalized \(v_p\ge1/e\); the discriminant square contributes \(2/e\) per unordered pair. Summation gives the first inequality, and Cauchy-Schwarz gives \(\sum N_a^2\ge s^2/q\). **PASS.** No Lehmer-gap closure is imported.

### 2/3 Bernoulli exact dissociation lemma — PASS

Source: `probability_1000/bernoulli_convolution_two_thirds_2026_09_07/bc23_L2_dictionary.tex`.

For \(n_i=2^i3^{K-i}\), \(\varepsilon_i\in\{0,\pm1,\pm2\}\), if \(i_1\) is the largest nonzero coefficient index, the term \(\varepsilon_{i_1}n_{i_1}\) has unique minimal 3-adic valuation \(K-i_1\); every earlier term has larger valuation. Hence \(\sum\varepsilon_in_i\ne0\). **PASS.** This is also a useful warning: arithmetic orthogonality must be proved, not replaced by phase independence.

## 9. Reproducibility

Run artifact:

`proofnet24/R18-salem-bernoulli-convolutions/artifacts/2026-09-16_12-50-00_UTC__R18__tri-geometry-a7c3__checker.py`.

Seed: `202609161250`.

It certifies the 34/18/12 class count, minimum strict Jacobian \(\sqrt3/2\), 544 signed zero/Jacobian cases, and finite coefficient geometry. The fuller local run additionally checked 100,000 nontriangle phase samples, degenerate \(\eta^{3/2}\) scaling diagnostics, 1,000 finite-atomic transfer identities, and the failed-return diagnostic. Local full-output SHA-256: `2fdd20a5c1c2834e3639b02e7972ef81c6c7a7f8c54872b7b4de84fdeb2b6028`.

Finite checks do not replace C001--C005 proofs.

## 10. GitHub-backed ledger initialized

| ID | Status | Content |
|---|---|---|
| R18-GH-C001 | **PROVED** | Polynomial translated-interval discrepancy for Lehmer's four neutral phases |
| R18-GH-C002 | **PROVED** | Complete coefficient phase trichotomy and strict transversality |
| R18-GH-C003 | **PROVED** | Deterministic two-gap small-ball laws: strict \(\eta^8\), degenerate \(\eta^6+\Delta\eta^{-2}\), nontriangle gap |
| R18-GH-C004 | **PROVED** | Growing truncated inverse-square bounds |
| R18-GH-C005 | **PROVED SUFFICIENT CRITERION** | Bounded transfer superharmonic majorant implies an \(L^2\) density |
| R18-GH-X001 | **DISPROVED ROUTE** | Final-return block contraction is non-iterable due to exit/re-entry |
| Lehmer reciprocal AC/singularity | **OPEN** | no pointwise decision |
| New reciprocal-Salem AC class | **OPEN** | none claimed |
| Full Salem fourth classification | **OPEN** | main target |

## 11. Next attack

For the 34 strict-triangle classes, C003 localizes every very small two-gap packet near one of only \(2^4=16\) fixed algebraic phase targets. The next target is a **target-specific Baker lower bound**:
\[
\max_s\bigl(|z_s^a-u_s^*|+|z_s^b-v_s^*|\bigr)
\ge C(1+a+b)^{-\tau},
\]
unless an explicitly classified algebraic identity occurs. Unlike a generic moving target, each target is an algebraic function of the fixed small coefficient triple. Such a theorem would replace C003's discrepancy floor by a no-floor polynomial depth ceiling for strict classes.

The 18 degenerate classes need tangent-depth control, while the 12 nontriangle classes already have a fixed short-packet gap. In parallel, C005 suggests a certified interval-arithmetic search for a bounded superharmonic majorant for the exact difference operator at \(\lambda_L\); any certificate must prove \(L_\lambda g\le g\) globally, not merely on a floating grid.

**No closure claim.**
