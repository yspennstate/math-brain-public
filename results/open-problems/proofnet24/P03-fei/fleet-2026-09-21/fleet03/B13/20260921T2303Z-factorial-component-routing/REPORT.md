# B13 FEI joint interface B — factorial-paid component routing and a Boolean obstruction to raw trigger payment

**Account/slot:** fleet03/B13  
**Joint interface:** B — compatibility and integrability of several derivative rows  
**Execution:** **WITHOUT_VERIFIED_BRAIN**  
**Full FEI status:** **OPEN / NOT PROVED**  
**Claim level:** universal conditional theorem for every Boolean function in the robust derivative-row sector, plus a genuine Boolean counterfamily refuting a stronger raw-trigger payment. No novelty or publication-priority claim.

## 0. Exact statement attempted

Let `S` be the spectral sample of a Boolean function, `K=|S|`, and
\[
\mathfrak F:=\mathbb E\log_2(K!).
\]
Consider any family `R` of derivative Palm rows that are `epsilon`-robust in the sense of fleet04/B12, with `epsilon<1/4`. Contract reciprocal robust rows into components `C`. The completed trigger-locking theorem gives one common trigger signature `T_C` for every reciprocal component, with
\[
F_i=T_C\setminus\{i\}\qquad(i\in C).
\]
Put
\[
W_C:=\sum_{i\in C}j_i,\qquad J_R:=\sum_C W_C.
\]

The exact universal statement attempted in this run is:

> **Factorial component-routing statement.** Sample a component `C_*` with probability `W_C/J_R`. Conditional on `C_*=C`, choose an arbitrary activation row `A_C in C` and an arbitrary trigger-address coordinate `U_C in T_C`, with any joint conditional law. Then the weighted Shannon cost of the activation/address pair is bounded by the already-existing factorial nonreuse bank:
> \[
> J_R H(A_{C_*},U_{C_*}\mid C_*)
> \le \frac{2}{1/4-\epsilon}\,\mathfrak F.
> \]
> At the live threshold `epsilon<=1/16`, the constant is `32/3`. For the address alone the constant is `16/3`.

This is proved below. It is not full FEI: it pays **which row / which trigger** inside a robust reciprocal component hierarchy under the natural influence-weighted selector normalization. It does not yet prove that the actual physical elimination strategy has this selector law, nor does it pay the event/reveal entropy of activating the subcube itself.

## 1. Named other-account result consumed

The substantive peer input is

`proofnet24/P03-fei/fleet-2026-09-21/fleet04/B12/20260921T212331Z-factorial-trigger-address/REPORT.md`

(report blob recorded by the newest fleet04/B18 integration as `d21168c13eb0ba0a52a38691206b0d726727eb79`). It proves the exact Palm partition
\[
\mathfrak F
=\sum_i j_i\,\mathbb E_{\nu_i}\frac{\log_2((1+|B|)!)}{1+|B|},
\]
and, for every robust row family,
\[
\mathfrak F\ge
\sum_i\left(\frac14-\epsilon_i\right)j_i\log_2(|F_i|+1).
\tag{1.1}
\]
At `epsilon_i<=1/16`,
\[
\sum_i j_i\log_2(|F_i|+1)\le\frac{16}{3}\mathfrak F.
\tag{1.2}
\]
The same report uses the earlier fleet04/B12 trigger-locking theorem: reciprocal robust components have an exact common signature `T_C` and the robust quotient is scale-acyclic. Thus `|F_i|+1=|T_C|` for every `i in C`.

**applied_to_claim:** turn the peer's rowwise factorial rebate into an exact component-level **activation plus routing-address code**, rather than another raw pair/depth charge.

## 2. PROVED: factorial-paid component-routing theorem

### Theorem 2.1

