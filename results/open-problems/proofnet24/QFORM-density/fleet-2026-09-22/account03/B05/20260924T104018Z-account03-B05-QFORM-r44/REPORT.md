SIGNED IN - working on the quadratic-form bounded-density conjecture (universal constant), account account03, slot B05, 2026-09-24T10:40:18Z.
attacking: QFORM-HIGHLEVERAGE-MIXED-VOLUME-HEAVYSET-COMPILER-v1 — convert the r43 small-regression-residual/slope-gap survivor into a three-way original-coordinate volume compiler: diffuse light determinant, a paid heavy-heavy pair-star, or one literal heavy coordinate carrying a quantified two-light determinant star.

# account03/B05 r44 — mixed-volume heavy-set compiler for the r43 high-leverage survivor

**Programme:** `QFORM-DENSITY-3EIG-20260922`  
**Assignment:** quadratic coarea / equivalent interval bounds preserving arbitrary original-coordinate product densities.  
**Run:** `20260924T104018Z-account03-B05-QFORM-r44`.  
**Status:** **NEW SUPPORTING EXACT-RANK-THREE STRUCTURAL/ANALYTIC COMPILER / FULL QFORM OPEN**.  
**Regularity:** a continuous `C_0` density is proved on the new diffuse-light branch; the pair-star and designated definite-pair branches give essential boundedness. Full-target continuity remains open.  
**Execution:** `WITHOUT_VERIFIED_BRAIN`.

Fresh startup control was read from `yspennstate/math-research-brain@5dc5b6cd2344d32a1f0f516bd6156a91409d484a`; OWNER CONTROL remains revision `2026-09-22.15`, QFORM-only. The live programme state and correction inbox were read before this proof and will be refreshed again before publication. No step below uses law-uniform pointwise quadratic-phase decay, arbitrary-joint rank-three coarea, conditional projection-density caps, post-rotation probabilistic independence, a dimension-growing fiber supremum, moment/support assumptions, or deletion of a small random quadratic term.

The immediate same-slot source is

`yspennstate/math-open-problems@d261ffafcef98c2e5eeecbbef006b1e8cb327b69`

`proofnet24/QFORM-density/fleet-2026-09-22/account03/B05/20260924T101020Z-account03-B05-QFORM-r43/REPORT.md`.

The present run changes mechanism from the r43 slope-gap coordinates to the complete third exterior-volume law of the two original-coordinate banks.

## 1. Incoming r43 hard chamber

Let

\[
A=RMR^T,\qquad R^TR=I_3,
\]

have exact rank three, with `M=M^T` invertible and all three eigenvalues of modulus at least one. Put

\[
D:=|\det M|\ge1.
\]

Fix an ORIGINAL physical coordinate `i` whose spectral leverage is

\[
c:=\|r_i\|^2\ge\frac12.
\]

Rotate only deterministic coefficient bookkeeping so that

\[
r_i=\sqrt c\,e_1.
\]

For `j!=i`, write

\[
r_j=(x_j,t_j),\qquad t_j\in\mathbb R^2,
\]

and put

\[
s:=1-c.
\]

Parseval gives

\[
\sum_{j\ne i}x_j^2=s,\qquad
\sum_{j\ne i}x_jt_j=0,\qquad
\sum_{j\ne i}t_jt_j^T=I_2.
\tag{1.1}
\]

The already-paid cases in r43 allow us, for the present new branch, to impose

\[
\frac12\le c\le\frac34,
\qquad \max_j\|t_j\|^2<\frac14.
\tag{1.2}
\]

Thus

\[
\frac14\le s\le\frac12.
\tag{1.3}
\]

R43 constructs an ORIGINAL-coordinate partition of the complement

\[
J\sqcup K=\{j:j\ne i\}
\]

with transverse Grams

\[
G:=\sum_{j\in J}t_jt_j^T,
\qquad G_K:=I_2-G,
\qquad \det G\det G_K>\frac1{32}.
\tag{1.4}
\]

Write

\[
a=\sum_{j\in J}x_j^2,
\qquad b=\sum_{j\in J}x_jt_j,
\]

and define the two exact longitudinal regression residuals

\[
\rho_J=a-b^TG^{-1}b,
\qquad
\rho_K=(s-a)-b^TG_K^{-1}b.
\tag{1.5}
\]

R43 already pays the branch `max(rho_J,rho_K)>=1/16` by an exact original-coordinate rank-three crossing with

\[
\|p_Q\|_\infty<19.049
\]

and a continuous density. Hence the only branch studied below is

\[
\rho_J<\frac1{16},\qquad \rho_K<\frac1{16}.
\tag{1.6}
\]

No use of the slope-gap identity is required for the new volume compiler; (1.6) alone forces a large mixed three-volume.

