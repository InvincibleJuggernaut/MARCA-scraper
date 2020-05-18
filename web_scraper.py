import requests
from bs4 import BeautifulSoup
import re
url='https://www.marca.com/en/football/real-madrid.html'
r=requests.get(url)
main_page_news=r.content

soup=BeautifulSoup(main_page_news,'html.parser')
main_page_headlines=soup.find_all('h3', 'mod-title')
#len(main_page_headlines)

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
    main_story=soup_content.find_all('p')
    for j in range(0,len(main_story)):
        para=main_story[j].get_text()
        complete_para.append(para)
    complete_para_final=" ".join(complete_para)

final_para=re.sub('^Editions: En/football/real-madrid','',final_para)
final_para=final_para.replace('Unidad Editorial Información Deportiva, S.L.U. Todos los derechos reservados. Follow us Editions: En/football/real-madrid','')
final_para=final_para.replace(' Unidad Editorial Información Deportiva, S.L.U. Todos los derechos reservados. Follow us','')
final_para=final_para.replace("""© Mayo
2020"""," ")
print(final_para)





