# fleet01/B16 — signed valuation / influence-class KL reserve

**Run:** `20260922T104019Z-B16-auto11`  
**Programme:** `FEI-ALL-TEAM-20260922T095941Z`  
**Classification:** `ESSENTIAL_STEP_APPLIED / FULL_FEI_OPEN`  
**Execution:** `WITHOUT_VERIFIED_BRAIN`  
**Full uniform-cube FEI:** **OPEN / NOT PROVED**.

## 0. Exact target and before/after

The current Path-B identity is the source-exact influence I-projection

\[
R_\Gamma=B_{\rm inf}^\Gamma+K_{\rm occ},\qquad
K_{\rm occ}=D_{\rm KL,2}(P\Vert Q_r)=H_{\max}(r)-H(P),
\]

where `P` is the actual nonempty spectral law and `Q_r` is the maximum-entropy law with the same original-coordinate occurrence marginals. The universal FEI payment remains

\[
K_{\rm occ}\ge[-B_{\rm inf}^\Gamma]_+.
\]

The sparse-suspension theorem proves that losing any fixed fraction of `K_occ` is fatal, even with an `O(I)` auxiliary bank. The recursive-majority barrier proves that retaining all individually labelled atoms below a fixed or sub-half-depth cutoff and merging the rest loses essentially all of the required dependence payment.

**Before this run:** there was no source statistic in this slot simultaneously certified to (i) be a genuine data-processing reserve below `K_occ`, (ii) retain the sparse-defect rare-event logarithm with only `O(I)` loss, and (iii) survive the recursive-majority multiscale preflight.

**After this run:** the statistic below is a genuine nonnegative reserve below `K_occ`, has **zero** loss on every one-point-defect suspension, and also has **zero** loss on every depth of recursive ternary majority. The remaining universal gap is isolated exactly as an odd-part anisotropy KL inside signed Walsh-lattice fibers.

This does **not** prove FEI. It turns the assignment's requested logarithm-preserving reserve into a precise theorem and identifies the next unpaid implication.

## 1. Sources actually used

### 1.1 Canonical dependence KL

Fleet02/B15, immutable source

`yspennstate/math-open-problems@4bd6d05f1eb8325d665f2748f4d74dcee2550a04`

`proofnet24/P03-fei/fleet-2026-09-21/fleet02/B15/20260922T0829Z-influence-iprojection-kl/REPORT.md`

proves the unique influence-matched nonempty-product I-projection `Q_r` and

\[
K_{\rm occ}=D_2(P\Vert Q_r).
\]

### 1.2 Sparse suspension no-loss obstruction

Fleet02/B15, source snapshot containing

`proofnet24/P03-fei/fleet-2026-09-21/fleet02/B15/20260922T085941Z-suspension-kl-no-loss/REPORT.md`

proves for

\[
g_m(x)=1-2\mathbf 1_{\{x=0\}},\qquad F_m(y,x)=y g_m(x),
\]

that

\[
\frac{K_{\rm occ}(F_m)}{I(g_m)}
=m-5+\frac1{\ln2}+o(1),
\]

and any fixed fractional loss of `K_occ` cannot be repaired by a dimension-independent `O(I)` bank.

### 1.3 Recursive-majority mandatory preflight

Fleet03/B18, immutable source

`yspennstate/math-open-problems@bff0d7b6c21485f386841c42582eb04f32705046`

`proofnet24/P03-fei/fleet-2026-09-21/fleet03/B18/20260922T100641Z-lowlevel-projection-barrier/REPORT.md`

proves that for depth-`m` recursive ternary majority, fixed/sub-half-depth labelled KL projections capture a vanishing fraction of the required dependence payment. It also gives

\[
r_i=2^{-m},\qquad I(M_m)=(3/2)^m,\qquad H(M_m)=4((3/2)^m-1).
\]

### 1.4 Named partner result consumed and applied

The latest compatible completed fleet02/B16 theorem used here is

`yspennstate/math-open-problems@730731281a24e70b01b4021a90ff758575414db1`

`proofnet24/P03-fei/fleet-2026-09-21/fleet02/B16/20260921T152751Z-qflip-channel-density/REPORT.md`.

It proves the physical q-flip radial multiplier identity

\[
\mathbb E_{\mathcal B}Q_{\mathcal B}(f)
=
\frac12\sum_i\sum_{\varnothing\ne T}\widehat{\tau_i}(T)^2K_{n-1}(|T|),
\]

with `K_m(k)` strictly increasing in the Walsh Hamming layer `k`. I use this exact expression as follows: in the equal-influence stress families below, the I-projection price is a function only of the same Hamming layer variable. Thus the partner theorem identifies the radial layer as a genuinely physical Walsh observable, while the present construction changes the **weighting** from an unweighted quadratic channel count to the exact logarithmic KL price. The partner theorem itself already shows why counting alone cannot supply the rare logarithm; the new reserve retains the layer but adds signed lattice information and KL weighting.

