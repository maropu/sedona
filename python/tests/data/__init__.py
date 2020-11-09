#  Licensed to the Apache Software Foundation (ASF) under one
#  or more contributor license agreements.  See the NOTICE file
#  distributed with this work for additional information
#  regarding copyright ownership.  The ASF licenses this file
#  to you under the Apache License, Version 2.0 (the
#  "License"); you may not use this file except in compliance
#  with the License.  You may obtain a copy of the License at
#
#    http://www.apache.org/licenses/LICENSE-2.0
#
#  Unless required by applicable law or agreed to in writing,
#  software distributed under the License is distributed on an
#  "AS IS" BASIS, WITHOUT WARRANTIES OR CONDITIONS OF ANY
#  KIND, either express or implied.  See the License for the
#  specific language governing permissions and limitations
#  under the License.

import os
from os import path

from tests.tools import tests_path

data_path = path.abspath(path.dirname(__file__))


def create_data_path(relative_path: str) -> str:
    return os.path.join(data_path, relative_path)


mixed_wkb_geometry_input_location = create_data_path("county_small_wkb.tsv")
mixed_wkt_geometry_input_location = os.path.join(tests_path, "data/county_small.tsv")
mixed_wkt_geometry_input_location_1 = os.path.join(tests_path, "data/county_small_1.tsv")
shape_file_input_location = create_data_path("shapefiles/dbf")
shape_file_with_missing_trailing_input_location = create_data_path("shapefiles/missing")
geojson_input_location = create_data_path("testPolygon.json")
area_lm_point_input_location = create_data_path("arealm.csv")
csv_point_input_location = create_data_path("testpoint.csv")
csv_polygon_input_location = create_data_path("testenvelope.csv")
csv_polygon1_input_location = create_data_path("equalitycheckfiles/testequals_envelope1.csv")
csv_polygon2_input_location = create_data_path("equalitycheckfiles/testequals_envelope2.csv")
csv_polygon1_random_input_location = create_data_path("equalitycheckfiles/testequals_envelope1_random.csv")
csv_polygon2_random_input_location = create_data_path("equalitycheckfiles/testequals_envelope2_random.csv")
overlap_polygon_input_location = create_data_path("testenvelope_overlap.csv")
union_polygon_input_location = create_data_path("testunion.csv")
csv_point1_input_location = create_data_path("equalitycheckfiles/testequals_point1.csv")
csv_point2_input_location = create_data_path("equalitycheckfiles/testequals_point2.csv")
geojson_id_input_location = create_data_path("testContainsId.json")
