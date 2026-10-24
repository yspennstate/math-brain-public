# account02/B02 — fixed-multiplicity full audit, run account02-B02-20260924T180837Z-auto11

Objective: `QFORM-FIXED-MULTIPLICITY-AUDIT-20260924`.

## Source pins

Preserved baseline:
- initial source commit `7c0d6e60946b19423e6400a12d34b473cf0591e2`;
- `manuscript.tex` git blob `183ccd294763214e6a707e8d4749ff9a8cf7006d`;
- manifest SHA-256 `9f3bdec0b88debe9a66076c7b4a5cc894fb14e69b89591a4107e785340f65e69`;
- 790 source lines.

Current standalone nine/400 candidate:
- source commit `eeb752c8943536541b34b42b8bf48e924f4d3d2f`;
- `improvements/interactive/20260924T145418Z-nine-400/paper.tex`;
- git blob `19fb119877426b640b2c0dae19ec2f78a399fe11`;
- SHA-256 `bf1caf6ae4b4bc33992f501c169b5dc6c795db757b0f6089eff9991391effdf3`;
- 955 source lines.

Independent nine-eigenvalue reconstruction:
- source commit `d3b12e27dc682a7fac0aa7edc1bd70de59cba8b1`;
- `proofnet24/QFORM-density/nine-eigenvalues-paper-2026-09-24/paper.tex`;
- git blob `823201f05363fcc60c38cce0feb5abb636f081d7`;
- SHA-256 `ea56bc35cff9815db71a9f5a620e0160e3a39cf53ff60c789707294d53240eba`;
- 711 source lines.

Fresh repository snapshot used for continuation search: master observed through `2c53bad698695caee235bae9534d5c69cad1b695`. Owner-control content remained blob `194c09609c2ce750efaa9634a0849b5a27ff651c`.

## Verdict

**Baseline 17 theorem: PASS after one local hyperbolic-tail presentation repair.**

**Nine/400 theorem: PASS after the same local hyperbolic-tail presentation repair.**

**Independent nine/400 reconstruction: PASS after the same local hyperbolic-tail presentation repair.** Its accompanying `AUDIT.md` saying that no gap exists is too strong at this one point.

No theorem in this audit proves the unrestricted three-eigenvalue conjecture. Global continuity remains separate from essential boundedness in pivot branches.

The later multiplicity-eight `<349 K^2/s` replacement at corrected commit `e9a425b9ec3455dfe13b787fb259dec11aa1b176` is mathematically consistent in this B02 review after the same hyperbolic repair; this file does **not** change owner/release status or self-award the two-review gate.

## Line ledger: preserved 790-line baseline

| Lines | Status | Check / impact |
|---|---|---|
| 1–46 | PASS | packages, notation, title and theorem setup; no mathematical hidden hypothesis. |
| 47–61 | PASS | quantifiers and main/corollary statements; density means essential supremum; scaling target is (K^2/s). |
| 62–90 | PASS | architecture and Fourier convention; continuity scope is not conflated with bounded density. |
| 91–160 | PASS | Plancherel (2\pi), inversion (1/(2\pi)), Gaussian regularization, power envelope and half-Riesz normalization rederived. |
| 161–220 | PASS | singular-value perturbation, rank shift, Schur spectral count including singular limit, strict diagonal dominance. |
| 221–301 | PASS | geometric Brascamp–Lieb heat flow, rough limiting steps, product projections, scalar Fourier powers. In the projection proof the mathematically correct step after zero (eta_i) are removed is (sum_{eta_i>0}(1-eta_i)le d); this is a presentation repair only. |
| 302–400 | PASS | independent-copy decoupling, determinant regularizer, Cauchy–Binet crossing volumes and the (-1/8) determinant exponent. |
| 401–436 | PASS | scalar-square and definite-pair changes of variables, including the (pi) Jacobian constant. |
| 437–482 | **GAP (local, repairable)** | hyperbolic pair. Positive tail chooses a physical coordinate for (u); the negative tail switches to (w) but lines 472–474 reuse the positive-tail coordinate bound. Equal norms do not force the same coordinate to be large. Repair: choose (i_+) with (|u_{i_+}|ge\rho_0/\sqrt2) and independently (i_-) with (|w_{i_-}|ge\rho_0/\sqrt2). Both cutoffs obey the same numerical bound, so every stated constant and every downstream branch is unchanged. |
| 483–525 | PASS after preceding repair | quarter-power concentration and log moment; physical coordinate cut and Gaussian smoothing normalization checked. |
| 526–645 | PASS | pivot/volume definitions, bordered determinant sampling, nonsymmetric completion, global rank (le3r) versus restricted rank (le r), spectral-to-volume contradiction, random cut and no-pivot estimates. |
| 646–715 | PASS after preceding repair | singular kernels, pivot half-potential and nine-direction half-potential. Full versus truncated half moment is handled correctly. |
| 716–749 | PASS after preceding repair | final 17-eigenvalue case split and (Y=KX), (A/s), output scaling (K^2/s). |
| 751–781 | PASS | threshold accounting, limitations and regularity scope are accurate. |
| 782–790 | UNCHECKED | bibliographic attribution only; not a proof dependency. |

