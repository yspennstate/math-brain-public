# FEI continuation: sharp affine-fibre gluing and quadratic tag phases

20 September 2026. Owner-requested continuation. Repository: `yspennstate/math-open-problems`, branch `master`.

**Full Friedgut–Kalai Fourier entropy–influence conjecture: NOT PROVED by this continuation.** The main result is an all-dimensional gluing theorem with a sharp constant-four threshold. It permits dependent branches on arbitrary affine partitions, retains any larger certified local FEI constant, and survives arbitrary quadratic phases on the existing tag coordinates. It does not assert that arbitrary Boolean functions have the required representation. Mathematical priority and independent review remain unverified.

## 1. What is new in this continuation

Let the existing physical coordinates be split as `(x,y) in F_2^k x F_2^m`. Suppose a map `pi:F_2^m -> F_2^k` has nonempty fibres that are affine subspaces. For a Boolean sign function `g(y)` and a quadratic polynomial `Q(x)`, consider

\[
 F_Q(x,y)=(-1)^{Q(x)+x\cdot\pi(y)}g(y).
\]

For each affine fibre, take sections parallel to all the physical coordinate axes tangent to that fibre. If each resulting Boolean section satisfies `H<=C J`, with the same constant `C`, then

\[
\boxed{H(F_Q)\le \max\{4,C\}\,J(F_Q)\le\max\{4,C\}\,I(F_Q).}
\tag{1.1}
\]

Here `J` is folded total influence, defined below. The constant does not depend on dimension, fibre number, fibre codimensions, the geometry of the affine partition, the number of recursive uses of the theorem, or the rank of `Q`.

In particular, if the restriction of `g` to each affine fibre is a quadratic phase in intrinsic affine coordinates, then

\[
\boxed{H(F_Q)\le4J(F_Q).}
\tag{1.2}
\]

The constant four cannot be decreased uniformly over this class: ordinary addressing functions have `H/I -> 4`. This sharpness statement concerns the present restricted class, not the optimal universal FEI constant.

The extension beyond the quadratic-cell case is substantive: cells may contain previously certified high-degree cores. For example, inserting the repository's quadratic-twisted symmetric-core certificates gives constant **12.04**, unchanged, whenever every required physical section satisfies those hypotheses. Distinct cells need not use disjoint coordinate sets, and no independence between their branches is assumed.

This is a theorem about a representation of the function being studied on its actual coordinates. Appending new tag variables to an arbitrary function does not prove FEI for that original function.

## 2. Sources consumed and attribution

The starting status and surviving research targets were read from these actual repository files:

- `proofnet24/P03-fei/README.md`, blob `9201da45afcf21156ae078cc505d37b57a1ae4b7`. It explicitly preserves OPEN status, the weighted/hereditary erasure target, and the retirement of the absolute-overlap and fixed-affine-drift shortcuts.
- `proofnet24/P03-fei/runs/2026-09-20/2026-09-20T12-28-55+0300__fei-isospectral-splicing-symmetry-quotient.md`, blob `3421c0cbfd22031554befb962ec92cd0c8bb45b9`, creation commit `7b445599e2165c53ae44c5f728d0538192e1edc1`. Its child-spectrum identities, Hellinger/KL bound, and zero-cost isospectral splice are retained, not presented as new here.
- `proofnet24/P03-fei/scheduled-continuation/runs/2026-09-20/2026-09-20T08-36-07Z__report.md`, blob `36b0037e3418820e8f487ef8c7869f8c3c3b9f1d`, creation commit `314297aaed68d78ef7fb28fe291de10d63040b3a`. Its dimension-adaptive endpoint potential remains a conditional selector route. Section 10 below records a new obstruction to one attempted coefficientwise proof of that selector, not a refutation of the selector.
- `proofnet24/P03-fei/continuations/2026-09-20-quadratic-symmetry/REPORT.md`, blob `11605492453c978a7cb45261eb563d006fee2db0`, creation commit `6cc02bb1fc64bb20a99c5a878d4bc27c8dc6bf56`. The entropy-deletion lemma and explicit constant-preserving quadratic-symmetry certificates are used with their stated hypotheses.

The published symmetric-function input is due to Ryan O'Donnell, John Wright and Yuan Zhou, *The Fourier Entropy–Influence Conjecture for Certain Classes of Boolean Functions*, ICALP 2011, DOI `10.1007/978-3-642-22006-7_28`. The part-symmetric constant is their result, not a new constant established here.

