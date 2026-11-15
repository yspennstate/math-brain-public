import json
from cone_certificate import build

if __name__=='__main__':
    assert json.load(open('tangent_cone_certificate.json'))==build()
    print('PROVED: exact tangent cone premises: strict direction, rational Cayley witness, fifteen proper cut varieties.')
