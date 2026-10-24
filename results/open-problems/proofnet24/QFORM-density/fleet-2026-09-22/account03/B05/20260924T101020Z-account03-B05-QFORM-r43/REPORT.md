SIGNED IN - working on the quadratic-form bounded-density conjecture (universal constant), account account03, slot B05, 2026-09-24T10:10:20Z.
attacking: QFORM-HIGHLEVERAGE-BALANCED-REGRESSION-CROSSING-v1 — turn the diffuse transverse aggregate star into a balanced original-coordinate rank-three crossing, or isolate the exact two-bank regression-gap factor when that crossing degenerates.

# account03/B05 — balanced transverse split, exact regression crossing, and finite-spike survivor

**Programme:** `QFORM-DENSITY-3EIG-20260922`  
**Assignment:** quadratic coarea / equivalent interval bounds preserving arbitrary original-coordinate product densities.  
**Run:** `20260924T101020Z-account03-B05-QFORM-r43`.  
**Status:** **NEW SUPPORTING EXACT-RANK-THREE COMPILER + NEW CONTINUOUS-DENSITY BRANCH / FULL QFORM OPEN**.  
**Regularity:** continuous `C_0` density is proved on the exact-cross and diffuse-complement branches below; the pair-star and designated definite-pair branches give essential boundedness. Full-target continuity remains open.  
**Execution:** `WITHOUT_VERIFIED_BRAIN`.

Fresh startup control was read from `yspennstate/math-research-brain@853f24ee3f2ec6baa05deceaac1c498feacdd154`; OWNER CONTROL remains revision `2026-09-22.15`, QFORM-only. Before publication I refresh controls and corrections again. Nothing below uses law-uniform pointwise quadratic-phase decay, an arbitrary-joint rank-three coarea theorem, a conditional projection-density cap, independence after rotating random coordinates, a curved-fiber supremum, moments, support bounds, log-concavity, or deletion of a small random term.

The immediate same-slot source is

`yspennstate/math-open-problems@461ca4597face7955d318d0540729ca6b809fce2`

`proofnet24/QFORM-density/fleet-2026-09-22/account03/B05/20260924T093516Z-account03-B05-QFORM-r44/REPORT.md`.

That run isolated the diffuse nonzero-pivot aggregate-star collar. The present run turns most of that collar into a literal original-coordinate rank-three crossing and identifies the exact factor when the crossing degenerates.

## 1. Exact-rank-three high-leverage setup

Let

\[
A=RMR^T,\qquad R^TR=I_3,
\tag{1.1}
\]

have exact rank three, where `M=M^T` is invertible and its three eigenvalues have modulus at least one. Put

\[
D:=|\det M|\ge1.
\tag{1.2}
\]

Fix an ORIGINAL coordinate `i` with spectral leverage

\[
c:=\|r_i\|^2\ge\frac12.
\tag{1.3}
\]

Rotate only the deterministic three-dimensional coefficient bookkeeping so that

\[
r_i=\sqrt c\,e_1.
\tag{1.4}
\]

No random variable is rotated. For every `j\ne i` write

\[
r_j=(x_j,t_j),\qquad t_j=(y_j,z_j)^T\in\mathbb R^2,
\qquad q_j:=\|t_j\|^2.
\tag{1.5}
\]

Parseval gives the exact identities

\[
\sum_{j\ne i}x_j^2=1-c=:s,
\qquad
\sum_{j\ne i}x_jt_j=0,
\qquad
\sum_{j\ne i}t_jt_j^T=I_2.
\tag{1.6}
\]

The previous r44 determinant-star identities are

\[
T_{ij}:=\sum_{k\notin\{i,j\}}|\det A_{\{i,j,k\}}|
      =cDq_j,
\tag{1.7}
\]

and

\[
\sum_{\substack{j<k\\j,k\ne i}}|\det A_{\{i,j,k\}}|=cD.
\tag{1.8}
\]

The point is to spend (1.8) before selecting a tiny physical minor.

## 2. First improvement: the transverse-heavy threshold is `1/4`, not `1/2`

My completed theorem `QFORM-PAIR-ANCHORED-DETSTAR-COAREA-v1`, source

`yspennstate/math-open-problems@22d59171a8870dbcdbf7641e990800db2fc9df42`

`proofnet24/QFORM-density/fleet-2026-09-22/account03/B05/20260924T033744Z-account03-B05-QFORM-r39/REPORT.md`,

states that every exact-rank-three form and every literal pair with `T_{ij}>0` obey

