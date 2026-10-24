# B17 early checkpoint — exact m=2 finite-bank value

Programme: QFORM-DENSITY-3EIG-20260922. Full conjecture remains OPEN.

We attack the first explicit finite-bank obstruction left by `QFORM-ONE-HEAVY-MAJORITY-EXACT-EXTREMIZER-v1`: for

A_m = diag(1, J_m/m, -J_m/m),

whose exact nonzero spectrum is {1,1,-1}, the preceding theorem reduces the optimization over every cap-one heavy-coordinate density and every output level to

C_m = p_{U^2+S_m^2-T_m^2}(0),

where U is uniform on [-1/2,1/2] and S_m,T_m are independent normalized sums of m such uniforms.

For m=2 the bank density is

h_2(s)=sqrt(2)(1-sqrt(2)|s|) 1{|s|<=1/sqrt(2)}.

Writing r=sqrt(u^2+s^2) and integrating out T_2 gives

C_2 = integral_{|u|<=1/2} integral h_2(s) h_2(r)/r * 1{r<=1/sqrt(2)} ds du.

By fourfold symmetry and polar coordinates (u,s)=(r cos theta,r sin theta), the Jacobian cancels 1/r and

C_2 = 8 [ integral_0^{pi/4} integral_0^{1/(2 cos theta)}
              (1-sqrt(2)r sin theta)(1-sqrt(2)r) dr dtheta
          + integral_{pi/4}^{pi/2} integral_0^{1/sqrt(2)}
              (1-sqrt(2)r sin theta)(1-sqrt(2)r) dr dtheta ].

Elementary integration gives

I_1 = -5/24 + (1/2) log(1+sqrt(2)),
I_2 = -1/12 + sqrt(2) pi/16,

hence

C_2 = -7/3 + pi/sqrt(2) + 4 log(1+sqrt(2))
    = 3.4136024838240218911... .

This is strictly below 3sqrt(2). A purely elementary certificate is

pi/sqrt(2) < 11sqrt(2)/7,   log(1+sqrt(2))<1,

so

C_2 < 5/3 + 11sqrt(2)/7 < 3sqrt(2),

where the last inequality is equivalent to 35 < 30sqrt(2).

Thus, conditional only on the already-completed exact-extremizer theorem (whose proof is source-pinned and correction-compatible), the entire arbitrary-heavy-law m=2 branch is below the candidate sharp obstruction 3sqrt(2). The m=1 branch similarly equals pi.

Required newest-Claude source application: Theorem C of `COUNTEREXAMPLE_SEARCH.md` at math-open-problems commit e5f71d79eff325201dd0274053d20268ce65b837 gives the independent one-sheet bound p(s)<=pi sqrt(2) for s>=0 in every exact (+,+,-) rank-three source-valid member. For the present branch this is a valid finite-m inequality, while the exact computation above sharpens the actual global m=2 branch to C_2<3sqrt(2). Theorem D does not control this family because every physical cross cut has rank at most two, so its 3-volume Z vanishes; Theorem F's leverage gate also fails at the singleton row of leverage one. This is precisely why the finite-bank calculation is complementary rather than a reproof of a paid Fourier case.
