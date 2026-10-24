# Density calculation

Let W=U+V/eps with U,V independent Uniform[-1/2,1/2]. The density of V/eps equals eps on the interval [-1/(2eps),1/(2eps)]. For eps<=1/2, convolution gives g(w)=eps for every |w|<=1/2.

For Z=W^2 and 0<z<1/4, the ordinary two-branch change of variables gives h(z)=eps/sqrt(z).

If Z1,Z2 are independent copies and 0<d<1/32, then

p(d) >= eps^2 * integral from 2d to 1/8 of 1/sqrt(u(u+d)) du.

For u>=2d, u+d<=3u/2, hence

p(d) >= eps^2 sqrt(2/3) log(1/(16d)).

Finally Q_eps=eps(Z1-Z2), so scaling preserves the logarithmic divergence. Thus the output density has infinite essential supremum.
