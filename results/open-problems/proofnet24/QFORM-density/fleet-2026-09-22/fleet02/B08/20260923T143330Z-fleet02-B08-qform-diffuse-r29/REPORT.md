SIGNED IN - working on the quadratic-form bounded-density conjecture (universal constant), account fleet02, slot B08, 2026-09-23T14:33:30Z.
attacking: the k=1 diffuse hybrid — aggregate one macroscopic child direction with an exact rank-two cross bank before any bounded physical pivot/minor selection.

# QFORM B08 r29 — rank-compressed diffuse hybrid witness

Status: SUPPORTING THEOREM + TARGET-VALID MECHANISM OBSTRUCTION; full QFORM target remains OPEN.


Source-pinned inputs actually used:

- Fixed source `yspennstate/math-open-problems@e5f71d79eff325201dd0274053d20268ce65b837`, record `proofnet24/QFORM-density/interactive/20260922T211500Z-decoupling-brascamp-lieb/RESULTS.md`, especially Theorem F.
- Partner `fleet03/B08` r38: brain handoff `20260923T131815Z-fleet03-B08-qform-diffuse-r38.md`, canonical mathematics `yspennstate/math-open-problems@1a70497363989dfea9fa4ce9e515fa279677df69`, especially the arbitrary-same-bank two-hub estimate `||p_Q||_3 <= 3^(2/3)e^(1/3)[det(CC^T)]^(-1/6)`.

## 1. First unpaid implication

`QFORM-K1-RANK-COMPRESSION-STABLE-COLLECTIVE-COMPILER-v1`:

In the actual one-child/two-cross gate, prove a full-ambient `O(L^-1)` density compiler that jointly aggregates one actual diffuse child eigendirection and an exact/narrow rank-two diffuse cross bank **before** bounded physical hub/pivot/minor selection. It must remain valid under arbitrary same-bank curvature that can rank-compress the two cross pairs into only three total spectral directions, retain a nonzero low-stable-rank cross tail rather than delete it, preserve original-coordinate product provenance, and remain stable under sparse original-coordinate conditioning. The theorem below shows this rank-compression phenomenon is real and target-valid.

## 2. Exact rank-three compressed Hadamard family

Let `m=2^q>=8`. Take normalized Sylvester-Hadamard columns `u_1,u_2 in R^m` on the left bank and `v_1,v_2,v_3 in R^m` on the right bank. Put

`rho = 1/4`,

`a_+ = (2+sqrt(3))/4`, `a_- = (2-sqrt(3))/4`.

Then `a_+ + a_- = 1` and `a_+ a_- = 1/16 = rho^2`. For any scale `L>=1`, define

```
A_(m,L) = L [ a_+ u1u1^T + a_- u2u2^T,         rho(u1v1^T+u2v2^T)
              rho(v1u1^T+v2u2^T),  a_- v1v1^T+a_+ v2v2^T+v3v3^T ].
```

### Proposition 2.1 — exact target spectrum

`A_(m,L)` has exact rank three and its three nonzero eigenvalues are `L,L,L`.

Proof. Because `a_+a_-=rho^2`,

```
[ a_+  rho ] = [sqrt(a_+)] [sqrt(a_+) sqrt(a_-)]
[ rho   a_-]   [sqrt(a_-)]
```

and similarly with `a_+` and `a_-` exchanged. Thus

`A_(m,L)=L(q1q1^T+q2q2^T+q3q3^T)`

with

`q1 = sqrt(a_+) u1  (+) sqrt(a_-) v1`,

`q2 = sqrt(a_-) u2  (+) sqrt(a_+) v2`,

`q3 = 0 (+) v3`.

The three vectors are orthonormal since the Hadamard columns are orthonormal and `a_++a_-=1`. Hence the only nonzero eigenvalues are three copies of `L`. In particular the exact target hypothesis holds for every `L>=1`.

### Proposition 2.2 — strongly diffuse selected frame

The physical leverage of the rank-three eigenframe is exactly `1/m` on every left coordinate and `2/m` on every right coordinate. Hence the maximum leverage is `2/m -> 0`.

