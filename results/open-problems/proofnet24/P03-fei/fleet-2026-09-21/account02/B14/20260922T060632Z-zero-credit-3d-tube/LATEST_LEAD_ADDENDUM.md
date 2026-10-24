# Latest-A-lead compatibility addendum

After the main report was committed, a fresher completed Campaign-A lead became visible and was consumed before run close:

`proofnet24/P03-fei/fleet-2026-09-21/account01/B18/20260922T055608Z-balanced-mux-collar-sharpen/REPORT.md`

at immutable commit `9e3563d95cb9583329e5011ff281a4e1cdc41be9`, report blob `411fe1c905f9051b7d2dfb9c2c337c0b13bfbb69`.

It strengthens the balanced-address (`t=1/2`) unequal-data terminal selector to

\[
|q_1-q_0|\le\frac1{112}\min\{q_0+q_1,2-q_0-q_1\}
\Longrightarrow D_{\Gamma^\dagger}(MUX;1/2,q_0,q_1)>0,
\]
with the stronger constant `1/86` when the two data biases lie on the same side of `1/2`. It also supplies a sharper rational bound on `1/ln 2`.

This newer result does **not** subsume Theorem 4.1 of `REPORT.md`: its address bias is exactly `1/2`, whereas Theorem 4.1 gives a full transverse address/data tube

\[
|t-1/2|\le2^{-14},\qquad
\min(|q_0-1/2|,|q_1-1/2|)\le2^{-14}
\]
with uniform margin `>1/1000`, for an arbitrary other data bias. Conversely, Theorem 4.1 does not subsume the lead's much wider balanced-address relative-data collar. The two results are complementary and use the same genuine physical address reveal with zero-defect literal leaves.

Thus any MUX counterexample to the live candidate must satisfy both of the following whenever applicable:

1. if `|t-1/2|<=2^-14`, then **both** data biases are more than `2^-14` away from `1/2`;
2. if `t=1/2`, then
   \[
   |q_1-q_0|>\frac1{112}\min\{q_0+q_1,2-q_0-q_1\},
   \]
   and in the same-side sector it must violate the stronger `1/86` condition.

This is the updated exact remaining MUX localization for this run. Full MUX positivity, arbitrary composition-prime gate positivity, and full FEI remain open.