## 2. Signed Walsh lattice and influence classes

Let

\[
f:\{-1,1\}^n\to\{-1,1\}
\]

be balanced under the uniform measure. Write normalized Walsh coefficients as `fhat(S)` and define the integer Walsh amplitudes

\[
A_S:=2^n\widehat f(S)\in\mathbb Z.
\]

Balancedness gives `A_empty=0`, and Parseval gives the probability law

\[
P(S)=\widehat f(S)^2=\frac{A_S^2}{4^n}
\qquad(S\ne\varnothing).
\]

Let

\[
r_i=P(i\in S)=\operatorname{Inf}_i(f),
\]

and let `Q_r` be the source-defined maximum-entropy nonempty law with these marginals.

Partition the coordinates into exact influence classes

\[
C_1,\ldots,C_d,
\qquad i,j\in C_a\iff r_i=r_j.
\]

For a Walsh label `S`, put

\[
k_a(S):=|S\cap C_a|,
\qquad
\mathbf k_r(S)=(k_1(S),\ldots,k_d(S)).
\]

For a nonzero integer `A`, write

\[
A=\operatorname{sgn}(A)\,2^{\nu_2(A)}u(A),
\]

where `u(A)` is positive and odd. For `A=0`, use a distinguished zero symbol.

Define the **signed valuation / influence-class statistic**

\[
\boxed{
Z_f(S)=
\left(
\operatorname{sgn}A_S,\ 
u_2(|A_S|),\ \mathbf k_r(S)
\right),
}
\tag{2.1}
\]

with the zero symbol when `A_S=0`.

Finally define

