# B15 — heterogeneous Numaro C-spine drives aggregate magnitude flow to 1.499391174778...

**Status:** **OPEN / PARTIAL. Full uniform-cube FEI remains OPEN / NOT PROVED.**  
**Execution:** **WITHOUT_VERIFIED_BRAIN.** No authenticated brain retrieval or receiver-side brain context was used.  
**Role:** FEI spectral remainder proof / unequal Fourier magnitudes.  
**Claim level:** an exact heterogeneous-composition identity plus a rigorously certified Boolean stress family for the current aggregate one-sided magnitude-flow route. No publication-priority claim.

## 0. Why this run changes the target

The current B15 route uses, for a physical coordinate `i`,

\[
L_i(f)=\sum_{T:v_T\ne0}v_T^2\log_2^+\frac{|u_T|}{|v_T|},
\qquad
u_T=\widehat f(T),\ v_T=\widehat f(T\cup\{i\}),
\]

and the aggregate one-sided Fourier magnitude flow

\[
\mathcal A(f)=\sum_iL_i(f).
\]

The inherited restriction estimate is

\[
\Delta_iH\le \frac3{\ln2}\operatorname{Inf}_i(f)+2L_i(f).
\]

Hence a universal estimate

\[
\mathcal A(f)\le\kappa I(f)
\]

would imply FEI with constant `3/ln(2)+2 kappa`. The focused remaining candidate is

\[
\mathcal A(f)\stackrel{?}{\le}\frac32I(f).
\]

The preceding B15 run certified that homogeneous recursive self-composition of the recovered 18-variable Numaro seed stays below `1.488912`. That left open the explicit next attack: heterogeneous composition.

This run finds a substantially sharper family. Its limiting ratio is rigorously enclosed by

\[
\boxed{
1.4993911747781890
<
\lim_{d\to\infty}\frac{\mathcal A(F_d)}{I(F_d)}
<
1.4993911747781891.
}
\]

At the same time every finite depth satisfies

\[
\boxed{
\frac{\mathcal A(F_d)}{I(F_d)}<1.499392<\frac32.
}
\]

Therefore this family does **not** refute the `3/2` target, but it proves that any universal aggregate-flow constant must satisfy

\[
\boxed{
\kappa_*:=\sup_f\frac{\mathcal A(f)}{I(f)}
>1.4993911747781890.
}
\]

So `3/2`, if true, is forced to be nearly sharp: the remaining numerical room is less than `0.000608825222`.

---

## 1. Exact heterogeneous balanced-composition identity

Let `G:{-1,1}^m->{-1,1}` be balanced. For each outer coordinate `i`, let `H_i` be an arbitrary balanced Boolean function on a disjoint block, and set

\[
F=G(H_1,\ldots,H_m).
\]

Write

\[
\alpha_i^G=\operatorname{Inf}_i(G),
\qquad
q_{i,x}=|\widehat H_i(\{x\})|.
\]

For the outer Fourier fibre at `i`, with

\[
a_K=\widehat G(K),\qquad b_K=\widehat G(K\cup\{i\}),
\]

define

\[
M_i^G(q)=\sum_{K:b_K\ne0}b_K^2
\log_2^+\frac{|a_K|}{|b_K|q}.
\]

### Proposition 1 — heterogeneous composition law

For arbitrary balanced, mutually disjoint `H_i`,

\[
\boxed{
\mathcal A(F)
=
\sum_{i=1}^m
\left(
\alpha_i^G\mathcal A(H_i)
+
\sum_x q_{i,x}^2 M_i^G(q_{i,x})
\right).
}
\tag{1}
\]

Also

\[
\boxed{
I(F)=\sum_i\alpha_i^G I(H_i).
}
\tag{2}
\]

### Proof

Expand

\[
F=\sum_{K\subseteq[m]}\widehat G(K)\prod_{j\in K}H_j.
\]

Because every `H_j` is balanced, a nonempty Fourier frequency in block `j` occurs exactly when `j\in K`. Fix a physical coordinate `x` in block `i` and pair Fourier coefficients that differ by `x`.

If the residual frequency inside block `i` is nonempty, both paired coefficients use an outer frequency containing `i`. Their common outer factor and all other block factors cancel in the logarithmic ratio. Summing squared weights over the outer frequencies and all other block frequencies by Parseval contributes exactly

\[
\alpha_i^G L_x(H_i).
\]

If the residual frequency in block `i` is empty, the lower member uses an outer frequency not containing `i`, while the upper member uses the corresponding outer frequency containing `i` together with the singleton coefficient `\widehat H_i({x})`. Summing the remaining blocks by Parseval gives exactly

\[
q_{i,x}^2M_i^G(q_{i,x}).
\]

Sum over `x` and then over `i` to obtain (1). Equation (2) is the standard disjoint balanced influence composition identity. `square`

The identical-inner formula used previously is the special case `H_1=...=H_m`; no identical-inner hypothesis is needed.

---

## 2. The exact Numaro seed data used

Let `G` be the already recovered external balanced monotone 18-variable Numaro seed. The checker refuses the seed unless its complete truth-table SHA-256 is