\[
\|p_Q\|_{\infty,\mathrm{ess}}
\le C_\star T_{ij}^{-1/3},
\qquad
C_\star=24(3+\sqrt2)10^{2/3}=491.735145127\ldots .
\tag{2.1}
\]

It remains valid when the physical pair itself is singular.

Therefore if

\[
q_*:=\max_{j\ne i}q_j\ge\frac14,
\tag{2.2}
\]

then (1.3), (1.7), and `D>=1` give `T_{ij}>=1/8` for some `j`, hence

\[
\boxed{
\|p_Q\|_{\infty,\mathrm{ess}}
\le2C_\star<983.471.
}
\tag{2.3}
\]

Thus the genuinely diffuse transverse survivor may be assumed to satisfy

\[
\boxed{q_*<\frac14.}
\tag{2.4}
\]

This sharper gate is useful because it supplies a uniformly nondegenerate two-bank transverse split.

## 3. A balanced original-coordinate split of the transverse Parseval frame

For `j<k` put

\[
w_{jk}:=\det(t_j,t_k)^2.
\tag{3.1}
\]

Cauchy--Binet and (1.6) give

\[
\sum_{j<k}w_{jk}=1.
\tag{3.2}
\]

The weighted degree of vertex `j` is

\[
d_j:=\sum_{k\ne j}w_{jk}=q_j.
\tag{3.3}
\]

Indeed

\[
\sum_k\det(t_j,t_k)^2
=\|t_j\|^2\operatorname{tr}I_2-t_j^TI_2t_j=q_j.
\]

Randomly partition the complementary ORIGINAL coordinates into `J\sqcup K`, each coordinate independently going left/right with probability `1/2`. Define

\[
G:=\sum_{j\in J}t_jt_j^T,
\qquad
G_K:=I_2-G=\sum_{k\in K}t_kt_k^T.
\tag{3.4}
\]

By Cauchy--Binet,

\[
\det G=\sum_{j<k\in J}w_{jk},
\qquad
\det G_K=\sum_{j<k\in K}w_{jk}.
\tag{3.5}
\]

In the product `det G det G_K`, an ordered pair of Pluecker edges contributes exactly when the two edges are vertex-disjoint, in which case the random split places the first wholly in `J` and the second wholly in `K` with probability `1/16`. The total ordered weight of intersecting edge pairs is at most `sum_j d_j^2`. Hence

\[
\mathbb E[\det G\det G_K]
\ge\frac1{16}\left(1-\sum_jd_j^2\right)
\ge\frac{1-2q_*}{16},
\tag{3.6}
\]

because `sum_j d_j=2`. Consequently some deterministic original-coordinate split satisfies

\[
\boxed{
P:=\det G\det G_K
\ge\frac{1-2q_*}{16}
>\frac1{32}.
}
\tag{3.7}
\]

This is the same aggregate-before-inversion mechanism underlying r31, now applied directly to the r44 transverse frame. In particular both `G` and `G_K` are positive definite.

## 4. Longitudinal regression residuals and the exact crossing volumes

For the split from Section 3 define

\[
a:=\sum_{j\in J}x_j^2,
\qquad
b:=\sum_{j\in J}x_jt_j.
\tag{4.1}
\]

Then by (1.6), on the other bank

\[
\sum_{k\in K}x_k^2=s-a,
\qquad
\sum_{k\in K}x_kt_k=-b.
\tag{4.2}
\]

Define the two least-squares residual energies

\[
\rho_J:=a-b^TG^{-1}b,
\qquad
\rho_K:=(s-a)-b^TG_K^{-1}b.
\tag{4.3}
\]

They are nonnegative because they are Schur complements of the positive-semidefinite bank Gram matrices. Explicitly,

\[
H_J:=\sum_{j\in J}r_jr_j^T
=\begin{pmatrix}a&b^T\\b&G\end{pmatrix},
\qquad
H_K:=\sum_{k\in K}r_kr_k^T
=\begin{pmatrix}s-a&-b^T\\-b&G_K\end{pmatrix},
\tag{4.4}
\]

so

\[
\det H_J=(\det G)\rho_J,
\qquad
\det H_K=(\det G_K)\rho_K.
\tag{4.5}
\]

Now add the literal hub row to one bank. The corresponding coefficient Grams are

\[
H_{\{i\}\cup J}=c e_1e_1^T+H_J,
\qquad
H_{\{i\}\cup K}=c e_1e_1^T+H_K,
\tag{4.6}
\]

and another Schur-complement calculation gives

