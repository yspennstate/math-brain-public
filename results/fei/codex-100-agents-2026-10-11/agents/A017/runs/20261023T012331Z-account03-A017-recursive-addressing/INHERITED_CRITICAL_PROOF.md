# Six coherent edits: exact critical-alphabet repair

Uniform signs, entropy in bits. Let x be n physical controls, q any quadratic polynomial including arbitrary linear and constant terms, M any binary linear map, and y_z independent distinct physical data signs. For a set E of at most six vertices lying in one address fiber, set F=(-1)^q(x)(1-2*1_E(x))y_(Mx). Repeated occurrences of one address z use the SAME data coordinate. Different labels use independent coordinates. We prove H(F)<=(4+2/ln2)(I(F)-1). The stopping proof also works without the shared-fiber assumption, but the packet claim keeps it for the exact fiber ledger. This is a restricted theorem, not full FEI.

## 1. Exact conditional ledgers under reuse

For delta=2^-n, base b=(-1)^q and a_z(S)=E[b(x)1_(Mx=z)chi_S(x)],

    a'_z(S)=a_z(S)-2delta sum_(w in E,Mw=z)b(w)chi_S(w).

This is a signed coherent amplitude sum. Squaring each amplitude gives the actual spectrum; no edit mixture is substituted. With r=rank M, K=ker M and k=rank(Q|K), for nonempty E in fiber z0,

    H(F)=2r+k+2^-r[H((b(1-2*1_E))|fiber z0)-k].

For E empty, H=2r+k. Quadratic flatness follows by autocorrelation: the phase autocorrelation vanishes outside the polar radical, and is a character on it. Its Fourier transform is the uniform law on an affine annihilator coset. A fiber law repeats across 2^r ambient control coefficients, while the data label costs r bits. A choice of kernel basis is used only for this entropy identity, never for physical influence.

An active address coordinate (Me_i nonzero) has influence 1/2. For an inactive coordinate let d_i(w)=ell_i+(Qw)_i. The exact change of influence is

    Delta Inf_i = 2delta sum_(w in E,w+e_i notin E)(-1)^d_i(w).

Each crossing edited edge is counted once; edges with two edited endpoints make no change. The baseline is 1/2 for a nonzero polar row, and ell_i otherwise. All data-coordinate influences sum to 1. At every restriction these statements hold with its actual affine address, restricted quadratic, conditional edit set and physical dimension. For any current spectrum p_(S,z),

    C_i=2I(D_i)=2 sum_(z,S contains i)|S|p_(S,z).

The degree includes the data-bit contribution to the derivative boundary cost. Iterated addressing M_t=A_t M_(t-1)+B_t and quadratic updates q_t=q_(t-1)+p_t may reuse physical controls and labels; evaluate these ledgers at each stage and take differences, preserving signed cancellations. Shared-fiber stages require M_t E to be a singleton. The terminal data label is never freshly charged per level.

## 2. Independent exact critical certificate: every four-bit Boolean coordinate

For a Boolean phase on D<=3 controls, positive influence is at least 2^(1-D)>=1/4, hence B_i<=1<=4Inf_i. For D=4 positive influences are multiples of 1/8. The only case not immediately paid by B<=1 is Inf_i=1/8, meaning exactly one pivotal undirected edge along i. Its two three-bit children a,b differ at exactly one vertex. Translate that vertex to zero and apply a global output sign so a(0)=1. This preserves B and selector influence; the seven remaining signs have exactly 128 possibilities.

Let W_s=sum_x a(x)chi_s(x), with integer direct character sums on three bits. Parent Fourier amplitudes are (W_s-1)/8 for the selector-absent label and 1/8 for the selector-present label. Thus Inf_i=1/8 and

    64 B_i = sum_s [(t_s+1)log2(t_s+1)-t_s log2(t_s)],
    t_s=(W_s-1)^2.

Parseval gives sum_s t_s=56. Code critical.py uses direct 8x8 character sums, independently of the inherited FFT helper. The exhaustive normalized 128-case certificate has exactly two squared-amplitude histograms:

    {1:4,9:3,25:1}  (112 seeds),
    {1:7,49:1}      (16 seeds).

For each histogram it checks ONLY the exact integer inequality

    product_t(t+1)^((t+1)c_t) < 2^32 product_t t^(t c_t).

The positive integer slacks are saved in out/CRITICAL_CERTIFICATE.json. This is precisely B_i<1/2=4Inf_i, not a floating-point estimate. The same certificate gives the exact maximum by rational comparison of the products. Therefore EVERY coordinate of EVERY actual Boolean function on at most four bits obeys B_i<=4Inf_i. If Inf_i=0, its spectral coordinate is absent and B_i=0. Adding a retained data sign leaves this conditional erasure entropy unchanged. This finite statement is closed by the complete normalized enumeration and integer certificates; no asymptotic inference is involved.

