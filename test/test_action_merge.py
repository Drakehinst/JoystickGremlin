# -*- coding: utf-8; -*-

# Copyright (C) 2015 - 2024 Lionel Ott
#
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program.  If not, see <http://www.gnu.org/licenses/>

import sys
sys.path.append(".")

import pytest
import uuid
from xml.etree import ElementTree

from gremlin.base_classes import DataInsertionMode
from gremlin.error import GremlinError
from gremlin.profile import Library, Profile
import gremlin.types as types
from gremlin.ui.device import InputIdentifier

import action_plugins.merge_axis as merge_axis
from action_plugins.description import DescriptionData


def test_ctor():
    a = merge_axis.MergeAxisData(types.InputType.JoystickAxis)

    assert len(a.children) == 0
    assert a.label == ""
    assert a.operation == merge_axis.MergeOperation.Average
    assert a.axis_in1 == InputIdentifier()
    assert a.axis_in2 == InputIdentifier()


def test_from_xml():
    p = Profile()
    p.from_xml("test/xml/action_merge_axis.xml")

    a = p.library.get_action(uuid.UUID("ac905a47-9ad3-4b65-b702-fbae1d133609"))

    assert len(a.children) == 1
    assert a.label == "test axis merge"
    assert a.operation == merge_axis.MergeOperation.Minimum
    assert a.axis_in1.device_guid == uuid.UUID("4DCB3090-97EC-11EB-8003-444553540001")
    assert a.axis_in1.input_type == types.InputType.JoystickAxis
    assert a.axis_in1.input_id == 1
    assert a.axis_in2.device_guid == uuid.UUID("4DCB3090-97EC-11EB-8003-444553540002")
    assert a.axis_in2.input_type == types.InputType.JoystickAxis
    assert a.axis_in2.input_id ==  2


def test_to_xml():
    d = DescriptionData()
    d._id = uuid.UUID("fbe6be7b-07c9-4400-94f2-caa245ebcc7e")

    a = merge_axis.MergeAxisData(types.InputType.JoystickAxis)
    a.label = "This is a test"
    a.operation = merge_axis.MergeOperation.Maximum
    a.insert_action(d, "children")

    a.axis_in1.device_guid = uuid.UUID("4DCB3090-97EC-11EB-8003-444553540001")
    a.axis_in1.input_type = types.InputType.JoystickAxis
    a.axis_in2.device_guid = uuid.UUID("4DCB3090-97EC-11EB-8003-444553540002")
    a.axis_in1.input_id = 1
    a.axis_in2.input_type = types.InputType.JoystickAxis
    a.axis_in2.input_id =  2

    node = a.to_xml()
    assert node.find(
            "./property/name[.='label']/../value"
        ).text == "This is a test"
    assert node.find(
            "./property/name[.='operation']/../value"
        ).text == "maximum"
    assert node.find(
            "./property/name[.='axis1-axis']/../value"
        ).text == "1"
    assert node.find(
        "./property/name[.='axis1-guid']/../value"
    ).text.upper() == "4DCB3090-97EC-11EB-8003-444553540001"