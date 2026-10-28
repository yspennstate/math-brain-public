SIGNED IN - working on the quadratic-form bounded-density conjecture (universal constant), account account03, slot B11, 2026-09-23T22:12:15Z.
attacking: the finite-heavy-row punctured receiver: prove that two heavy physical rows are already paid by partner pair-area, then reduce the unique-heavy-row survivor to either a scalar pivot, one strong physical edge, or two disjoint diffuse star banks.

# account03/B11 r43 — finite-heavy-row collar to unique hub + scalar/edge/two-star trichotomy

Status: **NEW STRUCTURAL REDUCTION / DESIGNATED PARTNER APPLIED / FULL QFORM OPEN**.
Execution: `WITHOUT_VERIFIED_BRAIN`.
Regularity: the partner pair-area and scalar/pair-log exits below establish essential boundedness in their stated branches. No new continuity theorem is claimed here. The full conjecture and full-target continuity remain open.

The owner target is unchanged: independent original coordinates with densities at most one, arbitrary real symmetric `A`, and at least three eigenvalues of absolute value at least one. No post-rotation independence, Gaussian/log-concave/moment/support hypothesis, law-uniform pointwise van-der-Corput decay, arbitrary-joint coarea, conditional-density cap, fiber-supremum, or deletion of a small nonzero quadratic term is used.

## 1. Source-pinned inherited hard chamber

Use the exact-rank-three indefinite factorization

\[
A=RMR^T,\qquad R^TR=I_3,\qquad s:=\min_a|\lambda_a(M)|\ge1,
\]
with signature `(2,1)` or `(1,2)`.

From account03/B11 r41 (`yspennstate/math-open-problems@7120df98e7d30de603f45a8823fb02d25564f218`), the true-near-coloop construction supplies a literal original-coordinate bank `H` for which

\[
\Gamma_H:=R_H^TR_H,\qquad
\lambda_{\min}(\Gamma_H)>\beta_0,
\qquad
\beta_0:=\frac{289}{15984}=0.01808058058058\ldots .
\tag{1.1}
\]

Choose any orthonormal basis `E` of `range(R_H)`. Then there is an invertible `K` with

\[
R_H=EK,\qquad K^TK=\Gamma_H.
\tag{1.2}
\]

Write

\[
C:=E^TA[H,H]E=KMK^T.
\tag{1.3}
\]
Consequently

\[
\sigma_{\min}(C)>\beta_0s.
\tag{1.4}
\]

For each physical coordinate `i in H`, put

\[
z_i:=E^Te_i,\qquad q_i:=\|z_i\|^2.
\tag{1.5}
\]
Thus `P:=EE^T` is an orthogonal projection, `P_ii=q_i`, and `sum_i q_i=3`.

From account03/B11 r42 (`yspennstate/math-open-problems@8207aee23be9554e960f48d82c2e706eacc50c04`), in the only branch not already paid by aggregate physical third-volume one has

\[
J:=\{i\in H:q_i>3/4\},\qquad 1\le |J|\le3,
\tag{1.6}
\]

and, with the r42 internal-curvature coefficients

\[
b_i:=h\cdot z_i,
\tag{1.7}
\]

\[
\sum_{i\in J}b_i^2>\frac{\beta_0^2}{2}s^2.
\tag{1.8}
\]

The present run sharpens this finite-heavy-row survivor.

The mandatory rank-two control remains: for independent centered unit uniforms,

\[
p_{2XY}(t)=\log\frac1{2|t|},\qquad 0<|t|<1/2.
\tag{1.9}
\]
Hence any full argument must supply a genuine third smoothing resource.

## 2. Two heavy rows are already paid by the designated account04/B11 pair-area theorem

The completed designated-partner result account04/B11 r6 is

`yspennstate/math-open-problems@30555c1ca97752e10f5089ccd95f8514c704be5a`

at

`proofnet24/QFORM-density/fleet-2026-09-22/account04/B11/20260923T131400Z-account04-B11-extension-mass-r6/REPORT.md`.

It gives, for every physical pair `{i,j}` of the rank-three spectral frame,

\[
\boxed{
\|p_Q\|_\infty\le\frac{128\sqrt2}{s\sqrt{g_{ij}}},
\qquad
 g_{ij}:=\|r_i\wedge r_j\|^2.
}
\tag{2.1}
\]

### Lemma `QFORM-TWO-HEAVY-E-ROWS-PAY-PAIRAREA-v1`

