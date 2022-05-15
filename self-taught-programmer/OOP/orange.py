class Orange:
    def __init__(self, w, c):
        self.weight = w
        self.color = c
        self.mold = 0
        print("Created an orange!")

    def __repr__(self):
        return f"I am an orange! I weigh {self.weight} ounces and have a {self.color} color."

    def rot(self, days, temp):
        self.mold = days * temp


or1 = Orange(10, "dark orange")
print(or1)
print(or1.color)
print(or1.weight)

or1.color = "light orange"

print(or1)
or1.rot(3, 85)
print(or1.mold)
