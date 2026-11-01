# Separated spectral packets give a paid Boolean degree reduction

2026-09-30 UTC. Status: constructive scoped theorem. Full FEI remains open. No publication-priority claim.

## Main result and prior work

An actual Boolean function whose Fourier support lies in two sufficiently separated Hamming balls can be reduced to two genuine Boolean functions of smaller real degree. The entropy increase is paid by the original function's extra influence with a dimension-free constant. A separated Sidon family of balls has a corresponding multi-child reduction.

These statements use full commutative Boolean multiplication. They do not assume a decomposition exists for arbitrary spectra.

Related prior repository results are retained: the Sept21 Sidon-projection lemma (blob 391021a84f6fc8590c5e75e1a923e6926a25e320) and Sidon-address normal form (blob 2c935b165a106421aa6f26370d2f067409d1a892), the Sept20 spectral-lattice flat-cell/shared-branch theorem (blob 9f981c30a0c8a80b3cbad92eb531d17c64688e03, Section 6), and the Sept18 interference-patching programme summarized in solo-2026-09-17/NEXT_STEPS.md (blob ccd310f1f2b276f400f39520ebc6da795b9516a7). Their physical-coordinate and flatness hypotheses are not silently dropped. The present sufficient condition is separated radius-d frequency packets on the same physical variables, and its conclusion includes an original-influence-paid degree reduction.

Standard ingredients, not claimed new, are low-degree integer granularity, the nonzero polynomial support bound, the one-bit entropy split estimate, and Walsh entropic uncertainty. The latter is the flat-unitary case of Maassen–Uffink, *Generalized entropic uncertainty relations*, Physical Review Letters 60 (1988), 1103–1106, DOI https://doi.org/10.1103/PhysRevLett.60.1103 . In dimension 2^r the two bases have overlap 2^(−r/2), so its entropy lower bound is r bits. Bounded searches did not find the exact radius-d paid statement; novelty remains unverified.

## Conventions

The cube is uniform, Fourier coefficients are normalized, entropy H is in bits, and I(f)=sum_S |S|fhat(S)^2. Degree means real Walsh degree. Frequency addition is symmetric difference. B(b,d) denotes the Hamming ball about frequency b.

Two elementary polynomial facts will be used:

1. A nonzero real cube polynomial of degree at most d is nonzero on at least a 2^(-d) fraction of the cube. Choose a nonzero monomial of maximum degree k; after any fixing of the other coordinates, its top coefficient remains nonzero. Each k-dimensional fiber therefore has a nonzero value.
2. An integer-valued degree-d cube polynomial has every Fourier coefficient in 2^(-d)Z. In 0/1 coordinates its multilinear coefficients are integers by finite differences; substituting x_i=(1−y_i)/2 proves the claim. A Boolean degree-d polynomial has the stronger lattice 2^(1−d)Z when d>=1.

## Two packets force complementary Boolean pieces

Let d>=1, let D=|b|>4d, and suppose Boolean f has Fourier support contained in

    B(0,d) union B(b,d).

The balls are disjoint. Write uniquely

    f=c+chi_b g,

where c and g both have degree at most d. Squaring gives

    c^2+g^2+2 chi_b cg=1.

The first group has Fourier support in B(0,2d), and the cross term has support in B(b,2d). These balls are disjoint because D>4d. Hence

    cg=0,                 c^2+g^2=1                    (1)

pointwise. Thus c and g take values in {0,+1,−1}, their nonzero supports partition the physical cube, and

    h_+=c+g,             h_−=c−g

are Boolean of degree at most d.

As c,g are integer-valued degree-d polynomials, every nonzero coefficient of f has magnitude at least 2^(-d). Therefore

    H(f)<=2d.                                            (2)

This entropy cap is a consequence of the structural theorem plus standard granularity, not a granularity statement for arbitrary packets.

## The two-child step preserves every FEI constant at least two

Assume g is nonzero and put

    m=E g^2=Pr(g!=0),
    Hbar=[H(h_+)+H(h_−)]/2,
    Ibar=[I(h_+)+I(h_−)]/2.

The support bound above gives m>=2^(-d).

Introduce one fresh auxiliary bit y and the Boolean function

    F(y,x)=c(x)+y g(x).

Its Fourier coefficients are precisely the coefficients of c and g with separate y-labels. The original packets of f are disjoint as well, so H(F)=H(f). The standard one-bit restriction identity and its JS bound give

    H(f)−Hbar <= h_2(m)+(2/ln2)m
               <= m[log2(1/m)+3/ln2]
               <= m[d+3/ln2].                          (3)

No overlapping-product entropy subadditivity is invoked.

A direct spectral calculation gives

    I(f)−Ibar
      =sum_S [|b symmetric_difference S|−|S|] ghat(S)^2
      >=(D−2d)m
      >=(2d+1)m.                                        (4)

For d>=1, d+3/ln2 <=2(2d+1). Combining (3)–(4),

    H(f)<=Hbar+2[I(f)−Ibar].                             (5)

Consequently, if H(h_+)<=C I(h_+) and H(h_−)<=C I(h_−) for any C>=2, then

    H(f)<=C I(f).                                        (6)

The child degree is at most d, while nonzero g forces deg(f)>=D−d>d. This is a strict degree reduction. If g=0, f already has degree at most d and no reduction is claimed. For d=0, (1) leaves only a constant or character, with zero entropy.

In particular a counterexample of minimal real degree to a proposed universal constant C>=2 cannot have a nonempty shifted packet satisfying this two-ball hypothesis. This is not a statement that the children are physical restriction descendants.

