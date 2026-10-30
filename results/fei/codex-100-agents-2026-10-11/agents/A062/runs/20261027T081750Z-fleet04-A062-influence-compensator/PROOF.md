# Affine choice cannot reduce this original product-reference bill

All logarithms are base two. This is an obstruction to a proposed source supplier, not a counterexample to FEI. The budget throughout is the influence in the ORIGINAL physical coordinates.

For an integer m>=8 put d=2^(1-m), L=floor(1/(md)), N=mL, and u=2^(1-N). Let g be the m-bit sign which is negative only at zero. On L disjoint blocks let F be the product of copies of g. Flip F at its zero vertex to obtain f. For any invertible affine change x=Ay+b over F_2^N, write f_A,b(y)=f(Ay+b). Let P_A,b be its squared Fourier law and Q_A,b the product of its OWN actual spectral marginals. Then

    min_(A,b) KL(P_A,b || Q_A,b)
       = N h2(d-u) - H(f)
       > (7/8)(m-1) - 69/16.

In particular the minimum divided by ORIGINAL I(f) is greater than (14m-83)/17, and tends to infinity. The original coordinate basis attains this minimum. Each f has full Fourier support, has no nontrivial affine sign-product decomposition, and satisfies 7/8<I(f)<17/16 and H(f)<69/16.

## 1. Exact directional influence

For nonzero v in F_2^N define D_f(v)=Pr_x[f(x)!=f(x+v)]. Let t be the number of blocks where v is nonzero; 1<=t<=L. In one touched block, g(x)g(x+v) has mean 1-2d, since exactly two vertices disagree. Independence between blocks gives

    D_F(v) = (1-(1-2d)^t)/2.

Only x=0 and x=v change the derivative after the flip. At these two vertices the old sign product is F(0)F(v)=(-1)^t. Therefore, EXACTLY,

    D_f(v) = (1-(1-2d)^t)/2 + (-1)^t u.       (1)

This is a finite counting identity, uniform in every nonzero v. Put a=d-u. Since 0<d<1/2 and u<d, (1) gives

    a <= D_f(v) <= 1/2+u <= 1-a.             (2)

The lower bound uses (1-2d)^t<=1-2d, valid because t>=1. The upper bound uses (1-2d)^t>=0, and the last inequality uses d<=1/2. Equality D_f(v)=a holds whenever v touches exactly one block, in particular on every original coordinate vector. Hence I(f)=Na exactly.

Binary entropy is concave on [0,1] and symmetric about 1/2. Its minimum on [a,1-a] is h2(a). Thus every nonzero directional influence satisfies h2(D_f(v))>=h2(a). No assumption that D_f(v)<=1/2 is needed.

## 2. Every affine basis is covered

The columns v_j=Ae_j of an invertible A are nonzero. Translation b has no effect on the uniform derivative count, so Inf_j(f_A,b)=D_f(v_j). Fourier coefficients under an affine input bijection are permuted with possible signs; H(f_A,b)=H(f). For ANY finite subset law P, KL to its actual marginal product is sum_j h2(P(j in S))-H(P). Apply this identity and (2):

    KL(P_A,b||Q_A,b)
       = sum_j h2(D_f(v_j))-H(f)
       >= N h2(a)-H(f).

Taking A=Id attains equality. This proves the minimum over ALL affine bijections without enumerating bases. Full support also means all reference marginals lie strictly between zero and one. The KL identity remains valid with deterministic marginals in general by restricting to the support.

Multiplying the transformed Boolean function by any Walsh character merely translates the Fourier law, complements selected marginals, and leaves this TC unchanged. Thus adding an arbitrary character phase does not repair the supplier either.

## 3. Uniform original budget and entropy estimates

The estimates from stage21 are repeated here to expose every asymptotic step. The point sign has p(0)=(1-d)^2 and p(S)=d^2 for nonempty S, so each original influence is d. With e=2d-d^2, its entropy is h2(e)+e log2(2^m-1). The elementary bound h2(e)<=e log2(1/e)+e log2(euler), log2(euler)<3/2, and d<=e<=2d give H(g)<=2d(2m+1). Since md<=1/16 for m>=8 and L=floor(1/(md)),

    15/16 <= N d <=1,
    H(F)=L H(g)<=4+2/m<=17/4.

Here L>=16 and N>=128. Since N>=32, Nu<1/16: it is true at 32 and decreases thereafter. Thus Na>7/8 and Na<=1<17/16. Also u<d because N>m. Therefore 0<a<=d and

    N h2(a) >= Na log2(1/a) >= Na(m-1) > (7/8)(m-1).  (3)