Under the setup above, assume all rows in the component family obey `epsilon_i<=epsilon<1/4`. Let
\[
\Pr(C_*=C)=\frac{W_C}{J_R}.
\]
For each component `C`, let `(A_C,U_C)` have an arbitrary joint law supported on
\[
C\times T_C.
\]
Then
\[
\boxed{
J_R H(U_{C_*}\mid C_*)
\le \frac{1}{1/4-\epsilon}\mathfrak F,
}
\tag{2.1}
\]
and
\[
\boxed{
J_R H(A_{C_*},U_{C_*}\mid C_*)
\le \frac{2}{1/4-\epsilon}\mathfrak F.
}
\tag{2.2}
\]
In particular, at `epsilon<=1/16`,
\[
\boxed{J_R H(U_{C_*}\mid C_*)\le\frac{16}{3}\mathfrak F,}
\tag{2.3}
\]
\[
\boxed{J_R H(A_{C_*},U_{C_*}\mid C_*)\le\frac{32}{3}\mathfrak F.}
\tag{2.4}
\]
If `U_C` is restricted to robust trigger coordinates and `D_C` denotes the reciprocal component containing `U_C`, then by data processing the same bounds hold with `D_C` in place of `U_C`.

### Proof

From the peer theorem (1.1) and trigger locking,
\[
\mathfrak F
\ge(1/4-\epsilon)\sum_C W_C\log_2|T_C|.
\tag{2.5}
\]
For every component,
\[
H(U_C)\le\log_2|T_C|.
\]
Therefore
\[
\begin{aligned}
J_R H(U_{C_*}\mid C_*)
&=\sum_C W_C H(U_C)\\
&\le\sum_C W_C\log_2|T_C|\\
&\le\frac{1}{1/4-\epsilon}\mathfrak F,
\end{aligned}
\]
which proves (2.1).

Also `C subseteq T_C`: for every `i in C`, the common-signature identity is `T_C={i} union F_i`. Hence
\[
|C|\le|T_C|.
\]
For arbitrary dependence between `A_C` and `U_C`,
\[
H(A_C,U_C)
\le\log_2(|C|\,|T_C|)
\le2\log_2|T_C|.
\]
Multiply by `W_C`, sum, and use (2.5), proving (2.2). The `epsilon=1/16` constants are immediate. Finally, a robust target component is a deterministic function of its addressed robust coordinate, so Shannon entropy cannot increase under that map. QED.

### Interpretation

This is the component-level nonreuse implication sought by the interface-B handoffs, but at the correct logarithmic granularity. The exact factorial partition already splits its rebate among occupied spectral rows; Theorem 2.1 says that, after reciprocal contraction, one can spend those row shares to identify one component-local activation and one trigger target without an ambient `log n`, a raw `sum d_i`, or a pairwise unit charge.

The theorem is deliberately selector-normalized by `W_C/J_R`. The unresolved question is whether the **actual realizable elimination process** can be arranged to have a component occupation law dominated by this influence-weighted law, or can otherwise telescope the same code without reusing the factorial bank.

## 3. REFUTED stronger route: the factorial bank cannot pay raw trigger size

A tempting strengthening would replace the logarithmic address by the raw number of triggers:
\[
\sum_C W_C|T_C|\stackrel{?}{\le}C\,\mathfrak F
\tag{3.1}
\]
with a universal constant `C`. This would have paid the physical trigger-load bank in one shot. It is **false even for a genuine Boolean family with exact Palm subcubes**.

For `n>=2`, let
\[
f_n(x)=1-2\mathbf 1_{\{0^n\}}(x).
\]
Its Fourier coefficients are
\[
\widehat f_n(\varnothing)=1-2^{1-n},
\qquad
\widehat f_n(A)=-2^{1-n}\quad(A\ne\varnothing).
\tag{3.2}
\]
Hence every coordinate has
\[
j_i=\Pr(i\in S)=2^{1-n}.
\tag{3.3}
\]
Conditioning on `i in S`, all `2^(n-1)` sets containing `i` have equal spectral mass, so
\[
S\setminus\{i\}\mid(i\in S)
\]
is **exactly** uniform on all subsets of `[n]\setminus\{i\}`. Thus `epsilon=0`, every row is reciprocal with every other row, there is one component
\[
C=[n],\qquad T_C=[n],\qquad W_C=n2^{1-n}.
\tag{3.4}
\]
The proposed raw load is
\[
L_{\rm raw}=W_C|T_C|=n^2 2^{1-n}.
\tag{3.5}
\]
For `K~Bin(n,1/2)`, (3.2) gives
\[
\mathfrak F
=2^{2-n}\,\mathbb E\log_2(K!).
\tag{3.6}
\]
Since `log2(K!)<=K log2 n`,
\[
\mathfrak F
\le2^{2-n}\frac n2\log_2n
=n\log_2n\,2^{1-n}.
\tag{3.7}
\]
Therefore
\[
\boxed{
\frac{L_{\rm raw}}{\mathfrak F}
\ge\frac n{\log_2n}\longrightarrow\infty.
}
\tag{3.8}
\]
So no universal version of (3.1) exists, even inside the exact zero-error reciprocal-component class. The factorial bank pays **addresses** (`log |T_C|`), not raw trigger incidence (`|T_C|`). This is a genuine Boolean counterexample, not a relaxed point process.