\[
\boxed{
\det H_{\{i\}\cup J}=(\det G)(c+\rho_J),
\qquad
\det H_{\{i\}\cup K}=(\det G_K)(c+\rho_K).
}
\tag{4.7}
\]

Consider the physical crossing for the original-coordinate cut

\[
S=\{i\}\cup J,\qquad T=K.
\]

Its cross block is

\[
B_{S,T}=R_SMR_T^T.
\tag{4.8}
\]

Whenever `rho_K>0`, both coefficient Grams in this factorization have rank three. Thin QR/Cauchy--Binet therefore gives the exact product of the three nonzero crossing singular values

\[
\boxed{
\Delta_K
:=\prod_{m=1}^3s_m(B_{S,T})
=D\sqrt{P(c+\rho_J)\rho_K}.
}
\tag{4.9}
\]

Similarly, for `S=J`, `T=\{i\}\cup K`,

\[
\boxed{
\Delta_J
=D\sqrt{P\rho_J(c+\rho_K)}.
}
\tag{4.10}
\]

These identities are exact. They do not approximate the coefficient tails or infer independence after a spectral rotation.

The determinant-sensitive exact-cross theorem is the product-preserving result at

`yspennstate/math-open-problems@95f94696393b5ad8b0def71fa0d93082de92bd85`

`proofnet24/QFORM-density/fleet-2026-09-22/account03/B05/20260923T193756Z-account03-B05-QFORM-r31/REPORT.md`, based on the exact-cross Fourier theorem at

`yspennstate/math-open-problems@51d2edb29d7a4c150e4d47ed3a6685875a8483ae`

`proofnet24/QFORM-density/interactive/20260923T194300Z-exact-cross-rank-fourier/REPORT.md`.

For either original-coordinate cut above it gives

\[
\boxed{\|p_Q\|_\infty\le6\Delta^{-1/3}}
\tag{4.11}
\]

and a continuous `C_0` density. The projected density factors used in that theorem are paid by the determinants in (4.9)-(4.10); no smallest physical minor is selected.

### Quantitative payment

If

\[
\max(\rho_J,\rho_K)\ge\frac1{16},
\tag{4.12}
\]

choose the crossing with that residual on the hub-free side. From `D>=1`, `P>1/32`, and `c>=1/2`,

\[
\Delta\ge
\sqrt{\frac1{32}\frac12\frac1{16}}
=\frac1{32}.
\tag{4.13}
\]

Therefore

\[
\boxed{
\|p_Q\|_\infty
\le6\,32^{1/3}
=19.0488126236\ldots<19.049,
\qquad p_Q\in C_0(\mathbb R).
}
\tag{4.14}
\]

This is the first new paid part of the r44 aggregate-star collar.

## 5. Exact identity when both crossings are nearly rank two

Suppose now

\[
\rho_J<\frac1{16},
\qquad
\rho_K<\frac1{16}.
\tag{5.1}
\]

Define the bank regression slopes

\[
u_J:=G^{-1}b,
\qquad
u_K:=G_K^{-1}(-b),
\qquad
w:=u_J-u_K.
\tag{5.2}
\]

Because `G_K=I-G`, the two matrices commute and

\[
G^{-1}+G_K^{-1}=[G(I-G)]^{-1}.
\tag{5.3}
\]

Thus

\[
w=[G(I-G)]^{-1}b.
\tag{5.4}
\]

Adding the two regression decompositions in (4.3) gives the exact identity

\[
\boxed{
1-c
=\rho_J+\rho_K+w^TG(I-G)w.
}
\tag{5.5}
\]

This is the precise factor lost by the rank-three crossing when both bank determinants collapse: the missing longitudinal direction is not absent; it is encoded as a **change of regression slope between two transverse banks**.

The balanced split (3.7) controls this metric quantitatively. Since the two eigenvalues of `G(I-G)` are each at most `1/4`, while

\[
\det(G(I-G))=P>\frac1{32},
\]

both eigenvalues are strictly larger than `1/8`. Hence

\[
\boxed{
\frac18\|w\|^2
<w^TG(I-G)w
\le\frac14\|w\|^2.
}
\tag{5.6}
\]

In particular, if the hub is not yet a near-coloop,

\[
c\le\frac34,
\tag{5.7}
\]

then `1-c>=1/4`, so (5.1), (5.5) imply

\[
\boxed{
w^TG(I-G)w>\frac18,
\qquad
\|w\|^2>\frac12.}
\tag{5.8}
\]

Thus the unpaid moderate-leverage endpoint is no longer described only as “aggregate star spread over many rows.” It is a quantitatively separated two-plane geometry: both original-coordinate banks are almost rank two in the full three-frame, but their longitudinal-on-transverse regression slopes differ by more than `1/sqrt(2)`.

