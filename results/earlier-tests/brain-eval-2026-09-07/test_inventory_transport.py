"""Independent receipt substitution controls, using synthetic transport only."""
import json
from pathlib import Path
import tempfile
import unittest
import export_reviewed_calibration as export
import recover_accepted_inventory as inventory
from test_reviewed_calibration import fixture

class TransportProvenance(unittest.TestCase):
    def setUp(self):
        self.temp=tempfile.TemporaryDirectory();self.addCleanup(self.temp.cleanup)
        self.root=Path(self.temp.name);self.values,self.review=fixture()
        self.review_path=self.root/'review.json';self.review_path.write_text(json.dumps(self.review),encoding='utf-8')
        self.review_pin={'path':str(self.review_path),'sha256':export.sha(self.review_path.read_bytes())}
        out=self.root/'transport'
        export.write_private(self.values,{},self.review,self.review_path,self.review_pin['sha256'],out,self.root)
        self.receipt=out/'PRIVATE_RECEIPT.json'
    def check(self):
        return inventory.transport_check(self.values,{'path':str(self.receipt),'sha256':export.sha(self.receipt.read_bytes())},self.review_pin)
    def mutate_receipt(self,field,value):
        data=json.loads(self.receipt.read_text());data[field]=value
        self.receipt.write_text(json.dumps(data),encoding='utf-8')
    def test_original_transport_preserved(self):
        self.assertEqual(self.check()['opaque_id_count'],6)
    def test_rehashed_different_review_digest_rejected(self):
        self.mutate_receipt('review_sha256','0'*64)
        with self.assertRaisesRegex(ValueError,'different review'):self.check()
    def test_rehashed_different_review_path_rejected(self):
        self.mutate_receipt('review_path',str(self.root/'different_review.json'))
        with self.assertRaisesRegex(ValueError,'different review'):self.check()
    def test_rehashed_altered_question_rejected(self):
        p=self.receipt.parent/'solver_input/items.jsonl';rows=export.records(p.read_bytes());rows[0]['claim']='Different synthetic question'
        data=''.join(json.dumps(r)+'\n' for r in rows).encode();p.write_bytes(data)
        self.mutate_receipt('solver_items_sha256',export.sha(data))
        with self.assertRaisesRegex(ValueError,'question changed'):self.check()

if __name__=='__main__':unittest.main()
