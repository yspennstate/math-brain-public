# fleet02/B15 — logarithmic magnitude/price compiler with influence-paid KL loss

**Run:** `20260922T103316Z-fleet02-B15-r11`  
**Classification:** `ESSENTIAL_STEP_APPLIED / LOG_KL_COMPILER / FULL_FEI_OPEN`  
**Execution:** `WITHOUT_VERIFIED_BRAIN`.  
**Full unrestricted uniform-cube FEI:** **OPEN / NOT PROVED**.

## 0. Current target and exact movement

The later owner control `2026-09-22.3` assigns this slot the Path-B task **Sparse-suspension logarithmic compiler**. The canonical FEI state keeps the exact I-projection residual
\[
R_\Gamma=B_{\rm inf}^{\Gamma}+K_{\rm occ},
\qquad
K_{\rm occ}=D_{\rm KL,2}(P\Vert Q_r)=H_{\max}(r)-H(P),
\tag{0.1}
\]
and the balanced-uniform endpoint
\[
\mathcal R_C(f)
=K_{\rm occ}(f)+C[I(f)-1]-H_{\max}(r)
=C[I(f)-1]-H(f).
\tag{0.2}
\]
Thus the first missing Shannon implication remains
\[
\boxed{
K_{\rm occ}(f)\ge H_{\max}(r)-C[I(f)-1]
}
\tag{0.3}
\]
whenever the right side is positive.

The last three completed substantive fleet02/B15 mechanisms relevant here were:

1. `20260922T0704Z-gibbs-kl-prime-tube`: exact gate-global Gibbs KL / packet-price factorization;
2. `20260922T0829Z-influence-iprojection-kl`: exact original-coordinate I-projection, leaving the potential-independent dependence credit `K_occ`;
3. `20260922T085941Z-suspension-kl-no-loss`: the suspension face is an isometric copy of FEI, and any usable compression must lose only `O(I(g))` KL on sparse defects.

No completed mathematical report was found for the later `20260922T1006Z-fleet02-B15-r15` operational start, so it is not counted as a substantive predecessor.

**FULL-PROBLEM CHANGE:** `OPEN -> OPEN`.

**MECHANISM CHANGE:** `exact-KL no-loss obstruction -> source-defined logarithmic magnitude/original-coordinate-price quantization with a proved <=2 excess-influence loss, plus exact multiscale cell compilers on the two canonical stress families`.

**TARGET-LEVEL CHANGE:** the explicit compiler sub-obligation demanded by the sparse-suspension no-loss theorem,
\[
K_{\rm occ}-\widetilde K=O(I(g)),
\tag{0.4}
\]
is now solved on **every Boolean character suspension** with constant `2`, while retaining `\widetilde K` as a genuine negative relative-entropy credit. The universal payment (0.3) for arbitrary balanced Boolean sources remains open.

This is not a relabeling of `K_occ`: `\widetilde K` is the KL of an explicit coarse statistic, and the omitted conditional KL is separately bounded by physical influence.

## 1. Named completed OTHER-account result consumed

The newest compatible fleet03/B15 result actually read and used is

`proofnet24/P03-fei/fleet-2026-09-21/fleet03/B15/20260922T092409Z-complement-packet-kl-gap/REPORT.md`

at commit `2c1afb444c3a4fa2cbee12f73fd8c19c44af9e56`.

It proves a complement-packet Boolean KL gap on the `c<1` branch of the I-projection, but explicitly leaves the `c=1` quantitative branch unresolved. That hypothesis is **exactly incompatible** with the sparse-suspension face: for
\[
F(y,x)=y\,g(x)
\]
the fresh coordinate has occurrence marginal `r_y=1`, and the I-projection equation forces `c=1`. Thus the partner theorem cannot supply the needed sparse rare-event logarithm. The present run attacks that precise missing `c=1` corridor by a different information mechanism.

I also use fleet04/B15's completed `20260922T093820Z-full-convolution-energy-obstruction` (commit `7ec649dfb3d1ab2f92855f2069590fca2ac956dd`) as a design constraint: on the same sparse suspension the entire unweighted signed convolution `L2` energy is only `O(I(g))` while `K_occ=Theta(m I(g))`. Therefore the statistic below preserves **log likelihood scale itself** instead of rescaling quadratic energy.

