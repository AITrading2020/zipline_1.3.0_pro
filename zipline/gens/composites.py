#
# Copyright 2013 Quantopian, Inc.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

import heapq


def _decorate_source(source):
    for message in source:
        yield ((message.dt, message.source_id), message)


def date_sorted_sources(*sources):
    """
    Takes an iterable of sources, generating namestrings and
    piping their output into date_sort.
    """
    sorted_stream = heapq.merge(*(_decorate_source(s) for s in sources))

    # Strip out key decoration
    for _, message in sorted_stream:
        yield message