No source line outside the bibliography is left mathematically unclassified.

## Line ledger: current 955-line nine/400 source

| Lines | Status | Check / impact |
|---|---|---|
| 1–72 | PASS | theorem quantifiers, normalization parameters and architecture. |
| 73–213 | PASS | Fourier identities, half-Riesz constant, singular-value and Schur lemmas, dominance. |
| 214–296 | PASS | heat-flow Brascamp–Lieb, product projection and integrated scalar Fourier powers. The zero-weight projection inequality is written correctly here. |
| 298–395 | PASS | two-copy decoupling, regularized determinant and volume envelopes. |
| 397–526 | PASS | grouped mollified-(L^2) compiler, weighted Hölder on the finite non-probability measure, entropy inequality, literal-row promotion, terminal hub and marginal-free (E_3/E_2) receivers. All promoted variables remain original coordinates. |
| 528–561 | PASS | square and definite-pair profiles. |
| 562–608 | **GAP (local, repairable)** | hyperbolic pair, specifically lines 598–600. The negative tail says to use (w) but then cites the coordinate bound chosen for (u). Choose a new physical coordinate for (w); constants unchanged. |
| 610–661 | PASS after repair | quarter-power concentration and logarithmic moment. |
| 663–765 | PASS | volume sampling, nonsymmetric completion, (4k-3) rank accounting, random cut and no-pivot consequences. |
| 767–859 | PASS after repair | full pair half potential, five-direction half potential, all final nine/400 branches and scaling. |
| 861–943 | PASS | overlap-tail theorem and threshold accounting. The overlap theorem is algebraic support, not by itself an (s_8) density theorem. |
| 944–955 | UNCHECKED | bibliography attribution only. |

The support package `AUDIT_NEW.md`, `MANIFEST.json`, `proof_map.csv`, `verify_new.py`, and `checks_new.json` is present on current master and its finite diagnostics agree with the stated arithmetic. Diagnostics are not substituted for proof.

## Line ledger: independent 711-line reconstruction

