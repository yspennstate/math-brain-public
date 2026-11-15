import json
from corner_face_certificates import build

if __name__=='__main__':
    assert json.load(open('corner_face_boxes.json'))==build()
    print('PROVED: two corner chart boxes and all fifteen distinct labeled equality graphs.')
