from __future__ import annotations
from typing import *
from dataclasses import dataclass


@dataclass
class SearchResult:
    room_infos: List[RoomInfo]

    @classmethod
    def from_list(cls, l: List[Dict]) -> SearchResult:
        return cls(room_infos=[RoomInfo.from_dict(element) for element in l])

    def __str__(self):
        return '\n'.join([str(info) for info in self.room_infos])


@dataclass
class RoomInfo:
    total_room_count: int
    available_room_count: int
    room_area_name: str
    room_area_no: int
    use_amount: Optional[int]

    @classmethod
    def from_dict(cls, d: dict) -> RoomInfo:
        return cls(
            total_room_count=d['TOT_ROOM_CNT'],
            available_room_count=d['ROOM_CNT'],
            room_area_name=d['ROOM_AREA_NAME'],
            room_area_no=d['ROOM_AREA_NO'],
            use_amount=d['USE_AMT']
        )

    def __str__(self):
        result = f'[{self.room_area_no}]{self.room_area_name} ({self.available_room_count}/{self.total_room_count}): '
        result += self.use_amount if self.use_amount else 'Not available'
        return result
