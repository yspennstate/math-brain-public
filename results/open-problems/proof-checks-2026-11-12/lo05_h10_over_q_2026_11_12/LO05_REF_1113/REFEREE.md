# Referee report on Sections 3 and 4 of paper_c.txt

Task received: 13 November 2026, approximately 20:20, Asia/Tbilisi.
Input SHA-256: `66c49b33aa151329eb8740f417638c0a2bcf122b12a07bfe53bee61165ac0517`.

This is an independent mathematical audit. No web searches, subagents, or parallel mathematical workers are used. The input is not edited. Computations use the Python standard library. Line references refer to the supplied extraction. External results checked only from memory are explicitly identified; agreement with a theorem quoted by this paper is not independent verification of that theorem's statement or proof. This distinction is particularly necessary for the 2026 companion preprints [48] and [49].

The text loses overbars on algebraic closures, sum/product signs, radicals, and parentheses, and moves some equation numbers across headings. Throughout, `Y(Q)` in geometric statements means `Y(Qbar)`, as the surrounding text requires. These are restored as extraction artifacts, not mathematical gaps.

The global mesh/checklist commands were attempted but cannot write their databases under this sandbox. This report and LOG.md provide the local audit trail.

## Lemma 3.1 — HOLDS (lines 739–775; (3.1)–(3.2))

Restore (3.2) as

\[
d=m_db,\quad b'=mb,\quad U=b\frac{1-dt^2}{1+dt^2},\quad H'=b'(b'-U^2).
\]

The cubic discriminant is nonzero for a nonzero parameter: its roots are 0, l, and -3l. In fact its polynomial discriminant is 144l^6 and the Weierstrass discriminant is 2304l^6. The existential encoding is valid: introduce inverse variables for every nonzero condition, coordinates for the two finite points, and nonzero square-root variables for `x=b'z²`; clear the fixed rational coefficients.

For q outside S1 put k=vq(b), assumed negative and odd. The multipliers are units. For t≠0, vq(dt²)=k+2vq(t) is odd, hence nonzero. The numerator and denominator in U have either both valuation zero or both valuation vq(dt²). For t=0 the ratio is 1. Thus vq(U)=k, vq(b'-U²)=2k, and vq(H')=3k. Exactly one of e and eH' has even valuation. Writing that parameter q^(2a)L and scaling x=q^(2a)X, y=q^(3a)Y preserves square classes. If vq(X)<0 the cubic has valuation 3vq(X); if vq(X)>0 it has valuation vq(X), because L and 3L are units. Both force even valuation. Unit X already has even valuation. Root points with nonzero X have valuation zero, so they do not escape the argument. This contradicts the odd valuation of b'.

No external theorem beyond elementary discrete-valuation arithmetic is needed.

## Lemma 3.2 — HOLDS (lines 777–837; (3.3)–(3.6))

The multiplier lists exist by weak approximation at finitely many places and the finiteness and openness of the local square-class groups (checked from memory). For M there are at most 2·8·4 prescribed sign/2-adic/3-adic tuples; multiplying by one representative corrects each possible input tuple. The same construction works for each Dm at S(m) and infinity. There is no uniformity requirement in b after the lists are fixed.

Near a local root dt²=1 the denominator tends to 2 and U tends to 0, so

\[
H'=b'^2(1-U^2/b')
\]

is positive over R and square at S(m). Additional smallness conditions at Supp(md)\S(m) are compatible with these by weak approximation. Since d>0, the real denominator is positive.

If q∈B\S(m), integrality of b gives the crucial **positive** odd valuation vq(b)=vq(b'). The ratio defining U is a unit: odd valuation of dt² proves this off Supp(md), and the explicitly imposed smallness proves it on that support. Consequently vq(U²/b')=vq(b)>0, and 1-U²/b' is square at this odd prime. For q∈B∩S(m), H' is square by construction. Hence θ is square at B and B∩J is empty.

For q∈J, q is outside S(m) and α=vq(b') and γ=2vq(U) are even. If unequal, vq(H')=α+min(α,γ) is even. They must therefore agree, and odd valuation of H' forces vq(b'-U²)>α. Thus b'/U²∈1+qZq is square, proving β square at J. If U=0 there is no J. The assertions at 2 and 3 are preserved on replacing by squarefree representatives; β≠1 because its class at 3 is nonsquare. Finally scaling (x,y) by (c²,c³) when H'=θc² verifies (3.6) directly.

The use of Hensel's lemma for 1+qZq requires q odd, which holds. No cited research result is needed here.

## Lemma 3.3 — HOLDS (lines 839–959; (3.7)–(3.17))

The split two-descent Kummer map and Selmer exact sequence are the standard results of Silverman [67, X.1.4 and X.4.2], checked from memory: characteristic different from 2, distinct rational roots, and local Kummer conditions at every completion are the hypotheses. All hold here. The references to Monsky [30], Mokrani [43], and Wei–Guo [72] are background; this proof supplies its own matrix and does not import a rank formula from those papers. I have not checked their exact section numbering or formulations against copies.

The replacement root values give τ1=(l,1), τ2=(3,-l), and their product (3l,-l). Indeed, 4l² and 12l² have classes 1 and 3, respectively. The signs and nonsquareness of l prove independence. At an odd prime the quotient E(Qq)/2E(Qq) has order |E(Qq)[2]|=4: the formal subgroup is uniquely 2-divisible, and the finite quotient has equal kernel and cokernel sizes under multiplication by 2. This argument works at bad primes as well.

At odd q∤3l, the integral distinct roots imply even coordinate valuations, including the replacement root values; the four-element unramified subgroup is therefore the whole local image. At q|l the two torsion classes have valuation vectors (1,0) and (0,1), hence exhaust the image. At 3, l≡2 and -l≡1 modulo 3; the classes of l and 3 generate the four first-coordinate classes, while both second coordinates are square. This proves (3.13).

For the 2-adic calculation, x=l+2u with u odd would give

\[
(y/2)^2=(l+2u)u(u+2l)\equiv l\pmod8
\]

when l≡3 modulo 4. Direct expansion gives the difference from l as 4(l+u) modulo 8, which is zero for odd l,u. The result is 3 or 7, impossible for a square. Otherwise, for odd nonroot x the two relevant differences have minimum valuation 2 and even valuation sum, so both valuations are even. The other cases and the torsion replacements also give even coordinate valuations. Only necessity at 2 is used for the upper bound.

Over R the permissible nonroot intervals are (-3l,0) and (l,∞). Thus the first coordinate is positive, and the sign of the second is a surjective character, witnessed by τ2. Its kernel has representatives (3^δ∏qi^ui,∏qi^vi), as in (3.14). Comparing at qi with τ1^ui τ2^vi gives, by dividing the unit parts,

\[
Ku+D_\lambda v=\delta\lambda,\qquad (K+D_s)v=0.
\]

The second unit quotient has residue bit (Kv)i+sivi; the first has (Ku)i+(δ+vi)λi. At 3, the second coordinate being square gives (λ+s)^tv=0. These recomputations reproduce (3.15)–(3.16).

For off-diagonal entries, reciprocity gives Kij+Kji=si sj, and the diagonal of both sides of (3.9) is zero. Also K1=0 by definition. The assumptions on l give s^t1=1 and λ^t1=0, whence K^t1=0 and N=K^t+ss^t. Left multiplication by 1^t proves ker N=ker K^t∩s⊥. The two-dimensional ker K^t contains 1, on which s is nonzero. Its intersection with s⊥ is a complementary line. Since λ∉im K, λ is nonzero on ker K^t; since it vanishes on 1, it is nonzero on that line. Thus v=0, then δ=0 and u∈⟨1,1B⟩. This bounds the sign kernel by four and the full Selmer group by eight.

