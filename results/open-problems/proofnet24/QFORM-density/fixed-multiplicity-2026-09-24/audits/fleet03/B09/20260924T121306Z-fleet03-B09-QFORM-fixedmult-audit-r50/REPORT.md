# fleet03/B09 independent fixed-multiplicity audit — spectral rank / diagonal dominance

Run: `20260924T121306Z-fleet03-B09-QFORM-fixedmult-audit-r50`  
Objective: `QFORM-FIXED-MULTIPLICITY-AUDIT-20260924`  
Pinned baseline source commit: `7c0d6e60946b19423e6400a12d34b473cf0591e2`  
Pinned source blob: `183ccd294763214e6a707e8d4749ff9a8cf7006d`  
Pinned source SHA-256 from owner objective: `9f3bdec0b88debe9a66076c7b4a5cc894fb14e69b89591a4107e785340f65e69`  
Latest source readback in this run: manuscript blob unchanged at `183ccd294763214e6a707e8d4749ff9a8cf7006d`.

## Verdict

**PASS for the mathematical 17-eigenvalue baseline in this independent fleet03/B09 audit.** I read the complete manuscript and independently reconstructed the full dependency chain. I found no fatal mathematical defect in the theorem

\[
 s_{17}(A)\ge s>0\quad\Longrightarrow\quad
 \|p_{X^TAX+b^TX+c}\|_\infty\le 10^4K^2/s
\]

for arbitrary dimension, arbitrary signs and remaining spectrum, arbitrary affine terms, and independent real coordinates with densities bounded by `K`.

This report is one scheduled-worker review, not formal verification and not a claim about the unrestricted three-eigenvalue conjecture. The manuscript's global conclusion is an **essentially bounded density**. Continuity is proved in the no-pivot Fourier branch but is not established globally by the pivot branches.

There is one nonmathematical/release **GAP**: at the master snapshots inspected in this run the manuscript root contained `manuscript.tex`, `README.md`, `AUDIT.md`, `audits/`, and `improvements/`, while the README/self-audit names `SOURCE_MANIFEST.json`, `proof_map.csv`, `verify.py`, and `checks.json` as package members. Those four files were absent from the root listing I inspected, so the repository-level reproducibility claims depending on them remain UNCHECKED here.

## End-to-end audit ledger

### 1. Statement, quantifiers, scaling — PASS (source lines 1–78 and 724–759)

The statement preserves all intended quantifiers. In the final scaling, `Y=KX` has coordinate densities bounded by one and

\[
 \widetilde Q=Y^T(A/s)Y+(K/s)b^TY+(K^2/s)c=(K^2/s)Q.
\]

Thus the normalized density bound scales by `K^2/s`, exactly as stated. No moment, support, log-concavity, Gaussian, or diagonal-coordinate assumption appears.

### 2. Fourier inversion and negative half potential — PASS (roughly lines 79–164)

The Fourier convention, Plancherel constant, Gaussian regularization, and inversion constant are mutually consistent. The Riesz calculation gives

\[
 \mathbb E|Z-a|^{-1/2}
 \le (2\pi)^{-1/2}\int |t|^{-1/2}|\phi_Z(t)|\,dt.
\]

The order-three envelope is used only after multiplication by the half-potential weight; it is never incorrectly treated as an `L^1` characteristic-function bound.

### 3. Schur spectral count — PASS AS WRITTEN (roughly lines 176–217)

The invertible case follows by identifying `S^{-1}` as a principal compression of `A^{-1}` and applying positive and negative interlacing at the inverse threshold.

I also rechecked the singular-ambient paragraph. A separate worker proposed a fixed-`delta` replacement, but I do **not** reproduce a mathematical gap in the baseline text. Let

\[
 q=N_A(t)-k.
\]

For small admissible `epsilon`, the baseline argument gives

\[
 N_{S_\epsilon}(t-|\epsilon|)\ge q.
\]

Equivalently, the `q`-th ordered eigenvalue modulus of the symmetric `S_epsilon` is at least `t-|epsilon|`. The Schur complements converge in operator norm to `S`, so ordered eigenvalue moduli converge. Passing to the limit directly gives the `q`-th modulus of `S` at least `t`, i.e.

\[
 N_S(t)\ge N_A(t)-k.
\]

Thus the moving-threshold sentence is terse but closes by the exact continuity it cites. The fixed-`delta` proof is a valid clarification, not needed for correctness of this implication.

### 4. Geometric Brascamp–Lieb heat flow — PASS (roughly lines 218–284)

The frame identity makes the relevant column operator a contraction, giving

