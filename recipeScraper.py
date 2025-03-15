from bs4 import BeautifulSoup
import requests
import json


class RecipeScraper():
    def __init__(self):

        # defining standard formats for online recipes
        with open("./recipeFormats.json") as formatFile:
            self.formats = json.load(formatFile)

    def identifyFormat(self, soup):
        
        # identify which format the scraped HTML uses
        for i, format_ in enumerate(self.formats):

            # return matched format index
            if soup.select(format_["recipe"]):
                return i
            
        # return no match    
        return -1
                
    def getSelector(self, obj, soup):

        # two scenarios: 
        # 1. format identifies one element at a time by class
        # 2. format identifies groups of elements using one class

        # 1. direct identification
        select = obj
        idx = 0
        min_len = 0

        # 2. nested identification
        if type(obj) is not str:

            # get selector, item's position in results, and minimum length for valid parsed result
            select = obj["class"] 
            idx = obj["idx"]
            min_len = obj["min_len"]

        # check if selector exists and result is over minimum length   
        if select and len(soup.select(select)) >= min_len:
            return soup.select(select)[idx].text

        return ""
    
    def scrapeRecipe(self, url):
        try:

            # get url as pseudo Mozilla browser
            data = requests.get(url, headers={'User-Agent': 'Mozilla/5.0'})
            
            # parse HTML via BeautifulSoup and identify format
            soup = BeautifulSoup(data.content, features="html5lib") 
            format_id = self.identifyFormat(soup)
            
            # check if format is recognized
            if format_id != -1:

                # retrieve format
                f = self.formats[format_id]
                
                # get recipe section
                print("parsing recipe details")
                recipe = soup.select(f["recipe"])[0]

                # get recipe name
                print("parsing recipe name")
                name = soup.select(f["name"])[0].text

                # get ingredients (as HTML)
                print("parsing ingredients")
                ingredients = recipe.select(f["ingredients"])

                # get instructions as list
                print("parsing instructions")
                instructions = recipe.select(f["instructions"])[0].select("li")
                instructions = [ins.text for ins in instructions]


                # organize parsed recipe
                parsed_recipe = {
                    "src": url,
                    "name": name,
                    "cookTime": self.getSelector(f["cookTime"], soup),
                    "prepTime": self.getSelector(f["prepTime"], soup),
                    "ingredientsHtml": ingredients,
                    "instructionsList": instructions
                }

                print(parsed_recipe)

        except Exception as e:
            
            # parse failed --> print error and let user know
            print("Failed to parse recipe from ", url, e)
        



rs = RecipeScraper()
url = "https://themediterraneandish.com/mediterranean-roasted-artichoke-recipe/"
# rs.scrapeRecipe("https://themediterraneandish.com/mediterranean-roasted-artichoke-recipe/")
rs.scrapeRecipe("https://www.indianhealthyrecipes.com/palak-paneer-recipe-easy-paneer-recipes-step-by-step-pics/")
# rs.scrapeRecipe("https://www.allrecipes.com/recipe/220663/easy-marinated-artichokes/")
# rs.scrapeRecipe("https://www.allrecipes.com/ginger-sesame-cabbage-recipe-11691855")



