# B14 — dimension-gap two-face selector and orientation dichotomy for the stable FEI gate candidate

**Classification:** `ESSENTIAL_STEP_APPLIED / EXACT_PHYSICAL_PAIR_SELECTOR`.  
**Full uniform-cube FEI:** **OPEN / NOT PROVED.**  
**Execution:** `WITHOUT_VERIFIED_BRAIN`.

## 0. Version/change summary


The old interface-A facts remain preserved exactly:

- the genuine Boolean addressing obstruction rules out every-coordinate payment;
- the folded physical block drift remains
  \[
  D_A^{\rm fold}=\mathcal J(f)-\mathbb E_z\mathcal J(f_{A=z})=I_A+C_A;
  \]
- fleet01/B18's curvature-refunded inequality requires retaining the nonmodular survivor/orientation refund rather than discarding it.

The new result below converts the exact two-face terminal identity from the immediately preceding B14 run into a dimension-dependent physical selector. Its contrapositive produces a quantitative orientation/checkerboard bank. Applied to the newest source-valid monotone spine-graft lower-bound family, it proves that every stage from `F_4` onward has a paid physical two-face restriction under the one fixed potential `Gamma_*`.

This does **not** prove the universal prime-gate statement.

## 1. Exact live candidate and sources consumed

The all-gate defect is
\[
D_\Gamma(G;p)=
\sum_i\frac{\operatorname{It}_i(G;p)}{V_{p_i}}
\bigl(\Gamma(p_i)+h_2(V_{p_i})\bigr)
-\Gamma(p_{\rm out})-\widetilde H_G(p),
\qquad V_u=4u(1-u).
\tag{1.1}
\]

The exact current stable candidate comes from

`proofnet24/P03-fei/fleet-2026-09-21/fleet01/B18/20260922T0222Z-shared-graft-tail/REPORT.md`,

report blob `7ea2c548afc0a5fc62f972f9c64df0578f7e0838`. It fixes
\[
C_*=6.5218512,\qquad C_0=6.4548,\qquad
\Delta:=C_*-C_0=0.0670512,
\tag{1.2}
\]
\[
a_*=4\Delta=0.2682048,\qquad
\Gamma_*(p)=\Gamma_{\rm RO}(p)+a_*p(1-p).
\tag{1.3}
\]
The remaining universal implication is `LIMIT-PRIME-GATE-LIFT-v1`:
\[
D_{\Gamma_*}(P;p)\ge0
\]
for every finite composition-prime Boolean gate and every interior product bias.

The source-exact curvature input required by the older A-interface prompt is

`fleet01/B18/20260921T1856Z-curvature-refunded-crossing/REPORT.md`,

blob `ef9f471c019a7d81e9864fd457a0e4bae9da890d`. It proves, for median-centered physical restriction,
\[
\Delta_A\mathcal F
\le B_A-\sum_{j\notin A}\mathfrak j'(p_j)c_j(A),
\qquad
D_A^{\rm fold}=I_A+C_A.
\tag{1.4}
\]
The exact source-to-next-arrow use here is conceptual but mathematically binding: a restriction proof may not throw away its survivor/orientation refund. In the all-gate two-face compiler below, the corresponding orientation term is the explicit positive checkerboard bank \(C_0X\). If the unsigned mixed-curvature part cannot pay a physical pair, the contrapositive forces that orientation bank quantitatively rather than deleting it.

The immediate predecessor is

`fleet04/B14/20260922T030938Z-two-face-terminal-reserve/REPORT.md`,

report blob `247ef5cdf541fccba63145dd9884f8c35b0be123`. It proves the exact two-face identity used in Section 2.

Finally, the newest stronger adversarial family consumed is

`fleet02/B17/20260922T021155Z-spine-shared-graft/REPORT.md`,

report blob `6b891bc8972db1bc9f55a5b3f49e6501a625fed4`. It gives a balanced monotone spine-graft family whose excess ratios converge to a value only about \(3.26\times10^{-8}\) below \(C_*\). Section 5 proves that this entire tail is nevertheless physically pair-selectable.

## 2. Exact terminal reserve recalled

