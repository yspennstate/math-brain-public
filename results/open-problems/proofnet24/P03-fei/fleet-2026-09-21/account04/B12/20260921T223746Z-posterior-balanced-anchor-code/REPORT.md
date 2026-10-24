# B12 FEI — posterior-balanced influence-relative row code

**Run:** `B12-20260921T223746Z-r40`  
**Execution:** `WITHOUT_VERIFIED_BRAIN`  
**Status:** **PARTIAL. Full uniform-cube Fourier entropy--influence remains OPEN / NOT PROVED.**  
**Claim level:** analytic interface-B auxiliary theorems plus exhaustive finite falsification checks. No novelty or publication-priority claim.

## 0. What changed

The preceding account04/B12 run compressed the robust Palm row label with the harmonic one-companion code, leaving explicit off-trigger/nonrobust companion channels. This run changes mechanism. It couples the **support-only mixed-curvature bank** to a Bernoulli physical reveal at exactly the posterior-crossing scale and uses the newest account02 actual-anchor theorem on the same random cut.

The new consequence is an influence-relative two-part robust-row budget. At the live relative `1/16` near-subcube threshold, after the balanced reveal,

\[
\mathbb E\,L_R^{\rm surv}\le {J^2\over 7M}\le {2\over7}J,
\]

where \(L_R^{\rm surv}\) is the row-weighted number of robust trigger incidences still unresolved among surviving coordinates, while the actual-anchor signed child-correction code satisfies

\[
\mathbb E\,\Gamma(A)
\le {J\over2}-{J^2\over8M}.
\]

Hence

\[
\boxed{\quad
\mathbb E\bigl[\Gamma(A)+L_R^{\rm surv}(A)\bigr]
\le {J\over2}+{J^2\over56M}
\le {15\over28}J.
\quad}
\]

There is no ambient dimension, no \(\log n\), and no use of
\(\sum_i d_i=O(J)\). The quantity \(M\) is the support-disagreement part of mixed curvature; opposite-sign orientation mass is not silently charged as support.

This still does **not** pay the Fourier-Shannon cost of the physical reveal or the varying branch-character label. Those remain the universal obstruction.

## 1. Fresh peer result consumed: account02/B13 actual-anchor correction

The named newest compatible account02 input is

`proofnet24/P03-fei/fleet-2026-09-21/account02/B13/20260921T215826Z-cross-plaquette-tensor-correction/REPORT.md`

(report blob `17387ba6940056fd7df07a4205d816e9ce4dc7cf`, introduced at scientific commit `fac5798cba0a75b45b237d0dfd1b431191d40da8`).

For every physical cut \(A\mid B\), it constructs one **actual anchor child** and branch signs. If

\[
\epsilon_a
=\Pr_b[f(a,b)\ne \sigma_a f(a_0,b)]
\]

and

\[
\Gamma(A):=\mathbb E_a h_2(\epsilon_a),
\]

then its theorem gives

\[
\boxed{\Gamma(A)\le {1\over2}P_{B\to A}(f),}
\tag{1.1}
\]

where \(P_{B\to A}\) is the genuine Boolean cross-support/plaquette bank. This is dimension-free and source-exact. The older direct use
\(P_{B\to A}\le4\sum_{i\in A}d_i\) retained a raw depth/base-selector term.

**Exact implication used here:** apply (1.1) *before* replacing the cross-support bank by total derivative depth. Averaging the actual cross-support bank over a carefully chosen Bernoulli physical cut makes the anchor correction itself \(O(J)\), while preserving the support/orientation split.

The same account02 theorem explicitly warns that physical correction entropy is not already Fourier-entropy continuity; this run preserves that limitation.

## 2. Mixed-curvature input retained exactly

Use the newest account04/B18 integration

`proofnet24/P03-fei/fleet-2026-09-21/account04/B18/20260921T221132Z-support-depth-stalled-core/REPORT.md`

(report blob `496b62576a50af809beddde4f0e1901d4358a486`).

After the minimizing-character gauge, write

\[
0<j_i=\operatorname{Inf}_i(f)\le {1\over2},
\qquad
J=\sum_i j_i.
\]

For the derivative support indicator \(\eta_i\), let

\[
p_{ik}=\Pr[\eta_i(x)\ne\eta_i(x+e_k)],
\]

and let \(o_{ik}\) be opposite-sign overlap. B18 proves

