"""
Manim-Compatible Pythagorean Theorem Scene
==========================================

This version is designed to work with the 3Blue1Brown manim setup when available,
but gracefully falls back to matplotlib when manim is not present.

Features:
- Animated geometric proof
- Step-by-step construction
- Smooth transitions
- Educational narration points
- Modern visual design
"""

try:
    from manim_imports_ext import *
    MANIM_AVAILABLE = True
    print("Manim available - using advanced animations")
except ImportError:
    MANIM_AVAILABLE = False
    print("Manim not available - using matplotlib fallback")
    import matplotlib.pyplot as plt
    import matplotlib.patches as patches
    import numpy as np
    from matplotlib.animation import FuncAnimation
    import math

# Enhanced color scheme for better visual appeal
THEOREM_COLORS = {
    'triangle_fill': '#FF6B6B',
    'triangle_stroke': '#E74C3C', 
    'square_a': '#4ECDC4',
    'square_b': '#45B7D1', 
    'square_c': '#96CEB4',
    'background': '#2C3E50',
    'text_primary': '#ECF0F1',
    'text_accent': '#F39C12',
    'highlight': '#E74C3C',
    'proof_bg': '#34495E'
}

if MANIM_AVAILABLE:
    class PythagoreanTheoremScene(Scene):
        """
        Animated Pythagorean theorem proof using manim
        """
        
        def construct(self):
            self.camera.background_color = THEOREM_COLORS['background']
            
            # Title
            title = Text("Pythagorean Theorem", font_size=48, color=THEOREM_COLORS['text_accent'])
            subtitle = MathTex("a^2 + b^2 = c^2", font_size=36, color=THEOREM_COLORS['highlight'])
            title_group = VGroup(title, subtitle).arrange(DOWN)
            
            self.play(Write(title))
            self.wait(0.5)
            self.play(Write(subtitle))
            self.wait(1)
            self.play(title_group.animate.to_edge(UP))
            
            # Create the main proof
            self.show_triangle_construction()
            self.show_square_construction() 
            self.show_proof_rearrangement()
            self.show_final_equation()
            
        def show_triangle_construction(self):
            """Animate the construction of the right triangle"""
            # Create triangle vertices
            A = np.array([-2, -1, 0])
            B = np.array([1, -1, 0]) 
            C = np.array([-2, 2, 0])
            
            # Create triangle
            triangle = Polygon(A, B, C, 
                             fill_color=THEOREM_COLORS['triangle_fill'],
                             fill_opacity=0.7,
                             stroke_color=THEOREM_COLORS['triangle_stroke'],
                             stroke_width=3)
            
            # Labels for sides
            a_label = MathTex("a", color=THEOREM_COLORS['text_primary']).scale(1.2)
            b_label = MathTex("b", color=THEOREM_COLORS['text_primary']).scale(1.2)  
            c_label = MathTex("c", color=THEOREM_COLORS['text_primary']).scale(1.2)
            
            # Position labels
            a_label.next_to(Line(A, B), DOWN)
            b_label.next_to(Line(A, C), LEFT)
            c_label.next_to(Line(B, C), UR)
            
            # Right angle indicator
            right_angle = RightAngle(Line(A, B), Line(A, C), length=0.3, color=WHITE)
            
            # Animate construction
            self.play(Create(triangle), run_time=2)
            self.play(Create(right_angle))
            self.play(Write(a_label), Write(b_label), Write(c_label))
            self.wait(1)
            
            # Store for later use
            self.triangle = triangle
            self.triangle_labels = VGroup(a_label, b_label, c_label)
            self.right_angle = right_angle
            self.A, self.B, self.C = A, B, C
            
        def show_square_construction(self):
            """Animate the construction of squares on each side"""
            A, B, C = self.A, self.B, self.C
            
            # Calculate side lengths
            a_len = np.linalg.norm(B - A)
            b_len = np.linalg.norm(C - A) 
            c_len = np.linalg.norm(C - B)
            
            # Create squares
            # Square on side a
            square_a = Rectangle(width=a_len, height=a_len,
                               fill_color=THEOREM_COLORS['square_a'],
                               fill_opacity=0.6,
                               stroke_color=WHITE,
                               stroke_width=2)
            square_a.next_to(Line(A, B), DOWN, buff=0)
            
            # Square on side b  
            square_b = Rectangle(width=b_len, height=b_len,
                               fill_color=THEOREM_COLORS['square_b'],
                               fill_opacity=0.6,
                               stroke_color=WHITE,
                               stroke_width=2)
            square_b.next_to(Line(A, C), LEFT, buff=0)
            
            # Square on side c
            square_c = Rectangle(width=c_len, height=c_len,
                               fill_color=THEOREM_COLORS['square_c'],
                               fill_opacity=0.6,
                               stroke_color=WHITE,
                               stroke_width=2)
            # Position square c along hypotenuse
            square_c.move_to(Line(B, C).get_center())
            square_c.rotate(Line(B, C).get_angle())
            
            # Area labels
            area_a = MathTex("a^2", color=THEOREM_COLORS['text_primary']).scale(0.8)
            area_b = MathTex("b^2", color=THEOREM_COLORS['text_primary']).scale(0.8)
            area_c = MathTex("c^2", color=THEOREM_COLORS['text_primary']).scale(0.8)
            
            area_a.move_to(square_a.get_center())
            area_b.move_to(square_b.get_center()) 
            area_c.move_to(square_c.get_center())
            
            # Animate square construction
            self.play(Create(square_a), Write(area_a))
            self.wait(0.5)
            self.play(Create(square_b), Write(area_b))
            self.wait(0.5)
            self.play(Create(square_c), Write(area_c))
            self.wait(1)
            
            # Store squares
            self.squares = VGroup(square_a, square_b, square_c)
            self.area_labels = VGroup(area_a, area_b, area_c)
            
        def show_proof_rearrangement(self):
            """Show the rearrangement proof"""
            # Move everything to make room for proof
            everything = VGroup(self.triangle, self.triangle_labels, self.right_angle, 
                              self.squares, self.area_labels)
            self.play(everything.animate.scale(0.6).to_edge(LEFT))
            
            # Create the proof diagram on the right
            proof_title = Text("Proof by Rearrangement", font_size=24, 
                             color=THEOREM_COLORS['text_accent'])
            proof_title.to_edge(RIGHT).shift(UP * 2.5)
            
            self.play(Write(proof_title))
            
            # Create large square for proof
            side_length = 3
            large_square = Square(side_length=side_length,
                                color=WHITE,
                                stroke_width=3)
            large_square.next_to(proof_title, DOWN, buff=0.5)
            
            # Create four triangles inside
            triangle_coords = [
                [[-1.5, -1.5], [0, -1.5], [-1.5, 0]], # Bottom left
                [[0, -1.5], [1.5, -1.5], [1.5, 0]],   # Bottom right  
                [[1.5, 0], [1.5, 1.5], [0, 1.5]],     # Top right
                [[0, 1.5], [-1.5, 1.5], [-1.5, 0]]    # Top left
            ]
            
            proof_triangles = VGroup()
            for coords in triangle_coords:
                triangle = Polygon(*[np.array([x, y, 0]) for x, y in coords],
                                 fill_color=THEOREM_COLORS['triangle_fill'],
                                 fill_opacity=0.7,
                                 stroke_color=THEOREM_COLORS['triangle_stroke'],
                                 stroke_width=2)
                proof_triangles.add(triangle)
            
            # Inner square (represents c²)
            inner_square = Square(side_length=side_length/2,
                                fill_color=THEOREM_COLORS['square_c'],
                                fill_opacity=0.6,
                                stroke_color=WHITE,
                                stroke_width=2)
            
            # Position everything relative to large square
            proof_group = VGroup(large_square, proof_triangles, inner_square)
            proof_group.move_to(large_square.get_center())
            
            # Animate proof construction
            self.play(Create(large_square))
            self.play(Create(proof_triangles), lag_ratio=0.2)
            self.play(Create(inner_square))
            
            # Add equation steps
            eq1 = MathTex("(a + b)^2 = 4 \\cdot \\frac{1}{2}ab + c^2",
                         color=THEOREM_COLORS['text_primary'])
            eq2 = MathTex("a^2 + 2ab + b^2 = 2ab + c^2",
                         color=THEOREM_COLORS['text_primary'])
            eq3 = MathTex("a^2 + b^2 = c^2", 
                         color=THEOREM_COLORS['highlight']).scale(1.2)
            
            equations = VGroup(eq1, eq2, eq3).arrange(DOWN, buff=0.3)
            equations.next_to(proof_group, DOWN, buff=0.5)
            
            self.play(Write(eq1))
            self.wait(1)
            self.play(Write(eq2))
            self.wait(1)
            self.play(Write(eq3))
            self.wait(2)
            
        def show_final_equation(self):
            """Highlight the final theorem"""
            # Create final emphasized equation
            final_eq = MathTex("a^2 + b^2 = c^2", font_size=72,
                             color=THEOREM_COLORS['highlight'])
            final_eq.move_to(ORIGIN)
            
            # Background box
            bg_rect = Rectangle(width=final_eq.width + 1, 
                              height=final_eq.height + 0.5,
                              fill_color=THEOREM_COLORS['proof_bg'],
                              fill_opacity=0.8,
                              stroke_color=THEOREM_COLORS['highlight'],
                              stroke_width=3)
            bg_rect.move_to(final_eq)
            
            # Fade out everything else and show final result
            self.play(FadeOut(*[mob for mob in self.mobjects]))
            self.play(FadeIn(bg_rect), Write(final_eq))
            self.wait(3)

    class PythagoreanProofMultiple(Scene):
        """
        Multiple proof methods in one scene
        """
        
        def construct(self):
            self.camera.background_color = THEOREM_COLORS['background']
            
            title = Text("Multiple Proofs of the Pythagorean Theorem",
                        font_size=36, color=THEOREM_COLORS['text_accent'])
            title.to_edge(UP)
            self.add(title)
            
            # Show different proof methods
            self.show_geometric_proof()
            self.show_algebraic_proof()
            self.show_similarity_proof()
            
        def show_geometric_proof(self):
            """Geometric rearrangement proof"""
            pass  # Implementation would go here
            
        def show_algebraic_proof(self):
            """Algebraic proof"""
            pass  # Implementation would go here
            
        def show_similarity_proof(self):
            """Similarity-based proof"""
            pass  # Implementation would go here

