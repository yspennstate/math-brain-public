# B17 — exact block-OR refutation of the `3/4` symmetric-softmax budget and a two-remainder dichotomy replacement

**Status:** **OPEN / PARTIAL. Full uniform-cube FEI remains OPEN / NOT PROVED.**

**Execution:** **WITHOUT_VERIFIED_BRAIN.** No authenticated brain retrieval or receiver-context use entered this mathematics.

**Role:** fleet04/B17, joint interface D: exact Boolean adversary plus genuinely different replacement.

## 1. Newest compatible other-account B15 input consumed

The named peer input is fleet03/B15,

`proofnet24/P03-fei/fleet-2026-09-21/fleet03/B15/20260921T211127Z-real-restriction-softmax-credit/REPORT.md`,

created by commit `fdd17d53a0e3cd42e2b4e4942449241b77c0e70d`.

For a coordinate `i`, write

\[
u_T=\widehat f(T),\qquad v_T=\widehat f(T\cup\{i\}),\qquad
q_i=\min\{\operatorname{Inf}_i(f),1-\operatorname{Inf}_i(f)\}.
\]

The peer report retains the exact packet-orientation mutual-information credit and defines the post-credit symmetric softmax current

\[
W_i(f)=\frac12\sum_T \min(u_T^2,v_T^2)
\log_2\frac{u_T^2+v_T^2}{2\min(u_T^2,v_T^2)},
\qquad
\mathcal W(f)=\sum_iW_i(f),
\]

with zero contribution when the minimum is zero. It proves

\[
\Delta_iH\le 2W_i+\left(1+\frac3{\ln2}\right)q_i
\tag{1.1}
\]

and therefore the conditional reduction

\[
\mathcal W(f)\le \kappa J(f)\ \text{for all Boolean }f
\quad\Longrightarrow\quad
H(f)\le\left(1+\frac3{\ln2}+2\kappa\right)I(f),
\tag{1.2}
\]

where `J=sum_i q_i`. Its strongest live numerical proposal is

\[
\boxed{\mathcal W(f)\stackrel{?}{\le}\frac34J(f).}
\tag{1.3}
\]

Width-two tribes reached `0.709091689...` but did not refute (1.3). This run refutes (1.3) with an exact Boolean function and then abandons the one-statistic target rather than merely increasing `3/4`.

For the replacement I also retain fleet04/B15's exact KL-refunded radius-one representation
`20260921T211141Z-refunded-radius1-transfer/REPORT.md`: after the self-XOR fibre KL credit is kept exactly, its sufficient remainder is

\[
T_2(f)=\sum_S p_S\log_2(1/p_S)
\left(1-p_S-\sum_i p_{S\triangle\{i\}}\right),
\qquad p_S=\widehat f(S)^2,
\tag{1.4}
\]

and `T_2<=4J` is sufficient for
`H <= (6+2/ln2)J`. The one-point defect makes the constant four asymptotically sharp.

## 2. Exact 16-variable Boolean adversary

Identify a four-bit word `x=(x_0,x_1,x_2,x_3)` with
`x_0+2x_1+4x_2+8x_3`. Define the Boolean gate

\[
g(x)=+1\quad\Longleftrightarrow\quad
x\in A:=\{2,8,10,11,14\},
\]

and `g(x)=-1` otherwise. On four disjoint four-bit blocks set

\[
F(x^{(1)},x^{(2)},x^{(3)},x^{(4)})
=
\begin{cases}
+1,&\text{if at least one }g(x^{(b)})=+1,\\
-1,&\text{otherwise}.
\end{cases}
\tag{2.1}
\]

Equivalently, with `r=(1-g)/2`,

\[
F=1-2\prod_{b=1}^4 r(x^{(b)}).
\tag{2.2}
\]

This is a literal 16-variable Boolean truth table; no free probability law, integrality assumption, or synthetic spectrum is used.

The unnormalized Walsh transform of `g`, in the same little-endian order, is exactly

\[
(-6,6,-6,-2,6,2,-2,2,-6,-2,2,-2,-2,2,-2,-6).
\tag{2.3}
\]

Thus `rhat(0)=11/16`, while every nonzero local Fourier coefficient of `r` has magnitude `3/16` or `1/16`. Formula (2.2) therefore gives the complete 16-bit Walsh spectrum by integer products, with the zero coefficient treated by the exact `1-2(11/16)^4` correction.

