SIGNED IN - working on the quadratic-form bounded-density conjecture (universal constant), account fleet03, slot B05, 2026-09-24T06:09:43Z.
attacking: QFORM-WITT-AGGREGATE-RESIDUAL-RECEIVER-v2 — derive a dependence-safe bank-residual small-ball/coarea inequality from aggregate within-bank Pluecker curvature.

# fleet03/B05 r41 — exact rank-three crossing volume in the live Witt packet

**Programme:** QFORM-DENSITY-3EIG-20260922.  
**Assignment:** quadratic coarea/equivalent interval bounds preserving arbitrary original-coordinate product densities.  
**Status:** new supporting theorem plus exact obstruction; full QFORM remains OPEN / NOT PROVED / NOT DISPROVED.  
**Regularity:** the paid exact-cross branches below have bounded continuous densities; the full-target continuity conclusion remains OPEN.  
**Execution:** `WITHOUT_VERIFIED_BRAIN`.

## 1. Sources and corrections actually consumed

I use the live exact Witt packet from fleet01/B05 and the correction-aware fleet03/B05 r40 decomposition. The current fleet02/B05 report proves that a nonzero r40 bank-regression gap in the actual orthonormal Witt frame necessarily forces shared-shear residual energy; in particular the r40 subcase in which both the completed transverse direction and the shared-shear direction are exactly bank-collinear with `v` is a correct abstract theorem but is empty in the live nonzero-gap orthonormal survivor. I do **not** use that empty subcase below.

I also use the completed exact-physical-cross theorem: for a partition of the ORIGINAL independent coordinates whose physical crossing block has exact rank three and nonzero singular values with product `Delta`,

`||p_Q||_infinity <= 6 Delta^(-1/3)`,

and the density is continuous. Same-bank quadratic and affine terms are arbitrary. This is a product-preserving theorem: it never treats rotated eigen-coordinates as independent.

The live corrections remain binding. Nothing below uses the false arbitrary-joint rank-three coarea lemma, the false positive conditional-density moment, pointwise law-uniform van der Corput decay, an unrestricted fiber supremum, bounded support, moments, log-concavity, or deletion of a small nonzero random tail.

## 2. Live Witt packet and a hidden orthonormal three-frame

The surviving exact-rank-three Witt packet is

\[
Q=2aV(H+\kappa U)+\alpha V^2+2\gamma VW+\delta W^2,                 \tag{2.1}
\]

where `H` is a literal original coordinate, independent of the residual original-coordinate product bank, and

\[
U=u\cdot X,\qquad V=v\cdot X,\qquad W=w\cdot X                     \tag{2.2}
\]

with `u,v,w` orthonormal coefficient vectors on that residual bank. The determinant-star currency is

\[
S_i=a^2|\delta|.                                                       \tag{2.3}
\]

In the target-normalized survivor, `S_i>=1/2`.

Put

\[
c_\kappa=1+\kappa^2,
\qquad
t=\frac{e_H+\kappa u}{\sqrt{c_\kappa}},                             \tag{2.4}
\]

where `e_H` is the literal hub coordinate vector, extended by zero on the residual bank. Then

\[
\boxed{t,v,w\ \text{are an orthonormal three-frame in the FULL original coordinate space}.} \tag{2.5}
\]

Writing

\[
T=t\cdot X_{\rm full}=\frac{H+\kappa U}{\sqrt{c_\kappa}},           \tag{2.6}
\]

(2.1) is exactly the rank-three latent form

\[
Q=(T,V,W)
\begin{pmatrix}
0&a\sqrt{c_\kappa}&0\\
a\sqrt{c_\kappa}&\alpha&\gamma\\
0&\gamma&\delta
\end{pmatrix}
\begin{pmatrix}T\\V\\W\end{pmatrix}.                              \tag{2.7}
\]

Let this latent matrix be `M`. Its determinant is

\[
\boxed{\det M=-a^2c_\kappa\delta,\qquad |\det M|=c_\kappa S_i.}     \tag{2.8}
\]

