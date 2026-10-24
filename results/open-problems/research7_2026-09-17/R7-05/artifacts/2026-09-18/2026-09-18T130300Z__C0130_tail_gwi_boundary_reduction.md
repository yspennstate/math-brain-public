Model actually running: GPT-5.6 Sol. Reasoning level: UNVERIFIED. This is not GPT-6 at maximum; authenticated runtime reasoning-effort telemetry and a binding model/effort selector are not exposed.

# C0130 — exact critical-GWI tail representation and finite boundary gluing

Target: `C0130`, Kosygina–Zerner Problem 3.12, escape probability of a transient one-dimensional excited random walk.  
Status of this artifact: **PARTIAL**. The frozen source-matching metric `M_closed` remains 2. The results below identify a classical critical Galton–Watson-with-immigration tail and compute the full depth-three low-state defect exactly; they do not evaluate the remaining generic depth-three connection coefficient.

## 1. Setup

Let a fresh site have an i.i.d. bounded cookie stack

\[
(p_1,\ldots,p_M,1/2,1/2,\ldots),
\]

and let

\[
\alpha_j=2p_j-1,\qquad
\delta=\mathbb E\sum_{j=1}^M\alpha_j.
\]

At the fresh site, let `S_k` denote the number of successes observed before the `k`-th failure. The annealed forward branching chain is

\[
V_{n+1}=S^{(n+1)}_{V_n},
\]

with state 0 absorbing. The preceding R7-05 run proved the Siegmund-dual identity

\[
s(k):=P_k(V\text{ survives})=\sum_{i<k}\pi_i,
\qquad
p_{\rm esc}=\mathbb E[p_1]s(1),
\]

where `pi` is the stationary law of the standard backward branching chain. For depth three,

\[
\kappa=\frac{\pi_1}{\pi_0}=\frac{s(2)-s(1)}{s(1)}
\]

is the remaining connection coefficient.

## 2. B1 — change category: the entire high-state kernel is exactly critical GWI

Let

\[
T(z)=\frac1{2-z},
\]

the pgf of a fair geometric random variable `G`, where `G` counts successes before one fair failure. Let `K` be the number of successes among the first `M` cookie tosses at a fresh site.

### Theorem 2.1 — tail GWI representation

For every integer `k>=M`,

\[
\boxed{
S_k\overset d=
K+\sum_{r=1}^{k-M+K}G_r,
}
\tag{2.1}
\]

and therefore, conditional on the site stack,

\[
\begin{aligned}
\mathbb E[z^{S_k}\mid(p_1,\ldots,p_M)]
&=T(z)^{k-M}\prod_{j=1}^M\big((1-p_j)+p_j zT(z)\big)\\
&=T(z)^k\prod_{j=1}^M\big((1-\alpha_j)+\alpha_j z\big).
\end{aligned}
\tag{2.2}
\]

After annealing over the fresh stack, define

\[
\boxed{
B(z)=\mathbb E\prod_{j=1}^M\big((1-\alpha_j)+\alpha_j z\big).
}
\tag{2.3}
\]

Then the exact high-state transition pgf is

\[
\boxed{
\mathbb E[z^{S_k}]=T(z)^kB(z),\qquad k\ge M.
}
\tag{2.4}
\]

If the cookies are nonnegative, `p_j>=1/2` almost surely, then `alpha_j in [0,1]`. Conditional on the site stack, introduce independent auxiliary Bernoulli variables

\[
J_j\mid(p_1,\ldots,p_M)\sim\operatorname{Bernoulli}(\alpha_j)
\]

and set

\[
I=\sum_{j=1}^M J_j.
\]

Then `B` is the genuine pgf of `I`, and for every `k>=M`

\[
\boxed{
S_k\overset d=\sum_{r=1}^kG_r+I.
}
\tag{2.5}
\]

Thus the forward ERW branching chain is, outside the finite set `{1,...,M-1}`, **exactly a critical Galton–Watson process with fair-geometric offspring and immigration `I`**.

Moreover,