The r44 isotropic-star stress family lands exactly here. For the natural sign cut one has

\[
G=G_K=\frac12I_2,
\quad
\rho_J=\rho_K=0,
\quad
w=(\sqrt2,0),
\]

so `w^TG(I-G)w=1/2=1-c`. The new identity therefore captures the exact obstruction rather than missing it.

## 6. Fresh diffuse-complement receiver and the finite-spike reduction

There is an additional payment available from the fresh account03/B19 theorem

`QFORM-BL-EXACTRANK-LATENT-ENDPOINT-v1`,

source

`yspennstate/math-open-problems@0c72e9d098b6a02da82ac63c3d856316587d7ea4`

`proofnet24/QFORM-density/fleet-2026-09-22/account03/B19/20260924T100359Z-account03-B19-QFORM-r53/REPORT.md`.

Assume `s=1-c>0`. Normalize the complementary spectral frame by

\[
\widetilde r_j=
\left(\frac{x_j}{\sqrt s},t_j\right),
\qquad j\ne i.
\tag{6.1}
\]

By (1.6),

\[
\sum_{j\ne i}\widetilde r_j\widetilde r_j^T=I_3.
\tag{6.2}
\]

Its physical row leverages are

\[
\ell_j:=\|\widetilde r_j\|^2
=\frac{x_j^2}{s}+q_j.
\tag{6.3}
\]

The complementary principal block is exactly

\[
A_{i^c,i^c}=\widetilde R\,\widetilde M\,\widetilde R^T,
\qquad
\widetilde M=\operatorname{diag}(\sqrt s,1,1)
M\operatorname{diag}(\sqrt s,1,1),
\tag{6.4}
\]

and

\[
|\det\widetilde M|=sD.
\tag{6.5}
\]

All coupling to the omitted literal hub is allowed by the cited B19 theorem. Hence if

\[
\max_{j\ne i}\ell_j\le\frac12,
\tag{6.6}
\]

then the full ambient quadratic form has a continuous `C_0` density with

\[
\boxed{
\|p_Q\|_\infty\le12(sD)^{-1/3}.
}
\tag{6.7}
\]

On the moderate-hub chamber `c<=3/4`, `s>=1/4` and `D>=1`, so

\[
\boxed{
\|p_Q\|_\infty
\le12\,4^{1/3}
=19.0488126236\ldots<19.049.
}
\tag{6.8}
\]

If (6.6) fails while the transverse-heavy branch has already been removed by (2.4), then every bad row satisfies

\[
\frac{x_j^2}{s}
=\ell_j-q_j
>\frac12-\frac14
=\frac14.
\tag{6.9}
\]

Since `sum_j x_j^2/s=1`, there can be at most three such rows. Thus every unpaid moderate-hub state has an explicit **finite literal longitudinal-spike set of cardinality at most three**.

Combining Sections 4--6: after the paid branches, a surviving state with `c<=3/4` has at most three literal longitudinal spikes, both balanced-bank regression residuals `<1/16`, and the two bank slopes satisfy (5.8). This is a much smaller product-preserving endpoint than the original diffuse aggregate-star collar.

## 7. Required designated partner application

The designated partner `account04/B05` theorem is

`QFORM-PHYSICAL-DEFINITE-PAIR-COAREA-v1`,

canonical source

`yspennstate/math-open-problems@33cabb3bd5e466a58adc6eac49eba210ef62ef14`

`proofnet24/QFORM-density/fleet-2026-09-22/account04/B05/20260924T011830Z-account04-B05-convex-pair-r3/REPORT.md`.

For every literal original-coordinate definite `2x2` principal block `C`, with arbitrary outside coupling retained,

\[
\|p_Q\|_{\infty,\mathrm{ess}}
\le\frac\pi{\sqrt{|\det C|}}.
\tag{7.1}
\]

Apply it at the actual hub pair `C=A_{\{i,j\},\{i,j\}}`. If

\[
\det C\ge\frac1{16},
\tag{7.2}
\]

then `C` is definite and the completed partner theorem gives

\[
\boxed{
\|p_Q\|_{\infty,\mathrm{ess}}
\le4\pi
=12.5663706144\ldots<12.567.
}
\tag{7.3}
\]

Thus the genuinely unpaid collar may additionally be assumed to have no positive hub-pair determinant at least `1/16`. This application is only to literal independent coordinates; no spectral coordinates are treated as independent.

## 8. Compiler and exact remaining factor

