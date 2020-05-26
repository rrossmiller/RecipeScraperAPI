from selenium import webdriver
from selenium.webdriver.chrome.options import Options
chrome_options = Options()
chrome_options.add_argument("--headless")
import time
driver = webdriver.Chrome('./chromedriver', options=chrome_options)

link = input('paste the link: ')
driver.get(link)

# ingredientsElem = driver.find_elements_by_xpath('//*[@id="bo-recipe"]/div[3]')[0]
# ingredientsElems = driver.find_elements_by_xpath("//*[contains(@id,'bo-recipe')]/div[3]")
ingredientsElems = driver.find_elements_by_class_name('wprm-recipe-ingredients')
ingredientsRaw = []
for elem in ingredientsElems:
    # comment_ids.append(i.get_attribute('id'))
    ingr = elem.text
    ingredientsRaw.append(ingr.split('\n'))
    print(ingredientsRaw)
    print()

driver.quit()

outString = '<ul>\n'
ingredients = []
for x in ingredientsRaw:
    for y in x:
        line = '\t<li>'+ y + '</li>'
        ingredients.append(line)

outString = outString + "\n".join(ingredients) + '\n</ul>'

with open('recipe.html','w') as outfile:
    outfile.write(outString)
