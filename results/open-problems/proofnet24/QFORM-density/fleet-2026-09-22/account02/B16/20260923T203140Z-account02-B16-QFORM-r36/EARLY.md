# account02/B16 r36 — early calculation

SIGNED IN - working on the quadratic-form bounded-density conjecture (universal constant), account account02, slot B16, 2026-09-23T20:31:40Z.

The fresh-hub canonical form appearing in the current two-bank work has a stronger zero-pivot reduction than the absolute-Fourier estimate suggests. If H is independent of the light variables, f_H<=1, (L,V) has joint density cap M, and T is any light-measurable random variable, then

Q = 2 gamma H L + 2 L T + alpha L^2 + 2 delta L V + kappa V^2

with gamma*kappa != 0 can be rewritten using Y=H+T/gamma as

Q = 2 gamma Y L + alpha L^2 + 2 delta L V + kappa V^2.

Conditional on (L,V), Y is a mixture of translates of the fixed independent hub density, hence ||p_{Y|(L,V)}||_infinity<=1. The coefficient matrix in (Y,L,V) has zero Y-diagonal and determinant -gamma^2 kappa. Therefore the completed zero-pivot conditional-trace theorem gives

||p_Q||_infinity <= 3*2^(2/3) M^(2/3) |gamma^2 kappa|^(-1/3).

In particular, for Q_epsilon=2HL+beta L^2+V^2+2 epsilon L P, take T=epsilon P, gamma=kappa=1. The current two-bank hypotheses imply M<=min(M_{2,A},M_{2,B}) by convolution, so the bound is uniform in epsilon and beta at every target; the logarithmic all-target loss of the absolute-Fourier receiver is not needed for essential boundedness. For a genuine orthonormal product projection, the pinned two-dimensional projection theorem gives M<=2 and hence ||p_Q||_infinity<=3*2^(4/3)=7.5595262994. Continuity/Hölder regularity remains a separate question.

This also recovers the account03/B16 true-near-coloop a=0 endpoint by taking H=X_0, L=U, T=bS, gamma=b*sqrt(c), and kappa=w, since |gamma^2 kappa|=c|det Lambda|. The punctured a!=0 collar is therefore isolated to the actual fresh hub square; all light terms divisible by the hub partner L can be absorbed without any projected-independence or conditional-projection-cap inference.
