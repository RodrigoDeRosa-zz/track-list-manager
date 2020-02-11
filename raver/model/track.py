from __future__ import annotations

from raver.model.camelot_wheel import CamelotWheel


class Track:

    def __init__(self, track_id, key):
        self.track_id = track_id
        self.key = key

    def in_key_with(self, other: Track):
        return CamelotWheel.keys_are_harmonic(self.key, other.key)
