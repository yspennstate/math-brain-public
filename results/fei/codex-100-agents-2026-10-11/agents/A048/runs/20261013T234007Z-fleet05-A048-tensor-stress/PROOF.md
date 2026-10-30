# Actual terminal spectral labels can inject adaptive schedule information

All entropies are in bits. The cube is uniform. Coordinates keep their original ambient labels throughout.

## Family and physical tree

For integers r>=1 and k>=2 let h_k=1-2*1_{all k bits are 1}. On disjoint k-bit blocks x_j and fresh coordinates y_a indexed by a in {0,1}^r, set

    F(x,y) = (product_{j=1}^r h_k(x_j)) (product_{a in {0,1}^r} y_a).

Put m=2^r and d=2^{1-k}. First query x_{j,1}, j=1,...,r, and record the r-bit history B. Then query y_B, record its fair outcome C, and stop. Thus Pi=(B,C), with its coordinate labels implicit in B. Every query is essential at its actual node: the next untouched defect has first-coordinate influence d>0, and each parity coordinate has influence 1. Every coordinate of F is essential. The tree is a partial stopping tree; its terminal function is retained, not discarded.

The tensor identities give

    I(F)=m+rkd, H(F)=r H(h_k).
    R:=I(F)-E I(F_leaf)=1+rd.
    E I(F_leaf)=m-1+r(k-1)d.
    E H(F_leaf)=r H(h_{k-1})/2.

For a block, half the first-bit restrictions are constant and half are h_{k-1}. The parity remainder has m-1>=1 coordinates and entropy zero. It makes the output Y conditionally fair at every leaf. Therefore o=I(Y;Pi)=0, H(Pi|Y)=r+1. Terminal influence can be large; this is not a counterexample to a whole-function influence budget or to FEI.

## Coherent root lift and actual descendant witness

Let S0 have the root Fourier-square law. At a query i, put T=S\{i}, q_T=P(S=T)+P(S=T union {i}); choose b with probability childhat_b(T)^2/(2q_T), then retain T. Parseval makes the transcript physical and each conditional descendant law exactly its actual Fourier-square law. Hence S_leaf=S0\Q(Pi), where Q is the set of coordinates queried along the realized history.

For one defect prefix, put p=2^{-(k-1)}, v=4p(1-p), and

    j_k = h2(v/2)-h2(v)/2.

The inactive child has empty spectrum; the active child is h_{k-1}, with nonempty spectral mass v. The channel information is the displayed j_k. Independent blocks give I(S0;B)=r j_k. The final parity query changes only signs of coefficients, not their squares, so its spectral channel information is zero. Thus

    I(S0;Pi)=r j_k.

Now use W=S_leaf itself as witness, with its original coordinate labels. This is a normalized actual terminal Fourier draw in every leaf, not an arbitrary extra copy of the transcript. The parity part of S0 is the deterministic full set of m data labels. Consequently the parity part of W is exactly that full set minus y_B. Its missing label recovers B. The spectral law does not depend on C. Therefore

    I(W;Pi)=r, H(Pi|W)=1,
    Gamma_W:=H(Pi|Y)-H(Pi|W)=r,
    o/2+[Gamma_W]_+/2=r/2.

Given S0, the selector part of W is its deterministic projection off the r fixed first coordinates, while its parity part encodes B injectively. Since C carries no information about S0,B,W,

    I(W;Pi|S0)=H(W|S0)=H(B|S0)=r(1-j_k).

This is precisely the failure of W->S0->Pi. It is not a failure of A047's theorem, which explicitly requires that Markov chain. Taking a root-conditional copy P(W|S0) and then running the tree gives a different joint law than the actual W above.

## Finite and all-dimensional obstruction

For r=4,k=10, n=56 and R=129/128, the actual conversion is 2. The uniform root-compatible allowance is R/ln2<3R/2=387/256<2. The strict elementary bound ln2>2/3 follows from ln2=2 sum_{j>=0}(1/3)^{2j+1}/(2j+1). This is a rational certificate that the root-compatible allowance cannot be applied unchanged to an actual descendant witness just because its marginal is a genuine leaf Fourier law.

