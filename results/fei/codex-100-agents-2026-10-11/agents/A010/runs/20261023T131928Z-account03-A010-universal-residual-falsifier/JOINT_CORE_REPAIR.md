# One fixed joint-core dictionary repairs this obstruction

Use precisely the family and original Q_r from TWO_CORES.md, r>=4. Let J be the uniform probability1/7 on every nonempty subset of the PUBLIC three-coordinate core K={z0,z1,z2}; it uses no target Fourier probabilities. Fix

    R_joint=(Q_r+J)/2

before sampling any spectral set. It is normalized; all actual clause anchor/allocation events and the new branch label are paid, and their complete output probabilities are summed before optimizing a posterior. This reference is outside the refuted class because it can output sets spanning K1 and K2. Then its COMPLETE nonempty cross entropy satisfies

    C_(R_joint)(f_r) < (3725/160) I(f_r) < 24 I(f_r).

## Uniform clause-law lower mass

For any nonempty physical output A, assign each of its coordinates to one support containing it, and let each local mask be its assigned coordinates (possibly empty). This is an allowed actual local-mask tuple; its union is A and it has at least one active anchor. All local mask probabilities are at least c=1/240: empty mass is15/16 and nonempty mass is exactly c. Hence the FULL fixed clause law has

    Q_r(A)>=c^(2r)/rho, rho=r/8.

Choosing a compatible tuple in this analysis does not alter the reference probabilities or priors. It is a selected real event giving a valid mass LOWER bound and thus a cost UPPER bound, unlike the full-law upper bound used for the obstruction. Therefore

    -log R_joint(A)<=1+log(r/8)+2r log240 < 17r

on every set involving a private coordinate. The last bound uses log240<8 and log r<=r for integers r>=1. On every nonempty pure-core set, R_joint(A)>=1/14 and its cost is <4.

## Exact physical private-sector mass

Let a=(3/4)^r. Parseval conditioned on the three physical core bits identifies the total Fourier mass involving at least one private coordinate with E_core Var_private(f|core). If z1=1, or z1=0 and z0=z2=1, the function is constant. There are two core assignments of probability1/8 giving the sign of A or B (variance4a(1-a)), and one assignment of probability1/8 giving the sign of AB (variance4a^2(1-a^2)). Thus

    M_private=a(1-a)+(a^2/2)(1-a^2)
              <=a+a^2/2 < (7/6)a,

because a<1/3 for r>=4. This is the true physical conditional variance, with the shared coordinates held fixed, not a disjoint-clone surrogate.

Consequently

    C_(R_joint) < 4 + 17r M_private
                <4+(119/6)ra
                <=4+(119/6)(81/64)=3725/128.

TWO_CORES.md proved I(f_r)>5/4, hence C/I<3725/160<24. No entropy of f pays this reference. Every other representation in the individual-core class still has the divergent lower bound already proved, while the infimum over any broader class containing this joint dictionary is at most this constant upper bound. The example therefore distinguishes both variational classes exactly.

## Remaining universal line

The joint core has only three public coordinates here. For an arbitrary core library its union may be large, and a uniform mask on the union can charge many coordinates whose spectral occupation is small. The unproved universal line is an influence-paid hierarchical or factored code for joint core combinations, retaining the global selector, local draws and physical allocation refund. This repair supplies a concrete calibration and a counterexample to the individual-core-only shortcut; it is not a universal core theorem or full FEI.
