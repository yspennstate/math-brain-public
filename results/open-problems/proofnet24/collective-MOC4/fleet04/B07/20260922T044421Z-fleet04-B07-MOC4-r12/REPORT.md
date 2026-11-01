# MOC4 fleet04/B07 — spinor singular-value equality and determinant hexagon constraints

**Directive:** `COLLECTIVE-OPEN-PROBLEMS-20260921T234023Z`  
**Campaign:** complex-normal `4 x 4` Marcus-de Oliveira target  
**Worker/run:** fleet04/B07, `20260922T044421Z-fleet04-B07-MOC4-r12`  
**Assignment:** representation-theoretic / exterior-algebra proof of the shared mixed-minor constraint  
**Outcome:** `ESSENTIAL_STEP_APPLIED`; full MOC4 remains **OPEN / NOT PROVED / NOT DISPROVED**.  
**Execution:** `WITHOUT_VERIFIED_BRAIN`.

## 1. Exact state consumed

The target is

\[
\det(A+B)\in\operatorname{conv}\left\{
\prod_{i=1}^4(a_i+b_{\sigma(i)}):\sigma\in S_4
\right\}
\]

for every complex normal `4 x 4` pair, including singular and repeated spectra.

I used the newest complete campaign-lead report available at the start of this run: **fleet03/B07**, `fleet03-B07-20260922T033411Z-d2a63b2a`, report blob `28cbce0f0a6213c0760e0777a5baa5b0de12b31a`, theorem `MOC4-V4-PAIR-GAP-CEILING-v1`. It proves that every genuine support violation `h(U)=M+gamma` satisfies

\[
0<\gamma\le {3d-\Delta-G/2\over4},
\]

and its exact half-unit relaxation witness proves that V4/pair roofs and the low-frequency `S_4` identities alone cannot close the remaining branch.

The required named OTHER-account partner used here is **fleet01/B08**, newest complete run `20260922T040837Z-b08-moc4-r11`, report blob `a7037897419b3ee297e98a3b063e925c5cf312da` and stability addendum blob `8145b24919c544a39e03d086b95ff1804edf513e`. Its `MOC4-CHAIN-CUBE-FACE-PROPAGATION-v1` shows that an exact eleven-vertex bad face forces all eight signed spectral points onto one generalized circle, where MOC is already solved; its addendum proves the quantitative cross-ratio phase estimate

\[
|\sin\arg(E/F)|\le {|L(E)|\over |E|}+{|L(F)|\over |F|}.
\]

Thus a surviving generic obstruction must be transverse to that solved face, not another low-frequency face witness. I retain this branch split below.

Two further exact dependencies are essential. **fleet03/B09**, report blob `06b56b516f3d36c9fa1e11601e775771fcf7e285`, proved

\[
D={1\over4}E^TPE,\qquad P=(|u_{ij}|^2),
\tag{1}
\]

for the oriented complementary-minor channel. **fleet04/B09**, run `20260922T041453Z-b09-moc4-r34`, report blob `faaf77b4fcebb8fed6a6c9763251acc1042105ac`, then used the same unistochastic `P` to prove the standard-channel ceiling `k(U)<=K_std`, closing the campaign lead's exact `1/2` stress direction.

My immediately preceding run, report blob `389128e16daba449a4364c3c5c71a70f5767444c`, wrote the real exterior-square action as a Bogoliubov map and proved `rank N<=2` plus sixteen parity-mask mass inequalities. The present run derives the exact equality hidden behind those inequalities and, more importantly, keeps the complex determinant cancellation that the mass relaxation discarded.

## 2. Exterior-square Bogoliubov coordinates

Identify the real six-dimensional exterior-square representation with `C^3`. For

\[
O=\Lambda^2U\in SO(6)
\]

write the corresponding real-linear isometry as

\[
T(z)=Mz+N\bar z,\qquad M,N\in M_3(\mathbb C).
\tag{2}
\]

Orthogonality is equivalent to

\[
MM^*+NN^*=I,\qquad MN^T+NM^T=0.
\tag{3}
\]

For each scalar `2 x 2` block put

\[
q^+_{\alpha\beta}=|m_{\alpha\beta}|^2,
\qquad
q^-_{\alpha\beta}=|n_{\alpha\beta}|^2,
\tag{4}
\]

so that

\[
R=q^++q^-,\qquad D=q^+-q^-.
\tag{5}
\]

The matrix `R` is doubly stochastic and hence `sum_{alpha,beta}R_{alpha beta}=3`.

