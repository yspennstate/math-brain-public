SIGNED IN - working on the quadratic-form bounded-density conjecture (universal constant), account account03, slot B06, 2026-09-24T09:00:40Z.
attacking: the exact rank-one / rank-zero localized three-hub endpoint by aggregating the full kernel-to-tail exterior area before any reciprocal minor, then spending one literal scalar square plus a rank-two product crossing.

# account03/B06 r56 — kernel-area compiler for rank-one and rank-zero three-hub faces

Programme: `QFORM-DENSITY-3EIG-20260922`, programme revision `2026-09-22.5`.  
Fresh prepublication control snapshot: `yspennstate/math-research-brain@d0dd8a67f07e770639d443230a811b354a51e279`, OWNER CONTROL revision `2026-09-22.15`.  
Immediate B06 input: account03/B06 r54, `yspennstate/math-open-problems@8bdce354a7ab12c52133f56532d8c7589cc94e98`, `proofnet24/QFORM-density/fleet-2026-09-22/account03/B06/20260924T075625Z-account03-B06-qform-r54/REPORT.md`.  
Rank-two crossing half-Riesz input: account01/B06 `QFORM-RANK2-CROSS-HALFRIESZ-v1`, source snapshot `yspennstate/math-open-problems@cb1cffb4f4644bd7cf1bb912f792dd9ce060957a`, `proofnet24/QFORM-density/fleet-2026-09-22/account01/B06/20260923T213616Z-account01-B06-QFORM-r40/REPORT.md`.  
Rank-three crossing input: `QFORM-THREE-HUB-JOINT-PLANCHEREL-v1`, `yspennstate/math-open-problems@f98635ec90f47da9c38e40516896462bb423f3c6`.  
Designated partner actually applied in Section 7: account04/B06 `QFORM-TANGENTIAL-SHARED-LEAKAGE-ABSORPTION-v1`, `yspennstate/math-open-problems@a09353b7b4cc9b1b812b1d1f2f319f5dcef5e10b`, `proofnet24/QFORM-density/fleet-2026-09-22/account04/B06/20260924T001014Z-account04-B06-QFORM-r3/REPORT.md`.  
Execution: `WITHOUT_VERIFIED_BRAIN`.

The full QFORM conjecture remains OPEN. This report closes the exact localized three-hub faces `rank F=1` and `rank F=0` except for an explicit **actual global-null certificate**. The bounds proved below depend on kernel-to-tail exterior volume and are therefore supporting theorems, not yet universal consequences of the bare three-large-eigenvalue hypothesis. No post-rotation independence, conditional projection-density cap, unrestricted fiber supremum, or law-uniform pointwise Fresnel estimate is used.

## 1. Exact packet and first missing implication

Use the exact localized packet already present in r53-r54:

\[
A=[I_3\ Z]^T B[I_3\ Z]+\operatorname{diag}(D_H,\Delta),
\qquad F:=B+D_H,
\tag{1.1}
\]

where `B=B^T` is the three-dimensional core coefficient, `D_H` is diagonal on the three literal hub coordinates, `Z` is `3 x m`, and `Delta` is an arbitrary diagonal tail perturbation. Thus

\[
A=\begin{pmatrix}
F&BZ\\ Z^TB&Z^TBZ+\Delta
\end{pmatrix}.
\tag{1.2}
\]

All random variables are the original independent cap-one coordinates.

r54 pays every exact `rank F=2` face when the null direction couples to the tail, and identifies zero coupling with an actual global null vector. The first remaining exact-singular implication is therefore `rank F<=1`. The point of this run is to keep the complete kernel-to-tail exterior volume before choosing any physical tail minor.

## 2. Rank-one hub and the complete kernel-area currency

Assume

\[
F=\kappa ss^T,
\qquad \kappa\ne0,
\qquad \|s\|_2=1.
\tag{2.1}
\]

Let `V` be any `3 x 2` matrix with orthonormal columns spanning `s^perp`. Define the complete kernel-to-tail coupling

\[
\Omega:=Z^T D_HV\in\mathbb R^{m\times2},
\qquad
\mathcal A:=\det(\Omega^T\Omega)\ge0.
\tag{2.2}
\]

`mathcal A` is independent of the choice of orthonormal basis `V` of `s^perp`.

The key dichotomy proved below is

