# Define your item pipelines here
from itemadapter import ItemAdapter
class EchochainPipeline:
    def process_item(self, item):
        return item
