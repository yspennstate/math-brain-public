SIGNED IN - working on the quadratic-form bounded-density conjecture (universal constant), account account01, slot B05, 2026-09-24T07:29:00Z.
attacking: QFORM-WITT-RANKTWO-TAIL-GLUE-v1; first test whether the apparent sigma_T interpolation is actually needed after reconciling the strongest existing null-hub and pair-star coarea theorems.

# account01/B05 auto11 — the sigma_T glue is unnecessary: complete closure of the exact-rank-three high-leverage null-pivot Witt survivor

**Programme:** `QFORM-DENSITY-3EIG-20260922`.  
**Assignment:** quadratic coarea / equivalent interval bounds preserving arbitrary original-coordinate product densities.  
**Control:** refreshed immediately before publication from `math-research-brain` head `8d31791cf57790e327f27bd814c4c26cd9fd375f`; OWNER CONTROL revision `2026-09-22.15`, QFORM-only.  
**Status:** `NEW SYNTHESIS CLOSURE OF THE B05 HIGH-LEVERAGE NULL-PIVOT EXACT-RANK3 SURVIVOR / FULL QFORM OPEN`.  
**Regularity:** essential boundedness is uniform on the whole branch; continuity is proved on the transverse-diffuse half, but is not established by the pair-star theorem on the complementary half. Full-target continuity remains OPEN.  
**Execution:** `WITHOUT_VERIFIED_BRAIN`.

The live corrections are retained: no independence after spectral rotation, no arbitrary-joint rank-three coarea theorem, no conditional projection-density cap, no fiber supremum, no pointwise law-uniform quadratic-phase decay, and no moment/support/log-concavity assumption.

## 1. The apparent remaining glue from the previous B05 run

The immediate predecessor `math-open-problems@763231817b4bb8114d827c8f428170f3b8e8b701` reduced the B05 heavy-null exact-rank-three survivor to the Witt form

\[
Q=2aV(H+\kappa U)+\alpha V^2+2\gamma VW+\delta W^2,                 \tag{1.1}
\]

where `H` is one literal original coordinate, independent of the residual original-coordinate product bank, while

\[
U=u\cdot X,\qquad V=v\cdot X,\qquad W=w\cdot X                      \tag{1.2}
\]

are three orthonormal projections of that residual product bank. The determinant-star currency is

\[
S_i=a^2|\delta|=cD,                                                  \tag{1.3}
\]

where `c` is the spectral leverage of the physical null hub and `D` is the product of the three nonzero eigenvalue magnitudes. In the target-normalized high-leverage branch,

\[
c\ge\frac12,\qquad D\ge1,\qquad S_i=cD\ge\frac12.                  \tag{1.4}
\]

The predecessor then removed at most three longitudinal spikes and isolated a tail departure parameter `sigma_T`. It paid the exact `sigma_T=0` endpoint but left a punctured interpolation problem for `sigma_T>0`.

The first calculation in this run shows that this interpolation is unnecessary: an earlier, stronger source-valid null-hub theorem already ignores the entire longitudinal component of every residual row. The complementary failure of its gate is exactly paid by the existing pair-anchored determinant-star theorem.

## 2. Exact mapping to the existing null-hub theorem

Use the physical Witt basis from the B05 compiler. The exact-rank-three spectral matrix can be written

\[
M=\begin{pmatrix}
0&\beta&0\\
\beta&\alpha&\gamma\\
0&\gamma&\delta
\end{pmatrix},
\qquad
\det M=-\beta^2\delta,                                               \tag{2.1}
\]

and the hub spectral row is

\[
r_i=\sqrt c\,e_1.                                                    \tag{2.2}
\]

For every complementary original coordinate write its spectral row as

\[
r_j=(x_j,y_j,z_j).                                                    \tag{2.3}
\]

Because the spectral frame has orthonormal columns and the hub row has only an `e_1` component,

\[
\sum_{j\ne i}\binom{y_j}{z_j}(y_j,z_j)=I_2.                         \tag{2.4}
\]

Define the transverse physical leverage

