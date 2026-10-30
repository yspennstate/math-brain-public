# Root-only norm admission cannot be frozen through data exposure

This is an application of A078's credited rare bent/spike query, not a new FEI counterexample or a refutation of an aggregate stopping price.

For even k>=4 let N=2^k, r=k/2, p=2^-r, b_k a tensor of k/2 quadratic two-bit signs, with b_k(0)=1 and all shared Fourier coefficients of magnitude N^-1/2. Let S be k shared bits, x one private bit, and Y r private controls disjoint from S,x,z. Define actual Boolean cores

    G(S,x)=1-2*1_{S=0,x=0},
    H(S,Y)=1+1_{Y=0}(b_k(S)-1),
    F=G if z=0, H if z=1.

Root conditional-private-mean profiles satisfy

    ||E_x G||_Fourier,1 = 2-2/N <2,
    ||E_Y H||_Fourier,1 = 1-p+p sqrt(N) =2-p <2.

For the second equality the constant coefficient is positive 1-p+p/sqrt(N), and the other N-1 coefficients have magnitude p/sqrt(N). This is exact; no hypothetical distribution is used. Thus root-only admission with L=2 holds in arbitrarily large shared dimension.

The physical data path exposing Y=0, of probability p, leaves the actual A078 pair G(S,x), H=b_k(S). Querying x at that reached node has Inf_x(F)=1/(2N). Writing a=1/N and b=1/sqrt(N), its exact signed collision correction is

    D_k=(N-1)S(-a,a;b)+S(1-a,a;b),

with S defined in GENERAL_PROFILE_RESERVE.md. A078 PROOF.md (3)-(4) proves D_k/Inf_x(F)>=k-4. Independently: Phi(p,q)>=q log2(p/q) gives S(-a,a;b)>=(a^2/2)log2(N-1)-a^2. The empty row is at least -a^2(k+3/4), using Phi(P,a^2)<=a^2 log2(e/a^2), P+a^2<=1 and 1/ln2<3/2. Therefore

    D_k/Inf_x(F)>=(1-1/N)log2(N-1)-2(1-1/N)-(2k+3/2)/N
                    >=k-3-(3k-3/2)/N >=k-4.

Here log2(N-1)>=k-1 and 3k/2^k<=1 for k>=4. This proves that no finite absolute pointwise collision price can follow from ROOT-only profile norm <=2 while freezing that price through arbitrary later private exposure. In particular k=14 already contradicts the literal 4L_root=8 pointwise price.

The activated leaf has ||b_k||_Fourier,1=sqrt(N), so it fails the hereditary slice hypothesis. This is exactly why our theorem requires every private-fixed slice, not merely the root conditional means. Reach probability p is retained: the expected bad-node cost is pD_k, and shared/control/core resources remain in the parent. No failure of a total-tree influence budget, no absence of a selected paid pivot, and no unbounded H/I are claimed. The source k-dependent rare-query obstruction is A078's; the additional result here isolates the distinction between root admission and a valid adaptive hypothesis.
