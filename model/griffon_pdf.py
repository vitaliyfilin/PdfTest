import re
from model.base_pdf import BasePDF
from util.pdf_validator_helper import PdfValidator


class GriffonPdf(BasePDF):
    template_regex = r'(.+?)?\n'
    sn_regex = f'SN: {template_regex}'
    uom_regex = f'UOM: {template_regex}'
    po_regex = f'PO: {template_regex}'
    mfg_regex = f'MFG: {template_regex}'
    dom_regex = f'DOM: {template_regex}'
    lot_regex = f'LOT# : {template_regex}'
    tagged_by_regex = f'TAGGED BY: {template_regex}'
    condition_regex = f'CONDITION: {template_regex}'
    description_regex = f'DESCRIPTION: {template_regex}'
    cert_source_regex = f'CERT SOURCE: {template_regex}'
    pn_regex = r'PN: (\w+)(?=.*?\sSN\b)'
    qty_regex = r'Qty:\s*(\d+).*?(?:(?!NOTES).)*\n'
    batch_regex = r'BATCH# : \s*(\d+).*?(?:(?!DOM).)*\n'
    rec_date_regex = r'REC\.DATE: (\d{2}\.\d{2}\.\d{4})'
    location_regex = r'LOCATION: (\d+)(?=.*?\sCONDITION\b)'
    receiver_regex = r'RECEIVER#: \s*(\d+).*?(?:(?!UOM).)*\n'
    remark_regex = r'REMARK:\s*(?P<REMARK>[^L\n]*)(?=LOT.*|\n)'
    exp_date_regex = r'EXP DATE: (\d{2}\.\d{2}\.\d{4})(?=.*?\sPO\b)'
    notes_regex = r'NOTES:\s*((?:(?!GRIFFON AVIATION SERVICES LLC).)*?(?:\n|$))'

    def __init__(self, pdf_file):
        super().__init__(pdf_file)

    def extract_data(self):
        extracted_data = {
            'pn': re.search(self.pn_regex, self.pdf_text).group(1),
            'description': re.search(self.description_regex, self.pdf_text).group(1),
            'location': re.search(self.location_regex, self.pdf_text).group(1),
            'receiver': re.search(self.receiver_regex, self.pdf_text).group(1),
            'exp_date': re.search(self.exp_date_regex, self.pdf_text).group(1),
            'cert_source': re.search(self.cert_source_regex, self.pdf_text).group(1),
            'rec_date': re.search(self.rec_date_regex, self.pdf_text).group(1),
            'batch': re.search(self.batch_regex, self.pdf_text).group(1),
            'tagged_by': re.search(self.tagged_by_regex, self.pdf_text).group(1),
            'sn': re.search(self.sn_regex, self.pdf_text).group(1),
            'condition': re.search(self.condition_regex, self.pdf_text).group(1),
            'uom': re.search(self.uom_regex, self.pdf_text).group(1),
            'po': re.search(self.po_regex, self.pdf_text).group(1),
            'mfg': re.search(self.mfg_regex, self.pdf_text).group(1),
            'dom': re.search(self.dom_regex, self.pdf_text).group(1),
            'lot': re.search(self.lot_regex, self.pdf_text).group(1),
            'remark': re.search(self.remark_regex, self.pdf_text).group(1),
            'qty': re.search(self.qty_regex, self.pdf_text).group(1),
            'notes': re.search(self.notes_regex, self.pdf_text).group(1)}
        return extracted_data

    def validate(self, required_fields):
        with self:
            pdf_reader = self.pdf_reader
            pdf_text = self.pdf_text
            extracted_data = self.extract_data()

            PdfValidator.validate_num_pages(pdf_reader)
            PdfValidator.validate_required_fields(pdf_text, required_fields)
            PdfValidator.validate_extracted_data(extracted_data)
            PdfValidator.validate_images_quantity(pdf_reader, 3)

            return True
