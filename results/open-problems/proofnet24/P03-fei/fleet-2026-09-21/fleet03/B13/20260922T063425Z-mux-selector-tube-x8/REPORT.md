# fleet03/B13 — factor-eight expansion of the live unequal-MUX selector tube

**Run:** `20260922T063425Z-b13-fei-a11`  
**Classification:** `ESSENTIAL_STEP_APPLIED / MUX_SAFE_REGION_EXPANDED / FULL_FEI_OPEN`  
**Execution:** `WITHOUT_VERIFIED_BRAIN` (`full_brain_connected=false`)  
**Full uniform-cube FEI:** **OPEN / NOT PROVED**.  
**Publication priority:** unverified; no novelty claim is made.

## 0. Later-owner precedence and exact candidate

The fresh owner control is revision `2026-09-22.2`. Its later natural-language FEI message converges the fleet on the all-gate inequality, so it supersedes the older fleet03/B13 derivative-row-only assignment where the two conflict. The older mixed-derivative integrability results remain valid inputs; this run does not reopen them.

The live source candidate is

\[
C^\dagger=6.521851214,\qquad C_0=6.4548,
\qquad a^\dagger=4(C^\dagger-C_0)=0.268204856,
\]
\[
\Gamma^\dagger(z)=\Gamma_0(z)+a^\dagger z(1-z),
\]

where `Gamma_0` is the committed h96 read-once potential, source blob
`1e2a1a5c293fa7b6ec9885b7a410910d6589be80`.

For a Boolean gate `G` at product bias `p`, write

\[
D_\Gamma(G;p)=
\sum_i {\operatorname{It}_i(G;p)\over V_{p_i}}
[\Gamma(p_i)+h_2(V_{p_i})]
-\Gamma(p_{\rm out})-\widetilde H_G(p),
\qquad V_u=4u(1-u).
\]

The universal target is `D_{Gamma^dagger}(G;p)>=0` for every Boolean gate and every interior product bias. That target is not proved here.

This run attacks the newest explicit missing MUX implication: enlarge the rigorously safe region for the unequal-data one-bit multiplexer while retaining the exact six-atom spectral entropy rather than dropping the selector information credit.

## 1. Named other-account results consumed and actually applied

### 1.1 fleet04/B18 off-center equal-data tube

The principal consumed result is

`fleet04/B18/20260922T061350Z-mux-equal-data-offcenter-tube/REPORT.md`.

It proves, for

\[
M(A;D_0,D_1)=D_A,
\quad \Pr(A=1)=t,
\quad \Pr(D_j=1)=q_j,
\]

and

\[
m:=\min\{q_0+q_1,2-q_0-q_1\},
\qquad v:=q_1-q_0,
\qquad s:=t-\frac12,
\]

the source-valid theorem

\[
|v|\le {m\over224},\qquad |s|\le {m\over8192}
\quad\Longrightarrow\quad
D_{\Gamma^\dagger}(M)>{m\over10}.
\tag{1.1}
\]

More importantly for the present extension, its proof establishes the stronger balanced-selector reserve

\[
\boxed{
|v|\le {m\over224}
\quad\Longrightarrow\quad
D_{\Gamma^\dagger}(M;1/2,q_0,q_1)>0.13m.
}
\tag{1.2}
\]

It also derives the exact perturbation bookkeeping from the six MUX spectral masses. I apply (1.2) and rework the perturbation constants instead of rerunning its proof.

### 1.2 fleet01/B18 balanced MUX collar

The source of the balanced reserve used by fleet04/B18 is

`fleet01/B18/20260922T055608Z-balanced-mux-collar-sharpen/REPORT.md`.

It proves the wider balanced-address collar

\[
|q_1-q_0|\le {1\over112}
\min\{q_0+q_1,2-q_0-q_1\}
\Longrightarrow D_{\Gamma^\dagger}(M;1/2,q_0,q_1)>0,
\]

and supplies the source derivative bounds from which (1.2) is obtained on the narrower `1/224` collar.

### 1.3 exact arbitrary-bias MUX formula

The underlying exact formula is fleet04/B18

`20260922T045533Z-mux-joint-credit-collapse/REPORT.md`, immutable compatible commit `7130b553e2efae3dde1002d0697da069f8c72d65`.

Its six squared biased-Walsh masses are

\[
\begin{aligned}
w_\varnothing&=(1-2r)^2,\\
w_A&=V_t(q_1-q_0)^2,\\
w_0&=(1-t)^2V_0,\\
w_1&=t^2V_1,\\
w_{A0}&={V_tV_0\over4},\\
w_{A1}&={V_tV_1\over4},
\end{aligned}
\tag{1.3}
\]

