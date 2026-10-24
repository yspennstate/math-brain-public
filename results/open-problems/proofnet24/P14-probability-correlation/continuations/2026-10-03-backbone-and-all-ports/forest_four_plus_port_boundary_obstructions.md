# Why a universal nonnegative boundary-row proof does not extend automatically

3 October 2026. Exact failed-route record. These are formal port-partition
rows, not weighted-forest counterexamples. The new all-port rank-one adjacent
theorem is proved for actual backbones using prior matroid log-concavity;
nonnegativity of an abstract boundary row alone eventually fails.

For r common ports, take all column profile weights equal to one and new
vertex row factors `a=c=1/1000`, `b=10`. Exact port-transfer cycle tests
compute the four adjacent marked coefficients for every initial partition.
For four ports, the coefficient of the product of the all-connected and
all-separated boundary weights in the Rayleigh polynomial is

    -16460857291451749/976562500000000000 < 0.

Thus the natural coefficientwise nonnegative bilinear expansion already
fails at four ports. This alone does not give a negative Rayleigh value;
the diagonal terms can absorb that negative cross coefficient.

For five ports, give the all-connected partition weight 3158, the
all-separated partition weight 1, and all other partitions weight zero.
The same direct connectivity computation gives exactly

    R=-100688580259552506656166009535155599
          /156250000000000000000000000000000 < 0.

Consequently a theorem valid for every nonnegative port-partition row is
false at five ports, even with proportional spoke profiles. This row
cannot be the actual partition row of an ordinary weighted forest backbone.
Indeed, putting `s=a+b+c=5001/500`, its one-apex partition would have to be

    Z(s)=3158(1+5s)+(1+s)^5.

Direct rational differentiation gives `(log Z)''(s)>0` at that value,
contradicting the credited ordinary graphic-matroid log-concavity theorem.
This proves unrealizability, rather than presuming it from the sign of R.

Equivalently, after component-transfer normalization the abstract row has
`Gamma>U/s`. The exact identity
`R=Z(s)^2 ac[U+acU^2-b Gamma]` still holds, but the closure inequality
`Gamma<=U/s` supplied for actual backbones by matroid log-concavity fails.
The all-port theorem therefore needs the actual-forest constraint.

The standalone exact checker
`forest_four_plus_port_boundary_obstructions.py` verifies both negative
coefficients, all four marked coefficients, the five-port negative value,
and the exact logarithmic-derivative identity. Its report is
`forest_four_plus_port_boundary_obstructions_results.json`. The preceding
floating exploration is preserved separately; it does not certify any
theorem or counterexample, and the exact certificate is the relevant
record here.

No negative-correlation failure on any graph is asserted. This is an
obstruction to a proof that drops the prior log-concavity input and treats
the backbone partition masses as arbitrary nonnegative numbers.
