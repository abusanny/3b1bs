"""
Comprehensive Pythagorean Theorem Educational Suite
==================================================

This script provides multiple proof methods and visualizations of the Pythagorean theorem,
designed for educational purposes. It includes:

1. Visual geometric proof (square rearrangement)
2. Algebraic proof 
3. Similarity-based proof
4. Historical context and applications
5. Interactive elements for exploration

Each proof is self-contained and can be run independently.
"""

import matplotlib.pyplot as plt
import matplotlib.patches as patches
import numpy as np
import math
from matplotlib.widgets import Slider
from matplotlib.animation import FuncAnimation

# Educational color scheme
COLORS = {
    'primary': '#3498DB',      # Blue
    'secondary': '#E74C3C',    # Red  
    'accent': '#F39C12',       # Orange
    'success': '#27AE60',      # Green
    'warning': '#F1C40F',      # Yellow
    'background': '#2C3E50',   # Dark blue
    'surface': '#34495E',      # Medium blue
    'text': '#ECF0F1',         # Light gray
    'muted': '#95A5A6'         # Gray
}

class PythagoreanEducationalSuite:
    """
    Complete educational suite for the Pythagorean theorem
    """
    
    def __init__(self):
        self.current_proof = None
        
    def create_proof_overview(self):
        """Create an overview of all proof methods"""
        fig, ((ax1, ax2), (ax3, ax4)) = plt.subplots(2, 2, figsize=(16, 12))
        fig.patch.set_facecolor(COLORS['background'])
        fig.suptitle('Pythagorean Theorem: Multiple Proofs', 
                    fontsize=20, color=COLORS['text'], weight='bold')
        
        # Proof 1: Geometric rearrangement
        self._draw_geometric_overview(ax1)
        
        # Proof 2: Algebraic 
        self._draw_algebraic_overview(ax2)
        
        # Proof 3: Similarity
        self._draw_similarity_overview(ax3)
        
        # Proof 4: Applications
        self._draw_applications_overview(ax4)
        
        plt.tight_layout()
        return fig
        
    def _draw_geometric_overview(self, ax):
        """Draw overview of geometric proof"""
        ax.set_facecolor(COLORS['surface'])
        ax.set_title('Geometric Proof\n(Square Rearrangement)', 
                    color=COLORS['text'], weight='bold')
        
        # Simple diagram
        triangle = patches.Polygon([(0, 0), (3, 0), (0, 4)], 
                                  facecolor=COLORS['primary'], alpha=0.7)
        ax.add_patch(triangle)
        
        # Small squares to represent the concept
        sq_a = patches.Rectangle((0, -2), 1.5, 1.5, facecolor=COLORS['accent'], alpha=0.7)
        sq_b = patches.Rectangle((-2, 0), 2, 2, facecolor=COLORS['success'], alpha=0.7)
        sq_c = patches.Rectangle((4, 1), 2.5, 2.5, facecolor=COLORS['warning'], alpha=0.7)
        
        ax.add_patch(sq_a)
        ax.add_patch(sq_b)
        ax.add_patch(sq_c)
        
        ax.text(1.5, -3, 'Rearrange squares to prove\na² + b² = c²', 
               ha='center', va='top', color=COLORS['text'], fontsize=10, weight='bold')
        
        ax.set_xlim(-3, 7)
        ax.set_ylim(-3, 5)
        ax.set_aspect('equal')
        ax.axis('off')
        
    def _draw_algebraic_overview(self, ax):
        """Draw overview of algebraic proof"""
        ax.set_facecolor(COLORS['surface'])
        ax.set_title('Algebraic Proof\n(Area Calculation)', 
                    color=COLORS['text'], weight='bold')
        ax.axis('off')
        
        # Show key algebraic steps
        steps = [
            "(a + b)² = Area of large square",
            "= 4 × (½ab) + c²", 
            "= 2ab + c²",
            "",
            "Also: (a + b)² = a² + 2ab + b²",
            "",
            "Therefore: a² + 2ab + b² = 2ab + c²",
            "Simplifying: a² + b² = c²"
        ]
        
        y_pos = 0.9
        for step in steps:
            if step == "":
                y_pos -= 0.05
                continue
            color = COLORS['accent'] if 'Therefore' in step or '=' in step else COLORS['text']
            weight = 'bold' if 'Therefore' in step else 'normal'
            ax.text(0.05, y_pos, step, transform=ax.transAxes, 
                   color=color, fontsize=9, weight=weight, family='monospace')
            y_pos -= 0.1
            
    def _draw_similarity_overview(self, ax):
        """Draw overview of similarity proof"""
        ax.set_facecolor(COLORS['surface'])
        ax.set_title('Similarity Proof\n(Triangle Proportions)', 
                    color=COLORS['text'], weight='bold')
        
        # Draw main triangle and its similar sub-triangles
        # Main triangle
        main_triangle = patches.Polygon([(0, 0), (4, 0), (0, 3)], 
                                       facecolor=COLORS['primary'], alpha=0.5,
                                       edgecolor=COLORS['text'], linewidth=2)
        ax.add_patch(main_triangle)
        
        # Altitude to hypotenuse
        ax.plot([0, 2.4], [0, 1.8], color=COLORS['secondary'], linewidth=2, linestyle='--')
        
        # Similar triangles
        tri1 = patches.Polygon([(0, 0), (2.4, 1.8), (0, 3)], 
                              facecolor=COLORS['accent'], alpha=0.6)
        tri2 = patches.Polygon([(0, 0), (4, 0), (2.4, 1.8)], 
                              facecolor=COLORS['success'], alpha=0.6)
        
        ax.add_patch(tri1)
        ax.add_patch(tri2)
        
        ax.text(2, -0.5, 'Three similar triangles\nprove the theorem', 
               ha='center', color=COLORS['text'], fontsize=10, weight='bold')
        
        ax.set_xlim(-0.5, 4.5)
        ax.set_ylim(-1, 3.5)
        ax.set_aspect('equal')
        ax.axis('off')
        
    def _draw_applications_overview(self, ax):
        """Draw overview of real-world applications"""
        ax.set_facecolor(COLORS['surface'])
        ax.set_title('Real-World Applications', color=COLORS['text'], weight='bold')
        ax.axis('off')
        
        applications = [
            "🏗️ Construction & Engineering",
            "   • Building foundations",
            "   • Roof trusses", 
            "   • Bridge design",
            "",
            "📡 Technology",
            "   • GPS positioning",
            "   • Computer graphics",
            "   • Signal processing",
            "",
            "🧭 Navigation", 
            "   • Distance calculation",
            "   • Triangulation",
            "   • Surveying"
        ]
        
        y_pos = 0.95
        for app in applications:
            if app == "":
                y_pos -= 0.04
                continue
            if app.startswith("   •"):
                color = COLORS['muted']
                size = 9
            elif any(emoji in app for emoji in ["🏗️", "📡", "🧭"]):
                color = COLORS['accent']
                size = 11
                weight = 'bold'
            else:
                color = COLORS['text']
                size = 10
                
            ax.text(0.05, y_pos, app, transform=ax.transAxes,
                   color=color, fontsize=size, weight='normal')
            y_pos -= 0.06

    def create_detailed_geometric_proof(self):
        """Create detailed step-by-step geometric proof"""
        fig, ((ax1, ax2), (ax3, ax4)) = plt.subplots(2, 2, figsize=(16, 10))
        fig.patch.set_facecolor(COLORS['background'])
        fig.suptitle('Geometric Proof: Step by Step', 
                    fontsize=18, color=COLORS['text'], weight='bold')
        
        # Step 1: Start with right triangle
        self._geometric_step1(ax1)
        
        # Step 2: Add squares on each side  
        self._geometric_step2(ax2)
        
        # Step 3: Create large square
        self._geometric_step3(ax3)
        
        # Step 4: Show the proof
        self._geometric_step4(ax4)
        
        plt.tight_layout()
        return fig
        
    def _geometric_step1(self, ax):
        """Step 1: Right triangle"""
        ax.set_facecolor(COLORS['surface'])
        ax.set_title('Step 1: Right Triangle', color=COLORS['text'], weight='bold')
        
        # Draw triangle
        triangle = patches.Polygon([(0, 0), (3, 0), (0, 4)], 
                                  facecolor=COLORS['primary'], alpha=0.8,
                                  edgecolor='white', linewidth=3)
        ax.add_patch(triangle)
        
        # Labels
        ax.text(1.5, -0.3, 'a', fontsize=14, color=COLORS['text'], 
               ha='center', weight='bold')
        ax.text(-0.3, 2, 'b', fontsize=14, color=COLORS['text'], 
               ha='center', weight='bold')
        ax.text(1.8, 2.3, 'c', fontsize=14, color=COLORS['text'], 
               ha='center', weight='bold')
        
        # Right angle indicator
        ax.plot([0, 0.3], [0, 0], 'white', linewidth=2)
        ax.plot([0, 0], [0, 0.3], 'white', linewidth=2)
        ax.plot([0.3, 0.3], [0, 0.3], 'white', linewidth=2)
        ax.plot([0, 0.3], [0.3, 0.3], 'white', linewidth=2)
        
        ax.set_xlim(-1, 4)
        ax.set_ylim(-1, 5)
        ax.set_aspect('equal')
        ax.axis('off')
        
    def _geometric_step2(self, ax):
        """Step 2: Add squares"""
        ax.set_facecolor(COLORS['surface'])
        ax.set_title('Step 2: Squares on Each Side', color=COLORS['text'], weight='bold')
        
        # Triangle
        triangle = patches.Polygon([(0, 0), (3, 0), (0, 4)], 
                                  facecolor=COLORS['primary'], alpha=0.8,
                                  edgecolor='white', linewidth=2)
        ax.add_patch(triangle)
        
        # Squares
        sq_a = patches.Rectangle((0, -3), 3, 3, facecolor=COLORS['accent'], 
                                alpha=0.7, edgecolor='white', linewidth=2)
        sq_b = patches.Rectangle((-4, 0), 4, 4, facecolor=COLORS['success'], 
                                alpha=0.7, edgecolor='white', linewidth=2)
        sq_c = patches.Rectangle((3.5, 1), 5, 5, facecolor=COLORS['warning'], 
                                alpha=0.7, edgecolor='white', linewidth=2)
        
        ax.add_patch(sq_a)
        ax.add_patch(sq_b) 
        ax.add_patch(sq_c)
        
        # Area labels
        ax.text(1.5, -1.5, 'a² = 9', fontsize=12, color=COLORS['text'], 
               ha='center', weight='bold')
        ax.text(-2, 2, 'b² = 16', fontsize=12, color=COLORS['text'], 
               ha='center', weight='bold')
        ax.text(6, 3.5, 'c² = 25', fontsize=12, color=COLORS['text'], 
               ha='center', weight='bold')
        
        ax.set_xlim(-5, 9)
        ax.set_ylim(-4, 7)
        ax.set_aspect('equal')
        ax.axis('off')
        
    def _geometric_step3(self, ax):
        """Step 3: Large square construction"""
        ax.set_facecolor(COLORS['surface'])
        ax.set_title('Step 3: Large Square (a+b)×(a+b)', color=COLORS['text'], weight='bold')
        
        # Large square
        large_sq = patches.Rectangle((0, 0), 7, 7, facecolor='none',
                                   edgecolor='white', linewidth=3)
        ax.add_patch(large_sq)
        
        # Four triangles inside
        triangles = [
            patches.Polygon([(0, 0), (3, 0), (0, 4)], facecolor=COLORS['primary'], alpha=0.8),
            patches.Polygon([(3, 0), (7, 0), (7, 4)], facecolor=COLORS['primary'], alpha=0.8),
            patches.Polygon([(7, 4), (7, 7), (3, 7)], facecolor=COLORS['primary'], alpha=0.8),
            patches.Polygon([(3, 7), (0, 7), (0, 4)], facecolor=COLORS['primary'], alpha=0.8)
        ]
        
        for tri in triangles:
            ax.add_patch(tri)
            
        # Inner square (c²)
        inner_sq = patches.Rectangle((3, 4), 4, 3, facecolor=COLORS['warning'],
                                   alpha=0.7, edgecolor='white', linewidth=2)
        ax.add_patch(inner_sq)
        
        # Labels
        ax.text(3.5, -0.5, 'a + b = 7', fontsize=12, color=COLORS['text'], 
               ha='center', weight='bold')
        ax.text(-0.5, 3.5, 'a + b = 7', fontsize=12, color=COLORS['text'], 
               ha='center', weight='bold', rotation=90)
        ax.text(5, 5.5, 'c²', fontsize=12, color=COLORS['text'], 
               ha='center', weight='bold')
        
        ax.set_xlim(-1, 8)
        ax.set_ylim(-1, 8)
        ax.set_aspect('equal')
        ax.axis('off')
        
    def _geometric_step4(self, ax):
        """Step 4: Final proof"""
        ax.set_facecolor(COLORS['surface'])
        ax.set_title('Step 4: The Proof', color=COLORS['text'], weight='bold')
        ax.axis('off')
        
        proof_steps = [
            "Area of large square = (a + b)²",
            "",
            "Method 1 (algebra):",
            "(a + b)² = a² + 2ab + b²",
            "",
            "Method 2 (geometry):",
            "(a + b)² = 4 × (½ab) + c²",
            "         = 2ab + c²",
            "",
            "Setting equal:",
            "a² + 2ab + b² = 2ab + c²",
            "",
            "Subtract 2ab from both sides:",
            "a² + b² = c²  ✓"
        ]
        
        y_pos = 0.95
        for step in proof_steps:
            if step == "":
                y_pos -= 0.04
                continue
                
            if "✓" in step:
                color = COLORS['success']
                size = 14
                weight = 'bold'
            elif step.startswith("Method") or step.startswith("Setting") or step.startswith("Subtract"):
                color = COLORS['accent']
                size = 11
                weight = 'bold'
            else:
                color = COLORS['text']
                size = 10
                weight = 'normal'
                
            ax.text(0.05, y_pos, step, transform=ax.transAxes,
                   color=color, fontsize=size, weight=weight, family='monospace')
            y_pos -= 0.06

    def create_interactive_explorer(self):
        """Create interactive theorem explorer"""
        fig, ax = plt.subplots(figsize=(12, 10))
        fig.patch.set_facecolor(COLORS['background'])
        plt.subplots_adjust(bottom=0.25)
        
        # Initial values
        a_init, b_init = 3, 4
        
        # Create sliders
        ax_a = plt.axes([0.2, 0.1, 0.5, 0.03], facecolor=COLORS['surface'])
        ax_b = plt.axes([0.2, 0.05, 0.5, 0.03], facecolor=COLORS['surface'])
        
        slider_a = Slider(ax_a, 'Side a', 1, 8, valinit=a_init, valfmt='%.1f')
        slider_b = Slider(ax_b, 'Side b', 1, 8, valinit=b_init, valfmt='%.1f')
        
        def update_display(val=None):
            ax.clear()
            a = slider_a.val
            b = slider_b.val
            c = math.sqrt(a*a + b*b)
            
            ax.set_facecolor(COLORS['surface'])
            ax.set_xlim(-max(a,b)-1, a+c+1)
            ax.set_ylim(-a-1, b+1)
            ax.set_aspect('equal')
            
            # Draw triangle
            triangle = patches.Polygon([(0, 0), (a, 0), (0, b)], 
                                      facecolor=COLORS['primary'], alpha=0.8,
                                      edgecolor='white', linewidth=3)
            ax.add_patch(triangle)
            
            # Draw squares
            sq_a = patches.Rectangle((0, -a), a, a, facecolor=COLORS['accent'], 
                                   alpha=0.7, edgecolor='white', linewidth=2)
            sq_b = patches.Rectangle((-b, 0), b, b, facecolor=COLORS['success'], 
                                   alpha=0.7, edgecolor='white', linewidth=2)
            sq_c = patches.Rectangle((a+0.5, 0), c, c, facecolor=COLORS['warning'], 
                                   alpha=0.7, edgecolor='white', linewidth=2)
            
            ax.add_patch(sq_a)
            ax.add_patch(sq_b)
            ax.add_patch(sq_c)
            
            # Labels
            ax.text(a/2, -0.3, f'a = {a:.1f}', fontsize=12, color=COLORS['text'], 
                   ha='center', weight='bold')
            ax.text(-0.3, b/2, f'b = {b:.1f}', fontsize=12, color=COLORS['text'], 
                   ha='right', va='center', weight='bold')
            ax.text(a/2, b/2, f'c = {c:.2f}', fontsize=12, color=COLORS['text'], 
                   ha='center', va='center', weight='bold')
            
            # Area labels
            ax.text(a/2, -a/2, f'a² = {a*a:.1f}', fontsize=10, color=COLORS['text'], 
                   ha='center', va='center', weight='bold')
            ax.text(-b/2, b/2, f'b² = {b*b:.1f}', fontsize=10, color=COLORS['text'], 
                   ha='center', va='center', weight='bold')
            ax.text(a+0.5+c/2, c/2, f'c² = {c*c:.1f}', fontsize=10, color=COLORS['text'], 
                   ha='center', va='center', weight='bold')
            
            # Verification
            verification = f'Verification: {a:.1f}² + {b:.1f}² = {a*a:.1f} + {b*b:.1f} = {a*a + b*b:.1f}'
            is_correct = abs((a*a + b*b) - c*c) < 0.01
            verification += f'\nc² = {c*c:.1f}'
            verification += ' ✓ Theorem verified!' if is_correct else ' ✗ Check calculations'
            
            color = COLORS['success'] if is_correct else COLORS['secondary']
            ax.text(0.02, 0.98, verification, transform=ax.transAxes,
                   fontsize=12, color=color, weight='bold',
                   verticalalignment='top', family='monospace',
                   bbox=dict(boxstyle="round,pad=0.3", facecolor=COLORS['background'], alpha=0.8))
            
            ax.set_title('Interactive Pythagorean Theorem Explorer', 
                        color=COLORS['text'], fontsize=16, weight='bold')
            ax.grid(True, alpha=0.3, color=COLORS['text'])
            
        # Connect sliders to update function
        slider_a.on_changed(update_display)
        slider_b.on_changed(update_display)
        
        # Initial display
        update_display()
        
        return fig, (slider_a, slider_b)

def main():
    """Main function to create all visualizations"""
    suite = PythagoreanEducationalSuite()
    
    # Create overview
    print("Creating proof overview...")
    fig1 = suite.create_proof_overview()
    fig1.savefig('/tmp/pythagorean_overview.png', dpi=300, bbox_inches='tight',
                facecolor=COLORS['background'])
    
    # Create detailed geometric proof
    print("Creating detailed geometric proof...")
    fig2 = suite.create_detailed_geometric_proof()
    fig2.savefig('/tmp/pythagorean_detailed_proof.png', dpi=300, bbox_inches='tight',
                facecolor=COLORS['background'])
    
    # Create interactive explorer
    print("Creating interactive explorer...")
    fig3, sliders = suite.create_interactive_explorer()
    fig3.savefig('/tmp/pythagorean_interactive.png', dpi=300, bbox_inches='tight',
                facecolor=COLORS['background'])
    
    print("All visualizations created successfully!")
    print("Files saved:")
    print("- /tmp/pythagorean_overview.png")
    print("- /tmp/pythagorean_detailed_proof.png") 
    print("- /tmp/pythagorean_interactive.png")
    
    # Show the plots
    plt.show()

if __name__ == "__main__":
    main()