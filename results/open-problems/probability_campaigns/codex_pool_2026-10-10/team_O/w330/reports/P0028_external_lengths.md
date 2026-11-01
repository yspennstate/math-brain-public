# P0028: an independent, non-identically distributed special case

2026-10-10. Label: proof of a special case, awaiting w346 KEEP. The general independent stopped-piece question is unresolved in this packet.

Known literature answer for the iid finite-mean subclass: Burdzy and Scheutzow, Forward Brownian motion (2014), arXiv:1302.6958, Theorem 5.1. P0028-A002 already records this as a known theorem. No new solution is claimed by repeating the stationary Palm argument.

Special case: let (B^k) indexed by all integers be mutually independent standard Brownian drivers. Let (L_k) be a sequence of positive finite random lengths independent of the entire driver family, with sums divergent in both directions. The length sequence itself need not be iid, independent across k, stationary, bounded, or integrable. Glue the restriction of B^k to [0,L_k] at a common origin between indices -1 and 0. The resulting process, pinned to zero at that origin, has the law of two-sided Brownian motion without an additional random shift.

Proof: condition on the full length sequence. The boundaries are deterministic and locally finite, since the partial sums diverge. Each increment over a deterministic interval is a sum of independent Gaussian driver increments with total variance the interval's length. Disjoint time intervals use disjoint increments, even if they cut the same segment, and are independent. On the negative side, time reversal within each deterministic segment preserves the Gaussian increment law; its drivers are disjoint from those on the positive side. Continuity holds at the joins and every compact interval intersects finitely many segments. Thus the conditioned pinned process has exactly the two-sided Wiener law, which does not depend on the lengths. Integrating the conditional law proves the claim.

Failure check: ordinary path-dependent stopping times are excluded from this conditioning proof. Conditioning on their lengths biases the segment paths. Independence of different stopped pieces does not make lengths independent of their own Brownian drivers. This special case therefore cannot be promoted to the full question.
