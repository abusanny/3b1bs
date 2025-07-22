#!/usr/bin/env python3
"""
Visual Proof of the Pythagorean Theorem - World-Class Manim Animation
Following the detailed script with precision timing and elegant visual design.

A masterpiece of mathematical visualization demonstrating a² + b² = c² through
the elegant rearrangement of four identical right triangles.
"""

from manim import *
import numpy as np

class PythagoreanVisualProof(Scene):
    def construct(self):
        # Mathematical configuration - using a perfect 3-4-5 triangle
        self.a = 3.0  # Shorter leg
        self.b = 4.0  # Longer leg  
        self.c = 5.0  # Hypotenuse
        
        # Color palette for world-class visual design
        self.bg_color = "#f8f9fa"  # Clean light background
        self.triangle_color = "#2c3e50"  # Elegant dark blue-gray
        self.triangle_stroke = "#34495e"
        self.triangle_fill_opacity = 0.85
        
        # Distinctive colors for the squares
        self.c_square_color = "#3498db"  # Vibrant blue for c²
        self.a_square_color = "#f1c40f"  # Bright yellow for a²
        self.b_square_color = "#e74c3c"  # Bright red for b²
        
        # Typography
        self.text_color = "#2c3e50"
        self.label_font_size = 28
        self.equation_font_size = 48
        
        # Set clean background
        self.camera.background_color = self.bg_color
        
        # Execute the scenes according to the script
        self.scene_1_introduction()      # [00:00 - 00:15]
        self.scene_2_first_arrangement() # [00:16 - 00:45]
        self.scene_3_rearrangement()     # [00:46 - 01:15]
        self.scene_4_second_arrangement()# [01:16 - 01:45]
        self.scene_5_conclusion()        # [01:46 - 02:30]
        
    def create_right_triangle(self):
        """Create a single right triangle with perfect proportions"""
        vertices = [
            ORIGIN,  # Right angle vertex
            self.a * RIGHT,  # End of shorter leg
            self.b * UP  # End of longer leg
        ]
        
        triangle = Polygon(
            *vertices,
            color=self.triangle_stroke,
            fill_color=self.triangle_color,
            fill_opacity=self.triangle_fill_opacity,
            stroke_width=2
        )
        
        return triangle
    
    def scene_1_introduction(self):
        """[00:00 - 00:15] SCENE 1: INTRODUCTION TO THE TRIANGLE"""
        
        # Create the main triangle
        triangle = self.create_right_triangle()
        triangle.move_to(ORIGIN)
        
        # Animate triangle entrance with elegant scaling
        self.play(
            DrawBorderThenFill(triangle),
            run_time=2
        )
        
        # Add the right angle indicator
        right_angle_square = Square(side_length=0.4)
        right_angle_square.set_fill(WHITE, opacity=0.8)
        right_angle_square.set_stroke(self.triangle_stroke, width=1.5)
        right_angle_square.move_to(triangle.get_vertices()[0] + 0.2 * (RIGHT + UP))
        
        self.play(FadeIn(right_angle_square), run_time=0.8)
        
        # Create and position labels with perfect typography
        label_a = MathTex("a", font_size=self.label_font_size, color=self.text_color)
        label_b = MathTex("b", font_size=self.label_font_size, color=self.text_color)
        label_c = MathTex("c", font_size=self.label_font_size, color=self.text_color)
        
        # Position labels elegantly
        label_a.next_to(triangle.get_center() + 0.7 * RIGHT, DOWN, buff=0.15)
        label_b.next_to(triangle.get_center() + 0.7 * UP, LEFT, buff=0.15)
        label_c.next_to(triangle.get_center() + 0.3 * (UP + RIGHT), UR, buff=0.1)
        
        # Animate labels appearing sequentially
        self.play(Write(label_a), run_time=0.6)
        self.play(Write(label_b), run_time=0.6)
        self.play(Write(label_c), run_time=0.6)
        
        # Show the Pythagorean equation briefly
        equation_preview = MathTex(
            "a^2 + b^2 = c^2",
            font_size=self.equation_font_size,
            color=self.text_color
        )
        equation_preview.to_edge(UP, buff=1)
        
        self.play(FadeIn(equation_preview), run_time=1.5)
        self.wait(2)
        self.play(FadeOut(equation_preview), run_time=1)
        
        # Store objects for next scene
        self.base_triangle = triangle
        self.triangle_labels = VGroup(label_a, label_b, label_c)
        self.right_angle_square = right_angle_square
        
        self.wait(1)
    
    def scene_2_first_arrangement(self):
        """[00:16 - 00:45] SCENE 2: THE FIRST ARRANGEMENT"""
        
        # Create three additional triangles
        triangle1 = self.base_triangle.copy()
        triangle2 = self.create_right_triangle()
        triangle3 = self.create_right_triangle()
        triangle4 = self.create_right_triangle()
        
        # Position the additional triangles at the corners initially
        triangle2.move_to(3 * UL)
        triangle3.move_to(3 * UR)
        triangle4.move_to(3 * DL)
        
        # Animate the three triangles sliding in from corners
        self.play(
            triangle2.animate.move_to(2 * UL),
            triangle3.animate.move_to(2 * UR),
            triangle4.animate.move_to(2 * DL),
            run_time=1.5
        )
        
        # Clear labels and right angle indicator for cleaner arrangement
        self.play(
            FadeOut(self.triangle_labels),
            FadeOut(self.right_angle_square),
            run_time=0.8
        )
        
        # Calculate positions for perfect square arrangement
        # The outer square has side length (a + b)
        outer_size = self.a + self.b
        scale_factor = 0.8  # Scale down for better visibility
        
        # Calculate target positions and rotations for each triangle
        # All hypotenuses point inward to form the central c² square
        
        # Triangle 1: Bottom-right
        target1 = triangle1.copy()
        target1.rotate(-PI/2, about_point=target1.get_center())
        target1.move_to((outer_size/2 - self.a/2) * RIGHT + (outer_size/2 - self.b/2) * DOWN)
        target1.scale(scale_factor)
        
        # Triangle 2: Top-right  
        target2 = triangle2.copy()
        target2.rotate(0, about_point=target2.get_center())
        target2.move_to((outer_size/2 - self.b/2) * RIGHT + (outer_size/2 - self.a/2) * UP)
        target2.scale(scale_factor)
        
        # Triangle 3: Top-left
        target3 = triangle3.copy()
        target3.rotate(PI/2, about_point=target3.get_center())
        target3.move_to((outer_size/2 - self.a/2) * LEFT + (outer_size/2 - self.b/2) * UP)
        target3.scale(scale_factor)
        
        # Triangle 4: Bottom-left
        target4 = triangle4.copy()
        target4.rotate(PI, about_point=target4.get_center())
        target4.move_to((outer_size/2 - self.b/2) * LEFT + (outer_size/2 - self.a/2) * DOWN)
        target4.scale(scale_factor)
        
        # Animate the elegant choreographed arrangement
        self.play(
            Transform(triangle1, target1),
            Transform(triangle2, target2),
            Transform(triangle3, target3),
            Transform(triangle4, target4),
            run_time=3,
            rate_func=smooth
        )
        
        # Create the central c² square (tilted)
        central_square = Square(side_length=self.c * scale_factor * 0.6)
        central_square.set_fill(self.c_square_color, opacity=0.9)
        central_square.set_stroke(self.c_square_color, width=3)
        central_square.rotate(PI/4)  # Tilt the square
        central_square.move_to(ORIGIN)
        
        # Highlight the central square with a flash
        self.play(
            FadeIn(central_square),
            run_time=1.5
        )
        
        # Add c labels to each side of the inner square
        c_labels = VGroup()
        for i in range(4):
            label = MathTex("c", font_size=self.label_font_size-4, color=WHITE)
            # Position labels on the sides of the tilted square
            angle = i * PI/2 + PI/4
            position = central_square.get_center() + 0.8 * (np.cos(angle) * RIGHT + np.sin(angle) * UP)
            label.move_to(position)
            c_labels.add(label)
        
        self.play(Write(c_labels), run_time=1)
        
        # Add the "Area = c²" text
        area_c_text = MathTex("\\text{Area} = c^2", font_size=32, color=WHITE)
        area_c_text.move_to(central_square.get_center())
        
        self.play(Write(area_c_text), run_time=1.5)
        
        # Store objects for next scene
        self.triangles = [triangle1, triangle2, triangle3, triangle4]
        self.central_square = central_square
        self.c_labels = c_labels
        self.area_c_text = area_c_text
        
        self.wait(2)
    
    def scene_3_rearrangement(self):
        """[00:46 - 01:15] SCENE 3: THE REARRANGEMENT"""
        
        # Clear the central square elements for clean rearrangement
        self.play(
            FadeOut(self.central_square),
            FadeOut(self.c_labels),
            FadeOut(self.area_c_text),
            run_time=1
        )
        
        # Create target positions for the two rectangles arrangement
        # Left rectangle and right rectangle, side by side
        
        rect_offset = 2.5
        triangle_scale = 0.9
        
        # Left rectangle: Top-left and bottom-right triangles align horizontally
        left_triangle1 = self.create_right_triangle()
        left_triangle1.scale(triangle_scale)
        left_triangle1.move_to(LEFT * rect_offset + UP * (self.b * triangle_scale / 2))
        
        left_triangle2 = self.create_right_triangle()
        left_triangle2.scale(triangle_scale)
        left_triangle2.rotate(PI)
        left_triangle2.move_to(LEFT * rect_offset + DOWN * (self.b * triangle_scale / 2))
        
        # Right rectangle: Top-right and bottom-left triangles align vertically
        right_triangle1 = self.create_right_triangle()
        right_triangle1.scale(triangle_scale)
        right_triangle1.rotate(-PI/2)
        right_triangle1.move_to(RIGHT * rect_offset + LEFT * (self.a * triangle_scale / 2))
        
        right_triangle2 = self.create_right_triangle()
        right_triangle2.scale(triangle_scale)
        right_triangle2.rotate(PI/2)
        right_triangle2.move_to(RIGHT * rect_offset + RIGHT * (self.a * triangle_scale / 2))
        
        # Perform the fluid, choreographed rearrangement
        self.play(
            Transform(self.triangles[0], left_triangle1),   # Top-left to left rect
            Transform(self.triangles[1], right_triangle1),  # Top-right to right rect
            Transform(self.triangles[2], left_triangle2),   # Bottom-right to left rect
            Transform(self.triangles[3], right_triangle2),  # Bottom-left to right rect
            run_time=4,
            rate_func=smooth
        )
        
        # Store the new triangle positions
        self.rearranged_triangles = [left_triangle1, right_triangle1, left_triangle2, right_triangle2]
        
        self.wait(1.5)
    
    def scene_4_second_arrangement(self):
        """[01:16 - 01:45] SCENE 4: THE SECOND ARRANGEMENT"""
        
        triangle_scale = 0.9
        
        # Create the a² square (smaller, from shorter legs)
        square_a = Square(side_length=self.a * triangle_scale)
        square_a.set_fill(self.a_square_color, opacity=0.9)
        square_a.set_stroke(self.a_square_color, width=3)
        square_a.move_to(RIGHT * 2.5 + UP * (self.b * triangle_scale / 2))
        
        # Create the b² square (larger, from longer legs)
        square_b = Square(side_length=self.b * triangle_scale)
        square_b.set_fill(self.b_square_color, opacity=0.9)
        square_b.set_stroke(self.b_square_color, width=3)
        square_b.move_to(LEFT * 2.5 + RIGHT * (self.a * triangle_scale / 2))
        
        # Highlight the a² square first
        self.play(FadeIn(square_a), run_time=1.5)
        
        # Add a labels
        a_labels = VGroup()
        for i, direction in enumerate([DOWN, RIGHT, UP, LEFT]):
            label = MathTex("a", font_size=self.label_font_size-4, color=self.text_color)
            label.next_to(square_a, direction, buff=0.1)
            a_labels.add(label)
        
        self.play(Write(a_labels), run_time=1)
        
        # Add "Area = a²" text
        area_a_text = MathTex("\\text{Area} = a^2", font_size=28, color=self.text_color)
        area_a_text.move_to(square_a.get_center())
        
        self.play(Write(area_a_text), run_time=1)
        
        self.wait(1)
        
        # Highlight the b² square
        self.play(FadeIn(square_b), run_time=1.5)
        
        # Add b labels
        b_labels = VGroup()
        for i, direction in enumerate([DOWN, RIGHT, UP, LEFT]):
            label = MathTex("b", font_size=self.label_font_size-4, color=self.text_color)
            label.next_to(square_b, direction, buff=0.1)
            b_labels.add(label)
        
        self.play(Write(b_labels), run_time=1)
        
        # Add "Area = b²" text
        area_b_text = MathTex("\\text{Area} = b^2", font_size=28, color=self.text_color)
        area_b_text.move_to(square_b.get_center())
        
        self.play(Write(area_b_text), run_time=1)
        
        # Store objects for the conclusion
        self.square_a = square_a
        self.square_b = square_b
        self.a_labels = a_labels
        self.b_labels = b_labels
        self.area_a_text = area_a_text
        self.area_b_text = area_b_text
        
        self.wait(2)
    
    def scene_5_conclusion(self):
        """[01:46 - 02:30] SCENE 5: THE CONCLUSION"""
        
        # Create split-screen effect by scaling and repositioning
        
        # Recreate the first arrangement (left side)
        left_group = VGroup()
        
        # Recreate central c² square for left side
        central_square_left = Square(side_length=1.5)
        central_square_left.set_fill(self.c_square_color, opacity=0.9)
        central_square_left.set_stroke(self.c_square_color, width=2)
        central_square_left.rotate(PI/4)
        central_square_left.move_to(LEFT * 3)
        
        c_squared_left = MathTex("c^2", font_size=36, color=WHITE)
        c_squared_left.move_to(central_square_left.get_center())
        
        left_group.add(central_square_left, c_squared_left)
        
        # Right side keeps the current arrangement
        right_group = VGroup(
            self.square_a, self.square_b,
            self.area_a_text, self.area_b_text
        )
        
        # Clear current scene and set up split screen
        self.play(
            *[FadeOut(obj) for obj in self.triangles],
            *[FadeOut(obj) for obj in [self.a_labels, self.b_labels]],
            run_time=1
        )
        
        # Move squares to right side
        self.play(
            self.square_a.animate.scale(0.7).move_to(RIGHT * 2 + UP * 1),
            self.square_b.animate.scale(0.7).move_to(RIGHT * 2 + DOWN * 1),
            self.area_a_text.animate.scale(0.8).move_to(RIGHT * 2 + UP * 1),
            self.area_b_text.animate.scale(0.8).move_to(RIGHT * 2 + DOWN * 1),
            run_time=2
        )
        
        # Show left side arrangement
        self.play(
            FadeIn(left_group),
            run_time=1.5
        )
        
        self.wait(1)
        
        # Animate the equation formation in the center
        # Extract the terms and move them to center
        
        c_squared_term = MathTex("c^2", font_size=self.equation_font_size, color=self.c_square_color)
        c_squared_term.move_to(ORIGIN + LEFT * 2)
        
        equals_sign = MathTex("=", font_size=self.equation_font_size, color=self.text_color)
        equals_sign.move_to(ORIGIN + LEFT * 0.8)
        
        a_squared_term = MathTex("a^2", font_size=self.equation_font_size, color=self.a_square_color)
        a_squared_term.move_to(ORIGIN + RIGHT * 0.2)
        
        plus_sign = MathTex("+", font_size=self.equation_font_size, color=self.text_color)
        plus_sign.move_to(ORIGIN + RIGHT * 1)
        
        b_squared_term = MathTex("b^2", font_size=self.equation_font_size, color=self.b_square_color)
        b_squared_term.move_to(ORIGIN + RIGHT * 1.8)
        
        # Animate the equation building up
        self.play(
            Transform(c_squared_left.copy(), c_squared_term),
            run_time=1.5
        )
        
        self.play(Write(equals_sign), run_time=0.8)
        
        self.play(
            Transform(self.area_a_text.copy(), a_squared_term),
            run_time=1.5
        )
        
        self.play(Write(plus_sign), run_time=0.8)
        
        self.play(
            Transform(self.area_b_text.copy(), b_squared_term),
            run_time=1.5
        )
        
        # Clear everything except the final equation
        final_equation = VGroup(c_squared_term, equals_sign, a_squared_term, plus_sign, b_squared_term)
        
        self.play(
            *[FadeOut(obj) for obj in [left_group, self.square_a, self.square_b, self.area_a_text, self.area_b_text]],
            final_equation.animate.move_to(ORIGIN),
            run_time=2
        )
        
        # Final presentation
        self.wait(3)
        
        # Fade to elegant conclusion
        self.play(FadeOut(final_equation), run_time=2)
        
        self.wait(1)

# Configuration for Google Colab
if __name__ == "__main__":
    # Optimized settings for Google Colab
    config.media_width = "75%"
    config.verbosity = "WARNING"
    config.frame_size = (1920, 1080)
    config.frame_rate = 30
    config.background_color = "#f8f9fa"
    
    # Create and render the scene
    scene = PythagoreanVisualProof()
    scene.render()

# Google Colab Setup Instructions:
"""
To run this world-class animation in Google Colab:

1. Install Manim:
!pip install manim

2. Install system dependencies:
!apt update &> /dev/null
!apt install libcairo2-dev ffmpeg texlive texlive-latex-extra texlive-fonts-extra texlive-latex-recommended texlive-science tipa libpango1.0-dev &> /dev/null

3. Copy this script to a file:
%%writefile pythagorean_visual_proof.py
[PASTE THE ENTIRE SCRIPT HERE]

4. Run the animation:
!manim pythagorean_visual_proof.py PythagoreanVisualProof

5. Display the result:
from IPython.display import Video
Video("/content/media/videos/pythagorean_visual_proof/1080p30/PythagoreanVisualProof.mp4", width=800)
"""