class clumsyibo:
	#Karenin alanını hesaplayan fonksiyon
	def kalanı(self,kenar):
		self.kenar = kenar * kenar
		print(self.kenar)
	#Karenin çevresini hesaplayan fonksiyon
	def kçevre(self,kenar):
		self.kenar = kenar * 4
		print(self.kenar)
		pass
	#simple cleanscreen
	def clscreen(self):
		import os
		if os.name == "posix":
			os.system("clear")
		else:
			os.system("clear")
	#simple root checker
	def rtcheck(self,text):
		import os
		if os.geteuid() != 0:
			exit(text)
		else:
			pass

if __name__ == "__main__":
	print("Clumsyibo ya hoşgeldiniz...")
