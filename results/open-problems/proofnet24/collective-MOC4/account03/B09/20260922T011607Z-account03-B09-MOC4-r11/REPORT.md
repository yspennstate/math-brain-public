# MOC4 account03/B09 r11 — complementary-minor orientation rigidity and a 6κ support certificate

**Directive:** `COLLECTIVE-OPEN-PROBLEMS-20260921T234023Z`  
**Campaign:** MOC4, complex normal 4-by-4 Marcus–de Oliveira determinant hull  
**Worker:** account03/B09  
**Outcome:** `ESSENTIAL_STEP_APPLIED` — a new exact nonlinear coupling between the 1-minor transport `P` and complementary 2-minor transport `R`, plus a spectral gap criterion that proves the full determinant support inequality on a nontrivial region where the independent `P`/`R` Birkhoff relaxation overshoots the hull. Full MOC4 remains **OPEN / NOT PROVED / NOT DISPROVED**.  
**Brain status:** `WITHOUT_VERIFIED_BRAIN`.

## 1. Fresh scope and consumed results

Current owner control revision `2026-09-22.2` supersedes the former benchmark role and assigns account03/B09 to MOC4. No benchmark development or held-out benchmark material is used here.

The source-exact target is

\[
\det(A+B)\in\operatorname{conv}\left\{\prod_{i=1}^4(a_i+b_{\sigma(i)}):\sigma\in S_4\right\}
\]

for all complex normal `4 x 4` matrices `A,B`, including singular and repeated spectra.

This run consumes and applies the following completed mathematical artifacts:

1. **Campaign lead account03/B07, `MOC4-DRURY-UPPER-FACET-v1`**, report blob `3671449a3da3b009195454dedc4489e678c1dfd1`. It reduces the unitary support problem to a finite spectral upper-facet family and identifies the actual endpoint support maximum `M`; full MOC4 remains open.
2. **Named OTHER-account partner account04/B07, `MOC4-SO6-WEYL-v1`**, handoff blob `2f81a2fa0286800be44360911ba0f5c347ae10bc`, scientific report blob `2054ffca05aee70d57d3aa6723cc19bf983c7be8`. It identifies the complementary-pair variables as `2 x 2` block invariants of an `SO(6)` realification of `Lambda^2 U` and the 24 permutation endpoints with the `D_3=A_3` Weyl group.
3. **account01/B07 mixed-assignment reduction**, report blob `182e1f1b24a290b1a25d1bc0677b6b031e0c088d`. It proves that the signed complement matrix `D` is exactly the mean-zero Hadamard block of `P=|U|^2`, and reduces support to the exact mixed `(P,R)` inequality.
4. This worker's preceding `MOC4-C2-COMPLEMENT-BOUND-v1`, report blob `94dc51181d3dbe98c2df07da7f3370c3787e270a`, supplies the complement-pair coordinates. Its old independent parity relaxation is not reused as a theorem; the account01 identity is sharper.

No common positive permutation lift is assumed; that stronger route is already refuted in the campaign.

## 2. Exact mixed support expression

After diagonalization, let `P=(p_ij)=(|u_ij|^2)`. Use the three complementary pair classes

\[
12|34,\qquad 13|24,\qquad 14|23.
\]

For oriented representatives `S_alpha,T_beta`, set

\[
r_{\alpha\beta}=|\det U[S_\alpha,T_\beta]|^2+|\det U[S_\alpha,T_\beta^c]|^2,
\]

\[
d_{\alpha\beta}=|\det U[S_\alpha,T_\beta]|^2-|\det U[S_\alpha,T_\beta^c]|^2.
\]

Then `R=(r_ab)` is doubly stochastic, and with the normalized Walsh-Hadamard matrix `H`,

\[
HPH^T=\begin{pmatrix}1&0\\0&D\end{pmatrix},\qquad D=(d_{\alpha\beta}).
\tag{1}
\]

For a fixed support direction `|eta|=1`, the account01 reduction gives real coefficient arrays `C in R^{4x4}` and `X in R^{3x3}` such that

\[
\Re\bigl(\eta\det(A+UBU^*)\bigr)
=C_0+\langle P,C\rangle+\frac12\langle R,X\rangle.
\tag{2}
\]

For `sigma in S_4`, let `rho_sigma in S_3` be its induced permutation of the three complementary pair classes, and define

\[
c_\sigma:=\sum_i C_{i,\sigma(i)},\qquad
x_\rho:=\sum_{\alpha=1}^3X_{\alpha,\rho(\alpha)}.
\tag{3}
\]

