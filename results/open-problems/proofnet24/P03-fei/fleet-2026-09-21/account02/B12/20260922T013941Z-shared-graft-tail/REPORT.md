# B12 FEI — infinite shared-graft tail theorem and a new source-valid lower floor

**Run:** `20260922T013941Z-b12-fei-graft-tail-r11`  
**Status:** **PARTIAL / TARGET-LEVEL LOWER-BOUND MOVEMENT. Full uniform-cube FEI remains OPEN / NOT PROVED.**  
**Execution:** `WITHOUT_VERIFIED_BRAIN`. Authorized GitHub control and scientific sources were read directly; no authenticated mathematical-brain retrieval/context was used.  
**Model self-report:** GPT-5.6 Sol. Requested effort: maximum actually supported. Configured effort and provider reasoning usage: not exposed / unknown.

## 0. Live target and why this is the same FEI problem

Fresh owner control revision `2026-09-22.2` supersedes the older interface-B-only prompt for this invocation. The live FEI target is the exact all-gate inequality: find a symmetric nonnegative potential `Gamma` of finite centre such that for every Boolean gate `G` and every product bias vector,

\[
\Gamma(p_{\rm out})+\widetilde H_G(p)
\le
\sum_i {\rm It}_i(G;p)
\frac{\Gamma(p_i)+h(V_{p_i})}{V_{p_i}},
\qquad V_u=4u(1-u).
\tag{G}
\]

The gate-reformulation report proves that existence of such a `Gamma` with finite `Gamma(1/2)` is equivalent to full uniform-cube FEI. For a **balanced** gate at uniform input bias, (G) specializes exactly to

\[
H(G)\le \Gamma(1/2)\,[I(G)-1].
\tag{0.1}
\]

Thus every balanced Boolean gate gives a necessary centre lower bound

\[
\Gamma(1/2)\ge R(G):=\frac{H(G)}{I(G)-1}.
\tag{0.2}
\]

The recent source-valid shared-core gates refute the former read-once-`Gamma`/AND-extremality candidate. This run does not repeat that finite refutation. It proves an **infinite-tail theorem** for the same genuine Boolean construction and obtains a strictly larger rigorous full-problem lower bound.

Scientific master read before this write: `78d3b49ef1610c2175c40c8a0952a84817486572`. Repository entry rules, `FLEET_RULES.md`, the P03 hourly protocol and the fresh P03 FEI README were read before writing.

## 1. Last three own substantive reports compared

The last three completed account02/B12 scientific reports on the inherited compression route were:

1. `20260921T232119Z-harmonic-root-marked-spectrum/REPORT.md`, blob `1a0ff3b828a377afde3461e6f130d46255ed1de5`: proved a one-source harmonic first-mark code \(H(J)\le4.8588229681\,I\), with exact continuation law, but left the global continuation entropy (not row-local depth) unpaid.
2. `20260921T211150Z-component-factorial-harmonic-capacity/REPORT.md`, scientific commit `62e2a41bd9ba8bde36e9c6d2cf7c51f9116dc84e`: factorially paid reciprocal-component routing and isolated exceptional component/address entropy.
3. `20260921T175134Z-physical-erasure-budget/REPORT.md`: exact physical-erasure/DTC conservation and near-subcube Palm stability, with a rigorous warning that TV/mean-degree closeness does not pay rare address entropy.

Those reports progressively sharpened the same harmonic/exceptional-address implication. The **later owner message changes the active mechanism**: all FEI workers now converge on the all-gate extremality/falsification target. Accordingly this run executes a materially different same-FEI mechanism rather than adding another row-local continuation estimate.

The three FLEET_RULES moves used substantively are **#5 add a parameter and differentiate**, **#7 take the limit**, and **#13 find what only increases**.

## 2. Named completed other-account results consumed

### 2.1 account01/B18: exact source-valid recurrence

Consumed in full:

`proofnet24/P03-fei/fleet-2026-09-21/account01/B18/20260922T0117Z-recursive-shared-graft/REPORT.md`

report blob `cbe682d84b52232ab4e91367b08bbfe73d74a39e`, reported scientific commit `b9b63c908139fcd280a4913229afd7ab62ca50aa`.

It proves that a fixed nine-host **shared-coordinate** graft sends any balanced monotone Boolean gadget with influence `I`, excess ratio

\[
R=\frac{H}{I-1},
\]

and a designated singleton Fourier coefficient `c`, after fourth balanced self-composition, to another genuine balanced monotone Boolean gadget satisfying