| Lines | Status | Check / impact |
|---|---|---|
| 1–94 | PASS | statement, scaling and architecture. |
| 95–199 | PASS | Fourier/conditioning/linear algebra, including singular Schur limit. |
| 200–267 | PASS | Brascamp–Lieb projection cap and scalar Fourier powers. |
| 268–417 | PASS | grouped crossing-volume decay, entropy and heavy-row promotion; constants agree algebraically with the 955-line source. |
| 418–439 | PASS | square and definite pair. |
| 440–467 | **GAP (local, repairable)** | line 462 says “same argument with (u')” but the following cutoff sentence still invokes the coordinate selected for (u). Use independent indices (i_+), (i_-). This is the same repair as above, not an independent theorem defect. |
| 469–535 | PASS after repair | concentration, exact singular kernels and full pair half potential. |
| 537–611 | PASS | disjoint-minor sampling/completion and spectral-to-volume proof. |
| 613–670 | PASS after repair | no-pivot, five-direction half potential, final (s_9) theorem and scaling. |
| 672–685 | PASS | limitations and the exact (E_2)-only logarithmic counterexample. |
| 686–711 | UNCHECKED | bibliographic attribution only. |

The two independent write-ups therefore agree on the substantive grouped Fourier mechanism, but they also share the same small hyperbolic-tail coordinate-selection slip. This is a real cross-paper audit finding because the independent paper’s own audit records the lemma as gap-free.

## B02 normalization and exact-law checks

1. **Scalar Fourier exponent is sharp.** For the cap-one Gaussian
[
f(x)=e^{-pi x^2},qquad widehat f(t)=e^{-t^2/(4pi)},
]
one has exactly
[
int_{mathbb R}|widehat f(t)|^p,dt=rac{2pi}{sqrt p}.
]
Thus the (p^{-1/2}) exponent in the scalar Fourier-power lemma cannot be improved for the allowed class merely by changing constants.

2. **Convolution cap is sharp.** If (X,X') are uniform on ([-1/2,1/2]), (X-X') has triangular density ((1-|x|)_+), whose supremum is exactly one.

3. **Projection benchmark.** For two such uniforms, ((X_1+X_2)/sqrt2) has density peak (sqrt2). Hence any universal scalar projection constant is at least (sqrt2); the self-contained Brascamp–Lieb proof’s (sqrt e) is safe but not sharp.

4. **Order two cannot be an (L^infty) endpoint.** The same uniform law has (X^2) density (s^{-1/2}) on ((0,1/4)), hence
[
p_{X_1^2-X_2^2}(0)=int_0^{1/4}rac{ds}{s}=infty.
]
This matches the grouped Fourier endpoint (|t|^{-1}) at total order two: absolute Fourier inversion diverges logarithmically.

5. Numerically recomputed source constants:
[
C_3=14.818337662843ldots,qquad
C_2=12.095072570796ldots.
]

## Audit of the fresh two-source shared-bank packet

Fresh account03/B18 files at commits `e12bf29...` through `37c3ed...` propose
[
Q=U_1T_1(V)+U_2T_2(V)+H(V)
]
with a rank-two slope matrix and claim (16sqrt2 K^2det(CC^T)^{-1/4}).

- dependent two-slope reciprocal-half-moment lemma: **PASS**;
- fixed-slope Fourier (L^1) step (2pi K/sqrt{|s_1s_2|}): **PASS**;
- slope marginal/joint density principle: **PASS**;
- the particular constant (16sqrt2): **UNCHECKED as a self-contained source claim**, because it needs the sharp one- and two-dimensional product-projection constants and the B18 packet does not prove or source-pin them. The canonical self-contained projection theorem gives (sqrt e) and (e), which yields the fully source-closed constant (16sqrt e) instead. This repair is recorded in the companion improvement file.

This distinction is only a constant issue; the theorem’s exponent and mechanism are sound.

## Later multiplicity-eight replacement

I also checked the corrected `s_8<349` report at `e9a425b9ec3455dfe13b787fb259dec11aa1b176` against the audited nine-source machinery and the later B16 exact review.

Key independently recomputed quantities are:
[
C_3=14.818337662843ldots,quad C_2=12.095072570796ldots,
]
inner (s_5) branches (52.292,51.947,52.487), outer large-(V_3) branch (348.153), scalar pivot (348.246), definite pair (20.839), indefinite pair (127.795), and terminal incident branch (49.817). The corrected collar determinant is
[
delta=0.1157957451ldots>23/200,qquad
g>delta^2/2>529/80000.
]
The exact two-high comparison and one-high diagonal-dominance margins are positive.

Verdict in this review: **PASS after the inherited hyperbolic-tail repair**. I do not change owner/release status here; the full candidate gate remains an external synthesis decision.

## Downstream impact and next obligation

The current analytic frontier below eight/seven is not a missing scalar-Fourier constant. Order-two grouped Fourier decay is exactly at the logarithmic endpoint, and the uniform difference-of-squares law shows that this obstruction can be real. The next receiver must spend shared-coordinate structure or an additional independent physical factor.

The companion improvement file proves two such safe subreceivers and supplies a source-valid obstruction showing why arbitrary source-source quadratic curvature cannot simply be ignored.
