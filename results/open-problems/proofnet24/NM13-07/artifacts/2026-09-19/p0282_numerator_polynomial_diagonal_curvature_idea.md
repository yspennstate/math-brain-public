# P0282 idea note — numerator polynomial cancellation and diagonal curvature

Date: 2026-09-19 UTC

This note records the mathematical route before production validation for the current NM13-07 invocation.

For fixed defect `j=n-k`, the retained hook factorization writes

`F_j(n)=ell_{n,n-j}=(n)_j^2/j! * A_j(1/n)`.

For a partition `mu` of `j`, the hook correction inside `A_j(t)` is

`R_mu(t)=prod_{x in contents(mu)} (1-(j+x)t)/(1-(j+x-1)t)`.

Telescoping along each row of `mu` gives

`R_mu(t)=prod_{r>=1} (1-(j+mu_r-r)t)/(1-(j-r)t)`.

The denominator is independent of `mu`. With

`D_j(t)=prod_{s=1}^{j-1}(1-s t)`

and

`P_j(t)=E_Plancherel(j)[ prod_{r=1}^j (1-(j+mu_r-r)t)^2 ]`,

we therefore expect the exact identity

`A_j(t)=P_j(t)/D_j(t)^2`.

Since `(n)_j=n^j D_j(1/n)`, this should cancel the entire falling-factorial denominator whenever the stable hook decomposition by `(n-j,mu)` is valid (in particular `n>=2j`):

`F_j(n)=n^(2j)/j! * P_j(1/n)`.

Hence the source Chen ratio should simplify to

`F_j(n)^2/(F_{j-1}(n)F_{j+1}(n))=((j+1)/j) * P_j(1/n)^2/(P_{j-1}(1/n)P_{j+1}(1/n))`.

This is a cleaner source-level object than the earlier `A_j` formulation and may expose a whole-series positivity mechanism.

A second route is to exploit the retained finite-degree lemma for the Taylor coefficients `D_m(j)` of `log A_j`. The working conjecture suggested by exact low orders is not global positivity in all defects (already false at `m=11,j=1`) but a diagonal threshold:

`C_m(j)=2D_m(j)-D_m(j-1)-D_m(j+1) > 0` for `j>=m`.

Production validation should test this through a substantially larger block than the predecessor's orders `10..18`, and only then use one analytic tail estimate. No all-order theorem is assumed from finite evidence.

Methods attached to this route: #18 SAY IT IN ANOTHER LANGUAGE (the `P_j` polynomial), #25 COUNT THE SAME THING TWICE / support-pattern accounting (attempt an all-order sign mechanism), and #30 DO ONE SCALE/ORDER AT A TIME (finite diagonal curvature block followed by a single tail bound). All three are RECYCLED on P0282 because every numbered method has already been used on this source; the triple differs from the preceding run's #23/#26/#3.
