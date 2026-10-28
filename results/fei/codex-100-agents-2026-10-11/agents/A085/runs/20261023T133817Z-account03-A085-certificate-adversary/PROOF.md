# Floor admission: complete endpoint and original-budget audit

Bits throughout. Full FEI is OPEN. This audits A097-NECESSARY-FLOOR-ADMISSION-SAME-ORIGINAL-OWNER@1 without changing its statement or hypotheses. A floor is necessary only for a DECLARED admission class. Ordinary inherited continuation can avoid admission entirely.

## 1. Exact minimum, including excluded endpoints

Let p be a finite probability law, with distinguished vacuum mass r, total nonempty mass t=1-r, and a specified nonempty set A of nonvacuum labels. Reference-only labels are allowed in A. Put a=p(A), b=t-a. A target q must be normalized, have the SAME vacuum mass r, and satisfy q(A)>=ell. We price D_2(p||q), allowing infinity if q vanishes on positive p mass.

For 0<=ell<=t, its infimum is:

* 0 if ell<=a, attained by q=p;
* a log2(a/ell)+b log2(b/(t-ell)) if a<ell<t, with the a=0 term interpreted as zero;
* infinity if ell=t and b>0 (no admitted finite-CE target);
* 0 if ell=t=a.

For t=0 only ell=0 is feasible, at cost zero. A floor ell>t is infeasible. These distinctions separate an infeasible class from a class containing only infinite-CE targets.

Proof: write z=q(A). Log-sum on A and its nonempty complement gives the displayed binary expression at z, retaining the vacuum separately. For a<z<t its derivative is t(z-a)/(z(t-z)ln2)>0. Therefore z=ell is optimal. When a,b>0, preserve p's conditional laws in A and its complement, rescaling their masses to ell and t-ell. Give all reference-only atoms zero mass. When a=0<ell, put ell on any reference-only atom in the nonempty set A and scale the complement by (t-ell)/t; the cost is t log2(t/(t-ell)). When b>0 and ell=t every target vanishes on positive true complement mass. The other cases follow by q=p and nonnegativity of KL. This proves the continuum statement; a finite grid is only corroboration.

In a complementary wrapper G=a_ctl+sigma*(1-a_ctl^2)*h, keep the ACTUAL signed vacuum, controller and coherent factors. For a matched incoming reference, the full conversion cost is EXACTLY beta times this minimum. Indeed each nonempty seed atom factors as B_U^2 p(T), each target as B_U^2 q(T), and sum_U B_U^2=beta. The vacuum contributes zero KL. This formula does not assume that the controller's vacuum amplitudes are individually nonzero. For mismatched incoming references, the conversion is a DIFFERENCE of cross-entropies, and the matched minimum must not be substituted without retaining that mismatch.

## 2. Independent reconstruction of A097's actual payment

Use the literal controller (1,0,0,0,-1,1,1,1,1,0,0,0,1,-1,-1,-1), with b_ctl=1-a_ctl^2 and beta=3/8. The core g equals -1 precisely on the two equal-sign three-bit inputs. Its polynomial is (1-y1*y2-y1*y3-y2*y3)/2. Thus the spectrum is uniform on empty and three pairs. Replacing each y by an independent L-bit parity preserves the four squared atoms and H(g)=2. Each physical seed coordinate has influence1/2; after the wrapper this is3/16. Direct controller edge counts give (5/16,5/16,1/2,1/2) for sigma=+ and (7/16,7/16,1/2,1/2) for sigma=-. Consequently the original B0=35/4 is <=4I(G) for ALL integers L>=1, independently of any later accounting. The actual source is P_G and its actual CE c_sigma=H(G) is charged once. It has at most64 atoms, so c_sigma<=6. Extra L-dependent influence credit is unused.

Reveal the whole first parity block. At every prefix all four support labels remain distinct and no two differ by the queried physical singleton, even at the last bit: every occurrence of the first block is paired with a nonempty other block. Each child spectrum is the inherited marginal, and matched references remain actual. Thus erasure, occupancy KL, singleton ghost, child JS and every calibration/phase-bin refund are exactly zero. The signed Fourier coefficients may change; their squares and full source CE do not. All 2^L histories have physical reaches summing to one. This is an analytic ALL-L argument, not extrapolation of the checks below.

