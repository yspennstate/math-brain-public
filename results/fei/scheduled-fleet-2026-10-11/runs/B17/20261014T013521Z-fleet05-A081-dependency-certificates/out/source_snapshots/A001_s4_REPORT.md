# exact target, quantifiers, hypotheses and units

The all-dimensions FEI target is one finite absolute C such that every finite n>=0 and every actual Boolean sign on the uniform {-1,1}^n cube satisfies H_2(f)<=C I(f). Here p_S=hat f(S)^2, H_2=sum_S p_S log2(1/p_S), I=sum_S |S|p_S, and zero terms vanish. Constants have H=I=0. Full FEI is OPEN.

This stage audits A096's normalized terminal refund at its full stated scope and resolves one proposed route to the missing payment: fixed low-degree inspection with one undifferentiated tail. For every fixed L>=0, this coarsening has an unbounded residual bill on actual full-support Boolean functions with all coordinates relevant and I tending to zero. The genuine oriented bill stays <=2I and entropy stays <4I. This is a scoped information-loss obstruction, not an FEI counterexample or a new proposed universal sufficient theorem. All entropy and KL are in bits.

# sources actually read, revisions and theorem locators

Read BOARD.md (supervisor snapshot 2026-10-14 01:10 UTC), B01 STREAM_NOTES.md v1 and own STATUS.md at stage start. Read EXECUTION_PROTOCOL.json in full, execution-v2. B01's old X009/B05 argmin assignment is completed and archived; A098's refreshed allocation and BOARD now direct A001/A096 to the signed-Boolean terminal-core KL payment. This consumes the new dependency without rebuilding old gap maps.

Critical originals read: A096 stage3 REPORT.md, DERIVATION.md equations (1)-(6), cutoff proof and CLAIMS.json; A073 stage3 REPORT.md, full-normalizer acceptance and lost-support mutation; A098 stage3 CLAIMS.json, independent acceptance of the influence-only slice of A001@1; own stage3 report and immediate stage4 derivation. Consulted A031 LEARNED.md for the existing carrier-only obstruction and to distinguish it from the degree-bucket obstruction here. A045/A073 STATUS and BOARD ownership keep mixed-biased work separate from the present uniform terminal-row audit. Source-byte receipts are in out/SOURCE_MANIFEST.json. No source folder was modified or upstream executable imported.

# complete derivation or exact first unsupported line

## 1. Acceptance interface and independent A096 reconstruction

For every relevant i, write e_i=Inf_i, mu_i(T)=p_(T+i)/e_i and r_i(T)=p_T+p_(T+i), T excluding i. Both are complete probability laws. Define D_i=D(mu_i||r_i), M_i=sum_T p_(T+i)log2(r_i(T)/p_(T+i)), M=sum_i M_i. Then

    M=sum_i e_i log2(1/e_i)-sum_i e_i D_i,
    M<=B<=M+I/ln2.

The joint laws P(i,T)=p_(T+i)/I and Q(i,T)=(e_i/I)r_i(T) normalize to one and share coordinate marginal e_i/I. Their joint divergence is I^-1 sum_i e_i D_i. These previously established identities are the exact interface, not new progress.

Take h=chi_Z product_{b=1}^m f_b, with ell>=2 fresh parity bits and arbitrary finite Boolean seed f. Let J=mI(f)+ell, F=1+A_k(h-1), q=2^-k and d=(1-q)^2+q^2. The row laws for a seed coordinate in h are the seed row laws tensored with the SAME spectator spectral distribution; their likelihood ratio is unchanged. Parity rows have mu=r and D=0. Hence original row divergences equal D_i(f), and the summed seed contribution is mI(f)D_f.

On activation, all core-support rows are extended by a uniform control-subset law. On derivative support the complete reference is q times that extension; the vacuum exception is outside it because h has no singleton coefficients. Thus each relevant core row satisfies D_i(F)=D_i(h)+k. A control row has exceptional derivative probability q, complete reference probability d, and all other occupied likelihood ratios 1/(2q), of total derivative mass 1-q. Therefore

    D_c=(1-q)(k-1)+q log2(q/d),
    I(F)=q(J+k),
    I(F)D_F=q[mI(f)D_f+kJ+kD_c],
    M(F)=qmM(f)+k[q(1-q)+q^2 log2(d/q^2)].       (1)

