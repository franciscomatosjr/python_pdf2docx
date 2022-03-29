from pdf2docx import Converter

pdf_file_path = r'<filpath pdf>.pdf'

docx_file_path = r'<file path output>.docx'


c = Converter(pdf_file_path)
c.convert(docx_file_path)
c.close()
