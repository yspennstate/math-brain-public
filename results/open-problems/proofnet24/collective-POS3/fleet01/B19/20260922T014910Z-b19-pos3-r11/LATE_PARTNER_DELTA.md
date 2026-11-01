# Late partner delta — first-boundary non-prefix reversal exceeds 2/5

After the immutable B19 report was frozen, the assigned partner fleet02/B10 completed run `20260922T014627Z-fleet02-B10-pos3-r12`, report blob `acdb868b3e35a9248d494126311bfff3bfee150b`. Its endpoint blocker-product theorem proves that, at the first adjacent strong-majority chain-block boundary `x ≺_* y` of a hypothetical POS3 counterexample,

`2/3 < Pr_P(x<y) < 7/9`,

and both canonical Hasse-blocker channels carry positive majority-direction deletion-fiber defect.

This combines directly with the B19 initial-block decomposition. Let `C={c_1<...<c_m}` be the first maximal same-chain block, so `x=c_m`, and let

`H = #{L in L(P): C is the initial m-element block} = e(P\C)`.

The B19/lead one-sided rank argument gives

`H/e(P)>4/9`.

Every prefix lift has `x<y`. Therefore every lift with `y<x` is a **non-prefix** lift. Put

`E=e(P)`, `N=E-H`, `B=#{L:y<x}`.

The partner's strict `7/9` cap gives

`B/E = 1-Pr(x<y) > 2/9`,

while the prefix bound gives

`N/E < 5/9`.

Hence

`B/N > (2/9)/(5/9) = 2/5`.                                      (D1)

Equivalently,

`Pr_P(y<x | C is not the initial block) > 2/5`.                  (D2)

Thus the exact non-prefix component is not merely a source of an uncontrolled bias: at the first strong-majority boundary it reverses the majority orientation on **more than forty percent** of its mass. Together with fleet02/B10's two-channel activation, a future transfer proof has a concrete three-way flow to balance: two nonempty positive Hasse-blocker channels and a non-prefix reversal component of relative mass `>2/5`.

This does not prove IBWT or POS3. It sharpens the next accounting target: decompose the `>2/5` reversal mass by the first interruption level of the ideal chain and compare it with the two active Hasse channels under the rank-one lambda-gradient from the main B19 report.

Outcome remains `ESSENTIAL_STEP_APPLIED`; parent POS3 remains OPEN / NOT PROVED; execution context remains `WITHOUT_VERIFIED_BRAIN`.
