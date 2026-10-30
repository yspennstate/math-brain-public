# fleet02/B11 — entropy-safe near-subcube stability at codimension-dependent tolerance

**Run:** `20260922T104712Z-b11-fei-r18`  
**Programme:** `FEI-ALL-TEAM-20260922T095941Z`  
**Assignment:** fleet02/B11, Path C, *Entropy-safe near-subcube stability*  
**Classification:** `ESSENTIAL_STEP_APPLIED / FULL_FEI_OPEN`  
**Execution:** `WITHOUT_VERIFIED_BRAIN`  
**Full uniform-cube FEI:** **OPEN / NOT PROVED.**

## 0. Current state, corrections, and exact scope

This run consumed control revision `2026-09-22.3` and state revision `FEI-20260922T1000Z-v1`. The current programme has suspended earlier POS3, installation and benchmark work. The relevant correction status is preserved literally:

* the fixed-relative near-subcube tolerance shortcut is **false** as a universal entropy-payment premise;
* raw hidden curvature `U_4=O(J)` under all-block terminality/primitivity is **refuted**;
* unweighted-L2 replacement of the rare-event logarithmic credit is **refuted**;
* fixed-depth/low-level KL extraction is **refuted** on recursive ternary majority;
* no fixed all-gate potential is used here.

The result below therefore keeps a tolerance that decays with the subcube codimension and works only with genuine physical coordinates.

The exact source inputs used are:

1. **C.1 near-support block theorem and elimination identity.**  
   Repository `yspennstate/math-open-problems`, commit `3739dd232ab781de9e899a5caf364a7144cf5bef`, path `proofnet24/P03-fei/fleet-2026-09-21/fleet02/interactive/20260921T192650Z-joint-fei-subcube-peeling/ADDENDUM.md`, Sections B--C. It proves the punctured-cube/log-Sobolev restriction machinery, the coefficient-12 block theorem under total support error `e<=q/(16r)`, and the sign-independent residual-pivot bound after the control block is exposed.
2. **Robust-row posterior crossing.**  
   Repository `yspennstate/math-open-problems`, commit `fdbfbcc1beed0db4cb6d13c8d61fd92db53a8113`, path `proofnet24/P03-fei/fleet-2026-09-21/fleet04/B12/20260922T081051Z-terminal-trigger-surplus/REPORT.md`, Lemma 2.1 / Theorem 3.1. It gives the exact trigger crossing lower bound `c_i(F)>=q_i-epsilon` and the terminal trigger-surplus inequality.
3. **Pairwise trigger transfer / codimension staircase.**  
   Repository `yspennstate/math-open-problems`, commit `a1b2a93210fe7cc871cd10c5bbbf43b1b983a254`, path `proofnet24/P03-fei/fleet-2026-09-21/fleet04/B12/20260922T094436Z-robust-row-codimension-staircase/REPORT.md`, Sections 2--4. It proves the Boolean-square identity `p_ik=p_ki<=2q_k` and hence influence on every genuine trigger.
4. **Fresh pathwise refund retention.**  
   Repository `yspennstate/math-open-problems`, commit `c6e0f3df3424a27d4a05aec2460ecc52085ea1e3`, path `proofnet24/P03-fei/fleet-2026-09-22/fleet03/B12/fleet03-B12-20260922T104514Z/REPORT.md`, Sections 1--4. This is the named OTHER-account result applied directly below. It proves
   \[
   D_A=I_A+C_A,
   \qquad
   \Delta_A\mathcal P=L_A+W_A+R_A,
   \]
   with `C_A,R_A>=0`, and exact adaptive-tree telescoping after child recentering.
5. **All-block terminal core.**  
   Repository `yspennstate/math-open-problems`, commit `85ffa60db26997421d980b1f86c03d82259504ca`, path `proofnet24/P03-fei/fleet-2026-09-21/fleet02/B13/20260922T075416Z-all-block-terminal-core/REPORT.md`, Sections 2--4. This supplies the candidate-independent `F/J` critical-core setting and the exact folded restriction drift.

The assignment names `fleet03/B11` as partner. At the last pre-write source refresh, no completed FEI artifact for `fleet03/B11` existed under the current all-team FEI root, so no unfinished partner result is cited or treated as a premise. The fresh compatible fleet03/B12 pathwise-refund theorem above is used instead, without waiting.

## 1. Setup

Work in a centered character gauge. Let

\[
f:\mathbb F_2^n\to\{-1,+1\}
\]

