#  kwargs - mengubah input menjadi dictionary
# def fav_colors(**kwargs):
#     print(kwargs)

# fav_colors(dani="black",ruby="red",ethel="teal")

# def fav_colors(**kwargs):
#     for person, color in kwargs.items():
#         print(f"{person}'s favorite color is {color}")

# fav_colors(dani="black",ruby="red",ethel="teal")
# fav_colors(dani="black",ruby="red",ethel="teal",ted="blue")
# fav_colors(dani="my favorite color is black")

# def special_greeting(**kwargs):
#     if "dani" in kwargs and kwargs["dani"] == "special":
#         return "you get a special greeting dani !"
#     if "dani" in kwargs:
#         return f"{kwargs['dani']} dani!"
#     return "Not sure who this is..."

# print(special_greeting(dani='hello'))
# print(special_greeting(bob='hello'))
# print(special_greeting(dani='special'))

# *args
# def sum_all_num(*args):
#     total = 0
#     for num in args:
#         total += num
#     return total

# print(sum_all_num(12,12,12))

# # unpacking dictionary
# def display_name(first, second):
#     print(f"{first} says hello to {second}") 
# names={"first" : "cold","second":"rusty"}
# display_name(**names)

# def add_and_multiply_numbers(a,b,c,**kwargs):
#     print(a+b*c)
#     print("tother stuff")
#     print(kwargs)
# data = dict(a=1,b=2,c=3,d=55, name="tony")
# add_and_multiply_numbers(**data,cat="blue")

# lambda - digunakan untuk membuat anonymous function + map ( melakukan perulangan yang dipanggil di dalam lambda)
# num = [2,2,4,6,8,10]
# doubles = map(lambda x: x*2, num)
# print(list(doubles))

# people=["Darycy", "Cristina", "Dana", "Annabel"]
# peoples = map(lambda peeps: peeps.upper(), people)
# print(list(peoples))
# names=['austin', 'penny', 'anthony', 'angel', 'billy']
# a_name = filter(lambda n: n[0] == 'a', names)
# print(list(a_name))


# lambda filter
# names=['austin', 'penny', 'anthony', 'angel', 'billy']
# a_name = filter(lambda n: n[0] == 'a', names)
# print(list(a_name))


users= [
        {"username" : "samuel","tweets":["i love cake!!"]},
        {"username" : "katie","tweets":["i love my cat!"]},
        {"username" : "jeff","tweets":[]},
        {"username" : "bob123","tweets":[]},
        {"username" : "doggo_luvr","tweets":["dogs are the best"]},
        {"username" : "guitar_gal","tweets":[]}
]

# menampilkan seluruh list dengan ketentuan tweet == 0
# inactive_users = list(filter(lambda u : len(u['tweets']) == 0, users))
# print(inactive_users)

# # menampilkan hany nama dari list
# nama = list(map(lambda user: user["username"].upper(),
# filter(lambda u: not u['tweets'],users)))

# print(nama)

# #extract inactive users using list comprehension:
# inactive_users2= [user for user in users if not user["tweets"]]
# print(inactive_users2)

# usernames2 = [user["username"].upper() for user in users if not user["tweets"]]
# print(usernames2)

midterms = [80,91,78]
finals = [98,89,53]
students = ['dan', 'ang', 'kate']
# final_grades =[max(pair) for pair in zip(midterms,finals)]
# # final_grades = {t[0]:max(t[1], t[2]) for t in zip(students, midterms, finals)}


# returns dict with {student:highest score} (same thing as above) USING MAP+LAMBDA
# {'dan': 98, 'ang': 91, 'kate': 78}
# final_grades = dict(
#     zip( #menggabungkan list student dengan nilai max dari final + midterms
#         students,
#         map(
#             lambda pair: max(pair), zip(midterms, finals)
#         )
#     )
# )
# print(final_grades)
# # returns dict with student:average score
# # {'dan': 89.0, 'ang': 90.0, 'kate': 65.5}
# avg_grades = dict(
#     zip(
#         students, map(
#             lambda  pair: ((pair[0]+pair[1])/2),
#             zip(midterms, finals)
#          )
#     )
# )
# print(avg_grades)


# OOP
class User:
    def __init__(self,first_name, last_name, age):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def full_name(self):
        return f"{self.first_name} {self.last_name}"

User1 = User('fauzi','Hamdani',26)
# print(User1.first_name, User1.last_name)
print(User1.full_name())



# # class Person:
#     def __init__(self):
#         self.name = "tony"
#         self.secret = "hi"

#         self.__msg = "i love purple"
#         self.__lol= "HAHAHA"

# p = Person()
# print(p.name)
# print(p.secret)
# print(p._Person__msg)