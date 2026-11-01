# MOC4 fleet03/B20 — mixed-Schur global trust gate collapses exactly to the Lyapunov–Schmidt reserve

**Directive:** `COLLECTIVE-OPEN-PROBLEMS-20260921T234023Z`  
**Campaign:** Marcus–de Oliveira, complex normal `4 x 4` case (`MOC4`)  
**Run:** `20260922T071802Z-fleet03-B20-MOC4-r12`  
**Outcome:** `ESSENTIAL_STEP_APPLIED` and `CANDIDATE_REFUTED` for treating the same-pair global trust gate as extra leverage beyond the lead's mixed-Schur Lyapunov–Schmidt reserve.  
**Execution:** `WITHOUT_VERIFIED_BRAIN`; `full_brain_connected=false`.  
**Parent target:** still **OPEN / NOT PROVED / NOT DISPROVED**.

## 1. Source-valid live state

The exact target is
\[
\det(D_a+UD_bU^*)\in \operatorname{conv}\left\{
\prod_i(a_i+b_{\sigma(i)}):\sigma\in S_4
\right\}
\]
for every true unitary `U` and all complex spectra, including singular and repeated cases.

The newest complete campaign-lead report used is fleet03/B07
`20260922T064004Z-fleet03-B07-MOC4-r12`,
`MOC4-KERNEL-QUARTIC-RESERVE-v1`.
After the strict Spin(4) saturation branches have been removed, a hypothetical positive-gap global maximizer has, on every complementary pair split, a true-unitary Hessian block
\[
\mathcal H=
\begin{pmatrix}
-AI_2&M\\
M^T&-BI_2
\end{pmatrix}\preceq0,\qquad A,B>0.
\tag{1}
\]
The lead's first unpaid branch `MSQR` is the mixed-Schur boundary
\[
\|M\|_{\rm op}=\sqrt{AB},
\tag{2}
\]
where a genuine Hessian kernel appears. Its sharpened necessary condition is the Lyapunov–Schmidt reserve
\[
J_4(k)+3\langle \ell,(-\mathcal H)^+\ell\rangle\le0.
\tag{3}
\]

The named OTHER-account result applied is fleet04/B09
`20260922T060924Z-b09-moc4-r12`,
`MOC4-ROOT-SATURATION-EXCLUSION-v1`: every support-violating genuine global maximizer has all elementary left/right pair gates strict. This justifies `A,B>0` without a genericity or nonzero-minor assumption.

I also use my immediately preceding exact same-unitary result
`MOC4-SPIN4-GLOBAL-TRUST-REGION-GATE-v1`: on a complementary genuine `SU(2) x SU(2)` product orbit the support is exactly bi-affine,
\[
f(n,m)=c+p\cdot n+q\cdot m+n^TZm,\qquad n,m\in S^2,
\tag{4}
\]
and global maximality at the north pole is equivalent to one exact sphere trust-region PSD certificate.

The purpose of this run is to combine (2)-(4), not to add another independent gate.

## 2. Pole normal form

Choose Bloch coordinates with the present point at
\[
e=(0,0,1)
\]
in both factors. Write
\[
Z=\begin{pmatrix}M&r\\s^T&z\end{pmatrix},
\qquad
p=(-r,A-z),\qquad q=(-s,B-z).
\tag{5}
\]
These are exactly the stationarity equations at `(e,e)`.

At the mixed-Schur boundary choose orthonormal tangent singular bases so that
\[
M=\operatorname{diag}(\sqrt{AB},m),\qquad |m|\le\sqrt{AB}.
\tag{6}
\]
Write
\[
r=(r_1,r_2),\qquad s=(s_1,s_2),\qquad H=A+B-2z.
\tag{7}
\]

## 3. Exact singular-circle factorization

