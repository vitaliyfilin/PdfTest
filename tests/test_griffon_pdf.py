import unittest

from model.griffon_pdf import GriffonPdf
from tests.base_test import BaseTest


class TestGriffonPdf(BaseTest):
    def __init__(self, method_name='runTest'):
        super().__init__(method_name=method_name, pdf_class=GriffonPdf)

    def test_extract_data(self):
        expected_data = {'batch': '1',
                         'cert_source': 'wef',
                         'condition': 'FN',
                         'description': 'PART',
                         'dom': '13.04.2022',
                         'exp_date': '13.04.2022',
                         'location': '111',
                         'lot': '1',
                         'mfg': 'efwfe',
                         'notes': 'inspection notes',
                         'pn': 'tst',
                         'po': 'P101',
                         'qty': '1',
                         'rec_date': '18.04.2022',
                         'receiver': '9',
                         'remark': '',
                         'sn': '123123',
                         'tagged_by': None,
                         'uom': 'EA'}
        self.assertEqual(self.pdf.extract_data(), expected_data)

    def test_validate(self):
        self.assertTrue(self.pdf.validate())


if __name__ == '__main__':
    unittest.main()
