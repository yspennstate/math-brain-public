# fleet01/B01 r14 — full baseline audit and independent threshold-nine reconstruction

Objective: `QFORM-FIXED-MULTIPLICITY-AUDIT-20260924`  
Run: `20260924T141042Z-fleet01-B01-fixedmult-r14`

## Source pin and coverage

Pinned mathematical source:

- repository: `yspennstate/math-open-problems`
- baseline source commit: `7c0d6e60946b19423e6400a12d34b473cf0591e2`
- manuscript path: `proofnet24/QFORM-density/fixed-multiplicity-2026-09-24/manuscript.tex`
- git blob: `183ccd294763214e6a707e8d4749ff9a8cf7006d`
- SHA-256: `9f3bdec0b88debe9a66076c7b4a5cc894fb14e69b89591a4107e785340f65e69`
- size: 47,883 bytes / 790 lines.

I reread the complete 790-line manuscript in this run, together with `README.md`, `AUDIT.md`, `proof_map.csv`, `SOURCE_MANIFEST.json`, `verify.py`, `checks.json`, and the current `DELIVERY_STATUS.md`. The manuscript blob is unchanged on current `master`. The finite checker reports PASS on its stated exact/numerical cases, but I treat it only as diagnostics, not proof.

**Baseline verdict: PASS.** No source line is left `UNCHECKED`; I found no fatal or nonfatal mathematical gap in the literal 17-eigenvalue proof. One point I classified too cautiously in my preceding B01 run—the singular Schur limiting paragraph—is in fact sound as written; the rank-only argument I supplied remains a useful optional simplification, not a necessary repair.

## End-to-end line audit

