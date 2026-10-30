# GMP Proposition 5.1: the actual decrement also diverges at the prescribed query

This is a quantitative audit of the primary family, not a priority claim. Let k>=1, n=3k, epsilon=2^{-n}=8^{-k}. Partition the data coordinates into k blocks of width three. Let f_k be the sign-valued OR of the k positive AND blocks. Let y be minus on the first k-1 blocks and plus on the last block, and put g_k=f_k-2 1_{y}. The point y is a minimal positive input of f_k, so g_k is Boolean and monotone. Define a new Boolean function F_k by F_k(x,+1)=f_k(x), F_k(x,-1)=g_k(x). It is monotone, and belongs to the source's delta-tribes class. The queried variable below is this new selector z, not a shared-block coordinate.

For every Fourier data index T, its selector packet has coefficients

c_T=fhat_k(T)-epsilon chi_T(y), d_T=epsilon chi_T(y).

Thus I_z=sum d_T^2=epsilon. Define the true decrement Delta_z=H(F_k)-(H(f_k)+H(g_k))/2. Its erasure part is B_z=sum_T (c_T^2+d_T^2) h2(d_T^2/(c_T^2+d_T^2)). The physical child mixing remainder R_z is nonnegative, so Delta_z=B_z+R_z>=B_z. This B_z is exactly GMP's equation (22) surrogate E, whereas its stronger equation (23) surrogate is V=sum|fhat_k(T)^2-ghat_k(T)^2|. Distinguishing these two surrogates is essential.

For nonempty T let r(T) be the number of blocks touched by T and j(T)=k-r(T) the number missed. Fourier factorization of f_k=1-2 product_b(1-1_{AND_b}) gives

|fhat_k(T)|=2 epsilon 7^{j(T)}.

Consequently |c_T|>=epsilon(2*7^{j(T)}-1)>=epsilon 7^{j(T)}. For a packet, dropping the nonnegative c_T^2 log2(1+d_T^2/c_T^2) part yields

(c_T^2+d_T^2) h2(d_T^2/(c_T^2+d_T^2)) >= epsilon^2 log2(1+c_T^2/epsilon^2) >= 2 epsilon^2 j(T) log2(7).

There are 8^k Fourier indices in total. Each one of the k blocks is missed by 8^{k-1} of them, so sum_T j(T)=k8^{k-1}. Removing the empty index subtracts k. Therefore, for every k>=1,

Delta_z/I_z >= B_z/I_z >= [k/4 - 2k/8^k] log2(7).

The lower bound tends to infinity. In particular log2(7)>2 follows from 7>4, so k=9 gives the exact rational certificate Delta_z/I_z > 9/2-36/8^9 >4; no floating logarithm is needed. More generally the lower bound is linear in k. This supplies the separate calculation explicitly left open in GMP Section 5.1 for its weaker equation (22), and consequently for the true decrement (21), at the chosen variable. It does not disprove an existential good-query statement.

The true decrement grows only linearly on this family. For a binary entropy packet, h2(t)<=t log2(e/t), since -(1-t)ln(1-t)<=t. Thus B_z<=epsilon^2 sum_T log2[e(1+c_T^2/epsilon^2)]. By concavity of log and Parseval sum c_T^2=1-epsilon, averaging over 1/epsilon indices gives B_z<=epsilon log2(e/epsilon). The refund bound R_z<=4I_z follows from the nonnegative entropy series as reconstructed in the preceding stage. Hence

Delta_z/I_z <= 3k+log2(e)+4.

This establishes Theta(k) growth without a numerical asymptotic fit. The stronger V grows exponentially: V=4epsilon sum_T |c_T|, D=sum(fhat-ghat)^2=4epsilon, so V/D=sum|c_T|>=sum|fhat_k(T)|-1. The exact Fourier l1 norm is

sum|fhat_k(T)|=|1-2(7/8)^k|+2[(7/4)^k-(7/8)^k].

Therefore V/D>=2(7/4)^k-3. GMP Proposition 5.1 is correct at its stated V-versus-D scope; its stronger surrogate is exponentially more expensive than the true decrement here.

For exact compressed checks, the number of nonempty Fourier indices with j missed blocks is N_j=binom(k,j)7^{k-j}, 0<=j<k. The signed sum of sigma_T=sign(fhat_k(T)chi_T(y)) in that sector is S_j=7 binom(k-1,j)-binom(k-1,j-1), with out-of-range binomials zero. To derive it, an ordinary block has 3 even nonempty subsets and 4 odd ones, giving signed generating factor x+1, while the special last block contributes x-7; the global minus sign gives (7-x)(x+1)^{k-1}. Hence (N_j+S_j)/2 fibers have |c_T|/epsilon=2*7^j-1, and (N_j-S_j)/2 have |c_T|/epsilon=2*7^j+1. The empty coefficient is c_empty/epsilon=8^k-2*7^k-1. These integer multiplicities reproduce the entire actual packet law without enumerating a large truth table.

Terminal influence is not erased by the expensive selector. The disjoint tribes child has I(f_k)=(3k/4)(7/8)^{k-1}. Flipping y changes exactly n incident edges, of which three were originally pivotal, giving I(g_k)-I(f_k)=2epsilon(3k-6). Thus

I(F_k)=I(f_k)+epsilon(3k-5).

For k>=2 this is at least I(f_k), while epsilon/I(f_k)=1/[6k7^{k-1}]. Since log2(e)<2, the upper bound above implies Delta_z/I(F_k)<(3k+6)/[6k7^{k-1}]<=7^{1-k}. The expensive local ratio therefore has an exponentially small cost relative to the root's total influence. It cannot by itself establish failure of an amortized stopping-tree payment, even if this first query is forced.

The source representation also gives a different physical stopping tree: query the three coordinates of the last block first. Every negative branch is H=OR of the first k-1 AND blocks; the all-positive branch is G=OR of the first 3(k-1) data bits and z. Both complete terminal entropy laws must be retained. The preceding stage reconstructs a uniform bound H(F_k)<=23I(F_k) using that tree, including the k=1 degenerate case. Its proof is reused at its pending-independent-review status. The wrong first query thus has an unbounded local rate while the root retains a finite global rate. This is not a Boolean FEI counterexample.

The first unsupported universal step is selecting and paying an alternative pivot or signed child reserve after arbitrary core data exposure; the source's special shared block does not furnish such a pivot in arbitrary functions. Existing results on rarity/point switches may overlap the mechanism; no novelty is claimed for the general phenomenon.
