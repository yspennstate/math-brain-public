# Shifted empty-row transport after one majority query

All physical inputs are independent uniform signs, entropy is in bits, and
all trees are finite adaptive physical-coordinate restriction trees. Put
Phi(p,q)=(p+q)h2(q/(p+q)), continuously extended at zero. Write B_i(G)
for H(S_i|S_-i), not the independent marginal entropy. Let G be any Boolean
core, mu=E G, a=Ghat({i}), d=Inf_i(G). Define the two actual majority3
children

W_+(x,y)=(1+x)/2+(1-x)G(y)/2,
W_-(x,y)=-(1-x)/2+(1+x)G(y)/2.

These are OR and AND in the sign convention; they arise by fixing one of
the two outer signs of Maj3(x1,x2,G).

## 1. Exact shifted row and sharp influence price

For either wrapper, every nonempty residual-core Fourier row is copied
twice at amplitude 1/2. Its summed erasure is one half the corresponding
core row. At the empty residual-core row the paired amplitudes, up to
signs and interchange, are (1+mu,a)/2 and (1-mu,a)/2. Therefore exactly

B_i(W_+)=B_i(W_-)=B_i(G)/2+D(mu,a),                         (1)
D(mu,a)=[Phi((1+mu)^2,a^2)+Phi((1-mu)^2,a^2)]/4
         -Phi(mu^2,a^2)/2.                               (2)

No balanced-child assumption is made. The negative subtraction is the
core empty row, not an independently reusable credit.

The elementary homogeneous entropy bound Phi(u^2,v^2)<=2|uv| implies

-|mu a| <= D(mu,a) <= |a|, hence |D(mu,a)|<=d.              (3)

Indeed, the shifted positive sum is at most
|a|(|1+mu|+|1-mu|)/2=|a|; the negative term is at least
-|mu a|. Finally |a|<=d follows by averaging the physical half-difference
of G, whose absolute value is exactly the pivotal indicator. The upper
coefficient 1 is sharp: G(y)=y_i gives mu=0,a=d=1,D=1.

For a self-contained scalar proof, assume 0<z=|v/u|<=1. In natural units
Phi(1,z^2)/(2z)=[(1+z^2)ln(1+z^2)-z^2 ln(z^2)]/(2z).
Its derivative has the sign of
(z^2-1)ln(1+z^2)-z^2 ln(z^2), which is nonnegative because
ln(1+s)<=s and -ln s>=1-s for 0<s<=1. Thus the ratio is at most its
value ln2 at z=1. Homogeneity, symmetry and continuity prove the stated
bit-unit bound. This reconstructs the scalar envelope in A057's stage-2
PROOF.md section 2; the exact arbitrary-bias composition split itself is
already available there and is not claimed as a newly discovered calculus.

## 2. Any adaptive partial core tree: no repeated charge

Let T query only y coordinates, according to any policy depending on the
previous physical y answers, and stop at any core leaves. Keep x unqueried.
The same reach probabilities w_v and core leaf functions G_l occur in the
lifted tree. Put Pi=I(G)-E I(G_l), B_T(G)=sum_v w_v B_i(G_v), and
D_T=sum_v w_v D(mu_v,a_v). Influence conservation gives exactly
Pi=sum_v w_v Inf_i(G_v). Equations (1)-(3) imply

B_T(W)=B_T(G)/2+D_T, |D_T|<=Pi,
Pi_I(W)=Pi/2.                                             (4)

Thus the extra shifted-row erasure costs at most twice the actually consumed
wrapper influence, even at arbitrary biased descendants and adaptive
stopping times. The inherited core B_T(G)/2 has not been paid by this result.

If the partial prefix is followed by querying x at every leaf, its erasure
is, for either wrapper,

B_x(W)=Phi((1+mu)^2,(1-mu)^2)/4+(1-mu^2)/2
       <=1-mu^2.                                         (5)

For W_+ its x influence is d_x=(1-mu)/2; for W_- it is
d_x=(1+mu)/2. Since 1-mu^2<=4d_x, the terminal x charge satisfies
E B_x(W_l)<=4d_x(root), using E mu_l=mu(root). Consequently

B_(T;x)(W)<=B_T(G)/2+Pi+4d_x(root).                        (6)

The labelled x influence has not been spent during the prefix. After x
is queried the expected remaining core influence is E I(G_l)/2; therefore
the full influence telescope remains exact. For a complete core prefix,
B_(T;x)(W)<=B_T(G)/2+I(G)+4d_x. This is a transport bound,
not a universal upper bound on the inherited erasure.

## 3. Exact terminal entropy potential

With phi(p)=p log2(1/p), define

R(mu)=1-mu^2+phi((1+mu)^2/4)+phi((1-mu)^2/4)-phi(mu^2)/2.

Directly summing the two Fourier copies, including the empty coefficients,
gives for either wrapper

H(W)=H(G)/2+R(mu).                                        (7)

For any prefix tree the terminal bill is EXACTLY
E H(W_l)=E H(G_l)/2+E R(mu_l), and
H(W)-E H(W_l)=[H(G)-E H(G_l)]/2+R(mu)-E R(mu_l).            (8)

After the terminal x query, the average leaf entropy is E H(G_l)/2:
one x child is constant and the other is G_l. This prevents treating
unqueried arbitrary cores as certified threshold leaves. No sign or
influence bound on the potential R is assumed.

## 4. Scope and exact universal gap

Equations (1)-(8) close the shifted-row interface requested by A076's
previous NEXT. This narrow repair extends the existing spectra/payment
bundles; it does not open a third broad unreviewed candidate. It improves
the one-control arbitrary-bias interface to the sharp signed correction
bound D<=Inf_i(G) and carries it through every adaptive partial core tree.
General point-activation capped banks and the composition identity were
already paid by A057; the new quantity here is the actual signed row
correction and its exact inherited/terminal separation.

The first unsupported universal line is a dimension-independent payment
of B_T(G)/2 plus the retained arbitrary-core terminal entropy for a
universal physical policy, or a common ownership rule when two activation
cores share physical data/control coordinates. Equations (4) and (8) do
not establish either. Full FEI remains OPEN. The next target is the first
shared-coordinate collision in two priority activation events: determine
whether the signed row corrections admit one exclusive influence reserve
without charging both inherited cores again.
