"""PROVED: replay all local face boxes, entirely in exact arithmetic."""
import json
from fractions import Fraction as F
from zero_face import construct
from centered_bounds import integer_polynomial,box_bound
from face_intervals import evaluate


def replay():
    C=construct()[-1];poly=integer_polynomial(C,80)
    records=json.load(open('face_boxes.json'))['boxes']
    for i,record in enumerate(records):
        box=[tuple(map(F,p))for p in record['box']]
        assert len(box)==6 and all(l<h for l,h in box)
        lower,upper=box_bound(poly,box)
        assert 80*lower==F(record['lower_Cface'])>0
        # A second exact evaluation method checks the center. The factored
        # matrix expression and the 1,254 coefficients must agree exactly.
        point=[(l+h)/2 for l,h in box]
        powers=[[x**k for k in range(9)]for x in point]
        direct=F(0)
        for mon,c in C.terms():
            val=F(int(c))
            for j,m in enumerate(mon):val*=powers[j][m]
            direct+=val
        expression=evaluate([(x,x)for x in point])[-1]
        assert expression.lo==expression.hi==direct
        assert 80*lower<=direct<=80*upper
    print('PROVED:',len(records),'local rational boxes replayed; every center independently matched F2 exactly.')
    return len(records)

if __name__=='__main__':replay()
