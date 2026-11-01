# P0282 idea before theorem validation — exact worst Plancherel-growth edge and a sharper linear window

Date: 2026-09-19 UTC  
Track: `proofnet24/NM13-07`  
Canonical claim: `P0282`  
Entry frozen metric: `N_exact = 103`

This note records the new route before its dedicated theorem self-check. It is not itself a certificate or an outside audit.

The preceding run obtained a linear defect theorem `j<=n/4` from the exact Plancherel-growth edge identity

`R_{s+1,n}(lambda)/R_{s,n}(mu) = prod_{x in mu}(1-1/(K-c(x))^2) * (1-1/(K-c0))`.

Its old lower bound replaced every old content by the single worst denominator `d+3`, which loses the entire distribution of old contents. The new idea is to identify the actual extremal growth edge exactly.

For the transition `j-1 -> j`, put `d=n-2j` and `K=n-j+1=j+d+1`. Enumerate the `j-1` boxes of `mu` in row-major order as `x_p=(r,q)`, `p=1,...,j-1`. Since `p>=q`,

`c(x_p)=q-r <= q-1 <= p-1`.

Therefore

`K-c(x_p) >= K-p+1`,

and the old-box product is bounded below by the telescoping one-row product

`prod_{p=1}^{j-1}(1-1/(K-p+1)^2)
 = prod_{m=d+3}^{j+d+1}(1-1/m^2)
 = (d+2)(j+d+2)/((d+3)(j+d+1))`.

The new box has `c0<=j-1`, so its factor is at least `(d+1)/(d+2)`. Hence every growth edge obeys

`R_{j,n}(lambda)/R_{j-1,n}(mu) >= q_j(d)`

with

`q_j(d) = (d+1)(j+d+2)/((d+3)(j+d+1))`.

Equality is attained by the one-row edge `(j-1) -> (j)`, so this is the exact minimum edge ratio, not merely a convenient bound.

Averaging under Plancherel growth gives `A_j >= q_j(d)^2 A_{j-1}`. The next-step factors are all in `(0,1)` in the regime below, so `A_{j+1}<A_j`. Thus the exact Chen ratio has the lower bound

`Q_j(n) > (j+1)/j * [ (d+1)(j+d+2) / ((d+3)(j+d)) ]^2`.

Let

`alpha=(sqrt(17)-1)/2`.

The asymptotic threshold of this exact worst-edge method is `d/j=alpha`. The intended finite proof is stronger: set `d=alpha*j+x`, `x>=0`, and expand

`E=(j+1)(d+1)^2(j+d+2)^2 - j(d+3)^2(j+d)^2`.

The expansion should have no `j^4` term because `alpha^2+alpha-4=0`, and every remaining coefficient in `x,j` should be strictly positive. If the exact symbolic self-check confirms this identity, it proves

`d >= alpha*j  => Q_j(n)>1`,

or equivalently

`j/n <= (sqrt(17)-3)/4`,

that is, a long-LIS theorem for

`k/n >= (7-sqrt(17))/4 ~= 0.7192236`.

This would improve the preceding `k>=3n/4` window and would also identify the best asymptotic constant obtainable from the one-step pointwise worst-edge lower bound. The next research question would then be to beat this barrier by averaging edge contents rather than minimizing pointwise over edges.