Relevant external context checked on 20 September 2026 includes González–MacManus–Pereyra, *Further evidence towards the Fourier Entropy-Influence conjecture*, arXiv `2606.00246`, whose abstract describes a stopping-tree approach and restricted classes; Arunachalam–Chakraborty–Koucký–Saurabh–de Wolf, *Improved bounds on Fourier entropy and Min-entropy*, arXiv `1809.09819`, which includes an average unambiguous parity-certificate bound; and O'Donnell–Tan, *A composition theorem for the Fourier Entropy-Influence conjecture*, arXiv `1304.1347`. These are relevant prior composition/partition methods. No claim that this continuation has cleared the literature for novelty is made. The sharp addressing example and elementary quadratic Fourier facts are standard ingredients and are proved here for completeness.

## 3. Definitions

All cubes have uniform probability and all logarithms in entropy are base two. For a Boolean sign function `h:F_2^n -> {-1,1}`, define

\[
 \widehat h(s)=2^{-n}\sum_z h(z)(-1)^{s\cdot z},\qquad
 H(h)=\sum_s\widehat h(s)^2\log_2\frac1{\widehat h(s)^2}.
\]

Zero summands are zero. Parseval gives `sum_s hhat(s)^2=1`. Define

\[
 \alpha_i(h)=\Pr[h(z)\ne h(z+e_i)],\quad
 j_i(h)=\min\{\alpha_i(h),1-\alpha_i(h)\},\quad
 I(h)=\sum_i\alpha_i(h),\quad J(h)=\sum_i j_i(h).
\]

For a function on `(x,y)`, write `J_x` and `J_y` for the sums over the two physical coordinate groups. We never replace these physical axes by arbitrary affine directions without explicitly accounting for the change.

Index the nonempty fibres of `pi` by their distinct actual labels `a`:

\[
 A_a=\pi^{-1}(a)=b_a+V_a,\quad
 r_a=\operatorname{codim}V_a,\quad q_a=\Pr[Y\in A_a]=2^{-r_a}.
\]

Let

\[
 T_a=\{i:e_i\in V_a\},\quad s_a=|T_a|,\quad
 \kappa_a=m-s_a,\quad d_a=\dim V_a-s_a=\kappa_a-r_a.
\]

Thus `kappa_a` is the number of physical directions that leave the cell. Choose a basis of `V_a` beginning with the distinct standard vectors `{e_i:i in T_a}` and extend it by `d_a` vectors `w_1,...,w_{d_a}`. Write points of the cell uniquely as

\[
 b_a+\sum_{i\in T_a}z_i e_i+\sum_{t=1}^{d_a}u_t w_t.
\]

Define the intrinsic Boolean function and its physical sections by

\[
 h_a(z,u)=g\left(b_a+\sum_{i\in T_a}z_i e_i+\sum_tu_tw_t\right),\qquad
 h_{a,u}(z)=h_a(z,u).
\]

The hypothesis in (1.1) is exactly `H(h_{a,u})<=C J(h_{a,u})` for every cell and every `u`. It is not an assumption about influence in arbitrary affine coordinates. Zero-dimensional sections are constant and have entropy and influence zero.

## 4. Exact affine-fibre Fourier entropy identity

First set `Q=0` and write `F=F_0`.

### Proposition 4.1

For arbitrary Boolean `g`, without any local FEI assumption,

\[
\boxed{H(F)=\sum_a q_a\,[2r_a+H(h_a)].}
\tag{4.1}
\]

### Proof

Fourier transform first in the `x` coordinates. For `t in F_2^m`, orthogonality gives

\[
 \widehat F(a,t)=2^{-m}\sum_{y\in A_a}g(y)(-1)^{t\cdot y}.
\tag{4.2}
\]

The squared Fourier mass at a fixed label `a`, summed over `t`, is `q_a`, by Parseval for `g 1_{A_a}`. Thus the first spectral label has probability law `(q_a)`.

Restriction of ambient characters to `V_a` maps `F_2^m` onto `V_a^*`, with kernel `V_a^perp` of size `2^{r_a}`. If `xi` is the restricted character, (4.2) has magnitude

