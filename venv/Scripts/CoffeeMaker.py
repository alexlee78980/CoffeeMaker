import CoffeeMakerData
res = CoffeeMakerData.resources
menu = CoffeeMakerData.MENU
money  = 0
def report():
    water = res.get("water")
    milk = res.get("milk")
    coffee = res.get("coffee")
    print(f"Water: {water}ml")
    print(f"Milk: {milk}ml")
    print(f"Coffee: {coffee}g")
    print(f"Money: ${money}")

def check_requirements(order):
    ingredients = menu.get(order).get("ingredients")
    for i in ingredients:
        resource = res.get(i)
        need = ingredients.get(i)
        if resource < need:
            return i
    return "enough"

def use_resource(order):
    ingredients = menu.get(order).get("ingredients")
    for i in ingredients:
        resource = res.get(i)
        need = ingredients.get(i)
        res[i] = resource - need


while True:
    command = input("What would you like? (espresso/latte/cappuccino): ")
    command = command.lower()
    if(command == "report"):
        report()
    else:
        check = check_requirements(command)
        if(check == "enough"):
            print("Please insert coins.")
            q = int(input("how many quarters?: "))
            d = int(input("how many dimes?: "))
            n = int(input("how many nickles?: "))
            p = int(input("how many pennies?: "))
            total =  round(q*0.25 + d*0.1 + n*0.05 + p*0.01, 2)
            cost = menu.get(command).get("cost")
            if(total > cost):
                use_resource(command)
                change = total-cost
                money += cost
                print(f"Here is ${change} in  change.")
                print(f"Here is your {command}. Enjoy!")
        else:
            print(f"Sorry there is not enough {check}")

