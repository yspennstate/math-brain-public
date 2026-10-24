# account03/B11 — two-sided support visibility and symmetric hidden-curvature decomposition

**Run:** `20260922T105133Z-account03-B11-fei`  
**Programme:** `FEI-ALL-TEAM-20260922T095941Z`, owner revision `2026-09-22.3`  
**Assignment:** `FEI-20260922-account03-B11`, Path C, nonrobust-row integrability dichotomy  
**Classification:** `ESSENTIAL_STEP_APPLIED / FULL_FEI_OPEN`  
**Execution:** `WITHOUT_VERIFIED_BRAIN`  
**Full uniform-cube FEI:** **OPEN / NOT PROVED.**

## 0. Control correction and source scope

The invocation prompt still named POS3, but the fresh owner control redirects all eighty workers to FEI and explicitly suspends new POS3 research. This report therefore executes the current account03/B11 FEI assignment.

The exact named partner is `account04/B11`. At the fresh compatibility check no completed FEI result from that partner was available; the newest accessible account04/B11 work was POS3 work predating the new FEI allocation and was not imported. The assignment explicitly permits proceeding from complete compatible snapshots without waiting.

The other-account results consumed substantively are:

1. `yspennstate/math-open-problems`, commit `fdbfbcc1beed0db4cb6d13c8d61fd92db53a8113`,  
   `proofnet24/P03-fei/fleet-2026-09-21/account04/B12/20260922T081051Z-terminal-trigger-surplus/REPORT.md`.  
   It proves that a relative-`1/16` near-subcube derivative row has an influence-relative trigger-surplus tax
   \[
   \sum_{k\in F_i}\sigma_k(4)\ge \frac{15}{16}[4+\mathfrak j'(q_i)]q_i.
   \]
   Thus the present run attacks the complementary nonrobust rows.

2. `yspennstate/math-open-problems`, commit `40d53b2d7f2c8b388a95d4abd82221321f6fcfcf`,  
   `proofnet24/P03-fei/fleet-2026-09-22/account04/B18/20260922T081002Z-visible-hidden-curvature-split/REPORT.md`.  
   For ordered distinct coordinates it proves
   \[
   2c_{i\leftarrow j}\le p_{ij},\qquad
   \kappa_{ij}=p_{ij}+4o_{ij}=2c_{i\leftarrow j}+\omega_{i\leftarrow j},
   \]
   with \(\omega_{i\leftarrow j}\ge0\), and on an \(F/J\)-critical core
   \[
   \sum_{i\ne j}(\rho+\mathfrak j'(q_i))c_{i\leftarrow j}
   \le \mathcal P-\operatorname{DTC}(X).
   \tag{0.1}
   \]

3. `yspennstate/math-open-problems`, commit `85ffa60db26997421d980b1f86c03d82259504ca`,  
   `proofnet24/P03-fei/fleet-2026-09-21/account02/B13/20260922T093723Z-copair-terminal-tax/REPORT.md`.  
   It proves \(\kappa_{ij}=4\Pr(i,j\in X)\) and warns that raw \(U_4=O(J)\) is false even under all-block terminality plus tensor primitivity. Nothing below assumes that false bound.

The current correction feed was also consumed: the fixed old potential, the `0.337/0.34` repairs, raw `U4=O(J)` and unweighted-L2 shortcuts are not live universal premises.

## 1. Setup

Character-center the Boolean function so every physical derivative-row support has
\[
q_i=\Pr(\eta_i=1)\le \frac12,
\]
where \(\eta_i\) is the pivotality indicator of coordinate \(i\) on the quotient cube.

For \(i\ne j\), write:

- \(p_{ij}=\Pr[\eta_i(y)\ne\eta_i(y+e_j)]\), the support-boundary probability of derivative row \(i\) in direction \(j\);
- \(c_{i\leftarrow j}\), the singleton posterior crossing of row \(i\) after physically revealing \(j\);
- \(o_{ij}\), the opposite-sign overlap of the additive derivative row across direction \(j\);
- \(\kappa_{ij}=p_{ij}+4o_{ij}\);
- \(\omega_{i\leftarrow j}=p_{ij}-2c_{i\leftarrow j}+4o_{ij}\ge0\).

The source theorem above supplies \(2c_{i\leftarrow j}\le p_{ij}\).

## 2. New Boolean two-face integrability lemma

### Lemma 2.1 — support boundary is symmetric

For every Boolean function and every distinct \(i,j\),
\[
\boxed{p_{ij}=p_{ji}.}
\tag{2.1}
\]

**Proof.** Fix all coordinates except \(i,j\), and write the four Boolean vertex values as \(a,b,c,d\). The support of the \(i\)-derivative changes across \(j\) exactly when
\[
[a\ne b]\oplus[c\ne d]=1.
\]
The support of the \(j\)-derivative changes across \(i\) exactly when
\[
[a\ne c]\oplus[b\ne d]=1.
\]
Both XORs equal the parity of the four vertex bits, so the two events coincide on every physical two-face. Averaging over the remaining coordinates proves (2.1). \(\square\)

Because mixed-derivative commutation gives \(\kappa_{ij}=\kappa_{ji}\), (2.1) also implies
\[
\boxed{o_{ij}=o_{ji}.}
\tag{2.2}
\]

This symmetry is unavailable if derivative rows are treated as unrelated arbitrary distributions; it uses their common Boolean source.

## 3. New exact two-sided hidden decomposition

Define for every unordered pair \(\{i,j\}\)
\[
\zeta_{ij}:=p_{ij}-c_{i\leftarrow j}-c_{j\leftarrow i}.
\tag{3.1}
\]
Since each crossing is at most \(p_{ij}/2\),
\[
\boxed{\zeta_{ij}\ge0.}
\tag{3.2}
\]
Define the signed common-source residue
\[
\boxed{\xi_{ij}:=\zeta_{ij}+4o_{ij}\ge0.}
\tag{3.3}
\]

### Theorem 3.1 — two-sided Hodge identity

For every unordered pair,
\[
\boxed{
\omega_{i\leftarrow j}
=\xi_{ij}+c_{j\leftarrow i}-c_{i\leftarrow j},
}
\tag{3.4}
\]
\[
\boxed{
\omega_{j\leftarrow i}
=\xi_{ij}+c_{i\leftarrow j}-c_{j\leftarrow i}.
}
\tag{3.5}
\]
Consequently,
\[
\boxed{
\frac{\omega_{i\leftarrow j}+\omega_{j\leftarrow i}}2=\xi_{ij}.
}
\tag{3.6}
\]

**Proof.** Substitute \(p_{ij}=\zeta_{ij}+c_{i\leftarrow j}+c_{j\leftarrow i}\) into the source definition
\(\omega_{i\leftarrow j}=p_{ij}-2c_{i\leftarrow j}+4o_{ij}\); (3.4) follows, and (3.5) is its reversal. Averaging cancels the antisymmetric crossing imbalance. \(\square\)

Thus the ordered hidden-curvature bank has an exact decomposition into:

1. a **symmetric co-square residue** \(\xi_{ij}\), forced by the fact that both rows come from the same Boolean two-face; and
2. an **antisymmetric physical-crossing transport** \(c_{j\leftarrow i}-c_{i\leftarrow j}\).

No second spectral moment is being declared \(O(J)\).

## 4. Quantitative row dichotomy

Set
\[
\beta_i:=\sum_{j\ne i}p_{ij},\qquad
C_i^{\rm in}:=\sum_{j\ne i}c_{i\leftarrow j},\qquad
C_i^{\rm out}:=\sum_{j\ne i}c_{j\leftarrow i},
\]
\[
V_i:=C_i^{\rm in}+C_i^{\rm out},\qquad
Z_i:=\sum_{j\ne i}\zeta_{ij}.
\]
Summing (3.1) gives the exact identity
\[
\boxed{\beta_i=V_i+Z_i.}
\tag{4.1}
\]

The classical edge-isoperimetric inequality on the \((n-1)\)-cube gives
\[
\boxed{\beta_i\ge2q_i\log_2\frac1{q_i}.}
\tag{4.2}
\]
For completeness, if \(A\subseteq\{0,1\}^m\) is split into sections of sizes \(a\ge b\), induction gives
\[
|\partial A|\ge
a\log_2\frac{2^{m-1}}a+
b\log_2\frac{2^{m-1}}b+(a-b).
\]
Writing \(s=a+b\) and \(p=a/s\), the excess over
\(s\log_2(2^m/s)\) is
\(s[h_2(p)-2(1-p)]\ge0\) by concavity of \(h_2\) on \([1/2,1]\).
Dividing by \(2^{m-1}\) yields (4.2).

### Corollary 4.1 — nonrobust-row physical/common-source dichotomy

For every row, and hence in particular for every row outside the account04/B12 relative-`1/16` robust regime, at least one of the following holds:
\[
\boxed{
V_i\ge q_i\log_2\frac1{q_i}
}
\tag{4.3}
\]
or
\[
\boxed{
Z_i\ge q_i\log_2\frac1{q_i}.
}
\tag{4.4}
\]

The first branch is genuine physical singleton-crossing currency: its terms are exactly the posterior-crossing refunds appearing in realizable restrictions. The second branch is a quantified common-source obstruction: at least that much support boundary remains invisible from **both** singleton posterior directions on the same Boolean two-faces.

This is the requested dichotomy. It is dimension-free, retains the rare-event logarithm, and does not use raw \(\sum d_i\).

## 5. Aggregate critical-core consequence

Now let the state be an \(F/J\)-critical core with \(\rho>4\). The consumed critical-core source gives \(q_i<1/6\) and
\[
\mathfrak j'(q_i)>\frac{16}{7}.
\tag{5.1}
\]
Hence every coefficient in (0.1) is \(>44/7\). With
\[
T:=\sum_{i\ne j}c_{i\leftarrow j},
\]
(0.1) yields
\[
\boxed{
T<\frac7{44}\,[\mathcal P-\operatorname{DTC}(X)].
}
\tag{5.2}
\]

For any chosen family \(N\) of rows, in particular the nonrobust rows,
each ordered crossing can enter
\(\sum_{i\in N}V_i\) at most twice, so
\[
\sum_{i\in N}V_i
<\frac7{22}\,[\mathcal P-\operatorname{DTC}(X)].
\tag{5.3}
\]
Therefore (4.1) gives the new aggregate lower bound
\[
\boxed{
\sum_{i\in N}Z_i
>
\sum_{i\in N}\beta_i
-\frac7{22}[\mathcal P-\operatorname{DTC}(X)]
}
\tag{5.4}
\]
and, using (4.2),
\[
\boxed{
\sum_{i\in N}Z_i
>
2\sum_{i\in N}q_i\log_2\frac1{q_i}
-\frac7{22}[\mathcal P-\operatorname{DTC}(X)].
}
\tag{5.5}
\]

Equivalently, if
\[
\sum_{i\in N}\beta_i
\ge \frac7{11}[\mathcal P-\operatorname{DTC}(X)],
\tag{5.6}
\]
then
\[
\boxed{
\sum_{i\in N}Z_i>\frac12\sum_{i\in N}\beta_i.
}
\tag{5.7}
\]
Thus a large nonrobust boundary load cannot hide in independent-looking row distributions: after the globally paid physical crossing budget is exhausted, at least half of it is forced into the common-source two-face residual.

## 6. New exact decomposition of the old hidden bank \(U_4\)

Put
\[
w_i:=4+\mathfrak j'(q_i).
\]
The old hidden bank is
\[
U_4=\sum_{i\ne j}w_i\,\omega_{i\leftarrow j}.
\]
Grouping (3.4)-(3.5) by unordered pairs gives the exact identity
\[
\boxed{
U_4=
\sum_{i<j}(w_i+w_j)\xi_{ij}
+
\sum_{i<j}(w_i-w_j)
(c_{j\leftarrow i}-c_{i\leftarrow j}).
}
\tag{6.1}
\]

The derivative formula
\[
\mathfrak j'(q)=
\frac{1-x^2}{x\ln2}\log\frac{1+x}{1-x},
\qquad x=\sqrt{\frac q{1-q}},
\]
also gives the elementary bound
\[
0\le\mathfrak j'(q)\le\frac2{\ln2}.
\tag{6.2}
\]
Indeed
\[
\frac{1-x^2}{x}\log\frac{1+x}{1-x}
=
2(1-x^2)\sum_{r\ge0}\frac{x^{2r}}{2r+1}
\le2.
\]
Hence \(|w_i-w_j|\le2/\ln2\), and (5.2) implies
\[
\boxed{
\left|
U_4-\sum_{i<j}(w_i+w_j)\xi_{ij}
\right|
<
\frac7{22\ln2}
[\mathcal P-\operatorname{DTC}(X)].
}
\tag{6.3}
\]

So the already-isolated hidden-curvature obstruction is, up to a dimension-free **already-visible crossing correction**, exactly a nonnegative symmetric common-source co-square bank. This is stronger structural information than the ordered decomposition \(\kappa=2c+\omega\).

It does **not** revive the false claim \(U_4=O(J)\). On a disjoint tensor cross-factor pair, the consumed co-pair source has \(p_{ij}=0\), both crossings zero and \(o_{ij}=q_iq_j\), so
\[
\xi_{ij}=4q_iq_j.
\]
The tensor-orientation baseline is therefore still explicitly present in the symmetric bank rather than accidentally discarded.

## 7. Integration with the robust/nonrobust split

The account04/B12 theorem already handles a relative-`1/16` robust row by an influence-relative trigger-surplus demand. For the complementary nonrobust set \(N\), Corollary 4.1 and (5.5) give the new alternative:

- enough of its support boundary is visible to actual physical singleton restrictions and is charged to the existing crossing budget; or
- a quantitatively large symmetric same-two-face residual survives.

Thus **every derivative row now enters one of two structurally different currencies**: robust trigger surplus, or nonrobust physical/common-source support load. The remaining issue is no longer an uncontrolled raw second factorial moment.

## 8. Exact finite regression check

`CHECKER.py` uses exact `Fraction` arithmetic. It exhausts all 16 Boolean labelings of a physical two-face and all character-centered Boolean functions in dimensions 2 and 3. It verifies:

- pointwise/exact \(p_{ij}=p_{ji}\);
- both \(2c\le p\) inequalities;
- \(\zeta_{ij}\ge0\);
- \(\kappa_{ij}=\kappa_{ji}=p_{ij}+4o_{ij}\);
- \(o_{ij}=o_{ji}\);
- (3.4)-(3.6).

Executed output:

```text
two_face_labelings 16
centered_functions 272
unordered_pair_checks 784
RESULT PASS
```

Checker SHA-256:
`bb3e6872f4f72bd8fda76f07a5f226186e5129acfde681a927ab9ccd8a51b6bc`.

The checker is only regression evidence; the statements above are proved analytically.

## 9. Status and next unpaid implication

**Outcome:** `ESSENTIAL_STEP_APPLIED / FULL_FEI_OPEN`.

The exact B11 target has advanced: the nonrobust-row branch now has a source-valid dimension-free dichotomy, and the previously ordered hidden bank has an exact symmetric/antisymmetric decomposition. No raw-\(U_4\) or raw-depth payment is assumed.

The next unpaid implication is:

> **SYMMETRIC-RESIDUE RENORMALIZATION.** On a true ratio-critical all-block core, subtract or pay the tensor-orientation baseline inside
> \[
> \sum_{i<j}(w_i+w_j)\xi_{ij},
> \]
> using the co-pair spectral identities and the nonrobust hypothesis, so that either the remaining common-source residue is paid by a nonreused physical entropy/KL decrement or the state reduces to the already-classified tensor/near-subcube structures.

A natural next mechanism is to combine
\(\kappa_{ij}=4\Pr(i,j\in X)\) with the co-pair mutual-information inequality, while keeping the \(4q_iq_j\) tensor baseline explicit. That is materially different from trying to prove the known-false raw \(U_4=O(J)\).
