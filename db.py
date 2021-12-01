
def process_input(total_input, db_dict):

    allowed_list = ["SET", "GET", "DELETE", "COUNT"]
    
    command = total_input.split()[0]

    if command not in allowed_list:
        print("please use allowed command from:", allowed_list )
        return db_dict
    
    #process SET
    if command == "SET":      
        if len(total_input.split()) != 3:
            print("please write proper SET command, e.g. SET a 10")
            return db_dict
        
        db_dict[total_input.split()[1]] = total_input.split()[2]

        return db_dict

    #process GET
    if command == "GET":       
        if len(total_input.split()) != 2:
            print("please write proper GET command, e.g. GET a ")
            return db_dict      
        try:
            print(db_dict[total_input.split()[1]])
            return db_dict
        except KeyError:
            print("please use proper variable")
            return db_dict
    
    #process DELETE
    if command == "DELETE":       
        if len(total_input.split()) != 2:
            print("please write proper DELETE command, e.g. DELETE a ")
            return db_dict
        
        try:
            del db_dict[total_input.split()[1]]
            return db_dict
        except KeyError:
            print("please use proper variable")
            return db_dict

    #process COUNT
    if command == "COUNT":       
        if len(total_input.split()) != 2:
            print("please write proper COUNT command, e.g. COUNT 2 ")
            return db_dict
        counter = 0
       
        for k, v in db_dict.items():
            if v == total_input.split()[1]:
                counter += 1
        
        print(counter)
        return db_dict
       
def process_transaction(total_input, db_dict, db_dict_backup):
    command = total_input.split()[0]
    
    if command == "BEGIN":
        db_dict_backup = db_dict
        myinput = input(">>>").strip()
        db_dict = process_input(myinput, db_dict)
        return db_dict, db_dict_backup 

    if command == "ROLLBACK" and db_dict_backup != {}:
        db_dict = db_dict_backup 
        return db_dict, db_dict_backup
    
    myinput = input(">>>").strip()
    db_dict = process_input(myinput, db_dict)
    return db_dict, db_dict_backup
    


db_space = {}
db_dict_backup = {}

while True:
    myinput = input(">>>").strip()   

    db_space, db_dict_backup = process_transaction(myinput, db_space, db_dict_backup)
    print(db_space)
    print(db_dict_backup)
    