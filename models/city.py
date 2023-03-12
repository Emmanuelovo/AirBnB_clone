#!/usr/bin/env python3
"""
City class, inherited from BaseModel
"""
from models.base_model import BaseModel


class City(BaseModel):
	"""
	A classs inherited from BaseModel class
	Public class attributes:
		state.id: (str) will be State.id
		name:	  (str)
	"""
	state_id = ""
	 name = ""