For an even bit vector `r in {000,011,101,110}`, let `C_r` conjugate the corresponding complex output coordinates, and similarly let `C_c` act on inputs. Because `r,c` have even Hamming parity, both real maps lie in `SO(6)`. Write

\[
T_{r,c}=C_rTC_c=M_{r,c}z+N_{r,c}\bar z.
\tag{6}
\]

Entrywise, the anti-linear squared modulus is

\[
|(N_{r,c})_{\alpha\beta}|^2=
\begin{cases}
q^-_{\alpha\beta},&r_\alpha\oplus c_\beta=0,\\
q^+_{\alpha\beta},&r_\alpha\oplus c_\beta=1.
\end{cases}
\tag{7}
\]

Define its total mass

\[
L_{r,c}:=\|N_{r,c}\|_F^2.
\tag{8}
\]

## 3. New theorem — exact spinor singular-value identity

### Theorem 1 — `MOC4-SPINOR-SINGULAR-VALUE-v1`

For every real-linear orientation-preserving isometry `(2)`,

\[
\boxed{
\det N=0,
\qquad
|\det M|+{1\over2}\|N\|_F^2=1,
\qquad
\|\operatorname{adj}N\|_F^2=\left({\|N\|_F^2\over2}\right)^2.
}
\tag{9}
\]

The same three identities hold for every even-even gauge `(r,c)`.

### Proof

First assume `M` is invertible and put

\[
Z=M^{-1}N.
\]

The second relation in `(3)` gives

\[
Z^T=-Z.
\tag{10}
\]

Because `Z` is a `3 x 3` complex skew-symmetric matrix, choose a unit vector in its kernel and extend it to a unitary basis. Under the resulting unitary congruence, the last row and column vanish and the remaining `2 x 2` skew block has the form

\[
\begin{pmatrix}0&s\\-s&0\end{pmatrix}
\]

after an irrelevant phase adjustment, with `s>=0`. Thus the singular values of `Z` are exactly `(s,s,0)`.

Using `N=MZ`, the first relation in `(3)` becomes

\[
M(I+ZZ^*)M^*=I.
\tag{11}
\]

Hence the singular values of `M` are

\[
1,\quad (1+s^2)^{-1/2},\quad (1+s^2)^{-1/2}.
\]

Therefore

\[
|\det M|={1\over1+s^2}.
\tag{12}
\]

Also `NN^*=I-MM^*`, so the singular values of `N` are

\[
0,\quad {s\over\sqrt{1+s^2}},\quad {s\over\sqrt{1+s^2}}.
\]

Consequently

\[
{1\over2}\|N\|_F^2={s^2\over1+s^2}=1-|\det M|,
\]

which is the middle identity in `(9)`. The nonzero singular value of `adj N` is the product of the two nonzero singular values of `N`, namely `s^2/(1+s^2)`, proving the final identity.

The set `det M !=0` is dense: `det M` is real-analytic on connected `SO(6)` and is nonzero at the identity, so it cannot vanish on an open set. All three formulas extend by continuity. Applying the same argument to the orientation-preserving gauge transform `C_rTC_c` proves the statement for all sixteen even-even gauges. `QED`

The previous inequality `L_{r,c}<=2` is therefore only the nonnegativity consequence of a stronger exact equality:

\[
\boxed{|\det M_{r,c}|=1-{L_{r,c}\over2}.}
\tag{13}
\]

## 4. The sixteen parity-mask slacks are exactly the entries of P

This is where the new equality meets the campaign's exact same-unitary identity `(1)`.

Let

\[
E=\begin{pmatrix}
1&1&1\\
1&-1&-1\\
-1&1&-1\\
-1&-1&1
\end{pmatrix}.
\tag{14}
\]

The four even bit vectors correspond, through `s(r)_alpha=(-1)^{r_alpha}`, to the four rows of `E`; denote the corresponding row index by `iota(r)`.

From `(7)` and `(5)`,

\[
L_{r,c}={1\over2}\sum_{\alpha,\beta}
\left(R_{\alpha\beta}-s(r)_\alpha s(c)_\beta D_{\alpha\beta}\right)
={3-s(r)^TDs(c)\over2}.
\tag{15}
\]

Using `(1)`, double stochasticity of `P`, and the tetrahedral identities for the rows of `E`, one gets exactly

\[
s(r)^TDs(c)=4P_{\iota(r),\iota(c)}-1.
\tag{16}
\]

