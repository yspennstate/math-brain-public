# MOC4 account01/B07 r11b — exact generic counterexample to the parity-slack gate and the X-aware rescue identity

**Directive:** `COLLECTIVE-OPEN-PROBLEMS-20260921T234023Z`  
**Campaign:** MOC4, complex normal `4 x 4` Marcus–de Oliveira target  
**Worker:** account01/B07  
**Assignment:** exact exterior-power/minor expansion and the remaining mixed-minor inequality  
**Outcome:** `CANDIDATE_REFUTED` — the proposed universal pair-strict `MOC4-PARITY-SLACK-v1` gate fails on an exact simple-spectrum, irreducible, strict-compound, uniquely exposed true-unitary datum. The parent MOC4 target is **OPEN**.  
**Brain status:** `WITHOUT_VERIFIED_BRAIN`.

## 1. Source-exact target and live team state

For complex normal `4 x 4` matrices `A,B` with spectra `a_1,...,a_4` and `b_1,...,b_4`, the target is

\[
\det(A+B)\in\operatorname{conv}\left\{\prod_{i=1}^4(a_i+b_{\sigma(i)}):\sigma\in S_4\right\}.
\tag{MOC4}
\]

This run starts from the exact account01/B07 exterior-power reduction `MOC4-MIXED-ASSIGNMENT-v1`. After diagonalizing `A` and writing `B=U\operatorname{diag}(b)U^*`, define the one-minor matrix `P=(|u_{ij}|^2)`, the complementary-pair transport `R`, and its signed partner `D`. The earlier B07 identity gives

\[
D=(HPH^T)_{1^\perp}
\]

for the normalized Hadamard matrix `H`, and the full support problem is exactly

\[
\langle D,K\rangle+\frac12\langle R,X\rangle
\le
\max_{\sigma\in S_4}
\left\{\langle S_\sigma,K\rangle+\frac12\langle |S_\sigma|,X\rangle\right\}.
\tag{SR}
\]

Here the 24 matrices `S_sigma` are the tetrahedral signed `3 x 3` permutation matrices obtained from the standard representation of `S_4`.

I directly consume and apply the named OTHER-account partner **account02/B08**, `MOC4-BOUNDARY-CORE-AND-COLLAR-v1` (scientific commit `05ac3fec5e80a9471306a892a397d744faf20f50`). That result proves the repeated-spectrum and common-reducing-block boundaries, proves the exact gauge `(A,B)->(A+tI,B-tI)` removes individual singularity, and supplies strict collars around generic repeated-spectrum faces. Therefore a remaining counterexample may be sought on the simple-spectrum, individually invertible, irreducible core.

The newest completed campaign-lead run, account03/B07 `MOC4-ZERO-ENTRY-COMMON-LIFT-v1`, refutes the idea that a zero entry restores a common subset-permutation lift and explicitly leaves the **pair-strict interior** with the six-fiber/parity-slack obligation. The immediately preceding lead candidate `MOC4-PARITY-SLACK-v1` compressed `(SR)` to a proposed orientation-slack payment. This run attacks that live interior gate directly.

I also use account04/B09's exact common-`(P,R)` lift obstruction and its rational orthogonal witness. A tiny exact Givens perturbation turns that witness into a strict-compound interior unitary while preserving a strict failure of the parity-slack gate constructed below.

This mechanism is materially different from my preceding B07 `MOC4-DUAL-PLUCKER-FLOOR-v1` run: the present proof is a six-state Birkhoff-polytope calculation plus an exact structured counterexample, not another assignment-dual/Pluecker lower bound.

## 2. Six-fiber notation and an exact gap identity

For `rho in S_3`, let

\[
F_\rho(K)=\max_{\epsilon_1\epsilon_2\epsilon_3=1}
\sum_{i=1}^3\epsilon_i K_{i,\rho(i)}.
\]

Writing

\[
m_\rho(K)=
\begin{cases}
0,&\prod_iK_{i,\rho(i)}\ge0,\\
\min_i|K_{i,\rho(i)}|,&\prod_iK_{i,\rho(i)}<0,
\end{cases}
\]

we have the exact identity

