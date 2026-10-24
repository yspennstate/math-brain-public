# Continuity addendum for QFORM-UNEQUAL-CUBE-BANKS-CENTERED-HEAVY-BARRIER-v1

The theorem's continuity conclusion is correct, but the sentence in `REPORT.md` saying that continuity follows merely because both one-sided densities are in `L^1` should not be used as the justification.

A direct valid argument is as follows. With the notation of the report,

`A=X^2+Y^2`, `B=Z^2`.

The polar formula

`a_A(t)=(1/2) int_0^{2pi} f(sqrt(t)cos(theta))h(sqrt(t)sin(theta))dtheta`

and the bounds on `f,h` show that `a_A` is bounded. Because `X,Y` have compact support, `a_A` is also compactly supported. Hence `a_A in L^3(R)`.

For `t>0`,

`b_B(t)=k(sqrt(t))/sqrt(t)`.

The density `k` is bounded and compactly supported, so `b_B(t)=O(t^{-1/2})` at zero and vanishes outside a compact interval. Therefore `b_B in L^{3/2}(R)`.

Now

`p_Q = a_A * check(b_B)`.

For every increment `h0`, Holder gives

`sup_s |p_Q(s+h0)-p_Q(s)|`

`<= ||a_A||_3 ||tau_{h0}check(b_B)-check(b_B)||_{3/2}`.

Translations are continuous in `L^{3/2}`, so the right-hand side tends to zero as `h0->0`. Thus `p_Q` has a bounded uniformly continuous representative.

This argument is scoped only to the finite centered-cube bank family of the theorem. No unrestricted QFORM continuity claim is made.