be Boolean and fix a physical pivot coordinate `x`. Write

\[
g(y)=D_xf(y)\in\{0,\pm1\},
\qquad
E=\{y:g(y)\ne0\},
\qquad
p=\mu(E)=q_x\le\frac12.
\]

No sign condition is imposed on `g`; only its genuine sensitivity support `E` is compared with a coordinate subcube.

Let `Z` be `r>=1` other physical coordinates and let

\[
Q=\{y_Z=a\},
\qquad q:=\mu(Q)=2^{-r},
\qquad e:=\mu(E\triangle Q).
\]

Put

\[
I_Z:=\sum_{k\in Z}q_k.
\]

Assume

\[
\boxed{I_Z\le rp}
\tag{1.1}
\]

and the codimension-dependent support accuracy

\[
\boxed{e\le\frac{q}{8r}.}
\tag{1.2}
\]

Condition (1.1) is automatic when `x` is a maximum-influence coordinate in the centered gauge. Condition (1.2), unlike the retired fixed-relative shortcut, becomes stricter with codimension.

The new result doubles the symmetric tolerance in the earlier coefficient-12 theorem from `q/(16r)` to `q/(8r)`, then compiles the control step with deletion of the pivot itself while retaining the full folded refund.

## 2. New theorem: coefficient 12 at the wider `q/(8r)` tolerance

### Theorem 2.1 — entropy-safe physical control block

Under (1.1)--(1.2), restricting the genuine physical control block `Z` satisfies

\[
\boxed{
\Delta_ZH
:=H(f)-\mathbb E_zH(f_{Z=z})
\le12I_Z.
}
\tag{2.1}
\]

This is analytic in arbitrary dimension and permits arbitrary signs of the derivative row.

### Proof

The support-density difference gives

\[
|p-q|\le e.
\tag{2.2}
\]

The exact Boolean boundary decomposition used in source C.1 has two pieces: edges incident to the distinguished subcube vertex and the punctured internal control boundary `B_int`. It gives

\[
I_Z\ge rq-re
\tag{2.3}
\]

and, using (1.1) and `p<=q+e`,

\[
B_{\rm int}
\le r(q+e)-(rq-re)
=2re.
\tag{2.4}
\]

By (1.2),

\[
\boxed{B_{\rm int}\le q/4,}
\qquad
\boxed{I_Z\ge q(r-1/8).}
\tag{2.5}
\]

Let `S_Z` denote the spectral intersection with the control block. The punctured-cube variance argument from the cited source is performed on the actual signed Boolean restrictions `f_{Z=z}` and yields

\[
\theta:=\Pr(S_Z\ne\varnothing)
\le2B_{\rm int}+4q
\le\frac92q.
\tag{2.6}
\]

The full-cube log-Sobolev restriction-mixture estimate, again for the actual signed restrictions, gives

\[
\boxed{
\Delta_ZH
\le H(S_Z)+\frac2{\ln2}I_Z.
}
\tag{2.7}
\]

It remains only to improve the scalar estimate enough to absorb the larger error.

For `r=1,2,3`, the trivial bound `H(S_Z)<=r` and (2.5) give respectively

\[
1<\frac{63}{16}=9q(r-1/8),
\]
\[
2<\frac{135}{32}=9q(r-1/8),
\]
\[
3<\frac{207}{64}=9q(r-1/8).
\]

Hence `H(S_Z)<9I_Z` in these cases.

Now take `r>=4`. Then `(9/2)q<=1-q`, so the maximum entropy with nonzero spectral mass at most `(9/2)q` is attained by spreading that mass uniformly over the `2^r-1` nonempty control subsets. Therefore

\[
H(S_Z)
\le h_2(9q/2)+\frac92q\log_2(2^r-1).
\tag{2.8}
\]

Using `h_2(t)<=t\log_2(e/t)` and `\log_2(2^r-1)<r`,

\[
H(S_Z)
<\frac92q\left(2r+\log_2\frac{2e}{9}\right).
\tag{2.9}
\]

The elementary bound `e<3` gives `2e/9<2/3<2^{-1/2}`; hence the logarithm in (2.9) is below `-1/2`. Thus

\[
H(S_Z)
<9rq-\frac94q
<9q(r-1/8)
\le9I_Z.
\tag{2.10}
\]

Finally `\ln2>2/3`, so `2/\ln2<3`. Combining (2.7) and (2.10) gives

