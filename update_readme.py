import re
from datetime import datetime, timezone, timedelta

def generate_new_content():
    # Calculate Indian Standard Time (IST) for the timestamp
    ist_offset = timezone(timedelta(hours=5, minutes=30))
    current_time = datetime.now(ist_offset).strftime("%Y-%m-%d %I:%M %p IST")
    
    # You can customize this text or add API calls here in the future
    # to fetch real data, like recent LeetCode submissions or repo commits.
    content = (
        f"⏳ *Last updated automatically on: **{current_time}***\n\n"
        f"- 🔭 **Currently focusing on:** Decentralized for Public Model\n"
        f"- 💻 **Recently practicing:** Python & SQL Data Manipulation\n"
    )
    return content

def update_readme():
    # Read the current README
    with open("README.md", "r", encoding="utf-8") as file:
        readme_content = file.read()

    new_content = generate_new_content()

    # Regex to replace content exactly between the markers
    pattern = r"(<!-- START_SECTION:activity -->\n).*?(<!-- END_SECTION:activity -->)"
    updated_readme = re.sub(pattern, rf"\1{new_content}\n\2", readme_content, flags=re.DOTALL)

    # Write the changes back to the file
    with open("README.md", "w", encoding="utf-8") as file:
        file.write(updated_readme)

if __name__ == "__main__":
    update_readme()
