SIGNED IN - working on the quadratic-form bounded-density conjecture (universal constant), account fleet02, slot B04, 2026-09-24T02:14:06Z.
attacking: high-leverage residual routing via anchored E4 carrier promotion; optimize admissible third-volume weights and compare ridge on the same physical matrix.

# Early substantive calculation — exact ambient E3 reweighting on the partner r46 carrier

Use the fleet03/B04 r46 physical cross block at epsilon=1/16. Its five orthogonal row-direction group squared singular weights are

x=(256,1,1,1,1/256),

realized by one physical hub row in the first direction, two equal physical rows in each of the remaining four directions. Thus

E3=e3(x)=197635/256,
E4=e4(x)=66305/256,
E5=e5(x)=1.

For a physical row triple S, after summing over all physical column triples T, Cauchy-Binet gives

z_S=sum_T det(M_ST)^2=det(M_S M_S^T).

Hence z_S vanishes if S repeats a row direction and otherwise equals the product of the three physical row norm-squares. The full arbitrary-minor determinant/entropy optimization therefore reduces exactly to a probability law p on supported physical row triples, with

log G(p)=log E3-D(p||nu),

where nu_S=z_S/E3 is the canonical physical row-triple law. Let q=p(row 0 is included). Under nu the total mass of triples containing row 0 is

W_in=771,

while the mass of triples excluding row 0 is

W_out=259/256,

so q0=W_in/(W_in+W_out)=197376/197635>3/4. Thus the canonical D and D' gates fail at the hub row.

For any p, KL chain decomposition across the two strata gives

D(p||nu)=D_Ber(q||q0)+q D(p_in||nu_in)+(1-q)D(p_out||nu_out)
        >=D_Ber(q||q0).

For the q=1 Theorem-D marginal cap alpha_i<=1/2, necessarily q<=1/2. Since q0>1/2, D_Ber(q||q0) is strictly decreasing on q<=1/2, so its minimum is attained at q=1/2. Equality is achieved by retaining the canonical conditional law within the two strata. The other physical row marginals of this candidate are

alpha_strong=(1/4)(171/257+258/259)=110595/266252=0.415377161486...<1/2

for each of the six strong duplicated rows, and

alpha_weak=(1/4)(1/257+3/259)=515/133126=0.003868515542...<1/2

for each weak duplicated row. Hence this is globally feasible, and the exact globally optimized determinant/entropy currency under the Theorem-D row cap is

G_{1/2}=E3 exp[-D_Ber(1/2||q0)]
       =2 sqrt(W_in W_out)
       =sqrt(199689)/8
       =55.8582189565689....

Applying the pinned e5 arbitrary-weight Theorem D therefore gives the actual target-valid inequality

||p_Q||_infinity <=6 sqrt(e) G_{1/2}^{-1/6}
                  =6 sqrt(2e) 199689^{-1/12}
                  =5.05961312687030....

This already removes the canonical third-volume marginal obstruction without rotating the independent variables or selecting one small local minor. The partner r46 hub-retaining E4 theorem on the same physical matrix is stronger (2.378720371807186...), so the remaining question is structural: when high leverage occurs in an arbitrary survivor, can one force a target-scale anchored E4 carrier (or a lower-order completed packet) before paying an ambient entropy penalty?