If `q_i>3/4` and `q_j>3/4` for distinct physical rows `i,j in H`, then

\[
\boxed{g_{ij}>\frac{\beta_0^2}{2}.}
\tag{2.2}
\]

Therefore the partner theorem gives the actual full-line bound

\[
\boxed{
\|p_Q\|_\infty<\frac{256}{\beta_0s}
=\frac{14158.83737025\ldots}{s}.
}
\tag{2.3}
\]

#### Proof

Because `P=EE^T` is an orthogonal projection, `I-P` is positive semidefinite. Its `2x2` principal minor on `{i,j}` gives

\[
|z_i\cdot z_j|^2=|P_{ij}|^2
\le(1-q_i)(1-q_j)<\frac1{16}.
\tag{2.4}
\]

Hence the squared Euclidean exterior area in the `E` coordinates obeys

\[
\|z_i\wedge z_j\|^2
=q_iq_j-(z_i\cdot z_j)^2
>\frac9{16}-\frac1{16}
=\frac12.
\tag{2.5}
\]

By (1.2), the physical spectral rows are `r_i=z_i^TK` and `r_j=z_j^TK`. The least singular value of `K` is `sqrt(lambda_min(Gamma_H))>sqrt(beta_0)`. On exterior two-vectors, `K` therefore expands area by at least `sigma_min(K)^2>beta_0`. Thus

\[
\|r_i\wedge r_j\|
>\beta_0\|z_i\wedge z_j\|,
\]
which yields (2.2). Substitution into the completed partner inequality (2.1) proves (2.3). QED.

### Consequence: the hard branch has exactly one heavy row

If the partner exit (2.3) has not fired, then the r42 set `J` contains exactly one coordinate, say `i_*`. Combining this with (1.8),

\[
\boxed{
q_{i_*}>\frac34,
\qquad
|b_{i_*}|>\frac{\beta_0}{\sqrt2}s
=0.0127849011363\ldots\,s.
}
\tag{2.6}
\]

This improves the r42 coefficient `beta_0/sqrt(6)` by a factor `sqrt(3)` in the genuine surviving branch.

## 3. A unique heavy row either has a paid scalar pivot or a robust physical self-star

Fix the unique heavy row `i=i_*`, write

\[
z:=z_i,\quad q:=\|z\|^2>3/4,
\quad v:=Cz,
\quad a:=A_{ii}=z^TCz.
\tag{3.1}
\]

Let

\[
c:=A[H\setminus\{i\},\{i\}]=E_{-i}Cz=E_{-i}v
\tag{3.2}
\]

be the physical off-diagonal self-star of row `i` within the original-coordinate bank `H`.

The exact identity

\[
E_{-i}^TE_{-i}=I_3-zz^T
\tag{3.3}
\]
gives

\[
\boxed{
\|c\|_2^2
=v^T(I_3-zz^T)v
=\|v\|_2^2-a^2.
}
\tag{3.4}
\]

Since (1.4) and `q>3/4` imply

\[
\|v\|_2=\|Cz\|_2>\beta_0s\sqrt q
>\frac{\sqrt3}{2}\beta_0s,
\tag{3.5}
\]
we obtain a quantitative pivot/star dichotomy.

### Theorem `QFORM-UNIQUE-HEAVYROW-PIVOT-OR-STAR-v1`

Define

\[
a_0:=\frac{\beta_0}{16},
\qquad
\eta_0:=\frac{\sqrt{191}}{16}\beta_0
=0.0156174121925\ldots .
\tag{3.6}
\]

Then either

\[
|A_{ii}|\ge a_0s,
\tag{3.7}
\]

or

\[
\boxed{
\sum_{j\in H\setminus\{i\}}A_{ij}^2
=\|c\|_2^2
>\eta_0^2s^2.
}
\tag{3.8}
\]

#### Proof

If (3.7) fails, then `a^2<(beta_0^2/256)s^2`. Combining with (3.4)--(3.5),

\[
\|c\|_2^2
>\left(\frac34-\frac1{256}\right)\beta_0^2s^2
=\frac{191}{256}\beta_0^2s^2
=\eta_0^2s^2.
\]
QED.

### The scalar-pivot branch is already bounded

For the full exact-rank-three form, the completed orientation-free scalar-pivot theorem `QFORM-RANK3-ALL-RESIDUAL-ORIENTATIONS-v1` from

