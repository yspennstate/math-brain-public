SIGNED IN - working on the quadratic-form bounded-density conjecture (universal constant), account account03, slot B08, 2026-09-24T14:49:16Z.
attacking: the current fixed-multiplicity frontier by intersecting the new multiplicity-seven invertible-seed overlap packet with physical two-deletion spectral-window rigidity, using the completed account04/B08 child-window receiver on an actual deletion chain.

# account03/B08 r58 — multiplicity-seven two-deletion ridge rigidity and overlap-one intersection

Objective: `QFORM-FIXED-MULTIPLICITY-AUDIT-20260924`  
Status: **PROVED SUPPORTING STRUCTURAL/ANALYTIC ROUTER; NO SEVEN-EIGENVALUE THEOREM CLAIMED**.  
Baseline manuscript: `yspennstate/math-open-problems@7c0d6e60946b19423e6400a12d34b473cf0591e2`, `proofnet24/QFORM-density/fixed-multiplicity-2026-09-24/manuscript.tex`, blob `183ccd294763214e6a707e8d4749ff9a8cf7006d`, SHA-256 `9f3bdec0b88debe9a66076c7b4a5cc894fb14e69b89591a4107e785340f65e69`.

The pinned 790-line baseline is byte-for-byte unchanged from the B08 end-to-end audits already recorded by this worker. The present run does not promote the baseline or the multiplicity-nine replacement; it uses only previously checked rank perturbation, the current multiplicity-seven overlap theorem, and the designated account04/B08 affine-uniform deletion receiver.

Throughout the normalized argument
\[
\eta=\frac1{100},\qquad \tau=\frac1{64},\qquad \kappa=\frac1{80^2}.
\]
A `no-pivot` matrix in this note is in the manuscript's normalized no-`\eta`-pivot chamber; in particular every physical diagonal satisfies `|A_{jj}|<eta`.

## 1. New threshold observation: multiplicity seven survives two physical deletions exactly to three directions

For a set `I` of original coordinates, put `q=|I|`, let
\[
C_I=A[I^c,I^c],
\]
and pad `C_I` by zeroes back to the ambient dimension. If `P_I` is the coordinate projection killing `I`, the padded matrix is `P_I A P_I`, while
\[
A-P_IAP_I=(I-P_I)A+P_IA(I-P_I).
\tag{1.1}
\]
Both summands on the right have rank at most `q`, so
\[
\operatorname{rank}(A-P_IAP_I)\le2q.
\tag{1.2}
\]
The manuscript's nonsymmetric singular-value rank perturbation lemma therefore gives
\[
\boxed{
 s_{j+2q}(A)\le s_j(C_I)
}
\tag{1.3}
\]
for every `j>=1`.

Assume now
\[
s_7(A)\ge1.
\tag{1.4}
\]
Taking `j=7-2q` in (1.3), for `q=0,1,2`, gives
\[
\boxed{
 s_7(A)\le s_7(C_\varnothing),\qquad
 s_7(A)\le s_5(C_{\{i\}}),\qquad
 s_7(A)\le s_3(C_{\{i,j\}}).
}
\tag{1.5}
\]
Thus **every principal child obtained by deleting at most two original coordinates still has at least three unit-scale singular directions**. The two-deletion endpoint is exact in the count: seven parent directions minus the rank-four deletion loss leave precisely the three directions required by the spectral-window receiver.

This lowers the multi-deletion rigidity statement previously recorded by B08 from the `s_8` chamber to the new structural `s_7` frontier.

## 2. Actual application of the designated account04/B08 theorem

The designated partner result is account04/B08 theorem `QFORM-PHYSICAL-DELETION-CHILD-WINDOW-v1`,

`yspennstate/math-open-problems@a5e66e2944c89857a41d5e18c283d53a4307be76`,

`proofnet24/QFORM-density/fleet-2026-09-22/account04/B08/20260923T212412Z-account04-B08-QFORM-r2/REPORT.md`.

At scale `m=1`, it says that after deleting one **original** coordinate, if the literal child quadratic matrix has at least three eigenvalues of modulus at least one and
\[
\max_j\left(\mathbf1_{\{|C|\ge1/64\}}\right)_{jj}\le\frac1{32},
\tag{2.1}
\]
then the full parent quadratic polynomial, retaining all cross terms as affine terms after conditioning, has
\[
\boxed{
\|p_Q\|_\infty
\le \frac{288\sqrt{3e}}{13}<64,
\qquad p_Q\in C_0(\mathbb R).
}
\tag{2.2}
\]