\[
 |\widehat F(a,t)|=q_a|\widehat h_a(\xi)|.
\]

For each `xi` there are exactly `2^{r_a}` possible lifts `t`. After conditioning on the label `a`, every lift has probability

\[
 q_a\widehat h_a(\xi)^2=2^{-r_a}\widehat h_a(\xi)^2.
\]

Hence the conditional entropy is `r_a+H(h_a)`. Also `H((q_a))=sum_a q_a r_a`, since `q_a=2^{-r_a}`. The entropy chain rule proves (4.1). An affine change of intrinsic basis only permutes the intrinsic Fourier labels, so their entropy does not depend on the chosen complement. QED.

The distinct-label condition is essential here. Two separate pieces given the same label contribute amplitudes to the same Fourier block and cannot be treated as a mixture.

## 5. Exact boundary payment in the physical coordinates

For a physical direction `e_i`, an affine cell either satisfies `A_a+e_i=A_a`, or has empty intersection with its translate. In the latter case every point in that cell changes label.

### Proposition 5.1

For every `i` among the `y` coordinates,

\[
\boxed{
 \alpha_{y_i}(F)=\frac12\sum_{a:i\notin T_a}q_a
 +\sum_{a:i\in T_a}q_a\,\mathbb E_u\alpha_i(h_{a,u}).}
\tag{5.1}
\]

Consequently,

\[
\boxed{
 J_y(F)\ge\frac12\sum_aq_a\kappa_a
 +\sum_aq_a\mathbb E_u J(h_{a,u}).}
\tag{5.2}
\]

### Proof

Fix `y`. If the two endpoints have different labels `a != b`, then the ratio of their Boolean values is a fixed sign times `(-1)^{x dot(a+b)}`. Since `a+b != 0`, precisely half the uniform `x` assignments give disagreement. If the labels agree, the tag characters cancel and the disagreement is exactly that of `g` along the same physical edge. Averaging gives (5.1).

The function `t -> min(t,1-t)` is concave. Regard the right side of (5.1) as an average of numbers `1/2` on cross-cell edges and the individual section influences on within-cell edges. Jensen's inequality gives

\[
 j_{y_i}(F)\ge\frac12\sum_{a:i\notin T_a}q_a
 +\sum_{a:i\in T_a}q_a\mathbb E_u j_i(h_{a,u}).
\]

Sum over the physical coordinates `i`. Each cell has exactly `kappa_a` leaving directions, which proves (5.2). QED.

This lower bound is the feature missing in blind counts of changed coordinates: all cross-cell edges have a proved half-disagreement payment, even when their branch signs and high-degree cores are arbitrarily dependent.

## 6. Entropy of the non-coordinate directions and the gluing theorem

We recall, and prove, the entropy-deletion estimate used in the earlier repository report. If a Boolean function `h(z,u)` has `d` coordinates in `u`, then

\[
 H(h)\le 2d+\mathbb E_u H(h_u).
\tag{6.1}
\]

Let `(S_z,S_u)` be its Fourier sample. Squaring the Fourier expansion of a restriction and averaging uniform `u` shows that `S_z` has the mixture law of the section Fourier samples. If `U` is uniform and `Z|U=u` has the squared Fourier law of `h_u`, then

\[
 H(h)=H(S_z)+H(S_u\mid S_z)
 \le H(Z,U)+d
 =\mathbb E_uH(h_u)+2d.
\]

This argument uses only the ordinary entropy chain rule and Fourier orthogonality. It also applies to the explicitly chosen intrinsic coordinates of each affine cell.

Apply (6.1) to `h_a`, with `d=d_a=kappa_a-r_a`, in (4.1):

\[
\boxed{
 H(F)\le 2\sum_aq_a\kappa_a+
             \sum_aq_a\mathbb E_uH(h_{a,u}).}
\tag{6.2}
\]

Suppose each section has the certificate `H(h_{a,u})<=C J(h_{a,u})`. Set

\[
 A=\frac12\sum_aq_a\kappa_a,\qquad
 B=\sum_aq_a\mathbb E_uJ(h_{a,u}),\qquad K=\max\{4,C\}.
\]

Equations (6.2) and (5.2) give

\[
 H(F)\le4A+CB\le K(A+B)\le KJ_y(F).
\tag{6.3}
\]

