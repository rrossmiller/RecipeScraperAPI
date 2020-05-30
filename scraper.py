from selenium import webdriver
from selenium.webdriver.chrome.options import Options

def halfBakedHarvest(recipeLink):
    chrome_options = Options()
    # chrome_options = webdriver.ChromeOptions()
    chrome_options.add_argument("--headless")
    chrome_options.add_argument('--no-sandbox')
    driver = None
    try:
        driver = webdriver.Chrome('./chromedriver', options=chrome_options)
    except:
        print('check the chrome driver')

    driver.get(recipeLink)
    ingredientsElems = driver.find_elements_by_class_name('wprm-recipe-ingredients')
    ingredientsRaw = []
    for elem in ingredientsElems:
        # comment_ids.append(i.get_attribute('id'))
        ingr = elem.text
        ingredientsRaw.append(ingr.split('\n'))

    driver.quit()

    ingredientsList = [y for x in ingredientsRaw for y in x]
    return ingredientsList


if __name__ == '__main__':
    link = input('paste link: ')
    ingredients = halfBakedHarvest(link)
    outList = []
    for x in ingredients:
        line = '\t<li>'+ x + '</li>'
        outList.append(line)

    outString = '<ul>\n'+ "\n".join(outList) + '\n</ul>'

    with open('recipe.html','w') as outfile:
        outfile.write(outString)