The class γ=(β,1) actually lies in each local image: identity at 2 and infinity, τ1 at 3, the indicated torsion class at the support primes because K1B=0, and an unramified class elsewhere. It is distinct from the four torsion classes since B is nonempty, l has an additional prime, and the other two classes have negative second coordinate. Hence the upper bound is attained and the dimension is exactly 3. No sufficiency assertion about the incomplete 2-adic conditions has slipped into the argument.

## Lemma 3.4 — HOLDS conditional on the quoted [48] (lines 960–994; (3.18))

The finite-level Selmer sequence gives 3=(r+2)+dim Sha[2], hence (3.18). For the full 2-primary sequence, write Sha[2∞]≅(Q2/Z2)^t⊕F. Its 2-torsion has dimension t+dim F[2], so t≤dim Sha[2]. Therefore r+t≤1 **before** any finiteness assumption. This is precisely the full-Selmer-corank condition the paper says [48, Theorem 1.1] requires, and E has rational nonzero two-torsion.

I do not have an independently checked statement or proof of the 2026 preprint [48]. The assertion “corank 0 or 1, together with rational two-torsion, implies finite Sha” is being checked here as a quoted external input, not from memory of an established theorem. No inference inside this lemma repairs or proves that input. If [48] has further hypotheses, they must be checked against an actual copy; its title alone cannot establish that there are none.

Conditional on this input, the rest holds. The Cassels–Tate pairing for an elliptic curve is alternating because the principal polarization is represented by the rational divisor (O); it is nondegenerate after quotienting by the maximal divisible subgroup, and is perfect when Sha is finite. These forms of Cassels [6] and Poonen–Stoll [55] are checked from memory. A finite 2-group with a perfect alternating pairing is a direct sum of pairs (Z/2^a)^2: pair an element of maximal order with one giving a pairing of that order and split off the nondegenerate summand. Thus dim Sha[2] is even. Equation (3.18) forces Sha[2]=0 and r=1. Surjectivity in the Kummer sequence realizes γ as a rational point, which is not any root or O. Multiplication of its two Kummer coordinates gives the nonzero x-class β.

Remark 3.5 makes the alternative dependence on [50] explicit. I have not independently verified that 2026 preprint either. Replacing one unchecked companion theorem by another does not remove the external dependency.

## Lemma 3.6 — HOLDS (lines 998–1093; (3.19)–(3.23))

Restore (3.19) as the four sums ΣB s=ΣJ s=0, ΣB λ=1, ΣJ λ=0. They follow from β,θ being 2-adic squares and from their prescribed 3-adic classes, using [q/3]=λq+sq. The two sets of cross-row sums in (3.20) are zero by (3.5); individual cross entries need not be zero.

An auxiliary q0≡7 modulo 12 has (s,λ)=(1,1), and each auxiliary in I, of size |B|-1, can have type (0,0) by being 1 modulo 12. Both supports then have total s=1, λ=0, giving exactly the two residue conditions on l.

For a=e(q0)+e(b*), a^t1=0 and a^t1B=1. Subject to K1B=0, K#=K+λa^t kills 1 on both sides and sends 1B to λ. The projection T=Id-1B a^t has image a⊥, kernel ⟨1B⟩, and fixes 1. Direct multiplication gives K#T=K. If ker K#=⟨1⟩, this proves ker K=⟨1,1B⟩. Were Kx=λ, y=Tx would satisfy a^ty=0 and y-1B∈⟨1⟩, contradicting a^t1B=1. Deleting the q0 row and column and proving the resulting matrix invertible is sufficient for ker K#=⟨1⟩, because one can subtract x(q0)·1 from any kernel vector.

Choose the B×I matrix C with basis columns for the even-sum hyperplane. The prescribed B–I and B–q0 symbols make K1B=0 at B by cancellation, at I by the zero column sums, at q0 by those sums together with ΣB s=0, and at J by (3.20). The deleted matrix on Q0 has block form [[A,C],[C^t,0]]. From K#1B=λ one gets A1B=λB, so 1B^t A1B=1. If C^tx=0 then x=c1B; multiplying Ax+Cy=0 by 1B^t yields c=0, then y=0. This proves nonsingularity without requiring A symmetric or |B| odd. For |B|=1 the matrix is (1).

Adding J leaves M0 unchanged because the B–J row sums vanish and I–J symbols are zero. Each free q0–J bit toggles exactly its surviving J diagonal entry. The determinant is multilinear in these bits, with full-product coefficient det M0=1. A nonzero multilinear polynomial represents a nonzero Boolean function, so at least one assignment gives determinant 1. This also covers J empty.

Finally, CRT and Dirichlet's theorem on primes in a reduced residue class (checked from memory) realize the symbols sequentially: specify type modulo 12 and a nonzero square/nonsquare residue at each already chosen prime. Reciprocity supplies the reverse symbols. These congruences are compatible, reduced, and exclude only finitely many primes. The product n is squarefree and prime to 6θ. The construction contains q0 even when |B|=1.

## Completion of Proposition 2.8 — HOLDS conditional on [48] (lines 1094–1100)

