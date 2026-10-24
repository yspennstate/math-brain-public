# account03/B03 r40 deterministic checks

No Monte Carlo or histogram is used in the proof.

## 1. Affine factorization

For symmetric invertible P, U=X-X', V=X+X',

U^T P U - V^T P V = -4 X^T P X'.

With

a=(1/4)P^{-1}(-ell_-+ell_+),
b=(1/4)P^{-1}( ell_-+ell_+),

we have

-4(X-a)^T P(X'-b)
= -4X^T P X'
  +(ell_-+ell_+)^T X
  +(-ell_-+ell_+)^T X'
  -4a^T P b.

Therefore S=A(U)+B(V) equals this expression plus

c=d_-+d_+ +4a^T P b.

A finite random numerical substitution check over five nonsingular symmetric 2x2 matrices gave absolute residuals

1.7763568394002505e-15,
2.220446049250313e-16,
1.7763568394002505e-15,
0,
1.7763568394002505e-15,

consistent with floating-point roundoff. The proof itself is the exact displayed expansion above.

## 2. Scalar cap half-Riesz constant

For density cap M,

int_0^infty min(1,2M t^{-2}) dt
= sqrt(2M) + 2M/sqrt(2M)
=2sqrt(2M).

## 3. Two-dimensional radial constant

For joint density cap M,

int_0^infty min(1,M pi t^{-4}) dt
=(M pi)^{1/4}
 +(M pi)/(3(M pi)^{3/4})
=(4/3)(M pi)^{1/4}.

## 4. Bilinear constants

The conditional scalar projection cap is

M_x <= sqrt(2)/||C^T(x-a)||.

Therefore the conditional half-Riesz coefficient is

2sqrt(2 M_x)
<=2^(7/4)||C^T(x-a)||^{-1/2}.

Averaging the transformed-vector radial estimate gives

C_2=(4/3)2^(7/4)pi^(1/4)
   =5.97074738624132....

For C=-4P,

|det C|^{-1/4}=16^{-1/4}|det P|^{-1/4}
              =(1/2)|det P|^{-1/4},

so

C_pair=(4/3)2^(3/4)pi^(1/4)
      =2.9853736931206605....

The whole-copy time coefficient is

C_time=sqrt(2pi) C_pair
      =(4/3)2^(5/4)pi^(3/4)
      =7.483222109515818....

If |lambda_1(P)|,|lambda_2(P)|>=1/2 and |d|>=1, then |det P|^{-1/4}<=sqrt(2), and

sqrt(2) C_pair=4.221955965563093....

## 5. Spectrum of the concrete control family

For

M=[[0,-2P,0],[-2P,0,0],[0,0,d]],

if Pe=lambda e then

M(e,e,0)=-2lambda(e,e,0),
M(e,-e,0)= 2lambda(e,-e,0),

and the Z-axis eigenvalue is d. Hence the spectrum is exactly

{2lambda_1,-2lambda_1,2lambda_2,-2lambda_2,d}.

## 6. Correction audit

- No pointwise law-uniform quadratic-phase decay is used.
- No independence of U and V is asserted.
- No conditional cap for U|V or V|U is used.
- The only conditional density cap is for a linear form of a genuine independent original product bank Y after fixing X.
- The deterministic transform C^T(X-a) is allowed to have dependent coordinates; only its joint-density Jacobian cap is used.
- No moment, compact-support, log-concavity, connected-support, or Gaussian assumption enters.
- Continuity is not claimed.

QFORM_B03_R40_CHECK_PASS
