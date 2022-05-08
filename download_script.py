import os
import argparse
from selenium import webdriver
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager

parser = argparse.ArgumentParser('Download movie script')
parser.add_argument('--script_name', type=str,
                    required=True, help='Name of movie')
parser.add_argument('--link', type=str, required=True,
                    help='Link to download script')


# TODO: Parse script to make cleaner
def read_script(driver, movie_name):
    """
      Reads script and saves script into {movie_name}.txt

      :param driver: Selenium webdriver to open Google Chrome
      :type driver: ChromeDriveManager
      :param movie_name: Script title name
      :type movie_name: str
      :rtype: None
    """

    element = driver.find_element(by=By.XPATH,
                                  value='//*[@id="mainbody"]/table[2]/tbody/tr/td[3]/table/tbody/tr/td/pre')
    with open(f'scripts/{movie_name}.txt', 'w') as f:
        f.write(element.text)
        f.close()


# TODO: Automate the process of loading up database and searching and click
if __name__ == '__main__':
    if(not os.path.isdir('scripts')):
        os.mkdir('scripts')

    driver = webdriver.Chrome(ChromeDriverManager().install())
    args = parser.parse_args()
    driver.get(args.link)

    read_script(driver, args.script_name)