### Theorem `QFORM-HIGHLEVERAGE-BALANCED-REGRESSION-CROSSING-v1`

Under the exact-rank-three target normalization `D>=1`, fix an original coordinate with spectral leverage `c>=1/2`. Then at least one of the following applies:

1. **transverse-heavy star:** `max q_j>=1/4`, and
   \[
   \|p_Q\|_{\infty,\mathrm{ess}}<983.471;
   \]
2. **balanced rank-three physical crossing:** `max q_j<1/4` and the balanced split from Section 3 has `max(rho_J,rho_K)>=1/16`, and
   \[
   \|p_Q\|_\infty<19.049,
   \qquad p_Q\in C_0(\mathbb R);
   \]
3. **diffuse complementary rank-three carrier:** `c<=3/4` and every normalized complementary row leverage is at most `1/2`, and
   \[
   \|p_Q\|_\infty<19.049,
   \qquad p_Q\in C_0(\mathbb R);
   \]
4. **moderate-hub finite-spike regression-gap survivor:** `c<=3/4`, there are at most three normalized longitudinal-heavy literal rows, both balanced-bank residuals are `<1/16`, and
   \[
   w^TG(I-G)w>1/8,
   \qquad \|w\|^2>1/2;
   \]
5. **near-coloop survivor:** `c>3/4`.

Independently, any literal definite hub pair with determinant at least `1/16` is paid by the designated partner with `<=4pi`.

The exact new missing factor is therefore not aggregate Pluecker mass itself: after transverse balancing, that mass already gives `P>1/32`. The missing factor is the **longitudinal bank regression area**. If either bank retains residual longitudinal area, the exact rank-three crossing pays it. If neither does, the longitudinal direction survives as a quantitative change of bank regression slope, equation (5.5). In the moderate-hub regime, the fresh diffuse-latent theorem further shows that only at most three literal longitudinal spikes can obstruct a complete payment.

The next B05 implication is consequently

`QFORM-HIGHLEVERAGE-THREESPIKE-REGRESSION-GAP-COAREA-v1`:

> retain the at-most-three literal longitudinal spikes jointly with the two balanced transverse product banks and spend the slope-gap currency `w^T G(I-G)w>1/8` before conditioning on any projected variable. The receiver must remain uniform as the two regression residuals tend to zero and must not pay a reciprocal individual physical minor.

A separate neighboring endpoint is the genuine near-coloop chamber `c>3/4`; the exact physical-null-pivot part of that chamber is already closed by account01/B05's `QFORM-HIGHLEVERAGE-NULLPIVOT-WITT-CLOSURE-v1`.

## 9. Scope audit

**Proved here:** the balanced split (3.7) after lowering the transverse-heavy threshold to `1/4`; the exact crossing-volume formulas (4.9)-(4.10); the continuous `<19.049` crossing branch; the exact regression-gap identity (5.5) and metric bounds (5.6)-(5.8); and the reduction of the moderate-hub complement to at most three literal longitudinal spikes using the fresh B19 exact-rank latent receiver.

**Actually applied designated partner:** account04/B05 definite-pair coarea at (7.2)-(7.3).

**Not proved:** the three-spike regression-gap receiver, the near-coloop nonzero-pivot endpoint, arbitrary exact rank three, arbitrary higher-rank matrices, the full QFORM conjecture, or full-target continuity. No counterexample to QFORM is claimed.

## 10. Source pins

- Startup control: `yspennstate/math-research-brain@853f24ee3f2ec6baa05deceaac1c498feacdd154`, OWNER CONTROL revision `2026-09-22.15`.
- Immediate own r44: `math-open-problems@461ca4597face7955d318d0540729ca6b809fce2`.
- Pair-star theorem r39: `math-open-problems@22d59171a8870dbcdbf7641e990800db2fc9df42`.
- Determinant-sensitive exact crossing r31: `math-open-problems@95f94696393b5ad8b0def71fa0d93082de92bd85`.
- Underlying exact-cross theorem: `math-open-problems@51d2edb29d7a4c150e4d47ed3a6685875a8483ae`.
- Fresh diffuse latent endpoint: `math-open-problems@0c72e9d098b6a02da82ac63c3d856316587d7ea4`.
- Designated account04/B05 definite-pair theorem: `math-open-problems@33cabb3bd5e466a58adc6eac49eba210ef62ef14`.
- Exact-null high-leverage closure: `math-open-problems@1ca1fc77ae8435274325c25657c496fd703c0b51`.

Repository use is not native brain ingestion; status remains `WITHOUT_VERIFIED_BRAIN`.