## 3. Exact refutation of `mathcal W <= 3J/4`

The verifier enumerates the `2^16` integer Walsh coefficients, not floating approximations. For every one of the 16 physical coordinates it obtains the same folded marginal

\[
q_i=\frac{3993}{32768},
\qquad
J(F)=\frac{3993}{2048}.
\tag{3.1}
\]

For any coordinate, group its `2^15` unordered Fourier pairs by

\[
R=\frac{u^2+v^2}{2\min(u^2,v^2)}.
\]

If the integer Walsh squares are used before the common `2^{-32}` normalization, the exact total `min`-weights are

\[
\begin{array}{c|r}
R&\sum\min(H_T^2,H_{T+i}^2)\\ \hline
1&65,421,312\\
5&87,228,416\\
65/9&132,487,740\\
172266089/15944049&63,776,196.
\end{array}
\tag{3.2}
\]

Hence

\[
W_i=
\frac{
87228416\log_2 5+
132487740\log_2(65/9)+
63776196\log_2(172266089/15944049)
}{2^{33}}.
\tag{3.3}
\]

There is a short exact certificate that (3.3) exceeds `3q_i/4`. The integer inequalities

\[
5^{25}>2^{58},
\quad
65^{20}>2^{57}9^{20},
\quad
172266089^{100}>2^{343}15944049^{100}
\]

give respectively

\[
\log_2 5>\frac{58}{25},\qquad
\log_2(65/9)>\frac{57}{20},\qquad
\log_2(172266089/15944049)>\frac{343}{100}.
\]

Substitution into (3.3) gives

\[
W_i>
\frac{1996780841}{21474836480},
\qquad
\frac34q_i=\frac{11979}{131072},
\]

and the exact positive difference of these rational bounds is

\[
\boxed{\frac{34141481}{21474836480}>0.}
\tag{3.4}
\]

All sixteen coordinates have the same pair table, so (3.4) proves

\[
\boxed{\mathcal W(F)>\frac34J(F).}
\tag{3.5}
\]

A separate exact-rational logarithm enclosure gives

\[
\boxed{\frac{\mathcal W(F)}{J(F)}
=0.763732859681689660\ldots.}
\tag{3.6}
\]

Therefore the fleet03/B15 conjectural constant `3/4` is **false**. The peer's exact restriction identities and KL/orientation credits are not refuted; only its proposed global `3/4` budget is.

## 4. Why simply replacing `3/4` by a larger number is the wrong repair

The counterexample margin is not a normalization error: Parseval holds exactly, all 16 folded marginals are the rational value (3.1), and (3.4) proves the sign without floating arithmetic.

Changing `3/4` to `0.77` would evade this example but would leave the proof architecture dependent on one universal remainder statistic. Interface D already has a second exact, independently KL-refunded representation, namely the radius-one exposure `T_2`. The two representations fail on complementary geometries, so the more useful replacement is an **either/or theorem**, not another guessed scalar constant.

## 5. New replacement: a two-remainder dichotomy

### CONDITIONAL theorem B17-DICHOTOMY-D

Suppose every Boolean `f` satisfies at least one of

\[
\boxed{\mathcal W(f)\le\frac34J(f)}
\tag{D1}
\]

or

\[
\boxed{T_2(f)\le4J(f).}
\tag{D2}
\]

Then full uniform-cube FEI follows with

\[
\boxed{
H(f)\le\left(6+\frac2{\ln2}\right)I(f)
<8.886\,I(f).
}
\tag{5.1}
\]

This dichotomy is **OPEN / CONJECTURAL**. What is proved here is that it is sufficient for FEI and that it survives the new exact adversary.

### Proof of sufficiency

Induct on dimension. Character multiplication may first fold every spectral marginal. It preserves `H`, `J`, and every unordered-pair `W_i`, and gives total influence `I=J`.

If (D2) holds, the exact KL-refunded radius-one decomposition from fleet04/B15 gives directly

\[
H(f)\le
\left(4+2+\frac2{\ln2}\right)J(f)
=
\left(6+\frac2{\ln2}\right)J(f),
\]

so (5.1) follows.

If (D1) holds and `J>0`, there is a relevant coordinate `i` with

\[
W_i\le\frac34q_i.
\]

The exact restriction bound (1.1) yields

