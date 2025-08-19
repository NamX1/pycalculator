# PyCalculator 🧮

A modern, responsive web-based calculator built with Flask and JavaScript. Features a sleek gradient design with smooth animations and full keyboard support.

![Calculator Interface](https://via.placeholder.com/800x600/667eea/ffffff?text=Calculator+Interface)

## ✨ Features

- **Modern UI Design**: Beautiful gradient background with smooth hover animations
- **Responsive Layout**: Works perfectly on desktop and mobile devices
- **Full Keyboard Support**: Use your keyboard for all calculator operations
- **Error Handling**: Graceful handling of division by zero and invalid expressions
- **Security**: Input validation prevents code injection attacks
- **Real-time Calculations**: Instant results via AJAX API calls
- **Clear & Delete Functions**: Multiple ways to clear or correct input

## 🚀 Quick Start

### Prerequisites

- Python 3.6 or higher
- pip (Python package installer)

### Installation

1. **Clone the repository**
   ```bash
   git clone https://github.com/NamX1/pycalculator.git
   cd pycalculator
   ```

2. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```
   
   Or install Flask directly:
   ```bash
   pip install flask
   ```

3. **Run the application**
   ```bash
   python main.py
   ```

4. **Open your browser**
   ```
   Navigate to http://127.0.0.1:5000
   ```

## 🎯 Usage

### Basic Operations
- **Numbers**: Click number buttons or use keyboard (0-9)
- **Operators**: Use +, -, ×, / for basic arithmetic
- **Decimal**: Click . or press . for decimal numbers
- **Calculate**: Click = or press Enter to get results

### Clear Functions
- **C (Clear)**: Clears the entire calculation
- **CE (Clear Entry)**: Clears current entry only
- **⌫ (Backspace)**: Deletes last entered character

### Keyboard Shortcuts
| Key | Action |
|-----|--------|
| `0-9` | Input numbers |
| `+` `-` `*` `/` | Mathematical operations |
| `.` | Decimal point |
| `Enter` or `=` | Calculate result |
| `Escape` | Clear all |
| `Backspace` | Delete last character |

## 🔧 API Endpoints

### POST /calculate
Processes mathematical expressions and returns results.

**Request Body:**
```json
{
  "expression": "2+3*4"
}
```

**Response (Success):**
```json
{
  "result": 14
}
```

**Response (Error):**
```json
{
  "error": "Cannot divide by zero"
}
```

## 📁 Project Structure

```
pycalculator/
├── main.py              # Flask application and API routes
├── templates/
│   └── index.html       # Calculator UI with CSS and JavaScript
├── requirements.txt     # Python dependencies
├── README.md           # Project documentation
└── LICENSE             # MIT License
```

## 🛠️ Technical Details

### Backend (Flask)
- **Framework**: Flask web framework
- **Security**: Regex validation for mathematical expressions
- **Error Handling**: Comprehensive error catching for edge cases
- **API**: RESTful endpoint for calculation processing

### Frontend
- **Design**: Modern CSS with gradients and animations
- **Layout**: CSS Grid for responsive button layout
- **JavaScript**: Vanilla JS for calculator logic and API communication
- **Accessibility**: Keyboard navigation and clear visual feedback

### Security Features
- Input validation using regex patterns
- Prevention of code injection attacks
- Safe expression evaluation

## 🎨 Customization

You can easily customize the calculator's appearance by modifying the CSS variables in `templates/index.html`:

```css
/* Color scheme */
background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
.calculator { background: #2c3e50; }
.display { background: #34495e; }
.btn { background: #3498db; }
.btn.operator { background: #e74c3c; }
.btn.clear { background: #f39c12; }
.btn.equals { background: #27ae60; }
```

## 🤝 Contributing

Contributions are welcome! Here's how you can help:

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/amazing-feature`)
3. Commit your changes (`git commit -m 'Add amazing feature'`)
4. Push to the branch (`git push origin feature/amazing-feature`)
5. Open a Pull Request

### Development Setup

For development, you might want to install additional tools:

```bash
# For code formatting
pip install black

# For testing (if you add tests)
pip install pytest
```

## 📝 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## 🐛 Known Issues

- None currently reported

## 🔮 Future Enhancements

- [ ] Scientific calculator functions (sin, cos, tan, etc.)
- [ ] Calculation history
- [ ] Multiple themes
- [ ] Unit tests
- [ ] Docker containerization
- [ ] Progressive Web App (PWA) features

## 📞 Support

If you encounter any issues or have questions:

1. Check the [Issues](https://github.com/NamX1/pycalculator/issues) page
2. Create a new issue if your problem isn't already reported
3. Provide detailed information about the problem

## 🙏 Acknowledgments

- Flask documentation and community
- Modern CSS design inspiration
- Contributors and testers

---

**Made with ❤️ by NamX**