# R19 screening artifact — D0029 non-B-convex beta branch

Date: 2026-09-18 UTC  
Repository / branch: `yspennstate/math-open-problems` / `master`  
Status: **screening theorem only / no ownership claim / no novelty claim**

## 1. Source being screened

Candidate `D0029` is Richard C. Bradley, *Basic Properties of Strong Mixing Conditions. A Survey and Some Open Questions* (2005), Question 1 in Section 1.2. For a nontrivial real Banach space `B`, Bradley defines

\[
R^B_{\infty,\infty}(\mathcal A,\mathcal C)
=\sup\frac{\left|E\langle X,Y\rangle-\langle EX,EY\rangle\right|}
{\|\|X\|_B\|_\infty\,\|\|Y\|_{B^*}\|_\infty},
\]

where the supremum is over simple `B`-valued `\mathcal A`-measurable `X` and simple `B^*`-valued `\mathcal C`-measurable `Y`. The source asks whether, for every `B`, this dependence coefficient is equivalent (in the vanishing sense) to either `alpha` or `beta`. The source records Hilbert spaces on the `alpha` side and `l_1`, `l_infinity`, `c_0` on the `beta` side.

The intake already contains an earlier attempt `D0029-A001` proposing B-convexity as the natural dividing line. The result below closes one direction of that proposed split exactly, but it does **not** close Bradley's source question.

## 2. Finite-partition matrix form

Fix finite partitions `A_1,...,A_I` in `\mathcal A` and `C_1,...,C_J` in `\mathcal C`, and put

\[
d_{ij}=P(A_i\cap C_j)-P(A_i)P(C_j).
\]

Then `D=(d_ij)` has zero row and column sums. For simple random variables

\[
X=\sum_i x_i 1_{A_i},\qquad Y=\sum_j y_j1_{C_j},
\]

with `\|x_i\|_B\le1` and `\|y_j\|_{B^*}\le1`, the centered covariance is exactly

\[
\sum_{i,j} d_{ij}\langle x_i,y_j\rangle.
\]

Thus the partition-level coefficient is the amplification norm

\[
R_B(D)
=\sup_{\|x_i\|\le1,\,\|y_j\|\le1}
\left|\sum_{i,j}d_{ij}\langle x_i,y_j\rangle\right|
=\|D\otimes I_{B^*}\|_{\ell_\infty^J(B^*)\to\ell_1^I(B^*)}.
\]

For scalar `B`, zero row/column sums identify the corresponding sign/cut norm with the `alpha` endpoint (up to the conventional factor); the entrywise `l_1` norm `\sum|d_ij|` is the `2 beta` endpoint. Bradley's question can therefore be read as asking whether every Banach-space amplification of a centered contingency matrix has the same *vanishing topology* as one of those two endpoints.

## 3. Exact beta-side theorem

### Theorem

Assume that `B` contains `l_1^n` uniformly: there is a constant `C<infinity` such that for every `n` there is a linear embedding

\[
T_n:\ell_1^n\longrightarrow B
\]

which, after rescaling, satisfies

\[
\|T_n\|\le1,\qquad \|T_n^{-1}\|\le C.
\]

Then for every pair of sigma-fields `(\mathcal A,\mathcal C)`,

\[
\boxed{
\frac{2}{C}\,\beta(\mathcal A,\mathcal C)
\le R^B_{\infty,\infty}(\mathcal A,\mathcal C)
\le 2\,\beta(\mathcal A,\mathcal C).
}
\]

Hence `R^B_{\infty,\infty}` is equivalent to `beta`. In particular, by the standard characterization of non-B-convexity, every non-B-convex Banach space lies on Bradley's `beta` side.

### Proof: universal upper bound

Take arbitrary simple `X,Y` with essential norm bounds at most one, and refine them to finite partitions as above. Then

\[
\left|\sum_{i,j}d_{ij}\langle x_i,y_j\rangle\right|
\le \sum_{i,j}|d_{ij}|.
\]

Bradley's convention for absolute regularity gives

\[
2\beta(\mathcal A,\mathcal C)
=\sup_{\{A_i\},\{C_j\}}\sum_{i,j}
\left|P(A_i\cap C_j)-P(A_i)P(C_j)\right|.
\]

