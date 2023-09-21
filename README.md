Tasks:
=================
1. 
class SchemaMappingManager:
	# Manages the schema mappings present in the dir schema_mappings
	# It will hold schema mappings for the specific devices and provide them using methods
	# It will be a singlton class

	def __init__():
		self.schemaDB => dict # OUI-PRODUCT_CLASS-FW_VERSION(string) -> mapping(dict)

	def init():
		Read dir files 
		calculate them into DEVICE_CLASS

		store the DEVICE_CLASS and schema_mapping in schemaDB

	def get_schema_mapping(DEVICE_CLASS):
		get DEVICE_CLASS from schemaDB
		return it.
