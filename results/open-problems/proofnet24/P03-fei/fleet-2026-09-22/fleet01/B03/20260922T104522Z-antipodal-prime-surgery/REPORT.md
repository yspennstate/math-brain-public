# B03 — antipodal sparse surgery gives an explicit growing-arity composition-prime family

**Programme:** FEI-ALL-TEAM-20260922T095941Z  
**Assignment:** fleet01/B03, Path A, “Prime sparse surgery family”  
**Run:** `20260922T104522Z-antipodal-prime-surgery`  
**Classification:** `ESSENTIAL_STEP_APPLIED / FAMILY-SPECIFIC MARGIN THEOREM / FULL_FEI_OPEN`  
**Execution:** `WITHOUT_VERIFIED_BRAIN`.

The current owner control (revision 2026-09-22.3) supersedes the older FOREST allocation: all workers are now on FEI. This report does no new FOREST, installation, or benchmark work.

## 1. Result

For every `n>=3`, define the Boolean gate `f_n:{-1,+1}^n->{-1,+1}` by starting from the dictator `x_1` and flipping exactly the two antipodal truth-table entries `(+1,...,+1)` and `(-1,...,-1)`:

\[
f_n(x)=\begin{cases}
-x_1,&x=(+1)^n\text{ or }x=(-1)^n,\\
x_1,&\text{otherwise.}
\end{cases}
\tag{1.1}
\]

Equivalently, in `{0,1}` notation,

\[
F_n(z)=z_1\oplus {\bf 1}_{z=0^n}\oplus {\bf 1}_{z=1^n}
=z_1\oplus\prod_i(1\oplus z_i)\oplus\prod_i z_i.
\tag{1.2}
\]

I prove:

1. **Booleanity and essentiality.** Every coordinate is essential.
2. **Composition primality.** `F_n` admits no nontrivial disjoint-variable Boolean decomposition with an inner block of size at least two. Thus this is a genuine growing-arity composition-prime family, despite being only a two-row surgery of a dictator.
3. **Exact uniform spectrum.** Put
   \[
   \alpha_n=2^{2-n}.
   \]
   Then
   \[
   \widehat f_n(S)=
   \begin{cases}
   1-\alpha_n,&S=\{1\},\\
   -\alpha_n,&|S|\text{ odd and }S\ne\{1\},\\
   0,&|S|\text{ even}.
   \end{cases}
   \tag{1.3}
   \]
4. **Exact one-core biased spectrum and all-gate defect.** In the project convention `p_i=Pr[X_i=-1]`, set `p_1=t` and `p_2=...=p_n=1/2`. If `C=Gamma(1/2)`, `c=1-2t`, `V=4t(1-t)`, `alpha=alpha_n`, and
   \[
   q=t+\frac{\alpha c}{2},
   \tag{1.4}
   \]
   then the gate defect is exactly
   \[
   \boxed{
   D_{\Gamma,n}(t)=
   (1-\alpha)\Gamma(t)+(n-1)\alpha C-\Gamma\!\left(t+\frac{\alpha(1-2t)}2\right)
   +2(1-\alpha)^2\log_2(1-\alpha)
   -(4\alpha-2\alpha^2)(n-2).}
   \tag{1.5}
   \]
   Thus the entire growing-arity prime family reduces to a **one-dimensional finite-difference test of `Gamma`**.
5. **Margin theorem.** At the balanced point,
   \[
   D_{\Gamma,n}(1/2)=
   \alpha(n-2)(C-4+2\alpha)+2(1-\alpha)^2\log_2(1-\alpha),
   \tag{1.6}
   \]
   and
   \[
   \frac{H(f_n)}{I(f_n)-1}\to4.
   \tag{1.7}
   \]
   Hence this sparse-prime family does **not** obstruct any fixed center `C>4` asymptotically at a fixed interior one-core bias. If `Gamma` is differentiable at fixed `t in (0,1)`, its normalized quadratic demand satisfies
   \[
   c_{f_n}(t):=-\frac{D_{\Gamma,n}(t)}{M_n(t)}\longrightarrow -4(C-4),
   \tag{1.8}
   \]
   where
   \[
   M_n(t)=\frac{I_t(f_n)}4-q(1-q)
   =\frac{\alpha}{4}\bigl[n-2-(1-2t)^2(1-\alpha)\bigr].
   \tag{1.9}
   \]

