# C034 v1: explicit numerical inputs for C031

Status: proof (unaudited), target3, kind bound. This is a numerical
corollary of C009/C031, not a new threshold theorem or a novelty claim.

On the largest interior k=4 Poisson branch at the two specified points,
let Z_i be total progeny, including the root, of C009's stationary
24-type downward-perturbation cascade started at type i. Let S be the
sum of the six boundary-pair cascade costs on the common tree as in
C023/C031; independence among those six costs is not assumed. Then

| c | H | lower bound p on every conditioning probability | 1/theta | 1/gamma |
|---|---|---|---|---|
| 11 | 91 | 1/1024 | 1898381312690450724864 | 11390287876142704349184 |
| 12 | 89 | 1/2048 | 38623146684146459504640 | 231738880104878757027840 |

For every starting type i, E exp(theta Z_i)<=e<3. Also
E exp(gamma S)<=e<3. Conditional Jensen preserves the corresponding
moment bounds for C023's canonical finite-history conditional costs,
uniformly in history length. In particular C024's inventory tail obeys

    2c E[S 1{S>L/2}] <= (4c/gamma) exp(-gamma L/4).

These are pointwise constants at c=11 and c=12, not a uniform interval
claim. The larger c has a worse certified exponent under this crude
method; no monotonicity of these bounds is asserted.

## Exact certificate

The inputs are the saved C006/C007 largest-fixed-point boxes
t3_kernel_JS_k4_c11.json and t3_kernel_JS_k4_c12.json. Their descriptive
status is "exact interval PASS; tree kernel and spectral stability only".
The new computation reads those boxes as prior lemmas; it does not
recalculate their old kernel endpoints or change their scope.

Write pi=(1-s,s-q,q-p,p), with every component positive. In the C009
column-parent convention,

    T[(u,v,z),(a,b,d)] = c*pi_z/pi_d *
      Pr(M(N+e_z)=d, M(N+e_a)=u, M(N+e_b)=v),

where a>b, u>v and N has independent Poisson(c*pi_j) coordinates.
The code sums the exact complete caps N0 in{0,>=1}, N2,N3
in{0,1,2,3,>=4}, with N1 irrelevant. Thus there is no discarded tail.
The source-bound receipts store all24 types and all576 matrix entries
as outward integer intervals with denominator D=10^60.

For each point let U be the rational matrix of entrywise upper bounds.
Interval Gaussian elimination on I-U^transpose, with right side2*1,
selects a rational candidate h by taking midpoints of the resulting
enclosures. The proof does not rely on this solver being accurate:
it separately checks h_i>=1 and every exact rounded residual

    h_i - sum_j h_j U[j,i] >= 1.

The actual matrix T is entrywise at most U, so this is the required
C031 unit left drift for T. The largest candidate coordinate is rounded
UP to the integer H in the table. The p bound is checked against the
LOWER endpoint of every pi interval. All vector coordinates, residuals,
matrix entries and source hashes are recorded in
logs/t3_cascade_rate_k4_c11.json and t3_cascade_rate_k4_c12.json.

As useful encoding checks, the independently grouped finite-cap
quantities satisfy interval enclosures of the C009 identities TE=EL
and HL=JH:144 plus18 scalar comparisons per point. These checks help
detect a transposition or cap mistake; they do not replace C009's proof
or an independent audit of the numerical code.

Set C=c, which is integral at both points, and evaluate using integers

    A=(3H^2/p)(9C^2+9C+1)3^(2C),
    s=1/A, theta=1/(2A), gamma=1/(12A).

The exact denominators are those in the table. The residual, H, p and
C checks supply every numerical hypothesis of C031. Apply C031 to
obtain the stated moment and inventory bounds, without multiplying
dependent offspring or boundary-pair probabilities.

Reproduce in a fresh directory containing the four C032 engine modules,
target3_cascade_rates.py and the two prior box receipts in their original
scripts/logs layout. Run the new script with argument11 and/or12.
It refuses to overwrite any completed point. Source hashes include
the C009 and C031 proof files; copy those proofs as well. No ordinary
floating-point value is used by the calculation.

What remains open: transfer of stationary cascade estimates to the
adaptively exposed finite graph, relative class depletion, genuine
two-coordinate hits and planted-to-ER comparison. This claim does not
supply a new circumference cutoff or finite strong-core onset.
