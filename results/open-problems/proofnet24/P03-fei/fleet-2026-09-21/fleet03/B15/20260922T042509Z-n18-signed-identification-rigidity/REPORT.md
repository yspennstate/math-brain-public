# fleet03/B15 — one-step signed-identification rigidity of the near-extremal n=18 FEI gate

**Run:** `20260922T042509Z-fleet03-B15-r11`  
**Outcome:** `ESSENTIAL_STEP_APPLIED / EXACT_ADVERSARY_FAMILY_REFUTED`  
**Full uniform-cube FEI:** **OPEN / NOT PROVED**.  
**Execution:** `WITHOUT_VERIFIED_BRAIN`.

## 1. Live candidate and decisive implication

The later natural-language owner order supersedes the older packet-only B15 assignment and asks every FEI worker to converge on the all-gate formulation. The current Campaign-B lead candidate, from fleet03/B18, is

\[
\texttt{LIMIT-PRIME-GATE-LIFT-v1},\qquad C_*=6.5218512,
\]
\[
\Gamma_*(p)=\Gamma_{RO}(p)+0.2682048\,p(1-p),
\]
with the still-unpaid universal implication
\[
D_{\Gamma_*}(P;p)\ge0
\tag{1.1}
\]
for every finite composition-prime Boolean gate \(P\) and every interior product-bias vector \(p\). If (1.1) were proved, the exact composition cocycle plus the all-gate equivalence would yield full FEI with finite constant \(C_*\).

This run does **not** prove (1.1). Instead it attacks a concrete adversarial escape from the source-valid, nearly saturating balanced \(n=18\) prime gate: can one identify two of its inputs (allowing a sign flip) and thereby obtain a smaller balanced gate with a larger amplified ratio \(H/(I-1)\), possibly crossing \(C_*\)?

The answer for every one-step signed identification is **no**, rigorously.

## 2. Named other-account result consumed

The compatible completed peer artifact used substantively is

`proofnet24/P03-fei/fleet-2026-09-21/fleet01/B12/20260922T011847Z-prime-n18-gate/REPORT.md`, blob `9ab98c0e82f7cf0f34eac98923df23b7b160670b`.

It supplies the exact source-valid balanced monotone composition-prime gate \(F\) on 18 variables, its truth-table SHA-256
```
f8a7bb2c738d86368305111633376b1a3a83d8ee1f1abcc9a37d841b0f9c7839
```
and the certified data
\[
I(F)=\frac{261}{128},
\]
\[
6.776605309005978082519790221891882314787235038
\le H(F)\le
6.776605309005978082519790221891882314787235039.
\tag{2.1}
\]

The gate has nine core variables \(x_0,\ldots,x_8\) and nine host variables \(y_0,\ldots,y_8\). Host \(y_j\) controls one disjoint two-cell core pair \(P_j=\{a_j,b_j\}\), where
\[
(78,79),(113,121),(228,484),(170,186),(149,151),
(338,466),(284,316),(291,295),(393,457).
\tag{2.2}
\]
Each pair is a Hamming edge. Its direction list is
\[
(r_0,\ldots,r_8)=(0,3,8,4,1,7,5,2,6),
\tag{2.3}
\]
a permutation of all nine core coordinates.

I also use fleet03/B18's current candidate version `LIMIT-PRIME-GATE-LIFT-v1` only for the target cap \(C_*=6.5218512\); the mathematical source data in (2.1)--(2.3) come from the named other-account artifact above.

## 3. Exact family tested

For every unordered pair of distinct original coordinates \(a<b\) and each \(s\in\{0,1\}\), form the 17-variable signed identification
\[
G_{a,b,s}:\quad X_b=X_a\oplus s,
\tag{3.1}
\]
leaving the other 16 original coordinates free. There are exactly
\[
2\binom{18}{2}=306
\tag{3.2}
\]
such one-step signed identifications.

The checker reconstructs the source truth table and requires the published SHA-256 before doing anything else. It then evaluates all 306 maps exactly. Exactly **90** are balanced:

* all \(2\binom92=72\) host-host identifications \(y_\ell=y_j\oplus s\);
* exactly 18 core-host identifications, namely
  \[
  y_j=x_{r_j}\oplus s,\qquad j=0,\ldots,8,\quad s=0,1.
  \tag{3.3}
  \]

