print("Sarthak Gaur (2581247)")
def filter_notes_by_tag(notes_list, search_tag):
"""Filters campus notes list by specific course tag."""
filtered = [note for note in notes_list if note.get('tag') == search_tag]
print(f"Found {len(filtered)} notes matching tag: {search_tag}")
return filtered
if __name__ == "__main__":
  sample_notes = [{"title": "Git Hooks Guide", "tag": "VCS"}, {"title": "Java OOP Basics", "tag": "OOPS"}]
filter_notes_by_tag(sample_notes, "VCS")