Only the k-bit activation rarity is universally refunded. The arbitrary seed divergence is still present. In the lower-endpoint degree>=2 tail, all positive core costs lie above the parity support. A control contributes q/2 from core sets and q^2[2^(k-1)-k] from pure-control sets, giving

    M_ge2(F)=qmM(f)+kq(1-kq).                   (2)

For a general fixed ell, replace the pure-control count by sum_{j=ell}^{k-1} binom(k-1,j). These reconstruct the finite part of A096@1, including constants (their seed contribution is zero) and irrelevant coordinates (omitted).

The cutoff quantifiers also hold. For nonconstant seed dimension n>=1 and finite nonnegative s(N)=o(N), eta_m=sup_{N>=mn}s(N)/N is finite and tends to zero. Choose k_m=ceil[4(n+1)m sqrt(eta_m)+2sqrt(m)]. Then k_m=o(m), N_m=mn+ell+k_m<=(n+2)m eventually, and s(N_m)<=4(n+1)m sqrt(eta_m). Eventually k_m-s(N_m)>log2(mI(f)+ell+k_m), so the actual F_m meets I(F_m)<=2^-s(N_m). Its retained tail contains qmM(f), so its ratio is at least mM(f)/(mI(f)+ell+k_m); this lower bound tends to M(f)/I(f). The reverse supremum inequality is M_geell<=M. For an infinite unrestricted supremum, apply this argument to each finite seed ratio, rather than exchange supremum and limit. This independently accepts A096-TERMINAL-KL-REFUND-AUDIT@1 at its full original scope without contributing a repair. A073's existing independent acceptance is consumed and retained.

## 2. Fixed bounded-degree inspection preserves normalizers but loses refund

Fix an integer L>=0. Let C_L keep each residual Fourier atom T with |T|<=L individually, and merge all |T|>L into one tail atom. Define

    D_i^L=D(C_L mu_i || C_L r_i),
    M^L=sum_i e_i[log2(1/e_i)-D_i^L].

The complete reference is coarsened, never conditioned on derivative support. Thus its normalizer remains exactly one. Data processing implies D_i^L<=D_i and M^L>=M>=0. Exact KL chain rule gives

    M^L-M=sum_i e_i mu_i(tail)
               D(mu_i(.|tail)||r_i(.|tail)).     (3)

Singleton cells have no conditional KL. Equation (3) identifies precisely the missing currency: within-tail likelihood ratios. Merely counting tail mass does not retain them.

## 3. Full-support, vanishing-influence witness with no auxiliary factor

Let f_n be the n-bit sign that is -1 at one point and +1 elsewhere, n>=2. Put e=2^(1-n). Its constant coefficient is 1-e and every nonempty coefficient has magnitude e. Every physical influence equals e, so I(f_n)=ne. Every Fourier coefficient is nonzero. Its oriented row bill is exactly

    M_i=e-e^2+e^2 log2(((1-e)^2+e^2)/e^2),
    M(f_n)/I(f_n)<=1+2(n-1)e<=2.                (4)

The last inequalities use (1-e)^2+e^2<=1 and (n-1)2^(1-n)<=1/2. Also, writing eta(u)=-u log2 u and W=2e-e^2,

    H(f_n)=eta((1-e)^2)+2(n-1)W
       <=2e/ln2+4(n-1)e<4ne,                   (5)

since eta(u)<=(1-u)/ln2 and ln2>1/2.

For fixed L take n>=max(6,2L+2), m=2^floor(n/2) and G_n=f_n^tensor(m). All mn coordinates remain relevant, every influence equals e, every Fourier coefficient remains nonzero, and there are no auxiliary parity bits or dummy coordinates. Tensor product spectra prove H and I add, while each derivative likelihood ratio has the same independent spectator factor in numerator and denominator. Thus

    I(G_n)=mn e=n*2^(1-ceil(n/2))->0,
    H(G_n)/I(G_n)<4, M(G_n)/I(G_n)<=2.           (6)

We now bound the coarsened divergence in every row. Write the residual subset as its seed-block component and m-1 spectator-block components. The seed derivative law is uniform on its 2^(n-1) residual atoms: each has probability e. Therefore total derivative mass on the individually inspected low atoms is at most

    beta=e sum_{j=0}^L binom(n-1,j).

On any occupied row atom, mu_i/r_i<=1/e because r_i>=p_(T+i). Thus the contribution of all low singleton cells to D_i^L is at most beta(n-1), including any negative terms.

Set a=(1-e)^2. The complete reference tail has probability at least the event that exactly one spectator block has degree >L and all other spectators are empty. The seed row is unrestricted and its reference mass is one. This event has mass

    (m-1) z a^(m-2),
    z=e^2 sum_{j=L+1}^n binom(n,j).

