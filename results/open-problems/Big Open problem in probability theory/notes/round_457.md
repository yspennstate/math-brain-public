# Round 457 current reduced obstruction map

Round 457 summarizes the reduced obstruction map after the annular and
endpoint corrections.

The original fixed-density spread-return profile has been decomposed into:

1. a few-root coverage branch, where radial level entropy is reduced to
   interval-cover entropy and the net defect gain is
   \[
     (2\delta-\kappa)L_H;
   \]
2. a many-root branch, with at least \(\kappa L_H\) time-disjoint root
   exterior returns.

Both branches require endpoint-controlled annular insertion estimates.  Those
estimates split further into:

1. annular transfer control, captured by the boundary exponent
   \[
     \Gamma_{\rm ann}(G)<1/Q;
   \]
2. endpoint \(L^2\) control for the skeleton weights.

Endpoint \(L^2\) control is not automatically supplied by the earlier
percolation two-replica profile, because the skeleton weights are
deterministic \(Q\)-weighted counts.  But Round 456 shows that failure of
endpoint \(L^2\) control extracts a support-congestion boundary set \(U\).

Thus the current live proof program has three named analytic obligations:

* prove an annular boundary SAW gap \(\Gamma_{\rm ann}(G)<1/Q\), or replace it
  by a weaker cut estimate;
* control deterministic endpoint support-congestion profiles for the relevant
  skeleton families;
* bridge those deterministic support profiles to the existing percolative
  finite-set/two-replica escape machinery, if possible.

This is progress over the raw spread-return entropy problem: the remaining
obstructions are now localized boundary-vector and support-congestion
statements rather than arbitrary subsets of return levels.
