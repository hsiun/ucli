import ConfigParser
import os,sys
import platform

class UCloudApiConfig(object):
	"""this is the file use to handle config"""
	def __init__(self, configParser = None):
		if configParser is None:
			configParser = ConfigParser.ConfigParser()
		# configParser is use to handle config file
		self.configParser = configParser

		# the directory use to install the tool
		self.home = ".ucli"

		self.configure = "ucloud.cfg"
		self.ucliConfigPath = os.path.join(self.findConfigPath(), self.home)


	def makeConfigDirs(self):
		if not os.path.exists(self.ucliConfigPath):
			os.makedirs(self.ucliConfigPath)

	def findConfigPath(self):
		homePath = ""
		if platform.system() == "Windows":
			homePath = os.environ['HOMEPATH']
			pass
		else:
			homePath = os.environ['HOME']
			pass
		return homePath

		
	def getConfigFileName(self):
		configFileName = os.path.join(self.ucliConfigPath,self.configure)
		return configFileName


	def readConfig(self):
		configFileName = self.getConfigFileName()
		self.configParser.read(configFileName)

	def newCredentials(self):
		self.readConfig()
		try:
			self.configParser.add_section("credentials")
		except Exception as e:
			pass
		self.configParser.set("credentials", "base_url", "https://api.ucloud.cn")


	def updateCreadentialsUseValue(self, private_key, public_key, project_id):
		self.readConfig()	
		self.configParser.set("credentials", "public_key", public_key)
		self.configParser.set("credentials", "private_key", private_key)
		self.configParser.set("credentials", "project_id", project_id)
		self.makeConfigDirs()
		
		self.configParser.write(open(self.getConfigFileName(), "w"))


	def getCredentialsValueByKey(self, key):
		self.readConfig()
		return self.configParser.get("credentials", key)
		
if __name__ == '__main__':
	pass