\[
\boxed{\mathcal A>0\ \Longrightarrow\ \text{full scalar density payment},}
\qquad
\boxed{\mathcal A=0\ \Longrightarrow\ \text{an actual global null vector}.}
\tag{2.3}
\]

## 3. `QFORM-RANK1-HUB-FIVE-MINOR-BANK-v1`

For a two-element tail set `J={j,k}`, let `Z_J` be the corresponding `3 x 2` submatrix and let `M_J` be the actual literal five-coordinate principal block of `A` consisting of all three hubs and the two tail coordinates. Then

\[
\boxed{
\det M_J=\kappa\,\det(\Omega_J)^2.
}
\tag{3.1}
\]

Consequently Cauchy--Binet gives the exact aggregate identity

\[
\boxed{
\sum_{j<k}|\det M_{\{j,k\}}|
=|\kappa|\,\det(\Omega^T\Omega)
=|\kappa|\mathcal A.
}
\tag{3.2}
\]

This is a weighted replacement for selecting a single tail pair: the entire determinant-squared pair law is summed before any reciprocal determinant is considered.

### Proof

The determinant-one congruence corresponding to the literal change of hub variables `x=u-Z_Jt` sends `M_J` to

\[
\begin{pmatrix}
F&-D_HZ_J\\
-Z_J^TD_H&Z_J^TD_HZ_J+\Delta_J
\end{pmatrix}.
\tag{3.3}
\]

Use the orthonormal hub basis `[s,V]`. The top-left block becomes `diag(kappa,0,0)`. Eliminate its nonzero scalar `kappa`. The remaining four-dimensional determinant has the form

\[
\det\begin{pmatrix}0_{2\times2}&R\\R^T&S\end{pmatrix},
\qquad R=-V^TD_HZ_J,
\tag{3.4}
\]

where `S` is arbitrary and contains every tail diagonal coefficient and the contribution from the eliminated scalar. For a square `2 x 2` matrix `R`,

\[
\det\begin{pmatrix}0&R\\R^T&S\end{pmatrix}=\det(R)^2.
\tag{3.5}
\]

Since `R^T=-Omega_J`, (3.1) follows. Summing its absolute value and applying Cauchy--Binet proves (3.2). Notice in particular that all `Delta_j` disappear from the bank identity.

## 4. Literal scalar pivot converts the whole bank into one rank-two crossing area

Choose a literal hub coordinate `i` with

\[
|s_i|=\max_h|s_h|\ge1/\sqrt3.
\tag{4.1}
\]

After permutation write `i` first and the other two hubs as `H`. The actual hub block is

\[
F=\begin{pmatrix}a&r^T\\r&P\end{pmatrix},
\qquad
a=\kappa s_i^2\ne0,
\tag{4.2}
\]

and, because `F` has rank one,

\[
P-r r^T/a=0.
\tag{4.3}
\]

Let `E=BZ` be the hub-to-tail cross matrix, with first row `e_i^T` and remaining rows `E_H`. Completing the **literal original scalar** `X_i` leaves no quadratic curvature on the two remaining hub coordinates; its residual hub-to-tail cross matrix is

\[
C:=E_H-\frac r a e_i^T.
\tag{4.4}
\]

Define

\[
L=\begin{pmatrix}-s_H/s_i&I_2\end{pmatrix}.
\tag{4.5}
\]

Then `C=LE`. Since `Ls=0`, `LF=0`, and `B=F-D_H`,

\[
C=LBZ=-LD_HZ=-(LV)(V^TD_HZ)=-(LV)\Omega^T.
\tag{4.6}
\]

Furthermore

\[
LL^T=I_2+\frac{s_Hs_H^T}{s_i^2},
\qquad
\det(LL^T)=\frac1{s_i^2}.
\tag{4.7}
\]

Because `Ls=0`, `L=(LV)V^T`, so `|det(LV)|=1/|s_i|`. Therefore the product of the two nonzero singular values of the **complete** cross matrix `C` is exactly

\[
\boxed{
\Delta_C:=\sqrt{\det(CC^T)}
=\frac{\sqrt{\mathcal A}}{|s_i|}.
}
\tag{4.8}
\]

This is the central aggregate-before-inversion identity of the run.

## 5. `QFORM-RANK1-HUB-KERNEL-AREA-COMPILER-v1`

Assume `mathcal A>0`. After completing the scalar pivot, the full quadratic form has the exact representation

