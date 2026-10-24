SIGNED IN - working on the quadratic-form bounded-density conjecture (universal constant), account account02, slot B15, 2026-09-23T09:07:20Z.
attacking: a posterior critical-value bridge for an ambient physical rank-three indefinite block; convert the completed ruled one-sheet density estimate plus the partner heat-mode subgaussianity into a quantitative global heat-height inequality with random conditional critical value.

# Early substantive checkpoint: random-critical-value posterior bridge

Full target remains OPEN.

Let X=(X_S,W), where S consists of three original independent coordinates and W denotes all other original coordinates. Suppose the fixed principal block B=A_SS is invertible of signature (2,1), with eigenvalues lambda_1, lambda_2, -mu and kappa=min(lambda_1,lambda_2,mu)>0. Conditional on W=w,

Q_w(x)=x^T Bx+2d(w)^T x+c_0(w)
      =(x+B^{-1}d(w))^T B(x+B^{-1}d(w))+c(w),

where c(w)=c_0(w)-d(w)^T B^{-1}d(w).

The completed ruled one-sheet theorem in the required Claude source gives, after the original-coordinate translation and a rough-law limiting argument,

mu_+(E):=P(Q in E, Q>=c(W)) <= C_B |E|,

C_B=(lambda_1 lambda_2 mu)^(-1/2) int_0^{2pi}
    [sin^2(theta)/lambda_1+cos^2(theta)/lambda_2+1/mu]^(-1/2) dtheta
    <= pi sqrt(2)/kappa.

Now fix epsilon>0 and let y_* maximize H_epsilon(y)=E gamma_epsilon(Q-y). Put M=H_epsilon(y_*) and define the Gaussian Gibbs posterior

dnu/dP=gamma_epsilon(Q-y_*)/M.

By the completed account03/B15 heat-mode theorem, U=(Q-y_*)/epsilon is 1-subgaussian under nu:
E_nu exp(vU)<=exp(v^2/2), hence nu(U<-d)<=exp(-d^2/2).

Define the random normalized critical gap D=(y_*-c(W))/epsilon. Since

(mu_+*gamma_epsilon)(y_*)=M nu(Q>=c(W)) <= C_B,

we have nu(Q>=c(W))<=C_B/M. Also, on {D>=d} minus {U<-d}, one has U>=-d>=-D and therefore Q>=c(W). Thus for every d>0,

nu(D>=d) <= C_B/M + exp(-d^2/2),

or equivalently, whenever nu(D>=d)>exp(-d^2/2),

M <= C_B/[nu(D>=d)-exp(-d^2/2)]
  <= (pi sqrt(2)/kappa)/[nu(D>=d)-exp(-d^2/2)].

This is the first nontrivial bridge I know that survives a RANDOM conditional critical value. It uses no continuity of the rough output density. It says any high global heat mode forces the Gibbs posterior to concentrate on outside configurations whose conditional cone vertex lies at or above that mode.

Remaining step: quantify the posterior law of D from original-coordinate product provenance, or combine this trapping statement with another N3 structural branch. The two-sheet/minority geometry remains unpaid.