The initial census separately tested all 1024 quadratic/linear four-bit codes with all 105 translated three-edit sets {0,u,v}: 107,520 roots, 376,320 polar-coordinate tests, including 21,504 critical Inf=1/8 tests, and no K4 bad polar coordinate. It was useful discovery evidence; the smaller independent certificate establishes the generic critical step.

## 3. All-dimensional good access pivots, now with six edits

Query all address-active physical controls first. Each has influence 1/2. Once the address is fixed, stop unedited branches at their quadratic phase. On edited branches query a nonzero row of the remaining polar matrix, stopping when that matrix vanishes. Restriction preserves at most six edited points. At a phase pivot with D remaining controls, the unedited quadratic influence is 1/2 and each edited point can change it by at most 2^(1-D), so

    Inf_i >= 1/2-12*2^-D.

For D>=6 this is at least 5/16>1/4, so B_i<=1<4Inf_i. For D=5 it is at least 1/8, with positive influences in the lattice (1/16)Z. The case Inf_i=1/8 is paid by the two-edge certificate below. Every other possible influence is at least 3/16. Conditional entropy concavity gives B_i<=h2(Inf_i), and h2(t)/t decreases for t>0 (its derivative has sign ln(1-t)). Exact integer arithmetic gives

    h2(3/16)<3/4  iff  3^3*13^13>2^52,

whose positive slack is saved in the certificate. Combining the two-edge certificate with this inequality gives B_i<=4Inf_i in D=5 as well. For D<=4 use the generic certificate above, including any irrelevant pivot with Inf_i=0. Every queried node is K4-good. Consequently the localized bill sum_(B_i>4Inf_i) w_i C_i is exactly ZERO. This is a stopping-tree claim; unqueried nonpolar dummy directions may still be bad. No boundary reserve or summed root second moment is spent.

## 4. Complete terminal payment and independent A022 reconstruction

A clean quadratic leaf has H=k<=2I_phase because there are at least k nonzero polar rows of influence 1/2. An edited leaf is a character times phi=1-2*1_E with s=|E|<=6. We prove

    H(character*phi) <= (4+log2 6) I(character*phi).

This reconstructs and extends the sparse-leaf argument in A022 PROOF.md section 2; only its s<=4 subclaim is independently accepted here, not the entire fair-selector/activation theorem.

If s=0 the character entropy is zero. Put u=s*2^-D. When 0<u<=1/4, each influence of phi is at most 2u<=1/2; multiplication by a character complements selected influences and therefore cannot decrease total influence. The empty spectral mass of phi is (1-2u)^2, and tail mass v=4u(1-u). With L=log2(1/u)>=2,

    H(phi)<=h2(v)+vD
           <=4u[2L+log2 s+log2(e)-log2(3)],
    I(phi)>=2u L.

The entropy step uses h2(v)<=v log2(e/v), 3u<=v<=4u and D=L+log2 s. If the bracket's constant correction is negative, the ratio is at most 4. Otherwise division by 2uL gives H/I<=4+log2 s because L>=2 and e<3. The estimate e<3 follows directly from its positive factorial series. Thus H/I<=4+log2 6.

For completeness, the edge-isoperimetric lower bound is elementary: a set of s vertices has at most (s/2)log2 s internal edges. Induct on dimension, splitting sizes a<=b, bounding cross edges by a. The needed inductive inequality is h2(a/(a+b))>=2a/(a+b), the concave chord bound. Its edge boundary is at least s log2(2^D/s), giving I(phi)>=2uL. The critical certificate also independently checks the internal-edge integer inequality on all its three-bit seed sets.

If u>1/4 and s<=6, then 2^D<4s<=24, hence D<=4. Apply entropy subadditivity and h2(p)<=p log2(e/p) to the ACTUAL character-multiplied function. Every positive physical influence is at least 2^(1-D), so

    H <= (D-1+log2 e) I <= (3+log2 e)I < (4+log2 6)I.

Constants have zero entropy. This avoids assuming character influence monotonicity in the dense regime. In A022's original s<=4 dense regime D<=3, its H/I<=4 bound follows from minimum nonconstant edge boundary D and H<=D; the complete isoperimetric induction above reconstructs that step too. A022's retained-core leaf result is independently reviewed at precisely this scope.

Finally 4+log2 6<4+2/ln2 because ln6<2: e>1+1+1/2=5/2 implies e^2>6. Thus every retained phase terminal is paid below the access coefficient.

