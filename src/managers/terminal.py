from PySide6.QtCore import QTime, QTimer


class TerminalModel:
    def __init__(self, terminal_widget) -> None:
        self.terminal_widget = terminal_widget

        self.autoscroll_enabled = True
        self.max_lines = 200
        terminal_clear_interval = 30000

        self.terminal_clearer = QTimer()
        self.terminal_clearer.setInterval(terminal_clear_interval)
        self.terminal_clearer.timeout.connect(self._check_line_amount)

        # self.root.ui.autoScrollButton.setChecked(self.autoscroll_enabled)

    def write(self, data: str, custom_prefix: str = "") -> None:
        time_stamp = QTime.currentTime().toString("hh:mm:ss.zzz")

        message_prefix = (
            f"[{time_stamp}]:"
            if custom_prefix == ""
            else f"[{time_stamp} {custom_prefix}]:"
        )
        message = f"<b>{message_prefix}</b> {data}"
        self.terminal_widget.append(message)

        # Autoscroll to the latest message
        if self.autoscroll_enabled:
            scrollbar = self.terminal_widget.verticalScrollBar()
            scrollbar.setValue(scrollbar.maximum())

    def toggle_autoscroll(self) -> None:
        self.autoscroll_enabled = not self.autoscroll_enabled

    def clear(self) -> None:
        self.terminal_widget.clear()

    def _check_line_amount(self) -> None:
        if self.terminal_widget.document().blockCount() > self.max_lines:
            self.clear()
