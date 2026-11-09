import json, math, os, html
from reportlab.pdfgen import canvas
from reportlab.lib.colors import HexColor, Color
from reportlab.lib.pagesizes import A4
from reportlab.platypus import Paragraph
from reportlab.lib.styles import ParagraphStyle

ROOT=os.path.dirname(__file__)
D=json.load(open(os.path.join(ROOT,'atlas-content.json'),encoding='utf-8'))
OUT=os.path.join(ROOT,'dist','assets','dr-ahmad-atlas.pdf')
W,H=A4
wine=HexColor('#80631c'); cream=HexColor('#f8f6ef'); ink=HexColor('#302c28'); muted=HexColor('#6d6860'); line=HexColor('#dfd8cc'); sage=HexColor('#ede4c9')
c=canvas.Canvas(OUT,pagesize=A4)
c.setTitle('Dr. Ahmad Atlas')
c.setAuthor('Dr. Ahmad Atlas')
BODY=ParagraphStyle('body',fontName='Helvetica',fontSize=9.1,leading=13.3,textColor=ink)
SMALL=ParagraphStyle('small',fontName='Helvetica',fontSize=7.2,leading=10.2,textColor=muted)
def clean(t):
 return t.replace('\u2011','-').replace('\u2013','-').replace('\u2014','-').replace('\u2019',"'").replace('\u2018',"'").replace('\u201c','"').replace('\u201d','"').replace('\u2260','is not')
def para(t,x,y,width,style=BODY):
 p=Paragraph(html.escape(clean(t)),style); _,height=p.wrap(width,1000); p.drawOn(c,x,y-height); return y-height
def text(t,x,y,size=10,font='Helvetica',color=ink):
 c.setFillColor(color);c.setFont(font,size);c.drawString(x,y,clean(t))
def footer(page,label='DR. AHMAD ATLAS / 9 NOVEMBER 2026'):
 c.setStrokeColor(line);c.line(40,42,W-40,42)
 text(label,40,28,6.5,color=muted);c.setFillColor(wine);c.setFont('Helvetica',7);c.drawRightString(W-40,28,str(page))
def new_page(title,chapter,page):
 c.setFillColor(cream);c.rect(0,0,W,H,fill=1,stroke=0)
 text('DR. AHMAD ATLAS',40,H-39,8,'Helvetica-Bold',wine)
 c.setFont('Helvetica',7);c.drawRightString(W-40,H-39,chapter.upper())
 c.setStrokeColor(wine);c.line(40,H-50,W-40,H-50)
 text(title,40,H-93,31,'Times-Roman',wine)
 footer(page)