\[
\boxed{\mathbb E I=B'(1)=\delta,}
\tag{2.6}
\]

and hence

\[
\mathbb E[S_k-k]=\delta,
\qquad
\operatorname{Var}(S_k)=2k+\operatorname{Var}(I)
\quad(k\ge M).
\tag{2.7}
\]

### Proof

Among the first `M` tosses there are `M-K` failures. If `k>=M`, the number of additional fair failures required to reach the `k`-th failure is exactly `k-M+K>=0`. Between successive fair failures the numbers of fair successes are independent copies of `G`, proving (2.1). Taking pgfs gives the first line of (2.2).

For one cookie,

\[
(1-p)+pzT(z)
=\frac{2-2p+(2p-1)z}{2-z}
=T(z)\big((1-\alpha)+\alpha z\big),
\]

which proves the second line of (2.2), and averaging proves (2.3)–(2.4). Under nonnegative cookies the last product is a conditional Bernoulli-sum pgf, proving (2.5). Differentiating (2.3) at 1 gives (2.6), and the critical geometric offspring have mean 1 and variance 2, giving (2.7). `QED`

### Scope warning

For cookies of mixed sign, identity (2.4) remains algebraically exact, but `B` need not have nonnegative coefficients and therefore need not itself be a probability pgf. The probabilistic GWI interpretation is asserted only when `B` is a pgf, in particular throughout the nonnegative-cookie subclass.

## 3. B21 — analogue import and prior-art boundary

The exact representation above changes the remaining problem from an opaque ERW tail to a classical stopped critical-GWI tail plus finitely many exceptional rows. This sits directly beside known branching-process literature and must not be advertised as a literature novelty without a much deeper search.

Relevant prior art recovered on 2026-09-18:

1. Kosygina–Zerner, *Positively and negatively excited random walks on integers, with branching processes* (EJP 2008), already bases the one-dimensional ERW theory on branching processes with migration.
2. Kosygina–Zerner, *Excursions of excited random walks on integers* (EJP 2014; arXiv:1307.6830), analyzes the related forward process by branching/diffusion methods and proves power-law extinction/survival asymptotics. In particular the source-adjacent literature already identifies the tail exponent; this run does **not** claim discovery of that exponent.
3. Ivanoff–Seneta (1985), *The critical branching process with immigration stopped at zero*, and Klebaner–Sagitov (2002), *The age of a Galton–Watson population with a geometric offspring distribution*, treat critical immigration processes stopped at zero, including the geometric-offspring setting.

The useful new reduction for this repository is therefore not “branching processes occur.” It is the **exact finite-depth decomposition**: the source-specific information is confined to a finite boundary defect, while the entire high-state kernel is a standard critical-GWI kernel with explicitly identified immigration pgf (2.3).

For `delta>1`, the source-adjacent asymptotics imply that the extinction harmonic profile has the form

\[
1-s(k)\asymp k^{1-\delta}
\]

(and in the stronger cited formulation is asymptotic to a positive constant times this power). Hence the tail profile is one-dimensional at leading order but its amplitude is not determined by the exponent. That amplitude is exactly the kind of finite-boundary connection coefficient which the source escape probability needs.

## 4. B30 — localize the gluing failure: exact depth-three boundary defect

Now take `M=3`. First condition on a deterministic triple `(p_1,p_2,p_3)` and write

\[
\alpha_j=2p_j-1.
\]

Let `Q^*` denote the auxiliary stopped critical-GWI chain whose positive-state transition pgfs are

\[
Q_k^*(z)=T(z)^kB(z),\qquad k\ge1,
\]

where

\[
B(z)=\prod_{j=1}^3\big((1-\alpha_j)+\alpha_j z\big).
\]

The true forward ERW chain agrees with `Q^*` for every `k>=3`. Its first two row pgfs are obtained by direct stopping of the first three cookie tosses:

\[
P_1(z)=
(1-p_1)+p_1(1-p_2)z+p_1p_2(1-p_3)z^2+p_1p_2p_3z^3T(z),
\tag{4.1}
\]

and

\[
\begin{aligned}
P_2(z)={}&(1-p_1)(1-p_2)\\
&+\big[p_1(1-p_2)(1-p_3)+(1-p_1)p_2(1-p_3)\big]z\\
&+\big[(1-p_1)p_2p_3+p_1(1-p_2)p_3+p_1p_2(1-p_3)\big]z^2T(z)\\
&+p_1p_2p_3z^3T(z)^2.
\end{aligned}
\tag{4.2}
\]

Define

\[
\boxed{
A=\frac{(1-\alpha_1)(\alpha_2+\alpha_3-\alpha_2\alpha_3)}2,
}
\tag{4.3}
\]

\[
\boxed{
D=\frac{\alpha_3(1+\alpha_1+\alpha_2-3\alpha_1\alpha_2)}4,
}
\tag{4.4}
\]

\[
\boxed{
C=\frac{\alpha_3(1-\alpha_1)(1-\alpha_2)}4.
}
\tag{4.5}
\]

### Theorem 4.1 — exact two-row defect

One has the polynomial identities

\[
\boxed{
P_1(z)-Q_1^*(z)=A(1-z)+Dz(1-z),
}
\tag{4.6}
\]

and

\[
\boxed{
P_2(z)-Q_2^*(z)=C(1-z).
}
\tag{4.7}
\]

For a random i.i.d. depth-three stack, the same formulas hold after replacing `A,D,C` by their expectations.

If all three cookies are nonnegative then `A,D,C>=0`. Indeed `A,C>=0` are immediate, while for `x,y in [0,1]`,

\[
1+x+y-3xy\ge0
\]

because this expression is affine in `x` and at `x=0,1` equals `1+y` and `2(1-y)` respectively. Therefore the true low-row transition laws are stochastically no larger than the auxiliary GWI rows. Explicitly, for row 1 the cumulative true-minus-auxiliary mass is `A` at state 0 and `D` through state 1, and returns to zero after state 2; for row 2 it is `C` at state 0 and zero thereafter.

Thus, under nonnegative cookies, the full forward ERW process can be coupled below the auxiliary stopped critical-GWI process, and

\[
\boxed{s(k)\le s^*(k)\qquad(k\ge0),}
\tag{4.8}
\]

where `s^*` is the auxiliary GWI survival function.

### Proof

Equations (4.1)–(4.2) come from enumerating whether the first or second failure occurs among the first three cookie tosses, with `T` or `T^2` appended only if fair failures are still needed. Subtracting `T B` and `T^2B` and simplifying gives (4.6)–(4.7). The exact symbolic checker archived with this artifact independently verifies the identities over the polynomial ring `Q[p1,p2,p3,z]`.

The sign claim follows from (4.3)–(4.5). The row-1 signed mass difference is

\[
A\,\delta_0+(D-A)\,\delta_1-D\,\delta_2,
\]

so its cumulative sums are `A,D,0`; the row-2 difference is `C delta_0-C delta_1` with cumulative sums `C,0`. Hence each true low row is stochastically below the corresponding auxiliary row. Since `Q^*` is stochastically monotone in its starting population (`sum_{r=1}^k G_r+I`), the standard quantile coupling propagates the order pathwise and proves (4.8). `QED`

## 5. Exact finite-rank gluing formula

The previous theorem does more than compare the two chains. It makes the unresolved connection coefficient a finite-rank perturbation of a classical stopped-GWI potential kernel.

Let `K^*` and `K` be the positive-state substochastic kernels of the auxiliary and true chains, respectively. Let

\[
U^*_{ki}=\sum_{n\ge0}(K^{*n})(k,i)
\]

be the auxiliary expected number of visits to state `i` before absorption. In the transient `delta>1` regime these finite-state Green quantities are finite. Let `s^*` and `s` be the corresponding survival functions. Then

\[
s^*-s=K^*(s^*-s)+(K^*-K)s.
\]

Because `K^*-K` is supported only in rows 1 and 2, iteration of this identity, together with `s^*(k)-s(k)->0` as `k->infinity`, gives

\[
\boxed{
 s_k^*-s_k
 =U^*_{k1}\big(A s_1+D(s_2-s_1)\big)
 +U^*_{k2}C s_1.
}
\tag{5.1}
\]

Putting `x=s_1`, `y=s_2` and restricting (5.1) to `k=1,2` yields the exact two-by-two system

\[
\boxed{
\big[1+(A-D)U^*_{11}+CU^*_{12}\big]x
 +D U^*_{11}y=s_1^*,
}
\tag{5.2}
\]

\[
\boxed{
\big[(A-D)U^*_{21}+CU^*_{22}\big]x
 +\big[1+D U^*_{21}\big]y=s_2^*.
}
\tag{5.3}
\]

This is the cleanest current gluing statement: generic depth-three ERW escape is reduced to six finite potential quantities of one **classical auxiliary stopped critical-GWI chain**, followed by a two-by-two linear solve. It is not yet a source-level closed formula because those finite GWI quantities have not been evaluated symbolically for arbitrary immigration law `B`.

### Justification of the Green iteration

The forcing `(K^*-K)s` is supported on `{1,2}`. In the `delta>1` regime the stopped GWI visits each fixed finite set only finitely often on its survival event, while on extinction it is eventually absorbed. Thus its potential of a finitely supported forcing is finite. Furthermore both extinction probabilities tend to zero with the starting population, so `s^*(k)-s(k)->0`; applying the Markov property to the remainder term `(K^*)^n(s^*-s)` and dominated convergence removes it. This yields (5.1).

## 6. The deterministic `4/5,4/5,4/5` benchmark becomes exceptionally sparse

Take

\[
p_1=p_2=p_3=\frac45,
\qquad
\alpha_1=\alpha_2=\alpha_3=\frac35.
\]

Then the auxiliary immigration variable is exactly

\[
I\sim\operatorname{Binomial}(3,3/5),
\]

with

\[
\boxed{
B(z)=\frac{8+36z+54z^2+27z^3}{125},
}
\tag{6.1}
\]

and

\[
A=D=\frac{21}{125},
\qquad
C=\frac3{125}.
\tag{6.2}
\]

Therefore

\[
\boxed{
P_1(z)-Q_1^*(z)=\frac{21}{125}(1-z^2),
}
\tag{6.3}
\]

\[
\boxed{
P_2(z)-Q_2^*(z)=\frac3{125}(1-z).
}
\tag{6.4}
\]

So, relative to the pure stopped GWI, the entire ERW-specific defect is exactly:

- in row 1, move mass `21/125` from state 2 directly to 0;
- in row 2, move mass `3/125` from state 1 directly to 0;
- leave every row `k>=3` unchanged.

The Green gluing system collapses to

\[
\boxed{
(1+\tfrac3{125}U^*_{12})s_1
+\tfrac{21}{125}U^*_{11}s_2=s_1^*,
}
\tag{6.5}
\]

\[
\boxed{
\tfrac3{125}U^*_{22}s_1
+(1+\tfrac{21}{125}U^*_{21})s_2=s_2^*.
}
\tag{6.6}
\]

This is a strict sharpening of the preceding “unknown `s(2)/s(1)`” diagnosis: the benchmark blocker is now a finite potential computation for the stopped critical geometric-GWI with Binomial(3,3/5) immigration.

## 7. Exact verification

The script

`research7_2026-09-17/R7-05/artifacts/2026-09-18/2026-09-18T130000Z__C0130_tail_gwi_boundary_checker.py`

symbolically verifies (4.6), (4.7), `B'(1)=alpha_1+alpha_2+alpha_3`, and all benchmark rational identities. Its archived execution output ends

`ALL_EXACT_CHECKS_PASS`.

No numerical truncation or fitted asymptotic is used to establish any theorem above.

## 8. What moved and what did not

The mathematical structure moved substantially:

1. every nonnegative finite-depth source instance has a **standard critical-GWI tail** with explicit immigration pgf;
2. the generic depth-three source has an exact two-row boundary defect;
3. the first unresolved deterministic benchmark has only two explicit downward mass shifts;
4. the remaining escape computation is an exact finite-rank Green-potential gluing problem for a classical stopped GWI.

But the frozen metric does **not** move:

\[
\boxed{M_{\rm closed}:2\to2.}
\]

No universal symbolic evaluation of the depth-three Green data `(s_1^*,s_2^*,U^*_{11},U^*_{12},U^*_{21},U^*_{22})` has been proved, so claiming `M_closed=3` would be false.

## 9. Next mathematical target

Do not return to generic stationary moments or higher truncation heights. The next useful step is to attack the auxiliary stopped-GWI potential itself. Two concrete possibilities are now sharply defined:

1. derive a special-function or dual-chain formula for `U^*_{ij}` and `s_i^*` for geometric offspring and polynomial immigration `B`;
2. prove that no elementary finite-moment formula can determine these quantities, which would explain why the depth-three source resists closure and would justify a different notion of “compute.”

For the `4/5` benchmark, any successful calculation of the six classical quantities in (6.5)–(6.6) immediately gives `s_1`, hence

\[
p_{\rm esc}=\frac45s_1.
\]
