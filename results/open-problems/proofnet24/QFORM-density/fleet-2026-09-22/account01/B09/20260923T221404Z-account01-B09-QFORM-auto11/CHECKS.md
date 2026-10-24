# Deterministic checks — third-compound overlap decomposition

These checks support algebra/arithmetic only; they are not substitutes for the universal proof.

## Random symmetric 8x8 regression

Using a fixed NumPy seed 12345, a random real symmetric 8x8 matrix A and physical triple T=(0,2,5) gave

- det((A^2)[T,T]) = 25.86212637123451
- overlap-0 term det(CC^T) = 5.025639710117449
- overlap-1 term sum ||P(c_r x c_s)||^2 = 11.64240926743441
- overlap-2 term ||adj(P)C||_F^2 = 7.6867263474315655
- overlap-3 term det(P)^2 = 1.507351046251108
- sum of four terms = 25.862126371234535
- difference = -2.49e-14.

Summing over all 56 column triples:

- sum_T det((A^2)[T,T]) = 1652.5176755905964
- direct overlap-class sums (E0,E1,E2,E3) =
  (188.06043259, 733.70863506, 624.71548666, 106.03312129)
- their sum = 1652.5176755905948
- direct eigenvalue computation of e3(A^2) = 1652.5176755905982.

## Random-cut constant

The no-marginal physical D3 constant is

C3 = 3*2^(4/3)*exp(1/3) = 10.550168831164775.

If E0>=1/4, a literal random bipartition captures Z3>=E0/64>=1/256, hence

C3*(1/256)^(-1/6)
 = 3*2^(8/3)*exp(1/3)
 = 26.58475958065858 < 26.585.

## Designated-partner target regression

For s>0, on physical coordinates (Y1,Y2,Y3,Z1,Z2), define

Q_s = 2s Y1 Y3 + 2Y1 Z1 + 2Y2 Z2.

Its symmetric coefficient matrix is the orthogonal direct sum, after reordering, of

[[0,s,1],[s,0,0],[1,0,0]]

and

[[0,1],[1,0]].

Therefore the spectrum is

{+sqrt(s^2+1), -sqrt(s^2+1), +1, -1, 0},

so the owner hypothesis holds for every s>0. For L={Y1,Y2,Y3}, R={Z1,Z2},

C=[e1,e2], w=e3, ||w||=1,
P w=s e1, ||P w||=s.

Account02/B09 QFORM-3x2-KERNELDERIVATIVE-L1-v1 therefore gives

||p_Qs||_infinity <= C_KD s^(-1/5),
C_KD=6.834830666196632.

At s=32, s^(1/5)=2 and

||p_Q32||_infinity <= 3.417415333098316 < 3.418,
P{Q32 in I} < 3.418 |I|,

with a continuous density. The anchored one-overlap currency for this L is V_L=s^2=1024, while the anchored disjoint third-volume det(CC^T) is zero because rank(C)=2.
