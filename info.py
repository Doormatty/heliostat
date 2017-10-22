# -*- coding: utf-8 -*-
from pyepsolartracer.client import EPsolarTracerClient
from pyepsolartracer.registers import registers, coils
import simplejson
import copy
from pprint import pprint

interest = {
    'Charging equipment input power': {
        'description': 'PV array power'},
    'Charging equipment input current': {
        'description': 'PV array current'},
    'Charging equipment input voltage': {
        'description': 'PV array voltage}'},
    'Charging equipment output current': {
        'description': 'Battery charging current'},
    'Charging equipment input power L': {
        'description': 'Solar charge controller--PV array power'},
    'Charging equipment rated input voltage': {
        'description': 'PV array max voltage'},
    'Discharging equipment output power': {
        'description': 'Load power'},
    'Battery status': {
        'description': 'D3-D0: 01H Overvolt , 00H Normal , 02H Under Volt, 03H Low Volt Disconnect, 04H Fault D7-D4: 00H Normal, 01H Over Temp.(Higher than the warning settings), 02H Low Temp.( Lower than the warning settings), D8: Battery inerternal resistance abnormal 1, normal 0 D15: 1-Wrong identification for rated voltage'},
    'Charging equipment status': {
        'description': 'D15-D14: Input volt status. 00 normal, 01 no power connected, 02H Higher volt input, 03H Input volt error. D13: Charging MOSFET is short. D12: Charging or Anti-reverse MOSFET is short. D11: Anti-reverse MOSFET is short. D10: Input is over current. D9: The load is Over current. D8: The load is short. D7: Load MOSFET is short. D4: PV Input is short. D3-2: Charging status. 00 No charging,01 Float,02 Boost,03 Equlization. D1: 0 Normal, 1 Fault. D0: 1 Running, 0 Standby.'},
    'Battery Temp.': {
        'description': 'Battery Temp.'},
    'Battery Temperature': {
        'description': 'Battery Temperature'},
    'Ambient Temp.': {
        'description': 'Ambient Temp.'},
    'Power components temperature': {
        'description': "Heat sink surface temperature of equipments' power components"},
    'Temperature inside equipment': {
        'description': 'Temperature inside case'},
    'Battery Current H': {
        'description': 'Battery Current H'},
    'Battery Current L': {
        'description': 'The net battery current,charging current minus the discharging one. The positive value represents charging and negative, discharging.'},
    'Charging equipment input power H': {
        'description': 'Charging equipment input power H'},
    'Charging equipment rated output power': {
        'description': 'Rated charging power to battery'},
    'Battery rated voltage code': {
        'description': '0, auto recognize. 1-12V, 2-24V'},
    'Discharging equipment output voltage': {
        'description': 'Load voltage'},
    'Battery Current': {
        'description': 'The net battery current,charging current minus the discharging one. The positive value represents charging and negative, discharging.'},
    'Charging equipment output power': {
        'description': 'Battery charging power'},
    'Charging limit voltage': {
        'description': 'Charging limit voltage'},
}

def get_charger_data(registers):
    client = EPsolarTracerClient(serialclient=None)
    client.connect()
    output = dict()
    for key in registers.iterkeys():
        value = client.read_input(key)
        output[key] = {'name': value.register.name, 'description': value.register.description, 'value': value.value}
    client.close()
    return output


# configure the client logging
import logging

logging.basicConfig()
log = logging.getLogger()
log.setLevel(logging.INFO)


output=get_charger_data(interest)

for key in output.iterkeys():
    print "{}: {}".format(output[key]['name'], output[key]['value'])



