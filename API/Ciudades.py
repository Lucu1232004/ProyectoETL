import requests
import csv
import random
from time import sleep
from pprint import pprint

Ciudades = [ "Nueva York", "Los Ángeles", "Chicago", "Houston", "Phoenix", "Filadelfia", "San Antonio", "San Diego", "Dallas", 
            "San José", "Austin", "Indianápolis", "Jacksonville", "San Francisco", "Columbus", "Fort Worth", "Charlotte", "Detroit", 
            "El Paso", "Memphis", "Boston", "Seattle", "Denver", "Washington, D.C.", "Nashville", "Baltimore", "Oklahoma City", "Louisville", 
            "Portland", "Las Vegas", "Milwaukee", "Albuquerque", "Tucson", "Fresno", "Sacramento", "Kansas City", "Long Beach", "Mesa", "Atlanta", 
            "Colorado Springs", "Raleigh", "Omaha", "Miami", "Oakland", "Tulsa", "Minneapolis", "Cleveland", "Wichita", "Arlington", "New Orleans", 
            "Bakersfield", "Tampa", "Honolulu", "Anaheim", "Aurora", "Santa Ana", "St. Louis", "Riverside", "Corpus Christi", "Pittsburgh", "Lexington", 
            "Anchorage", "Stockton", "Cincinnati", "St. Paul", "Toledo", "Greensboro", "Newark", "Plano", "Henderson", "Lincoln", "Buffalo", "Fort Wayne", 
            "Jersey City", "Chula Vista", "Orlando", "St. Petersburg", "Norfolk", "Chandler", "Laredo", "Madison", "Winston-Salem", "Lubbock", "Baton Rouge", 
            "Durham", "Garland", "Glendale", "Reno", "Hialeah", "Chesapeake", "Scottsdale", "North Las Vegas", "Irving", "Fremont", "Irvine", "Birmingham", "Rochester", 
            "San Bernardino", "Spokane", "Gilbert", "Arlington", "Montgomery", "Boise", "Richmond", "Des Moines", "Fayetteville", "Shreveport", "Akron", "Tacoma", "Aurora", 
            "Oxnard", "Fontana", "Yonkers", "Augusta", "Mobile", "Little Rock", "Moreno Valley", "Glendale", "Amarillo", "Huntington Beach", "Columbus", "Grand Rapids", "Salt Lake City", 
            "Tallahassee", "Worcester", "Newport News", "Huntsville", "Knoxville", "Providence", "Santa Clarita", "Grand Prairie", "Brownsville", "Jackson", "Overland Park", "Garden Grove", 
            "Santa Rosa", "Chattanooga", "Port St. Lucie", "Fort Lauderdale", "Rancho Cucamonga", "Ontario", "Vancouver", "Tempe", "Springfield", "Lancaster", "Eugene", "Pembroke Pines", "Salem", 
            "Cape Coral", "Peoria", "Sioux Falls", "Springfield", "Elk Grove", "Rockford", "Palmdale", "Corona", "Salinas", "Pomona", "Pasadena", "Joliet", "Paterson", "Kansas City", "Torrance", 
            "Bridgeport", "Alexandria", "Sunnyvale", "Cary", "Lakewood", "Hollywood", "Thornton", "Pasadena", "Syracuse", "Naperville", "McAllen", "Mesquite", "Dayton", "Savannah", "Irvine", "Salt Lake City", 
            "Huntington Beach", "Modesto", "San Bernardino", "Oxnard", "Fontana", "Moreno Valley", "Fayetteville", "Santa Clarita", "Grand Prairie", "Overland Park", "Tallahassee", "Worcester", "Newport News", 
            "Huntsville", "Knoxville", "Providence", "Santa Rosa", "Chattanooga", "Port St. Lucie", "Fort Lauderdale", "Rancho Cucamonga", "Ontario", "Vancouver", "Tempe", "Springfield", "Lancaster", "Eugene", 
            "Pembroke Pines", "Salem", "Cape Coral", "Peoria", "Sioux Falls", "Springfield", "Elk Grove", "Rockford", "Palmdale", "Corona", "Salinas", "Pomona", "Pasadena", "Joliet", "Paterson", "Kansas City", "Torrance", 
            "Bridgeport", "Alexandria", "Sunnyvale", "Cary", "Lakewood", "Hollywood", "Thornton", "Pasadena", "Syracuse", "Naperville", "McAllen", "Mesquite", "Dayton", "Savannah", "Corona", "Salinas", "Pomona", "Pasadena", 
            "Joliet", "Paterson", "Kansas City", "Torrance", "Bridgeport", "Alexandria", "Sunnyvale", "Cary", "Lakewood", "Hollywood", "Thornton", "Pasadena", "Syracuse", "Naperville", "McAllen", "Mesquite", "Dayton", "Savannah", 
            "Irvine", "Salt Lake City", "Huntington Beach", "Modesto", "San Bernardino", "Oxnard", "Fontana", "Moreno Valley", "Fayetteville", "Santa Clarita", "Grand Prairie", "Overland Park", "Tallahassee", "Worcester", "Newport News", 
            "Huntsville", "Knoxville", "Providence", "Santa Rosa", "Chattanooga", "Port St. Lucie", "Fort Lauderdale", "Rancho Cucamonga", "Ontario", "Vancouver", "Tempe", "Springfield", "Lancaster", "Eugene", "Pembroke Pines", "Salem", "Cape Coral", 
            "Peoria", "Sioux Falls", "Springfield", "Elk Grove", "Rockford", "Palmdale", "Corona", "Salinas", "Pomona", "Pasadena", "Joliet", "Paterson", "Kansas City", "Torrance", "Bridgeport", "Alexandria", "Sunnyvale", "Cary", "Lakewood", "Hollywood", 
            "Thornton", "Pasadena", "Syracuse", "Naperville", "McAllen", "Mesquite", "Dayton", "Savannah", "Irvine", "Salt Lake City", "Huntington Beach", "Modesto", "San Bernardino", "Oxnard", "Fontana", "Moreno Valley", "Fayetteville", "Santa Clarita", 
            "Grand Prairie", "Overland Park", "Tallahassee", "Worcester", "Newport News", "Huntsville", "Knoxville", "Providence", "Santa Rosa", "Chattanooga", "Port St. Lucie", "Fort Lauderdale", "Rancho Cucamonga", "Ontario", "Vancouver", "Tempe", "Eugene", 
            "Pembroke Pines", "Salem", "Cape Coral", "Peoria", "Sioux Falls", "Springfield", "Elk Grove", "Rockford", "Palmdale", "Corona", "Salinas", "Pomona", "Pasadena", "Joliet", "Paterson", "Kansas City", "Torrance", "Bridgeport", "Alexandria", "Sunnyvale", 
            "Cary", "Lakewood", "Hollywood", "Thornton", "Pasadena", "Syracuse", "Naperville", "McAllen", "Mesquite", "Dayton", "Savannah", "Irvine", "Salt Lake City", "Huntington Beach", "Modesto", "San Bernardino", "Oxnard", "Fontana", "Moreno Valley", "Fayetteville", 
            "Santa Clarita", "Grand Prairie", "Overland Park", "Tallahassee", "Worcester", "Newport News", "Huntsville", "Knoxville", "Providence", "Santa Rosa", "Chattanooga", "Port St. Lucie", "Fort Lauderdale", "Rancho Cucamonga", "Ontario", "Vancouver", "Tempe", "Springfield", 
            "Lancaster", "Eugene", "Pembroke Pines", "Salem", "Cape Coral", "Peoria", "Sioux Falls", "Springfield", "Elk Grove", "Rockford", "Palmdale", "Corona", "Salinas", "Pomona", "Pasadena", "Joliet", "Paterson", "Kansas City", "Torrance", "Bridgeport", "Alexandria", "Sunnyvale", 
            "Cary", "Lakewood", "Hollywood", "Thornton", "Pasadena", "Syracuse", "Naperville", "McAllen", "Mesquite", "Dayton", "Savannah", "Corona", "Salinas", "Pomona", "Pasadena", "Joliet", "Paterson", "Kansas City", "Torrance", "Bridgeport", "Alexandria", "Sunnyvale", "Cary", "Lakewood", 
            "Hollywood", "Thornton", "Pasadena", "Syracuse", "Naperville", "McAllen", "Mesquite", "Dayton", "Savannah", "Irvine", "Salt Lake City", "Huntington Beach", "Modesto", "San Bernardino", "Oxnard", "Fontana", "Moreno Valley", "Fayetteville", "Santa Clarita", "Grand Prairie", "Overland Park", 
            "Tallahassee", "Worcester", "Newport News", "Huntsville", "Knoxville", "Providence", "Santa Rosa", "Chattanooga", "Port St. Lucie", "Fort Lauderdale", "Rancho Cucamonga", "Ontario", "Vancouver", "Tempe", "Eugene", "Pembroke Pines", "Salem", "Cape Coral", "Peoria", "Sioux Falls", 
            "Springfield", "Elk Grove", "Rockford", "Palmdale", "Corona", "Salinas", "Pomona", "Pasadena", "Joliet", "Paterson", "Kansas City", "Torrance", "Bridgeport", "Alexandria", "Sunnyvale", "Cary", "Lakewood", "Hollywood", "Thornton", "Pasadena", "Syracuse", "Naperville", "McAllen", 
            "Mesquite", "Dayton", "Savannah", "Irvine", "Salt Lake City", "Huntington Beach", "Modesto", "San Bernardino", "Oxnard", "Fontana", "Moreno Valley", "Fayetteville", "Santa Clarita", "Grand Prairie", "Overland Park", "Tallahassee", "Worcester", "Newport News", "Huntsville", "Knoxville", 
            "Providence", "Santa Rosa", "Chattanooga", "Port St. Lucie", "Fort Lauderdale", "Rancho Cucamonga", "Ontario", "Vancouver", "Tempe", "Springfield", "Lancaster"
            "Nueva York", "Los Ángeles", "Chicago", "Houston", "Phoenix", "Filadelfia", "San Antonio", "San Diego", "Dallas", "San José", "Austin", "Indianápolis", "Jacksonville", "San Francisco", "Columbus", "Fort Worth", "Charlotte", "Detroit", "El Paso", "Memphis", "Boston", "Seattle", "Denver", "Washington, D.C.", "Nashville", 
            "Baltimore", "Oklahoma City", "Louisville", "Portland", "Las Vegas", "Milwaukee", "Albuquerque", "Tucson", "Fresno", "Sacramento", "Kansas City", "Long Beach", "Mesa", "Atlanta", "Colorado Springs", "Raleigh", "Omaha", "Miami", "Oakland", "Tulsa", "Minneapolis", "Cleveland", "Wichita", "Arlington", "New Orleans", "Bakersfield", 
            "Tampa", "Honolulu", "Anaheim", "Aurora", "Santa Ana", "St. Louis", "Riverside", "Corpus Christi", "Pittsburgh", "Lexington", "Anchorage", "Stockton", "Cincinnati", "St. Paul", "Toledo", "Greensboro", "Newark", "Plano", "Henderson", "Lincoln", "Buffalo", "Fort Wayne", "Jersey City", "Chula Vista", "Orlando", "St. Petersburg", "Norfolk", "Chandler", 
            "Laredo", "Madison", "Winston-Salem", "Lubbock", "Baton Rouge", "Durham", "Garland", "Glendale", "Reno", "Hialeah", "Chesapeake", "Scottsdale", "North Las Vegas", "Irving", "Fremont", "Irvine", "Birmingham", "Rochester", "San Bernardino", "Spokane", "Gilbert", "Arlington", "Montgomery", "Boise", "Richmond", "Des Moines", "Fayetteville", "Shreveport", "Akron", 
            "Tacoma", "Aurora", "Oxnard", "Fontana", "Yonkers", "Augusta", "Mobile", "Little Rock", "Moreno Valley", "Glendale", "Amarillo", "Huntington Beach", "Columbus", "Grand Rapids", "Salt Lake City", "Tallahassee", "Worcester", "Newport News", "Huntsville", "Knoxville", "Providence", "Santa Clarita", "Grand Prairie", "Brownsville", "Jackson", "Overland Park", "Garden Grove", 
            "Santa Rosa", "Chattanooga", "Port St. Lucie", "Fort Lauderdale", "Rancho Cucamonga", "Ontario", "Vancouver", "Tempe", "Springfield", "Lancaster", "Eugene", "Pembroke Pines", "Salem", "Cape Coral", "Peoria", "Sioux Falls", "Springfield", "Elk Grove", "Rockford", "Palmdale", "Corona", "Salinas", "Pomona", "Pasadena", "Joliet", "Paterson", "Kansas City", "Torrance", "Bridgeport", 
            "Alexandria", "Sunnyvale", "Cary", "Lakewood", "Hollywood", "Thornton", "Pasadena", "Syracuse", "Naperville", "McAllen", "Mesquite", "Dayton", "Savannah", "Irvine", "Salt Lake City", "Huntington Beach", "Modesto", "San Bernardino", "Oxnard", "Fontana", "Moreno Valley", "Fayetteville", "Santa Clarita", "Grand Prairie", "Overland Park", "Tallahassee", "Worcester", "Newport News", 
            "Huntsville", "Knoxville", "Providence", "Santa Rosa", "Chattanooga", "Port St. Lucie", "Fort Lauderdale", "Rancho Cucamonga", "Ontario", "Vancouver", "Tempe", "Springfield", "Lancaster", "Eugene", "Pembroke Pines", "Salem", "Cape Coral", "Peoria", "Sioux Falls", "Springfield", "Elk Grove", "Rockford", "Palmdale", "Corona", "Salinas", "Pomona", "Pasadena", "Joliet", "Paterson", "Kansas City", "Torrance", 
            "Bridgeport", "Alexandria", "Sunnyvale", "Cary", "Lakewood", "Hollywood", "Thornton", "Pasadena", "Syracuse", "Naperville", "McAllen", "Mesquite", "Dayton", "Savannah", "Irvine", "Salt Lake City", "Huntington Beach", "Modesto", "San Bernardino", "Oxnard", "Fontana", "Moreno Valley", "Fayetteville", "Santa Clarita", "Grand Prairie", "Overland Park", "Tallahassee", "Worcester", "Newport News", "Huntsville", 
            "Knoxville", "Providence", "Santa Rosa", "Chattanooga", "Port St. Lucie", "Fort Lauderdale", "Rancho Cucamonga", "Ontario", "Vancouver", "Tempe", "Springfield", "Lancaster", "Eugene", "Pembroke Pines", "Salem", "Cape Coral", "Peoria", "Sioux Falls", "Springfield", "Elk Grove", "Rockford", "Palmdale", "Corona", "Salinas", "Pomona", "Pasadena", "Joliet", "Paterson", "Kansas City", "Torrance", "Bridgeport", "Alexandria", 
            "Sunnyvale", "Cary", "Lakewood", "Hollywood", "Thornton", "Pasadena", "Syracuse", "Naperville", "McAllen", "Mesquite", "Dayton", "Savannah", "Irvine", "Salt Lake City", "Huntington Beach", "Modesto", "San Bernardino", "Oxnard", "Fontana", "Moreno Valley", "Fayetteville", "Santa Clarita", "Grand Prairie", "Overland Park", "Tallahassee", "Worcester", "Newport News", "Huntsville", "Knoxville", "Providence", 
            "Santa Rosa", "Chattanooga", "Port St. Lucie", "Fort Lauderdale", "Rancho Cucamonga", "Ontario", "Vancouver", "Tempe", "Springfield", "Lancaster", "Eugene", "Pembroke Pines", "Salem", "Cape Coral", "Peoria", "Sioux Falls", "Springfield", "Elk Grove", "Rockford", "Palmdale", "Corona", "Salinas", "Pomona", "Pasadena", "Joliet", "Paterson", "Kansas City", "Torrance", "Bridgeport", "Alexandria", "Sunnyvale", "Cary", "Lakewood", 
            "Hollywood", "Thornton", "Pasadena", "Syracuse", "Naperville", "McAllen", "Mesquite", "Dayton", "Savannah", "Irvine", "Salt Lake City", "Huntington Beach", "Modesto", "San Bernardino", "Oxnard", "Fontana", "Moreno Valley", "Fayetteville", "Santa Clarita", "Grand Prairie", "Overland Park", "Tallahassee", "Worcester", "Newport News", "Huntsville", "Knoxville", "Providence", "Santa Rosa", "Chattanooga", "Port St. Lucie", "Fort Lauderdale", 
            "Rancho Cucamonga", "Ontario", "Vancouver", "Tempe", "Springfield", "Lancaster", "Eugene", "Pembroke Pines", "Salem", "Cape Coral", "Peoria", "Sioux Falls", "Springfield", "Elk Grove", "Rockford", "Palmdale", "Corona", "Salinas", "Pomona", "Pasadena", "Joliet", "Paterson", "Kansas City", "Torrance", "Bridgeport", "Alexandria", "Sunnyvale", "Cary", "Lakewood", "Hollywood", "Thornton", "Pasadena", "Syracuse", "Naperville", "McAllen", "Mesquite", 
            "Dayton", "Savannah", "Irvine", "Salt Lake City", "Huntington Beach", "Modesto", "San Bernardino", "Oxnard", "Fontana", "Moreno Valley", "Fayetteville", "Santa Clarita", "Grand Prairie", "Overland Park", "Tallahassee", "Worcester", "Newport News", "Huntsville", "Knoxville", "Providence", "Santa Rosa", "Chattanooga", "Port St. Lucie", "Fort Lauderdale", "Rancho Cucamonga", "Ontario", "Vancouver", "Tempe", "Springfield", "Lancaster"
            "Nueva York", "Los Ángeles", "Chicago", "Houston", "Phoenix", "Filadelfia", "San Antonio", "San Diego", "Dallas", "San José", "Austin", "Indianápolis", "Jacksonville", "San Francisco", "Columbus", "Fort Worth", "Charlotte", "Detroit", "El Paso", "Memphis", "Boston", "Seattle", "Denver", "Washington, D.C.", "Nashville", "Baltimore", "Oklahoma City", "Louisville", "Portland", "Las Vegas", "Milwaukee", "Albuquerque", "Tucson", "Fresno", "Sacramento", 
            "Kansas City", "Long Beach", "Mesa", "Atlanta", "Colorado Springs", "Raleigh", "Omaha", "Miami", "Oakland", "Tulsa", "Minneapolis", "Cleveland", "Wichita", "Arlington", "New Orleans", "Bakersfield", "Tampa", "Honolulu", "Anaheim", "Aurora", "Santa Ana", "St. Louis", "Riverside", "Corpus Christi", "Pittsburgh", "Lexington", "Anchorage", "Stockton", "Cincinnati", "St. Paul", "Toledo", "Greensboro", "Newark", "Plano", "Henderson", "Lincoln", "Buffalo", 
            "Fort Wayne", "Jersey City", "Chula Vista", "Orlando", "St. Petersburg", "Norfolk", "Chandler", "Laredo", "Madison", "Winston-Salem", "Lubbock", "Baton Rouge", "Durham", "Garland", "Glendale", "Reno", "Hialeah", "Chesapeake", "Scottsdale", "North Las Vegas", "Irving", "Fremont", "Irvine", "Birmingham", "Rochester", "San Bernardino", "Spokane", "Gilbert", "Arlington", "Montgomery", "Boise", "Richmond", "Des Moines", "Fayetteville", "Shreveport", "Akron", 
            "Tacoma", "Aurora", "Oxnard", "Fontana", "Yonkers", "Augusta", "Mobile", "Little Rock", "Moreno Valley", "Glendale", "Amarillo", "Huntington Beach", "Columbus", "Grand Rapids", "Salt Lake City", "Tallahassee", "Worcester", "Newport News", "Huntsville", "Knoxville", "Providence", "Santa Clarita", "Grand Prairie", "Brownsville", "Jackson", "Overland Park", "Garden Grove", "Santa Rosa", "Chattanooga", "Port St. Lucie", "Fort Lauderdale", "Rancho Cucamonga", 
            "Ontario", "Vancouver", "Tempe", "Springfield", "Lancaster", "Eugene", "Pembroke Pines", "Salem", "Cape Coral", "Peoria", "Sioux Falls", "Springfield", "Elk Grove", "Rockford", "Palmdale", "Corona", "Salinas", "Pomona", "Pasadena", "Joliet", "Paterson", "Kansas City", "Torrance", "Bridgeport", "Alexandria", "Sunnyvale", "Cary", "Lakewood", "Hollywood", "Thornton", "Pasadena", "Syracuse", "Naperville", "McAllen", "Mesquite", "Dayton", "Savannah", "Irvine", "Salt Lake City", 
            "Huntington Beach", "Modesto", "San Bernardino", "Oxnard", "Fontana", "Moreno Valley", "Fayetteville", "Santa Clarita", "Grand Prairie", "Overland Park", "Tallahassee", "Worcester", "Newport News", "Huntsville", "Knoxville", "Providence", "Santa Rosa", "Chattanooga", "Port St. Lucie", "Fort Lauderdale", "Rancho Cucamonga", "Ontario", "Vancouver", "Tempe", "Springfield", "Lancaster", "Eugene", "Pembroke Pines", "Salem", "Cape Coral", "Peoria", "Sioux Falls", "Springfield", 
            "Elk Grove", "Rockford", "Palmdale", "Corona", "Salinas", "Pomona", "Pasadena", "Joliet", "Paterson", "Kansas City", "Torrance", "Bridgeport", "Alexandria", "Sunnyvale", "Cary", "Lakewood", "Hollywood", "Thornton", "Pasadena", "Syracuse", "Naperville", "McAllen", "Mesquite", "Dayton", "Savannah", "Irvine", "Salt Lake City", "Huntington Beach", "Modesto", "San Bernardino", "Oxnard", "Fontana", "Moreno Valley", "Fayetteville", "Santa Clarita", "Grand Prairie", "Overland Park", 
            "Tallahassee", "Worcester", "Newport News", "Huntsville", "Knoxville", "Providence", "Santa Rosa", "Chattanooga", "Port St. Lucie", "Fort Lauderdale", "Rancho Cucamonga", "Ontario", "Vancouver", "Tempe", "Springfield", "Lancaster", "Eugene", "Pembroke Pines", "Salem", "Cape Coral", "Peoria", "Sioux Falls", "Springfield", "Elk Grove", "Rockford", "Palmdale", "Corona", "Salinas", "Pomona", "Pasadena", "Joliet", "Paterson", "Kansas City", "Torrance", "Bridgeport", "Alexandria", 
            "Sunnyvale", "Cary", "Lakewood", "Hollywood", "Thornton", "Pasadena", "Syracuse", "Naperville", "McAllen", "Mesquite", "Dayton", "Savannah", "Irvine", "Salt Lake City", "Huntington Beach", "Modesto", "San Bernardino", "Oxnard", "Fontana", "Moreno Valley", "Fayetteville", "Santa Clarita", "Grand Prairie", "Overland Park", "Tallahassee", "Worcester", "Newport News", "Huntsville", "Knoxville", "Providence", "Santa Rosa", "Chattanooga", "Port St. Lucie", "Fort Lauderdale", "Rancho Cucamonga", 
            "Ontario", "Vancouver", "Tempe", "Springfield", "Lancaster", "Eugene", "Pembroke Pines", "Salem", "Cape Coral", "Peoria", "Sioux Falls", "Springfield", "Elk Grove", "Rockford", "Palmdale", "Corona", "Salinas", "Pomona", "Pasadena", "Joliet", "Paterson", "Kansas City", "Torrance", "Bridgeport", "Alexandria", "Sunnyvale", "Cary", "Lakewood", "Hollywood", "Thornton", "Pasadena", "Syracuse", "Naperville", "McAllen", "Mesquite", "Dayton", "Savannah", "Irvine", "Salt Lake City", "Huntington Beach", 
            "Modesto", "San Bernardino", "Oxnard", "Fontana", "Moreno Valley", "Fayetteville", "Santa Clarita", "Grand Prairie", "Overland Park", "Tallahassee", "Worcester", "Newport News", "Huntsville", "Knoxville", "Providence", "Santa Rosa", "Chattanooga", "Port St. Lucie", "Fort Lauderdale", "Rancho Cucamonga", "Ontario", "Vancouver", "Tempe", "Springfield", "Lancaster", "Eugene", "Pembroke Pines", "Salem", "Cape Coral", "Peoria", "Sioux Falls", "Springfield", "Elk Grove", "Rockford", "Palmdale", "Corona", 
            "Salinas", "Pomona", "Pasadena", "Joliet", "Paterson", "Kansas City", "Torrance", "Bridgeport", "Alexandria", "Sunnyvale", "Cary", "Lakewood", "Hollywood", "Thornton", "Pasadena", "Syracuse", "Naperville", "McAllen", "Mesquite", "Dayton", "Savannah", "Irvine", "Salt Lake City", "Huntington Beach", "Modesto", "San Bernardino", "Oxnard", "Fontana", "Moreno Valley", "Fayetteville", "Santa Clarita", "Grand Prairie", "Overland Park", "Tallahassee", "Worcester", "Newport News", "Huntsville", "Knoxville", 
            "Providence", "Santa Rosa", "Chattanooga", "Port St. Lucie", "Fort Lauderdale", "Rancho Cucamonga", "Ontario", "Vancouver", "Tempe", "Springfield", "Lancaster", "Eugene", "Pembroke Pines", "Salem", "Cape Coral", "Peoria", "Sioux Falls", "Springfield", "Elk Grove", "Rockford", "Palmdale", "Corona", "Salinas", "Pomona", "Pasadena", "Joliet", "Paterson", "Kansas City", "Torrance", "Bridgeport", "Alexandria", "Sunnyvale", "Cary", "Lakewood", "Hollywood", "Thornton", "Pasadena", "Syracuse", "Naperville", "McAllen", "Mesquite", "Dayton", "Savannah"
]

