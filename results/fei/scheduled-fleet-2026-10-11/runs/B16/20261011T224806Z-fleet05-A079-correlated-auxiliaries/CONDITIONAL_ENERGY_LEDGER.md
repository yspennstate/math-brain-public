# Bent branches with arbitrary and correlated selector phases

All inputs are independent uniform physical bits in F_2. All Fourier transforms use normalized counting measure; entropy is in bits. Spectral variables are distinct from physical inputs. No novelty or independent acceptance is asserted.

## 1. General bent-branch ledger

Let X have k bits, Y have d even bits, and let F(x,y)=g_x(y), where every g_x is bent: ghat_x(t)=2^(-d/2) sigma_t(x), sigma_t(x) in {-1,1}. Put nu_t(v)=sigmahat_t(v)^2. Direct partial Walsh expansion gives

    Fhat(v,t)=2^(-d/2) sigmahat_t(v),
    P(V=v,T=t)=2^(-d) nu_t(v).

Therefore T is uniform, and

    B_X := H(V|T)=2^(-d) sum_t H(sigma_t),
    H(F)=d+B_X,
    I_Y=d/2,
    I_X=2^(-d) sum_t I(sigma_t),
    H(T|V)=d+B_X-H(V)=d-I(V;T) <= d=2 I_Y.

The influence statement follows either by Parseval or by expanding the squared difference between neighboring branch coefficients. More explicitly, the signed phase energy is

    E_phase=(1/4) sum_i E_x sum_t (ghat_x(t)-ghat_(x+e_i)(t))^2=I_X.

The corresponding magnitude energy, with absolute values inside each difference, is zero. Also the physical assignment-to-data-spectrum channel has information zero: every physical child has the same squared Fourier law. Thus the standard shared-data mixing term M_X is zero, while its conditional phase term B_X survives.

IMPORTANT orientation: B_X=H(S_X|S_Y); the requested auxiliary remainder is H(S_Y|S_X). They are different terms. The displayed ledger retains both.

## 2. A fully Boolean realization permitting arbitrary phase rows

Write Y=(A,B), each with m bits, and prescribe ANY family h_b:{0,1}^k -> {-1,1}. Define

    F(x,a,b)=(-1)^(a dot b) h_b(x).

This is Boolean for every prescription. Sum first over a in its normalized Walsh coefficient:

    Fhat(v,s,t)
      = E_(x,a,b) [(-1)^(a dot b+s dot a+t dot b+v dot x) h_b(x)]
      = 2^(-m) (-1)^(s dot t) hhat_s(v).

In particular every branch at fixed x is bent, with Fourier signs sigma_(s,t)(x)=(-1)^(s dot t)h_s(x). The exact joint law is

    P(V=v,S=s,T=t)=2^(-2m) hhat_s(v)^2.

Its spectral T is independent of (V,S), but S and V can be dependent. The arbitrary phase prescriptions are compatible with full Booleanity; there is no omitted simultaneous phase-admission condition in this family. Hence

    H(F)=2m+E_s H(h_s),    I_Y=m,    I_X=E_s I(h_s),
    H(S_Y|S_X)=2m-I(V;S),    B_X=E_s H(h_s).

Conditional selector entropy can be paid at K I_X if FEI(K) is known for every h_s. Conversely, taking all h_s equal to an arbitrary seed g yields B_X=H(g), I_X=I(g). Therefore a uniform phase-row payment on this family already contains full FEI. The auxiliary side alone is paid, but this does not complete the joint bound.

## 3. An explicit dependent, distinct-branch control

For 1<=k<=m, take h_b(x)=(-1)^(x dot b_[k]). Then

    Fhat(v,s,t)=2^(-m) (-1)^(s dot t) 1{v=s_[k]}.

The joint spectrum is uniform on an affine graph of 2^(2m) atoms. Thus

    H(F)=2m,   H(S_X)=k,   H(S_Y|S_X)=2m-k,
    B_X=0,    I_X=k/2,    I_Y=m,    I(S_X;S_Y)=k.

Every branch g_x is distinct. Spectral dependence is explicit: S_X is a deterministic nonconstant function of S_Y. This is not independent spectral padding. With k=1 and m increasing, H(S_Y|S_X)/I_X=4m-2 diverges, whereas H(F)/I(F)=2m/(m+1/2)<2. It refutes the candidate H(S_Y|S_X)<=K E_phase for any fixed K. It also refutes any such payment using only magnitude energy, which is zero. Neither conclusion refutes auxiliary-block payment by I_Y or full FEI.