## 2. A two-bit logarithmic KL compiler

The elementary lemma below is the information-theoretic engine.

### Lemma 2.1 — mass-weighted log-bin loss

Let `P<<Q` be probability laws on a finite set `Omega`, and let `A subset Omega` be a set of atoms retained individually. For every `x notin A` with `P(x)>0`, define
\[
U(x)=\left\lfloor-\log_2P(x)\right\rfloor,\qquad
V(x)=\left\lfloor-\log_2Q(x)\right\rfloor .
\]
Let `sigma(x)` be any additional source label (in the Boolean application it is the actual Fourier sign). Define a statistic `Z` which:

* gives every atom of `A` its own label;
* gives every `P(x)=0` atom a separate zero-source label; and
* otherwise records `(sigma(x),U(x),V(x))`.

Then
\[
\boxed{
0\le D(P\Vert Q)-D(Z_\#P\Vert Z_\#Q)
\le 2P(A^c).
}
\tag{2.1}
\]

#### Proof

The KL chain rule gives
\[
D(P\Vert Q)
=
D(Z_\#P\Vert Z_\#Q)
+\sum_zP_Z(z)D(P(\cdot\mid z)\Vert Q(\cdot\mid z)).
\tag{2.2}
\]
Singleton fibres in `A` contribute zero, as does every fibre of zero `P`-mass.

On any remaining fibre, the two floor bins imply that both `P(x)` and `Q(x)` vary by factors strictly smaller than `2`. Therefore the likelihood ratio
\[
L(x)=P(x)/Q(x)
\]
varies across the fibre by a factor strictly smaller than `4`. The cell average `P_Z(z)/Q_Z(z)` is a `Q(\cdot|z)`-weighted average of `L`, hence lies between the minimum and maximum `L` in the cell. Consequently
\[
\frac{P(x\mid z)}{Q(x\mid z)}
=
\frac{L(x)}{P_Z(z)/Q_Z(z)}
<4,
\]
so each conditional divergence in (2.2) is at most `2` bits. Summing only over `A^c` gives (2.1). `QED`

This lemma spends the **discarded** negative information credit quantitatively rather than dropping it.

## 3. Character suspensions: the lost KL is at most twice the excess influence

Let
\[
g:\{-1,1\}^m\to\{-1,1\},\qquad
F(y,x)=y\,g(x)
\tag{3.1}
\]
with `y` a fresh unbiased bit. Put
\[
P(T)=\widehat g(T)^2,\qquad
j_i=\operatorname{Inf}_i(g),
\qquad
Q(T)=\prod_{i\in T}j_i\prod_{i\notin T}(1-j_i).
\tag{3.2}
\]
As proved in the previous B15 suspension theorem, this `Q` is exactly the old-coordinate factor of the complete I-projection of `F`, and
\[
K_{\rm occ}(F)=D(P\Vert Q),\qquad
I(F)-1=I(g)=\sum_i j_i.
\tag{3.3}
\]

Contract deterministic old coordinates if necessary, and apply Lemma 2.1 with the Fourier-empty atom retained individually and with
\[
\sigma(T)=\operatorname{sgn}\widehat g(T).
\tag{3.4}
\]
Denote the resulting projected KL by `K_log(F)`.

### Theorem 3.1 — `B-CHAR-SUSPENSION-LOG-COMPILER-v1`

For **every** Boolean `g`,
\[
\boxed{
0\le K_{\rm occ}(F)-K_{\log}(F)
\le
2\operatorname{Var}(g)
\le
2I(g)
=
2[I(F)-1].
}
\tag{3.5}
\]

#### Proof

Under the spectral law,
\[
P(T\ne\varnothing)
=
1-\widehat g(\varnothing)^2
=
\operatorname{Var}(g).
\]
Equation (2.1) with `A={emptyset}` gives the first inequality. The uniform-cube Poincare inequality
\[
\operatorname{Var}(g)\le\sum_i\operatorname{Inf}_i(g)
\]
gives the second. `QED`

Hence the exact common residual has the source-exact decomposition
\[
\boxed{
R_C(F)
=
B_{\rm inf}^C(F)
+
K_{\log}(F)
+
L_{\log}(F),
\qquad
0\le L_{\log}(F)\le2[I(F)-1].
}
\tag{3.6}
\]
This is the requested **influence payment for the omitted relative entropy**. The retained term `K_log` remains a bona fide negative KL credit of an explicit signed-source statistic; no product normalizer, physical projection integrality, valuation-depth proxy, or unweighted `L2` replacement is used.

The theorem applies to every character suspension, not only a one-point defect.

## 4. Sparse one-point defects: exact degree compiler and actual finite-center payment

Take the genuine Boolean family used in the no-loss and `L2` obstruction reports:
\[
p=2^{1-m},\qquad
g_m(x)=1-2{\bf1}_{\{x=0\}},\qquad
F_m(y,x)=y\,g_m(x),\qquad m\ge2.
\tag{4.1}
\]
Then
\[
\widehat g_m(\varnothing)=1-p,\qquad
\widehat g_m(T)=-p\quad(T\ne\varnothing),
\tag{4.2}
\]
every old influence is `p`, and
\[
J:=I(g_m)=mp.
\tag{4.3}
\]
The I-projection old factor is exactly iid `Bernoulli(p)`.

Let `K=|T|`. Both actual and reference atom probabilities are constant on each degree:
\[
P(T)=
\begin{cases}
(1-p)^2,&T=\varnothing,\\
p^2,&T\ne\varnothing,
\end{cases}
\qquad
Q(T)=p^{|T|}(1-p)^{m-|T|}.
\tag{4.4}
\]
Therefore the degree itself is a sufficient statistic for the likelihood ratio:
\[
\boxed{
K_{\rm occ}(F_m)=D(P_K\Vert Q_K).
}
\tag{4.5}
\]
Explicitly,
\[
P_K(0)=(1-p)^2,\qquad
P_K(k)=\binom mkp^2\quad(k\ge1),
\tag{4.6}
\]
while `Q_K=Bin(m,p)`. Thus the rare-event logarithm survives with **zero** compression loss, unlike every fixed fractional KL recovery or unweighted convolution-energy compression.

The exact entropy is
\[
H(g_m)
=
2(1-p)^2\log_2\frac1{1-p}
+
2(2p-p^2)(m-1).
\tag{4.7}
\]
Moreover
\[
\boxed{H(g_m)<4mp=4J.}
\tag{4.8}
\]
Indeed, writing `L=log_2(1/(1-p))` and using
\[
L\le {p\over(1-p)\ln2},
\]
one obtains
\[
\begin{aligned}
4J-H(g_m)
&=4p+2p^2(m-1)-2(1-p)^2L\\
&\ge
2p\left[2+p(m-1)-{1-p\over\ln2}\right]\\
&>
2p\left(2-{1\over\ln2}\right)>0.
\end{aligned}
\tag{4.9}
\]

Consequently the **coarse** logarithmic compiler of Theorem 3.1 already pays the common residual at the fixed finite center `C=6`:
\[
\boxed{
B_{\rm inf}^{6}(F_m)+K_{\log}(F_m)
\ge
6J-H(g_m)-2J
=
4J-H(g_m)
>0.
}
\tag{4.10}
\]
The still stronger exact degree compiler pays it already at `C=4`:
\[
\boxed{
B_{\rm inf}^{4}(F_m)+D(P_K\Vert Q_K)
=
4J-H(g_m)>0.
}
\tag{4.11}
\]
This closes the previously adversarial sparse-suspension family for the **compiler mechanism** without dropping the negative KL. It is not a proof of unrestricted FEI.

## 5. Exact block-equal-influence compiler

There is a broader exact structural statement.

Suppose a balanced Boolean source has its physical coordinates partitioned into classes
\[
B_1,\dots,B_\ell
\]
such that the occurrence marginal `r_i` is constant inside each class. The I-projection atom probability `Q_r(S)` then depends only on the count vector
\[
\kappa(S)=\bigl(|S\cap B_1|,\dots,|S\cap B_\ell|\bigr).
\]
The actual spectral atom probability is `P(S)=|\widehat f(S)|^2`. Therefore, after optionally retaining the actual Fourier sign, the statistic
\[
\boxed{
Z_{\rm cell}(S)
=
\left(
\operatorname{sgn}\widehat f(S),
|\widehat f(S)|,
\kappa(S)
\right)
}
\tag{5.1}
\]
is sufficient for `P/Q_r`, because that likelihood ratio is constant on every fibre. Hence
\[
\boxed{
D(P\Vert Q_r)
=
D((Z_{\rm cell})_\#P\Vert(Z_{\rm cell})_\#Q_r).
}
\tag{5.2}
\]
For a bounded number of influence types this replaces all physical-coordinate labels by finitely many occupancy counts while preserving **all** of `K_occ`.

This is an exact arithmetic/entropy disintegration, not a valuation-tail claim. In particular, dyadic magnitude does not imply an integral physical projection anywhere in the argument.

## 6. Mandatory recursive-majority preflight: the compiler retains the missing high-cardinality KL

Fleet03/B18's completed `20260922T100641Z-lowlevel-projection-barrier` (commit `bff0d7b6c21485f386841c42582eb04f32705046`) proves that fixed or sub-half-depth labelled projections recover a vanishing fraction of the required `K_occ` on recursive ternary majority. The present compiler survives that barrier because it is genuinely multiscale rather than low-level.

Let `M_d` be depth-`d` recursive `Maj_3`, where
\[
\operatorname{Maj}_3(x_1,x_2,x_3)
={x_1+x_2+x_3-x_1x_2x_3\over2}.
\tag{6.1}
\]
Every leaf influence is
\[
r=2^{-d},\qquad
n=3^d,\qquad
I(M_d)=(3/2)^d.
\tag{6.2}
\]
Every nonzero Fourier magnitude is dyadic. Define the active-node exponent `A_d(S)` by
\[
|\widehat M_d(S)|=2^{-A_d(S)}.
\tag{6.3}
\]
If
\[
N_d(k,a)=\#\{S:|S|=k,\ A_d(S)=a\},
\]
then
\[
N_1(1,1)=3,\qquad N_1(3,1)=1,
\tag{6.4}
\]
and disjoint composition gives the exact recurrence
\[
\boxed{
N_{d+1}(k,a)
=
3N_d(k,a-1)
+
\!\!\!\sum_{\substack{k_1+k_2+k_3=k\\a_1+a_2+a_3=a-1}}
\prod_{j=1}^3N_d(k_j,a_j).
}
\tag{6.5}
\]
Because all influences are equal, the I-projection atom probability depends only on `k`. Hence `(sign,A_d,|S|)` is an exact instance of (5.1):
\[
\boxed{
K_{\rm occ}(M_d)
=
D\!\left((A_d,|S|,\operatorname{sgn}\widehat M_d)_\#P
\middle\|
(A_d,|S|,\operatorname{sgn}\widehat M_d)_\#Q_r
\right).
}
\tag{6.6}
\]

The expected active-node exponent obeys
\[
e_{d+1}=1+\frac32e_d,\qquad e_1=1,
\]
so
\[
e_d=2\bigl((3/2)^d-1\bigr).
\tag{6.7}
\]
Therefore
\[
\boxed{
H(M_d)=2e_d=4[I(M_d)-1].
}
\tag{6.8}
\]
The compiled KL consequently pays the exact balanced demand at `C=4`:
\[
\boxed{
B_{\rm inf}^{4}(M_d)+K_{\rm cell}(M_d)=0
}
\tag{6.9}
\]
for every depth. Thus the recursive-majority obstruction is specifically to **low-level** KL extraction; it is not an obstruction to the multiscale magnitude/occupancy compiler.

## 7. Composition credit and what remains

The completed fleet04/B15 hierarchy theorem `20260922T091017Z-iprojection-composition-transfer` (commit `2bf247373576eb406ca91bb3ea5f3ce5e5ab8588`) proves
\[
K_{\rm occ}(G(f_1,\ldots,f_s))
=
K_{\rm occ}(G)
+\sum_i\alpha_iK_{\rm occ}(f_i)
+C_{\rm hier},
\qquad
C_{\rm hier}\ge0,
\tag{7.1}
\]
with `C_hier` itself an explicit KL divergence, and the actual FEI remainder composes exactly. Therefore the new compiler must be transported through composition **with** this hierarchy credit; it is not legitimate to keep only local compiled KL values. The present run does not drop `C_hier`.

The new exact remaining obligation is no longer “find any statistic that keeps the sparse rare-event logarithm.” That subproblem is solved on the suspension face. The universal next step is:

\[
\boxed{
\text{construct a global/recursive compiler }\widetilde K(f)\le K_{\rm occ}(f)
\text{ with }
K_{\rm occ}(f)-\widetilde K(f)
\le L[I(f)-1]
}
\tag{7.2}
\]
for all balanced Boolean `f` with one finite `L`, **while retaining the hierarchy KL under restriction/composition**, and then prove that the retained `\widetilde K` pays the negative first-moment term. The character-suspension theorem proves (7.2) with `L=2` on an infinite codimension-one Boolean class, and the block-equal-influence theorem has `L=0` on its exact cell statistic. Neither statement is the unrestricted FEI theorem.

## 8. Deterministic self-check

A standard-library checker verifies:

* sparse defects for `2<=m<=30`: degree KL equals `K_occ` to floating residual below `1.2e-16`, and `4I(g_m)-H(g_m)>0`;
* recursive ternary majority for depths `1<=d<=4`: the cell recursion normalizes, gives `H=4(I-1)`, and the cell KL agrees with `Hmax-H` to residual below `2.4e-14`.

Representative values include

* sparse `m=24`: `H/J=3.95355767009178`, `K_occ/J=20.4891372848059`;
* recursive majority `d=4`: `I=5.0625`, `H=16.25`, `K_occ=11.062616258208`.

These are implementation checks only. Lemma 2.1 and Theorems 3.1, 4.5/4.8, 5.2, and the recursive-majority recursion/payment are analytic.

## 9. Source pins and status

Mathematical premises used in this report:

* fleet02/B15 I-projection theorem: `yspennstate/math-open-problems@4bd6d05f1eb8325d665f2748f4d74dcee2550a04`, `proofnet24/P03-fei/fleet-2026-09-21/fleet02/B15/20260922T0829Z-influence-iprojection-kl/REPORT.md`;
* fleet02/B15 suspension no-loss theorem: `yspennstate/math-open-problems@730731281a24e70b01b4021a90ff758575414db1`, `.../20260922T085941Z-suspension-kl-no-loss/REPORT.md`;
* fleet03/B15 complement packet theorem: `yspennstate/math-open-problems@2c1afb444c3a4fa2cbee12f73fd8c19c44af9e56`, `.../fleet03/B15/20260922T092409Z-complement-packet-kl-gap/REPORT.md`;
* fleet04/B15 hierarchy theorem: `yspennstate/math-open-problems@2bf247373576eb406ca91bb3ea5f3ce5e5ab8588`, `.../fleet04/B15/20260922T091017Z-iprojection-composition-transfer/REPORT.md`;
* fleet04/B15 full-L2 obstruction: `yspennstate/math-open-problems@7ec649dfb3d1ab2f92855f2069590fca2ac956dd`, `.../fleet04/B15/20260922T093820Z-full-convolution-energy-obstruction/REPORT.md`;
* fleet03/B18 recursive-majority low-level barrier: `yspennstate/math-open-problems@bff0d7b6c21485f386841c42582eb04f32705046`, `.../fleet03/B18/20260922T100641Z-lowlevel-projection-barrier/REPORT.md`.

No novelty or priority claim is made. The abstract finite-partition KL chain rule is elementary; the contribution here is its source-exact logarithmic compiler specialization, the `2[I(F)-1]` suspension loss payment, and the exact sparse/recursive-majority applications in the current FEI ledger.
