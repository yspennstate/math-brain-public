# B19 / A094 independent review: the B05 one-point-defect credit boundary

**Run:** `20261011T225023Z-fleet01-B19-b05-credit-boundary-review-a094`  
**Primary packet:** A094 (proof-chain challenger)  
**Reviewed target:** B05 / A023, claim `B05-A023-ORDER-SWAP-CREDIT-BOUNDARY-v1`  
**Stable gap:** `B05_RARE_REFUNDS`  
**Verdict:** the stated conditional-label theorem is accepted at its narrow scope. The phrase “order-swap credit” is unsafe without the superscript `L`: a physical selector/data swap contains the phase packet `Q` as well. This review repairs that scope gap and proves that the **complete physical `L+Q` credit is also negative** for the entire AND point-defect family and for both coordinate classes of the displayed `q_4 \otimes q_5` near-tensor witness. The repaired strengthening is contributor-proved and requires a fresh independent reviewer. Full FEI remains **OPEN**.

## 1. Source-bound object and review separation

The reviewed author bundle is

- repository `yspennstate/math-open-problems`, commit `f8af483622a55611c7933f7d8252fe3c94e4c06e`;
- path `reports/fei-2026-10-11/runs/B05/20261011T222410Z-fleet01-B05-credit-boundary-a023/`;
- `REPORT.md` blob `0f097b74548e4be301b39a918774c4465638b2df`;
- `CLAIMS.json` blob `beb1af6098f1cc56558f840eca3794ac9e8f84f7`;
- author checker blob `9be31981e5d5a5764ce07dada585ad5a57f221b7`.

The immediately preceding B19 audit is commit `030226fba465fb9ead1f3cfaf5dd474a99db194c`, path `reports/fei-2026-10-11/runs/B19/20261011T214601Z-fleet01-B19-b05-data-prefix-review-a094/`, report blob `99d9dc4d701564d005c19d673ac8050be3e514c5`. It established that a complete physical order swap uses `L+Q`, not `L` alone. On its bent family, the repaired `L+Q` credits were nonnegative. That result does not determine the present AND-defect signs.

This review keeps three statements separate:

1. **Accepted author theorem:** exact negativity of the conditional-label `L` credit.
2. **Scope repair:** the author’s theorem alone says nothing about the sign of the complete physical `L+Q` credit.
3. **New strengthened theorem:** for the author’s AND point defects, `Q` is itself negative; consequently `L+Q` is negative too.

## 2. Ledger definitions

For a midpoint/half-difference pair `(a,v)`, put

\[
  q=a^2+v^2,\qquad
  L(a,v)=\phi(a^2)+\phi(v^2)-\phi(q),
\]

where \(\phi(t)=t\log_2(1/t)\), and

\[
  Q(a,v)=q\,j\!\left(\frac{v^2}{q}\right),\qquad
  j(t)=1-h_2\!\left(\frac12+\sqrt{t(1-t)}\right).
\]

The exact physical selector/data packet is

\[
  D(a,v)=L(a,v)+Q(a,v).
\]

For a coordinate split, the order-swap credit is the parent packet minus one half of the corresponding restricted-child packet. Thus `L`, `Q`, and `D=L+Q` credits may be audited independently and then added.

## 3. Accepted narrow B05 theorem

Let \(q_n:\{0,1\}^n\to\{-1,1\}\) be `+1` only at the origin and `-1` elsewhere, and write \(\delta=2^{-n}\). The B05 derivation gives, for every coordinate,

\[
\Gamma_{n}^{L}
=\sum_{T\not\ni i}
\left[
\Psi(x_T,\delta^2)+\Psi(y_T,\delta^2)
-\frac12\Psi(x_T+y_T,4\delta^2)
\right],
\]

with the author’s declared `Psi` convention. Direct term-by-term reconstruction confirms the formula, endpoint multiplicities, and strict sign

\[
  \Gamma_n^L<0\qquad(n\ge 3).
\]

The reported asymptotic is also correct:

\[
  \Gamma_n^L
  =\delta^2\left(-2n+6-\frac1{\ln2}\right)+O(\delta^3).
\]

For \(q_4\otimes q_5\), the author’s two `L` credits are rigorously negative. This review independently reconstructed all parent and child Walsh spectra from their genuine Boolean truth tables.

**Review verdict at this scope:** `ANALYTICALLY_PROVED_INDEPENDENTLY_REVIEWED`.

## 4. Exact phase formula for the AND defect

Define

\[
 P(x)=Q(1-x,x).
\]

For the `q_n` split, the empty Fourier cell has `(a,v)=(-1+delta,delta)` and every nonempty cell has `(a,v)=(delta,delta)`. Since `Q(delta,delta)=2delta^2`,

\[
  Q_n=P(\delta)+2\delta-2\delta^2.
\]

After restricting the chosen data coordinate to the exceptional child, the defect density doubles. Hence the phase order-swap credit is exactly

\[
  \boxed{\Gamma_n^Q=P(\delta)-\frac12P(2\delta)+2\delta^2.}
\]

This identity includes the endpoint cells and uses no asymptotic approximation.

## 5. Analytic sign of the phase credit

Put \(r=2\sqrt{t(1-t)}\). The binary entropy expansion gives

\[
j(t)=\frac1{\ln2}\sum_{m\ge1}
\frac{r^{2m}}{(2m)(2m-1)}.
\]

The first term yields

\[
  j(t)\ge \frac{2t(1-t)}{\ln2}.
\]

For the upper bound, compare coefficients with

\[
1-\sqrt{1-r^2}
=\sum_{m\ge1}\frac{\binom{2m}{m}}{4^m(2m-1)}r^{2m}.
\]

The elementary bound \(\binom{2m}{m}/4^m\ge 1/(2m)\) gives, for \(0\le t\le1/2\),

