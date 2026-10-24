Model actually run: **GPT-5.6 Sol. Reasoning level: UNVERIFIED — not GPT-6 maximum.**

# HARD7-06 idea-before-checker checkpoint — stationary finite-support ACG descent

Target remains canonical claim `F0095`: the fixed-`k=3` constant-location problem for ordinary sparse Erdos--Renyi 3-colourability. The fixed metric is `W_3=U_3-L_3` with `L_3=4.03` and incoming exact `U_3=4.686507635`.

This run deliberately does not continue cavity quantization with the previous B7/B8/B10 triple. It tries **B5 / B19 / B24**.

## B5 — add a deformation parameter and differentiate numerically before certifying anything

The incoming four-atom witness has support architecture `(alpha_1,alpha_2,alpha_3,1)` and weights `(w_1,w_2,w_3,w_4)`. Keep the boundary atom `alpha_4=1`, but free all three interior locations and all four weights (three independent after normalization). In unconstrained coordinates use softmax weights and logits for the three interior supports. For fixed `d`, minimize the exact ACG finite-support objective numerically only as a *discovery device*.

The important observation is structural: the cavity-quantized witness is not stationary inside this seven-dimensional manifold. A deterministic local descent moves substantial mass and support locations rather than merely changing the last decimal digit:

```
incoming weights  = (0.15333616, 0.28476429, 0.48318715, 0.07871240)
incoming support  = (0.56153802, 0.26488215, 0.06698304, 1)

descent weights   ~= (0.124850142907, 0.374444818986, 0.426458481720, 0.074246556387)
descent support   ~= (0.625207841412, 0.257440439986, 0.056067259169, 1)
```

At `d=4.686507635`, summing the Poisson/multinomial vertex term through total degree 28 gives approximately `Sigma=-8.95e-10`, compared with about `-2.57e-10` for the incoming certified law. The numerical calculation is not a theorem and is used only to select a rational candidate.

## B19 — make the search an explicit algorithm

The exploratory algorithm is:

1. parameterize weights by softmax and interior support points by logits;
2. evaluate the four-atom ACG functional by exact enumeration of all multinomial count vectors conditional on total Poisson degree `n<=28` in floating point;
3. run local constrained descent from the incoming certificate;
4. round the resulting law to a fixed rational grid;
5. decrease `d` until the rounded law still has a visible negative margin;
6. only then invoke the one-sided exact `Fraction` certificate used in the preceding run.

This separates discovery from proof. No floating-point optimizer output is promoted without step 6.

The rounded rational candidate selected for certification is

```
weights = (12485014, 37444482, 42645848, 7424656) / 10^8
support = (62520784, 25744044, 5606726, 10^8) / 10^8
candidate d = 46865076265 / 10^10 = 4.6865076265.
```

A direct floating-point evaluation through degree 28 gives `Sigma ~= -4.22e-11`; the exact checker will decide the sign.

## B24 — extremal/support-size test

A five-atom deformation was also tested as a counterexample to the hypothesis that the four-atom manifold is already locally extremal. Three separate initial splits of the interior atoms were optimized. In every case the extra support either collapsed toward an existing interior cell or produced a value agreeing with the four-atom stationary value to the `1e-12` scale at the incoming `d`. This is **exploratory evidence only**, not a proof that four atoms are globally optimal.

The useful conclusion is negative but substantive: the next route should not be blind support-size inflation. The four-atom contact equations appear to be the right finite-dimensional object to solve or bound analytically.

## Exact claim to be tested now

For the rational law above and `d=4.6865076265`, prove by one-sided rational logarithm/exponential bounds and exact enumeration through total degree 28 that

`Sigma_d(a_4) < 0`.

If that exact sign passes, the existing Ayre--Coja-Oghlan--Greenhill implication gives the rigorous endpoint movement

`U_3 <= 4.6865076265`, hence `W_3 <= 0.6565076265`.

This would remain PARTIAL: it improves only the rigorous non-3-colourability endpoint and does not prove convergence of the random 3-colourability threshold to a constant.