## 2. Exact mixed third-volume identity

Define the full three-dimensional bank Grams

\[
H_J:=\sum_{j\in J}r_jr_j^T
=\begin{pmatrix}a&b^T\\ b&G\end{pmatrix},
\]

\[
H_K:=\sum_{k\in K}r_kr_k^T
=\begin{pmatrix}s-a&-b^T\\ -b&G_K\end{pmatrix}.
\tag{2.1}
\]

By (1.1),

\[
H_J+H_K=\operatorname{diag}(s,1,1),
\qquad
\det(H_J+H_K)=s.
\tag{2.2}
\]

By the Schur-complement definitions (1.5),

\[
\det H_J=(\det G)\rho_J,
\qquad
\det H_K=(\det G_K)\rho_K.
\tag{2.3}
\]

Define the two mixed Cauchy--Binet currencies

\[
\Xi_{21}:=
\sum_{\substack{j_1<j_2\in J\\k\in K}}
\det(r_{j_1},r_{j_2},r_k)^2,
\]

\[
\Xi_{12}:=
\sum_{\substack{j\in J\\k_1<k_2\in K}}
\det(r_j,r_{k_1},r_{k_2})^2.
\tag{2.4}
\]

Every three-row Cauchy--Binet term for `H_J+H_K` is either all in `J`, all in `K`, of type `JJK`, or of type `JKK`. Therefore, exactly,

\[
\boxed{
\Xi_{21}+\Xi_{12}
=s-(\det G)\rho_J-(\det G_K)\rho_K.
}
\tag{2.5}
\]

This is the first new identity.

If `lambda_1,lambda_2 in [0,1]` are the eigenvalues of `G`, then

\[
\det G+\det(I-G)
=\lambda_1\lambda_2+(1-\lambda_1)(1-\lambda_2)\le1,
\tag{2.6}
\]

because `2 lambda_1 lambda_2<=lambda_1+lambda_2`. Hence (1.6) and (2.5) imply

\[
\Xi_{21}+\Xi_{12}
>s-\frac1{16}.
\tag{2.7}
\]

Using `s>=1/4`,

\[
\boxed{\Xi_{21}+\Xi_{12}>\frac3{16}.}
\tag{2.8}
\]

Thus when both r43 exact crossings lose their third direction, at least `3/16` of a complete original-coordinate third exterior volume survives across the two banks. The missing curvature is not absent.

## 3. Normalize the complement and obtain a 3/4 mixed-basis mass

Put

\[
S:=\operatorname{diag}(\sqrt s,1,1),
\qquad
\widetilde r_j:=S^{-1}r_j
=\left(\frac{x_j}{\sqrt s},t_j\right).
\tag{3.1}
\]

From (1.1),

\[
\sum_{j\ne i}\widetilde r_j\widetilde r_j^T=I_3.
\tag{3.2}
\]

So the complement rows form an exact three-dimensional Parseval frame. For every three-row set `B`,

\[
\det(r_B)^2=s\,\det(\widetilde r_B)^2.
\tag{3.3}
\]

Let `Omega_mix` be the total normalized squared volume of mixed `J/K` triples. Dividing (2.7) by `s` gives

\[
\Omega_{mix}
>1-\frac1{16s}
\ge\frac34.
\tag{3.4}
\]

This `>3/4` is a probability statement for the standard volume-sampling law of the Parseval frame (3.2). It is exact finite-dimensional algebra, not Monte Carlo.

## 4. A fixed heavy-set threshold and a paid diffuse-light branch

For each complement coordinate define its normalized complement leverage

\[
\ell_j:=\|\widetilde r_j\|^2.
\tag{4.1}
\]

Then

\[
\sum_{j\ne i}\ell_j=3.
\tag{4.2}
\]

Define the finite heavy set

\[
\mathcal H:=\{j:\ell_j>3/16\},
\qquad
\mathcal L:=\{j:\ell_j\le3/16\}.
\tag{4.3}
\]

Since sixteen strict inequalities `ell_j>3/16` would make their sum exceed three,

\[
\boxed{|\mathcal H|\le15.}
\tag{4.4}
\]

Let

\[
\widetilde G_L:=
\sum_{j\in\mathcal L}\widetilde r_j\widetilde r_j^T.
\tag{4.5}
\]

### Branch A: `det(tilde G_L)>=3/8`

Because `0<=tilde G_L<=I_3`, each eigenvalue is at most one. Hence

\[
\lambda_{min}(\widetilde G_L)\ge\det\widetilde G_L\ge\frac38.
\tag{4.6}
\]

For every `j in L`,

\[
\widetilde r_j^T\widetilde G_L^{-1}\widetilde r_j
\le\frac{8}{3}\ell_j
\le\frac12.
\tag{4.7}
\]