The important point is that (2.5) is a deterministic coefficient identity, not a probabilistic independence assertion about `(T,V,W)`.

## 3. Exact crossing-volume theorem

Fix any partition `J sqcup K` of the residual ORIGINAL coordinates. Define the two- and three-frame Gram determinants

\[
E_J:=\det\operatorname{Gram}(v_J,w_J),\qquad
E_K:=\det\operatorname{Gram}(v_K,w_K),                              \tag{3.1}
\]

\[
D_J:=\det\operatorname{Gram}(u_J,v_J,w_J),\qquad
D_K:=\det\operatorname{Gram}(u_K,v_K,w_K).                          \tag{3.2}
\]

All four quantities are nonnegative.

### Theorem 3.1 — `QFORM-WITT-EXACT-CROSSVOLUME-v1`

For the original-coordinate cut

\[
S=\{H\}\cup J,\qquad T=K,                                           \tag{3.3}
\]

the physical crossing block `B=A_{S,T}` has rank three iff

\[
\kappa\ne0,\qquad D_K>0,\qquad E_J+\kappa^2D_J>0.                  \tag{3.4}
\]

When this holds, the product of its three nonzero singular values is exactly

\[
\boxed{
\Delta_{H\cup J,K}
=S_i|\kappa|\sqrt{D_K\bigl(E_J+\kappa^2D_J\bigr)}.
}                                                                    \tag{3.5}
\]

For the opposite cut `S=J`, `T={H}\cup K`, one has symmetrically

\[
\boxed{
\Delta_{J,H\cup K}
=S_i|\kappa|\sqrt{D_J\bigl(E_K+\kappa^2D_K\bigr)}.
}                                                                    \tag{3.6}
\]

Consequently, whenever either right-hand side is positive, the law of `Q` has a bounded **continuous** density and

\[
\boxed{
\|p_Q\|_\infty
\le
6\,\Delta^{-1/3}
}                                                                    \tag{3.7}
\]

for the corresponding crossing volume `Delta`.

#### Proof

Let `R=[t\ v\ w]` be the full `n x 3` orthonormal frame from (2.5). For an original-coordinate cut `S sqcup T`, write `R_S,R_T` for its row restrictions and

\[
G_S=R_S^TR_S,\qquad G_T=R_T^TR_T.                                  \tag{3.8}
\]

The physical cross block factors exactly as

\[
B=R_SMR_T^T.                                                         \tag{3.9}
\]

If both restricted frames have column rank three, thin QR factorizations give

\[
\prod_{j=1}^3 s_j(B)
=|\det M|\sqrt{\det G_S\det G_T}.                                  \tag{3.10}
\]

For `T=K`, the restrictions of the three frame columns are

\[
t_K=\frac{\kappa}{\sqrt{c_\kappa}}u_K,\qquad v_K,\qquad w_K.
\]
Therefore

\[
\boxed{\det G_K=\frac{\kappa^2}{c_\kappa}D_K.}                     \tag{3.11}
\]

On `S={H}\cup J`, the first column has the additional literal hub component `1/sqrt(c_kappa)`. Hence

\[
G_{H\cup J}
=
\operatorname{Gram}\left(\frac{\kappa}{\sqrt{c_\kappa}}u_J,v_J,w_J\right)
+\operatorname{diag}(c_\kappa^{-1},0,0).
\]
Expanding the determinant in that single added diagonal entry gives the exact identity

\[
\boxed{
\det G_{H\cup J}
=\frac{E_J+\kappa^2D_J}{c_\kappa}.
}                                                                    \tag{3.12}
\]

Insert (2.8), (3.11), and (3.12) into (3.10): the factors `c_kappa` cancel and yield (3.5). The symmetric formula (3.6) follows by interchanging `J,K`. Since `M` is invertible, positivity of the two restricted Gram determinants is equivalent to exact crossing rank three. Finally apply the completed determinant-sensitive exact-cross theorem with `k=3`, whose geometric-mean singular scale is `Delta^(1/3)`. This gives (3.7) and continuity by `L^1` Fourier inversion. QED.

