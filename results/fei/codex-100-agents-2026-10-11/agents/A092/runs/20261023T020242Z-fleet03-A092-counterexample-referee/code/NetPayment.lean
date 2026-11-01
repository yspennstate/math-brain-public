import Lean

theorem signed_net_payment (c b old new rho z : Int)
    (h : c = b + old + rho) (hreset : new = old + z) :
    b + new - c = z - rho := by omega

theorem refund_lower_bound (z rho rho0 bound : Int)
    (h : rho0 <= rho) (hnet : z - rho0 <= bound) :
    z - rho <= bound := by omega

#print signed_net_payment
#print axioms signed_net_payment
#print refund_lower_bound
#print axioms refund_lower_bound
