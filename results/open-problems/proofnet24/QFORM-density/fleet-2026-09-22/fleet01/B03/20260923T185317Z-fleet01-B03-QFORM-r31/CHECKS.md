# Deterministic finite algebra checks

These checks were executed in the current run's Python interpreter. They verify only the determinant/Schur identities, random-cut averages, and displayed constants; they are **not** a probabilistic or numerical proof of QFORM.

The test logic was:

```python
import itertools, numpy as np

# Scalar-pivot overlap-one check.
# For each random symmetric A and each h with |A[h,h]| safely nonzero:
#   S = A[-h,-h] - outer(A[-h,h],A[h,-h])/A[h,h]
#   E1h = sum_{I,K disjoint, |I|=|K|=2} det(A[{h}+I,{h}+K])**2
#   rhs = A[h,h]**2 * sum_{I,K disjoint} det(S[I,K])**2
#   enumerate all cuts L|R of the complement and average
#       Z2(S[L,R]) = sum_{I subset L, K subset R, |I|=|K|=2} det(S[I,K])**2
#   compare average with E1h/(16*A[h,h]**2).

# Disjoint overlap-zero check.
#   E0 = sum_{S,T disjoint, |S|=|T|=3} det(A[S,T])**2
#   enumerate all cuts L|R and average
#       Z3(A[L,R]) = sum_{S subset L,T subset R,|S|=|T|=3} det(A[S,T])**2
#   compare with E0/64.

# Pair-pivot overlap-two check.
# For each nonsingular principal pair H:
#   B=A[H,H], S=A[R,R]-A[R,H]@inv(B)@A[H,R]
#   E2H=sum_{i!=j in R} det(A[H+{i},H+{j}])**2
#   rhs=det(B)**2 * sum_{i!=j} S[i,j]**2
#   enumerate all cuts L|R2 of the complement and average
#       Z1(S[L,R2]) = sum_{i in L,j in R2} S[i,j]**2
#   compare with E2H/(4*det(B)**2).
```

Fixed-seed results on real symmetric `7x7` Gaussian matrices:

* 30 matrices, overlap-one scalar-Schur determinant identity: maximum relative discrepancy `1.3374914839110293e-15`.
* Same 30 matrices, exact all-cut average `E Z2=E1(h)/(16 a^2)`: maximum relative discrepancy `9.053093319388847e-16`.
* 10 matrices, exact all-cut disjoint identity `E Z3=E0/64`: maximum relative discrepancy `3.8022510758302244e-16`.
* 20 matrices, overlap-two pair-Schur identity: maximum relative discrepancy `8.89341179507158e-16`.
* Same 20 matrices, exact all-cut average `E Z1=E2(H)/(4D^2)`: maximum relative discrepancy `8.626762647381183e-16`.

Independent constant evaluation:

```text
K1 = 2^(3/4)*sqrt(pi)                         = 2.98090017885818...
H1 = sqrt(2*e)*Gamma(1/4)                    = 8.453631522124514...
C1 = 8*sqrt(2)*(2*e)^(1/4)                   = 17.275717919798065...
C2 = 8*e^(1/4)*sqrt(Gamma(1/4))              = 19.55933769831132...
partner-heavy = 8*2^(5/8)                    = 12.337686603263526...
latest partner Z3 coefficient                = 10.550168831164775...
latest partner disjoint E0 coefficient       = 21.10033766232955...
latest partner E0 coefficient at theta=1/4   = 26.58475958065858...
```

Every identity checked here also has an exact symbolic proof in `REPORT.md`; these computations are regression checks only.
