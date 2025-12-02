# Read and fix the app.py with unterminated f-string on line 36
app_path = "/mnt/data/app.py"
fixed_app_path = "/mnt/data/app_fixed.py"

with open(app_path, "r") as file:
    lines = file.readlines()

# Patch the line containing the unterminated f-string
fixed_lines = []
for line in lines:
    if "st.markdown(f\"**{row['Title']}**" in line:
        fixed_line = (
            "        st.markdown(f\"\"\"\n"
            "        **{row['Title']}** ({row['Source']}, {row['Publication Date']})  \n"
            "        [Read Article]({row['URL']})\n"
            "        \"\"\")\n"
        )
        fixed_lines.append(fixed_line)
    else:
        fixed_lines.append(line)

# Save corrected app.py
with open(fixed_app_path, "w") as file:
    file.writelines(fixed_lines)

fixed_app_path