\[
F_\rho(K)=\sum_i|K_{i,\rho(i)}|-2m_\rho(K).
\tag{1}
\]

Put

\[
x_\rho=\sum_i X_{i,\rho(i)},\qquad
M=\max_{\rho\in S_3}\left(F_\rho(K)+\frac12x_\rho\right),
\tag{2}
\]

and define the nonnegative fiber support gaps

\[
g_\rho=M-\left(F_\rho(K)+\frac12x_\rho\right)\ge0.
\tag{3}
\]

Finally define the exact orientation slack

\[
\mathcal S(D,R;K)
:=\langle R,|K|\rangle-\langle D,K\rangle
=\sum_{ij}\bigl(R_{ij}|K_{ij}|-D_{ij}K_{ij}\bigr).
\tag{4}
\]

### Theorem 1 — exact `X`-aware decomposition identity

For **every** Birkhoff decomposition

\[
R=\sum_{\rho\in S_3}\lambda_\rho R_\rho,
\qquad \lambda_\rho\ge0,\quad \sum_\rho\lambda_\rho=1,
\tag{5}
\]

the exact support gap in `(SR)` is

\[
\boxed{
M-\left(\langle D,K\rangle+\frac12\langle R,X\rangle\right)
=
\mathcal S(D,R;K)
-2\sum_\rho\lambda_\rho m_\rho(K)
+\sum_\rho\lambda_\rho g_\rho.
}
\tag{6}
\]

### Proof

Because `(5)` gives `x_R:=\langle R,X\rangle=\sum_\rho\lambda_\rho x_\rho`,

\[
\begin{aligned}
M-\langle D,K\rangle-\frac12x_R
&=\sum_\rho\lambda_\rho\left(M-\frac12x_\rho\right)-\langle D,K\rangle\\
&=\sum_\rho\lambda_\rho(F_\rho+g_\rho)-\langle D,K\rangle.
\end{aligned}
\]

Using `(1)` and `R=\sum\lambda_\rho R_\rho`,

\[
\sum_\rho\lambda_\rho F_\rho
=\langle R,|K|\rangle-2\sum_\rho\lambda_\rho m_\rho,
\]

which is `(6)`. QED.

This identity clarifies the parity-slack proposal exactly. If some decomposition satisfies

\[
2\sum_\rho\lambda_\rho m_\rho(K)\le\mathcal S(D,R;K),
\tag{PS}
\]

then `(SR)` follows immediately after dropping the nonnegative `g` term. Thus the **existential** parity-slack condition is indeed a valid sufficient condition for the actual fixed `X`. It does not require the stronger convex-roof argument. Conversely, if `(PS)` fails, `(SR)` can still hold because the actual structured `X` supplies the rescue term `\sum\lambda_\rho g_\rho`.

## 3. The Birkhoff existential collapses to two exact endpoints

For a `3 x 3` doubly stochastic matrix `R=(r_{ij})`, enumerate the six one-line permutations as

\[
123,231,312,132,213,321,
\]

with the first three even and the last three odd. The unique affine dependence is

\[
R_{123}+R_{231}+R_{312}
=R_{132}+R_{213}+R_{321}=J_3,
\tag{7}
\]

so the space of Birkhoff decompositions of a fixed `R` is one-dimensional.

Taking `t=lambda_{123}`, every decomposition is exactly

\[
\begin{aligned}
\lambda_{123}&=t,\\
\lambda_{231}&=t+r_{23}-r_{11},\\
\lambda_{312}&=t+r_{32}-r_{11},\\
\lambda_{132}&=r_{11}-t,\\
\lambda_{213}&=r_{33}-t,\\
\lambda_{321}&=r_{22}-t,
\end{aligned}
\tag{8}
\]

with

\[
L:=\max\{0,r_{11}-r_{23},r_{11}-r_{32}\}
\le t\le
U:=\min\{r_{11},r_{22},r_{33}\}.
\tag{9}
\]

Therefore the parity penalty

\[
M_K(t):=\sum_\rho\lambda_\rho(t)m_\rho(K)
\tag{10}
\]

is affine in `t`, and

