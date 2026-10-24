# The cutoff envelope still has a logarithmically unbounded influence price

This is a quantitative stress test of the exact source-versioned A046
envelope, not another test of the already-refuted unfiltered rule. The
separator length here is STRICTLY ABOVE the cutoff, so its early layers
have zero reserve drift. Only the final m layers enter V.

For each integer h>=2 let

    w=2^h-2, m=h+2, s=2m, L=4m, R=T=w, g=z.

These specify actual Boolean signs on n=6m+2w+1 fair bits. The source
cutoff is exactly ceil(log2(w+2))+2=m. Write

    alpha=2^-2m, q=2^-w, eta=alpha^2 q^2,
    e=2q-(1+alpha^2)q^2,
    JB=(4m+2w)alpha^2 q^2, JC=2wq(1-q), JD=JB+JC.

Because g=z, I(g)=1, H(g)=0. All terminal costs are retained; their
entropy is exactly zero here, and their influence is pi=eta+alpha e.
The exact accounts in the independently reviewed source theorem give

    I_h=2m alpha e+(1-alpha)JB+alpha JC+eta+alpha e,
    V_h=alpha[m JD+e m(m-1)/2+m e].

These formulas come from physical edge counting and a finite reached-
layer sum, so they apply in every dimension without a search limit.

## All-integer divergence certificate

For h>=4, 2m<=w, and w>=2. Since q<=1/4, e<=2q, and
e>=q,

    (3/4)w <= JC/e <= w.

For the upper bound, cancel q and use
2(1-q)<=2-(1+alpha^2)q. The lower bound follows from e<=2q.
Also

    [(1-alpha)JB+eta]/(alpha e)
       <=(4m+2w+1)alpha q
       <=(4w+1)alpha q <1.

The last step uses w 2^-w<=1/2, q<=1/4 and alpha<=1/256.
Therefore

    I_h/(alpha e)<2m+w+2<=3w,
    V_h>=alpha m JC>=(3/4)alpha e m w,
    V_h/I_h>=m/4=(h+2)/4.                         (1)

For any finite K, choose an integer h>=4 with h+2>4K. This actual
Boolean family then refutes the specifically defined rule V_s<=K I(F).
It does not say Q_bad exceeds K I. Most eligible envelope layers could
be good, so the inequality Q_bad<=V cannot be reversed.

## Exact asymptotic coefficient

Here q->0, alpha->0 and m/w->0. Direct cancellation gives

    JC/(e w)=(1-q)/(1-(1+alpha^2)q/2) -> 1,
    JB/(alpha e w) -> 0, eta/(alpha e w) -> 0.

Thus

    I_h/(alpha e w) -> 1,
    V_h/(alpha e m w)
      =JD/(e w)+(m-1)/(2w)+1/w -> 1.

Consequently

    V_h/I_h ~ m=h+2 ~ log2(w),
    V_h/(m I_h) -> 1.                              (2)

Unlike A025's earlier fixed R=T=1, unfiltered all-s counterfamily, this
one has s=2m, a genuine zero-drift prefix, and only the last m charges.
The problem is the growth of that cutoff as w increases. No larger fixed
constant repairs this particular envelope. An improvement must exploit
the actual row coefficients/badness or a different remaining reserve.

## Physical coordinates which exhaust the account

The same issue is visible without summing the full influence. Each U
coordinate has actual influence u_h=(1-alpha)eta+alpha q(1-q) and
envelope debit b_h=m alpha[eta+q(1-q)]. Hence b_h/u_h~m. The single
core coordinate z has actual influence pi and debit m alpha e, whose
ratio is m/[1+eta/(alpha e)]~m. The final separator coordinate has
actual influence alpha e and is included as a remaining coordinate in
exactly m-1 eligible face costs, so its debit/influence ratio is EXACTLY
m-1. Thus replacing the total account by per-coordinate ownership does
not remove the growth: the envelope repeatedly requests the same actual
physical influence capacities, despite distinct first-revealed faces and
zero expected early drift.

All these statements concern envelope requests. Filtering actual good
nodes could delete every such request; no contrary badness is assumed.

## Certificates and limitations

out/ENVELOPE_OBSTRUCTION.json records six exact rational controls,
h in {2,3,4,6,8,10}, up to an actual formula family dimension 2117.
There are no 2117-bit truth tables or floating spectral searches: exact
factorized edge accounts evaluate the displayed formulas. The 168
rational assertions pass, including 42 original envelope checks and
126 finer owner checks, with (1) on the frozen h>=4 cases.
Equations (1)-(2) are the separate all-h proof; finite ratios are checks.
No growing actual localized bill, positive universal KL price, or
unbounded H/I is established. Full FEI remains open.