## 5. One influence partition and the final theorem

For any Boolean one-bit query, Delta H=B_i+JS_i with JS_i<=2Inf_i/ln2. A self-contained scalar proof is in the saved stage-3 DERIVATION section 4: the scalar Jensen-Shannon term is at most (sqrt(p)-sqrt(q))^2/(2ln2), and signed child amplitudes only increase this difference. Its derivative proof uses atanh(x)<=x/sqrt(1-x^2), valid including endpoints by continuity. Hence every access decrement is <=K Inf_i, K=4+2/ln2.

Influence and entropy telescope exactly along the finite physical tree. Leaves retain one named data coordinate each; their weighted data influence is exactly 1, even when many branches reuse the same physical y_z. Therefore

    I(F)-1 = sum_internal w_i Inf_i + sum_leaf w_leaf I_phase(leaf),
    H(F) <= K sum_internal w_i Inf_i
             +(4+log2 6) sum_leaf w_leaf I_phase(leaf)
          <= K (I(F)-1).

This is the complete terminal-inclusive all-dimensional six-edit theorem. The earlier two-edit signed ledger and K2 separator obstruction remain valid and are not refuted. Independent full-chain review of this continuation is pending.

## 6. Generic two-edge certificate at D=5

When Inf_i=1/8 on five controls, the four-bit children differ at exactly two vertices. A translation and invertible linear map of the UNQUERIED coordinates maps them to (0,0) and (1,0), writing the four-bit space as (t,z) with z three-bit. A common character of these unqueried variables and a global sign make the two child values +1. These operations preserve selected-coordinate B_i and Inf_i only: they are NOT used to transport other physical influences, C_i, or terminal budgets.

The projected child h(z)=[a(0,z)+a(1,z)]/2 is ternary, h(z) in {-1,0,1}, h(0)=1. Selected-coordinate coefficients vanish on t-frequency one; on t-frequency zero, the absent/present amplitudes are (W_s-1)/8 and 1/8 with W_s=sum_z h(z)chi_s(z). Thus the same integer-product formula for 64B applies. All 3^7=2187 normalized ternary cores are exhaustively checked by direct character sums in ternary.py, with 13 amplitude histograms and zero violations of B<=1/2. This closes the only D=5 critical access case for six edits. The certificate is local and does not transfer a resampling-code refund into physical influence.

## 7. First seven-edit failure of the fixed order, and its adaptive repair

Take five physical controls, M=0, q=x0*x1+x1*x2+x3*x4, and E={x:x0=x1=1} minus the vertex (1,1,0,0,0), so |E|=7. The minimum-index polar pivot x0 has

    Inf_x0=1/16,
    B_x0=1-(45/64)log2 3-(25/32)log2 5+(39/64)log2 13,
    C_x0=3/8.

B_x0>4Inf_x0 is the exact integer inequality 2^192*13^156>3^180*5^200. The two children are a four-bit bent quadratic and its one-point flip, which explains the coherent small-influence collision. Code seven.py independently checks actual edge/mixed-face energies and the spectrum.

The minimum-index polar stopping tree has exactly one K4-bad node, with total bill 3/8. Query x1 first instead: all subsequent phase nodes have dimension <=4, so the generic certificate pays every query. The exact repaired bill is zero, queried influence is 7/8, and terminal phase influence is 21/16, totaling the original 35/16 phase influence. Terminals with <=7 edits satisfy H<=(4+log2 7)I_phase by the same sparse/dense proof; since ln7<2 (e>1+1+1/2+1/6=8/3 and 64/9>7), this is below K. The repaired fixture therefore retains the full terminal cost and proves H<=K(I-1). This is a specified-order obstruction and an actual adaptive repair, not a seven-edit universal theorem or an FEI counterexample.

## 8. Exact first unsupported universal line

For arbitrary seven-edit quadratic phases on five controls, no proof yet selects a K4-good nonzero polar row or pays all unavoidable bad rows with one conserved reserve. At this threshold a nonzero polar coordinate may have influence 1/16 and its children may differ at one vertex in a four-bit core; the three-bit critical certificate no longer applies. Larger point counts eventually make the retained sparse-leaf coefficient grow logarithmically. Neither a point-count-independent representation/refinement for arbitrary Boolean sources nor a universal boundary payment is supplied. NEXT is the seven-edit five-control pivot-selection/reserve problem, with the displayed 3/8 bad-bill fixture as a mandatory test. A069's simultaneous cell-resampling refund concerns fixed-code occupation cost and must not be renamed as this physical-query reserve.
