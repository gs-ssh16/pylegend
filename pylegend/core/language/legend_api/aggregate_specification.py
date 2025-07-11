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

from pylegend._typing import (
    PyLegendSequence,
    PyLegendCallable
)
from pylegend.core.language.legend_api.primitive_collection import LegendApiPrimitiveCollection
from pylegend.core.language import (
    LegendApiTdsRow,
    LegendApiPrimitive,
    LegendApiPrimitiveOrPythonPrimitive,
)

__all__: PyLegendSequence[str] = [
    "LegendApiAggregateSpecification",
    "agg",
]


class LegendApiAggregateSpecification:
    __map_fn: PyLegendCallable[[LegendApiTdsRow], LegendApiPrimitiveOrPythonPrimitive]
    __aggregate_fn: PyLegendCallable[[LegendApiPrimitiveCollection], LegendApiPrimitive]
    __name: str

    def __init__(
            self,
            map_fn: PyLegendCallable[[LegendApiTdsRow], LegendApiPrimitiveOrPythonPrimitive],
            aggregate_fn: PyLegendCallable[[LegendApiPrimitiveCollection], LegendApiPrimitive],
            name: str
    ) -> None:
        self.__map_fn = map_fn
        self.__aggregate_fn = aggregate_fn
        self.__name = name

    def get_name(self) -> str:
        return self.__name

    def get_map_fn(self) -> PyLegendCallable[[LegendApiTdsRow], LegendApiPrimitiveOrPythonPrimitive]:
        return self.__map_fn

    def get_aggregate_fn(self) -> PyLegendCallable[[LegendApiPrimitiveCollection], LegendApiPrimitive]:
        return self.__aggregate_fn


def agg(
    map_fn: PyLegendCallable[[LegendApiTdsRow], LegendApiPrimitiveOrPythonPrimitive],
    aggregate_fn: PyLegendCallable[[LegendApiPrimitiveCollection], LegendApiPrimitive],
    name: str
) -> LegendApiAggregateSpecification:
    return LegendApiAggregateSpecification(map_fn=map_fn, aggregate_fn=aggregate_fn, name=name)
