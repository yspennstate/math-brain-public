# B13 FEI campaign A — asymmetric defect compiler and influence-relative exceptional-set ledger

**Account/slot:** account04/B13  
**Live assignment:** A — prove an influence-relative exceptional-set estimate strong enough for A's precise induction.  
**Status:** **ESSENTIAL_STEP_APPLIED / PARTIAL. Full uniform-cube FEI remains OPEN / NOT PROVED.**  
**Execution:** **WITHOUT_VERIFIED_BRAIN**. No authenticated brain retrieval or receiver-context use occurred.  
**Novelty/priority:** unverified; no publication-priority claim.

## 0. Exact candidate and newest peer input

This run is bound to the current campaign-A lead candidate

`account01/B18/20260921T2205Z-folded-cooling-compiler/REPORT.md`, blob `9f2bb40584be20e5e440e7f3913873c34858bc91`.

Its precise local obligation is to find, on a high corrected-ratio core, one physical block/survivor pair `(A,j)` satisfying

\[
c_j(A)\ge \gamma j_j,
\qquad
E_A-\lambda\Lambda_A\le K h_2(j_j)
\tag{0.1}
\]

for universal `gamma>0`, `K<infinity`, `lambda>=0`, or to force a complementary already-paid branch. Under this certificate the lead compiler gives a finite universal FEI constant. The lead also proves that the folded activation bank can be re-centered at descendants and is spent only once.

The **newest compatible other-account result actually used** is

`account02/B14/20260921T230653Z-asymmetric-shortcircuit-ledger/REPORT.md`, blob `242a3fddee17db5ed1d723962b76c8659f623d6a`.

For a pivot `x`, an ideal coordinate-subcube proxy `Q={Z=a}` of codimension `r`, density `q=2^{-r}`, pivotality event `E_x`, and one-sided errors

\[
E^-:=\Pr(Q\cap E_x^c),\qquad E^+:=\Pr(Q^c\cap E_x),
\tag{0.2}
\]

that report proves the **asymmetric physical block theorem**

\[
I_Z\le rj_x,\qquad
E^-\le q/16,\qquad E^+\le {q\over 8(r+1)}
\quad\Longrightarrow\quad
\Delta_ZH\le 12I_Z.
\tag{0.3}
\]

This changes the argument materially. The preceding account04/B18 scalar compiler used the older symmetric condition `e<=q/(16r)`. The new theorem says fixed-relative false-negative mass is harmless; only outside false-positive pollution needs the `1/r` scale. This run converts that asymmetry into a larger defect-certifiable region and a one-sided description of the surviving exceptional rows.

I also retain the completed account04/B13 stability input. For a low normalized depth-defect row,

\[
\delta_x={d_x\over j_x}-{1\over2}\log_2{1\over j_x},
\tag{0.4}
\]

there is a coordinate-subcube proxy `Q` with total support error `e=E^-+E^+` satisfying

\[
\alpha:={e\over j_x}
\le
\phi(\delta_x):=
{4\delta_x\over \log_2(1/(2\delta_x))}
\le\delta_x
\tag{0.5}
\]

through the current low-defect threshold `eta_0<=1/32`.

Throughout, the exact account04/B18 mixed-curvature law remains untouched:

\[
\kappa_{ik}=\kappa_{ki}=p_{ik}+4o_{ik},
\qquad
\sum_{i\ne k}(p_{ik}+4o_{ik})=4d_k.
\tag{0.6}
\]

No step drops the opposite-sign term `o_ik`, and no step assumes `sum d_k=O(J)`.

## 1. New asymmetric scalar threshold

For `r>=1` define

\[
M_r:=8r+9
\tag{1.1}
\]

and let

\[
\boxed{
\delta_{\rm asy}(r)
:=
{W(2\ln2\,M_r)\over 4\ln2\,M_r},
}
\tag{1.2}
\]

where `W` is the principal Lambert-W function. Equivalently `delta_asy(r)` is the unique positive solution of

\[
\boxed{
\phi(\delta_{\rm asy}(r))={1\over 8r+9}.
}
\tag{1.3}
\]

The equivalence follows from

\[
4M_r\ln2\,\delta=\ln{1\over2\delta}
\iff
(4M_r\ln2\,\delta)e^{4M_r\ln2\,\delta}=2M_r\ln2.
\]

As in the previous scalar compiler, `phi` is strictly increasing on the relevant interval, so `delta_asy(r)` is strictly decreasing in `r`.

## 2. PROVED: asymmetric defect-to-certificate compiler

### Theorem 2.1

Median-character center the current Boolean state. Let `x` be a maximum-influence active coordinate,

\[
j:=j_x=\operatorname{Inf}_x(f)\le1/2.
\]