For fixed `n`, maximizing (4) over `m` gives
\[
g(n)=c+p\cdot n+\|q+Z^Tn\|.
\tag{8}
\]
Let
\[
L=A+B-z
\]
and define the squared trust gap
\[
\Phi(n)=(L-p\cdot n)^2-\|q+Z^Tn\|^2.
\tag{9}
\]
On the great circle through the top left singular direction,
\[
n(\theta)=(\sin\theta,0,\cos\theta),
\]
a direct exact expansion, using only (5)-(6), gives
\[
\boxed{
\Phi(\theta)=
\bigl(AH-\|s\|^2\bigr)(1-\cos\theta)^2
+2\bigl(A r_1+\sqrt{AB}\,s_1\bigr)
\sin\theta(1-\cos\theta).
}
\tag{10}
\]

At a local, hence global, maximum the second term cannot survive: near zero it has opposite signs for `theta` and `-theta` and is cubic. Therefore
\[
A r_1+\sqrt{AB}\,s_1=0.
\tag{11}
\]
Set
\[
r_1=\sqrt B\,\rho,\qquad s_1=-\sqrt A\,\rho.
\tag{12}
\]
Then the **entire** singular great-circle trust condition collapses to
\[
\Phi(\theta)=
\left[A(H-\rho^2)-s_2^2\right](1-\cos\theta)^2.
\tag{13}
\]
Thus the exact continuum on this singular circle is controlled by one scalar coefficient.

Equation (11) is precisely the mixed-kernel cubic cancellation in this bi-affine normal form.

## 4. Full product-orbit trust certificate collapses to a 2 x 2 PSD matrix

The preceding B20 trust-region theorem writes the squared condition as
\[
n^TQ_0n+2b_0^Tn+c_0\ge0,\qquad \|n\|=1,
\tag{14}
\]
with
\[
Q_0=pp^T-ZZ^T,\quad
b_0=-(Lp+Zq),\quad
c_0=L^2-\|q\|^2.
\tag{15}
\]
Its exact S-lemma certificate is
\[
\mathscr T_\lambda=
\begin{pmatrix}
Q_0-\lambda I_3&b_0\\
b_0^T&c_0+\lambda
\end{pmatrix}\succeq0.
\tag{16}
\]

Under (6),(11),(12), the north-pole equality forces
\[
\lambda=-AB.
\tag{17}
\]
In the ordered basis `(u,w,e,1)`, where `u` is the top singular tangent and `w` its tangent orthogonal complement, exact algebra gives
\[
\mathscr T_{-AB}=
\begin{pmatrix}
0&0&0&0\\
0&D&-E&E\\
0&-E&C&-C\\
0&E&-C&C
\end{pmatrix},
\tag{18}
\]
where
\[
D=AB-m^2,\qquad
E=A r_2+m s_2,\qquad
C=A(H-\rho^2)-s_2^2.
\tag{19}
\]

Consequently the complete four-real-dimensional product-orbit global-maximality condition is equivalent to
\[
\boxed{
\begin{pmatrix}
D&-E\\
-E&C
\end{pmatrix}\succeq0.
}
\tag{20}
\]
No arbitrary bistochastic or independent-minor data enter this reduction.

### Simple mixed singular value

If `|m|<sqrt(AB)`, then `D>0`, and (20) is equivalent to
\[
\boxed{
H\ge
\rho^2+
\frac{A r_2^2+2m r_2s_2+B s_2^2}{AB-m^2}.
}
\tag{21}
\]
The sign condition needed before squaring the trust inequality follows automatically from (21), so no extra branch is hidden.

### Double mixed singular value

If `m=epsilon sqrt(AB)`, `epsilon=+-1`, then `D=0`. Positivity of (20) forces
\[
A r_2+m s_2=0.
\tag{22}
\]
Writing
\[
r_2=\sqrt B\,\rho_2,\qquad
s_2=-\epsilon\sqrt A\,\rho_2,
\]
the remaining condition is exactly
\[
\boxed{H\ge \rho^2+\rho_2^2.}
\tag{23}
\]

Hence the double-kernel case is included rather than discarded as a genericity exception.

## 5. Identification with the lead's Lyapunov–Schmidt reserve

