# Operator norm plus the Hilbert-Schmidt outside block

Status: elementary analytic lemma, unaudited.

Let P be an orthogonal projection and let T be a bounded operator. Suppose ||PTP|| <= lambda and ||T-PTP||_HS^2 <= tau. Then ||T|| <= sqrt(lambda^2+tau).

For unit vectors f,g, set s=||Pf|| ||Pg|| in [0,1]. The Hilbert-Schmidt norm of the rank-one operator f g* after removing its P-to-P block is sqrt(1-s^2). Hilbert-Schmidt Cauchy-Schwarz therefore gives

|<f,Tg>| <= lambda s + sqrt(tau) sqrt(1-s^2) <= sqrt(lambda^2+tau).

Taking the supremum proves the result. This requires neither positivity nor positive semidefiniteness of T. In the kernel setting P restricts to [0,L], so tau is exactly the squared-kernel integral over the entire complement of [0,L]^2, including both cross rectangles. The finite positive cell matrix bounds ||PTP||. The source analytic tail bounds tau. The final arithmetic is performed in Arb on exact binary64 upper-bound inputs.

This improves the conservative triangle bound lambda+sqrt(tau) used in C004 version 1. It does not alter any previously accepted certificate or weaken its validity.
