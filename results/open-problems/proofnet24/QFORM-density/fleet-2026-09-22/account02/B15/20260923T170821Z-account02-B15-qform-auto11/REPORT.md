SIGNED IN - working on the quadratic-form bounded-density conjecture (universal constant), account account02, slot B15, 2026-09-23T17:08:21Z.
attacking: exact point-density core, rough ruled bridge, and source-valid obstructions to extracting the universal height from continuity or one physical triple.

# account02/B15 — point-core regularity reduction and generic-core obstructions

Programme: `QFORM-DENSITY-3EIG-20260922`  
Run: `20260923T170821Z-account02-B15-qform-auto11`  
Execution context: `WITHOUT_VERIFIED_BRAIN`  
Status: `NEW SUPPORTING REDUCTIONS / NEW CORE REGULARITY OBSTRUCTION / FULL QFORM OPEN`.

## 1. First unpaid implication

Write `s_3(A)` for the third singular value of the symmetric matrix `A`. The central unpaid statement is
\[
\boxed{
C_*:=\sup_{\substack{n\ge3,\ s_3(A)\ge1\\X_i\ \mathrm{independent},\ 0\le f_i\le1}}
\|p_{X^TAX}\|_\infty<\infty.
}
\tag{1.1}
\]
No continuity assertion is used in formulating or paying (1.1).

The newest completed designated-partner result I apply is account03/B15,
`math-open-problems@a0ff8602933dff6df3182b969fec03af0f2dcc25`,
`proofnet24/QFORM-density/fleet-2026-09-22/account03/B15/20260923T163043Z-account03-B15-qform-auto23/REPORT.md`.
It proves an exact zero-loss countable heat core for (1.1).

Let `R` be the countable class of finite unions of bounded half-open intervals with rational endpoints and total length one. Let `G_n` be the rational symmetric `n x n` matrices with simple spectrum, every entry nonzero and every principal minor nonzero. The partner theorem says
\[
C_*=\sup_{\substack{n\ge3,\ B\in G_n,\ s_3(B)>1\\E_i\in R,\varepsilon\in\mathbb Q_{>0},\ y\in\mathbb Q}}
\int_{E_1\times\cdots\times E_n}
\gamma_\varepsilon(x^TBx-y)\,dx.
\tag{1.2}
\]
The reduction first purifies each cap-one marginal by the bathtub principle, then approximates its unit-measure set by rational finite unions, and only after compactification approximates the matrix by an outward-dilated algebraically generic rational one. Thus no support, moment, connectedness or finite-fragment-count assumption is imposed on the original target.

## 2. New exact point-density core

A completed account02/B15 theorem at
`math-open-problems@9b8bb7e84811978a2c46c7bb5ec50f2570dbc056`,
`proofnet24/QFORM-density/fleet-2026-09-22/account02/B15/20260922T200544Z-account02-B15-qform-r11/REPORT.md`, proves that for every fixed symmetric matrix of rank at least three and every independent cap-one product law,
\[
p_{X^TAX}\in C_0(\mathbb R)\cap L^\infty(\mathbb R),
\tag{2.1}
\]
with an instance-dependent bound. I re-read the proof in this invocation; its zero-diagonal rough branch and complementary nonzero-diagonal branch do not assume post-rotation independence or a universal physical minor.

Every `B in G_n` is invertible, so (2.1) applies to every countable-core instance. The heat-height identity used in account03/B15 gives, for a core output law `mu`,
\[
\sup_{\varepsilon>0,y}(\mu*\gamma_\varepsilon)(y)=\|p_\mu\|_\infty.
\tag{2.2}
\]
Since a `C_0` function has the same supremum over rational and real centers,
\[
\boxed{
C_*=\sup_{\substack{n\ge3,\ B\in G_n,\ s_3(B)>1\\E_1,\ldots,E_n\in R,\ y\in\mathbb Q}}
p_{B,E}(y).
}
\tag{2.3}
\]
This is an exact identity in `[0,+infinity]`.

A useful contraposition is now rigorous:

> If the universal QFORM constant is false, there is a sequence of algebraically generic rational target matrices `B_m`, compact finite-fragment unit-set product laws, and rational centers `y_m` such that every output density is individually bounded and continuous, but
> \[
> p_m(y_m)\to\infty.
> \tag{2.4}
> \]

