# P0019: Quantitative hemisphere containment at a Holder differentiable boundary

Label: proof; author checked only. Independent audit: PENDING w347.

Suppose a domain near a boundary point z is, in coordinates with outward unit normal e_d, contained in {x_d<g(x')}, with g(0)=0 and |g(x')|<=C*|x'|^(1+gamma), gamma>0. For any interior x approaching z=0, its normalized approach vector u=(z-x)/|z-x| satisfies e_d dot u>=-C*|z-x|^gamma. Consequently every limiting approach direction lies in the closed outward hemisphere. This applies pathwise to Brownian exits at such points.

Assumptions: A local boundary graph at the exit point with the displayed remainder bound; The orientation e_d is outward; Interior points approach that boundary point

Write r=|x|. Because x_d<=g(x')<=C*|x'|^(1+gamma)<=C*r^(1+gamma), the outward component of u=-x/r is -x_d/r>=-C*r^gamma. Let r decrease to zero along any convergent sequence of directions. The error vanishes, giving e_d dot u>=0. This is a deterministic local boundary statement, so continuity of a Brownian exit path is the only stochastic ingredient in this containment conclusion.

Limits: Containment does not establish that every hemisphere direction occurs. Arbitrary nonsmooth domains need not have the displayed boundary graph.

Existing card: math:probability.core:open-problem-p0019-brownian-exit-approach-directions-in-higher-dimensions
Source snapshot: ~/math-brain-build/export/population/nodes.jsonl:5773
