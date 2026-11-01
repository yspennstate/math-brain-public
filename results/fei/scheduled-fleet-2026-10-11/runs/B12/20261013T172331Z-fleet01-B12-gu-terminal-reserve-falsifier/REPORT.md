# B12 / A056 — exact falsifier for the constant-3 terminal reserve

## Status

**PROVED (pending independent review):** the candidate terminal-reserve bound

\[
\overline\Theta_{g,y}(\mu)\le 3\,\operatorname{Inf}_y(g)(1-\mu^2)
\tag{C3}
\]

from `B12-A056-GU-BIASED-CHILD-COCYCLE-v1` is false, even for a genuine
four-input Boolean outer gate and a genuine eight-input Boolean point-defect
child.  The stronger local candidate is not adjudicated by this example.

Universal GU and full FEI remain **OPEN**.  This run neither proves nor
disproves either conjecture.

## Exact witness

Index truth-table rows by masks `0,...,15`, with the distinguished outer
coordinate `y` equal to bit 0.  Let `g` have row-order truth table

```text
(1,1,1,-1,-1,-1,1,1,-1,-1,-1,1,-1,1,-1,-1).
```

Writing `g(y,z)=a(z)+y b(z)`, its exact Walsh coefficient vectors are

\[
a=\frac18(-1,-1,1,1,3,-1,1,5),\qquad
b=\frac18(1,1,-1,-1,-3,1,-1,3),
\]

so

\[
\beta=\operatorname{Inf}_y(g)=\sum_Tb_T^2=\frac38.
\]

Let `h` be the point defect on eight bits: it is `+1` at one input and `-1`
at the other 255 inputs.  Then

\[
\mu=\mathbb Eh=-\frac{127}{128}.
\]

Using the already-proved exact one-biased-child potential, direct exact
rational Walsh/cap arithmetic gives

\[
Q:=\frac{\overline\Theta_{g,y}(-127/128)}
         {\beta(1-(127/128)^2)}
\]

equal to

\[
\begin{aligned}
Q={}&\frac{3440249}{6120}\log_2 2-\frac{3317}{8}\log_2 3
-\frac{1273}{4}\log_2 5-\frac{514}{765}\log_2 7\\
&-\frac{1275}{4}\log_2 17-\frac{514}{765}\log_2 37
+\frac{32258}{255}\log_2 127+\frac{255}{8}\log_2 263\\
&+\frac{67081}{6120}\log_2 271+\frac{765}{8}\log_2 769.
\end{aligned}
\tag{1}
\]

Numerically, only for readability,

\[
Q=3.4006857580164371867211438373712870\ldots>3.
\]

### Exact strict comparison

Multiplying `Q-3` by 6120 and exponentiating base 2 shows that `Q>3` is
equivalent to the integer inequality

\[
2^{3421889}127^{774192}263^{195075}271^{67081}769^{585225}
>
3^{2537505}5^{1947690}7^{4112}17^{1950750}37^{4112}.
\tag{2}
\]

The two integers in (2) have exact bit lengths 16,553,282 and 16,550,830,
respectively, so (2) is strict.  `symbolic_outer4_witness.py` constructs the
formal logarithmic expression and performs this comparison using arbitrary
precision integers; it uses no floating point for the strict sign.

Thus (C3) is rigorously refuted by an actual Boolean composition
`F(z,x)=g(h(x),z)`.

## Parametric endpoint pattern

For the same fixed `g`, take the `n`-bit point defect, so
`mu_n=-1+2^{1-n}`.  Differentiating the finite cap formula at `mu=-1` gives

\[
\lim_{n\to\infty}
\frac{\overline\Theta_{g,y}(\mu_n)}{\beta(1-\mu_n^2)}
=R,
\]

where

\[
R=-\frac1{24}-\frac14\log_2 3+\frac12\log_2 5
  +\frac{15}{8}\log_2 e
=3.4281099572635318507\ldots.
\tag{3}
\]

The differentiation is legitimate at zero atoms because their contributions
are `O(epsilon^2 log(1/epsilon))`, hence have zero one-sided derivative.
Moreover `R>3` follows without decimal approximation: after multiplying by
24 it is equivalent to

\[
e^{45}5^{12}>2^{73}3^6.
\]

Since `e>1+1+1/2=5/2`, it suffices that

\[
5^{57}>2^{118}3^6,
\]

whose integer difference is
`6696642101675427459810979088831534154149 > 0`.

This is the general mechanism: the rare-bias endpoint slope, not an interior
collision, forces a reserve constant strictly above 3.  It is consistent with
the B19/A091 warning that rare bias cannot be discarded as an `O(p)` tax.

## Exhaustive four-input search

`search_outer4_envelope.py --grid-denominator 128` scanned all 65,536
four-input Boolean outer gates, each of four distinguished coordinates, and
all biases `mu=k/128` with `-128<k<128`.  It evaluated 66,585,600 normalized
values.  The largest grid value was the exact witness above.  This exhaustive
search is float64 candidate-location evidence only; the witness was then
recomputed independently with exact Fractions and 100-digit Decimal logs, and
the strict sign was certified by (2).

The same scan leaves constant 4 with numerical margin
`0.599314241983537...` at this finite scope.  That is evidence, not a theorem.

## Previous and new bound

- Previous status: (C3) was open and supported by 555,024 small local cases,
  whose maximum normalized value was about 2.28025.
- New status: (C3) is **REFUTED** by a genuine 11-input composition (four
  outer inputs, with one replaced by an eight-bit child, leaving three other
  physical outer inputs).  Any universal terminal-reserve constant must be at
  least `R=3.428109957...`.
- What survives: the exact biased-child formula and complete-tree cocycle are
  unchanged.  Only their proposed constant-3 payment is killed.

## Remaining unpaid step

Prove a corrected uniform payment, with constant at least `R`; the immediate
candidate is

\[
\overline\Theta_{g,y}(\mu)\le4\beta(1-\mu^2).
\]

The next proof attempt should split off the explicit endpoint slope (the rare
point-defect term) and apply the signed near/separated cap analysis only to the
residual.  It must also test five-input outer gates and both bias endpoints
before treating 4 as credible.  Simultaneous biased children and overlapping
physical variables remain beyond this one-child reduction.

## Reproduction

```bash
python3 search_outer4_envelope.py --grid-denominator 128
python3 certify_outer4_witness.py
python3 symbolic_outer4_witness.py
```

No random seed is used.