This partner theorem applies directly to every one-coordinate child under (1.4), because (1.5) gives `s_5(C_{i})>=1` and hence `s_3(C_i)>=1`.

It also applies **iteratively to every two-coordinate child**. Fix distinct original coordinates `i,j`. First condition on `X_i=x`. The remaining variables are still independent with their original density caps, and their quadratic matrix is `C_{\{i\}}`; all dependence on `x` enters only through affine/separable terms. Within that conditional problem apply account04/B08 to the original coordinate `j`. Its deletion child is exactly `C_{\{i,j\}}`, and (1.5) gives `s_3(C_{\{i,j\}})>=1`. Therefore, whenever (2.1) holds for this two-deletion child, every conditional law has the uniform bound (2.2). Mixing in `x` preserves the same essential-supremum bound. The conditional densities are uniformly bounded and each is `C_0`, so dominated convergence also preserves continuity and vanishing at infinity.

Consequently, under `s_7(A)>=1`, if **any** one- or two-coordinate deletion child has a diffuse `1/64` window, then
\[
\boxed{
\|p_Q\|_\infty<64,\qquad p_Q\in C_0(\mathbb R).
}
\tag{2.3}
\]
The same affine-uniform spectral-window theorem also pays the parent itself if its own `1/64` window is diffuse.

## 3. Failure of all three levels forces three nested physical stars

Assume now that `A` is no-pivot, satisfies (1.4), and no parent/one-deletion/two-deletion diffuse-window payment is available. Then there are distinct original coordinates `i_1,i_2,i_3` such that
\[
\left(\mathbf1_{\{|A|\ge\tau\}}\right)_{i_1i_1}>\frac1{32},
\tag{3.1}
\]
\[
\left(\mathbf1_{\{|C_{\{i_1\}}|\ge\tau\}}\right)_{i_2i_2}>\frac1{32},
\tag{3.2}
\]
and
\[
\left(\mathbf1_{\{|C_{\{i_1,i_2\}}|\ge\tau\}}\right)_{i_3i_3}>\frac1{32}.
\tag{3.3}
\]

The spectral-variance identity gives a literal original-coordinate coefficient lower bound. For any symmetric child `C`, physical coordinate `j`, `a=C_{jj}`, and spectral measure `mu_j` of `C` at `e_j`,
\[
\|C[j,-j]\|_2^2
=\int(\lambda-a)^2\,d\mu_j(\lambda).
\tag{3.4}
\]
Because all retained physical diagonals inherit `|a|<eta`, on the window `|lambda|>=tau` we have `|lambda-a|>tau-eta`. If its leverage exceeds `1/32`, then
\[
\|C[j,-j]\|_2
>(\tau-\eta)\sqrt{\frac1{32}}
=\frac9{6400\sqrt2}.
\tag{3.5}
\]
Define
\[
c_*:=\frac9{6400\sqrt2}
=0.0009943689110435824\ldots .
\tag{3.6}
\]
Applying (3.5) to (3.1)--(3.3) gives the nested physical certificate
\[
\boxed{
\|A[i_1,[n]\setminus\{i_1\}]\|_2>c_*,
}
\tag{3.7}
\]
\[
\boxed{
\|A[i_2,[n]\setminus\{i_1,i_2\}]\|_2>c_*,
}
\tag{3.8}
\]
\[
\boxed{
\|A[i_3,[n]\setminus\{i_1,i_2,i_3\}]\|_2>c_*.
}
\tag{3.9}
\]
No rotated coordinate is used, and these three lower bounds do **not** assert that the star vectors are linearly independent. In particular they may not be renamed as a third compound or a good physical `3x3` minor.

## 4. Intersection with the new invertible-seed overlap-one theorem

The current structural frontier from account03/B10 theorem `QFORM-S7-INVERTIBLE-OVERLAPONE-JENSEN-v1` is

`proofnet24/QFORM-density/fixed-multiplicity-2026-09-24/improvements/account03/B10/20260924T141329Z-account03-B10-QFORM-FM-audit-r11/S7_OVERLAPONE_SHARPENING.md`.

