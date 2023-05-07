import PyPDF2
from abc import ABC, abstractmethod


class BasePDF(ABC):
    def __init__(self, pdf_file):
        self.pdf_reader = PyPDF2.PdfReader(pdf_file)
        self.page_number = 0  # если дата на первой странице
        self.page = self.pdf_reader.pages[self.page_number]
        self.pdf_text = self.page.extract_text()

    @abstractmethod
    def extract_data(self):
        pass

    @abstractmethod
    def validate(self, required_fields):
        pass
