# Quantitative checks for account03/B14 auto11

These are arithmetic/spectral checks only; the proof is in REPORT.md.

## 1. r=12/7 constants

For the general partner+receiver bound

    C(r)=2^[(9r-7)/(6r)] [6r/((3r-4)(2-r))]^(1/r),

at r=12/7:

    3r-4=8/7,
    2-r=2/7,
    6r/((3r-4)(2-r))=63/2,
    (9r-7)/(6r)=59/72.

Hence

    C(12/7)=2^(59/72)(63/2)^(7/12)
            =13.203584441928335...

At |h|>=2^(-1/2), |gamma|>=1 and R_0>=1, the h factor contributes 2^(7/36), so

    C_norm=2^(73/72)(63/2)^(7/12)
          =15.108642933903862...

For the target family in REPORT Section 5, gamma=1/2 and d^2+||c||^2=2. Thus

    C_target
      = C(12/7) * 2^(7/36) * 2^(-5/24)
      = 2^(29/36)(63/2)^(7/12)
      = 13.077082846480915...

## 2. Receiver-star spectrum

For a_m=(1,...,1)/sqrt(m), the matrix on (W,Z_1,...,Z_m) is

    B_m = [[1,a_m^T],[a_m,0_m]].

Its kernel contains the (m-1)-dimensional subspace of Z orthogonal to a_m. On span{W,a_m}, its matrix is exactly

    [[1,1],[1,0]],

so the two nonzero eigenvalues are exactly

    lambda_+ = (1+sqrt(5))/2 = 1.618033988749895...,
    lambda_- = (1-sqrt(5))/2 = -0.618033988749895...

for every m.

Numerical diagonalisation at m=1,2,10,100 reproduces these values to floating precision.

## 3. Core spectrum and leverage gate

Use the coefficient-space frame rows

    r_0=(1,0,0),
    r_1=r_2=(0,1/sqrt(2),0),
    r_3=r_4=(0,0,1/sqrt(2)).

Their column Gram matrix is I_3. With

    M_core=[[0,1,0],[1,0,0],[0,0,1/2]],

its nonzero physical spectrum is exactly {1,-1,1/2}. Coordinate 0 has leverage c=1>1/2 and physical null pivot A_00=0. Every residual transverse row has v_j^2+w_j^2=1/2, exactly meeting the account04/B14 r9 diffuse gate.

The direct sum with B_m therefore has large eigenvalues 1,-1,(1+sqrt(5))/2. This verifies the original three-large-eigenvalue hypothesis while the partner core by itself has only two eigenvalues of modulus >=1.