Every other core-host identification and every core-core identification is unbalanced. The balance classification has a direct explanation. Outside the 18 exceptional cells, hosts do nothing and the signed core sum is zero. On \(P_j=\{a_j,a_j\oplus e_{r_j}\}\), identifying \(y_j\) with \(x_r\oplus s\) gives two opposite values exactly when \(r=r_j\); otherwise it gives equal values and leaves a nonzero mean.

The checker also examines all 36 one-coordinate fixings of \(F\); **none is balanced**.

## 4. Exact influence rigidity

For every one of the 90 balanced signed identifications the exact integer edge count gives
\[
\boxed{I(G_{a,b,s})=\frac{261}{128}=I(F).}
\tag{4.1}
\]

For host-host identifications this also has a short Fourier explanation. Write the host-\(j\) singleton Fourier block as
\[
A_j(S)=2^{-9}\bigl(\chi_S(a_j)+\chi_S(b_j)\bigr).
\tag{4.2}
\]
After \(y_\ell=y_j\oplus s\), the merged block is
\[
A_j(S)+(-1)^s A_\ell(S).
\tag{4.3}
\]
The degree-weighted cross term vanishes. The unweighted part vanishes because the two physical supports are disjoint. The \(|S|\)-weighted part is a sum of derivative inner products, and these can be nonzero only if a cell in \(P_j\) is Hamming-adjacent to a cell in \(P_\ell\). The source geometry has no such cross-pair Hamming edges: the only distance-one edges inside the 18 exceptional cells are the nine source pairs themselves. Hence merging two different host channels changes neither total Fourier mass nor total influence.

The core-host cases in (3.3) are also checked by exact edge counts; all have the same value (4.1).

## 5. Exact entropy loss for every host-host merge

Because \(b_j=a_j\oplus e_{r_j}\),
\[
A_j(S)=
\begin{cases}
2^{-8}\chi_S(a_j),&S_{r_j}=0,\\
0,&S_{r_j}=1.
\end{cases}
\tag{5.1}
\]
Thus each original singleton-host block has 256 atoms of squared mass \(2^{-16}\), and two separate blocks contribute
\[
2\cdot256\cdot2^{-16}\cdot16=\frac18
\tag{5.2}
\]
to spectral entropy.

For \(j\ne\ell\), the direction coordinates \(r_j,r_\ell\) are distinct. Among the 512 core characters, 128 have only \(A_j\) nonzero, 128 have only \(A_\ell\) nonzero, 128 have neither nonzero, and 128 have both nonzero. For the last 128 characters, the two phases align on exactly 64 and cancel on exactly 64. The reason is source-exact: for every \(j\ne\ell\), \(a_j\oplus a_\ell\) has at least one nonzero coordinate outside \(\{r_j,r_\ell\}\); varying that free character bit flips the relative phase. The checker verifies this geometry for all 36 host-pair choices.

Therefore the merged block has 256 atoms of mass \(2^{-16}\), 64 atoms of mass \(2^{-14}\), and the rest zero. Its entropy is exactly
\[
256\,2^{-16}\,16+64\,2^{-14}\,14
=\frac{15}{128}.
\tag{5.3}
\]
Comparing (5.2) and (5.3),
\[
\boxed{H(G_{a,b,s})=H(F)-\frac1{128}}
\tag{5.4}
\]
for **every** host-host signed identification, independently of the chosen pair and of \(s\).

## 6. The remaining 18 balanced identifications are strictly worse

The exact Walsh scan finds only two spectra among the 18 balanced core-host identifications, one for each sign \(s\). Exact-rational 48-term atanh logarithm enclosures with an explicit positive remainder bound give
\[
H(G_{x_{r_j},y_j,0})
<6.750822190391666857746938007852,
\tag{6.1}
\]
\[
H(G_{x_{r_j},y_j,1})
<6.750298848902807597755032765284.
\tag{6.2}
\]
Both are far below the lower endpoint of
\[
H(F)-\frac1{128}
\ge6.768792809005978082519790221891882314787235038.
\tag{6.3}
\]
Since all balanced identifications have the same influence (4.1), the host-host merges are the entropy-maximizing type within this one-step family.

