# Define your item pipelines here
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
from itemadapter import ItemAdapter
class EchochainPipeline:
    def process_item(self, item):
        return item