Let \(f:\{0,1\}^n\to\{-1,1\}\) be viewed at uniform bias. For distinct physical coordinates \(i,j\), freeze all other coordinates to a uniform assignment \(z\). Put
\[
D_iD_jf(z)
=\frac{f_{00}-f_{10}-f_{01}+f_{11}}4
\tag{2.1}
\]
and let \(X_{ij}\) be the probability that the resulting two-face is an XOR/XNOR checkerboard.

The preceding B14 theorem gives exactly
\[
\boxed{
T_{ij}(f):=
\mathbb E_zD_{\Gamma_*}(f_{ij\mid z})
=
\Delta\,\|D_iD_jf\|_2^2+C_0X_{ij}.
}
\tag{2.2}
\]
Every two-variable terminal has nonnegative \(D_{\Gamma_*}\); constants and literals have zero defect, AND/OR faces have defect \(\Delta/4\), and checkerboards have defect \(C_*\).

Write
\[
N_2={n\choose2},\qquad
M_2(f):=\sum_{i<j}\|D_iD_jf\|_2^2
=\sum_S{|S|\choose2}\widehat f(S)^2,
\tag{2.3}
\]
\[
X(f):=\sum_{i<j}X_{ij}.
\tag{2.4}
\]
Averaging (2.2),
\[
\boxed{
\overline T_2(f)
=\frac{\Delta M_2(f)+C_0X(f)}{N_2}.
}
\tag{2.5}
\]

## 3. New theorem: dimension-gap physical pair selector

Assume \(f\) is balanced and \(I(f)>1\). Put
\[
R(f):=\frac{H(f)}{I(f)-1}.
\tag{3.1}
\]
At the balanced uniform root,
\[
D_{\Gamma_*}(f)
=C_*I(f)-H(f)-C_*
=(C_*-R(f))(I(f)-1).
\tag{3.2}
\]

### Lemma 3.1 — second-factorial mass is dimension-discounted

Since balance gives \(\widehat f(\varnothing)=0\), every spectral support size \(k\) contributing to (2.3) has \(k\ge1\). For \(1\le k\le n\),
\[
{k\choose2}
=\frac{k(k-1)}2
\le \frac n2(k-1).
\tag{3.3}
\]
Therefore
\[
\boxed{
M_2(f)\le\frac n2\,(I(f)-1)
}
\tag{3.4}
\]
and hence
\[
\boxed{
\frac{M_2(f)}{N_2}\le\frac{I(f)-1}{n-1}.
}
\tag{3.5}
\]

Also, face by face,
\[
1_{\{\mathrm{XOR/XNOR}\}}
\le (D_iD_jf)^2,
\]
because checkerboards have squared mixed derivative \(1\), while the indicator is zero on all other face types. Thus
\[
\boxed{X(f)\le M_2(f).}
\tag{3.6}
\]

### Theorem 3.2 — universal balanced selector

Equations (2.5), (3.5), and (3.6) imply
\[
\boxed{
\overline T_2(f)
\le
C_*\frac{I(f)-1}{n-1}.
}
\tag{3.7}
\]

Consequently, if
\[
\boxed{
C_*-R(f)\ge\frac{C_*}{n-1},
}
\tag{3.8}
\]
then
\[
D_{\Gamma_*}(f)\ge\overline T_2(f).
\]
Hence at least one **actual physical pair** \(i,j\) satisfies
\[
\boxed{
D_{\Gamma_*}(f)
\ge
\mathbb E_zD_{\Gamma_*}(f_{ij\mid z}).
}
\tag{3.9}
\]

The associated stopping rule is realizable: reveal the physical block
\[
A=[n]\setminus\{i,j\}
\]
and stop. The children are genuine two-variable restrictions, and every terminal defect is nonnegative by the exact table. Therefore (3.9) gives a nonnegative common-\(\Gamma_*\) block residual with no affine coordinate change and no reuse of terminal currency.

### Theorem 3.3 — sharp monotone/unate improvement

