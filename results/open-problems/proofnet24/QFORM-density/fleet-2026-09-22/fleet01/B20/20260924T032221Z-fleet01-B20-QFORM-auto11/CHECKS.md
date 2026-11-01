# Numerical and algebraic checks

Run: `20260924T032221Z-fleet01-B20-QFORM-auto11`.

Source constants:

- `Lambda = 16.405318852237478`
- `eta0 = 0.008411726321812482`
- `C3 = 10.3450832321475`
- rank bound `r<=42`

Derived values:

- `d0 = 1/(8 Lambda) = 0.007619480067767874...`
- `gamma0 = 1-d0-eta0 = 0.9839687936104196...`
- diffuse leverage threshold `q0=1/(16*42)=1/672=0.001488095238095238...`
- half-cut lower Gram eigenvalue `g0=3/8`
- actual physical cross-block third singular lower bound
  `c0=(3/8)gamma0-eta0 = 0.36057657128209486...`
- third-volume lower bound `c0^6 = 0.0021977841057714068...`
- density bound `C3/c0 = 28.690392155440648... < 28.691`.

Exact expectation identity used in the half-cut lemma:

For row vectors `v_i^T` of an orthonormal-column carrier matrix `V`, with independent `delta_i~Bernoulli(1/2)`,

`G=sum_i delta_i v_i v_i^T`,

then

`E ||G-(1/2)I||_F^2
 = (1/4) sum_i ||v_i v_i^T||_F^2
 = (1/4) sum_i ||v_i||^4`.

If `max_i ||v_i||^2<=1/672` and `sum_i||v_i||^2=r<=42`, the last expression is at most

`(1/4)(1/672)42 = 1/64`.

Thus a physical half-cut exists with Frobenius, hence operator, deviation at most `1/8`, giving both carrier Gram matrices at least `(3/8)I`.

Heavy-set cardinality check:

For `L={i:P_ii>1/672}` and `sum_iP_ii=r<=42`,

`|L|/672 < sum_{i in L}P_ii <=42`,

so `|L|<28224`; the report uses the safe integer statement `|L|<=28224`.

No random simulation or floating computation is used as proof; decimals only display consequences of exact inequalities and source-pinned constants.