numero_solicitudes = 1000

respuestas = []

clave_api = '6c3b939ef768c204c279b8b2a430dc82'

for i in range(numero_solicitudes):
    ciudad = random.choice(Ciudades)
    
    url = f'http://api.openweathermap.org/data/2.5/weather?q={ciudad}&appid={clave_api}'
    
    response = requests.get(url)
    
    if response.status_code == 404:
        respuestas.append(response.json())
    else:
        respuestas.append(None)
        print(f'Error al obtener datos para {ciudad}. Código de estado: {response.status_code}')
    
    sleep(0.1)

archivo_csv = 'Cuidades_CO .csv'

with open(archivo_csv, mode='w', newline='') as file:
    writer = csv.writer(file)
    
    writer.writerow(['Ciudad', 'Temperatura (K)', 'Descripción del Clima', 'Humedad'])
    
    for ciudad, respuesta in zip(Ciudades, respuestas):
        if respuesta:
            temperatura = respuesta.get('main', {}).get('temp')
            descripcion_clima = respuesta.get('weather', [{}])[0].get('description')
            humedad = respuesta.get('main', {}).get('humidity')
            
            writer.writerow([ciudad, temperatura, descripcion_clima, humedad])
        else:
            writer.writerow([ciudad, 'No disponible', 'No disponible', 'No disponible'])
            print(f'No se obtuvo respuesta para {ciudad}.')

print(f'Se ha creado el archivo CSV: {archivo_csv}')