# A quantitative common incoming-road gauge

This checks Lemma `found:lem-common-gauge` in OpenAI, *Strict convexity and differentiability of the planar exponential first-passage limit shape*, September 24, 2026. The [current primary source](https://github.com/openai/math/blob/main/preprints/Strict-convexity-and-differentiability-of-the-planar-exponential-first-passage-limit-shape-September-24-2026/build/sections/strict/foundations.tex) is saved as [strict-foundations-current.tex](strict-foundations-current.tex). The result below is conditional on the stated product-cell and comparison-network hypotheses. It does not establish the strict-convexity theorem.

## 1. Precise hypotheses and bound

Use the independent coarse cells, comparison labels and gauges of the finite-cell lemma. Let `H >= 2` be an integer and put

`R=8H+20`, `m=(2H+1)^2`, `q=(4H+1)^2`,

`N=(2R+1)^2 2^q`, `L=2R+4H+22`, `J=L+4R+4H+11`.

Write `A_z` for the nonempty sets `S` with cardinality at most `m`, infinity-diameter at most `2H`, and `z in Q_R(k(S))`, where `k(S)` is the lexicographically least point of `S`. Put `z_S=k(S)+(R+4H+10)e_1`.

In world `j`, cell `u` contains `(a_u,b_u^j)`. The whole array `a` is the baseline's incoming input: its own actual tube weights, its private exterior completion and its road seeds. The array `b^j` contains the remaining world inputs. Assume that the `a_u` are independent and each `b^j` is a product array independent of the entire array `a`. The different `b^j` arrays may share coordinates and may contain different auxiliary labels. Independence is required within each world, not across worlds. The separate joint-law hypothesis below concerns the actual world environment and the random baseline anchor; equality of all auxiliary marginals across worlds is unnecessary.

Let `F_I^j=sigma(a_u,b_u^j : u in I)` and let `Pi_S^j` be the paper's inclusion-exclusion projection with respect to these fields. Let `V_(z,lambda)^j` be its integrable calibration value at the indicated anchor. Assume every ordered same-index or nearest-neighbor comparison has a local approximation `E_ab^j`, measurable on `F_(Q_H(z))^j`, satisfying

`||E_ab^j-(V_b^j-V_a^j)||_1 <= K beta`,

with one constant `K` for all required labels and worlds. Increasing `H` once absorbs the fixed attachment support if necessary; all the constants below refer to that chosen `H`.

For a baseline anchor at index `z`, its `L` preceding periods end at an anchor at index `y=z-L e_a`, where `a=1` for the A-road and `a=2` for the B-road. The common signed baseline cost `Q_(y,z)` is an integrable function of `a` alone. Assume its period defects in each world are nonnegative with mean at most `beta`. Additivity then gives

`||Q_(y,z)-(V_z^j-V_y^j)||_1 <= L beta`.  (1)

Finally assume the random baseline anchor and the world environment have the same joint law in each world and the same measurable calibration map is used. Section 5 checks these assumptions for the private-completion insertion, given an admissible input road with period excess at most `beta`.

For the gauge defined by the paper's formula,

`g_z^j=E V_z^j + sum_(S in A_z) Pi_S^j(V_z^j-V_(z_S,0)^j)`,

there is a common function `g_z^in` of incoming inputs in `Q_(R+2H)(z)` alone, with

`E |g_z^j-g_z^in| <= C_common beta`,

where

`C_common = N 2^m [L+J K]`.  (2)

The bound does not grow with the number of worlds. For `H=2`, it is

`C_common=5329(102+265K)2^106`.

## 2. A comparison route avoiding the projected cells

Fix `S in A_z` and translate indices so that `z=0`. Write `k=k(S)`. Then `|k|_infinity <= R` and `S subset Q_(2H)(k)`.

If the baseline is an A-road, `y=(-L,0)`. Follow the horizontal segment from `y` to `(k_1-R,0)`. Its length is `L+k_1-R`, which lies between `L-2R` and `L`. Its endpoint is on the west side of `Q_R(k)`, because `|k_2|<=R`. Every point of the segment lies outside or on that square.

For a B-road, `y=(0,-L)`. Follow the vertical segment to `(0,k_2-R)`. Its length is `L+k_2-R`, again between `L-2R` and `L`, and its endpoint is on the south side of the square.

In either case, follow the shorter square-boundary arc to `k+R e_1`. The boundary has `8R` edges, so this takes at most `4R` edges. Then take `4H+10` eastward edges to `z_S`. The complete route has at most `L+4R+4H+10` edges. At `y`, first switch from the baseline label to the network's label 0. Counting this switch gives at most `J` comparisons.

Every route vertex `u` has `|u-k|_infinity >= R`. Since `R>3H`, no cell in `Q_H(u)` belongs to `Q_(2H)(k)`: a cell in both would imply `|u-k|_infinity <=3H`. Thus every local comparison support, including the switch at `y`, is disjoint from `S`.

For a nonempty `S`, independence and inclusion-exclusion imply `Pi_S^j E=0` for any integrable `E` measurable on such a support. Its operator norm on L1 is at most `2^|S| <=2^m`. Telescoping the comparison increments along this route therefore gives

`||Pi_S^j(V_y^j-V_(z_S,0)^j)||_1 <= J 2^m K beta`.  (3)

This route uses labels at intermediate grid anchors only. It requires no physical baseline path outside its own tube: the comparisons are signed estimates, rather than physical competitors.

## 3. Replace a calibration summand by a baseline summand

Subtract `Q_(y,z)` from `V_z^j-V_(z_S,0)^j` and insert `V_y^j`. The difference is

`[(V_z^j-V_y^j)-Q_(y,z)] + [V_y^j-V_(z_S,0)^j]`.

Projecting the first bracket and applying (1) costs at most `2^m L beta`. Applying (3) to the second bracket costs at most `2^m J K beta`. Hence

`||Pi_S^j(V_z^j-V_(z_S,0)^j)-Pi_S^j Q_(y,z)||_1 <= 2^m(L+JK) beta`.  (4)

There are at most `N` contributing sets: choose `k` in `Q_R(z)`, then a subset of `Q_(2H)(k)`. This overcounts admissible sets and is a valid bound. Summing (4) gives (2), once the common projected costs and means have been identified.

## 4. Common conditional expectations, means and independence

Put `A_I=sigma(a_u : u in I)`. For every integrable `Q` measurable on the full incoming array `a`, independence of `b^j` from `a` gives

`E[Q | F_I^j]=E[Q | A_I]`.  (5)

For a direct justification, multiply each side by a test function `f(a_I)h(b_I^j)` and integrate. Both integrals equal `E[Q f(a_I)] E[h(b_I^j)]`. A monotone-class argument extends this from products of bounded test functions to all bounded `F_I^j`-measurable tests. Truncation handles integrable `Q`. Thus the right side is a version of the left side.

Define the incoming projection

`Pi_S^in Q=sum_(I subset S) (-1)^(|S|-|I|) E[Q | A_I]`.

Equation (5) gives `Pi_S^j Q=Pi_S^in Q` in L1 for every world. It remains valid if different worlds share all or some of their exterior coordinates. In standard Borel input spaces the conditional expectations can be chosen as measurable functions of `a_I`; their marginal law is the same in all worlds, so the same functions work. For arbitrary collections of worlds this is a separate almost-sure identity in each world, which is enough for each asserted L1 bound. No uncountable intersection of exceptional null sets is used.

Let `m_z=E V_z^j`. The joint-law and common-map hypotheses make this deterministic number independent of `j`, even though the anchor is random. There is no assertion that `m_z=0`.

Set

`g_z^in=m_z+sum_(S in A_z) Pi_S^in Q_(y,z)`.

Every summand has mean zero, is incoming-measurable, and uses cells in `S`. Since `S subset Q_(2H)(k)` and `k in Q_R(z)`, their union is contained in `Q_(R+2H)(z)`. The baseline cost may depend on incoming inputs far from this support; taking its conditional expectation integrates those inputs out. The resulting random function reads only the displayed local inputs.

Combining (4) and the count of summands proves (2). Neither a union bound over worlds nor the number of labels enters the bound.

For two disjoint baseline tubes, their actual weight collections are independent. If their private input collections are jointly independent of each other and of the actual field, the two entire incoming sigma fields are independent. Their incoming gauges, including all anchor and interpolated values, are measurable functions of those independent fields and deterministic means. They are therefore independent. Spatially overlapping projections of private arrays do not spoil this: the arrays have distinct independent roles. Conversely, independence of each private array from its own tube alone would be insufficient; independence from the other baseline's inputs is needed.

## 5. Insertion of the same baseline into completed worlds

Let `T` be a deterministic edge tube containing every edge the original baseline can travel. For its period covariance assume `T+d=T`, where `d` is the road's direction vector; the infinite straight tubes used in the improvement construction have this property. Retain actual iid weights `eta_0` on `T`. Draw a private iid copy `c` of all edge weights on `T^c` and private original road seeds `u`, jointly independent of every actual edge and of every world completion. Let `xi=(c,u)`.

Form the hybrid environment `omega_tilde=(eta_0,c)` and run the original road rule on `(omega_tilde,u)`. This environment has the correct iid law. The road stays in `T`, so every traveled edge has its actual weight `eta_0`. Its path and marked cuts are functions only of `(eta_0,xi)` and are fixed once for all worlds.

Now let a world have environment `omega^j=(eta_0,zeta^j)` where `zeta^j` is an iid complement independent of `eta_0` and of `xi`. Regard the same baseline as a rule on this world with private inputs `xi`: the rule ignores `zeta^j` and substitutes `c` when the original rule requests a weight outside `T`.

This rule preserves tracking and the nominal parametrization. It also preserves locality: each requested actual or substituted weight has the same spatial location as the corresponding original input. Its private arrays remain product arrays independent of the world. Translation by `d` preserves `T`, and hence commutes with the substitution and the original road rule. The required marked-cut covariance follows. Finite expected period cost is unchanged because the hybrid environment and original seeds have their original law. Thus the inserted baseline is admissible.

Let `P^j` be the centered, dominated cocycle from the common calibration map in world `j`. For a marked cut, covariance and the cocycle identity give

`P^j(X_(i+1))=P^j(d)+P_(theta_d omega^j)(X_i(theta_d omega^j,theta_d xi))`.

The first term has mean zero; the second has the law of `P^j(X_i)` by joint shift invariance. Integrability follows from bounded tracking of a fixed marked cut and domination on finitely many deterministic edges. Therefore

`E[P^j(X_(i+1))-P^j(X_i)]=0`.

The actual traveled weights and path are the same as in the hybrid environment. Consequently the centered period cost `Q_i` has its original law and mean at most `beta`. Domination in the world gives the nonnegative defect

`D_i^j=Q_i-P^j(X_(i+1))+P^j(X_i) >=0`.

It follows that `E D_i^j=E Q_i<=beta`. Adding `L` period defects proves (1). No equality of the two worlds' calibration values was used.

Furthermore `(omega^j,eta_0,xi)` has the same joint law for all `j`: the own-tube marginal and private law are fixed and the independent complement has its fixed product law. Since `X_z` is a common function of `(eta_0,xi)` and `P^j` uses the same measurable map on `omega^j`, the pair `(omega^j,X_z)` has the same law in every world. Its integrable calibration value has the same mean `m_z`. This verifies the random-anchor mean hypothesis rather than replacing it by a zero-mean claim.

For the manuscript's primary and transition worlds, assign the baseline's narrow tube to `eta_0` and take the entire remaining world array as `zeta^j`, as in improvement lines 165–176. Deterministic partitions of iid actual weights and independent completions give precisely the required product complement. The primary and spare narrow tubes are disjoint, and their private arrays are chosen mutually independent and independent of the actual field. This establishes the claimed independence of their incoming gauges, subject to the stated tube containment and original road hypotheses.

## 6. Interpolation

For `t in [i,i+1]`, write `u=t-i` and use the same raw baseline costs in both interpolations:

`g^j(t)=g_i^j+Q(i,t)-u[Q(i,i+1)-g_(i+1)^j+g_i^j]`,

with the identical formula for `g^in(t)`. Subtracting gives exactly

`g^j(t)-g^in(t)=(1-u)(g_i^j-g_i^in)+u(g_(i+1)^j-g_(i+1)^in)`.

Raw costs cancel even during nominal pauses, provided occurrence labels are retained as stipulated in the paper. Thus the supremum of the absolute difference on one period is bounded by the larger endpoint absolute difference, and hence by their sum. On a prescribed bounded interval meeting `p` periods, summing over at most `p+1` distinct bounding anchors gives

`E sup |g^j-g^in| <= (p+1) C_common beta`.

This supremum also bounds any attachment chosen after inspecting those periods. The count is for a prescribed bounded parameter interval; no uniform assertion over an arbitrary random distant interval is needed.

## 7. Independent checks and remaining hypotheses

The earlier finite-cell bound has an independent derivation. Its projections equal the product of the one-coordinate centering operators on `S`, followed by integration outside `S`. Thus they have norm at most `2^|S|`, have mean zero for nonempty `S`, and annihilate a function missing one coordinate of `S`. Subtracting two gauges leaves a centered residual of norm at most `2 epsilon`, common projected errors, and cutoff errors. There are at most `2N` such projected terms. A boundary detour takes at most `4R+4H+10` steps plus one label switch, so the earlier bound is `2+2N(4R+4H+11)2^m`. Its `H=2` coefficient is `2*73^2*163=1737254`, with exponent `81+25=106`. This reproduces the earlier result.

For the new bound, `H=2` gives `R=36`, `L=102`, `J=265`, `N=5329*2^81` and `m=25`. Thus (2) becomes `5329(102+265K)2^106`; when `K=1`, its integer coefficient is `1955743`. These constants count signed comparisons and are not physical passage-time estimates.

The script [check_common_gauge.py](check_common_gauge.py) checks the earlier product identities by successive coordinate integration, independently of the earlier script's atom-projection implementation. Breadth-first boundary distances verify the new detour for every possible square center at H=2,3,5 in both baseline directions. Exact rational conditional expectations check three worlds with shared exterior coordinates, common projected incoming costs, random-anchor mean equality, and independent-block factorization. A negative control deliberately introduces exterior dependence and must produce unequal projections.

The numerical checks can also be derived without the enumeration. Expanding the formulas gives `L=20H+62` and `J=56H+153`. For an A-road, a west-side entry at relative height `-k_2` has shorter boundary distance `4R-|k_2|`. Its total detour is maximized at `k_1=R,k_2=0` and equals `J-1=56H+152`. For a B-road, the shorter boundary distance from relative point `(-k_1,-R)` to `(R,0)` is `2R+k_1` for `-R<=k_1<=R`. Adding the approach length and tail gives a maximum `L+3R+4H+10=48H+132`, attained at `k_1=k_2=R`. These give exactly the three pairs of distances printed by the script.

In the toy random-anchor check, the anchor bit is `X=a_0 xor a_1`. The incoming probabilities are `1/3,2/5,3/7`, so `P(X=1)=7/15`. The common calibration test map is `(2X-1)(b_0+2b_1+4b_2)+Xa_2`, with exterior bit probability `4/9`. Direct averaging gives `(-1/15)(28/9)+(7/15)(3/7)=-1/135`, agreeing with enumeration. The negative control compares two independent exterior bits; its expected absolute difference is `2(4/9)(5/9)=40/81`. These are finite-product checks of the probabilistic identities, not estimates for FPP.

The failed variants identify essential hypotheses. A baseline that reads the current world's exterior need not have common projected costs. Private arrays shared by two baselines need not give independent incoming gauges. A tube not preserved by the period shift need not give an admissible inserted road. None of these variants is used in the displayed primary/spare/transition construction; the proof above explicitly checks the corresponding restrictions.

The remaining unverified input is the uniform comparison-network bound with constant `K` for every label actually used downstream, together with the link estimates, phase constructions and closure of the improved road class. The present argument proves the conditional common-gauge step and the private-completion insertion facts; it does not turn those remaining inputs into established theorems or assess the full strict-convexity proof.
