# Arbitrary-overlap collision reserve, v7

All cubes are finite and uniform; entropy uses bits. G and H are arbitrary Boolean functions on the SAME physical data coordinates. They may ignore any subset; no independence between branches is assumed. Let z be a new fair bit and F=(G+H)/2+z(G-H)/2. Write J=Pr(G!=H)=Inf_z(F), e=GH, and K=(H(G)+H(H))/2.

## Exact coherent posterior

For every data Fourier index T put a=Ghat(T), b=Hhat(T), r=(a^2+b^2)/2, d=(a-b)^2/4. The actual mux amplitudes are (a+b)/2 and (a-b)/2. When r>0 define v=d/r and w=a^2/(2r). With h the binary entropy,

    Psi(a,b)=E((a+b)/2)+E((a-b)/2)-(E(a)+E(b))/2
            =r [h(v)+1-h(w)],       E(x)=x^2 log2(1/x^2).

The zero row contributes zero. Thus L=H(F)-K=sum Psi is nonnegative. Parseval gives sum r=1 and sum d=J. This explicitly retains coherent collisions on every shared Fourier row; no disjoint-input chain rule is used.

For x in [-1,1], h((1+x)/2)>=1-x^2. Indeed its entropy deficit is the convergent nonnegative series sum_{k>=1} x^(2k)/(ln(2)*2k*(2k-1)); the coefficients sum to1 by continuity at x=1, and x^(2k)<=x^2. Here (2w-1)^2=4v(1-v). Consequently

    0<=Psi(a,b)<=r h(v)+4r v(1-v)<=r h(v)+4d.

Concavity of binary entropy therefore proves, in every dimension,

    0<=L<=h(J)+4J.                                      (1)

## The source is actual disagreement influence

For every Boolean e on independent fair input bits,

    h(Pr(e=-1))<=I(e).                                  (2)

Here is a direct reveal-chain proof. If a fair bit selects Bernoulli output laws of means alpha,beta, their mutual information is at most |alpha-beta|: split both laws into a common part of mass1-|alpha-beta| and their disjoint residuals, introduce an independent mixture flag, and reveal that flag. The common component carries no information about the selector; the residual carries at most one bit. In the input reveal chain for e, the two conditional output means differ by at most the probability that flipping this bit changes e, using the same unrevealed suffix as a coupling. Average over prefixes and sum the mutual informations. The sum is H(e), while the averaged pivotal probabilities are exactly the physical coordinate influences. This proves (2), including constants.

Since flipping e=GH requires flipping at least one branch, I(e)<=I(G)+I(H). Combining with (1),

    H(F)<=K+4J+I(GH)
         <=K+4J+I(G)+I(H).                              (3)

These are complete inherited branch entropies. If both branches have FEI constant C, (3) yields FEI constant max(C+2,4) for THIS mux. The +2 may not be restarted at every nested composition.

## One original reserve, all adaptive stopping histories

At each live node let L_v=H(F_v)-(H(G_v)+H(H_v))/2. It remains nonnegative by the exact posterior formula, for arbitrary simultaneous physical restrictions. At a data query let Delta K_v=K_v-E K_child. The coherent charge is Delta H_v-Delta K_v=L_v-E L_child. At selector revelation the charge is L_v, and the inherited selected core entropy has expected value K_v. After selection all further queries are inherited-core queries, with zero coherent charge.

For ANY finite adaptive physical stopping tree, using true reach weights,

    H(F_root)-E H(actual terminal)
       -sum_data w_v Delta K_v
      =L_root-sum_live_terminal w_v L_terminal
      <=L_root<=4J_root+I(G_root H_root).                (4)

After selector revelation K is the actual chosen core entropy. Every actual terminal entropy and both branch bills remain in (4). The data debits are signed; a negative debit is a refund and is not discarded. Start with the named original allowance B=4J_root+I(G_root H_root), debit the reached signed coherent charges, and retain L_v at each live frontier plus the original slack B-L_root. The exact identity proves conservation and nonnegative expected unspent reserve for every frontier. This is one root-owned reserve; it is never replaced by a new descendant allowance. Also B<=4I(F_root), since I(F_root)=(I(G)+I(H))/2+J. This is a composition-overhead statement, NOT an influence payment for the still present inherited branch entropy or its signed decrements.

## Bent one-point edit: the selector-only price must diverge

Let n=2m, N=2^n, M=2^m, and u(s)=(-1)^(sum_{j=1}^m s_{2j-1}s_{2j}) on the 0/1 cube. It is Boolean, u(0)=1, and every Walsh coefficient is +/-1/M, by multiplying the explicit two-bit transform (1,1,1,-1)/2. Flip u only at0 to obtain v. Thus vhat(T)=uhat(T)-2/N and J=1/N. Every mux row has d=1/N^2 and r=(N +/-2M+2)/N^2. From Psi>=r h(d/r)>=d log2(r/d),

    L/J >= log2(N-2M+2) >= log2 N-1=n-1,
    R/J=(L-4J)/J >=n-5.

The last inequality is the integer identity N-2M+2-N/2=(M-2)^2/2>=0. Hence no absolute selector-only price is possible, even for a single actual Boolean phase edit away from the common ray. The original disagreement e=uv is a point defect and I(e)=2n/N, so the supplied source in (3) has the right logarithmic order. This is not an unbounded H(F)/I(F) family.

## Honest universal boundary

The scalar split profile and bent point-edit obstruction are PRIOR WORK, independently rederived here, not novelty claims: math-brain cards claim_76e621c18b4bc9fb5327f154b1f567e583b339d4cbcd041d2453291adf7cd257 and claim_7f5f22ff912203aa5274e2ba4e216316da9392bbfda1386c6f02803c17b8e759 explicitly record the stronger upper profile h(J)+(2/ln2)J and the sharp additive constant. Our 4 is a convenient proved rational relaxation. The delta is the explicit original disagreement-source allocation and stopping ledger, together with the following obstruction to renewing that allocation.

Take even n>=2 and the actual Boolean complete quadratic f_n(x)=(-1)^(sum_{i<j} x_i x_j). At every reached restriction with k remaining bits the quadratic part stays complete; only its affine part changes. Split on ANY next bit. The two branches multiply to a parity of the other k-1 bits, up to sign. Its disagreement-source influence is therefore k-1. The true reach weights at each depth sum to1, so the total of newly supplied I(GH) tickets over any complete coordinate-order decomposition is n(n-1)/2. At the root every derivative is a nonconstant parity, so I(f_n)=n/2. The ticket sum divided by original influence is n-1, unbounded. This proves that the naive nested summation is FALSE on actual Boolean functions, even when the query order is adaptive. It does not refute the one-original-reserve ledger (4), or FEI.

The all-dimensional overlap overhead and its one-reserve stopping ledger are proved above. What is NOT proved is an allocation of this disagreement-influence source across arbitrary nested mux decompositions without charging the same physical edge again, while also paying every complete inherited core entropy. The first unsupported line would be summing I(G_v H_v) over mux levels and asserting that the sum is O(I(F_root)). Full FEI remains OPEN. The next step is to exhibit a physical-edge ownership rule or a counterexample to such a rule, with the old original reserve debit retained.
