food = [(1, 25, 'Beef', 'Meal'), (2, 25, 'Cheese', 'Mea;'), (3, 50, 'Veggie', 'Other')]
drinks = [(1, 3, 'CocaCola', 'Meal'), (2, 5, 'Fanta', 'Meal')]
sides = [(1, 25, 'Garlic Bread', 'Meal'), (2, 15, 'Cheese bite', 'Meal'), (3, 5, 'Fries', 'Meal'),
         (4, 10, 'Jalapeno poppers', 'Other')]
discount_rate = 0.5
#==========================================
#Filter Menu based on customer target price
#==========================================
# def find_combo(target_price = int(input("How much is your target? "))):
#     for x in food:
#         for y in drinks:
#             for z in sides:
#                 if x[1] + y[1] + z[1] <= target_price:
#                     total = x[1] + y[1] + z[1]
#                     print("{}:{} {}:{} {}:{} = {}".format(x[0], x[2], y[0], y[2], z[0], z[2], total))

#==================================
# Discount Combo Meal
#==================================
def combo_discount():
    for j in food:
        for k in drinks:
            if j[3] =='Meal' and k[3] == 'Meal':
                total = j[1] + k[1]
                discount = total * discount_rate
                print("{}:{} {}:{} total to pay = £{}, instead of £{}".format(j[0], j[2], k[0], k[2], discount, total))


# find_combo()
combo_discount()