\[
\boxed{
\min_{\lambda:\,(5)}\sum_\rho\lambda_\rho m_\rho(K)
=\min\{M_K(L),M_K(U)\}.
}
\tag{11}
\]

Hence `MOC4-PARITY-SLACK-v1` is not an optimization problem anymore: its universal assertion is exactly the single explicit endpoint inequality

\[
\boxed{
2\min\{M_K(L),M_K(U)\}\le\mathcal S(D,R;K).
}
\tag{12}
\]

The counterexample below shows `(12)` is **false even on the generic source-valid MOC4 core**.

## 4. Exact generic structured counterexample to `(12)`

Start from the exact rational orthogonal matrix used in account04/B09's common-`(P,R)` lift obstruction,

\[
U_0=\begin{pmatrix}
 492/625&-31/625&-48/125&12/25\\
 -9/25&12/25&-4/5&0\\
 -36/125&48/125&9/25&4/5\\
 -256/625&-492/625&-36/125&9/25
\end{pmatrix}.
\tag{13}
\]

Let `G_{14}(c,s)` be the real Givens rotation on columns `1,4` and set

\[
c=\frac{24999999}{25000001},\qquad
s=\frac{10000}{25000001},\qquad
U=U_0G_{14}(c,s).
\tag{14}
\]

Exact arithmetic verifies that `U` is orthogonal, **all 16 entries are nonzero**, and all 18 designated complementary `2 x 2` minors used to form `(R,D)` are nonzero. Thus `|D_{ij}|<R_{ij}` in every cell.

Take the exact rational complex spectra

\[
\begin{aligned}
a={}&(-9/40-39i/20,\;-7/20-37i/40,\;-13/10+13i/40,\;1/4-7i/10),\\
b={}&(-1/40+11i/40,\;13/40+17i/40,\;-23/40-21i/40,\;-59/40+33i/40),
\end{aligned}
\tag{15}
\]

and support direction `eta=1`. Both spectra are simple and nonzero. Since `A` has simple spectrum and `U` has no zero entry, a common reducing coordinate block would force a zero rectangular block in `U`; hence the pair is irreducible. The datum therefore lies in the residual simple-spectrum, invertible, irreducible, strict-compound core singled out by the partner account02/B08 theorem, not on a boundary case already solved there.

The exact B07 coefficient construction gives

\[
K=\begin{pmatrix}
245983/5120000&5030591/5120000&-39077/1024000\\
-5113569/5120000&56671/5120000&19643/1024000\\
-8539/1024000&-35819/1024000&5009153/5120000
\end{pmatrix},
\tag{16}
\]

and

\[
X=\begin{pmatrix}
-3609633/1280000&111173/51200&2385071/1280000\\
-917133/1280000&1431961/1280000&525623/256000\\
-1352967/1280000&1061147/1280000&948017/1280000
\end{pmatrix}.
\tag{17}
\]

For this exact true-unitary datum, the two Birkhoff endpoints satisfy

\[
L=0,
\qquad
U=\frac{673669333687725216}{8418642914870703125},
\tag{18}
\]

and the smaller parity penalty is

\[
M_{\min}
=\frac{297835083875558166821318503}
{1250000100000002000000000000}
\approx0.2382680480.
\tag{19}
\]

The orientation slack is

\[
\mathcal S
=\frac{292305267845517476382331431}
{625000050000001000000000000}
\approx0.4676883911.
\tag{20}
\]

Therefore

\[
\boxed{
2M_{\min}-\mathcal S
=
\frac{86403375469385788109173}
{9765625781250015625000000}
>0,
}
\tag{21}
\]

numerically about `0.00884770494`. Since `(11)` is the exact minimum over **all** Birkhoff decompositions of `R`, no decomposition satisfies `(PS)`.

Thus the proposed universal pair-strict `MOC4-PARITY-SLACK-v1` condition is false on a source-valid generic MOC4 datum.

## 5. This is not a counterexample to MOC4: the structured X term rescues it

Enumerating the exact six fiber values in `(2)` gives a unique maximizing fiber `rho=(2,3,1)` in one-based notation. Enumerating the four allowed even sign patterns in every fiber gives a **unique maximizer among all 24 signed S4 endpoint images**.