If \(f\) is unate, input/output negations turn it into a monotone gate. Checkerboard status of a two-face is invariant under these NPN operations, while a monotone two-face cannot be XOR/XNOR. Therefore
\[
X(f)=0.
\tag{3.10}
\]
Equation (2.5) sharpens to
\[
\overline T_2(f)
=\Delta\frac{M_2(f)}{N_2}
\le
\Delta\frac{I(f)-1}{n-1}.
\tag{3.11}
\]
Thus a physical paid pair exists already under the much weaker gap condition
\[
\boxed{
C_*-R(f)\ge\frac{\Delta}{n-1}.
}
\tag{3.12}
\]

This is the useful regime because \(\Delta=C_*-C_0=0.0670512\), about ninety-seven times smaller than \(C_*\).

## 4. Exact orientation/checkerboard dichotomy

The same calculation has a stronger contrapositive that preserves the old curvature-refund lesson.

Suppose **every** physical pair fails the stopped inequality:
\[
T_{ij}(f)>D_{\Gamma_*}(f)
\qquad\text{for all }i<j.
\tag{4.1}
\]
Then \(\overline T_2>D_{\Gamma_*}(f)\), so by (2.5), (3.2), and (3.5),
\[
\Delta\frac{I-1}{n-1}
+
C_0\frac{X(f)}{N_2}
>
(C_*-R)(I-1).
\]
Therefore
\[
\boxed{
C_0\,\frac{X(f)}{N_2}
>
(I(f)-1)
\left[
C_*-R(f)-\frac{\Delta}{n-1}
\right].
}
\tag{4.2}
\]

So a failure of every physical pair has only two possibilities:

1. the root is within \(\Delta/(n-1)\) of the stable cap; or
2. there is quantitatively forced XOR/XNOR orientation mass.

This is exactly the source-to-next-arrow use of the fleet01/B18 curvature-refund principle: the orientation component is not discarded. It becomes an explicit positive bank which a future non-unate proof must spend.

Using \(X\le M_2\), (4.2) also recovers the universal no-pair barrier
\[
\boxed{
C_*-R(f)<\frac{C_*}{n-1}.
}
\tag{4.3}
\]

None of (4.2)--(4.3) is a prescribed-coordinate statement; the pair is existential and chosen after seeing the entire gate.

## 5. Application: the entire monotone spine-graft tail from F4 onward is paid

The source-valid fleet02/B17 family has
\[
n_1=162,\qquad n_{t+1}=36n_t-27,
\tag{5.1}
\]
so
\[
n_2=5805,\quad
n_3=208953,\quad
n_4=7{,}522{,}281,\quad
n_5=270{,}802{,}089.
\tag{5.2}
\]

It also has singleton recurrence
\[
c_{t+1}=\frac{57+c_t^4}{256},
\tag{5.3}
\]
which contracts on \([0,1/4]\) by
\[
q=\frac1{4096},
\tag{5.4}
\]
and ratio recurrence
\[
R_{t+1}=(1-\lambda_t)R_t+\lambda_t T(c_t),
\qquad
1-\lambda_t\le
\rho:=\frac{1683}{35731}
<0.048.
\tag{5.5}
\]

The source proves
\[
c_1=\frac{14593}{65536},
\qquad
0.22266585228<c_\infty<0.22266585229,
\tag{5.6}
\]
\[
R_2\in[
6.5218511190811741401649047123071878637276611493668,
6.5218511190811741401649047123167742489206633278087],
\tag{5.7}
\]
and
\[
T(c_\infty)\in[
6.5218511673423727025654896282010361877746102003501,
6.5218511673532720920534233991583790594494969981239].
\tag{5.8}
\]

