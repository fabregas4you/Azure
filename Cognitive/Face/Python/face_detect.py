import sys
import cognitive_face as CF

args = sys.argv
KEY = args[1]
CF.Key.set(KEY)

img_url = args[2]
result = CF.face.detect(img_url)
print (result)
