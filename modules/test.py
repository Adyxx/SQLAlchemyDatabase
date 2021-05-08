from database import *
db = Database(dbtype='sqlite', username='root', password='', dbname='animals.db')

type1 = Type()
type1.full_name = "fish"
db.create_type(type1)

type2 = Type()
type2.full_name = "mammal"
db.create_type(type2)

type3 = Type()
type3.full_name = "reptile"
db.create_type(type3)

type4 = Type()
type4.full_name = "bird"
db.create_type(type4)

type5 = Type()
type5.full_name = "amphibian"
db.create_type(type5)

type6 = Type()
type6.full_name = "invertebrate"
db.create_type(type6)




animal1 = Animal()
animal1.name = "Clownfish"
animal1.typee = "fish"
db.create_animal(animal1)

photo1 = Photo()
photo1.title = "Clownfish"
photo1.source = "https://www.zoohit.cz/magazin/wp-content/uploads/2018/12/Klaunni-ryba.jpg"
db.create_photo(photo1)


animal2 = Animal()
animal2.name = "Red Kangaroo"
animal2.typee = "mammal"

db.create_animal(animal2)

photo2 = Photo()
photo2.title= "Red Kangaroo"
photo2.source = "https://ichef.bbci.co.uk/news/976/cpsprodpb/A6CA/production/_103589624_011717548.jpg"
db.create_photo(photo2)


animal3 = Animal()
animal3.name = "Loggerhead sea turtle"
animal3.typee = "reptile"

db.create_animal(animal3)

photo3 = Photo()
photo3.title= "Loggerhead sea turtle"
photo3.source = "https://upload.wikimedia.org/wikipedia/commons/thumb/8/8e/Loggerhead_sea_turtle.jpg/800px-Loggerhead_sea_turtle.jpg"
db.create_photo(photo3)


animal4 = Animal()
animal4.name = "Blue-and-yellow macaw"
animal4.typee = "bird"

db.create_animal(animal4)

photo4 = Photo()
photo4.title= "Blue-and-yellow macaw"
photo4.source = "https://upload.wikimedia.org/wikipedia/commons/6/6d/Blue-and-Yellow-Macaw.jpg"
db.create_photo(photo4)





animal5 = Animal()
animal5.name = "Polar fox"
animal5.typee = "mammal"

db.create_animal(animal5)

photo5 = Photo()
photo5.title= "Polar fox"
photo5.source = "https://upload.wikimedia.org/wikipedia/commons/thumb/8/83/Iceland-1979445_%28cropped_3%29.jpg/270px-Iceland-1979445_%28cropped_3%29.jpg"

db.create_photo(photo5)





animal6 = Animal()
animal6.name = "American bullfrog"
animal6.typee = "amphibian"

db.create_animal(animal6)

photo6 = Photo()
photo6.title= "American bullfrog"
photo6.source = "https://upload.wikimedia.org/wikipedia/commons/thumb/a/aa/North-American-bullfrog1.jpg/220px-North-American-bullfrog1.jpg"
db.create_photo(photo6)





animal7 = Animal()
animal7.name = "Meliponines"
animal7.typee = "invertebrate"

db.create_animal(animal7)

photo7 = Photo()
photo7.title= "Meliponines"
photo7.source = "https://upload.wikimedia.org/wikipedia/commons/1/12/Meliponula_ferruginea.jpg"
db.create_photo(photo7)