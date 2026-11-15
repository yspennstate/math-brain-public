# FEIB24 proofs and boundaries

Coordinates are input bits with the order 0 < 1; Boolean outputs are -1 < +1. Fourier signs depend on whether the character is (-1)^x or its negative; all statements about squared coefficients are invariant. All logarithms are base two. Write delta_i = Inf_i, H^- = sum_i E_i, eta = log2(e), and Phi(p,q) = (p+q)h2(q/(p+q)), with zero terms interpreted continuously.

## 1. PROVED: what the reductions actually imply about constants

Let C_* = sup H/I, A_* = sup H^-/I, G_* = sup min_{i:delta_i>0} E_i/delta_i, over a restriction-closed class. Constants are omitted. Han's inequality gives G_* <= A_* <= C_*: the minimum coordinate ratio is at most its influence-weighted average, and H^- <= H.

Suppose G_* is finite. At each nonconstant restriction choose a coordinate with E_i <= G_* delta_i. The restriction entropy identity is H(f) = average H(f_+,f_-) + E_i + J_i, where 0 <= J_i <= 2 eta delta_i. Iterate until constants. The entropy terms telescope. Influence satisfies I(f) = delta_i + average I(f_+,f_-), so its terms telescope on the same tree. Thus H(f) <= (G_* + 2 eta) I(f). The same argument with arbitrarily near infima covers a supremum which is not attained. Consequently

    C_* - 2 eta <= G_* <= A_* <= C_*.

All three boundedness assertions are equivalent. Equality of the three optimal constants does not follow. The brief's asserted equality G_* = C_* and the transfer of the entire 6.5218 entropy lower bound to G_* need an additional argument not present in FLOW section 7. The deductions here transfer the lower bound only after subtracting 2 eta. No assertion that equality is impossible is made.

## 2. PROVED: parity leakage bounds every coordinate

Let Z = |U| modulo 2. Given U without i, the bits Z and 1[i in U] determine each other. Therefore

    E_i = H(Z | U without i) <= H(Z) = h2(epsilon),

where epsilon is the mass on even spectral sets (using its complement gives the same bound). Also E_i <= h2(delta_i), by dropping all conditioning. In particular, an odd function f(-x)=-f(x) has Fourier support on odd sets and E_i=0. This does not require monotonicity.

This is a universal lemma; `proof_checks.py` checks it on the entire six-variable permutation census. It is elementary and no novelty is claimed.

## 3. PROVED: exact base hidden-coordinate identities

Let k be odd, y0 have (k-1)/2 one bits, M = MAJ_k, and

    f(x,y) = M(y) OR (x AND [y >= y0]).

Outside y=y0, the extra clause changes nothing: if y >= y0 and y != y0 then |y| >= (k+1)/2. With outputs +-1,

    f = M + (1+x) 1[y=y0],

where x in this display is the +-1 coordinate. Put delta=2^-k and a=binom(k-1,(k-1)/2)/2^(k-1). The Fourier coefficients of the perturbation all have modulus delta. M has only odd Fourier levels. Exactly half of the perturbation's squared Fourier mass is on even levels; there are 2^k such sets, each with mass delta^2. Thus the even spectral mass of f is delta.

The x derivative is 1[y=y0], so delta_x=delta. Changing the output at (x=1,y=y0) creates a pivotal edge in coordinate j when y0_j=1 and removes one when y0_j=0. An individual such edge has influence mass 2^-k=delta on the remaining k input bits. Hence

    delta_j = a+delta if y0_j=1; a-delta if y0_j=0,
    sum_j delta_j = k a - delta,   I(f)=k a.

These signs matter: total influence is unchanged, rather than increased by 2 delta. Since a is the largest atom of a binomial law with k possible values, a >= 1/k. Thus I(f)>=1. For k>=3, delta<=1/(2k), giving delta_j>=1/(2k).

The parity lemma yields

    H^-(f) <= (k+1) h2(delta) <= 2 I(f).

