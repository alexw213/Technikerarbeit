tempData = "/sys/class/thermal/thermal_zone0/temp"
dateilesen = open(tempData, "r")
temperatur = dateilesen.readline(2)
dateilesen.close()
print("Deine CPU hat " + temperatur + " Grad")