\[
\Delta_iH
\le
\left(\frac52+\frac3{\ln2}\right)q_i
=
6.8280851226\ldots\,q_i.
\tag{5.2}
\]

The average influence of the two Boolean restrictions is exactly `I-q_i`. Applying the induction hypothesis to both children with the larger constant

\[
C_D=6+\frac2{\ln2}=8.8853900817\ldots
\]

and using `C_D > 5/2+3/ln2`, we obtain

\[
H(f)
\le C_D(I-q_i)
+\left(\frac52+\frac3{\ln2}\right)q_i
\le C_DI.
\]

The `J=0` case is a character/constant and is trivial. This proves the conditional theorem.

The point is logical: (D1) need not hold for every function and (D2) need not hold for every function. The induction can choose whichever exact remainder representation pays the current function.

## 6. The replacement is executed on both complementary adversaries

For the new 16-variable function (2.1), the checker evaluates (1.4) from the exact integer Walsh spectrum and rigorous rational logarithm bounds:

\[
\boxed{
T_2(F)/J(F)
=
3.136106016892250992\ldots<4.
}
\tag{6.1}
\]

Thus this function **fails (D1) but passes (D2)**. Its full Fourier entropy also satisfies
`H/J=3.573558727309672278...`.

Conversely, for the one-point-defect family on `N=2^n` points, the radius-one branch is asymptotically sharp:
`T_2/J -> 4`. But the softmax current has only one unequal Fourier pair per coordinate. Writing

\[
P=\frac{(N-2)^2}{N^2},\qquad u=\frac4{N^2},
\]

gives exactly

\[
\frac{\mathcal W}{J}
=
\frac1N
\log_2\frac{N^2-4N+8}{8}
\longrightarrow0.
\tag{6.2}
\]

So the sharp radius-one family lies deep inside (D1), while the new `3/4` softmax counterexample lies safely inside (D2). Width-two tribes (`0.709091689...`) and the recovered Numaro seed (`0.489019733...`) remain on the softmax side as well.

This is why the dichotomy is a genuinely different replacement: it spends **one** of two exact negative-credit-compatible representations according to the Boolean geometry rather than demanding a single remainder statistic dominate every function.

## 7. Verification

`verify_b17_softmax_block_or.py` is standard-library only. It:

1. constructs the literal 16-variable Boolean truth table;
2. computes the full integer Walsh transform and checks Parseval;
3. verifies the exact local gate spectrum (2.3);
4. verifies all sixteen coordinates have identical exact pair tables and `q_i=3993/32768`;
5. verifies the three integer-power logarithm inequalities and the exact positive rational margin (3.4);
6. independently encloses all logarithms by an exact rational atanh series with a rigorous positive tail bound;
7. evaluates the radius-one exposure from exact Walsh squares and certifies `T_2<4J`.

Checker SHA-256:

`c66437cc6acdc8e0e1a31b77d6571a718c6643f86342294e6fc2df7e5a67d56a`.

Recorded output SHA-256:

`d9331ab531e465fced90ec9762a98915d44dd79d89525020a21383bd6a194141`.

Truth-table bit hash:

`9dd7dc9eeffae93632bf7483f4d9e636877b3da765c6ab4069f5bd57d78ecd74`.

Integer-Walsh-vector hash:

`b68abe1ca3e2118e8c15248f62079ea1eb61b6cc686f115e6a7fe42019dfe904`.

## 8. What changed

**Before:** the strongest new fleet03/B15 route proposed the universal budget `mathcal W<=3J/4`, which would imply FEI with constant `6.828...`. Width-two tribes only forced the coefficient above `0.709...`.

**After:** `3/4` is rigorously false on an explicit 16-variable Boolean block-OR construction; any universal inequality `mathcal W<=kappa J` must have

\[
\boxed{\kappa\ge0.763732859681689660\ldots.}
\]

Rather than merely weakening `kappa`, this run derives the open two-remainder dichotomy (D1)/(D2), which would still prove full FEI with constant `6+2/ln2`, and it verifies that the new softmax adversary and the one-point-defect radius-one adversary fall on opposite paying branches.

**Next exact obligation:** try to prove or refute the dichotomy itself. A counterexample now has to satisfy **both**
`mathcal W>3J/4` and `T_2>4J` simultaneously while obeying an actual Boolean signed Walsh spectrum. Search/composition work should therefore optimize the two normalized remainders jointly, not either one in isolation. Full FEI remains OPEN.
