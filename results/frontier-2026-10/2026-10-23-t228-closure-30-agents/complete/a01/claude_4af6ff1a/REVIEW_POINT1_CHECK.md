# T228 target 2, review point 1: where ABB uses continuity of Psi

claude-4af6ff1a, 21 Oct 2026 21:5x. A second pass of my own; the outside review is still owed.

Source: src/ABB.txt (arXiv v2 text, 2,824 lines). Every match of continu/Feller/semicontinuous:

| line | what is continuous | used for |
|---|---|---|
| 9, 45-47 | Psi, assumption (1) | stated |
| 55 | Psi via (1) | "has the Feller property" |
| 482 | a self-map of [0,1] | example 2.1.3 only |
| 600 | f | definition of Lip(f) |
| 821-851 | rho(t), entries of P(t) | Lemma 4.2, the Cramer function |
| 1508, 1555 | g (directly Riemann integrable) | Markov renewal theorem |
| 2576 | Psi via (1) | Prop. 9.1, existence of a stationary law (Feller) |

Section 8 (positivity, Lemma 8.2 and 8.3) uses the invariance of nu, independence of (Psi_n) from R ~ nu, the
identity Lambda_{1..T}(x) = x Z_T for x > 0 and the comparison (31) of Lemma 3.1, which rests on (4) only. No step
uses continuity of Psi or the Feller property. Joint measurability of (omega, x) -> Psi(omega, x) is used (the
martingale M_n); it holds here because Psi is piecewise affine in x with measurable coefficients.

So the reading in T228_B_v1.md section 4 stands at the level of the text. Existence comes from Harris recurrence
(section 3), not Feller, so the jump of Psi at 0 is never used. The Goldie fallback in section 4 remains as a second
route to the limits.
