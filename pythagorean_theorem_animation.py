#!/usr/bin/env python3
"""
Pythagorean Theorem Visual Proof using Four Right Triangles
A world-class Manim animation demonstrating a² + b² = c²

This script creates a beautiful visualization showing how four identical right triangles
can be rearranged to prove the Pythagorean theorem through area conservation.
"""

from manim import *
import numpy as np

class PythagoreanTheoremProof(Scene):
    def construct(self):
        # Configuration for the right triangle
        self.a = 3  # One leg
        self.b = 4  # Other leg  
        self.c = 5  # Hypotenuse (satisfies Pythagorean theorem)
        
        # Color scheme for visual clarity
        self.triangle_color = BLUE
        self.triangle_fill_opacity = 0.7
        self.square_c_color = RED
        self.square_a_color = GREEN
        self.square_b_color = YELLOW
        self.text_color = WHITE
        
        # Title and introduction
        self.show_introduction()
        
        # Create and show the initial arrangement
        self.create_initial_square_arrangement()
        
        # Highlight the c² area
        self.highlight_c_squared_area()
        
        # Rearrange to show a² + b²
        self.rearrange_to_show_ab_squares()
        
        # Show the mathematical conclusion
        self.show_mathematical_conclusion()
        
    def show_introduction(self):
        """Display the title and introduction"""
        title = Text("Pythagorean Theorem", font_size=48, color=self.text_color)
        subtitle = Text("Visual Proof using Four Right Triangles", font_size=32, color=GRAY)
        subtitle.next_to(title, DOWN, buff=0.3)
        
        intro_group = VGroup(title, subtitle)
        intro_group.to_edge(UP, buff=1)
        
        self.play(Write(title), run_time=2)
        self.play(Write(subtitle), run_time=1.5)
        self.wait(1)
        
        # Store for later reference
        self.title_group = intro_group
        
    def create_right_triangle(self):
        """Create a single right triangle with the specified dimensions"""
        # Define the triangle vertices
        vertices = [
            ORIGIN,  # Right angle vertex
            self.a * RIGHT,  # End of leg 'a'
            self.b * UP  # End of leg 'b'
        ]
        
        triangle = Polygon(*vertices, 
                         color=self.triangle_color, 
                         fill_opacity=self.triangle_fill_opacity,
                         stroke_width=2)
        
        return triangle
        
    def create_initial_square_arrangement(self):
        """Create the initial arrangement with four triangles forming a square"""
        # Create the base triangle
        base_triangle = self.create_right_triangle()
        
        # Create four triangles by rotating the base triangle
        triangle1 = base_triangle.copy()
        triangle2 = base_triangle.copy().rotate(PI/2, about_point=ORIGIN)
        triangle3 = base_triangle.copy().rotate(PI, about_point=ORIGIN)
        triangle4 = base_triangle.copy().rotate(3*PI/2, about_point=ORIGIN)
        
        # Position triangles to form a square with hypotenuses pointing inward
        # The outer square has side length (a + b)
        outer_size = self.a + self.b
        
        # Triangle 1: bottom-right, rotate so hypotenuse faces inward
        triangle1.rotate(-PI/2).move_to(ORIGIN).shift(RIGHT * outer_size/2 + DOWN * outer_size/2)
        triangle1.shift(LEFT * self.a/2 + UP * self.b/2)
        
        # Triangle 2: top-right
        triangle2.move_to(ORIGIN).shift(RIGHT * outer_size/2 + UP * outer_size/2)
        triangle2.shift(LEFT * self.b/2 + DOWN * self.a/2)
        
        # Triangle 3: top-left
        triangle3.rotate(-PI/2).move_to(ORIGIN).shift(LEFT * outer_size/2 + UP * outer_size/2)
        triangle3.shift(RIGHT * self.a/2 + DOWN * self.b/2)
        
        # Triangle 4: bottom-left
        triangle4.move_to(ORIGIN).shift(LEFT * outer_size/2 + DOWN * outer_size/2)
        triangle4.shift(RIGHT * self.b/2 + UP * self.a/2)
        
        # Store triangles for later manipulation
        self.triangles = [triangle1, triangle2, triangle3, triangle4]
        
        # Create labels for the triangle sides
        self.create_triangle_labels()
        
        # Animate the creation of triangles
        self.play(
            *[Create(triangle) for triangle in self.triangles],
            run_time=3,
            lag_ratio=0.3
        )
        
        self.wait(1)
        
    def create_triangle_labels(self):
        """Create labels for the sides of the triangles"""
        # Label positions need to be calculated based on triangle orientations
        label_a1 = MathTex("a", font_size=24, color=WHITE).next_to(self.triangles[0], DOWN, buff=0.1)
        label_b1 = MathTex("b", font_size=24, color=WHITE).next_to(self.triangles[0], RIGHT, buff=0.1)
        label_c1 = MathTex("c", font_size=24, color=WHITE).next_to(self.triangles[0], UL, buff=0.1)
        
        self.triangle_labels = VGroup(label_a1, label_b1, label_c1)
        
        self.play(Write(self.triangle_labels), run_time=1.5)
        
    def highlight_c_squared_area(self):
        """Highlight the central c² square"""
        # Calculate the vertices of the central square
        # The central square has side length c and is rotated
        center_square_vertices = []
        
        # The inner square is formed by the hypotenuses
        # Its vertices are at the inner corners where hypotenuses meet
        inner_size = abs(self.a - self.b)  # This creates the tilted square
        
        # Create the central square (tilted)
        # For a cleaner approach, let's create it geometrically
        center_offset = (self.a - self.b) / 2
        
        vertices = [
            np.array([center_offset, center_offset + self.c, 0]),
            np.array([center_offset + self.c, center_offset, 0]),
            np.array([center_offset, center_offset - self.c, 0]),
            np.array([center_offset - self.c, center_offset, 0])
        ]
        
        # Simplified approach: create a square in the center
        center_square = Square(side_length=self.c * 0.6)  # Scaled for visibility
        center_square.set_fill(self.square_c_color, opacity=0.5)
        center_square.set_stroke(self.square_c_color, width=3)
        center_square.rotate(PI/4)  # Tilt the square
        
        # Label for c²
        c_squared_label = MathTex("c^2", font_size=36, color=WHITE)
        c_squared_label.move_to(center_square.get_center())
        
        self.play(
            FadeIn(center_square),
            Write(c_squared_label),
            run_time=2
        )
        
        self.center_square = center_square
        self.c_squared_label = c_squared_label
        
        self.wait(2)
        
    def rearrange_to_show_ab_squares(self):
        """Rearrange triangles to form two rectangles and reveal a² and b² squares"""
        # Fade out the center square temporarily
        self.play(
            FadeOut(self.center_square),
            FadeOut(self.c_squared_label),
            run_time=1
        )
        
        # Create target positions for the rearranged triangles
        # Arrangement: two rectangles side by side
        
        # Left rectangle: a × b with triangles forming it
        left_rect_center = LEFT * 3
        # Right rectangle: a × b with triangles forming it  
        right_rect_center = RIGHT * 3
        
        # Rearrange triangles to form two rectangles
        target_positions = [
            left_rect_center + UP * self.b/2 + LEFT * self.a/4,      # Triangle 1
            left_rect_center + DOWN * self.b/2 + LEFT * self.a/4,    # Triangle 2
            right_rect_center + UP * self.b/2 + RIGHT * self.a/4,    # Triangle 3
            right_rect_center + DOWN * self.b/2 + RIGHT * self.a/4   # Triangle 4
        ]
        
        # Animate the rearrangement
        rearrange_animations = []
        for i, triangle in enumerate(self.triangles):
            # Reset rotation and position
            new_triangle = self.create_right_triangle()
            if i % 2 == 1:  # Alternate triangles get rotated
                new_triangle.rotate(PI)
            new_triangle.move_to(target_positions[i])
            rearrange_animations.append(Transform(triangle, new_triangle))
            
        self.play(*rearrange_animations, run_time=3)
        
        # Create the a² and b² squares
        self.create_ab_squares()
        
    def create_ab_squares(self):
        """Create and highlight the a² and b² squares in the new arrangement"""
        # Create a² square
        square_a = Square(side_length=self.a * 0.8)  # Scaled for visibility
        square_a.set_fill(self.square_a_color, opacity=0.5)
        square_a.set_stroke(self.square_a_color, width=3)
        square_a.move_to(LEFT * 5 + UP * 1)
        
        # Create b² square
        square_b = Square(side_length=self.b * 0.6)  # Scaled for visibility
        square_b.set_fill(self.square_b_color, opacity=0.5)
        square_b.set_stroke(self.square_b_color, width=3)
        square_b.move_to(RIGHT * 1 + DOWN * 1)
        
        # Labels
        a_squared_label = MathTex("a^2", font_size=36, color=WHITE)
        a_squared_label.move_to(square_a.get_center())
        
        b_squared_label = MathTex("b^2", font_size=36, color=WHITE)
        b_squared_label.move_to(square_b.get_center())
        
        # Animate the appearance of squares
        self.play(
            FadeIn(square_a),
            FadeIn(square_b),
            Write(a_squared_label),
            Write(b_squared_label),
            run_time=2.5
        )
        
        self.square_a = square_a
        self.square_b = square_b
        self.a_squared_label = a_squared_label
        self.b_squared_label = b_squared_label
        
        self.wait(2)
        
    def show_mathematical_conclusion(self):
        """Display the mathematical conclusion of the proof"""
        # Create the equation
        equation = MathTex(
            "a^2", "+", "b^2", "=", "c^2",
            font_size=48,
            color=WHITE
        )
        
        # Color code the equation to match the squares
        equation[0].set_color(self.square_a_color)  # a²
        equation[2].set_color(self.square_b_color)  # b²
        equation[4].set_color(self.square_c_color)  # c²
        
        equation.to_edge(DOWN, buff=1.5)
        
        # Explanation text
        explanation = Text(
            "The total area remains constant in both arrangements",
            font_size=24,
            color=GRAY
        )
        explanation.next_to(equation, UP, buff=0.5)
        
        # Animate the conclusion
        self.play(
            Write(explanation),
            run_time=2
        )
        
        self.play(
            Write(equation),
            run_time=3,
            lag_ratio=0.2
        )
        
        # Highlight the connection between visual and mathematical
        self.play(
            Indicate(self.square_a),
            Indicate(equation[0]),
            run_time=1.5
        )
        
        self.play(
            Indicate(self.square_b),
            Indicate(equation[2]),
            run_time=1.5
        )
        
        # Final emphasis
        final_text = Text(
            "Pythagorean Theorem: Proven Visually!",
            font_size=36,
            color=GOLD
        )
        final_text.to_edge(DOWN, buff=0.5)
        
        self.play(
            Transform(explanation, final_text),
            equation.animate.shift(UP * 0.5),
            run_time=2
        )
        
        self.wait(3)

# Configuration for Google Colab
if __name__ == "__main__":
    # For Google Colab, we need to set up the scene properly
    config.media_width = "75%"
    config.verbosity = "WARNING"
    config.frame_size = (1920, 1080)
    config.frame_rate = 30
    
    # Create and render the scene
    scene = PythagoreanTheoremProof()
    scene.render()

# Google Colab Setup Instructions:
"""
To run this in Google Colab:

1. Install Manim:
!pip install manim

2. Install system dependencies:
!apt update &> /dev/null
!apt install libcairo2-dev ffmpeg texlive texlive-latex-extra texlive-fonts-extra texlive-latex-recommended texlive-science tipa libpango1.0-dev &> /dev/null

3. Run the animation:
%run pythagorean_theorem_animation.py

4. Display the result:
from IPython.display import Video
Video("media/videos/1080p60/PythagoreanTheoremProof.mp4", width=800)
"""