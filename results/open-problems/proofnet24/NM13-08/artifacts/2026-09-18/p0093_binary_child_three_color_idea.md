# P0093 route idea — binary offspring, three colors

Source target: Johnson–Podder–Skerman Section 6 asks whether a finite tree automaton with at least three colors can have infinitely many fixed points of its automaton distributional map.

Use the admissible deterministic child law `chi = delta_2`. With three colors, an automaton is determined on the six unordered two-child color multisets. The distributional map is then a quadratic stochastic map of the 2-simplex. Instead of studying a generic analytic map, look for a rule with a one-dimensional fixed locus.

A natural mechanism is to make colors 1 and 2 dynamically indistinguishable except for their label: let color 0 act as a carrier. If exactly one child is color 0 and the other child is nonzero, copy the nonzero child's label; in every other two-child configuration output color 0. Then both nonzero masses should be multiplied by the same scalar. If that scalar can be forced to one at an interior value of the color-0 mass, the split between colors 1 and 2 becomes a free parameter and yields a continuum of fixed points.

This route directly attacks the source existence question rather than a proxy. The exact calculation/checker should verify the induced polynomial map and fixed locus symbolically.