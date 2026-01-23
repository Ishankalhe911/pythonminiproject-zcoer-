Projects = {
    "Mobile App": [
        {"id": "BUG-01", "title": "Login crash", "status": "Open"},
        {"id": "BUG-02", "title": "Slow loading", "status": "Resolved"}
    ],
    "Website": [
        {"id": "WEB-01", "title": "Header overlapping", "status": "Open"}
    ]
}

def add_error():
    choice = input("Enter (M) for Mobile, (W) for Website: ")
    # Map input to the dictionary key
    target_key = "Mobile App" if choice == "M" else "Website"

    if target_key in Projects:
        new_id = input("Enter id: ")
        new_title = input("Enter title: ")
        new_status = input("Enter status: ")

        new_entry = {"id": new_id, "title": new_title, "status": new_status}
        
        # DRILL DOWN: Access the list inside the dict, then append
        Projects[target_key].append(new_entry)
        print("Bug added!")
    else:
        print("Invalid project!")

def display_all():
    for project, bug_list in Projects.items():
        print(f"\nProject: {project}")
        for index, bug in enumerate(bug_list):
            # Using the 'Drill Down' we discussed for a clean look
            print(f"  {index}. ID: {bug['id']} | Title: {bug['title']} [{bug['status']}]")

def delete_bug():
    choice = input("Enter (M) for Mobile, (W) for Website: ")
    target_key = "Mobile App" if choice == "M" else "Website"
    target_id = input("Enter the ID to delete: ")

    if target_key in Projects:
        # Get the list pointer
        current_list = Projects[target_key]
        found = False
        
        for index, bug in enumerate(current_list):
            if bug["id"] == target_id:
                # POP from the list, not the bug dictionary
                current_list.pop(index)
                print(f"Bug {target_id} deleted successfully.")
                found = True
                break 
        
        if not found:
            print("ID not found.")
        
        display_all() # Re-use your display function!
    else:
        print("Project not found.")

# Testing the code
delete_bug()