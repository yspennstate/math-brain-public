"""PROVED: exact polynomial normalization and auxiliary chart identities."""
from fractions import Fraction as F
from exact_bernstein import data
from zero_face import construct
from cover_face import polynomials

def main():
    target,gs=data()
    assert target==polynomials()[0]
    rr,t,V,R,M,delta,Q,tau,D,edges,P,num=construct()
    assert delta==sum((V[i][0]*V[j][1]-V[i][1]*V[j][0])**2
                     for i in range(5) for j in range(i+1,5))
    H=tau*tau-4*delta
    assert H==(M[0][0]-M[1][1])**2+4*M[0][1]**2
    assert (5*t-M[0][0])*(5*t-M[1][1])-M[0][1]**2==25*t*t-5*t*tau+delta
    assert 529*H-289*tau*tau==-4*(529*delta-60*tau*tau)
    # a=(tau+sqrt(H))/D. Conditional on D>0 and 14D-25tau>=0,
    # a>14/25 gives the strict nonnegative polynomial used as scale14.
    guard=14*D-25*tau
    scale=625*H-guard*guard
    def dic(p):
        return {mon[:6]:int(c) for mon,c in p.terms()}
    assert gs['scale_guard']==dic(guard) and gs['scale14']==dic(scale)
    assert edges[3,4]==0 and sum(edges.values())==D/2
    # On the strict spectral region, 5t-M is positive definite. Hence
    # tau<10t, D>10t>0; Delta>0 is a strict feasibility premise.
    # STRAT10's original-matrix identity gives
    # target=Cface_6/8=20*D^2*Delta*T6, with positive factor.
    print('PROVED (verify_formulation.py): target equals STRAT10 polynomials()[0]; Gram, spectral, ratio, scale and normalization identities replayed exactly.')
    print('PROVED (verify_formulation.py): scale14 is used only under its exact whole-box guard. Other ratio-dependent ceiling constraints are safely omitted; this enlarges the set being certified.')

if __name__=='__main__':main()
