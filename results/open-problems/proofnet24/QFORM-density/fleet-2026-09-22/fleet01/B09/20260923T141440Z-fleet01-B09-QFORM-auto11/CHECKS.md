# Finite checks for fleet01/B09 20260923T141440Z

These checks verify arithmetic and finite matrices only; they are not substitutes for the universal proof in REPORT.md.

## Constant in QFORM-INDEFINITE-PAIR-PLUS-ONECROSS-v1

For `gamma=1/8`,

`c_gamma = 2^(1-gamma) Gamma((1-gamma)/2)/(2 sqrt(pi) Gamma(gamma/2))
          = 0.0676665159158548...`.

The fleet03/B01 fractional compiler gives

`C_* = 32 c_gamma e^(1/8) pi^(1/8) 2^(-1/16)
     = 2.71106520785432...`.

With `A0=2sqrt(2)` and

`B0=(8/e) 2^(1/8) C_* = 8.70090081748689...`,

minimizing `A0/r+B0 r^(1/4)` yields

`K_*=(5/4)(4A0)^(1/5) B0^(4/5)
    =11.4625801249411... <11.463`.

Scaling check for the pair-anchored volume form:

`D^(-2/5) kappa^(-1/10) Delta^(1/20) V^(-1/20)`

scales under `A -> sA` as

`s^(-4/5) s^(-1/10) s^(4/20) s^(-6/20)=s^(-1)`.

## Six-coordinate zero-pivot stress matrix

Nonzero edges are `(1,2),(1,4),(2,5),(3,6)`, all weight one. It is the disjoint union of the adjacency matrix of `P4` and one edge, after relabeling. Hence its spectrum is exactly

`{phi, phi^(-1), 1, -1, -phi^(-1), -phi}`,

`phi=(1+sqrt(5))/2`.

Numerically:

`{-1.61803398875,-1,-0.61803398875,0.61803398875,1,1.61803398875}`.

For `P={1,2}`, `U={3}`, `V={4,5,6}`:

`E=[[0,1],[1,0]]`, so `D=kappa=1`;
`a=(1,0,0)`, `b=(0,1,0)`, so `Delta=1`;
`m_3=c_3=(0,0,1)`, so `V_P=||C||_F^2=1`.

Thus the REPORT theorem gives `<11.463` for every admissible cap-one product law.

## Partner-application matrix

The `5x3` cross matrix has rows

`(1,0,0)`, `(0,1/sqrt2,0)`, `(0,1/sqrt2,0)`, `(0,0,1/sqrt2)`, `(0,0,1/sqrt2)`.

Its Gram matrix is exactly `M^T M=I_3`; therefore the symmetric cross-only matrix `[[0,M],[M^T,0]]` has nonzero spectrum

`{-1,-1,-1,1,1,1}`

and two additional zeros.

The four selected nonzero `3x3` minors each have determinant magnitude `1/2`, hence squared weight `1/4`; total `Z=1`. Each non-anchor physical row appears in exactly two of the four equally weighted minors, so every non-anchor row marginal equals `1/2`. The partner theorem gives

`5*2^(4/5)*sqrt(e)=14.352952309263... <14.353`.
