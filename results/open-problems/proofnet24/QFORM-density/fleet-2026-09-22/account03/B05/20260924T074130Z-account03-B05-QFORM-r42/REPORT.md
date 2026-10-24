SIGNED IN - working on the quadratic-form bounded-density conjecture (universal constant), account account03, slot B05, 2026-09-24T07:41:30Z.
attacking: QFORM-WITT-RANKTWO-BANK-AGGREGATE-COAREA-v1 — prove a product-preserving interval/coarea bound when rank-three crossing collapses but aggregate two-plane change remains.

# account03/B05 r42 — exact rank-two-bank null-hub compiler

**Programme:** `QFORM-DENSITY-3EIG-20260922`  
**Assignment:** quadratic coarea / interval bounds preserving arbitrary original-coordinate product laws.  
**Status:** `PROVED SUPPORTING THEOREM + EXACT SURVIVOR IDENTIFIED / FULL QFORM OPEN`.  
**Regularity:** essential boundedness only in the new paid branches; continuity is not claimed.  
**Execution:** `WITHOUT_VERIFIED_BRAIN`.

Fresh owner control before this write was `yspennstate/math-research-brain@9facf7b09210cc7fe92f44934f1acece9df87e76`; OWNER CONTROL remains revision `2026-09-22.15`, QFORM-only, with no later stop or reassignment for this slot.

## 1. Inputs actually used

The immediate predecessor is account03/B05 r41,

`yspennstate/math-open-problems@fe9f82e0c3206c1056b60963a75989baff4aa0ef:`
`proofnet24/QFORM-density/fleet-2026-09-22/account03/B05/20260924T060943Z-account03-B05-QFORM-r41/REPORT.md`.

Its live Witt packet is

\[
Q=2aV(H+\kappa U)+\alpha V^2+2\gamma VW+\delta W^2,                 \tag{1.1}
\]

where `H` is one literal original coordinate, independent of the residual original-coordinate product bank, and

\[
U=u\cdot X,\qquad V=v\cdot X,\qquad W=w\cdot X                     \tag{1.2}
\]

with `u,v,w` orthonormal coefficient vectors on that residual bank. The determinant-star currency is

\[
\boxed{S_i=a^2|\delta|}.                                               \tag{1.3}
\]

In the target-normalized heavy-null survivor, `S_i>=1/2`.

For a residual original-coordinate cut `J\sqcup K`, r41 defines

\[
D_J=\det\operatorname{Gram}(u_J,v_J,w_J),\qquad
D_K=\det\operatorname{Gram}(u_K,v_K,w_K).                            \tag{1.4}
\]

Its exact rank-three crossing receiver pays every branch with a quantitative positive `D_J` or `D_K`, but it leaves the exact rank-two-bank endpoint `D_J=D_K=0`, as well as near-zero versions that cannot be treated perturbatively under arbitrary unbounded input laws.

The analytic receiver used below is account02/B05's completed rough Borel theorem `QFORM-NULL-HUB-TRANSVERSE-SQUARE-v1`, canonical source

`yspennstate/math-open-problems@e7a21ed67b943d7aded714ac17ca48bdab4a1349:`
`proofnet24/QFORM-density/fleet-2026-09-22/account02/B05/20260923T200516Z-account02-B05-QFORM-auto11c/REPORT.md`.

It states: if `H_0` is independent of a pair `(L,Z)`, `||f_{H_0}||_\infty<=m`, the pair has joint-density cap `M`, and

\[
R=2H_0L+A L^2+2B LZ+c_2Z^2+dL+eZ+f,\qquad c_2\ne0,                 \tag{1.5}
\]

then

\[
\boxed{
\|p_R\|_{\infty,\mathrm{ess}}
\le C_{NH}(Mm)^{2/3}|c_2|^{-1/3},
\qquad C_{NH}=7.761982175235\ldots .
}                                                                    \tag{1.6}
\]

