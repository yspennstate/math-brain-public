# Quantitative checks for account03/B14 r38

The theorem uses

`A = 4 sqrt(pi)/( |h| sqrt(|gamma|) )`,

so

`K = sqrt(pi A) = 2 pi^(3/4)/(sqrt(|h|)|gamma|^(1/4))`.

At unit partner scale `|b|>=1`, `c>1/2`, `|gamma|>=1`, and `h=b sqrt(c)`, hence

`|h|>2^(-1/2)` and

`K < 2 pi^(3/4) 2^(1/4) = 5.612416582136864...`.

For an envelope `|phi(t)|<=min(1,K|t|^(-3/4))`, choose `t0=K^(4/3)`. Then

`int_R |phi|^2 <= 2[t0+K^2 int_t0^infty t^(-3/2)dt] = 6K^(4/3)`.

Thus

`||p||_2 <= sqrt(3/pi) K^(2/3) < 3.086163688434105`.

Endpoint example: for independent `X,L,W~Unif[-1/2,1/2]`, `U=X+L` has triangular density `1-|u|` on `[-1,1]`. Hence on `0<s<1/4`,

`p_(U^2)(s)=(1-sqrt(s))/sqrt(s)>=1/(2sqrt(s))`,

and `p_(W^2)(s)=1/sqrt(s)`. Their difference therefore has logarithmic density divergence at zero by `int_0^(1/4) ds/(2s)=infinity`.
