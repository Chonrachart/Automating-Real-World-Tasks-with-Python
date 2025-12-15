#! /usr/bin/env python3 

# Import core reportlab components for building PDF
from reportlab.platypus import SimpleDocTemplate, Paragraph

# Import biult-in style presets (font, heading, styles)
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle

# Text alignment constant
from reportlab.lib.enums import TA_LEFT


"""def function generat report pdf use reportlab module (reprots.py)
"""


def generate_reports(title, data, output_location):
    # set outpur location and load styles sheet 
    report = SimpleDocTemplate(output_location)
    styles = getSampleStyleSheet()

    # set report_title and report_body
    report_title = Paragraph(title, styles["h1"])

    data_style = ParagraphStyle("Data_left",
                                alignment=TA_LEFT,
                                parent=styles["BodyText"],
                                )
    
    report_info = Paragraph(data, data_style)
    
    
    #build report
    report.build([report_title,report_info])

