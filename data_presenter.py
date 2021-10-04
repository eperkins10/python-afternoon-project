cupcakes_invoices = open("CupcakeInvoices.csv")

# for cupcake in cupcakes_invoices:
#     cupcake = cupcake.rstrip("\n").split(",")
#     print(cupcake[2])




cupcake_total = 0
for cupcake in cupcakes_invoices:
    cupcake = cupcake.rstrip("\n").split(",")
    amount = int(cupcake[3])
    total = float(cupcake[4])
    store_total = amount *  total
    two_dec_total = round(store_total, 2)
    print(two_dec_total)
    
    for row in cupcake:
        customer_total = float(store_total)
        customer_total = round(customer_total, 2)
        cupcake_total += customer_total
print(round(cupcake_total, 2))

    


    