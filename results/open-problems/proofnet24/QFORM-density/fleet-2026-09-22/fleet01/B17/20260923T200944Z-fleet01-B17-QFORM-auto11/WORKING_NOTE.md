# Working note — sharp periodic-frame Edgeworth deficit

Use the previously proved B17 expansion for a fixed Parseval row pattern `v_1,...,v_r in R^3`, `sum_j v_j v_j^T=I_3`, repeated `m` times with independent centered unit intervals:

`p_{Q_m}(0)=3 sqrt(2)[1-(20m)^{-1} sum_j E_J(v_j)+O(m^{-2})]`,

where, with `s=v_1^2+v_2^2` and `t=v_3^2`,

`E_J(v)=(57/32)s^2+(15/4)st+(3/4)t^2`.

New observation: put `a=57/32`, `b=15/4`, `c=3/4`. Since `b^2=225/16 > 4ac=171/32`,

`E_J(v) >= (sqrt(a)s+sqrt(c)t)^2`.

By Cauchy and Parseval (`sum s_j=2`, `sum t_j=1`),

`sum_j E_J(v_j) >= r^{-1}(2sqrt(a)+sqrt(c))^2 = (63+2sqrt(342))/(8r)`.

Thus, with total physical dimension `n=rm`, every fixed periodic Parseval cube frame has

`p_{Q_m}(0) <= 3sqrt(2)[1-c_*/n+O(n^{-2})]`,

`c_*=(63+2sqrt(342))/160 = 0.6249155251113366...`.

This improves the prior universal coefficient `27/80=0.3375`.

Sharpness at the level of row-pattern size: split the rows into `k` rows forming an equal-norm Parseval frame of the positive 2-plane and `r-k` rows parallel to `e_3`. Then

`sum E_J = 57/(8k)+3/[4(r-k)]`.

Choosing `k/r -> sqrt(38)/(sqrt(38)+2)` makes `r sum E_J -> (63+2sqrt(342))/8`; hence `c_*` is asymptotically optimal for this Edgeworth coefficient among fixed Parseval patterns.

The simple `r=4,k=3` pattern has `sum E_J=25/8`, giving relative deficit `5/(8n)`, only `(37-2sqrt(342))/160 = 8.44748e-5` above `c_*`.

Next: make this four-row pattern genuinely dense by a small exact rational orthogonal rotation and verify all physical matrix entries are nonzero; then apply the latest fleet02/B17 separated-bank barrier to a concrete comparator.
