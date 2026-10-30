SIGNED IN - working on the quadratic-form bounded-density conjecture (universal constant), account fleet02, slot B03, 2026-09-24T10:55:36Z.
attacking: the punctured-pivot bridge from the opposite direction — test whether a uniform whole-copy half-Riesz/time budget can itself force linear small-ball after a 2+1 product bank has been compressed to an arbitrary dependent two-dimensional density.

# fleet02/B03 r55 — pivot-placement / half-Riesz obstruction

Status: **new source-valid obstruction to a tempting compressed 2+1 receiver; newest partner r52 applied; required pinned theorem applied; full unrestricted QFORM OPEN; unrestricted continuity OPEN; WITHOUT_VERIFIED_BRAIN**.

## 1. First unpaid implication

The preceding r54 run left a small-nonzero-pivot bridge: its whole-copy negative-half time integral stayed uniformly bounded through the pivot singularity, but that alone did not yield a one-copy density bound in the genuinely rough unlocalized residue.

This run identifies a hard obstruction to that route. A uniform bound on

    A_-(Q) = integral_R |t|^(-1/2) |phi_Q(t)|^2 dt

cannot by itself imply a universal density or linear small-ball bound, even for a fixed 3x3 quadratic matrix with spectrum {1,1,-1}, once two coordinates have been compressed to an arbitrary dependent joint density cap. Moreover, determinant and spectrum do not determine whether the latest partner r52 zero-pivot theorem is available: the placement of the genuinely independent scalar inside the quadratic geometry matters.

Therefore the next unpaid implication is not 'upgrade A_- to L-infinity abstractly'. It is: in every punctured 2+1 residue, retain original product provenance long enough to expose either (i) a zero-pivot hyperbolic edge carrying the independent scalar, (ii) a complementary positive-half / two-slope resource, or (iii) another already-paid aggregate receiver. A spectral permutation that moves the independent scalar is not legitimate probabilistically.

## 2. An exact cap-one dependent pair with a flat hyperbolic product

Fix 0 < epsilon <= 1 and define

    E_epsilon = { (s,r): 1 <= s <= exp(2/epsilon),
                           -epsilon/(2s) <= r <= 0 }.

Its area is exactly

    integral_1^{exp(2/epsilon)} epsilon/(2s) ds = 1.

Let (S,R) have joint density 1_{E_epsilon}. Thus its joint probability density has exact L-infinity cap one. Let V be independent of (S,R), uniform on [0,1], so its density cap is also one.

Put

    U = -2 S R.

Under the change r = -u/(2s), |dr/du| = 1/(2s), and the support becomes simply

    1 <= s <= exp(2/epsilon),   0 <= u <= epsilon.

Therefore

    p_U(u)
      = 1_{[0,epsilon]}(u)
        integral_1^{exp(2/epsilon)} ds/(2s)
      = epsilon^(-1) 1_{[0,epsilon]}(u).

So U is exactly Uniform[0,epsilon]. This uses dependence inside the two-dimensional bank essentially.

## 3. Fixed target-spectrum matrix with divergent density after compression

Consider

    Q_epsilon = 2 S R + V^2 = V^2 - U.

Its 3x3 coefficient matrix in the ordered variables (S,R,V) is

    B_bad = [[0,1,0],
             [1,0,0],
             [0,0,1]],

with

    spec(B_bad) = {1,-1,1},   det(B_bad) = -1.

Thus the deterministic matrix scale is exactly the owner target scale.

Because Z=V^2 has density

    p_Z(z) = (2 sqrt(z))^(-1) 1_{(0,1)}(z),

and U is independent of V, for 0 <= epsilon <= 1

    p_{Q_epsilon}(x)
      = epsilon^(-1) integral_0^epsilon p_Z(x+u) du.

At x=0,

    p_{Q_epsilon}(0)
      = epsilon^(-1) integral_0^epsilon du/(2 sqrt(u))
      = epsilon^(-1/2).

In fact for -epsilon <= x <= 0,

    p_{Q_epsilon}(x) = sqrt(x+epsilon)/epsilon,

and for x >= 0 the convolution formula shows the height is no larger. Hence

    ||p_{Q_epsilon}||_(infinity,ess) = epsilon^(-1/2) -> infinity.    (3.1)

Equivalently, for I_epsilon=[-epsilon/2,0],

    P(Q_epsilon in I_epsilon)
      >= |I_epsilon| / sqrt(2 epsilon),

so the linear small-ball ratio diverges at least as (2epsilon)^(-1/2).

This is **not** a counterexample to the original QFORM conjecture: (S,R) are dependent. It is a counterexample to any proof interface that replaces an original product two-dimensional bank by only an arbitrary joint density cap and then hopes to control an arbitrary invertible 2+1 quadratic by determinant/spectrum alone.

## 4. The whole-copy negative-half time budget nevertheless stays universal

Because U and V are independent,

    phi_{Q_epsilon}(t) = phi_{V^2}(t) phi_{-U}(t),

hence

    |phi_{Q_epsilon}(t)|^2 <= |phi_{V^2}(t)|^2.

