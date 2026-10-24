# account01/B07 r14 — full audit of the nine-eigenvalue / constant-400 source

Objective: `QFORM-FIXED-MULTIPLICITY-AUDIT-20260924`  
Run: `20260924T153324Z-account01-B07-fixedmult-nine-audit-r14`  
Role lens: ordered disjoint minors, bordered determinant identities, zero/singular seeds, volume-sampling multiplicities, random-cut expectation, restricted/global interpolation ranks, and the spectral-overlap theorem. The full source was nevertheless audited end to end.

## 0. Fresh control and source pin

Fresh `yspennstate/math-research-brain/main/AGENTS.md` and `scheduled_tasks/CURRENT_OBJECTIVE.md` were read before substantive work. The current objective supersedes the historical seventeen-eigenvalue baseline as the active source: the complete standalone candidate to audit is the nine-eigenvalue paper.

Pinned source:

- repository: `yspennstate/math-open-problems`;
- source commit: `eeb752c8943536541b34b42b8bf48e924f4d3d2f`;
- path: `proofnet24/QFORM-density/fixed-multiplicity-2026-09-24/improvements/interactive/20260924T145418Z-nine-400/paper.tex`;
- git blob: `19fb119877426b640b2c0dae19ec2f78a399fe11`;
- manifest SHA-256: `bf1caf6ae4b4bc33992f501c169b5dc6c795db757b0f6089eff9991391effdf3`;
- source size: 955 lines, 60,749 bytes.

I read all 955 source lines and the complete textual support package `README.md`, `NINE_400_AND_OVERLAP.md`, `AUDIT_NEW.md`, `MANIFEST.json`, `proof_map.csv`, `verify_new.py`, and `checks_new.json`.

## 1. Verdict

**Mathematical verdict: PASS WITH ONE LOCAL PRESENTATION REPAIR.**

The theorem

\[
s_9(A)\ge s>0\quad\Longrightarrow\quad
\|p_{X^TAX+b^TX+c}\|_{\infty,\mathrm{ess}}\le 400 K^2/s
\]

is sound in this review for arbitrary independent real coordinate densities bounded by `K`, arbitrary real symmetric `A`, arbitrary affine `b,c`, arbitrary dimension/signature/remaining spectrum, and rough laws. No moment, support, iid, Gaussian, log-concavity, connected-support, diagonal-basis, exact-rank, or post-rotation-independence assumption is used.

The only source-level GAP is a notation/selection issue in the negative tail of the hyperbolic-pair proof: the coordinate maximizing the positive exponential vector `u` need not also maximize the negative exponential vector `w`. The repair is to choose the physical coordinate independently on the two tails. Since `|u|=|w|`, the displayed cutoff and all constants are unchanged. This has no downstream mathematical impact.

The new spectral-tail/overlap theorem also receives **PASS**.

## 2. Complete source ledger

`PASS` means the displayed statement, proof transition, hypotheses, and downstream use were independently checked. `GAP` means a repair is needed; the exact repair and impact are given. `UNCHECKED` is used only for external/reproducibility matters not needed by the proof.

