# B16 FEI signed transport — parity-current Walsh-frame diagonalisation

**Date:** 21 September 2026  
**Scope:** `account04 / B16`, FEI signed transport proof  
**Execution:** **WITHOUT_VERIFIED_BRAIN**  
**Status of unrestricted FEI:** **OPEN / NOT PROVED**  
**Claim level:** exact signed parity-current identities and a new averaged square-function reduction. No novelty or publication-priority claim.

## 0. Fresh entering state and route

This run continues the newest compatible signed-transport state rather than restarting an older shortcut.

The immediate inputs are:

1. the exact signed R32 q-flip parity compiler and the active-syndrome Walsh/Bernoulli representation;
2. the paired-selector theorem: ordinary fine-player Shapley minus the dummy-invariant block-coupled selector is pure third-and-higher curvature;
3. the newer double-resolvent theorem: that selector defect is the divergence of a signed minimum current and all higher orders resum exactly into third finite differences of the plaquette-plus-terminal field;
4. the newest arbitrary-pivot q-flip theorem: every q-flip derivative-disagreement kernel is conditionally negative type and has the same central odd Radon square payment as a physical-coordinate pivot;
5. the frame warning: unit-weight summation over arbitrary q-flip pivots can grow with dimension, so the compiler must supply normalization or signed cancellation.

The calculation below identifies an exact normalization mechanism already inside the parity selector. It is relationwise, preserves signs, and diagonalizes cross-relation current energy under the natural syndrome translation. It does **not** yet prove the final original-coordinate influence payment.

The three FLEET_RULES moves used deliberately are **#11 DUALIZE** (pass from the signed current to its syndrome-Walsh multiplier), **#14 FIND THE GROUP ACTING** (average over the syndrome-translation group so distinct parity characters diagonalize exactly), and **#20 FIND WHY THE ALGORITHM FAILS** (construct an exponential pointwise cross-term amplification showing why the translation/frame step cannot be omitted).

No R32 coefficient is positive-parted. The terminal code remains outside the current and retains its separate payment. Dual-code multiplicity is retained by aggregating only relations with the **same** active syndrome before any square is taken.

---

## 1. One signed odd parity relation on clone pairs

Let the fine q-flip players be partitioned into clone pairs

\[
P_j=\{j0,j1\},\qquad j=1,\dots,m.
\]

For an odd nonempty fine support `R`, consider the signed parity game

\[
Q_R(S)=c\,\frac{1-(-1)^{|S\cap R|}}2,
\tag{1.1}
\]

where `c` may have either sign. Put

\[
q=|R|.
\]

Let `r` be the number of clone pairs hit twice and `k` the number hit once. Then

\[
q=k+2r,
\qquad k\ge1\text{ is odd},
\qquad s=r+k
\tag{1.2}
\]

is the number of touched blocks.

Ordinary fine Shapley assigns `c/q` to every fine player in `R`. Hence its aggregate block share is

\[
\Psi_j=
\begin{cases}
2c/q,&P_j\subseteq R,\\
c/q,&|P_j\cap R|=1,\\
0,&P_j\cap R=\varnothing.
\end{cases}
\tag{1.3}
\]

The exact block-coupled parity selector sees only odd block occupancy, so it assigns

\[
\Phi_j=
\begin{cases}
c/k,&|P_j\cap R|=1,\\
0,&|P_j\cap R|\in\{0,2\}.
\end{cases}
\tag{1.4}
\]

Therefore the refinement defect `delta_j=Psi_j-Phi_j` is

\[
\boxed{
\delta_j=
\begin{cases}
2c/q,&P_j\subseteq R,\\[1mm]
-2rc/(qk),&|P_j\cap R|=1,\\[1mm]
0,&P_j\cap R=\varnothing.
\end{cases}}
\tag{1.5}
\]

and `sum_j delta_j=0` exactly.

---

## 2. `P03-B16-PARITY-MINIMUM-CURRENT` — PROVED