\[
  j(t)\le\frac{1-\sqrt{1-r^2}}{\ln2}
  =\frac{2t}{\ln2}.
\]

Now \(q=(1-x)^2+x^2\) and \(t=x^2/q\). Therefore

\[
 P(x)\le \frac{2x^2}{\ln2},
\]

while

\[
P(2x)\ge
\frac{8x^2}{\ln2}\,
\frac{(1-2x)^2}{(1-2x)^2+4x^2}.
\]

When \(0<x\le1/8\), the last rational factor is at least `9/10`. Consequently

\[
\Gamma_n^Q
\le x^2\left(2+\frac2{\ln2}-\frac{18}{5\ln2}\right)
=x^2\left(2-\frac{8}{5\ln2}\right)<0,
\]

using \(\ln2<4/5\). Taking \(x=\delta=2^{-n}\) proves

\[
  \boxed{\Gamma_n^Q<0\quad\text{for every }n\ge3.}
\]

Moreover, since \(P(x)=2x^2/\ln2+O(x^4)\),

\[
\Gamma_n^Q
=\left(2-\frac2{\ln2}\right)\delta^2+O(\delta^4).
\]

Combining with the accepted B05 `L` asymptotic gives the complete physical credit

\[
\boxed{
\Gamma_n^{D}=\Gamma_n^{L}+\Gamma_n^{Q}
=\delta^2\left(-2n+8-\frac3{\ln2}\right)+O(\delta^3)<0
}
\]

for every \(n\ge3\), with strict negativity furnished by the two separate exact sign theorems rather than by the asymptotic alone.

## 6. Exact finite certification

`full_credit_review_checker.py` imports no author code. It uses:

- exact rational arithmetic for all Fourier coefficients and entropy arguments;
- an atanh series with an explicit rational tail for every logarithm;
- all four quotient corners for signed interval division;
- exact integer fast Walsh transforms of the genuine Boolean truth tables for `q_4 tensor q_5`, `q_3 tensor q_5`, and `q_4 tensor q_4`;
- no random search.

Command:

```text
python3 full_credit_review_checker.py
```

The run certified `L<0`, `Q<0`, and `D<0` for all `q_n`, `3<=n<=40`, and certified all six signs for the two coordinate classes of `q_4 tensor q_5`. Representative rigorous caps are:

| Witness / factor | `L` upper cap | `Q` upper cap | `D=L+Q` upper cap |
|---|---:|---:|---:|
| `q_4 tensor q_5`, `q_4` coordinate | `-0.00022` | `-0.000011` | `-0.00023` |
| `q_4 tensor q_5`, `q_5` coordinate | `-0.00026` | `-0.000005` | `-0.00026` |

There were 120 rigorous sign assertions and 1,024 exact Walsh-coefficient assertions, for 1,144 total assertions. `CHECK.out` records `status=PASS`.

## 7. Mandatory falsifiers and scope

| Control | Result |
|---|---|
| Sparse one-point defect | Complete `L+Q` credit is strictly negative for every `q_n`, `n>=3`. The rare logarithmic term survives. |
| Rare activation/suspension | Multiplying the core by a fresh activation event scales the exposed spectral packet by the activation probability; it does not change this core sign. This does not supply a global refund. |
| Near tensor | Both factor-coordinate classes of genuine Boolean `q_4 tensor q_5` have negative complete credit. |
| Bent selector | The preceding B19 repair found nonnegative complete credits on the declared bent family. Hence no sign-universal local theorem survives across the two families. |
| Addressing/multiplexer | No new universal statement is made. Fresh-selector/orthogonality endpoints from the campaign manuscript remain intact. |
| Actual prime Boolean gates | Every `q_n` is a genuine Boolean gate; the result is not a non-Boolean prefix-law artifact. |

The result is a no-go theorem for a particular **nodewise nonnegative first-credit mechanism**. It does not refute signed telescoping, multistep cancellations, globally chosen restriction trees, or nonlocal stopping-time payments. It is not a Boolean counterfamily with unbounded `H/I`; in particular, it is not a counterexample to FEI.

## 8. Literature overlap check

Primary-source checks included González–MacManus–Pereyra, *The Fourier Entropy-Influence Conjecture for Certain Decision Trees* (arXiv:2606.00246v2), especially its wrong-versus-well-chosen split-variable framework; Wan–Wright–Wu, *Decision Trees, Protocols, and the Fourier Entropy-Influence Conjecture* (arXiv:1312.3003); and O’Donnell–Tan, *A composition theorem for the Fourier Entropy-Influence conjecture* (arXiv:1304.1347). These sources motivate tree and composition accounting but do not, from the portions checked, supply this exact point-defect `L/Q` sign calculation. This is an overlap check, **not** a priority or novelty claim.

## 9. Claim/dependency delta and handoff

- **Accepted:** `B05-A023-ORDER-SWAP-CREDIT-BOUNDARY-v1`, only after reading “order-swap credit” as the conditional-label `L` credit explicitly defined by B05.
- **Required editorial repair:** qualify all unadorned uses as `L-credit`; do not cite the author bundle alone for a physical `L+Q` statement.
- **New contributor-proved claim:** `B19-A094-FULL-ORDER-SWAP-CREDIT-BOUNDARY-v1`.
- **Independent-review status:** pending. B19 materially added the phase proof and therefore cannot serve as the independent reviewer for the strengthened claim.
- **Next action:** A087 or A090 should reconstruct the exact `Gamma_n^Q` identity, the two scalar bounds for `j(t)`, and one tensor sign certificate. If accepted, B05 may retire the fixed-price nodewise nonnegative-credit route at full physical `L+Q` scope while retaining signed/global routes.

Full Fourier Entropy-Influence remains **OPEN**.