Thus a target counterexample to **uniformity** need not and, in view of (2.1), cannot be a single rank-at-least-three target law with an infinite essential height. Failure must be a sequence of finite continuous peaks escaping every common bound. Continuity is used in (2.3) only to choose pointwise rational test centers after the fixed-instance density has already been established; it does not produce the height estimate.

## 3. New obstruction: the exact countable core still has no common translation regularity

The compact/generic normal form does not restore any class-wide modulus of continuity. I give an explicit construction entirely inside the core.

For a large integer `N`, put
\[
D_N=\{x\in[1,3]:\cos(Nx^2)\ge0\}.
\tag{3.1}
\]
After `u=x^2`, periodic averaging against the smooth weight `du/(2sqrt(u))` gives, for every bounded Riemann-integrable `2pi`-periodic function `H`,
\[
\int_1^9 H(Nu)\frac{du}{2\sqrt u}
\longrightarrow
\left(\frac1{2\pi}\int_0^{2\pi}H(t)dt\right)\int_1^9\frac{du}{2\sqrt u}.
\tag{3.2}
\]
Apply this to
`H_0=1_{\{\cos t\ge0\}}`, whose mean is `1/2`, and to
`H_1=e^{it}1_{\{\cos t\ge0\}}`, whose mean is `1/pi`. Hence
\[
|D_N|\to1,
\qquad
\int_{D_N}e^{iNx^2}dx\to\frac2\pi.
\tag{3.3}
\]
Adjust `D_N` by a set of measure `o(1)` to total measure exactly one, and approximate in symmetric difference by a finite union `F_N` of rational half-open intervals of total measure one. This may be done inside a fixed interval such as `[1,4]`. For all sufficiently large `N`, arrange
\[
\boxed{
\left|\int_{F_N}e^{iNx^2}dx\right|\ge\frac12.
}
\tag{3.4}
\]
Thus `1_{F_N}` is an exact core marginal.

For the temporary matrix `I_3`, three iid copies have characteristic function at frequency `N` of magnitude at least `1/8`. To move into the generic matrix core without losing the spike, set
\[
A_N=(1+N^{-3})I_3
\]
and choose rational `B_N in G_3` with
\[
\|B_N-A_N\|_{op}<\frac1{2N^3}.
\tag{3.5}
\]
Then `s_3(B_N)>1`. On `F_N^3 subset [1,4]^3`,
\[
\left|e^{iN x^TB_Nx}-e^{iN|x|^2}\right|
\le N\|B_N-I_3\|_{op}|x|^2
\le\frac{72}{N^2}.
\tag{3.6}
\]
Therefore, for all sufficiently large `N`, the exact core output density `p_N` satisfies
\[
\boxed{|\widehat p_N(N)|\ge\frac1{16}.}
\tag{3.7}
\]

Now apply a completed result from the required Claude source
`math-open-problems@e5f71d79eff325201dd0274053d20268ce65b837`, `COUNTEREXAMPLE_SEARCH.md`, Theorem A: in dimension three, if all eigenvalue magnitudes are at least `sigma`, then the quadratic output density is at most `6sqrt(pi)/sigma`. Since `B_N` is positive definite with minimum eigenvalue greater than one,
\[
\boxed{\|p_N\|_\infty\le6\sqrt\pi.}
\tag{3.8}
\]
This is a real use of the completed source theorem at an inequality. Also `||B_N||<2` and `F_N subset[1,4]`, so all `p_N` have support in one fixed compact interval, say `[0,96]`.

Nevertheless, with `h_N=pi/N`,
\[
\begin{aligned}
\|p_N(\cdot+h_N)-p_N\|_1
&\ge\left|e^{-iNh_N}-1\right|\,|\widehat p_N(N)|\\
&\ge\frac18.
\end{aligned}
\tag{3.9}
\]
Thus `h_N->0` but the translation distance stays bounded away from zero. Consequently:

\[
\boxed{
\text{even the exact rational/generic countable core has no common }L^1
\text{ translation modulus.}
}
\tag{3.10}
\]

Because these densities have common compact support and a common height bound, (3.10) also rules out a common pointwise modulus of continuity and rules out relative compactness in `L^1`. Each individual density is nevertheless in `C_0` by (2.1). Hence continuity cannot be upgraded to a compactness principle that pays (1.1), even after the newest countable-core reduction.

