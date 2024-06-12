from mongoengine import Document, FloatField

class Land(Document):
  width = FloatField(required=True) # Panjang
  height = FloatField(required=True) # Lebar
  local_price_per_area = FloatField(required=True) #
  tax_per_area = FloatField(required=True) # 
   
meta = {"collection" : "Lands"}