In geodesic product coordinates `(x,y)` for the two Bloch spheres, the cubic part of (4) at the stationary pole is
\[
J_3(x,y)=
-3\left[(r\cdot x)\|y\|^2+(s\cdot y)\|x\|^2\right].
\tag{24}
\]
For the mixed Hessian kernel
\[
k=(\sqrt B\,u,\sqrt A\,v),
\tag{25}
\]
equation (11) is `J_3(k)=0`.

The quartic derivative along `k` is
\[
J_4(k)=3AB(2z-A-B)=-3ABH.
\tag{26}
\]
For the simple case `|m|<sqrt(AB)`, direct inversion of the nonzero Hessian modes gives
\[
\left\langle \ell,(-\mathcal H)^+\ell\right\rangle
=
AB\left[
\rho^2+
\frac{A r_2^2+2m r_2s_2+B s_2^2}{AB-m^2}
\right].
\tag{27}
\]
Substituting (26)-(27) into the lead's reserve (3) gives **exactly (21)**.

For the double-singular case, the requirement that the cubic covector annihilate the two-dimensional Hessian kernel gives (11) and (22), and the pseudoinverse reserve reduces exactly to (23).

Therefore:

### `MOC4-MIXED-SCHUR-TRUST-COLLAPSE-v1`

> On a genuine complementary Spin(4) product orbit at a support-violating global maximizer, once the pair Hessian reaches the mixed-Schur boundary, the exact global `S^2 x S^2` trust-region condition is **equivalent** to the lead's Lyapunov–Schmidt kernel reserve (including the double-kernel case). It supplies no additional same-pair obstruction.

This is the decisive point of the run. The prior idea that one could close `MSQR` simply by adding the full same-pair global trust gate to the LS reserve is refuted: at the singular boundary they are the same condition in different coordinates.

## 6. What this removes from the live proof tree

The live `MSQR` branch no longer needs to carry both

1. the mixed-kernel cubic/quartic/LS condition, and
2. a separate exact global trust-region condition for that **same** complementary pair split.

They collapse to (20)-(23). Thus further exact optimization of that one Spin(4) orbit cannot by itself exclude the residual; a proof must use information coupling this split to other genuine-unitary data.

The first unpaid implication is sharpened to:

> **`MOC4-MIXED-SCHUR-CROSS-SPLIT-COUPLING-v1` (OPEN).**  
> For structured spectral coefficients `(K,X)` from one MOC4 support direction and one genuine `O=Lambda^2 U`, prove that a positive support residual cannot satisfy one mixed-Schur pair boundary together with its exact reduced certificate (20), the other five left/right pair conditions, full Spin(6) stationarity, subgroup roofs, and same-unitary `P/R/D` identities. Alternatively produce actual complex spectra and a true unitary satisfying all conditions and separating from all 24 permutation endpoints.

A concrete next route is to substitute the explicit spectral/Vandermonde identities into the other five pair certificates and compare their Schur complements with (20). The present theorem says not to spend another run optimizing the already-collapsed singular pair orbit.

## 7. Exact verification

`verify_mixed_schur_trust_collapse.py` symbolically checks:

- the exact great-circle factorization (10);
- the forced trust multiplier `lambda=-AB`;
- the full `4 x 4` certificate reduction (18);
- the determinant identity turning (20) into (21);
- the double-singular reduction (22)-(23).

Captured output is `VERIFY_OUTPUT.txt`.

Verifier SHA-256:
`978428bdb97f328a9893a8814678698615cd974faa2829a8780d0337d8922f1d`.

Output SHA-256:
`56c2b54edc195118757d4ae2fa89ad9d49e9c2d6231dc2bad5f81c0a63930970`.

The verifier checks algebraic identities only; it is not evidence that the remaining structured cross-split implication is proved.

## 8. Honest status

- `MOC4-MIXED-SCHUR-TRUST-COLLAPSE-v1`: **PROVED**.
- Same-pair global-trust-as-extra-MSQR-leverage: **REFUTED / REDUNDANT**.
- `MOC4-MIXED-SCHUR-CROSS-SPLIT-COUPLING-v1`: **OPEN**.
- Full MOC4: **OPEN / NOT PROVED / NOT DISPROVED**.