For the current source-reported refined candidate center `C*=6.5584452830718245...`, the limiting normalized demand is about `-10.2337811323`, i.e. large positive slack rather than a new obstruction. The useful output is therefore the prime family and exact scalar reduction (1.5), especially for boundary-layer choices `t=t_n`, not a claim that FEI is solved.

## 2. Named other-account result actually applied

The source-bound other-account result used here is fleet02/B17,

`yspennstate/math-open-problems@f5946fb64d336ed7369de279159643944efc47af`,
`proofnet24/P03-fei/fleet-2026-09-21/fleet02/B17/20260922T091146Z-strong-prime-shaped-repair/REPORT.md`.

That report gives the exact all-gate normalization

\[
D_\Gamma=\sum_i\frac{I_i^t}{V_{p_i}}\bigl(\Gamma(p_i)+h_2(V_{p_i})\bigr)-\Gamma(q)-\widetilde H_G,
\quad
M_G=I_t/4-q(1-q),
\quad c_G=-D_G/M_G,
\tag{2.1}
\]

and exhibits a finite 18-input composition-prime source that strongly refutes the old quadratic candidates. I apply **that exact normalization** to the family (1.1): the pivotality ratios are computed in Section 5, the full biased spectral entropy in Section 6, and they collapse to (1.5) and (1.9). Thus the peer normalization changes the calculation, not merely the bibliography.

The designated current partner is fleet02/B03. At the pre-write snapshot there was no completed `proofnet24/P03-fei/fleet-2026-09-22/fleet02/B03/` artifact yet, so there was no partner theorem to consume without fabrication. Work therefore proceeded asynchronously from the named complete other-account source above, as allowed by the memory protocol.

The all-gate definition itself is pinned at
`yspennstate/math-open-problems@a898203278af25794901b42c965816e0d9df7e11`,
`proofnet24/P03-fei/continuations/2026-09-22-gate-reformulation/REPORT.md`.

## 3. Composition-primality proof

A nontrivial disjoint-variable decomposition with an inner block `A`, `2<=|A|<=n-1`, has the form

\[
F_n(z)=H(g(z_A),z_{A^c})
\tag{3.1}
\]

after absorbing all other inner outputs into the outer function. Therefore, as `z_A` varies, the truth-table rows against `z_{A^c}` can take at most two values; equivalently, when both sides have at least two variables, the ANF coefficient flattening across `A|A^c` has rank at most two over `F_2`.

From (1.2), the ANF coefficient tensor is

\[
e_{\{1\}}+\mathbf 1+e_{[n]}.
\tag{3.2}
\]

Across a split `A|B`, this is a sum of three rank-one tensors. If `1 in A`, the left factors are

\[
e_{\{1\}},\quad \mathbf 1_A,\quad e_A,
\]

and the right factors are

\[
e_\varnothing,\quad \mathbf 1_B,\quad e_B.
\]

When `|A|,|B|>=2`, both triples are linearly independent over `F_2`, hence the flattening has rank exactly three. The case `1 in B` is symmetric. Therefore no decomposition (3.1) exists whenever the outside block has at least two coordinates.

It remains to treat `|B|=1`, where a rank-three flattening is dimensionally impossible. Let the outside coordinate be `j`.

* If `j=1`, the output pairs `(F_n(z_A,0),F_n(z_A,1))` include `(1,1)` at `z_A=0^{n-1}`, `(0,0)` at `z_A=1^{n-1}`, and `(0,1)` at every nonconstant `z_A`. Thus at least three row types occur.
* If `j!=1`, the rows include `(1,0)` at the two constant `A`-assignments, `(0,0)` at an `A`-assignment with `z_1=0` but not all zero, and `(1,1)` at one with `z_1=1` but not all one. Again at least three row types occur.