\[
q_j:=y_j^2+z_j^2.                                                     \tag{2.5}
\]

Now apply the source-valid theorem `QFORM-NULL-HUB-TRANSVERSE-LEVERAGE-CLOSURE-v1` from

`math-open-problems@c0d7e627b3b877fcecc3004a58335658f6541d64`,
`proofnet24/QFORM-density/fleet-2026-09-22/account03/B10/20260923T114517Z-account03-B10-QFORM-r24/REPORT.md`.

In its notation choose `r=e_1`. Since

\[
Me_1=\beta e_2,                                                       \tag{2.6}
\]

its transverse orthonormal basis is exactly `(e_2,e_3)`. Therefore its gate

\[
\|P_{r^\perp}r_j\|^2\le\frac12                                      \tag{2.7}
\]

is **exactly**

\[
q_j=y_j^2+z_j^2\le\frac12.                                          \tag{2.8}
\]

No condition at all is imposed on the longitudinal coefficient `x_j`. In particular the former B05 “longitudinal spikes” are harmless whenever (2.8) holds: the mixed-Fresnel shear in the B10 proof absorbs the entire longitudinal part before absolute values are taken.

The B10 theorem gives a continuous `C_0` density and

\[
\boxed{
\|p_Q\|_\infty
\le 3\,2^{4/3}(cD)^{-1/3}
=3\,2^{4/3}S_i^{-1/3}.
}                                                                    \tag{2.9}
\]

At the target normalization (1.4),

\[
\boxed{\|p_Q\|_\infty\le3\,2^{5/3}<9.525.}                         \tag{2.10}
\]

Thus every state with `max_j q_j<=1/2` is completely paid, uniformly through every value of the former tail parameter `sigma_T`, including `sigma_T downarrow0`.

## 3. If the null-hub gate fails, the pair-star theorem pays immediately

Suppose instead that for some complementary physical coordinate `j`,

\[
q_j>\frac12.                                                         \tag{3.1}
\]

For the literal physical pair `I={i,j}`, define the aggregate principal-triple star

\[
T_{ij}:=\sum_{k\notin\{i,j\}}|\det A_{\{i,j,k\}}|.                  \tag{3.2}
\]

The exact identity is

\[
\boxed{T_{ij}=S_i q_j.}                                              \tag{3.3}
\]

For completeness, this can be derived directly, without any selected minor. Cauchy-Binet gives

\[
|\det A_{\{i,j,k\}}|
=D\,\det[r_i;r_j;r_k]^2
=cD\,(y_jz_k-z_jy_k)^2.                                             \tag{3.4}
\]

Summing over `k`, using (2.4), gives

\[
\sum_k(y_jz_k-z_jy_k)^2
=y_j^2+z_j^2=q_j,                                                     \tag{3.5}
\]

which proves (3.3).

Hence (1.4) and (3.1) imply

\[
T_{ij}>\frac14.                                                       \tag{3.6}
\]

Now apply `QFORM-PAIR-ANCHORED-DETSTAR-COAREA-v1` from

`proofnet24/QFORM-density/fleet-2026-09-22/account03/B05/20260924T033744Z-account03-B05-QFORM-r39/REPORT.md`.

That theorem applies to every exact-rank-three form and every literal physical pair with positive aggregate star, including a singular or isotropic physical pair, and gives

\[
\|p_Q\|_{\infty,\mathrm{ess}}
\le C_\star T_{ij}^{-1/3},
\qquad
C_\star=24(3+\sqrt2)10^{2/3}=491.735145127\ldots .                  \tag{3.7}
\]

Therefore

\[
\boxed{
\|p_Q\|_{\infty,\mathrm{ess}}
<4^{1/3}C_\star
<780.581.
}                                                                    \tag{3.8}
\]

The r39 theorem proves absolute continuity and essential boundedness in this branch; it does not by itself prove a continuous representative.

## 4. Main synthesis theorem

### Theorem `QFORM-HIGHLEVERAGE-NULLPIVOT-WITT-CLOSURE-v1`