\[
\Delta_ZH<9I_Z+3I_Z=12I_Z.
\]

This proves (2.1). `QED`

### Scope comparison

This is **not** a fixed-relative theorem. The tolerance is `e/q<=1/(8r)`. The old fixed-relative `1/16` trigger-tax theorem remains useful for posterior crossing, but it cannot be substituted for (1.2) at large `r` when a Shannon block decrement is required.

The theorem is also complementary to the source's asymmetric result allowing much larger false-negative mass and smaller outside false-positive mass. Neither statement subsumes the other.

## 3. Influence-relative reformulation and exact trigger refund

From `e<=q/(8r)` and `q<=p+e`,

\[
8re\le q\le p+e,
\]
so

\[
\boxed{
e\le\frac{p}{8r-1}.}
\tag{3.1}
\]

Thus the accuracy is explicitly influence-relative, with a tolerance that decays as `1/r`.

The fleet04/B12 posterior-polarization identity applies without discarding signs:

\[
c_x(Z)\ge p-e.
\]
Consequently

\[
\boxed{
c_x(Z)\ge\gamma_rp,
\qquad
\gamma_r:=1-\frac1{8r-1}.}
\tag{3.2}
\]

At the same tolerance, the robust trigger-surplus theorem can be invoked with

\[
\eta_r:=\frac1{8r-1}<\frac12,
\]
so every all-block terminal core at level `K` obeys