For the infinite family k=2r+2, R=1+r*2^{-2r-1}->1, but Gamma_W/2=r/2. Hence there is no dimension-independent K with this conversion <=K R for all such actual terminal witnesses. The growing parity factor carries m-1 terminal influence. Its root spectral entropy is zero, yet adaptive removal of one coordinate manufactures r bits of label information. It is independent of the defect factors and is actively queried, not a dummy coordinate.

For disjoint t-fold tensor products of the function and this tree, all the complete-joint entropy, channel, injection, and influence quantities add: R_t=tR, Gamma_t=t Gamma, and injection_t=t r(1-j_k). There is no extra logarithm from tensoring a fixed complete normalized law. The logarithm here is log2(m)=r bits carried by an adaptively selected missing label.

## Exact guard and repair boundary

For any finite coherent singleton tree with ambient retained set W=S0\Q(Pi), W is deterministic given S0 and Pi. Thus

    I(W;Pi|S0)=H(W|S0)<=H(Q|S0),
    I(W;Pi)<=I(S0;Pi)+H(Q|S0).

The second inequality follows from I(W;Pi)<=I(S0,W;Pi). Our family saturates the first bound: Q has fixed defect coordinates and one parity label indexed by B, so H(Q|S0)=r(1-j_k). A fixed final query set makes W a deterministic projection of S0 and restores the required Markov property. History-dependent ordering alone is harmless if the final query set stays fixed. Branch-dependent relabeling can make all parity remainders look the same, but any decoder recovering ambient labels needs the removed-label schedule; that cost cannot be silently deleted.

Combining this guard with the scoped uniform A047 bound gives the valid extension

    o/2+[Gamma_W]_+/2 <= R/ln2 + H(Q|S0)/2.

This is an accounting guard, not a payment of the added term. The first unsupported universal line is: the same normalized witness reference pays H(Q|S0)/2, signed erasure and terminal Fourier entropy using nonduplicated physical influence.

## Partial independent reconstruction of A047 v1

The main scoped conversion, excluding its additional rare-output sharpness certificates, reconstructs as follows. The coherent kernel depends on S0 only through the current retained set and history; the information chain rule therefore gives I(S0;Pi)=sum_v w_v J_v. A single root append Z satisfies Z->S0->Pi, giving j_Z<=I(S0;Pi). Physical product independence gives I(X_i;Y|history)<=H(Y|X_-i,history)=h2(p_i)Inf_i<=Inf_i, so o<=R. The identity Gamma_Z=j_Z-o proves the combined payment max(o,j_Z)/2.

For the uniform local bound, with actual child amplitudes G,H in each retained-frequency fiber, q=(|G|^2+|H|^2)/2. The natural-unit mixture information is at most (|G|-|H|)^2/2. To check the scalar inequality, scale the smaller magnitude to 1 and put t>=1. Twice the difference is

    F(t)=(t^2+1)ln((t^2+1)/2)-2t^2 ln t+(t-1)^2.

F(1)=0 and F'(t)>=0 follows from ln(2t^2/(t^2+1))<=1-1/t; the difference has derivative (t-1)^2/[t^2(t^2+1)]>=0. Zero magnitudes follow by continuity. Parseval and (|G|-|H|)^2<=(G-H)^2 then give J_v<=2 Inf_i/ln2, and summing gives the scoped allowance R/ln2. The full nonuniform constant follows from ln u<=u-1 and weighted Cauchy: the fiber information <=p(1-p)(G^2-H^2)^2/q<=(G-H)^2, so J_v<=4 Inf_i/ln2. This verifies the main conversion at its stated scope; it does not accept the unreviewed bank-supply/reset line or independently audit all ancillary claims in A047's bundled statement.
