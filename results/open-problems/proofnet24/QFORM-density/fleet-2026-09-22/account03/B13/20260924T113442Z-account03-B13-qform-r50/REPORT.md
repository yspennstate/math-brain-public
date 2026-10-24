SIGNED IN - working on the quadratic-form bounded-density conjecture (universal constant), account account03, slot B13, 2026-09-24T11:34:42Z.
attacking: the r49 heavy-Schur-row survivor by one literal physical deletion inside the exact rank-two Schur carrier, using an L^3 diffuse receiver before reinserting the heavy square.

# account03/B13 r50 — heavy Schur deletion: tiny currency or a second heavy row

Programme: `QFORM-DENSITY-3EIG-20260922`  
Run: `20260924T113442Z-account03-B13-qform-r50`  
Role: extremal product laws / quantitative inequalities and rigorous computations  
Execution: `WITHOUT_VERIFIED_BRAIN`  
Status: **NEW SUPPORTING THEOREM / DESIGNATED PARTNER APPLIED / FULL QFORM OPEN**.

All probabilistic coordinates below remain the original independent physical coordinates. The only rotations used are inside the two-dimensional coefficient space. No Gaussian, moment, log-concave, compact-support, connected-support, interval-extremality, bounded-diameter, fixed-fragment-count, post-rotation independence, pointwise scalar van-der-Corput, unrestricted fiber-supremum, or coefficient-small-implies-random-small step is used.

## 1. Starting packet from r49

Use account03/B13 r49:

`yspennstate/math-open-problems@ac6e24e64237a6e6f3be4ca826106b1bf6d39b70`

`proofnet24/QFORM-density/fleet-2026-09-22/account03/B13/20260924T103426Z-account03-B13-qform-r49/REPORT.md`.

In the non-ultracollapse part of the exact diagonal-plus-rank-two chamber, there is an original-coordinate indefinite pair `I={k,j}` with

\[
D_B:=|\det B|\ge D_0:=\frac{1001}{12544},\qquad
\kappa_B:=\sigma_{\min}(B)\ge \kappa_0:=\frac{13}{112},
\]

and, after completing this pair, the exact residual Schur form is

\[
S=D_R+WLW^T,\qquad W^TW=I_2.
\]

Moreover

\[
|\det L|\ge a_0\frac{|\det\Lambda|}{D_B},
\qquad a_0:=\frac{49}{576},
\]

while the non-ultracollapse packet obeys

\[
|\det\Lambda|\ge K_\Lambda \rho^{-4},
\qquad K_\Lambda:=6144e^2.
\]

If every residual row leverage is at most `1/2`, r49 already gives
\(\rho\le209.077161\). Hence every witness with

\[
\rho>209.078
\]

in this packet has an original residual coordinate \(h\) with

\[
c:=\|w_h\|^2>\frac12.
\]

The product-indicator reduction from r49 remains in force: the supremum over cap-one mass-one product densities equals the supremum over arbitrary unit-measure product indicators, in the supremal/epsilon-near-maximizer sense only. Nothing below strengthens this to interval extremality.

## 2. Inputs used after the heavy row is exposed

Two previously completed analytic facts are used exactly within their stated scopes.

First, `QFORM-DIFFUSE-RANK2-L3-SEPARABLE-v1`, source

`yspennstate/math-open-problems@d094743ca1c1429601fe7fdc4a4f548103a62bb0`

gives, for a rank-two Parseval physical frame \(V\) whose row leverages are at most \(1/2\), an invertible symmetric coefficient \(C\), and arbitrary coordinate-separable quadratic/affine phases,

\[
\|p_T\|_3\le (3e)^{2/3}|\det C|^{-1/3}.
\tag{2.1}
\]

Second, account03/B06 r52 proves the dependence-safe \(L^3\)-to-\(L^\infty\) square smoothing lemma: if \(T\) has density \(p_T\) with \(\|p_T\|_3\le M_3\), and conditionally on the remaining variables a translated original physical coordinate still has density cap one, then for \(q\ne0\)

