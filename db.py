
def process_input(total_input, db_dict):

    allowed_list = ["SET", "GET", "DELETE", "COUNT"]
    
    command = total_input.split()[0]

    if command not in allowed_list:
        print("please use allowed command from:", allowed_list )
        return False
    
    #process SET
    if command == "SET":      
        if len(total_input.split()) != 3:
            print("please write proper SET command, e.g. SET a 10")
            return False
        
        db_dict[total_input.split()[1]] = total_input.split()[2]

        return True

    #process GET
    if command == "GET":       
        if len(total_input.split()) != 2:
            print("please write proper GET command, e.g. GET a ")
            return False      
        try:
            print(db_dict[total_input.split()[1]])
            return True
        except KeyError:
            print("please use proper variable")
            return False
    
    #process DELETE
    if command == "DELETE":       
        if len(total_input.split()) != 2:
            print("please write proper DELETE command, e.g. DELETE a ")
            return False
        
        try:
            del db_dict[total_input.split()[1]]
            return True
        except KeyError:
            print("please use proper variable")
            return False

    #process COUNT
    if command == "COUNT":       
        if len(total_input.split()) != 2:
            print("please write proper COUNT command, e.g. COUNT 2 ")
            return False
        counter = 0
       
        for k, v in db_dict.items():
            if v == total_input.split()[1]:
                counter += 1
        
        print(counter)
        return True
       
           
db_space = {}

while True:
    myinput = input(">>>").strip()
    process_input(myinput, db_space)
    