For independent V,V' uniform on [0,1],

    E |V^2-(V')^2|^(-1/2)
      = 2 integral_0^1 integral_0^v (v^2-w^2)^(-1/2) dw dv
      = 2 integral_0^1 (pi/2) dv
      = pi,

where w=v sin(theta) in the inner integral. Using the positive regularized one-dimensional Riesz identity

    integral_R |t|^(-1/2) e^{itx} dt
      = sqrt(2pi) |x|^(-1/2),

we obtain, uniformly in epsilon,

    integral_R |t|^(-1/2)|phi_{Q_epsilon}(t)|^2 dt
      <= pi sqrt(2pi)
      = 7.874804972861209... .                                (4.1)

Equivalently, for an independent copy Q_epsilon',

    E |Q_epsilon-Q_epsilon'|^(-1/2) <= pi.                    (4.2)

Only the whole-output independent-copy identity

    |phi_Q(t)|^2 = E exp(it(Q-Q'))

is used. No coordinatewise sum/difference pair is separated or declared independent.

Thus a universal negative-half whole-copy time budget can coexist with arbitrarily large one-copy density. A complementary positive-half resource, phase structure, or original-product provenance is genuinely necessary to recover L^1_t and linear small-ball scale.

## 5. Newest partner fleet03/B03 r52: same spectrum, opposite placement

The latest compatible partner theorem is fleet03/B03 r52, `QFORM-2PLUS1-ZEROPIVOT-DETERMINANT-v1` (canonical report at math-open-problems commit cead39f2714d739dd5d00c7d3a537de4adba4732). For a dependent pair of joint density cap M and an independent scalar of density cap N, an invertible matrix

    B = [[A,c],[c^T,0]]

obeys

    ||p_Q||_(infinity,ess)
      <= 6 M^(2/3) N^(2/3) |det B|^(-1/3).

Apply it to the **same law architecture** ((S,R) dependent cap one; V independent cap one) but the permutation-congruent matrix

    B_good = [[1,0,0],
              [0,0,1],
              [0,1,0]],

so

    Q_good = S^2 + 2 R V,
    spec(B_good)={1,1,-1},
    det(B_good)=-1.

Here the independent scalar V has zero quadratic pivot and lies on the hyperbolic edge, so partner r52 gives the genuine bound

    ||p_{Q_good}||_(infinity,ess) <= 6,                       (5.1)

and its whole-copy conversion gives

    integral |t|^(-1/2)|phi_{Q_good}(t)|^2 dt
      <= 4 sqrt(6pi).                                         (5.2)

The matrices B_bad and B_good are related by swapping the first and third coordinate. Their determinant and spectrum are identical. Yet that permutation moves which variable is the genuinely independent scalar, and the compressed probability class is not invariant under that move. Therefore independence placement is extra structure not recorded by spectral data.

## 6. Required pinned e5f71... result applied at an actual target inequality

Now return to genuine original independent cap-one coordinates X_1,X_2,X_3 and keep the *same bad matrix* B_bad:

    Q_orig = 2 X_1 X_2 + X_3^2.

All three eigenvalues of B_bad have modulus one. The completed pinned `COUNTEREXAMPLE_SEARCH` Theorem A at `math-open-problems@e5f71d79eff325201dd0274053d20268ce65b837` states that for a three-dimensional quadratic with all eigenvalues of modulus at least sigma, uniformly in affine terms,

    ||p_Q||_infinity <= 6 sqrt(pi)/sigma.

With sigma=1 this yields the actual exact-target inequality

    ||p_{Q_orig}||_infinity <= 6 sqrt(pi)
      = 10.634723105433096... .                               (6.1)

So the blow-up in (3.1) is not caused by the matrix B_bad; it is caused precisely by discarding the original-coordinate independence and replacing the first two coordinates by an arbitrary dependent joint density cap. This is an equation-level use of the required pinned result and a source-valid obstruction to that compression step.

## 7. Consequence for the punctured-pivot programme

The r54 collision estimate showed that a nonzero scalar square can be harmless for the assigned negative-half time integral. The present construction proves that this information alone is insufficient for one-copy density after arbitrary 2D compression, even at perfect determinant and spectrum scale.

The structurally legitimate next routes are therefore:

1. keep enough original product provenance to use the rank-two affine half-Riesz theorem before compression and pair it with an independent complementary resource;
2. expose a zero-pivot 2+1 packet of partner r52 type, where the independent scalar remains on the hyperbolic edge;
3. obtain a positive-half weighted-time estimate from an aggregate two-slope packet and combine it with the negative-half budget by Cauchy-Schwarz in time;
4. or route to the already-paid E3 / Fresnel-frame / grouped-hub / finite-carrier receivers.

What is ruled out is an abstract theorem of the form 'joint 2D density cap + independent scalar cap + invertible 3x3 determinant + bounded A_- implies bounded density'. The family above has all those properties except the desired conclusion.

The unrestricted QFORM conjecture remains OPEN. Unrestricted continuity remains OPEN.
