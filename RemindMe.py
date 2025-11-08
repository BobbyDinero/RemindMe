import tkinter as tk
from tkinter import font as tkfont
import sys
import re


class ReminderOverlay:
    def __init__(self):
        self.root = tk.Tk()
        self.root.title("Coding Reminder")
        self.root.geometry("700x500")
        self.root.configure(bg="#2b2b2b")

        # Center the input window
        self.root.eval("tk::PlaceWindow . center")

        # Make window stay on top
        self.root.attributes("-topmost", True)

        self.setup_input_window()

    def setup_input_window(self):
        """Setup the initial input window"""
        # Create main container with two columns
        main_container = tk.Frame(self.root, bg="#2b2b2b")
        main_container.pack(fill=tk.BOTH, expand=True, padx=10, pady=10)

        # Left side - Input area
        left_frame = tk.Frame(main_container, bg="#2b2b2b")
        left_frame.pack(side=tk.LEFT, fill=tk.BOTH, expand=True, padx=(0, 5))

        # Title label
        title_label = tk.Label(
            left_frame,
            text="Where did you leave off?",
            font=("Arial", 14, "bold"),
            bg="#2b2b2b",
            fg="#ffffff",
        )
        title_label.pack(pady=(0, 10))

        # Text input box
        self.text_input = tk.Text(
            left_frame,
            height=15,
            width=40,
            font=("Arial", 11),
            wrap=tk.WORD,
            bg="#3c3c3c",
            fg="#ffffff",
            insertbackground="#ffffff",
        )
        self.text_input.pack(pady=(0, 10))
        self.text_input.focus()

        # Submit button
        submit_btn = tk.Button(
            left_frame,
            text="Create Overlay",
            command=self.create_overlay,
            font=("Arial", 12, "bold"),
            bg="#4a90e2",
            fg="#ffffff",
            activebackground="#357abd",
            activeforeground="#ffffff",
            relief=tk.RAISED,
            borderwidth=2,
            padx=20,
            pady=10,
            cursor="hand2",
        )
        submit_btn.pack(pady=5)

        # Right side - Markdown cheatsheet
        right_frame = tk.Frame(main_container, bg="#2b2b2b")
        right_frame.pack(side=tk.RIGHT, fill=tk.BOTH, padx=(5, 0))

        # Cheatsheet title
        cheatsheet_title = tk.Label(
            right_frame,
            text="Markdown Cheatsheet",
            font=("Arial", 12, "bold"),
            bg="#2b2b2b",
            fg="#00ff00",
        )
        cheatsheet_title.pack(pady=(0, 5))

        # Cheatsheet content
        cheatsheet_text = tk.Text(
            right_frame,
            height=20,
            width=35,
            font=("Courier New", 9),
            bg="#1a1a1a",
            fg="#cccccc",
            wrap=tk.WORD,
            borderwidth=1,
            relief=tk.SOLID,
            padx=10,
            pady=10,
        )
        cheatsheet_text.pack()

        cheatsheet_content = """# Header 1
## Header 2
### Header 3

**Bold text** (yellow)
*Italic text* (cyan)
`inline code` (red)

```
Code block
multiple lines
```

- Bullet point
- Another point

1. Numbered item
2. Another item

Example:
# Task: Fix Login Bug
- File: `auth.py` line 245
- Issue: **null check** needed
- Test with *admin user*
"""

        cheatsheet_text.insert("1.0", cheatsheet_content)
        cheatsheet_text.config(state=tk.DISABLED)

        # Bind Enter key to submit (Ctrl+Enter for multiline support)
        self.root.bind("<Control-Return>", lambda e: self.create_overlay())

    def parse_and_display_markdown(self, parent_frame, markdown_text):
        """Parse markdown and display with formatting using tkinter Text widget"""

        # Create text widget
        text_widget = tk.Text(
            parent_frame,
            font=("Arial", 18),
            bg="#1a1a1a",
            fg="#00ff00",
            wrap=tk.WORD,
            borderwidth=0,
            highlightthickness=0,
            padx=50,
            pady=20,
            spacing3=10,
        )
        text_widget.pack(fill=tk.BOTH, expand=True, padx=100, pady=40)

        # Configure tags for different markdown elements
        text_widget.tag_configure(
            "h1", font=("Arial", 32, "bold"), foreground="#00ff00", spacing3=15
        )
        text_widget.tag_configure(
            "h2", font=("Arial", 28, "bold"), foreground="#00ff00", spacing3=12
        )
        text_widget.tag_configure(
            "h3", font=("Arial", 24, "bold"), foreground="#00ff00", spacing3=10
        )
        text_widget.tag_configure(
            "bold", font=("Arial", 18, "bold"), foreground="#ffff00"
        )
        text_widget.tag_configure(
            "italic", font=("Arial", 18, "italic"), foreground="#00ffff"
        )
        text_widget.tag_configure(
            "code", font=("Courier New", 16), foreground="#ff6b6b", background="#2a2a2a"
        )
        text_widget.tag_configure(
            "code_block",
            font=("Courier New", 14),
            foreground="#ff6b6b",
            background="#2a2a2a",
            spacing1=10,
            spacing3=10,
        )
        text_widget.tag_configure("bullet", lmargin1=30, lmargin2=50)
        text_widget.tag_configure("normal", font=("Arial", 18))

        lines = markdown_text.split("\n")
        i = 0

        while i < len(lines):
            line = lines[i]

            # Code blocks (```)
            if line.strip().startswith("```"):
                i += 1
                code_content = []
                while i < len(lines) and not lines[i].strip().startswith("```"):
                    code_content.append(lines[i])
                    i += 1
                text_widget.insert(tk.END, "\n".join(code_content) + "\n", "code_block")
                i += 1
                continue

            # Headers
            if line.startswith("# "):
                text_widget.insert(tk.END, line[2:] + "\n", "h1")
            elif line.startswith("## "):
                text_widget.insert(tk.END, line[3:] + "\n", "h2")
            elif line.startswith("### "):
                text_widget.insert(tk.END, line[4:] + "\n", "h3")

            # Bullet points
            elif line.strip().startswith("- ") or line.strip().startswith("* "):
                self.parse_inline_markdown(
                    text_widget, "• " + line.strip()[2:] + "\n", "bullet"
                )

            # Numbered lists
            elif re.match(r"^\d+\.\s", line.strip()):
                self.parse_inline_markdown(text_widget, line.strip() + "\n", "bullet")

            # Regular text with inline formatting
            elif line.strip():
                self.parse_inline_markdown(text_widget, line + "\n", "normal")

            # Empty line
            else:
                text_widget.insert(tk.END, "\n")

            i += 1

        # Make read-only
        text_widget.config(state=tk.DISABLED)

        return text_widget

    def parse_inline_markdown(self, text_widget, line, base_tag):
        """Parse inline markdown formatting (bold, italic, code)"""
        pos = 0

        # Pattern for inline code, bold, and italic
        pattern = r"(`[^`]+`|\*\*[^*]+\*\*|\*[^*]+\*)"

        for match in re.finditer(pattern, line):
            # Insert text before match
            if match.start() > pos:
                text_widget.insert(tk.END, line[pos : match.start()], base_tag)

            matched_text = match.group()

            # Inline code
            if matched_text.startswith("`") and matched_text.endswith("`"):
                text_widget.insert(tk.END, matched_text[1:-1], "code")
            # Bold
            elif matched_text.startswith("**") and matched_text.endswith("**"):
                text_widget.insert(tk.END, matched_text[2:-2], "bold")
            # Italic
            elif matched_text.startswith("*") and matched_text.endswith("*"):
                text_widget.insert(tk.END, matched_text[1:-1], "italic")

            pos = match.end()

        # Insert remaining text
        if pos < len(line):
            text_widget.insert(tk.END, line[pos:], base_tag)

    def create_overlay(self):
        """Create the overlay window with the reminder text"""
        reminder_text = self.text_input.get("1.0", tk.END).strip()

        if not reminder_text:
            return

        # Destroy input window
        self.root.destroy()

        # Create overlay window
        self.overlay = tk.Tk()
        self.overlay.title("Reminder")

        # Make fullscreen and semi-transparent
        self.overlay.attributes("-fullscreen", True)
        self.overlay.attributes("-topmost", True)
        self.overlay.attributes("-alpha", 0.85)  # 85% opaque
        self.overlay.configure(bg="#1a1a1a")

        # Create main frame
        main_frame = tk.Frame(self.overlay, bg="#1a1a1a")
        main_frame.pack(fill=tk.BOTH, expand=True)

        # Parse and display markdown
        self.parse_and_display_markdown(main_frame, reminder_text)

        # Instructions label at bottom
        instruction_label = tk.Label(
            main_frame,
            text="Press ESC or Ctrl+Q to close",
            font=("Arial", 12),
            bg="#1a1a1a",
            fg="#888888",
        )
        instruction_label.pack(side=tk.BOTTOM, pady=20)

        # Bind keyboard shortcuts to close overlay
        self.overlay.bind("<Escape>", lambda e: self.close_overlay())
        self.overlay.bind("<Control-q>", lambda e: self.close_overlay())
        self.overlay.bind("<Control-Q>", lambda e: self.close_overlay())

        self.overlay.mainloop()

    def close_overlay(self):
        """Close the overlay window"""
        self.overlay.destroy()
        sys.exit(0)

    def run(self):
        """Start the application"""
        self.root.mainloop()


if __name__ == "__main__":
    app = ReminderOverlay()
    app.run()
