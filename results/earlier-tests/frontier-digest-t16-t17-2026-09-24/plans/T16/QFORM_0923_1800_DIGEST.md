# QFORM plan, next few hours

The goal is the whole conjecture; this plan targets its open core. Every digest note is provisional or unverified and three carry "(corrected)", so I re-derive each before building on it.

Building on: three hubs with any remainder (Thm 6.3); two hubs with a remainder crossing a split (Thm 6.5); a single hub with a BV law or a free partner-only or square-only block (Props 3.13-3.15); a hub spread over several coordinates (6.9); the curved-marginal bounds for U + cV² (5.1); Rogozin and Ball-type bounds for linear marginals; the Banks-Garza-Vargas-Kulkarni-Srivastava rank-two condition for bilinear forms.

Avoiding:
- any route through the two-dimensional maximal functional (Example 5.2: unbounded on a spread frame whose curved marginals are all bounded);
- Fourier decay along a localized direction: N intervals of width 1/N spaced 2π/s give a density ≤ 1 with |φ(s)| near 1 at any chosen s;
- ∫|φ| as the density bound for a definite rank-two form (aW₁² + bW₂² has bounded density, non-integrable φ);
- Rogozin applied to Q itself (it concerns linear sums);
- the optimal quadratic Littlewood-Offord bound (itself open) and the random-matrix notes (unverified, one an open obligation, none bounding a sup-density).

Step 0, first hour: fix the target. The open-core note (14:58) predates Prop 5.1 and Example 5.2 (16:19-16:30). I read it with the exact-rank-three and method notes and redraw the case table: rows, how many of the three large eigendirections sit on hubs; columns, whether a hub enters through its own square or only through cross terms, and whether the remainder crosses a split with rank two or only one (a single spread square μV² crosses every split with rank one). My guess at the open core: a zero-diagonal hub coupled to spread linear forms that share coordinates with the spread squares (no free block), plus an arbitrary remainder. Prototype: Q = 2X₁U + μV² + R(X_L), U = ⟨v, X_L⟩, V = ⟨w, X_L⟩, v ⊥ w spread with overlapping supports. Conditioning on one hub can remove an eigenvalue of each sign (interlacing), so hubs and spread directions do not decouple. I also re-derive 5.1, 6.3 and 6.5 on uniform laws, comb laws and the 5.2 frame.

Main line, hours 1-4.
(a) Fix an absolute δ; H = coordinates of weight ≥ δ in the span of the three eigenvectors, |H| ≤ 3/δ. Given X_H = x, Q is a quadratic polynomial in X_L with quadratic part A_LL and linear part 2xᵀA_HL.
(b) For each open cell, compute ∫G(x)f_H(x)dx, where G(x) is the sup-density of that polynomial's Gaussian model (the density, not ∫|φ|). For the prototype with R = 0, G(x) ≍ min(|x|⁻¹, (μ|x|)^(-1/2)), integrable against any density ≤ 1 with constant ≲ 1 + μ^(-1/2). It comes first: cheap, and it fixes, cell by cell, the shape of the bound to prove. A cell meeting the hypothesis with a divergent integral is where I look for a counterexample.
(c) Prove "product-law density ≤ C·G" at rank ≤ 2 plus a linear term, first extending 5.1 from U + cV² to U + cV² + R. The extension must use the full spectrum: R = μ(vvᵀ − wwᵀ) leaves 2X₁U + μU², with one large eigenvalue and G infinite. A pure definite rank-two form needs no Fourier analysis: coarea over the ellipse gives density ≤ π‖f_(U,V)‖∞/√(ab).

Side tool (check against the record). For a coordinate with aᵢᵢ ≠ 0, solving the quadratic in Xᵢ gives density_Q(t) ≤ |aᵢᵢ|^(-1/2) E[(−sgn(aᵢᵢ)(S(X₋ᵢ) − t))₊^(-1/2)], S the Schur-complement form, which by Haynsworth inertia and interlacing for A⁻¹ keeps two eigenvalues of modulus ≥ 1 (A invertible, else a limit). A large-diagonal hub thus trades density with three large eigenvalues for a half-moment small-ball bound with two, and a second such step gives a log-moment bound with one. Zero-diagonal hubs escape the chain; hence the prototype.

First concrete step. Read the open-core note and Prop 5.1 in full, re-derive 5.1's two bounds by hand, then test the shape min(|x|⁻¹, (μ|x|)^(-1/2)) numerically: sup-density of 2X₁U + μV² with n up to 400, uniform and comb laws, v and w overlapping, conditioning exactly on X₁ and using fine histograms.