`yspennstate/math-open-problems@e542b1a6ef471b329e4e88a6553e1aacb45acc1a:proofnet24/QFORM-density/interactive/20260922T161801Z-rank-two-fusion/REPORT.md`

states

\[
\|p_Q\|_\infty
\le128[c_i|A_{ii}||\det M|]^{-1/4},
\qquad c_i:=\|r_i\|^2.
\tag{3.9}
\]

Here `r_i=z_i^TK`, so

\[
c_i\ge\lambda_{\min}(\Gamma_H)q
>\frac34\beta_0.
\tag{3.10}
\]

Using `|det M|>=s^3` and (3.7),

\[
\boxed{
\|p_Q\|_\infty
<128\left(\frac{64}{3\beta_0^2}\right)^{1/4}\frac1s
=\frac{2045.825\ldots}{s}.
}
\tag{3.11}
\]

Thus the only new survivor of Section 3 is the robust-star branch (3.8).

## 4. A strong individual star edge is also already paid

Continue in the robust-star branch and define

\[
\theta_0:=\frac{\eta_0}{2}
=\frac{\sqrt{191}}{32}\beta_0
=0.00780870609624\ldots .
\tag{4.1}
\]

Suppose for some `j!=i`,

\[
|A_{ij}|\ge\theta_0s.
\tag{4.2}
\]

We show that this branch is already uniformly bounded using only completed exact-rank-three receivers.

Scale `A` by `1/s`; density scales back by `1/s`, so it is enough to take `s=1`. In the current robust-star branch, Section 3 also has

\[
|A_{ii}|<\beta_0/16<\theta_0/4.
\tag{4.3}
\]

Put

\[
B=\begin{pmatrix}A_{ii}&A_{ij}\\A_{ij}&A_{jj}\end{pmatrix}.
\]

There are two cases.

### 4A. The second diagonal is not tiny

If

\[
|A_{jj}|\ge\theta_0/4,
\]
then the full exact-rank-three scalar-pivot corollary from the same completed theorem gives

\[
\|p_Q\|_\infty\le128|A_{jj}|^{-1/2}
\le\frac{256}{\sqrt{\theta_0}}.
\tag{4.4}
\]

After restoring scale,

\[
\boxed{
\|p_Q\|_\infty<\frac{2897.013}{s}.
}
\tag{4.5}
\]

### 4B. Both physical diagonals are tiny

If instead `|A_jj|<theta_0/4`, then (4.2)--(4.3) give

\[
|\det B|
=|A_{ii}A_{jj}-A_{ij}^2|
>\frac{15}{16}\theta_0^2,
\tag{4.6}
\]
while Weyl's inequality relative to
`[[0,A_ij],[A_ij,0]]` gives

\[
\sigma_{\min}(B)>|A_{ij}|-\theta_0/4
\ge\frac34\theta_0.
\tag{4.7}
\]

Apply the completed exact-rank-three pair-log theorem `QFORM-PAIR-LOG` from

`yspennstate/math-open-problems@f7f0fedb2d93b46824f96cac1164af6f8a55626f:proofnet24/QFORM-density/interactive/20260922T180015Z-pair-log/PAIR_LOG_THEOREM.md`,

\[
\|p_Q\|_\infty
\le8\sqrt5\,(|\det B|\,\sigma_{\min}(B)\,s)^{-1/4}.
\tag{4.8}
\]

For normalized `s=1`, (4.6)--(4.7) yield

\[
\|p_Q\|_\infty
<8\sqrt5\left(\frac{45}{64}\theta_0^3\right)^{-1/4}
=743.674\ldots .
\]
Restoring scale gives

\[
\boxed{\|p_Q\|_\infty<743.674/s.}
\tag{4.9}
\]

Therefore every strong individual edge (4.2) is paid, with the uniform combined bound

\[
\boxed{\|p_Q\|_\infty<2897.013/s.}
\tag{4.10}
\]

## 5. The genuine finite-heavy-row survivor is now a two-bank diffuse star

Assume none of the paid exits above fires. Then the unique heavy row `i` satisfies

\[
\sum_{j\ne i}A_{ij}^2>\eta_0^2s^2,
\qquad
|A_{ij}|<\theta_0s=\frac{\eta_0}{2}s
\quad\text{for every }j\ne i.
\tag{5.1}
\]

Let