\[
\kappa_{ik}=p_{ik}+4o_{ik},\qquad
\sum_{k\ne i}\kappa_{ik}=4d_i.
\]

Define

\[
M={1\over4}\sum_{i\ne k}p_{ik},\qquad
O=\sum_{i\ne k}o_{ik},\qquad
D=\sum_i d_i.
\]

Then the exact support/orientation split is

\[
\boxed{D=M+O.}
\tag{2.1}
\]

In particular, no statement below substitutes \(D=O(J)\).

The same report proves two further inputs used here:

\[
\boxed{M\ge J/2,}
\tag{2.2}
\]

and, for the relative-\(\varepsilon\) physical near-subcube robust sector \(R\),

\[
\sum_{i\in R}j_i|F_i|
\le {2\over1-2\varepsilon}\,M.
\tag{2.3}
\]

At the live threshold \(\varepsilon=1/16\),

\[
\boxed{
L_R:=\sum_{i\in R}j_i|F_i|
\le {16\over7}M.
}
\tag{2.4}
\]

B18 also retains the centered crossing refund \(C_A\). If \(A_t\) includes every physical coordinate independently with probability \(t\), \(s=1-t\), then

\[
\boxed{
\mathbb E C_{A_t}\ge s[J-2sM]_+.
}
\tag{2.5}
\]

## 3. New theorem: Bernoulli averaging prices the actual-anchor correction by support depth

For a physical block \(A\), put \(B=A^c\). In the notation above,

\[
P_{B\to A}
=\sum_{\substack{i\in B\\ k\in A}}p_{ik}.
\tag{3.1}
\]

Let \(A_t\) be a Bernoulli block: each coordinate is revealed independently with probability \(t\), and let \(s=1-t\).

### Theorem B12-BERNOULLI-ANCHOR-01

For every centered nonconstant Boolean \(f\),

\[
\boxed{
\mathbb E P_{A_t^c\to A_t}
=4tsM.
}
\tag{3.2}
\]

Consequently the account02 actual-anchor code obeys

\[
\boxed{
\mathbb E\Gamma(A_t)
\le 2tsM.
}
\tag{3.3}
\]

### Proof

For each ordered pair \(i\ne k\), the event
\(i\notin A_t,\ k\in A_t\) has probability \(st\). Therefore

\[
\mathbb E P_{A_t^c\to A_t}
=st\sum_{i\ne k}p_{ik}
=4stM.
\]

Apply (1.1) pointwise in \(A_t\) and average. QED.

This is deliberately a **support** calculation. The opposite-sign bank \(O\) never enters (3.2).

## 4. New balanced scale: actual physical correction costs at most \(J/2\)

Set

\[
\boxed{s_*={J\over4M},\qquad t_*=1-s_*.}
\tag{4.1}
\]

By (2.2), \(0<s_*\le1/2\), so this is a valid physical Bernoulli reveal.

Apply Theorem 01:

\[
\begin{aligned}
\mathbb E\Gamma(A_{t_*})
&\le 2s_*(1-s_*)M\\
&={J\over2}-{J^2\over8M}.
\end{aligned}
\]

Thus

\[
\boxed{
\mathbb E\Gamma(A_{t_*})
\le {J\over2}-{J^2\over8M}
\le {J\over2}.
}
\tag{4.2}
\]

This is the first conclusion of the run: the newest account02 **actual-anchor signed correction** can be made influence-relative without replacing \(M\) or \(D\) by \(O(J)\). If \(M/J\) is large, the policy reveals more coordinates rather than paying the large support bank at unit price.

At the same scale, (2.5) gives

\[
\boxed{
\mathbb E C_{A_{t_*}}
\ge {J^2\over8M}.
}
\tag{4.3}
\]

So the same randomized physical step simultaneously creates a real centered-influence crossing refund.

## 5. New robust-row compression: unresolved trigger incidences are \(O(J)\) at the same scale

For a realized block \(A\), define the **surviving robust trigger load**

\[
L_R^{\rm surv}(A)
:=
\sum_{\substack{i\in R\\ i\notin A}}
j_i\,|F_i\setminus A|.
\tag{5.1}
\]

This is a conservative one-bit-per-incidence address budget for the robust rows that physically survive the reveal. It is not asserted to equal Fourier entropy.

Because \(i\notin A\) and \(k\notin A\) for \(k\in F_i\) are independent events of probability \(s\),

