# Arbitrary resampling masks

Let x' agree with x outside a resampling set R and be independent on R. For one mate z, write a=2^-L, s=P[Q=0]=(1-a)^(D-1). If clause c of Q has r_c resampled leaves, then

    t=P[Q=Q'=0]=product_c (1-2a+a 2^-r_c).

The clause joint-success probability is a 2^-r_c, since the L-r_c shared leaves and two sets of r_c independent leaves must all be 1. Thus this formula covers every mask, including partial clauses and interleaving with z.

Put eta=E[zz']=1/2 if z is shared, 1/4 if z is resampled. At a mate define n=1-zQ and b=z(1-Q). Their pair moments are

    u=E[n n']=s+eta(1-2s+t),
    v=E[n b']=E[b n']=s/2-eta(s-t),
    d=E[b b']=eta t.

For a block containing L mates, let N_t=product n and B_t=product b, M_t=N_t-B_t. Independence between mates gives

    A_t=E[N_t N_t']=product u,
    C_t=E[N_t B_t']=product v,
    J_t=E[B_t B_t']=product d,
    E[N_t M_t']=E[M_t N_t']=A_t-C_t,
    E[M_t M_t']=A_t-2C_t+J_t.

Across blocks define A=product A_t, B=product(A_t-C_t), C=product(A_t-2C_t+J_t). Write P=(1-x)N+xM for the indicator that the DNF is false. Its mean is

    pbar=[alpha^(DL)+(alpha^L-beta^L)^D]/2,
    alpha=(1+s)/2, beta=s/2.

If the root is shared, E[P P']=(A+C)/2. If it is resampled, E[P P']=(A+2B+C)/4. Either sign convention for the Boolean function gives

    Corr(R)=E[f(x)f(x')]=1-4pbar+4E[P P'].

For any target coordinate i not in R, independent resampling at i kills exactly the Fourier coefficients containing i, hence

    G_i(R)=Corr(R union {i}),
    W_i(R)=Corr(R)-Corr(R union {i}).

This treats root, mate, and leaf coordinates with the same engine. At R=empty, W_i=Inf_i. Grow R by adding the coordinates in reverse reveal order. Each step contributes

    Phi(G_i(R)-G_i(R+j), W_i(R)-W_i(R+j)).

The final empty-set cell contributes Phi(G_i(all others), W_i(all others)). This includes every variable in the order; it does not merge the leaf-only cells into one cell.

`nested.py` updates just the affected clause product, mate factor, block factor, and three global products per added variable. Runtime and mask-state storage are linear in the number of variables; no truth table is used for the large rows. `decimal_audit.py` implements the same identities independently with 70-digit Decimal scalars and no NumPy product updates.
