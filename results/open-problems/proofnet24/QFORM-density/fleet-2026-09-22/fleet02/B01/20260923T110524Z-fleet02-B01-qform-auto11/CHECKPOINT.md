# fleet02/B01 early mathematical checkpoint

Programme: QFORM-DENSITY-3EIG-20260922
Run: 20260923T110524Z-fleet02-B01-qform-auto11
Status: substantive partial derivation; full QFORM open.

## Binary product small-ball endpoint

Let X,Y be independent real random variables with probability densities bounded by one, and

q(x,y)=a x^2+2bxy+c y^2+ux+vy+w.

Put H=[[a,b],[b,c]] and

m(H)=max(|a|,|c|,|b|/2).

For every s in R and rho>0,

P(|q(X,Y)-s|<=rho) <= 2 sqrt(2) m(H)^(-1/2) sqrt(rho).

Proof: conditioning on Y and completing the square in X gives the bound 2 sqrt(2rho/|a|) when a!=0; conditioning on X gives the analogous c-bound. For the mixed term, fix eta>0 and split according to |partial_y q|=|2bX+2cY+v|<=eta. Given Y, this event restricts X to an interval of length eta/|b|, hence has probability <=eta/|b|. On its complement, for each fixed X the quadratic function of Y has at most two monotone branches; on each branch the set |q-s|<=rho has length <=2rho/eta. Therefore

P(|q-s|<=rho) <= eta/|b|+4rho/eta.

Choosing eta=2 sqrt(rho |b|) gives 4 sqrt(rho/|b|). Taking the best of the a,c,b bounds yields the displayed estimate exactly.

## Indefinite L2 plan

Assume det H<0, set D=|det H| and kappa=sigma_min(H)>0. For an independent copy (X',Y'), the difference S=q(X,Y)-q(X',Y') has the first-copy block H as an invertible indefinite physical pair and Schur remainder -q(X',Y'). The completed pair theorem from the required decoupling/Brascamp-Lieb source gives

||p_S||_infinity <= 4 sqrt(2H0) (D kappa)^(-1/4),

with H0=2 sqrt(2) m(H)^(-1/2), hence

||p_S||_infinity <= 2^(13/4) (m(H) D kappa)^(-1/4).

If mu=law(q), then law(S)=mu*mu_tilde. Convolving mu with an L2 approximate identity k_epsilon and using the bounded density of mu*mu_tilde gives

||mu*k_epsilon||_2^2 <= ||p_S||_infinity.

Weak L2 compactness therefore yields an L2 density p_q with

||p_q||_2 <= 2^(13/8) (m(H) D kappa)^(-1/8).

This is an integrated-frequency replacement for a genuinely mixed indefinite two-coordinate kernel. It uses original-coordinate product structure and does not diagonalize H. The next step is to combine it by L2 x L2 in time with the designated partner fleet03/B01 rank-two cross-bicore L2 bound.