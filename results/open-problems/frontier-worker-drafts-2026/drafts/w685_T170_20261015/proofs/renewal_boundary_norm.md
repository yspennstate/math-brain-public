# Encoded renewal boundary norm (C015-v1; proof unaudited)

The statement is about the finite graph in scripts/height_renewal_graph.json at the exact rational d=21 point in logs/height_bridge_tail_certificate.json. It does not assert that the graph is the intended FPP model, or that its renewal operator contracts. Both require additional checks.

Write a=s+1. A state carries an incoming odd-square flag I in {0,1} and moment index p in {0,1}, with p=0 if I=0. Define w(I,p)=(a/(a+I))^(p+1). For each mark in {0,1} and directional sign sigma, let M(mark,sigma) be the corresponding nonnegative, balanced transition matrix, including direction multiplicities and tilt z^sigma. The finite claim is

M(mark,sigma) w <= (d z^sigma/a) w, componentwise.

There are 641 states and 2,564 rational row checks. The largest exact ratio is one. The graph SHA256, point SHA256, and results are in logs/height_renewal_norm_certificate.json. Reproduce using python -X utf8 scripts/certify_renewal_norm.py.

Here is a direct derivation of the block entries used by the independent checker. Let E be the retained even-square flag, O the outgoing odd-square flag, and c0,c1 the two nonnegative chord coverages. The integrated variables are t0,t1. Their rates are x=a+c0+I+E and y=a+c1+E+O. Expand

t0^p (1+t0+t1)^E (1+t1+t2)^O.

For its coefficient of t2^q, integrate each monomial t0^u t1^v as u! v!/(x^(u+1)y^(v+1)). Multiply by a^(1+p-q) for the diagonal similarity used to balance the two parities. Nonfinalising transitions have factor 1/a. The checker obtains the integral by this monomial expansion, independently of the production code's two-by-two matrix multiplication, then sums each complete sign row with multiplicities 1 or d-r and exact target w.

The norm also has a probabilistic interpretation. Under independent Exp(a) variables, w(I,p) is the expectation of (a t)^p exp(-I t). After completing a pair, summing against target w integrates the future variable t2. The factors exp(-(t0+t1))(1+t0+t1) and exp(-(t1+t2))(1+t1+t2) are Gamma(2,1) survival probabilities and are at most one. Chord exponential factors are at most one. Removing them yields the source w and the baseline factor 1/a per directional transition. At most d actual directions have a given sign. The finite rational check avoids relying on this interpretation to certify the encoded matrix inequality.

Consequently any encoded sign profile of length n and final height ell has common-norm bound (d/a)^n z^ell. A family of omitted profiles with scalar mass at most R maps v to at most R max_j(v_j/w_j) w. This is the precise use of the scalar tail. It is not a licence to multiply overlapping marginal Gamma probabilities.
