# Rigor addendum: the square-receiver bathtub step

This addendum supplies the attainment-free proof of equation (4.2) in REPORT.md, in view of the programme warning not to assume a bathtub threshold on an infinite line without justification.

Let q in (1,2), c>0, and let h be a probability density on (0,infinity) satisfying h(u)<=g(u):=c u^(-1/2) almost everywhere. Let R be the unique number with integral_0^R g=1, so R=1/(4c^2), and set a=g(R)=2c^2.

For 0<u<R we have g(u)>=a and 0<=h(u)<=g(u). Since q>1,

  g(u)^q-h(u)^q >= a^(q-1)(g(u)-h(u)).

For u>R we have h(u)<=g(u)<=a, hence

  h(u)^q <= a^(q-1)h(u).

Integrating and using integral h = integral_0^R g =1 gives

  integral_0^infinity h^q
  <= integral_0^R g^q
     -a^(q-1)[integral_0^R g-integral_0^R h]
     +a^(q-1)integral_R^infinity h
  = integral_0^R g^q.

Thus no extremizer-existence theorem is being assumed: the claimed saturated initial interval is proved optimal by this elementary mass-transfer inequality. Finally

  integral_0^R g(u)^q du
  = c^q R^(1-q/2)/(1-q/2)
  = [2^(q-1)/(2-q)] c^(2q-2).

Taking q-th roots and c=|gamma|^(-1/2) gives exactly

  ||p_(gamma Z^2+2wZ+c0)||_q
  <= [2^(q-1)/(2-q)]^(1/q)|gamma|^(-(1-1/q)).

Hence the q=6/5 constant and all subsequent inequalities in REPORT.md are unchanged.