It is an interval/Borel argument for rough laws; it does not use the refuted arbitrary-joint rank-three coarea lemma. I also use the standard two-dimensional product-projection density estimate already used in the source-pinned B05 chain: an orthonormal two-column projection of independent cap-one coordinates has joint density cap at most `2`.

The designated partner result used in Section 6 is account04/B05's `QFORM-PHYSICAL-DEFINITE-PAIR-COAREA-v1`,

`yspennstate/math-open-problems@33cabb3bd5e466a58adc6eac49eba210ef62ef14`,

which for a literal original-coordinate definite principal pair `C` gives

\[
\boxed{
\Pr\{Q\in I\}\le \frac{\pi}{\sqrt{|\det C|}}|I|,
\qquad
\|p_Q\|_{\infty,\mathrm{ess}}\le\frac{\pi}{\sqrt{|\det C|}}.
}                                                                    \tag{1.7}
\]

Arbitrary outside curvature and affine terms are retained.

## 2. Exact geometry when both bank three-volumes vanish

Let

\[
R=[u\ v\ w]\in\mathbb R^{N\times3},\qquad R^TR=I_3,                \tag{2.1}
\]

and put

\[
G_J=R_J^TR_J,\qquad G_K=R_K^TR_K=I_3-G_J.                           \tag{2.2}
\]

Assume the exact endpoint

\[
\boxed{\det G_J=\det G_K=0.}                                         \tag{2.3}
\]

Since `0<=G_J<=I`, its eigenvalues lie in `[0,1]`. Equation (2.3) says one eigenvalue is zero and one eigenvalue is one. Hence for some `\tau\in[0,1]` there is an orthogonal `O\in O(3)` such that

\[
\boxed{
O^TG_JO=\operatorname{diag}(1,\tau,0),\qquad
O^TG_KO=\operatorname{diag}(0,1-\tau,1).
}                                                                    \tag{2.4}
\]

Let the rotated deterministic coefficient frame be

\[
[r_1\ r_2\ r_3]=RO.                                                   \tag{2.5}
\]

This is only a coefficient-space identity; no rotated random coordinates are declared independent. Equation (2.4) implies exactly

\[
r_{1,K}=0,\qquad r_{3,J}=0,                                         \tag{2.6}
\]

and, whenever the indicated denominator is nonzero,

\[
\left(r_{1,J},\frac{r_{2,J}}{\sqrt\tau}\right)
\quad\text{and}\quad
\left(\frac{r_{2,K}}{\sqrt{1-\tau}},r_{3,K}\right)                 \tag{2.7}
\]

are orthonormal two-frames on the ORIGINAL banks `J` and `K`, respectively.

Thus the apparently degenerate three-frame cut has an exact **one / split-one / one** product decomposition: latent direction `r_1` is supported on `J`, latent direction `r_3` is supported on `K`, and only `r_2` is shared between the banks.

## 3. The hidden null-hub curvatures

Write the residual latent quadratic matrix in the original `(u,v,w)` basis as

\[
N=
\begin{pmatrix}
0&a\kappa&0\\
a\kappa&\alpha&\gamma\\0&\gamma&\delta
\end{pmatrix}.                                                       \tag{3.1}
\]

After the same coefficient rotation `O`, set

\[
C=O^TNO,\qquad h=O^Te_v,\qquad z=O^Te_w.                            \tag{3.2}
\]

Here `h,z` are orthonormal. The hub term is `2aH h^T Y`, where `Y=(r_1\cdot X,r_2\cdot X,r_3\cdot X)`, and `z` is the transformed coefficient direction of the literal square `\delta W^2`.

A crucial exact cancellation holds on the plane perpendicular to `h`. In the original basis, any `x\perp e_v` has the form `x=x_1e_u+x_3e_w`, hence

\[
x^TNx=\delta x_3^2.                                                  \tag{3.3}
\]

After conjugation this becomes

