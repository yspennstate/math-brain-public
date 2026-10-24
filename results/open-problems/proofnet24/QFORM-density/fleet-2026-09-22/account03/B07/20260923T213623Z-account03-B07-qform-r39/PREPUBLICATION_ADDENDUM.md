# r39 pre-publication arithmetic addendum — authoritative for Section 5 integers

The mathematical theorem `QFORM-O0-DIRECT-Z3-PAYMENT-v1`, its density constant, the Hadamard inequality (5.2), and the dimension lower bound `n>=5730381` are unchanged.

A final high-precision readback caught one **numerical transcription issue** in the huge integer in REPORT.md equation (5.3): the first checker used binary64 arithmetic to take the ceiling of a number of order `10^39`, which cannot certify its final digits. Recomputing the same exact expression with 120-digit Decimal arithmetic gives

`h=(2 sqrt(2)-1)/1572864`

and

`65536/(27 h^6)
 =983551868769507679208432245932178290487.964907683674353835367512756965431069096163218920964461551632837451267369361525256...`.

Therefore the authoritative integer is

`boxed: N0 >= 983551868769507679208432245932178290488.`

The exact combinatorial binary search still gives

`boxed: n>=5730381`, 

with `binom(5730380,3)binom(5730377,3)<N0<=binom(5730381,3)binom(5730378,3)`.

`CHECKS.py` and `CHECKS.txt` were corrected before publication and now use high-precision Decimal arithmetic for this huge-number step. The exact integer overlap identities and the main analytic proof never depended on the erroneous low-order digits of the first floating-point printout.
