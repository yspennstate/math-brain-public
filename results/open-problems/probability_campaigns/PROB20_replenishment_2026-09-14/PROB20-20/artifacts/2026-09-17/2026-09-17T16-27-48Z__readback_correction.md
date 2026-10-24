# PROB20-20 exact-readback correction for the 2026-09-17T16-27-48Z report

This note preserves the report at creation commit `ff4bedc128bc31444664d773a57cdcc5b261805d` immutably. It records three notation corrections and one omitted easy boundary case found during exact-commit readback. None changes Theorem 5.1, the frozen metric, or the proof mechanism.

## 1. Notation-only corrections

In the report, the fixed sparse-chain activity sequence is denoted `u_r`. Three displayed occurrences accidentally use `\nu_r` instead of `u_r`:

1. Equation (4.6) should read
   \[
   u_r\ge C R^{-r}.
   \]
2. Equation (12.1) should read
   \[
   u_r=\frac1{(r+2)(\log(r+2))^{1+\eta}}.
   \]
3. Equation (12.5) should read
   \[
   u_r\asymp\frac1{r(\log r)^{1+\eta}}.
   \]

The surrounding prose, equations (4.2)--(4.4), (12.2), (12.6)--(12.8), and every use in the proof already refer to the same `u_r`; these are typesetting-only slips.

## 2. Boundary case omitted in the phase proof

Lemma 10.1 is stated for `j>r_n`. In Section 11, at the selected phase one always has `r_{n_l}\le j_l` for large `l`, because the source-valid cutoff satisfies `K_n\le\sqrt n=o(s_{j_l})` while `s_{j_l}/n_l\to\delta>0`.

The report applies Lemma 10.1 without separately spelling out the possible equality case `r_{n_l}=j_l`.

That equality case is easier and needs no fiber estimate. On the high-probability phase event
\[
s_{j_l}<E_{n_l}<s_{j_l+1},
\]
all excess boxes have supported size at least `s_{j_l}` because `r_{n_l}=j_l`. If there were no `s_{j_l}` excess box, then either `E_{n_l}=0` or the first positive excess contribution would be at least `s_{j_l+1}`, contradicting the displayed phase event. Hence an `s_{j_l}` box exists deterministically on that event.

Thus Section 11 should be read as the following dichotomy:

- if `r_{n_l}=j_l`, the phase event itself forces `Y_(1)\ge s_{j_l}`;
- if `r_{n_l}<j_l`, Lemma 10.1 gives the stated bound `8R\varepsilon_{n_l}`.

In both cases
\[
P(Y_{(1)}\ge s_{j_l})\to1,
\]
so equations (11.10)--(11.14) and Theorem 5.1 are unchanged.

## 3. Status

The report remains **PARTIAL / OPEN** with respect to unrestricted Janson Problem 18.39. The new restricted theorem and metric statement remain exactly:
\[
b(w,\lambda)=\lambda-\nu
\]
for the arbitrary-radix sparse-chain class satisfying the report's summability and bounded-adjacent-activity-ratio hypotheses. No closure or publication claim is added by this correction.