\[
S_*:=\sum_{j\ne i}A_{ij}^2.
\]
Since every squared edge is `<theta_0^2s^2=eta_0^2s^2/4<=S_*/4`, a deterministic greedy partition of the ORIGINAL coordinates `H\setminus\{i\}` into two disjoint banks `B_1,B_2` gives

\[
\boxed{
\sum_{j\in B_1}A_{ij}^2\ge\frac{S_*}{4},
\qquad
\sum_{j\in B_2}A_{ij}^2\ge\frac{S_*}{4}.
}
\tag{5.2}
\]

Indeed, add coordinates to `B_1` until its accumulated squared star mass first reaches `S_*/4`. Immediately before the last addition it is below `S_*/4`, and the added term is at most `S_*/4`, so the resulting mass is below `S_*/2`; the complement therefore has more than `S_*/2`.

Using (5.1), each bank therefore carries the explicit physical star energy

\[
\boxed{
\sum_{j\in B_r}A_{ij}^2
>\frac{\eta_0^2}{4}s^2
=\theta_0^2s^2,
\qquad r=1,2.
}
\tag{5.3}
\]

The banks are literal disjoint sets of original independent coordinates; no random-variable rotation is performed.

This is a genuine reduction of the r42 finite-row collar. The difficult state is no longer "up to three heavy physical rows". It is now one physical row with

1. `q_i>3/4`;
2. a nontrivial internal-curvature coefficient `|b_i|>beta_0 s/sqrt2`;
3. a tiny physical scalar pivot `|A_ii|<beta_0 s/16`;
4. no large physical star edge `|A_ij|>=theta_0 s`;
5. two disjoint original-coordinate banks, each carrying star `l2` energy `>theta_0^2s^2`.

This is the first unpaid B11 interface after r43.

## 6. Why this is the correct third-direction picture

The rank-two opposite-sign model (1.9) shows that one hyperbolic pair alone leaves a logarithmic density singularity. In the punctured collar the two strong crossing directions from r40 still generate precisely that endpoint. The r41/r42 mechanism shows the third curvature cannot vanish; r43 now shows more:

- if that curvature is represented by two physical heavy rows, the designated partner pair-area theorem immediately pays it;
- if it appears as a physical scalar pivot, the orientation-free scalar Schur receiver pays it;
- if it appears on one physical edge, either a second scalar pivot or the exact-rank-three pair-log receiver pays it;
- therefore a genuinely unresolved third direction must be **collective**: one near-coloop physical row couples weakly to each coordinate separately but with fixed total energy in two disjoint source banks.

That is a product-provenance statement. It rules out trying to close the finite-heavy-row collar by another reciprocal tiny minor.

The statement is invariant under `M -> -M`, so signatures `(2,1)` and `(1,2)` are treated symmetrically.

## 7. Remaining implication

The full conjecture remains OPEN. The next exact B11 implication is

`QFORM-UNIQUE-HEAVYROW-TWOSTAR-LINEAR-SMALLBALL-v1`:

> In the exact-rank-three punctured collar, assume one physical row `i` satisfies the five properties in Section 5. Use the two disjoint original-coordinate star banks together with the already-paid rank-two crossing to prove `P(Q in I)<=C|I|` uniformly, while retaining every same-bank and cross-bank quadratic coefficient. Do not condition in a way that replaces a product law by an unbounded conditional density, and do not treat the small third shear as a random perturbation.

A promising mechanism is a joint two-bank decoupling in which the two star slopes are kept before absolute values are taken; the r40 fragmented-support counterexample rules out a mere `L^1_W(L^2_v)` slice estimate.

Even a closure of this exact-rank-three successor would still leave the owner's arbitrary-additional-nonseparable-spectrum bridge. Full-target continuity remains open.

## 8. Verification and source state

The deterministic identities used here were checked numerically on random orthonormal frames: for every tested pair of rows with `q_i,q_j>3/4`, the `E`-frame squared area exceeded `1/2` (minimum observed `0.503304...` over 65,978 tested heavy pairs), and the identity

\[
\|E_{-i}Cz_i\|^2=\|Cz_i\|^2-(z_i^TCz_i)^2
\]

had maximum floating error `1.56e-15` over the test set. These computations only check algebra already proved above; no numerical experiment is used as evidence for the universal density claim.


No scheduler/task-state change, email, notification, public release, paid API/model, Codex call, installation, credential/permission expansion, remote workflow, unrelated-data access, or cross-account authentication was performed.
