# r35 finite algebra/numerical check

For `G_*=(U_1+U_2)/sqrt(2)` with iid `U_i~Unif[-1/2,1/2]`,

`p_*(x)=sqrt(2)(1-sqrt(2)|x|)` on `|x|<=1/sqrt(2)`.

For `H_1(x)=min((2|x|)^(-1),sqrt(2/|x|))`, the crossing solves

`1/(2x)=sqrt(2/x)` => `x=1/8`.

The exact two integrals are

`J_1=2∫_0^(1/8) sqrt(2)(1-sqrt(2)x)sqrt(2/x)dx=2sqrt(2)-1/6`,

`J_2=2∫_(1/8)^(1/sqrt(2)) sqrt(2)(1-sqrt(2)x)/(2x)dx=(5sqrt(2)/2)log2-sqrt(2)+1/4`.

Hence

`J_1+J_2=1/12+sqrt(2)+(5sqrt(2)/2)log2=3.9481922543777963...`.

Partner cap-only constant:

`6 exp(-1/3)=4.299187863442736...`.

Relative certificate reduction:

`1-(J_1+J_2)/(6 exp(-1/3))=0.0816423055269482...`.

This file checks only the elementary integration/constants; the mathematical proof is in `REPORT.md`.