The same source bounds \(|K'(b)|<19\). Since
\[
T(c)=\frac{128}{133}K(c^4),
\]
for \(c\le1/4\),
\[
|T'(c)|
\le\frac{128}{133}\,19\,4c^3
\le\boxed{\frac87}.
\tag{5.9}
\]

Let \(T_\infty=T(c_\infty)\). From (5.6),
\[
|c_1-c_\infty|
<
\frac{14593}{65536}-0.22266585228
=0.0000056565090625.
\tag{5.10}
\]
Therefore the target errors at the updates producing \(R_3,R_4,R_5\) are bounded by
\[
\frac87(0.0000056565090625)q
<
1.578267037527902\times10^{-9},
\tag{5.11}
\]
then by the preceding quantity times \(q\), and so on.

Using (5.7)--(5.8), the initial uniform distance satisfies
\[
|R_2-T_\infty|
<
4.827209795188852\times10^{-8}.
\tag{5.12}
\]
Propagating (5.5) gives
\[
|R_3-T_\infty|
<
3.851977285016872\times10^{-9},
\tag{5.13}
\]
\[
|R_4-T_\infty|
<
1.818209847885523\times10^{-10}.
\tag{5.14}
\]
Because subsequent target errors shrink by \(q\), the invariant tail bound
\[
\boxed{
|R_t-T_\infty|
<
E:=1.8182108351059993\times10^{-10}
\quad(t\ge4)
}
\tag{5.15}
\]
follows from the geometric estimate
\[
E=e_4+\frac{\varepsilon_4}{1-\rho}.
\]

Combining (5.8) and (5.15),
\[
\boxed{
C_*-R_t
>
3.2464906824435976673\times10^{-8}
\qquad(t\ge4).
}
\tag{5.16}
\]

At the smallest such dimension,
\[
\boxed{
\frac{\Delta}{n_4-1}
=
8.913680426679145153\times10^{-9}.
}
\tag{5.17}
\]
The ratio of the lower gap in (5.16) to the threshold in (5.17) is
\[
>3.64214.
\tag{5.18}
\]
Since \(n_t\) increases, \(\Delta/(n_t-1)\) only decreases. Every \(F_t\) is monotone. Theorem 3.3 therefore gives:

\[
\boxed{
\text{For every }t\ge4,\text{ some physical pair }i,j
\text{ satisfies }
D_{\Gamma_*}(F_t)
\ge
\mathbb E_zD_{\Gamma_*}((F_t)_{ij\mid z}).
}
\tag{5.19}
\]

Thus the newest thin-spine monotone lower-bound family, despite converging to within roughly \(3.3\times10^{-8}\) of the stable cap, is **not** an asymptotic obstruction to this exact two-face physical restriction compiler from stage \(4\) onward.

This conclusion is analytic for the whole infinite family once the cited source intervals are accepted; it is not a finite truth-table sweep.

## 6. What changed and what remains

**Old missing implication.** Prove `LIMIT-PRIME-GATE-LIFT-v1` for every composition-prime gate/product bias, or find a counterexample.

**New proved inference.** On the balanced uniform slice, there is an exact dimension-gap physical pair selector. For unate gates the sufficient gap is only \(\Delta/(n-1)\). If no pair works for a general gate, the failure forces an explicit checkerboard/orientation bank (4.2). The entire current monotone spine-graft tail \(F_t,\ t\ge4\), satisfies the selector.

**Remaining universal implication.** Handle the residual corridor:
- bounded/medium arity gates that are within the dimension-gap threshold of \(C_*\);
- non-unate gates where the forced checkerboard bank in (4.2) must be converted into a signed restriction credit;
- arbitrary product biases, where the present uniform two-face table is not yet the needed full biased terminal identity.

The most direct next arrow is to derive the biased analogue of (2.2), or to show that the exact restriction cocycle spends the checkerboard bank forced by (4.2). This is still the one fixed `LIMIT-PRIME-GATE-LIFT-v1` target, not a new FEI route.

Full uniform-cube FEI remains **OPEN / NOT PROVED**.

## 7. Verification scope

`CHECKER.py` independently verifies the exact arity recurrence, the numerical interval propagation in (5.11)--(5.18), and the elementary coefficient inequality behind (3.3) for a large finite range as a regression check. The coefficient inequality and selector theorems are proved analytically above.

Executed checker SHA-256:
`3c4600813011dbbbd36274a3127f13008bc3112d9b95aa2f42bb55bd508a340f`.

Captured output SHA-256:
`3a8fb24a65ddb75d492f6446e7a1a9334f7c3685313e4393b92d955b6a43294f`.

Scoped privacy review: the files contain only FEI mathematics, repository-relative source references, public numerical constants from the cited proof artifacts, and sanitized logical worker provenance. No credentials, scheduler identifiers, machine paths, benchmark gold, unrelated private data, email/Drive action, paid compute, remote workflow, permission change, or public-posting action is included.
