from IPython.display import display, clear_output

def main():
    showIntro()
    global testData
    global taxRate
    taxRate = 0.06
    testData = [
    {'name': 'Apple', 'quantity': '5', 'price': '.89'},
    {'name': 'Pear', 'quantity': '3', 'price': '.59'},
    {'name': 'Banana', 'quantity': '7', 'price': '.19'}
    ]
    cart = []
    showMenu(cart)
    return
    
def showIntro():
    print("")
    print("           ************************")
    print("           *  Shopping Cart 1.0   *")
    print("           ************************")
    return

def showOutro():
    print("")
    print("==============================================")
    print("      Thank you for using Shopping Cart!")
    print("==============================================")
    return

def showMenuHeader():
    print("")
    print("==============================================")
    print("                  Main Menu")
    print("==============================================")
    return

def showMenu(cart):
    while True:
        showMenuHeader()
        print("")
        print(f"Total cart items:  {len(cart)}")
        print(f"Total item qty:    {getTotalQty(cart)}")
        print(f"Total cart value: ${getSubTotal(cart)}")
        print("")
        print("Enter the number of your choice:")
        print("1) Add Item")
        print("2) Delete Item")
        print("3) Update Item")
        print("4) Display Receipt")
        print("5) Search Items")
        print("6) Quit")
        print("")
        print("9) (Re)Load Test Data")
        print("")
        x = input("Menu #: ")
        if x.isdigit():
            x = int(x)
        if x == 1:
            addEntry(cart)
        elif x == 2:
            delEntry(cart)
        elif x == 3:
            updateEntry(cart)
        elif x == 4:
            showEntries(cart)
        elif x == 5:
            searchEntries(cart)
        elif x == 6:
            showEntries(cart,True)
            showOutro()
            break
        elif x == 9:
            loadTestData(cart)
    return

    
def searchEntries(cart):
    if preCheck(cart) == False: return
    
    print("")
    print("==============================================")
    print("               Search Items")
    print("==============================================")
    
    sval = input("Enter the item to search for: ")
    rval = isKeyValid(cart, sval)
    
    if rval != False:
        print(f"Found entry for {sval.capitalize()}!")
        print(f"Quantity: {getQty(cart,sval)}")
        print(f"Unit Price: ${getPrice(cart,sval)}")
        print(f"Subtotal: ${getQty(cart,sval,True)*getPrice(cart,sval,True)}")
        waitforuser()
        return
    else:
        print("No items found with that name!")
        waitforuser()
        return
    
    print("Problem in search function. Contact developer.")
    return

def addEntry(cart):
    print("")
    print("==============================================")
    print("                   Add Item")
    print("==============================================")
    sval = input("Enter the item to add: ")
    if isKeyValid(cart,sval) == True:
        print("Cannot add duplicate item!")
        waitforuser()
        return
    else:      
        if sval != "":
            uname = sval.capitalize()
        else:
            print("Item name cannot be blank")
            return
        
        print("")
        uqty = input("Enter quantity: ")
        
        if uqty.isdigit == False:
            print("Invalid quantity!")
            uqty = 1
            print(f"Quantity will be set to 1")
        else:
            try:
                if int(uqty) > 0:
                    uqty = int(uqty)
                else:
                    print("Cannot set quantity to 0")
                    uqty = 1
                    print(f"Quantity will be set to 1")
            except:
                print("Problem with quantity input")
                uqty = 1
                print(f"Quantity will remain: {uqty}")
        
        print("")
        uprc = input("Enter price: ")
        try:
            uprc = float(uprc)
            if uprc >= 0:
                pass
            else:
                print("Price cannot be negative")
                uprc = 1.00
                print(f"Price will be set to: $1.00")
        except:
            print("Invalid price!")
            uprc = 1.00
            print(f"Price will be set to: $1.00")
            
        print("")
        
        addListEntry(cart,uname,uqty,uprc)
        
        waitforuser()
        return
    
    print("Problem in update function. Contact developer.")
    return

