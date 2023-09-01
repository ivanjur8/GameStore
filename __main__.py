from model import *
from model.relacije import *
from model.cache import region, api

k = Narudzba(name="Igrica")
session.add(k)
session.commit()

ID = 1
KEY = f'Narudzba_{ID}'
k = region.get(KEY)
print(k)
if k is api.NO_VALUE:
    k = session.query(Narudzba).filter(Narudzba.id==ID).one()
    region.set(KEY, k)
print(k.name)
