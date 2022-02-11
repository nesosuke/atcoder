import math
 
A, B, H, M = map(int, input().split())
 
deg_long = M * 6
deg_short = 30 * H + M / 2
    
rad = math.radians( min(deg_long - deg_short, 360-(deg_long-deg_short)))
print( math.sqrt(A **2 + B ** 2 - 2* A * B* math.cos(rad)) )