# Independent reconstruction of the selector-only fixed-bank obstruction

Scope reviewed: A033's stage17 all-finite-C obstruction, based on even-dimensional quadratic bent signs with one physical point flipped. The whole terminal spectra are retained. This is an obstruction to paying EVERY history from a fixed controller-only reserve, not to choosing a paid history and not to FEI.

Let m>=2 be even, M=2^m, delta=1/M, g(y)=(-1)^(y1y2+...+y_(m-1)y_m), and h=g-2*1_{y=0}. Let f have selector children g,h, and write f=a+z b with a=g-1_{0}, b=1_{0}. Both children and f are Boolean. All Fourier coefficients of g are sigma_T/sqrt(M), with sigma_T in+-1 and sum sigma_T=sqrt(M), since g(0)=1. Thus ||a||^2=1-delta and ||b||^2=delta, with b's normalized spectrum uniform on M atoms.

Let P_a be the normalized squared spectrum of a. Direct expansion, using only the displayed signed sum, gives

chi^2(P_a || Uniform_M)=4/(M-1).

For completeness, the deviation of each unnormalized a coefficient squared from (1-delta)/M is 2 delta^(3/2)(sqrt(delta)-sigma_T). Squaring, summing, dividing by delta(1-delta)^2, and using sum(sigma_T-sqrt(delta))^2=M-1 gives exactly4/(M-1). The denominator is positive for m>=2.

The elementary log(t)<=t-1 inequality gives D_2(P_a||Uniform)<=chi^2/ln2. The exact selector-frequency grouping and H(g),H(h)<=m yield

Delta_z H(f)>=h2(delta)-(1-delta)D_2(P_a||Uniform)
>=delta*m-4delta/ln2.

Inf_z(f)=delta. Hence Delta_z H-C Inf_z>0 whenever m>C+4/ln2; any even m>=max(2,C+6) suffices because ln2>2/3. This works for every fixed finite rate C by choosing m first.

Independently, flipping the origin creates exactly2delta influence in every data direction, because g(0)=g(e_i)=1. Therefore I(f)=m/2+(m+1)delta. Grouping the two Fourier selector sectors gives H(f)<=m+h2(delta)<=m+1<=3m/2<=3I(f). This is an actual FEI-bounded Boolean family.

For t tensor copies, query only the t selector coordinates, then STOP. Tensor additivity leaves every g/h terminal intact and makes the stopped cost t*(Delta_z H-Cdelta)>0. It exceeds any fixed controller-only reserve as t increases while H/I<=3 remains valid. Any fixed protected-tag outer mask with nonzero branch mass beta scales that seed spend by beta; querying the tag itself is NOT reviewed here and must retain both interfering terminals.

Verdict: HOLDS at this exact scope, with no repair supplied by this reviewer. The argument does not pay an inherited reference conversion, establish a universal all-history upper bound, or refute an existential stopping tree. The new two-cell theorem excludes these arbitrary tensor seeds through its proved cubic tensor guard, rather than silently charging their entropy to an outer controller.