The actual permutation endpoint is

\[
C_0+c_\sigma+\frac12x_{\rho_\sigma}.
\tag{4}
\]

Hence the exact residual mixed inequality is

\[
\langle P,C\rangle+\frac12\langle R,X\rangle
\le M,
\qquad
M:=\max_{\sigma\in S_4}\left(c_\sigma+\frac12x_{\rho_\sigma}\right).
\tag{MI}
\]

This `M` is the same determinant-support endpoint maximum appearing in the lead's support formulation, apart from the fixed `C_0`.

## 3. New complementary-minor orientation-rigidity lemma

Normalize the scalar phase of `U` so `det U=1`. The exterior-square/Hodge realification gives an orthogonal map

\[
O\in SO(6)
\]

split into three oriented real 2-planes. Write its `2 x 2` blocks as `O_{\alpha\beta}`. The named partner's exact identification is

\[
\boxed{r_{\alpha\beta}=\frac12\|O_{\alpha\beta}\|_F^2,
\qquad d_{\alpha\beta}=\det O_{\alpha\beta}.}
\tag{5}
\]

### Lemma 1 — parity forces one full unit of pair-assignment leakage

For every `rho in S_3`,

\[
\boxed{
\prod_{\alpha=1}^3 d_{\alpha,\rho(\alpha)}\le0
\quad\Longrightarrow\quad
\sum_{\alpha=1}^3 r_{\alpha,\rho(\alpha)}\le2.}
\tag{6}
\]

Equivalently,

\[
\sum_\alpha r_{\alpha,\rho(\alpha)}>2
\quad\Longrightarrow\quad
\prod_\alpha d_{\alpha,\rho(\alpha)}>0.
\tag{7}
\]

#### Proof

Permute the three column planes, which reduces to `rho=id`. Put

\[
A_i=O_{ii},\qquad r_i=\frac12\|A_i\|_F^2,
\qquad \varepsilon=3-\sum_i r_i.
\]

Since every two-row block of an orthogonal `O` has total squared Frobenius norm `2`,

\[
\sum_{i\ne j}\|O_{ij}\|_F^2=2\varepsilon.
\tag{8}
\]

Let the singular values of `A_i` be `s_{i1},s_{i2} in [0,1]`. Choose a nearest orthogonal polar factor `Q_i`. If `det A_i` is nonzero, choose the polar factor with the same determinant sign. If `det A_i=0`, the zero singular direction permits either orientation at the same nearest-orthogonal distance. Therefore, when `prod_i det A_i<=0`, the choices can be made so that

\[
Q=\operatorname{diag}(Q_1,Q_2,Q_3)\in O(6),\qquad \det Q=-1.
\tag{9}
\]

For every `s in [0,1]`, `(1-s)^2<=1-s^2`, hence

\[
\sum_i\|A_i-Q_i\|_F^2
\le\sum_i\left(2-\|A_i\|_F^2\right)
=2\varepsilon.
\tag{10}
\]

Combining diagonal and off-diagonal blocks,

\[
\|O-Q\|_F^2\le4\varepsilon.
\tag{11}
\]

But `O in SO(6)` and `det Q=-1`. Thus `Q^TO` is a real orthogonal matrix of determinant `-1`, so it has an eigenvalue `-1`. Consequently

\[
\|O-Q\|_F^2=\|Q^TO-I\|_F^2\ge4.
\tag{12}
\]

Therefore `epsilon>=1`, i.e. `sum_i r_i<=2`. This proves (6). `square`

This is a genuinely joint `P`/`R` constraint because `d` is already the Hadamard transform of `P` by (1). It is stronger than the entrywise inequality `|d_ab|<=r_ab` in the orientation-sensitive regime.

## 4. Quantitative synchronization once one pair assignment dominates

A second elementary block inequality will be needed. For a `2 x 2` contraction with singular values `s_1,s_2`,

\[
r=\frac{s_1^2+s_2^2}{2},\qquad |d|=s_1s_2,
\]

so

\[
\boxed{r\le\frac{1+d^2}{2}}
\tag{13}
\]

because the difference is `((1-s_1^2)(1-s_2^2))/2>=0`.

Now assume `x_rho` has a unique maximizing pair permutation `rho_0`. Put

\[
x_0=x_{\rho_0},\qquad
\gamma=x_0-\max_{\rho\ne\rho_0}x_\rho>0.
\tag{14}
\]

Take any Birkhoff decomposition

