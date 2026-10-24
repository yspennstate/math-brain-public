# Zero carrier does not mean zero signed branch

All cubes are uniform, outputs are signs, Walsh coefficients are normalized, and logarithms use bits. This is a repair of the existing A035 trace, with a concrete counterexample to deleting zero-carrier rows. It does not pay the universal FEI residual.

## 1. Family and exact scope

For every even m>=2, L>=1 and core point y*, retain the previous Boolean family

    f=b_m(y) product_j b_4(x_j) (-1)^[p(y) sum_j 1_(x_j=0) z_j],
    p(y)= parity(y) XOR 1_(y=y*).

Here b_r=(-1)^(x0*x1+...+x_(r-2)*x_(r-1)). Any selectors may first be fixed. Expose one private bit, then one core bit. The target selector remains free. Permuting quadratic pairs and the two coordinates in each pair justifies taking the private bit to be x_0; this preserves the origin indicator. The proof below covers any core coordinate, not merely those in the finite check.

Let c_-=b_m 1_(p=1), c_+=b_m-c_-, and write f=c_+G+c_-T before squaring. G and T are the signed product factors from stage5, with the target selector retained in T. After core restriction, let B=hat(b_m restricted), C=hat(c_- restricted). At each core frequency the homogeneous pair is (B-C,C). Dividing C/B is allowed only where B is nonzero.

## 2. Core support and the lost sector

Fix core bit y_k=s. Its quadratic mate t survives. The restricted carrier is (-1)^(s*t) times a bent sign on the remaining m-2 coordinates. Thus B is supported exactly at mate frequency s, with magnitude 2^(-(m-2)/2). The parity-weighted restricted carrier has the opposite mate frequency and the same magnitude. Let P denote its Fourier transform, including the sign (-1)^s.

If s differs from the corresponding bit of y*, there is no point surgery and C=(B-P)/2. If s matches, then

    C=(B-P)/2 + h,
    h(omega)=(-1)^parity(y*) b_m(y*) chi_omega(y* without k) / 2^(m-1).

This follows by expanding 1_(p=1)=[1-(-1)^parity(y)(1-2*1_(y=y*))]/2 before restriction. The supports of B and P are disjoint. On B=0, c_+hat=-C, which can be nonzero. The exact squared C mass on B=0 is

    inactive point slice: 1/4,
    active point slice:   1/4-2^(-m).

For the active slice, the three terms are ||P/2||²=1/4, ||h||² on the half-support=2^(-m), and the cross term -sum P*h=-2^(-(m-1)). The latter identity follows from Fourier inversion of the parity-weighted carrier at y* without k. No limit or interchange of infinite sums occurs. At m=2 the active value is zero: these boundary slices must not be asserted to contain a positive derivative sector. The inactive slice always has positive C mass.

## 3. Lossless trace repair

Reuse the private support flags of stage5. If the target private carrier vanishes, its signed target factors are (-q,q), so the target likelihood is 1/(2d). If another private carrier vanishes, the old other-off states apply. These statements retain rows of zero derivative and positive reference.

Otherwise all private carriers survive. Write epsilon for the target private quadratic sign and

    w=(3/4)^A (5/4)^(F-A) (1/2)^E (3/2)^(J-E).

F,J count the other free and fixed-one active modules, and A,E count their positive signs. A physically inactive exposed private block is a common spectator and is removed from these counts, with its full cost retained. The target signed pair, up to its common private carrier, is

    alpha=(B-C)+C*w*(1-epsilon/4),
    beta=C*w*epsilon/4.

If B!=0 this is the previous coherent state with ell=C/B. If B=0 it becomes

    alpha=C*[w*(1-epsilon/4)-1], beta=C*w*epsilon/4.       (Z)

The common signed C cancels in beta²/[d*(alpha²+beta²)] whenever the denominator is positive. The new state is therefore (zero-core,epsilon,w). It does not require the magnitude or sign of C as a likelihood label, but their squared masses are retained in aggregation. C=0 gives zero reference and derivative, so no division is performed. Every state with positive reference has a constant likelihood, including states of likelihood zero; this is exactly the finite KL equality criterion. Counts alone do not pay the KL or code length.

