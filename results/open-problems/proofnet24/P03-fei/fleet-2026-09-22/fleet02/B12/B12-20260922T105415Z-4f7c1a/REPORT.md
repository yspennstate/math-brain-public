# fleet02/B12 — signed pivotal trigger code with physical nonreuse

**Run:** `B12-20260922T105415Z-4f7c1a`  
**Programme:** `FEI-ALL-TEAM-20260922T095941Z`, Path C  
**Assignment:** fleet02/B12, **Signed trigger code**  
**Classification:** `ESSENTIAL_STEP_APPLIED / MARKED_PREFIX_CODE / PHYSICAL_NONREUSE / FULL_FEI_OPEN`  
**Execution:** `WITHOUT_VERIFIED_BRAIN`; authenticated repository controls and source-bound mathematics were read, but no separately authenticated native mathematical-brain receiver/context was used.  
**Full uniform-cube FEI:** **OPEN / NOT PROVED.**

## 0. Exact target, controls, and correction status

The active owner control is revision `2026-09-22.3`; the all-team FEI order supersedes the older seven-worker assignment while preserving its mathematical history. The exact B12 card asks:

> Construct a prefix-free physical restriction code for robust signed derivative rows whose trigger surplus is charged once. Retain the orientation mode and encode actual child choices; exploit common-source overlaps instead of counting trigger labels.

No pending correction was present in `CORRECTION_INBOX.json` at the final pre-write control check. The mandatory no-go corrections remain in force: no fixed-potential closure, no raw `U_4=O(J)`, no unweighted-L2 payment, no fixed-depth low-level KL payment, and no sign-free replacement of the co-pair law.

This report proves an exact prefix code for the **marked pivotal physical-block payload** and shows that its all-generation expected cost is at most `8/5` of the root folded influence under the newest sequential physical compiler. It also gives a genuine Boolean witness proving that the orientation bit cannot be dropped even for an exact subcube row. The report does **not** claim a standalone one-shot prefix code for the activity/nonactivity mark itself; that remaining distinction is quantified in Section 7.

## 1. Completed partner result consumed and applied

The assigned partner `fleet03/B12` completed:

* repository `yspennstate/math-open-problems`;
* introduction commit `c6e0f3df3424a27d4a05aec2460ecc52085ea1e3`;
* path `proofnet24/P03-fei/fleet-2026-09-22/fleet03/B12/fleet03-B12-20260922T104514Z/REPORT.md`;
* report blob `5be463a87c8ed06f29aca9f045a912d871e33157`.

I use two exact expressions from that report. For a relative-`eta` robust row `i`, with folded influence `q_i`, trigger set `F_i`, `r_i=|F_i|`, and physical elimination block

\[
A_i=\{i\}\cup F_i,
\]
its Theorem 3.1 gives

\[
\boxed{
D_{A_i}
:=\mathcal J(g)-\mathbb E_z\mathcal J(g_{A_i=z})
\ge [1+(1-2\eta)r_i]q_i.
}
\tag{1.1}
\]

Its pathwise theorem then gives, for an arbitrary adaptive descendant tree using these actual physical blocks,

\[
\boxed{
\sum_v\pi_vD_{A_v}
=\mathcal J(g_\varnothing)-\mathbb E\mathcal J(g_L)
\le\mathcal J(g_\varnothing).
}
\tag{1.2}
\]

This is the nonreuse bank below. A trigger shared by many rows is physically removed the first time a selected elimination block contains it; later descendants cannot charge the ancestor decrement again.

The partner also proves the robust activity/address entropy estimate

\[
\sum_v\pi_v h_2(q_v)\le C_\eta\mathcal J(g_\varnothing),
\tag{1.3}
\]
with `C_{1/16}=1.3494175371409616...`. I preserve that as the separate activity-mark bank; it is not folded into the prefix-code theorem below.

## 2. Other source-valid inputs retained

### Robust-row geometry

I retain the fleet04/B12 trigger theorem at immutable commit
`a1b2a93210fe7cc871cd10c5bbbf43b1b983a254`, path
`proofnet24/P03-fei/fleet-2026-09-21/fleet04/B12/20260922T094436Z-robust-row-codimension-staircase/REPORT.md`, blob
`06a4c1d51bb5d53d0783e567e6176511a68b1167`.
It proves, from one genuine Boolean derivative row rather than arbitrary rows,

\[
q_k\ge(1-2\eta)q_i\qquad(k\in F_i),
\tag{2.1}
\]
which is the source of (1.1).

### Ratio-critical trigger surplus