where `r=(1-t)q_0+tq_1` and `V_j=4q_j(1-q_j)`. It gives the exact defect

\[
D_{\Gamma^\dagger}(M)
=dB(t)+(1-t)B(q_0)+tB(q_1)-\Gamma^\dagger(r)-H(w),
\tag{1.4}
\]

with

\[
d=q_0+q_1-2q_0q_1,
\qquad B(u)=\Gamma^\dagger(u)+h_2(V_u).
\]

No non-Boolean probability relaxation is used below.

## 2. Exact universal statement attempted

### Theorem 2.1 — factor-eight selector expansion

For every interior one-bit MUX, if

\[
\boxed{
|q_1-q_0|\le {m\over224},
\qquad
\left|t-\frac12\right|\le {m\over1024},
}
\tag{2.1}
\]

where

\[
m=\min\{q_0+q_1,2-q_0-q_1\},
\]

then

\[
\boxed{
D_{\Gamma^\dagger}(M;t,q_0,q_1)>{7m\over250}>0.
}
\tag{2.2}
\]

Thus, on the same `1/224` unequal-data collar, the certified selector displacement expands from `m/8192` in the consumed fleet04/B18 theorem to `m/1024`, a factor of eight.

Boundary data biases follow by continuity; the all-gate formulation itself only requires interior biases.

## 3. Reduction and source derivative bounds

Complementing both data bits and the output leaves the squared spectrum and the defect invariant. Hence assume

\[
q_0+q_1=m\le1.
\tag{3.1}
\]

Then

\[
q_0={m-v\over2},\qquad q_1={m+v\over2}.
\]

Under `|v|<=m/224`, both data arguments have reflected small-side representative at least `m/4`. The output bias is

\[
r={m\over2}+sv,
\tag{3.2}
\]

and under `|s|<=m/1024` its reflected small-side representative is also greater than `m/4`.

Put

\[
L=\log_2(1/m).
\]

The source bounds already established in the consumed fleet04/B18 proof give, on the data/output range,

\[
|B'(z)|<9L+83,
\qquad
|(\Gamma^\dagger)'(z)|<5L+67.
\tag{3.3}
\]

At the selector itself, `|s|<=1/1024`. The source near-center estimate gives

\[
|(\Gamma^\dagger)'(t)|<66.
\tag{3.4}
\]

For completeness, the entropy part of `B` also stays below one in derivative magnitude here. With `z=2|s|<=1/512`,

\[
\left|{d\over dt}h_2(V_t)\right|
=4z\left|\log_2{z^2\over1-z^2}\right|
<4z\left(1+2\log_2{1\over z}\right)
\le {76\over512}<1.
\tag{3.5}
\]

Therefore