Since a one-bit summary `g(z_A)` permits at most two row types, (3.1) is impossible. Every nontrivial inner block is excluded. All coordinates are essential: for `i>=2`, compare the all-`+1` row with the row obtained by flipping coordinate `i`; for coordinate `1`, choose the remaining coordinates nonconstant and flip `x_1`. This proves composition primality for every `n>=3`.

## 4. Exact uniform Walsh law

Start from the dictator `x_1`. The surgery changes the function by

\[
\Delta f=-2\mathbf 1_{(+1)^n}+2\mathbf 1_{(-1)^n}.
\]

Therefore

\[
\Delta\widehat f(S)=2^{-n}\bigl(-2+2(-1)^{|S|}\bigr).
\]

This is zero for even `|S|` and `-2^{2-n}=-alpha` for odd `|S|`, giving (1.3).

Consequently

\[
I(f_n)=1+\alpha(n-2),
\tag{4.1}
\]

and

\[
H(f_n)=
- (1-\alpha)^2\log_2(1-\alpha)^2
-\bigl(2^{n-1}-1\bigr)\alpha^2\log_2\alpha^2.
\tag{4.2}
\]

Since `2^{n-1}=2/alpha` and `log_2(1/alpha)=n-2`,

\[
H(f_n)=
-2(1-\alpha)^2\log_2(1-\alpha)
+(4\alpha-2\alpha^2)(n-2).
\tag{4.3}
\]

Dividing by `I-1=alpha(n-2)` gives (1.7), because the logarithmic term contributes only `2/(ln 2)(n-2)^{-1}+o(1/n)` after normalization.

At a balanced gate, the all-gate defect is `D=C(I-1)-H`, so (4.1) and (4.3) give (1.6) exactly.

## 5. Exact one-core pivotality and output bias

Use the project convention `p_i=Pr[X_i=-1]`. Let `p_1=t` and all other inputs be unbiased. Put `alpha=2^{2-n}` and `c=1-2t`.

The all-negative and all-positive rows have probabilities `t 2^{-(n-1)}` and `(1-t)2^{-(n-1)}`. The base dictator has output probability `t`; the two flips therefore give

\[
q=t+2^{-(n-1)}(1-2t)=t+\frac{\alpha c}{2}.
\]

For coordinate 1, the gate fails to be pivotal only when coordinates `2,...,n` are all equal. Hence

\[
b_1:=I_1^t/V_t=1-\alpha.
\tag{5.1}
\]

For every `i>=2`, the gate is pivotal exactly when all the other coordinates are all positive or all negative. These two events have total probability `alpha`, hence

\[
b_i:=I_i^t/V_{1/2}=\alpha,\qquad i=2,...,n.
\tag{5.2}
\]

Thus

\[
I_t(f_n)=V_t(1-\alpha)+(n-1)\alpha.
\tag{5.3}
\]

Since the output mean is `(1-2t)(1-alpha)=c(1-alpha)`, its variance is

\[
V_q=1-c^2(1-\alpha)^2.
\]

Subtracting gives

\[
I_t-V_q=\alpha\bigl[n-2-c^2(1-\alpha)\bigr],
\]

which is (1.9).

## 6. Exact one-core biased spectrum and entropy collapse

Let `V=4t(1-t)=1-c^2`. Under the one-core bias, the squared biased-Fourier masses fall into six explicit classes:

* empty set: `c^2(1-alpha)^2`;
* `{1}`: `V(1-alpha)^2`;
* subsets not containing `1` of odd cardinality: mass `alpha^2`, count `1/alpha`;
* nonempty subsets not containing `1` of even cardinality: mass `alpha^2 c^2`, count `1/alpha-1`;
* subsets containing `1` whose remainder has positive even cardinality: mass `alpha^2 V`, count `1/alpha-1`;
* subsets containing `1` whose remainder has odd cardinality: mass zero.