\[
I'=\frac{261}{128}+\frac9{256}(I^4-1),
\tag{2.1}
\]

\[
c'=\frac{57}{256}+\frac{c^4}{256},
\tag{2.2}
\]

and

\[
R'-R=
\frac{K(c^4)-\frac{133}{128}R}
     {\frac9{256}I^4+\frac{257}{256}},
\tag{2.3}
\]

where, with \(\phi(x)=-x\log_2x\),

\[
K(b)=H_{\rm core}(b)+\frac9{256}
[-\phi(b^2)+16(1-b^2)].
\tag{2.4}
\]

Crucially, this is not an arbitrary spectral recurrence: the report proves Booleanity and balanced monotonicity are preserved at every application.

### 2.2 account03/B18: certified rounds through \(F_4\)

Also consumed in full:

`proofnet24/P03-fei/fleet-2026-09-21/account03/B18/20260922T011005Z-recursive-shared-graft-extension/REPORT.md`

report blob `4d1e86bd941df8bb941ba974f6478bbe4842ef84`, with arithmetic checker blob `dc24627e2c157e87992698b4e43a28315548d3fc`.

It certifies the exact source and two further shared-graft rounds. In particular

\[
R_3\in[
6.5218509158557171794336583919648574196767563718341573,\,
6.5218509158557171794342597335463471829453334335276482],
\tag{2.5}
\]

\[
R_4\in[
6.5218509485644448965490881329959858569477358114202361,\,
6.5218509485644448965496895824490791318643557898359042],
\tag{2.6}
\]

and

\[
I_3=
\frac{
7293635508681408439604535567475568379907630049888658770829188246173012479808017893097
}{
1942668892225729070919461906823518906642406839052139521251812409738904285205208498176
}.
\tag{2.7}
\]

The peer explicitly left the infinite-tail sign of (2.3) open. That is the first implication attacked here.

## 3. Exact relaxation form

Put

\[
\alpha=\frac9{256},\qquad
a=\frac{133}{128},\qquad
B=\frac{257}{256},
\]

and define

\[
T(c):=\frac1a K(c^4)=\frac{128}{133}K(c^4),
\qquad
D_t:=B+\alpha I_t^4=I_{t+1}-1,
\qquad
\lambda_t:=\frac{a}{D_t}.
\tag{3.1}
\]

Then (2.3) becomes the exact relaxation identity

\[
\boxed{
R_{t+1}
=
R_t+\lambda_t\bigl(T(c_t)-R_t\bigr).
}
\tag{3.2}
\]

This isolates the sign of every future ratio increment: it is positive exactly when the current ratio lies below the moving threshold `T(c_t)`.

The singleton recurrence is

\[
F(c)=\frac{57}{256}+\frac{c^4}{256},
\qquad c_{t+1}=F(c_t).
\tag{3.3}
\]

For the inherited exact \(c_1=14593/65536\),

\[
0<c_4<c_3<c_2<c_1<\frac14.
\tag{3.4}
\]

## 4. The threshold moves by less than \(1.2\times10^{-12}\)

### 4.1 Contraction of the marked singleton

On \(0\le c\le1/4\),

\[
F'(c)=\frac{c^3}{64}\le\frac1{4096}=:L.
\tag{4.1}
\]

Hence `F` has a unique fixed point \(c_*\) in this interval and, using
\(c_1-c_2<10^{-5}\),

\[
|c_3-c_*|
\le
\frac{L^2}{1-L}|c_1-c_2|
<
3.372\times10^{-13}.
\tag{4.2}
\]

Thus all later \(c_t\), \(t\ge3\), remain in an extremely short interval around \(c_3\).

### 4.2 A source-exact Lipschitz bound for \(T\)

The peer checker represents the core coefficients as

\[
y_S(b)=\frac{A_S+bQ_S}{512},
\]

where `Q_S` is the sum of nine Walsh transforms of signed two-point host indicators. Each such transform has numerator magnitude at most `2`, so

\[
\sum_{S\subseteq[9]} |y_S'(b)|
\le 18.
\tag{4.3}
\]

For \(|y|\le1\),

\[
\phi(y^2)=-y^2\log_2(y^2)
\]

satisfies

\[
\left|\frac d{dy}\phi(y^2)\right|
=
\frac{2}{\ln2}e^{-u}|2u-1|
\le\frac2{\ln2},
\qquad u=-\ln|y|\ge0.
\tag{4.4}
\]

Indeed \(e^{-u}|2u-1|\le1\): it is immediate for \(0\le u\le1/2\), while on \(u\ge1/2\) the maximum is \(2e^{-3/2}<1\).