## 4. Genericity also does not repair the physical-triple degeneration

There is a second obstruction inside the exact core. For `m>=3`, define
\[
A_m=2\,\operatorname{diag}\left(1,\frac1mJ_m,-\frac1mJ_m\right).
\tag{4.1}
\]
Its three nonzero eigenvalues are `2,2,-2`, so `s_3(A_m)=2`. Every `3 x 3` principal block has smallest singular value at most `2/m`. Choose, using density of `G_{2m+1}`,
\[
B_m\in G_{2m+1},
\qquad
\|B_m-A_m\|_{op}<\frac1{10m}.
\tag{4.2}
\]
Then
\[
s_3(B_m)>2-\frac1{10m}>1,
\tag{4.3}
\]
and for every physical triple `S`,
\[
\boxed{\sigma_{\min}((B_m)_{SS})\le\frac{21}{10m}.}
\tag{4.4}
\]
So all exact algebraic degeneracies can be removed while preserving the no-uniform-minor obstruction.

The completed ruled theorem in the required `e5f71d...` source gives, for an invertible physical block of signature `(2,1)` with eigenvalue magnitudes `lambda_1,lambda_2,mu`, the majority-side interval constant
\[
C_S=(\lambda_1\lambda_2\mu)^{-1/2}
\int_0^{2\pi}
\frac{d\theta}{\sqrt{\sin^2\theta/\lambda_1+\cos^2\theta/\lambda_2+1/\mu}}.
\tag{4.5}
\]
Equivalently,
\[
C_S=\int_0^{2\pi}
\frac{d\theta}{\sqrt{\lambda_2\mu\sin^2\theta+\lambda_1\mu\cos^2\theta+\lambda_1\lambda_2}}.
\tag{4.6}
\]
For an indefinite triple of `B_m` containing the singleton coordinate, at most one eigenvalue is macroscopic: one magnitude is at most `3`, the other two are at most `5/m`. Therefore the expression under the square root in (4.6) is at most `55/m`, and
\[
C_S\ge2\pi\sqrt{m/55}.
\tag{4.7}
\]
If the triple avoids the singleton, all three eigenvalue magnitudes are at most `7/m`, hence
\[
C_S\ge\frac{2\pi m}{\sqrt{147}}
\ge2\pi\sqrt{m/55}
\qquad(m\ge3).
\tag{4.8}
\]
Thus
\[
\boxed{
\inf_{\substack{|S|=3\\(B_m)_{SS}\ \mathrm{indefinite}}}C_S
\ge2\pi\sqrt{m/55}\to\infty,
}
\tag{4.9}
\]
with the infimum `+infinity` if there is no indefinite triple.

Equation (4.9) is not a QFORM counterexample; the same bank family is known to be controlled after aggregation. It is an exact obstruction to the proof interface “genericize, choose one physical triple, and quote the law-uniform ruled constant.” The aggregation has to occur before the reciprocal local-curvature payment.

## 5. Independent rough-input audit of the ruled bridge

I independently checked the rough-input passage required by the newest continuation.

Fix three active **original** coordinates and condition on all others. Let the conditional quadratic part be an invertible signature `(2,1)` block `B`. Completing the square gives
\[
Q_w(x)=(x+B^{-1}d(w))^TB(x+B^{-1}d(w))+c(w).
\tag{5.1}
\]
This is a translation in the original independent coordinates, so the translated active marginals remain independent and cap one. Because `B` is invertible, every conditional affine term lies in its range, exactly matching the linear-term scope recorded in the current audit of the ruled theorem.

Mollify only those three original marginals:
\[
f_i^{(\eta)}=f_i*\gamma_\eta.
\tag{5.2}
\]
Then `f_i^(eta)<=1`, independence is preserved, and
\[
\left\|\prod_{i\in S}f_i^{(\eta)}-\prod_{i\in S}f_i\right\|_1
\le\sum_{i\in S}\|f_i^{(\eta)}-f_i\|_1\to0.
\tag{5.3}
\]
The completion-of-square translation does not change this distance. Deterministic quadratic pushforward and restriction to the majority event are contractions for total variation. Hence the smooth conditional majority submeasures converge in total variation to the rough conditional majority submeasure. The smooth ruled estimate therefore passes interval by interval with exactly the same `C_S`, and averaging the untouched outside product law gives
\[
\boxed{
\Pr(Q\in I,\ Q\ge c(W))\le C_S|I|.
}
\tag{5.4}
\]
No continuity of the rough output is used in obtaining (5.4).

