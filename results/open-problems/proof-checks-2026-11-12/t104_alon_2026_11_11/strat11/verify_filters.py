import json
from filter_certificate import build

if __name__=='__main__':
    assert json.load(open('filter_certificate.json'))==build()
    print('PROVED: strict inherited moment/scale/chart filter exclusions at P0, all 192 charts.')
