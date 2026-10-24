SIGNED IN - working on the quadratic-form bounded-density conjecture (universal constant), account account02, slot B14, 2026-09-23T15:56:25Z.
attacking: moving-fold receiver localization — average a quadratic receiver's moving critical point against the whole independent driver law before taking any active-fragment supremum.

# Early substantive checkpoint

## QFORM-MOVING-FOLD-RECEIVER-LOCALIZATION-v1

Let Z=(Z_1,...,Z_m) have independent probability densities <=1, let W be an independent scalar with density <=1, and for a.e. z let T_z be independent of W with density q_z satisfying ||q_z||_3 <= K uniformly. Let v != 0, and a,d be arbitrary real numbers. Set

Q = T_Z + a W^2 + (2 v^T Z + d) W.

Then

||p_Q||_infinity <= 2^(7/6) K ||v||_2^(-1/3).

The constant is independent of a,d, translations, support diameter, fragments, tails and moments.

Proof skeleton. Conditional on Z=z, Young gives ||p_{Q|z}||inf <= K ||p_{aW^2+bW}||_{3/2}, b=2v^Tz+d. If a!=0 and x=-b/(2a), direct root change-of-variables plus (u+v)^(3/2)<=sqrt(2)(u+v) gives

||p_{aW^2+bW}||_{3/2} <= |a|^(-1/3) H_f(x)^(2/3),
H_f(x)=int |w-x|^(-1/2) f(w)dw.

The random critical point X=-(2v^TZ+d)/(2a) has density cap M<=sqrt(2)|a|/||v||_2 by the product-projection theorem. The cap-only half-Riesz rearrangement bound gives sup_w E|X-w|^(-1/2)<=2sqrt(2) M^(1/2). Therefore Jensen gives E H_f(X)^(2/3)<=2 M^(1/3), and the |a| powers cancel exactly, yielding 2^(7/6)||v||^(-1/3). If a=0, ||p_{bW}||_{3/2}<=|b|^(-1/3), and the cap-only one-third Riesz bound gives the smaller constant (3/2)2^(1/6)||v||^(-1/3).

This closes the scalar receiver-self-curvature gap in account03/B14's whole-law bilinear receiver mechanism, provided the core is upgraded from uniform L2 to uniform L3. It still does not pay receiver-core couplings or prove that every N3 matrix exposes such a disjoint driver/receiver scalar.