| Lines | Labels / content | Status | Independent reasoning / downstream consequence |
|---|---|---|---|
| 1–46 | preamble, notation, abstract | PASS | Scope matches the result actually proved. Essential boundedness is distinguished from continuity; eight and three are not claimed in the source. |
| 47–75 | `thm:main`, `cor:33`, normalized parameters | PASS | Quantifiers are complete. `d=3/40`, `p=1/400`, `h=2/25`, `kappa=4/625` are used consistently. Scaling target is `K^2/s`. |
| 76–164 | Fourier convention, Plancherel/inversion, power envelope, half-Riesz, rank perturbation | PASS | Fourier factors `2pi` and `1/(2pi)` are consistent. The Gaussian/Riesz representation is used under Tonelli with nonnegative majorants. Singular-value rank shifts are valid for nonsymmetric auxiliaries. |
| 165–215 | Schur spectral count and strict diagonal dominance | PASS | The fixed-threshold perturbative Schur proof works even for singular ambient `A`; no ambient inverse is assumed. The diagonal-dominance criterion is applied with strict positive margins later. |
| 216–252 | geometric rank-one Brascamp–Lieb | PASS | Heat-flow sign, integration by parts, Gaussian end state, and approximation of rough inputs close. Orthogonal transformations are deterministic integration devices, never claims of random-coordinate independence. |
| 253–297 | product projection and scalar Fourier powers | PASS | The projection-density proof correctly handles zero row weights by `sum_{b_i>0}(1-b_i)<=sum_i(1-b_i)=d`. Scalar Fourier-power exponents and scaling are correct. |
| 298–396 | physical-bank decoupling, regularized determinant, Cauchy–Binet volumes | PASS | Only literal independent coordinates are copied. The graph frame has the correct weights and regularizer `(2 pi e)^2`; the fourth root gives determinant exponent `-1/8`. Order-five is used for density, order-three only for half-potential at this stage. |
| 397–477 | grouped product-Fourier lemma | PASS | The phase-weighted image is `L^2` because its variation is dominated by an ordinary projected convolution with bounded density. Jensen is applied to mollified `L^2` norms before expansion. The pure `J` phase is discarded only after integrating original independent `I` coordinates. Weighted Holder is valid for the finite kernel measure even when not normalized. The joint map has Gram determinant `S^2 det(C_TC_T^T)`. The subset-entropy identity exactly cancels the weighted determinant/marginal loss. The estimate is uniform in the mollifier and passes to the genuine `L^2` image. |
| 478–527 | terminal physical hub and row-promotion tree | PASS | Promoted hubs are literal original coordinates; all hub-to-unpromoted couplings remain in `M_I`. Gram–Schmidt incident-volume identities are exact. The order-three endpoint gives a density, while order two is correctly only a full negative-half potential. Constants `C3<15`, `C2<14` check. |
| 528–562 | scalar square and definite pair | PASS | The square profile is conditional measure domination, not an independence assertion. The definite pair uses deterministic two-dimensional integration against the original joint density cap. |
| 563–589 | hyperbolic pair, positive tail | PASS | Hyperbolic parametrization and Jacobian `1/(2 sqrt D)` are correct. The positive tail selects one literal coordinate with `|u_i|>=|u|/sqrt2` and uses only its original density cap. |
| 590–606 | hyperbolic pair, negative tail | GAP — repaired | The source says to treat the negative tail with `w` but then reuses the coordinate symbol selected from `u`. A single coordinate need not maximize both vectors. Repair: choose `i_+` for `u` and independently `i_-` for `w`. Because `|u|=|w|`, both cutoffs satisfy the same displayed bound, so the envelope and every downstream constant are unchanged. |
| 607–662 | quarter-power concentration and log potential | PASS | Diagonal and sign-cut branches are exhaustive. The physical cross block norm is correct, Gaussian smoothing gives the stated `Gamma(3/8)` coefficient, the elementary bound `<5` is valid, and layer cake gives `4+4 log 5`. |
| 663–678 | ordered disjoint volumes and no-pivot entry cap | PASS | `V_r` is over ordered disjoint set pairs. Absence of a principal pair pivot gives `|A_ij|^2<p+d^2=13/1600<1/121`; symmetry is used only where stated. |
| 679–699 | volume-sampled interpolation / bordered determinant | PASS | Only nonsingular seeds receive determinant-squared sampling mass. For each off-diagonal extension, `det(border)^2=det(B)^2(A_lm-P_lm)^2` after sorting signs disappear. Singular seeds may have nonsingular extensions and are correctly excluded, so the aggregate relation is an inequality. Each ordered `(r+1)` disjoint pair is charged at most `(r+1)^2` times—one removed row and one removed column. |
| 700–715 | diagonal + interpolation completion | PASS | `D` is diagonal and vanishes on the seed; `E` has zero diagonal. The exact support decomposition gives global `rank R<=3r`; separately `R[L,L]=P[L,L]`, hence restricted rank `<=r`. These are not conflated later. |
| 716–742 | no-pivot spectral-to-volume proposition | PASS | Telescoping gives a bad ratio. The `r=0` Frobenius/operator bound contradicts a unit singular value. For `r=1,2`, nonsymmetric rank perturbation forces `r+1` large diagonal defects outside the seed; the exact diagonal-dominance slacks are `1131/2200` and `51/2200`, both positive, contradicting restricted rank `<=r`. |
| 743–753 | fair random coordinate cut | PASS | Each ordered disjoint `(S,T)` of size `k` survives exactly with probability `2^{-2k}=4^{-k}`. Linearity of expectation gives `E Z_k(A_{I,J})=4^{-k}V_k(A)` without any dimension factor. |
| 754–766 | no-pivot analytic consequences | PASS | The cut plus volume lower bounds give `Z_k^{-1/(2k)}<=25`; the reviewed marginal-free receivers yield `<70` half potential at five directions and `<375` density at nine. |
| 767–789 | scalar convolution kernel | PASS | Exact inverse-hyperbolic formulas and the interval-overlap rearrangement yield `J_0+2 log_+(1/|u|)` with no symmetry assumption on the input law. |
| 790–811 | full pair half-potential | PASS | Definite case follows from a density cap. In the indefinite case output normalization by `sqrt D` is correct; near/far split at `delta=1/64` gives `12+5 log2<16`, hence `16D^{-1/4}` uniformly in affine terms. |
| 812–833 | five-direction full half-potential | PASS | No-pivot/scalar/pair alternatives exhaust all matrices. The scalar Schur child needs only one surviving unit spectral direction for the logarithmic bound; the pair endpoint is a full half-potential, not a truncated one. |
| 834–860 | main nine-direction theorem and scaling | PASS | Recomputed branch bounds are `<375`, `<280`, `<383`, `<320`, `<80`, `<392.5`. At a scalar pivot the Schur complement retains eight large directions, enough for the five-direction proposition. Pair Schur loss is two. `Y=KX` and normalization by `s` give exactly `K^2/s`. |
| 861–907 | overlap definition and spectral-tail/overlap proof | PASS | The overlap sum is restricted to invertible disjoint seeds. For every sampled seed, `A-R=D+E` with `D` diagonal and `E` zero diagonal, so `||D+E||_F^2=||D||_F^2+||E||_F^2` exactly. Best rank-`3r` approximation gives the singular-value tail. The same-index bordered identity gives expected `D` energy exactly `W/V_r`; the off-diagonal sampling multiplicity gives expected `E` energy at most `(r+1)^2V_{r+1}/V_r`. |
| 908–926 | eight-direction overlap corollary | PASS | `s_8>=1` implies tail beyond six at least `s_7^2+s_8^2>=2`; hence `W>=2V_2-9V_3`. In the no-pivot chamber `V_2>=kappa^2`. The source correctly does not claim this alone is a density theorem. |
| 927–946 | threshold accounting and limitations | PASS | The manuscript correctly identifies nine as sufficient and eight/three as unproved within that source. |
| 947–955 | bibliography | UNCHECKED externally | Bibliographic metadata/priority was not independently researched in this run. Neither citation is an unproved dependency of the theorem because the specialized inputs are proved in the source. |

