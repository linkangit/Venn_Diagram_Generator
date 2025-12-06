import matplotlib.pyplot as plt
import matplotlib.patches as patches
from matplotlib.patches import Circle
import numpy as np
from matplotlib_venn import venn2, venn3
import os
from pathlib import Path

class VennDiagramGenerator:
    def __init__(self):
        self.num_sets = None
        self.values = {}
        self.set_names = []
        self.colors = None
        self.transparency = 0.6
        self.edge_width = 2
        self.font_size = 12
        self.title = "Venn Diagram"
        
    def get_number_of_sets(self):
        """Ask user for number of sets (2-5)"""
        while True:
            try:
                num = int(input("\nHow many sets do you want to compare? (2-5): "))
                if 2 <= num <= 5:
                    self.num_sets = num
                    return num
                else:
                    print("❌ Please enter a number between 2 and 5.")
            except ValueError:
                print("❌ Invalid input. Please enter a number.")
    
    def get_intersection_values(self):
        """Dynamically generate prompts based on number of sets"""
        print(f"\n{'='*60}")
        print(f"Enter intersection values for {self.num_sets} sets")
        print(f"{'='*60}")
        
        if self.num_sets == 2:
            self.values = self.get_2set_values()
        elif self.num_sets == 3:
            self.values = self.get_3set_values()
        elif self.num_sets == 4:
            self.values = self.get_4set_values()
        elif self.num_sets == 5:
            self.values = self.get_5set_values()
    
    def get_2set_values(self):
        """Get values for 2-set Venn diagram"""
        print("\nSet naming: You can name your sets (e.g., 'Cats', 'Dogs')")
        set_a_name = input("Name for Set A: ").strip() or "Set A"
        set_b_name = input("Name for Set B: ").strip() or "Set B"
        
        self.set_names = [set_a_name, set_b_name]
        
        values = {}
        values['10'] = self.get_positive_int(f"Only in {set_a_name}: ")
        values['01'] = self.get_positive_int(f"Only in {set_b_name}: ")
        values['11'] = self.get_positive_int(f"In both {set_a_name} and {set_b_name}: ")
        
        return (values['10'], values['01'], values['11'])
    
    def get_3set_values(self):
        """Get values for 3-set Venn diagram"""
        print("\nSet naming:")
        set_a = input("Name for Set A: ").strip() or "Set A"
        set_b = input("Name for Set B: ").strip() or "Set B"
        set_c = input("Name for Set C: ").strip() or "Set C"
        
        self.set_names = [set_a, set_b, set_c]
        
        values = {}
        values['100'] = self.get_positive_int(f"Only in {set_a}: ")
        values['010'] = self.get_positive_int(f"Only in {set_b}: ")
        values['001'] = self.get_positive_int(f"Only in {set_c}: ")
        values['110'] = self.get_positive_int(f"In {set_a} and {set_b}, not {set_c}: ")
        values['101'] = self.get_positive_int(f"In {set_a} and {set_c}, not {set_b}: ")
        values['011'] = self.get_positive_int(f"In {set_b} and {set_c}, not {set_a}: ")
        values['111'] = self.get_positive_int(f"In all three ({set_a}, {set_b}, {set_c}): ")
        
        return (values['100'], values['010'], values['001'], 
                values['110'], values['101'], values['011'], values['111'])
    
    def get_4set_values(self):
        """Get values for 4-set Venn diagram"""
        print("\nSet naming:")
        sets = {}
        for letter in ['A', 'B', 'C', 'D']:
            sets[letter] = input(f"Name for Set {letter}: ").strip() or f"Set {letter}"
        
        self.set_names = [sets['A'], sets['B'], sets['C'], sets['D']]
        
        values = {}
        # Single sets
        values['1000'] = self.get_positive_int(f"Only in {sets['A']}: ")
        values['0100'] = self.get_positive_int(f"Only in {sets['B']}: ")
        values['0010'] = self.get_positive_int(f"Only in {sets['C']}: ")
        values['0001'] = self.get_positive_int(f"Only in {sets['D']}: ")
        
        # Pairwise intersections
        values['1100'] = self.get_positive_int(f"In {sets['A']} and {sets['B']}, not others: ")
        values['1010'] = self.get_positive_int(f"In {sets['A']} and {sets['C']}, not others: ")
        values['1001'] = self.get_positive_int(f"In {sets['A']} and {sets['D']}, not others: ")
        values['0110'] = self.get_positive_int(f"In {sets['B']} and {sets['C']}, not others: ")
        values['0101'] = self.get_positive_int(f"In {sets['B']} and {sets['D']}, not others: ")
        values['0011'] = self.get_positive_int(f"In {sets['C']} and {sets['D']}, not others: ")
        
        # Three-way intersections
        values['1110'] = self.get_positive_int(f"In {sets['A']}, {sets['B']}, {sets['C']}, not {sets['D']}: ")
        values['1101'] = self.get_positive_int(f"In {sets['A']}, {sets['B']}, {sets['D']}, not {sets['C']}: ")
        values['1011'] = self.get_positive_int(f"In {sets['A']}, {sets['C']}, {sets['D']}, not {sets['B']}: ")
        values['0111'] = self.get_positive_int(f"In {sets['B']}, {sets['C']}, {sets['D']}, not {sets['A']}: ")
        
        # Four-way intersection
        values['1111'] = self.get_positive_int(f"In all four sets: ")
        
        # Store as dict for 4-set diagram
        self.four_set_values = values
        
        return values
    
    def get_5set_values(self):
        """Get values for 5-set Venn diagram"""
        print("\nSet naming:")
        sets = {}
        for letter in ['A', 'B', 'C', 'D', 'E']:
            sets[letter] = input(f"Name for Set {letter}: ").strip() or f"Set {letter}"
        
        self.set_names = [sets['A'], sets['B'], sets['C'], sets['D'], sets['E']]
        
        print(f"\n⚠️  For simplicity, enter a few key intersection values.")
        print("(Leave blank or enter 0 for values you don't need)\n")
        
        values = {}
        # Single sets (5 values)
        for letter in ['A', 'B', 'C', 'D', 'E']:
            values[letter] = self.get_positive_int(f"Only in {sets[letter]}: ", allow_blank=True)
        
        # Center - all 5 intersecting
        values['ALL'] = self.get_positive_int(f"In all five sets: ", allow_blank=True)
        
        # Store for 5-set diagram
        self.five_set_values = values
        
        return values
    
    def get_positive_int(self, prompt, allow_blank=False):
        """Get positive integer input from user"""
        while True:
            try:
                user_input = input(prompt).strip()
                if allow_blank and user_input == '':
                    return 0
                value = int(user_input)
                if value >= 0:
                    return value
                else:
                    print("❌ Please enter a non-negative number.")
            except ValueError:
                print("❌ Invalid input. Please enter a number.")
    
    def customize_appearance(self):
        """Allow user to customize diagram appearance"""
        print(f"\n{'='*60}")
        print("Customize Venn Diagram Appearance")
        print(f"{'='*60}")
        
        # Color scheme
        print("\nColor Schemes (All colorblind-friendly):")
        print("1. Tol Bright (blue, orange, green, purple, tan)")
        print("2. Tol Muted (blue, red, green, yellow, cyan)")
        print("3. Tol Light (purple, cyan, teal, green, olive)")
        print("4. Tol Medium (blue, burgundy, yellow, navy, brown)")
        print("5. Tol Pale (cyan, pink, yellow, green, purple)")
        print("6. Custom (enter hex codes)")
        
        scheme = input("Choose color scheme (1-6) [default: 1]: ").strip() or "1"
        self.set_color_scheme(scheme)
        
        # Transparency
        trans_input = input("Transparency level (0.0-1.0) [default: 0.6]: ").strip()
        if trans_input:
            try:
                self.transparency = float(trans_input)
                if not (0 <= self.transparency <= 1):
                    self.transparency = 0.6
            except ValueError:
                self.transparency = 0.6
        
        # Edge width
        edge_input = input("Edge width (0-5) [default: 2]: ").strip()
        if edge_input:
            try:
                self.edge_width = float(edge_input)
            except ValueError:
                self.edge_width = 2
        
        # Font size
        font_input = input("Font size (8-30) [default: 12]: ").strip()
        if font_input:
            try:
                self.font_size = int(font_input)
                if not (8 <= self.font_size <= 30):
                    self.font_size = 12
            except ValueError:
                self.font_size = 12
        
        # Title
        title_input = input("Diagram title [default: Venn Diagram]: ").strip()
        if title_input:
            self.title = title_input
    
    def set_color_scheme(self, scheme):
        """Set color scheme based on user choice"""
        schemes = {
            '1': ['#0173B2', '#DE8F05', '#029E73', '#CC78BC', '#CA9161'],  # Colorblind safe - Tol Bright
            '2': ['#4477AA', '#EE6677', '#228833', '#CCBB44', '#66CCEE'],  # Colorblind safe - Tol Muted
            '3': ['#332288', '#88CCEE', '#44AA99', '#117733', '#999933'],  # Colorblind safe - Tol Light
            '4': ['#6699CC', '#994455', '#EECC66', '#004488', '#997700'],  # Colorblind safe - Tol Medium
            '5': ['#88CCEE', '#CC6677', '#DDCC77', '#117733', '#332288'],  # Colorblind safe - Tol Pale
        }
        
        if scheme in schemes:
            self.colors = schemes[scheme]
        elif scheme == '6':
            self.colors = []
            for i in range(self.num_sets):
                hex_color = input(f"Enter hex color for set {i+1} (e.g., #FF5733): ").strip()
                if hex_color.startswith('#') and len(hex_color) == 7:
                    self.colors.append(hex_color)
                else:
                    self.colors.append(schemes['1'][i])  # Fallback
        else:
            self.colors = schemes['1']  # Default to colorblind safe
    
    def blend_colors(self, hex_colors):
        """Blend multiple hex colors together by averaging RGB values"""
        if len(hex_colors) == 1:
            return hex_colors[0]
        
        # Convert hex to RGB
        rgb_colors = []
        for hex_color in hex_colors:
            hex_color = hex_color.lstrip('#')
            rgb = tuple(int(hex_color[i:i+2], 16) for i in (0, 2, 4))
            rgb_colors.append(rgb)
        
        # Average the RGB values
        avg_r = int(sum(r for r, g, b in rgb_colors) / len(rgb_colors))
        avg_g = int(sum(g for r, g, b in rgb_colors) / len(rgb_colors))
        avg_b = int(sum(b for r, g, b in rgb_colors) / len(rgb_colors))
        
        # Convert back to hex
        return f'#{avg_r:02x}{avg_g:02x}{avg_b:02x}'
    
    def generate_venn(self):
        """Generate and display the Venn diagram"""
        fig, ax = plt.subplots(figsize=(14, 10))
        
        try:
            if self.num_sets == 2:
                # Use equal sizes for all circles
                normalized_values = (1, 1, 1)  # Equal sizes
                v = venn2(subsets=normalized_values, ax=ax, 
                          set_labels=self.set_names[:2], alpha=self.transparency, normalize_to=1.0)
                
                # Manually set colors for regions to show overlaps
                # Region '10' - only A
                patch_10 = v.get_patch_by_id('10')
                if patch_10:
                    patch_10.set_facecolor(self.colors[0])
                    patch_10.set_edgecolor('black')
                    patch_10.set_linewidth(self.edge_width)
                
                # Region '01' - only B
                patch_01 = v.get_patch_by_id('01')
                if patch_01:
                    patch_01.set_facecolor(self.colors[1])
                    patch_01.set_edgecolor('black')
                    patch_01.set_linewidth(self.edge_width)
                
                # Region '11' - A and B intersection (blend colors)
                patch_11 = v.get_patch_by_id('11')
                if patch_11:
                    blended_color = self.blend_colors([self.colors[0], self.colors[1]])
                    patch_11.set_facecolor(blended_color)
                    patch_11.set_edgecolor('black')
                    patch_11.set_linewidth(self.edge_width)
                
                # Update the text labels to show actual values
                label_ids = ['10', '01', '11']
                actual_values = self.values
                for i, label_id in enumerate(label_ids):
                    label = v.get_label_by_id(label_id)
                    if label:
                        label.set_text(str(actual_values[i]))
                        
            elif self.num_sets == 3:
                # Use equal sizes for all circles
                normalized_values = (1, 1, 1, 1, 1, 1, 1)  # Equal sizes
                v = venn3(subsets=normalized_values, ax=ax,
                          set_labels=self.set_names[:3], alpha=self.transparency, normalize_to=1.0)
                
                # Manually set colors for regions to show overlaps
                color_map = {
                    '100': [self.colors[0]],  # Only A
                    '010': [self.colors[1]],  # Only B
                    '001': [self.colors[2]],  # Only C
                    '110': [self.colors[0], self.colors[1]],  # A and B
                    '101': [self.colors[0], self.colors[2]],  # A and C
                    '011': [self.colors[1], self.colors[2]],  # B and C
                    '111': [self.colors[0], self.colors[1], self.colors[2]]  # All three
                }
                
                for patch_id, colors in color_map.items():
                    patch = v.get_patch_by_id(patch_id)
                    if patch:
                        blended_color = self.blend_colors(colors)
                        patch.set_facecolor(blended_color)
                        patch.set_edgecolor('black')
                        patch.set_linewidth(self.edge_width)
                
                # Update the text labels to show actual values
                label_ids = ['100', '010', '001', '110', '101', '011', '111']
                actual_values = self.values
                for i, label_id in enumerate(label_ids):
                    label = v.get_label_by_id(label_id)
                    if label:
                        label.set_text(str(actual_values[i]))
                        
            elif self.num_sets == 4:
                self.create_venn4(ax)
            elif self.num_sets == 5:
                self.create_venn5(ax)
            
            # Apply title customization
            ax.set_title(self.title, fontsize=self.font_size + 6, fontweight='normal', pad=20)
            
            # Style text for 2-3 set diagrams
            if self.num_sets in [2, 3]:
                for text in ax.texts:
                    text.set_fontsize(self.font_size)
                    text.set_fontweight('normal')
                    text.set_fontfamily('sans-serif')
            
            plt.tight_layout()
            return fig
        
        except Exception as e:
            print(f"❌ Error generating Venn diagram: {e}")
            import traceback
            traceback.print_exc()
            return None
    
    def create_venn4(self, ax):
        """Create a 4-set Venn diagram using circles with proper text positioning and color blending"""
        # Create 4 circles arranged in a 2x2 grid pattern
        centers = [(-0.8, 0.8), (0.8, 0.8), (-0.8, -0.8), (0.8, -0.8)]
        radius = 1.2
        
        # Add circles with transparency to show overlaps
        for i, (cx, cy) in enumerate(centers):
            circle = Circle((cx, cy), radius, color=self.colors[i], 
                          alpha=self.transparency, ec='black', linewidth=self.edge_width, zorder=1)
            ax.add_patch(circle)
        
        # Add set labels
        label_distance = 1.8
        label_positions = [(-label_distance, label_distance), (label_distance, label_distance), 
                          (-label_distance, -label_distance), (label_distance, -label_distance)]
        
        for i, pos in enumerate(label_positions):
            ax.text(pos[0], pos[1], self.set_names[i], fontsize=self.font_size + 8, 
                   fontweight='normal', ha='center', va='center',
                   bbox=dict(boxstyle='round,pad=0.5', facecolor='white', edgecolor='black', linewidth=1), zorder=10)
        
        # Define which sets contribute to each region for color blending
        region_color_map = {
            '1000': [0],        # Only A
            '0100': [1],        # Only B
            '0010': [2],        # Only C
            '0001': [3],        # Only D
            '1100': [0, 1],     # A and B
            '1010': [0, 2],     # A and C
            '1001': [0, 3],     # A and D
            '0110': [1, 2],     # B and C
            '0101': [1, 3],     # B and D
            '0011': [2, 3],     # C and D
            '1110': [0, 1, 2],  # A, B, C
            '1101': [0, 1, 3],  # A, B, D
            '1011': [0, 2, 3],  # A, C, D
            '0111': [1, 2, 3],  # B, C, D
            '1111': [0, 1, 2, 3]  # All
        }
        
        # Add region values with proper positioning and color indicators
        region_positions = {
            # Only single sets
            '1000': (-1.5, 1.5),   # Only A
            '0100': (1.5, 1.5),    # Only B
            '0010': (-1.5, -1.5),  # Only C
            '0001': (1.5, -1.5),   # Only D
            # Pairwise
            '1100': (0.0, 1.2),    # A and B
            '1010': (-1.2, 0.0),   # A and C
            '1001': (-0.4, 0.0),   # A and D
            '0110': (0.4, 0.0),    # B and C
            '0101': (1.2, 0.0),    # B and D
            '0011': (0.0, -1.2),   # C and D
            # Three-way
            '1110': (-0.3, 0.5),   # A, B, C
            '1101': (-0.3, -0.3),  # A, B, D
            '1011': (0.3, -0.3),   # A, C, D
            '0111': (0.3, 0.3),    # B, C, D
            # Four-way
            '1111': (0.0, 0.0),    # All
        }
        
        # Get stored values
        if hasattr(self, 'four_set_values'):
            for key, value in self.four_set_values.items():
                pos = region_positions.get(key, (0, 0))
                # Blend colors for this region
                color_indices = region_color_map.get(key, [])
                region_colors = [self.colors[i] for i in color_indices]
                blended_color = self.blend_colors(region_colors) if region_colors else 'white'
                
                ax.text(pos[0], pos[1], str(value), fontsize=self.font_size + 2, 
                       fontweight='normal', ha='center', va='center',
                       color='black',
                       bbox=dict(boxstyle='round,pad=0.3', facecolor=blended_color, 
                               edgecolor='black', alpha=0.9, linewidth=1), zorder=5)
        
        ax.set_xlim(-3, 3)
        ax.set_ylim(-3, 3)
        ax.set_aspect('equal')
        ax.axis('off')
    
    def create_venn5(self, ax):
        """Create a 5-set Venn diagram using circles in a pentagon arrangement"""
        # Arrange 5 circles in a pentagonal pattern
        angles = np.linspace(np.pi/2, 2*np.pi + np.pi/2, 6)[:-1]  # Start from top
        radius = 1.2
        circle_centers = [(1.5*np.cos(angle), 1.5*np.sin(angle)) for angle in angles]
        
        # Add circles with transparency to show overlaps
        for i, (cx, cy) in enumerate(circle_centers):
            circle = Circle((cx, cy), radius, color=self.colors[i], 
                          alpha=self.transparency, ec='black', linewidth=self.edge_width, zorder=1)
            ax.add_patch(circle)
        
        # Add set labels outside the circles
        label_dist = 2.6
        for i, angle in enumerate(angles):
            label_x = label_dist * np.cos(angle)
            label_y = label_dist * np.sin(angle)
            ax.text(label_x, label_y, self.set_names[i], fontsize=self.font_size + 8, 
                   fontweight='normal', ha='center', va='center',
                   bbox=dict(boxstyle='round,pad=0.5', facecolor='white', edgecolor='black', linewidth=1), zorder=10)
        
        # Add values if available
        if hasattr(self, 'five_set_values'):
            # Single set values - positioned towards the outer edge with blended colors
            for i, angle in enumerate(angles):
                value_x = 2.0 * np.cos(angle)
                value_y = 2.0 * np.sin(angle)
                letter = ['A', 'B', 'C', 'D', 'E'][i]
                # Single set gets its own color
                blended_color = self.colors[i]
                ax.text(value_x, value_y, str(self.five_set_values[letter]), 
                       fontsize=self.font_size + 2, fontweight='normal', 
                       ha='center', va='center', color='black',
                       bbox=dict(boxstyle='round,pad=0.3', facecolor=blended_color, 
                               edgecolor='black', alpha=0.9, linewidth=1), zorder=5)
            
            # Center value (all 5) - blend all colors
            all_colors_blended = self.blend_colors(self.colors[:5])
            ax.text(0, 0, str(self.five_set_values['ALL']), 
                   fontsize=self.font_size + 4, fontweight='normal', 
                   ha='center', va='center', color='black',
                   bbox=dict(boxstyle='round,pad=0.3', facecolor=all_colors_blended, 
                           edgecolor='black', alpha=0.9, linewidth=1), zorder=5)
        
        ax.set_xlim(-3.8, 3.8)
        ax.set_ylim(-3.8, 3.8)
        ax.set_aspect('equal')
        ax.axis('off')
        
        ax.set_xlim(-3.8, 3.8)
        ax.set_ylim(-3.8, 3.8)
        ax.set_aspect('equal')
        ax.axis('off')
    
    def save_diagram(self, fig):
        """Ask user to save the diagram"""
        print(f"\n{'='*60}")
        print("Save Venn Diagram")
        print(f"{'='*60}")
        
        save = input("Do you want to save the diagram? (yes/no) [default: yes]: ").strip().lower()
        if save in ['no', 'n']:
            print("Diagram not saved.")
            return
        
        print("\nSupported formats: PNG, JPEG, TIFF, PDF, SVG")
        format_choice = input("Choose format (PNG/JPEG/TIFF/PDF/SVG) [default: PNG]: ").strip().upper() or "PNG"
        
        valid_formats = ['PNG', 'JPEG', 'TIFF', 'PDF', 'SVG']
        if format_choice not in valid_formats:
            print("❌ Invalid format. Using PNG.")
            format_choice = 'PNG'
        
        filename = input("Enter filename (without extension) [default: venn_diagram]: ").strip() or "venn_diagram"
        
        # Create output directory if it doesn't exist
        output_dir = Path("venn_diagrams")
        output_dir.mkdir(exist_ok=True)
        
        # Map format to file extension
        ext_map = {'PNG': 'png', 'JPEG': 'jpg', 'TIFF': 'tiff', 'PDF': 'pdf', 'SVG': 'svg'}
        extension = ext_map[format_choice]
        
        # Determine DPI for quality (not applicable for vector formats)
        if format_choice in ['PNG', 'JPEG', 'TIFF']:
            dpi = input("Image quality - DPI (72/150/300) [default: 150]: ").strip() or "150"
            try:
                dpi = int(dpi)
            except ValueError:
                dpi = 150
        else:
            dpi = 100  # Default for vector formats
        
        filepath = output_dir / f"{filename}.{extension}"
        
        try:
            fig.savefig(filepath, dpi=dpi, bbox_inches='tight', facecolor='white')
            print(f"\n✅ Diagram saved successfully!")
            print(f"📁 Location: {filepath.absolute()}")
        except Exception as e:
            print(f"❌ Error saving file: {e}")
    
    def run(self):
        """Main application loop"""
        print("\n" + "="*60)
        print("🎯 VENN DIAGRAM GENERATOR")
        print("="*60)
        print("Create beautiful, customizable Venn diagrams!")
        
        # Get number of sets
        self.get_number_of_sets()
        
        # Get intersection values
        self.get_intersection_values()
        
        # Customize appearance
        customize = input("\nCustomize appearance? (yes/no) [default: yes]: ").strip().lower()
        if customize in ['', 'yes', 'y']:
            self.customize_appearance()
        else:
            # Use default colorblind-friendly colors
            default_colors = ['#0173B2', '#DE8F05', '#029E73', '#CC78BC', '#CA9161']
            self.colors = default_colors[:self.num_sets]
        
        # Generate diagram
        print("\n⏳ Generating Venn diagram...")
        fig = self.generate_venn()
        
        if fig:
            plt.show()
            
            # Ask to save
            self.save_diagram(fig)
        
        print("\n" + "="*60)
        print("✨ Thank you for using Venn Diagram Generator!")
        print("="*60)

def main():
    generator = VennDiagramGenerator()
    generator.run()

if __name__ == "__main__":
    main()
