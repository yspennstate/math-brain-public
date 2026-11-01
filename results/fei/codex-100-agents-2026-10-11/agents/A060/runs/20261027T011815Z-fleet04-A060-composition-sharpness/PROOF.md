# Exact terminal retention under compulsory stopping

All cubes are finite and uniform. Functions take values in {-1,1}; spectral entropy is in bits. This sharpens the terminal limitation of A059-PREPAID-TWO-TICKETS-AND-GEOMETRIC-STOPPING@1. It does not refute that theorem.

## 1. A059 transaction review, conditional on its original source

Let k=29/13. The previously reconstructed universal singleton inequality is D_i(g)<=k I(g). A059's original source rate 9/2 splits as 2k+1/26. For a pending ticket k t I(g), conditional influence conservation is I(g)=Inf_i(g)+E_a I(g_a). Transporting a ticket through an already-paid query releases k t Inf_i(g), with the remaining principal assigned to its actual children. At a ticket's selected query it is closed, and its cash k t I(g)-tD_i(g) is nonnegative. The other labelled ticket is transported, not spent. This independently reconstructs the new two-ticket transaction. No retrospectively recreated principal is available.

For independent continuation q<1, put A=k/(1-q). After a selected query the actual fee is tD_i(g), expected surviving principal is q A t (I(g)-Inf_i(g)), and the release is at least q A t Inf_i(g). If q<=1/2 then A<=2k<9/2, preserving the original 1/26 reserve. The independent coin has zero function influence and zero entropy fee; it has nonzero resource innovations. Both stopped and surviving children must remain. This is an expected-resource result, not a subtraction-only childwise account. It is conditional on the same original coherent-source/exterior escrow already reviewed in A060 stage9. A060 contributed the singleton dependency, so this is independent reconstruction of the NEW transactions, not an independent review of every dependency in the full theorem.

## 2. Exact actual Boolean control, including complete terminals

Let h(a,b) be -1 only at a=b=+1. Its four squared Fourier coefficients are 1/4, so H(h)=2, I(h)=1, and Inf_a(h)=1/2. Fixing a leaves a constant or a dictator, each with entropy zero and mean influence 1/2. Define G_r=z product_{j=1}^r h(a_j,b_j), where z is an untouched fresh tag. Thus H(G_r)=2r and I(G_r)=r+1. After querying one a_j in each of l distinct factors, every actual terminal core remains balanced, has entropy 2(r-l), and its expected influence is r+1-l/2. A sign from previous constant factors does not change either quantity.

Let b(x)=(-1)^(u1*u2+u3*u4), u_i=(1+x_i)/2, C=1_{x=(+1,+1,+1,+1)}, c=1/16, and K=b-C. Put F_r=K+C G_r. Since b is +1 on C, F_r is Boolean and matches A059's actual source family. The 16 coefficients of K have magnitudes 3/16 (ten) and 5/16 (six). Since every reached G remains balanced, its Fourier support is disjoint from K's core-empty sector. Hence for EVERY reached terminal, with its actual full spectrum retained,

    H(K+C G)=E0+c H(G),
    E0=8-(45/64)log2(3)-(75/64)log2(5).

The exterior coordinate influences are each 1/2-c: the only changed exterior edge has a balanced value on C and value -1 at its neighbor. Therefore

    H(F_r)=E0+r/8,       I(F_r)=7/4+(r+1)/16.

Let L be the number of distinct a_j queried before stopping, with a_1 always queried and each continuation independently accepted with probabilities q_1,...,q_{r-1}. For actual finite uniform physical dummy blocks these probabilities are dyadic, including 0 and 1; the formulas also hold algebraically for real probabilities in [0,1]. Write s_1=1 and s_j=product_{i<j} q_i. These are actual survival probabilities, not probabilities conditioned on successful core answers. All dummy outcomes and core siblings are retained. The tail-sum identity gives S_r=E L=sum_{j=1}^r s_j. Consequently

    E H(F_leaf)=E0+(r-S_r)/8,
    H(F_r)-E H(F_leaf)=S_r/8,
    E I(F_leaf)=7/4+(r+1-S_r/2)/16,
    I(F_r)-E I(F_leaf)=S_r/32.

