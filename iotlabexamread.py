import urllib



def main():
	anagha = urllib.urlopen("https://api.thingspeak.com/channels/920451/feeds.csv?api_key=HGSAYBI3YXNPJ8Y8&results=3")

	response = anagha.read()
	print(response)
	print("http status code = %s" % (anagha.getcode()))
	anagha.close()

if __name__ == '__main__':
	main()