No mathematical proof line other than the repaired tail-coordinate presentation point remains unchecked.

## 3. Support package audit

- `README.md`: PASS. It pins the source and correctly distinguishes the source package from the conversation-delivered PDF.
- `NINE_400_AND_OVERLAP.md`: PASS as derivation/handoff; its theorem and constants match `paper.tex`.
- `AUDIT_NEW.md`: PASS as a self-audit, not independent certification.
- `MANIFEST.json`: PASS for recorded repository metadata. The raw SHA-256 was not independently recomputed from bytes in this connector run.
- `proof_map.csv`: PASS; labels/ranges match the 955-line source.
- `verify_new.py`: PASS by static code review. It checks exact interpolation/support/rank identities and exact constants, and labels spectral-tail floating tests as diagnostics.
- `checks_new.json`: PASS as the recorded finite diagnostic output. It reports 96 exact interpolation seeds, 8 exact aggregate overlap/sampling cases, and 8 numerical spectral-tail diagnostics.

**UNCHECKED in this run:** I did not re-execute `verify_new.py`; I did not independently rebuild/render the conversation-only PDF binary; I did not perform an exhaustive novelty search. None is a mathematical dependency of the proof.

## 4. Review-gate status of the exact nine/400 revision

Two genuinely separate exact-revision reviews already exist and were read after completing my own reconstruction:

1. account01/B01, commit `0a3f4521a74e46856317ba5b4645151917b4146e`, full 955-line PASS;
2. account02/B02, commit `1b284444c91119a0bcefdc082ec6ad4c86a8afb9`, full review with the same local hyperbolic-tail presentation repair and no mathematical defect.

This B07 report is a further independent full reconstruction. Thus the mathematical **two-review requirement for the exact nine/400 source is satisfied by existing artifacts**, subject to owner/release reconciliation. I do not mutate or self-award an owner-level validation/release flag.

## 5. Downstream status

The nine-direction theorem and the spectral-overlap theorem are safe dependencies for further threshold reduction. A separate improvement artifact in this same run independently reconstructs the newer multiplicity-eight candidate and records the present threshold frontier.
