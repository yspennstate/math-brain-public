# account03/B10 — rank-three coupled quadratic-form density

Run: `b10-20260922T115000Z-qform-r1`  
Programme: `QFORM-DENSITY-3EIG-20260922`, owner-control revision `2026-09-22.5`  
Assignment: `Rank-three coupled case`  
Classification: `SUPPORTING_THEOREMS + ROUTE_REFUTATION`; full target `OPEN / NOT PROVED`  
Brain status: `WITHOUT_VERIFIED_BRAIN`

## Control resolution

Fresh `scheduled_tasks/README.md` on `yspennstate/math-research-brain` explicitly supersedes the incoming FEI order and makes QFORM the sole research target for all eighty workers. The current B10 card asks for arbitrary rank-three symmetric forms with all three nonzero eigenvalues of magnitude at least one, independent original-coordinate densities bounded by one, and arbitrary orientation; projected/eigenbasis coordinates must not be treated as independent.

The named current-programme partner is `account04/B10`. No completed current-QFORM handoff from that partner was present at the fresh read, so this run did not infer a result from absence and did not wait. It consumed the completed other-account source `account02/B06`, handoff `b06-20260922T113045Z-d47192d10a82`, whose reusable result is the same-sign determinant-mass identity

\[
\det(P_{\{i,j\}})=\lambda_1\lambda_2\det(U_{\{i,j\}})^2,
\qquad
\sum_{i<j}\det(P_{\{i,j\}})=\lambda_1\lambda_2,
\]

for the positive rank-two spectral component. That result is applied quantitatively below. The account02/B05 product-kernel handoff was also used as a correction against fiber-supremum arguments.

---

# 1. A genuine coupled rank-three product-law theorem

## Theorem `QFORM-CROSS-SQUARE-PRODUCT-v1`

Let `X,Y,Z` be independent real random variables with probability densities bounded by `1`. Let `b,c` be nonzero reals. For arbitrary real linear coefficients `alpha,beta,gamma` and constant `d`, define

\[
Q=2bXY+cZ^2+\alpha X+\beta Y+\gamma Z+d.
\]

Then `Q` has a density and

\[
\boxed{\|p_Q\|_\infty\le {4\sqrt2\over\sqrt{|bc|}}.}
\]

In particular, if `|b|,|c|>=1`, then `||p_Q||_infty <= 4 sqrt(2)`.

### Proof

Separate translations preserve independence and the density bounds. Indeed,

\[
2bxy+\alpha x+\beta y
=2b\left(x+{\beta\over2b}\right)
     \left(y+{\alpha\over2b}\right)-{\alpha\beta\over2b},
\]

and completing the square removes the linear term in `z`. It therefore suffices to treat

\[
Q=2bXY+cZ^2.
\]

The density of `T=cZ^2` obeys, on its support,

\[
p_T(t)\le {1\over\sqrt{|c|}\sqrt{|t|}}.
\]

Consequently, for every `a`,

\[
p_Q(a)
\le {1\over\sqrt{|c|}}
\mathbb E\,|a-2bXY|^{-1/2}.
\]

Fix `x != 0`. Put `s=a-2bxy`. Since `0<=f_Y<=1` and `int f_Y=1`, after this change of variables the multiplier `g(s)=f_Y((a-s)/(2bx))` satisfies `0<=g<=1` and

\[
\int g(s)\,ds=2|bx|.
\]

Among all such `g`, the integral against the symmetric decreasing kernel `|s|^{-1/2}` is maximized by the indicator of the centered interval of length `2|bx|`. Hence

\[
\begin{aligned}
\int f_Y(y)|a-2bxy|^{-1/2}\,dy
&={1\over2|bx|}\int g(s)|s|^{-1/2}\,ds\\
&\le {1\over2|bx|}\int_{-|bx|}^{|bx|}|s|^{-1/2}\,ds\\
&={2\over\sqrt{|b|}\sqrt{|x|}}.
\end{aligned}
\]

Because `X` is absolutely continuous, the exceptional point `x=0` has zero probability. A second one-dimensional rearrangement gives

\[
\int f_X(x)|x|^{-1/2}\,dx
\le\int_{-1/2}^{1/2}|x|^{-1/2}\,dx
=2\sqrt2.
\]

Therefore