\[
T+qV^2
\quad\text{has density cap}\quad
4|q|^{-1/2}M_3^{3/4}.
\tag{2.2}
\]

Source:

`yspennstate/math-open-problems@fdcb2e5ac7ce86f617c79cbeaae2d33aafd25a7a`

`proofnet24/QFORM-density/fleet-2026-09-22/account03/B06/20260924T052046Z-account03-B06-qform-r52/REPORT.md`.

Finally, r49's source-pinned physical-pair logarithmic smoothing theorem says: if the Schur scalar \(R\) satisfies

\[
\sup_t\Pr\{|R-t|<r\}\le H\sqrt r,
\tag{2.3}
\]

then

\[
\|p_Q\|_\infty
\le4\sqrt{2H}\,(D_B\kappa_B)^{-1/4}.
\tag{2.4}
\]

## 3. Exact one-heavy-row deletion

Fix a heavy residual row \(h\), write \(w=w_h\), \(c=\|w\|^2\), and decompose the actual Schur diagonal coefficient as

\[
b:=w^TLw,\qquad d:=d_h,\qquad q:=S_{hh}=d+b.
\tag{3.1}
\]

Assume first

\[
\frac12<c<1,\qquad dq\ne0.
\tag{3.2}
\]

Let \(W_0\) be \(W\) with row \(h\) removed. Then

\[
G:=W_0^TW_0=I_2-ww^T,\qquad \det G=1-c.
\tag{3.3}
\]

Completing the square only in the literal independent coordinate \(X_h\) gives

\[
X_R^TSX_R
=
q\bigl(X_h+m(X_{R\setminus\{h\}})\bigr)^2+T_h,
\tag{3.4}
\]

where all remaining diagonal terms are retained and the rank-two carrier of \(T_h\) is

\[
L_h=L-\frac{(Lw)(Lw)^T}{q}.
\tag{3.5}
\]

Normalize the entire surviving physical product frame by

\[
V=W_0G^{-1/2},\qquad V^TV=I_2,
\qquad C_h=G^{1/2}L_hG^{1/2}.
\tag{3.6}
\]

The determinant currency is exact. By the matrix determinant lemma,

\[
\det L_h
=\det L\left(1-\frac{w^TLw}{q}\right)
=\det L\,\frac d q,
\tag{3.7}
\]

and therefore

\[
\boxed{
\det C_h=(1-c)\det L\,\frac d q.
}
\tag{3.8}
\]

For every surviving original coordinate \(r\ne h\), define the normalized post-deletion leverage

\[
\eta_r:=w_r^TG^{-1}w_r.
\tag{3.9}
\]

## 4. Heavy-row sequential receiver

### Theorem 4.1 — `QFORM-HEAVY-SCHUR-SEQUENTIAL-L3-RECEIVER-v1`

Under (3.2), if

\[
\max_{r\ne h}\eta_r\le\frac12,
\tag{4.1}
\]

then the Schur scalar \(R:=X_R^TSX_R\) has an essentially bounded density with

\[
\boxed{
\|p_R\|_\infty
\le
4\sqrt{3e}\,
\bigl((1-c)|\det L|\,|d q|\bigr)^{-1/4}.
}
\tag{4.2}
\]

Consequently the full quadratic form satisfies

\[
\boxed{
\|p_Q\|_\infty
\le
2^{13/4}(3e)^{1/8}
(D_B\kappa_B)^{-1/4}
\bigl((1-c)|\det L|\,|d q|\bigr)^{-1/16}.
}
\tag{4.3}
\]

#### Proof

Under (4.1), apply (2.1) to the complete residual \(T_h\). The diagonal tail and all affine terms remain coordinate-separable, so

