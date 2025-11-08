# Coding Reminder Overlay

A simple Python tool to help you remember where you left off when taking breaks from coding. Creates a full-screen overlay with your custom reminder text.

## 🎯 Purpose

When you step away from coding for a break, it's easy to forget exactly where you were. This tool lets you quickly jot down a reminder that will greet you with a full-screen overlay when you return, helping you pick up right where you left off.

## ✨ Features

- **Full-screen opaque overlay** - Impossible to miss when you return
- **Markdown support** - Format your reminders with headers, bold, code blocks, and more
- **Built-in cheatsheet** - Markdown reference right in the input window
- **Simple keyboard shortcuts** - ESC or Ctrl+Q to close
- **No installation** - Just Python (comes with Windows)
- **Silent launch** - No command windows or flashing

## 📋 Requirements

- Python 3.x (usually pre-installed on Windows 10/11)
- No additional packages needed - uses only built-in libraries!

## 🚀 Quick Start

1. **Download all files** to the same folder:

   - `RemindMe.py`
   - `Run_RemindMe.vbs`

2. **Double-click** `Run_RemindMe.vbs` to launch

3. **Type your reminder** in the input box (with optional markdown formatting)

4. **Click "Create Overlay"** or press Ctrl+Enter

5. **Go take your break!**

6. **When you return**, press ESC or Ctrl+Q to close the overlay and resume coding

## 📝 Markdown Support

The reminder supports markdown formatting for better readability:

### Headers

```markdown
# Main Header

## Sub Header

### Smaller Header
```

### Text Formatting

- `**bold text**` - Displays in **yellow**
- `*italic text*` - Displays in _cyan_
- `` `inline code` `` - Displays in red with dark background

### Code Blocks

```python
def my_function():
    return "formatted code"
```

### Lists

```markdown
- Bullet point
- Another point

1. Numbered item
2. Another item
```

## 💡 Usage Example

```markdown
# Task: Fix Login Bug

- File: `auth.py` line 245
- Issue: **null check** needed for email field
- Test with _admin user_ after fixing
```

if user.email is None:
raise ValidationError()

```text

Next: Update unit tests
```

## ⌨️ Keyboard Shortcuts

- **Ctrl+Enter** - Create overlay (from input window)
- **ESC** - Close overlay
- **Ctrl+Q** - Close overlay

## 🎨 Color Scheme

- **Normal text & headers**: Green
- **Bold text**: Yellow
- **Italic text**: Cyan
- **Code**: Red on dark gray background
- **Background**: Dark translucent overlay (85% opacity)

## 🔧 Customization

You can edit `RemindMe.py` to customize:

- Colors (search for color hex codes like `#00ff00`)
- Font sizes (look for font size numbers)
- Opacity (change the `0.85` value in `attributes('-alpha', 0.85)`)
- Window size of input dialog

## 🐛 Troubleshooting

### "Python is not recognized"

- Install Python from python.org
- Make sure "Add Python to PATH" is checked during installation

### Window doesn't appear

- Try running from Command Prompt: `python RemindMe.py`
- Check for error messages

### Overlay won't close

- Press ESC or Ctrl+Q
- If stuck, press Alt+F4 or Ctrl+Alt+Delete to force close

## 📁 File Structure

```text
your-folder/
├── RemindMe.py           # Main Python script
├── Run_RemindMe.vbs      # Silent launcher (recommended)
└── README.md             # This file
```

## 🤝 Tips

- Keep reminders concise - you want to quickly get back to coding
- Use markdown to highlight the most important information
- Include file names and line numbers for quick navigation
- Mention what you were about to do next

## 📄 License

Free to use and modify for personal or commercial use.

## 🙋 Support

This is a simple standalone tool. If you encounter issues:

1. Make sure Python is installed
2. Check that all files are in the same folder
3. Try running `RemindMe.py` directly from Command Prompt to see error messages

---

**Live Long and Prosper** 🖖

---
