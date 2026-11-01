# Root analytic audit: union entropy and random maximal chains

Date: 2026-10-02 UTC. Status: **PASS** for the disjoint-union lemma and the nonmonotone layer theorem, including the strengthened projection and maximum-run bounds below. Independent internal review does not certify novelty or replace outside specialist review.

I read the full union and almost-symmetric candidates, their author review, the K union audit, the heat almost-symmetric audit, the shared checker, and the inherited entropy-comparison/adjacency derivations in the Hamming-band proof. The symmetric-function input is O'Donnell--Wright--Zhou (2011), Theorem 1, with constant 12.04; its primary manuscript has been inspected. Its part-symmetric theorem is also prior work and must not be conflated with arbitrary assignments on exceptional layers.

## Disjoint union

For nonempty S, fhat(S)=sum_j gjhat(S). With a=fhat², b_j=gjhat² and u=sum b_j, Cauchy--Schwarz gives a<=ru. If 0<u<=1, write a=tu: e(a)=t e(u)-ut log2(t)<=r sum e(b_j)+(log2(e)/e)u. If u>1, the global maximum e(a)<=log2(e)/e gives the same bound. Thus the inequality is valid even where the component squared masses sum to more than one. The empty atom contributes at most log2(e) Var(f); disjoint densities give Var(f)<=sum Var(g_j). No minority-density convention is needed.

Boundary additivity is exactly conditional on no joining edge between distinct components. More generally sum_j I_i(g_j)=I_i(f)+2Pr[the i-edge joins distinct nonzero components]. There is no lost factor from directed versus undirected sampling. Poincare then gives H(f)<=[rC+log2(e)(1+1/e)]I(f) from component FEI with constant C and no joining edges. For parallel intervals, strict gaps wider than 2w_max guarantee the hypothesis. Arbitrary narrow component widths are allowed; arbitrary gaps are not.

## Random-chain comparator and exact projection energy

For any Boolean f, a uniform maximal chain samples each layer uniformly and each interlayer edge uniformly. The symmetric comparator g takes f's chain label on each layer. Hence E g=P f, where P is orthogonal coordinate-permutation symmetrization, and E I(g)=I(f) by exact edge counting. Let L chi_S=|S| chi_S, so I(u)=<u,Lu>. P is self-adjoint, idempotent, and commutes with L. Therefore

E I(f-g)=I(f)+E I(g)-2<f,L E g>
=2[I(f)-I(Pf)].

Write D=I(f)-I(Pf)=I((1-P)f)>=0. This is an exact identity; g need not be a random permutation of f. Only its averaged layer values and averaged influence enter the proof.

## Disagreement and exceptional-layer geometry

Put delta=Pr(f!=g). Two independent chain comparators g,g' have average mutual disagreement equal to E delta, since both quantities at a layer equal 2q(1-q). Also E mean(g)=mean(f). With Q=Pr(g!=g'), the always-valid |mean(g)-mean(g')|<=2Q and Q²<=Q give

E Var(f-g)=4E delta-Var_chain(mean(g))>=2E delta.

Poincare and the exact energy identity imply E delta<=D, without monotonicity.

Let ell be the maximum length of a consecutive block of exceptional layers. Their total number may be unbounded. Since f-g is supported on those layers, the induced layer path is a disjoint union of blocks of length at most ell. The edge Cauchy--Schwarz bound gives <u,A u><=(n+1)cos(pi/(ell+1))||u||² for any u with that support. For n>=(ell+1)², 1-cos(pi/(ell+1))>=2/(ell+1)² implies

I(u)>=[n/(2(ell+1)²)]||u||².

Applying this to f-g, averaging, and using ||f-g||²=4delta and E I(f-g)=2D gives n E delta<=(ell+1)² D. For n<(ell+1)², the earlier E delta<=D gives the same bound. Thus for ell>=1,

H(f)<=24.08 I(f)+32(ell+1)²[I(f)-I(Pf)].

This follows from averaging the fully derived entropy perturbation inequality H(f)<=2H(g)+32n delta and symmetric FEI. It implies the stated count-k bound with constant 25+32(k+1)² because ell<=k. When ell=1, the induced cube adjacency is zero, so I(f-g)=n||f-g||²/2=2n delta exactly. The energy identity then gives n E delta=D, improving the last bound to H(f)<=24.08I(f)+32D<=57I(f), for arbitrarily many isolated exceptional layers. When no exceptional layer exists, f is symmetric and the original 12.04 bound applies directly.

## Weighted finite crossings

After sign changes and deletion of zero weights, a total normalized deviation A=sum |w_i/c-1| bounds the score's discrepancy from 2r-n by A at every cube point. A crossing can intersect at most floor(A)+1 eligible Hamming centers, including closed endpoints. For at most m crossings, k<=m(floor(A)+1). Therefore the sharpened theorem gives a constant depending only on m and A, without a crossing-spacing or output-bias hypothesis. This is a restricted finite-crossing theorem, not the arbitrary-weight three-crossing problem.

## Verification

The shared finite checker was read fully and rerun successfully: 3,200 disjoint unions, 616 Boolean functions, and 47,172 full maximal-chain permutations. Its coefficient and boundary identities are dyadic at the tested dimensions; entropy logarithms and comparison tolerances are numerical. The projection identity and all dimension-independent conclusions above have analytic proofs. Separate independent audits also pass. No claim about unrestricted Boolean FEI, input-biased measures, or research priority follows from these checks.