For k=1, f is OR_2 and H^-=2 I. For k=3, I=3/2 and (k+1)h2(1/8) < 3, so the inequality holds. For odd k>=5, h2(delta)<=delta log2(e/delta), and (k+1)(k+eta)2^-k <= 6(5+eta)/32 < 2. The sequence decreases: the ratio at k+2 versus k is ((k+3)/(k+1))((k+2+eta)/(k+eta))/4 < 1 for k>=5. Since I>=1, this proves the claim.

The entropy inequality used above follows from -(1-t)ln(1-t)<=t, which follows by integrating 1/(1-u) over [0,t] and multiplying by 1-t.

Thus the large E_x/delta is harmless in this family: its absolute cost is at most h2(delta), and the entire erasure sum is at most twice the total influence.

## 4. PROVED: exact leaf formula after odd balanced substitutions

Replace each y_j by a disjoint, nonconstant, balanced, monotone, odd Boolean function phi_j. Odd means phi_j(-z)=-phi_j(z), so it has only odd-degree Fourier coefficients and mean zero. The phi_j may have different dimensions. Let F be the substituted hidden function, and let ell be a leaf in block j with tau=Inf_ell(phi_j)>0. For monotone phi_j, |phihat_j({ell})|=tau.

For a subset T of the outer variables other than j (including x), write p_T=fhat(T)^2, q_T=fhat(T+j)^2. Then

    Inf_ell(F) = tau delta_j,
    E_ell(F) = sum_T Phi(p_T, tau^2 q_T).                 (4.1)

Proof of the entropy formula. Fix the Fourier set on all other blocks. If a nonempty set remains in block j after ell is erased, both outer coefficients must come from a set containing j, and the two inner coefficients differ by the membership of ell. Their parities differ, so at least one inner coefficient is zero. That pair costs zero. If no element remains in block j, the absent coefficient is the outer coefficient without j, because phihat_j(empty)=0; the present coefficient is the outer coefficient with j multiplied by phihat_j({ell}). The products of other-block coefficients multiply p and q by the same nonnegative factor. Phi is homogeneous. Summing their squared factors for each occupied block gives 1, by balance and Parseval. This leaves exactly (4.1). The influence formula follows either by pivotal independence or summing the squared derivative coefficients.

Similarly the untouched x coordinate satisfies E_x(F)=E_x(f), delta_x(F)=delta. Each outer spectral set expands into a set of the same parity, because every occupied block contributes odd cardinality. Consequently the even spectral mass of F is still delta.

Let b=tau^2 delta_j. Concavity and homogeneity of Phi imply superadditivity: sum_T Phi(p_T,tau^2 q_T) <= Phi(sum p_T,sum tau^2 q_T). The sums are 1-delta_j and b. Their total is <=1. Increasing the first argument up to 1-b gives

    E_ell(F) <= h2(b).

Together with parity leakage,

    E_ell(F) <= min(h2(delta), h2(tau^2 delta_j)).        (4.2)

## 5. PROVED: a dimension-independent charging bound for the substituted hidden family

For k>=3, set r=sqrt(delta/delta_j). Using h2(t)<=t log2(e/t), (4.2) gives the following bounds. If tau>=r, then

    E_ell/(tau delta_j) <= h2(delta)/(r delta_j)
                         <= r log2(e/delta).

If tau<=r, then

    E_ell/(tau delta_j) <= tau log2(e/(tau^2 delta_j)).

The derivative of the last expression with respect to tau is log2(1/(tau^2 delta_j))-eta. For tau<=r, tau^2 delta_j<=delta<=1/8<1/e, so this derivative is positive. The expression is therefore at most its value at r. In both cases,

    E_ell/Inf_ell(F) <= sqrt(delta/delta_j) log2(e/delta)
                     <= sqrt(2k 2^-k) (k+eta) < 4.     (5.1)

For completeness, define B_k=sqrt(2k 2^-k)(k+eta). For odd k>=3,

    B_(k+2)/B_k = (1/2)sqrt(1+2/k)(1+2/(k+eta))
                <= (1/2)sqrt(5/3)*(3/2) < 1,

