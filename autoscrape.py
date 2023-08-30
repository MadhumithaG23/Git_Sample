from autoscraper import AutoScraper
import json
import pandas as pd


url1 ='https://www.google.com/search?q=autoflake+python&rlz=1C1CHBD_enIN1054IN1054&oq=autoflake+&gs_lcrp=EgZjaHJvbWUqBwgCEAAYgAQyBggAEEUYOTIHCAEQABiABDIHCAIQABiABDIHCAMQABiABDIHCAQQABiABDIHCAUQABiABDIHCAYQABiABDIHCAcQABiABDIHCAgQABiABDIHCAkQABiABNIBCTMwNzM1ajBqN6gCALACAA&sourceid=chrome&ie=UTF-8'
wanted_list = ['autoflake']
scraper = AutoScraper()
result = scraper.build(url1,wanted_list)
print(result)