Assume `0<delta_x<=eta_0`, and let the completed stability theorem supply a coordinate-subcube proxy

\[
Q=\{Z=a\},\qquad |Z|=r,\qquad q=2^{-r}
\]

with `e/j<=phi(delta_x)`. If

\[
\boxed{\delta_x\le\delta_{\rm asy}(r),}
\tag{2.1}
\]

then `Z` is a genuine campaign-A certificate for the current account01/B18 compiler. More precisely,

\[
\boxed{
\Delta_ZH\le12I_Z,
\qquad
c_x(Z)\ge{16\over17}j,
\qquad
I_Z\le h_2(j),
}
\tag{2.2}
\]

and hence for every fixed `lambda>=0`,

\[
\boxed{
E_Z-\lambda\Lambda_Z\le12h_2(j).
}
\tag{2.3}
\]

Thus this branch supplies a `(gamma,K,lambda)=(16/17,12,lambda)` certificate.

### Proof

Put `alpha=e/j`. By (2.1), monotonicity of `phi`, and (1.3),

\[
\alpha\le{1\over8r+9}.
\tag{2.4}
\]

Density error is bounded by symmetric-difference error, so

\[
q\ge j-e=(1-\alpha)j.
\tag{2.5}
\]

Consequently

\[
e=\alpha j
\le {q\over8(r+1)},
\tag{2.6}
\]

because (2.4) is exactly

\[
8(r+1)\alpha\le1-\alpha.
\]

Both one-sided errors are at most the total error, hence

\[
E^+\le e\le {q\over8(r+1)},
\qquad
E^-\le e\le {q\over8(r+1)}\le {q\over16}.
\tag{2.7}
\]

Since `x` has maximum influence, every control satisfies `j_k<=j`, so

\[
I_Z\le rj.
\tag{2.8}
\]

The newest account02/B14 theorem (0.3) now gives

\[
\Delta_ZH\le12I_Z.
\tag{2.9}
\]

For crossing, the already established physical block inequality is

\[
c_x(Z)\ge j-e=(1-\alpha)j.
\]

Since `alpha<=1/(8r+9)<=1/17`,

\[
c_x(Z)\ge{16\over17}j.
\tag{2.10}
\]

It remains to compare the control influence with the target marginal entropy. From (2.5) and (2.4),

\[
j\le 2^{-r}{8r+9\over8r+8}
=2^{-r}\left(1+{1\over8r+8}\right).
\tag{2.11}
\]

Therefore

\[
\log_2{1\over j}
\ge r-\log_2\left(1+{1\over8r+8}\right).
\tag{2.12}
\]

For `0<j<=1/2`,

\[
{h_2(j)\over j}
=
\log_2{1\over j}
+{1-j\over j}\log_2{1\over1-j}
\ge
\log_2{1\over j}+{1\over2\ln2},
\tag{2.13}
\]

using `-ln(1-j)>=j` and `1-j>=1/2`. Also

\[
\log_2\left(1+{1\over8r+8}\right)
\le {1\over(8r+8)\ln2}
<{1\over2\ln2}.
\tag{2.14}
\]

Combining (2.12)--(2.14) gives `h_2(j)>=rj`, so (2.8) yields `I_Z<=h_2(j)`.

Finally the exact corrected-entropy decomposition already used by account04/B14 gives

\[
E_Z-\lambda\Lambda_Z
\le E_Z\le B_Z\le\Delta_ZH,
\]

because `Lambda_Z>=0` and the correction/refund terms are nonnegative. Apply (2.9) and `I_Z<=h_2(j)` to obtain (2.3). QED.

### What this improves

The preceding scalar compiler required, after converting total error to density error,

\[
\alpha\le {1\over16r+1}.
\]

The new sufficient condition is

\[
\boxed{\alpha\le{1\over8r+9}.}
\tag{2.15}
\]

For large `r`, this asymptotically doubles the admissible total relative support error and correspondingly raises the positive-defect threshold from order `(log r)/(64r)` to `(log r)/(32r)`.

## 3. PROVED: stronger one-sided compiler when the proxy is not smaller than the row

The asymmetric peer theorem permits a sharper result when the proxy density lies on the false-negative-heavy side.

Define

\[
A_r^+:=\max\{16,\,4(r+1)\}
\tag{3.1}
\]

and

\[
\boxed{
\delta_+(r)
:={W(2\ln2\,A_r^+)\over4\ln2\,A_r^+},
\qquad
\phi(\delta_+(r))={1\over A_r^+}.
}
\tag{3.2}
\]

### Theorem 3.1 — false-negative-heavy rows are easier

Under the hypotheses of Theorem 2.1, suppose additionally

\[
q\ge j.
\tag{3.3}
\]

If