\[
\boxed{
\sum_{k\in Z}\bigl(h_2(q_k)-Kq_k\bigr)
\ge
\gamma_r\,[K+\mathfrak j'(p)]p.
}
\tag{3.3}
\]

This is an exact application of the named other-account robust-row formula. It also makes the distinction requested by the assignment explicit: (3.3) is a trigger tax; (2.1) is the stronger Shannon block decrement and needs the codimension-dependent tolerance.

## 4. New theorem: delete the whole row with the same coefficient 12

The control block almost eliminates the pivot row. The sign-independent source identity gives

\[
\boxed{
\mathbb E_z q_x(f_{Z=z})\le e
}
\tag{4.1}
\]

and the concave single-coordinate restriction cap gives

\[
\boxed{
\mathbb E_z\Delta_xH(f_{Z=z})\le\Psi(e),
}
\tag{4.2}
\]

where

\[
\Psi(t)=h_2(t)+1-h_2\!\left(\frac12+\sqrt{t(1-t)}\right)
\le t\left(\log_2\frac1t+\frac3{\ln2}\right).
\tag{4.3}
\]

Under (1.2) this residual cost is small compared with the original pivot influence.

### Lemma 4.1 — residual pivot entropy costs at most `3p/2`

\[
\boxed{\Psi(e)\le\frac32p.}
\tag{4.4}
\]

**Proof.**  The right side of (4.3) is increasing on `(0,1]`. Hence

\[
\Psi(e)
\le\frac{q}{8r}
\left(r+\log_2(8r)+\frac3{\ln2}\right).
\]
Use `\log_2r<=r`, `3/\ln2<9/2`, and `p>=q-e>=q(1-1/(8r))` to get

\[
\frac{\Psi(e)}p
\le
\frac{2r+15/2}{8r-1}
\le\frac32,
\]
where the last inequality is equivalent to `9<=10r`. `QED`

Now reveal `Z` and then reveal `x`; this is exactly the physical block `A=Z\cup\{x\}`.

### Theorem 4.2 — full near-subcube row elimination

\[
\boxed{
\Delta_AH
\le12(I_Z+p)
=12I_A.
}
\tag{4.5}
\]

Indeed, restriction entropy telescopes and Theorem 2.1 plus Lemma 4.1 give

\[
\Delta_AH
=\Delta_ZH+\mathbb E_z\Delta_xH(f_{Z=z})
\le12I_Z+\frac32p
\le12(I_Z+p).
\]

The block consists only of the original pivot and its original physical controls. The derivative row is gone after the step; no abstract selector coordinate or affine rebasing is introduced.

## 5. Full folded refund and pathwise nonreuse

Apply the fresh fleet03/B12 pathwise-refund identity to the same elimination block `A`.

Write

\[
D_A=I_A+C_A,
\]

where `C_A` is the total folded survivor crossing, and write the exact phase decrement as

\[
\Delta_A\mathcal P=L_A+W_A+R_A,
\qquad
L_A,W_A,R_A\ge0.
\]

Theorem 4.2 therefore gives the stronger corrected-entropy estimate

\[
\begin{aligned}
\Delta_A\mathcal F
&=\Delta_AH-\Delta_A\mathcal P\\
&\le12I_A-L_A-W_A-R_A\\
&=12D_A-\boxed{\bigl(12C_A+L_A+W_A+R_A\bigr)}.
\end{aligned}
\tag{5.1}
\]

Thus the full folded refund is not thrown away. The parent block pays its entropy from the actual physical loss, while survivor crossing, deleted phase, first-order phase refund and reflected-curvature remainder remain as explicit nonnegative credit.

This immediately compiles along a genuine adaptive restriction tree. At each reached descendant, if a row satisfying (1.1)--(1.2) exists, choose one and query its full physical elimination block `A_v={x_v}\cup Z_v`; recenter children by characters and repeat. If `pi_v` is the reach probability, then the fresh fleet03/B12 exact drift telescope gives

\[
\boxed{
\sum_v\pi_v\Delta_{A_v}H
\le12\sum_v\pi_v I_{A_v}
\le12\sum_v\pi_vD_{A_v}
=12\bigl(J(f)-\mathbb EJ(f_L)\bigr)
\le12J(f).
}
\tag{5.2}
\]

Moreover, summing (5.1) retains the refunds across generations:

\[
\boxed{
\mathcal F(f)-\mathbb E\mathcal F(f_L)
\le
12\bigl(J(f)-\mathbb EJ(f_L)\bigr)
-
\sum_v\pi_v\bigl(12C_v+L_v+W_v+R_v\bigr).
}
\tag{5.3}
\]

No trigger or crossing credit can be reused after recentering, because each term in (5.3) belongs to the exact one-step decrement at the node where it is created.

This directly consumes and strengthens the fresh fleet03/B12 sequential-nonreuse mechanism on the present entropy-safe subcube branch.

## 6. What this changes, and the first unpaid implication

### Before

The strongest symmetric coefficient-12 block theorem available in the cited source required

\[
e\le\frac{q}{16r}.
\]
A separate fixed-relative robust theorem supplied a strong trigger tax, but the fixed-relative tolerance could not be promoted to a Shannon block decrement.

### After

The symmetric entropy-safe region is widened by a factor of two:

\[
\boxed{e\le\frac{q}{8r}.}
\]
Within this region one can remove the **entire** pivot-plus-controls block at total Shannon cost at most `12` times the actual parent influence of those coordinates, and the exact folded/phase refunds survive pathwise.

Therefore any centered ratio-critical obstruction that survives the corresponding adaptive compiler must satisfy, for every selected maximum row and every codimension-`r` coordinate subcube proxy,

\[
\boxed{\mu(E_x\triangle Q)>\frac{2^{-r}}{8r},}
\tag{6.1}
\]

unless it is already caught by a different source-valid asymmetric paid branch.

The first genuinely unpaid implication is now the nonrobust residual:

> **NONROBUST ROW DICHOTOMY AT THE `q/(8r)` FRONTIER.** Show that a maximum derivative row which is separated from every coordinate subcube by more than `2^{-r}/(8r)` yields a physical entropy decrement / common-source mixed-derivative obstruction that is influence-relative and nonreusing; or construct a genuine Boolean family refuting that proposed dichotomy.

This is precisely the neighboring `fleet03/B11` target. No completed current-FEI partner result was available during this run, so this report does not pretend the residual is solved.

## 7. Acceptance check and status

The assignment acceptance condition is met at the following exact scope:

* **analytic entropy bound:** Theorem 2.1 and the stronger full-row Theorem 4.2;
* **influence-relative error:** `e<=p/(8r-1)` follows from the source-geometric hypothesis;
* **codimension-dependent tolerance:** `e<=2^{-r}/(8r)`, not a fixed relative constant;
* **original-coordinate decoding:** the queried block is the genuine physical `Z` or `Z\cup{x}`;
* **derivative signs retained:** the proof uses actual signed Boolean restrictions, never replaces the row by an unsigned artificial source;
* **full folded refund retained:** (5.1)--(5.3) keep `C,L,W,R` explicitly;
* **no retired mechanism revived:** no fixed potential, raw-U4 payment, unweighted-L2 substitute, or fixed-depth KL compression is used.

No finite census or floating-point computation is used in the proof. There is therefore no executable certificate on which the theorem depends.

**Outcome:** `ESSENTIAL_STEP_APPLIED / FULL_FEI_OPEN`.