Let `A` have exact rank three, with its three nonzero eigenvalues satisfying `|lambda_k|>=1`. Suppose an ORIGINAL physical coordinate `i` has

\[
A_{ii}=0,
\qquad
c_i:=\|r_i\|^2\ge\frac12.                                          \tag{4.1}
\]

For arbitrary independent original-coordinate inputs with densities at most one, the law of `X^TAX` is absolutely continuous and

\[
\boxed{\|p_Q\|_{\infty,\mathrm{ess}}<781.}                          \tag{4.2}
\]

More precisely, after the deterministic spectral Witt normalization above, either

1. `q_j<=1/2` for all `j!=i`, in which case `p_Q in C_0(R)` and `||p_Q||_infinity<9.525`; or
2. some `q_j>1/2`, in which case the literal pair `{i,j}` has `T_ij>1/4` and `||p_Q||_(infinity,ess)<780.581`.

#### Proof

The two cases are exhaustive. Case 1 is (2.9)-(2.10); Case 2 is (3.3)-(3.8). Every probabilistic theorem is applied to original-coordinate product inputs at its proved scope. The only spectral rotation is deterministic bookkeeping inside the rank-three coefficient representation. QED.

### Consequence for the previous B05 blocker

The former debt

`QFORM-WITT-RANKTWO-TAIL-GLUE-v1`

is **retired on this exact scope**. The apparent `sigma_T` puncture arose only after discarding the stronger null-hub mixed-Fresnel theorem. There is no need to interpolate a three-frame determinant through zero: the B10 receiver pays all longitudinal geometry whenever the transverse physical leverages are at most `1/2`, and r39 pays the complementary transverse-heavy coordinate directly by its aggregate star.

This is not a proof of arbitrary exact rank three, because the theorem assumes a physical **zero diagonal** with leverage at least `1/2`. It is also not a proof for arbitrary higher-rank matrices with additional spectrum. The full owner conjecture therefore remains OPEN.

## 5. Designated account02/B05 result applied to an actual inequality

The completed account02/B05 source-disjoint Pluecker max-cut theorem from

`math-open-problems@3ca6f8113ff32fc642cc3582b4a338082e8d6d25`

applies directly to the transverse orthonormal two-frame `(y,z)` in (2.4). It gives an ORIGINAL-coordinate partition of the complement

\[
J\sqcup K=\{1,\ldots,n\}\setminus\{i\}
\]

such that

\[
\sum_{j\in J,k\in K}(y_jz_k-z_jy_k)^2\ge\frac12.                   \tag{5.1}
\]

Multiplying by the exact determinant factor `S_i=cD` from (3.4), we obtain the actual target inequality

\[
\boxed{
\sum_{j\in J,k\in K}|\det A_{\{i,j,k\}}|
\ge\frac{S_i}{2}
\ge\frac14.
}                                                                    \tag{5.2}
\]

This partner application is not needed to select a single pair in Theorem 4.1; it independently certifies that a dimension-free amount of principal-triple curvature crosses disjoint original-coordinate banks. It is useful for the successor aggregate-coarea problem and, importantly, it performs aggregation before reciprocal-minor selection.

## 6. Scope audit and next work

**Proved/reconciled in this run:** the complete exact-rank-three high-leverage physical-null-pivot branch (Theorem 4.1), with universal essential density bound `<781`; continuous density `<9.525` on the transverse-diffuse half; exact pair-star identity (3.3); designated account02/B05 max-cut applied to obtain the cross-bank determinant mass (5.2).

**Not proved:** arbitrary exact rank three without a high-leverage zero physical pivot; arbitrary higher-rank matrices; the full three-large-eigenvalue conjecture; a continuous representative on the pair-star half; full-target continuity.

Because the previous `sigma_T` glue is now unnecessary on its exact scope, the next B05 mechanism should move to the neighboring **nonzero/near-zero physical-pivot high-leverage collar** and seek a coarea estimate continuous across the zero-pivot closure just proved, or else aggregate the pair-star currency in the arbitrary higher-rank setting before a Schur reduction. Do not return to the retired tail interpolation.
