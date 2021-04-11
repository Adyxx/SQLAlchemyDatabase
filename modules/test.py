from database import *
db = Database(dbtype='sqlite', username='root', password='', dbname='animals.db')

typee = Type()
typee.full_name = "ryby"
db.create_type(typee)

animal = Animal()
animal.name = "Klaun Očkatý"
animal.typee = 1
db.create_animal(animal)

info = Info()
info.text = "Klaun očkatý (Amphiprion ocellaris) je druh tropické ryby z čeledi sapínovití (Pomacentridae) a rodu Amphiprion. Druh popsal roku 1830 Georges Cuvier."
db.create_info(info)

typee = Type()
typee.full_name = "savci"
db.create_type(typee)

animal = Animal()
animal.name = "Kočka domácí"
animal.typee = 2
db.create_animal(animal)

info = Info()
info.text = "Kočka domácí (Felis silvestris f. catus) je domestikovaná forma kočky plavé, která je již po tisíciletí průvodcem člověka. Stejně jako její divoká příbuzná patří do podčeledi malé kočky, a je typickým zástupcem skupiny."
db.create_info(info)