Therefore

\[
|H_{\rm core}'(b)|\le\frac{36}{\ln2}.
\tag{4.5}
\]

Since \(b=c^4\le1/256\),

\[
|K'(b)|
\le
\frac{36}{\ln2}
+\alpha\left(\frac2{\ln2}+\frac18\right).
\tag{4.6}
\]

The elementary atanh series gives
\(\ln2=2(1/3+1/(3^3\,3)+\cdots)>2/3\), so \(1/\ln2<3/2\). Combining (4.6) with \(4c^3\le1/16\),

\[
\boxed{
|T'(c)|<
\frac{10}{3}
\qquad(0\le c\le1/4).
}
\tag{4.7}
\]

From (4.2),

\[
|T(c_t)-T(c_3)|
<
1.124\times10^{-12}
\qquad(t\ge3).
\tag{4.8}
\]

This is the quantitative ingredient that was missing from the finite per-round peer certificate.

## 5. Recover the threshold from the certified \(R_3,R_4\)

From (3.2),

\[
T(c_3)
=
R_3+\frac{128}{133}(I_4-1)(R_4-R_3).
\tag{5.1}
\]

Using (2.7) and the exact recurrence (2.1),

\[
I_4
=
8.9891831269165525119469526862195470748936495017444294\ldots,
\qquad
8<I_4<9.
\tag{5.2}
\]

Applying the certified interval endpoints (2.5)--(2.6) with outward-safe choices gives

\[
T(c_3)\in[
6.5218511673478223997467338854786279585\ldots,\,
6.5218511673478223997565832923484880675\ldots].
\tag{5.3}
\]

Together with (4.8), every future threshold satisfies

\[
\boxed{
6.5218511673466984724830073516552831112
<
T(c_t)
<
6.5218511673489463270203098261718329148
\quad (t\ge3).
}
\tag{5.4}
\]

Call these two rationally certified envelope endpoints \(T_{\min},T_{\max}\).

## 6. The future relaxation weights are summable before the ratio can catch the threshold

For \(t=4\), (5.2) gives

\[
0.0044852122888072033183
<
\lambda_4
<
0.0071657552328870450689.
\tag{6.1}
\]

Also

\[
I_5
=
1+B+\alpha I_4^4
>
1+B+\alpha\,8^4
=
146.00390625.
\tag{6.2}
\]

For \(I_t\ge146\),

\[
I_{t+1}
=
\frac{261}{128}+\alpha(I_t^4-1)
>
\alpha I_t^4
>
I_t^2.
\tag{6.3}
\]

Therefore, for all \(t\ge5\), the remaining relaxation weights are dominated by a doubly-exponentially decaying geometric majorant:

\[
\sum_{t\ge5}\lambda_t
<
\frac a\alpha
\frac{I_{5,\min}^{-4}}{1-I_{5,\min}^{-4}}
<
6.504010403\times10^{-8}.
\tag{6.4}
\]

Consequently

\[
\boxed{
\sum_{t\ge4}\lambda_t
<
0.007165820272991071.
}
\tag{6.5}
\]

Even if every future step were charged at the top threshold \(T_{\max}\), its total possible rise from the certified \(R_4\) interval is less than

\[
1.567771\times10^{-9}.
\tag{6.6}
\]

But the certified gap from \(R_{4,\max}\) to \(T_{\min}\) is

\[
T_{\min}-R_{4,\max}
>
2.18782253575\times10^{-7}.
\tag{6.7}
\]

The residual headroom after paying the entire future relaxation budget is still

\[
\boxed{
T_{\min}-R_{4,\max}
-
\left(\sum_{t\ge4}\lambda_t\right)
(T_{\max}-R_{4,\min})
>
2.17214483160\times10^{-7}.
}
\tag{6.8}
\]

## 7. Infinite-tail theorem

### Theorem 7.1 — every later shared-graft round strictly raises the balanced excess ratio

For the source-valid shared-graft sequence \(F_t\) inherited from account01/B18 and account03/B18,

\[
\boxed{
R_{t+1}>R_t
\quad\text{for every }t\ge4.
}
\tag{7.1}
\]

Moreover \(R_t\) converges to a finite limit \(R_\infty<T_{\min}\).

#### Proof

At \(t=4\), (2.6) and (5.4) give \(R_4<T_{\min}\le T(c_4)\), so (3.2) gives a positive increment.

