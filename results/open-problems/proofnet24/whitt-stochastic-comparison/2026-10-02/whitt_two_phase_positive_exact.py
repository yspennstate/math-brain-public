"""Two strictly positive exponential mixtures: stronger explicit certificate."""
from fractions import Fraction as F
import json
from whitt_positive_service_exact import certify,dec

if __name__=='__main__':
    al,au,a=certify('baseline_positive_H2',F(11,10),[F(3,7),F(4,7)],[F(5),F(5,8)])
    bl,bu,b=certify('more_variable_positive_H2',F(11,10),[F(200,533),F(333,533)],[F(1000),F(5,8)])
    assert al>F(39287,100000)
    assert bu<F(39037,100000)
    gap=al-bu; assert gap>F(1,400)
    print(json.dumps({'arithmetic':'exact Fraction; decimals only display',
                      'models':[a,b],'gap_lower_display':dec(gap),
                      'exact_assertions':['P_delay(S)>.39287','P_delay(T)<.39037',
                                          'P_delay(S)-P_delay(T)>1/400'],
                      'coupling':'baseline short .2E replaced by .001E with probability 1400/1599 or 1.6E with probability 199/1599; long branch unchanged',
                      'positive_threshold_corollary':'at h=1/100000, P(W_S>h)-P(W_T>h)>3/1250=.0024'},indent=2))
