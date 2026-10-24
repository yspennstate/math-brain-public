# account01/B01 r15 — independent full audit of the nine-eigenvalue / constant-400 revision

Objective: `QFORM-FIXED-MULTIPLICITY-AUDIT-20260924`.
Run: `20260924T150735Z-account01-B01-fixedmult-r15`.

## Source pin and scope

Fresh control changed during this run: the latest complete source to audit is the standalone nine-eigenvalue manuscript, not merely the preserved seventeen-eigenvalue baseline.

Pinned source audited here:

- repository: `yspennstate/math-open-problems`
- source commit: `eeb752c8943536541b34b42b8bf48e924f4d3d2f`
- path: `proofnet24/QFORM-density/fixed-multiplicity-2026-09-24/improvements/interactive/20260924T145418Z-nine-400/paper.tex`
- git blob: `19fb119877426b640b2c0dae19ec2f78a399fe11`
- SHA-256: `bf1caf6ae4b4bc33992f501c169b5dc6c795db757b0f6089eff9991391effdf3`
- length: 955 lines / 60,749 bytes.

I read the entire 955-line `paper.tex` and the complete current package: `README.md`, `NINE_400_AND_OVERLAP.md`, `AUDIT_NEW.md`, `MANIFEST.json`, `proof_map.csv`, `verify_new.py`, and `checks_new.json`. I also reread the preserved 790-line seventeen-eigenvalue baseline and its support package earlier in this same invocation before the fresh objective redirected the active review to the nine-eigenvalue revision.

**Verdict on the literal nine/400 manuscript: PASS.** I found no fatal or nonfatal mathematical defect and no source region remains `UNCHECKED` in this B01 review. This report is one independent end-to-end reconstruction of this revision; it does not by itself assign an owner/release `independently validated` status, which requires a genuinely separate second full review and reconciliation.

## Line-by-line / dependency audit

| Source lines | Labels / content | Status | Independent reasoning and downstream impact |
|---|---|---|---|
| 1–46 | preamble, abstract, scope | PASS | Abstract matches the theorem actually proved: arbitrary independent rough coordinate laws, arbitrary signature/dimension/affine terms, essential density bound, and only supporting progress at eight. No global continuity or three-eigenvalue claim is made. |
| 47–75 | `thm:main`, `cor:33`, parameters | PASS | Quantifiers are complete. `d=3/40`, `p=1/400`, `h=2/25`, `kappa=4/625` are used consistently. `s_17>=s` or `s_33>=s` implies `s_9>=s`. |
| 76–162 | Fourier convention, Plancherel/inversion, power envelope, half-Riesz | PASS | Fourier constants are mutually consistent. The half-Riesz derivation uses nonnegative Tonelli majorants and gives exactly the displayed coefficient; the `3/4` envelope integrates to `12 sqrt(u)`. |
| 163–213 | singular-value perturbation, Schur count, diagonal dominance | PASS | Rank inequalities apply to nonsymmetric auxiliaries. The singular Schur step uses a fixed threshold `t-delta`, so no moving-threshold ambiguity remains: `S_m->S` and finite-dimensional eigenvalue continuity give the exact count. |
| 216–296 | geometric BL, product projections, scalar Fourier powers | PASS | The heat-flow proof closes at both time endpoints. Orthogonal changes occur only in deterministic integration. Projection density `<=e^{d/2}` and the scalar Fourier-power estimate are proved from the original product coordinates, not rotated independence. |
| 298–396 | decoupling, regularized determinant, volume envelopes | PASS | The independent copy is taken only in a literal product bank. The graph frame, Jacobian, `d_i` cancellation, entropy factor `prod c_j^{-c_j/2}`, and regularizer `(2 pi e)^2` give determinant exponent `-1/8`. Order-five and order-three consequences have the correct distinct analytic uses. |
| 397–477 | grouped product-Fourier lemma | PASS | This is the most delicate new block and I reconstructed it independently. The phase-weighted image `mu_t` is genuinely `L^2`: its total variation is dominated by the ordinary convolution image, whose density is bounded because `M_J` has full row rank. Jensen is applied to **mollified** `L^2` norms before expansion. After duplicating only `X_J`, the pure `J` phase is discarded only after integrating the original independent `X_I` coordinates. Weighted Holder is valid for the finite measure `K_delta(M_JD)dP_D` even though its mass need not be one. The joint linear image has row-Gram determinant `S^2 det(C_TC_T^T)`, scalar powers are legal because `1/alpha_i>=2`, and the subset-entropy inequality cancels determinant-cardinality loss. The bound is uniform in the mollifier and the already-established `mu_t in L^2` permits the approximate-identity limit. No conditional-density or rotated-independence shortcut is present. |
| 478–527 | terminal hub block, marginal-free row promotion | PASS | Literal promoted rows remain original independent coordinates. Gram–Schmidt gives exact incident-volume identities at each promotion; all couplings to unpromoted left-bank coordinates remain in `M_I`. The `q=3` branch produces an integrable `|t|^{-3/2}` envelope and the `q=2` branch is correctly only a full half-potential estimate. Recomputing the promotion constants gives the displayed `C3` and `C2`. |
| 528–610 | scalar profile, definite/hyperbolic pairs | PASS | Conditional square profile is measure domination, not independence. Deterministic diagonalization in the definite case does not rotate the random product law. Hyperbolic parametrization and Jacobian are correct, and the tail uses an original coordinate. Exceptional critical values are handled through test functions/Tonelli. |
| 611–662 | quarter-power concentration | PASS | The scalar-diagonal and random-sign cross-block branches are exhaustive. The Gaussian smoothing coefficient is correctly bounded by five; the elementary Gamma estimate and rational comparisons are valid. Layer cake gives `L0=4+4 log 5` and excludes atoms. |
| 663–753 | disjoint volumes, sampling/completion, spectral-to-volume | PASS | `V_r` uses ordered disjoint pairs. Singular deleted seeds are correctly excluded from determinant-squared sampling, so the `(r+1)` count is an inequality. Completion has `rank R<=3r`, `rank R_LL<=r`, diagonal `D` zero on the seed, and zero-diagonal `E`. With the new parameters the exact diagonal-dominance slacks are `1131/2200` and `51/2200`, both positive. Thus orders two/three require five/nine directions. |
| 754–766 | no-pivot analytic consequences | PASS | Random cuts give `Z_k^{-1/(2k)}<=25`. Combining with the marginal-free receivers yields the stated `<70` full half potential at five directions and `<375` density at nine. |
| 767–811 | sharper kernel and full pair half potential | PASS | The exact `J(u)` formulas imply `J0+2 log_+(1/|u|)`. For an indefinite pair, output scaling by `sqrt(D)` is handled correctly, so the half potential scales as `D^{-1/4}`. The near/far split at `delta=1/64` gives `12+5 log2<16`; the rearrangement step is justified by interval layer cake and does not assume symmetric input laws. |
| 812–859 | five-direction half potential and main theorem | PASS | `prop:five` cleanly separates no-pivot, scalar-pivot and pair-pivot cases. In the main scalar branch the first Schur child has eight large directions and hence satisfies the five-direction proposition. Recomputed normalized branch bounds are `<375`, `<280`, `<383`, `<320`, `<80`, and `<392.5`; all are below 400. Affine terms remain arbitrary throughout. General `K,s` scaling gives exactly `400 K^2/s`: with `Y=KX`, `Qtilde=(K^2/s)Q`, hence scalar density scaling contributes `K^2/s`. |
| 861–926 | spectral-tail/overlap theorem and `s_8` corollary | PASS | For every sampled invertible seed, `A-R=D+E` with diagonal `D` and zero-diagonal `E`, hence exact Frobenius orthogonality. Best rank-`3r` approximation gives the singular-value tail. The expected `D` energy is exactly the invertible-seed overlap volume divided by `V_r`; expected `E` energy has the correct `(r+1)^2 V_{r+1}/V_r` upper bound. For `s_8>=1`, `T_6>=2`; together with `V_2>=kappa^2` this gives the displayed explicit overlap lower bound. It is correctly not promoted to an eight-direction density theorem. |
| 927–955 | threshold accounting, limitations, references | PASS | Limitations are accurate: the general eight- and three-eigenvalue assertions remain open. Citations are antecedent/attribution only; every specialized theorem used in the proof is proved inside `paper.tex`. |

