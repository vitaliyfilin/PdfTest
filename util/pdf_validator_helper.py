import re


class PdfValidator:
    @staticmethod
    def validate_num_pages(pdf_reader):
        num_pages = len(pdf_reader.pages)
        if num_pages != 1:
            raise ValueError(f"Expected 1 page in PDF file, but got {num_pages} pages")

    @staticmethod
    def validate_required_fields(pdf_text, required_fields):
        missing_fields = []
        for field_name, regex in required_fields.items():
            match = re.search(regex, pdf_text)
            if not match:
                missing_fields.append(field_name)

        if missing_fields:
            raise ValueError(f"Required fields {missing_fields} not found in PDF file")

    @staticmethod
    def validate_extracted_data(extracted_data):
        for key, value in extracted_data.items():
            if value is None or value == "":
                print(f"Warning: Field {key} is empty")

    @staticmethod
    def validate_images_quantity(pdf_reader, image_quantity):
        for page in pdf_reader.pages:
            resources = page.get('/Resources')
            if resources is None:
                continue
            procsets = resources.get('/ProcSet')
            if procsets is None:
                continue
            count = 0
            for procset in procsets:
                if '/Image' in str(procset):
                    count += 1
                    if count == image_quantity:
                        return True
            if count != image_quantity:
                print(f"Found {count} '/Image' types instead of {image_quantity}")
        return False
