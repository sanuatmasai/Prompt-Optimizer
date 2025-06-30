# This module provides explanations for how and why a prompt was optimized for a specific tool.
def generate_explanation(original, optimized, tool_name):
    explanation = []

    print(f"[LOG] Generating explanation for tool: {tool_name}")
    # If the optimized prompt is different from the original, explain what was changed
    if original != optimized:
        # If a language hint was added, explain why
        if "Python" in optimized and "Python" not in original:
            explanation.append("Added language hint for better understanding by " + tool_name)
        # If input/output examples were added, explain why
        if "input/output" in optimized:
            explanation.append("Prompt was vague; added request for input/output examples")
        # If file structure was added, explain why
        if "file structure" in optimized:
            explanation.append("Replit performs better with explicit file layout; added that.")
    else:
        # If nothing was changed, state that the prompt was already optimal
        explanation.append("Prompt was already optimal.")

    print(f"[LOG] Explanation list: {explanation}")
    return "\n".join(explanation)