This proves (1.1) for `Q=0`. It even avoids using any of the influence of the tag variables.

There is no factor for the number of cells, and no decision-tree depth appears. The affine partition need not come from a physical coordinate decision tree or have a common orientation.

## 7. Quadratic cells: exact rank formula and a sharp constant

A quadratic sign function on `F_2^d` has squared Fourier law uniform on an affine subspace of dimension equal to the rank `R` of its polar bilinear form. Here is a proof.

For a quadratic polynomial `q`, its multiplicative derivative in direction `v` is `(-1)^{q(x)+q(x+v)}`, a linear character of `x` times a constant. Its mean is zero unless `v` is in the radical of the polar form. On that radical the derivative is a constant sign, and those signs form a character. The autocorrelation is therefore a character times the indicator of the radical. Fourier inversion of the identity

\[
 \mathbb E_x[(-1)^{q(x)+q(x+v)}]
 =\sum_s\widehat{(-1)^q}(s)^2(-1)^{s\cdot v}
\]

shows that the squared spectrum is uniform on the corresponding affine annihilator, with `2^R` points. Thus its Fourier entropy is exactly `R`.

In standard coordinates, every nonzero row of the polar matrix gives influence `1/2`. A zero row gives influence zero or one, hence folded influence zero. If there are `t` nonzero rows, `J=t/2` and `R<=t`, so

\[
 H((-1)^q)=R\le2J((-1)^q).
\tag{7.1}
\]

Every physical section of an intrinsically quadratic cell is still quadratic. Thus Section 6 gives `H(F)<=4J_y(F)` with no restriction on cell rank. Proposition 4.1 also gives the exact identity

\[
\boxed{H(F)=\sum_aq_a(2r_a+R_a),}
\tag{7.2}
\]

where `R_a` is the polar rank on the intrinsic tangent space of cell `a`.

An alternative direct payment of (7.2) is useful. In an intrinsic basis beginning with the `s_a` tangent standard vectors, let `t_a` of those rows be nonzero. The other `d_a` rows account for all remaining possible nonzero rows, so `R_a<=t_a+d_a`. Therefore

\[
 2r_a+R_a\le r_a+\kappa_a+t_a\le2\kappa_a+t_a.
\]

The folded boundary estimate pays at least `(kappa_a+t_a)/2` on average. This is consistent with the constant four and also retains a possible extra rebate.

### Sharpness

Take `m` address bits `y` and `2^m` data bits `x_a`, and put `F(x,y)=(-1)^{x_y}`. The fibres of `pi(y)=e_y` are singletons, and `g=1`. Equation (7.2) gives `H(F)=2m`. Every address bit has influence `1/2`, and each data bit has influence `2^{-m}`. Hence, for `m>=1`,

\[
 J(F)=I(F)=m/2+1,\qquad
 \frac{H(F)}{I(F)}=\frac{2m}{m/2+1}\longrightarrow4.
\tag{7.3}
\]

No constant less than four can cover the whole class, even with constant sections. The example is standard; its role here is to establish that the gluing threshold cannot be improved uniformly.

## 8. Arbitrary quadratic phases on the existing tag variables

Let `Q(x)` have polar matrix `B` of rank `rho`, and put `F_Q=(-1)^Q F`. There are two elementary facts:

\[
 H(F_Q)\le H(F)+\rho,\qquad
 J_y(F_Q)=J_y(F),\quad J_x(F_Q)\ge\rho/2.
\tag{8.1}
\]

To prove the entropy statement, the Fourier support of `(-1)^Q` is an affine coset `b+L`, where `L=im B` has dimension `rho`, by the quadratic Fourier fact proved above. Multiplication by this phase is an orthogonal operator in Fourier coordinates. For each fixed `y` frequency it maps the subspace supported on any coset of `L` in the `x` frequencies onto the subspace supported on its translate by `b`. The norm of each such block is preserved. Thus the joint distribution of the `y` frequency and the coarse `x` coset is unchanged up to relabeling. The conditional entropy within an `x` coset lies between zero and `rho`, so the total entropy can increase by at most `rho`.

The factor `(-1)^Q` cancels in every derivative along `y`, proving the middle identity. For a tag coordinate with a nonzero row of `B`, its derivative contains a nonconstant character in the other uniform `x` variables, independently of `y`. Its influence is exactly `1/2`. There are at least `rho` such rows, proving the last inequality.

