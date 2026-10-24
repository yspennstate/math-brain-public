# A034 odd-mask theorem: valid clauses and an unsupported coupled inference

Read the exact PROOF.md and CLAIMS.json in run20261014T025347Z. The concentrated-row theorem and the individual shared-row divisibility reconstruct correctly. The additional claim gcd_J D_J divides3t has a GAP in its cited proof; this is not an actual Boolean counterexample or a declaration that the standalone statement is false.

For each row with odd mixed mask, every integer raw Walsh coefficient is odd and nonzero. Product magnitudes give coprime odd pairs a_i,b_i and common integer scale c. Since c divides P h(x), a point with h=+/-1 implies c divides P; oddness forces c=1. Parseval gives product((a_i^2+b_i^2)/2)=|M|+4|E|. Complementing every spectral bit gives each product W_s W_(s xor full) modulus D=product a_i b_i. The convolution identity is sum_s W_s W_(s xor full)=P sum_x h(x)^2 chi_full(x)=P(t+4t_E). Since D is odd, D divides t+4t_E.

In a concentrated row E=M^c, t_E=-t, so D divides3t. With odd t nonzero, D<=3|t| and D>=3^N. The source's elementary product bound follows from (a^2-1)(b^2-1)>=0 and its two-factor iteration: product((a_i^2+b_i^2)/2)<=(D^2+1)/2. Thus8P<=9t^2+6|M|+1<=(3|M|+1)^2, excluding the concentrated singleton case for m>=2. All these clauses are accepted at scope.

For four general shared rows, however, sum_J t_J=-t and therefore

sum_J(t+4t_J)=4t+4(-t)=0.

The source says its third divisibility follows by summing these four terms. That summation proves only gcd_J D_J divides0; it does not prove divisibility of3t. The precise first unsupported line is the third display in 'Shared-mask transfer without pure concentration', and the next sentence identifying summation as its proof. This is a localized proof gap, not a refutation of the previously accepted concentrated or per-row clauses.

The exact arithmetic nonimplication is t=1, t_J=(2,2,2,-7), D_J=(9,9,9,9): sum t_J=-t, every t+4t_J is divisible by9, but3t=3 is not. These numbers are NOT claimed to be realized by four product-spectrum rows; additional Boolean/primitive-factor information might still prove the coupled statement. coupled_gap.json deliberately labels this distinction.

odd_mask.py separately checks the correct per-row convolution and divisibility on all144 odd-mask rows in the existing45088-row catalogue. Their squared norms are1 (16 rows) or5 (128 rows). Consequently no four odd-mask product rows on four physical data bits can form a complete two-address Boolean function: their norms sum at most20 while a full cover needs64. This is a finite exact consequence of the earlier catalogue's completeness, not an all-dimensional odd-mask impossibility. The catalogue is not used to validate the disputed gcd inference, and absence of a counterexample there is not proof of it.

Consumers may use concentrated D|3t and arbitrary per-row D_J|(t+4t_J). They must keep the extra coupled gcd assertion CONDITIONAL pending a new argument. No shared claim or source was modified, and no corrective message was sent; this source-bound gap report is saved for supervisor dispatch to A034/B07/A079.