Return to the unnormalized rows. Their Gram is

\[
G_L:=\sum_{j\in\mathcal L}r_jr_j^T
=S\widetilde G_LS,
\]

so

\[
\det G_L=s\det\widetilde G_L
\ge\frac14\frac38
=\frac3{32}.
\tag{4.8}
\]

Condition only on the ORIGINAL coordinates outside `L`, and whiten the retained rows by `G_L^{-1/2}`. The remaining variables stay independent with their original density caps. The whitened row leverage is exactly the left side of (4.7), and the latent coefficient determinant is

\[
|\det(G_L^{1/2}MG_L^{1/2})|
=D\det G_L\ge\frac3{32}.
\tag{4.9}
\]

Apply the completed leverage-one-half Wiener--Fresnel theorem

`QFORM-DIFFUSE-SEPARABLE-PHASE-v1 / leverage-1/2 exact-rank3 compiler`,

source `yspennstate/math-open-problems@aff6876a6017be77544c50e8904e9baf8dac3bfe`.

It is uniform in arbitrary affine terms generated by the conditioned ORIGINAL coordinates and gives

\[
\boxed{
\|p_Q\|_\infty
\le3e\left(\frac{32}{3}\right)^{1/3}
<17.952.
}
\tag{4.10}
\]

The characteristic function is `L^1`, so this branch has a continuous `C_0` density.

This is a new paid portion of the r43 finite-spike/slope-gap survivor.

## 5. If the diffuse-light determinant fails, one of at most fifteen literal rows carries a large mixed star

Assume now

\[
\det\widetilde G_L<\frac38.
\tag{5.1}
\]

By Cauchy--Binet, `det tilde G_L` is exactly the normalized squared-volume mass of all triples lying entirely in `L`. Since the mixed mass is greater than `3/4` by (3.4), the mixed triples which hit `H` have total normalized mass greater than

\[
\frac34-\frac38=\frac38.
\tag{5.2}
\]

For `h in H`, define

\[
\omega_h:=
\sum_{\substack{B\text{ mixed }J/K\\|B|=3,\ h\in B}}
\det(\widetilde r_B)^2.
\tag{5.3}
\]

Summing `omega_h` over `h in H` counts every mixed triple hitting `H` at least once. Thus, by (4.4)-(5.2), some literal original coordinate `h in H` satisfies

\[
\boxed{\omega_h>\frac1{40}.}
\tag{5.4}
\]

Equation (3.3), `s>=1/4`, and the exact-rank-three principal determinant identity

\[
|\det A_B|=D\det(r_B)^2
\tag{5.5}
\]

then give the physical aggregate principal-triple star

\[
\boxed{
\sum_{\substack{B\text{ mixed }J/K\\|B|=3,\ h\in B}}
|\det A_B|
>\frac1{160}.
}
\tag{5.6}
\]

Unlike a selected minor, (5.6) cannot deteriorate with the ambient dimension.

## 6. A second split: either a heavy-heavy pair-star is paid, or the entire debt becomes one-heavy/two-light

Split the `omega_h` mass according to whether a mixed triple containing `h` contains another member of `H`.

### Branch B: at least half of `omega_h` also contains another heavy row

Then the normalized volume mass in such triples exceeds `1/80`. There are at most fourteen choices of a second heavy row `h'`. Therefore some literal pair `{h,h'}` has normalized anchored third-volume mass greater than

\[
\frac{1}{80\cdot14}=rac1{1120}.
\tag{6.1}
\]

Returning to raw rows and physical principal determinants gives

