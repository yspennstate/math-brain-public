# FEI: a corrected reduction and constant-preserving erasure obstructions

Date: 18 September 2026. Status: **proved coding implications and an exact counterexample to a false shortcut; full FEI remains unproved here**. No independent audit or first-priority claim is made.

All entropy in this note is measured in bits. For Boolean f on the n-cube, let p_S=fhat(S)^2, let X be the spectral subset with distribution p, and write

    H(f)=sum_S p_S log_2(1/p_S),
    I(f)=sum_S |S|p_S,
    B(f)=sum_i H(X_i | X_(-i)).

## 1. Erratum: global constants are not a pointwise inequality

The first section of the existing `proofnet24/P03-fei/solo-2026-09-17/FINAL_HANDOFF_2026-09-18.md` states

    H(f)<=B(f)+(2/ln 2)I(f).                                (FALSE)

The underlying `ERASURE_REDUCTION.md`, blob `770f1fc8438b360549ed89480cb260768d839923`, proves something different and valid. If **every** Boolean g satisfies B(g)<=K I(g), then **every** Boolean f satisfies H(f)<=(K+2/ln2)I(f). Thus, for global suprema,

    K_E := sup_f B(f)/I(f),
    C_FEI := sup_f H(f)/I(f),
    K_E<=C_FEI<=K_E+2/ln2.                                  (1.1)

The universal hypothesis must hold for the restrictions used in the induction. Replacing K_E by B(f)/I(f) of a single function is not justified. This note preserves the original reports and supplies a correction; it does not silently rewrite their history.

### Exact counterexample to the pointwise statement

Let g be the addressing function with eight selector bits and 256 data bits. Its spectrum has 2^16 nonzero coefficients, each of squared magnitude 2^(-16). A spectral set consists of one data coordinate and a uniformly selected subset of the eight selectors. Thus H(g)=16 and I(g)=5.

Introduce one more physical bit z and put

    F(u,z)=g(zu_1,...,zu_264).

Each spectral set S is replaced by (S,|S| mod 2). All sets in the new spectrum have even cardinality, so any one spectral bit is determined by all the others: B(F)=0. Entropy is unchanged. Half the selector subsets require an extra bit, giving

    H(F)=16,  I(F)=11/2,  B(F)=0.

The false inequality would say 16<=11/ln2. But the positive-series identity for arctanh gives

    ln2=2 sum_{j>=0} 1/[(2j+1)3^(2j+1)]>56/81>11/16.

Indeed 16*(56/81)-11=5/81>0. This is an exact 265-variable counterexample. It neither proves nor disproves FEI.

### A correct hereditary pointwise replacement

Let K_restr(f) be the maximum of B(g)/I(g) over all nonconstant coordinate restrictions g of f, including f itself. The existing restriction identity implies

    H(f)<=(K_restr(f)+2/ln2)I(f).                            (1.2)

To see this, write Delta_i(g)=H(g)-(H(g_+)+H(g_-))/2. The existing identity Delta_i=B_i+JS_i and bound sum_i JS_i<=(2/ln2)I(g) guarantee some relevant i with Delta_i<= (K_restr(f)+2/ln2)Inf_i(g). Apply induction to g_+,g_-, all of whose restrictions remain restrictions of f, and use

    I(g)=(I(g_+)+I(g_-))/2+Inf_i(g).

This is a safe specialization of the existing universal argument, not a new FEI estimate: K_restr(f) is not known to be uniformly bounded.

## 2. Systematic spectral coding

Let h be Boolean on N variables and let A be an r by N binary matrix. Its columns are A_i. Define

    F(x,z)=h(x_i chi_(A_i)(z): 1<=i<=N),

where z has r extra independent uniform sign coordinates. The Fourier expansion is exactly

    F(x,z)=sum_{S subset[N]} hhat(S) chi_S(x) chi_(AS)(z).

Consequently the injective map S -> (S,AS) transports all squared coefficients without changing their magnitudes. In particular,

    H(F)=H(h),
    I(F)=I(h)+E|AS_h|,  so  I(h)<=I(F)<=I(h)+r.            (2.1)

Here matrix multiplication is over F_2 and S_h is the spectral random set of h. This is a Boolean substitution, not an assertion that arbitrary nonnegative probability vectors are Boolean spectra.

If the systematic code C={(S,AS)} has minimum Hamming distance greater than k, then

    H(X_B | X_(B^c))=0  for every spectral block |B|<=k.     (2.2)

Indeed two codewords agreeing off B would have distance at most k. Thus the observed complement uniquely determines the entire codeword. The same reasoning applies to any subset of the code, including a Fourier support with zero coefficients.

## 3. Small-redundancy code existence, with all quantifiers

