# LO05: Section 5 (the rank-one elliptic group and its local parameters) read line by line (12 Nov 2026)

Source: lit/openai_oct6/paper_c.txt, lines 1862-1985, against the statements of Propositions 2.1 and 2.2 (lines
241-305), in the text extraction of paper.pdf from openai/math tree 0a112e434f6bf7f316e2999a63813ce58447e432. The
arithmetic was redone by hand.

E : y^2 = x^3 - d^2 x over F = Q(sqrt 2), d = 75 - 53 sqrt 2.

| Part | Content | Check | Result |
|---|---|---|---|
| fixed data | d totally positive of norm 7 | 75^2 - 2*53^2 = 7; embeddings 0.047 and 149.95 | holds |
| Prop. 2.1, field | O_F principal, totally positive units are squares | Minkowski bound sqrt(8)/2 < 2; -1 and 1 + sqrt 2 realize all four sign patterns | holds |
| Prop. 2.1, im alpha = 8 | two-isogeny descent with E' : y^2 = x^3 + 4d^2 x | unit-coefficient valuation argument bounds the image by 8; w = d(1+sqrt 2)^3 = -5 + 4 sqrt 2, w^3 - w = -8d, so Q = (-dw, 2 sqrt 2 d^2) lies on E; -dw has mixed signs, the four torsion classes do not | holds |
| Prop. 2.1, im alpha' = 1 | every x on E' is a square class 1 | totally positive; at sqrt 2 the valuations 3v and 4 + v differ for odd v; at d only v = 1 survives and needs -4 = 3 to be a square mod 7, which it is not | holds |
| Prop. 2.1, conclusion | rank one, mE(F) = ZP | 8 * 1 = 4 * 2^r | holds |
| Prop. 2.2, (2.6) | v(z(nP)/z(n'P)) = v_p(n/n') | formal-group differential integral; v(c_t) >= -v_p(t); (t - 1) v(Z) > v_p(t) for p > 2, so the logarithm converges and preserves valuation on the kernel; n' l(z(nP)) = n l(z(n'P)) | holds |
| Prop. 2.2, (2.7) | truncated logarithm approximates n/n' to precision K | (5.2) t - 1 - v_p(t) >= K for t > K and p > K + 1 (p^j - 1 - j >= p - 2); tail bound (5.3); v(l_K(z(n'P))) = v(z(n'P)) | holds |

Remarks. The formula |im alpha| |im alpha'| = 2^(rank + 2) is Silverman X.4.7 and X.4.9, used as quoted. S_E has to
contain 2 and 7 (bad reduction of E and its conjugate, and the ramified prime); the proof says so. The same argument
applies verbatim to the conjugate curve and the point P^sigma.

What this changes: Sections 3, 4 and 5 show no gap on a first independent read. LO05 stays REPORTED_SOLVED: Section 2's
reduction and Section 6 (the prime patterns), the companions' proofs, and a second independent audit remain.