\[
\mathbb E L_R^{\rm surv}(A_t)
=s^2\sum_{i\in R}j_i|F_i|
=s^2L_R.
\tag{5.2}
\]

Use (2.4) and the balanced scale (4.1):

\[
\boxed{
\mathbb E L_R^{\rm surv}(A_{t_*})
\le {16\over7}s_*^2M
={J^2\over7M}
\le {2\over7}J.
}
\tag{5.3}
\]

This is directly an interface-B influence-relative conversion. The raw robust trigger codimension may be large, but after a single support-adaptive physical reveal the expected unresolved row-weighted trigger load is bounded by a universal multiple of \(J\).

### Combined budget

Add (4.2) and (5.3):

\[
\begin{aligned}
\mathbb E[
 \Gamma(A_{t_*})+L_R^{\rm surv}(A_{t_*})
]
&\le
{J\over2}-{J^2\over8M}
+{J^2\over7M}\\
&=
{J\over2}+{J^2\over56M}\\
&\le {15\over28}J.
\end{aligned}
\]

Hence

\[
\boxed{
\mathbb E[
 \Gamma(A_{t_*})+L_R^{\rm surv}(A_{t_*})
]
\le {15\over28}J.
}
\tag{5.4}
\]

The two positive objects here are genuinely different: \(\Gamma\) is the source-exact signed actual-anchor correction entropy from account02/B13, while \(L_R^{\rm surv}\) is a conservative unresolved robust trigger-address capacity. Neither term contains \(n\), \(\log n\), or \(\sum d_i\).

## 6. Deterministic nontrivial cut: correction can be charged to the crossing refund

There is also a derandomized form that prevents the existence statement from being satisfied only by a trivial full reveal.

For any \(0<s<J/(2M)\), let \(t=1-s\). From (3.3) and (2.5),

\[
\mathbb E\Gamma(A_t)\le2s(1-s)M,
\qquad
\mathbb E C_{A_t}\ge s(J-2sM)>0.
\]

Therefore some block with \(C_A>0\) satisfies

\[
\boxed{
\Gamma(A)
\le
{2(1-s)M\over J-2sM}\,C_A.
}
\tag{6.1}
\]

Indeed, otherwise the strict reverse inequality on every \(C_A>0\) block would contradict the two averaged bounds. Since \(C_A>0\), this selected block is not a trivial no-information cut.

At the balanced scale \(s_*=J/(4M)\),

\[
\boxed{
\Gamma(A)
\le
\left({4M\over J}-1\right)C_A
}
\tag{6.2}
\]

for at least one nontrivial physical block.

Thus whenever the support-depth ratio is bounded, \(M\le LJ\), the actual-anchor correction is absorbed by a bounded multiple of the **existing centered-influence crossing refund**:

\[
\boxed{\Gamma(A)\le(4L-1)C_A.}
\tag{6.3}
\]

This is a clean A/B-interface glue statement; it does not assert that \(M/J\) is universally bounded.

## 7. Relation to the newest account04/B13 proxy-gauge theorem

The current account04/B13 result

`proofnet24/P03-fei/fleet-2026-09-21/account04/B13/20260921T2225Z-proxy-gauge-closure/REPORT.md`

(report blob `1ec1555932e690e403f7d4320640040628697b96`) reveals the source-frontier plus high-defect exceptional coordinates once and then quotients each surviving child by its explicit branch-dependent proxy character. It proves the exact identity

\[
\mathbb E_z I(\chi_{T(z)}f_{B=z})
=\sum_{r\in S}e_r
\le\mathcal D(f),
\]

with no ambient-dimensional multiplier.

The present result complements it: the **signed nonproduct correction** produced by a physical reveal admits the \(O(J)\) balanced actual-anchor code (4.2), and robust unresolved trigger incidences admit (5.3). Therefore the remaining universal obstruction is more sharply localized to the parent-to-child Fourier-Shannon cost of the reveal and the varying branch-character label \(T(z)\), together with the exceptional/off-trigger channels not already eliminated by the source frontier. The physical correction itself no longer needs a raw-depth payment.

## 8. New account01/B12 closed-component result and compatibility

A new compatible account01/B12 result landed during this run:

`proofnet24/P03-fei/fleet-2026-09-21/account01/B12/20260921T2238Z-component-predictor/REPORT.md`