\[
\boxed{
K_{\rm SVIC}(f)
:=D_{\rm KL,2}\bigl((Z_f)_\#P\Vert(Z_f)_\#Q_r\bigr).
}
\tag{2.2}
\]

This is a true source statistic: it uses the actual signed integer Walsh coefficients, their exact 2-adic lattice depth, and only the counts of selected coordinates inside equal-influence classes. It does not retain arbitrary coordinate labels inside a class.

## 3. Main theorem — exact KL disintegration

### Theorem 3.1 (`B16-SVIC-KL-RESERVE-v1`)

For every balanced uniform-cube Boolean function,

\[
\boxed{0\le K_{\rm SVIC}(f)\le K_{\rm occ}(f).}
\tag{3.1}
\]

More precisely, for each occupied statistic value

\[
z=(\sigma,v,\mathbf k),
\]

let

\[
\mathcal F_z:=\{S:Z_f(S)=z\},
\qquad m_z:=|\mathcal F_z|.
\]

For `S in F_z`, write

\[
A_S=\sigma 2^v u_S,
\qquad u_S\in2\mathbb Z+1,\ u_S>0,
\]

and define

\[
\pi_z(S)=\frac{u_S^2}{\sum_{T\in\mathcal F_z}u_T^2}.
\]

Then

\[
\boxed{
K_{\rm occ}(f)-K_{\rm SVIC}(f)
=
\sum_{z:(Z_f)_\#P(z)>0}
(Z_f)_\#P(z)
\left[\log_2m_z-H_2(\pi_z)\right].
}
\tag{3.2}
\]

In particular,

\[
\boxed{
K_{\rm SVIC}(f)=K_{\rm occ}(f)
}
\tag{3.3}
\]

whenever the odd part `u_S` is constant on each occupied signed-valuation/influence-class fiber.

### Proof

The inequality (3.1) is the data-processing inequality for relative entropy applied to the deterministic map `Z_f`.

For the exact loss, use the chain rule

\[
D(P\Vert Q_r)
=
D(Z_\#P\Vert Z_\#Q_r)
+
\mathbb E_{z\sim Z_\#P}
D(P(\cdot\mid z)\Vert Q_r(\cdot\mid z)).
\tag{3.4}
\]

The nontrivial point is that `Q_r` is **uniform inside every fiber F_z**. Indeed, the source I-projection is a conditional product law. Hence its atom probability depends on a label `S` only through which coordinate-marginal values occur and how many coordinates from each equal-`r` class are selected. That information is exactly `k_r(S)`. Therefore all `S in F_z` have the same `Q_r(S)`, and

\[
Q_r(S\mid z)=\frac1{m_z}.
\tag{3.5}
\]

On the other hand, inside `F_z`, sign and 2-adic valuation are fixed, so

\[
P(S)\propto A_S^2=2^{2v}u_S^2.
\]

Thus

\[
P(S\mid z)=\pi_z(S).
\tag{3.6}
\]

Substitute (3.5)--(3.6) into (3.4):

\[
D(\pi_z\Vert\mathrm{Unif}(\mathcal F_z))
=
\log_2m_z-H_2(\pi_z),
\]

which gives (3.2). Equality is exactly the vanishing of every conditional divergence, equivalently constant odd part on each occupied fiber. `QED`.

### Interpretation

The missing piece after this theorem is no longer an unspecified “Walsh lattice reserve.” It is the explicit nonnegative **odd-part anisotropy loss**

\[
\Delta_{\rm odd}(f)
:=K_{\rm occ}(f)-K_{\rm SVIC}(f).
\tag{3.7}
\]

Valuation depth by itself can be zero while `K_occ` is huge. The new reserve retains the *logarithmic occupancy-class price* as well as signed valuation, so that the rare-event logarithm can survive even when the valuation coordinate is constant.

## 4. Sparse one-point-defect suspension — zero loss, exact rare logarithm

Take the source family

\[
g_m(x)=1-2\mathbf1_{\{x=0\}},
\qquad
F_m(y,x)=y g_m(x),
\qquad \alpha=2^{-m}.
\]

The exact Fourier coefficients are

\[
\widehat F_m(\{y\})=1-2\alpha,
\qquad
\widehat F_m(\{y\}\cup T)=-2\alpha
\quad(T\ne\varnothing).
\]

In total dimension `m+1`, the Walsh integers are therefore

\[
A_{\{y\}}=2^{m+1}-4
=4(2^{m-1}-1),
\]

and

\[
A_{\{y\}\cup T}=-4
\quad(T\ne\varnothing).
\]

The I-projection marginals are

\[
r_y=1,
\qquad r_i=2\alpha\quad(1\le i\le m).
\]

Hence all old coordinates lie in one influence class. Every occupied fiber with `T != empty` is determined by

\[
\operatorname{sgn}=-1,\qquad
\nu_2=2,\qquad |T|=k,
\]

and has odd part `u_S=1` identically. The `T=empty` fiber contains one atom only. Therefore every conditional divergence in (3.2) vanishes:

\[
\boxed{
K_{\rm SVIC}(F_m)=K_{\rm occ}(F_m)
\quad\text{for every }m\ge2.
}
\tag{4.1}
\]

Combining this with the source asymptotic gives

\[
\boxed{
\frac{K_{\rm SVIC}(F_m)}{I(g_m)}
=m-5+\frac1{\ln2}+o(1).
}
\tag{4.2}
\]

So the new reserve retains the entire rare-event logarithm that the unweighted convolution `L2` energy and valuation-depth tails miss. Its loss on the mandatory sparse-suspension barrier is not merely `O(I)`; it is exactly zero.

## 5. Recursive ternary majority — the multiscale barrier is also passed exactly

Let `M_1=Maj_3` and `M_m` be depth-`m` disjoint recursive ternary majority. The source gives

\[
r_i=2^{-m}
\]

for every physical coordinate. Thus there is only one influence class and the class-count coordinate of `Z_f` is simply `|S|`.

The remaining fact is an exact signed-Walsh statement.

### Lemma 5.1 — every nonzero recursive-majority coefficient is a signed power of two

For every `m` and every `S` with `fhat_m(S) != 0`,

\[
\boxed{|\widehat M_m(S)|=2^{-a_m(S)}}
\tag{5.1}
\]

for an integer `a_m(S)>=1`.

#### Proof

For `m=1`,

\[
Maj_3(x_1,x_2,x_3)
=\frac{x_1+x_2+x_3-x_1x_2x_3}{2},
\]

so every nonzero coefficient has magnitude `1/2`.

Inductively write

\[
M_{m+1}=\frac{F_1+F_2+F_3-F_1F_2F_3}{2},
\]

where the `F_j` are copies of `M_m` on disjoint blocks. Every `F_j` is balanced. Hence a Fourier label at the new root can be nonzero only in one of two mutually exclusive ways:

1. it occupies exactly one top block, in which case its coefficient is `1/2` times one child coefficient;
2. it occupies all three top blocks, in which case its coefficient is `-1/2` times the product of the three child coefficients.

There is no collision between these cases and no two-block term. By induction every resulting nonzero magnitude is again a power of two. `QED`.

Since the total dimension is `N_m=3^m`, the Walsh integer

\[
A_S=2^{N_m}\widehat M_m(S)
\]

is therefore a signed power of two. Its odd part is identically one on the nonzero spectrum. The odd-part anisotropy loss (3.7) vanishes identically, and hence

\[
\boxed{
K_{\rm SVIC}(M_m)=K_{\rm occ}(M_m)
\quad\text{for every depth }m.
}
\tag{5.2}
\]

This directly passes the current mandatory preflight. Unlike a fixed low-level projection, `Z_f` retains the full multiscale/high-cardinality dependence on recursive majority through the exact valuation and shell coordinates.

Using the source identity `H(M_m)=4(I(M_m)-1)`, this means the reserve retains the entire canonical dependence credit

\[
H_{\max}(r^{(m)})-4((3/2)^m-1),
\]

not a vanishing low-level fraction.

## 6. Relation to the partner q-flip radial theorem

The fleet02/B16 q-flip theorem proves that an actual physical random q-flip channel samples derivative Walsh layers through the strictly increasing radial kernel `K_{n-1}(|T|)`. In the equal-influence families above, `Q_r` is exchangeable, so its atom price is also radial:

\[
-\log_2Q_r(S)
=\text{constant}+|S|\log_2\frac{1-t}{t}.
\]

Thus the same physical radial variable that partner B16 found in the q-flip channel law becomes a **logarithmic entropy price** here. This explains why the present reserve succeeds on the one-point defect while the partner's unweighted channel count is only `O(J)`: the relevant multiplier is not a bounded channel-incidence weight but a KL price growing like the rare-event logarithm.

The present theorem does not claim that every `Z_f` fiber is directly observable by one q-flip experiment. The physical claim used from the partner is only the exact radial-layer identity and its strict ordering.

## 7. Tensor and equality-endpoint checks

If two Boolean factors have pure-power nonzero Walsh integers, their disjoint product again has pure-power Walsh integers because

\[
A_{S_1\cup S_2}^{f_1f_2}=A_{S_1}^{f_1}A_{S_2}^{f_2}.
\]

Thus the zero-odd-part-loss property is stable on this pure-power subclass, even though the universal FEI hierarchy still requires the separate composition KL ledger.

The exact `K_occ=0` family classified by fleet03/B15 (character times bent) is consistent with this theorem: its flat nonzero Walsh magnitude gives zero odd-part anisotropy, while of course both `K_occ` and `K_SVIC` are zero.

These checks do not replace the source hierarchy theorem and do not assert a universal tensor payment.

## 8. What is and is not solved

### Newly proved

`B16-SVIC-KL-RESERVE-v1`:

\[
0\le K_{\rm SVIC}\le K_{\rm occ},
\]

with the exact loss formula (3.2). The reserve is **exact** on:

- every sparse one-point-defect suspension `F_m`, retaining the full `m I` rare-event logarithm;
- every depth of recursive ternary majority, retaining the full multiscale dependence KL;
- more generally, every balanced Boolean source whose Walsh odd part is constant on each signed valuation / equal-influence-class occupancy fiber.

### Not proved

No universal bound of the form

\[
\Delta_{\rm odd}(f)\le C_0 I(f)
\]

has been established. No theorem here says `K_SVIC` alone pays `[-B_inf^Gamma]_+` for every balanced Boolean source. Addressing/tribes and the known unequal-magnitude physical-lattice constructions remain necessary adversarial tests for that next statement. Off-center biased gates require a separate non-dyadic analogue; this report does not pretend the uniform integer lattice survives arbitrary product bias.

### Exact next unpaid implication

The next B16 target is now precise:

> Prove, in the dangerous balanced deficit region, that the odd-part anisotropy loss
> \[
> \Delta_{\rm odd}
> =\sum_zP_Z(z)[\log_2m_z-H_2(\pi_z)]
> \]
> is either `O(I)` or is itself paid by an already-retained hierarchy / signed-Booleanity credit; otherwise construct a genuine Boolean family with `Delta_odd/I -> infinity` that defeats this reserve.

That is a materially smaller and source-exact question than recovering the rare-event logarithm from an unweighted norm: the two current universal stress families already have `Delta_odd=0` identically.

## 9. Diagnostic computation

`CHECK.py` checks the formula on the sparse suspension for `m=2,...,8` and on recursive majority at depths one and two. It also verifies that the recursive-majority Walsh integers encountered are pure powers of two. The recorded run prints `PASS`; the numerical equality errors are at floating roundoff scale. The finite diagnostic is implementation evidence only. The statements (3.1)--(5.2) are analytic.

## 10. Result classification

**Old missing implication:** find a source-valid logarithmically weighted dependence reserve below `K_occ` that is not killed by the sparse-suspension or recursive-majority barriers.

**New implication established:** `K_SVIC` is such a reserve and is exactly equal to `K_occ` on both mandatory barrier families.

**Remaining implication:** control the explicit odd-part anisotropy loss on arbitrary balanced Boolean sources, then connect the resulting reserve to the exact Bellman deficit. Full FEI remains open.
