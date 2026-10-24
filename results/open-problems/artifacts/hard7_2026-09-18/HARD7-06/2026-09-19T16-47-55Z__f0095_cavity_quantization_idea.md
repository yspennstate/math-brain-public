# HARD7-06 idea before code — cavity-guided quantization rather than another three-atom decimal shave

Runtime metadata for this invocation: **GPT-5.6 Sol; reasoning level UNVERIFIED — not GPT-6 maximum.**

Target remains canonical claim `F0095`: the fixed-`q=3` constant-location problem for ordinary sparse Erdos--Renyi 3-colourability.  The fixed source metric entering this run is

\[
W_3=U_3-L_3,
\qquad L_3=4.03,
\qquad U_3=4.6865076662.
\]

The two immediately preceding HARD7-06 runs did not move `W_3`, so an unchanged third run would trigger Section I.  The purpose of this note is to try a genuinely different route **before** writing any checker.

## B7 — take the limit object seriously

The preceding two runs derived the exact scalar cavity recursion in the transformed coordinate

\[
\lambda=\frac{1-\alpha}{2+\alpha}\in[0,1/2],
\qquad
T=\frac{1-2P+Q}{2-P},
\quad
P=\prod_i(1-\lambda_i),\quad Q=\prod_i(1-2\lambda_i),
\]

and proved that an infinite-support convex-mixture local minimizer must be a distributional fixed point of this recursion.  The small positive-mass scalar branch has already been excluded; any nontrivial fixed point at the current degree has

\[
\Pr\{\lambda>0\}\in(0.9319,0.9320).
\]

Instead of trying to prove more moment inequalities about that fixed point, use the fixed-point law as a **design guide** for a finite variational witness.  This reverses the previous direction: the continuum branch is not an obstacle to eliminate; it may be the object whose low-cardinality quantization beats the best three-atom law.

A population iteration of the exact RDE is used only as a heuristic to locate mass clusters.  It is **not** evidence for the source theorem and will not be used in the final proof.  The observed positive-message mass concentrates on several separated bands rather than on the two positive atoms of the current three-atom ACG witness.

## B8 — discretize the continuum object

Quantize the heuristic large-branch law to three positive transformed-message cells plus the forced zero-message atom.  Convert each cell centroid back to the original `alpha` coordinate.  Then deterministically re-optimise the resulting four-atom ACG law near `d=4.6865076662`.

A local search gives a candidate extremely close to

\[
a_4=
0.15333616\,\delta_{0.56153802}
+0.28476429\,\delta_{0.26488215}
+0.48318715\,\delta_{0.06698304}
+0.07871240\,\delta_1.
\]

This is structurally different from the current certified three-atom law

\[
0.30378594\,\delta_{0.44712052}
+0.61227086\,\delta_{0.08630144}
+0.08394320\,\delta_1.
\]

The new support is not obtained by adding an infinitesimal fourth atom to the old witness; it is a rebalanced discretization of the continuum cavity shape.

Floating-point evaluation predicts that `a_4` stays negative down to roughly `d=4.686507637...`.  This prediction is only a route-selection diagnostic.

## B10 — derandomize the route completely

Freeze every weight and support coordinate above as an exact rational with denominator `10^8`, and test the lower rational degree

\[
d_*=4.686507635=\frac{4686507635}{10^9}.
\]

The proof obligation is now finite and deterministic:

1. evaluate the ACG Poisson vertex expectation by exact multinomial enumeration through a certified truncation;
2. upper-bound each logarithm by rational atanh expansions and a dyadic enclosure;
3. lower-bound the edge-log expectation similarly;
4. lower-bound `e^{-d_*}` by the reciprocal of a rational upper bound for `e^{d_*}`;
5. use negativity of all omitted vertex-log terms to make Poisson truncation one-sided;
6. conclude a rigorous upper bound `Sigma^*_{d_*,3}(a_4)<0`.

If this succeeds, Ayre--Coja-Oghlan--Greenhill's same-degree implication gives a genuine source-metric movement

\[
U_3:4.6865076662\to4.686507635,
\qquad
W_3:0.6565076662\to0.656507635.
\]

The exact checker will be written only after this idea note is committed.