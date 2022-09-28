
# List : Add, insert , delete




fav_movies = ["sandlot", "the lego ", "dune"]

print(len(fav_movies)) # 3

fav_movies.append("IRON MAN")  

print(len(fav_movies)) # 3
print(fav_movies) # ["sandlot", "the lego ", "dune","IRON MAN"]

fav_movies.insert(1, "batmam")
print(fav_movies) # ["sandlot","batmam" "the lego ", "dune","IRON MAN"]

del(fav_movies[2])
print(fav_movies) # ["sandlot","batmam","dune","IRON MAN"]



#for loop

for number in range(5):
  print(number,"Hello")

for moviesList in fav_movies:
  print(moviesList)

# for Num in range(20):
#   print((Num + 1)*2)


#Dictionaries 

rating = {"sandlot":5, "the lego":7, "dune":10}
print(rating)
rating["welliom"] = 11
print(rating)
del(rating["dune"])
print(rating)


#for big string to using triple quation {""""""}

text = """
Four score and seven years ago our fathers brought forth on this continent, a new nation, 
conceived in Liberty, and dedicated to the proposition that all men are created equal.

Now we are engaged in a great civil war, testing whether that nation, or any nation so
conceived and so dedicated, can long endure. We are met on a great battle-field of that war. 
We have come to dedicate a portion of that field, as a final resting place for those who here gave their
lives that that nation might live. It is altogether fitting and proper that we should do this.
"""

print(len(text))
print(text.split())
print(len(text.split()))
