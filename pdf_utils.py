
import io
import logging
from datetime import datetime
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer, Table, TableStyle, PageBreak
from reportlab.lib.pagesizes import LETTER
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.lib.units import inch
from reportlab.lib import colors
from reportlab.lib.enums import TA_LEFT, TA_CENTER
import markdown
from bs4 import BeautifulSoup

logger = logging.getLogger(__name__)


def html_to_reportlab(html_str):
    """Convert HTML tags to ReportLab-compatible format"""
    html_str = html_str.replace('<strong>', '<b>').replace('</strong>', '</b>')
    html_str = html_str.replace('<em>', '<i>').replace('</em>', '</i>')
    return html_str


def get_custom_styles():
    """Create and return custom styles for PDF generation"""
    styles = getSampleStyleSheet()

    style_h2 = ParagraphStyle(
        'CustomH2',
        parent=styles['Heading1'],
        fontSize=20,
        textColor=colors.HexColor('#1a472a'),
        spaceAfter=20,
        spaceBefore=12,
        fontName='Helvetica-Bold',
        alignment=TA_LEFT
    )

    style_h3 = ParagraphStyle(
        'CustomH3',
        parent=styles['Heading2'],
        fontSize=14,
        textColor=colors.HexColor('#2c5f2d'),
        spaceAfter=12,
        spaceBefore=16,
        fontName='Helvetica-Bold',
        leftIndent=0
    )

    style_body = ParagraphStyle(
        'CustomBody',
        parent=styles['BodyText'],
        fontSize=11,
        leading=16,
        textColor=colors.HexColor('#333333'),
        spaceAfter=8,
        alignment=TA_LEFT
    )

    style_h4 = ParagraphStyle(
        'CustomH4',
        parent=styles['Heading3'],
        fontSize=12,
        textColor=colors.HexColor('#2c5f2d'),
        spaceAfter=10,
        spaceBefore=12,
        fontName='Helvetica-Bold',
        leftIndent=0
    )

    style_bullet = ParagraphStyle(
        'CustomBullet',
        parent=styles['BodyText'],
        fontSize=11,
        leading=15,
        textColor=colors.HexColor('#444444'),
        leftIndent=20,
        bulletIndent=10,
        spaceAfter=6
    )

    return {
        'h2': style_h2,
        'h3': style_h3,
        'h4': style_h4,
        'body': style_body,
        'bullet': style_bullet,
        'normal': styles['Normal']
    }


import traceback

def markdown_to_pdf_bytes(markdown_content):
    try:
        logger.info(f"[PDF] Starting markdown → PDF conversion. Input length={len(markdown_content)} chars")

        styles = get_custom_styles()
        html_content = markdown.markdown(markdown_content, extensions=['tables'])
        logger.debug(f"[PDF] HTML conversion complete. HTML length={len(html_content)} chars")

        soup = BeautifulSoup(html_content, 'html.parser')
        flowables = []

        element_count = 0

        for elem in soup.children:
            element_count += 1
            logger.debug(f"[PDF] Processing element #{element_count}, type={elem.name}")

            if elem.name == 'h2':
                flowables.append(Paragraph(elem.get_text(), styles['h2']))
                flowables.append(Spacer(1, 0.15*inch))

            elif elem.name == 'h3':
                flowables.append(Spacer(1, 0.1*inch))
                flowables.append(Paragraph(elem.get_text(), styles['h3']))
                flowables.append(Spacer(1, 0.08*inch))

            elif elem.name == 'h4':
                flowables.append(Spacer(1, 0.08*inch))
                flowables.append(Paragraph(elem.get_text(), styles['h4']))
                flowables.append(Spacer(1, 0.06*inch))

            elif elem.name == 'p':
                formatted_text = html_to_reportlab(str(elem))
                flowables.append(Paragraph(formatted_text, styles['body']))
                flowables.append(Spacer(1, 0.08*inch))

            elif elem.name == 'ul':
                li_count = len(elem.find_all('li', recursive=False))
                logger.debug(f"[PDF] Rendering bullet list with {li_count} items")

                for li in elem.find_all('li', recursive=False):
                    li_html = ''.join(str(content) for content in li.contents)
                    formatted_li = html_to_reportlab(li_html)
                    bullet_text = f"• {formatted_li}"
                    flowables.append(Paragraph(bullet_text, styles['bullet']))
                flowables.append(Spacer(1, 0.1*inch))

            elif elem.name == 'ol':
                li_items = elem.find_all('li', recursive=False)
                li_count = len(li_items)
                logger.debug(f"[PDF] Rendering numbered list with {li_count} items")

                for idx, li in enumerate(li_items, 1):
                    li_html = ''.join(str(content) for content in li.contents)
                    formatted_li = html_to_reportlab(li_html)
                    numbered_text = f"{idx}. {formatted_li}"
                    flowables.append(Paragraph(numbered_text, styles['bullet']))
                flowables.append(Spacer(1, 0.1*inch))

            elif elem.name == 'table':
                rows = [
                    [td.get_text().strip() for td in tr.find_all(['td','th'])]
                    for tr in elem.find_all('tr')
                ]

                logger.info(
                    f"[PDF] Rendering table: {len(rows)} rows × "
                    f"{len(rows[0]) if rows else 0} columns"
                )

                table = Table(
                    rows,
                    hAlign='LEFT',
                    colWidths=[3*inch, 1.5*inch, 1.2*inch]
                )

                table.setStyle(TableStyle([
                    ('BACKGROUND', (0,0), (-1,0), colors.HexColor('#2c5f2d')),
                    ('TEXTCOLOR', (0,0), (-1,0), colors.whitesmoke),
                    ('FONTNAME', (0,0), (-1,0), 'Helvetica-Bold'),
                    ('FONTSIZE', (0,0), (-1,0), 11),
                    ('BOTTOMPADDING', (0,0), (-1,0), 10),
                    ('TOPPADDING', (0,0), (-1,0), 10),

                    ('BACKGROUND', (0,1), (-1,-1), colors.white),
                    ('TEXTCOLOR', (0,1), (-1,-1), colors.HexColor('#333333')),
                    ('FONTNAME', (0,1), (-1,-1), 'Helvetica'),
                    ('FONTSIZE', (0,1), (-1,-1), 10),

                    ('ROWBACKGROUNDS', (0,1), (-1,-1), [colors.white, colors.HexColor('#f5f5f5')]),
                    ('GRID', (0,0), (-1,-1), 0.75, colors.HexColor('#cccccc')),
                    ('BOX', (0,0), (-1,-1), 1.5, colors.HexColor('#2c5f2d')),
                ]))

                flowables.append(table)
                flowables.append(Spacer(1, 0.2*inch))

        logger.info(f"[PDF] Finished parsing. Total flowables={len(flowables)}")

        pdf_buffer = io.BytesIO()
        doc = SimpleDocTemplate(
            pdf_buffer,
            pagesize=LETTER,
            leftMargin=0.75*inch,
            rightMargin=0.75*inch,
            topMargin=0.75*inch,
            bottomMargin=0.75*inch
        )

        doc.build(flowables)
        pdf_buffer.seek(0)

        logger.info(f"[PDF] PDF built successfully. Output size={len(pdf_buffer.getvalue())} bytes")

        return pdf_buffer.getvalue()

    except Exception as e:
        logger.error(
            f"[PDF] ERROR during markdown -> PDF conversion: {str(e)}\n"
            f"Traceback:\n{traceback.format_exc()}"
        )
        raise


def generate_pdf_filename():
    """Generate a filename for the PDF with timestamp"""
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    return f"chatbot_response_{timestamp}.pdf"
