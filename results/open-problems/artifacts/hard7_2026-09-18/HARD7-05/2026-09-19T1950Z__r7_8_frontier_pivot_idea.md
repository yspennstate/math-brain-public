# HARD7-05 B24 pivot — the simpler r=q=7/8 comparator is stronger

The first certified parameter trial in this run was `r=q=22/25`. Before freezing the run at that interior point, I used the B24 extremal-object step as intended: vary the comparator parameter itself and look for the best balance between covariance admissibility and the spectral certificate.

The key observation is that moving *slightly downward* from `22/25` improves the Temple/trace-four balance more than it hurts the Lamperti grid density. The rational point

`r=q=7/8`

is especially favorable:

- edge-smoothed covariance prefactor `(1+r)/2=15/16`;
- tail ratio `((1+r)/2)/r=15/14>1`;
- `r^5=16807/32768<287831/500000`, so only lags `1,2,3,4` need direct source-covariance checks;
- edge-sum correlation in the four-cycle is exactly `113/114`;
- `1-r^4=1695/4096`;
- in the three-step residual representation the independent common residual has variance exactly `1/31`.

A degree-18 Ritz reconnaissance at this parameter suggests the same fourth-moment/Temple mechanism can cross `theta=0.1614`, which would beat the already certified `r=22/25` rung. The next exact checker should therefore certify `r=7/8`, not spend the rest of the run polishing the weaker interior point.

This is still the same source-valid edge-smoothed comparison family; the pivot changes only the comparator parameter and frozen trial polynomial. No theorem claim is made in this note.