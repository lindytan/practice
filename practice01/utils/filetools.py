
# 1. 保存信息到文件
def save_file(file_path="./conf/token.txt", token=""):
    with open(file_path, "w") as f:
        f.writelines(token)

# 2. 读取txt文件
def read_file(file_path="./conf/token.txt"):
    with open(file_path, "r") as f:
        token = f.read()
        
    return token

    
# 1. 保存信息到文件
def save_filei(file_path="./conf/iid.txt", iid=""):
    with open(file_path, "w") as f:
        f.writelines(str(iid))

# 2. 读取txt文件
def read_filei(file_path="./conf/iid.txt"):
    with open(file_path, "r") as f:
        iid = f.read()
        
    return iid