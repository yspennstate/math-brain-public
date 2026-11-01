# A031 review of A090-DEGREE-COARSENED-REFUND-OBSTRUCTION@1

Verdict ACCEPT_AT_STATED_SCOPE; no repair supplied, supervisor adoption
pending. The accepted source theorem is the complete degree-coarsening
obstruction in REPORT.md equations (1)-(19), including its all-width
analytic bridge. It does not assert that full conditional references fail.

Reconstructed critical argument: the derivative's queried block has a
Bin(w-1,1/2) residual subset; other block spectra have zero mass 1-q and
nonempty block degree law q*Bin(w,1/2) conditioned nonempty. In the queried
block, positive degree masses are at most 2(1-q) times that conditional
block law. A forced extra active block changes the Bin(m,q) block-count
likelihood by j/(mq)=j. Since j<=residual degree, this gives the source
pointwise domination mu_degree(t)<=[2q/(1-q)+2(1-q)t]nu(t).
The zero-block component has likelihood at most 1/(1-q) and total mass
2q, completing the domination without assuming uniformity within degree.

At degrees 1..n/2, the actual r_degree lower bound and (1-q)^m>=1/4
give mu_degree/r_degree<=4(t+1). Jensen and exact derivative mean
w-1/2 bound the head KL contribution by 2+log2(w+1/2).
The degree-zero contribution is nonpositive because r_degree(0)>=1/16
and mu_degree(0)=epsilon<=1/16. Markov bounds tail probability by 2/m;
r>=epsilon mu bounds its logarithmic likelihood by log2(1/epsilon)<w+1/2,
so the tail contributes less than one. This proves the source all-width
D_degree<=3+log2(w+1/2), hence M_degree/I>=w-4-log2(w+1/2)>=w/2
for w>=32. Its logarithmic comparisons follow from ln2>2/3 and e>8/3.

The source actual-spectrum entropy expansion was separately checked:
nonempty mass is4(1-q)^m times the product normalized factor law,
whose expected occupied-block count is1. Expanding -p log p gives its
equation (17). Dropping the stated negative term and using
m[-log2(1-q)]<8/5, h(W0)<=1 and (1-q)^(m-1)>=1/e>1/3 yields
H/I<=4+8/w<=6. Therefore the entire claimed conditional refund difference
is at least w/2-6, as stated. No source argument is repaired.

Independent implementation code/review_degree.py uses Fraction PGF
convolution to reconstruct the queried-block derivative law and separately
the size-biased Boolean degree law, then checks their equality and every
critical pointwise domination on two frozen widths4,5 (dimensions64,160).
No Boolean truth-table array at those dimensions is allocated. Exact
normalizations, mean, head predicates, tail mass and r>=epsilon mu are
checked in out/DEGREE_REVIEW.json. This is a different agent's analytical
reconstruction and critical implementation, not a rerun of source code.

The new A031 three-state statistic is a separate repair of the discarded
information, not a contribution to this original obstruction version.
It confirms degree-only failure while preserving the source theorem's
scope. The original source files and shared registries are untouched.