def diagram(cat,x,y,w=220,h=140):
 c.saveState();c.translate(x,y);c.scale(w/280,h/180)
 c.setFillColor(HexColor('#f0e9de'));c.roundRect(0,0,280,180,5,fill=1,stroke=0)
 c.setStrokeColor(HexColor('#aa7f70'));c.setLineWidth(1.2)
 if cat in (0,2,3):
  for yy,height,col in [(25,27,'#e2cda6'),(52,42,'#edcfc0'),(94,15,'#e7b5a0')]:
   c.setFillColor(HexColor(col));c.rect(25,yy,230,height,fill=1,stroke=0)
  for i in range(8):
   c.setStrokeColor(HexColor('#c38b87'));c.ellipse(32+i*27,65,52+i*27,79,fill=0,stroke=1)
  if cat==0:
   c.setStrokeColor(HexColor('#7e9683'))
   for xx in (72,137,202):
    c.line(xx,123,xx,150);c.line(xx,150,xx-5,145);c.line(xx,150,xx+5,145)
   label='THE SURFACE IS A BARRIER'
  elif cat==2:
   c.setStrokeColor(HexColor('#8c9c8b'));c.setLineWidth(15);c.line(105,156,157,119)
   c.setStrokeColor(wine);c.setLineWidth(1.5);c.line(157,119,176,99);c.circle(176,96,15,fill=0,stroke=1)
   label='ENERGY AND TISSUE / CONCEPT ONLY'
  else:
   c.setFillColor(HexColor('#a87a65'));c.ellipse(115,102,150,129,fill=1,stroke=0)
   c.setStrokeColor(HexColor('#7e9683'));c.setLineWidth(2);c.circle(132,114,30,fill=0,stroke=1);c.setLineWidth(6);c.line(110,91,87,68)
   label='ASSESS THE LESION FIRST'
 elif cat==1:
  c.setFillColor(HexColor('#e7c9b5'));c.ellipse(92,35,188,154,fill=1,stroke=1)
  c.setStrokeColor(HexColor('#a77e6e'));c.setLineWidth(1.5);c.line(113,109,125,109);c.line(156,109,168,109);c.line(139,104,134,85);c.line(134,85,144,83);c.arc(124,64,155,80,180,180)
  c.setFillColor(HexColor('#d69d91'));c.circle(112,87,7,fill=1,stroke=0);c.circle(166,87,7,fill=1,stroke=0)
  label='INDIVIDUAL ANATOMY MATTERS'
 elif cat==4:
  for xx,col,level in [(86,'#b97076',69),(156,'#d4b17d',50)]:
   c.setStrokeColor(HexColor('#80917c'));c.setFillColor(HexColor('#f8f5eb'));c.roundRect(xx,35,39,105,10,fill=1,stroke=1);c.setFillColor(HexColor(col));c.rect(xx+4,40,31,level,fill=1,stroke=0);c.setFillColor(sage);c.rect(xx-1,136,41,13,fill=1,stroke=1)
  label='MEASURE / INTERPRET / REVIEW'
 else:
  c.setFillColor(sage);c.setStrokeColor(HexColor('#839675'));c.ellipse(72,29,208,160,fill=1,stroke=1)
  c.setFillColor(HexColor('#eddcbd'));c.ellipse(88,46,193,147,fill=1,stroke=1)
  c.setFillColor(HexColor('#d7a8a2'));c.ellipse(119,70,164,122,fill=1,stroke=0)
  c.setFillColor(HexColor('#aa777c'));c.circle(142,96,9,fill=1,stroke=0)
  c.setFillColor(HexColor('#8da58d'));c.ellipse(98,92,109,113,fill=1,stroke=0);c.ellipse(170,67,181,88,fill=1,stroke=0)
  label='BIOLOGY NEEDS CONTEXT'
 c.setFont('Helvetica',6.5);c.setFillColor(muted);c.drawCentredString(140,12,label);c.restoreState()

# Cover
c.setFillColor(HexColor('#090909'));c.rect(0,0,W,H,fill=1,stroke=0)
c.setStrokeColor(HexColor('#bca06c'));c.rect(25,25,W-50,H-50,fill=0,stroke=1);c.rect(32,32,W-64,H-64,fill=0,stroke=1)
c.drawImage(os.path.join(ROOT,'dist','assets','hsa-logo.png'),W/2-42,676,84,84,mask='auto');c.setFillColor(HexColor('#d5af48'));c.setFont('Times-Roman',24);c.drawCentredString(W/2,650,'DR. AHMAD')
c.setFont('Times-Bold',92);c.drawCentredString(W/2,552,'ATLAS')
c.setFont('Times-Italic',29);c.drawCentredString(W/2,490,'A clearer picture.')
c.setFont('Helvetica',10);c.drawCentredString(W/2,438,'FACIAL SKINCARE')
c.setStrokeColor(HexColor('#c7b18b'));c.line(250,402,345,402)
c.setFont('Helvetica',11);c.drawCentredString(W/2,362,'9 REFERENCE SHEETS')
c.drawCentredString(W/2,340,'3 CHAPTERS / 3 COMPANION WORKSHEETS')
c.setFont('Helvetica',8);c.drawCentredString(W/2,128,'Prepared 9 November 2026 / General education, not medical advice')
c.showPage()

# Index
new_page('Your reference index','Start here',2)
para('Use these sheets to explore a topic and prepare questions for your clinician. They do not diagnose conditions, establish suitability or provide procedural instructions.',40,H-122,W-80)
for ci,cat in enumerate(D['categories']):
 col=ci%2;row=ci//2;x=40+col*265;y=H-200-row*145
 text(f'0{ci+1} / {cat["name"]}',x,y,17,'Times-Roman',wine)
 for n,g in enumerate([v for v in D['guides'] if v['category']==ci]):
  yy=y-28-n*21;text(f'{g["id"]:03d}  {g["title"]}',x,yy,8.7)
  c.linkAbsolute(g['title'],f'sheet-{g["id"]}',(x,yy-3,x+240,yy+12),thickness=0)
