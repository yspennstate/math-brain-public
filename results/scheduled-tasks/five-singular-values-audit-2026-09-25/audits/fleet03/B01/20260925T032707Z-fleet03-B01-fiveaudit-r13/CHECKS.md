# r13 exact checks

All inequalities below are analytic certificates, not numerical evidence.

1. Exponential:
e < sum_{n=0}^6 1/n! + (1/7!)/(1-1/8)
= 1957/720 + 1/4410 = 31967/11760.
Also e > 1+1+1/2+1/6 = 8/3.

2. Line 465:
On [0,1], e^{-x} <= 1-x+x^2/2-x^3/6+x^4/24, so
int_0^1 x^{-3/4}e^{-x} dx <= 67243/19890.
The tail is <=e^{-1}<3/8. Hence Gamma(1/4)<298807/79560.
Since 2^(1/4)<119/100 and e^(3/4)<2119/1000,
2*2^(1/4)*e^(3/4)*Gamma(1/4)
< 340938787/18000000 = 18.9410437222... < 19.
Exact margin: 1061213/18000000.

3. C3:
sqrt(2)<99/70, e<68/25, (9/2)^(1/6)<257/200.
Thus C3<14.8296342857...<15.

4. C2:
sqrt(e)<1649/1000 because (1649/1000)^2-31967/11760
=135047/147000000>0.
Also 2^(-1/8)<459/500. Hence C2<12.110256<12.2.

5. log2:
At x=347/500 the positive exponential partial sum through degree 5 exceeds 2 by
5753852769007/3750000000000000, so log2<347/500.

6. Diagonal-pivot contribution:
pi<22/7, log2<347/500, log19<3, sqrt12<693/200 give
sqrt12*(pi+4+4log2+4log19)<75.94884<76.

7. Indefinite terminal:
log2<347/500, log19<3 and 1/e<3/8 give
16*(8+4log2+2log19)+1/e < 268.791 < 269.
