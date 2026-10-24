# B18 addendum: child slack + strong-concavity rebate

**Status:** proved reduction/synthesis only; **full FEI remains OPEN**.  
**Input:** B18 marginal-profile child-slack criterion plus the later compatible B14 theorem `JS_i <= j(M_i)-(c_*/3)V_i`, where `c_*=2/ln 2`. No novelty or priority claim is made.

Let `a_i=Inf_i(f)`, `B_i=H(X_i|X_-i)`, and use the folded Fourier-fibre quantities

\[
M_i=\sum_T w_T s_T,\qquad
V_i=\sum_Tw_T(s_T-M_i)^2,
\]

with

\[
j(s)=1-h_2\!\left(\frac12+\sqrt{s(1-s)}\right),
\qquad c_*=\frac2{\ln2}.
\]

For a candidate constant `C`, retain B18's explicit child slack

\[
P_C(g)=\left(CI(g)-\sum_k h_2(\operatorname{Inf}_k(g))\right)_+.
\]

## 1. Slack-rebated erasure selector — PROVED SUFFICIENT REDUCTION

B18 proved that lower-dimensional FEI(C) closes at coordinate `i` whenever

\[
\Delta_iH\le Ca_i+\frac{P_C(f_+)+P_C(f_-)}2.
\tag{1}
\]

B14 proved

\[
\Delta_iH=B_i+JS_i
\le B_i+j(M_i)-\frac{c_*}{3}V_i.
\tag{2}
\]

Therefore it is sufficient to find a relevant coordinate satisfying

\[
\boxed{
B_i+j(M_i)-\frac{c_*}{3}V_i
\le
Ca_i+\frac{P_C(f_+)+P_C(f_-)}2.
}
\tag{3}
\]

This strictly combines two kinds of credit which earlier one-statistic selectors discarded: a **same-node fibre rebate** `c_*V_i/3` and **lower-dimensional marginal slack** in the children.

Let `tau(C)` be the root of `Psi(tau)/tau=C` on `(0,1/2]`, where the already-proved concave cap gives `Delta_iH<=Psi(min(a_i,1-a_i))`. If some `a_i>=tau(C)` (or `a_i>1/2`), direct local payment is available. Hence full FEI(C) follows if (3) can be proved existentially on states with every relevant influence below `tau(C)`.

At the Hod calibration `C=6.4547837`, the current value is

\[
\tau(C)=0.18055402378719737\ldots.
\]

Thus any minimal counterexample at that calibration must have **all** relevant influences below `0.180555` and must violate (3) at **every** relevant coordinate.

## 2. Sharpened two-channel total-correlation identity

B18's exact identity is

\[
\Delta_iTC
=I(X_i;X_{-i})+
\sum_{j\ne i} I(x_i;Y_j)-JS_i,
\tag{4}
\]

where `Y_j` is the indicator that the `j`-edge is pivotal. Combining (4) with B14's strong-concavity estimate gives

\[
\boxed{
\Delta_iTC
\ge
I(X_i;X_{-i})+
\sum_{j\ne i} I(x_i;Y_j)
-j(M_i)+\frac{c_*}{3}V_i.
}
\tag{5}
\]

The weaker marginal-only form is

\[
\Delta_iTC
\ge I(X_i;X_{-i})+
\sum_{j\ne i}I(x_i;Y_j)
-c_*\left(j_i-\frac{j_i^2}{3}\right),
\qquad j_i=\min(a_i,1-a_i).
\tag{6}
\]

Equation (5) identifies three compatible payments for an influence-greedy restriction step: spectral dependence, physical pivotal dependence, and fibre variance. Child `P_C` slack is a fourth payment available after restriction.

## 3. Precise next universal target

A source-exact closure target for APPROACH 11/12 is now:

> For every low-influence Boolean state (`0<a_i<tau(C)` for every relevant `i`), find a coordinate `i` satisfying (3).

Equivalently, a hypothetical minimal counterexample must obey simultaneously for every relevant `i`

\[
B_i+j(M_i)-\frac{c_*}{3}V_i
>
Ca_i+\frac{P_C(f_+)+P_C(f_-)}2.
\tag{7}
\]

The previously found bent-selector obstruction only defeats the version without child slack; its deliberately bad selector has child `P_C` of order `m` versus selector debit of order `m2^{-m}`. Width-two tribes defeat an older fixed tangent-erasure threshold, but B14's quadratic/fibre rebate already repairs that family. Therefore (3) survives both mandatory scope tests for different structural reasons.

What remains missing is a Booleanity lemma forcing at least one of the four payments in (5)/(3) to be large on a state satisfying (7). Product-spectrum rigidity controls the zero-dependence endpoint, while pivotal-subcube rigidity controls an exact physical endpoint; a quantitative stability bridge between those endpoints and (7) would close this route. No such universal stability bound is proved here.
