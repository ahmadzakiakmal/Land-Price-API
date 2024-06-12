from mongoengine import Document, FloatField, StringField

class Land(Document):
  width = FloatField(required=True) # Panjang
  length = FloatField(required=True) # Lebar
  local_price_per_area = FloatField(required=True) #
  tax_per_area = FloatField(required=True) # 
  city = StringField(required=True)
   
meta = {"collection" : "Lands"}