# Independent checks and attempted counterexamples

All checks are analytic. No computed spectral gap or simulated trajectory is
claimed. The constants below refer to the half squared loss and fixed prior
N(0,I_2) in PROOF.md.

## Earlier theorem

Gaussian moment generation in the output coordinate gives the factor
`exp(g(w)^2/(2 lambda^2))` without completing a square. A neighborhood of
a maximizer gives `lambda^2 log Z -> M^2/2`. At the separating line w=0,
g=0. An odd cutoff supported across that line therefore has exponentially
small energy and variance tending to one. The bounded-density ratio and
Lipschitz shear supply the reverse exponential inequality. This checks the
earlier LSI and Poincare exponent `-M^2/2` independently of its variational
barrier argument. The sign perturbation is invisible to every neuron feature,
exactly as the earlier report states.

A different-coordinate check avoids the earlier w-strip upper bound entirely.
Fix r>0 and set `Q_lambda=p_lambda(|a|<=r)`. Direct integration before
eliminating a gives

```
Q_lambda
 = Z_lambda^-1 int_{|a|<=r} int exp(a g(w)/lambda) gamma(dw) gamma(da)
 <= exp(rM/lambda)/Z_lambda.
```

The neighborhood lower bound for Z and the bound `Z<=exp(M^2/(2lambda^2))`
give `lambda^2 log Z -> M^2/2`. It follows that Q_lambda tends to zero
and `limsup lambda^2 log Q_lambda <= -M^2/2`. The a marginal is even:
change w to -w in its density at -a. The odd clipped-linear test in a,
with slope 1/r on [-r,r], therefore has mean zero, variance at least 1-Q,
and energy Q/r^2. Its Rayleigh quotient is at most `Q/[r^2(1-Q)]`.
This reproduces the unrestricted Poincare upper exponent by an output-weight
bottleneck, independently of the earlier hidden-weight bottleneck. LSI is
at most Poincare in the conventions used here. Combined with the earlier
verified density-comparison/shear lower bound, both exact exponents follow.
This new test is also S-odd and invisible to predictions.

## The folded marginal bound by a second method

Write q for its normalized density, F for its CDF, and
`D=c exp(c^2/2)`. The ratios (13) and (15) of PROOF.md imply

```
F(x) <= c exp(c^2/2) q(x)         for 0<=x<=c,
1-F(x) <= q(x)/c                 for x>=c.
```

Since c>1, these imply `min(F(x),1-F(x)) <= D q(x)` for every x.
Let m be the unique median. If v(m)=0, the fundamental theorem of calculus
and Tonelli give

```
int |v| q
 <= int_0^m |v'(s)| F(s) ds
    + int_m^infinity |v'(s)| (1-F(s)) ds
 <= D int |v'| q.
```

Apply this to `v=(u-u(m))^2`. Cauchy--Schwarz then gives

```
int (u-u(m))^2 q <= 2D sqrt(int (u-u(m))^2 q) sqrt(int u'^2 q),
Var_q(u) <= 4 c^2 exp(c^2) int u'^2 q.
```

This looser, temperature-independent coefficient confirms the central
uniform-in-lambda marginal claim without the anchored weighted-Cauchy
estimate used in the proof. Truncation handles infinite intermediate
integrals before passing to the finite-energy class.

## The two precise anchored constants

For the left side, view `u(r)-u(c)=-int_r^c u'(s) ds` as an operator from
weighted derivative L2 to weighted function L2. In unweighted coordinates
its kernel is `1_{r<=s<=c} sqrt(q(r)/q(s))`. The squared Hilbert--Schmidt
norm is at most

```
int_0^c int_r^c exp(c^2/2) ds dr = c^2 exp(c^2/2)/2.
```

The operator norm is at most the Hilbert--Schmidt norm, reproducing precisely
the first coefficient in (12).

For the right side, differentiation gives
`q'/q=-r+g(r)g'(r)/lambda^2 <= -c` for r>=c. Put v=u-u(c), so v(c)=0.
For bounded functions, integration by parts gives

```
int_c^infinity v^2 q
 <= -(1/c) int_c^infinity v^2 q'
 = (2/c) int_c^infinity v v' q
 <= (2/c) sqrt(int_c^infinity v^2 q) sqrt(int_c^infinity v'^2 q).
```

The boundary term at infinity vanishes because q has Gaussian or faster
decay on this half-line. This gives `4/c^2`, the same coefficient as (17).
Truncation extends the result. These two checks recover the exact constants
by different arguments.

## Remaining load-bearing factors

- The exact largest singular value of the shear derivative with entry
  `k=g'/lambda` is `(sqrt(k^2+4)+|k|)/2`, which is at most `1+|k|`.
  Its square agrees with the proof's energy factor. The Gaussian factor's
  Poincare coefficient is one, checked by the equality test h(b)=b.