Finally, with `K=max{4,C}` and using the stronger bound (6.3),

\[
\begin{aligned}
 H(F_Q)&\le KJ_y(F)+\rho\\
 &\le KJ_y(F_Q)+2J_x(F_Q)\\
 &\le KJ(F_Q).
\end{aligned}
\]

This proves the full theorem (1.1), and in particular (1.2).

Quadratic terms in `y` may be absorbed into the cell functions if the section hypotheses still hold. A mixed quadratic term `x dot Ay` changes the effective label map to `pi(y)+Ay`; the theorem applies if the fibres of that effective map satisfy the hypotheses. **We do not assert arbitrary mixed quadratic twisting preserves affine fibres.** Distinct original cells can acquire the same effective label, and ignoring that collision would invalidate (4.1).

## 9. Repeated gluing and integration with the existing results

The theorem may be applied recursively. Start with any family of Boolean functions carrying folded certificates bounded by a common constant `C_0`. At a construction step, use already-certified functions as all the physical sections required by an affine-fibre gluing, and allow a quadratic tag phase as in Section 8. Every finite resulting function satisfies

\[
 H\le \max\{4,C_0\}J.
\tag{9.1}
\]

Proof is induction on the finite construction: the local constant is changed only by `C -> max{4,C}`, an idempotent operation.

Disjoint products also retain the maximum constant, because both spectral entropy and folded influence add. The earlier isospectral physical-splice theorem is compatible with folded influence: identical child squared Fourier laws give identical child coordinate influences, zero entropy decrement, and parent folded influence equal to the child's folded influence plus a nonnegative queried term. Such splices therefore also preserve the same constant.

Consequently the new gluing operation can be interleaved, at arbitrary finite depth, with disjoint products and the already-proved zero-cost isospectral splices. Inserting the previous quadratic-twisted symmetric product cores with constant 12.04 retains **12.04** throughout. Inserting only characters/quadratic cores gives the sharp class constant **4**.

This is not a claim of closure under arbitrary physical restrictions. In particular, fixing tag coordinates can merge labels, destroy the distinct affine-fibre structure, and produce a function not certified by this argument. These are direct stopping-class certificates, not an unrestricted hereditary theorem.

## 10. Attempt at the full endpoint induction: a coefficientwise obstruction

The preceding scheduled continuation uses the endpoint potential

\[
 \Phi_n(f)=n\left(\sum_s|\widehat f(s)|^{2-1/n}-1\right).
\]

It leaves open the existence of a uniformly payable coordinate. One attempted way to prove that selector is to control each paired Walsh coefficient separately. This continuation shows that this stronger scalar payment cannot work.

Put

\[
 \psi_n(t)=n(t^{2-1/n}-t^2),\quad
 \delta_n=2^{1-n},\quad u_n=1-\delta_n,\quad v_n=\delta_n.
\]

The parent pair `(u_n,v_n)` comes from child coefficients `(1,1-2delta_n)`. These are not artificial forbidden amplitudes: they are the empty-set Fourier coefficients of a constant child and a child differing from it at one input on `n-1` bits. Define the scalar adaptive charge

\[
 T_n=\psi_n(1-\delta_n)+\psi_n(\delta_n)
       -\tfrac12\psi_{n-1}(1)-\tfrac12\psi_{n-1}(1-2\delta_n).
\]

### Proposition 10.1

\[
\boxed{\frac{T_n}{\delta_n^2}=n+\frac32-2\ln2+o(1).}
\tag{10.1}
\]

In particular no finite universal constant bounds this single-fibre charge by `C v_n^2`.

### Proof

At `t=1`,

\[
 \psi_n(1)=0,\quad\psi_n'(1)=-1,\quad\psi_n''(1)=-3+1/n.
\]

Third derivatives are uniformly bounded on `[1/2,1]` for `n>=3`, so Taylor's theorem gives, uniformly,

\[
 \psi_n(1-\delta)=\delta+\tfrac12(-3+1/n)\delta^2+O(\delta^3),
\]
\[
 \tfrac12\psi_{n-1}(1-2\delta)
 =\delta+(-3+1/(n-1))\delta^2+O(\delta^3).
\]

Also, exactly,

\[
 \frac{\psi_n(\delta_n)}{\delta_n^2}
 =n(2^{1-1/n}-1).
\]

