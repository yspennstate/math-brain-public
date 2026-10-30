# r54 retuned interpolation

Normalize K=s=1 and set
d=71801/1000000, p=2699/1000000,
q=709/8000, h=41719/500000.

No scalar/pair pivot implies |A_ii|<d and |A_ij|^2<=p+d^2<q^2. Exact slack:
q^2-(p+d^2)=439/62500000000.

The three margins in the source sampled-interpolation proof are
1-d-h=844761/1000000,
1-d-q-4h=252911/500000,
1-d-2q-9h=7/1000000.
All are positive.

Therefore the identical proof gives, for 1<=k<=3,
no pivot and s_(4k-3)(A)>=1  =>  V_k(A)>=h^(2k).

A fair literal coordinate cut then gives
Z_3^(-1/6)<=2/h and
Z_2^(-1/8)<=sqrt(2/h).
No rotated random coordinates are introduced.
