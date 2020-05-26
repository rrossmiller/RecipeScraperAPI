from selenium import webdriver
from selenium.webdriver.chrome.options import Options

def halfBakedHarvest(recipeLink):
    chrome_options = Options()
    chrome_options.add_argument("--headless")
    driver = webdriver.Chrome('./chromedriver', options=chrome_options)

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
    # outString = '<ul>\n'
    # ingredients = []
    # for x in ingredientsRaw:
    #     for y in x:
    #         line = '\t<li>'+ y + '</li>'
    #         ingredients.append(line)
    #
    # outString = outString + "\n".join(ingredients) + '\n</ul>'
    #
    # with open('recipe.html','w') as outfile:
    #     outfile.write(outString)