\[
\boxed{x^TCx=\delta(z\cdot x)^2\quad\text{for every }x\perp h.}     \tag{3.4}
\]

Define the Pluecker numbers

\[
p_{12}=h_1z_2-h_2z_1,\qquad
p_{13}=h_1z_3-h_3z_1,\qquad
p_{23}=h_2z_3-h_3z_2.                                                \tag{3.5}
\]

Since `h,z` are orthonormal,

\[
\boxed{p_{12}^2+p_{13}^2+p_{23}^2=1.}                               \tag{3.6}
\]

The two bank receivers see the exact curvatures

\[
\boxed{\chi_J=S_i\,\tau\,p_{12}^2,\qquad
       \chi_K=S_i(1-\tau)p_{23}^2.}                                  \tag{3.7}
\]

This is independent of `\kappa`, including at `\kappa=0`.

To prove (3.7), consider the `J` bank. Normalize its two active product projections as

\[
X_J^{(2)}=\left(r_1\cdot X_J,\frac{r_2\cdot X_J}{\sqrt\tau}\right). \tag{3.8}
\]

They have joint-density cap at most `2`. After conditioning on all original coordinates in `K`, the quadratic in `H` and the pair (3.8) has hub-coupling vector

\[
b_J=a(h_1,\sqrt\tau h_2)                                           \tag{3.9}
\]

and pair Hessian

\[
A_J=
\begin{pmatrix}
C_{11}&\sqrt\tau C_{12}\\
\sqrt\tau C_{12}&\tau C_{22}
\end{pmatrix}.                                                       \tag{3.10}
\]

The conditioned `K` variables contribute only affine terms in `(H,X_J^{(2)})`; the affine term in `H` is absorbed by translating the pair coordinate along `b_J`. Rotate the pair orthogonally so the first coordinate is parallel to `b_J`. In the notation of (1.5), scale the hub to `H_0=|b_J|H`, so its density cap is `|b_J|^{-1}`. The transverse-square coefficient `c_{2,J}` then obeys

\[
|b_J|^2c_{2,J}
=b_{J,1}^2(A_J)_{22}-2b_{J,1}b_{J,2}(A_J)_{12}
+b_{J,2}^2(A_J)_{11}.                                                \tag{3.11}
\]

Substitution gives

\[
|b_J|^2c_{2,J}
=a^2\tau\bigl(h_1^2C_{22}-2h_1h_2C_{12}+h_2^2C_{11}\bigr).         \tag{3.12}
\]

The vector `(-h_2,h_1,0)` is perpendicular to `h`, so (3.4) gives

\[
h_1^2C_{22}-2h_1h_2C_{12}+h_2^2C_{11}
=\delta(h_1z_2-h_2z_1)^2=\delta p_{12}^2.                            \tag{3.13}
\]

Taking absolute values and using `S_i=a^2|\delta|` proves the first formula in (3.7). The `K` formula follows identically from the vector `(0,-h_3,h_2)`.

The cancellation in (3.13) is the main new geometric point: `\alpha`, `\gamma`, and the shared-shear coefficient `a\kappa` all disappear from the coarea currency.

## 4. Main theorem — exact rank-two-bank aggregate coarea

Define

\[
\Gamma:=\tau p_{12}^2+(1-\tau)p_{23}^2.                              \tag{4.1}
\]

### Theorem `QFORM-WITT-RANKTWO-BANK-NULLHUB-v1`

Under (1.1), the original-coordinate product assumptions, and the exact bank endpoint `D_J=D_K=0`, if `\Gamma>0`, then `Q` has an essentially bounded density and

\[
\boxed{
\|p_Q\|_{\infty,\mathrm{ess}}
\le 2C_{NH}(S_i\Gamma)^{-1/3}
<15.524\,(S_i\Gamma)^{-1/3}.
}                                                                    \tag{4.2}
\]

