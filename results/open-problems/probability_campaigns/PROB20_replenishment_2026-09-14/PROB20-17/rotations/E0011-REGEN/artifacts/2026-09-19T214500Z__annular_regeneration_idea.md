# E0011 first active run — idea before checker

Methods: **B2 / B12 / B19**.

The fresh object is not another fixed-width fuel strip. At `p=1/2`, the exact charge identity from the retired R08 work is

`L Q = (V-E_00)/2`.

For one connected vacancy component this equals `(1-beta_1)/2`, so a connected vacancy interface has zero charge drift exactly when it is **unicyclic**. This suggests a location-flexible annular seed: an O core separated from a CO exterior by one vacancy circuit. The smallest square examples are an `n x n` vacancy perimeter with an `(n-2)x(n-2)` O core and a CO exterior.

Counterexample-first plan: compute an exact fatal subevent under the legal all-CO exterior. Require every effective event until poisoning to be a CO adsorption; any O2 clock exits the subevent. If this CO-only poisoning probability is at least `1/64`, then any SUCCESS event that must retain oxygen is disjoint from the subevent, so `a <= 1-f` and `a-63f <= 1-64f <= 0`. Such a seed cannot give positive `M_reg`.

If the first annulus surviving this filter exists, do **not** freeze its adjacent CO collar: every vacancy perimeter has `V=E_00`, hence the first effective event is O2 with probability exactly `1/3`, and an O2 event on a rigid collar immediately removes collar CO at `r=infinity`. A viable seed class must therefore treat early collar erosion as RETRY, not FATAL.

B19 candidate algorithm after the screen: use a **soft-collar annular class** in a finite protected box. Membership is existence-based and location-flexible: an O core, a simple vacancy circuit around it, and enough nested CO protection that one interface excursion does not expose the arbitrary exterior. SUCCESS is two disjoint translated copies in prescribed forward child windows; RETRY is return to the same annular class before outer protection is breached; FATAL is phase extinction, protection breach, or horizon expiry outside the class. Stop before arbitrary exterior information can enter. At `p=1/2` all effective transition and reaction-choice rates are rational, so once a manageable state description is found, `(a,f)` can be certified by an exact absorbing-chain computation.

This artifact states the route before any checker. It makes no metric claim.