using eta>1. Also eta<3/2 gives B_3<(9/4)sqrt(3)<4. This proves the strict constant in (5.1).

For k=1, delta_j=1/2. From h2(t)<=t log2(e/t),

    E_ell/Inf_ell <= tau log2(2e/tau^2).

On 0<tau<=1 this is at most 2sqrt(2/e)/ln 2 < 3 (differentiate; the maximum is at sqrt(2/e)), hence also below 4.

Let I_B be the sum of all leaf influences. For any nonconstant balanced Boolean phi_j, I(phi_j)>=Var(phi_j)=1, by Parseval and |S|>=1 on its nonempty spectrum. Thus

    I(F)=delta + sum_j delta_j I(phi_j)
        >= delta + sum_j delta_j = k a >= 1.

Finally E_x(F)<=h2(delta)<=1<=I(F), and (5.1) bounds all other coordinates. Therefore

    H^-(F) = E_x(F)+sum_leaves E_ell(F)
            <= I(F)+4 I_B <= 5 I(F).                  (5.2)

This is a sum-over-coordinates charging argument for every hidden-coordinate gadget with arbitrary disjoint balanced odd monotone substitutions, including majority blocks and majority towers of any size. The special coordinate's unbounded ratio is paid from the total influence budget, not from its own influence. The family need not be closed under all restrictions, so (5.2) alone is not a new FEI theorem for its restriction closure.

## 6. PROVED: four simple coordinate rules fail uniformly

The following base hidden-coordinate bound also supplies a fully written divergence argument. The Fourier coefficient of MAJ_k at an odd-sized set T, |T|=r, has modulus

    b_r = a * binom((k-1)/2,(r-1)/2) / binom(k-1,r-1).  (6.1)

To derive it, choose j in T. The coefficient equals, up to a character sign, the coefficient on T without j of D_j M, the indicator of weight (k-1)/2 on the other k-1 bits. For a uniform middle slice on 2m bits,

    sum_l E[chi_S | middle slice] z^|S| over all S
      = (1-z)^m(1+z)^m = (1-z^2)^m.

Thus its coefficient at an even set of size 2s is (-1)^s binom(m,s)/binom(2m,2s), proving (6.1).

Under the normalized derivative spectrum of x, T is uniform over all subsets of k bits. For odd r with (k-1)/4 <= r-1 <= 3(k-1)/4, put m=(k-1)/2, s=(r-1)/2. The elementary product formula for binomial coefficients gives binom(m,s)>=2^min(s,m-s)>=2^((k-1)/8). Also a>=1/k and binom(k-1,r-1)<=2^(k-1). Hence

    b_r/delta >= 2^((k-1)/8+1)/k.

For sufficiently large odd k this is at least 2. The average coefficient ghat differs from the majority coefficient by a term of modulus delta, so |ghat(T)|>=b_r/2 and

    log2(ghat(T)^2/delta^2) >= (k-1)/4 - 2log2 k.

A binomial variable R~Bin(k,1/2) has variance k/4. Outside the displayed interval for R-1, |R-k/2| is at least (k-3)/4. Chebyshev gives outside probability at most 4k/(k-3)^2. Odd cardinality has probability 1/2 exactly. Since Phi(p,q)>=q log2(p/q) for p>=q, we obtain, whenever the right side is positive and the preceding b_r/delta condition holds,

    E_x/delta >= (1/2-4k/(k-3)^2) ((k-1)/4-2log2 k).

This tends to infinity; no sharp k/2 asymptotic is needed here.

Smallest influence fails: delta_x=2^-k is smaller than a-delta for large k, so the rule selects x. Largest normalized level-two mass fails too: all degree-two Fourier coefficients of the hidden f have modulus delta because majority has no even levels. Thus W_i^(2)=k delta^2 for every coordinate i, and maximizing W_i^(2)/delta_i is the same as minimizing delta_i.