## 7. Certified maximum and consequence for the live candidate

Combining (2.1), (4.1), and (5.4), every balanced one-step signed identification satisfies
\[
\frac{H(G)}{I(G)-1}
\le
\frac{H(F)_{\rm upper}-1/128}{133/128}.
\]
Hence
\[
\boxed{
\frac{H(G)}{I(G)-1}
<6.514326913930565372650625175956097266.
}
\tag{7.1}
\]
Against the current candidate center \(C_*=6.5218512\), the certified safety gap is
\[
\boxed{
C_*-\sup_{\rm balanced\ one\text{-}step\ signed\ identifications}
\frac{H}{I-1}
>0.007524286069434627349374824043902734.
}
\tag{7.2}
\]

Thus the explicit adversarial claim that the source \(n=18\) near-extremal gate can be converted into a stronger balanced obstruction to `LIMIT-PRIME-GATE-LIFT-v1` by one signed identification of two original inputs is **REFUTED** for all 306 possible identifications. Coordinate fixing does not give a balanced child either.

This is a genuine rigidity theorem about the actual source gate, not a generic entropy monotonicity claim. In general variable identification need not decrease spectral entropy or preserve influence.

## 8. What remains unpaid

This does **not** prove the universal implication (1.1). It treats only the balanced-uniform slice of one exact source gate under one-step signed identifications.

The replacement obligation is therefore materially different:

1. test genuinely **biased** product points of composition-prime gates against the same \(\Gamma_*\);
2. alter the exceptional support or host group sizes rather than merely merging existing coordinates;
3. or prove a source-valid rigidity/compactness principle that turns the near-extremal shared-core geometry into a universal prime-gate bound.

The most useful next recipient is `fleet03/B18`, the Campaign-B lead. A secondary recipient is `fleet01/B12`, whose exact source gate is consumed here: this result shows its obstruction is locally rigid under every one-step signed quotient preserving balance.

## 9. Required state fields

`candidate_version`: `LIMIT-PRIME-GATE-LIFT-v1`  
`prior_missing_implication`: \(D_{\Gamma_*}(P;p)\ge0\) for every composition-prime Boolean \(P\) and every interior product bias \(p\).  
`new_proved_inference_or_exact_failed_claim`: all 306 one-step signed identifications of the source \(n=18\) gate were classified; exactly 90 are balanced, all have \(I=261/128\), and all satisfy (7.1); the proposed stronger-obstruction escape by one signed identification is refuted.  
`replacement_obligation`: biased prime-gate analysis or a genuinely changed shared-core/support/host construction, not another coordinate merge of this source gate.  
`peer_artifact`: fleet01/B12 `20260922T011847Z-prime-n18-gate`, blob `9ab98c0e82f7cf0f34eac98923df23b7b160670b`.  
`next_recipient`: `fleet03/B18` primary; `fleet01/B12` secondary.  
`implication_to_full_FEI`: still (1.1); if proved for all prime gates/all biases, the gate cocycle and all-gate equivalence yield full FEI with \(C_*=6.5218512\).

**Classification:** `ESSENTIAL_STEP_APPLIED / EXACT_ADVERSARY_FAMILY_REFUTED`.  
**Full FEI:** **OPEN / NOT PROVED**.

## 10. Reproducibility

`check_n18_signed_identification_rigidity.py` reconstructs the exact source truth table, verifies the published SHA-256, enumerates all 306 signed pair identifications and all 36 coordinate fixings, computes balance and influence by exact integer counts, computes Walsh spectra by integer FWHT, and applies exact-rational logarithm enclosures to the two nontrivial balanced core-host spectral types. It returned `PASS`.

Local execution SHA-256 values before repository delivery:

* checker source: `a71beea1e5051f7d26e5cdfcf9ef245886bc7fce122402aa59ef6019917d6eb0`;
* captured output: `10f50bc439ed7a8a658dd35f60c82eded77b6f9372047c3721ee8a27d8f5b426`.

No paid model/API/Codex, workflow dispatch, email, Drive, public posting, scheduler repair, cross-account mutation, or credential access was used.
