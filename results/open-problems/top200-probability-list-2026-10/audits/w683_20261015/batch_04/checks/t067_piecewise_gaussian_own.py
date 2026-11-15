"""Independent conditional-bin Gaussian quadrature for the displayed q=3 map."""
from fractions import Fraction
from pathlib import Path
from hashlib import sha256
from time import monotonic
import json
import sys
from flint import arb,ctx

ctx.prec=192

def ar(q):
    q=Fraction(q); return arb(q.numerator)/q.denominator

class GaussianQuadrature:
    def __init__(self):
        start=monotonic(); sqrt2=arb(2).sqrt(); denominator=(2*arb.pi()).sqrt()
        self.bins=[]
        for j in range(96):
            a=arb(j)/16; b=arb(j+1)/16
            fa=(-a*a/2).exp()/denominator; fb=(-b*b/2).exp()/denominator
            w=((b/sqrt2).erf()-(a/sqrt2).erf())/2
            assert w>0
            numerator=fa-fb; mean=numerator/w
            variance=w+a*fa-b*fb-numerator*numerator/w
            assert mean>a and mean<b and variance>0
            self.bins.append((w,mean,variance))
        self.P=2*sum((b[0] for b in self.bins),arb(0))
        self.D=2*sum((b[2] for b in self.bins),arb(0))
        assert 0<self.P<1 and self.D>0
        self.setup_seconds=monotonic()-start

    def evaluate(self,signal):
        start=monotonic(); signal=Fraction(signal); s=ar(signal)
        assert Fraction(1,10)<=signal<=Fraction(2,3)
        drift=(-9*s/2).exp(); product=4*drift*drift
        alpha=3*(3*s).sqrt()/2; beta=3*s.sqrt()/2
        rows=[(w,4*drift*(alpha*m).cosh()) for w,m,_ in self.bins]
        cols=[(w,(beta*m).cosh()) for w,m,_ in self.bins]
        Q=arb(0)
        # Each positive-bin pair represents the four sign combinations.
        # f(z1,z2) is even in z2. For the +/-z1 pair, Aplus*Aminus=4e^-9s,
        # Aplus+Aminus=4e^(-9s/2)cosh(alpha*m), so their sum is one fraction.
        for wi,A_sum in rows:
            subtotal=arb(0)
            for wj,B in cols:
                mixed=A_sum*B
                subtotal+=wj*(2+mixed)/(1+mixed+product*B*B)
            Q+=2*wi*subtotal
        K=9*s/10; error=K*self.P*self.D
        upper=(Q+error+1-self.P*self.P-ar(Fraction(1,3))).upper().fmpq()
        lower=(Q-error-ar(Fraction(1,3))).lower().fmpq()
        return {'signal':str(signal),'precision_bits':ctx.prec,'bin_width':'1/16','full_bins':192,'folded_blocks':9216,'g_lower':str(lower),'g_upper':str(upper),'Q_lower':str(Q.lower().fmpq()),'Q_upper':str(Q.upper().fmpq()),'P_lower':str(self.P.lower().fmpq()),'P_upper':str(self.P.upper().fmpq()),'D_upper':str(self.D.upper().fmpq()),'seconds':monotonic()-start,'script_sha256':sha256(Path(__file__).read_bytes()).hexdigest()}

def main():
    point=Fraction(sys.argv[1]); engine=GaussianQuadrature(); result=engine.evaluate(point)
    path=Path('checks')/('t067_piecewise_endpoint_'+str(point).replace('/','_')+'_own.json')
    path.write_text(json.dumps(result,indent=2)+'\n',encoding='utf-8')
    print(json.dumps({'signal':str(point),'g_upper_display':float(Fraction(result['g_upper'])),'seconds':result['seconds'],'setup_seconds':engine.setup_seconds,'precision_bits':ctx.prec,'receipt':str(path)}))
if __name__=='__main__': main()
