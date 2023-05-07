from model.griffon_pdf import GriffonPdf
from tests.base_test import BaseTest
from util.write_to_csv import PDFToCSVWriter


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
        self.assertTrue(self.pdf.validate({
                "PN": GriffonPdf.pn_regex,
                "SN": GriffonPdf.sn_regex,
                "DESCRIPTION": GriffonPdf.description_regex,
                "LOCATION": GriffonPdf.location_regex,
                "RECEIVER#": GriffonPdf.receiver_regex,
                "EXP": GriffonPdf.exp_date_regex,
                "CERT": GriffonPdf.cert_source_regex,
                "REC DATE": GriffonPdf.rec_date_regex,
                "BATCH": GriffonPdf.batch_regex,
                "TAGGED BY": GriffonPdf.tagged_by_regex,
                "CONDITION": GriffonPdf.condition_regex,
                "UOM": GriffonPdf.uom_regex,
                "PO": GriffonPdf.po_regex,
                "MFG": GriffonPdf.mfg_regex,
                "DOM": GriffonPdf.dom_regex,
                "LOT": GriffonPdf.lot_regex,
                "Qty": GriffonPdf.qty_regex,
                "NOTES": GriffonPdf.notes_regex
            }))

    def tearDown(self):
        PDFToCSVWriter(self.pdf.extract_data())
