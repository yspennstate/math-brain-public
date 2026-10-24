# Literature transfer and partner application

## Sharp product-projection source
Livshyts--Paouris--Pivovarov, "On sharp bounds for marginal densities of product measures", Israel J. Math. 216 (2016), arXiv:1507.07949, prove that every d-dimensional orthogonal marginal of a product density with one-dimensional factors bounded by one has density bounded by 2^(d/2). Scaling gives 2^(d/2) K^d.

This is an exact hypothesis match for the product-projection steps used here: no iid, moment, support, log-concavity, smoothness, Gaussianity, centering, or connected-support condition appears. It is a joint marginal bound and is never treated as independence after rotation.

Rudelson--Vershynin, "Small ball probabilities for linear images of high dimensional distributions", IMRN 2015, is compatible with the scalar linear-image step. Kwan--Sauermann's quadratic Littlewood--Offord theorem controls point probabilities (and has a discrete arbitrary-distribution extension via fixing boxes), not interval-length-linear density under the present spectral hypothesis. Herry--Malicet--Poly require iid inputs with a sufficiently smooth Gaussian-field representation and therefore do not cover the owner's rough non-iid class.

No exact published solution matching all unrestricted QFORM quantifiers was found in this targeted source check.

## Designated account04/B18 result applied to a live inequality
The completed account04/B18 grouped-Fourier receiver is pinned at commit
95f366162de5f788f357d2dac97ae6e6a5849503.
Its order-three constant is
[
C_3^{partner}=3sqrt2,e,(9/2)^{1/6}=14.818337662843ldots.
]

The new account01/B03 diffuse-near-bipartite router, commit
bd3baec1f47e33138b85272a08fc158e562f2319,
shows that if sigma=s2(M), a physical recut satisfies
[
s_3(A_{I,J})ge sigma/16.
]
Applying the completed partner receiver gives the actual inequality
[
|p_Q|_infty
le {16C_3^{partner}oversigma}K^2
< {237.093403oversigma}K^2.
]
At the live no-pivot floor sigma>0.237 this is <1000.395 K^2.

Replacing only the product-projection and Fourier-power constants by the sharp LPP theorem gives
[
C_3^{sharp}=6sqrt2(9/2)^{1/6}=10.902723556993ldots
]
and therefore
[
|p_Q|_infty
< {174.443577oversigma}K^2
<736.049K^2
qquad(sigma>0.237).
]
This is an equation-level literature-to-proof transfer on the current four-eigenvalue router.

## Frontier
The newest account01/B06 structural theorem leaves, after already-paid branches, only a two-hub configuration with
[
0<|A_{HH}|<(1+sqrt2)/10000,qquad
|det A_{HH}|<10^{-8},qquad
lambda_{min}(A_{HR}A_{HR}^T)>9cdot10^{-5},
]
with arbitrary leaf curvature and affine terms. THEOREM.md pays the exact endpoint A_HH=0. The small nonzero hub-block glue remains open.

The full unrestricted s3 density conjecture remains OPEN / NOT PROVED / NOT DISPROVED.
