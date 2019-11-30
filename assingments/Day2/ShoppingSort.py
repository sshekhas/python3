Product=[
    {
    "pid":"P001",
    "name":"Mobile Phone",
    "cost":"120000",
    "brand":"Apple",
    "category":"Electronics",
    "rating":"5",
    "discount":"50"
    },
    {
    "pid":"P002",
    "name":"Television",
    "cost":"130000",
    "brand":"Onida",
    "category":"Electronics",
    "rating":"3",
    "discount":"80"
    },
     {
    "pid":"P003",
    "name":"Shirt",
    "cost":"1200",
    "brand":"Zara",
    "category":"Clothing",
    "rating":"5",
    "discount":"20"
    }
    ]


choices = [
		{
      "choice":"cost",
      "reverse":False,
      "input": 1
    },
    {
      "choice":"cost",
      "reverse":True,
      "input": 2
    },
    {
      "choice":"rating",
      "reverse":True,
      "input": 3
    },
    {
      "choice":"discount",
      "reverse":False,
      "input": 4
    },
    {
      "choice":"discount",
      "reverse":True,
      "input": 5
    },
]

while True:
    print("1. Sort by cost (Low to High)")
    print("2.Sort by cost (High to Low)")
    print("3.Sort by rating")
    print("4.Sort by discount (Low to high)")
    print("5.Sort by discount (High to low)")
    c=int(input("Enter a choice\n"))
    #Product.sort(key=lambda p:p[choices[c-1]["choice"]],reverse=choices[c-1]["reverse"])

    Product.sort(key=lambda p:p[next(filter(lambda x: (x["input"]==c), choices), None)["choice"]],reverse=next(filter(lambda x: (x["input"]==c), choices), None)["reverse"])

    print(Product)
        
    x = input("Do you want to continue? Y or N\n")
    if x == "N" or x == "n":
        break