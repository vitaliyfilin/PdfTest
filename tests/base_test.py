import unittest


class BaseTest(unittest.TestCase):
    def __init__(self, method_name='runTest', pdf_class=None):
        super().__init__(methodName=method_name)
        self.pdf_class = pdf_class

    def setUp(self):
        self.pdf_file = r'D:\JetBrains\PycharmProjects\PdfTest\data\input\test_task.pdf'
        if self.pdf_class:
            self.pdf = self.pdf_class(self.pdf_file)

    def tearDown(self):
        pass
