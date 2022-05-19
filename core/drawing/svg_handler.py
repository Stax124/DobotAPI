from importlib.resources import path
from typing import NamedTuple
from svg.path import parse_path
from core.dobot_interfaces import Position2D
from xml.dom import minidom


class VectorPath(NamedTuple):
    id: int
    points: list[Position2D]


class Handler:
    def __init__(self, quality) -> None:
        self.svg = None
        self.basic_svg = """<svg viewBox="0 0 100 100" xmlns="http://www.w3.org/2000/svg">
            <path fill="none" stroke="red"
                d="M 10,30
                    A 20,20 0,0,1 50,30
                    A 20,20 0,0,1 90,30
                    Q 90,60 50,90
                    Q 10,60 10,30 z" />
            </svg>"""
        self.doc = None
        self.paths = []
        self.quality = quality
        self.load_svg(self.basic_svg, self.quality)

    def load_svg(self, svg, quality):
        self.svg = svg
        doc = minidom.parseString(self.svg)
        paths = self.points_from_doc(
            doc, density=quality, scale=1, offset=(0, 5))
        doc.unlink()
        self.paths = paths
        return paths

    def get_paths(self) -> list[VectorPath]:
        return self.paths

    def get_point_at(self, path, distance, scale, offset):
        pos = path.point(distance)
        pos += offset
        pos *= scale
        return pos.real, pos.imag

    def points_from_path(self, path, density, scale, offset):
        step = int(path.length() * density)
        last_step = step - 1

        if last_step == 0:
            yield self.get_point_at(path, 0, scale, offset)
            return

        for distance in range(step):
            yield self.get_point_at(
                path, distance / last_step, scale, offset)

    def points_from_doc(self, doc, density=5., scale=1., offset=(0, 0)):
        offset = offset[0] + offset[1] * 1j
        paths: list[VectorPath] = []
        for element in doc.getElementsByTagName("path"):
            points = []
            for path in parse_path(element.getAttribute("d")):
                points.extend(self.points_from_path(
                    path, density, scale, offset))
            new_points = []
            for point in points:
                new_points.append(Position2D(point[0], point[1]))
            paths.append(VectorPath(0, new_points))  # type: ignore
        return paths