On the complete graph of the `s` touched blocks, the unique minimum-energy antisymmetric current with divergence `delta` is

\[
J_{ab}=\frac{\delta_a-\delta_b}{s}.
\tag{2.1}
\]

For the parity defect (1.5), same-type block pairs carry zero current. Every doubled-to-single edge carries exactly

\[
\boxed{J_{D,U}=\frac{2c}{qk}.}
\tag{2.2}
\]

There are `rk` such edges. Consequently

\[
\boxed{
\mathcal E_{\rm cur}(R,c)
:=\sum_{a<b}J_{ab}^2
=\frac{4r}{q^2k}c^2
=2\left(\frac1{qk}-\frac1{q^2}\right)c^2.
}
\tag{2.3}
\]

This has three useful consequences.

### 2.1 Singleton syndrome is annihilated exactly

If `q=1`, then `r=0,k=1`, hence

\[
\boxed{\mathcal E_{\rm cur}=0.}
\tag{2.4}
\]

Thus the exponential singleton-syndrome obstruction to a **basiswise raw q-flip load bound** does not appear in the selector-refinement current at all. This is an exact cancellation, not an estimate.

### 2.2 Exact double inverse-number gap

The current multiplier has the resolvent representation

\[
\boxed{
2\left(\frac1{qk}-\frac1{q^2}\right)
=
2\int_0^1\!\int_0^1
x^{q-1}\bigl(y^{k-1}-y^{q-1}\bigr)\,dx\,dy.
}
\tag{2.5}
\]

The multiplier is nonnegative because `k<=q`. The first inverse number resolves the fine relation degree `q`; the second records the odd-block degree `k`. The subtraction is the refund produced by even clone occupancy.

### 2.3 Sharp domination by the Ward refinement dissipation

For the same signed relation, the already-proved binary Ward coarse-to-fine dissipation is

\[
\mathcal W(R,c)=c^2\left(1-\frac1q\right).
\tag{2.6}
\]

From (2.3),

\[
\frac{\mathcal E_{\rm cur}}{\mathcal W}
=
\frac{2(q-k)}{qk(q-1)}
\le\boxed{\frac23},
\tag{2.7}
\]

with equality at `q=3,k=1`. Indeed `q-k<=q-1` and `qk>=3` whenever `q>1` is odd. Hence

\[
\boxed{
\mathcal E_{\rm cur}(R,c)
\le\frac23c^2\left(1-\frac1q\right).
}
\tag{2.8}
\]

A coarser inverse-degree estimate that will be useful below is

\[
\boxed{
\mathcal E_{\rm cur}(R,c)\le\frac{2c^2}{q}
\qquad(q\ge3),
}
\tag{2.9}
\]

while the `q=1` term is exactly zero.

---

## 3. Signed syndrome aggregation before squaring

At a fixed Borel scale, several dual-code relations can have the same active q-flip syndrome `R`. As in the previous central-Walsh compiler, aggregate them first:

\[
b_R:=\sum_{A:R_A=R}c_A.
\tag{3.1}
\]

This is essential: `b_R` is signed. A `2 mod 4` R32 credit can cancel a `0 mod 4` debit with the same active syndrome before any quadratic payment is formed. No multiplicity is discarded; only equal characters are combined.

Let

\[
F(S)=\sum_{R\text{ odd}}b_R\frac{1-(-1)^{|S\cap R|}}2.
\tag{3.2}
\]

For a syndrome translation `z` define the based translate

\[
F^{z}(S)=F(z\triangle S)-F(z).
\tag{3.3}
\]

For each parity relation,

\[
Q_R^{z}(S)=(-1)^{|z\cap R|}Q_R(S).
\tag{3.4}
\]

Because the Shapley defect and its minimum current are linear in the game, the current of `F^z` is therefore

\[
J_{ab}^{z}
=
\sum_R(-1)^{|z\cap R|}J_{ab}^{(R)}.
\tag{3.5}
\]

---

