# Released occupancy credit cannot pay every reset at a fixed rate

This changes the attempted mechanism after its successful exact fixture: root occupancy credit and occupancy KL **released by this particular physical erasure** are distinct. The latter fails to pay the original product Bayes reset at any universal multiplicative rate. This is a new source-compatible release obstruction, not the already retired Gamma<=constant*influence test.

Use A038's actual ancestor u=(-1,-1,-1,+1), expose essential u0=0, and replace its independent remaining core by v_n=1-2*1_zero on n fresh data bits. The reached u is -1, with no variance. All controls and data coordinates are uniform and independent. Query private a in the opposite-orientation gate. Put e=2^-n, m=(1+Ev_n)/2=1-e, L=n+1, v=1-m^2/4. Every n>=16 is an actual Boolean function of n+3 relevant reached coordinates, with the same essential exposure provenance as the audited fixture.

At the reached root, coefficients at empty and {x} have squared mass m^2/4, those at {a} and {x,a} have mass 1/4, and all other nonzero coefficients have a=0. Erasing a gives equal residual masses q_empty=q_{x}=(1+m^2)/4, conditional queried-bit probability p=1/(1+m^2) on both exceptional fibers, and total mass W=(1-m^2)/2 on all other fibers. On those other fibers the queried spectral a bit is deterministically zero. All physical influences are d_x=d_a=1/2 and d_b=d_data=e/2. Therefore the canonical completed occupancy reference has

    r_x=r_a=1/(2v),  r_b=r_data=e/(2v),
    1-c=(1-c/(2v))^2*(1-ce/(2v))^L.

There is one unique positive root c in (0,1), by strict concavity of g(c)=1-c-product and g'(0)>0, g(1)<0. Set t=c/(2v), s=(1-ce/(2v))^L. Its conditional reference a-probability is t on every nonempty residual fiber. At the empty residual fiber it is b0=h/(m^2/4+h), h=(1-t)s/2=(1-c)/(2(1-t)). Thus the exact KL released by erasing a is

    E_n=q_empty D_2(Ber(p)||Ber(b0))
       +q_{x} D_2(Ber(p)||Ber(t))
       +W log2(1/(1-t)).                                    (1)

This formula has no dependence on how the nonempty data Fourier masses are split beyond their total. It comes from conditional KL of the actual queried spectral bit given the residual set, not an entropy decrement or a new projection reset.

## Explicit all-n root and release bound

At c=v, g(v)=[m^2-(1-e/2)^L]/4. For n>=4, L>=5, and Taylor's second-order upper bound gives (1-e/2)^L<=(1-e/2)^5<=1-(5/2)e+(5/2)e^2<m^2=1-2e+e^2. Hence g(v)>0 and c>v. Bernoulli's lower bound gives g(v)<=Le/8.

For c>=v, write r=1/(2v)<=2/3, z=1-ce/(2v). Differentiation gives

    g'(c)=-1+2r(1-cr)z^L+L(e/(2v))(1-cr)^2 z^(L-1)
          <=-1/3+Le/6<=-1/4,

because 1-cr<=1/2 and Le<=1/2 for n>=16. By the mean value theorem, delta=c-v<=4g(v)<=Le/2. Consequently

    1/2<t<=1/2+Le/3,
    1/2<=p<=1/2+e.

Also h=m^2/4+delta(1-2v)/(v-delta), so b0<=1/2. For n>=16, delta<=1/16, v-delta>=11/16 and m^2/4>=1/5. It follows that

    |b0-1/2|<=|h-m^2/4|/[2(m^2/4)]<4delta<=2Le.

Thus t,b0 lie in [1/4,3/4], |p-t|<=Le and |p-b0|<=3Le. The Bernoulli KL chi-square upper bound, from ln x<=x-1, is

    D_2(Ber(p)||Ber(z))<=(p-z)^2/[z(1-z)ln2]
                       <=16(p-z)^2  (z in [1/4,3/4]),

using ln2>1/2. Since q_empty=q_x<=1/2, W<=e and log2(1/(1-t))<=2, (1) gives E_n<=2e+80L^2 e^2. For n>=16, L^2e<=289/65536<1/80; this expression decreases with n, since (L+1)^2/(2L^2)<1. Therefore

    0<E_n<=3e.                                               (2)

## Reset lower bound and unbounded ratio

The original residual-product reference predicts fair outcomes exactly, as in the source's arbitrary-v proof; the owned rarity release is zero. Its reset is rho=JS-Gamma. Here Gamma=1-h2(e/2), A=(1+m)^2/4, B=e^2/4, and JS=A+B-phi(A,B). Hence

    rho=h2(e/2)-e+e^2/2-phi(A,B).

Because A+B<=1 and phi(A,B)<=B log2(euler_e/B), with log2(euler_e)<2, one has phi(A,B)<=e^2(n+2)/2. Also h2(e/2)>=(e/2)(n+1). Since (n+2)e<=1 for n>=16,

    rho_n >= e(n-2)/2,
    rho_n/E_n >= (n-2)/6 -> infinity.                        (3)

Thus no finite constant C can make rho_n<=C E_n for every actual exposed priority gate. In particular, the fixture's release-paid reset cannot be extended to all remaining biases. This says nothing against full FEI, against the availability of other retained root credit, or against a price that also charges physical influence/core slack. Root occupancy KL may remain large; the child inherited reference debts in the exact telescope are not available for a second simultaneous withdrawal.

The true terminal spectra remain those of the children, of equal entropy H(1-2*1_zero on n+2 bits), with their heavy Fourier atom swapped between empty and {x}. Their influence is retained. The proof uses no census extrapolation or unproved entropy/influence constant. Frozen exact n=16,24,32,64 enclosures corroborate (2)-(3); the displayed analytic proof establishes all n>=16.

## Actual projection conversion also needs an additional debit

The obstruction is not merely that rho was defined using a different reference. Let A_n be the original weighted occupancy KL, O_occ,n its actual Bayes outcome KL, and sigma_occ,n the reset into the two actual child product projections. The exact ledger in PROOF (3) gives

    A_n-O_occ,n-average TC(child)=E_n-sigma_occ,n.

Root product KL is TC_root=A_n+Delta_n, Delta_n>=0 by its exact projection Pythagorean identity. The compensated physical TC formula with d_a=1/2 and original-product outcome KL zero gives

    E_n-sigma_occ,n=1-B_a-rho_n-Delta_n-O_occ,n
                  <=1-B_a-rho_n.

Here B_a=((1+m^2)/2)h2(1/(1+m^2)). Binary entropy lies above the chord h2(p)>=2(1-p) on p>=1/2, so B_a>=m^2 and 1-B_a<=2e. Applying (3) proves, for every n>=16,

    A_n-O_occ,n-average TC(child)
        <=-((n-6)/2)e<0.                                  (4)

Equivalently sigma_occ,n-E_n>=((n-6)/2)e. Even the original occupancy bank itself, not just its released part, is insufficient for its outcome mismatch plus the newly projected complete child product KL at this physical step. The missing positive debit is explicit. Since E_n<=3e, sigma_occ,n/E_n>=(n-6)/6 as well. This does not deny retaining the inherited Bayes child references; it rules out resetting them to their product projections without a separate owned payment. The successful two-bit source fixture has the opposite, strictly positive margin, so this is a precise boundary for the proposed projection monotonicity.

The finite certificate independently computes the moment-only root occupancy A_n, both actual child product KLs and the exact Bayes outcome law. It never replaces a child terminal by its root projection. Equation (4) follows analytically from the existing compensated identity and the entropy chord, rather than from finite observed growth.
