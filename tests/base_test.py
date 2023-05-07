import configparser
import unittest


class BaseTest(unittest.TestCase):
    config = configparser.ConfigParser()
    config.read(r'D:\JetBrains\PycharmProjects\PdfTest\config.ini')
    default_path = config.get('pdf', 'default_path')

    def __init__(self, method_name='runTest', pdf_class=None, pdf_file=None):
        super().__init__(methodName=method_name)
        self.pdf_class = pdf_class
        self.pdf_file = pdf_file or self.default_path
        self.pdf = None

    def setUp(self):
        if self.pdf_class and self.pdf_file:
            self.pdf = self.pdf_class(self.pdf_file)

    def tearDown(self):
        pass