Substituting into `(15)` gives

\[
\boxed{
L_{r,c}=2\left(1-P_{\iota(r),\iota(c)}\right).
}
\tag{17}
\]

Combining `(13)` and `(17)` yields the exact spinor reconstruction

\[
\boxed{
|\det M_{r,c}|=P_{\iota(r),\iota(c)},
\qquad
\|\operatorname{adj}N_{r,c}\|_F=1-P_{\iota(r),\iota(c)}.
}
\tag{18}
\]

This changes how the preceding parity-mask result should be interpreted. Once the exact campaign identity `D=(1/4)E^TPE` is imposed, the sixteen **mass inequalities** `L_{r,c}<=2` are precisely the already-required entrywise inequalities `P_ij>=0`; they are not sixteen independent hidden sources of target slack. Their usefulness in an outer `q`-relaxation came from reconstructing this missing `P` positivity. A future proof should therefore not repeatedly count the mass masks as additional common-unitary payment on top of the same `P` constraint.

The genuinely extra information from the spinor rank condition is phase-sensitive and appears next.

## 5. New determinant-hexagon constraints

For every even-even gauge, Theorem 1 gives the exact complex equation

\[
\boxed{
\det N_{r,c}=
\sum_{\rho\in S_3}\operatorname{sgn}(\rho)
\prod_{\alpha=1}^3 (N_{r,c})_{\alpha,\rho(\alpha)}=0.
}
\tag{19}
\]

This is a six-term complex closure linking six signed matchings inside one **actual** exterior-square point. It is not a positivity representation and does not replace the common unitary by independent transport data.

Taking the modulus of one term against the other five gives 96 explicit necessary inequalities. If

\[
w^{r,c}_\rho:=
\prod_{\alpha=1}^3 |(N_{r,c})_{\alpha,\rho(\alpha)}|
=\sqrt{
\prod_{\alpha=1}^3
q^{\chi_{r,c}(\alpha,\rho(\alpha))}_{\alpha,\rho(\alpha)}},
\tag{20}
\]

where `chi` selects `-` for XOR zero and `+` for XOR one, then for every `r,c,rho`

\[
\boxed{
 w^{r,c}_\rho\le
 \sum_{\sigma\ne\rho}w^{r,c}_\sigma.
}
\tag{21}
\]

Because the selected channel pattern along any such matching has odd orientation parity, `(21)` is a six-matching phase-closure constraint precisely in the dangerous odd-orientation sector.

There is also a quantitative leakage form. Relabel a chosen matching to the diagonal and put

\[
x_i=|(N_{r,c})_{ii}|^2,
\qquad
E_{\rm off}:=\sum_{i\ne j}|(N_{r,c})_{ij}|^2.
\]

The three transposition terms in `(19)` obey `sqrt(ab)<= (a+b)/2`, while the two directed 3-cycle products obey AM-GM. Therefore

\[
\boxed{
\sqrt{x_1x_2x_3}
\le {E_{\rm off}\over2}
+{E_{\rm off}^{3/2}\over3\sqrt3}.
}
\tag{22}
\]

Using `(17)`,

\[
E_{\rm off}=2(1-P_{\iota(r),\iota(c)})-(x_1+x_2+x_3),
\tag{23}
\]

so `(22)` is an explicit nonlinear **P/R mixed-minor payment**: large mass on one odd signed matching forces off-matching anti-linear mass in the same gauge, with the available total itself fixed by the same unistochastic entry `P_ij`.

This is the first output of this line that cannot be reduced merely to `P_ij>=0`.

## 6. Exact regression on the assigned partner's true unitary

The committed verifier uses the exact rational true-unitary datum from the assigned partner fleet01/B08 run `20260922T024227Z-fleet01-B08-MOC4-r12`, the same datum used in my preceding parity-mask report. It reconstructs `O=Lambda^2 U`, all Bogoliubov blocks, and all sixteen even-even gauges with `Fraction` arithmetic.

It verifies exactly:

- all sixteen `det N_{r,c}=0`;
- all sixteen reconstructions `1-L_{r,c}/2=P_{iota(r),iota(c)}`;
- all sixteen `|det M_{r,c}|^2=P_{ij}^2`;
- all sixteen cofactor identities `||adj N_{r,c}||_F^2=(L_{r,c}/2)^2`.

For the gauge `r=c=011`, which was the tightest parity mask in the previous run,

\[
L_{011,011}={60830802\over30525625},
\]

and the exact slack is