\[
Q=a\bigl(X_i+\Psi(H,X_T)\bigr)^2+S(H,X_T),
\tag{5.1}
\]

where `H` consists of the two remaining **original** hub coordinates, `X_T` is the entire original tail bank, and

\[
S=F_0(H)+2H^TCX_T+G(X_T)
\tag{5.2}
\]

with arbitrary measurable internal terms `F_0,G` generated by the original quadratic/affine coefficients. The two banks `H` and `X_T` remain genuinely independent.

The completed account01/B06 theorem `QFORM-RANK2-CROSS-HALFRIESZ-v1` therefore applies to (5.2):

\[
\sup_t\mathbb E|S-t|^{-1/2}
\le4\sqrt2\,e^{1/4}\Delta_C^{-1/4}.
\tag{5.3}
\]

The cap-one law of the literal scalar `X_i` gives the standard translated-square kernel

\[
p_{a(X_i+u)^2}(y)\le |a|^{-1/2}|y|^{-1/2}
\tag{5.4}
\]

on the appropriate half-line. Averaging (5.4) against `S` and using (5.3) yields

\[
\|p_Q\|_\infty
\le4\sqrt2\,e^{1/4}|a|^{-1/2}\Delta_C^{-1/4}.
\tag{5.5}
\]

Insert `a=kappa s_i^2` and (4.8):

\[
\boxed{
\|p_Q\|_\infty
\le4\sqrt2\,e^{1/4}
|\kappa|^{-1/2}\mathcal A^{-1/8}|s_i|^{-3/4}
\le10.967\,|\kappa|^{-1/2}\mathcal A^{-1/8}.
}
\tag{5.6}
\]

The numerical front factor in the last inequality is

\[
4\sqrt2\,e^{1/4}3^{3/8}=10.9665261905\ldots .
\tag{5.7}
\]

This conclusion is for the **full ambient scalar output** in the stated rank-one localized packet; arbitrary tail diagonal curvature and all other same-bank tail curvature are retained inside `G`. It proves absolute continuity and essential boundedness. Continuity is not claimed by this half-Riesz insertion.

## 6. Exact zero-area branch is an actual global null direction

If `mathcal A=0`, then `rank Omega<=1`. Hence there is `q!=0` in `R^2` with `Omega q=0`. Put

\[
w=Vq/\|q\|.
\tag{6.1}
\]

Then `Fw=0` and

\[
Z^TD_Hw=\Omega q/\|q\|=0.
\tag{6.2}
\]

Using `B=F-D_H`, the full matrix (1.2) satisfies

\[
A\binom w0
=
\binom{Fw}{Z^TBw}
=
\binom0{-Z^TD_Hw}
=0.
\tag{6.3}
\]

Thus

\[
\boxed{
\mathcal A=0\quad\Longrightarrow\quad (w,0)\in\ker A.
}
\tag{6.4}
\]

So the exact rank-one hub face has no mysterious low-area high-dimensional survivor: it is either density-paid by (5.6) or produces a literal three-hub-supported global null eigenvector.

## 7. Actual designated-partner application

The freshest completed designated partner result available at publication is account04/B06 r3, `QFORM-TANGENTIAL-SHARED-LEAKAGE-ABSORPTION-v1`, canonical mathematics `math-open-problems@a09353b7b4cc9b1b812b1d1f2f319f5dcef5e10b`.

On the present rank-one packet assume `mathcal A>0` and whiten its complete kernel-tail coupling:

\[
R=(\Omega^T\Omega)^{-1/2}\Omega^T\in\mathbb R^{2\times m}.
\tag{7.1}
\]

The rows of `R` are orthonormal. Write the squared column leverages

\[
\ell_j=\omega_j^T(\Omega^T\Omega)^{-1}\omega_j,
\tag{7.2}
\]

where `omega_j^T` is row `j` of `Omega`. On the actual diffuse inequality

\[
\max_j\ell_j\le\frac12,
\tag{7.3}
\]

the product-Fourier step proved inside the partner theorem applies to the two tail statistics

\[
(L,V)=RX_T
\tag{7.4}
\]

and gives the concrete continuous-density estimate

\[
\boxed{\|p_{L,V}\|_\infty\le4.}
\tag{7.5}
\]