text('COMPANION WORKSHEETS',40,173,8,'Helvetica-Bold',wine)
for i,b in enumerate(D['bonuses']):
 text(f'{i+1}. {b["title"]}',40,151-i*21,10)
 c.linkAbsolute(b['title'],f'bonus-{i}',(40,148-i*21,400,164-i*21),thickness=0)
text('Edition notes and source context appear on the final page.',40,66,8,color=muted)
c.showPage()

for g in D['guides']:
 c.bookmarkPage(f'sheet-{g["id"]}');c.addOutlineEntry(f'{g["id"]:03d} {g["title"]}',f'sheet-{g["id"]}',0)
 new_page(g['title'],f'Sheet {g["id"]:03d} / '+D['categories'][g['category']]['name'],g['id']+2)
 para(g['subtitle'],40,H-115,W-80,SMALL)
 c.drawImage(os.path.join(ROOT,'dist','assets','photos',f'{g["id"]:03d}.jpg'),170,H-290,255,155,preserveAspectRatio=True,anchor='c')
 para(g['caption'],85,H-297,W-170,SMALL)
 top=H-332;cw=245
 for i,(heading,body) in enumerate(zip(D['headings'],g['sections'])):
  x=40+(i%2)*270;y=top-(i//2)*112
  c.setStrokeColor(line);c.line(x,y+8,x+cw,y+8)
  text(f'0{i+1} / {heading}',x,y-6,9,'Helvetica-Bold',wine)
  bottom=para(body,x,y-18,cw)
  if bottom<y-101:raise ValueError(f'Overflow in sheet {g["id"]} section {i}')
 sy=H-684
 text('SOURCES AND CONTEXT',40,sy,7,'Helvetica-Bold',wine)
 for key in g['sources']:
  sy-=13;name,url=D['sources'][key];text(name,40,sy,6.9,color=muted);c.linkURL(url,(40,sy-2,W-40,sy+9),relative=0,thickness=0)
 para('Clinic links identify business topics, not independent proof of benefit. Other links offer selected further reading. Sources do not endorse this Atlas. Individual clinical assessment is required.',40,sy-12,W-80,SMALL)
 c.showPage()

for i,b in enumerate(D['bonuses']):
 c.bookmarkPage(f'bonus-{i}');c.addOutlineEntry(b['title'],f'bonus-{i}',0)
 new_page(b['title'],f'Companion worksheet {i+1}',12+i)
 para(b['subtitle'],40,H-118,W-80)
 c.drawImage(os.path.join(ROOT,'dist','assets','photos',f'companion-{i+1}.jpg'),40,H-247,120,110,preserveAspectRatio=True,anchor='w')
 for n,(heading,body) in enumerate(b['sections']):
  y=H-275-n*104
  text(f'0{n+1} / {heading}',40,y,16,'Times-Roman',wine)
  bottom=para(body,40,y-14,W-80,BODY)
  for yy in (y-59,y-73,y-87):c.setStrokeColor(line);c.line(40,yy,W-40,yy)
 c.showPage()
new_page('About this edition','Sources and edition notes',15)
c.drawImage(os.path.join(ROOT,'dist','assets','photos','director.jpg'),42,H-219,84,102,preserveAspectRatio=True,anchor='c')
text('Dr. Ahmad',145,H-145,18,'Times-Roman',wine)

notes=[
 ('About the Atlas','Nine facial skincare topics, arranged in three chapters. Each sheet includes a photograph, six short sections and links for further reading.'),
 ('How sources are used','The sheets link to clinic information and selected patient guidance from the NHS, American Academy of Dermatology and US FDA. Clinic links identify topics; they do not independently establish benefit.'),
 ('What this collection does','The sheets offer general explanations and questions for a consultation. The photographs provide editorial context. No personalised diagnosis, treatment plan, outcome guarantee or prescribing advice is provided.'),
 ('Using the worksheets','The companion pages are for your own notes. Keep completed copies private. Follow written instructions from your treating clinician; the worksheets do not replace preparation, aftercare or urgent-contact advice.'),
 ('Business sources','Harley Street Aesthetics: harleystreetaesthetic.co.uk\nHarley Street Medics: harleystreetmedics.clinic\nHarley Street Medical Wellness: harleystreetmedicalwellness.co.uk')]
y=H-250
for heading,body in notes:
 text(heading,40,y,18,'Times-Roman',wine);y=para(body,40,y-15,W-80)-30
c.showPage();c.save();print(OUT)
