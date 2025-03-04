# query_enhancer.py

def enhance_query(raw_query: str) -> str:
    """
    Takes the raw user query and returns an enhanced version.
    Currently does minimal improvements. Extend as needed.
    """
    # For demonstration, let's just add some prompt context
    # and fix trivial issues. You could integrate external libraries here.
    if not raw_query.strip():
        return raw_query

    # Example improvement technique: ensure query is a full sentence
    # If user typed "And food?", we might expand it:
    # "Can you tell me more about the local food options?"
    # We'll do something simple for now:
    enhanced = raw_query.strip()

    # Basic grammar fix / clarifying phrase:
    if enhanced.lower().startswith("and "):
        enhanced = "Can you give more details about " + enhanced[4:].strip() + "?"
    elif not enhanced.endswith("?"):
        enhanced += "?"

    # You can add more logic like:
    # 1. Grammar checks with LanguageTool
    # 2. Context injection (e.g., "User is planning a trip to Japan, user wants info:")
    # 3. Breaking up run-on sentences, etc.

    return enhanced
