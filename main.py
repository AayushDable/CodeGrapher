import sys
import traceback
from PyQt5.QtWidgets import QApplication, QMessageBox
from ui.main_window import CodeGraphWindow


def trace_calls(frame, event, arg):
    """Trace function calls for debugging"""
    if event != 'call':
        return
    
    code = frame.f_code
    filename = code.co_filename
    
    # Only trace our project files, not Qt/Python internals
    if 'codeflow_visualizer' in filename or 'main_window' in filename:
        func_name = code.co_name
        line_num = frame.f_lineno
        
        # Only show relevant validation functions
        relevant = ['validate', 'check_function', 'check_class', 'search_function', 
                   'get_current_search', 'exists']
        
        if any(keyword in func_name.lower() for keyword in relevant):
            print(f"→ {func_name}() at line {line_num}")
    
    return trace_calls


def exception_hook(exctype, value, tb):
    """Global exception handler for debugging"""
    error_msg = ''.join(traceback.format_exception(exctype, value, tb))
    print("=" * 80)
    print("UNHANDLED EXCEPTION:")
    print("=" * 80)
    print(error_msg)
    print("=" * 80)
    
    QMessageBox.critical(
        None,
        "CodeGraph Error",
        f"An error occurred:\n\n{exctype.__name__}: {value}\n\nSee console for full traceback."
    )


def main():
    DEBUG = False
    TRACE_CALLS = False  # Enable call tracing
    
    if DEBUG:
        sys.excepthook = exception_hook
        print("=" * 80)
        print("CodeGraph - DEBUG MODE")
        print("=" * 80)
    
    if TRACE_CALLS:
        print("\n🔍 CALL TRACING ENABLED - Click 'Validate Blocks' to see function calls\n")
        sys.settrace(trace_calls)
    
    app = QApplication(sys.argv)
    app.setApplicationName('CodeGraph')
    app.setOrganizationName('CodeGraph')
    
    try:
        window = CodeGraphWindow()
        window.show()
        
        if DEBUG:
            print("✓ Main window loaded")
            print("=" * 80)
        
        sys.exit(app.exec_())
    
    except Exception as e:
        print("=" * 80)
        print("STARTUP ERROR:")
        print("=" * 80)
        traceback.print_exc()
        print("=" * 80)
        sys.exit(1)


if __name__ == '__main__':
    main()