| Source lines / labels | Status | Independent reasoning and downstream impact |
|---|---|---|
| 1–46, preamble/abstract | PASS | Scope matches the paper: arbitrary independent real densities, indefinite symmetric matrices, no moment/support/log-concavity assumptions. Abstract accurately describes the algebraic auxiliaries and does not claim continuity globally. |
| 47–79, `thm:main`, `cor:33`, architecture | PASS | Quantifiers are complete. The theorem claims essential density bound only. The fixed constants `eta=1/100`, `kappa=1/80^2` are used consistently. `s_33>=s` implies `s_17>=s`, so the corollary is immediate. |
| 81–160, `lem:fourier`, `lem:envelope`, `lem:riesz` | PASS | Fourier convention, Plancherel factor `2 pi`, inversion factor `1/(2 pi)`, Gaussian identity, and half-Riesz coefficient are mutually consistent. Tonelli is applied only to nonnegative majorants; the weighted integral for exponent `3/4` is exactly `12 sqrt(u)`. |
| 161–181, `lem:rank` | PASS | Approximation-number formula proves both perturbation and rank inequalities for nonsymmetric matrices; this is the correct tool later for nonsymmetric `R,E`. |
| 183–207, `lem:schur` | PASS | Invertible case follows from the complementary compression of `A^{-1}`. For singular `A`, put `A_m=A+eps_m I`, `eps_m->0`. If `q=N_A(t)-k>0`, the manuscript inequality gives `s_q(S_m)>=t-|eps_m|`; because `S_m->S`, singular-value continuity gives `s_q(S)>=t`. Hence `N_S(t)>=q`. The moving threshold therefore loses nothing. My prior B01 rank-only decomposition `A=UBU^T+diag(0,S)` is an optional shorter proof, not a source repair. |
| 209–217, `lem:dd` | PASS | Standard maximum-coordinate proof; symmetry is not used, as required later. |
| 221–255, `thm:bl` | PASS | Heat-flow differentiation gives the nonnegative square defect from the Parseval frame. Compact-support Gaussian tails justify differentiation/integration by parts; the `t->infinity` Gaussian limit and `t->0` Fatou step are valid. |
| 258–301, `lem:projection`, `lem:scalar-fourier` | PASS | Orthogonal completion is used only inside deterministic integration, not to assert rotated independence. After rows with `b_i=0` are dropped, one may write `sum_{b_i>0}(1-b_i)<=sum_i(1-b_i)=d`; this is exactly enough for `e^{d/2}`. Scalar Fourier powers follow from a genuine product projection of the `2m` original signed coordinates. |
| 303–400, `lem:decoupling`, `thm:determinant`, `cor:vol-fourier` | PASS | Copies occur only in an original-coordinate bank, so the difference coordinates remain independent with cap-one densities. The graph frame, Jacobian, `d_i` cancellation and regularizer `alpha=(2 pi e)^2` give determinant exponent `-1/8`. Order five gives integrable `|t|^{-5/4}`; order three is used only with the Riesz weight. |
| 401–434, `lem:square`, `lem:definite` | PASS | Scalar profile is a conditional measure domination statement. The deterministic two-dimensional rotation in the definite-pair integral does not rotate the random product law. |
| 437–482, `lem:hyperbola` | PASS | Hyperbolic parametrization has Jacobian `1/(2 sqrt(D))`; the tail estimates use an original coordinate, and the critical level is handled through test functions/Tonelli rather than pointwise rough conditional densities. |
| 485–525, `lem:quarter` | PASS | Diagonal-large branch and random-sign cross-block branch are exhaustive. Gaussian smoothing with the rank-one determinant bound gives the stated quarter-power small-ball estimate. The layer-cake logarithmic bound follows and excludes atoms. |
| 528–564, `def:pivot-volume`, `lem:sampling` | PASS | `V_r` uses ordered disjoint pairs. Determinant-squared sampling sees only invertible seeds. Singular seeds can have nonsingular extensions, so the manuscript correctly states an inequality, not equality, in the `(r+1)`-minor count. |
| 566–580, `lem:completion` | PASS | `D=0` on the seed, `E` has zero diagonal, `R_LL=P_LL`, `rank R_LL<=r`, while globally `rank R<=3r`; no symmetry of `R,E` is assumed. The support decomposition of `R-P` into rows `T` plus columns `S` is exact. |
| 582–619, `prop:volume` | PASS | The telescoping ratio step covers zero volumes. For `r>0`, `s_m(A-E)>=1-eps`, then rank `R<=3r` forces at least `r+1` large diagonal entries of `D`; because `D` vanishes on the seed they lie in `L`. Strict diagonal dominance of `R[H,H]` contradicts the restricted rank `<=r`. This is the key reason `4k-3`, rather than a global `6k`-type count, suffices. |
| 621–645, `lem:cut`, `cor:no-pivot` | PASS | Every ordered disjoint `k`-minor survives a fair cut with probability `4^{-k}`. The resulting crossing-volume powers and constants are correct: `k=3` gives a full half-potential; `k=5` gives a bounded continuous density. |
| 647–674, `lem:kernels` | PASS | The two singular integral bounds have the correct truncation and logarithmic behavior. The shifted logarithmic kernel is maximized by aligned interval superlevel sets. |
| 676–714, `prop:pivot-H` | PASS | Scalar, definite-pair, and indefinite-pair pivots exhaust the definition. Scalar pivot uses a Schur remainder with one surviving unit direction; pair bounds are conditional measure bounds and survive averaging. Determinant-dependent logarithms are handled by the explicit scalar maximum. |
| 716–724, `prop:nine` | PASS | Pivot branch uses only the two-direction hypothesis required by `prop:pivot-H`; no-pivot branch uses the already-proved order-three full half-potential. The tail outside distance one contributes at most one, so full versus truncated half potentials are not conflated. |
| 726–749, main theorem proof | PASS | No-pivot `s_17` uses order five. Scalar pivot loses one direction and leaves at least sixteen, hence enough for `prop:nine`. Pair pivots are paid directly / by one surviving Schur direction. All branches keep arbitrary affine terms. |
| 751–790, threshold discussion, limitations, references | PASS | Limitations are accurate: no `s_3` theorem and no global continuity claim. Citations are antecedent/attribution only; all specialized inputs used by the proof are proved in the manuscript. |

### Scaling check

For general `K,s`, put `Y=KX`. Each `Y_i` has density at most one. The manuscript variable

`Qtilde=Y^T(A/s)Y+(K/s)b^T Y+(K^2/s)c`

satisfies `Qtilde=(K^2/s)Q`, so `Q=(s/K^2)Qtilde`. Therefore a normalized density cap `C` becomes exactly `C K^2/s`. This proves the advertised homogeneity and confirms that no hidden normalization of `b,c` is needed.

## Independent reconstruction of the current nine-eigenvalue replacement

I did not use a peer PASS as a premise. I checked the complete fleet02/B01 replacement argument equation-by-equation against the baseline inputs.

