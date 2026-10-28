# A shared-core obstruction surviving every uniform-mask activation retuning

Fix any integer w>=8 and r=w*2^w. Let X_1,...,X_r be disjoint private blocks of width w and let z be ONE common physical bit. Put U=product_j OR_w(X_j), T=z OR U, f=2T-1. The supplied supports E_j={z} union X_j all have size w+1 and their read at z is r. Write epsilon=2^-w, p=1-epsilon, a=p^r, b=1-a. Direct physical pivots give

    I(f)=b+J,  J=a*r*w*epsilon/p=a*w^2/p,       fhat({z})^2=b^2. (1)

Here {z} uses the sign coordinate 2z-1. The expansion f=(1+g)/2+(2z-1)(1-g)/2, g=2U-1, proves the coefficient and private Fourier identities without treating copies of z as independent bits.

Consider ANY reference with this sampler: choose ANY probability distribution on a NONEMPTY set K of active support instances; conditional on K draw an independent UNIFORM nonempty subset in each active E_j and decode their union. The activation law may be dependent, may come from any independent gate weights conditioned nonempty, and need not satisfy incidence constraints. A mixture of any such references is also allowed. The dictionaries themselves remain these E_j with uniform nonempty subset laws. For the output to be exactly {z}, every active local subset must be exactly {z}. Hence with N=2^(w+1)-1,

    Q({z}|K)=N^(-|K|)<=1/N, and therefore Q({z})<=1/N. (2)

This bound survives EVERY activation choice and every convex mixture; no output-dependent law is used. It applies in particular to every feasible global fractional activation vector and to A006-style forced-anchor samplers with arbitrary anchor weights, because conditional on the active supports their subset draws have this uniform independent law. If some positive spectral output has Q=0 its cost is infinite and the same obstruction holds.

The elementary binomial inequality (1-1/m)^m<1/2 for m>=2 follows from (1-1/m)^(-m)=(1+1/(m-1))^m>1+m/(m-1)>2. With m=2^w it gives a<2^-w. The ratio w^2/2^w decreases for w>=3, so for w>=8

    J< (w^2/2^w)/(1-2^-w)<=64/255<1,
    I(f)<2, b^2>(255/256)^2>1/2, log2 N>w.

All nonempty reference lengths are nonnegative. From the single ACTUAL Fourier atom {z} and (2),

    C_Q(f)/I(f)>=b^2 log2 N/I(f)>w/4 -> infinity. (3)

This is a stronger scope of dictionary obstruction than failure of one fixed width-dependent activation law: it rules out ALL activation retunings and arbitrary mixtures while the uniform subset dictionary is kept fixed. It does not refute changing the dictionary to include a core atom, as A008 already does, and it does not refute FEI.

For completeness these actual Boolean functions have bounded FEI ratio. Let nu=Uhat^2/a be its product private-block distribution. A clause has entropy h_w=2w epsilon+(1-2epsilon)log2(1/p)<2w epsilon+(3/2)epsilon, using ln2>2/3 and -p ln p<=epsilon (or the weaker -ln p<=epsilon/p with p>=255/256). More directly use h_w<2w epsilon+(3/2)epsilon/p. Thus

    H(f)=2a H(nu)+2b h2(a)=2a*r*h_w+2b h2(a)
         <(4+3/w)J+2b h2(a)<= (35/8)J+2b <=(35/8)I(f).

The exact entropy identity follows by grouping the empty/core coefficients a^2,b^2 and the two equal private coefficient copies Uhat(B)^2 for every B nonempty. The only entropy inequality used is h2(a)<=1. This confirms that (3) is a coding-family obstruction on a bounded-entropy actual Boolean family.

Universal bridge: C020 now needs a changed core/intersection dictionary, not merely a better fractional activation optimizer for the same uniformly sampled clause masks. The convex dual in DUAL.md remains useful after supplying such dictionaries and allocation witnesses; it cannot bypass (2).
