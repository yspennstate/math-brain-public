# Deterministic checks — fleet01/B20 20260924T051854Z

These are self-checks of constants/algebra in `REPORT.md`; they are not independent audits.

Let

- `eps=2^-16=0.0000152587890625`;
- `alpha=1/16`;
- `g=1/2-sqrt(alpha/2)=1/2-1/(4 sqrt(2))=0.32322330470336313...`;
- `c=g/2-eps=0.16159639356261907...`;
- `h=1/8-eps=0.1249847412109375`;
- `eta12=3 eps/sqrt(2)=0.000032368779656366614...`.

Then

`c^4 eps^2 = 1.5876939700448584e-13`.

Using the inherited physical-E3 constant

`C_E3=8.4530212255281768747...`,

`C_E3*(c^4 eps^2)^(-1/6)=1148.7287579750073...<1148.729`.

The same-bank spectral threshold is

`1/2-eta12=0.49996763122034366...`.

## Algebra checks

1. Paving expectation:

`E ||U_I^T U_I-I/2||_F^2 = (1/4) sum_i ell_i^2 <= (alpha/4) sum_i ell_i = alpha/2`, because `sum_i ell_i=2`.

2. Therefore one coloring has operator deviation at most `sqrt(alpha/2)=1/(4 sqrt(2))`, and both color Grams are at least `g I_2`.

3. Quadrant core:

`s_2(U_a Sigma V_b^T)>=sqrt(g) s_2(Sigma) sqrt(g)>=g/2`; subtracting the retained SVD tail costs at most `eps` in operator norm.

4. For a crossed cut with `s_2>c` and Frobenius rank-two tail at least `eps`,

`e_3 >= s_1^2 s_2^2 sum_{r>=3}s_r^2 > c^4 eps^2`.

5. Four-bank balanced-cut identity: every unordered pair of distinct banks crosses exactly two of the three `2+2` cuts, hence the sum of the three symmetric cut extensions equals twice the exact four-bank off-diagonal matrix.

6. Each rank-two cut approximant has symmetric extension rank at most four. The half-sum of three such extensions therefore has rank at most twelve.

7. Symmetric extension doubles squared Frobenius norm, hence the carrier residual is at most `(1/2)*3*sqrt(2)*eps=3 eps/sqrt(2)`.
