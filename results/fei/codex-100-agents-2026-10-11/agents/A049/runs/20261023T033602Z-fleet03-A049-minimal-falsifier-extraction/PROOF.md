# Divergent data histories after a fair activation pair

All cubes are finite and uniform; entropy and KL are in bits. Full FEI remains open. The new lemma concerns actual terminal eligibility, not the existence of an arbitrary-core reference supplier.

Let h be any Boolean sign on a data cube and set J_s(x,z)=s when x=0 and h(z) when x=1, for s=+1,-1. After the fair sign s is exposed, allow an arbitrary finite adaptive fresh DATA-only stopping tree T_s, chosen separately for each sign. Do not query x. Assume each actual terminal restricted core g has the supplied certificate H(g)<=4I(g). Both sign branches, every stopped leaf, and all physical reaches are retained.

Write mu_g=E g and S(g)=4I(g)-H(g). Direct pivotal probabilities give I(J_s(g))=(1-s*mu_g)/2+I(g)/2. Erasing x from the spectral set gives the mixture (delta_empty+p_g)/2. Its entropy is at most 1+H(g)/2 by retaining the fair mixture label; the erased coordinate contributes at most one further bit. Thus H(J_s(g))<=2+H(g)/2. Therefore

    4I(J_s(g))-H(J_s(g)) >= -2s*mu_g + S(g)/2.       (1)

This uses no point-factor, tensor, fixed-width, equal-child-mean or identical-policy assumption. In particular one activation child is allowed to have negative surplus. The lower bound is signed; replacing it by zero at each leaf would be unjustified.

For either sign, its stopping leaves form a disjoint cylinder partition of the original uniform data cube. Finite conditional expectation gives E_{leaf|s} mu_g=E h, even when the policy is adaptive and differs with s. Average (1) over both independent policies and the fair sign. The two mean terms cancel exactly, giving

    E_{s,leaf}[4I(J_s(g))-H(J_s(g))]
       >= (1/4) sum_{s=+,-} E_{leaf|s} S(g) >= 0.    (2)

This is the entire infinite-dimensional bridge: it is a finite partition identity for every dimension and every finite policy. It does not extrapolate a finite census. The fair sign, preservation of BOTH sign subtrees, and same initial core on both sides are used in the cancellation. No bound for an unpaired sign is asserted; its lower estimate in (1) may be negative. Arbitrary terminal core certificates are hypotheses, not a newly proved universal FEI statement.

Application to the current B10 incoming account: start with A046's specified original1/8 full-spike correlated lift for F_h, b first, any data-only prefix in b1, then one a or x exposure at selected leaves with its already paid prescribed1/7 correlated reset sigma1. Retain b0, every unselected leaf and all query siblings. The original margin satisfies M0-sigma1>1. The old eligible booking omega<=1/4 remains booked. At every a-pair allow arbitrary separately chosen subsequent finite data-only histories, transporting the SAME already-reset reference without further reset. Each terminal core remains a restricted tensor of point factors and has its elementary H<=4I certificate. Equation (2) applies at each original a-pair, so its complete mean surplus remains nonnegative. Pure x-descendants have nonnegative core surplus and retained character partners. The unchanged b0 contributes one. Hence the whole actual terminal S=E(4I-H) remains >=1 after ALL these divergent histories.

Let A0 be the original source KL, e=H0-Hf-4(I0-If), and keep the actual sigma1 from the first reset. Same-channel inherited transport retains the complete source/erasure/outcome/terminal chain. Exact algebra gives

    S-[A0+e+sigma1]_+ = min(S,M0-sigma1) >=1,
    S-[A0+e+sigma1]_+-omega >=3/4.                  (3)

No initial source, reset, old quarter or terminal debt is renewed. Equation (3) extends the incoming scoped theorem through arbitrary divergent post-a DATA histories, WITHOUT an additional reset. It repairs the specific frontier-eligibility gap; a further positive prescribed reset is a separate bill. The universal missing supplier for arbitrary cores is unchanged.

The incoming A046 constants are independently reconstructible: each width-r point has nonempty entropy8(r-1)delta(1-delta), empty entropy<=Var/ln2, ln2>2/3, and initial KL<=Var log2(8/7)<Var/4. Thus CE(point,q)<4I-delta, so M0>1+2t+m delta/4. A fresh1/7 full-spike factor has KL<=Var log2(7/6)<Var/4 (7^4<2*6^4). Both x/a reset choices introduce at most one quarter of the sum of conditional factor variances at the chosen frontier. The finite total-variance identity bounds this by m Var(original point)/4, yielding sigma1<m delta/4. Their difference is >1+2t. Actual inherited KL is subtracted in sigma1, never charged a second time.

Finite reset experiment, separate scope: code/check.py verifies b,a,first data query in either or both a-branches, resetting all queried children to the SAME full-spike1/7 activation lift. On the frozen six(r,m) pairs it finds a strictly negative second signed reset and a same-owner final margin>3/4. This is an exact finite certificate only. No statement that all subsequent reset increments are nonpositive in every dimension follows; that is the NEXT target. The experiment keeps reference-only rows and verifies every used atomwise likelihood product exactly before interval logarithms.

First unsupported line: extend the observed nonpositive post-a full-spike refresh to arbitrary widths, spectators and divergent histories, or price its positive part from the actual remaining original account. More fundamentally the complete correlated supplier for an arbitrary Boolean core remains unpaid. Neither line is hidden in (2)-(3).
