import json
import asyncio
import aiohttp
import pytest


async def get_current_test(url, test_name, test):
	async with aiohttp.ClientSession() as session:
		try:
			async with session.post(url, json=test) as res:
				return {test_name: await res.json()}
		except aiohttp.ServerDisconnectedError:
			return {test_name: "Ошибка отключения сервера"}


def get_very_big_str():
	with open('very_big_string.txt', 'r') as file:
		very_big_str = file.read()
	return very_big_str


def get_big_str():
	with open('big_string.txt', 'r') as file:
		big_str = file.read()
	return big_str


class TestS:
	file = 'tests.json'
	tests = {}
	answers_dict = {}
	url = 'http://127.0.0.1:8080/converter'

	def setup_class(self):
		with open(TestS.file, 'r') as test_file:
			TestS.tests = json.load(test_file)
		TestS.tests['big_str'] = {
			"test": {
				"string": get_big_str()
			},
			"response": {
				"number": 6
			}
		}
		TestS.tests['very_big_str'] = {
			"test": {
				"string": get_very_big_str()
			},
			"response": {
				"number": 70392
			}
		}
		requests_functions = []
		for test in TestS.tests:
			requests_functions.append(get_current_test(TestS.url, test, TestS.tests[test]['test']))
		loop = asyncio.get_event_loop()
		answers = loop.run_until_complete(asyncio.gather(*requests_functions))
		for a in answers:
			TestS.answers_dict.update(a)

	def test_42(self):
		test_name = '42'
		test_output = TestS.tests[test_name]['response']
		output = TestS.answers_dict[test_name]
		assert test_output == output

	def test_simple(self):
		test_name = 'simple'
		test_output = TestS.tests[test_name]['response']
		output = TestS.answers_dict[test_name]
		assert test_output == output

	def test__empty(self):
		test_name = 'empty'
		test_output = TestS.tests[test_name]['response']
		output = TestS.answers_dict[test_name]
		assert test_output == output

	def test_single(self):
		test_name = 'single'
		test_output = TestS.tests[test_name]['response']
		output = TestS.answers_dict[test_name]
		assert test_output == output

	def test_single_digit(self):
		test_name = 'single_digit'
		test_output = TestS.tests[test_name]['response']
		output = TestS.answers_dict[test_name]
		assert test_output == output

	def test_hard(self):
		test_name = 'hard'
		test_output = TestS.tests[test_name]['response']
		output = TestS.answers_dict[test_name]
		assert test_output == output

	def test_not_string(self):
		test_name = 'not_string'
		test_output = TestS.tests[test_name]['response']
		output = TestS.answers_dict[test_name]
		assert test_output == output

	def test_alphabet(self):
		test_name = 'alphabet'
		test_output = TestS.tests[test_name]['response']
		output = TestS.answers_dict[test_name]
		assert test_output == output

	def test_only_digits(self):
		test_name = 'only_digits'
		test_output = TestS.tests[test_name]['response']
		output = TestS.answers_dict[test_name]
		assert test_output == output

	def test_spec_chars(self):
		test_name = 'spec_chars'
		test_output = TestS.tests[test_name]['response']
		output = TestS.answers_dict[test_name]
		assert test_output == output

	def test_invalid_field_name(self):
		test_name = 'invalid_field_name'
		test_output = TestS.tests[test_name]['response']
		output = TestS.answers_dict[test_name]
		assert test_output == output

	def test_unicode(self):
		test_name = 'unicode'
		test_output = TestS.tests[test_name]['response']
		output = TestS.answers_dict[test_name]
		assert test_output == output

	def test_big_str(self):
		test_name = 'big_str'
		test_output = TestS.tests[test_name]['response']
		output = TestS.answers_dict[test_name]
		assert test_output == output

	def test_very_big_str(self):
		test_name = 'very_big_str'
		test_output = TestS.tests[test_name]['response']
		output = TestS.answers_dict[test_name]
		assert test_output == output