\[
\delta_x\le\min\{\eta_0,\delta_+(r)\},
\tag{3.4}
\]

then `Z` again satisfies the account01/B18 certificate, now with the uniform crossing fraction

\[
\boxed{c_x(Z)\ge{15\over16}j.}
\tag{3.5}
\]

### Proof

Let `alpha=e/j<=1/A_r^+`. Because `q>=j`,

\[
E^-\le e=\alpha j\le j/16\le q/16.
\tag{3.6}
\]

Moreover the exact density identity

\[
j=q+E^+-E^-
\]

gives

\[
E^+={e+j-q\over2}\le{e\over2}
\le{\alpha j\over2}
\le{q\over8(r+1)}.
\tag{3.7}
\]

Thus the asymmetric block theorem applies. The crossing estimate is `c_x(Z)>=j-e>=(1-alpha)j>=15j/16`. The entropy comparison `I_Z<=h_2(j)` is easier than in Theorem 2.1 because `q>=j=2^{-L}` implies `r<=L`, hence `rj<=jL<=h_2(j)`. The corrected certificate follows exactly as before. QED.

### Small-codimension consequence

Because the stability regime already gives `alpha<=delta_x<=eta_0<=1/32`, for every

\[
1\le r\le7
\]

we automatically have

\[
\alpha\le1/32\le\min\{1/16,1/[4(r+1)]\}.
\]

Hence:

\[
\boxed{
\text{No low-defect terminal maximum row with }q\ge j\text{ can have proxy codimension }r\le7.
}
\tag{3.8}
\]

Any such surviving small-codimension low-defect row must be on the **outside-heavy side** `q<j`, exactly the side measured by the new peer theorem's false-positive obstruction.

This is the one-sided structural gain that the former symmetric `e<=q/(16r)` compiler could not see.

## 4. PROVED: influence-relative exceptional-set estimate

The preceding statements can be turned into an all-eligible-row exceptional ledger without an ambient-dimension factor.

Let `R` be any family of active rows for which:

1. the current stability theorem supplies a proxy `Q_i` of codimension `r_i` and relative error `alpha_i<=phi(delta_i)` whenever `delta_i<=eta_0`; and
2. the physical controls satisfy the campaign-A average-control condition
   \[
   I_{F_i}\le r_i j_i.
   \tag{4.1}
   \]

(The maximum-influence row at every node of the A induction automatically satisfies (4.1).)

Call `i` **asymmetrically exceptional** if the row is not captured by Theorem 2.1, including the high-defect case `delta_i>eta_0`. Put

\[
\tau(r):=\min\{\eta_0,\delta_{\rm asy}(r)\}.
\tag{4.2}
\]

### Theorem 4.1 — weighted exceptional influence is defect-paid

For every such family,

\[
\boxed{
\sum_{i\in R_{\rm exc}} j_i\,\tau(r_i)
<
\sum_{i\in R_{\rm exc}} j_i\delta_i
\le
\mathcal D(f):=\sum_i j_i\delta_i.
}
\tag{4.3}
\]

Consequently, for every finite codimension cutoff `R_0`,

\[
\boxed{
\sum_{\substack{i\in R_{\rm exc}\\ r_i\le R_0}}j_i
\le {\mathcal D(f)\over\tau(R_0)}.
}
\tag{4.4}
\]

No factor `n`, number of rows, or cube-alphabet size appears.

### Proof

If an exceptional row has `delta_i>eta_0`, then trivially `delta_i>tau(r_i)`. Otherwise `delta_i<=eta_0`. If it also had `delta_i<=delta_asy(r_i)`, Theorem 2.1 would capture it, contradicting exceptionality. Hence again `delta_i>tau(r_i)`. Multiply by `j_i` and sum to obtain (4.3).

The function `delta_asy(r)` is decreasing, hence so is `tau(r)`. If `r_i<=R_0`, then `tau(r_i)>=tau(R_0)`, and (4.4) follows from (4.3). QED.

This is the requested influence-relative exceptional-set estimate: the exceptional mass is not paid by cube measure times ambient dimension. Its exact weight is the scalar threshold that separates rows already removable by a real physical coefficient-12 block from the positive-defect remainder.

A stronger version holds on the `q_i>=j_i` side by replacing `tau(r)` with

\[
\tau_+(r):=\min\{\eta_0,\delta_+(r)\}.
\tag{4.5}
\]

## 5. PROVED: recursive nonreuse with the enlarged certificate region

Modify the existing account04/B14 physical peeling policy only in its local acceptance test:

- at a reached node, median-character center;
- choose a maximum-influence pivot `x`;
- if its low-defect stability proxy satisfies the scalar condition of Theorem 2.1 (or the stronger one-sided condition of Theorem 3.1), reveal that genuine physical proxy block `Z` and recurse on every child;
- otherwise stop that branch for this phase.

