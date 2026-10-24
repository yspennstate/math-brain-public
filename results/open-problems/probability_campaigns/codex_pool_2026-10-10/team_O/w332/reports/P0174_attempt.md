# P0174: independent reconstruction, 2026-10-10

Status: full candidate proof reconstructed from the stored moment route; the cached source criterion has now been checked. Pending w346's blind KEEP and full proof check. No novelty or literature clearance. The support diameter is D and the semicircle variance is t.

If D=0, mu is a point mass and its free convolution with a semicircle is a translated semicircle, which is unimodal (with the point-mass case at t=0). Hence assume D>0. For R>0 let y=R^2 and F(u)=integral ((x-u)^2+y)^(-1) dmu(x). At a stationary point u, put Z=integral ((x-u)^2+y)^(-2) dmu and dQ=Z^(-1)((x-u)^2+y)^(-2)dmu. For X=x-u under Q, E_Q X=0. Write a=E_Q X^2 and b=E_Q X^4. The support length is at most D.

The centered moment inequalities are a<=D^2/4 and b+3a^2<=D^2 a. For the second, take an independent copy X': (X-X')^4<=D^2(X-X')^2 pointwise. Expectations are 2b+6a^2 and 2a. For the first, if support lies in [l,h], centering gives a<=-lh<=(h-l)^2/4.

Normalization and reweighting give 1/F=(b+2ay+y^2)/(a+y). Direct differentiation gives F''/(2Z)=3-4y E_Q[1/(X^2+y)]. If F''>=0, Jensen's inequality for the convex reciprocal function implies 1/(a+y)<=E_Q[1/(X^2+y)]<=3/(4y), so y<=3a. This implication requires F''>=0; it does NOT hold at arbitrary stationary points.

Consequently

1/F-D^2 <= ((y-3a)(y+a)+(4a-D^2)y)/(a+y) <= 0.

If equality holds, y>0 forces a=D^2/4 and y=3a. Equality in the variance bound forces equally weighted endpoint atoms at X=+/-D/2. For this law put a=D^2/4. The exact formula at y=3a is

F(u)-F(0) = -u^4 / (4a(16a^2+4au^2+u^4)) < 0 for u != 0.

Thus the equality point is a strict fourth-order maximum, not a minimum. Every local minimum has F>1/D^2. Since F tends to zero at both infinities, a horizontal level 1/t<=1/D^2 can have at most two solutions: any three solutions would force a separating local minimum of value <=1/t. Analyticity excludes a constant interval; a horizontal tangency at a maximum together with other roots also forces a separating minimum.

Applying the cached source's sufficient Lemma 3.1 gives the candidate unimodality conclusion for t>=D^2. For the symmetric law on {-c,c}, t>c^2 and the central Biane-boundary second derivative is (4c^2-t)/(t sqrt(t-c^2)); it is positive for c^2<t<4c^2, supplying failure of unimodality arbitrarily close below D^2. This suffices to exclude every universal C<1. No claim is made here about the threshold-attainment rigidity corollary for every other measure: that requires a limiting argument absent from the earlier memo.

Sources inspected: reports/P0174_sources.json, especially the author-only moment-route card; Probability_I0086_free_brownian_unimodality_sharp_constant_2026-09-14.md. The earlier memo's non-strict proposition alone proves t>D^2; the strict-maximum equality argument above supplies the endpoint t=D^2.

Source check completed: ~/Downloads/Probability_1000_20h_20260906/sources/free_unimodality_2018/text.txt, lines 436-451, Lemma 3.1. It states the at-most-two-roots condition as sufficient for unimodality. The I0086 memo calls it an equivalence; that stronger reading is unnecessary here and was not asserted by this source lemma. The support diameter convention is explicit in Theorem 1.2 at lines 94-96. See reports/exact_primary_sections.json. The source is Hasebe and Ueda, Large time unimodality for classical and free Brownian motions with initial distributions, arXiv:1710.08240; ALEA 15 (2018), 353-374.

Checks that could fail: Jensen direction; reweighting normalization; fourth-order equality; the analytic root-count step; unresolved literature novelty. Run check_math.py for reproducible algebra and boundary checks. The complete free-probability claim stays a concept marked candidate until an independent KEEP and full proof check.