At every leaf the remaining seed law is uniform on empty, B2, B3, B2 union B3. Set A={B2 union B3}. Then r=a=1/4, t=3/4, ell=1/3. Section1 gives the exact minimizer (1/4,5/24,5/24,1/3). Its full wrapper liability is delta=(3/32)log2(27/25)>0. Reached mean liability is delta, not 2^L delta. For any supplied eligible old booking 0<=omega<=1/4, the SAME original remainder is

35/4-c_sigma-omega-delta >35/4-6-1/4-3/32=77/32.

The booking's provenance is an external integration hypothesis, not a newly verified prior policy. Querying one remaining second-block bit with the INSTALLED full reference carried by marginalization gives the exact chain increment -D_occ<=0, with BOTH full children retained, including any constant-seed child. This establishes the original claim at its exact scope; no repair is supplied by this review. The A083 recipe is only an interface producing the stated target, not an independently accepted composite payment theorem.

## 3. A sharp adversarial boundary on extending the payment

Keep the SAME Boolean family, matched source, prefix, sign and original budget. Replace only the DECLARED admission floor by ell_k=3/4-2^-k for integer k>=1. At k=1 it equals the current mass1/4 and costs zero. For k>=2 the sharp full conversion price is

delta_k=(3/32)[2k-4-log2(3/4-2^-k)].

The formula follows directly from Section1 with a=1/4,b=1/2. The floors and their minimum prices strictly increase for k>=1, and delta_k diverges. Hence no finite unused original budget pays ALL such floor admissions. The exact budget condition is c_sigma+omega+delta_k<=35/4. out/FLOOR_FRONTIER.json records the first failing k for both signs and omega=0,1/4 in this FIXED dyadic family. out/INDEPENDENT.json verifies the immediate preceding and first failing values by clearing all rational exponents and directly comparing two integers; monotonicity proves minimality within the ENTIRE infinite dyadic family. This is not a claim of smallest dimension or smallest failure among all possible floor families.

In particular k=49 has delta_49>(3/32)*94=141/16>35/4 even BEFORE source cost and old debits. This gives a simple exact budget obstruction independent of computing c_sigma. At the limiting floor ell=t the finite-CE class disappears entirely. The original ell=1/3 theorem is unaffected; arbitrary strengthening of its floor is the invalid extension. No optional conversion, early borrowing of a future refund, changed source, extra influence or new ghost prepayment is allowed in this original-account comparison.

## 4. Independent validation and honest stopping point

The primary checker imports only A085's own earlier algebra/log helpers, byte-pinned before evaluation. It imports no A097 checker or proof code. An explicit signed three-pair polynomial independently predicts physical Fourier coefficients; integer FWHT and literal pivotal edge counts check the actual Boolean wrappers. Complete CE/KL identities use Fraction prime-log maps. All nonzero signs use100-bit outward dyadic bounds for40-term atanh series with a proved remainder, rather than a float tolerance or interval-overlap equality.

The second checker imports NO primary or author helper. Direct character sums reconstruct both128-vertex sources and four64-vertex converted children. Full conversion cost is rechecked by exact rational exponent products. It also maximizes the exact product of the three positive support masses over denominator24 floor-admitted laws INCLUDING an extra reference-only ghost atom; the unique maximizer is (5,5,8,0), confirming that ghosts cannot evade this minimum. Eight exact integer-power comparisons independently settle the budget boundaries.

First unsupported universal line: prescribe a useful, policy-compatible admission class for EVERY arbitrary Boolean core and bound its sharp conversion cost by the ACTUAL unused original margin, or construct an influence-priced initial source for every core. Neither an arbitrary floor nor its necessity nor its payment follows from the finite-core theorem. This review gains no universal FEI constant and produces no unbounded H/I Boolean family.
