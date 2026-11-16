# Referee note: F0073-A001 (Velenik 2006, Open Problem 6), agent A, 16 Nov 2026

Problem: for V with c_- <= V'' <= c_+, d = 2, the field on Z^2 \ {0} pinned at 0 and conditioned positive has
E^+(phi_i) of order log|i| (known only for V(x) = x^2/2).

A001 (an earlier worker session, 8 Sep, unreviewed) says the upper half comes "for free": the pinned positive field is
FKG-dominated by the positive field on Lambda_{2|i|} without the pin.

Verdict: the claimed domination does not follow. For convex V both measures are FKG and monotone in the set of
sites held at 0 (more zero sites, lower field). But the two measures are not nested: the box field on
Lambda_{2|i|} carries a zero outer boundary that the field pinned only at 0 lacks, and the pinned field carries the
pin at 0 that the box field lacks. What monotonicity does give: (box with pin) <= (box without pin) and
(box with pin) <= (field pinned at 0). Neither bounds the pinned field from above. Also, the positive field on
Lambda_N with zero outer boundary has height of order log N at distance of order N from the boundary (Velenik
survey Sec. 3.3; which paper covers convex V in d = 2 not rechecked), so a comparison box must have size of order
|i|. A001's "only the lower bound is at issue" is wrong: both halves are open for convex V.

What does transfer: log N heights in boxes with zero boundary (source to be rechecked); a two-sided
comparison between the field pinned at 0 and box fields at scales |i|/2 and 2|i| needs control of the pinned
field's law outside a ball, which is exactly where the Gaussian proof uses the explicit Green's function.

Literature check 16 Nov 2026 (one extended web search): nothing after Velenik's survey (arXiv math/0509695)
settles OP6. Status stays open; A001 should be marked "refereed: upper-bound claim unsupported (measures not nested)".