## 4. Decisive numerical reproduction

`check_one_point_factorial.py` evaluates the exact family above through `n=4096` using the cancellation-free ratios
\[
\frac{L_{\rm raw}}{\mathfrak F}
=\frac{n^2}{2\,\mathbb E\log_2(K!)},
\qquad
\frac{W_C\log_2n}{\mathfrak F}
=\frac{n\log_2n}{2\,\mathbb E\log_2(K!)}.
\]
Selected values from `CHECK_OUTPUT.txt` are:

| n | raw load / factorial | log-address / factorial |
|---:|---:|---:|
| 16 | 8.179778748493 | 2.044944687123 |
| 64 | 17.352828605192 | 1.626827681737 |
| 256 | 45.732041940055 | 1.429126310627 |
| 1024 | 135.281743997620 | 1.321110781227 |
| 4096 | 428.415406530940 | 1.255123261321 |

The raw ratio diverges as the analytic lower bound (3.8) forces, while the logarithmic address ratio remains bounded, exactly matching the qualitative distinction in Theorem 2.1. The full output and standard-library reproducer are adjacent to this report.

## 5. Consequence for the joint proof chain

The newest fleet04/B13 proxy-gauge handoff localizes its remaining Shannon obligation to character/reveal labels; fleet01/B13 subsequently converts one such character-label entropy to a genuine mixed-boundary bank. The present result resolves a different part of interface B: **once a robust reciprocal component is selected, the component-local activation and one routing address do not need a raw-depth or ambient-dimension payment.** They are already factorial-paid under the natural `W_C` normalization.

This also explains why the fleet04/B18 support-depth trigger-load estimate and the fleet04/B12 factorial address estimate should not be conflated. The former controls a linear incidence quantity using support curvature `M`; the latter controls a logarithmic code quantity. The one-point-defect family proves that a direct replacement of the former by the latter is impossible.

### Status distinctions

- **PROVED:** Theorem 2.1, universally for every Boolean function and every robust row family satisfying its stated hypotheses.
- **REFUTED:** universal raw-trigger-size payment (3.1), by the exact Boolean one-point-defect family.
- **OPEN:** convert the actual realizable component-elimination occupation measure to the `W_C`-weighted code without reuse, and combine that with the physical reveal/event entropy and exceptional-row handling.
- **OPEN:** full FEI.

## 6. Next attack and handoff

**remaining_implication:** construct a physical nonreusing selector/stopping rule for the robust quotient DAG whose component occupation masses `a_C` obey an influence-relative domination strong enough to imply
\[
\sum_C a_C\log_2|T_C|
\lesssim
\sum_C W_C\log_2|T_C|,
\tag{6.1}
\]
or else produce a Boolean counterexample to such domination. The raw-size version is now ruled out and must not be retried.

A particularly concrete next experiment is to choose a robust component externally with probability proportional to `W_C`, reveal only its locked signature, and compute whether the expected centered-influence drift / entropy drift is sufficient for the current adaptive recursion. If it is not, the obstruction should be stated as a mismatch between the physical progress law and the factorial-paid selector law, not as a missing coding inequality.

**next_recipient:** primary `fleet04/B13` (proxy-gauge/source-frontier elimination); secondary `fleet01/B13` (character-label boundary payment) and `fleet04/B12` (factorial trigger code).

**consumed_peer_artifact:** `fleet04/B12/20260921T212331Z-factorial-trigger-address/REPORT.md`.

**applied_to_claim:** component-local activation + one trigger/target address is factorial-paid under the natural influence-weighted component selector, with constants `16/3` and `32/3` at the live robustness threshold.

**mechanism_change:** information/coding of reciprocal-component routing, rather than another support-stability, depth-contraction, or proxy-geometry argument.

Full FEI remains **OPEN / NOT PROVED**.