`f8a7bb2c738d86368305111633376b1a3a83d8ee1f1abcc9a37d841b0f9c7839`.

Its first nine coordinates form class `C`, and its last nine form class `A`. Exact integer Walsh arithmetic gives

\[
c:=\alpha_C=s_C=\frac{57}{256},
\qquad
a:=\alpha_A=s_A=\frac1{256},
\]

where `s` denotes singleton Fourier magnitude. Thus

\[
I(G)=9c+9a=\frac{261}{128}.
\]

For class `C`, let the outer paired magnitudes be `(u,v)` and define

\[
B_C=\sum_{u,v>0}v^2
=\frac{5613}{32768},
\]

with the normalization inherited from the Fourier spectrum, and

\[
C_C=\sum_{u,v>0}v^2\log_2\frac uv.
\]

The minimum positive ratio `u/v` in class `C` is exactly `1/2`. Therefore, for every `0<q<=c<1/2`, all overlapping terms are active and

\[
\boxed{
M_C(q)=B_C\log_2(1/q)+C_C.
}
\tag{3}
\]

The class-`A` dictator correction is simply `L_A=M_A(1)`. The direct seed values remain

\[
\frac{L_C}{c}=0.6685747069\ldots,
\qquad
\frac{L_A}{a}=2.2480374028\ldots.
\]

The second number is why a coordinatewise `3/2` statement is impossible; the question is whether cross-coordinate averaging saves the aggregate inequality.

---

## 3. The heterogeneous C-spine family

Let `F_0` be a one-bit dictator. Recursively define `F_{d+1}` by feeding:

- nine independent copies of `F_d` into the nine class-`C` inputs of `G`; and
- nine fresh dictators into the nine class-`A` inputs of `G`.

Every `F_d` is balanced and Boolean. Its dimension is finite:

\[
n_d=\frac{17\cdot9^d-9}{8}.
\]

For a leaf coordinate `x` of `F_d`, write

\[
p_x=\operatorname{Inf}_x(F_d).
\]

Because `s_C=c=\alpha_C` and `s_A=a=\alpha_A`, induction from the dictator shows

\[
\boxed{|\widehat F_d(\{x\})|=p_x}
\tag{4}
\]

for every leaf. Introduce

\[
I_d=\sum_xp_x,
\qquad
Q_d=\sum_xp_x^2,
\qquad
E_d=\sum_xp_x^2\log_2(1/p_x),
\qquad
A_d=\mathcal A(F_d).
\]

For `d>=1`, every descendant leaf under a class-`C` input has `p_x<=c<1/2`, so the exact full-log formula (3) applies. Proposition 1 now gives the closed recurrence

\[
\boxed{
I_{d+1}=9cI_d+9a,
}
\tag{5}
\]

\[
\boxed{
Q_{d+1}=9c^2Q_d+9a^2,
}
\tag{6}
\]

\[
\boxed{
E_{d+1}=9c^2\bigl(E_d+\log_2(1/c)Q_d\bigr)+9a^2\cdot8,
}
\tag{7}
\]

and

\[
\boxed{
A_{d+1}
=9cA_d+9(B_CE_d+C_CQ_d)+9L_A.
}
\tag{8}
\]

The initial level is the original Numaro seed with dictator children:

\[
I_1=9c+9a,
\quad
Q_1=9c^2+9a^2,
\quad
E_1=9c^2\log_2(1/c)+9a^2\cdot8,
\quad
A_1=9L_C+9L_A.
\]

These are exact identities, not a floating-point dynamic program.

---

## 4. Rigorous all-depth certificate

The checker reconstructs the seed by integer Walsh transform and encloses every logarithm with rational arithmetic using

\[
\ln y=2\sum_{j=0}^{N-1}\frac{z^{2j+1}}{2j+1}+R_N,
\qquad
z=\frac{y-1}{y+1},
\]

with the explicit positive tail bound

\[
0\le R_N\le\frac{2z^{2N+1}}{(2N+1)(1-z^2)}.
\]

It uses 24 terms and propagates only upper endpoints through (5)--(8). Certified upper ratios include

| depth | upper bound for `A_d/I_d` |
|---:|---:|
| 1 | 0.6958068223803938 |
| 5 | 1.4920382665442982 |
| 10 | 1.4993565525516569 |
| 15 | 1.4993903031161630 |
| 20 | 1.4993911479641464 |
| 25 | 1.4993911739485019 |

Put

\[
r=9c=\frac{513}{256}>1,
\qquad
\lambda=9c^2<1.
\]

Since `Q_d<=1`, equation (7) gives the uniform bound

\[
E_d\le
E_{\max}:=
\frac{\lambda\log_2(1/c)+8\cdot9a^2}{1-\lambda}.
\]

Hence the additive forcing in (8) is bounded by one constant

\[
F_{\max}=9(B_CE_{\max}+C_C)+9L_A.
\]

For every `k>=0`,

\[
A_{25+k}
\le r^kA_{25}+F_{\max}\frac{r^k-1}{r-1},
\qquad
I_{25+k}\ge r^kI_{25}.
\]

