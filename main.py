from random import randint, choices, sample
from Customers import Casual, Business, Regular
from Store import Store
from Tools import Painting, Concrete, Plumbing, Woodwork, Yardwork

def main():
    store = Store("HomeDepot")

    customers = []
    customers.append(Casual("Jack"))
    customers.append(Casual("David"))
    customers.append(Casual("Emily"))
    customers.append(Business("Betty"))
    customers.append(Business("John"))
    customers.append(Business("Rose"))
    customers.append(Regular("Ruby"))
    customers.append(Regular("Andrew"))
    customers.append(Regular("Helen"))
    customers.append(Regular("Paul"))

    for i in range(20):
        if i<4:
            store.addTools(Painting("Painting_tool_"+str(i),10))
        elif i<8:
            store.addTools(Concrete("Concrete_tool_"+str(i),20))
        elif i<12:
            store.addTools(Plumbing("Plumbing_tool_"+str(i),35))
        elif i<16:
            store.addTools(Woodwork("Woodwork_tool_"+str(i),55))
        else:
            store.addTools(Yardwork("Yardwork_tool_"+str(i),100))

    for i in range(34):
        #return tools before the store opens
        for customer in customers:
            tools = customer.get_returns()
            if tools:
                for t in tools:
                    store.give_back(customer,t)
                    customer.return_tool(t)
                    t.returned()
        
        #store opens, customers can enter only when store has tools
        candidates = []
        for c in customers:
            if len(c.get_rental())<3:
                candidates.append(c)
        
        cus = choices(candidates, k = randint(0,len(candidates)))
        # available_tools = store.get_tools()
        for c in cus:
            if not store.isempty():
                if isinstance(c, Business) and store.num_tools()>=3:
                    rent_tools = sample(store.get_tools(),k=3)
                    c.rent(rent_tools,7)
                    for rt in rent_tools:
                        rt.rent()
                        store.rent(c,rt,7)
                        
                if isinstance(c, Regular):
                    if store.num_tools() >= 3:
                        rent_tools = sample(store.get_tools(),k=randint(1,3))
                        nights = randint(3,5)
                        c.rent(rent_tools,nights)
                        for rt in rent_tools:
                            rt.rent()
                            store.rent(c,rt,nights)
                    elif store.num_tools() ==2 :
                        rent_tools = sample(store.get_tools(),k=randint(1,2))
                        nights = randint(3,5)
                        c.rent(rent_tools,nights)
                        for rt in rent_tools:
                            rt.rent()
                            store.rent(c,rt,nights)
                    else:
                        rent_tools = store.get_tools()
                        nights = randint(3,5)
                        c.rent(rent_tools,nights)
                        rent_tools[0].rent()
                        store.rent(c,rent_tools[0],nights)

                if isinstance(c, Casual):
                    if store.num_tools() > 1:
                        rent_tools = sample(store.get_tools(),k=randint(1,2))
                        nights = randint(1,2)
                        c.rent(rent_tools,nights)
                        for rt in rent_tools:
                            rt.rent()
                            store.rent(c,rt,nights)
                    else:
                        rent_tools = store.get_tools()
                        nights = randint(1,2)
                        c.rent(rent_tools,nights)
                        rent_tools[0].rent()
                        store.rent(c,rent_tools[0],nights)

            else:
                break

    rental = store.get_rental()
    print("Total rental:")
    for re in rental:
        print(re["customer"].get_name(),"rent",re["tool"].get_name(),"for",re["nights"], "nights in total",re["price"], "dollars.")
    print("Total income in 35 days:")
    print(store.get_income(),"dollars")
    print(store.num_tools(),"tools remaing in store:")
    for t in store.get_tools():
        print(t.get_name())

    print("Active rental:")
    for re in rental:
        if re["active"]:
            print(re["customer"].get_name(),"rent",re["tool"].get_name(),"for",re["nights"], "nights in total",re["price"], "dollars.")
    



if __name__ == '__main__':
    main()