Every selected step obeys

\[
\Delta_ZH\le12I_Z\le12D_Z,
\tag{5.1}
\]

where `D_Z=J(f)-EJ(child)` is the exact folded-influence drift. Therefore the same nonreuse telescope as in account04/B14 gives

\[
\boxed{
\sum_{u\text{ internal}}w_u\Delta_{Z_u}H
\le12\sum_u w_uD_{Z_u}
\le12J(f_{\rm root}).
}
\tag{5.2}
\]

Thus the larger asymmetric certificate region is not merely a one-row statement: it can replace the older local test in A's actual physical induction without reusing influence budget.

At a nonconstant terminal leaf, its maximum row `x` therefore obeys the sharpened alternative

\[
\boxed{
\delta_x>
\min\left\{\eta_0,\delta_{\rm asy}(r_x)\right\},
}
\tag{5.3}
\]

and, if `q_x>=j_x`, the still stronger

\[
\boxed{
\delta_x>
\min\left\{\eta_0,\delta_+(r_x)\right\}.
}
\tag{5.4}
\]

In particular, a low-defect terminal maximum row of codimension at most seven must have `q_x<j_x` by (3.8).

This is the exact old/new missing-implication change for campaign A:

- **old:** terminality only forced the symmetric `delta_*(r)` floor coming from `1/(16r+1)`;
- **new:** terminality forces the larger `delta_asy(r)` floor coming from `1/(8r+9)`, and false-negative-heavy rows obey the still larger `delta_+(r)` floor.

The remaining hard branch is correspondingly one-sided: genuinely positive-defect and/or outside-false-positive-heavy rows.

## 6. Quantitative calibration

A standard-library checker solves the three scalar root equations by monotone bisection and verifies the exact sufficient-condition algebra for every `1<=r<=4096`.

Selected values are:

| `r` | old symmetric floor | new general asymmetric floor | `q>=j` floor | new/old |
|---:|---:|---:|---:|---:|
| 1 | 0.0491958682 | 0.0491958682 | 0.0513184260 | 1.000 |
| 2 | 0.0305504676 | 0.0374059025 | 0.0513184260 | 1.224 |
| 4 | 0.0183413658 | 0.0260061261 | 0.0438790491 | 1.418 |
| 8 | 0.0107384965 | 0.0167729985 | 0.0286485648 | 1.562 |
| 32 | 0.0034904370 | 0.0060160152 | 0.0105443037 | 1.724 |
| 128 | 0.0010803224 | 0.0019386972 | 0.0034735364 | 1.795 |
| 4096 | 0.0000506200 | 0.0000943608 | 0.0001751187 | 1.864 |

The maximum numerical residual in `phi(delta_asy(r))=1/(8r+9)` over this range was `2.082e-17`; the exact algebraic sufficient-condition checks had no positive violation beyond floating roundoff (`1.110e-16`). These computations are calibration/falsification checks only; the theorem is analytic.

## 7. Preservation of mixed curvature and the exact zero-defect endpoint

Nothing in this run modifies the account04/B18 mixed-curvature conservation (0.6). The exceptional ledger is defined using the same normalized positive depth defect `delta_i`; it does not replace curvature by unsigned support boundary and does not spend `sum d_i` as though it were `O(J)`.

The exact zero-defect classification is also preserved. If all active rows have `delta_i=0`, then every row lies below every positive scalar threshold in this report, but the stronger account04/B18 theorem still supplies the root classification: a character times a signed one-point defect, with irrelevant variables allowed, and `H<4J`. The present certificate/peeling statements are compatible consequences, not a replacement proof of that endpoint.

## 8. Exact remaining implication

This run **does not** close FEI. It enlarges and recursively pays the physical branch that the campaign-A lead needs, and it gives an influence-relative weighted ledger for what remains.

The next unpaid class is now narrower:

1. high-defect rows `delta>eta_0`;
2. low-defect rows above the new `delta_asy(r)` floor; and
3. in the smallest surviving low-defect codimensions, necessarily **outside-heavy** rows `q<j` rather than fixed-relative false-negative rows.

The newest account02/B14 result also supplies, on the remaining fixed-relative branch, a random-order first-mismatch tree with folded drift at least `15rq/16` and residual pivotality entropy at most `h_2(e)`. The campaign-A next attack should therefore target the **upper corrected-entropy cost of that same realizable tree**, or couple the outside-heavy exceptional ledger (4.3) to the lead's folded activation / curvature-refund bank without reuse.

The raw second-factorial moment is not an admissible substitute.

**Classification:** `ESSENTIAL_STEP_APPLIED`.  
**Full FEI:** **OPEN / NOT PROVED**.