- `c>1` and `c<2` follow directly from the critical equation. Thus
  `c^2 exp(c^2/2)/2 <= 2e^2` and `4/c^2 < 4 < 2e^2`.
  For lambda<=1, `(1+L/lambda)^2 <= 4/lambda^2`, giving
  `beta_S >= lambda^2/(8e^2)` with no numerical root estimate.
- The invariant-space energy decay has factor `2 lambda beta_S`, since
  the generator's Dirichlet form is `lambda int |grad h|^2`. Thus the
  coarse chi-square exponent is at least `lambda^3/(4e^2)`.
  This also follows from differentiating `int q_t^2 dp` directly in the
  Fokker--Planck equation. Dropping the factor lambda would give the wrong
  physical time normalization.
- Integrating `q_0^2 p=Z exp(-ag/lambda) pi` in a gives `Z^2`. As a second
  check, the general identity `int (pi/p)^2 p = int pi^2/p` gives
  `Z E_pi exp(-ag/lambda)=Z^2`. Therefore the large initial chi-square norm
  contributes `M^2/lambda^2` to the logarithmic time bound, and multiplying
  by the inverse decay rate gives order lambda^-5, not exponential time.
- The predictor estimate uses `int a^2 dp <= 1+M^2/lambda^2`, from the
  conditional variance one and conditional mean g/lambda. Its square root
  multiplies the square root of chi-square; the displayed squared predictor
  estimate has exactly one factor `1+M^2/lambda^2`.

## Frozen teacher-risk asymptotic checked with the kernel

Let

```
K(w,v) = [exp(-(w-v)^2/2)-exp(-(w+v)^2/2)]/2.
```

Directly expanding the risk, independently of the predictor limit, gives

```
R(p_lambda)
 = (1/(2 lambda^2)) int int g(w)g(v)K(w,v) nu_lambda(dw)nu_lambda(dv)
   - (1/lambda) int g(w)^2 nu_lambda(dw) + K(1,1)/2.
```

The kernel and g are bounded continuous functions. As nu_lambda tends to
the equal mixture at +/-c, every term in the leading double integral has
value `M^2 K(c,c)`; the signs cancel in the mixed-sign pairs. Hence
`lambda^2 R -> M^2 K(c,c)/2 = M^2(1-exp(-2c^2))/4`, agreeing with (34).
The cross term is order lambda^-1 and cannot cancel the leading positive
lambda^-2 term.

## Attempts to break the conclusion

- Folding only w without also identifying the output sign would be wrong
  for general functions. The proof instead conditions on w>0 and uses
  invariance of h, h^2 and its gradient norm to equate full and conditional
  integrals. It proves an inequality for a larger half-plane function class;
  a boundary identification is not assumed or imposed on the diffusion.
- The odd cutoff from the earlier proof is not S-invariant. Multiplying it
  by a makes it invariant but adds the output derivative. Specifically for
  `H=a h_r(w)` with `|h_r|<=1` and `h_r^2=1` outside the central strip,
  its energy is at least `E h_r^2 >= 1-nu_lambda([-r,r])`, while its variance
  is at most `E a^2 <= 1+M^2/lambda^2`. Its Rayleigh quotient is therefore
  at least `(1-nu_lambda([-r,r]))/(1+M^2/lambda^2)`. This cannot reproduce
  the earlier exponential bottleneck.
- The proof never assumes strong log-concavity. In fact the folded density
  can be non-log-concave. What is used is monotonicity of g^2 on each side
  of c, and the Gaussian tail ratio after c.
- The spectral gap estimate holds for all lambda>0. Only the convenient
  simplification (6) and its displayed runtime use lambda<=1.
- The prediction features `a sin(wx)` are invariant and have finite energy
  under p_lambda for each x. The argument applies to their symmetry class;
  it does not claim a quotient LSI or an unrestricted spectral gap.
- The frozen linear diffusion is not MFLD. Its equilibrium has divergent
  teacher risk, as shown twice above. In the nonlinear equation the residual
  correlation (35) changes with the predictor. Single-peak geometry at
  initialization does not prove the same geometry later.
- Nothing here establishes a lower bound or upper bound for nonlinear
  time to small unregularized risk, or handles annealing. No optimality of
  the power lambda^2 in the quotient bound is claimed.

## Nonlinear symmetrization checked directly on the density equation

For a density r write `r^+(theta)=(r(theta)+r(-theta))/2`. Every feature is
even under theta -> -theta, so its integral depends only on r^+. The
residual-dependent drift b is odd. Therefore the Fokker--Planck operator
`lambda Delta r - div(b r)` sends the even and odd parts of r to even and
odd parts respectively, for each fixed b. Its even part is exactly
`lambda Delta r^+ - div(b[r^+] r^+)`. This independently checks (40), which
the proof derived with weak test functions. A varying common lambda(t)
does not change the parity calculation.

The consequence comparing two solutions uses uniqueness; the equation-level
identity itself does not. This qualification is stated in PROOF.md.
The reduction removes only the S-odd sector. There may still be several
prediction-relevant wells in the even sector once the residual changes.
