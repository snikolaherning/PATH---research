"""Optional document build: requires reportlab; model runtime remains stdlib only."""
from pathlib import Path
import re,html,shutil
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer, Table, TableStyle, PageBreak, Preformatted
from reportlab.lib.styles import getSampleStyleSheet,ParagraphStyle
from reportlab.lib import colors
from reportlab.lib.enums import TA_LEFT
from reportlab.lib.pagesizes import letter
ROOT=Path(__file__).resolve().parents[1]
DOC=ROOT/'docs'
styles=getSampleStyleSheet()
styles.add(ParagraphStyle(name='TitleX',fontName='Helvetica-Bold',fontSize=22,leading=26,textColor=colors.HexColor('#17394b'),spaceAfter=15))
styles.add(ParagraphStyle(name='H2X',fontName='Helvetica-Bold',fontSize=12,leading=15,textColor=colors.HexColor('#174d59'),spaceBefore=12,spaceAfter=6,keepWithNext=True))
styles.add(ParagraphStyle(name='BodyX',fontName='Helvetica',fontSize=9.5,leading=13.3,spaceAfter=7))
styles.add(ParagraphStyle(name='CellX',fontName='Helvetica',fontSize=7.5,leading=10,spaceAfter=0))
styles.add(ParagraphStyle(name='HeadCellX',parent=styles['CellX'],fontName='Helvetica-Bold',textColor=colors.white))
styles.add(ParagraphStyle(name='CodeX',fontName='Courier',fontSize=7,leading=9,spaceAfter=7))

def inline(s):
 s=s.replace('—',' - ').replace('–','-').replace('→',' -> ').replace('−','-').replace('’',"'").replace('“','"').replace('”','"').replace('×',' x ').replace('≤',' <= ').replace('÷',' / ')
 links=[]
 def link(m):
  key=f'LINKTOKEN{len(links)}';links.append((key,m.group(1),m.group(2)));return key
 s=re.sub(r'\[([^\]]+)\]\(([^)]+)\)',link,s)
 s=html.escape(s)
 s=re.sub(r'\*\*(.+?)\*\*',r'<b>\1</b>',s)
 s=re.sub(r'`([^`]+)`',r'<font name="Courier">\1</font>',s)
 for key,label,url in links:
  if url.startswith('https://'): s=s.replace(key,f'<link href="{html.escape(url,quote=True)}" color="#175d8b">{html.escape(label)}</link>')
  else:s=s.replace(key,html.escape(label))
 return s

def render_md(text):
 lines=text.splitlines();story=[];i=0
 while i<len(lines):
  line=lines[i].strip()
  if not line: i+=1;continue
  if line.startswith('```'):
   block=[];i+=1
   while i<len(lines) and not lines[i].strip().startswith('```'): block.append(lines[i]);i+=1
   # Wrapped display preserves text; original Markdown is separately unchanged.
   import textwrap
   wrapped='\n'.join('\n'.join(textwrap.wrap(x,100,replace_whitespace=False,drop_whitespace=False)) or ' ' for x in block)
   story.append(Preformatted(wrapped,styles['CodeX']));i+=1;continue
  if line.startswith('|'):
   table=[]
   while i<len(lines) and lines[i].strip().startswith('|'):
    cells=[x.strip() for x in lines[i].strip().strip('|').split('|')]
    if not all(re.fullmatch(r':?-+:?',x) for x in cells):table.append(cells)
    i+=1
   n=max(map(len,table));width=504
   widths=([95,409] if n==2 else [110,140,254] if n==3 else [92,128,128,156] if n==4 else [90]+[(width-90)/(n-1)]*(n-1))
   if table[0]==['Requirement','Evidence','Status']: widths=[120,245,139]
   data=[[Paragraph(inline(x),styles['HeadCellX'] if ri==0 else styles['CellX']) for x in row+['']*(n-len(row))] for ri,row in enumerate(table)]
   t=Table(data,colWidths=widths,repeatRows=1,hAlign='LEFT')
   t.setStyle(TableStyle([('BACKGROUND',(0,0),(-1,0),colors.HexColor('#17394b')),('VALIGN',(0,0),(-1,-1),'TOP'),('LEFTPADDING',(0,0),(-1,-1),6),('RIGHTPADDING',(0,0),(-1,-1),6),('TOPPADDING',(0,0),(-1,-1),6),('BOTTOMPADDING',(0,0),(-1,-1),6),('LINEBELOW',(0,0),(-1,-1),.3,colors.HexColor('#cbd5dd')),('ROWBACKGROUNDS',(0,1),(-1,-1),[colors.white,colors.HexColor('#f2f5f7')])]))
   story.extend([t,Spacer(1,9)]);continue
  if line.startswith('# '):story.append(Paragraph(inline(line[2:]),styles['TitleX']));i+=1;continue
  if line.startswith('##'):story.append(Paragraph(inline(line.lstrip('#').strip()),styles['H2X']));i+=1;continue
  if line=='---':story.append(Spacer(1,8));i+=1;continue
  if line.startswith('- '):story.append(Paragraph('&#8226; '+inline(line[2:]),styles['BodyX']));i+=1;continue
  para=[line.lstrip('> ')]
  i+=1
  while i<len(lines) and lines[i].strip() and not lines[i].strip().startswith(('#','|','- ','```','>')):para.append(lines[i].strip());i+=1
  story.append(Paragraph(inline(' '.join(para)),styles['BodyX']))
 return story

def footer(c,doc):
 c.setStrokeColor(colors.HexColor('#cbd5dd'));c.line(54,43,558,43)
 c.setFont('Helvetica',7);c.setFillColor(colors.HexColor('#536477'))
 c.drawString(54,31,'PATH | Submission package | Valuation 2026-10-19 | Prepared 2026-10-19')
 c.drawRightString(558,31,str(doc.page))

def build(name,parts):
 story=[]
 for i,part in enumerate(parts):
  if i:story.append(PageBreak())
  story+=render_md(part)
 out=DOC/name
 SimpleDocTemplate(str(out),pagesize=letter,leftMargin=54,rightMargin=54,topMargin=48,bottomMargin=55,title=name.replace('-',' ').replace('.pdf',''),author='Student analysis with disclosed Codex assistance').build(story,onFirstPage=footer,onLaterPages=footer)
 print(out)

if __name__=='__main__':
 build('decision-memo.pdf',[(DOC/'decision-memo.md').read_text()])
 notice='# Research evolution - checkpoint status\n\nThe next section reproduces the supplied Edition A working copy without filling its blanks, followed by Edition B. The student confirms that this exact file was submitted September 1 at 2:40 p.m. Its original Brightspace receipt has not been independently inspected. The supplied file retains its original post-receipt label and blanks. The exact supplied Markdown is preserved separately with a hash in the validation record. Do not fill original blanks retroactively or recreate pre-AI reasoning.\n'
 build('research-evolution.pdf',[(DOC/'edition-b.md').read_text(),(DOC/'edition-a-supplied-unchanged.md').read_text()])
 build('validation-and-ai-use.pdf',[(DOC/'validation-and-ai-use.md').read_text()])
 for low,up in [('decision-memo.pdf','Decision-Memo.pdf'),('research-evolution.pdf','Research-Evolution.pdf'),('validation-and-ai-use.pdf','Validation-and-AI-Use.pdf')]:shutil.copy2(DOC/low,ROOT.parent/up)