The exact left and right sides of `(SR)` are

\[
\operatorname{LHS}
=\frac{2220845529469952017022870089}
{1250000100000002000000000000},
\]

\[
\operatorname{RHS}
=\frac{13195057}{5120000},
\]

and therefore

\[
\boxed{
\operatorname{RHS}-\operatorname{LHS}
=
\frac{125075523892079396068283817}
{156250012500000250000000000}
>0,
}
\tag{22}
\]

numerically about `0.80048328887`. Hence this datum is safely inside the correct support half-plane. It refutes only the parity-slack proof gate, not MOC4.

At the endpoint decomposition minimizing the parity penalty, the actual support-gap rescue in `(6)` is

\[
\sum_\rho\lambda_\rho g_\rho
=\frac{1945507352301377979662009}
{2403846346153850000000000}
\approx0.80933099381.
\tag{23}
\]

The verifier checks the exact identity

\[
\left(\sum_\rho\lambda_\rho g_\rho\right)
-\left(2M_{\min}-\mathcal S\right)
=\operatorname{RHS}-\operatorname{LHS},
\tag{24}
\]

so the failure mechanism is completely accounted for: the dropped `X`-dependent support gap is not a lower-order nuisance; here it is the decisive payment.

## 6. Compact conditional end-to-end argument after this run

The current route is now:

1. By account02/B08 `MOC4-BOUNDARY-CORE-AND-COLLAR-v1`, repeated spectra, common reducing blocks, and individual singularity are removed exactly; only the simple-spectrum, individually-invertible, irreducible core remains essential.
2. By the newest account03/B07 lead result, zero-entry structure does not restore a common subset-permutation lift. The pair-strict interior remains the genuine core.
3. By account01/B07 `MOC4-MIXED-ASSIGNMENT-v1`, the full support problem on that core is exactly `(SR)`.
4. The proposed universal parity-slack gate `(12)` is now refuted by the exact generic datum `(13)`--`(21)`.
5. Therefore any complete proof must retain the **actual X-dependent fiber gaps**. The exact identity `(6)` gives the next smallest obligation.

A convenient canonical choice is the endpoint decomposition `lambda*` that minimizes the parity penalty. Then the first surviving implication can be written as

> **`MOC4-SUPPORT-GAP-RESCUE-v1`.** For every source-valid generic MOC4 datum,
> \[
> \boxed{
> \sum_\rho\lambda^*_\rho g_\rho
> \ge
> 2\sum_\rho\lambda^*_\rho m_\rho(K)-\mathcal S(D,R;K).
> }
> \tag{25}
> \]
> Whenever the right side is nonpositive, the old parity-slack gate already closes the datum. The genuinely residual regime is the positive-deficit case, where `(25)` asks the structured `X`-support gaps to pay exactly the unpaid parity deficit.

Equation `(25)` is equivalent to the exact six-fiber support inequality, but it separates the already-controlled orientation slack from the now-proved-essential `X` rescue and reduces the Birkhoff choice to one explicit endpoint. It is therefore a sharper target for the next cycle-by-cycle / structured-coefficient argument than the refuted X-free parity-slack conjecture.

## 7. Verification and safeguards

The companion verifier uses Python standard-library `Fraction` arithmetic only. It verifies:

- exact orthogonality of `(14)`;
- nonzero all 16 entries and all designated complementary `2 x 2` minors;
- exact reconstruction of `(K,X)` from the source spectra via the B07 exterior-power formulas;
- strict `|D|<R`, row/column stochasticity of `R`;
- the complete one-parameter Birkhoff family `(8)`--`(9)` and exact endpoint minimum `(11)`;
- the strict parity-slack failure `(21)`;
- all 24 signed endpoint support values, with a unique maximizer;
- the positive exact `(SR)` margin `(22)`;
- the exact rescue identity `(24)`.

Verifier: `verify_parity_slack_refutation.py`.  
Verification output: `VERIFICATION.txt`.

No benchmark gold, held-out answers, keys, credentials, scheduler identifiers, machine paths, unrelated private data, email, Drive, public posting, paid model/API calls, Codex, remote workflows, or permission changes were used. The parent MOC4 conjecture remains open.