Assume inductively that the increments through step \(t-1\) are positive. Then \(R_s\ge R_{4,\min}\) for every \(4\le s\le t\), and from (3.2) and \(T(c_s)\le T_{\max}\),

\[
R_t
\le
R_{4,\max}
+\sum_{s=4}^{t-1}\lambda_s(T_{\max}-R_{4,\min}).
\]

By (6.8) this is strictly below \(T_{\min}\le T(c_t)\). Hence (3.2) gives \(R_{t+1}>R_t\), closing the induction.

The total increments are bounded by the convergent series in (6.5), so \(R_t\) has a finite limit. The same strict headroom estimate places that limit below \(T_{\min}\). QED.

This converts the previous two finite extension checks into a theorem about **all later Boolean rounds** of the same construction.

## 8. New full-problem lower bound: one more round without enumerating it

Using the lower weight in (6.1) and the gap in (6.7),

\[
R_5-R_4
>
9.8128485231170\times10^{-10}.
\tag{8.1}
\]

Therefore

\[
\boxed{
R_5
>
6.5218509495457297488607979520127607\ldots
}
\tag{8.2}
\]

and in particular

\[
\boxed{
C_{\rm FEI}
>
6.5218509495457.
}
\tag{8.3}
\]

Reason: \(F_5\) is a genuine finite balanced Boolean function by the inherited source theorem, and ordinary balanced disjoint self-composition of \(F_5\) has \(H/I\to R_5\).

The same argument gives a rigorous bracket for this **particular construction's** limiting excess ratio,

\[
6.5218509495457
<
R_\infty
<
6.521850950133,
\tag{8.4}
\]

where the upper endpoint is only a family-specific tail bound, not an FEI upper bound.

By (0.2), any all-gate potential proving FEI must therefore satisfy at least

\[
\Gamma(1/2)>6.5218509495457.
\tag{8.5}
\]

The important structural conclusion is stronger than the tiny numerical movement: **freezing a scalar gate lift at any finite member of this recursive shared-coordinate family is invalid**, because a later member provably has a larger balanced excess ratio.

## 9. Exact checker and limitations

`CHECK_TAIL.py` uses only Python's exact `Fraction` arithmetic. It consumes the peer-certified exact-rational interval endpoints for \(R_3,R_4\), the exact rational \(I_3\), and the exact recurrence. It checks:

- \(8<I_4<9\);
- the outward-safe interval for \(T(c_3)\);
- the exact singleton contraction and fixed-point tail bound;
- the threshold envelope using the proved \(|T'|<10/3\);
- the all-future relaxation-weight sum;
- the strict bootstrap headroom \(>2.17\times10^{-7}\);
- the next-round gain \(>9.81\times10^{-10}\);
- \(R_5>6.5218509495457\).

The checker output is archived beside this report. It is an arithmetic self-check of the new tail theorem; it does **not** independently reconstruct the 18-bit source truth table. Boolean source validity, the core Fourier formulas and the certified \(R_3,R_4\) endpoints remain explicit dependencies on the two named peer reports/checkers above.

## 10. FULL-PROBLEM CHANGE and MECHANISM CHANGE

**FULL-PROBLEM CHANGE:** **YES, lower-bound movement only.** Before this run the strongest consumed rigorous floor was

\[
C_{\rm FEI}>
6.5218509485644448965490881329959858569\ldots
\]

from \(F_4\). This run proves

\[
C_{\rm FEI}>6.5218509495457.
\]

No finite dimension-independent universal upper bound is proved. Full FEI remains **OPEN / NOT PROVED**.

**MECHANISM CHANGE:** **YES.** Before: the recursive shared-graft obstruction had to be certified one gigantic rational round at a time, and eventual monotonicity was explicitly left open. After: the recurrence is rewritten as a moving-threshold relaxation, the singleton state is proved contractive, the threshold is uniformly Lipschitz, and the future relaxation weights are summable. This proves strict improvement for **every later round** from the same Boolean source.

**Quantified remaining implication:** the gate route now needs a finite-centre symmetric potential whose all-gate slack survives this entire limiting shared-coordinate family (centre necessarily above `6.5218509495457`) **and** every other gate/bias, or a further genuine Boolean family forcing a still larger centre. This run does not supply that universal potential.

## 11. Privacy / provenance review

Changed scientific files contain only mathematical formulas, exact public-to-this-private-repository artifact identifiers, sanitized model/provenance metadata and checker output. They contain no credentials, scheduler identifiers, machine paths, raw private transcripts, benchmark material, email/Drive content, permission changes or unrelated private data.

No publication-priority or novelty claim is made.