Taking the supremum over `X,Y` yields

\[
R^B_{\infty,\infty}(\mathcal A,\mathcal C)\le2\beta(\mathcal A,\mathcal C).
\]

### Proof: lower bound from a uniform `l_1` embedding

Fix finite partitions `A_1,...,A_I` and `C_1,...,C_J`, with centered table `D=(d_ij)`. Choose an embedding

\[
T:\ell_1^I\to B,
\qquad \|T\|\le1,
\qquad \|T^{-1}\|\le C.
\]

Set

\[
x_i=Te_i.
\]

Then `\|x_i\|\le1`. Let `E=T(\ell_1^I)`. For each column `j`, define on `E`

\[
\phi_j(Tz)=\sum_{i=1}^I \operatorname{sgn}(d_{ij})z_i,
\]

with an arbitrary sign choice when `d_ij=0`. For every `z`,

\[
|\phi_j(Tz)|
\le\|z\|_1
\le\|T^{-1}\|\,\|Tz\|
\le C\|Tz\|.
\]

Hence `\|\phi_j\|_{E^*}\le C`. Hahn--Banach extends `\phi_j` to a functional `\widetilde\phi_j\in B^*` with the same norm. Put

\[
y_j=C^{-1}\widetilde\phi_j,
\]

so `\|y_j\|\le1`. Then

\[
\begin{aligned}
\sum_{i,j}d_{ij}\langle x_i,y_j\rangle
&=\frac1C\sum_{i,j}d_{ij}\operatorname{sgn}(d_{ij})\\
&=\frac1C\sum_{i,j}|d_{ij}|.
\end{aligned}
\]

Therefore the partition-level value satisfies

\[
R_B(D)\ge \frac1C\sum_{i,j}|d_{ij}|.
\]

Taking partitions whose absolute-regularity sum approaches the supremum gives

\[
R^B_{\infty,\infty}(\mathcal A,\mathcal C)
\ge\frac{2}{C}\beta(\mathcal A,\mathcal C).
\]

This proves the theorem. `\square`

## 4. What this does and does not settle

The theorem gives a complete mechanism on the non-B-convex side because the standard Banach-space characterization says that `B` is non-B-convex iff it contains `l_1^n` uniformly. This extends the elementary `l_1/c_0/l_infinity` examples to the entire non-B-convex class, at least at the level of equivalence constants.

I make **no novelty claim** for this lemma. The proof is short enough that it may be folklore or implicit in the geometry behind Bradley's examples; a complete literature audit was not obtained in this screening run.

The unresolved side is B-convex `B`. The tempting strategy is to combine the matrix amplification form with type/cotype, regular-operator, or uniformly-curved-space inequalities to force `R_B(D)->0` whenever the scalar cut norm (hence `alpha`) tends to zero. A direct implementation fails for a precise reason: small `alpha` permits dependence to concentrate on atoms of arbitrarily small probability. After normalizing `|D|` by row/column variation weights, one gets a regular `L_2`-type contraction, but small cut norm alone need not make the scalar `L_2` norm small without lower-density / bounded-likelihood-ratio control. This is exactly the sort of extra regularity that appears in Bradley's restricted dichotomy results.

Thus the current source-level situation after this screening is:

- non-B-convex / uniform `l_1^n` side: beta-equivalence proved above;
- B-convex side: still open in this argument;
- possible intermediate third equivalence class: not excluded by this run;
- full D0029 source question: **not solved here**.

## 5. Method accounting

- **#2 ATTACK THE NEGATION FIRST.** Tried to force a third equivalence class from intermediate Banach geometry. No source-valid counterexample emerged; instead the beta endpoint became rigid on every non-B-convex space.
- **#18 SAY IT IN ANOTHER LANGUAGE.** Rewrote Bradley's coefficient as a Banach-space amplification norm of a centered contingency matrix.
- **#21 ASK WHO ELSE HAS THIS SHAPE.** Imported the uniform-`l_1^n` / B-convexity dichotomy from local Banach-space geometry. This completely proves the beta side but leaves a real rare-atom obstruction on the B-convex/alpha side.

No exact-arithmetic checker is appropriate: this artifact contains an analytic theorem with no finite computational core.