\[
p_Q(a)
\le {1\over\sqrt{|c|}}
{2\over\sqrt{|b|}}(2\sqrt2)
={4\sqrt2\over\sqrt{|bc|}},
\]

uniformly in `a`. QED.

### High-dimensional conditional corollary

Let `X_1,...,X_n` be independent with densities <=1. If some physical-coordinate principal `3x3` block of `A`, after permuting those three coordinates, is

\[
\begin{pmatrix}
0&b&0\\
b&0&0\\
0&0&c
\end{pmatrix},
\]

then conditioning on all other coordinates turns all cross-terms with the outside variables into linear terms in the selected three variables. The theorem applies conditionally with the same constant and averaging the conditional densities cannot increase the bound. Thus

\[
\boxed{\|p_{X^TAX}\|_\infty\le4\sqrt2/\sqrt{|bc|}.}
\]

This is a genuine original-product-law rank-three result; no rotation or false independence assumption is used.

---

# 2. Exact payment of the third eigendirection against same-sign determinant mass

This is the direct application of the consumed account02/B06 determinant-mass result.

Assume a rank-three form has signature `(2,1)` and write its spectral decomposition as

\[
A=P-vv^T,
\qquad
P=RR^T,
\]

where the two columns of `R` are `sqrt(lambda_1) u_1` and `sqrt(lambda_2) u_2`, while `v=sqrt(mu)u_3`; here `lambda_1,lambda_2,mu>0` and `u_1,u_2,u_3` are orthonormal.

For a physical coordinate pair `S={i,j}` with `det(P_S)>0`, define the negative-direction leverage

\[
\tau_S:=v_S^T P_S^{-1}v_S.
\]

The matrix determinant lemma gives

\[
\boxed{\det(A_S)=\det(P_S)(1-\tau_S).}
\]

The B06 determinant masses

\[
w_S:={\det(P_S)\over\lambda_1\lambda_2}
\]

form a probability distribution by Cauchy-Binet. The new exact identity is

\[
\boxed{
\sum_S \det(P_S)\tau_S=\mu(\lambda_1+\lambda_2),
\qquad
\mathbb E_w\tau
=\mu\left({1\over\lambda_1}+{1\over\lambda_2}\right).
}
\]

### Proof

Write `r_i in R^2` for row `i` of `R`. For `S={i,j}`,

\[
\det(P_S)\tau_S
=v_S^T\operatorname{adj}(P_S)v_S
=\|v_i r_j-v_jr_i\|_2^2.
\]

Summing over all unordered pairs gives the exterior-product identity

\[
\sum_{i<j}\|v_i r_j-v_jr_i\|^2
=\|v\|^2\|R\|_F^2-\|R^Tv\|^2.
\]

Now `R^Tv=0` by spectral orthogonality, `||v||^2=mu`, and `||R||_F^2=lambda_1+lambda_2`, proving the formula.

### Consequence and limitation

If

\[
m:=\mu(1/\lambda_1+1/\lambda_2)<1,
\]

then Markov's inequality under `w` gives

\[
w\{S:\tau_S\ge1\}\le m,
\]

so at least `1-m` of the same-sign determinant mass lies on physical pairs for which `A_S` remains positive definite. This is a quantitative favorable-ratio regime.

But this does **not** close QFORM. First, the target allows `m>=1`; for the symmetric spectrum `(1,1,-1)`, `m=2`. Second, even when positive determinant mass exists, it may be spread over `Theta(n^2)` tiny minors, and the account02/B06 Hadamard example shows that no fixed coordinate pair need have a dimension-free determinant. Thus positivity of weighted definite mass alone cannot be converted into a universal density bound by choosing one pair.

This identity nevertheless pinpoints exactly how the third eigendirection spends the determinant-mass resource, rather than merely saying that cancellation is possible.

---

# 3. Refutation of the tempting spectral-slice mixed-norm completion

A natural attempt is: diagonalize the rank-three form, use the same-sign two-dimensional ellipse bound on two eigen-coordinates, and hope that the projected joint density `h(y_1,y_2,z)` satisfies a universal bound

\[
\int \sup_{y_1,y_2} h(y_1,y_2,z)\,dz\le C.
\]

That implication is false even for an orthogonal image of **three independent density-one inputs**.

## Construction `QFORM-SPECTRAL-SLICE-MIXED-NORM-FALSE-v1`

For an integer `M>=3`, let