At most 3+12(F+1)(J+1) states suffice: the target-off state, two other-off states, at most four carrier ell types each with two epsilon values, and two epsilon values for zero-core (the displayed bound is conservative). On the active core slice ell=1/2 +/- 2^(-m/2); on the inactive slice ell=1/2. The finite checker uses the looser bound 3+12 L² since F+J<=L-1 implies (F+1)(J+1)<=L². This is an extension of the existing scoped trace, not a new universal Booleanity inequality.

## 4. Five-bit exact countercertificate

Take m=2,L=1,y*=0, expose the first private bit as zero and the first core bit as one. In the remaining coordinates (r,v,a,b,z), the actual Boolean function is

    f=(-1)^[r+a*b+(1-r)*(1-v)*(1-a)*(1-b)*z].

The core carrier is (-1)^r; c_-=1_(r=0). At empty data frequency the target selector signed pair is (-1/16,1/16), while B=0 and C=1/2. Direct character sums give d=1/16, mu=1/16, r_reference=1/128 and likelihood 8 at that row. Summing the eight rows with core frequency zero gives derivative-law mass 1/2 and complete reference mass 1/16. Deleting zero-carrier rows therefore destroys both normalized laws. This is an actual Boolean support obstruction, not a triangle inequality failure and not a counterexample to FEI. Replacing the signed contrast T-G by an incoherent mixture would change (Z).

The binary zero-carrier flag alone contributes

    D((1/2,1/2)||(1/16,15/16)) = (1/2) log2(64/15) > 1 bit

to the complete child KL. The strict inequality is exactly 64>4*15, with no numerical logarithm. The physical reach is 1/4 and child d=1/16, so the reached flag part of the d*D credit exceeds 1/64 bit. This is an identified part of the retained credit, not a claim that deleting and renormalizing a sector always changes the full KL by this amount.

## 5. Same incoming reference, both channels, both terminals

For each successive physical query keep the stage5 source-owned laws: parent selector pair alpha,beta; d=sum beta²; mu=beta²/d and r=alpha²+beta². Collapse only the queried spectral bit to obtain mubar,rbar. The actual physical child pair uses alpha0 +/- alpha1, beta0 +/- beta1. Its complete joint laws are P(s,U)=beta_s(U)²/(2d) and Q(s,U)=r_s(U)/2. Q retains mass 1/2 even in a zero-derivative child. Let

    delta=D(mu||r)-D(mubar||rbar),
    K=D(P||Q)-D(mubar||rbar).

Both are nonnegative conditional KL terms. The exact transport remains

    mean_child Lambda-parent Lambda=d*(delta-K),
    Lambda=sum beta² log2[(alpha²+beta²)/beta²].

A zero-d parent contributes zero price, without inventing a normalized mu. Across the private query and core query the two drifts telescope with their original physical reaches; a fresh d or child influence is not an additional bank. The checker verifies both channels at every stated parent and the full physical influence identity. It records complete H and I of every final child, including nonconstant inactive branches. These final children are retained terminal functions, not zero-cost leaves. Their recorded entropy is not claimed to be paid by a new reserve.

The first unsupported universal step is still a dimension-independent bound for these accumulated signed reference debits, the queried core costs and the retained terminal debts from one genuinely unused original influence/child reserve. The homogeneous trace resolves the division-by-zero interface; it does not resolve that payment.

## 6. Validation risks and proof rung

The risks are an incorrect point-surgery sign, conflating a vanishing carrier with a vanishing branch, losing zero-derivative reference mass, renewing child normalizers, and assuming the m=2 active slice is positive. Exact checks cover all of these, with m=2 and m=4, both point parities and both core outcomes. An independent five-bit implementation uses direct character sums and all 32 signed convolution shifts, rather than the transform or family builder. The core cancellation identity is submitted to Lean separately; its result certifies only that algebraic statement, not the entropy trace or FEI. The full scoped derivation is an author proof with exact certificates and independent-agent review pending.