Therefore every later ratio is at most

\[
\frac{A_{25}}{I_{25}}
+
\frac{F_{\max}}{(r-1)I_{25}}
<
\boxed{1.4993912858335811}
<1.499392.
\]

Together with the first 25 certified levels, this proves the all-depth upper bound.

---

## 5. Exact limiting obstruction for the universal aggregate-flow constant

The linear recurrences also give a closed generating-function expression for the limit. Set

\[
S_Q=\sum_{j\ge1}\frac{Q_j}{r^j},
\qquad
S_E=\sum_{j\ge1}\frac{E_j}{r^j}.
\]

Equations (6)--(7) imply

\[
S_Q=
\frac{Q_1/r+9a^2/[r(r-1)]}{1-\lambda/r},
\]

and

\[
S_E=
\frac{
E_1/r+(\lambda\log_2(1/c)/r)S_Q
+72a^2/[r(r-1)]
}{1-\lambda/r}.
\]

Dividing (5) and (8) by `r^{d-1}` and summing yields

\[
\boxed{
\lim_{d\to\infty}\frac{A_d}{I_d}
=
\frac{
A_1+9B_CS_E+9C_CS_Q+9L_A/(r-1)
}{
I_1+9a/(r-1)
}.
}
\tag{9}
\]

The same rational logarithm enclosures certify

\[
1.4993911747781890
<
\text{right side of (9)}
<
1.4993911747781891.
\]

Since every `F_d` is a genuine finite Boolean function, this proves the obstruction

\[
\boxed{
\sup_f\frac{\mathcal A(f)}{I(f)}
>1.4993911747781890.
}
\]

Thus **no universal aggregate magnitude-flow bound with a constant below this number can be true**. The proposed constant `3/2` survives, but if it is correct it is extraordinarily close to optimal for this proof route.

---

## 6. What is proved and what is not

### Proved

1. The balanced-composition identity for `A` extends exactly to heterogeneous disjoint balanced inner functions.
2. The explicit C-spine family is Boolean and balanced at every finite depth.
3. Its state closes under the exact four-variable recurrence `(I,Q,E,A)`.
4. Every depth has `A/I<1.499392<3/2`.
5. The limiting ratio lies in the certified interval above, giving the rigorous lower obstruction on any universal `A/I` constant.

### Not proved

- The universal inequality `A(f)<=3I(f)/2` is still open.
- Full FEI is not proved.
- This does not bound the original packet remainder `D` directly.
- The Numaro seed is prior work and is not claimed here.
- No novelty or publication-priority claim is made for Proposition 1 or the C-spine construction.

The result is nevertheless decisive for the current arithmetic-remainder strategy: the clean `3/2` aggregate-flow target, if valid, cannot have much slack, and homogeneous self-composition was not the actual sharp stress mechanism. Repeatedly recursing only the high-influence `C` coordinates while terminating the rare `A` coordinates is substantially worse.

---

## 7. Next mathematical attack

The next useful question is no longer whether simple recursion approaches `3/2`; it nearly does. The proof must explain the residual gap.

Two concrete directions survive:

1. **Pathwise amortization with a sharp boundary term.** Derive a universal inequality on spectral-edge paths whose extremal recurrence reduces to the C-spine dynamics above and whose terminal contribution accounts for the remaining `0.0006088...` gap.
2. **Counterexample search beyond stationary C-spines.** Test genuinely nonstationary heterogeneous trees, allowing different subtrees on different `C` branches, to determine whether the supremum crosses `3/2`. Any such crossing would rigorously kill the aggregate-flow route while leaving FEI itself open.

A coarse replacement of `L_i` by `J_i` or by `alpha_i log(1/alpha_i)` remains unusable because rare tribes destroy those surrogates while the exact one-sided flow is small.

---

## 8. Current primary-literature check

A fresh primary-source check on 21 September 2026 found no unrestricted uniform-cube FEI proof in the relevant current sources.

- González--MacManus--Pereyra, arXiv:2606.00246 (29 May 2026), develop the restriction/stopping-tree framework and state that the missing general restriction inequality would imply full FEI.
- Potapov, arXiv:2609.21563 (18 September 2026), proves FEI for plateaued functions with sharp class constant `4` and for partially bent functions with sharp constant `2`; this does not cover arbitrary unequal Fourier magnitudes.
- Li--Han, arXiv:2512.03117, retain an additional influence-profile entropy term in a general information-theoretic inequality rather than proving `H<=CI` alone.

The recovered Numaro 18-variable seed is treated as external prior work throughout. This report makes no publication-priority claim.

---

## 9. Reproducibility

`check_numaro_c_spine.py` is standard-library only. It reconstructs the seed, computes the integer Walsh transform, verifies both coordinate classes, uses rational log intervals, checks the first 25 levels, proves the geometric all-later-depth envelope, and independently encloses the generating-function limit.

The recorded verification output has SHA-256

`df2d37c80ddfcb9b6c610144e46ce7170374ff227217a40da026cc8ba82d3452`.

The checker is a self-check of the theorem above, not an independent audit and not evidence of full FEI.
