SIGNED IN - working on the quadratic-form bounded-density conjecture (universal constant), account fleet02, slot B06, 2026-09-24T14:54:26Z.
attacking: full fixed-multiplicity audit with B06 emphasis on graph determinant/Jacobian/frame weights/regularizer, followed by adversarial threshold-reduction checking.

# fleet02/B06 independent audit — QFORM-FIXED-MULTIPLICITY-AUDIT-20260924

## Source pin and scope

Fresh brain control was resolved before work. Current objective: `QFORM-FIXED-MULTIPLICITY-AUDIT-20260924`.

Mathematical repository: `yspennstate/math-open-problems`, branch `master`.
Fresh master observed during this run: `ffe7e1f2ae1dfb107196dcd6275fd84d0632e1c9` (the manuscript blob below was unchanged there).
Pinned baseline source commit: `7c0d6e60946b19423e6400a12d34b473cf0591e2`.
Pinned manuscript blob: `183ccd294763214e6a707e8d4749ff9a8cf7006d`.
Pinned manuscript SHA-256: `9f3bdec0b88debe9a66076c7b4a5cc894fb14e69b89591a4107e785340f65e69`.
Pinned size: 47,883 bytes, 790 source lines.

I read the complete current package: `README.md`, `DELIVERY_STATUS.md`, `SOURCE_MANIFEST.json`, all 790 lines of `manuscript.tex`, `AUDIT.md`, `proof_map.csv`, `verify.py`, and `checks.json`. The current support suite reports PASS on 534 exact interpolation seeds, 18 exact volume comparisons, 240 numerical Schur-threshold cases, and 30 graph-weight cases. Those diagnostics are not used as substitutes for proof.

## Overall verdict

**PASS — baseline seventeen-eigenvalue theorem.** I found no fatal mathematical gap in the pinned theorem

`independent densities <= K, A=A^T, s_17(A)>=s>0, arbitrary b,c => ||p_(X^TAX+b^TX+c)||_infty <= 10000 K^2/s`.

This is one independent worker audit, not formal verification or journal peer review. It does not solve the unrestricted three-eigenvalue conjecture. No line of the pinned mathematical source remains UNCHECKED in this review. A separate improvement artifact from this same run records a gap in my own earlier proposed threshold-nine replacement; that correction does not affect the pinned seventeen-eigenvalue proof.

## Line-by-line / statement ledger