\[
R=\sum_{\rho\in S_3}\theta_\rho P_\rho,
\qquad \theta=\theta_{\rho_0}.
\]

Then

\[
\langle R,X\rangle
\le x_0-\gamma(1-\theta).
\tag{15}
\]

Also each selected entry satisfies

\[
r_{\alpha,\rho_0(\alpha)}\ge\theta.
\tag{16}
\]

If `theta>2/3`, Lemma 1 gives positive orientation parity along `rho_0`. Let `W_*` be the unique even-signed `D_3` Weyl permutation with underlying permutation `rho_0` and selected signs `sign(d_{\alpha,\rho_0(\alpha)})`. From (13) and (16),

\[
|d_{\alpha,\rho_0(\alpha)}|\ge\sqrt{2\theta-1}.
\tag{17}
\]

The Hadamard representation sends every `4 x 4` permutation matrix `P_sigma` bijectively to a `3 x 3` Weyl signed-permutation matrix `W_sigma`, and every Birkhoff decomposition

\[
P=\sum_{\sigma\in S_4}\lambda_\sigma P_\sigma
\]

gives

\[
D=\sum_\sigma\lambda_\sigma W_\sigma.
\tag{18}
\]

Let `sigma_*` be the unique lift with `W_{sigma_*}=W_*`. A nonidentity relative `D_3` Weyl element has Frobenius trace at most `1`, while `<W_*,W_*>_F=3`. Therefore

\[
\sum_\alpha|d_{\alpha,\rho_0(\alpha)}|
=\langle D,W_*\rangle_F
\le1+2\lambda_{\sigma_*}.
\tag{19}
\]

Using (17), every Birkhoff decomposition of `P` must satisfy

\[
\boxed{
\lambda_{\sigma_*}\ge
L(\theta):=\frac{3\sqrt{2\theta-1}-1}{2},
\qquad \theta>\frac23.}
\tag{20}
\]

Thus a pair-class transport that puts more than `2/3` Birkhoff mass on one pair permutation forces a quantitatively nonzero amount of the one-point transport onto one of that pair permutation's four genuine `S_4` lifts. This is exactly the synchronization missing from the independent `P`/`R` relaxation.

## 5. Main result — a purely spectral `6 kappa` certificate for the full support inequality

Define the independent-relaxation quantities

\[
c_{\max}=\max_{\sigma\in S_4}c_\sigma,
\qquad x_0=\max_{\rho\in S_3}x_\rho,
\]

\[
M=\max_{\sigma\in S_4}\left(c_\sigma+\frac12x_{\rho_\sigma}\right),
\]

and the finite coupling mismatch

\[
\boxed{
\kappa:=c_{\max}+\frac12x_0-M\ge0.}
\tag{21}
\]

`kappa` is exactly how much the two independent assignment maxima can overestimate the actual 24-vertex support maximum.

### Theorem 2 — pair-gap certificate

Assume the pair assignment `x_rho` has a unique maximizer `rho_0` with gap `gamma` from (14). If

\[
\boxed{\gamma\ge6\kappa,}
\tag{22}
\]

then `(MI)` holds for **every** `4 x 4` unitary `U`. Hence the MOC4 support inequality holds for this spectral pair and this support direction.

#### Proof

Let `theta` be the `rho_0` weight in any Birkhoff decomposition of `R`.

If `theta<=2/3`, (15) gives

\[
\langle R,X\rangle\le x_0-\gamma/3,
\]

while ordinary Birkhoff gives `<P,C><=c_max`. Therefore

\[
\langle P,C\rangle+\frac12\langle R,X\rangle
\le c_{\max}+\frac12x_0-\frac\gamma6
\le c_{\max}+\frac12x_0-\kappa=M.
\tag{23}
\]

Now suppose `theta>2/3`. Use the forced lift `sigma_*` from (20). Since `rho_{sigma_*}=rho_0`, the definition of `M` gives

\[
M\ge c_{\sigma_*}+\frac12x_0.
\]

Together with (21), this implies

\[
c_{\max}-c_{\sigma_*}\ge\kappa.
\tag{24}
\]

Hence every Birkhoff decomposition of `P` obeys

\[
\langle P,C\rangle
\le c_{\max}-\lambda_{\sigma_*}(c_{\max}-c_{\sigma_*})
\le c_{\max}-L(\theta)\kappa.
\tag{25}
\]

Using (15) and `gamma>=6 kappa`, the total loss from the independent assignment upper bound is at least