## Sensitive calculations independently rechecked

1. **No-pivot spectral constants.** For `r=2`, `eps<=3h=6/25`; the diagonal lower bound and two off-diagonal row terms leave exactly `51/2200>0`, so the restricted-rank contradiction is valid at the claimed endpoint.
2. **Order-three row-promotion constant.** Fourier inversion of `min(1,B|t|^{-3/2})` gives `(3/pi)B^{2/3}`. Combining this with the `2^k` incident-volume loss reproduces the coefficients in the manuscript and the worst value `C3=3 sqrt(2)e(9/2)^(1/6)<15`.
3. **Order-two half potential.** The Riesz weight applied to `min(1,B/|t|)` contributes `8 sqrt(B)/sqrt(2 pi)`, giving `C2=8 sqrt(e)2^{-1/8}<14` in the diffuse branch; promotion branches are smaller.
4. **Full pair potential.** After scaling an indefinite pair by `sqrt(D)`, the near integral is `4 sqrt(delta)[8+log(16/delta)]`; at `delta=1/64` plus the far part it is `12+5 log2<16`, hence `16D^{-1/4}`.
5. **Final constants.** The actual checker values (`370.458...`, `360.847...`, `384.575...`) sit below the manuscript's rational envelopes. The finite suite is diagnostic evidence only, not part of this proof reconstruction.

## Support package

`README.md`, `NINE_400_AND_OVERLAP.md`, `AUDIT_NEW.md`, `MANIFEST.json`, `proof_map.csv`, `verify_new.py`, and `checks_new.json` are internally consistent with the pinned source. `checks_new.json` reports 96 exact interpolation seeds, 8 exact aggregate overlap/sampling cases and 8 floating spectral-tail diagnostics, all PASS on their stated finite scope. These checks do not certify the theorem in all dimensions.

## Status after this review

- **PASS:** the new standalone `s_9` / constant-400 theorem, with all original quantifiers.
- **PASS:** the spectral-tail/overlap inequality as a supporting theorem.
- **GAP:** multiplicity eight. The new algebra guarantees overlap-one mass, but no general product-preserving shared-coordinate analytic receiver is yet proved.
- **UNCHECKED:** none in the 955-line source or the listed package files for this B01 run.
- **FALSE:** none found in this revision.

The full three-eigenvalue conjecture and global continuity remain outside the proved scope. This B01 review is not formal verification or journal peer review.