| Source range / label | Status | Independent check, impact, next obligation |
|---|---|---|
| 1–46: preamble, abstract, definitions | PASS | Quantifiers and terminology agree with the theorem. Singular values of symmetric matrices are absolute eigenvalues. Essential supremum and density scope are standard. No hidden regularity or support assumptions introduced. |
| 47–57 `thm:main` | PASS | Statement preserves arbitrary dimension, signature, remaining spectrum, affine terms, and arbitrary independent coordinate densities bounded by `K`. Interval domination is equivalent to the essential density bound. |
| 59–61 `cor:33` | PASS | Immediate from `s_17(A)>=s_33(A)`. |
| 63–79 architecture / parameters | PASS | `eta=1/100`, `kappa=1/80^2`; stated spectral counts `9=4*3-3`, `17=4*5-3` match later propositions. No rotated-coordinate independence is asserted. |
| 81–120 `lem:fourier` | PASS | Fourier convention, Plancherel constant `2*pi`, Gaussian regularization, inversion constant `1/(2*pi)`, and Gaussian identity were recomputed. Approximate-identity and weak-limit steps are valid for the rough laws used. |
| 122–130 `lem:envelope` | PASS | Integral of `min(1,(a/|t|)^p)` is `2ap/(p-1)`; inversion gives the stated constant. |
| 132–160 `lem:riesz` | PASS | Gamma representation and the substitution in the `v` integral give coefficient `1/sqrt(2*pi)`. The weighted envelope integral is exactly `12 sqrt(u)`, yielding the stated half-potential estimate. |
| 161–181 `lem:rank` | PASS | SVD approximation formula proves both perturbation and rank-shift inequalities without symmetry. Invocations later correctly use singular values for nonsymmetric auxiliaries. |
| 183–207 `lem:schur` | PASS | Invertible case follows from the inverse principal compression and positive/negative variational counts. In the singular case, applying the invertible statement to `A+eps I` at threshold `t-|eps|` and passing to ordered eigenvalue moduli yields `N_S(t)>=N_A(t)-k`; no fixed-threshold patch is needed. |
| 209–217 `lem:dd` | PASS | Standard max-coordinate proof, valid for nonsymmetric matrices. |
| 221–255 `thm:bl` | PASS | Heat-flow differentiation gives the nonnegative quadratic form because the frame synthesis map is a contraction. Gaussian tail domination justifies differentiation/integration by parts. Trace identity gives total exponent `d`; `t->infinity`, `t->0`, truncation and monotone convergence are valid. |
| 258–282 `lem:projection` | PASS | Orthogonal completion and BL application are source-valid. For all original rows `b_i=1-|U^Te_i|^2`, so `sum_i(1-b_i)=d` exactly; rows with `b_i=0` contribute zero to `-b_i log b_i` and may be omitted from the product. Scalar scaling gives `sqrt(e)/|a|`. |
| 284–301 `lem:scalar-fourier` | PASS | `m=floor(p/2)>=p/4`, and `|hat f|<=1` gives the correct power comparison. Difference density is bounded by one. Plancherel/inversion plus the projection lemma yield `2*pi*sqrt(2e)/sqrt(p)`. |
| 310–324 `lem:decoupling` | PASS | Cauchy–Schwarz, independent copy expansion, cancellation of same-bank phases, and integration of the untouched independent coordinates give the stated second- and fourth-power inequalities. Difference coordinates remain independent with cap-one densities. |
| 326–373 `thm:determinant` | PASS | Recomputed in detail below. Jacobian, frame weights, Fourier powers, entropy loss, and regularizer cancellation all match. Boundary weights cause no defect. |
| 375–400 crossing volumes / `cor:vol-fourier` | PASS | Cauchy–Binet expansion is correct. Retaining one `Z_k` term gives exponent `k/4`; `k=5` is integrable and `k=3` is sufficient against the Riesz `|t|^-1/2` weight. Constants `5e` and the displayed half-potential bound check. |
| 404–414 `lem:square` and profile | PASS | Two monotone inverse branches give the square-root density profile. Interval inverse-image length `2 sqrt(2 rho/|a|)` is valid. Conditional measure domination gives the profile without asserting independence between the square and the Schur remainder. |
| 423–434 `lem:definite` | PASS | Completing the square and deterministic orthogonal diagonalization are used only inside a 2D integral. Jacobian in `(delta,theta)` is `1/(2 sqrt(det B))`; integration in angle gives `pi M/sqrt(|det B|)`. |
| 437–482 `lem:hyperbola` | PASS | Hyperbolic parametrization has exact Jacobian `1/(2 sqrt(D))`. Tail monotonicity, one-coordinate change of variables, rearrangement bound using mass <=1, middle interval length, and `Lambda>=2/sqrt(D)` yield the stated logarithmic envelope. Exceptional critical level is correctly handled by test functions/Tonelli. |
| 485–525 `lem:quarter` | PASS | Diagonal alternative and random sign cut are correct. The cross block has norm at least `L/4`; the rank-one factor from the determinant theorem gives `|t|^-1/4`. Gaussian smoothing integral and elementary gamma bound give the stated constant. Layer cake gives `L_0=4+4 log 16`. |
| 528–535 pivot/volume definitions | PASS | Ordered disjoint-pair convention is explicit and used consistently. |
| 545–564 `lem:sampling` | PASS | Bordered determinant identity is exact after row elimination. Each ordered `(r+1)` disjoint minor is counted at most `(r+1)^2` times; singular seeds can have nonsingular extensions, so the proof correctly claims an inequality rather than equality. Interpolation and rank `<=r` are exact. |
| 566–580 `lem:completion` | PASS | Construction gives `A=D+R+E`, zero seed diagonal for `D`, zero diagonal for `E`, Frobenius error bound, `rank R<=3r`, and the sharper `rank R[L,L]<=r`. Support decomposition of `R-P` is valid. |
| 582–619 `prop:volume` | PASS | Telescoping/singular-volume split is exhaustive. `r=0` gives operator norm `<1`. For `1<=r<=4`, perturbation plus global rank forces at least `r+1` large diagonal entries of `D` in `L`; restricted rank then contradicts strict diagonal dominance. Exact slack is `371/400-23/28=297/2800>0`. |
| 621–630 `lem:cut` | PASS | Each ordered disjoint `(S,T)` survives a fair cut with probability `4^-k`; expectation and existence conclusion are exact. |
| 632–645 `cor:no-pivot` | PASS | With `Z_k^(-1/(2k))<=160`, order three gives full half potential `<200`; order five gives density `<=800e<2400`. Affine and same-bank terms remain in the cross-form theorem. |
| 654–674 `lem:kernels` | PASS | Near/far split for `J(d)` is valid; logarithmic kernel bound follows from interval-overlap rearrangement and evaluates to 8. |
| 676–714 `prop:pivot-H` | PASS | Scalar pivot uses Schur count plus the quarter-power logarithmic potential; definite pair uses conditional coarea; indefinite pair uses the hyperbolic envelope and `sup D^-1/2 log_+ D=2/e`. Constants stay below 600. |
| 716–724 `prop:nine` | PASS | Pivot case controls truncated half potential; no-pivot case controls full half potential. Outside unit distance the kernel is <=1, so the full potential is <=601. |
| 726–749 main proof | PASS | No-pivot branch `<2400`; scalar pivot leaves at least 16 unit-scale directions, hence at least nine, and costs `10*601=6010`; definite pair `<40`; indefinite pair leaves at least fifteen directions and costs `<251`. Scaling `Y=KX` gives exactly `10000 K^2/s`. |
| 751–790 accounting, remarks, bibliography | PASS | Dependency table matches the actual proof. Limitations correctly deny a three-eigenvalue theorem and do not claim continuity in pivot branches. Classical citations are attribution rather than hidden dependencies. |