Largest influence fails after majority substitutions: for MAJ_(2r+1), tau=binom(2r,r)/4^r <=1/sqrt(r+1). Proof by induction: the ratio at r+1 versus r is (2r+1)/(2r+2), whose square is <=(r+1)/(r+2), since expansion leaves the nonnegative difference 3r+2. Choose r+1>4^k. Then tau<delta; every block-leaf influence tau delta_j<delta, so x is the unique maximum. Formula (4.1) leaves its unbounded erasure ratio unchanged.

Most shortest minterms fails already with MAJ_3 substitutions. Every inner shortest positive certificate has width 2. The x clause has width 1+2(k-1)/2=k; the majority clauses have width k+1. Thus all shortest minterms contain x, while each designated-block leaf is in a strict fraction of those terms, and other leaves are in none. More explicitly, a leaf of a MAJ_3 block appears in 2 of its 3 minterms, so it appears in 2/3 of the shortest outer terms. Therefore x is the unique most frequent variable among shortest minterms and retains its divergent ratio. These are monotone functions on 3k+1 variables.

## 7. PROVED: complementary pivotal points defeat the minimum level-two rule

Let k>=6 be even, y0 have k/2 ones, and y1 be its bitwise complement. Let B(y)=1 iff |y|>=k/2, and define f(x,y)=B(y), except f(x,y)=x on y=y0 or y1. Both exceptional points lie in the middle layer, so changing either from 0 to 1 preserves monotonicity; consequently f is monotone in every coordinate.

In +-1 notation, if P=1[y in {y0,y1}], then

    f = B - (1-x)P,   D_x f=P,   g=E_x f=B-P.

Set delta=2^(1-k). The Fourier transform of P vanishes at every odd-sized T, and has modulus delta at every even-sized T, because its two point characters differ by (-1)^|T|. Thus every coefficient through x at total degree two is zero: W_x^(2)=0 exactly.

For y coordinates the two modifications cause opposite changes in edge influence, since y0_j and y1_j are opposite. Hence delta_j=a0=binom(k,k/2)2^-k for all j. The middle-slice generating-polynomial identity in section 6 gives the even Fourier coefficient of B at |T|=r:

    bhat(T) = (-1)^(r/2) 2^-k binom(k,k/2)
              binom(k/2,r/2)/binom(k,r).               (7.1)

Indeed B is the sum of its odd part, the tie-breaking odd-sign threshold which is zero on ties, and the indicator of the middle slice. Only that indicator contributes even levels. In particular |bhat({j,l})|=a0/(k-1). This is larger than delta for all even k>=6. At k=6 the ratio is binom(6,3)/(2(6-1))=2; its ratio at k+2 to k is 4(k-1)/(k+2)>1 for k>=6. (Directly substituting binomial coefficients gives the same inequality.) Subtracting a P coefficient of modulus delta cannot cancel a degree-two coefficient through a y coordinate. Every such coordinate therefore has W_j^(2)>0.

It follows that x uniquely minimizes W_i^(2)/delta_i.

To prove its ratio diverges, take even r in [k/4,3k/4]. The binomial product bound gives binom(k/2,r/2)>=2^(k/8); binom(k,k/2)>=2^k/(k+1), and binom(k,r)<=2^k. Thus (7.1) has modulus b_r>=2^(-7k/8)/(k+1). For all sufficiently large even k, b_r>=2 delta. Then |ghat(T)|>=b_r/2, giving

    log2(ghat(T)^2/delta^2) >= k/4 - 4 - 2log2(k+1).

The normalized derivative spectrum is uniform over the even subsets of k variables. Chebyshev for Bin(k,1/2), followed by division by the parity probability 1/2, puts at least 1-8/k of this mass in [k/4,3k/4]. Summing Phi(p,q)>=q log2(p/q) yields

    E_x/delta >= (1-8/k) (k/4-4-2log2(k+1))

for sufficiently large even k. This diverges. This construction proves that the minimum normalized level-two rule also has no universal constant. The exact finite checks, including all coordinate influences and level-two masses, are in `paired_hidden.json`, generated by `python3 priority.py python3 paired_hidden.py`.

## 8. OPEN: the remaining term/clause selector and general monotone FEI

