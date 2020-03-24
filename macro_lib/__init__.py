try:
	import numpy
except:
	raise ImportError("numpy is needed for the library to function")
try:
	import pandas
except:
	raise ImportError("pandas is needed for the library to function")
from ._assist import introduce
from ._assist import version