\[
\|p_{T_h}\|_3
\le(3e)^{2/3}|\det C_h|^{-1/3}.
\tag{4.4}
\]

Because \(X_h\) is an untouched original independent coordinate, conditioning on all other physical coordinates turns
\(X_h+m(\cdot)\) into a translation of its original cap-one density. Thus (2.2) applies to (3.4):

\[
\|p_R\|_\infty
\le4|q|^{-1/2}
\left[(3e)^{2/3}|\det C_h|^{-1/3}\right]^{3/4}.
\tag{4.5}
\]

Using (3.8),

\[
\|p_R\|_\infty
\le4\sqrt{3e}\,
|q|^{-1/2}
\left((1-c)|\det L|\frac{|d|}{|q|}\right)^{-1/4},
\]

which is exactly (4.2).

Put \(M=\|p_R\|_\infty\). Then for every \(r>0\),

\[
\Pr\{|R-t|<r\}\le\min\{1,2Mr\}
\le\sqrt{2M}\,\sqrt r.
\tag{4.6}
\]

Hence (2.3) holds with \(H=\sqrt{2M}\). Substitute this into (2.4):

\[
\|p_Q\|_\infty
\le4\,2^{3/4}M^{1/4}(D_B\kappa_B)^{-1/4}.
\tag{4.7}
\]

Taking the fourth root of (4.2) yields the factor
\(4^{1/4}(3e)^{1/8}=2^{1/2}(3e)^{1/8}\), proving (4.3). QED.

The theorem is dependence-safe: no conditional density cap is asserted for a rotated coordinate, and arbitrary same-bank diagonal curvature remains in the residual before the \(L^3\) estimate.

## 5. Quantitative high-ratio compiler: tiny deletion currency or second heavy row

Insert the r49 determinant transport

\[
|\det L|\ge a_0\frac{|\det\Lambda|}{D_B},
\qquad a_0=\frac{49}{576},
\tag{5.1}
\]

into (4.3), and use the physical-pair floors \(D_B\ge D_0\), \(\kappa_B\ge\kappa_0\). This gives

\[
\|p_Q\|_\infty
\le
C_0\,|\det\Lambda|^{-1/16}
\bigl((1-c)|dq|\bigr)^{-1/16},
\tag{5.2}
\]

where

\[
C_0
=
2^{13/4}(3e)^{1/8}
D_0^{-3/16}\kappa_0^{-1/4}a_0^{-1/16}
=
39.706137279\ldots .
\tag{5.3}
\]

On the non-ultracollapse packet

\[
|\det\Lambda|\ge K_\Lambda\rho^{-4},
\qquad K_\Lambda=6144e^2,
\tag{5.4}
\]

this becomes

\[
\|p_Q\|_\infty
\le
C_1\rho^{1/4}
\bigl((1-c)|dq|\bigr)^{-1/16},
\qquad
C_1=20.313868142\ldots .
\tag{5.5}
\]

Since every slab witness ratio satisfies \(\rho\le\|p_Q\|_\infty\), (5.5) forces

\[
\boxed{
(1-c)|d q|
\le K_{50}\rho^{-12},
\qquad
K_{50}:=C_1^{16}
<8.408\times10^{20}.
}
\tag{5.6}
\]

If \(c=1\), \(d=0\), or \(q=0\), the left side of (5.6) is already zero, so the same conclusion holds without invoking Theorem 4.1.

If (4.1) fails instead, there is a second literal original residual coordinate \(g\) with

\[
\boxed{
\eta_g=w_g^T(I-ww^T)^{-1}w_g>\frac12.
}
\tag{5.7}
\]

Equivalently, the twice-deleted normalized frame has exact volume collapse

\[
\boxed{
\det(I-ww^T-w_gw_g^T)
=(1-c)(1-\eta_g)
<\frac{1-c}{2}.
}
\tag{5.8}
\]

Thus every r49 high-ratio heavy-row survivor obeys the exhaustive structural alternative

