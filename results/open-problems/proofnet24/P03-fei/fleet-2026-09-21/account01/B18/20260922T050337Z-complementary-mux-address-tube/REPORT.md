# B18 FEI — quantitative complementary-MUX reserve opens an address-bias tube

**Status:** `ESSENTIAL_STEP_APPLIED / COMPLEMENTARY_MUX_ADDRESS_TUBE / FULL_FEI_OPEN`.

Full unrestricted uniform-cube Fourier entropy-influence remains **OPEN / NOT PROVED**.  This report proves the live fixed candidate on a two-parameter non-unate MUX family.  It removes the balanced-address restriction from the just-completed complementary-data theorem in a source-exact neighborhood; it does not prove the full unequal-data MUX and does not settle FEI.

**Execution:** `WITHOUT_VERIFIED_BRAIN`.  Fresh authenticated repository controls and exact peer/source files were read directly; no authenticated mathematical-brain receiver/context was used.

## 1. Live candidate and compact conditional full chain

Use the current account01/B18 candidate

\[
C^\dagger=6.521851214,
\qquad C_0=6.4548,
\qquad a^\dagger=4(C^\dagger-C_0)=0.268204856,
\]
\[
\Gamma^\dagger(u)=\Gamma_0(u)+a^\dagger u(1-u).
\]

For every Boolean gate `G` at product bias `p`, write

\[
D_\Gamma(G;p)=
\sum_i {\operatorname{It}_i(G;p)\over V_{p_i}}
\bigl(\Gamma(p_i)+h_2(V_{p_i})\bigr)
-\Gamma(p_{\rm out})-\widetilde H_G(p),
\qquad V_u=4u(1-u).
\]

The source gate-reformulation theorem says: if `D_{Gamma^dagger}(G;p)>=0` for every Boolean gate, every arity, every interior product bias, then full FEI follows with constant `C^dagger`.  Composition reduces the unpaid work to composition-prime gates.  Common-data MUX/addressing is already closed in

`account01/B18/20260922T0325Z-addressing-star-cdagger/REPORT.md`
(blob `6deb28dc6f2e8f36da01fdc7ac24f600f7553a5c`).

The first essential missing inference was therefore the genuine unequal-data MUX.

## 2. Named peer result consumed and applied

This run substantively uses the completed account02/B12 theorem

`account02/B12/20260922T045519Z-complementary-mux-fourstep/REPORT.md`
(blob `5246a98a875da29c7e902237e269a0f7acd899e9`) and its exact checker
(blob `885892ea837683d4db6918805ff4685237abbba6`).

For the one-bit MUX

\[
M(a,x_0,x_1)=(1-a)x_0+a x_1
\]

with balanced address and complementary data,

\[
t={1\over2},\qquad q_0=q,\qquad q_1=1-q,\qquad 0<q\le {1\over2},
\]

that theorem proves

\[
D_{\Gamma^\dagger}(M;1/2,q,1-q)=F(q)>0
\]

for the full continuum.  More precisely its four-generation AND bootstrap gives, on `0<q<=2^-11`,

\[
F(q)>2.913692716\,q,
\]

and on `[2^-11,1/2]` an exact-rational 1280-cell certificate.  Its exact minimum is attained on the first cell `[1/2048,129/262144]`.

The first new step here is a quantitative extraction from that exact certificate.  Re-evaluating only its already-defined rational lower bounds (not the read-once certificate) gives

\[
\min_{\text{1280 certified cells}}\mathcal L_{\rm cell}>{1\over64}.
\]

Since `q<=1/2`, the compact branch therefore has `F(q)>q/32`; the tiny branch is much stronger.  Thus the peer theorem yields the global reserve

\[
\boxed{F(q)>{q\over32}\qquad(0<q\le1/2).}
\tag{2.1}
\]

The exact-rational post-processing is recorded in `check_address_tube.py`; no finite sample is promoted to a theorem.

## 3. Exact MUX spectrum off the balanced-address midline

Keep complementary data but allow

\[
t={1\over2}+s,\qquad q_0=q,\qquad q_1=1-q,\qquad 0<q\le {1\over2}.
\]

Put

\[
A=1-2q,\qquad V=V_q,\qquad r={1\over2}+sA,
\qquad d=q+(1-q)-2q(1-q)=1-{V\over2}.
\]

The six squared biased Fourier masses are exactly

\[
\begin{aligned}
w_\varnothing&=4s^2A^2,\\
w_a&=(1-4s^2)A^2,\\
w_0&=(1/2-s)^2V,\\
w_1&=(1/2+s)^2V,\\
w_{a0}&=(1/4-s^2)V,\\
w_{a1}&=(1/4-s^2)V.
\end{aligned}
\tag{3.1}
\]

At `s=0` this is

\[
0,\ 1-V,\ V/4,\ V/4,\ V/4,\ V/4.
\]

The biased influence prices are

\[
{\operatorname{It}_a\over V_t}=d,
\qquad
{\operatorname{It}_0\over V_q}=1-t,
\qquad
{\operatorname{It}_1\over V_q}=t.
\]

Since `Gamma^dagger(q)=Gamma^dagger(1-q)`, the two data-price terms sum to the same quantity for every `t`.  Consequently the only changes from the balanced-address slack are the address potential, the output potential, and the six-point spectral entropy.

## 4. A source-valid `60`-Lipschitz bound for the potential near the center