## 4. What the r40 currencies become

Use the r40 notation

\[
s=\|v_J\|^2,\qquad
w_J=\alpha_Jv_J+r_J,\qquad
w_K=\alpha_Kv_K+r_K,                                                \tag{4.1}
\]

with `r_J perp v_J`, `r_K perp v_K`, and

\[
d_J=\|r_J\|^2,\qquad d_K=\|r_K\|^2.                              \tag{4.2}
\]

Then exactly

\[
\boxed{E_J=s d_J,\qquad E_K=(1-s)d_K.}                              \tag{4.3}
\]

Thus an r40 within-bank Pluecker currency is not yet the whole rank-three crossing currency. The additional factor is a **three-frame bank volume** `D_K` or `D_J`.

Regress the shared-shear vector on `v` as well:

\[
u_J=\beta_Jv_J+p_J,\qquad u_K=\beta_Kv_K+p_K,                    \tag{4.4}
\]

with `p_J perp v_J`, `p_K perp v_K`. Subtracting multiples of the `v` column does not change a Gram determinant, so

\[
\boxed{
D_J=s\bigl(\|p_J\|^2\|r_J\|^2-\langle p_J,r_J\rangle^2\bigr),
}                                                                    \tag{4.5}
\]

\[
\boxed{
D_K=(1-s)\bigl(\|p_K\|^2\|r_K\|^2-\langle p_K,r_K\rangle^2\bigr).
}                                                                    \tag{4.6}
\]

This identifies the precise factor missing from the fresh fleet02/B05 forced-residual theorem. That theorem supplies residual **length** in the bank-gap branch, e.g.

\[
\|p_J\|^2+\|p_K\|^2\ge G,
\]

but an exact rank-three physical crossing requires residual **area**: the sine-angle factor between `p_B` and `r_B` in (4.5)-(4.6). A large residual norm alone cannot supply `D_B`.

This is not a technicality. In the four-coordinate Walsh frame

\[
v=\tfrac12(1,1,1,1),\quad
w=\tfrac12(1,1,-1,-1),\quad
u=\tfrac12(1,-1,1,-1),                                               \tag{4.7}
\]

with `J={1,2}`, `K={3,4}`, one has

\[
s=1/2,\quad d_J=d_K=0,\quad
s(1-s)(\alpha_J-\alpha_K)^2=1,
\]

and the forced `u` residual has full norm, but

\[
\boxed{D_J=D_K=0.}                                                    \tag{4.8}
\]

Hence both exact-cross volumes (3.5)-(3.6) vanish. This is a valid coefficient-frame obstruction to replacing the fleet02 residual-length currency by a crossing-volume lower bound.

## 5. A quantitative chamber closed now

Suppose the r40 max-cut has

\[
\frac14\le s\le\frac34                                              \tag{5.1}
\]

and one of its transverse currencies is at least `1/6`. For example, if

\[
(1-s)d_J\ge\frac16,                                                  \tag{5.2}
\]

then by (4.3)

\[
E_J=s d_J\ge\frac1{18}.                                              \tag{5.3}
\]

If in addition

\[
|\kappa|\ge\frac18,\qquad D_K\ge\frac1{64},\qquad S_i\ge\frac12,   \tag{5.4}
\]

then (3.5) gives

\[
\Delta_{H\cup J,K}
\ge \frac12\cdot\frac18\sqrt{\frac1{64}\frac1{18}}
=\frac1{384\sqrt2}.                                                  \tag{5.5}
\]

Therefore

\[
\boxed{
\|p_Q\|_\infty
\le6(384\sqrt2)^{1/3}<48.952,
\qquad p_Q\in C^0(\mathbb R).
}                                                                    \tag{5.6}
\]

The symmetric statement holds when `s d_K>=1/6` and `D_J>=1/64`.

