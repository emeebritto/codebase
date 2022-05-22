class Nexa:
	project_file_names = []

	@staticmethod
	def back_parent(file_name, backs=1):
		try:
			import os
			import sys
		
			sys.path.append(
				os.path.abspath(
					os.path.join(
						os.path.dirname(__file__),
						(backs * '../')
					)
				)
			)
		except ImportError:
			raise

	@staticmethod
	def scan_project(file_name):
		with open(file_name, 'r') as file:
			print(file.read())
	
	@staticmethod
	def autocomplete(prefix, before, after, location, file_name):
#		print(prefix)
#		print({'before': before})
#		print({'after': after})
#		print(location)
#		print(file_name)

		return {
			"results": [{}]
		}