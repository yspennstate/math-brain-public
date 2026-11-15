# T067-GAUSSIAN-QUAD-001 v1

Status: proof (unaudited). Elementary method extracted from the Gaussian
gap proof. No novelty assertion.

Let Z_1,Z_2 be independent standard normals. Let R>0 and let finitely many
nonempty intervals partition [-R,R], up to endpoints of Gaussian measure
zero. For bin i let w_i be its Gaussian probability, m_i its conditional
mean, and v_i=E[(Z-m_i)^2; Z in bin i] its unnormalized variance. Put
P=sum_i w_i and D=sum_i v_i. Let f:R^2->[0,B] be C^2, with finite B>=0
and global Euclidean Hessian operator norm at most K>=0. Define

    Q=sum_ij w_i*w_j*f(m_i,m_j).

Then

    |E[f(Z_1,Z_2); |Z_1|,|Z_2|<=R]-Q|<=K*P*D,
    Q-K*P*D <= E f(Z_1,Z_2) <= Q+K*P*D+B*(1-P^2).

Proof. In each product bin, Taylor-expand about (m_i,m_j). The integrated
linear term is zero because both coordinates have their exact bin
conditional means. The pointwise remainder is bounded in absolute value
by (K/2)[(z_1-m_i)^2+(z_2-m_j)^2]. Independence makes its integrated sum
(K/2)sum_ij(v_i*w_j+w_i*v_j)=K*P*D. The omitted square complement has
probability 1-P^2 by independence, and its integral lies in [0,B(1-P^2)].
These establish both claims, including all boundary points by null sets.

For a Gaussian bin [a,b], integration by parts gives
w=Phi(b)-Phi(a), m=[phi(a)-phi(b)]/w and
v=w+a*phi(a)-b*phi(b)-[phi(a)-phi(b)]^2/w. The exact Gaussian gap
certificate applies this method with R=6, bin width 1/8, B=1, K=9s/4.
Its numerical rounding is handled by outward interval arithmetic; the
method itself requires exact probabilities and conditional means, or
validated enclosures for them.