This is a genuine dimension-free branch of the hard shared-source Witt packet. It uses an ORIGINAL-coordinate cut and exact physical crossing; it does not condition on a projected residual or infer independence after rotation.

## 6. Designated partner fleet04/B05 applied to an actual target inequality

The completed partner theorem `QFORM-PHYSICAL-DEFINITE-PAIR-COAREA-v1`, canonical mathematics

`yspennstate/math-open-problems@33cabb3bd5e466a58adc6eac49eba210ef62ef14`,

proves for any literal original-coordinate definite principal pair `C` under cap-one laws, with arbitrary outside coupling retained,

\[
\|p_Q\|_{\infty,\mathrm{ess}}\le\frac{\pi}{\sqrt{|\det C|}}.       \tag{6.1}
\]

Apply it to the explicit target-valid Walsh control (4.7) with

\[
a=\delta=1,\quad \alpha=\gamma=0,\quad \kappa=\frac14.            \tag{6.2}
\]

The latent spectrum is

\[
\{+\sqrt{1+\kappa^2},-\sqrt{1+\kappa^2},1\},                       \tag{6.3}
\]

so all three nonzero eigenvalues have absolute value at least one. For the literal residual physical pair `{1,3}`, direct substitution gives

\[
C_{13}=\begin{pmatrix}3/8&-1/8\\-1/8&3/8\end{pmatrix},
\qquad \det C_{13}=\frac18>0.                                      \tag{6.4}
\]

Hence the designated partner theorem gives the actual target inequality

\[
\boxed{
\|p_Q\|_{\infty,\mathrm{ess}}
\le\pi\sqrt8=2\sqrt2\,\pi<8.886.
}                                                                    \tag{6.5}
\]

This control is useful for interpretation: the four-coordinate Walsh bank-gap example kills the rank-three cross-volume receiver for the displayed cut, but it is still paid by a different honest original-coordinate coarea mechanism. It is not a counterexample to QFORM.

## 7. Exact remaining factor

The new theorem removes every live Witt branch in which a balanced r40 transverse bank has quantitative two-volume and the opposite bank has quantitative three-frame volume, with `|kappa|` bounded below. The first unpaid implication is now sharper:

`QFORM-WITT-RANKTWO-BANK-AGGREGATE-COAREA-v1`:

> control the product-law interval probability when the r40/fleet02 max-cut has constant transverse or forced shared-shear residual currency but both bank three-frame determinants are small or zero; equivalently, the bank restrictions are quantitatively close to rank two and the curvature lives in a **change of two-dimensional bank planes** rather than a rank-three physical crossing.

Equations (4.5)-(4.6) show the precise missing factor: the angle between the shared-shear residual and transverse residual inside a bank. The fleet02 theorem controls their lengths, not that angle. The exact Walsh frame (4.7) shows that no positive lower bound on this angle follows from the current currencies alone.

The small-`|kappa|` puncture is also real for the exact-cross mechanism: (3.5)-(3.6) necessarily contain `|kappa|`, because at `kappa=0` the hub direction is supported only on the `H` side and every such crossing drops to rank at most two. The existing pairwise quadratic-coarea theorem is uniform in `kappa`, so the next aggregate receiver should combine its `kappa`-uniform curvature with the rank-two-bank plane-change geometry rather than try to remove the `|kappa|` factor from an exact-rank-three crossing identity where it is algebraically necessary.

## 8. Literature check

A fresh search found no published theorem matching the owner quantifiers. The returned quadratic-form concentration papers impose Gaussian, sub-Gaussian, Bernstein-moment, smooth-transform, or other distributional assumptions. They therefore do not terminate this product-density problem and were not used as premises.

## 9. Scope statement

This report does not prove or disprove the full conjecture. It proves an exact original-coordinate crossing-volume formula and a dimension-free continuous-density branch, applies the designated partner theorem to a concrete target-valid inequality, and isolates a strictly sharper remaining geometric factor. Full-target continuity remains open.