\[
\boxed{|B'(t)|<67}
\tag{3.6}
\]

through the whole new selector interval.

## 4. Smooth part of the selector perturbation

Compare (1.4) at `t=1/2+s` with `t=1/2`. Since `d<=q_0+q_1=m`, the address-price change is at most

\[
67m|s|.
\]

The data-mixture change is bounded by

\[
|s|\,|B(q_1)-B(q_0)|
<|s||v|(9L+83),
\]

and (3.2)-(3.3) give output-potential change

\[
|\Gamma^\dagger(r)-\Gamma^\dagger(m/2)|
<|s||v|(5L+67).
\]

Hence the total nonentropy debit is

\[
E_{\rm smooth}
<67m|s|+|s||v|(14L+150).
\tag{4.1}
\]

Using

\[
|s|\le {m\over1024},
\qquad |v|\le {m\over224},
\qquad mL\le1,
\qquad m\le1,
\]

we obtain

\[
\boxed{
{E_{\rm smooth}\over m}
< {67\over1024}+{164\over1024\cdot224}
={3793\over57344}
<0.066145.
}
\tag{4.2}
\]

The elementary bound `m log_2(1/m)<=1` is deliberately loose.

## 5. Exact six-atom entropy perturbation

From (1.3), relative to `t=1/2`, the four masses involving a data singleton have total displacement at most

\[
4m(|s|+2s^2).
\tag{5.1}
\]

The zero mode changes by at most

\[
4|s||v|\le {m|s|\over56},
\tag{5.2}
\]

and the pure-address mass changes by exactly at most

\[
4s^2v^2.
\tag{5.3}
\]

After division by `m|s|`, the sum of the coefficients in (5.1)-(5.3) is bounded by

\[
4+{8\over1024}+{1\over56}+{4\over1024\cdot224^2}
<5.
\tag{5.4}
\]

Therefore

\[
\|w(t)-w(1/2)\|_1<5m|s|,
\]

so the total variation distance satisfies

\[
\tau<{5\over2}m|s|\le {5m^2\over2048}.
\tag{5.5}
\]

Fannes--Audenaert on the six-point alphabet gives

\[
|H(w(t))-H(w(1/2))|
\le h_2(\tau)+\tau\log_2 5
\le \tau\log_2{5e\over\tau}.
\tag{5.6}
\]

The right side is increasing throughout the range (5.5), so substitute the upper endpoint. Since

\[
\log_2 e<\frac32,
\qquad m\log_2(1/m)\le1,
\]

we get

\[
\begin{aligned}
{E_{\rm ent}\over m}
&< {5m\over2048}
\left(\log_2(2048e)+2L\right)\\
&< {5\over2048}\left({25\over2}+2\right)\\
&=\boxed{{145\over4096}}
<0.035401.
\end{aligned}
\tag{5.7}
\]

Here `log_2(2048e)=11+log_2 e<25/2`.

## 6. Finish the theorem

Combining (4.2) and (5.7), the total defect decrease caused by moving the selector from `1/2` to `1/2+s` is less than

\[
\left({3793\over57344}+{145\over4096}\right)m
={5823\over57344}m
<0.102m.
\tag{6.1}
\]

The consumed balanced-selector theorem (1.2) supplies more than `0.13m`. Therefore

\[
\begin{aligned}
D_{\Gamma^\dagger}(M;t,q_0,q_1)
&>\left({13\over100}-{5823\over57344}\right)m\\
&={40793\over1433600}m\\
&> {7\over250}m.
\end{aligned}
\tag{6.2}
\]

This proves Theorem 2.1. QED.

The adjacent exact-rational checker verifies every numerical comparison in (3.5), (5.4), and (6.1)-(6.2). It is a checker of the new constant bookkeeping; the source analytic inequalities are proved above and inherited from the named reports.

## 7. Counterexample search and route boundary

The theorem itself rules out a source-valid negative MUX point in the region (2.1). To stress the enlarged boundary rather than merely repeat the predecessor constants, the exact-rational checker evaluates the worst allowed coefficient envelope at `|s|=m/1024`, `|v|=m/224`, and `m=1`: the total allowed selector debit is below

\[
0.101545062m,
\]

leaving a certified reserve above

\[
0.028454938m.
\]

Thus the new factor-eight expansion is not a floating-point near miss.

A crude attempt to close the entire MUX cube using only the global two-sided envelope

\[
z[4.9096\log_2(1/z)+2.229]
\lesssim \Gamma_0(z)
\lesssim
z[4.9096\log_2(1/z)+8.629]
\]

fails decisively: the independent upper/lower envelope destroys the cancellations in the exact scalar formula and yields large negative lower bounds even at known-safe central points. That route is recorded as dead; the compact remainder must retain local source-segment cancellation or stronger exact information credits.

## 8. Old/new missing implication and next recipient

**Exact candidate version:** `Gamma^dagger = Gamma_0 + 0.268204856 p(1-p)`, `Gamma^dagger(1/2)=6.521851214`, with `Gamma_0` the committed h96 candidate.

**Prior first missing implication:** prove nonnegative live-candidate defect on the compact unequal-MUX remainder outside the previously certified common-data, complementary-data and zero-credit neighborhoods, or exhibit a genuine negative point.

**New proved inference:** on the `|q_1-q_0|<=m/224` collar, the selector-safe radius is enlarged by a factor of eight, from `m/8192` to `m/1024`, with the explicit reserve `D>7m/250`.

**Replacement obligation:** the remaining MUX compact region is now further separated from the equal-data surface. A useful next step is an interval/source-segment proof on the residual compact set, using the exact selector credit and the simultaneous data-pivot cross-deficit constraints rather than the failed independent global potential envelope.

**Consumed peer artifact:** fleet04/B18 `20260922T061350Z-mux-equal-data-offcenter-tube/REPORT.md`, together with fleet01/B18 `20260922T055608Z-balanced-mux-collar-sharpen/REPORT.md` and the exact fleet04/B18 MUX collapse.

**Next recipient:** `fleet04/B18` first, then `fleet01/B18` and `fleet04/B14`, because their current work is precisely the MUX compact remainder and its complementary/zero-credit tubes.

**Implication to full FEI:** this shrinks one explicit prime-gate obstruction region for the fixed candidate but does not prove the full MUX theorem, the arbitrary composition-prime gate inequality, or FEI.

\[
\boxed{\text{Full uniform-cube FEI remains OPEN / NOT PROVED.}}
\]
