# 🎯 Venn Diagram Generator

A powerful, interactive Python tool for creating beautiful and customizable Venn diagrams with 2-5 sets. Perfect for data visualization, presentations, and educational purposes.

![Python](https://img.shields.io/badge/python-3.7+-blue.svg)
![Matplotlib](https://img.shields.io/badge/matplotlib-required-orange.svg)

## ✨ Features

- **Multiple Set Support**: Create Venn diagrams with 2, 3, 4, or 5 sets
- **Custom Set Names**: Personalize your sets with meaningful labels
- **Colorblind-Friendly Palettes**: 5 built-in accessible color schemes based on Paul Tol's palettes
- **Custom Colors**: Option to use your own hex color codes
- **Color Blending**: Intersection regions automatically blend colors from contributing sets
- **Flexible Customization**: Adjust transparency, edge width, font size, and title
- **Multiple Export Formats**: Save as PNG, JPEG, TIFF, PDF, or SVG
- **Interactive CLI**: User-friendly command-line interface with helpful prompts

## 📋 Requirements

- Python 3.7 or higher
- matplotlib
- matplotlib-venn
- numpy

## 🚀 Installation

1. **Clone the repository:**
```bash
git clone https://github.com/yourusername/venn-diagram-generator.git
cd venn-diagram-generator
```

2. **Install dependencies:**
```bash
pip install matplotlib matplotlib-venn numpy
```

Or use the requirements file (if provided):
```bash
pip install -r requirements.txt
```

## 📖 Usage

### Basic Usage

Run the script:
```bash
python venn_diagram_generator.py
```

### Step-by-Step Guide

#### 1. Choose Number of Sets
```
How many sets do you want to compare? (2-5): 3
```

#### 2. Name Your Sets
```
Set naming:
Name for Set A: Cats
Name for Set B: Dogs
Name for Set C: Birds
```

#### 3. Enter Intersection Values

The program will prompt you for values based on the number of sets:

**For 2 sets:**
- Only in Set A
- Only in Set B
- In both A and B

**For 3 sets:**
- Only in each set (3 values)
- Pairwise intersections (3 values)
- All three sets (1 value)

**For 4 sets:**
- Only in each set (4 values)
- Pairwise intersections (6 values)
- Three-way intersections (4 values)
- All four sets (1 value)

**For 5 sets:**
- Only in each set (5 values)
- All five sets (1 value)

#### 4. Customize Appearance (Optional)

Choose from various options:
- **Color Schemes**: 5 colorblind-friendly palettes or custom colors
- **Transparency**: 0.0 (opaque) to 1.0 (transparent)
- **Edge Width**: Line thickness around circles
- **Font Size**: Text size for labels and values
- **Title**: Custom diagram title

#### 5. Save Your Diagram

Choose your preferred format and quality:
- **Formats**: PNG, JPEG, TIFF, PDF, SVG
- **Quality**: DPI settings for raster formats
- **Location**: Automatically saved to `venn_diagrams/` folder

## 🎨 Color Schemes

All built-in color schemes are colorblind-friendly:

1. **Tol Bright** - Blue, orange, green, purple, tan
2. **Tol Muted** - Blue, red, green, yellow, cyan
3. **Tol Light** - Purple, cyan, teal, green, olive
4. **Tol Medium** - Blue, burgundy, yellow, navy, brown
5. **Tol Pale** - Cyan, pink, yellow, green, purple
6. **Custom** - Enter your own hex codes

## 💡 Examples

### Example 1: Simple 2-Set Venn Diagram
```
Sets: Programming Languages (Python, JavaScript)
Only in Python: 15
Only in JavaScript: 20
In both: 10
```

### Example 2: 3-Set Survey Analysis
```
Sets: Netflix Users, Spotify Users, Amazon Prime Users
Only in Netflix: 100
Only in Spotify: 150
Only in Amazon Prime: 120
Netflix & Spotify: 80
Netflix & Amazon: 60
Spotify & Amazon: 70
All three: 40
```

### Example 3: 4-Set Academic Study
```
Sets: Math, Science, English, History
[Enter values for all 15 possible intersections]
```

## 📂 Project Structure

```
venn-diagram-generator/
│
├── venn_diagram_generator.py    # Main application
├── README.md                     # This file
├── requirements.txt              # Python dependencies
└── venn_diagrams/               # Output folder (auto-created)
    └── [your saved diagrams]
```

## 🔧 Advanced Features

### Color Blending Algorithm

The generator automatically blends colors in intersection regions by averaging RGB values from contributing sets, creating visually intuitive representations of overlapping data.

### Normalized Circle Sizes

For 2 and 3-set diagrams, circles are normalized to equal sizes, ensuring intersections are clearly visible regardless of the input values.

### 4 and 5-Set Layouts

- **4 sets**: Arranged in a 2×2 grid pattern with strategically positioned value labels
- **5 sets**: Arranged in a pentagonal pattern for optimal visualization

## 🤝 Contributing

Contributions are welcome! Please feel free to submit a Pull Request. For major changes, please open an issue first to discuss what you would like to change.


## 🐛 Known Limitations

- For 4 and 5-set diagrams, not all possible intersections are individually labeled due to visual complexity
- The matplotlib-venn library has inherent limitations for 4+ set diagrams
- Very large numbers may require font size adjustments for readability

## 📧 Contact

For questions, suggestions, or issues, please open an issue on GitHub.

## 🙏 Acknowledgments

- Built with [matplotlib](https://matplotlib.org/) and [matplotlib-venn](https://github.com/konstantint/matplotlib-venn)
- Color schemes based on [Paul Tol's accessible color palettes](https://personal.sron.nl/~paultol/data/colourschemes.pdf)

---

**Made with ❤️ for data visualization enthusiasts**
