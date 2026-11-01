# Correction to EARLY.md

The early calculation contains one arithmetic factorization error in the symmetric three-carrier stationary equation. The equation itself is correct:

`2 y(9+12y+3y^2)=3(4+9y+6y^2+y^3)`.

After subtraction this is

`y^3+2y^2-3y-4=0=(y+1)(y^2+y-4)`, not a polynomial having `y=2` as a root. The unique positive solution is therefore

`y_*=(sqrt(17)-1)/2 = 1.5615528128088303...`.

Consequently the exact symmetric carrier-balanced currency for the stress family is

`G_* = C_3 L^3`,

where

`C_3 = [4+9y_*+6y_*^2+y_*^3]/y_*^(3/2)
     = 8(3+y_*)/y_*^(3/2)
     = 18.701122669207606...`.

The structural dual formula, complementary-face AM-GM lower bound, exact face masses, and light-row marginal argument in EARLY.md are unchanged. All later calculations use this corrected value.