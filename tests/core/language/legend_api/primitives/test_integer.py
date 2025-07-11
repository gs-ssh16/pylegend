# Copyright 2023 Goldman Sachs
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#      http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

import typing
from pylegend._typing import PyLegendCallable
from pylegend.core.databse.sql_to_string import (
    SqlToStringFormat,
    SqlToStringConfig,
    SqlToStringDbExtension,
)
from pylegend.core.tds.tds_frame import FrameToSqlConfig
from pylegend.core.tds.tds_frame import FrameToPureConfig
from pylegend.extensions.tds.legend_api.frames.legend_api_table_spec_input_frame import LegendApiTableSpecInputFrame
from pylegend.core.tds.tds_column import PrimitiveTdsColumn
from pylegend.core.language import LegendApiTdsRow, LegendApiPrimitive, LegendApiInteger


class TestLegendApiInteger:
    frame_to_sql_config = FrameToSqlConfig()
    frame_to_pure_config = FrameToPureConfig()
    db_extension = SqlToStringDbExtension()
    sql_to_string_config = SqlToStringConfig(SqlToStringFormat(pretty=True))
    test_frame = LegendApiTableSpecInputFrame(['test_schema', 'test_table'], [
        PrimitiveTdsColumn.integer_column("col1"),
        PrimitiveTdsColumn.integer_column("col2")
    ])
    tds_row = LegendApiTdsRow.from_tds_frame("t", test_frame)
    base_query = test_frame.to_sql_query_object(frame_to_sql_config)

    def test_integer_col_access(self) -> None:
        assert self.__generate_sql_string(lambda x: x.get_integer("col2")) == '"root".col2'
        assert self.__generate_pure_string(lambda x: x.get_integer("col2")) == '$t.col2'

    def test_integer_add_expr(self) -> None:
        assert self.__generate_sql_string(lambda x: x.get_integer("col2") + x.get_integer("col1")) == \
               '("root".col2 + "root".col1)'
        assert self.__generate_sql_string(lambda x: x.get_integer("col2") + 10) == \
               '("root".col2 + 10)'
        assert self.__generate_sql_string(lambda x: 10 + x.get_integer("col2")) == \
               '(10 + "root".col2)'
        assert self.__generate_pure_string(lambda x: x.get_integer("col2") + x.get_integer("col1")) == \
               '($t.col2 + $t.col1)'
        assert self.__generate_pure_string(lambda x: x.get_integer("col2") + 10) == \
               '($t.col2 + 10)'
        assert self.__generate_pure_string(lambda x: 10 + x.get_integer("col2")) == \
               '(10 + $t.col2)'

    def test_integer_float_add_expr(self) -> None:
        assert self.__generate_sql_string_no_integer_assert(lambda x: x.get_integer("col2") + 1.2) == \
               '("root".col2 + 1.2)'
        assert self.__generate_sql_string_no_integer_assert(lambda x: 1.2 + x.get_integer("col2")) == \
               '(1.2 + "root".col2)'
        assert self.__generate_pure_string(lambda x: x.get_integer("col2") + 1.2) == \
               '($t.col2 + 1.2)'
        assert self.__generate_pure_string(lambda x: 1.2 + x.get_integer("col2")) == \
               '(1.2 + $t.col2)'

    def test_integer_subtract_expr(self) -> None:
        assert self.__generate_sql_string(lambda x: x.get_integer("col2") - x.get_integer("col1")) == \
               '("root".col2 - "root".col1)'
        assert self.__generate_sql_string(lambda x: x.get_integer("col2") - 10) == \
               '("root".col2 - 10)'
        assert self.__generate_sql_string(lambda x: 10 - x.get_integer("col2")) == \
               '(10 - "root".col2)'
        assert self.__generate_pure_string(lambda x: x.get_integer("col2") - x.get_integer("col1")) == \
               '($t.col2 - $t.col1)'
        assert self.__generate_pure_string(lambda x: x.get_integer("col2") - 10) == \
               '($t.col2 - 10)'
        assert self.__generate_pure_string(lambda x: 10 - x.get_integer("col2")) == \
               '(10 - $t.col2)'

    def test_integer_float_subtract_expr(self) -> None:
        assert self.__generate_sql_string_no_integer_assert(lambda x: x.get_integer("col2") - 1.2) == \
               '("root".col2 - 1.2)'
        assert self.__generate_sql_string_no_integer_assert(lambda x: 1.2 - x.get_integer("col2")) == \
               '(1.2 - "root".col2)'
        assert self.__generate_pure_string(lambda x: x.get_integer("col2") - 1.2) == \
               '($t.col2 - 1.2)'
        assert self.__generate_pure_string(lambda x: 1.2 - x.get_integer("col2")) == \
               '(1.2 - $t.col2)'

    def test_integer_multiply_expr(self) -> None:
        assert self.__generate_sql_string(lambda x: x.get_integer("col2") * x.get_integer("col1")) == \
               '("root".col2 * "root".col1)'
        assert self.__generate_sql_string(lambda x: x.get_integer("col2") * 10) == \
               '("root".col2 * 10)'
        assert self.__generate_sql_string(lambda x: 10 * x.get_integer("col2")) == \
               '(10 * "root".col2)'
        assert self.__generate_pure_string(lambda x: x.get_integer("col2") * x.get_integer("col1")) == \
               '($t.col2 * $t.col1)'
        assert self.__generate_pure_string(lambda x: x.get_integer("col2") * 10) == \
               '($t.col2 * 10)'
        assert self.__generate_pure_string(lambda x: 10 * x.get_integer("col2")) == \
               '(10 * $t.col2)'

    def test_integer_float_multiply_expr(self) -> None:
        assert self.__generate_sql_string_no_integer_assert(lambda x: x.get_integer("col2") * 1.2) == \
               '("root".col2 * 1.2)'
        assert self.__generate_sql_string_no_integer_assert(lambda x: 1.2 * x.get_integer("col2")) == \
               '(1.2 * "root".col2)'
        assert self.__generate_pure_string(lambda x: x.get_integer("col2") * 1.2) == \
               '($t.col2 * 1.2)'
        assert self.__generate_pure_string(lambda x: 1.2 * x.get_integer("col2")) == \
               '(1.2 * $t.col2)'

    def test_integer_modulo_expr(self) -> None:
        assert self.__generate_sql_string(lambda x: x.get_integer("col2") % x.get_integer("col1")) == \
               'MOD("root".col2, "root".col1)'
        assert self.__generate_sql_string(lambda x: x.get_integer("col2") % 10) == \
               'MOD("root".col2, 10)'
        assert self.__generate_sql_string(lambda x: 10 % x.get_integer("col2")) == \
               'MOD(10, "root".col2)'
        assert self.__generate_pure_string(lambda x: x.get_integer("col2") % x.get_integer("col1")) == \
               '($t.col2 % $t.col1)'
        assert self.__generate_pure_string(lambda x: x.get_integer("col2") % 10) == \
               '($t.col2 % 10)'
        assert self.__generate_pure_string(lambda x: 10 % x.get_integer("col2")) == \
               '(10 % $t.col2)'

    def test_integer_abs_expr(self) -> None:
        assert self.__generate_sql_string(lambda x: abs(x.get_integer("col2"))) == \
               'ABS("root".col2)'
        assert self.__generate_sql_string(lambda x: abs(x.get_integer("col2") + x.get_integer("col1"))) == \
               'ABS(("root".col2 + "root".col1))'
        assert self.__generate_pure_string(lambda x: abs(x.get_integer("col2"))) == \
               '$t.col2->abs()'
        assert self.__generate_pure_string(lambda x: abs(x.get_integer("col2") + x.get_integer("col1"))) == \
               '($t.col2 + $t.col1)->abs()'

    def test_integer_neg_expr(self) -> None:
        assert self.__generate_sql_string(lambda x: -x.get_integer("col2")) == \
               '(0 - "root".col2)'
        assert self.__generate_sql_string(lambda x: -(x.get_integer("col2") + x.get_integer("col1"))) == \
               '(0 - ("root".col2 + "root".col1))'
        assert self.__generate_pure_string(lambda x: -x.get_integer("col2")) == \
               '$t.col2->minus()'
        assert self.__generate_pure_string(lambda x: -(x.get_integer("col2") + x.get_integer("col1"))) == \
               '($t.col2 + $t.col1)->minus()'

    def test_integer_pos_expr(self) -> None:
        assert self.__generate_sql_string(lambda x: + x.get_integer("col2")) == \
               '"root".col2'
        assert self.__generate_sql_string(lambda x: +(x.get_integer("col2") + x.get_integer("col1"))) == \
               '("root".col2 + "root".col1)'
        assert self.__generate_pure_string(lambda x: + x.get_integer("col2")) == \
               '$t.col2'
        assert self.__generate_pure_string(lambda x: +(x.get_integer("col2") + x.get_integer("col1"))) == \
               '($t.col2 + $t.col1)'

    @typing.no_type_check
    def test_integer_equals_expr(self) -> None:
        assert self.__generate_sql_string_no_integer_assert(lambda x: x["col2"] == x["col1"]) == \
               '("root".col2 = "root".col1)'
        assert self.__generate_sql_string_no_integer_assert(lambda x: x["col2"] == 1) == \
               '("root".col2 = 1)'
        assert self.__generate_sql_string_no_integer_assert(lambda x: 1 == x["col2"]) == \
               '("root".col2 = 1)'
        assert self.__generate_sql_string_no_integer_assert(lambda x: 1 == (x["col2"] + x["col1"])) == \
               '(("root".col2 + "root".col1) = 1)'
        assert self.__generate_pure_string(lambda x: x["col2"] == x["col1"]) == \
               '($t.col2 == $t.col1)'
        assert self.__generate_pure_string(lambda x: x["col2"] == 1) == \
               '($t.col2 == 1)'
        assert self.__generate_pure_string(lambda x: 1 == x["col2"]) == \
               '($t.col2 == 1)'
        assert self.__generate_pure_string(lambda x: 1 == (x["col2"] + x["col1"])) == \
               '(($t.col2 + $t.col1) == 1)'

    def __generate_sql_string(self, f: PyLegendCallable[[LegendApiTdsRow], LegendApiPrimitive]) -> str:
        ret = f(self.tds_row)
        assert isinstance(ret, LegendApiInteger)
        return self.db_extension.process_expression(
            ret.to_sql_expression({"t": self.base_query}, self.frame_to_sql_config),
            config=self.sql_to_string_config
        )

    def __generate_sql_string_no_integer_assert(self, f: PyLegendCallable[[LegendApiTdsRow], LegendApiPrimitive]) -> str:
        ret = f(self.tds_row)
        return self.db_extension.process_expression(
            ret.to_sql_expression({"t": self.base_query}, self.frame_to_sql_config),
            config=self.sql_to_string_config
        )

    def __generate_pure_string(self, f) -> str:  # type: ignore
        return str(f(self.tds_row).to_pure_expression(self.frame_to_pure_config))