\[
 \partial_tF-\Delta F
 =F\Big(\sum_i c_i v_i^2-\big|\sum_i c_i u_i v_i\big|^2\Big)\ge0.
\]

The large-time Gaussian limit and monotone truncation argument are consistent with the stated rough nonnegative inputs.

### 5. Product projection and scalar Fourier powers — PASS (roughly lines 285–343)

The product-projection proof gives `||p_{U^TX}||_infty <= e^{d/2}` without asserting independence after an orthogonal change of variables. The line

\[
 \sum_i(1-b_i)=d
\]

is valid when the zero-`b_i` indices are included on the right-hand side of `-b log b <= 1-b`; they contribute zero to the entropy term and one to `1-b`. I therefore do not regard this as a required mathematical repair.

For the scalar Fourier powers, `|fhat|^{2m}` is integrable because it is bounded by `|fhat|^2`, and the projected-density estimate for the sum of `m` independent differences gives the claimed `p^{-1/2}` integral bound.

### 6. Decoupling and regularized crossing determinant — PASS (roughly lines 344–413)

The two-copy Cauchy–Schwarz/Jensen steps use only original-coordinate independence. With

\[
 H=\alpha I+a^2M^TM,
\]

the weights `c_j` and `d_i` form the required geometric frame. The powers of `d_i` cancel against the scalar Fourier estimate; the `c_j` entropy factor is paid by `e^{theta/2}`; `alpha=(2 pi e)^2` cancels the remaining scalar factor. Taking fourth roots yields exactly

\[
 |\phi_Z(t)|\le
 \det\!\left(I+\frac{t^2}{\pi^2e^2}M^TM\right)^{-1/8}.
\]

No rank, signature, or coordinate-leverage assumption is smuggled in.

### 7. Crossing volumes and the two analytic exponents — PASS (roughly lines 414–446)

Cauchy–Binet gives the coefficient identity for `Z_k`. Retaining only the order-`k` term gives exponent `k/4`. Consequently:

- `k=5` gives an `L^1` characteristic-function envelope and `||p||_infty <= 5e Z_5^{-1/10}`;
- `k=3` gives the weighted negative-half-potential bound, not a direct density bound.

This distinction is maintained everywhere downstream.

### 8. Scalar, definite-pair, hyperbolic-pair and quarter-power estimates — PASS (roughly lines 447–543)

The scalar-square estimate is conditional measure domination, not an independence assertion. The definite-pair estimate is a deterministic two-dimensional coarea calculation. In the indefinite case, the hyperbolic parameterization has Jacobian `1/(2 sqrt D)`. The tail estimate selects an **original coordinate**, uses only its density cap and mass, and produces the logarithmic envelope. The quarter-power concentration lemma correctly obtains a physical sign cut with cross-block norm at least one quarter of the quadratic operator norm and then uses Gaussian smoothing of the `|t|^{-1/4}` envelope.

### 9. Volume-sampled interpolation — PASS (roughly lines 544–593)

For a nonsingular disjoint seed `B=A[S,T]`,

\[
 P=A_{\cdot,T}B^{-1}A_{S,\cdot}
\]

has rank at most `r`, agrees with `A` on rows `S` and columns `T`, and the bordered determinant identity controls each off-diagonal residual in `L x L`. Singular seeds contribute zero weight, so the aggregate extension count is correctly an inequality rather than an equality.

### 10. Completion: global rank `<=3r`, restricted rank `<=r` — PASS (roughly lines 594–621)

With `E` supported on the off-diagonal residual in `L x L`, the diagonal `D` vanishes on the `2r` seed coordinates. The remainder satisfies

\[
 R_{L,L}=P_{L,L},\qquad \operatorname{rank}R_{L,L}\le r.
\]

Moreover `R-P` vanishes on rows `S`, columns `T`, and the entire `L x L` block. Its remaining support lies in the union of rows `T` and columns `S`, hence has rank at most `2r`. Together with `rank P<=r`, this gives the required global bound `rank R<=3r`. Nonsymmetry of these algebraic auxiliaries causes no problem because only rank and singular-value inequalities are applied to them.

### 11. B09 focus: spectral rank perturbation and diagonal-dominance contradiction — PASS (roughly lines 622–656)

Assume a bad ratio at an index `1<=r<=4`. The completion gives

\[
 \varepsilon=\|E\|_F\le(r+1)\sqrt\kappa\le1/16.
\]

With `m=4k-3`, rank perturbation by a global rank-`3r` matrix yields at least

\[
 m-3r\ge r+1
\]