For completeness, the flip changes the Fourier coefficient vector in Euclidean norm by 2*2^(-N/2). Cauchy-Schwarz gives squared-spectrum total variation at most eta=2^(1-N/2). Maximal coupling of two distributions on 2^N atoms gives entropy change <=h2(eta)+eta log2(2^N-1), since this bound increases up to eta here. It is <=eta(3N/2+1/2), using log2(euler)<3/2. At N=32 this is (97/2)*2^-15<1/16. For all integral N>=32 the ratio between successive bounds is (3N/2+2)/((3N/2+1/2)*sqrt(2))<1, since ((3N/2+2)/(3N/2+1/2))<=100/97<sqrt(2). This covers odd N as well. Hence H(f)<17/4+1/16=69/16.

Combine (3) with H(f)<69/16. The lower bound is positive for m>=8. Dividing by I(f)<17/16 gives KL/I(f)>(14m-83)/17 uniformly in (A,b). No exchange of limits, optional stopping theorem, or infinite-dimensional random object occurs: each m specifies one finite Boolean function, and the explicit lower bound diverges as m grows.

## 4. Structural side conditions and scope

F has an even number of negative vertices because it is a product on at least two nonempty blocks; its one-point flip f has an odd number. A product on r,s>=1 coordinates with factor negative counts c,e has negative count c*2^s+e*2^r-2ce, which is even. An affine bijection preserves the negative count, so no transformed f factors across a nontrivial partition. Since N>=2, multiplying f by a nontrivial character toggles 2^(N-1) signs, an even number. Every Walsh numerator is consequently 2 modulo 4 and is nonzero. This proves full support after every affine bijection too. Constant and anti-period directions are excluded by the same parity count.

This statement does NOT assert unbounded KL divided by transformed I(f_A,b): a basis change can increase physical influence and that increase is not a free original budget. It also does not refute a nonproduct reference, a mixture of affine product references, or a selected stopping rule which does not require the stated initial KL capital. It preserves full terminal entropy and all previous debits rather than discarding them. The history transport identities of A065/A087 remain conditional on supplying the original owner and are not re-proved here.

## 5. A nonproduct reference pays this same family

There is a concrete repair for this family, and it makes the scope of the obstruction sharper. Let Q be the squared spectrum of the UNFLIPPED product F, in the original coordinates. It is explicitly the product over blocks of the known point-sign spectral law; within each block it is not a product over individual spectral bits. Its least atom is d^(2L), since d<=1-d, so its largest code length is 2L(m-1)<=2N. It has full support. It does not require computing H(f) or assuming FEI to define it.

The following elementary finite-reference lemma applies to any two Boolean functions F,f differing on an epsilon fraction of the truth table. If Q=Fhat^2 has full support, its code lengths lie in [0,M], and eta=2 sqrt(epsilon), then

    H(f)+KL(fhat^2||Q) = CE(fhat^2,Q) <= H(F)+eta M.   (4)

Indeed Parseval and Cauchy-Schwarz give TV(fhat^2,Fhat^2)<=eta. The expectation of a function in [0,M] changes by at most M times TV (split the positive and negative parts of the signed difference). Taking that function to be -log2 Q proves (4). No entropy-continuity theorem, product-source hypothesis, or restriction invariance is required. Full support and the bound on ALL code lengths are necessary side conditions for this argument; tiny or zero reference atoms cannot be ignored.

Here epsilon=2^-N and M<=2N. Hence

    CE(fhat^2,Q) <= 17/4 + 2N*2^(1-N/2) < 69/16 < 5 I(f).  (5)

At N=32, 2N*2^(1-N/2)=64*2^-15<1/16. The successive ratio is (N+1)/(N sqrt(2))<1 for N>=32, so the strict bound holds for our N>=128, including odd N. The last inequality uses I(f)>7/8, since 69/16<5*(7/8).

Thus the FULL initial entropy-plus-KL owner is paid at rate five on the SAME original function that defeats every affine actual-marginal product reference. Initial full H has not been discarded. One may now use the established finite physical-kernel KL telescope, retaining its signed E/O correction when representations are changed; (5) does not authorize a free replacement by product marginals or repeated fresh installations. With the one globally inherited Q and no installations, the already established entropy and KL telescopes give E[H_terminal+K_terminal]+E sum(D_entropy+E_erasure+O_outcome)=CE_initial<5 I(f), for every finite fair fresh-coordinate tree. This is a consequence of the paid initial source, not a new optional-stopping argument. There is no assertion of uniform integrability across changing dimensions.

The first unsupported universal line is an influence-priced ORIGINAL nonproduct complete reference (or a necessary selected policy avoiding this product admission) for an ARBITRARY Boolean core, retaining old debits, signed erasure/outcome terms, and both full terminal bills. Formula (4) supplies such an owner only when an explicit full-support template already has paid entropy and controlled maximum code length. No theorem supplies that template for every core. The affine marginal-product alternative is excluded for this family, while (5) demonstrates that a structured nonproduct source can pay it.
