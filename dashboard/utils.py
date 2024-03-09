import re
import ocrspace
from django.conf import settings
import json
from collections import defaultdict

def perform_ocr(file_path):
    api = ocrspace.API(api_key=settings.OCR_API_KEY)
    ocr_output = api.ocr_file(file_path)
    parased_ocr_output = ocr_output["ParsedResults"]
    data = extract_questions(parased_ocr_output)
    # data = ocr_output
    return data

def extract_questions(ocr_output):
    grouped_lines = defaultdict(list)
    for item in ocr_output:
        text_overlay = item.get('TextOverlay')
        if text_overlay:
            lines = text_overlay.get('Lines', [])
            current_question = ''
            
            for line in lines:
                line_text = line.get('LineText', '').strip()
                if line_text:
                    # Check if the line ends with a punctuation mark
                    if line_text.endswith(('.', '?', '!')):
                        current_question += line_text + ' '
                        grouped_lines[current_question].append(line_text)
                        current_question = ''
                    else:
                        current_question += line_text + ' '
    return grouped_lines 