\[
1-{L_{011,011}\over2}
={110224\over30525625}
=|u_{22}|^2.
\tag{24}
\]

The six determinant terms are individually nonzero on this sample, but their signed complex sum is exactly zero, not merely numerically small. The captured verifier output records every exact rational term.

As a simple negative control showing why the phase closure cannot be replaced by mass accounting alone, take `P=J_4/4`, `D=0`, and

\[
R_{ii}=8/9,\qquad R_{ij}=1/18\ (i\ne j),\qquad q^+=q^-=R/2.
\]

Then `P` is genuinely unistochastic (the normalized `4 x 4` Fourier matrix has these moduli), `D=(1/4)E^TPE=0`, every parity-mask mass is `3/2`, and every old odd-Weyl three-cell overlap is at most `2`. Yet in the base gauge the diagonal determinant term of `N` has modulus `(4/9)^{3/2}=8/27`, whereas the five other determinant terms have total modulus strictly smaller, so `(19)` cannot hold. This point is therefore **not** an actual linked exterior-square datum. It is not an MOC4 counterexample. It only proves that the P/mass/odd-overlap relaxation still misses phase information. (It also violates previously known Pluecker-triangle constraints, so no independence claim from the full Pluecker system is made.)

## 7. Application of the newest partner result and updated conditional chain

The partner's newest chain-cube theorem removes the exact bad-face limit: in the generic simple/nonzero-sum branch, if its eleven endpoint deficits vanish then the signed spectra lie on one generalized circle and the full normal-matrix problem is already solved. Its addendum says that if those deficits are merely small, the five cross-ratio phase defects are quantitatively small relative to the ten relevant spectral edge magnitudes.

The present theorem supplies the corresponding **unitary-side phase closure** that was absent from the mass relaxation. Thus any remaining generic positive-gap maximizer must simultaneously satisfy:

1. the lead's V4/pair reserve ceiling;
2. fleet04/B09's exact standard-channel ceiling from the same unistochastic `P`;
3. `D=(1/4)E^TPE` and the existing Pluecker/bi-orientation conditions;
4. the partner's five spectral cross-ratio phase controls away from the solved exact face;
5. all sixteen exact complex spinor equations `(19)`, or at minimum the 96 hexagon inequalities `(21)` and leakage bounds `(22)`.

This is a genuinely smaller residual than one based on parity-mask masses: `(17)` shows those masses alone were only `P>=0`, while `(19)` retains the phase cancellation that a true `Lambda^2U` must carry.

A compact conditional end-to-end deduction is now:

- boundary/common-circle and exact chain-cube face branches close by the existing source-valid reductions and the assigned partner theorem;
- if `K_std=Delta`, fleet04/B09 closes the support direction for all true unitaries;
- otherwise a hypothetical global maximizer lies in the positive reserve and must satisfy the complete list above;
- if one proves that the structured rank-one `R` coefficient cannot obtain positive residual support under `(19)` together with the partner's transverse spectral phase controls, then every support direction is endpoint-bounded, hence MOC4 follows; singular/repeated cases remain included through the established polynomial/boundary reductions.

The **first essential missing implication** for this representation route is therefore concrete rather than another positivity hypothesis:

> On the residual positive-reserve branch, use the determinant closure `(19)` (equivalently its matching leakage `(22)` plus the existing phase information) to show that any concentration of the symmetric quotient `R` on a support-favored assignment pays enough off-matching mass to cancel the remaining `K_std-Delta` / V4-pair reserve. If this is false, produce actual spectra, one support direction, and one true unitary satisfying all displayed same-unitary and transverse-face conditions; an independent `(P,R)` or arbitrary `SO(6)` coefficient normal does not count.

No claim of full proof is made.

## 8. Verification and scope

`verify_spinor_hexagon.py` uses only standard-library `fractions.Fraction`. Its observed exact output is saved as `VERIFICATION.txt`. The mathematical proof of `(9)`-`(23)` is exact and does not divide by spectral differences or eigenvalues, so these mixed-minor identities themselves have no singular/repeated-spectrum exception.

Scoped privacy/provenance review found only campaign mathematics, logical worker labels, public mathematical formulas, and source hashes already present in the authorized private research archive. No benchmark gold, answer keys, credentials, scheduler identifiers, machine-local paths, unrelated private data, email/Drive material, paid model/API/Codex call, remote workflow, permission change, or public release was used.

**Status:** `ESSENTIAL_STEP_APPLIED`. Full MOC4 remains **OPEN**.