## 4. `P03-B16-PARITY-CURRENT-WALSH-FRAME` — PROVED

Average (3.5) over the uniform syndrome cube. Distinct supports `R` are distinct Walsh characters, so character orthogonality kills every cross term **exactly**. Hence

\[
\boxed{
\mathbb E_z\sum_{a<b}(J_{ab}^{z})^2
=
\sum_{R\text{ odd}}
2\left(\frac1{q_Rk_R}-\frac1{q_R^2}\right)b_R^2.
}
\tag{4.1}
\]

Combining (2.8) relation by relation gives the sharp frame-normalized Ward domination

\[
\boxed{
\mathbb E_z\sum_{a<b}(J_{ab}^{z})^2
\le
\frac23\sum_{R\text{ odd}}b_R^2\left(1-\frac1{q_R}\right).
}
\tag{4.2}
\]

The singleton layer contributes zero to the left side. Equivalently,

\[
\boxed{
\mathbb E_z\sum_{a<b}(J_{ab}^{z})^2
\le
2\sum_{\substack{R\text{ odd}\\q_R\ge3}}
\frac{b_R^2}{q_R}.
}
\tag{4.3}
\]

This is the missing normalization **at the parity-current level**: the current does not carry a unit weight per arbitrary q-flip pivot. It carries an explicit two-resolvent multiplier, and syndrome translation turns its cross-relation square into a diagonal Walsh frame.

### Operator form

Let `D` be the fine syndrome-degree operator (`D chi_R=q_R chi_R`) and `K` the odd-block-degree operator (`K chi_R=k_R chi_R`) on the odd parity sector. Then (4.1) is

\[
\boxed{
\mathbb E_z\|J^z\|_2^2
=2\left\langle F_{\rm odd},
D^{-1}(K^{-1}-D^{-1})F_{\rm odd}\right\rangle_{\rm Walsh},
}
\tag{4.4}
\]

with the degree-one kernel interpreted by the exact zero multiplier. This is a positive double-resolvent operator because `K<=D` frequency by frequency.

The coarser right side of (4.3) is the inverse-noise square function

\[
\sum_{q_R\ge3}\frac{b_R^2}{q_R}
=
\int_0^1 t^{-1}
\left\|T_{\sqrt t}F_{\ge3,\rm odd}\right\|_2^2\,dt,
\tag{4.5}
\]

where `T_rho` is the Walsh noise operator on the active syndrome cube. Thus the current is automatically high-pass: the killed `q=1` mode contributes nothing, and higher relation degrees receive inverse-degree damping before the physical Radon payment is attempted.

---

## 5. Why the syndrome average cannot simply be omitted

There is a generic parity-game obstruction to a pointwise cross-relation square estimate.

Take one doubled block and `k` odd single blocks, with `k` odd. For every choice of which clone is selected in each single block, one gets a distinct odd support `R`; there are `2^k` such supports. All have the **same** parity-current vector at the untranslated base point.

With equal coefficients, their pointwise current energy is therefore `2^{2k}` times one-relation energy, whereas the diagonal sum in (4.1) is only `2^k` times that energy. The amplification is exactly

\[
\boxed{2^k.}
\tag{5.1}
\]

So a generic proof that simply squares the unaveraged relation sum and discards character orthogonality can fail exponentially. This is a parity-game obstruction, **not** an FEI counterexample and not asserted to be an authentic equal-coefficient R32 packet. It explains why the new Walsh-frame step is mathematically substantive rather than cosmetic.

---

## 6. Interface with the newest arbitrary-q-flip Radon theorem

The newest B18 theorem proves that every nonzero q-flip pivot `u` has a conditionally-negative derivative-disagreement kernel and central odd source square

\[
\mathcal S_u\le\frac1{40}E_u^2.
\]

Its remaining compiler condition is a dimension-free weighted frame rather than a unit-weight sum over pivots.

