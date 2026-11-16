# F0073: the two-dimensional gradient field pinned at the origin and kept positive (working record, 16 November 2026)

The problem is Open Problem 6 of Y. Velenik, *Localization and delocalization of random interfaces*, Probab. Surveys
3 (2006), arXiv:math/0509695, Section 3.3: for an even potential V with c_- <= V'' <= c_+ in dimension two, show
that the field on Z^2 \ {0}, pinned at the origin and conditioned to stay positive, has mean height of order
log|i| at site i. This is known for the Gaussian case V(x) = x^2/2.

The problem remains open. The record is one partial attempt and one referee note on an earlier attempt.

| file | what it is |
|---|---|
| `01_attempt_agent_A.md` | Existence of the monotone limit, a uniform variance bound, the lower bound c log|i| (modulo the exact statement of Deuschel and Giacomin), and an analysis of why the upper bound is hard. |
| `02_referee_note_on_earlier_attempt_A001.md` | Shows that an earlier attempt's FKG domination argument fails because the two measures it compares are not nested. |

## What existed before and what is new

The Gaussian proof is due to G. Giacomin (lecture notes, 2001). The lower bound reduces, by FKG, to the entropic
repulsion estimate of J.-D. Deuschel and G. Giacomin (*Entropic repulsion for massless fields*, Stoch. Proc. Appl.
89 (2000) 333-354). The variance bound is the Brascamp-Lieb inequality. The analysis of the upper bound uses the
Helffer-Sjöstrand random-walk representation and the heat-kernel bounds of T. Delmotte and J.-D. Deuschel. The
attempt also mentions W. Wu's local limit theorem (arXiv:2202.13578) and the work of F. Schweiger, W. Wu and
O. Zeitouni on the maximum of such fields (arXiv:2403.11500) as possible tools.

New in the record: the infinite-volume measure exists exactly when the upper bound is finite; an
integration-by-parts identity at the wall, E[sum_y V'(phi_x - phi_y)] = rho_x(0); and the observation that the
upper bound reduces to an escape probability for the dynamic random walk with exponent exactly one, which the
known heat-kernel bounds do not give.
