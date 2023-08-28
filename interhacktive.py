import requests
from bs4 import BeautifulSoup
from urllib.parse import quote


def switch (city_name) :
    if city_name == "delhi" or city_name == "Delhi":
        return 2
    if city_name == "mumbai" or city_name == "Mumbai":
        return 3
    if city_name == "kolkata" or city_name == "Kolkata":
        return 4
    if city_name == "chennai" or city_name == "Chennai":
        return 5
    if city_name == "pune" or city_name == "Pune":
        return 7
    if city_name == "hyderabad" or city_name == "Hyderabad":
        return 8
    if city_name == "agartala" or city_name == "Agartala":
        return 9
    if city_name == "ahmedabad" or city_name == "Ahmedabad" :
        return 10
    if city_name == "aizawl" or city_name == "Aizawl":
        return 11
    if city_name == "bhopal" or city_name == "Bhopal":
        return 13
    if city_name == "bhubaneswar" or city_name == "Bhubaneswar":
        return 14
    if city_name == "chandigarh" or city_name == "Chandigarh":
        return 15
    if city_name == "dehradun" or city_name == "Dehradun":
        return 16
    if city_name == "gangtok" or city_name == "Gangtok":
        return 17
    if city_name == "guawahati" or city_name == "Guawahati":
        return 18
    if city_name == "imphal" or city_name == "Imphal":
        return 19
    if city_name == " itanogor" or city_name == " Itanogor":
        return 20
    if city_name == "jaipur" or city_name == " Jaipur":
        return 21
    if city_name == "jammu" or city_name == "Jammu":
        return 22
    if city_name == "kohima" or city_name == "Kohima":
        return 24
    if city_name == "lucknow" or city_name == "Lucknow":
        return 25
    if city_name == "panjim" or city_name == "Panjim":
        return 26
    if city_name == "patna" or city_name == "Patna":
        return 27
    if city_name == "pondicherry" or city_name == "Pondicherry":
        return 28
    if city_name == "port blair" or city_name == "Port blair":
        return 29
    if city_name == "raipur" or city_name == "Raipur" :
        return 30
    if city_name == " ranchi" or city_name == " Ranchi":
        return 31
    if city_name == "shillong" or city_name == "Shillong":
        return 32
    if city_name == "shimla" or city_name == "Shimla":
        return 33
    if city_name == "srinagar" or city_name == "Srinagar":
        return 34
    if city_name == "trivandrum" or city_name == "Trivandrum":
        return 35
    if city_name == "gandhinagar" or city_name == "Gandhinagar":
        return 36
    if city_name == "gurgaon" or city_name == "Gurgaon" :
        return 40
    if city_name == "thane" or city_name == "Thane" :
        return 41
    if city_name == "navi mumbai" or city_name == "Navi Mumbai" :
        return 42
    if city_name == "kota" or city_name == "Kota":
        return 45
    if city_name == "indore" or city_name == "Indore" :
        return 46
    if city_name == "ujjain" or city_name == "Ujjain" :
        return 47
    if city_name == "mysore" or city_name == "Mysore":
        return 49
    if city_name == "surat" or city_name == "Surat" :
        return 51
    if city_name == "rajkot" or city_name == "Rajkot" :
        return 52
    if city_name == "vadodara" or city_name == "Vadodara":
        return 53
    if city_name == "vijayawada" or city_name == "Vijayawada" :
        return 54
    if city_name == "silvassa" or city_name == "Silvassa":
        return 65
    if city_name == "agra" or city_name == "Agra":
        return 72
    if city_name == "ludhiana" or city_name == "Ludhiyana":
        return 73
    if city_name == "mangalore" or city_name == "Mangalore" :
        return 75
    if city_name == "nagpur" or city_name == "Nagpur" :
        return 76
    if city_name == "kolhapur" or city_name == "Kolhapur" :
        return 78
    if city_name == "guntur" or city_name == "Guntur" :
        return 85
    if city_name == "puri" or city_name == "Puri" :
        return 91
    if city_name == "cuttack" or city_name == "Cuttack":
        return 92
    if city_name == "Chittoor" or city_name == "chittoor":
        return 113
    if city_name == "moga" or city_name == "Moga" :
        return 116
    if city_name == "patiala" or city_name == "Patiala" :
        return 124
    if city_name == "kakinada" or city_name == "Kakinada" :
        return 132
    if city_name == "silchar" or city_name == "Silchar" :
        return 137
    if city_name == "tezpur" or city_name == "Tezpur":
        return 142
    if city_name == "dibrugarh" or city_name == "Dibrugarh":
        return 147
    if city_name == "kozihikode" or city_name == "Kozihikode" :
        return 148
    if city_name == "gaya" or city_name == "Gaya" :
        return 151
    if city_name == "sasaram" or city_name == "Sasaram" :
        return 152
    if city_name == "thrissur" or city_name == "Thrissur" :
        return 154
    if city_name == "namchi" or city_name == "Namchi" :
        return 163
    if city_name == "kollam" or city_name == "Kollam" :
        return 166
    if city_name == "haridwar" or city_name == "Haridwar" :
        return 167
    if city_name == "nainital" or city_name == "Nainital" :
        return 170
    if city_name == "bhagalpur" or city_name == "Bhagalpur" :
        return 181
    if city_name == "motihari" or city_name == "Motihari" :
        return 200
    if city_name == "godda" or city_name == "Godda" :
        return 201
    if city_name == "deoghar" or city_name == "Deoghar" :
        return 208
    if city_name == "dhanbad" or city_name == "Dhanbad" :
        return 210
    if city_name == "jamshedpur" or city_name == "Jamshedpur" :
        return 220
    if city_name == "jodhpur" or city_name == "Jodhpur" :
        return 221
    if city_name == "udaipur" or city_name == "Udaipur" :
        return 225
    if city_name == "korba" or city_name == "Korba" :
        return 263
    if city_name == "jashpur" or city_name == "Jashpur" :
        return 267
    if city_name == "margao" or city_name == "Mardao" :
        return 274
    if city_name == "kanpur" or city_name == "Kanpur" :
        return 292
    if city_name == "jamnagar" or city_name == "Jamnagar" :
        return 301
    if city_name == "bhiwani" or city_name == "Bhiwani" :
        return 319
    if city_name == "sonepat" or city_name == "Sonepat" :
        return 321
    if city_name == "panipat" or city_name == "Panipat" :
        return 324
    if city_name == "kullu" or city_name == "Kullu" :
        return 340
    if city_name == "amravati" or city_name == "Amravati":
        return 366
    if city_name == "nasik" or city_name == "Nasik" :
        return 372
    if city_name == "purulia" or city_name == "Purulia" :
        return 392
    if city_name == "howrah" or city_name == "Howrah" :
        return 400
    if city_name == "barasat" or city_name == "Barasat" :
        return 401
    if city_name == "hoogly" or city_name == "Hoogly" :
        return 402
    if city_name == "bardhaman" or city_name == "Bardhaman" :
        return 403
    if city_name == "cooch behar" or city_name == "Cooch Behar" :
        return 406
    if city_name == "allahabad" or city_name == "Allahabad" :
        return 442
    if city_name == "varanasi" or city_name == "Varanasi" :
        return 451
    if city_name == "tirnueveli" or city_name == "Tiruneveli" :
        return 471
    if city_name == "madurai" or city_name == "Madurai":
        return 478
    if city_name == "warangal" or city_name == "Warangal" :
        return 489
    if city_name == "coimbatore" or city_name == "Coimbatore":
        return 509
    if city_name == "ooty" or city_name == "Ooty":
        return 511
    if city_name == "vellore " or city_name == "Vellore":
        return 517
    if city_name == "ashoknagar" or city_name == "Ashoknagar" :
        return 530
    if city_name == "jaisalmer" or city_name == "Jaisalmer" :
        return 610
    if city_name == "baharampur" or city_name == "Baharampur" :
        return 665
    if city_name == "leh" or city_name == "Leh":
        return 668
    if city_name == "kargil" or city_name == "Kargil":
        return 672    
    