else:
    # Matplotlib fallback implementation
    class PythagoreanAnimatedDemo:
        """
        Animated demonstration using matplotlib
        """
        
        def __init__(self):
            self.fig, self.ax = plt.subplots(figsize=(12, 8))
            self.fig.patch.set_facecolor(THEOREM_COLORS['background'])
            self.ax.set_facecolor(THEOREM_COLORS['background'])
            self.frame = 0
            
        def animate_construction(self):
            """Create animated construction of the theorem"""
            
            def update_frame(frame):
                self.ax.clear()
                self.ax.set_facecolor(THEOREM_COLORS['background'])
                self.ax.set_aspect('equal')
                self.ax.set_xlim(-6, 8)
                self.ax.set_ylim(-5, 6)
                
                # Progressive construction based on frame
                if frame < 30:
                    self.draw_triangle_progressive(frame / 30)
                elif frame < 60:
                    self.draw_triangle_progressive(1.0)
                    self.draw_squares_progressive((frame - 30) / 30)
                elif frame < 90:
                    self.draw_triangle_progressive(1.0)
                    self.draw_squares_progressive(1.0)
                    self.draw_proof_rearrangement((frame - 60) / 30)
                else:
                    self.draw_complete_scene()
                    
                self.ax.grid(True, alpha=0.2, color=THEOREM_COLORS['text_primary'])
                self.ax.set_title('Animated Pythagorean Theorem Proof', 
                                color=THEOREM_COLORS['text_primary'], fontsize=16, weight='bold')
                
            return update_frame
            
        def draw_triangle_progressive(self, progress):
            """Draw triangle with progressive animation"""
            if progress <= 0:
                return
                
            # Triangle vertices
            vertices = np.array([[0, 0], [3, 0], [0, 4]])
            
            # Draw progressively
            if progress >= 0.33:
                # Base
                self.ax.plot([0, 3], [0, 0], 'white', linewidth=3)
                self.ax.text(1.5, -0.3, 'a = 3', fontsize=14, color=THEOREM_COLORS['text_primary'],
                           ha='center', weight='bold')
                           
            if progress >= 0.66:
                # Height
                self.ax.plot([0, 0], [0, 4], 'white', linewidth=3)
                self.ax.text(-0.3, 2, 'b = 4', fontsize=14, color=THEOREM_COLORS['text_primary'],
                           ha='right', va='center', weight='bold')
                           
            if progress >= 1.0:
                # Hypotenuse
                self.ax.plot([3, 0], [0, 4], 'white', linewidth=3)
                self.ax.text(1.8, 2.3, 'c = 5', fontsize=14, color=THEOREM_COLORS['text_primary'],
                           ha='center', va='center', weight='bold')
                           
                # Fill triangle
                triangle = patches.Polygon(vertices, facecolor=THEOREM_COLORS['triangle_fill'],
                                         alpha=0.7, edgecolor='white', linewidth=2)
                self.ax.add_patch(triangle)
                
        def draw_squares_progressive(self, progress):
            """Draw squares with progressive animation"""
            if progress <= 0:
                return
                
            if progress >= 0.33:
                # Square a
                square_a = patches.Rectangle((0, -3), 3, 3, 
                                           facecolor=THEOREM_COLORS['square_a'],
                                           alpha=0.7, edgecolor='white', linewidth=2)
                self.ax.add_patch(square_a)
                self.ax.text(1.5, -1.5, 'a² = 9', fontsize=12, color=THEOREM_COLORS['text_primary'],
                           ha='center', va='center', weight='bold')
                           
            if progress >= 0.66:
                # Square b
                square_b = patches.Rectangle((-4, 0), 4, 4,
                                           facecolor=THEOREM_COLORS['square_b'],
                                           alpha=0.7, edgecolor='white', linewidth=2)
                self.ax.add_patch(square_b)
                self.ax.text(-2, 2, 'b² = 16', fontsize=12, color=THEOREM_COLORS['text_primary'],
                           ha='center', va='center', weight='bold')
                           
            if progress >= 1.0:
                # Square c
                square_c = patches.Rectangle((4, 0), 5, 5,
                                           facecolor=THEOREM_COLORS['square_c'],
                                           alpha=0.7, edgecolor='white', linewidth=2)
                self.ax.add_patch(square_c)
                self.ax.text(6.5, 2.5, 'c² = 25', fontsize=12, color=THEOREM_COLORS['text_primary'],
                           ha='center', va='center', weight='bold')
                           
        def draw_proof_rearrangement(self, progress):
            """Draw the proof rearrangement"""
            if progress <= 0:
                return
                
            # Show equation building up
            if progress >= 0.5:
                equation = 'a² + b² = 9 + 16 = 25 = c²'
                self.ax.text(1.5, 5, equation, fontsize=16, color=THEOREM_COLORS['highlight'],
                           ha='center', weight='bold', 
                           bbox=dict(boxstyle="round,pad=0.3", facecolor=THEOREM_COLORS['proof_bg']))
                           
        def draw_complete_scene(self):
            """Draw the complete scene"""
            self.draw_triangle_progressive(1.0)
            self.draw_squares_progressive(1.0)
            self.draw_proof_rearrangement(1.0)
            
        def create_animation(self):
            """Create the full animation"""
            anim = FuncAnimation(self.fig, self.animate_construction(), 
                               frames=120, interval=100, repeat=True)
            return anim

def create_pythagorean_scene():
    """Create the appropriate scene based on available libraries"""
    if MANIM_AVAILABLE:
        return PythagoreanTheoremScene()
    else:
        return PythagoreanAnimatedDemo()

if __name__ == "__main__":
    if MANIM_AVAILABLE:
        # This would be run with manimgl command
        print("To run with manim: manimgl pythagorean_theorem_manim.py PythagoreanTheoremScene")
    else:
        # Run matplotlib animation
        demo = PythagoreanAnimatedDemo()
        anim = demo.create_animation()
        
        # Save animation
        print("Creating animated demonstration...")
        try:
            anim.save('/tmp/pythagorean_animation.gif', writer='pillow', fps=10)
            print("Animation saved to /tmp/pythagorean_animation.gif")
        except Exception as e:
            print(f"Could not save animation: {e}")
            
        plt.show()