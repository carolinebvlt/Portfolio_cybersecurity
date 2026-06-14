import os
def generate_report(report_lines) :
    # store it in the same dir than this file
    base_dir = os.path.dirname(os.path.abspath(__file__))
    path = os.path.join(base_dir, "file_integrity_monitor_report.txt")

    report_lines.insert(0, "### File integrity Report ###\n")

    with open(path, "w") as file:
        file.write("\n".join(report_lines))