# The non-cyclic Volterra operators on the two-dimensional simplex satisfy Ulam's ergodic theorem

Settled 2026-09-08. Ledger id E0061 (intake E, source `qso_open_2009`, Rozikov's Problem 4).

## The problem as the source states it

Rozikov, *Quadratic stochastic operators: results and open problems* (arXiv:0902.4207), p. 4. The
Volterra quadratic stochastic operators on S^2 are

    V : x' = x (1 + a y - b z),   y' = y (1 - a x + c z),   z' = z (1 + b x - c y),      a, b, c in [-1, 1].   (*)

> Theorem 3 [3]. If the parameters a, b, c for the Volterra QSO (9) have the same sign and each is
> non-zero, then the ergodic theorem will fail for this operator.
> Problem 4. Is the condition of Theorem 3 sufficient for the ergodic theorem to hold?

The ergodic theorem (Ulam) for V means: for every x in S^2 the Cesaro limit lim (1/n) sum_{k<n} V^k x
exists. [3] is Ganikhodzhaev and Zanin, Russian Math. Surveys 59:3 (2004) 571-572; read in full today,
it proves exactly the failure in the cyclic case and nothing else. A later paper by the same authors
(arXiv:1205.3841, 2012, in Russian) states as its Theorem 1 that V is non-ergodic if and only if
a, b, c are nonzero and of one sign, and attributes the equivalence to [3]; the sufficiency half is
not in [3]. It is proved below; it is elementary.

## Theorem

If it is not the case that a, b, c are all nonzero and of the same sign, then every trajectory of (*)
converges to a fixed point. In particular the Cesaro means converge for every initial point, and
together with Theorem 3 of the source: the ergodic theorem holds for (*) if and only if a, b, c are
not all nonzero of one sign.

## Proof

Write the trajectory as (x_n, y_n, z_n) = V^n (x_0, y_0, z_0). All three coordinates stay in [0, 1]
and sum to 1, and the coordinate planes are invariant (a zero coordinate stays zero).

**Case 1: some coefficient is zero.** Say a = 0 (the other two cases are the same after relabelling).
Then x_{n+1} = x_n (1 - b z_n) and y_{n+1} = y_n (1 + c z_n). Since b has a fixed sign and z_n >= 0,
the sequence x_n is monotone (nonincreasing if b >= 0, nondecreasing if b <= 0); likewise y_n is
monotone. Both are bounded, so both converge, and z_n = 1 - x_n - y_n converges too. The limit is a
fixed point because V is continuous.

**Case 2: a, b, c all nonzero and not of one sign.** Read the signs as a tournament on the three
species: a > 0 means x beats y (x gains from y and y loses to x), b > 0 means z beats x, c > 0 means
y beats z. All positive is the cycle x -> y -> z -> x, all negative the reversed cycle; any mixture of
signs breaks the cycle and the tournament is transitive, with one species beating both others. Call
that species w and the other two u, v. Its update is

    w_{n+1} = w_n (1 + p u_n + q v_n)     with p, q > 0 the absolute values of its two coefficients,

so w_n is nondecreasing and bounded by 1, hence converges to some w* with w* >= w_0.

If w_0 > 0: the product prod_{k<n} (1 + p u_k + q v_k) = w_n / w_0 converges to w*/w_0, a finite
positive limit, and since each factor is >= 1 this forces sum_k (p u_k + q v_k) < infinity, so
u_n -> 0 and v_n -> 0, and the trajectory converges to the vertex of w.

If w_0 = 0: the trajectory lives on the edge {w = 0}, where V restricts to the two-species map
u' = u (1 + alpha v), v' = v (1 - alpha u) with alpha the remaining nonzero coefficient (up to sign
and labelling). One of u_n, v_n is nondecreasing and the other nonincreasing, both converge, and as
above the growing one's product forces the other to 0 unless the growing one starts at 0; in every
case the trajectory converges to a vertex, or is itself a vertex.

Convergent trajectories have convergent Cesaro means; that is the theorem. Nothing in the argument
needs |a|, |b|, |c| <= 1 beyond keeping V a map of the simplex.

## Remarks

* The cyclic case fails for the opposite reason: there the interior fixed point is a repeller and no
  coordinate is monotone; the trajectory spirals out to the boundary and visits the three vertices in
  turn for geometrically growing sojourns (1, 3, 2, 1, ... with sojourns 12, 51, 1073, ... steps in a
  simulation of a = b = c = 1; e0060.py), which is the mechanism of [3].
* In the degenerate Case 1 the limit need not be a vertex: with a = 0 the whole edge {z = 0} consists
  of fixed points and a trajectory can converge to any point of it (a = 0, b = c = 0.5: the orbit from
  (0.384, 0.61, 0.006) converges to (0.384, 0.616, 0); e0061.py). So the ergodic theorem holds there
  in Ulam's sense while the limit depends on the initial point.
* Long-orbit numerics for every sign pattern (e0061.py, 300,000 iterates) show convergence in all the
  non-cyclic cases and, in the cyclic controls, a trajectory parked at a vertex for the whole horizon,
  as the growing sojourns predict.

## Prior art

The 2004 note proves the necessity only; the 2012 paper asserts the equivalence and cites the note for
it; Rozikov's 2009 list poses the sufficiency as Problem 4 five years after the note. The proof above
is the natural one from R. Ganikhodzhaev's tournament picture (Mat. Sb. 1992/93: a transitive
tournament on three types has no interior fixed point) and may well be regarded as folklore in that
school; I have not found it written out.