The selector minimizing E_i/delta_i inside the intersection of variables occurring in a shortest minterm and in a shortest zero-certificate attains at most 2.944495303872 on the complete n=6 census. It uses the spectrum, so it is not a simple-data selector. The hidden-coordinate constructions above do not refute it: the exceptional coordinate is excluded by one of the two shortest-certificate conditions. No dimension-independent theorem for this selector is proved.

The general inequality H^-<=C I for monotone functions remains open. The preceding arguments use actual Fourier parity or an exact composition formula. The next obstruction explains why the two singleton identities alone cannot supply a proof.

## 9. PROVED: singleton masses and their square sum alone cannot bound erasure

This is an obstruction to a proof using only two necessary spectral identities; it is not a Boolean counterexample.

For each integer n>=100 put p=1/n, let K~Bin(n,p), and q=Pr[K>=2]. Define rho to be the product Bernoulli-p law on subsets of [n], conditioned on cardinality at least two. Let d=rho[i in U], the same for every i, and b=1/4. Set

    delta = (1-sqrt(1-4 b d))/2,

so delta=delta^2+b d. Define a probability law mu by assigning mass b rho to sets of size at least two, mass delta^2 to each singleton, and the remaining mass 1-b-n delta^2 to the empty set.

Here are elementary checks of validity. The bound ln(1-x)>=-x/(1-x), obtained by integrating the increasing derivative, gives (1-1/n)^(n-2)>=e^-1>1/3. Therefore

    q >= Pr[K=2]
      = (n-1)/(2n) (1-1/n)^(n-2) >= 1/12.

Thus d<=p/q<=12/n, b d<=3/n<1/4, delta<=2 b d<=6/n, and n delta^2<=36/n<=0.36. The empty mass is at least 1-1/4-0.36>0. Every mass is nonnegative and the masses sum to one. The marginal of coordinate i is precisely delta^2+b d=delta, and mu({i})=delta^2. In particular

    mu({i})=Pr[i in U]^2,   sum_i Pr[i in U]^2<=1,

exactly the squared singleton identity and its Parseval consequence used for monotone Boolean functions. Coefficient signs can be assigned consistently to make all singleton coefficients positive, but the resulting inverse transform is not claimed Boolean.

For each i restrict its entropy sum to T without i having |T|>=2. Both endpoints T and T+i lie in the conditioned product part and have ratio p/(1-p). Their total mass over these T is

    (b/q) Pr[Bin(n-1,p)>=2].

Consequently

    E_i >= (b/q) Pr[Bin(n-1,p)>=2] h2(p).

For n>=100, Pr[Bin(n-1,p)>=2] is at least its size-two atom,

    (n-1)(n-2)/(2n^2) (1-1/n)^(n-3) >= 1/12,

using the same exponential bound and (n-1)(n-2)/(2n^2)>=1/4. Since q<=1 and delta<=6/n,

    (sum_i E_i)/(sum_i Pr[i in U]) = E_i/delta
      >= n h2(1/n)/288 >= log2(n)/288 -> infinity.

The last inequality drops the nonnegative second term of h2(1/n). Thus the two singleton constraints, even with exchangeability, are insufficient for the desired universal inequality. Any successful argument using them must also use genuinely Boolean or monotone Fourier constraints beyond those two facts.

## 10. CHECKED NUMERICALLY and HEURISTIC boundaries

CHECKED NUMERICALLY: the n<=6 finite maxima in RESULTS.md and census_summary.json, the complete unrestricted NPN comparison through n=5, the saved hill-climb/sample witnesses, the original and complementary hidden functions, and the composition identities on the exact truth tables named by proof_checks.json. These use integer transforms and floating-point logarithms. High-precision extremizer checks are separately recorded; the exhaustive ordering is not interval-certified.

HEURISTIC: finite good-coordinate ratios appear moderate; all-dimensional boundedness does not follow from this census. No universal constant is proposed for all monotone functions. The remaining shortest-minterm/shortest-maxterm oracle is a candidate to investigate, not a proved rule.