Feed this **actual partner inequality** into the exact-rank-two crossing Fourier theorem for the residual (5.2). The left bank consists of exactly two literal original hub coordinates and hence its two-dimensional density cap after an orthogonal coefficient change is one. Therefore

\[
|\phi_S(t)|
\le
\min\left\{1,\frac{2\pi}{|t|\sqrt{\Delta_C}}\right\}.
\tag{7.6}
\]

The completed one-half Riesz Fourier lemma then gives

\[
\sup_u\mathbb E|S-u|^{-1/2}\le8\Delta_C^{-1/4}.
\tag{7.7}
\]

Spending the same literal scalar square yields the partner-backed branch

\[
\boxed{
\|p_Q\|_\infty
\le8|\kappa|^{-1/2}\mathcal A^{-1/8}|s_i|^{-3/4}
\le12.079\,|\kappa|^{-1/2}\mathcal A^{-1/8}.
}
\tag{7.8}
\]

The leverage-free estimate (5.6) is numerically sharper, but (7.8) is an actual use of the designated partner theorem on the live rank-one geometry rather than a merely analogous citation. The partner provides a continuous `C_0` two-output density at (7.5); continuity of the final scalar density is still not asserted here.

## 8. `QFORM-RANK0-HUB-RANK3-CROSS-OR-GLOBALNULL-v1`

The exact `rank F=0` endpoint is even cleaner. Now `F=0`, hence `B=-D_H`. Put

\[
\Omega_0:=Z^TD_H\in\mathbb R^{m\times3}.
\tag{8.1}
\]

If `rank Omega_0=3`, then the literal three original hub coordinates have a rank-three cross matrix

\[
E=BZ=-D_HZ=-\Omega_0^T.
\tag{8.2}
\]

The completed `QFORM-THREE-HUB-JOINT-PLANCHEREL-v1` theorem allows arbitrary internal hub and tail curvature and gives a continuous `C_0` density with

\[
\boxed{
\|p_Q\|_\infty
\le3\sqrt2\,[\det(\Omega_0^T\Omega_0)]^{-1/6}.
}
\tag{8.3}
\]

If `rank Omega_0<3`, choose nonzero `w in ker Omega_0`. Since `F=0`,

\[
A\binom w0
=
\binom0{-Z^TD_Hw}=0.
\tag{8.4}
\]

Thus the exact rank-zero hub face is likewise either density-paid or supplies an actual three-hub-supported global null vector.

## 9. Combined endpoint statement and remaining debt

Combining r54 with this run gives the following exact-singular localized compiler:

- `rank F=2`: r54 pays every non-global-null branch (`omega!=0`), both signatures;
- `rank F=1`: this run pays every positive kernel-area branch (`mathcal A>0`); `mathcal A=0` gives an actual global null vector;
- `rank F=0`: this run pays the rank-three kernel-to-tail crossing branch; otherwise there is an actual global null vector.

Hence **every exact singular localized three-hub block is now reduced to either a proved density receiver or a concrete global-null certificate.** This is not yet a universal theorem because the numerical currencies in the paid branches need not be uniformly bounded below from the bare spectral hypothesis, and the near-singular transition `det F ->0` still needs a scale-stable compiler.

The next exact B06 debt is

`QFORM-GLOBALNULL-PRODUCT-QUOTIENT-OR-NEARSINGULAR-STABILITY-v1`:

> exploit the fact that the remaining null direction is supported on only three literal original coordinates, so the form depends on a two-dimensional product projection of that hub triple, and combine that bounded two-dimensional projection density with the surviving three-large spectrum without rotating it into fictitious independent coordinates; in parallel, make the exact-singular compiler stable for small nonzero `det F` by aggregating kernel-area / determinant bank currency before reciprocal hub determinants.

## 10. Checks and status

A fixed-seed diagnostic checker tests (3.1) and (4.8) on 5,000 random rank-one hub packets. The largest normalized discrepancies are approximately `2.95e-15` for the five-minor identity and `6.08e-14` for the cross-area identity. These are sanity checks only; Sections 3--8 are exact algebraic/analytic proofs.

**Full QFORM:** OPEN / NOT PROVED / NOT DISPROVED.  
**Global continuity:** OPEN.  
**New rank-one branch:** absolute continuity + essential boundedness; no final continuity claim.  
**New rank-zero rank-three-cross branch:** continuous `C_0` density.  
**Execution:** `WITHOUT_VERIFIED_BRAIN`.
