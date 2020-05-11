import json
import asyncio
import aiohttp
import configparser
import pytest


async def get_current_test(url, test_name, test):
	async with aiohttp.ClientSession() as session:
		try:
			async with session.post(url, json=test) as res:
				return {
					test_name: {
						"answer": await res.json(),
						"status_code": res.status
					}
				}
		except aiohttp.ServerDisconnectedError:
			return {
				test_name: {
					"answer": 'Ошибка отключения сервера'
				}
			}


def get_very_big_str():
	with open('very_big_string.txt', 'r') as file:
		very_big_str = file.read()
	return {
		"test": {
			"string": very_big_str
		},
		"response": {
			"number": 70392
		}
	}


def get_big_str():
	with open('big_string.txt', 'r') as file:
		big_str = file.read()
	return {
		"test": {
			"string": big_str
		},
		"response": {
			"number": 6
		}
	}


def read_config():
	config = configparser.ConfigParser()
	config.read('config.ini')
	return config['default']['file'], config['default']['url']]


class TestS:
	file, url = read_config()
	tests = {}
	answers_dict = {}

	def setup_class(self):
		with open(TestS.file, 'r') as test_file:
			TestS.tests = json.load(test_file)
		TestS.tests['big_str'] = get_big_str()
		TestS.tests['very_big_str'] = get_very_big_str()
		requests_functions = []
		for test_name in TestS.tests:
			requests_functions.append(get_current_test(TestS.url, test_name, TestS.tests[test_name]['test']))
		loop = asyncio.get_event_loop()
		answers = loop.run_until_complete(asyncio.gather(*requests_functions))
		for a in answers:
			TestS.answers_dict.update(a)

	def test_42(self):
		test_name = '42'
		test_output = TestS.tests[test_name]['response']
		output = TestS.answers_dict[test_name]['answer']
		assert test_output == output
		assert TestS.answers_dict[test_name]['status_code'] == 200

	def test_simple(self):
		test_name = 'simple'
		test_output = TestS.tests[test_name]['response']
		output = TestS.answers_dict[test_name]['answer']
		assert test_output == output
		assert TestS.answers_dict[test_name]['status_code'] == 200

	def test_empty(self):
		test_name = 'empty'
		test_output = TestS.tests[test_name]['response']
		output = TestS.answers_dict[test_name]['answer']
		assert test_output == output
		assert TestS.answers_dict[test_name]['status_code'] == 200

	def test_single(self):
		test_name = 'single'
		test_output = TestS.tests[test_name]['response']
		output = TestS.answers_dict[test_name]['answer']
		assert test_output == output
		assert TestS.answers_dict[test_name]['status_code'] == 200

	def test_single_digit(self):
		test_name = 'single_digit'
		test_output = TestS.tests[test_name]['response']
		output = TestS.answers_dict[test_name]['answer']
		assert test_output == output
		assert TestS.answers_dict[test_name]['status_code'] == 200

	def test_hard(self):
		test_name = 'hard'
		test_output = TestS.tests[test_name]['response']
		output = TestS.answers_dict[test_name]['answer']
		assert test_output == output
		assert TestS.answers_dict[test_name]['status_code'] == 200

	def test_not_string(self):
		test_name = 'not_string'
		test_output = TestS.tests[test_name]['response']
		output = TestS.answers_dict[test_name]['answer']
		assert test_output == output
		assert TestS.answers_dict[test_name]['status_code'] == 200

	def test_escape_sequence(self):
		test_name = 'escape_sequence'
		test_output = TestS.tests[test_name]['response']
		output = TestS.answers_dict[test_name]['answer']
		assert test_output == output
		assert TestS.answers_dict[test_name]['status_code'] == 200

	def test_cyrillic(self):
		test_name = 'cyrillic'
		test_output = TestS.tests[test_name]['response']
		output = TestS.answers_dict[test_name]['answer']
		assert test_output == output
		assert TestS.answers_dict[test_name]['status_code'] == 200

	def test_alphabet(self):
		test_name = 'alphabet'
		test_output = TestS.tests[test_name]['response']
		output = TestS.answers_dict[test_name]['answer']
		assert test_output == output
		assert TestS.answers_dict[test_name]['status_code'] == 200

	def test_only_digits(self):
		test_name = 'only_digits'
		test_output = TestS.tests[test_name]['response']
		output = TestS.answers_dict[test_name]['answer']
		assert test_output == output
		assert TestS.answers_dict[test_name]['status_code'] == 200

	def test_spec_chars(self):
		test_name = 'spec_chars'
		test_output = TestS.tests[test_name]['response']
		output = TestS.answers_dict[test_name]['answer']
		assert test_output == output
		assert TestS.answers_dict[test_name]['status_code'] == 200

	def test_invalid_field_name(self):
		test_name = 'invalid_field_name'
		test_output = TestS.tests[test_name]['response']
		output = TestS.answers_dict[test_name]['answer']
		assert test_output == output
		assert TestS.answers_dict[test_name]['status_code'] == 200

	def test_unicode(self):
		test_name = 'unicode'
		test_output = TestS.tests[test_name]['response']
		output = TestS.answers_dict[test_name]['answer']
		assert test_output == output
		assert TestS.answers_dict[test_name]['status_code'] == 200

	def test_big_str(self):
		test_name = 'big_str'
		test_output = TestS.tests[test_name]['response']
		output = TestS.answers_dict[test_name]['answer']
		assert test_output == output
		assert TestS.answers_dict[test_name]['status_code'] == 200

	def test_very_big_str(self):
		test_name = 'very_big_str'
		test_output = TestS.tests[test_name]['response']
		output = TestS.answers_dict[test_name]['answer']
		assert test_output == output
		assert TestS.answers_dict[test_name]['status_code'] == 200