The committed h96 source diagnostics give the transformed slope bound `|Ghat'|<=30.080`; the relation between `Ghat` and the source `G` gives the deliberately weaker

\[
|G'(x)|<31.
\tag{4.1}
\]

Also `G(1)=2C_0=12.9096`.  If

\[
|s|\le {q^2\over8192},
\]

then `q<=1/2` gives `|s|<=1/32768`.  Both `t` and `r` therefore lie within `1/32768` of `1/2`.  For the smaller representative `u` of either point,

\[
x=\log_2(1/u)<1.001.
\]

Indeed `2u>=1-1/16384`, `-\ln(1-y)<=y/(1-y)`, and `\ln2>2/3`.
Hence (4.1) gives

\[
|G(x)|<12.9096+{31\over1000}=12.9406.
\]

For `Gamma_0(u)=uG(\log_2(1/u))`,

\[
|\Gamma_0'(u)|
\le |G(x)|+{|G'(x)|\over\ln2}
<12.9406+31\,{3\over2}<59.441.
\]

Adding the derivative of `a^dagger u(1-u)` still leaves

\[
\boxed{|(\Gamma^\dagger)'(u)|<60}
\tag{4.2}
\]

throughout this center window.  Therefore the address-potential and output-potential changes cost at most

\[
60|s|+60|s|=120|s|.
\tag{4.3}
\]

The positive address entropy `d h_2(V_t)` is discarded rather than charged.

## 5. Six-point entropy continuity costs only `9q/4096`

Let `P_s` be the six-mass vector (3.1), and `P_0` the balanced-address vector.  Directly from (3.1),

\[
\|P_s-P_0\|_1
\le 2|s|+12s^2.
\]

Thus its total variation distance `delta` obeys

\[
\delta\le |s|+6s^2\le2|s|
\le {q^2\over4096}.
\tag{5.1}
\]

Fannes--Audenaert on an alphabet of size six gives

\[
|H(P_s)-H(P_0)|
\le h_2(\delta)+\delta\log_2 5
\le \delta\log_2{5e\over\delta}.
\]

Using `e<3` and (5.1),

\[
|H(P_s)-H(P_0)|
\le {q^2\over4096}
\log_2{61440\over q^2}.
\]

The function `q log_2(61440/q^2)` is increasing on `(0,1/2]`: its derivative is
`log_2(61440/q^2)-2/ln2>17-3>0`.  Hence

\[
{ |H(P_s)-H(P_0)| \over q}
< {1\over8192}\log_2(245760)
< {18\over8192}
={9\over4096}.
\tag{5.2}
\]

## 6. The address-tube theorem

Combining the peer reserve (2.1), the potential cost (4.3), and (5.2), and using

\[
{120|s|\over q}
\le {120q\over8192}
\le {60\over8192}
={15\over2048},
\]

gives

\[
\begin{aligned}
D_{\Gamma^\dagger}(M;t,q,1-q)
&>{q\over32}
- {15q\over2048}
- {9q\over4096}\\
&={89\over4096}\,q.
\end{aligned}
\]

Therefore:

### Theorem 6.1 — complementary-data MUX address tube

For every

\[
0<q\le {1\over2},
\qquad
\left|t-{1\over2}\right|\le {q^2\over8192},
\]

the live candidate satisfies

\[
\boxed{
D_{\Gamma^\dagger}(M;t,q,1-q)
>{89\over4096}\,q>0.
}
\tag{6.1}
\]

The `q>1/2` form follows by exchanging the two data labels.  Boundary values follow by continuity.

This is an infinite two-parameter genuinely non-unate prime-gate family.  It strictly extends account02/B12's balanced-address midline theorem by releasing the condition `t=1/2` on an explicit source-valid neighborhood.

The owner requests the comparable gate margin rather than only raw `D`.  For complementary data,

\[
W={I\over4}-r(1-r)={V_tV_q\over8}\le {q\over2}.
\]

Since `D_{Gamma^dagger}=D_{Gamma_0}+a^dagger W`, (6.1) implies, throughout this tube,

\[
\boxed{
c_M\le a^\dagger-{89\over2048}
=0.22474782475,
}
\tag{6.2}
\]

well below the current lift `a^dagger=0.268204856`.

## 7. Exact old/new missing implications

**Old missing implication.**  After common-data addressing and before the peer run, a genuine unequal-data MUX was not covered.  Account02/B12 then closed the exact balanced-address complementary-data line `t=1/2, (q,1-q)`.

**New proved implication.**  The same complementary-data family is safe throughout the explicit tube

\[
|t-1/2|\le q^2/8192,
\]

with quantitative slack (6.1) and margin bound (6.2).

**Still missing.**  One must remove the complementary-data relation `q_1=1-q_0` and then the small address-tube restriction, or find a source-valid violating bias.  No statement here controls all unequal-data MUX biases, still less all composition-prime gates.

**Classification:** `ESSENTIAL_STEP_APPLIED`.

Full FEI remains **OPEN / NOT PROVED**.

## 8. Provenance and privacy

The supporting checker is only an exact-rational post-processing of the already-completed account02/B12 scalar certificate plus rational verification of the new tube constants; it does not rerun a read-once certificate.  Changed files contain only mathematical derivation and sanitized numeric constants.  No credentials, scheduler identifiers, machine paths, email/Drive data, benchmark gold, public posting, permission changes, remote workflows, or paid compute are used.
