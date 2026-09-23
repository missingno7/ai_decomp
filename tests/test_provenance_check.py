import hashlib
import tempfile
import unittest
from pathlib import Path
from tools.provenance_check import check

class ProvenanceTests(unittest.TestCase):
    def test_drift_missing_and_path_escape(self):
        with tempfile.TemporaryDirectory() as tmp:
            root=Path(tmp)
            (root/'project').mkdir()
            (root/'project'/'evidence.txt').write_bytes(b'synthetic evidence')
            source=dict(id='fixture',repository='project',path='evidence.txt',
                        content_kind='working_tree',sha256=hashlib.sha256(b'synthetic evidence').hexdigest())
            self.assertEqual(check([source],root)['verified'],1)
            (root/'project'/'evidence.txt').write_bytes(b'changed')
            self.assertEqual(check([source],root)['results'][0]['status'],'drifted')
            for path in ('absent','../../outside'):
                result=check([dict(source,path=path)],root)
                self.assertEqual(result['results'][0]['status'],'unavailable')

if __name__=='__main__': unittest.main()