For a symmetric matrix define
\[
V_2(A)=\sum_{S\cap T=\varnothing,\ |S|=|T|=2}\det A[S,T]^2,
\]
\[
V_3(A)=\sum_{S\cap T=\varnothing,\ |S|=|T|=3}\det A[S,T]^2,
\]
and let `W^times_{2,1}` be the same-index bordered third-minor volume summed only over **invertible** disjoint two-seeds. B10 proves under `s_7(A)>=1`
\[
W^\times_{2,1}(A)
\ge
V_2(A)\left(1-3\sqrt{V_3(A)/V_2(A)}\right)_+^2.
\tag{4.1}
\]

In the normalized no-pivot chamber, the baseline order-two spectral-to-volume proposition gives
\[
V_2(A)\ge\kappa^2.
\tag{4.2}
\]
Hence either
\[
V_3(A)\ge\kappa^3,
\tag{4.3}
\]
or
\[
\boxed{
W^\times_{2,1}(A)
>\left(\frac{77}{80}\right)^2\kappa^2
=\frac{5929}{262144000000}
=2.2617340087890625\times10^{-8}.
}
\tag{4.4}
\]

The first branch (4.3) is already paid by the reviewed marginal-free `E_3` physical-crossing receiver: a fair original-coordinate cut has `E_3>=4^{-3}kappa^3`, hence
\[
\boxed{
\|p_Q\|_\infty<2400,\qquad p_Q\in C_0(\mathbb R).
}
\tag{4.5}
\]
(the sharper recorded value is about `2370.934`).

Combining (2.3), (3.7)--(3.9), and (4.4)--(4.5) gives the new terminal router:

### Theorem — `QFORM-S7-OVERLAP-PLUS-MULTIDELETE-RIDGE-RIGIDITY-v1`

Let `A=A^T` be in the normalized no-`eta`-pivot chamber and satisfy `s_7(A)>=1`. For every independent cap-one product input and arbitrary affine terms, **at least one** of the following holds:

1. `Q` has a `C_0` density with `||p_Q||_infinity<2400`; or
2. the exact invertible-seed overlap-one currency satisfies (4.4), and there exist distinct original coordinates `i_1,i_2,i_3` satisfying all three nested star bounds (3.7)--(3.9).

Indeed, if (4.3) holds use (4.5). Otherwise (4.4) holds. In that overlap branch, if the parent or either deletion level has a diffuse `1/64` window, (2.3) (or the parent affine-window theorem) gives the stronger `<64` payment and we are in alternative 1. If not, the nested-star construction gives alternative 2. `QED`.

This is a strict strengthening of the previous multiplicity-seven structural endpoint: the unpaid overlap-one packet now simultaneously carries three scale-uniform, nested, original-coordinate off-diagonal stars.

## 5. Scaling

For general `s>0`, apply the normalized statement to `A/s`. The no-pivot thresholds scale in the manuscript's usual way. The paid branches become
\[
\|p_Q\|_\infty<2400\,K^2/s
\]
(and `<64 K^2/s` on a diffuse child-window branch). The terminal currencies scale as
\[
V_3(A)<\kappa^3s^6,
\qquad
W^\times_{2,1}(A)>
\frac{5929}{262144000000}s^6,
\tag{5.1}
\]
and each nested star satisfies
\[
\boxed{
\|A[i_r,\text{remaining coordinates}]\|_2>c_*s,
\qquad r=1,2,3.
}
\tag{5.2}
\]
The output-density scaling is the standard `K^2/s` scaling used in the manuscript and the multiplicity-nine replacement.

## 6. What remains

This does **not** prove a seven-eigenvalue theorem. The first unpaid no-pivot implication is now more rigid:

> Build a dependence-safe overlap-one/shared-anchor receiver for the aggregate `W^times_{2,1}` packet **while also using, or at least preserving, the nested physical stars (3.7)--(3.9)**. The receiver must keep the common physical anchor inside both translated product banks until after source averaging; it may not bound the bilateral shear translations by the induced anchor determinant, since the current counterexample shows those shear norms can diverge while the induced anchor remains uniformly nonsingular.

The star chain alone is not a third-compound certificate, and paying a reciprocal of one selected tiny seed determinant would lose dimension-free control. A successful receiver at this intersection would close the current no-pivot `s_7` frontier; the pivot branches and lower multiplicities remain separate accounting.

The unrestricted three-eigenvalue conjecture remains OPEN. Global continuity at the unrestricted target remains OPEN. The payments (2.3) and (4.5) are `C_0`; no continuity is asserted for the unpaid terminal structure.

Execution status remains `WITHOUT_VERIFIED_BRAIN`: repository retrieval and publication are not evidence of authenticated native learned-memory ingestion.