def updateEntry(cart):
    if preCheck(cart) == False: return
    print("")
    print("==============================================")
    print("                Update Item")
    print("==============================================")
    sval = input("Enter the item to update: ")
    if isKeyValid(cart,sval) == False:
        print("No entries found with that name!")
        waitforuser()
        return
    else:
        print(f"Found entry for {sval.capitalize()}!")
        print(f"Quantity: {getQty(cart,sval)}")
        print(f"Unit Price: ${getPrice(cart,sval)}")
        print(f"Subtotal: ${getQty(cart,sval,True)*getPrice(cart,sval,True)}")
        print("")
        uqty = input("Enter updated quantity or -1 to leave as-is: ")
        
        if uqty == "-1":
            uqty = getQty(cart,sval)
            print(f"Quantity will remain: {uqty}")
        else:
            if uqty.isdigit == False:
                print("Invalid quantity!")
                uqty = getQty(cart,sval)
                print(f"Quantity will remain: {uqty}")
            else:
                try:
                    if int(uqty) > 0:
                        uqty = int(uqty)
                        print("Quantity updated!") if updQty(cart,sval,uqty) == True else print("Quantity NOT updated!")
                    else:
                        print("Cannot set quantity to 0")
                        print("Use DELETE function instead")
                        uqty = getQty(cart,sval)
                        print(f"Quantity will remain: {uqty}")
                except:
                    print("Problem with quantity input")
                    uqty = getQty(cart,sval)
                    print(f"Quantity will remain: {uqty}")
        
        print("")
        uprc = input("Enter updated price or -1 to leave as-is: ")
        try:
            uprc = float(uprc)
            if uprc == -1:
                uprc = getPrice(cart,sval)
                print(f"Price will remain: ${uprc}")
            elif uprc >= 0:
                print("Price updated!") if updPrc(cart,sval,uprc) == True else print("Price NOT updated!")
            else:
                print("Price cannot be negative")
                uprc = getPrice(cart,sval)
                print(f"Price will remain: ${uprc}")
        except:
            print("Invalid price!")
            uprc = getPrice(cart,sval)
            print(f"Price will remain: ${uprc}")
            
        print("")
        waitforuser()
        return
    
    print("Problem in update function. Contact developer.")
    return
    
def delEntry(cart):
    if preCheck(cart) == False: return
    print("")
    print("==============================================")
    print("                Delete Item")
    print("==============================================")
    sval = input("Enter the item to delete: ")
    if isKeyValid(cart,sval) == False:
        print("No items found with that name!")
        waitforuser()
        return
    else:
        print(f"Found entry for {sval.capitalize()}!")
        print(f"Quantity: {getQty(cart,sval)}")
        print(f"Unit Price: ${getPrice(cart,sval)}")
        print(f"Subtotal: ${getQty(cart,sval,True)*getPrice(cart,sval,True)}")
        print("")
        uval = input("Confirm deletion by typing 'D' (uppercase) or 0 to cancel: ")
        if uval.isdigit():
            if int(uval) == 0:
                print("Delete canceled!")
                waitforuser()
                return
        if uval == "D":
            delItem(cart,sval)
            print("Delete completed!")
            waitforuser()
            return
        else:
            print("Confirmation Failed! Entry was not deleted")
            waitforuser()
            return
    
    print("Problem in delete function. Contact developer.")
    return
    
def showEntries(cart,noWait=False):
    if preCheck(cart) == False: return
    print("")
    print("==============================================")
    print("                   Receipt")
    print("==============================================")
    for i in cart:
        print(f"Name: {i.get('name')}\nQty: {i.get('quantity')}\nUnit Price: ${i.get('price')}\nTotal Unit Price: ${round(float(i.get('price'))*int(i.get('quantity')),2)}")
        print("")
    print("==============================================")
    print(f"Total Items: {getTotalQty(cart)}")
    print(f"Subtotal: ${getSubTotal(cart)}")
    print(f"Tax: ${getTaxCart(cart)}")
    print(f"Total: ${getTotalCart(cart)}")
    if noWait == False: waitforuser()
    return