## 4. Distinct branches do not eliminate arbitrary selector seeds

Fix ANY g:{0,1}^k -> {-1,1}, k>=1, and take m>=k+1. Embed each u in {0,1}^k as a distinct B-point tag(u). Define

    h_b(x)=g(x) (-1)^(1{b=tag(x)}),
    F_m(x,a,b)=(-1)^(a dot b) h_b(x).

All physical selector branches are bent. They are pairwise distinct even modulo global sign: different x values have different exceptional B-points, and there is an untagged B-point. The construction differs from a tensor by changing branch-specific phases, not by manipulating a non-Boolean spectral relaxation.

Let g^(u) denote g with its sign flipped only at u; set delta=2^(k-m), epsilon=2^(2-m), p_g(v)=ghat(v)^2. The phase family consists of 2^m-2^k copies of g and one copy of each g^(u). Thus

    B_X=(1-delta)H(g)+2^(-m) sum_u H(g^(u)).                    (1)

Writing c=2^(1-k), the flip coefficient is

    ghat^(u)(v)=ghat(v)-c g(u)(-1)^(v dot u).

Orthogonality gives sum_u g(u)(-1)^(v dot u)=2^k ghat(v), so

    sum_u [ghat^(u)(v)^2-ghat(v)^2]=-4 ghat(v)^2+2^(2-k).

The exact marginal and selector influence are therefore

    P(S_X=v)=(1-epsilon)p_g(v)+epsilon 2^(-k),                 (2)
    I_X=I(g)+2^(1-m)(k-2I(g)).                                (3)

Equation (3) also follows directly from each physical selector edge: the exceptional phases change at exactly two B-points, giving disagreement probability alpha+(1-2alpha)2^(1-m) on an edge whose seed disagreement is alpha in {0,1}.

The marginals really are dependent for every k>=1. There is an untagged row with squared spectrum p_g, and a tagged row with a different squared spectrum. To see the latter assertion, if any old coefficient is zero it becomes nonzero after a flip. Otherwise equality of all squared coefficients before/after a flip forces ghat(v)=2^(-k)g(u)(-1)^(v dot u) for every v, contradicting Parseval (their squared sum would be 2^(-k)<1). Hence I(V;S)>0 by strict concavity of entropy.

No numerical continuity assumption is needed. Since entropy of a law on 2^k points is in [0,k],

    |B_X-H(g)| <= delta k,
    0 <= H((1-epsilon)p_g+epsilon U)-H(g) <= h2(epsilon)+epsilon k,
    0 < I(V;S) <= h2(epsilon)+(epsilon+delta)k,
    |I_X-I(g)| <= 2^(1-m) k.                                  (4)

The marginal entropy estimate follows by introducing the Bernoulli mixture label: H(q)<=h2(epsilon)+(1-epsilon)H(p_g)+epsilon k; concavity gives H(q)>=H(p_g). Equations (1)-(4) imply, for any fixed nonconstant seed,

    B_X/I_X -> H(g)/I(g) as m -> infinity.

Thus even on this family of pairwise distinct bent branches with genuinely dependent spectral marginals, a finite uniform conditional selector payment B_X<=K I_X would imply FEI(K) for ALL seeds. FEI(K) conversely pays every phase row and hence B_X. Branch distinctness is not a noncircular phase-payment hypothesis.

There is no FEI counterexample here. Because m>=k+1, the full family has H(F)<=2m+k<3m and I(F)>=m, so H(F)/I(F)<3 uniformly. The arbitrary-seed guard concerns B_X/I_X, not the full H/I after its data energy is included.

## 5. Exact remaining obligation

First unsupported completion: infer a dimension-free bound for E_s H(h_s) from E_s I(h_s), using only the Boolean realization and common flat data magnitudes. The realization above allows arbitrary Boolean h_s, and its distinct-branch limit still admits every seed. That completion is full-FEI difficulty.

A noncircular next action is to demand an explicit restriction-stable condition on the entire family of phase rows, specify which independent-seed and rare-tag embeddings it excludes, and then check a proposed nonreusing physical stopping payment. Merely bounding a marginal phase law or requiring distinct branches does not state such a condition.
