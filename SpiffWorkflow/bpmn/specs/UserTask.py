# -*- coding: utf-8 -*-
from __future__ import division
# Copyright (C) 2012 Matthew Hampton
#
# This library is free software; you can redistribute it and/or
# modify it under the terms of the GNU Lesser General Public
# License as published by the Free Software Foundation; either
# version 2.1 of the License, or (at your option) any later version.
#
# This library is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the GNU
# Lesser General Public License for more details.
#
# You should have received a copy of the GNU Lesser General Public
# License along with this library; if not, write to the Free Software
# Foundation, Inc., 51 Franklin Street, Fifth Floor, Boston, MA
# 02110-1301  USA

from .BpmnSpecMixin import BpmnSpecMixin
from ...specs.Simple import Simple


class UserTask(Simple, BpmnSpecMixin):
    """
    Task Spec for a bpmn:userTask node.
    """

    def is_engine_task(self):
        return False

    # Note that we can reuse the super's serialize()
    @classmethod
    def deserialize(cls, serializer, wf_spec, s_state):
        almost_user_task: Simple = serializer.deserialize_simple(wf_spec, s_state)
        user_task: UserTask = almost_user_task
        user_task.__class__ = UserTask
        return user_task
