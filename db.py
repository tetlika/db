
def process_input(total_input):

    allowed_list = ["SET", "GET", "DELETE", "COUNT"]
    
    command = total_input.split()[0]

    if command not in allowed_list:
        print("please use allowed command from:", allowed_list )
        return False
    
    if command == "SET":
        
        if len(total_input.split()) != 3:
            print("please write proper SET command, e.g. SET a 10")
            return False

    
    

while True:
    command = input(">>>").strip()
    process_input(command)