On a genuine all-block ratio-critical core of ratio `rho`, the earlier fleet04/B12 theorem at commit
`fdbfbcc1beed0db4cb6d13c8d61fd92db53a8113`, path
`proofnet24/P03-fei/fleet-2026-09-21/fleet04/B12/20260922T081051Z-terminal-trigger-surplus/REPORT.md`, proves

\[
\boxed{
\sum_{k\in F_i}[h_2(q_k)-\rho q_k]
\ge(1-\eta)[\rho+\mathfrak j'(q_i)]q_i.
}
\tag{2.2}
\]

Thus the robust row being encoded is a real terminal obstruction, not an abstract near-subcube row. The present code deliberately does **not** sum (2.2) over rows at one fixed state, because that would reuse overlapping trigger surplus. Instead it moves to the physical nonreuse bank (1.2).

### Signed co-pair warning

The exact co-pair source at commit `85ffa60db26997421d980b1f86c03d82259504ca`, path
`proofnet24/P03-fei/fleet-2026-09-21/fleet02/B13/20260922T093723Z-copair-terminal-tax/REPORT.md`, proves

\[
r_{ik}=\frac14p_{ik}+o_{ik},\qquad o_{ik}\ge0.
\tag{2.3}
\]

The opposite-sign mode cannot be discarded. Accordingly the code below carries the derivative orientation sign explicitly rather than pretending that near-subcube support makes the row sign-constant.

A fresh compatible fleet01/B19 result at commit `8ad7c177c7383231438c789b84298db4e0e030ab` independently shows that robust trigger overlap can be organized into a directed forest and paid from genuine pair mutual information. That theorem is compatible with the code below but is not needed for its proof; the present theorem uses the stronger physical decrement nonreuse (1.2) supplied by the assigned partner.

## 3. Setup: one robust signed derivative row

Work at one centered Boolean descendant `g`. Fix a physical coordinate `i`. On the quotient cube let

\[
E_i=\{y:D_i g(y)\ne0\},\qquad \mu(E_i)=q_i\le\frac12.
\]

Assume that `E_i` is relative-`eta` close to one actual coordinate subcube

\[
Q_i=\{y_{F_i}=a_i\},
\qquad r_i=|F_i|,
\]
with

\[
\varepsilon_i:=\mu(E_i\triangle Q_i)\le\eta q_i.
\tag{3.1}
\]

At the live threshold `eta=1/16`, every centered robust row has `r_i>=1`.

Let `Y` be the actual quotient-cube point, conditioned on the **marked pivotal event** `Y in E_i`. Let

\[
S_i(Y):=\operatorname{sgn}D_i g(Y)\in\{\pm1\}.
\]

Let `B_i in {+-1}` be the actual physical child choice for coordinate `i`; under a uniform physical restriction it is independent of `Y`. The payload to be decoded is

\[
\boxed{(B_i,\,Y_{F_i},\,S_i(Y)).}
\tag{3.2}
\]

The decoder is source-bound: from the current Boolean descendant and the deterministic robust-row selector it already knows the original coordinate `i`, the actual trigger set `F_i`, the proxy word `a_i`, and `r_i`. No trigger **label** is transmitted. The code transmits only the actual child choices and the signed orientation mode.

The key same-source fact is

\[
\theta_i:=\Pr(Y_{F_i}\ne a_i\mid Y\in E_i)
=\frac{\mu(E_i\cap Q_i^c)}{q_i}
\le\frac{\varepsilon_i}{q_i}
\le\eta.
\tag{3.3}
\]

This is where Boolean realizability enters: the same derivative support that defines the pivotal event also supplies the rare trigger exception.

## 4. Main local theorem: an exact prefix-free signed physical-child code

### Theorem 4.1 — `SIGNED-PIVOTAL-BLOCK-CODE-v1`

For every robust row satisfying (3.1), there is an instantaneous binary prefix code which, conditioned on `Y in E_i`, decodes the full payload (3.2) and has expected length

\[
\boxed{
\mathbb E[\ell_i\mid Y\in E_i]
\le
\begin{cases}
3,&r_i=1,\\
3+\eta r_i,&r_i\ge2.
\end{cases}}
\tag{4.1}
\]

At `eta=1/16`, its pivotal-mass weighted cost obeys

\[
\boxed{
q_i\,\mathbb E[\ell_i\mid E_i]
\le\frac85\,D_{A_i},
\qquad A_i=\{i\}\cup F_i.
}
\tag{4.2}
\]

### Construction

Use the following codebook.

* **Proxy child:** if `Y_{F_i}=a_i`, emit
  \[
  0\;|\;b(B_i)\;|\;b(S_i(Y)),
  \]
  exactly three bits.
* **Exceptional child:** if `Y_{F_i}\ne a_i`, emit
  \[
  1\;|\;b(B_i)\;|\;b(S_i(Y))\;|\;\operatorname{idx}_{F_i,a_i}(Y_{F_i}).
  \]
  Here `idx` is a fixed injective binary index of the `2^{r_i}-1` nonproxy trigger words. For `r_i=1` the exceptional trigger word is unique and the index is empty. For `r_i>=2`, use an `r_i`-bit index.

The first bit separates proxy from exceptional words. Within each branch the remaining lengths are fixed, so decoding is immediate. The decoded trigger word is `a_i` on the proxy branch and is the transmitted actual word on the exceptional branch; the row child and orientation bits are explicit.

### Prefix-free verification

There are four proxy words of length three. For `r=1` there are four exceptional words of the same length, so the Kraft sum is exactly `1`.

For `r>=2`, there are `4(2^r-1)` exceptional words of length `r+3`, hence

\[
\sum_w2^{-|w|}
=\frac4{2^3}
 +\frac{4(2^r-1)}{2^{r+3}}
=1-2^{-(r+1)}<1.
\tag{4.3}
\]

Thus the code is prefix-free for every physical codimension.

### Expected length

For `r=1`, the actual exceptional trigger word is forced once the proxy word is excluded, hence every codeword has length three.

For `r>=2`, (3.3) gives

\[
\mathbb E[\ell_i\mid E_i]
\le3+\theta_i r_i
\le3+\eta r_i,
\]
proving (4.1).

At the live `eta=1/16`, the partner theorem gives

\[
D_{A_i}\ge\left(1+\frac78r_i\right)q_i.
\tag{4.4}
\]

If `r_i=1`,

\[
3q_i=\frac85\cdot\frac{15}{8}q_i\le\frac85D_{A_i}.
\]

If `r_i>=2`,

\[
\frac85\left(1+\frac78r_i\right)-\left(3+\frac1{16}r_i\right)
=-\frac75+\frac{107}{80}r_i>0.
\tag{4.5}
\]

This proves (4.2). `QED`.

## 5. All-generation theorem: trigger payload is charged once

Run the assigned partner's adaptive sequential robust compiler. At every reached internal node `v`, choose one current relative-`1/16` robust row, use its actual elimination block

\[
A_v=\{i_v\}\cup F_v,
\]
recenter the genuine Boolean children by characters, and continue. Let `pi_v` be the reach probability. Attach the code of Theorem 4.1 to the marked pivotal payload at that node.

### Theorem 5.1 — `SIGNED-TRIGGER-PHYSICAL-NONREUSE-v1`

\[
\boxed{
\sum_v\pi_v q_v
\mathbb E[\ell_v\mid E_v]
\le\frac85\,\mathcal J(g_\varnothing).
}
\tag{5.1}
\]

### Proof

Apply (4.2) at every reached node and multiply by `pi_v`. Then use the partner's exact physical telescoping identity (1.2):

\[
\sum_v\pi_v q_vE[\ell_v\mid E_v]
\le\frac85\sum_v\pi_vD_{A_v}
\le\frac85\mathcal J(g_\varnothing).
\]

No trigger incidence is summed at a fixed state. If several rows share a trigger coordinate, the first actual elimination block containing that coordinate removes it from all descendants. Later codewords are charged only to later folded-influence decrement. `QED`.

This is stronger than a row-count or trigger-label estimate: the code cost is attached to the **actual surviving source path** and paid by a bank that literally disappears when the physical coordinates are queried.

## 6. Orientation is genuinely necessary: exact Boolean witness

The co-pair correction says orientation cannot be erased abstractly. There is also a direct Boolean witness.

Fix `r>=1`, let `Q={y_1=...=y_r=+1}`, and add one extra physical coordinate `z`. Define

\[
f_r(x_i,y,z)
:=z\times
\begin{cases}
x_i,&y\in Q,\\1,&y\notin Q.
\end{cases}
\tag{6.1}
\]

This is a genuine `\{\pm1\}`-valued Boolean function. Its additive derivative row satisfies exactly

\[
D_i f_r(y,z)=z\,1_Q(y).
\tag{6.2}
\]

Hence the derivative support is an **exact** coordinate subcube (`eta=0`, `q_i=2^{-r}`), but conditioned on pivotality the orientation sign is the independent balanced bit `z`. Therefore a support-only code which assumes a fixed row sign is not decodable even in the exact-subcube regime. One explicit orientation bit is not bookkeeping pessimism; it protects a realizable Boolean mode that the sign-free route would lose.

The executable checker archives this witness together with the exact Kraft and `8/5` inequalities.

## 7. Exact scope boundary: why the activity mark is separate

Theorem 5.1 is a prefix code for the **marked pivotal trigger payload**. It does not encode, by itself, whether a reached row is pivotal. This separation is essential rather than cosmetic.

A one-shot prefix code for a nondegenerate binary activity symbol has expected length at least one bit, regardless of how small its success probability is. Consequently one cannot assign a fresh one-shot activity code at every candidate robust row and hope to charge its cost by `q_i` when `q_i` is tiny. The exact `AND_n` family already makes this failure visible: every derivative row is an exact subcube row with `q_i=2^{-(n-1)}` while `J=n2^{-(n-1)}->0`; a unit overhead per candidate row is not influence-relative.

The partner result supplies the correct information-theoretic replacement:

\[
\sum_v\pi_v h_2(q_v)
\le1.3494175371409616\ldots\,J(root).
\tag{7.1}
\]

Combining (7.1) with (5.1) shows that the **information rate** of the activity indicators plus the complete signed marked payload is at most

\[
\boxed{
(1.3494175371409616\ldots+1.6)J
=2.9494175371409616\ldots\,J.
}
\tag{7.2}
\]

Standard block/arithmetic coding can approach (7.2) with one global prefix overhead across many independent copies, but that is not claimed here as a one-source physical stopping theorem. The first unpaid coding implication is therefore precise:

> merge the activity-information stream with the exact physical restriction recursion in a one-source decodable way, or prove that the existing selector-debit term already carries exactly this mark without an additional independent code.

This is narrower than the old ambient trigger-label gap: the actual trigger word, row child, orientation sign, and all descendant trigger reuse are now paid.

## 8. Relation to the true ratio-critical core

Assume the Path-C minimum-dimensional obstruction exists, with

\[
\rho=\mathcal F/\mathcal J>4.
\]

Then the all-block theorem makes it terminal at level `rho`, and every robust row satisfies the trigger-surplus demand (2.2). The present code applies without weakening this hypothesis. In particular:

1. source-valid terminal surplus identifies a robust row as a genuine obstruction;
2. its actual signed child payload has prefix cost bounded by (4.2);
3. the physical block is then retired, so its trigger coordinates and influence decrement cannot be charged again;
4. any new robust row appearing after recentering receives a fresh code paid only from the remaining descendant `J`.

Thus the robust branch no longer has an orientation/address/nonreuse obstruction at the marked-payload level. What remains before a full terminal-core exclusion is the activation-to-restriction transfer in Section 7 together with the complementary nonrobust/small-row branch. No statement `TC=O(J)`, `U_4=O(J)`, or `sum d_i=O(J)` is used.

## 9. Checker

`CHECKER.py` uses exact `Fraction` arithmetic. It verifies for `1<=r<=256`:

* the Kraft inequality for the explicit code;
* the sharp live constant `max ratio = 8/5`, attained at `r=1`;
* representative exact ratios at `r=1,2,3,8,32`;
* the balanced orientation signs of the genuine Boolean witness (6.1).

Executed output:

```text
eta 1/16
max_ratio 8/5 argmax_r 1
max_kraft 1 argmax_r 1
1 kraft 1 ratio 8/5
2 kraft 7/8 ratio 25/22
3 kraft 15/16 ratio 51/58
8 kraft 511/512 ratio 7/16
32 kraft 8589934591/8589934592 ratio 5/29
orientation_witness_signs [-1, 1]
RESULT PASS
```

The finite loop is only a regression certificate. The proofs (4.3)--(4.5) are analytic for arbitrary codimension.

## 10. Status

**FULL-PROBLEM CHANGE:** `OPEN -> OPEN`. No universal finite FEI constant was proved.

**MECHANISM CHANGE:** yes. The preceding fleet02/B12 line had moved through fixed-potential falsification and safe-direction barriers. Under the all-team reallocation this run changes to a source-exact physical code: actual trigger children are encoded only on the rare same-source exception, the orientation mode is retained explicitly, and overlapping triggers are paid by descendant folded-influence decrement rather than simultaneous incidence counting.

**New proved implication:** the signed marked robust-trigger payload across every generation of the sequential physical compiler costs at most `8J/5`, dimension-free and without reuse.

**Next unpaid implication:** integrate the activity mark with the one-source restriction recursion (or identify it exactly with the already paid selector-debit stream), then combine that completed robust branch with the nonrobust/small-row alternative on every genuine `rho>4` critical core.

Primary handoff recipient: `fleet04/B19`, as required by the assignment card.
