import random
import sys
import string

def main():
    # 默认字符集为小写和大写字母
    char_set = string.ascii_lowercase + string.ascii_uppercase
    
    try:
        # 获取命令行参数
        seed = int(sys.argv[1])
        length = int(sys.argv[2])
        
        # 检查是否有第四个参数，如果有，则使用它作为字符集
        if len(sys.argv) == 4:
            user_char_set = sys.argv[3]
            if user_char_set != "":
            	char_set = user_char_set
            
    except (IndexError, ValueError):
        print("Usage: python script.py <seed> <length> [<character_set>]")
        sys.exit(1)
    
    # 设置随机数种子
    random.seed(seed)
    
    # 生成随机字符串
    random_string = "".join(random.sample(char_set, length))
    print(random_string)

if __name__ == "__main__":
    main()