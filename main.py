import json
import sys

from src.core.dryvrmain import verify
from src.common.utils import importSimFunction

from src.plotter.parser import parse
import random
import numpy as np

assert ".json" in sys.argv[-1], "Please provide json input file"
with open(sys.argv[-1], 'r') as f:
	data = json.load(f)
simFunction = importSimFunction(data["directory"])
safety, reach = verify(data, simFunction)