The estimate is uniform in `\kappa`, including `\kappa=0`, and uniform in all conditioned affine translations and arbitrary rough/fragmented cap-one input laws.

#### Proof

If `\chi_J>0`, Section 3 and (1.6), with pair cap `M<=2` and scaled-hub cap `m<=|b_J|^{-1}`, give

\[
\|p_Q\|_{\infty,\mathrm{ess}}
\le C_{NH}2^{2/3}\chi_J^{-1/3}.                                    \tag{4.3}
\]

This conditional bound is uniform in every fixed value of the opposite original-coordinate bank `K`, so averaging the interval inequality over `K` is legitimate. The same argument yields

\[
\|p_Q\|_{\infty,\mathrm{ess}}
\le C_{NH}2^{2/3}\chi_K^{-1/3}                                    \tag{4.4}
\]

when `\chi_K>0`.

Since

\[
\max\{\chi_J,\chi_K\}\ge \frac{S_i}{2}\Gamma,                     \tag{4.5}
\]

choose the better bank. Combining (4.3)-(4.5) gives (4.2). QED.

If `S_i>=1/2` and `\Gamma>=1/16`, then

\[
\boxed{\|p_Q\|_{\infty,\mathrm{ess}}<49.286.}                       \tag{4.6}
\]

This branch was unavailable from r41's exact rank-three crossing theorem: its crossing volumes contain `|\kappa|D_J^{1/2}` or `|\kappa|D_K^{1/2}` and therefore vanish identically at the present endpoint. Equation (4.2) is a genuinely different coarea mechanism.

## 5. Exact survivor and the missing factor

The remaining exact rank-two-bank obstruction is

\[
\boxed{\Gamma=0.}                                                     \tag{5.1}
\]

If `0<\tau<1`, this forces `p_{12}=p_{23}=0`, hence by (3.6)

\[
\boxed{p_{13}^2=1.}                                                   \tag{5.2}
\]

Thus `h` (the hub-coupling direction) and `z` (the retained square direction) lie entirely in the two pure bank axes `e_1,e_3`, while the shared middle latent direction `e_2` is perpendicular to both. In the original Witt basis this means the shared middle direction is exactly the longitudinal `u` direction, up to sign. The same source-sharing term that defeated a perturbative treatment is therefore isolated with no ambiguity.

At the boundary `\tau=0`, the exact unpaid condition is `p_{23}=0`; at `\tau=1` it is `p_{12}=0`. These boundary cases likewise have one bank of latent rank one and the other of rank two. A small nonzero `\tau`, `D_J`, or `D_K` cannot be deleted as a small random perturbation because the input laws have no moment or support bounds.

The next B05 implication is therefore `QFORM-WITT-PURE13-SHARED-MIDDLE-COAREA-v1`: in the product-bank normal form (2.4), pay the case in which the hub direction and square direction carry all their Pluecker area in the pure bank plane `(e_1,e_3)`, while the longitudinal direction is precisely the split middle coordinate. The proof must aggregate the two bank-pair laws before a reciprocal local minor or a conditional projected-density supremum.

## 6. Designated partner account04/B05 applied at the new survivor

The four-coordinate Walsh frame is an exact `\Gamma=0` control. Let

\[
v=\tfrac12(1,1,1,1),\quad
w=\tfrac12(1,1,-1,-1),\quad
u=\tfrac12(1,-1,1,-1),                                               \tag{6.1}
\]

and split `J={1,2}`, `K={3,4}`. Then

\[
G_J=
\begin{pmatrix}
1/2&0&0\\0&1/2&1/2\\0&1/2&1/2
\end{pmatrix}                                                        \tag{6.2}
\]

in the `(u,v,w)` basis, with eigenvalues `{1,1/2,0}`. Thus `\tau=1/2`. Take

\[
e_1=(v+w)/\sqrt2,\qquad e_2=u,\qquad e_3=(-v+w)/\sqrt2.             \tag{6.3}
\]

Then