For n>=2L+2, binomial symmetry gives z>=e. For n>=6, me<=1/4 and m-1>=m/2. Bernoulli's inequality gives a^(m-2)>=(1-2e)^(m-2)>=1-2e(m-2)>=1/2. Consequently

    r_i(tail)>=me/4=2^-(ceil(n/2)+1).

The tail KL term mu_tail log2(mu_tail/r_tail) is at most log2(1/r_tail), since mu_tail<=1; this remains true when the term is negative. Hence

    D_i^L<=beta(n-1)+ceil(n/2)+1,
    M^L(G_n)/I(G_n)>=floor(n/2)-2-beta(n-1).     (7)

For fixed L, beta(n-1) is an exponentially decaying polynomial in n, so (7) diverges. Together with (3),(6), it also proves

    (M^L-M)/I>=floor(n/2)-4-beta(n-1)->infinity. (8)

This is a normalized-reference obstruction on actual Boolean functions even at vanishing total influence and full Fourier support. It is stronger than the parity-shift diagnostic below because stripping dummy coordinates or an independent parity factor does not remove it.

The same witness has an exact repair if its genuine block structure is retained: discard only the independent spectator components, keeping the complete seed row. The likelihood ratio is then unchanged and KL loss is zero. M<=2I is still paid from the one original influence budget by (4). This is a comparison of two quotients on the same family, not a new class-FEI theorem. Absolute degree merging and spectator-aware marginalization are mathematically different operations.

## 4. Exact activated-row mutation and scope boundary

An additional audit on A096's precise interface takes h=chi_Z f_n^tensor(m), ell=L+2, F=1+A_k(h-1). Every core derivative row has residual degree >L, and its coarsened derivative is concentrated on the tail. Direct complete-reference counting gives

    r_i(tail)=q+q^2 sum_{j=L+1}^k binom(k,j),
    D_i^L=log2(1/r_i(tail))<=k.                 (9)

Taking m=2^n and k=n, seed rows alone give M^L/I>=2n(n-1)/(3n+ell), while actual M/I<=2. Actual H/I<4 follows from (5), H(h)=mH(f_n), and the balanced activation spectrum, whose selector entropy is <=4kq+2q/ln2 and whose physical influence is q(mI(f_n)+ell+k). The full-support tensor witness in (7) already suffices; (9) supplies a literal mutation of the accepted A096 normalizer/refund.

The conclusion excludes exactly fixed bounded-degree atom inspection followed by one undifferentiated tail, and any weaker partition obtained by merging its cells. It does not exclude an adaptive degree bound growing with the function, a structured tail reference, the full row KL, or a signed conditional reference that preserves tail information. A031's earlier carrier-only scalar-envelope obstruction is not repeated or upgraded; this proof concerns an explicitly normalized KL coarsening and its exact within-tail loss.

## 5. First unsupported universal implication

No dimension-independent bound has been proved for the complete terminal bill M, or for R_ge2 after the already paid root and T12 layers. The surviving line is

    D(P_f||Q_f)>=sum_i(e_i/I)log2(1/e_i)-K

for one finite K and every actual Boolean seed. Replacing D by the normalized D^L gives a strictly stronger sufficient requirement; (7) refutes that replacement. The large exact activation refund alone does not imply the surviving line. A signed Booleanity argument must retain or pay the within-tail conditional divergence, not infer payment from tail probability or a finite degree prefix.

# executed validation with domain, arithmetic, commands and outputs

Frozen specs preceded their jobs. Commands from A001:

    python -X utf8 runs\20261014T011101Z-fleet05-A001-quantifier-audit\code\check.py review
    python -X utf8 runs\20261014T011101Z-fleet05-A001-quantifier-audit\code\check.py coarse
    python -X utf8 runs\20261014T011101Z-fleet05-A001-quantifier-audit\code\check.py symbolic
    python -X utf8 runs\20261014T011101Z-fleet05-A001-quantifier-audit\code\check_tensor.py

REVIEW.json: 78 explicit Boolean activations, eight named seeds, declared m/ell/k only, 5,437 assertions PASS in 5.645 seconds. It independently recomputes integer Walsh spectra and direct physical flips, complete row/joint normalizers, literal joint KL, tensor divergence, every activated core/control row and the exact M_ge2 tail. COARSE.json: 30 physical point-seed tensor/parity activations, L=0,1,2, 1,906 assertions PASS in 0.863 seconds, including the exact tail normalizer and likelihood-ratio mutation. SYMBOLIC.json: 12 declared factored large-family parameters, 37 assertions PASS in 0.001 seconds; no exponential truth table is allocated.

