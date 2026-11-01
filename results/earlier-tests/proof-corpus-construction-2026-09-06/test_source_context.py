"""Synthetic parser regression controls. None are corpus questions."""
from pathlib import Path
import io
import gzip
import tarfile
import tempfile
import unittest

import extract_source_context as E

HEADER = r'\documentclass{article}\newtheorem{theorem}{Theorem}\begin{document}'
PAIR = r'''
\begin{theorem}\label{thm:test}For every integer $n\geq 1$, the explicitly defined quantity $S_n=\sum_{j=1}^n j$ satisfies $S_n=n(n+1)/2$.\end{theorem}
\begin{proof}%HEADING%
First observe that $S_1=1=1(1+1)/2$, so the required identity holds at the initial index. Suppose that $S_n=n(n+1)/2$ for the particular positive integer under consideration. The definition then gives $S_{n+1}=S_n+(n+1)=n(n+1)/2+(n+1)=(n+1)(n+2)/2$. This verifies the claimed induction step and proves the identity for every positive integer $n$.
\end{proof}
'''


class SourceContextTests(unittest.TestCase):
    def setUp(self):
        # Keep even disposable test artifacts inside this lane's claimed worktree.
        self.temp = tempfile.TemporaryDirectory(prefix='context-test-',dir=E.HERE)
        self.root = Path(self.temp.name)
        self.paper = self.root/'1101.9999'
        self.paper.mkdir()
        self.download={'base_id':'1101.9999','arxiv_id':'1101.9999v2',
                       'kind':'tar','n_tex':1,'sha256':'a'*64}

    def tearDown(self):
        assert Path(self.temp.name).resolve().is_relative_to(E.HERE)
        self.temp.cleanup()

    def put(self,name,text):
        target=self.paper/name
        target.parent.mkdir(parents=True,exist_ok=True)
        target.write_bytes(text.encode('utf-8'))
        return target

    def run_paper(self):
        return E.extract_paper(self.root,'1101.9999',self.download)

    def test_full_context_offsets_and_no_semantic_acceptance(self):
        self.put('main.tex',HEADER+PAIR.replace('%HEADING%','')+r'\end{document}')
        rows,receipt,body=self.run_paper()
        self.assertEqual(len(rows),1)
        row=rows[0]
        self.assertTrue(row['candidate_filter_pass'])
        start,end=row['proof_span_characters']
        self.assertIn(row['raw_proof'],body[start:end])
        self.assertEqual(row['source_version'],'1101.9999v2')
        self.assertEqual(row['semantic_acceptance'],'UNREVIEWED')
        self.assertEqual(receipt['mechanical_dependency_scan'],'NO_DETECTED_INCLUDE_FAILURE')

    def test_missing_include_is_preserved_and_disqualifies(self):
        self.put('main.tex',HEADER+r'\input{missing}'+PAIR.replace('%HEADING%',''))
        rows,receipt,body=self.run_paper()
        self.assertIn(r'\input{missing}',body)
        self.assertTrue(receipt['issues'])
        self.assertFalse(rows[0]['candidate_filter_pass'])

    def test_include_escape_never_reads_outside_paper(self):
        (self.root/'outside.tex').write_text('private sentinel',encoding='utf-8')
        self.put('main.tex',HEADER+r'\input{../outside}'+PAIR.replace('%HEADING%',''))
        rows,receipt,body=self.run_paper()
        self.assertNotIn('private sentinel',body)
        self.assertEqual(len(receipt['files']),1)
        self.assertIn('escapes',receipt['issues'][0]['reason'])
        self.assertFalse(rows[0]['candidate_filter_pass'])

    def test_repeated_include_is_not_silently_dropped_or_counted_distinct(self):
        self.put('main.tex',HEADER+r'\input{part}\input{part}')
        self.put('part.tex',PAIR.replace('%HEADING%',''))
        rows,receipt,body=self.run_paper()
        self.assertEqual(len(rows),2)
        self.assertEqual(len({r['source_proof_identity'] for r in rows}),1)
        self.assertEqual(len({r['source_occurrence_identity'] for r in rows}),2)

    def test_cycle_is_preserved_as_unresolved_context(self):
        self.put('main.tex',HEADER+r'\input{a}'+PAIR.replace('%HEADING%',''))
        self.put('a.tex',r'\input{a}')
        rows,receipt,body=self.run_paper()
        self.assertTrue(any('cyclic' in i.get('reason','') for i in receipt['issues']))
        self.assertFalse(rows[0]['candidate_filter_pass'])

    def test_flat_archive_include_keeps_exact_file_receipt(self):
        self.put('main.tex',HEADER+r'\input{section/part}')
        self.put('section__part.tex',PAIR.replace('%HEADING%',''))
        rows,receipt,body=self.run_paper()
        self.assertEqual(len(rows),1)
        self.assertEqual({r['relative_path'] for r in receipt['files']},{'main.tex','section__part.tex'})
        self.assertFalse(receipt['issues'])

    def test_partial_heading_checked_before_display_truncation(self):
        heading='[Proof of Theorem~\\ref{thm:test} '+('context '*40)+', part (3)]'
        self.put('main.tex',HEADER+PAIR.replace('%HEADING%',heading))
        rows,_,_=self.run_paper()
        self.assertIn('part (3)',rows[0]['proof_heading'])
        self.assertNotIn('part (3)',rows[0]['proof_opt'])
        self.assertEqual(rows[0]['candidate_filter_reject_reason'],'partial_statement_proof')

    def test_source_drift_and_wrong_version_receipt_refused(self):
        path=self.put('main.tex',HEADER)
        reader=E.SourceReader(self.paper)
        reader.read(path)
        path.write_text('different',encoding='utf-8')
        with self.assertRaisesRegex(E.SourceContextError,'changed'):
            reader.verify_unchanged()
        self.download['arxiv_id']='1101.9999'
        with self.assertRaisesRegex(ValueError,'exact-version'):
            self.run_paper()

    def test_ambiguous_include_is_not_chosen_arbitrarily(self):
        self.put('main.tex',HEADER+r'\input{section/part}')
        self.put('section/part.tex',PAIR.replace('%HEADING%',''))
        self.put('section__part.tex',PAIR.replace('%HEADING%',''))
        rows,receipt,_=self.run_paper()
        self.assertFalse(rows)
        self.assertIn('ambiguous include',receipt['issues'][0]['reason'])

    def test_external_reference_labels_remain_distinguishable(self):
        count=[0]
        text=E.U.clean_text(r'Use \ref{lemma:one} and \ref{lemma:two}.',{},count)
        self.assertIn('lemma:one',text)
        self.assertIn('lemma:two',text)
        self.assertEqual(count[0],2)

    def archive(self,members):
        path=self.root/'source.bin'
        with tarfile.open(path,'w:gz') as stream:
            for name,raw in members:
                member=tarfile.TarInfo(name)
                member.size=len(raw)
                stream.addfile(member,io.BytesIO(raw))
        self.download['sha256']=E.file_sha(path)
        return path

    def test_archive_verifies_bytes_not_just_filenames(self):
        raw=(HEADER+PAIR.replace('%HEADING%','')).encode()
        self.put('main.tex',raw.decode())
        archive=self.archive([('main.tex',raw)])
        rows,receipt,_=E.extract_paper(self.root,'1101.9999',self.download,archive=archive)
        self.assertEqual(receipt['archive_origin_validation']['status'],'ARCHIVE_HASH_AND_READ_SOURCE_MEMBER_BYTES_MATCH')
        self.put('main.tex',raw.decode()+' changed')
        with self.assertRaisesRegex(E.SourceContextError,'differs'):
            E.extract_paper(self.root,'1101.9999',self.download,archive=archive)

    def test_archive_filename_collision_and_hash_drift_refused(self):
        raw=b'first'
        archive=self.archive([('a/b.tex',raw),('a__b.tex',raw)])
        files=[{'relative_path':'a__b.tex','sha256':E.sha(raw),'bytes':len(raw)}]
        with self.assertRaisesRegex(E.SourceContextError,'colliding'):
            E.verify_archive_origin(archive,self.download,files)
        self.download['sha256']='b'*64
        with self.assertRaisesRegex(E.SourceContextError,'hash differs'):
            E.verify_archive_origin(archive,self.download,files)

    def test_single_tex_gzip_origin(self):
        raw=b'\\documentclass{article}test'
        archive=self.root/'single.bin'
        archive.write_bytes(gzip.compress(raw))
        self.download.update(kind='single_tex',sha256=E.file_sha(archive))
        files=[{'relative_path':'main.tex','sha256':E.sha(raw),'bytes':len(raw)}]
        receipt=E.verify_archive_origin(archive,self.download,files)
        self.assertEqual(receipt['members'][0]['archive_member'],'single_tex_payload')


if __name__=='__main__': unittest.main()