Equation (4.1) supplies exactly such a **compiler-side normalization candidate**: the signed selector current comes with a nonnegative two-resolvent multiplier and diagonalizes after syndrome translation. It also kills the known singleton basiswise obstruction identically.

What is **not yet proved** is the final admissible coupling

\[
\text{parity-current edge }(a,b)
\quad\longrightarrow\quad
\text{dependent q-flip kernel }p_u(v)
\]

with the same weights while preserving the original physical influence budget of the fixed Boolean function. A syndrome translate corresponds algebraically to changing the base phase by q-flip generators, and its influence need not equal the original influence. Therefore (4.1) cannot simply be averaged into an FEI bound without another identity.

This is the exact residual obligation, not a hidden norm gap.

---

## 7. New exact collision form for the next attack

The previous RM(1,n) two-point calculation becomes directly relevant here. For the signed Borel coefficients, equal active syndromes satisfy

\[
R_A=R_B
\iff
R_{A\triangle B}=\varnothing.
\]

Thus

\[
\boxed{
\sum_R b_R^2
=
\sum_{\Delta:\,R_\Delta=\varnothing}
\sum_A c_Ac_{A\triangle\Delta},
}
\tag{7.1}
\]

up to the already-known retained-code/terminal boundary bookkeeping. Every such symmetric difference is unfrustrated for the active phase. The exact two-point RM(1,n) Borel correlation formula can therefore be applied on the **kernel of the active-syndrome map**, rather than to all relation pairs.

Likewise the inverse-degree term in (4.3) has the exact noise-resolvent form (4.5). This suggests a concrete next calculation: combine the RM(1,n) correlation on the inactive-syndrome kernel with the inverse-noise parameter `t`, retaining the terminal subtraction, and test whether the resulting collision kernel is bounded by the authentic R16 first-separation/moment bank before any absolute value is taken.

That route uses the same signed collision geometry as the earlier Hardy/R16 bridge but now after the parity-current frame normalization.

---

## 8. Exact verification and killed routes

The standard-library exact checker verifies:

- 42 direct ordinary-fine/coarse-block Shapley calculations against (1.5);
- 42 exact current-energy identities (2.3);
- 136 exact double-resolvent and `2/3` domination cases through odd fine degree 31;
- 48 deterministic signed multi-relation families, including negative aggregate coefficients;
- 4,080 translated-state current-energy evaluations giving exact equality in (4.1);
- 269 distinct-character orthogonality checks;
- the pointwise cross-term obstruction with amplification `2,8,32,128,512` for `k=1,3,5,7,9`;
- exact zero current for `q=1`.

The checker is falsification evidence; the identities above are proved algebraically.

This run does **not** revive any previously killed route:

- no basiswise `L_v=O(n)` bound;
- no unit-weight arbitrary-pivot frame;
- no unsigned divergence or pairwise-square replacement before signed cancellation;
- no generic endpoint `L2` estimate;
- no one-resolvent selector transport;
- no positive-part collision order;
- no reuse of the terminal band as a second payment.

---

## 9. Status and next exact target

**PROVED this run:** the parity-specific minimum-current formula (2.3), its exact double-resolvent gap (2.5), sharp `2/3` Ward domination (2.8), and the signed syndrome-translation Walsh-frame identity (4.1).

**PRESERVED:** R32 signed cancellation, same-syndrome negative credits, original q-flip generator geometry, dual-code multiplicity, R16/moment refunds, and the separate terminal-band payment.

**OPEN:** unrestricted FEI. The remaining bridge is to attach the frame-normalized parity current to the newest dependent-triple q-flip Radon kernels **without averaging away the original function's influence budget**.

The next precise attack is to insert (7.1) and the exact RM(1,n) two-point Borel correlation into the inverse-noise integral (4.5), including the retained-code/terminal subtraction, and compare that signed inactive-syndrome collision kernel directly with the R16 first-separation moments. A failure on authentic R32 data should be preserved as a counterexample and the route changed; a generic parity-game failure is not enough because the live coefficients have the Reed--Muller/Borel structure.