\[
A_M=B_M=\bigcup_{k=1}^M[10^k,10^k+1/M],
\qquad C=[0,1].
\]

All three indicators are probability densities bounded by one. Let `X_1,X_2,X_3` have these independent laws and make the orthogonal change of variables

\[
y_1={X_1+X_2\over\sqrt2},
\qquad
z={X_1-X_2\over\sqrt2},
\qquad
y_2=X_3.
\]

The joint density in `(y_1,y_2,z)` is

\[
h(y_1,y_2,z)
=1_{A_M}\!\left({y_1+z\over\sqrt2}\right)
 1_{B_M}\!\left({y_1-z\over\sqrt2}\right)
 1_C(y_2).
\]

For fixed `z`, `sup_{y_1,y_2}h=1` exactly when `z` belongs to `(A_M-B_M)/sqrt(2)`. Hence

\[
\int\sup_{y_1,y_2}h(y_1,y_2,z)\,dz
={|A_M-B_M|\over\sqrt2}.
\]

For distinct ordered pairs `(i,j)`, the differences `10^i-10^j` are distinct: equality

\[
10^i-10^j=10^k-10^\ell,
\quad i>j,\ k>\ell,
\]

forces `j=ell` from the exact power of `10` dividing each side and then `i=k`. The off-diagonal difference intervals therefore give `M(M-1)` disjoint intervals of length `2/M`. Consequently

\[
|A_M-B_M|\ge2(M-1),
\]

and

\[
\boxed{
\int\sup_{y_1,y_2}h(y_1,y_2,z)\,dz
\ge\sqrt2(M-1)\to\infty.
}
\]

So no dimension-free or law-uniform spectral-slice `L^1_zL^infty_{y_1,y_2}` theorem of this type exists. This strengthens the current correction that unrestricted fiber suprema lose dimension: even in exactly three variables the disconnected-support geometry can make the mixed norm arbitrarily large.

The third spectral variable must therefore remain **inside** the curved/oscillatory averaging. Taking a supremum over the two same-sign coordinates before paying the third direction irreversibly discards the needed product information.

---

# 4. Updated rank-three coupled frontier

Three facts now have to be respected simultaneously:

1. A nontrivial indefinite rank-three physical pattern (`2bXY+cZ^2`) admits a universal product-law density bound `4 sqrt(2)/sqrt(|bc|)`.
2. Same-sign spectral determinant mass has an exact third-direction leverage average `mu(1/lambda_1+1/lambda_2)`; this quantifies cancellation but does not supply one large physical minor.
3. The obvious spectral `L^1_z L^infty_{y_1,y_2}` route is false for arbitrary density-one product laws, so one cannot finish by rotating and applying a slice supremum.

The first missing implication is therefore a **product-preserving weighted curved aggregation**: combine the determinant-mass weights (or the account02/B05 phase-space kernels) with the third eigendirection *before* taking absolute values/suprema, in a way that remains dimension-free when all physical minors are tiny. An acceptable completion must work in the delocalized equal-spectrum control `(1,1,-1)` where the mean negative leverage is `2` and every small physical principal block can be indefinite.

No claim of the full conjecture is made in this run.

## Source-bound dependencies

- Fresh owner control and target: `yspennstate/math-research-brain`, `scheduled_tasks/README.md`, revision `2026-09-22.5`.
- Assignment: `yspennstate/math-research-brain`, `scheduled_tasks/work/shared/qform-density-2026-09-22/assignments/account03/B10.json`.
- Current corrections/state: `scheduled_tasks/work/shared/qform-density-2026-09-22/CURRENT_RESEARCH.md` and `CORRECTION_INBOX.json`.
- Applied completed other-account result: `account02/B06`, canonical report `yspennstate/math-open-problems@6902eb62f21a7c833ca27dcca69f34d50e711a7d`, path `proofnet24/QFORM-density/fleet-2026-09-22/account02/B06/b06-20260922T113045Z-d47192d10a82/REPORT.md`; brain handoff records report blob `9cced3d58d10574ef548c119c8d5a67276dc870f`.
- Product-kernel/fiber-sup correction: `account02/B05`, canonical report `yspennstate/math-open-problems@63ae1057b5ad8a5bc3c764d733de79e5c917b752`, path `proofnet24/QFORM-density/fleet-2026-09-22/account02/B05/20260922T112240Z-b05-qform-9d86c905/REPORT.md`.