The complete physical entropy debit is exactly FOUR times actual removed influence. There is no omitted signed exterior correction: the profile E0 stays fixed because the untouched tag keeps every core balanced. More explicitly, after ell deterministic factor queries already paid, retain their old debit ell/8 and all their siblings. The additional stopped debit is S_(r-ell)/8, and complete expected terminal entropy is E0+(r-ell-S_(r-ell))/8. The old influence removal ell/32 remains booked. Thus the same obstruction occurs after a positive old debit (take ell=1 and r tending to infinity), without deleting an old cost or refreshing an owner.

## 3. Sharp stopping requirement

For constant q in [0,1), S_r=(1-q^r)/(1-q); for q=1, S_r=r. Thus at A059's q=1/2 the complete debit is (1-2^-r)/4, while the complete expected terminal entropy is E0+r/8-(1-2^-r)/4. In particular the terminal/root entropy ratio tends to ONE, although the policy has paths of unbounded genuine query depth. The same is true for every fixed q<1. Tensorization removes fixed E0/r, but leaves the extensive unpaid terminal term.

For a horizon-dependent constant continuation q_r, the terminal/root ratio tends to zero if and only if r(1-q_r) tends to zero. Sufficiency: 0<=1-S_r/r=(1/r)sum_{j=0}^{r-1}(1-q_r^j)<=((r-1)/2)(1-q_r), by the finite geometric identity. Necessity: if r(1-q_r)>=epsilon on a subsequence, at least floor(r/2) terms have j>=ceil(r/2); q_r^j<=(1+j(1-q_r))^-1<=1/(1+epsilon/2), by (1-d)^j<=1/(1+jd). Their average deficit stays positive. Only r tending to infinity is at issue; r=1 and q=0,1 are handled directly.

For a general horizon-dependent schedule, the EXACT necessary and sufficient condition is (1/r)sum_j s_j ->1. For one FIXED infinite schedule, s_j is nonincreasing in [0,1]; its Cesaro average can tend to 1 only if EVERY s_j=1, equivalently all q_j=1. More strongly, any single fixed loss q_j<1 leaves asymptotic residual fraction at least 1-q_j. Later continuation cannot undo that loss while stopped siblings are retained.

## 4. Consequence for the SAME original pending owner

For the particular geometric potential A t I(g), retaining rate K=9/2 and reserve 1/26 requires A<=58/13, hence q<=1/2 when A=k/(1-q). Even discarding that reserve allows only q<=1-k/K=59/117. On the actual tensor control either fixed ceiling leaves terminal/root entropy ratio tending to one. Conversely terminal exhaustion requires q_r->1 with 1-q_r=o(1/r), so the SUFFICIENT coefficient k/(1-q_r) diverges faster than r and cannot fit the fixed original owner.

This is an incompatibility of this pending-potential mechanism with terminal exhaustion, not a lower bound on every possible payment. The SAME actual control admits the deterministic q=1 policy with total bill r/8, exactly four times removed influence and less than the original (9/2)c(r+1) core owner. Therefore the control disproves a no-killing conclusion FROM THE GEOMETRIC CERTIFICATE, not affordability of no-killing work in general. A059 already states the qualitative limitation; the new contribution is the exact full-terminal law and sharp horizon condition.

## 5. Universal unpaid step

A universal arbitrary-core stopping theorem must pay the full entropy of its retained terminals, or remove it by useful continuation paid from genuinely unused original capacity. Neither an unbounded possible depth nor an absolute affordable occupation bill implies entropy decay. Even allowing horizon-dependent continuation inside the same geometric potential cannot meet both requirements. The next mathematical target is an entropy-sensitive continuation rule whose fee is charged to actual removed influence (or another decreasing original resource), with both terminals retained. Supplying that universally remains open and cannot be replaced by this solvable tensor family.