## B06 reconstruction: determinant, Jacobian, weights, regularizer

In lines 326–373 set

`a=2t`, `alpha=(2*pi*e)^2`, `H=alpha I+a^2 M^T M`.

For row transposes `m_i`, define

`c_j=alpha e_j^T H^-1 e_j`, `d_i=a^2 m_i^T H^-1 m_i`.

The vectors `sqrt(alpha) H^-1/2 e_j` and `a H^-1/2 m_i` form an exact Parseval frame:

`sum_j c_j u_j u_j^T + sum_i d_i v_i v_i^T = I`.

Consequently `0<c_j<=1`, `0<=d_i<=1`, and taking traces yields

`theta=sum_i d_i=sum_j(1-c_j)`.

After `x=H^-1/2 z`, the exact Jacobian is `det(H)^-1/2`. For the coordinate factor,

`x_j=sqrt(c_j/alpha) (u_j dot z)`,

so BL contributes `alpha^(c_j/2)c_j^(-c_j/2)||g_j||_(1/c_j)`. The Fourier row scale is `sqrt(d_i)`, giving `d_i^(-d_i/2)||h_i||_(1/d_i)`. The scalar Fourier-power lemma with `p=2/d_i` gives

`||h_i||_(1/d_i) <= (2*pi*sqrt(e d_i))^d_i`,

and the `d_i` powers cancel exactly. Since `g_j<=1`, its norm factor is at most one. The only coordinate entropy loss is

`prod_j c_j^(-c_j/2) <= exp(theta/2)`.

Factoring `alpha^d` from `det H` leaves

`det(I+a^2 M^T M/alpha)^(-1/2) * (2*pi*e/sqrt(alpha))^theta`.

The chosen `alpha=(2*pi*e)^2` kills the multiplier exactly. Fourth-rooting the decoupled estimate yields

`|phi_Z(t)| <= det(I+t^2 M^T M/(pi^2 e^2))^(-1/8)`.

No coordinate leverage assumption or post-rotation independence occurs. If `d_i=0`, that Fourier factor is identically one and is omitted; `c_j=1` is benign. The limit `c_j downarrow 0` is also benign because `c^(-c/2)->1`.

## Package/reproducibility status

`SOURCE_MANIFEST.json`, `proof_map.csv`, `verify.py`, and `checks.json` are now present. The earlier package gap caused by their absence is therefore resolved. I inspected the checker logic: it guards the pinned manuscript SHA, tests exact interpolation/rank/bordered-minor identities and exact diagonal-dominance arithmetic, then labels the Schur/graph tests as floating diagnostics. `checks.json` is consistent with that code. The historical larger test counts in the authoring `AUDIT.md` remain historical self-report rather than independently reproduced evidence; this has no role in the symbolic proof.

## Counterexample pressure and impact

The pinned seventeen-eigenvalue proof survives the fleet02 adversarial checks above. However, a threshold reduction must not be inferred from the borderline order-four determinant envelope: rank/order four gives only `|t|^-1` after the fourth root and therefore is not integrable for density inversion. A separate immutable correction from this run shows that my preceding B06 threshold-nine grouped-receiver sketch has an unfilled mixed-norm step; the cap-one uniform density furnishes a direct obstruction to the implicit first-power Fourier `L^1` estimate. That earlier threshold-nine claim is therefore not counted as a completed reduction in this audit.

## Next obligation

Preserve the audited seventeen-eigenvalue baseline. To lower the multiplicity, supply a complete product-preserving endpoint/grouped receiver with every Hölder/decoupling exponent written explicitly and no hidden `L^1` Fourier assumption, then re-close the pivot/no-pivot dependency map with constants. The unrestricted three-eigenvalue conjecture remains open.