\[
\boxed{
\text{second normalized heavy row}
\quad\text{or}\quad
(1-\|w_h\|^2)|d_hS_{hh}|
\le8.408\times10^{20}\rho^{-12}.
}
\tag{5.9}
\]

This is the first quantitative receiver on the r49 heavy row itself; it retains the entire same-bank Schur curvature and therefore does not use the refuted “one heavy row plus one cross coefficient pays everything” shortcut.

## 6. Designated account04/B13 result applied to the actual inequality

Use account04/B13's completed fifth-diagonal sparsification theorem:

`yspennstate/math-open-problems@635da12cb1c19b27c455c662be800eb1113dd845`

`proofnet24/QFORM-density/fleet-2026-09-22/account04/B13/20260924T031520Z-account04-B13-diagonal-sparsification-r2/REPORT.md`.

It states

\[
d_{(5)}\le\frac{C_5}{\rho},
\qquad
C_5=2\sqrt{30\pi}=19.416259126\ldots .
\tag{6.1}
\]

The r48 physical pair satisfies \(|d_k|,|d_j|\ge7/8\). For

\[
\rho>\frac{8C_5}{7}=22.19001043\ldots,
\tag{6.2}
\]

both pair coordinates must therefore lie among the four largest diagonal coordinates. Since the present branch already has \(\rho>209.078\), after removing the pair there are at most **two** residual diagonal-center coordinates. Every other residual physical row obeys

\[
\boxed{|d_h|\le19.416260\,\rho^{-1}.}
\tag{6.3}
\]

Apply this to the heavy row from r49. Combining (5.9) with (6.3) yields the following actual partner-driven trichotomy:

1. **Two-heavy chain:** some \(g\) satisfies (5.7), with the exact volume collapse (5.8); or
2. **Small-twist heavy row:** the chosen heavy row is outside the at-most-two residual diagonal centers and
   \[
   |d_h|\le19.416260\,\rho^{-1};
   \tag{6.4}
   \]
   or
3. **Residual diagonal center:** \(h\) is one of at most two residual centers and \(|d_h|>C_5/\rho\). In the diffuse post-deletion branch, (5.6) then forces
   \[
   \boxed{
   (1-c)|S_{hh}|
   \le
   \frac{K_{50}}{C_5}\rho^{-11}
   <
   4.331\times10^{19}\rho^{-11}.
   }
   \tag{6.5}
   \]

So an unbounded-ratio non-ultracollapse sequence can no longer retain a generic isolated heavy Schur row. It must move into a second-heavy normalized chain, an \(O(\rho^{-1})\) physical diagonal-twist row, or one of only two residual diagonal centers whose near-coloop/near-null product is \(O(\rho^{-11})\).

The account04/B13 fixed physical-star conclusion from r49 remains simultaneously active in this same packet; it is not used to erase or perturb any of the terms above.

## 7. Status and next exact obligation

This run does **not** prove unrestricted QFORM and does not prove global continuity. The new receiver proves essential boundedness in the stated diffuse-after-heavy-deletion branch.

The first remaining B13 implication is now:

`QFORM-SECONDHEAVY-OR-SMALLTWIST-HEAVYROW-RECEIVER-v1`.

It must pay one of the three survivors in Section 6 while retaining:
- the original uniformly indefinite physical pair,
- the account04 physical star,
- all remaining coordinate-separable diagonal curvature,
- and the exact rank-two same-bank carrier.

The live correction `QFORM-ONE-HEAVY-ROW-SAME-SQUARE-ABSORPTION-FALSE-v1` is respected: no single cross coefficient is treated as a complete receiver.

Full QFORM: **OPEN / not proved / not disproved**.  
Full-target continuity: **OPEN**.  
Execution: `WITHOUT_VERIFIED_BRAIN` because authenticated repository retrieval/use occurred but authenticated native receiver ingestion was not established.
