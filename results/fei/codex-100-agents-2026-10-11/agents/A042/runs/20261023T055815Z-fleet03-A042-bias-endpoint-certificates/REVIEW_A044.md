# Scoped independent review of A044's complete flat reference

Source: A044-COMPLETE-DYADIC-REFERENCE-CARRY@1, statement hash
31700d6da9cd4b820a87ff0b8420023f970a09f56abdee380bd7ec219f41d2fc;
PROOF.md hash 6727f39a54e56743a355dca7e72dfbc6ceb57f5fa3e9f1a9e9f746c07938592b,
run 20261023T033305Z-fleet03-A044-non-symmetric-gate-classes.
Verdict: the complete-flat identity and Z-w<=9Delta-6R HOLD at stated
Boolean scope. This review does not independently certify every composition
and all-depth conclusion in the larger source claim. No source repair supplied.

Independent reconstruction: for each occupied label let t=|c|,
r=2^-j and u=t/r in (1/2,1]. Then W-P=v(r^2-t^2)>=0 and W-P<3P.
For a singleton with t<=1/2, r<=1/2 and r<2t, so r^2<=r/2<t.
Thus W-P<=v(t-t^2). For t>1/2, r=1 and
1-t^2=(1+t)(1-t)<=3t(1-t).
The actual half-derivative D takes values -1,0,1. Hence
E D^2>=|ED|=t, and Var(D)>=t-t^2. Summing singleton excesses
costs at most 3 sum_i v_i Var(D_i)=3(2Delta-R), by Parseval applied
to each derivative. High-degree excess costs at most 3(Delta-R).
The resulting SAME-spectrum sum is 9Delta-6R. Zero terms contribute zero.

The normalized complete Q has actual empty mass and Q(S)=wW(S)/Z.
For occupied S, P(S)/Q(S)=(P(S)/W(S))(Z/w). Multiply logarithms by
P and sum, including the empty ratio one, to get K=n-L and E=J+n-K.
Also n=w ln(Z/w)<=Z-w, using ln x<=x-1; n>=0 since Z>=w.
At w=0 use the actual empty point mass. No empty entropy has been silently
converted into a conditional law. This is a direct density-ratio proof,
independent of the source implementation.

The new direct-moment checker verifies Z-w<=9Delta-6R for all 986
nonconstant seed fixtures (including repeated parameter values), together
with actual complete-flat and two-level-tree normalization and exact
pointwise likelihood-ratio factors. These finite checks support, and do
not replace, the above all-dimensional proof. The source's published
check counts were not adopted as our own.

Downstream use: only this normalizer bound is imported into PROOF.md (10)
to show that the reference transfer is charged to epsilon times the seed's
original reserve. The main endpoint, sharp 3ln4 gate payment, complete KL
split and finite formulas are proved directly without importing the source.
