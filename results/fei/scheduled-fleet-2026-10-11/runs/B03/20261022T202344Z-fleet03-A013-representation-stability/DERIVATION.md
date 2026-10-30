# Independent reconstruction of the three-row extension

The new three-row collision and reference identities hold at the stated scope. This is a review of A012 v5's new increment, not independent acceptance of its entire inherited grammar: earlier A013 work is a credited input. Full FEI remains open.

## 1. Exact owner and private correlation

Let c be any Boolean sign on three uniform shared coordinates, let w0,w1,w2 be distinct rows, and let Ej be arbitrary events on one independent private cube. The events need not be independent of one another. Set qj=Pr(Ej), G=c and H=c(1-2 sum_j 1_(s=wj)1_Ej), and select G or H with a fresh uniform bit z. Row disjointness, rather than event independence, makes H Boolean. Put d=sum qj/8, delta=sum qj^2/8, a_T=chat(T), and b_T=sum_j c(wj)chi_T(wj)qj/8.

On private frequency zero the parent amplitudes are a-b and b. On every nonempty private frequency the G amplitude is zero, so the two parent selector amplitudes have equal squares Hhat^2/4. Parseval gives private H mass 4(d-delta). Therefore, writing Phi(A,B)=(A+B)log2(A+B)-Alog2 A-Blog2 B,

    B_z=2(d-delta)+sum_T Phi((a_T-b_T)^2,b_T^2).

This calculation uses the actual JOINT private transform and does not factor the events. Also I_z=d and I(F)=(I(G)+I(H))/2+d on the original physical coordinates. Affine changes of shared variables used in classifying B_z do not preserve individual physical influences and are not used in that identity.

## 2. Tangent inequality, convexity and coverage

For a fixed 0<r<1, Gibbs gives Phi(A,B)<=lambda A+mu B, where lambda=-log2(1-r), mu=-log2 r. The axes follow by continuity. Since r(1-r)<=1/4, lambda+mu>=2. Thus

    Phi((a-b)^2,b^2)-2b^2
      <=lambda a^2-2lambda ab+(lambda+mu-2)b^2.

Here b is affine in the row probabilities. The coefficient of each squared coordinate is nonnegative; the expression is convex along every coordinate. Adding the linear -2d preserves this property, so successive chord inequalities bound B_z-4d by its maximum at the corners of a box. If a=0, the left side is identically zero and is omitted exactly. Upper rounding of lambda and mu still bounds both nonnegative squares, and preserves their required sum.

Every ordered triple of distinct F2^3 points maps to (0,1,2) under an invertible affine map. Common signs and characters then reduce all 256 phases to the 16 explicitly checked representatives. For each representative the saved A012 boxes are re-evaluated, without importing any author module. The independent logarithm implementation maintains a 160-bit enclosing interval for a normalized positive ratio. Squaring and, when appropriate, dividing by two recover successive binary logarithm digits with outward rounding. An ambiguous digit returns the full remaining tail; after 64 digits the upper bound adds one final unit. Consequently every returned integer divided by 2^64 is an upper bound. This is different arithmetic from both source implementations, which use atanh series.

All 1,326 tangent boxes have strictly negative maxima, and all 384 other boxes satisfy their declared analytic domain. Duplicate boxes, range, exact dyadic volume one and absence of nested boxes are checked. A finite closed union inside the unit cube, of volume one and with disjoint interiors, covers the whole cube: a nonempty relative open complement would have positive volume. Boundary faces therefore are covered too.

For completeness, the analytic domains follow from delta<=min(d,8d^2) and concavity: B_z<=2d+h2(delta)-2delta. For 0<d<=1/32 set x=8d<=1/4. The increasing bound yields B_z/d<=2+x(1+1/ln2-2log2 x)<=2+(5+1/ln2)/4<4; ln2>2/3 suffices. For d>=1/6, maximize h2(u)-2u at u=1/5, obtaining B_z<=2d+log2(5/4)<2d+1/3<=4d, using (5/4)^3<2. At d=0 all events vanish almost surely and B_z=0. There is no division by d on that boundary.

This proves the all-real probability statement B_z<4d for d>0. Private finite dimension is arbitrary because the exact identity depends only on q. The baseline scalar JS bound then gives Delta_z<=Kd, K=4+2/ln2<7. This scalar JS estimate is an explicitly retained dependency, not a newly certified universal estimate.