\[
T_{hh'}:=
\sum_{k\notin\{h,h'\}}
|\det A_{\{h,h',k\}}|
>Ds\frac1{1120}
\ge\frac1{4480}.
\tag{6.2}
\]

Apply my completed `QFORM-PAIR-ANCHORED-DETSTAR-COAREA-v1`, source

`yspennstate/math-open-problems@22d59171a8870dbcdbf7641e990800db2fc9df42`

`proofnet24/QFORM-density/fleet-2026-09-22/account03/B05/20260924T033744Z-account03-B05-QFORM-r39/REPORT.md`.

With

\[
C_*=24(3+\sqrt2)10^{2/3}=491.735145127\ldots,
\]

it yields

\[
\boxed{
\|p_Q\|_{\infty,\mathrm{ess}}
\le C_*4480^{1/3}
<8106.324.
}
\tag{6.3}
\]

This theorem allows the physical pair itself to be singular; no reciprocal pair determinant appears.

### Branch C: at least half of `omega_h` has `h` as the unique heavy row

Then both other rows lie in `L`, and their normalized mixed volume satisfies

\[
\sum_{\substack{j<k\in\mathcal L\\\{h,j,k\}\text{ mixed }J/K}}
\det(\widetilde r_h,\widetilde r_j,\widetilde r_k)^2
>\frac1{80}.
\tag{6.4}
\]

Therefore the physical aggregate satisfies

\[
\boxed{
\Sigma_h^{(2L)}:=
\sum_{\substack{j<k\in\mathcal L\\\{h,j,k\}\text{ mixed }J/K}}
|\det A_{\{h,j,k\}}|
>\frac1{320}.
}
\tag{6.5}
\]

At the same time every light row satisfies the deterministic original-frame leverage bound

\[
\boxed{
\left\|
\left(\frac{x_j}{\sqrt{1-c}},t_j\right)
\right\|^2\le\frac3{16},
\qquad j\in\mathcal L.
}
\tag{6.6}
\]

Equations (6.5)-(6.6) are the new exact endpoint. They say the surviving obstruction is no longer an unspecified three-spike regression gap: one literal heavy source carries a universal aggregate third determinant star whose other two legs lie in a uniformly light original-product bank.

No claim is made that (6.5) alone implies a bounded density. Paying this one-heavy/two-light aggregate before selecting a reciprocal pair is the remaining analytic step.

## 7. Designated partner account04/B05 applied to the surviving endpoint

The completed designated partner theorem is

`QFORM-PHYSICAL-DEFINITE-PAIR-COAREA-v1`,

source

`yspennstate/math-open-problems@33cabb3bd5e466a58adc6eac49eba210ef62ef14`

`proofnet24/QFORM-density/fleet-2026-09-22/account04/B05/20260924T011830Z-account04-B05-convex-pair-r3/REPORT.md`.

For any literal original-coordinate definite principal pair `C=A[{r,s},{r,s}]`, with cap-one laws and arbitrary outside coupling retained, it proves

\[
\|p_Q\|_{\infty,\mathrm{ess}}
\le\frac{\pi}{\sqrt{|\det C|}}.
\tag{7.1}
\]

Apply it to the actual branch-C geometry. If the selected heavy coordinate `h` has any light partner `j in L` for which the literal pair `A[{h,j},{h,j}]` is definite and

\[
|\det A_{\{h,j\}}|\ge\frac1{64},
\tag{7.2}
\]

then

\[
\boxed{
\|p_Q\|_{\infty,\mathrm{ess}}
\le8\pi<25.133.
}
\tag{7.3}
\]

Thus the genuinely unpaid endpoint may additionally be assumed to satisfy

\[
\boxed{
\text{every definite literal pair }\{h,j\},\ j\in\mathcal L,
\text{ has }|\det A_{\{h,j\}}|<1/64.
}
\tag{7.4}
\]

This is an actual target inequality from the designated partner, not a citation-only use.

## 8. Compact conditional proof assembly and exact new debt

Within the r43 moderate-hub, transverse-diffuse, small-regression-residual chamber, the present run gives the following exhaustive compiler:

1. If `det tilde G_L>=3/8`, the complete ambient law has a continuous density with `||p_Q||_infinity<17.952`.
2. Otherwise one of at most fifteen literal coordinates carries mixed third-volume star `>1/160`.
3. If at least half that star meets another heavy row, a literal pair has determinant-star `>1/4480` and r39 gives `||p_Q||_(infinity,ess)<8106.324`.
4. Otherwise one literal heavy coordinate `h` carries the one-heavy/two-light star (6.5), with every light row satisfying (6.6). If any such `h`-light pair is definite with determinant at least `1/64`, the designated account04/B05 theorem improves the branch to `8 pi<25.133`.

The first exact unpaid implication is therefore

`QFORM-ONEHEAVY-DIFFUSE-TWOLIGHT-STAR-COAREA-v1`:

> Under (6.5)-(6.6) and the no-large-definite-pair gate (7.4), spend the aggregate two-light determinant star before selecting/inverting an individual physical pair. The likely receiver is a one-heavy plus two-dimensional product-projection `L^p`/Fresnel or interval estimate. It must retain the longitudinal component of the light bank and arbitrary same-bank quadratic curvature; conditioning on a projected light variable is not allowed.

This endpoint is source-preserving: `h`, `j`, `k` are literal original coordinates, while all coefficient-space rotations used above are deterministic algebra only.

The separate near-coloop chamber `c>3/4` remains routed to the fresh near-coloop compilers; this run does not relabel it as solved.

## 9. Scope and status

This report is a supporting exact-rank-three compiler, not a full proof of the owner target. It establishes new uniform density bounds on Branches A, B, and the designated definite-pair subbranch of C, and isolates the exact remaining factor (6.5)-(6.6) on this route.

**Full QFORM remains OPEN / NOT PROVED / NOT DISPROVED.**  
**Full-target continuity remains OPEN.**
