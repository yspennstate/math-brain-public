# account04/B11 independent audit — Schur counts and fixed-multiplicity interfaces

Run: `20260924T151545Z-account04-B11-fixedmult-schur-r1`  
Objective: `QFORM-FIXED-MULTIPLICITY-AUDIT-20260924`  
Pinned source: `yspennstate/math-open-problems@7c0d6e60946b19423e6400a12d34b473cf0591e2`  
Manuscript: `proofnet24/QFORM-density/fixed-multiplicity-2026-09-24/manuscript.tex`  
Git blob: `183ccd294763214e6a707e8d4749ff9a8cf7006d`  
Owner-recorded SHA-256: `9f3bdec0b88debe9a66076c7b4a5cc894fb14e69b89591a4107e785340f65e69`

## Verdict

The written 17-eigenvalue theorem is **PASS** in this account04 reconstruction. No fatal mathematical defect was found. The global statement retains arbitrary independent cap-(K) coordinate densities, arbitrary symmetric matrices and affine terms, all signatures, arbitrary tails, and no post-rotation independence.

The now-established nine-eigenvalue replacement has a **PASS B11 interface**: all scalar/pair Schur spectral charges and the singular-ambient limiting step satisfy the exact hypotheses needed by its branch assembly. This report does not relabel the grouped product-Fourier compiler as newly reviewed; it audits the Schur dependency independently.

The unrestricted three-eigenvalue theorem and global continuity remain open.

## Schur lemma reconstructed, including singular ambient matrices

Let
[
A=egin{pmatrix}B&C\\C^T&Dend{pmatrix}=A^T,qquad det B
e0,qquad
S=D-C^TB^{-1}C,
]
where (B) has order (k). The manuscript claims
[
N_S(t)ge N_A(t)-k,qquad
N_H(t)=#{j:|lambda_j(H)|ge t}.
]

### Invertible ambient matrix

Block elimination shows that the complementary principal block of (A^{-1}) is (S^{-1}). Interlacing applied separately to (A^{-1}) and (-A^{-1}) gives
[
#{|lambda(S^{-1})|>t^{-1}}
le
#{|lambda(A^{-1})|>t^{-1}}.
]
The strict inverse threshold corresponds exactly to the complement of the original non-strict threshold:
[
#{|lambda(S^{-1})|>t^{-1}}=(n-k)-N_S(t),
]
[
#{|lambda(A^{-1})|>t^{-1}}=n-N_A(t).
]
Rearrangement proves the claim without losing eigenvalues lying exactly at (t).

### Singular ambient matrix

Choose (arepsilon_m	o0) avoiding the finitely many roots for which (A+arepsilon_mI) is singular. For all sufficiently large (m), (B+arepsilon_mI) is also invertible and
[
S_m=D+arepsilon_mI-C^T(B+arepsilon_mI)^{-1}C	o S.
]
Weyl's inequality gives
[
N_{A+arepsilon_mI}(t-|arepsilon_m|)ge N_A(t).
]
The invertible result at the moving threshold yields
[
N_{S_m}(t-|arepsilon_m|)ge N_A(t)-k.
]
If the right side is positive, continuity of the corresponding ordered eigenvalue modulus gives the same count for (S) at threshold (t); otherwise the assertion is trivial. This closes the endpoint and singularity cases.

Equivalently,
[
s_j(S)ge s_{j+k}(A),qquad 1le jle n-k.
]

## Exact sharpness family

The sibling improvement artifact proves, for every signature ((p,q)), an exact family with
[
B=arepsilonoperatorname{diag}(I_p,-I_q),quad
C=sqrtarepsilon I,quad
D=operatorname{diag}(I_p,-I_q),
]
whose Schur complement is zero while the ambient spectrum is
[
{1+arepsilon}^{p}cup{-(1+arepsilon)}^{q}cup{0}^{p+q}.
]
Thus the loss (k=p+q) is sharp even for singular ambient matrices and arbitrarily small pivots. In particular, small pivot norm cannot refund a spectral direction.

## Actual fixed-multiplicity branch accounting

For the reviewed nine-eigenvalue replacement, normalize (K=s=1).

| Branch | Ambient reserve actually required by this interface | Reason |
|---|---:|---|
| No pivot | 9 | The order-three structural/analytic receiver is the controlling branch. |
| Scalar pivot | 6 suffices for the Schur bookkeeping | Loss one leaves five directions; a no-pivot child pays the order-two full half-potential route, while a pivot child needs only the two-direction pivot theorem. |
| Definite pair | no surviving reserve is required | Direct conditional density bound pays the branch. |
| Indefinite pair | 3 | Loss two leaves one direction, sufficient for the logarithmic critical-value potential. |

Therefore the multiplicity nine is not forced by scalar or pair Schur loss. The (9	o8) debt lies entirely in the no-pivot endpoint. The sharpness family proves this is not repairable by a universal improvement of the Schur count under the present hypotheses.

## End-to-end baseline audit ledger

| Source range | Status | Independent check |
|---|---|---|
| 1–87 | PASS | The theorem, corollary, normalization, pivot definitions and quantifiers match later use. |
| 88–160 | PASS | Fourier convention, Gaussian inversion, envelope integration and Riesz half-potential constants are consistent. |
| 161–217 | PASS | Nonsymmetric singular-value perturbation, Schur count and strict diagonal dominance are valid. |
| 218–301 | PASS with presentation correction retained | Geometric BL and projection-density arguments use deterministic integration, not rotated independence. After zero-weight rows are omitted, the projection proof needs (sum(1-b_i)le d), not equality; the required bound is unchanged. |
| 302–400 | PASS | Decoupling copies remain in original coordinate banks; graph determinant, regularizer, exponents and crossing volumes check. |
| 401–525 | PASS | Square, definite-pair, hyperbolic and quarter-concentration bounds are measure dominations uniform in affine terms. |
| 528–645 | PASS | Ordered minor sampling, singular-seed inequality, nonsymmetric interpolation, both rank bounds, seed-vanishing diagonal, spectral contradiction and random cut are correct. |
| 646–724 | PASS | Kernel integrals, truncated/full half-potential distinction and all pivot branches close. |
| 726–790 | PASS with notation clarification | Main branches and (K^2/s) scaling close. The symbol (A/B) is read as the already-defined Schur complement; spelling this out would improve presentation. The limitations correctly keep the three-eigenvalue problem and global continuity open. |

The supplementary package now contains `README.md`, `SOURCE_MANIFEST.json`, `AUDIT.md`, `proof_map.csv`, `verify.py`, and `checks.json`. Their finite checks are diagnostics, not proof. The exact manuscript git blob was read; the external SHA-256 was not independently recomputed from raw bytes in this run and remains **UNCHECKED** here.

## Final status

- Pinned 17-eigenvalue theorem: **PASS**.
- Schur interface of the nine-eigenvalue replacement: **PASS**.
- Universal Schur loss (k): **sharp**, even for arbitrarily small invertible pivots and singular ambient matrices.
- Eight-eigenvalue bounded-density endpoint: **OPEN**; Schur counting is not the missing step.
- Unrestricted three-eigenvalue conjecture: **OPEN**.
