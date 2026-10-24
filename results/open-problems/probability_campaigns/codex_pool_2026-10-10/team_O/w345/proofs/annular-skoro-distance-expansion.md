# P0024: Exact finite-time expansion in the annular Skorokhod problem

Label: proof; author checked only. Independent audit: PENDING w347.

For the smooth bounded connected annulus D={x in R^2:1<|x|<3}, normal reflection driven by w(t)=(-t,0) can increase the distance of two synchronously driven paths. Start X(0)=(1,0) and Y(0)=(cos(theta),sin(theta)), 0<theta<pi/2. Until t<log(cot(theta/2)), X(t)=(1,0) and Y(t)=(cos(phi(t)),sin(phi(t))) with phi(t)=2 arctan(exp(t)tan(theta/2)); the squared distance has derivative 2 sin(phi(t))^2>0.

Assumptions: Deterministic continuous finite-variation driving path; Normal Skorokhod reflection on the closed annulus; Boundary starting points and 0<theta<pi/2; 0<=t<log(cot(theta/2))

On the inner circle the inward normal of the annulus is the outward radial vector. For X, take reflection regulator L_X(t)=t, so dX=(-1,0)dt+(1,0)dL_X=0. For Y, choose dL_Y=cos(phi)dt, which is nonnegative while phi<pi/2. The Skorokhod equation then gives Y'=(-1,0)+cos(phi)(cos(phi),sin(phi))=(-sin(phi)^2,cos(phi)sin(phi)). This equals (-sin(phi),cos(phi))*phi' when phi'=sin(phi), and the displayed solution solves that ODE. Both regulators increase only on the inner boundary, both paths stay in the closed annulus, and neither reaches the outer boundary. Their squared distance is 2(1-cos(phi)), with derivative 2 sin(phi)^2. This is a complete deterministic calculation.

Limits: Finite-time deterministic expansion is compatible with eventual Brownian contraction. The cached author page excludes one-hole domains as long-term counterexamples (see one-hole-exclusion-source-restriction.md). No positive long-time limsup is established.

Existing card: math:probability.core:open-problem-p0024-failure-of-synchronous-contraction-in-a-bounded-planar-domain
Source snapshot: ~/math-brain-build/export/population/nodes.jsonl:6405
