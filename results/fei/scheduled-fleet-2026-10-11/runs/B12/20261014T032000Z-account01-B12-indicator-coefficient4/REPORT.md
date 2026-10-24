# B12 / A058 — coefficient four fails for indicator activation

## Outcome

**REFUTED the unsigned coefficient-four indicator payment; PROVED an exact
all-depth co-singleton family above four and a certified six-bit seed above
4.5.  Independent review pending.**

For a nonzero Boolean indicator `q`, set

\[
\Phi(q)=\mathcal E(q)-p\log_2(1/p),\qquad p=\mathbb E q.
\]

The normalized Fourier law gives `Phi=p H(P_q)` and
`I=p E_{P_q}|S|`.  These quantities tensor exactly on disjoint physical
blocks, so every seed's ratio `Phi/I` survives every tensor depth.

## Clean parametric obstruction

Let `q_r` be one on all but one point of the `r`-cube.  With `N=2^r`,

\[
\frac{\Phi(q_r)}{\mathcal I(q_r)}=
\frac{2(N-1)}r\left(r-\frac{N-2}{N}\log_2(N-1)\right)=K_r.
\]

The proof in `PROOF.md` shows

\[
K_r>4\quad(r\ge3),\qquad
K_r=4+\frac{2}{r\ln2}+O(r2^{-r}).
\]

In particular `K_3=4.174257772798386...>4`, certified exactly by
`7^7<2^20`, and `K_5=4.407467891752582...>4.4`, certified by
`31^155<2^768`.  Every tensor power has the same ratio.  This is a genuine
growing family, not a finite-case survival or a depth-dependent constant.

## Stronger exact seed

A deterministic six-bit search found truth-table mask
`18446708751093190623`, with zeros `[5,12,13,28,29,37,45]`.  Its exact
integer Walsh-square multiplicities are

`{3249:1, 49:3, 9:24, 1:36}`,

and its degree-weighted square sum is 832.  Hence `p=57/64`, `I=13/64`, and

\[
\boxed{\Phi/I=4.512256384896659\ldots>4.5}.
\]

The exact sign certificate is

\[
2^{3024}>3^{547}19^{475}7^{49}.
\]

Tensor powers preserve this ratio at every depth and dimension `6k`.
Floating searches produced larger leads through dimension nine, but those
are retained only as numerical candidates; no stronger exact claim is made.

## Relevance to the active coherent gap

The preceding finite signed-ensemble ledger left the physical sign and
activation witness unpaid.  Independently paying its agreement and
disagreement indicators at coefficient four would have closed that route.
The co-singleton family and six-bit seed prove that projection impossible.

The next mechanism must therefore keep joint signed information: the exact
near/separated kernel should be combined with companion-sign, posterior
activation, or terminal-reserve credit under the actual changing hierarchy
weights.  Any separately isolated unsigned indicator budget must allow a
coefficient at least `4.512256384896659...`.

## Controls and limitations

- This is an exact disjoint-product activation obstruction, not an
  overlapping-input closure theorem.
- It concerns the normalized indicator remainder, not raw convolution mass.
- The genuine Boolean companions `f_k=2q^{tensor k}-1` have bounded FEI
  ratios: the six-bit family's limit is
  `5.244969399712791...`.  No FEI counterexample is claimed.
- The numerical search is heuristic; only the co-singleton formulas and
  six-bit integer certificates are promoted to proved claims.
- No independent review or native downstream adoption was observed.

Full FEI remains **OPEN**.

## Verification

`CHECK.py` reconstructs the integer Walsh spectra, exact rational influence,
co-singleton formulas, tensor invariance, and exact integer sign
certificates.  It directly checks co-singletons through `r=10`, the
three-bit family through tensor dimension 15, and the six-bit seed through
tensor dimension 12.  `CHECK.out` records `STATUS PASS`.

The exploratory program used deterministic seed `20261014032000`, dimensions
five through nine, forty annealing restarts, and 20,000 flips per restart.
Its source and retained output are archived; the compiled binary is excluded.

Execution metadata: natural scheduled invocation, primary packet `A058`,
actual exposed model identity `Codex`; no distinct runtime effort selector
or hour-long capacity guarantee was exposed.