diagonal entries of `D` of modulus at least `1-epsilon`. Because `D` vanishes on the seed, these entries lie in `L`. On an `(r+1)`-set `H` of such coordinates,

\[
 |R_{ii}|\ge1-1/16-1/100=371/400,
\]

while, using the no-pivot physical entry bound and `|E_ij|<=||E||_F`,

\[
 \sum_{j\in H\setminus\{i\}}|R_{ij}|
 <4\left(\frac17+\frac1{16}\right)=\frac{23}{28}.
\]

The exact slack is

\[
 \frac{371}{400}-\frac{23}{28}=\frac{297}{2800}>0.
\]

Thus `R[H,H]` is strictly row-diagonally dominant and invertible, so it has rank `r+1`, contradicting `rank R[L,L]<=r`. The `r=0` branch is separately closed by `||diag A||+||offdiag A||_F<1`. This verifies the manuscript's crucial `4k-3` spectral-to-volume implication.

### 12. Random cut, nine-direction half potential and main theorem — PASS (roughly lines 657–759)

Each ordered disjoint `k`-minor crosses a fair physical cut with probability `4^{-k}`. The resulting no-pivot estimates are

\[
 s_9(A)\ge1\Rightarrow\sup_a\mathbb E|Q-a|^{-1/2}<200,
\]

and

\[
 s_{17}(A)\ge1\Rightarrow\|p_Q\|_\infty\le800e<2400.
\]

The pivot branch correctly distinguishes truncated from full half potentials, adding at most one outside `|Q-a|<=1`. The main scalar-pivot branch removes one coordinate and still leaves at least nine spectral directions for the half-potential theorem. The two-coordinate pivot branches keep enough spectrum for their stated uses. All displayed branch constants are below `10^4`.

## Threshold accounting — PASS / no lower threshold claimed

The present determinant-plus-interpolation architecture genuinely stops at 17. For an order-`k` crossing volume the Fourier exponent is `k/4`; absolute Fourier inversion therefore requires `k>=5`. At `k=4` the available envelope is the borderline `O(1/|t|)` and does not by itself give a bounded density.

Algebraically, a bad volume ratio can occur at `r<=k-1`. Since the global correction rank is `3r` and the restricted contradiction needs `r+1` large diagonal coordinates,

\[
 m-3r\ge r+1\quad\Longleftrightarrow\quad m\ge4r+1.
\]

For `k=5`, worst case `r=4` gives `m>=17`. With only sixteen large singular values the present argument forces only four large diagonal entries in that terminal chamber, compatible with restricted rank four. Therefore **no 17-to-16 (or 13) reduction is certified by this architecture alone**. This is a barrier of this proof method, not a lower bound for the underlying conjecture.

A true reduction now needs an endpoint order-four density theorem, a stronger global/restricted rank tradeoff, or a separate terminal `r=4` receiver.

## Independent constant improvement

Without changing any theorem hypothesis or threshold, the written estimates prove a better numerical constant than `10000`. In the scalar-pivot half-potential branch retain the exact displayed value

\[
 C_H=10(20+12\log16).
\]

All other pivot/no-pivot alternatives are smaller, hence the nine-direction full half potential is at most `C_H+1`. The main scalar pivot contributes a further factor `10`, giving

\[
 \boxed{\|p_Q\|_\infty\le(2010+1200\log16)\,K^2/s}
\]

with

\[
 2010+1200\log16=5337.106466687737\ldots<10^4.
\]

This is recorded separately as an improvement, not patched into the pinned baseline.

## Status summary

- 17-eigenvalue mathematical baseline: **PASS in this independent audit**.
- Fatal mathematical defect found: **none**.
- Singular-Schur baseline paragraph: **PASS as written** by ordered-modulus continuity; a fixed-`delta` rewrite is optional clarification.
- Projection-density zero-row wording: **PASS as written** when the RHS sum includes the zero-`b` rows.
- Repository reproducibility package: **GAP/UNCHECKED** because four README-named files were absent from the root snapshots inspected.
- Rigorous constant improvement: **proved**, `2010+1200 log 16` in place of `10000`.
- Rigorous multiplicity improvement below 17: **none proved in this run**.
- Full three-eigenvalue conjecture: **OPEN**.
- Global continuity: **OPEN/not claimed by the manuscript**; no-pivot branch continuous, pivot branches only essential boundedness.

Next proof obligation: obtain a dimension-free order-four endpoint density receiver, or isolate and pay the terminal `r=4` interpolation chamber without deleting residual quadratic curvature or rotating the independent source coordinates.