## Several separated Sidon packets

Let b_0=0,b_1,...,b_{M−1} be distinct frequency centers. Assume every two different elements of

    {0} union {b_j symmetric_difference b_k : j<k}

have distance greater than 4d, and that the unordered pair differences in the display are all distinct. Suppose Boolean f is supported in the union of B(b_j,d). Write

    f=sum_j chi_(b_j) c_j,           deg(c_j)<=d.

The preceding frequency-separation argument, now applied to f^2, isolates every product packet. It gives

    c_j c_k=0 for j!=k,             sum_j c_j^2=1.        (7)

Thus the c_j are signed physical partition functions, not arbitrary low-degree real fields. Set m_j=E c_j^2. Every nonzero c_j has m_j>=2^(-d), so at most 2^d packets are nonzero. Integer granularity again gives H(f)<=2d.

Choose distinct binary labels ell_j in F_2^r for the nonzero packets and define, for each z in F_2^r,

    h_z(x)=sum_j (−1)^(ell_j dot z) c_j(x).

By (7), every h_z is Boolean of degree at most d. Pairwise character orthogonality gives

    E_z I(h_z)=sum_j sum_S |S| chat_j(S)^2.               (8)

### Entropy cost of recombination

Let (J,S) have joint law chat_j(S)^2, and q_S=sum_j chat_j(S)^2. The disjoint original packet labels give H(f)=H(J,S). Define a second joint law by

    Pr(S=s,Z=z)=2^(−r) hzhat(s)^2.

Z is uniform, because every h_z is Boolean; S has marginal q. Conditional on S=s, this Z-law is the squared normalized Walsh transform of the amplitude vector chat_j(s)/sqrt(q_s), extended by zeros at unused labels. The standard Walsh entropic uncertainty inequality gives

    H(Z|S=s)+H(J|S=s)>=r.

Consequently I(S;Z)<=H(J|S), and

    H(f)−E_z H(h_z)
      =H(J|S)+I(S;Z)
      <=2H(J|S)<=2H((m_j)_j).                           (9)

This identity retains the actual coherent recombination information. It is not a product entropy triangle inequality.

### The original influence pays the cost

Put m=sum_(j>0)m_j. When m>0, m>=2^(−d). There are at most 2^d nonzero shifted packets, so

    H((m_j)_j)<=h_2(m)+md
                 <=m[2d+log2(e)].                      (10)

The inequality includes the case m_0=0. Each shifted center has |b_j|>=4d+1, since its difference from b_0 appears among the separated differences. Therefore

    I(f)−E_z I(h_z)>=(2d+1)m.                           (11)

For d>=1,

    4d+2log2(e)<=3(2d+1).

Equations (9)–(11) yield the paid step

    H(f)<=E_z H(h_z)+3[I(f)−E_z I(h_z)].                 (12)

Thus any common FEI constant C>=3 valid for all h_z also holds for f. If any shifted packet is nonzero, all children have strictly smaller real degree. If no shifted packet is present, no reduction is asserted. The d=0 case is a single character.

## What remains necessary for the full conjecture

These packet hypotheses are genuine sufficient conditions and may fail for a general Boolean spectrum. No approximate packet theorem, no entropy-stable rounding result, and no universal search procedure finding such a separation is proved here. Additive collisions between packet differences are exactly where (7) ceases to follow term by term. A further proof must pay or retain those interacting products rather than discarding them.

The theorem does, however, explain why inserting a very small remote spectral tail cannot always repair an otherwise forbidden diffuse low-degree law: when the product packets separate, Booleanity forces actual complementary low-degree pieces and provides a paid reduction.

## Normalization check for the uncertainty inequality

For completeness, let U be the normalized N-by-N Walsh matrix and v a unit Euclidean vector. Its operator norms are ||U||_(1 to infinity)=N^(−1/2) and ||U||_(2 to 2)=1. Riesz–Thorin interpolation gives, for 1<p<=2 and q=p/(p−1),

    ln||Uv||_q <=(1/2−1/p)ln N+ln||v||_p.

Equality holds at p=2. For any Euclidean unit vector v,

    (d/dp) ln||v||_p at p=2 =−H_nats(v^2)/4.

Taking the left derivative of the preceding inequality at its equality endpoint, and using q'(2)=−1, yields H_nats(v^2)+H_nats((Uv)^2)>=ln N. Zero entries cause no problem, with 0 ln0=0. Dividing by ln2 and taking N=2^r gives exactly the r-bit inequality used in (9). This is the standard interpolation proof, included to make the padded-label normalization explicit.

## Verification ledger

- PROVED: exact two-packet Boolean decomposition (1), entropy cap (2), and C>=2 paid strict-degree reduction (5)–(6).
- PROVED: separated-Sidon multi-packet partition (7), exact entropy accounting (9), and C>=3 paid degree reduction (12).
- RECOVERED STANDARD INPUTS: polynomial support and coefficient lattice bounds, one-bit entropy/JS estimate, Walsh entropic uncertainty.
- NOT CLAIMED: full FEI, novelty, physical restriction closure, or existence of the packet hypotheses in every hard case.

The parent independently checked the two-packet decomposition, the auxiliary-selector entropy identity, the support bound, and the influence payment before publication. It also checked the multi-packet argument at the structural, conditional-Walsh-entropy, and scalar-payment level; the exact padded Walsh normalization is written above. No executable script or numerical certificate is used. The proofs above are finite exact analytic arguments.