def petrol_price(city) :
    base_url = "https://www.mypetrolprice.com/"+num+"/Petrol-price-in-"
    encoded_city = quote(city) 
    #print(encoded_city) 
    url = f"{base_url}{encoded_city}"
    response = requests.get(url)
    #print(response.status_code)

    if response.status_code == 200:
        soup = BeautifulSoup(response.content, 'html.parser')
        price_span = soup.find('span', itemprop='price')  

        if price_span:
            price = price_span.get_text()
            print(f"Petrol price in {city}: {price}")
        else:
            print("Price information not found on the page.")
    else:
        print("Error: 401")
def diesel_price(city) :
    base_url = "https://www.mypetrolprice.com/"+num+"/Diesel-price-in-"
    encoded_city = quote(city) 
    #print(encoded_city) 
    url = f"{base_url}{encoded_city}"
    response = requests.get(url)
    #print(response.status_code)

    if response.status_code == 200:
        soup = BeautifulSoup(response.content, 'html.parser')
        price_span = soup.find('span', itemprop='price')  

        if price_span:
            price = price_span.get_text()
            print(f"Diesel price in {city}: {price}")
        else:
            print("Price information not found on the page.")
    else:
        print("Error: 401")


#driver code 

fuel = input("Enter the fuel type: ")
country = input()
city = input()
#city = input("Enter the city: ")
num = str(switch(city))
if fuel == "petrol" :
    petrol_price(city)
elif fuel == "diesel" :
    diesel_price(city)
else :
    petrol_price(city)
    diesel_price(city)
        


