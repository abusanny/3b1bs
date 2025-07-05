from manim import *
import numpy as np
from typing import List, Tuple
from dataclasses import dataclass
from enum import Enum

class PieceType(Enum):
    """Enumeration for different piece types in the cubic decomposition."""
    A_CUBED = "a^3"
    B_CUBED = "b^3"
    A_SQUARED_B = "a^2b"
    A_B_SQUARED = "ab^2"

@dataclass
class CubePiece:
    """Data class representing a piece of the decomposed cube."""
    piece_type: PieceType
    dimensions: Tuple[float, float, float]
    position: np.ndarray
    color: str
    label: str
    count: int = 1
    mobject: VMobject | None = None

class GeometricCubicProofMasterpiece(ThreeDScene):
    """A visual demonstration of (a+b)^3 = a^3 + 3a^2b + 3ab^2 + b^3."""

    def __init__(self, **kwargs):
        self.config = {
            "colors": {
                "a_cube": BLUE_D,
                "b_cube": RED_D,
                "a2b": GREEN_D,
                "ab2": ORANGE,
                "highlight": YELLOW,
                "text": WHITE,
            },
            "dimensions": {
                "a": 2.0,
                "b": 1.2,
                "explosion": 0.6,
            },
        }
        super().__init__(**kwargs)

    def construct(self):
        self._setup_scene()
        self._build_cube()
        self._slice_cube()
        self._separate_pieces()
        self._show_formula()
        self._finale()

    def _setup_scene(self):
        self.set_camera_orientation(phi=70 * DEGREES, theta=-45 * DEGREES)
        self.camera.background_color = "#0e1117"

    def _build_cube(self):
        a = self.config["dimensions"]["a"]
        b = self.config["dimensions"]["b"]
        total = a + b
        cube = Cube(side_length=total)
        cube.set_fill(opacity=0.1)
        cube.set_stroke(WHITE, 2)
        self.main_cube = cube
        self.play(Create(cube))

        length = Line3D(ORIGIN, total * RIGHT, color=RED, stroke_width=6)
        width = Line3D(ORIGIN, total * UP, color=GREEN, stroke_width=6)
        height = Line3D(ORIGIN, total * OUT, color=BLUE, stroke_width=6)
        self.play(LaggedStartMap(Create, VGroup(length, width, height)))

        def edge_parts(direction, color):
            part_a = Line3D(ORIGIN, a * direction, color=color, stroke_width=4)
            part_b = Line3D(a * direction, total * direction, color=color, stroke_width=4)
            return part_a, part_b
        x_a, x_b = edge_parts(RIGHT, RED)
        y_a, y_b = edge_parts(UP, GREEN)
        z_a, z_b = edge_parts(OUT, BLUE)
        self.play(LaggedStartMap(Create, VGroup(x_a, x_b, y_a, y_b, z_a, z_b)))

        labels = VGroup(
            MathTex("a", color=RED).scale(0.6).next_to(x_a, DOWN, SMALL_BUFF),
            MathTex("b", color=RED).scale(0.6).next_to(x_b, DOWN, SMALL_BUFF),
            MathTex("a", color=GREEN).scale(0.6).next_to(y_a, LEFT, SMALL_BUFF),
            MathTex("b", color=GREEN).scale(0.6).next_to(y_b, LEFT, SMALL_BUFF),
            MathTex("a", color=BLUE).scale(0.6).next_to(z_a, OUT, SMALL_BUFF),
            MathTex("b", color=BLUE).scale(0.6).next_to(z_b, OUT, SMALL_BUFF),
        )
        for lab in labels:
            lab.fix_in_frame()
        self.play(LaggedStartMap(Write, labels))
        self.wait()

    def _slice_cube(self):
        a = self.config["dimensions"]["a"]
        b = self.config["dimensions"]["b"]
        total = a + b
        cut = a - total / 2
        planes = []
        colors = [RED_B, GREEN_B, BLUE_B]
        axes = [RIGHT, UP, OUT]
        for col, axis in zip(colors, axes):
            plane = Square(total, stroke_color=col, fill_color=col, fill_opacity=0.2)
            if axis is RIGHT:
                plane.rotate(PI / 2, axis=UP)
            elif axis is UP:
                plane.rotate(PI / 2, axis=RIGHT)
            plane.move_to(self.main_cube.get_center() + axis * cut)
            planes.append(plane)
        for plane in planes:
            self.play(FadeIn(plane))
        self.wait(0.5)
        self.play(*[FadeOut(p) for p in planes])

    def _create_all_pieces(self) -> List[CubePiece]:
        a = self.config["dimensions"]["a"]
        b = self.config["dimensions"]["b"]
        colors = self.config["colors"]
        corner = self.main_cube.get_corner(DL + IN)
        pieces: List[CubePiece] = []

        cube_a = Cube(side_length=a)
        cube_a.set_fill(colors["a_cube"], opacity=0.85)
        cube_a.move_to(corner + (RIGHT + UP + OUT) * a / 2)
        pieces.append(CubePiece(PieceType.A_CUBED, (a, a, a), cube_a.get_center(), colors["a_cube"], "a^3", 1, cube_a))

        cube_b = Cube(side_length=b)
        cube_b.set_fill(colors["b_cube"], opacity=0.85)
        cube_b.move_to(corner + RIGHT * a + UP * a + OUT * a + (RIGHT + UP + OUT) * b / 2)
        pieces.append(CubePiece(PieceType.B_CUBED, (b, b, b), cube_b.get_center(), colors["b_cube"], "b^3", 1, cube_b))

        a2b_specs = [
            ([b, a, a], corner + RIGHT * a + (UP + OUT) * a / 2 + RIGHT * b / 2),
            ([a, b, a], corner + UP * a + (RIGHT + OUT) * a / 2 + UP * b / 2),
            ([a, a, b], corner + OUT * a + (RIGHT + UP) * a / 2 + OUT * b / 2),
        ]
        for dims, pos in a2b_specs:
            prism = self._create_box(dims, colors["a2b"], 0.8)
            prism.move_to(pos)
            pieces.append(CubePiece(PieceType.A_SQUARED_B, tuple(dims), prism.get_center(), colors["a2b"], "a^2b", 1, prism))

        ab2_specs = [
            ([a, b, b], corner + RIGHT * a + UP * a + (OUT * a + (RIGHT + UP) * b / 2 + OUT * b / 2)),
            ([b, a, b], corner + RIGHT * a + OUT * a + (UP * a + (RIGHT + OUT) * b / 2 + UP * b / 2)),
            ([b, b, a], corner + UP * a + OUT * a + (RIGHT * a + (UP + OUT) * b / 2 + RIGHT * b / 2)),
        ]
        for dims, pos in ab2_specs:
            prism = self._create_box(dims, colors["ab2"], 0.8)
            prism.move_to(pos)
            pieces.append(CubePiece(PieceType.A_B_SQUARED, tuple(dims), prism.get_center(), colors["ab2"], "ab^2", 1, prism))

        return pieces

    def _create_box(self, dims: List[float], color: str, opacity: float) -> Polyhedron:
        w, h, d = dims
        verts = [
            (-w/2, -h/2, -d/2), (w/2, -h/2, -d/2), (w/2, h/2, -d/2), (-w/2, h/2, -d/2),
            (-w/2, -h/2, d/2), (w/2, -h/2, d/2), (w/2, h/2, d/2), (-w/2, h/2, d/2),
        ]
        faces = [
            [0,1,2,3], [4,5,6,7], [0,1,5,4], [2,3,7,6], [0,3,7,4], [1,2,6,5]
        ]
        box = Polyhedron(vertex_coords=verts, faces_list=faces)
        box.set_fill(color, opacity=opacity)
        box.set_stroke(WHITE, 2)
        return box

    def _separate_pieces(self):
        self.pieces = self._create_all_pieces()
        self.play(LaggedStart(*[FadeIn(p.mobject) for p in self.pieces], lag_ratio=0.05))
        center = self.main_cube.get_center()
        animations = []
        for p in self.pieces:
            direction = p.position - center
            if np.linalg.norm(direction) == 0:
                direction = OUT
            direction = direction / np.linalg.norm(direction)
            target = p.position + direction * self.config["dimensions"]["explosion"]
            animations.append(p.mobject.animate.move_to(target))
        self.play(*animations)
        self._add_labels()
        self.wait(1)

    def _add_labels(self):
        labels = VGroup()
        for p in self.pieces:
            tex = MathTex(p.label, color=p.color)
            bg = BackgroundRectangle(tex, fill_opacity=0.8, buff=0.1)
            grp = VGroup(bg, tex)
            grp.next_to(p.mobject, OUT, buff=0.1)
            self.add_fixed_orientation_mobjects(grp)
            labels.add(grp)
        self.labels = labels
        self.play(LaggedStart(*[FadeIn(l) for l in labels], lag_ratio=0.1))

    def _show_formula(self):
        formula = MathTex("(a+b)^3 = a^3 + 3a^2b + 3ab^2 + b^3", color=self.config["colors"]["text"])
        bg = BackgroundRectangle(formula, fill_opacity=0.9, buff=0.2)
        grp = VGroup(bg, formula)
        grp.to_edge(DOWN)
        self.add_fixed_in_frame_mobjects(grp)
        self.play(FadeIn(grp))
        self.wait(2)

    def _finale(self):
        self.play(*[FadeOut(l) for l in self.labels])
        self.play(*[FadeOut(p.mobject) for p in self.pieces])
        self.play(FadeOut(self.main_cube))
        thanks = Text("Thanks for watching!", color=self.config["colors"]["text"])
        thanks.to_edge(DOWN)
        self.play(Write(thanks))
        self.wait(2)