## 3. Complete reference and physical stability

Partition a supplied normalized child reference into individual private-zero atoms and one private-nonzero category. Replace category masses by their true spectral masses and retain the original conditional reference inside the private category, including off-target atoms. The CE improvement is categorical KL, hence nonnegative. If the true private mass is zero the whole category is assigned zero; no division by zero is performed. The pure G reference becomes its spectrum.

For the parent, use actual probabilities on private-zero atoms and assign R_Hcal(T,U)/4 to each of the two selector sectors when U is nonempty. Its mass is (1-rho/2)+rho/2=1, where rho is the true private H mass. Both the support and every off-target private mass are retained. Expanding the log ratio gives D_F=D_Hcal/2 exactly. Thus CE_F=(CE_Gcal+CE_Hcal)/2+Delta_z; if both ACTUAL children have complete CE<=KI, the parent does too. Nothing pays or removes arbitrary opaque child entropy. An independent common terminal factor adds its entire CE, KL and influence by tensor additivity.

A private restriction replaces each event by its actual cofactor, retaining their common private cube. A shared-coordinate restriction leaves at most two shared coordinates, so the inherited overlap<=2 rule applies. A selector restriction chooses an already certified actual child. These observations check only the NEW node's hereditary operation assuming the earlier grammar's established hypotheses. They do not re-audit all earlier admission rules or the five-bit grammar-nonmember argument.

For an explicit union-of-cells representation, prefix every G cell by z=+ and every H cell by z=-. Gate count is at most N_G+N_H, with one additional selector-literal incidence per cell. Densities are pi_j/2 before simplification. After a physical query discard contradictory cells, remove satisfied literals, merge duplicates if the declared convention does so, and recompute the number N' of live nonconstant cells and their densities pi'_j. For uniform weight lambda=1/N', the independent root-reference Bernoulli parameter is pi'_j/(N'+pi'_j). A last satisfied literal may create a constant union: then use the vacuum reference. These root/name probabilities are reference metadata, not actual witness-root probabilities. No contraction of the original L,S,R helper expectations is asserted; earlier counterexamples remain valid.

## 4. Four-shared-bit scope control

Let c(s)=(-1)^(s0*s1+s2*s3) on four shared bits, h equal c with its value at the origin flipped, and F=mux_z(c,h). This is an actual five-bit Boolean function. The Walsh coefficients of c are +1/4 ten times and -1/4 six times. Consequently h has squares 1/64 ten times and 9/64 six times, while F has squares 9/256 ten times, 25/256 six times, and 1/256 sixteen times. Direct Walsh reconstruction checks these distributions and I_z=1/16.

The exact entropy surcharge is

    Delta_z=3+(9/64)log2 3-(75/64)log2 5.

It exceeds 7 I_z: multiplying by 64 and exponentiating reduces this strict claim to the checked integer inequality 3^9*2^164>5^75. Also B_z=(10 Phi(9,1)+6 Phi(25,1))/256>4 I_z; its checked integer form is 10^100*26^156>2^64*9^90*25^150. This is a concrete instance of the existing bent-edit obstruction, not a new universal counterfamily. The physical total influence is 37/16, with child influences 2 and 5/2. FEI is unaffected; a complete growing-overlap transfer needs unused shared or terminal surplus instead of a selector-only bound at the three-bit constant.

## 5. Audit scope and remaining line

The new v5 three-row collision payment and its complete-reference transport are reconstructed at their stated hypotheses. Independent finite fixtures check zero/full events, equal events, complementary and correlated events, unequal probabilities, all 256 phases, and references with mass off true private support. These fixtures verify identities, while the complete probability-cube cover supplies the continuum bridge. The fresh selector, independent shared/private coordinate blocks and pure shared child are essential hypotheses. The four-bit witness explicitly defeats dropping the width restriction. Both-private branches are not admitted by the proof.

First unsupported line: arbitrary three-bit conditional rows with four-to-eight separately varying entries reduce to at most three edited rows, or satisfy the corresponding signed all-row tangent payment directly. There is no such reduction here. Beyond that finite shared width, the four-bit example already requires a nonreused shared/terminal surplus. Lean source for the quadratic chord is saved, but compiler admission was refused by memok (exit 1); no Lean-checked result is claimed.
