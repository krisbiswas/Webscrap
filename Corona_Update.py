import requests
from bs4 import BeautifulSoup
'''
class StateCondition:
    def __init__(self,name,confirmed,cured,dead):
        self.name = name
        self.confirmed = confirmed
        self.cured = cured
        self.dead = dead
    def get_confirmed(self):
        return self.confirmed
    def get_cured(self):
        return self.confirmed
    def get_deaths(self):
        return self.confirmed
    def get_status(self):
        print("Confirmed: %s\nCured: %s\nDeaths: %s" %(self.confirmed,self.cured,self.dead))
'''

url = "https://www.mygov.in/corona-data/covid19-statewise-status"
try:
    request = requests.get(url)
    page_source = request.content
except:
    print("No Connection!")
    quit(-1)

bsoup = BeautifulSoup(page_source, features="html.parser")
info_block = bsoup.find_all("div", {"class": "field-items"})
status = {}
i = 8
while i < len(info_block):
    state_name = info_block[i].string
    i += 1
    confirmed_case = int(info_block[i].string)
    i += 1
    cured_case = int(info_block[i].string)
    i += 1
    deaths = int(info_block[i].string)
    i += 1
    # state_condition = StateCondition(state_name, confirmed_case, cured_case, deaths)
    # state_condition.get_status()

    status.__setitem__(state_name.lower(), {"confirmed": confirmed_case, "cured": cured_case, "deaths": deaths})

def get_activeStatus(val):
    active = val.get("confirmed")-val.get("cured")-val.get("deaths")
    return "Total: "+str(val.get("confirmed"))+"\nActive: "+str(active)+"\nCured: "+str(val.get("cured"))+"\n" \
            "Deaths: "+str(val.get("deaths"))

#######################################################################
#               Find totals
total = [0,0,0,0]
for key in status.keys():
    total[0] += int(status.get(key).get("confirmed"))
    total[2] += int(status.get(key).get("cured"))
    total[3] += int(status.get(key).get("deaths"))
    total[1] = total[0]-total[2]-total[3]
print("#====>>>>>>>>>>>>>>>>    Country Total   <<<<<<<<<<<<<<<<<<====#")
print("Total: "+str(total[0])+"\nActive: "+str(total[1])+"\nCured: "+str(total[2])+"\n" \
            "Deaths: "+str(total[3]))
#######################################################################
show_state_data = input("Want to know state data: ")
if show_state_data.lower().find("y") > -1:
    query = input("Enter state name without spaces: ").lower()
    while not query.__eq__("no"):
        if query.find("madhya") > -1:
            query = "mp"
        elif (query.find("jammu") > -1) or (query.find("kashmir") > -1):
            query = "j &amp; k"
        elif (query.find("andaman") > -1) or (query.find("nicobar") > -1):
            query = "andamannicobar"
        elif query.find("arunachal") > -1:
            query = "arunachal pradesh"
        elif query.find("westbengal") > -1:
            query = "west bengal"
        elif query.find("ap") > -1:
            query = "andrapradesh"
        elif query.find("up") > -1:
            query = "uttarpradesh"
        else:
            pass

        if query in status:
            print(get_activeStatus(status.get(query.lower())))
            query = input("Enter state name without spaces: ").lower()
        else:
            print("Please enter correct Name!")
            query = input().lower()
else:
    quit(0)

'''
----------------->>>>>>>>>    String Operations   <<<<<<<<<------------------
i = 8
while i < len(info_block):
    data = str(info_block[i]).split(">")[2]
    data = data[:data.index("<")]
    state_name = data
    i+=1
    data = str(info_block[i]).split(">")[2]
    data = data[:data.index("<")]
    confirmed_case = int(data)
    i += 1
    data = str(info_block[i]).split(">")[2]
    data = data[:data.index("<")]
    cured_case = int(data)
    i += 1
    data = str(info_block[i]).split(">")[2]
    data = data[:data.index("<")]
    deaths = int(data)
    i += 1
    # state_condition = StateCondition(state_name, confirmed_case, cured_case, deaths)
    # state_condition.get_status()

    status.__setitem__(state_name.lower(), {"confirmed": confirmed_case, "cured": cured_case, "deaths": deaths})

def get_activeStatus(val):
    active = val.get("confirmed")-val.get("cured")-val.get("deaths")
    return "Total: "+str(val.get("confirmed"))+"\nActive: "+str(active)+"\nCured: "+str(val.get("cured"))+"\n" \
            "Deaths: "+str(val.get("deaths"))

#######################################################################
#               Find totals
total = [0,0,0,0]
for key in status.keys():
    total[0] += int(status.get(key).get("confirmed"))
    total[2] += int(status.get(key).get("cured"))
    total[3] += int(status.get(key).get("deaths"))
    total[1] = total[0]-total[2]-total[3]
print("#====>>>>>>>>>>>>>>>>    Country Total   <<<<<<<<<<<<<<<<<<====#")
print("Total: "+str(total[0])+"\nActive: "+str(total[1])+"\nCured: "+str(total[2])+"\n" \
            "Deaths: "+str(total[3]))
#######################################################################
show_state_data = input("Want to know state data: ")
if show_state_data.lower().find("y") > -1:
    query = input("Enter state name without spaces: ")
    query = query.lower()
    while not query.__eq__("no"):
        if query.find("madhya") > -1:
            query = "mp"
        elif (query.find("jammu") > -1) or (query.find("kashmir") > -1):
            query = "j &amp; k"
        elif (query.find("andaman") > -1) or (query.find("nicobar") > -1):
            query = "andamannicobar"
        elif query.find("arunachal") > -1:
            query = "arunachal pradesh"
        elif query.find("westbengal") > -1:
            query = "west bengal"
        elif query.find("ap") > -1:
            query = "andrapradesh"
        elif query.find("up") > -1:
            query = "uttarpradesh"
        else:
            pass

        if query in status:
            print(get_activeStatus(status.get(query.lower())))
            query = input("Enter state name without spaces: ")
            query = query.lower()
        else:
            print("Please enter correct Name!")
            query = input()
else:
    quit(0)
'''