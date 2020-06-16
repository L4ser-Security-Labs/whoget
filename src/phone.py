#!/usr/bin/python
#coding=utf-8

__AUTHOR__	= "L4ser Secruity Labs"
__DATE__	= "15/06/2020"
__VERSION__	= "0.0.1"
__GITHUB__	= "https://github.com/L4ser-Security-Labs"

'''OSINT tool  for Nigerian Phone numbers'''

"""
    Copyright (C) 2020 L4ser Security Labs
    This program is free software; you can redistribute it and/or modify
    it under the terms of the GNU General Public License as published by
    the Free Software Foundation; either version 2 of the License, or
    (at your option) any later version.
    This program is distributed in the hope that it will be useful,
    but WITHOUT ANY WARRANTY; without even the implied warranty of
    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
    GNU General Public License for more details.
"""
import phonenumbers
from phonenumbers import carrier
from phonenumbers import geocoder
from phonenumbers import timezone


def allinfo(ngnumber):
	# Basic OSINT INFO	
	target_info = phonenumbers.parse(ngnumber, "NG")

	# Geocode information
	target_geocode = geocoder.description_for_number(target_info, "en")
	
	# Carrier information
	target_carrier = carrier.name_for_number(target_info, "en")	

	# Timezone information
	target_timezone = timezone.time_zones_for_number(target_info)

	return {
		"phone": ngnumber,
		"carrier": target_carrier,
		"geocode": target_geocode,
		"timezone": target_timezone
	}
	pass

def geocode_info(ngnumber):
	# Basic OSINT Info
	target_info = phonenumbers.parse(ngnumber, "NG")

	# Geocode information
	target_geocode = geocoder.description_for_number(target_info, "en")
	
	return {
		"phone": ngnumber,
		"geocode": target_geocode,
	}

def carrier_info(ngnumber):
	# Basic OSINT Info
	target_info = phonenumbers.parse(ngnumber, "NG")

	# Carrier information
	target_carrier = carrier.name_for_number(target_info, "en")	
	
	return {
		"phone": ngnumber,
		"carrier": target_carrier,
	}	

def timezone_info(ngnumber):
	# Basic OSINT Info
	target_info = phonenumbers.parse(ngnumber, "NG")

	# Timezone information
	target_timezone = timezone.time_zones_for_number(target_info)
	
	return {
		"phone": ngnumber,
		"timezone": target_timezone
	}		

