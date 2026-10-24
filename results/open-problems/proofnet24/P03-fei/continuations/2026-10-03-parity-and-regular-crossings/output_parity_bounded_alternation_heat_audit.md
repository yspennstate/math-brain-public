# Independent full audit of output parity and bounded alternation

Date: 2026-10-02. **PASS.** I read the complete separate
[proof](output_parity_bounded_alternation_fei_proof.md), including its
sharper unate proposition, signed/zero-weight clauses and endpoint scope.
Its only theorem input, the complete
[bounded ascending-path support theorem](bounded_ascending_path_support_fei_proof.md),
was independently audited in
[my earlier full audit](bounded_ascending_path_support_heat_audit.md).
The conclusion is a corollary of that theorem. No historical priority,
external review or solution of ordinary arbitrary-crossing FEI is certified.

## The general constant and exact budget

For `h=chi_T g`, a constant-label upward path of `h` forces a change of
`g` on **every** edge in `T`, and no change of `g` on an edge outside
`T`. Thus its number of `T` edges is at most the prescribed `m`
alternations of `g` on the entire path. Its number of other edges is at
most `q=n-|T|`, since upward paths flip each coordinate at most once.
The path has at most `m+q+1` **vertices**. The support theorem must
therefore be used with `k=m+q+1`, giving exactly

\[
 H(h)=H(g)\le4\cot^2\left(\frac{\pi}{2(m+q+2)}\right)I(h).
\]

I checked the distinction between vertices and edges, and the fact that
paths may start or end anywhere. Restricting attention to maximal paths
is unnecessary. The argument applies to both label classes, so there is
no minority-label assumption.

Parity multiplication permutes Fourier indices by symmetric difference,
and complements the pivotal condition precisely in coordinates of `T`.
Consequently

\[
 I(h)=|T|+I(g)-2\sum_{i\in T}I_i(g).
\]

In particular full parity uses **complementary** influence `n-I(g)`.
The proof correctly avoids substituting `I(g)` for this quantity. If the
specified `h` is constant, its entropy is zero and the theorem has no
division by `I(h)`. Dimension zero is also dealt with separately.
When `m=0`, extending from the bottom vertex shows `g` is constant;
its parity modulation is a character and has entropy zero.

## Scalar scores and their scope

For nonnegative weights the score is nondecreasing on upward paths.
With every retained point assigned one of its opposite adjacent labels,
one crossing can create at most one sign change on the path. Even if
several scores tie or a path lands at a crossing, no crossing can be
passed twice. Thus the number of sign changes is at most the actual
retained scalar variation.

Zero-weight coordinates do not change `g`, because `g` depends only on
the score. They can appear in `h` through parity and then contribute
one to its influence; they cannot be silently discarded from an already
specified output character. The proof states this correctly. Coordinate
sign flips orient negative weights without changing influences or
entropy, and change the selected output character only by a global sign.
For arbitrary functions the path premise must be checked in the chosen
orientation; the proof does not assert it is order invariant.

An isolated attained-point anomaly with equal left/right labels can
create two path sign changes. The explicit clause counting two changes
is necessary and correct. Arbitrary spacings are permitted, whereas
counting anomalous locations as one crossing would not prove this theorem.

## The sharper unate proposition

For unate `g`, orient coordinates so it is monotone. The Chow identity
`I_i(g)=E[g X_i]` follows by conditioning on all other inputs. For
`t=|T|>=2`, therefore

\[
 s:=\sum_{i\in T}I_i(g)
 =\mathbb E[g\sum_{i\in T}X_i]
 \le M_t:=\mathbb E|\sum_{i=1}^tX_i|\le\sqrt t.
\]

With `a=sum_{i notin T}I_i(g)>=0`, the exact budget is `I(h)=t-s+a`.
The universal finite-alphabet bound is `H(h)<=n=t+q`. For `t=2`, the
exact `M_2=1` yields `H/I<=q+2`. For `t=3`, `M_3=3/2` gives
`(q+3)/(3/2)<=q+2`. For `t>=4`, `t-sqrt(t)>=t/2`, hence
`H/I<=2+2q/t<=2+q/2<=q+2`. All denominator bounds are positive.
Thus

\[
 H(\chi_Tg)\le(q+2)I(\chi_Tg),\qquad |T|\ge2.
\]

Full parity has `q=0`, proving constant two for every unate function
in dimensions at least two. Dimensions zero and one have entropy zero
for every Boolean function. The two-bit OR example has four equal
squared Fourier coefficients, entropy two, base influence one and
parity influence one. Its ratio is exactly two, so the constant is sharp.
Orienting unate inputs preserves this example's general budget argument.

## Limits of this audit

These are complete analytic implications, independently checked term by
term; a checker is supplementary. They do not prove ordinary FEI for
all monotone functions, all bounded-alternation functions, or arbitrary
nearby-three-crossing score functions. Keeping `q` bounded is essential
for a uniform constant in the stated general parity result. The sharper
unate proposition likewise retains the `q+2` dependence for partial
parity. No novelty claim follows from these elementary observations.

I also read and independently reran the entire
[author checker](verify_output_parity_bounded_alternation.py); it exited
zero. Its
[report](output_parity_bounded_alternation_checks.json)
contains all **65,814** Boolean functions through dimension four with
every output character, plus **96** scalar-score cases through dimension
twelve: **1,051,466** function/character pairs. The actual maximum path
alternation, output-label path depth, coordinate influence identities and
Walsh coefficient permutation use integer calculations. Its entropy
targets are expressly numerical supplements. Scalar cases separately
include attained endpoints, zero weights and reoriented negative weights.
The sharper unate test selects monotone functions and then uses the
analytically justified orientation argument; it is not described here
as an enumeration of every unate orientation. This was a rerun of the
author's code, **not** a claim of independently implementing that suite.
