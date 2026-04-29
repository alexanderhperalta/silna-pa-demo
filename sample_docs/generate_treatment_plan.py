"""
Generates a realistic synthetic ABA treatment plan PDF.
This is the PDF input document the Claude extractor will parse.
"""
from reportlab.lib.pagesizes import letter
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.lib.units import inch
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer, Table, TableStyle, HRFlowable
from reportlab.lib import colors
from reportlab.lib.enums import TA_CENTER, TA_LEFT
import os

OUTPUT_PATH = os.path.join(os.path.dirname(__file__), "treatment_plan.pdf")

def build_pdf():
    doc = SimpleDocTemplate(
        OUTPUT_PATH,
        pagesize=letter,
        rightMargin=0.85 * inch,
        leftMargin=0.85 * inch,
        topMargin=0.9 * inch,
        bottomMargin=0.9 * inch,
    )

    styles = getSampleStyleSheet()

    header_style = ParagraphStyle("header", fontSize=16, fontName="Helvetica-Bold",
                                   textColor=colors.HexColor("#1a3f6f"), spaceAfter=4)
    subheader_style = ParagraphStyle("subheader", fontSize=10, fontName="Helvetica",
                                      textColor=colors.HexColor("#6b7e91"), spaceAfter=16)
    section_style = ParagraphStyle("section", fontSize=11, fontName="Helvetica-Bold",
                                    textColor=colors.HexColor("#1a3f6f"),
                                    spaceBefore=16, spaceAfter=6,
                                    borderPad=4)
    body_style = ParagraphStyle("body", fontSize=10, fontName="Helvetica",
                                 leading=15, textColor=colors.HexColor("#1a2e3b"),
                                 spaceAfter=6)
    label_style = ParagraphStyle("label", fontSize=9, fontName="Helvetica-Bold",
                                  textColor=colors.HexColor("#445566"), spaceAfter=2)

    story = []

    # Header
    story.append(Paragraph("APPLIED BEHAVIOR ANALYSIS (ABA) TREATMENT PLAN", header_style))
    story.append(Paragraph("Behavioral Health Services — Prior Authorization Support Document", subheader_style))
    story.append(HRFlowable(width="100%", thickness=1, color=colors.HexColor("#d0d9e4")))
    story.append(Spacer(1, 14))

    # Patient & Provider Info Table
    info_data = [
        ["PATIENT INFORMATION", "", "PROVIDER INFORMATION", ""],
        ["Patient Name:", "Marcus J. Thompson", "Treating Provider:", "Dr. Sarah K. Nguyen, BCBA-D"],
        ["Date of Birth:", "March 14, 2018", "Provider NPI:", "1437892056"],
        ["Member ID:", "AET-00291847", "Clinic Name:", "Bright Horizons ABA Center"],
        ["Insurance:", "Aetna Commercial PPO", "Tax ID:", "82-4910273"],
        ["Plan ID:", "AET-PPO-NY-2024", "Phone:", "(212) 555-0174"],
    ]
    info_table = Table(info_data, colWidths=[1.4*inch, 2.2*inch, 1.6*inch, 2.1*inch])
    info_table.setStyle(TableStyle([
        ("FONTNAME", (0, 0), (-1, 0), "Helvetica-Bold"),
        ("FONTSIZE", (0, 0), (-1, 0), 8),
        ("TEXTCOLOR", (0, 0), (-1, 0), colors.HexColor("#1a3f6f")),
        ("FONTNAME", (0, 1), (0, -1), "Helvetica-Bold"),
        ("FONTNAME", (2, 1), (2, -1), "Helvetica-Bold"),
        ("FONTSIZE", (0, 1), (-1, -1), 9),
        ("TEXTCOLOR", (0, 1), (-1, -1), colors.HexColor("#1a2e3b")),
        ("BACKGROUND", (0, 0), (-1, 0), colors.HexColor("#f0f4f8")),
        ("ROWBACKGROUNDS", (0, 1), (-1, -1), [colors.white, colors.HexColor("#f8fafc")]),
        ("BOX", (0, 0), (-1, -1), 0.5, colors.HexColor("#d0d9e4")),
        ("INNERGRID", (0, 0), (-1, -1), 0.25, colors.HexColor("#e8eef4")),
        ("TOPPADDING", (0, 0), (-1, -1), 5),
        ("BOTTOMPADDING", (0, 0), (-1, -1), 5),
        ("LEFTPADDING", (0, 0), (-1, -1), 8),
    ]))
    story.append(info_table)
    story.append(Spacer(1, 14))

    # Diagnosis
    story.append(Paragraph("1. DIAGNOSIS & CLINICAL CLASSIFICATION", section_style))
    story.append(HRFlowable(width="100%", thickness=0.5, color=colors.HexColor("#e8eef4")))
    story.append(Spacer(1, 6))
    diag_data = [
        ["ICD-10 Code", "Diagnosis Description", "Severity", "Date of Diagnosis"],
        ["F84.0", "Autism Spectrum Disorder", "Level 2 — Requiring Substantial Support", "June 3, 2021"],
        ["F80.2", "Mixed Receptive-Expressive Language Disorder", "Moderate", "June 3, 2021"],
    ]
    diag_table = Table(diag_data, colWidths=[1.0*inch, 2.8*inch, 2.2*inch, 1.3*inch])
    diag_table.setStyle(TableStyle([
        ("FONTNAME", (0, 0), (-1, 0), "Helvetica-Bold"),
        ("FONTSIZE", (0, 0), (-1, -1), 9),
        ("BACKGROUND", (0, 0), (-1, 0), colors.HexColor("#1a3f6f")),
        ("TEXTCOLOR", (0, 0), (-1, 0), colors.white),
        ("ROWBACKGROUNDS", (0, 1), (-1, -1), [colors.white, colors.HexColor("#f0f4f8")]),
        ("BOX", (0, 0), (-1, -1), 0.5, colors.HexColor("#d0d9e4")),
        ("INNERGRID", (0, 0), (-1, -1), 0.25, colors.HexColor("#e8eef4")),
        ("TOPPADDING", (0, 0), (-1, -1), 6),
        ("BOTTOMPADDING", (0, 0), (-1, -1), 6),
        ("LEFTPADDING", (0, 0), (-1, -1), 8),
    ]))
    story.append(diag_table)

    # Requested Services
    story.append(Paragraph("2. REQUESTED SERVICES & AUTHORIZATION PERIOD", section_style))
    story.append(HRFlowable(width="100%", thickness=0.5, color=colors.HexColor("#e8eef4")))
    story.append(Spacer(1, 6))
    svc_data = [
        ["CPT Code", "Service Description", "Requested Units", "Frequency", "Auth Period"],
        ["97153", "ABA Therapy — Technician-Delivered", "120 units/month", "5x per week", "6 months"],
        ["97155", "ABA Therapy — Supervision (BCBA)", "16 units/month", "As needed", "6 months"],
        ["97156", "Family Training — Caregiver Guidance", "8 units/month", "2x per month", "6 months"],
    ]
    svc_table = Table(svc_data, colWidths=[0.85*inch, 2.4*inch, 1.3*inch, 1.1*inch, 1.0*inch])
    svc_table.setStyle(TableStyle([
        ("FONTNAME", (0, 0), (-1, 0), "Helvetica-Bold"),
        ("FONTSIZE", (0, 0), (-1, -1), 9),
        ("BACKGROUND", (0, 0), (-1, 0), colors.HexColor("#1a3f6f")),
        ("TEXTCOLOR", (0, 0), (-1, 0), colors.white),
        ("ROWBACKGROUNDS", (0, 1), (-1, -1), [colors.white, colors.HexColor("#f0f4f8")]),
        ("BOX", (0, 0), (-1, -1), 0.5, colors.HexColor("#d0d9e4")),
        ("INNERGRID", (0, 0), (-1, -1), 0.25, colors.HexColor("#e8eef4")),
        ("TOPPADDING", (0, 0), (-1, -1), 6),
        ("BOTTOMPADDING", (0, 0), (-1, -1), 6),
        ("LEFTPADDING", (0, 0), (-1, -1), 8),
    ]))
    story.append(svc_table)

    # Medical Necessity
    story.append(Paragraph("3. MEDICAL NECESSITY JUSTIFICATION", section_style))
    story.append(HRFlowable(width="100%", thickness=0.5, color=colors.HexColor("#e8eef4")))
    story.append(Spacer(1, 6))
    necessity_text = """
    Marcus Thompson is a 6-year-old male presenting with Autism Spectrum Disorder (ASD), Level 2, 
    characterized by significant deficits in social communication, restricted and repetitive behaviors, 
    and sensory sensitivities that substantially impair daily functioning across home, school, and 
    community settings. A comprehensive evaluation conducted at Bright Horizons ABA Center on 
    January 12, 2026 confirmed the diagnosis and established baseline functioning across adaptive 
    behavior domains using the Vineland Adaptive Behavior Scales, Third Edition (Vineland-3).
    <br/><br/>
    Marcus demonstrates significant delays in expressive and receptive language (estimated functional 
    communication age equivalent: 2.5 years), independent daily living skills, and peer interaction. 
    He exhibits frequent maladaptive behaviors including self-injurious behavior (head-banging, 
    hand-biting) occurring at an average rate of 12 times per day, and elopement behaviors occurring 
    3–5 times per school day. These behaviors represent a safety risk and significantly limit his 
    ability to access educational programming.
    <br/><br/>
    Applied Behavior Analysis therapy delivered at the requested intensity (120 units/month of 
    direct technician-delivered therapy plus BCBA supervision) is medically necessary and consistent 
    with Aetna Clinical Policy Bulletin #0473 for ASD. Research-based ABA intervention at this 
    intensity level is the only evidence-based treatment with documented efficacy for reducing 
    maladaptive behaviors and building adaptive skill repertoires in children with Level 2 ASD. 
    Without this intervention, Marcus is at risk of regression and increased restrictiveness of 
    care environment.
    """
    story.append(Paragraph(necessity_text, body_style))

    # Treatment Goals
    story.append(Paragraph("4. TREATMENT GOALS (90-DAY TARGETS)", section_style))
    story.append(HRFlowable(width="100%", thickness=0.5, color=colors.HexColor("#e8eef4")))
    story.append(Spacer(1, 6))
    goals = [
        "Reduce self-injurious behavior (head-banging, hand-biting) from 12/day to ≤3/day as measured by direct observation data.",
        "Increase functional communication using PECS or AAC device to make 10+ independent requests per session across 3 consecutive sessions.",
        "Improve independent task completion (3-step routines) from 20% to 70% accuracy with no more than 1 prompt.",
        "Reduce elopement incidents from 3–5/day to 0–1/day across school and home settings.",
        "Increase caregiver implementation fidelity of ABA strategies to ≥80% accuracy as measured by direct observation.",
    ]
    for i, goal in enumerate(goals, 1):
        story.append(Paragraph(f"{i}.  {goal}", body_style))

    # Signature
    story.append(Spacer(1, 20))
    story.append(HRFlowable(width="100%", thickness=1, color=colors.HexColor("#d0d9e4")))
    story.append(Spacer(1, 10))
    sig_data = [
        ["Treating Provider Signature:", "Date of Plan:", "Next Review Date:"],
        ["Dr. Sarah K. Nguyen, BCBA-D", "January 30, 2026", "July 30, 2026"],
        ["License #: NY-BCBA-004821", "", ""],
    ]
    sig_table = Table(sig_data, colWidths=[2.7*inch, 2.0*inch, 2.0*inch])
    sig_table.setStyle(TableStyle([
        ("FONTNAME", (0, 0), (-1, 0), "Helvetica-Bold"),
        ("FONTSIZE", (0, 0), (-1, -1), 9),
        ("TEXTCOLOR", (0, 0), (-1, 0), colors.HexColor("#6b7e91")),
        ("FONTNAME", (0, 1), (-1, 1), "Helvetica-Bold"),
        ("TEXTCOLOR", (0, 1), (-1, 1), colors.HexColor("#1a2e3b")),
        ("FONTSIZE", (0, 2), (-1, 2), 8),
        ("TEXTCOLOR", (0, 2), (-1, 2), colors.HexColor("#6b7e91")),
        ("TOPPADDING", (0, 0), (-1, -1), 4),
    ]))
    story.append(sig_table)

    doc.build(story)
    print(f"✓ Treatment plan generated: {OUTPUT_PATH}")

if __name__ == "__main__":
    build_pdf()