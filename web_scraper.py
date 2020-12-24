import requests
from bs4 import BeautifulSoup
import re
from datetime import date, timedelta

current_year=(date.today()).strftime("%Y-%m-%d")[0:4]
months=['Enero', 'Febrero', 'Marzo', 'Abril', 'Mayo', 'Junio', 'Julio', 'Agosto', 'Septiembre', 'Octubre', 'Noviembre', 'Diciembre']

url='https://www.marca.com/en/football/real-madrid.html'
r=requests.get(url)
main_page_news=r.content

soup=BeautifulSoup(main_page_news,'html.parser')
main_page_headlines=soup.find_all('h3', 'mod-title')

#Getting the link to the articles
queries=4
list_of_links=[]
list_of_titles=[]
complete_para=[]
complete_para_final_list=[]

for i in range(0,queries):
    link_url=main_page_headlines[i].find('a')['href']
    list_of_links.append(link_url)
    
#Getting the title of the articles
    title=main_page_headlines[i].find('a')['title']
    list_of_titles.append(title)
    
#Getting the content of the headlines
    real_story=requests.get(link_url)
    story=real_story.content
    soup_content=BeautifulSoup(story,'html.parser')
    
    for x in soup_content.find_all('p','summary-lead second izquierda'):
        x.extract()
        
    main_story=soup_content.find_all('p')
    for j in range(0,len(main_story)):
        para=main_story[j].get_text()
        complete_para.append(para)
        
    complete_para_final=" ".join(complete_para)
    complete_para.clear()
    complete_para_final=re.sub('^Editions: En/football/real-madrid','',complete_para_final)
    complete_para_final=complete_para_final.replace('Unidad Editorial Información Deportiva, S.L.U. Todos los derechos reservados. Follow us Editions: En/football/real-madrid','')
    complete_para_final=complete_para_final.replace(' Unidad Editorial Información Deportiva, S.L.U. Todos los derechos reservados. Follow us','')

    for x in months:
        omission = """ © {x}
{current_year}""".format(x=x, current_year=current_year)
        complete_para_final=complete_para_final.replace(omission," ")

    complete_para_final_list.append(complete_para_final)
    
    print(list_of_titles[i])
    print(complete_para_final_list[i].strip())
    print('\n')
   