Indeed, on the left bank only q1,q2 contribute, with squared row mass `(a_++a_-)/m=1/m`; on the right q1,q2,q3 contribute `(a_-+a_++1)/m=2/m`.

### Proposition 2.3 — explicit actual spectral gate

Let

`c = (1/2)sqrt(3/5) = 0.3872983346207417...`,

`beta = (3/16)sqrt(3/5) = 0.1452368754827781...`.

The left child has nonzero spectrum `a_+L,a_-L`, with `a_+=0.9330127018922193...>c>a_-=0.0669872981077807...`, so it carries exactly one `cL`-large actual child eigenvalue. The right child has nonzero spectrum `L,a_+L,a_-L`, so it carries exactly two `cL`-large eigenvalues. The full physical cross block is

`B = rho L (u1v1^T+u2v2^T)`

and has exactly two nonzero singular values, both `rho L=L/4>beta L`. Therefore this family lies exactly in the unresolved `k=min(k_left,k_right)=1` child/two-cross gate, with **zero cross tail**.

This proves a structural obstruction: two macroscopic cross singular directions plus one macroscopic child direction do not force four or five macroscopic spectral directions after same-bank curvature is restored. Here arbitrary-looking same-bank curvature rank-compresses the relevant geometry all the way to the minimum three target eigenvalues.

## 3. Completed fixed-source theorem pays the whole family uniformly

Apply Theorem F from the fixed source at commit `e5f71d79eff325201dd0274053d20268ce65b837` to the exact spectral decomposition above, taking `B=0` in that theorem and all physical coordinates in its frame set. The frame Gram matrix is the identity, and every physical row leverage is at most `2/m<=1/2` for `m>=4`. Since the three spectral coefficients equal `L`,

`|lambda_1 lambda_2 lambda_3| = L^3`.

Therefore for **every** independent input law with one-dimensional densities bounded by one,

`||p_(X^T A_(m,L) X)||_infinity <= 12/L`.                                    (3.1)

The same theorem supplies an integrable `|t|^(-3/2)` Fourier envelope, so the density in (3.1) has a continuous `C_0` representative. No moments, support bounds, log-concavity, diagonal-basis assumption, or post-rotation independence is used.

Thus the construction is not a QFORM counterexample. It is a source-valid counterexample to any proof reduction that first selects a bounded number of physical pivots/hubs and expects dimension-free strength from them.

## 4. Localized-coordinate conditioning remains uniformly paid

The preceding B08 exact-range conditioning theorem applies with rank `r=3` and maximal row leverage `delta=2/m`. If `H` is **any** set of `h<=m/8` original physical coordinates, then `h delta<=1/4`, and after conditioning on `X_H` the surviving original coordinates remain independent. The theorem yields, uniformly in the conditioned values and all induced affine terms,

`||p_(Q | X_H)||_infinity <= 12 (1-2h/m)^(-1) L^(-1) <= 16/L`.               (4.1)

This is a genuine original-coordinate conditioning statement; no rotated coordinates are conditioned on.

The actual spectral gate also persists quantitatively. If `h_L,h_R` coordinates are removed from the left/right banks with `h_L+h_R<=m/8`, then for the left two-column frame `U`,

`||I-U_H^T U_H||_op >= 1-2h_L/m`,

so the high child eigenvalue is at least

`a_+(1-2h_L/m)L >= (3a_+/4)L = 0.6997595264191645... L > cL`,

while the low child eigenvalue is at most `a_-L<cL`. Hence the left child still has exactly one `cL`-large eigenvalue.

For the right three-column frame, deletion changes the compressed Gram matrix by operator norm at most `3h_R/m`; Weyl gives the second high child eigenvalue at least

`(a_+ - 3h_R/m)L >= (a_+-3/8)L = 0.5580127018922193... L > cL`,

while Loewner monotonicity keeps the third eigenvalue at most `a_-L<cL`. Hence the right child still has exactly two `cL`-large eigenvalues.

Finally, for the restricted cross block,

