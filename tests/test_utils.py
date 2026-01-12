import datetime
from unittest import TestCase

from bai2.constants import TypeCodes
from bai2.exceptions import NotSupportedYetException
from bai2.utils import (
    parse_date,
    parse_military_time,
    parse_time,
    parse_type_code,
    write_time,
)


class ParseDateTestCase(TestCase):
    def test_parse(self):
        parsed = parse_date("150330")
        self.assertEqual(
            datetime.date(year=2015, month=3, day=30),
            parsed,
        )


class ParseTimeTestCase(TestCase):
    def test_clock_time(self):
        parsed_value = parse_time("21:45:34")

        self.assertEqual(
            datetime.time(hour=21, minute=45, second=34),
            parsed_value,
        )

    def test_military_time(self):
        parsed_value = parse_time("2145")

        self.assertEqual(
            datetime.time(hour=21, minute=45),
            parsed_value,
        )


class ParseMilitaryTime(TestCase):
    def test_parse(self):
        parsed_value = parse_military_time("2145")

        self.assertEqual(
            datetime.time(hour=21, minute=45),
            parsed_value,
        )

    def test_parse_end_of_day_as_9999(self):
        parsed_value = parse_military_time("9999")

        self.assertEqual(
            datetime.time.max,
            parsed_value,
        )

    def test_parse_end_of_day_as_2400(self):
        parsed_value = parse_military_time("2400")

        self.assertEqual(
            datetime.time.max,
            parsed_value,
        )

    def test_parse_beginning_of_day(self):
        parsed_value = parse_military_time("0000")

        self.assertEqual(
            datetime.time(hour=0, minute=0),
            parsed_value,
        )


class WriteTime(TestCase):
    def test_write_intra_day_time_with_setting_false(self):
        time = datetime.time(hour=17, minute=59)

        str_value = write_time(time, False)
        self.assertEqual(str_value, "1759")

    def test_write_intra_day_time_with_setting_true(self):
        time = datetime.time(hour=17, minute=59, second=0)

        str_value = write_time(time, True)
        self.assertEqual(str_value, "17:59:00")

    def test_write_end_of_day_time_with_setting_false(self):
        time = datetime.time.max

        str_value = write_time(time, False)
        self.assertEqual(str_value, "2400")

    def test_write_end_of_day_time_with_setting_true(self):
        time = datetime.time.max

        str_value = write_time(time, True)
        self.assertEqual(str_value, "2400")


class TestParseTypeCode(TestCase):
    def test_parse_type_code(self):
        parsed_value = parse_type_code("165")
        self.assertEqual(TypeCodes["165"], parsed_value)

    def test_parse_type_code_with_empty_string(self):
        parsed_value = parse_type_code("")
        self.assertEqual(TypeCodes[""], parsed_value)

    def test_parse_type_code_with_none(self):
        parsed_value = parse_type_code(None)
        self.assertEqual(TypeCodes[""], parsed_value)

    def test_parse_type_code_with_whitespace(self):
        parsed_value = parse_type_code("  165  ")
        self.assertEqual(TypeCodes["165"], parsed_value)

    def test_parse_type_code_with_invalid_type_code(self):
        self.assertRaises(NotSupportedYetException, parse_type_code, "ABC")