TENSOR.json: 12 complete unpadded physical tensor cases, n=2,3 and m=2,3, plus 12 declared symbolic parameters n=6,8,12,20, L=0,1,2 and m=2^floor(n/2). It passes 480 assertions in 0.387 seconds. Exact degree probabilities use the generating polynomials

    P(t)=(1-e)^2+e^2[(1+t)^n-1],
    mu_seed(t)=e(1+t)^(n-1),
    r_seed(t)=(1-e)^2+e^2+2e^2[(1+t)^(n-1)-1].

Truncated convolution of each seed row with P(t)^(m-1) computes the full low-degree masses exactly. Every finite row is matched to direct physical spectra; symbolic event bounds and tail probabilities are compared as rational numbers. The analytic proof, not these finite cases, supplies all fixed L and all admissible n.

Total: 7,860 exact assertions in 144 declared cases, zero failures. No floating logarithm decides a sign: review identities are exact Fraction-weighted dictionaries of prime logarithms, and new comparisons are rational inequalities. Both helpers are independent and execute only from A001; no upstream code or import cache is written. Maximum physical dimension is 12. Estimated memory is 80 MB; all jobs ran below 55 seconds and below the 300 MB memok trigger. No automatic dimension increase, GPU, background process or heavy census occurred.

# proof dependencies and changed downstream conclusions

A096-TERMINAL-KL-REFUND-AUDIT@1 is independently accepted at its original full scope by A001, without repair; A073's earlier acceptance is retained. The new diagnostic is self-contained finite Fourier product algebra, probability KL chain rule, integer binomial symmetry and Bernoulli's inequality. It uses A096 transport only for the additional activated mutation; the stronger unpadded proof (7) does not depend on that claim.

Adopt A098's independent acceptance of only the influence-vector-only reference slice of prior A001@1. The earlier product-reference/sparse-row/bent clauses remain pending their own full review. Historical statement hashes and source bytes are preserved; local envelope hashes are recorded separately. No shared claim status is changed.

The B01 broad-candidate review cap remains active. This stage performs source review and closes a narrow mechanism obstruction rather than opening a universal proof candidate. A096/A073/A099 should reject a finite-degree/coarse-tail divergence as an adequate substitute for the complete Q refund. A031/A033 should retain within-carrier/tail information when combining signed correlations with degree localization. The obstruction does not refute a paid growing-degree or function-specific tail mechanism.

# one next mathematical action and independent reviewer

Next: construct a spectator-compatible quotient for the first genuinely non-product derivative row and state its exact within-tail conditional KL remainder; price that remainder once from a physical influence account while retaining the complete Q and terminal core. The tensor guard requires zero loss when both row laws share an independent spectator factor; the new full-support guard requires restoring the refund hidden above every fixed degree. A096 owns the signed row mechanism, A073 its exact normalization, A001 its quantifier and budget audit. A086 primary and A094 alternate independently review (7)-(9); A073 can certify the polynomial tail bounds. This is a saved handoff, not an external message.

# actual persistence receipts or precise save blocker

The assigned run contains REPORT.md, CLAIMS.json, PROGRESS.json, byte-identical PACKET_DELTA.json, immediately saved DERIVATION.md, two frozen specs, independent scripts and four exact outputs. STATUS.md has two lines; WORKLOG.md is appended and LEARNED.md updated. out/PERSISTENCE_RECEIPT.json gives byte sizes, hashes and schema/readback checks; all artifacts are below 20 MB. Only A001 was written. Supervisor adoption, mirrors, downstream use and independent acceptance of the new diagnostic are unobserved; no local save blocker exists.

**Universal bridge:** This stage moves C018 by independently accepting A096's complete terminal-KL transport and excluding a normalized bounded-degree refund mechanism even on unpadded full-support Boolean families with I tending to zero: its unpaid bill/I is at least floor(n/2)-2-beta(n-1), while genuine M/I<=2. The new universal erasure payment improvement is zero; the complete terminal-core divergence and R_ge2<=K I remain unproved. NEXT retains spectator-compatible within-tail information on the first non-product row because the exact loss identity shows what finite-degree merging discards; paying that signed remainder from one original influence budget addresses the surviving universal bridge rather than adding another isolated class result.
