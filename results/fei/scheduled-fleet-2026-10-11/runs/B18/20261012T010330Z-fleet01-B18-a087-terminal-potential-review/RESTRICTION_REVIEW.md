# A087 restriction review: accepted point-defect phase sign, first universal-tree gap

## Reviewed object

This review reconstructs the restriction chain behind
`B20-A096-TERMINAL-COMPENSATION-v1`, using the original B05 conditional-label
packet, the B19 phase repair, and the B20 terminal telescope.  It does not
infer acceptance from any registry label.

## Independent reconstruction of the B19 phase sign

For a midpoint/half-difference pair `(a,v)`, put

\[
 q=a^2+v^2,\qquad
 Q(a,v)=qj(v^2/q),\qquad
 j(t)=1-h_2\!\left(\tfrac12+\sqrt{t(1-t)}\right).
\]

Let `q_n` be the Boolean one-point defect and `x=2^{-n}`.  The empty
frequency has `(a,v)=(-1+x,x)` and each nonempty frequency has `(x,x)`.
Since `Q(x,x)=2x^2`, direct multiplicity counting gives

\[
 Q_n=P(x)+2x-2x^2,
 \qquad P(x)=Q(1-x,x).
\]

The constant physical child has phase packet zero and the exceptional child
is `q_{n-1}`.  Therefore

\[
 \Gamma_n^Q=Q_n-\tfrac12Q_{n-1}
 =P(x)-\tfrac12P(2x)+2x^2.
\tag{1}
\]

Writing `r=2 sqrt(t(1-t))`, the binary-entropy Taylor series is

\[
 j(t)=\frac1{\ln2}\sum_{m\ge1}
 \frac{r^{2m}}{(2m)(2m-1)}.
\]

The first term gives `j(t)>=2t(1-t)/ln2`.  Comparing coefficients with
`1-sqrt(1-r^2)` and using
`binom(2m,m)/4^m >= 1/(2m)` gives `j(t)<=2t/ln2` for `0<=t<=1/2`.
Consequently,

\[
 P(x)\le\frac{2x^2}{\ln2},\qquad
 P(2x)\ge\frac{8x^2}{\ln2}
 \frac{(1-2x)^2}{(1-2x)^2+4x^2}.
\]

For `0<x<=1/8`, the rational factor is at least `9/10`, hence

\[
 \Gamma_n^Q\le x^2\left(2-\frac8{5\ln2}\right)<0.
\]

Thus the B19 phase theorem is accepted for every `n>=3`.  Combined with the
already independently accepted B05 `L` sign, it proves
`Gamma_n^(L+Q)<0` at the stated point-defect scope.  A separately written
exact-rational checker reproduced both factor-coordinate signs of
`q_4 tensor q_5` and 64 rigorous phase/full-packet signs.

## B20 chain identity

With `D_n=L_n+Q_n` and
`Gamma_n^D=D_n-D_{n-1}/2`, direct iteration gives

\[
 D_N=2^{-(N-2)}D_2+
 \sum_{n=3}^N2^{-(N-n)}\Gamma_n^D.
\]

All path probabilities are correct: each surviving exceptional restriction
has fair probability `1/2`.  The constant branch has zero packet, while the
terminal `q_2` cost is retained.  The identity and its interpretation as a
counterexample to nodewise nonnegative refunds are accepted.

## First gap in the universal continuation

The next displayed B20 target writes a terminal cost `D(f_l)` for every leaf.
That notation is not defined by the original proof.  The source packet
`D=L+Q` belongs to a chosen physical selector/data split.  Outside the
coordinate-symmetric `q_n` chain it can depend on the chosen coordinate or
block.  A stopped leaf has no declared next split, so `D(f_l)` is not yet a
coordinate-free potential.

This is the first gap, before any attempted estimate: the proposed universal
terminal inequality is not a fully quantified statement.  It also has not
specified the local credits that must telescope with the same terminal
potential.

`TREE_LEDGER_REPAIR.tex` supplies the correct abstract replacement.  One must
preassign a coherent scalar potential to every node, retain fair path weights,
and use the exact influence recursion.  The repaired ledger proves that
local-credit and terminal bounds together imply a nonreusing global bound.
It does not construct the required universal potential or prove either bound.

## Verdict

- `B19-A094-FULL-ORDER-SWAP-CREDIT-BOUNDARY-v1`: **ACCEPTED at its explicit
  point-defect and q4-tensor-q5 scope** by this independent review.
- `B20-A096-TERMINAL-COMPENSATION-v1`: **ACCEPTED for the canonical q_n
  chain**.
- Universal terminal-budget continuation: **OPEN / first gap
  G-TERMINAL-POTENTIAL-COHERENCE**.
- Full FEI: **OPEN**.
