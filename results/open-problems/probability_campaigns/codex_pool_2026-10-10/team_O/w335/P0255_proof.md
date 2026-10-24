# P0255: an absolute bound for positive weighted stars

Label: proof of a special class and a numerical counterexample search, pending w347. No bound for arbitrary graphs is proved.

Consider a star with m>=2 leaves, positive leaf-edge lengths w_i, total S, and largest two lengths w_1>=w_2. A nearest-unvisited walk stops when every vertex has been visited; it does not return to its start. Its length from the centre is B=2S-w_1. From leaf r it first visits the centre and then the remaining leaves in increasing edge-length order, giving L_r=2S-w_r-max_{j!=r} w_j. Ties between equal weights do not change the total length.

Hence every start length lies between A=2S-w_1-w_2 and B. Since S>=w_1+w_2 and w_1>=w_2, B>=3w_2 and B/A<=3/2. For any random start, not only the uniform law, if u=E L then averaging (L-A)(B-L)>=0 gives Var(L)<=(B-u)(u-A). Further,

    (B-A)^2/(4AB) - (B-u)(u-A)/u^2
      = ((A+B)*u-2AB)^2/(4AB*u^2) >= 0.

Thus sd(L)/E L <= (B-A)/(2 sqrt(AB)) <= 1/(2 sqrt(6)). A one-leaf star has constant length and ratio zero. This proves an absolute bound for the weighted-star class requested as a boundary case of P0255.

The constant is sharp if arbitrary start distributions are allowed: on the three-vertex star with both weights one, give the centre probability 2/5 and each leaf probability 3/10. Then L is three with probability 2/5 and two with probability 3/5, giving Var(L)/(E L)^2=1/24. Under the uniform law that same star has coefficient sqrt(2)/7; no claim of optimality within the uniform-start subclass is made.

The earlier attempt proves a general range-based O(sqrt(log n)) bound. The present result proves a constant for stars directly from their route geometry, without using a worst-case tour comparison. A seeded search over small weighted connected graphs is recorded as numerical evidence only; failure to find a counterexample is not evidence of a proof for all graphs.
