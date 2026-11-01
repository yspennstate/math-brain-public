# B18 / A087 — restriction referee: terminal-potential coherence

**Run:** `20261012T010330Z-fleet01-B18-a087-terminal-potential-review`  
**Primary packet:** A087 (Restriction referee)  
**Reviewed target:** `B20-A096-TERMINAL-COMPENSATION-v1`, including dependency
`B19-A094-FULL-ORDER-SWAP-CREDIT-BOUNDARY-v1`  
**Stable gap:** `G-TERMINAL-POTENTIAL-COHERENCE@1`  
**Verdict:** the B19 full phase sign and the B20 one-point-defect telescope
are accepted at their exact scopes.  The proposed universal tree continuation
has a first definitional/quantifier gap.  A coherent-potential tree lemma is
proved as a repair.  Full FEI remains **OPEN**.

## Mathematical movement

The B19 contributor proof of the omitted phase packet was reconstructed from
the entropy-deficit series.  The exact identity

\[
 \Gamma_n^Q=P(2^{-n})-\tfrac12P(2^{1-n})+2^{1-2n}
\]

and the bounds

\[
 \frac{2t(1-t)}{\ln2}\le j(t)\le\frac{2t}{\ln2}
 \quad(0\le t\le1/2)
\]

give `Gamma_n^Q<0` for every `n>=3`.  The endpoint `n=3` is included because
the rational factor is exactly at least `9/10` for `x<=1/8`.  Combining this
with the independently reviewed B05 `L` sign accepts the complete `L+Q` sign
for the one-point-defect family.  The independent checker also rigorously
reproduced the two factor-coordinate signs for `q_4 tensor q_5`.

The B20 telescope is algebraically correct and keeps the fair-path terminal
cost:

\[
 D_N=2^{-(N-2)}D_2+
 \sum_{n=3}^N2^{-(N-n)}\Gamma_n^D.
\]

It therefore refutes only a nodewise nonnegative-refund route, not a globally
chosen restriction tree.

## First exact gap

The universal continuation writes

\[
 \sum_{\ell}2^{-\operatorname{depth}(\ell)}D(f_\ell)\le C I(f).
\]

But B05--B19 define `D` for a chosen physical selector/data split.  They do
not define a coordinate-free terminal functional `D(f_l)` for an arbitrary
stopped Boolean descendant.  Symmetry makes the suppressed split harmless
for `q_n`; it is a hidden hypothesis in the universal line.  Hence the first
gap occurs before estimation: the claimed terminal quantity and its coherent
parent credits are unspecified.

## Repaired lemma

For any finite fair physical restriction tree with a scalar potential `P_v`
preassigned to every node, define

\[
 \Gamma_v=P_v-\tfrac12(P_{v0}+P_{v1}).
\]

Then

\[
 P_{root}=\sum_{v\ internal}2^{-d(v)}\Gamma_v+
 \sum_{\ell\ terminal}2^{-d(\ell)}P_\ell.
\]

If each path reveals a coordinate at most once, total influence satisfies the
parallel exact ledger

\[
 I(f)=\sum_{v\ internal}2^{-d(v)}I_{i(v)}(f_v)+
 \sum_{\ell\ terminal}2^{-d(\ell)}I(f_\ell).
\]

Thus local bounds `Gamma_v<=C I_i(f_v)` and terminal bounds
`P_l<=C I(f_l)` imply `P_root<=C I(f)` without credit reuse.  This repair
preserves the `q_n` identity but exposes the two genuinely unpaid universal
bounds.  Because B18 supplied this abstract repair, it requires a fresh
independent reviewer.

## Computation

Command: `python3 independent_phase_reconstruction.py`  
Randomness: none.  The checker used exact rational arithmetic and outward
atanh-series logarithm intervals.  It passed 64 rigorous signs: `Q` and
`D=L+Q` for `q_n`, `3<=n<=32`, plus both packets for both coordinate classes
of `q_4 tensor q_5`.  `CHECK.out` records the four tensor intervals.

## Scope and controls

- Constant child: packet exactly zero.
- Rare branch: fair probability `2^{-depth}` retained.
- Terminal child: `2^{-(N-2)}D_2` retained; dropping it is invalid.
- Near tensor: both `q_4 tensor q_5` factor classes independently reproduced.
- Bent controls: opposite local signs remain compatible; no universal sign
  claim is made.
- Addressing and shared-variable interference: not claimed covered by the
  point-defect calculation.
- No Boolean counterfamily with unbounded `H/I` is produced.

## Source pins

- B18 contract blob `e6e014bc066a2f8b0454a1944ef6e03b969a5690`.
- Protocol blob `457358ff62cbf1141a72096bcabdf95bf18c1be2`.
- Stream index blob `58e3eb0b1f0e9c03ebf709f83ad496ee8f2df704`.
- Packet status blob `1beba565780ac4c3c1f28a00b20ca4d5e4e59ebb`.
- Claim registry blob `bceaed2294e4dab574d363750858c6d3866137f8`.
- Obstruction registry blob `e111933338dff1d7798c5e59b43700bbf30f7b96`.
- B05 original report blob `0f097b74548e4be301b39a918774c4465638b2df`.
- B19 original report blob `8281ad83ec178bd98a8a9cbfac192959d7d996bd`.
- B19 proof blob `7e56ec0c2d413d60ba850048b933b57deb41eb85`.
- B20 telescope blob `752a1bb2fd0069a1cfadda79e0a605ef088ea656`.

## Handoff

Route the accepted B19 sign and B20 chain scope to A096/A097.  Route
`G-TERMINAL-POTENTIAL-COHERENCE@1` and `TREE_LEDGER_REPAIR.tex` to A089 and
A090.  The next mathematical action is to define one coherent terminal
potential on a nontrivial closed family and prove both the local-credit and
terminal inequalities against the exact influence ledger.

No full-FEI solution, public release, scheduler change, extra worker, or
native Brain ingestion is claimed.  The runtime exposed no separate model or
reasoning-effort selector.
