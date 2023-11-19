try:
    import requests as req
    link = input("Enter the profile view count API link -> ")
    while True:
        try:
            numReq = int(input("Enter the number of request -> "))
            break
        except TypeError:
            print("Please enter numerical value!")
            continue
    sucreq = 0
    losssend = 0
    try:
        request = req.get(link)
        sucreq+=1
    except req.ConnectionError:
        print("Sorry! There is no internet connection or the URL is invalid.")
        losssend+=1
        exit(-1)
    print("Starting...")
    for count in range(numReq-1):
        request = req.get(link)
        if request.status_code == 200:
            print(count," : request sent successfully!")
            sucreq+=1
        else:
            print(count," : Sorry! There was a mistake. Status code ->",request.status_code)
            losssend += 1
    print(f"\nIt's over! Attack results ->\nAccuracy -> {(sucreq/numReq)*100}\nLoss -> {(losssend/numReq)*100}")
except KeyboardInterrupt:
    print("See you again! Soon.")