`s_2(B_(T_L,T_R)) >= rho L sqrt(1-2h_L/m) sqrt(1-2h_R/m)`.

Since `h_L+h_R<=m/8`, the product under the square root is at least `3/4`, whence

`s_2(B_(T_L,T_R)) >= (sqrt(3)/8)L = 0.2165063509461097... L > beta L`.          (4.2)

So sparse localized-coordinate conditioning neither destroys the unresolved hybrid geometry nor harms the dimension-free whole-range estimate.

## 5. Newest partner theorem applied to an actual inequality — and why local hubs lose dimension

Take two left physical rows whose Hadamard sign patterns in `(u1,u2)` are orthogonal, e.g. proportional to `(1,1)` and `(1,-1)`. Let `C` be the resulting two-row physical cross matrix. Since `v1,v2` are orthonormal,

`CC^T = (2 rho^2 L^2/m) I_2`,

so

`det(CC^T)=4 rho^4 L^4/m^2 = L^4/(64m^2)`.                                  (5.1)

Apply the newest completed partner result `fleet03/B08` r38, which is valid with arbitrary same-bank quadratic-affine curvature retained. It gives the actual inequality

`||p_Q||_3 <= 3^(2/3)e^(1/3)[det(CC^T)]^(-1/6)`

and hence on this target family

`||p_Q||_3 <= 2*3^(2/3)*e^(1/3) m^(1/3) L^(-2/3)`

`             = 5.805981657343624... m^(1/3) L^(-2/3)`.                     (5.2)

Equation (5.2) is a valid full-ambient partner certificate, but it deteriorates as `m^(1/3)`, whereas the whole-range fixed-source theorem gives the uniform `12/L` bound (3.1). The gap is therefore not loss of aggregate cross geometry: it is exactly the reciprocal cost incurred by selecting finitely many physical hubs before aggregating the delocalized child/cross range.

The same obstruction appears at the determinant level. Every nonzero physical `2x2` cross minor has magnitude at most

`rho^2 L^2 * 4/m^2 = L^2/(4m^2)`,

while physical diagonal entries are only `O(L/m)`. Hence neither one fixed local pivot nor one fixed local minor can carry a dimension-free payment on this family.

## 6. Consequence for the remaining hybrid proof

The correct missing receiver must be collective. A bounded-hub approach can at best recover powers of `m` on the family above even though the actual target density is uniformly bounded. Moreover, the example shows why one cannot model the two cross singular directions as independent `+/-` spectral pairs once arbitrary same-bank curvature is present: the same-bank blocks can compress those two cross directions together with the child direction into exactly three positive eigenvalues.

Accordingly the next valid subproblem is `QFORM-K1-RANK-COMPRESSION-STABLE-COLLECTIVE-COMPILER-v1`: aggregate the actual child eigendirection and the top-two cross singular frame at the level of the original product measure, in a way stable under arbitrary same-bank curvature and the already-isolated low-stable-rank cross tail. Any candidate theorem should reproduce `O(L^-1)` on this family, preserve (4.1) under original-coordinate conditioning, and only then specialize to local pivots if a genuinely macroscopic physical pivot exists.

## 7. Scope and correction compliance

This run does **not** claim the full conjecture. It does not discard a small quadratic tail, infer a single good minor from a determinant bank, assume uniform conditional caps after arbitrary conditioning, condition on spectral coordinates, or assume independence after an orthogonal rotation. Continuity is asserted only in the branches where the fixed-source Fourier theorem supplies an integrable characteristic-function majorant. The partner `L^3` inequality is used only with the scope proved in r38.

Numerical identities used above were independently evaluated in-run:

`a_+=0.9330127018922193`, `a_-=0.0669872981077807`, `c=0.3872983346207417`, `beta=0.14523687548277814`, `sqrt(3)/8=0.21650635094610965`, partner coefficient `2*3^(2/3)*e^(1/3)=5.805981657343624`.

Outcome: `PROVED_SUPPORTING_THEOREM / TARGET-VALID_MECHANISM_OBSTRUCTION / FULL_TARGET_OPEN`.