(commit `7b55b6af31b351c44260c178e5315923b3868f83`).

It proves, in the **closed fine** physical/Palm reciprocal-component sector
\(\epsilon_i\le1/(16m_C)\), a Kraft inequality

\[
\sum_C2^{-m_C}\le17/22
\]

and an actual predecessor predictor paying the component macro-label:

\[
I H(\rho)-D_{\rm seq}\le {25\over8}I.
\]

It also proves the universal Boolean bipartition interaction bound
\(AB\le4\Delta\).

**Exact implication for this run:** that theorem already closes the fine closed-component macro-label branch, while (5.4) works at the coarser live relative-\(1/16\) robust threshold and does not require closed components. The two mechanisms are complementary rather than duplicate: Kraft/prefix prediction handles the fine closed macro-label; posterior-balanced revealing handles coarse robust trigger load plus the actual physical correction.

## 9. Decisive exhaustive calculation

`check_posterior_balanced_anchor_code.py` was executed locally with the standard library. It enumerated every Boolean function modulo global output sign through dimension four, applied the minimizing-character gauge, and for every physical cut:

- computed the genuine support bank \(p_{ik}\) and \(M\);
- exhaustively optimized the **actual physical anchor child** and branch signs;
- checked the account02 bound \(\Gamma(A)\le P_{A^c\to A}/2\);
- checked the Bernoulli cross-bank identity exactly;
- computed the centered crossing refund \(C_A\) exactly;
- checked (4.2)--(4.3) and the averaged correction-minus-crossing inequality.

Results:

- nonconstant gauged Boolean functions: `32,876`;
- physical cut checks: `525,008`;
- minimum observed \(M/J\): exactly `1/2`;
- maximum excess in the peer actual-anchor inequality: `0`;
- maximum excess in the balanced expectation inequality: `0`;
- maximum excess in the correction-minus-crossing inequality: `0`;
- equality functions for the balanced correction bound: `124`;
- maximum observed expected actual-anchor correction: `0.444444444444`;
- violations: `0`.

The code exited `0`. The Python environment emitted an unrelated spreadsheet-runtime warmup warning on stderr before normal execution; it did not alter the checker output or exit status.

Checker SHA-256:
`1f36ffd9c799a0230d709b07a475c1f60fad7baa2ec3302bfc20900ec50973df`.

Captured theorem-check stdout SHA-256:
`8e070ec1428884f4d029b51af3b4442c6227d5c6e9f3f749adef715dd3d385b5`.

The enumeration is falsification evidence only. The inequalities in Sections 3--6 are analytic consequences of the cited source-exact peer theorems.

## 10. What remains open

This run does **not** prove FEI. In particular:

1. \(L_R^{\rm surv}\) is a conservative robust address budget, not itself a proof of the parent Fourier-entropy recursion.
2. The physical reveal block can still carry unpaid Fourier-Shannon information.
3. The branch-dependent character label \(T(z)\) from the proxy-gauge theorem still needs a source-exact nonreusing code outside the fine closed-component branch.
4. Nonrobust/off-trigger companion channels remain live.
5. No estimate \(\sum_i d_i=O(J)\) is used or implied.

The next interface-B target is now narrower: combine the coarse balanced reveal (5.4) with the fine closed-component Kraft predictor and the proxy-gauge identity to encode the **varying branch-character label** without paying the reveal block by ambient dimension. The mandatory ledger should retain the crossing refund \(C_A\), factorial/prefix negative credits, and the exact support/orientation split \(D=M+O\) exactly once.

`joint_directive`: `FEI-JOINT-FOUR-ACCOUNTS-2026-09-21-192650Z`.

`consumed_peer_artifact`: account02/B13 `20260921T215826Z-cross-plaquette-tensor-correction`, plus the current account04/B18 support-depth integration and the newly landed account01/B12 closed-component predictor.

`mechanism_change`: harmonic one-companion coding -> Bernoulli physical posterior balancing plus actual-anchor correction.

`full_problem_change`: robust unresolved trigger incidence plus actual signed anchor-correction cost is now \(O(J)\) in expectation at one common support-adaptive reveal scale. Full FEI remains OPEN.

`next_recipient`: account04/B18 and account04/B13 for integration with the stalled-core/proxy-gauge recursion; account02/B13 for reuse of the same actual-anchor code at the balanced support scale.