\[
h=O^Te_v=(1/\sqrt2,0,-1/\sqrt2),\qquad
z=O^Te_w=(1/\sqrt2,0,1/\sqrt2),                                     \tag{6.4}
\]

so

\[
\boxed{p_{12}=p_{23}=0,\quad p_{13}=1,\quad \Gamma=0.}              \tag{6.5}
\]

Now take the target-valid family

\[
Q_\kappa=2V(H+\kappa U)+W^2.                                        \tag{6.6}
\]

Its nonzero spectrum is

\[
\boxed{\{1,+\sqrt{1+\kappa^2},-\sqrt{1+\kappa^2}\},}               \tag{6.7}
\]

so it lies in the exact owner target for every `\kappa`.

For `\kappa>0`, the literal original-coordinate pair `{1,3}` in the residual bank has principal block

\[
C_{13}=
\begin{pmatrix}
1/4+\kappa/2&-1/4+\kappa/2\\
-1/4+\kappa/2&1/4+\kappa/2
\end{pmatrix},\qquad
\det C_{13}=\kappa/2>0.                                              \tag{6.8}
\]

It is positive definite. The completed designated partner theorem (1.7) therefore gives

\[
\boxed{
\|p_{Q_\kappa}\|_{\infty,\mathrm{ess}}
\le \pi\sqrt{\frac{2}{\kappa}},\qquad \kappa>0.
}                                                                    \tag{6.9}
\]

For `\kappa<0`, the literal pair `{2,4}` is positive definite with determinant `|\kappa|/2`, giving

\[
\boxed{
\|p_{Q_\kappa}\|_{\infty,\mathrm{ess}}
\le \pi\sqrt{\frac{2}{|\kappa|}},\qquad \kappa<0.
}                                                                    \tag{6.10}
\]

At `|\kappa|>=1/4`, this is

\[
\boxed{\|p_{Q_\kappa}\|_{\infty,\mathrm{ess}}\le2\sqrt2\pi<8.886.} \tag{6.11}
\]

At `\kappa=0`, the partner pair degenerates, while the independent-hub null-square theorem applies directly to `2HV+W^2` and remains bounded. Thus this exact `\Gamma=0` control displays the real punctured issue: the physical-pair estimate deteriorates as `|\kappa|\downarrow0`, even though the endpoint itself is bounded. The new theorem (4.2) removes this puncture whenever `\Gamma>0`; only the pure-`13` source-sharing orientation still needs a uniform interpolation.

## 7. Corrections and scope

Nothing above uses law-uniform pointwise quadratic-phase decay, independence after rotating the random coordinates, the refuted arbitrary-joint three-dimensional coarea inequality, a curved-fiber supremum, a positive conditional-density moment, bounded support, moments, log-concavity, connected support, or deletion of a small nonzero coefficient as a small random perturbation.

The latent rotations are deterministic coefficient-space identities. Every probabilistic smoothing step is taken on an actual original-coordinate bank, with the two-dimensional projection cap replacing false post-rotation independence.

The theorem proves only a scoped **essential** density bound. It does not prove continuity for the paid branch, and it does not solve the unrestricted QFORM conjecture.

## 8. Delivery status and next step

**New theorem:** `QFORM-WITT-RANKTWO-BANK-NULLHUB-v1`, equation (4.2).  
**Exact new geometric currency:** `\Gamma=\tau p_{12}^2+(1-\tau)p_{23}^2`.  
**Exact survivor:** pure `p_{13}` source-sharing, equation (5.2), plus the rank-one-bank boundary analogues.  
**Next step:** attack `QFORM-WITT-PURE13-SHARED-MIDDLE-COAREA-v1` directly, preferably by keeping the two independent bank-pair densities until after the split-middle variable is integrated; do not condition on that projected middle variable.

Full QFORM status remains **OPEN / NOT PROVED / NOT DISPROVED**. Full-target continuity remains **OPEN**.