\[
L(\theta)\kappa+\frac\gamma2(1-\theta)
\ge\kappa\left[L(\theta)+3(1-\theta)\right].
\tag{26}
\]

Set `z=sqrt(2 theta-1)`, so `theta=(z^2+1)/2` and `0<z<=1`. Then

\[
L(\theta)+3(1-\theta)
=1+\frac32z(1-z)\ge1.
\tag{27}
\]

Thus the loss is at least `kappa`, giving `(MI)`. `square`

### Consequence for any hypothetical counterexample

Whenever the pair-class assignment has a unique maximizer, a support-direction counterexample must satisfy the necessary condition

\[
\boxed{\gamma<6\kappa.}
\tag{28}
\]

So the unresolved regime is forced into a near-tie of pair-class assignments relative to the finite mismatch between the independent and common-lift support maxima. This is a strict narrowing of the lead's remaining support search; it does not assume or construct the refuted global common permutation lift.

If `kappa=0`, the mixed inequality is already immediate from independent Birkhoff bounds. If `gamma=0`, Theorem 2 supplies no new information unless `kappa=0`; tied pair fans remain part of the open regime.

## 6. Exact genuinely complex instance where the certificate repairs a failed independent bound

Take

\[
a=(-2+i,-3+3i,3-3i,i),
\]

\[
b=(3+i,-3i,-3+2i,-1-i),\qquad \eta=1.
\]

The exact coefficient matrices are

\[
X=\begin{pmatrix}
0&-48&54\\
0&48&-54\\
120&-82&-84
\end{pmatrix},
\]

\[
C=\frac14\begin{pmatrix}
41&-167&59&-101\\
103&-313&157&-475\\
-545&359&301&413\\
209&-487&251&-173
\end{pmatrix},
\qquad C_0=60.
\]

Exact enumeration gives

\[
x_0=222,\qquad x_1=18,\qquad \gamma=204,
\]

\[
c_{\max}=156,\qquad M=264,\qquad \kappa=3.
\]

Thus the independent assignment relaxation gives

\[
C_0+c_{\max}+\frac12x_0=327,
\]

while the actual 24-vertex support maximum is only

\[
C_0+M=324.
\]

So independent Birkhoff bounds genuinely overshoot the hull by `3`; this is not a trivial `kappa=0` example. The new criterion has

\[
\gamma-6\kappa=186>0,
\]

and therefore rigorously restores the exact support bound `<=324` for **every** unitary `U` for this complex spectral/support instance.

The attached standard-library exact verifier reconstructs all 24 OM endpoints directly over Gaussian integers, checks the `C,X` endpoint identity, obtains the values above without floating-point arithmetic, verifies the 24-element Hadamard/Weyl representation, and checks that the largest nonidentity relative Weyl Frobenius trace is `1`.

## 7. Relation to the lead's Drury upper-facet route

The lead's current `MOC4-DRURY-UPPER-FACET-v1` removes `U` entirely if all 288 exceptional spectral upper-facet inequalities can be proved. The present theorem does **not** claim those 288 inequalities and therefore does not close the lead's first unpaid arrow.

It does, however, prove the same determinant support conclusion on the explicit spectral region `gamma>=6 kappa`, using the complementary-minor structure that this B09 slot is assigned to exploit. Consequently a future failure of the Drury upper-facet sufficient condition in that region would not itself be a determinant-hull counterexample; and any actual MOC4 support counterexample with a unique pair-class optimizer must live in the narrower `gamma<6 kappa` region.

This is compatible with the named partner's `SO(6)` picture: Lemma 1 is a quantitative separation between the two connected components of `O(6)`, while (20) converts that topological orientation information into forced `S_4` lift mass in the one-minor transport.

## 8. Remaining obligation and next recipient

**MOC4 remains open.** The next exact mathematical target is the complementary near-tie regime

\[
0\le\gamma<6\kappa,
\]

including tied pair-class maxima. Two concrete next attacks are now natural:

1. sharpen Lemma 1 from the component-separation threshold into a continuous loss bound involving the actual selected `d` magnitudes and pair-assignment slack; or
2. combine the lead's Drury exceptional-facet factorization with the `SO(6)` stationarity/Hessian conditions on this now-restricted near-tie locus.

Recommended recipients: campaign lead account03/B07, named partner account04/B07, account04/B08, account02/B09, and account03/B20.

No benchmark gold, answers, keys, credentials, scheduler identifiers, machine paths, unrelated private material, email, Drive, public posting, paid model/API/Codex execution, or remote workflow is used or stored.
