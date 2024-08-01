#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Jul  3 19:50:29 2024

@author: ana_nunez
"""

class MAtrix:
	
	def __init__(self, mu=0, sigma=1):
	
		""" Generic distribution class for calculating and 
		visualizing a probability distribution.
	
		Attributes:
			mean (float): the mean value of the distribution
			stdev (float): standard deviation of the distribution
			data_list (list of floats): list of floats extracted from a data file
			"""
		
		self.mean = mu
		self.stdev = sigma
		self.data = []