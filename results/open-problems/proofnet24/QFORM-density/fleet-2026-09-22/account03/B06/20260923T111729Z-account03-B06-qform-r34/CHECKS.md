# Deterministic checks for r34

These are sanity checks only; the proof is symbolic in REPORT.md/CHECKPOINT.md.

1. For `eta in {0,0.01,0.5,3,100}`, the matrix

`[[-eta,sqrt(1+eta),0],[sqrt(1+eta),0,0],[0,0,1]]`

has numerical eigenvalues respectively

- `{-1,1,1}`
- `{-1.01,1,1}`
- `{-1.5,1,1}`
- `{-4,1,1}`
- `{-101,1,1}`

matching the exact factorisation `(lambda-1)(lambda+1+eta)` of the 2x2 block characteristic polynomial.

2. The near-coloop two-sheet constant is

`2^(13/4) (64/63)^(1/4) = 9.551186867231433`.

The newest ruled one-sheet constant is

`pi sqrt(2) = 4.442882938158366`.

3. The shell-superlevel inequality used in the proof is algebraically exact:

`L_exact = 2/sqrt(a) [sqrt(R+lambda^(-2))-sqrt(R)]`

and

`L_exact / [1/(sqrt(aR)lambda^2)]`
` = 2 sqrt(R)/(sqrt(R+lambda^(-2))+sqrt(R)) <= 1`.

A random floating-point check over 100,000 logarithmically distributed positive `(R,lambda)` pairs produced maximum stable-form ratio exactly `1.0` to machine precision.
