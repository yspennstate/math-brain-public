# Exact localized odd-face ledger: ordering is essential

Units are bits. A node is strictly K-bad when B_i=H(S_i|S_-i)>K Inf_i. Its odd-face charge is I(f_i^+ f_i^-)/2; the tree charge weights it by physical reach probability.

Fixed seed: on four data bits b4(x)=(-1)^(x1*x2+x3*x4), let b4' flip b4 only at zero, let a(y,x) choose b4 or b4', and balance with a fresh sign z: b=z a. Its dimension is 6, influence i=53/16, and selector influence d=1/16. The selector erasure satisfies B_y>4d; a rigorous rational log certificate is in out/validation.json. Every coordinate of every physical restriction of b4 or b4' has erasure <=4 influence (216 exact split certificates, code/check.py).

Let g_t be t disjoint copies of b, q=2^-k, and F=1+A_k(g_t-1). Query either (CF) controls, all selectors, all four-bit data, all balancing signs, or (DF) all selectors, all four-bit data, all balancing signs, controls. For K=4, the only bad nodes in either complete tree are the selector stages. Each selector keeps the disagreement probability d=1/16; multiplication by all other factors cancels in the child product. In CF, total physical reach of each selector stage is q, with node charge 4/16. In DF, each stage has total reach one, with node charge q(k+4)/16. Consequently, for every t,k>=1,

    I(F)=q(53t/16+k),
    Q_bad,4(CF)=qt/4,              Q_bad,4(CF)/I(F)=4t/(53t+16k)<=4/53,
    Q_bad,4(DF)=qt(k+4)/16,        Q_bad,4(DF)/I(F)=t(k+4)/(53t+16k).

For t=k^2, the DF ratio diverges like k/53 while influence and minority probability vanish. CF remains paid. Four finite actual Boolean functions, dimensions 7,8,9,13, were checked in both complete trees with exact interval-classified erasure and rational influence/face charge. The infinite claim follows from the proofs in REPORT.md, not extrapolation of those cases.

General obstruction: for any fixed finite K>=0, choose an even m>=4 with m-2>K, and use the balanced seed z times the selector between bent_m and its zero flip. The selector has d=2^-m, B_y/d>=m-2>K, and I(seed)=1+m/2+(m+1)2^-m. At every selector-first stage of the designated DF tree on t activated copies, independent balancing signs ensure B_i(F)=qB_i(core), d_i(F)=qd, and odd-face charge q(m+k)d. Hence

    Q_bad,K(DF)/I(F) >= td(m+k)/(tI(seed)+k).

Taking t=k^2 and k->infinity makes this ratio unbounded for every fixed K. This refutes any dimension-independent localized odd-face payment demanded for EVERY complete physical tree, even on balanced-core activations. It does not refute existential selection of a tree or a suitable stopping rule with terminal entropy. For K>=3, CF's control nodes are good and its remaining bad charge is at most qt Q(seed), so this chosen finite seed has a paid alternative order.

Thus the C019 bridge must include an actual policy that removes rare-control face amplification before a bad data split, or prove a rebate for those faces. Replacing the existential tree quantifier by arbitrary order is impossible at every fixed threshold.