Thus

\[
 \frac{T_n}{\delta_n^2}
 =n(2^{1-1/n}-1)+\frac32+\frac1{2n}-\frac1{n-1}+O(\delta_n).
\]

Expanding `2^{1-1/n}=2 exp[-(ln2)/n]` proves (10.1). QED.

This refutes only a proposed **coefficientwise** proof. The other spectral fibres of the same Boolean function supply compensating terms. The existing whole-function adaptive selector has not been refuted, and the earlier bounded one-point-defect result remains intact. Any successful endpoint proof must retain cancellation or a joint allocation between fibres rather than bound every pair by its own minority squared mass.

## 11. What remains to prove for unrestricted FEI

The new theorem pays affine-labelled dependent branches exactly, but arbitrary Boolean functions need not have an eligible nonempty tag block with affine fibres and certified physical sections. Expanding an arbitrary function into singleton pieces does not fix this: the tags required to distinguish those pieces change the function, and discarding or fixing them can merge spectral blocks and cancel boundary influence.

There are two live full-scope avenues, not claims of closure:

1. Prove a dimension-free physical restriction-tree allocation for general child-spectrum defects, including coherent collisions between pieces with the same label. The prior exact identity `Delta_i H=B_i+JS(P_i,Q_i)` and its Hellinger/KL rebate remain valid. The new class supplies additional rigorously certified stopping points.
2. Prove the dimension-adaptive whole-function endpoint selector while using genuine cross-fibre cancellation. Proposition 10.1 explains why an otherwise tempting scalar inequality cannot supply that proof.

For completeness, the inherited weighted-erasure target is still unproved:

\[
 \sum_iH(S_i\mid S_{-i})\le K I(f)
\]

for every Boolean function with one universal `K`. This continuation does not establish that estimate, a universal endpoint selector, or a decomposition theorem placing all Boolean functions in (9.1).

**Source-level status remains OPEN.** No numerical percentage of completion or unsupported forecast of a full proof is claimed.

## 12. Executed checks and reproducibility

Run `python verify_affine_fibres.py --output verification.json` from this directory. The included `verification.json` is the actual successful output of the included code.

- **233,530 structured partition/phase cases**, exhaustively covering all affine partitions of `F_2^m` for `0<=m<=3` and all cellwise quadratic sign tables, with canonical distinct binary labels. This includes 912 affine partitions for `m=3`, and checks the exact entropy/rank identity and constant-four bound by integer Walsh transforms. There were **700,392** corresponding physical `y`-coordinate cases. This is exhaustive for the stated structured enumeration, not all Boolean functions or all possible labelings.
- **240 reproducibly sampled arbitrary-core affine-fibre cases** in `1<=m<=7`, testing the exact entropy identity, physical-section deletion bound, and folded influence payment. These include **3,275 physical sections** and **942 exact boundary-coordinate identities**.
- The same 240 geometries also test an arbitrary quadratic tag phase, and another 240 cellwise-quadratic/tag-quadratic cases test `H<=4J`. These families overlap and should not be summed as distinct functions.
- Actual addressing truth tables with 3, 6 and 11 total variables verify (7.3) in those cases. The limiting sharpness statement is proved analytically, not by extrapolation.
- A separately labeled 120-digit Decimal probe illustrates (10.1) at `n=4,8,16,32,64`; it is not a rigorous numerical certificate and is not needed for its proof.

Walsh transforms and influence counts are integers. General entropy comparisons are first expressed as exact rational linear combinations of logarithms of odd integers, with matching terms cancelled symbolically. Each logarithm is then enclosed by the rational series

\[
 \ln x=2\sum_{j=0}^{47}\frac{z^{2j+1}}{2j+1}+R,
 \quad z=\frac{x-1}{x+1},\quad1\le x\le2,\quad
 0\le R\le\frac{2z^{97}}{97(1-z^2)}.
\]

The program fails on either a violated inequality or an unresolved interval. All stated exact checks passed. They are self-checks of a candidate analytical continuation, not independent review or a formal proof assistant verification.

Checker SHA-256: `6be939e2cf6dfb604408852e85fbf89c3fae08d0c77c82fc78058eff2e9fc995`.

No schedules, permissions, repository visibility, unrelated files, or previous results are changed by this continuation.
