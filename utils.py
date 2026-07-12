import numpy as np
import pandas as pd
import math
import re

def extract_features(s):
    s = str(s).lower()
    length = len(s)
    # 1. Tính Entropy (Độ hỗn loạn)
    prob = [float(s.count(c)) / length for c in dict.fromkeys(list(s))]
    entropy = - sum([p * math.log(p) / math.log(2.0) for p in prob])
    
    # 2. Tỷ lệ ký tự đặc biệt
    special_chars = r'[!@#$%^&*(),.?":{}|<>/\-+=_]'
    special_count = len(re.findall(special_chars, s))
    special_ratio = special_count / length if length > 0 else 0
    
    count_at = s.count("@")            # Bắt @@version
    count_percent = s.count("%")       # Bắt URL Encoding (%55nion)
    count_star = s.count("*")          # Bắt comment /* */
    count_bracket = s.count("(")       # Bắt các hàm concat(, sleep(
    is_hex = 1 if "0x" in s else 0     # Bắt mã Hex (0x223e)
    
    # 4. Kiểm tra từ khóa nhạy cảm
    keywords = ['select', 'union', 'insert', 'update', 'drop', 'sleep', 'concat', 'version', 'extractvalue']
    kw_feats = [1 if k in s else 0 for k in keywords]
    
    # Tổng hợp lại thành một list (14 đặc trưng)
    features = [entropy, length, special_ratio, count_at, count_percent, 
                count_star, count_bracket, is_hex] + kw_feats
    return features