Choose A uniformly with independent fair entries. For a fixed nonzero S of weight j, AS is uniform on F_2^r. Therefore the probability of at least one nonzero codeword of weight at most k is at most

    2^(-r) sum_{j=1}^k binom(N,j) sum_{ell=0}^{k-j} binom(r,ell)
      <=2^(-r) sum_{h=1}^k binom(N+r,h)
      <=2^(-r) k (N+r)^k.                                 (3.1)

When k<=N, set r=3k ceil(log_2(2N)). If r<=N, (3.1) is at most k/(2N)^(2k)<1. A suitable matrix therefore exists. It can also be found by a finite exhaustive search: enumerate the binary matrices and test all nonzero messages of weight at most k; messages of greater weight cannot create a short systematic codeword.

For fixed k this requires r=O_k(log N). More generally, whenever

    k_N log N=o(N),

the same construction gives r_N=o(N) and minimum distance exceeding k_N for all sufficiently large N.

## 4. The full optimal FEI constant survives spectral erasure isolation

### Theorem 4.1

For every fixed integer k>=1, the supremum of H(f)/I(f) over nonconstant Boolean functions whose Fourier support has minimum Hamming distance greater than k equals the unrestricted optimal FEI constant C_FEI, in the extended real sense.

Thus the subclass in which *every* conditional spectral entropy of blocks of size at most k vanishes is already FEI-complete, with **no loss in the optimal constant**.

### Proof

Fix any nonconstant Boolean g on n variables. On m disjoint blocks take

    h_m=g tensor ... tensor g,  N=mn.

Product spectra give H(h_m)=mH(g) and I(h_m)=mI(g). Use Section 3 to embed its spectrum in a distance->k systematic code with r=O_k(log(mn)) extra bits. Equation (2.1) yields

    H(F_m)=mH(g),
    mI(g)<=I(F_m)<=mI(g)+r.

Since I(g)>0 and r/m->0,

    H(F_m)/I(F_m) -> H(g)/I(g).

Every F_m belongs to the restricted class. Its supremum is therefore at least the ratio of every g, and hence at least C_FEI. The reverse inequality follows from containment in the class of Boolean functions. The argument also applies when the supremum is infinite. QED.

For k=1, one parity bit already suffices: apply the parity lift to h_m. The additive cost of at most one in influence disappears after division by m. This sharpens the earlier repository's factor-two comparison from a single parity lift. For general k the systematic code extends the obstruction to blocks.

### Growing-block strengthening

The same tensor argument works with any chosen k_N=o(N/log N), because r_N=o(N). It produces Boolean functions preserving the original H/I ratio asymptotically while all conditional spectral entropies of blocks up to k_N vanish. For example k_N=floor(sqrt N) is allowed. N here is the number of coordinates *before* the redundant parity bits are added; the new dimension is N+r_N.

This is not a contradiction to (1.1). Physical coordinate restrictions of a coded function need not retain the code-support property. The quantifier over all descendants in a valid induction is essential.

## 5. What this rules out and what it leaves

A proof strategy that assumes a bounded collection of small spectral erasure entropies detects all difficult functions is insufficient. The obstruction survives tensor amplification and systematic coding at negligible relative influence cost. Even increasing the spectral block size slowly with dimension does not automatically repair it.

This does not rule out the existing global bound B<=K I as a route: proving it **for all Boolean functions**, including physical restrictions and uncoded functions, would still prove FEI. It also does not refute the repository's conditional interference-patching theorem. It says that a universal decomposition must genuinely simplify physical restrictions or control coherence; a pointwise claim about sparse spectral adjacency is not enough.

The active constructive target remains a hereditary bound or an interference-controlled decomposition whose local estimates do not merely restate FEI for an arbitrary leaf. No such universal bound is proved here.

## 6. Exact tests

`check_fei.py` uses Fraction arithmetic and a direct Walsh transform. It tests all 256 Boolean functions on three variables under each of three systematic embeddings, of minimum distances 2,3,4. It checks 768 function lifts, 53,248 Fourier coefficient identities, 88 complement-injectivity tests for full-code erasure blocks, and the exact influence identity (2.1). Entropy preservation is tested by equality of the multiset of nonzero squared Fourier coefficients, with no floating logarithms. Four rational/integer union-bound instances also pass.

The asymptotic construction and the equality of global constants follow from the written proof, not from those finite enumerations. The 265-variable addressing example is checked through its exact combinatorial spectrum, without constructing its exponential truth table.

## 7. Attribution

The original erasure/restriction and parity-lift arguments are in the cited repository notes. O'Donnell and Tan, arXiv:1304.1347, supply related FEI composition results; Gonzalez, MacManus and Pereyra, arXiv:2606.00246v2, develop a restriction/stopping-tree approach. Systematic linear codes, random-code union bounds, Walsh substitution, and tensor amplification are standard ingredients. This note gives their explicit constant-preserving combination as an obstruction to the present proposed mechanism; it does not certify first publication of that combination.
