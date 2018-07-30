from lxml import html
from lxml import etree
import requests

def parse_word(page):
    tree = html.fromstring(page.content)
    furigana = listing = tree.xpath('//div[@class="concept_light-representation"]')
    a=1


def main():
    page = requests.get('https://jisho.org/word/盛り')
    parse_word(page)



page = requests.get('https://jisho.org/word/%E8%A1%8C%E3%81%8F')
tree = html.fromstring(page.content)
meanings={}
meanings['japanese'] = tree.xpath('//div[@class="concept_light-representation"]/span[@class="text"]')[0].text.strip() + tree.xpath('//div[@class="concept_light-representation"]/span[@class="text"]/span')[0].text.strip()
meanings['furigana'] = tree.xpath('//div[@class="concept_light-representation"]/span[@class="furigana"]/span')[0].text
meanings['jisho-link'] = page.url
meanings['english']={}
for m in tree.xpath('//div[@class="meanings-wrapper"]')[0]:
    if m.attrib['class']=='meaning-tags':
        if m.text in ['Other forms', 'Notes']:
            cur=None
        else:
            cur=m.text
            if cur not in meanings['english']:
                meanings['english'][cur]=[]
    if cur != None and m.attrib['class']=='meaning-wrapper':
        key = m.xpath('.//span[@class="meaning-definition-section_divider"]')[0].text.strip()
        meanings['english'][cur][key]={}
        meanings['english'][cur][key]['definition']=m.xpath('.//span[@class="meaning-meaning"]')[0].text

        for i in m.xpath('.//span[@class="meaning-meaning"]'):
            meanings['english'][cur].append(i.text)


meanings