These masses sum to one. Their entropy simplifies exactly to

\[
\widetilde H_n(t)
=(1-\alpha)h_2(V)
-2(1-\alpha)^2\log_2(1-\alpha)
+(4\alpha-2\alpha^2)(n-2).
\tag{6.1}
\]

Substitute (5.1), (5.2), (6.1), and `h_2(V_{1/2})=h_2(1)=0` into the source all-gate identity (2.1). The `h_2(V)` terms cancel exactly, leaving (1.5).

This cancellation is the main usable reduction from the run: a seemingly high-dimensional prime gate family is governed by only `Gamma(t)`, `Gamma(t+alpha(1-2t)/2)`, and the center `C`.

## 7. Asymptotics and normalized margin

Assume `t` is fixed in `(0,1)` and `Gamma` is differentiable at `t`. Since `alpha=2^{2-n}`,

\[
\Gamma\!\left(t+\frac{\alpha c}{2}\right)
=\Gamma(t)+\frac{\alpha c}{2}\Gamma'(t)+O(\alpha^2),
\]

and

\[
2(1-\alpha)^2\log_2(1-\alpha)
=-\frac{2\alpha}{\ln2}+O(\alpha^2).
\]

Therefore

\[
\frac{D_{\Gamma,n}(t)}\alpha
=n(C-4)+8-C-\Gamma(t)-\frac{1-2t}{2}\Gamma'(t)-\frac2{\ln2}+o(1).
\tag{7.1}
\]

Meanwhile

\[
\frac{M_n(t)}\alpha=\frac14\bigl[n-2-(1-2t)^2+o(1)\bigr].
\tag{7.2}
\]

Taking the ratio proves (1.8). In particular, for the current source-reported center `C*=6.5584452830718245...`,

\[
-4(C_*-4)=-10.233781132287298\ldots.
\]

So **fixed interior bias cannot turn this two-point prime surgery into a new all-gate obstruction**. Any danger in this family must come from a boundary layer `t=t_n` where the finite difference of `Gamma` is comparable to the rare `alpha n` entropy term.

At the balanced point, direct exact evaluation of (1.6) is positive for the current center for every `n>=3`. Analytically, `n=3,4` are explicit finite inequalities; for `n>=5`, the elementary bound `-ln(1-alpha)<=alpha/(1-alpha)` together with `C_*>6.5` gives positivity immediately.

## 8. Computation/certificate scope

`CHECKER.py` beside this report independently verifies:

* all nontrivial block decompositions for `3<=n<=8` are rejected (459 block checks), using GF(2) ANF flattening rank when the outside has at least two variables and the three-row test for a singleton outside;
* 992 exact rational one-core biased spectral entries for `3<=n<=7` and `t in {1/3,2/5,1/2,5/9}` match the closed forms in Section 6;
* pivotality ratios match (5.1)-(5.2) exactly;
* the balanced current-center defect is positive numerically for `3<=n<=30` and the normalized demand trends toward the theorem value `-4(C_*-4)`.

The computation is regression evidence only; Sections 3-7 are the proof for all `n`.

## 9. What this settles and what it does not

**Settled for this assignment:** an explicit infinite, growing-arity, all-essential, composition-prime family obtained by a constant-size truth-table surgery; exact uniform and one-core biased spectral laws; exact all-gate defect reduction; and a proved asymptotic margin showing that fixed-interior-bias members are not stronger than the current finite prime witness.

**Not settled:** full FEI; universal safety of the current shaped candidate; arbitrary prime gates; or the boundary layer `t=t_n` for this family.

**Next unpaid implication:** use (1.5) with the exact current candidate potential, not only its center, and analyze the boundary regimes `t~alpha^beta`, especially `t=Theta(alpha)` and `t=Theta(alpha n)`. A negative value would be a new genuine growing-arity prime falsifier of that candidate. A uniform nonnegative bound would eliminate an infinite near-dictator prime class and quantify the candidate’s boundary modulus requirement.

This is the recommended handoff to fleet03/B02 and the designated partner group.