For b=0 the disjunct applies. For nonzero integral b, Lemma 3.2 supplies β,θ; Lemma 3.6 supplies one n for both n and nθ; Lemma 3.4 realizes the required class on both curves; (3.6) transports the second point to E(nH'). All nonzero conditions follow from H'>0 and n>0. Lemma 3.1 gives the pole restriction for the same fixed lists. The sole unverified research input in this chain is the quoted 2-converse, rather than the matrix computation.

## Unnumbered geometric proposition, §4.1 — HOLDS (lines 1126–1205; (4.1))

This is a load-bearing proposition although not given a lemma number. There is an indefinite quaternion division algebra with discriminant 210 because exactly four finite primes ramify and the real place does not. The standard quaternionic Shimura datum has reflex field Q. The canonical-model and functoriality facts invoked from Deligne [16,17] are checked from memory: they apply to this Shimura datum and its compact-open levels, and define level maps and finite-adelic right actions over the reflex field. The full Shimura variety must indeed be used when subsequently changing levels.

For maximal level, the norm quotient is trivial: finite idelic valuations can be matched by a positive rational number; reduced norms from B(Q) have no real sign restriction; the remaining norm-one finite adele is handled by strong approximation, since B^1 is split at the omitted real place. At each finite prime the norm of maximal-order units is Zp×. These are the hypotheses of the norm theorem and strong approximation, checked from memory. A negative-norm rational element joins the half planes. Thus X(C) has one component and its effective group is O^1/{±1}.

The only possible noncentral elliptic norm-one units have integral trace 0 or ±1, giving Q(i) or Q(√-3). These fields split at 5 or 7 respectively, which prevents embedding in B. There are no cusps because B is division. The Eichler area formula, as remembered from Voight [68], gives

\[
\frac{\mathrm{area}}{2\pi}=\frac{(2-1)(3-1)(5-1)(7-1)}6=8,
\quad 2g(X)-2=8,\quad g(X)=5.
\]

This checks the normalization against Gauss–Bonnet independently. I have not compared the stated theorem number 39.1.2 with a copy of the book.

The local normalizer quotient has one C2 factor at each division prime and no extra factors at split primes after removing scalars and units. Finite idelic scalars act trivially over Q because Af×=Q× Zhat×. The generic stabilizer argument proves faithfulness, so |W|=16. In characteristic zero a point stabilizer acts faithfully on its tangent line, hence is cyclic. Since W has exponent two, every nontrivial stabilizer has order two. Therefore each branch fiber contains 16/2=8 ramified points and contributes 8 to the ramification divisor. Recomputing Riemann–Hurwitz gives

\[
8=16(2g(X^*)-2)+8r,
\qquad 2g(X^*)-2+r/2=1/2,
\qquad r=5-4g(X^*).
\]

This restores the broken fractions in (4.1).

For m=30,42,70 the only odd ramified prime not dividing m is 7,5,3, and -m has residues 5,3,2 respectively, all nonsquares. The five quadratic-field discriminants are -120,-168,-280,-420,-840. In particular 2 ramifies for m=105 as required. Every prime ramified in B is nonsplit in each chosen quadratic field. The Albert–Brauer–Hasse–Noether quadratic embedding criterion (checked from memory, as cited in [68]) therefore applies; there is no missing real obstruction since B is split over R.

The integral element √-m is in a maximal order locally: use a stable lattice at split primes and the unique maximal order at division primes. The global order obtained by intersecting local orders is maximal. The conjugacy of maximal orders over Q in this indefinite case is the Eichler/strong-approximation fact cited from Voight [68, 28.2.10–11], checked from memory: the relevant rational ideal-class quotient is trivial. It places a conjugate of the element in the fixed O. At primes outside 210 its norm is a unit, so it is an order unit; at division primes it normalizes the unique maximal order. Its positive norm m and trace zero make it elliptic in the real projective action, with the asserted norm-parity Atkin–Lehner label.

The five distinct labels give distinct branch values because stabilizers are constant along a W-orbit. Hence r≥5; the formula forces r=5 and g(X*)=0. Each label has a unique branch value. Since each involution is Q-defined, that value is Galois-fixed and rational. A genus-zero Q-curve with a rational point is P1. Thus there are five individually rational points C, with one sent to infinity. The tabulations [35,47] are corroboration, not necessary premises of this independent calculation; their particular entries were not checked against copies.

## Unnumbered geometric proposition, §4.2 — HOLDS (lines 1207–1272)

On V=B, right multiplication by the standard conjugate gives a genuine representation, since both quaternion conjugation and composition of right multiplications reverse products. The trace identity gives

\[
\psi(x\bar g,y\bar g)=\operatorname{Nrd}(g)\psi(x,y).
\]

For pure nonzero Δ with Δ²<0, ψ(x,y)=Trd(Δxȳ) is alternating and nondegenerate. Such Δ exists because the negative-square locus is a nonempty real open set in the rational trace-zero space. With J=[[0,-1],[1,0]], the matrix identity J·adj(x)=x^tJ gives

\[
\psi(x,x\bar J)=\mathrm{tr}(J\Delta xx^t).
\]

For trace-zero Δ, JΔ is symmetric and has determinant det Δ=-Δ²>0, so is definite. Choosing Δ's sign selects the required positive polarization on one half plane. The similitude relation supplies the appropriate other component. This verifies the polarizability and weight conditions for the morphism into the Siegel datum, rather than merely assuming that a quaternion action furnishes a principal polarization on an arbitrary O-lattice.

A rational symplectic basis does give a self-dual lattice. The intersection of O-hat× with the inverse image of a sufficiently small integral principal Siegel level is compact open and of finite index. Level at least 3 is fine for principally polarized abelian varieties, so the universal scheme pulls back to a principally polarized abelian surface scheme over Y. These moduli and Shimura-functoriality results of [16,17] are checked from memory; the necessary compatible levels and fine level are supplied. The whole O need not preserve the chosen lattice; only rational B-endomorphisms are subsequently used.

Because X has no elliptic stabilizers, the level map Y→X is unramified. Consequently Y→P1 has index exactly two above C and one elsewhere. Its finitely many components are smooth and projective. Left B commutes with all the right complex structures, and gives rational Hodge endomorphisms. The Hodge description of abelian varieties up to isogeny, and invariance of geometric Hom under extension of algebraically closed characteristic-zero fields, are the standard results cited from Mumford [45], checked from memory. They give B⊂End^0(Ay) over Qbar.

Changing the finite-adelic coordinate preserves the rational Hodge structure up to isomorphism; domain coordinates above a common quotient point differ by G(Q). This proves that all fibers above a common base point are geometrically isogenous, including CM fibers. No compatibility claim beyond this is needed until the explicit intertwining argument in §4.6. Guitart–Molina [29] is a comparison, rather than an input requiring a non-CM hypothesis here.

Finally the map to polarized moduli is nonconstant on each component: the half-plane gives uncountably many complex structures on V, whereas the presentations of a fixed rational Hodge structure on V form a countable orbit under GL(V)(Q). A constant polarized moduli map would give a single rational Hodge isomorphism class and contradict this. This is enough; generic injectivity of the moduli map is not required.

## Lemma 4.1 — HOLDS (lines 1273–1317)

After excluding finitely many primes, proper smooth models, the finite map, the disjoint branch sections, their reduced étale inverse images, and the abelian scheme all spread as claimed. Smoothness, finite étaleness, and the fixed divisor multiplicities persist after removing finitely many bad primes. These standard spreading-out facts are checked from memory; all objects and exclusions are chosen before s.

The splitting field of the finite étale generic fiber has degree at most (deg π)!, since its Galois action faithfully permutes at most deg π points. At a prime q outside S, contact is the valuation of the primitive linear form after normalizing min(vq(u),vq(v)) to zero, exactly the expression in the lemma. Different branch sections cannot both be met there.

In a formal branch neighborhood the divisor identity gives t=z²e(z) for a unit e. An unramified extension defines the special branch points and a square root of the residue of e. Since q≠2, Hensel's lemma gives a square root in the formal power-series ring. **Restore the lost radical at line 1300:** the new coordinate is z·√e(z), not z·e(z). This is the same radical-loss extraction artifact as elsewhere in the file, not a mathematical gap. Then t=z². If vq(t(s)) is even, √t(s) is defined over an unramified extension after extracting the unit's square root. Both lifts at every branch point are unramified, and properness accounts for every point in the fiber. Thus the splitting field is unramified outside S and the odd-contact primes.

Every lifted point extends to the local integer ring by properness of Y, including when that ring is ramified over Zq. Pullback of the spread abelian scheme gives good reduction outside **S**, a stronger statement than outside T. The Darmon–Granville/Beckmann specialization result [11, Proposition 3.2] is contextual: I have not checked its exact quoted formulation from a copy, and the present proof derives the needed index-two case without it.

## Lemma 4.2 — HOLDS (lines 1318–1429; (4.2)–(4.4))

Here and throughout the geometric quantifier is y∈Y(Qbar), with the overbar lost in extraction. The proof does not impose a bound on the degree of y.

At a fixed even level r, a symmetric representative M of the principal polarization and its finite theta data are defined over a finite extension of the generic function field and spread on a dense open in a fixed covering curve. A principal polarization has h0(M)=1. The theorem of the square for symmetric line bundles gives [r]*M≅M^(r²); Riemann–Roch on an abelian surface gives h0(M^(r²))=(r²)^2=r^4. The r^4 pairs (a,b)∈((r^-1 Z²)/Z²)^2 in (4.3) therefore have the right count. The level at least 2 makes M^(r²) basepoint-free. The standard theta-group and theta-height construction is cited from Pazuki [51, §2.3]; these facts and the construction are checked from memory, not against a local copy.

The coordinate comparisons deserve checking because arbitrary independent coordinate scalings would not give a uniform height bound. With k=r², the good-choice relation gx gy=ζxy g(x+y), ζxy∈μk, implies g0∈μk and gx^k∈μk; hence gx^(k²)=1. Normalizing ux=cx gx to satisfy ux^(2k)=1 gives cx^(k²)=1 since 2k divides k². Thus this normalization changes coordinates only by bounded-order roots of unity, not by arbitrary functions of the fiber.

For t=(m+τl)/k, the analytic translation operator on a section is multiplication by exp(πi l^tτl/k+2πi l^tz) followed by z↦z+t. Applying it k times and using theta automorphy gives the scalar exp(πi(k-1)l^tm), which is ±1. Its order divides 2k, as asserted. Acting on θ[a,b](τ,rz) shifts the characteristic by (l/r,m/r) with root-of-unity factors of bounded order. Two such lifts differ by a scalar in μ(2k). Symmetric representatives differ by a 2-torsion line bundle, and r even accommodates the resulting characteristic shifts.

To check the Fourier step explicitly, write a=j/r and group rn+j modulo k=r². The index e∈(Z/kZ)² satisfies e≡j modulo r. The b-index contributes the finite Fourier factors exp(2πi e^tb/r); as b runs through (r^-1 Z²)/Z² these give an invertible Fourier block of size r². Hence the characteristic coordinates and the θ[e/k,0](kτ,0) coordinates differ by fixed invertible matrices at that level. Roots of unity, permutations, and a common scalar preserve projective height; a fixed invertible matrix changes it by O(1). The ℓ2 projective height differs from the maximum-coordinate height by at most (1/2)log(r^4) at the archimedean places, after normalization. All constants are independent of the residue-field degree.

For nonconstancy, suppose all sufficiently divisible even-level characteristic vectors were projectively constant on a marked disk. Choose rational b0 with θ[0,b0] nonzero; existence follows because its Fourier series as a function of real b has constant coefficient 1. For every rational b, a common level makes θ[0,b]/θ[0,b0] constant. Continuity in b and absolute convergence imply proportional theta functions of real b for τ and τ0. Their constant Fourier coefficients are both 1, so they are equal. The coefficients exp(πi n^tτn) are therefore fixed. Continuity removes the discrete ambiguity in their logarithms, and taking n=e1,e2,e1+e2 fixes every entry of τ. This contradicts varying periods. Thus one finite even level is nonconstant; any multiple retains the old coordinates, and a common multiple works for all finitely many components.

Finite coordinate ambiguities cannot destroy nonconstancy on a connected disk: a holomorphic vector confined to a finite set is constant. The resulting algebraic maps extend to the complete smooth covering curves. Their pullbacks of O(1) have positive degree and are ample. For a sufficiently large integer C, C times this line bundle minus the pullback of O(P1)(1) also has positive degree. The height machine and a lower bound for an ample height on a projective curve then give (4.4). These are the standard height facts in Bombieri–Gubler [3], checked from memory, with projectivity and positivity of degrees both verified. The omitted geometric points form a fixed finite set and can be absorbed into the constant.

The normalization conversion is hF^D=hF+(g/2)log π, hence a difference log π for g=2. This is the original-to-Deligne conversion cited in [51, §2.2] and [24, §2.3], checked from memory. For the clipped heights HΘ=max(hΘ,1), HD=max(hF^D,1), the quoted Pazuki comparison has the form

\[
|H_\Theta-\tfrac12 H_D|\le C_2\log(\min(H_\Theta,H_D)+2).
\]

From this displayed bound, HΘ≤(1/2)HD+C2 log(HD+2)≤(1/2+2C2)HD since HD≥1. Also HD≤max(hF,1)+log π. Thus the claimed linear upper bound for hΘ and then (4.2) follow. My check of Pazuki's comparison is from memory of the fixed-dimension, fixed-level theta/Faltings comparison; I have not independently checked the precise clipping/minimum formulation or the numbering of Corollary 1.3(2). The conclusion also follows from the compact-image argument below using Theorem 1.1, so it does not depend on that precise formulation.

## Remark 4.3, alternative height estimate — HOLDS (lines 1430–1443)

The period-corrected theta/Faltings comparison in Pazuki [51, Theorem 1.1], checked from memory, differs by the average of (1/4)log det Im τ, up to bounded error at fixed dimension and level. This is the required form; the coefficient and sign are immaterial once that term is uniformly bounded. The image of the projective Y in the open moduli space is compact, so the shortest nonzero polarization-metric period length is bounded below by δ>0. On the Z² sublattice the metric matrix is (Im τ)^-1. Minkowski's first theorem gives δ²≤C(det Im τ)^(-1/2), hence det Im τ≤Cδ^-4. Siegel reduction supplies a positive lower bound. The same compact image contains all conjugates. The period term is bounded at every embedding and in its normalized average. Thus hΘ=(1/2)hF^D+O(1) on this family, which is stronger than the upper bound needed. This supplies an alternative to the precise clipped-height quotation above, once the same nonconstant theta map has been constructed.

## Lemma 4.4 — HOLDS (lines 1444–1470)

Let d0=[K0:Q], already uniformly bounded. There are at most d0 conjugates of A. Each geometric Hom group between two surfaces is a torsion-free finitely generated abelian group of rank at most 4·4=16, by its faithful action on integral homology. Thus the direct sum H has rank at most 16d0². Its GK0-action has finite image because finitely many generators of all summands are defined over one finite extension. A finite subgroup of GLr(Z) injects into GLr(F3): the principal congruence subgroup of level 3 is torsion-free. This gives an explicit bound |GLr(F3)| if desired. These familiar lattice facts are checked from memory and use the bounded rank, rather than an unproved bound on degrees of individual isogenies.

The kernel inside GK0 is normal in GQ, since K0/Q is Galois and H carries the transport action of GQ permuting the summands. Its fixed field L is therefore Galois over Q and of bounded degree. At q outside T, K0/Q is unramified and every conjugate has good reduction. Inertia acts trivially on its prime-to-q Tate module by the good-reduction direction of Néron–Ogg–Shafarevich (checked from memory). The natural injection Hom→Hom of Tate modules is equivariant and faithful, so inertia acts trivially on H. Thus L has no additional ramification there. Rational B-endomorphisms are defined over L too: clear a denominator to reduce to the integral Hom groups. Good reduction outside S persists on extending K0 to L.

## Unnumbered descent proposition, §4.6 — HOLDS (lines 1472–1556; (4.5)–(4.8))

The rational homology is the regular left B-module. Its left-B centralizer is right B; commuting also with the real complex structure cuts this down to a real copy of C. The rational algebra CB in that copy is either Q or an imaginary quadratic field k: a nonscalar element generates a quadratic field with nonreal conjugate embeddings, and its real centralizer has dimension two. A finite-dimensional algebra containing the B matrix units after a splitting extension is a matrix algebra over their centralizer. Consequently End^0(A)=B when CB=Q and End^0(A)=B⊗k≅M2(k) when CB=k. The latter is split because k embeds as a maximal subfield of B. This checks the double-centralizer claim without assuming ahead of time that End^0(A) is division. In the first case it is division, so A is absolutely simple.

In the CM case, the matrix idempotents are defined over L. Clearing a denominator and taking the image produces an elliptic subvariety E/L; the matrix units give A∼L E². The center k acts on E, so it has CM. Since E is L-defined, [Q(j(E)):Q]≤[L:Q]. The CM theorem identifies the degree of a singular modulus with the class number of its imaginary quadratic order, and Siegel's class-number growth together with the order-conductor formula implies finitely many such orders of bounded class number. These are the precise CM facts cited from Cox [10] and Siegel [65], checked from memory. They apply to nonmaximal orders as well; restricting to fields alone would not have sufficed. The resulting finiteness is ineffective, which is acceptable for this stated existence of constants. There are finitely many geometric CM elliptic isomorphism classes of the bounded degree, so their stable heights, and hF(E²), are uniformly bounded.

Restore the quantitative isogeny bound (4.5) as

\[
\kappa(C_1)=\left((14g)^{64g^2}d
\max\{h_F(C_1),\log d,1\}^{2}\right)^{1024g^3}.
\]

This is the standard explicit Gaudron–Rémond isogeny bound cited from [23, Theorem 1.4], checked from memory of its formula. Its relevant use here is over the common field itself: both varieties are defined and isogenous over a number field of degree d. No semistability or principal polarization is needed for that form. I have not verified the paper's extra general phrasing about arbitrary extensions K/k0 against a copy; all actual applications set K=k0 and need only the usual same-field bound. The source-height dependence is crucial and has been used in the correct direction. Apply it to E², whose height and field degree are bounded, not to A of initially unknown height.

For an isogeny φ:C1→C2, the standard Faltings inequality

\[
h_F(C_2)\le h_F(C_1)+\tfrac12\log\deg\phi
\]

and additivity of stable height are the results cited from Faltings [20], checked from memory; they hold after an extension to semistable reduction and hence for stable heights without a semistability assumption on the original field. They give the uniform bound for hF(A) in the CM case, and then Lemma 4.2 proves the target height bound for these fibers since M≥1.

In the non-CM case, for each g∈Γ=Gal(L/Q) start with an L-defined conjugacy isogeny. Transport of gB gives a Q-algebra automorphism of B=End^0(A); Skolem–Noether makes it inner. Composing with the appropriate element of B× gives µg intertwining the two B-actions, as in (4.7). The quotient of µg·gµh by µgh centralizes B, so is c(g,h)∈Q×. A scalar c on a surface has degree c^4. Multiplicativity of degree, including rational quasi-isogenies, gives

\[
|c(g,h)|^4=\frac{\deg\mu_g\deg\mu_h}{\deg\mu_{gh}}.
\]

Put ag=(deg µg)^(-1/4), with the positive real fourth root, and let the **normalized** map be agµg. Galois acts on the Hom factor and trivially on these coefficient scalars. Its composition discrepancy is

\[
\frac{a_ga_h}{a_{gh}}c(g,h)=c(g,h)/|c(g,h)|\in\{\pm1\}.
\]

Thus (4.8) is a normalized sign-valued 2-cocycle by associativity. The extraction uses indistinguishable µ symbols for normalized and unnormalized maps; keeping them distinct restores the argument. No bound on the individual degrees is required. Ribet [59, §6], Pyle [56], and Quer [57] are background on building-block cocycles; the construction here explicitly proves the needed cocycle assertion and does not depend on importing their compatibility conclusions without hypotheses. I have not checked those exact passages against copies.

## Lemma 4.5 — HOLDS (lines 1557–1608; (4.9))

The isomorphism H²(GQ,μ2)=Br(Q)[2] is the Kummer exact sequence with the natural action on μ2, which is trivial. This does not require incorrectly identifying the trivial and natural actions on Qbar×. In the square-root obstruction sequence for **characters**, the coefficient action on the scalars is trivial, as the paper says. Outside T the sign cocycle factors through the unramified quotient Zhat (the hat is lost in the extraction), whose torsion cohomological dimension is one. Its local class is zero there.

The local criterion for a finite character to have a continuous character square root can be rederived directly. For odd p, Qp×≅p^Z×μ(p-1)×Zp. On the valuation factor choose any square root of the uniformizer value. On the Zp factor a continuous square root exists (also on Z2 when p=2). On a finite cyclic group of even order, a character is a square precisely when its value on the unique element of order two is 1. At p=2 use Q2×≅2^Z×{±1}×Z2, with the same criterion on -1. At R the Galois group is C2 and the criterion is identical. Thus the only local obstruction is χv(-1). The local reciprocity and Brauer local-global statements cited from Serre [64] and Milne [42,41] are checked from memory; their needed forms are local reciprocity for finite characters and injectivity of Br(Q) into the sum of local Brauer groups, with sum of invariants zero.

At every odd finite place with nonzero sign obstruction choose a character modulo q that is odd, e.g. a faithful character of the cyclic group Fq×. At 2 use the odd character modulo 4 if necessary. Their product is a global Dirichlet character χ unramified outside T. Its local obstruction matches at all finite places. Reciprocity of Brauer invariants forces the matching real obstruction too. The local-global injection therefore proves ∂χ=[ε]. Its order m divides the least common multiple of the factor orders, and in particular

\[
m\le 2\prod_{q\in T,\ q\ne2}(q-1)\le C\prod_{q\mid M}q=CM.
\]

The fixed primes of S contribute only a constant. The conductor divides the squarefree product of the participating odd primes, times 4. Thus χ is tame at odd primes and has uniformly bounded conductor at every fixed prime.

A pointwise square root of the finite character χ can be chosen continuously with values in μ(2m). Equality of obstruction classes means its coboundary differs from ε by the coboundary of a continuous sign cochain; multiplication by that cochain gives β²=χ and δβ=ε exactly. On GL the inflated cocycle is identically 1, so β is a character. Comparing β(gu) and β((gug^-1)g), using the two mixed cocycle values equal to 1, proves conjugacy invariance for u∈GL.

At an odd prime outside T, β on inertia is a quadratic character, because inertia fixes L and β²=χ is unramified. Continuity into a finite set implies that β factors through a finite quotient as a function, so only finitely many such inertial characters are nontrivial. Wild inertia is pro-odd, and tame inertia has exactly one nontrivial quadratic character. The quadratic character of Q(√dβ), with dβ the product of those offending odd primes, has exactly those inertial restrictions and can introduce ramification only also at 2∈S. Multiplication cancels them without changing the square, coboundary, or root-of-unity value group. This proves the asserted triviality on all inertia outside T, and preserves conjugacy invariance on GL. No uncontrolled field extension has been silently used to obtain the splitting.

## Unnumbered modularity proposition, §4.7 — HOLDS conditional on the quoted [49] (lines 1609–1679; (4.10)–(4.12))

Fix embeddings of Qbar into Qbarℓ for ℓ=2,3. Formula (4.10) uses the **normalized** µg, so

\[
R_\ell(g)R_\ell(h)=\beta(g)\beta(h)\epsilon(g,h)\,
\widetilde\mu_{gh}\circ gh
=\beta(gh)\widetilde\mu_{gh}\circ gh.
\]

The two discrepancies cancel because ε²=1. Continuity follows from the finite cocycle data and the continuous Tate action on an open subgroup. There are only finitely many normalization scalars; after choosing embeddings they lie in one finite coefficient extension, as does a splitting of B. Intertwining (4.7) makes Rℓ commute with B. Over the split coefficient field a module for M2 decomposes as its two-dimensional defining module tensor a multiplicity space, so the four-dimensional Rℓ is two copies of a two-dimensional rℓ. This proves (4.11), including the multiplicity.

The kernel of β|GL is normal in GQ by Lemma 4.5. Its index in GL is at most 2m, hence L'/Q is Galois, contains L, and

\[
[L':Q]\le2m[L:Q]\le CM.
\]

On GL' the scalar and normalized map are both 1, so Rℓ is exactly Vℓ(A). The bounded degree used later in local estimates is that of L, not this growing degree.

Faltings' semisimplicity and endomorphism theorems [20], checked from memory, require an abelian variety over a number field, which A/L' is. They give End(GL')(Vℓ(A))=B⊗Qℓ since all geometric endomorphisms are already defined over L. Semisimplicity persists on coefficient extension. Under Rℓ=rℓ⊕rℓ, its commutant is M2(End(rℓ)); equality with the split B forces End(rℓ)=the scalar field. A semisimple representation over the algebraic closure with scalar commutant is irreducible. Thus rℓ is absolutely irreducible even after restriction to GL', and therefore over GQ.

The smooth-proper de Rham comparison and Hodge–Tate decomposition invoked from Scholze [61, Corollary 1.8], with [62]'s corrected definitions, are checked from memory in their usual smooth-proper form. An abelian variety over a finite extension of Qℓ satisfies those hypotheses even with bad reduction. Its first cohomology has two weights of multiplicity two, and the covariant dual Tate module has cyclotomic exponents 0,1, each twice. De Rham descent under finite local extensions, cited from Fontaine [21, §3.9(ii)], is checked from memory and applies to the already defined Qℓ-representation Rℓ. Each rℓ has exponents 0,1 once each (weights 0,-1 in the convention of the text).

For a complex conjugation j, comparison with Betti homology is legitimate for the quasi-isogeny defined over Qbar and its algebraic coefficient scalars. The map j exchanges the two nonzero Hodge summands; the holomorphic quasi-isogeny preserves the types on source and target, so their composite still exchanges them. Multiplication by a scalar does not change that. Hence Rℓ(j), and thus rℓ(j), cannot be scalar. Since rℓ(j)²=1 in characteristic zero, its eigenvalues are 1 and -1. This proves oddness, including for ℓ=2. At primes outside T∪{ℓ}, inertia fixes L, acts trivially on the Tate module by good reduction, and is killed by β. Thus rℓ is unramified there.

These checks establish precisely the hypotheses **quoted here** for [49, Theorem 1.1]: a continuous irreducible odd two-dimensional 2-adic representation, finitely ramified, de Rham at 2 with distinct weights. I have no independently checked statement or proof of that 2026 companion preprint. In particular I cannot independently certify its asserted absence of a residual-image hypothesis. If it requires one, this paper has not supplied that additional verification. Assuming the quoted unrestricted statement is correct, its application is valid.

In the arithmetic-Frobenius normalization, a weight-k form has exponents {0,k-1}. A Tate shift t changes them to {t,t+k-1}. Matching {0,1} with k≥2 gives t=0, k=2. In a dual presentation the exponents are {n+1-k,n}, giving n=1, k=2. Algebraically Vf^∨≅Vf⊗ψf^-1⊗χcyc^(1-k), so

\[
V_f^\vee\otimes\chi_{\rm cyc}^{n}
\simeq V_{(f\otimes\psi_f^{-1})^{\rm new}}
\otimes\chi_{\rm cyc}^{n+1-k}.
\]

This restores the garbled exponent at line 1670. The determinant and exponent convention agree with the usual Deligne representation [15], checked from memory. Inverting Frobenius eigenvalues upon switching Frobenius conventions does not itself dualize the representation. The newform may have nebentypus and nonrational coefficients; neither is excluded or assumed away.

## Lemma 4.6 — HOLDS given that modular realization (lines 1680–1706)

At q outside T∪{2,3} and the level, A and its conjugates have good reduction, and the coefficient primes are distinct from q. Arithmetic Frobenius transports the geometric special fiber to its q-power twist and acts on prime-to-q torsion by the relative Frobenius Abar→Abar^(q). The reduction of the unnormalized quasi-isogeny µg returns it to Abar. After clearing its denominator and extending over good reduction, this composition is a rational endomorphism uq of the single special-fiber abelian surface.

The characteristic polynomial of an abelian-variety endomorphism on Vℓ has rational coefficients and is independent of ℓ≠q, also for rational endomorphisms after clearing denominators. This is the precise Milne [40, I.10] fact used, checked from memory. No field-degree bound is needed. Consequently

\[
\alpha_q=\tfrac12\beta(g)a_{\bar g}\operatorname{Tr}(u_q)\in\overline{\mathbf Q}
\]

has images equal to the trace of r2 and r3 at the chosen Frobenius. The factor 1/2 is forced by Rℓ=rℓ⊕rℓ; the fourth-root normalization factor ag is necessary, and has not been omitted. The extraction's final `Q` here is Qbar, not an assertion that αq is rational.

The isomorphism for r2 chooses one embedding of the Hecke field into Qbar; every embedding of a number field into Qbar2 has algebraic images and thus determines such an embedding under the fixed Qbar embedding. Injectivity then gives αq=aq(f) as algebraic numbers. The same numbers under the chosen 3-adic embedding are the traces of r3. The omitted primes are finite. Chebotarev density and the characteristic-zero character criterion identify the semisimplifications; r3 is irreducible by the preceding argument, and the modular representations are semisimple. These are the standard Chebotarev/Brauer–Nesbitt facts cited through [40], checked from memory; I have not verified the precise IV.3.3/3.9 numbering in those notes. Deligne [15] supplies the compatible system for the fixed algebraic newform, including the 3-adic member. Thus the same algebraic conjugate of f is obtained, not merely an unrelated form at 3. This is enough to use r3 to measure the conductor at 2.

## Lemma 4.7 — HOLDS given the modular realization (lines 1707–1770; (4.13))

The displaced label (4.13) belongs to N≤CM^a. For a primitive weight-two newform, the q-exponent in its primitive level equals the Artin/Weil–Deligne conductor exponent of its ℓ-adic representation for ℓ≠q. This is the conductor-preserving local–global compatibility result cited from Carayol [5], checked from memory in its standard characteristic-zero form. Its hypotheses here are a classical primitive cuspidal form, weight at least two, and q≠ℓ; they are satisfied. It includes the monodromy term, so merely bounding the semisimplified inertia action would not suffice. The exact theorem label and normalization passages in [5] were not independently inspected. Use r2 at q≠2 and the same form's r3 at q=2, supplied by Lemma 4.6. At q outside T the conductor is zero.

Choose a fixed threshold above S, 2,3 and the bound on [L:Q]. For a larger q∈T, wild inertia has trivial image in Gal(L/Q) since a finite q-group cannot have nontrivial order dividing [L:Q]<q. Over L, A has good reduction at q because q∉S. Thus wild inertia acts trivially on Vℓ(A). On this subgroup β is a character and β²=χ is tame, so β is sign-valued and trivial on the pro-q wild inertia. Consequently Rℓ and rℓ are tame. The conductor exponent is then the dimension minus the dimension of inertia invariants, at most 2.

For a fixed smaller q, the completions F=Lv lie among finitely many embedded extensions of Qq, since their degrees are bounded. This local-field finiteness result is standard and checked from memory: there are finitely many extensions of each fixed degree, and only finitely many embeddings of each into a fixed algebraic closure. It is essential that the degree is that of L, which is uniformly bounded.

On GF, β is a character. Local reciprocity identifies its square with χ∘Norm(F/Qq). The conductor of χ on Qq-units is bounded (at most 1 at an odd participating prime, at most 2 at 2); factors at other primes contribute only unramified characters. By continuity of the norm and the finite list of F, there is a uniform b such that this square character is trivial on UF^b and logarithm identifies UF^b with the additive ideal mF^b. Hence β(UF^b)⊂{±1}. For odd q, squaring is a bijection on UF^b, and β is trivial there. For q=2, logarithm turns squaring into multiplication by 2, giving

\[
(U_F^b)^2=U_F^{b+e_F},\qquad e_F=v_F(2).
\]

The character is therefore trivial on this uniformly deeper group. Arbitrarily large order on a uniformizer has no effect on these bounds. Quadratic corrections to β leave its square unchanged, so this reasoning controls them too. Local reciprocity translates the unit bound to a bounded upper ramification cut for β|GF.

For the Tate action choose p0=3 if q≠3 and p0=5 if q=3, and let F1=F(A[p0]). Then [F1:F]≤|GL4(Fp0)|. The full prime-to-q torsion is rational over F1, so the semistable reduction criterion applies. The cited Silverberg–Zarhin [66, Theorem 3.5] is checked from memory in the sufficient form “full n-torsion rational, n≥3 prime to the residue characteristic, implies semistable reduction.” That sufficient form also follows from the usual integral monodromy argument: a finite semisimple inertia action cannot survive in the torsion-free principal congruence subgroup of level p0. The full level condition used here is stronger than just a quadratic relation on inertia modulo a small n. The exact theorem number in [66] is not independently checked.

Over F1, inertia acts unipotently on the prime-to-q Tate module. A compact unipotent subgroup over Qℓ is pro-ℓ after choosing a lattice; its pro-q wild subgroup is trivial when ℓ≠q. Thus the Tate action kills wild inertia over F1. The degrees of F1 and of its normal closure over Qq are bounded, so these extensions again range over a finite set. Choose a uniform upper cut beyond their breaks and, using the finitely many Herbrand functions, beyond the cuts of β|GF. The subgroup and quotient rules for ramification filtrations in Serre [64], checked from memory, put every sufficiently deep G(Qq)^u simultaneously inside GF, inside the character kernel, and inside the wild Tate kernel over F1. There µg is µ1=1 and β=1, so Rℓ and rℓ are trivial.

If uq≥0 is such a uniform upper cut, Swan(rℓ)≤2uq by the conductor integral. The remaining tame-plus-monodromy term is at most 2, because the representation has dimension 2. Hence its full exponent is bounded by 2uq+2 at this fixed q. This proves a uniform bound even at 2 without using an invalid coefficient-prime-equals-residue-prime conductor comparison.

The finitely many small primes contribute a fixed constant. All other ramified primes divide M and have exponent at most 2. Therefore the proof actually gives

\[
N\le C M^2,
\]

so one may take a=2 in (4.13). No discriminant or degree of the potentially larger field L' enters this local estimate.

## Lemma 4.8 — HOLDS given the modular realization (lines 1771–1796)

The weight-two Eichler–Shimura construction places the representation of any normalized primitive weight-two newform of level N and nebentypus in the Tate module of J1(N), after extension of coefficients. This is the precise realization needed from Ribet [58] and Deligne [15], checked from memory. Using J1 rather than only J0 allows the nebentypus; rational Hecke coefficients are not required. I have not checked the exact position of the “following weight-two realization” after [58, Theorem 2.1].

Over H=GL', V2(A) becomes two copies of r2|H, while V2(J1(N)) contains one. Thus a nonzero intertwiner exists over Qbar2. To descend it, regard the intertwiner space as the solution to linear equations in the finite-dimensional Q2-space Hom(V,W). The intersection of the kernels of all equations h·f=f·h is already the intersection for a finite subset: keep an equation only when it decreases dimension. This finite linear system commutes with field extension, so its Q2 solution space is nonzero as well. There is no need to assume a bound on the Hecke field degree or to infer an abelian factor merely from a constituent over an algebraic closure.

Faltings' homomorphism theorem [20], checked from memory, now identifies this space with Hom(L')(A,J)⊗Q2 and yields a nonzero actual homomorphism. Absolute simplicity of A makes its kernel finite, so its image is an abelian subvariety isogenous to A. Poincaré complete reducibility over the base number field, as in [45], applies using a polarization defined over L' and gives J∼L' A×D0. The necessary Hom and complement are over L' itself. A possible division-algebra Schur index causes no gap: once the rational Hom exists, its full rational Tate injection supplies the forced multiplicity automatically. In particular g0=dim J≥2.

The Murty–Pasten [46] elliptic O(N log N) estimate and the strategies of von Känel [70] and Alpöge [1] are contextual comparisons, not numerical bounds used in this proof. I have not checked their precise theorem statements or section references from copies, and no step here requires them.

## Final height proposition and completion of Theorem 2.4 — HOLDS conditional on [49] (lines 1797–1853; (4.14)–(4.16))

For N≥3 the modular index is [SL2(Z):Γ1(N)]=N²∏(1-p^-2)≤N²; the effective PSL2 degree may further divide by 2. The few smaller N can be included by a fixed constant. Thus the j-map has degree at most CN². It is ramified only at 0,1728,∞, giving a Belyi map after dividing j by 1728. If d is its degree, Riemann–Hurwitz gives 2g0-2≤d (the three branch fibers contribute at most 3d), hence g0≤CN². The curve X1(N) is geometrically connected and smooth projective, and g0≥2 by Lemma 4.8, so the genus-at-least-one hypothesis is met.

Javanpeykar [32, Theorem 1.1.1] bounds the stable height of a curve's Jacobian by 13·10^6 g degB(X)^5. This theorem and its polynomial degree 5 are checked from memory, not against a source copy. Its application requires a smooth projective connected curve of positive genus over Qbar, not a bound on its field of definition. The explicit Belyi map supplies an upper bound for the minimal Belyi degree. Recomputing the exponent gives

\[
g_0\,\deg_B(X_1(N))^5\ll N^2(N^2)^5=N^{12}.
\]

Thus both bounds in (4.14) follow. The original versus Deligne height normalization differs by (g0/2)log π, only O(g0), so either convention still gives the same N^12 bound. I have checked the normalization conversion from memory; I have not independently compared [32, Lemma 2.4.4]'s convention against the paper's exact assertion. This possible source-normalization ambiguity cannot change (4.14).

Choose a polarization of D0 over L'; it gives an L'-isogeny with its dual. Zarhin's trick gives a principal polarization over L' on DZ=(D0×D0^∨)^4. This is the form cited from Zarhin [74, Theorem 1.1(ii) and Remark 1.4] and Bost [4], checked from memory: the fourth power of the product with the dual is needed, and no extension of L' is necessary. Since D0^8∼L' DZ,

\[
C_1=J^8\sim_{L'}C_2=A^8\times D_Z,
\quad \dim C_1=\dim C_2=8g_0.
\]

Indeed dim DZ=8(g0-2), and dim A^8=16. If D0=0 the omitted contribution is zero and the same dimension identity holds.

Write g=8g0, d=[L':Q]. Then d≤CM, g≤CM^(2a), and max(0,hF(C1))≤CM^(12a). Applying (4.5) to the **known-height source** C1 gives exactly

\[
\log\deg\phi\le1024g^3\left(64g^2\log(14g)+\log d
+2\log\max\{h_F(C_1),\log d,1\}\right).
\]

This restores the parentheses in (4.15). The dominant growth is O(M^(10a)(1+log M)); the other terms are O(M^(6a)(1+log M)). In particular log degree is bounded by a fixed power of M. It would be wrong to bound the degree itself by that fixed power, but the proof only needs its logarithm.

Additivity and the isogeny height inequality give

\[
8h_F(A)+h_F(D_Z)\le h_F(C_1)+\tfrac12\log\deg\phi.
\]

The lower bound quoted from Gaudron–Rémond [24, Corollary 8.4], attributed to Bost, is checked from memory in the stated Deligne normalization:

\[
h_F^D(D_Z)\ge-\tfrac12\dim(D_Z)\log(2\pi).
\]

The complement has a principal polarization, so it satisfies even a version stated only for principally polarized varieties. Subtracting (dim DZ/2)log π gives

\[
h_F(D_Z)\ge-\tfrac12\dim(D_Z)\log(2\pi^2).
\]

This verifies the sign and the extra π factor. Its negative contribution is only O(g), so it can be moved to the other side and absorbed in the polynomial bound. This proves (4.16); simply discarding hF(DZ) without this lower bound would not have been justified.

More explicitly, the proved a=2 gives

\[
g=O(M^4),\quad h_F(C_1)\le O(M^{24}),\quad
\log\deg\phi=O(M^{20}(1+\log M)).
\]

Since M≥1, the latter and the O(M^4) complement correction are O(M^24). Hence one admissible conclusion of these estimates is hF(A)≤CM^24, and Lemma 4.2 gives h(s)≤H M^24. This supplies an explicit admissible **exponent**, not an effective numerical value for H; the CM finiteness step was ineffective. The paper only requests existence of fixed H,c>0, so that is sufficient. Its CM case also fits this exponent after enlarging H. All geometric covers, levels, theta data, exceptional primes, and constants were chosen independently of s. Taking a larger positive integer exponent is valid because M≥1.

## Remark 4.9 — contextual citations not verified (lines 1854–1861)

The quoted von Känel [69, Proposition 9.9] and von Känel–Kret [71, Theorem 7.1] concern height bounds for abelian schemes in the specified GL2-type/CM classes over a number field, with constants depending on fixed dimension and field degree. I have not independently checked these exact formulations or their Q-virtual/product hypotheses from copies and do not claim a memory check of those precise theorem statements. They are not used to supply the height bound above: that bound was proved directly using the newform, modular Jacobian, and isogeny estimate. Thus the validity of the deductions in Sections 3–4 does not depend on the accuracy of this contextual comparison. If those remarks are to be retained for publication, their exact formulations should be checked against the cited versions.

## Coverage of displayed formulas and estimates

Every numbered display in the requested sections is accounted for below. “HOLDS” records the computation or deduction under the hypotheses identified in the detailed entry; the dependencies on [48] and [49] are not silently upgraded to independently verified theorems.

| Display | Classification | Check and location above |
|---|---|---|
| (3.1) | HOLDS | Separable cubic; discriminants 144l^6 and 2304l^6; Lemma 3.1. |
| (3.2) | HOLDS | Restored U formula and positive existential encoding; Lemma 3.1. |
| (3.3)–(3.4) | HOLDS | Finite local square-class lists and weak approximation; Lemma 3.2. |
| (3.5) | HOLDS | Both local square implications, including valuation cancellation; Lemma 3.2. |
| (3.6) | HOLDS | Direct substitution of (c²x,c³y); Lemma 3.2. |
| (3.7) | HOLDS | Standard full two-Selmer exact sequence, hypotheses checked from memory; Lemma 3.3. |
| (3.8) | HOLDS | Binary residue-matrix definitions and local unit quotients; Lemma 3.3. |
| (3.9)–(3.10) | HOLDS | Entrywise reciprocity and the total s-sum; Lemma 3.3. |
| (3.11) | HOLDS as hypothesis, and is achieved | Both-support construction; Lemma 3.6. |
| (3.12) | HOLDS | Root Kummer values 4l² and 12l²; Lemma 3.3. |
| (3.13) | HOLDS | Four-element local Kummer image at 3; Lemma 3.3. |
| (3.14) | HOLDS | Positive sign kernel, prime supports, and 3-adic restriction; Lemma 3.3. |
| (3.15)–(3.16) | HOLDS | Recomputed support-prime unit residue equations and reciprocity at 3; Lemma 3.3. |
| (3.17) | HOLDS | Multiply Nv=0 by 1^t, then use N=K^t+ss^t; Lemma 3.3. |
| (3.18) | HOLDS | 3=(r+2)+dim Sha[2], independent of [48]; Lemma 3.4. |
| (3.19)–(3.20) | HOLDS | Four total symbol sums and both cross-row sums; Lemma 3.6. |
| (3.21)–(3.22) | HOLDS | K#1B=λ, projection T, and K#T=K; Lemma 3.6. |
| (3.23) | HOLDS | Nonsingular block matrix, including even |B| and |B|=1; Lemma 3.6. |
| (4.1) | HOLDS | 8=16(2g*-2)+8r, so r=5-4g*; §4.1 proposition. |
| (4.2) | HOLDS | Theta-height comparison and field-independent ample-height inequality; Lemma 4.2. |
| (4.3) | HOLDS | Theta series and fixed Fourier blocks; Lemma 4.2. |
| (4.4) | HOLDS | Positive degrees on fixed projective covering curves; Lemma 4.2. |
| (4.5) | HOLDS in the used same-field form | Reconstructed explicit Gaudron–Rémond bound, checked from memory; §4.6 and final height proposition. |
| (4.6) | HOLDS | Stable isogeny height inequality, checked from memory; §4.6. |
| (4.7) | HOLDS | Inner automorphism correction by Skolem–Noether; §4.6. |
| (4.8) | HOLDS | Degree of a scalar on a surface is its fourth power; §4.6. |
| (4.9) | HOLDS | Brauer square-root obstruction, continuous cochain correction, inertia correction; Lemma 4.5. |
| (4.10)–(4.11) | HOLDS | Two sign discrepancies cancel; split quaternion matrix units give two equal copies; §4.7. |
| (4.12) | HOLDS | Character kernel index at most 2m; §4.7. |
| (4.13) | HOLDS given the form from [49] | Uniform conductor exponent ≤2 away from fixed primes; a=2; Lemma 4.7. |
| (4.14) | HOLDS given that modular realization | Index O(N²), genus O(N²), and N²·(N²)^5=N^12; final height proposition. |
| (4.15) | HOLDS | Logarithm of (4.5), with growth O(M^(10a)(1+log M)); final height proposition. |
| (4.16) | HOLDS conditional on [49] | Additivity, Bost lower bound, and a=2 give hF(A)≤CM^24; final height proposition. |

The unnumbered displays have also been checked in their respective entries: the pole valuations k,2k,3k; the 2-adic congruence; the local quotient order four; the full 2-primary Selmer-corank bound; the alternating-pairing parity; both deleted-matrix arguments; the norm/area computations; the symplectic and positivity identities; the relative Cartier divisor and contact order; the theta dimension, lift orders, Fourier coefficients, normalization and clipped-height estimates; the Hom-rank and field bounds; the CM class-number reduction; the fourth-root degree normalization; the Dirichlet-order estimate; the Frobenius trace; the unit-squaring and Swan estimates; the modular index/Belyi degree; the Zarhin dimensions and complement lower bounds. These displays introduce no additional unexamined arithmetic estimate.

The opening discussion at lines 725–733 cites Demeyer–Van Geel [18] and Cornelissen–Zahidi [9]. I did not verify the exact theorem/section formulations from copies or memory. They are historical comparisons, and neither their predicates nor any theorem from them enters the formula or its proof. Similarly, the background tables, comparison papers, and optional [50] mentioned above are distinguished from the actual load-bearing inputs.

## Reproducible exact computations

Run `python3 check_referee.py` in this folder. It uses no external packages, network access, or child processes. Its completed checks are:

- The two discriminants, the area and genus, the Riemann–Hurwitz branch contribution, all five quadratic discriminants, and the three nonsquare embedding residues.
- All eight combinations of l modulo 8 and odd u modulo 8 in the 2-adic congruence.
- The two-support residue matrices for β=17, θ=409, n=323, and for β=65, θ=601, n=16835. The respective enlarged parameters are 132107 and 10117835. Each support has kernel dimension 2 and λ outside its image; exhaustive enumeration of (δ,u,v) gives exactly four sign-normalized solutions of (3.15)–(3.16).
- 640 deterministic small abstract constructions, with |B|=1 through 4 and |J|=0 through 3, varying reciprocity types and fixed symbol blocks subject to the required row sums. Every construction has a nonsingular choice of J-diagonal toggles and both claimed kernel/image properties. These finite checks support, rather than replace, the general proof given above.
- The final exponent arithmetic and the unchanged input SHA-256.

The last run used one Python process, with measured peak resident memory 17,907,712 bytes (about 17.1 MiB), below the requested 1 GB. The sandbox rejected attempts to install process resource limits; the code's matrices and enumerations are explicitly bounded and the actual resident usage is reported. No long-running compute was started.

## Final verdict

I found **no internal GAP** in the deductions in Sections 3 and 4 after restoring the extraction artifacts. I found no definite authorial MISPRINT; the lost radical in the local coordinate, lost overbars and summation signs, garbled exponents, and displaced equation labels have been restored explicitly. They should not be presented as mathematical defects.

Section 3 proves exactly the two properties in Proposition 2.8 **assuming the pointwise 2-converse in the form quoted from [48]**. Its finite-level Selmer dimension computation, passage to full Selmer corank, Cassels–Tate parity, and simultaneous twist construction are consistent. Section 4 proves Theorem 2.4 **assuming the unrestricted 2-adic modularity statement quoted from [49]**, together with the classical results checked from memory above. Its ramification argument controls odd contact, the modular level is at most CM², and the final height estimates allow c=24.

This is a conditional positive verdict on these sections, not independent certification of the two 2026 companion theorems. Their full statements and proofs were neither supplied nor independently verified here. The remaining load-bearing source check is to read [48, Theorem 1.1] and [49, Theorem 1.1 and §2.1] and confirm both their validity and the asserted absence of additional hypotheses. Several exact classical citation numbers and normalization formulations were also checked only from memory, as individually recorded. Those limitations are not evidence of a gap, but they prevent an unconditional referee endorsement based solely on this audit. No conclusion about the correctness of the other sections or of the full undecidability proof is asserted.

Task: “Referee task: Sections 3 and 4 of paper_c.txt (a preprint on Hilbert's tenth problem over Q)” — 13 November 2026, approximately 20:20, Asia/Tbilisi.
