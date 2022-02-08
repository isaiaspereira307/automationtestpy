from selenium import webdriver
from selenium.webdriver.firefox.options import Options
import argparse


#### WEB DRIVER

DRIVER_PATH = '/home/isaias/Documentos/automationtestpy/geckodriver/geckodriver'
options = Options()
options.headless = False

def pesquisa(keyword):
    driver = webdriver.Firefox(options=options, executable_path=DRIVER_PATH)  
    driver.get("https://google.com/search?q=" + keyword)
    driver.quit()


#### ARGPARSER
parser = argparse.ArgumentParser(prog="webscrapy", description='WebScraping para buscar NCM', 
                                    epilog="Author: Isaías Pereira",
                                    usage="%(prog)s [options]")

parser.version = "webscarapy cli 1.0.0"
parser.add_argument('-v','--version', action="version")
parser.add_argument('-s','--search', type=str, help='search word', nargs='*')

args = parser.parse_args()

if __name__=='__main__':
    if args.search:
        pesquisa(keyword=str(args.search))
            