The geometric constants also check: after spectral scaling, the ruling parametrisation of the one-sheet level has coarea quotient `(1/2)dtheta dt`; undoing scaling makes the line direction
\[
v_\theta=(-\sin\theta/\sqrt{\lambda_1},\ \cos\theta/\sqrt{\lambda_2},\ 1/\sqrt\mu),
\]
so the non-arclength parameter contributes `1/|v_theta|`. The two-dimensional product-projection cap `2` cancels the coarea `1/2`, producing exactly (4.5). This avoids evaluating an arbitrary `L^infinity` projection representative along a curve.

## 6. Exact regularity ledger

The three notions must be kept distinct.

**Absolute continuity.** For every nonzero symmetric `A`, any absolutely continuous joint input law pushes forward under `x -> x^TAx` to an absolutely continuous law. Local coarea away from `ker A` proves this. Product structure and the cap-one condition are unnecessary for this qualitative implication.

**Instancewise essential boundedness and continuity under the target.** The fixed-instance theorem (2.1) says the target hypotheses, indeed merely `rank(A)>=3` plus the cap-one product structure, imply an individually bounded `C_0` density. Its constants depend on physical geometry and are not uniform.

**Universal essential boundedness.** This is exactly (1.1), equivalently the point-core supremum (2.3), and remains open. Neither absolute continuity nor qualitative continuity supplies it. Section 3 shows that even a common compact support and a common height inside the exact core do not produce a common continuity modulus; Section 4 shows genericity does not produce a common local-curvature certificate.

Thus the stronger continuous-density conclusion is already a fixed-instance qualitative fact at the source-complete theorem (2.1), but it is logically separate from the missing matrix- and dimension-uniform height. The shared protected claim ledger still lists the continuous-representative item as open; this worker does not mutate that ledger.

## 7. Remaining mathematical obligation

After the countable-core and ruled payments, the first unpaid implication can be written without regularity ambiguity as
\[
\boxed{
\sup_{\substack{n,B\in G_n,\ s_3(B)>1\\E_i\in R,\ y\in\mathbb Q}}
p_{B,E}(y)<\infty.
}
\tag{7.1}
\]
A proof must remain uniform as the number/separation of fragments grows and as all physical triples degenerate as in (4.2). On an indefinite triple the majority one-sheet submeasure is paid by (5.4); a high peak beyond that payment must be carried by the product-provenance-sensitive minority/two-sheet part, unless an aggregate cross-volume/hub receiver fires before local inversion. The live `QFORM-TWOSHEET-XRAY-ONLY-FALSE` correction forbids replacing that missing product-sensitive step by a generic X-ray norm.

The newest current Claude continuation `math-open-problems@c4c23b784395630c094ba299a50712209921d1ae` adds the proposed single-hub `(SP)` route but explicitly leaves it open. Nothing in this report treats `(SP)` as proved.

## 8. Integrity ledger

- Full universal QFORM theorem: **OPEN**.
- New exact result: point-density countable-core identity (2.3), obtained by combining the completed account03/B15 core with the completed fixed-instance `C_0` theorem.
- New exact obstruction: the core family (3.1)--(3.9) has generic rational matrices, finite rational interval sources, common support and common height, yet no common `L^1` translation modulus.
- New structural obstruction: algebraic genericization preserves the no-uniform-physical-triple family, and the exact ruled certificate diverges at least like `sqrt(m)` on every indefinite physical triple.
- Required `e5f71d...` source applied at real equations: Theorem A at (3.8) and the ruled one-sheet theorem at (4.5), (5.4).
- Designated partner applied: account03/B15 countable-core theorem at (1.2)--(2.3).
- Rough-input ruled passage independently checked by original-coordinate mollification and total-variation contraction.
- No hidden moments, support assumptions on the original target, log-concavity, post-rotation independence, arbitrary-joint coarea height bound, pointwise law-uniform phase decay, fixed fragment count, or uniformly good physical minor is used.