### Grouped product-Fourier compiler — PASS

For disjoint original banks `H,I,J`, a `k`-dimensional product projection `W`, a full-rank `k`-row map into the `J` bank, and residual crossing rows with weighted `ell`-volume `Z_ell`, the complex pushforward of `e^{itF}dP_H` has `L^2` norm squared at most the projection density cap. Plancherel at scale `2t` contributes `(pi/|t|)^k`. Expanding the light-bank `L^2` norm uses an independent copy only of the original `J` bank; arbitrary same-bank phases are retained or cancel in modulus, and no conditional density cap is assumed.

For an `ell`-subset `T`, the literal product projection has Gram determinant `S^2 det(C_T C_T^T)`. Weighted Holder uses powers `1/alpha_i>=2`; the baseline scalar Fourier-power theorem applies. Ordering the sampled subset and applying entropy subadditivity gives

`H(w)+sum_i alpha_i log alpha_i <= ell log ell-log(ell!)`.

Thus the stated envelope

`|phi_Q(t)| <= min(1,K_{k,ell}|t|^{-(k+ell)/2})`

has the claimed constant. Promotion of heavy physical rows is exact Gram-Schmidt algebra and yields the marginal-free endpoints

`||p_Q||_infinity <= C3 E_3(M)^(-1/6)`,  `C3=3 sqrt(2)e(9/2)^(1/6)=14.818337662843...`,

and

`sup_a E|Q-a|^(-1/2) <= C2 E_2(M)^(-1/8)`,  `C2=8 sqrt(e)2^(-1/8)=12.095072570796...`.

The latter is correctly a half-potential theorem, not a rank-two bounded-density theorem.

### Compilation at multiplicity nine — PASS

Normalize `K=s=1` and assume `s_9(A)>=1`.

- **No pivot.** Baseline `prop:volume` at `k=3` gives `V_3>=kappa^3`; a fair cut gives `E_3(M)>=4^{-3}kappa^3`, hence `E_3(M)^(-1/6)<=160`. Therefore
  `||p_Q||_infinity <=160 C3=2370.934026...<2400`.
- **Scalar pivot.** The Schur child retains eight unit directions. If it has a pivot, baseline `prop:pivot-H` gives truncated half-potential `<=600`, hence full half-potential `<=601`. If it has no pivot, it has `s_5>=1`; baseline `prop:volume` at `k=2` and a fair cut give `E_2>=4^{-2}kappa^2`, so the grouped order-two receiver gives `<153`. Thus every scalar-pivot child has full half-potential `<=601`, and the outer square profile yields `<=10*601=6010`.
- **Definite pair.** Directly `<=10 pi<32`.
- **Indefinite pair.** The Schur child retains at least seven unit directions, hence operator norm at least one; the baseline logarithmic argument gives `<251`.

All hypotheses of every imported lemma are therefore met. Rescaling yields the full theorem

`boxed: s_9(A)>=s>0 => ||p_(X^TAX+b^TX+c)||_infinity <=6010 K^2/s.`

This preserves arbitrary independent rough laws, dimension, signature, remaining spectrum and affine terms. It is a full replacement theorem, not a subclass. Multiple other repository artifacts provide genuinely separate complete reviews; I do not change any owner/release certification flag here.

## Current threshold boundary

`PASS`: multiplicity nine is a complete theorem with the original quantifiers.  
`GAP`: multiplicity eight is not yet a bounded-density theorem. The newest source-backed `s_8` terminal analysis reaches a critical split-row Fourier bound `|phi(t)|<=min(1,U/|t|)`, hence every finite `L^r` and an `epsilon log(1/epsilon)` small-ball bound, but not `L^infinity`. The exact remaining debt is to spend the additional overlap-one / rank-saturated currency before the critical logarithm is lost.

No part of the baseline manuscript or the nine-direction replacement remains `UNCHECKED` in this B01 run. The unrestricted three-eigenvalue conjecture remains open, and global continuity is not claimed.

## Review-status and diagnostics note

The repository checker is finite diagnostic evidence only. This B01 report is an independent mathematical review, not formal verification or journal peer review. Manual privacy review of the changed-file allowlist found only mathematical statements, repository hashes and run metadata; no credentials, personal archives, scheduler IDs, or unrelated private material are included.