def loadTestData(cart):
    print("")
    print("==============================================")
    print("               Test Data")
    print("==============================================")
    print("")
    print("Warning: Test Data may overwrite existing entries!")
    print("")
    uval = input("Confirm by typing 'OK' (uppercase) or 0 to cancel: ")
    if uval.isdigit():
        if int(uval) == 0:
            print("Test canceled!")
            waitforuser()
            return
    if uval == "OK":
        for data in testData:
            if data not in cart:
                cart.append(data)
        print("Test data integrated!")
        waitforuser()
        return
    else:
        print("Confirmation Failed! Test aborted")
        waitforuser()
        return

def preCheck(cart):
    if len(cart) == 0:
        print("")
        print("==============================================")
        print("               No Entries")
        print("==============================================")
        waitforuser()
        return False
    else:
        return True
    
def clr():
    clear_output(wait=True)
    
def waitforuser():
    print("")
    input("         Press Enter to continue              ")
    return

def getName(cart,name):
    if isKeyValid(cart,name):
        for item in cart:
            if item.get('name').lower() == name.lower():
                return item.get('name').capitalize()
    else:
        return -1
    
def getQty(cart,name,asNumber=False):
    if isKeyValid(cart,name):
        if asNumber == False:
            for item in cart:
                if item.get('name').lower() == name.lower():
                    return item.get('quantity')
        else:
            for item in cart:
                if item.get('name').lower() == name.lower():
                    return int(item.get('quantity'))
    else:
        return -1

def addListEntry(cart,name,qty,price):
    cart.append({'name': f"{name}", 'quantity': f"{qty}", 'price': f"{price}"})
    
def updQty(cart,name,newqty):
    if isKeyValid(cart,name):
        for item in cart:
            if item.get('name').lower() == name.lower():
                item.update({'quantity': str(newqty)})
            return True
    else:
        return False

def updPrc(cart,name,newprc):
    if isKeyValid(cart,name):
        for item in cart:
            if item.get('name').lower() == name.lower():
                item.update({'price': str(newprc)})
            return True
    else:
        return False

def getPrice(cart,name,asNumber=False):
    if isKeyValid(cart,name):
        if asNumber == False:
            for item in cart:
                if item.get('name').lower() == name.lower():
                    return item.get('price')
        else:
            for item in cart:
                if item.get('name').lower() == name.lower():
                    return round(float(item.get('price')),2)
    else:
        return -1

def getTotalQty(cart,asNumber=False):
    subQty = 0
    for item in cart:
        subQty += int(item.get('quantity'))
    if asNumber == False:
          return str(subQty)
    else:
          return int(subQty)

def getSubTotal(cart,asNumber=False):
    stotal = 0.0
    for i in cart:
        stotal += float(i.get('price')) * int(i.get('quantity'))
    if asNumber == False:
        return str(round(stotal,2))
    else:
        return round(stotal,2)

def getTaxCart(cart, asNumber=False):
    if asNumber == False:
        return str(round(getSubTotal(cart,True) * taxRate, 2))
    else:
        return round(getSubTotal(cart,True) * taxRate, 2)

def getTotalCart(cart, asNumber=False):
    if asNumber == False:
        return str(round(getSubTotal(cart,True) + getTaxCart(cart,True),2))
    else:
        return round(getSubTotal(cart,True) + getTaxCart(cart,True),2)

def delItem(cart,name):
    cart.pop(getIndex(cart, name))
    return
    
def getIndex(cart,name):
    if isKeyValid(cart,name):
        iCounter = 0
        for item in cart:
            if item.get('name').lower() == name.lower():
                return iCounter
            iCounter += 1
    else:
        return -1
    
def isKeyValid(cart,name):
    for item in cart:
        if item.get('name').lower() == name.lower():
            return True
    return False

main()